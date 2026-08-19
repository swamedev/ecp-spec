# -*- coding: utf-8 -*-
"""
MR-C7 phase4 — labelers.py (consenso algorítmico determinístico, S-A/S-B/S-C).

Substitui o consenso de IA (§4.3 do protocolo) pelo consenso algorítmico de três
sinais independentes, conforme C-MODEL-SUBSTITUTION-ADDENDUM.md §4. Regra ≥2/3 em
ambas as dimensões (correção e relevância), correção ancorada ao gerador.

Sinais (determinísticos, entradas disjuntas da métrica):
  S-A — relevância temática: sobreposição de tokens com o núcleo do caso
        (entidades centrais + fatos-base). overlap > 0 -> "relevante", senão "irrelevante".
  S-B — redundância lexical/entailment: cobertura dos tokens do candidato pelos
        fatos-base. cobertura >= 0.5 -> "redundante", senão "relevante".
  S-C — novidade estrutural vs G0: categorias/relações desenhadas do candidato
        (metadado do gerador) vs G0. novelty_score >= 0.5 -> "relevante";
        0 < score < 0.5 -> "irrelevante"; score == 0 -> "redundante".

NÃO importa reconstruction.py, metric.py nem generate_cases.py (standalone).
NÃO usa embedding, WL kernel, F1, entropia, grafo de reconstrução nem referência.
"""
import os
import re

import numpy as np
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS = os.path.join(HERE, "..", "inputs")

SEED_DRAW = 20260819
SEED_MASTER = 20260819
N_CASES = 24

TAU_SA = 0          # overlap > TAU_SA -> relevante
TAU_SB = 0.5        # cobertura >= TAU_SB -> redundante
TAU_SC = 0.5        # novelty_score >= TAU_SC -> relevante

# Nós e arestas de G0 por caso (fornecidos pelo gerador em cases.yaml).


def _tokens(text):
    """Tokenização local (standalone) — mesma semântica do engine, símbolo próprio."""
    stop = {
        "o", "a", "os", "as", "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas",
        "para", "por", "com", "sem", "que", "era", "ser", "for", "foi", "sao", "mais", "menos",
        "um", "uma", "uns", "umas", "como", "mas", "ou", "se", "ja", "tambem", "e", "nao",
        "entre", "sobre", "ate", "apos", "depois", "antes", "durante", "contra",
    }
    return {
        t for t in re.findall(r"[A-Za-zÀ-ÿ0-9]+", text.lower())
        if len(t) >= 4 and t not in stop
    }


def derive_seeds(n_cases):
    """Procedimento do generate_seeds.py congelado com seed_master 20260819 (para registro)."""
    out = {}
    for ci in range(n_cases):
        ss = np.random.SeedSequence(SEED_MASTER, spawn_key=(ci, 0))
        rng = np.random.Generator(np.random.PCG64(ss))
        out[ci] = [int.from_bytes(rng.bytes(8), "little") for _ in range(3)]
    return out


def signal_votes(candidate, core_tokens, base_tokens, g0_nodes, g0_edges, last_base_cat):
    text = candidate["text"]
    cat = candidate["intended_category"]
    is_true = candidate["is_true"]
    cand_tokens = _tokens(text)

    # S-A — relevância temática.
    overlap_a = len(cand_tokens & core_tokens)
    s_a_dec = "relevante" if overlap_a > TAU_SA else "irrelevante"

    # S-B — redundância lexical/entailment.
    coverage = (len(cand_tokens & base_tokens) / len(cand_tokens)) if cand_tokens else 0.0
    s_b_dec = "redundante" if coverage >= TAU_SB else "relevante"

    # S-C — novidade estrutural vs G0 (metadados do gerador + G0 apenas).
    designed_rels = []
    if candidate["pool"] in ("V1", "V3"):
        # Relação desenhada: arco follows que prende o fato novo à cadeia do caso.
        designed_rels = [(last_base_cat, cat)]
    novo_no = 0 if cat in g0_nodes else 1
    nova_aresta = sum(1 for r in designed_rels if r not in g0_edges)
    denom = 1 + len(designed_rels)
    novelty = (novo_no + nova_aresta) / denom if denom else 0.0
    if novelty >= TAU_SC:
        s_c_dec = "relevante"
    elif novelty > 0:
        s_c_dec = "irrelevante"
    else:
        s_c_dec = "redundante"

    corr = "verdadeiro" if is_true else "falso"

    return {
        "S-A": {"resposta_bruta": {"overlap": overlap_a}, "decisao": s_a_dec},
        "S-B": {"resposta_bruta": {"cobertura": round(coverage, 6)}, "decisao": s_b_dec},
        "S-C": {"resposta_bruta": {"novelty_score": round(novelty, 6),
                                   "novo_no": novo_no, "nova_aresta": nova_aresta},
                "decisao": s_c_dec},
        "correcao": corr,
        "text_tokens": sorted(cand_tokens),
    }


def consensus(votes):
    # Correção: ancorada ao gerador — todos os sinais reportam a mesma verdade factual.
    correcao = votes["correcao"]
    rel_votes = [votes[s]["decisao"] for s in ("S-A", "S-B", "S-C")]
    from collections import Counter
    rel_count = Counter(rel_votes)
    best, best_n = rel_count.most_common(1)[0]
    if best_n >= 2:
        return correcao, best
    return None, None  # sem consenso de relevância


def main():
    with open(os.path.join(INPUTS, "cases.yaml"), encoding="utf-8") as f:
        cases = yaml.safe_load(f)["cases"]

    rng = np.random.default_rng(SEED_DRAW)
    seeds = derive_seeds(N_CASES)

    registry = []
    states = {"seed_draw": SEED_DRAW, "seed_master": SEED_MASTER, "cases": {}}
    excluded = []

    for ci, case_id in enumerate(sorted(cases.keys())):
        c = cases[case_id]
        base_facts = c["base_facts"]
        base_cats = c["base_cats"]
        new_cats = c["new_cats"]
        last_base_cat = base_cats[-1]
        core_tokens = set(c["topic_tokens"])
        for bf in base_facts:
            core_tokens |= _tokens(bf)
        base_tokens = set().union(*(_tokens(bf) for bf in base_facts))

        g0_nodes = set(n["id"] for n in c["g0"]["nodes"])
        g0_edges = set((e["source"], e["target"]) for e in c["g0"]["edges"])

        case_states = {}
        pools_drawn = {}
        for pool_name in ("V1", "V2", "V3"):
            pool = c["pools"][pool_name]
            labeled = []
            for cand in pool:
                votes = signal_votes(cand, core_tokens, base_tokens, g0_nodes, g0_edges,
                                     last_base_cat)
                corr, rel = consensus(votes)
                labeled.append({
                    "candidate": cand,
                    "votes": votes,
                    "label_correcao": corr,
                    "label_relevancia": rel,
                })
                registry.append({
                    "caso": case_id,
                    "candidate_id": cand["candidate_id"],
                    "pool": cand["pool"],
                    "texto": cand["text"],
                    "correcao_generador": "verdadeiro" if cand["is_true"] else "falso",
                    "consenso": {"correcao": corr, "relevancia": rel},
                    "sinais": {
                        s: {
                            "modelo_exato": s,
                            "versao_model_id": "SINAL-ALGORITMICO-v1",
                            "data": "2026-08-18T00:00:00Z",
                            "prompt_completo": "algoritmo determinístico %s" % s,
                            "resposta_bruta": votes[s]["resposta_bruta"],
                            "decisao": votes[s]["decisao"],
                            "justificativa": "regra congelada em labelers.py",
                        } for s in ("S-A", "S-B", "S-C")
                    },
                })

            consensual = [l for l in labeled if l["label_correcao"] is not None]
            pools_drawn[pool_name] = consensual

        # Exclusão (§4.4): pool consensual < 3 -> caso excluído.
        if any(len(pools_drawn[p]) < 3 for p in ("V1", "V2", "V3")):
            excluded.append(case_id)
            states["cases"][case_id] = {
                "excluded": True,
                "reason": "pool consensual < 3",
                "pool_sizes": {p: len(pools_drawn[p]) for p in ("V1", "V2", "V3")},
            }
            continue

        # Sorteio determinístico (seed_draw = 20260819).
        # V1 e V3: estratificado por categoria nova (1 por categoria em new_cats),
        # garantindo |ΔV1|=|ΔV3|=3 com 3 categorias novas distintas (§4.4, §6.2).
        # V2: 3 de 6 candidatos.
        drawn_v1 = []
        drawn_v3 = []
        for cat in new_cats:
            cands_v1 = [l for l in pools_drawn["V1"] if l["candidate"]["intended_category"] == cat]
            cands_v3 = [l for l in pools_drawn["V3"] if l["candidate"]["intended_category"] == cat]
            drawn_v1.append(cands_v1[int(rng.integers(0, len(cands_v1)))])
            drawn_v3.append(cands_v3[int(rng.integers(0, len(cands_v3)))])
        drawn_v2 = list(rng.choice(pools_drawn["V2"], size=3, replace=False))

        facts_v1 = [l["candidate"]["text"] for l in drawn_v1]
        facts_v2 = [l["candidate"]["text"] for l in drawn_v2]
        facts_v3 = [l["candidate"]["text"] for l in drawn_v3]

        case_states = {
            "V0": {"facts": [], "drawn_ids": []},
            "V1": {"facts": facts_v1,
                   "drawn_ids": [l["candidate"]["candidate_id"] for l in drawn_v1],
                   "categories": [l["candidate"]["intended_category"] for l in drawn_v1]},
            "V2": {"facts": facts_v2,
                   "drawn_ids": [l["candidate"]["candidate_id"] for l in drawn_v2]},
            "V3": {"facts": facts_v3,
                   "drawn_ids": [l["candidate"]["candidate_id"] for l in drawn_v3]},
        }

        states["cases"][case_id] = {
            "excluded": False,
            "base_facts": base_facts,
            "states": case_states,
            "seeds": seeds[ci],
        }

    os.makedirs(INPUTS, exist_ok=True)
    with open(os.path.join(INPUTS, "states.yaml"), "w", encoding="utf-8") as f:
        yaml.safe_dump(states, f, allow_unicode=True, sort_keys=False)
    with open(os.path.join(INPUTS, "consensus_registry.yaml"), "w", encoding="utf-8") as f:
        yaml.safe_dump({"seed_draw": SEED_DRAW, "registro": registry},
                       f, allow_unicode=True, sort_keys=False)

    print("Casos: %d, excluídos: %d" % (N_CASES, len(excluded)))
    if excluded:
        print("  excluídos:", excluded)
    print("Candidatos rotulados:", len(registry))
    print("saved: inputs/states.yaml, inputs/consensus_registry.yaml")


if __name__ == "__main__":
    main()
