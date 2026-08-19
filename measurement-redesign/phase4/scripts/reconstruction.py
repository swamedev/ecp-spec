# -*- coding: utf-8 -*-
"""
MR-C7 phase4 — reconstruction.py (pipeline espelho do engine congelado, namespace MRCAT).

Espelho de GO-8D-NC/scripts/{pilot_engine.py, graph_from_reconstruction.py} para o
namespace procedural neutro MRCAT-01..12 (protocolo MR-C7 §3, §7.5). Determinístico,
usa SOMENTE embedding por hash-fallback (numpy puro, sem rede, sem SentenceTransformer)
conforme C-MODEL-SUBSTITUTION-ADDENDUM.md §5.1.

NÃO importa labelers.py nem metric.py. NÃO lê texto de candidatos fora daquilo que
constrói as reconstruções (os fatos de entrada de cada estado).
"""
import os
import re
import json
import hashlib

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS = os.path.join(HERE, "..", "inputs")
OUTPUTS = os.path.join(HERE, "..", "outputs")

# ---------------------------------------------------------------------------
# Cópia EXATA do tokenizador do engine congelado (pilot_engine.py).
# ---------------------------------------------------------------------------
PT_STOP = {
    "o", "a", "os", "as", "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas",
    "para", "por", "com", "sem", "que", "era", "ser", "for", "foi", "sao", "mais", "menos",
    "um", "uma", "uns", "umas", "como", "mas", "ou", "se", "ja", "tambem", "e", "nao",
    "entre", "sobre", "ate", "apos", "depois", "antes", "durante", "contra",
}


def fact_tokens(text):
    """Tokens de conteúdo (cópia exata do engine congelado)."""
    return {
        t for t in re.findall(r"[A-Za-zÀ-ÿ0-9]+", text.lower())
        if len(t) >= 4 and t not in PT_STOP
    }


def _norm(v):
    if v is None:
        return np.zeros(384)
    v = np.asarray(v, dtype=float).flatten()
    return v / np.linalg.norm(v) if np.linalg.norm(v) > 0 else v


def text_emb(text):
    """Embedding determinístico por hash-fallback (cópia exata do engine congelado)."""
    t = (text or "").strip()
    if not t:
        return np.zeros(384)
    vec = np.zeros(384, dtype=float)
    for tok in fact_tokens(t):
        h = hashlib.sha256(("tok|" + tok).encode()).digest()
        vec += (np.frombuffer(h * 24, dtype=np.uint8).astype(float)[:384] * 3.0 + 8.0)
    return _norm(vec)


# ---------------------------------------------------------------------------
# Definições procedurais neutras MRCAT-01..12 (namespace do gate).
# ---------------------------------------------------------------------------
MRCAT_DEFS = {
    "MRCAT-01": "registro das ocorrencias com catalogacao e arquivamento",
    "MRCAT-02": "protocolo com roteiro e sequencia padronizada de passos",
    "MRCAT-03": "medida com quantificacao de grandezas por mensuracao",
    "MRCAT-04": "unidade organizacional com responsabilidades e competencias definidas",
    "MRCAT-05": "insumo com estoque e fornecimento de suprimentos",
    "MRCAT-06": "dado com informacao bruta coletada do ambiente",
    "MRCAT-07": "processo com fluxo de tarefas e rotina de operacao",
    "MRCAT-08": "produto entregavel e resultado gerado ao final",
    "MRCAT-09": "padrao com requisito e referencia de conformidade",
    "MRCAT-10": "prazo com cronograma e vencimento previsto",
    "MRCAT-11": "risco com contingencia e ameaca identificada",
    "MRCAT-12": "qualidade com avaliacao de aceitacao e aptidao",
}

BASE_CATS = ["MRCAT-%02d" % i for i in range(1, 10)]      # MRCAT-01..09
NEW_CATS = ["MRCAT-%02d" % i for i in range(10, 13)]      # MRCAT-10..12
ALL_CATS = BASE_CATS + NEW_CATS


class Classifier:
    """Classificador por cosseno do embedding hash-fallback (cópia exata)."""

    def __init__(self, definitions, slots):
        self.slots = slots
        self.def_emb = {s: text_emb(definitions[s]) for s in slots}

    def classify(self, text):
        emb = text_emb(text)
        best, best_sim = None, -1.0
        for s, d in self.def_emb.items():
            sim = float(np.dot(emb, d))
            if sim > best_sim:
                best, best_sim = s, sim
        conf = min(1.0, max(0.1, round((best_sim + 1) / 2.0, 4)))
        return best, conf


def make_classifier():
    return Classifier(MRCAT_DEFS, list(MRCAT_DEFS.keys()))


# ---------------------------------------------------------------------------
# Construção de entidades/relações (cópia exata do engine congelado).
# ---------------------------------------------------------------------------
def build_entities_relations(units):
    """units: lista de dicts {text, af_id}. Relações follows/relates idênticas ao engine."""
    clf = make_classifier()
    entities = []
    relations = []
    tokensets = []
    n = len(units)
    for i, u in enumerate(units, start=1):
        eid = "ENT-%04d" % i
        rid = "REL-%04d" % i
        cat, conf = clf.classify(u["text"])
        entities.append({
            "entity_id": eid,
            "syn_category": cat,
            "confidence": conf,
            "source_af_ids": [u["af_id"]],
        })
        ts = fact_tokens(u["text"])
        tokensets.append(ts)
        if i < n:
            relations.append({
                "relation_id": rid,
                "source": eid,
                "target": "ENT-%04d" % (i + 1),
                "relation_type": "follows",
                "confidence": 0.8,
                "evidence_af_ids": [u["af_id"]],
            })
    rel_counter = 0
    for i in range(n):
        for j in range(i + 2, n):
            overlap = tokensets[i] & tokensets[j]
            if len(overlap) >= 2:
                rel_counter += 1
                relations.append({
                    "relation_id": "REL-%04d" % (9000 + rel_counter),
                    "source": "ENT-%04d" % (i + 1),
                    "target": "ENT-%04d" % (j + 1),
                    "relation_type": "relates",
                    "confidence": 0.7,
                    "evidence_af_ids": [units[i]["af_id"], units[j]["af_id"]],
                })
    return entities, relations


# ---------------------------------------------------------------------------
# Colapso por categoria — espelho de GraphFromReconstruction.parse para MRCAT.
# ---------------------------------------------------------------------------
def graph_from_reconstruction_mrcat(entities, relations):
    """Colapso de entidades/relações em grafo (nós = categorias MRCAT; arestas = relações)."""
    for e in entities:
        if not re.match(r"^MRCAT-\d{2}$", e["syn_category"]):
            raise ValueError("NAMESPACE_MIX")

    node_map = {}
    for e in entities:
        cat = e["syn_category"]
        if cat not in node_map:
            node_map[cat] = {"syn_category": cat, "_conf_sum": 0.0, "_conf_n": 0}
        node_map[cat]["_conf_sum"] += e["confidence"]
        node_map[cat]["_conf_n"] += 1

    ent_to_cat = {e["entity_id"]: e["syn_category"] for e in entities}
    edge_map = {}
    for r in relations:
        s_cat = ent_to_cat.get(r["source"])
        t_cat = ent_to_cat.get(r["target"])
        if s_cat is None or t_cat is None:
            continue
        key = (s_cat, t_cat, r["relation_type"])
        if key not in edge_map:
            edge_map[key] = {"source": s_cat, "target": t_cat,
                             "relation_type": r["relation_type"],
                             "_conf_sum": 0.0, "_conf_n": 0}
        edge_map[key]["_conf_sum"] += r["confidence"]
        edge_map[key]["_conf_n"] += 1

    nodes = []
    for cat, nd in sorted(node_map.items()):
        nodes.append({
            "node_id": cat,
            "syn_category": cat,
            "confidence": round(nd["_conf_sum"] / nd["_conf_n"], 6),
        })

    edges = []
    for (s, t, rt), ed in sorted(edge_map.items()):
        edges.append({
            "edge_id": "E-%04d" % (len(edges) + 1),
            "source": s,
            "target": t,
            "relation_type": rt,
            "confidence": round(ed["_conf_sum"] / ed["_conf_n"], 6),
        })

    return {"nodes": nodes, "edges": edges}


def graph_view(graph):
    """Visão id-only para o WL kernel (s_struct usa apenas nós/arestas)."""
    return {
        "nodes": [{"id": n["node_id"]} for n in graph["nodes"]],
        "edges": [{"source": e["source"], "target": e["target"]} for e in graph["edges"]],
    }


def _counts(categories):
    out = {}
    for c in categories:
        out[c] = out.get(c, 0) + 1
    return out


def reconstruct_facts(facts):
    """facts: lista de strings (fatos de entrada do estado). Retorna grafo colapsado."""
    units = [{"text": f, "af_id": "AF-%03d" % (i + 1)} for i, f in enumerate(facts)]
    entities, relations = build_entities_relations(units)
    return graph_from_reconstruction_mrcat(entities, relations), \
        [e["syn_category"] for e in entities]


# ---------------------------------------------------------------------------
# Seeds (§7.5) — procedimento do generate_seeds.py congelado com seed_master 20260818.
# ---------------------------------------------------------------------------
SEED_MASTER = 20260818


def derive_seeds(n_cases):
    """PCG64(SeedSequence(20260818, spawn_key=(ci, 0))) -> 3 uint64 por caso."""
    out = {}
    for ci in range(n_cases):
        ss = np.random.SeedSequence(SEED_MASTER, spawn_key=(ci, 0))
        rng = np.random.Generator(np.random.PCG64(ss))
        out[ci] = [int.from_bytes(rng.bytes(8), "little") for _ in range(3)]
    return out


# ---------------------------------------------------------------------------
# Execução principal.
# ---------------------------------------------------------------------------
def main():
    import yaml
    with open(os.path.join(INPUTS, "states.yaml"), encoding="utf-8") as f:
        states = yaml.safe_load(f)

    cases = states["cases"]
    n_cases = len(cases)
    case_ids = sorted(cases.keys())
    seeds = derive_seeds(n_cases)
    seed_map = {case_id: seeds[i] for i, case_id in enumerate(case_ids)}

    results = {}
    invariance = {}
    truth_graphs = {}

    for case_id in case_ids:
        c = cases[case_id]
        base_facts = c["base_facts"]
        g0, g0_cats = reconstruct_facts(base_facts)
        truth_graphs[case_id] = {"G0": g0, "G0_cat_counts": _counts(g0_cats)}

        state_facts = {
            "V0": list(base_facts),
            "V1": base_facts + c["states"]["V1"]["facts"],
            "V2": base_facts + c["states"]["V2"]["facts"],
            "V3": base_facts + c["states"]["V3"]["facts"],
        }

        # Verdade por estado (§7.4): V1 = G0 estendido pelos fatos verdadeiros de ΔV1;
        # V2 e V3 = G0 (entailados / falsos não pertencem à verdade).
        truth_v1, _cats = reconstruct_facts(state_facts["V1"])
        truth_graphs[case_id]["V1"] = truth_v1
        truth_graphs[case_id]["V2"] = truth_graphs[case_id]["G0"]
        truth_graphs[case_id]["V3"] = truth_graphs[case_id]["G0"]

        row = {}
        inv = {}
        for state in ("V0", "V1", "V2", "V3"):
            full, cats = reconstruct_facts(state_facts[state])
            identical = all(reconstruct_facts(state_facts[state])[0] == full
                            for _ in range(2))
            inv[state] = identical
            row[state] = {
                "graph": full,
                "cat_counts": _counts(cats),
                "seed_values": seed_map[case_id],
                "nodes": len(full["nodes"]),
                "edges": len(full["edges"]),
                "categories": sorted(n["syn_category"] for n in full["nodes"]),
            }
        results[case_id] = row
        invariance[case_id] = inv

    os.makedirs(OUTPUTS, exist_ok=True)
    out_path = os.path.join(OUTPUTS, "reconstruction_graphs.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({
            "seed_master": SEED_MASTER,
            "results": results,
            "truth_graphs": truth_graphs,
            "seed_invariance": invariance,
        }, f, indent=2, ensure_ascii=False)

    all_inv = all(all(v for v in inv.values()) for inv in invariance.values())
    print("Reconstruções: %d casos × 4 estados" % n_cases)
    print("Invariância a seed (idêntico nos 3 seeds): %s" % ("OK" if all_inv else "FALHOU"))
    print("saved:", out_path)


if __name__ == "__main__":
    main()
