# -*- coding: utf-8 -*-
"""
MR-C7 phase4 — generate_cases.py (gerador procedural determinístico, §3–§4).

Gera N=24 casos-base sintéticos (seed_casegen = 20260818) com:
  - universo MRCAT-01..12; por caso, um subconjunto base de 9 categorias (G0) sorteado
    deterministicamente; as 3 categorias complementares são as categorias novas de V1/V3;
  - 9 fatos-base verdadeiros (1 por categoria base), classificáveis com confiança pelo
    pipeline espelho (verificação na geração);
  - G0 = grafo de verdade do caso (cadeia follows sobre as categorias-base + relates
    decorrentes da sobreposição de tokens entre fatos-base);
  - núcleo temático (entidades centrais) para o sinal S-A;
  - pool de 18 candidatos/caso: 6 pares estruturais (V1, V3) casados (mesma pegada:
    mesma categoria nova, mesmas relações, mesma aridade — o texto de V3 é a negação
    com tokens idênticos após remoção de "nao"/"sem", portanto mesma pegada) + 6
    candidatos V2 (verdadeiros, entailados, redundantes);
  - pegada estrutural dos pares (V1,V3) por construção (§4.2, §6.2/§6.3).

O gerador usa o classificador do pipeline espelho (reconstruction.py) APENAS para
verificar que cada fato/candidato classifica na categoria intencional. Não usa
nenhuma métrica nem nenhum sinal de rotulação.
"""
import os
import re

import numpy as np
import yaml

from reconstruction import (
    MRCAT_DEFS, ALL_CATS, fact_tokens, make_classifier, reconstruct_facts, graph_view,
)

HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS = os.path.join(HERE, "..", "inputs")

SEED_CASEGEN = 20260818
N_CASES = 24

# Tokens temáticos procedurais neutros (fora do vocabulário das definições MRCAT).
TOPIC_POOL = [
    "transporte", "entrega", "lote", "carga", "armazem", "frota", "rota",
    "terminal", "expedicao", "despacho", "coleta", "trajeto", "origem",
    "destino", "veiculo", "motorista", "pacote", "pedido", "contrato",
    "fornecedor", "cliente", "equipe", "turno", "escala", "aprovacao",
    "conferencia", "movimentacao", "custeio", "relatorio", "vistoria",
]

_RESERVED = set().union(*(fact_tokens(d) for d in MRCAT_DEFS.values()))
TOPIC_POOL = [t for t in TOPIC_POOL if t not in _RESERVED]

# Cláusula por categoria para os fatos-base (palavras-chave da definição).
DEF_CLAUSE = {
    "MRCAT-01": "registra as ocorrencias com catalogacao e arquivamento",
    "MRCAT-02": "segue o protocolo com roteiro e sequencia padronizada",
    "MRCAT-03": "mede as grandezas com quantificacao e mensuracao",
    "MRCAT-04": "organiza as responsabilidades e competencias da unidade",
    "MRCAT-05": "controla o estoque e o fornecimento de suprimentos",
    "MRCAT-06": "coleta dado e informacao bruta do ambiente",
    "MRCAT-07": "executa o fluxo de tarefas e a rotina de operacao",
    "MRCAT-08": "gera o produto entregavel como resultado final",
    "MRCAT-09": "aplica o padrao com requisito e referencia de conformidade",
    "MRCAT-10": "estabelece o prazo com cronograma e vencimento previsto",
    "MRCAT-11": "aponta o risco com contingencia e ameaca identificada",
    "MRCAT-12": "verifica a qualidade com avaliacao de aceitacao e aptidao",
}

# Núcleo de adição correta/relevante (V1) por categoria.
NEW_NUCLEUS = {
    "MRCAT-01": "amplia o registro das ocorrencias com catalogacao e arquivamento",
    "MRCAT-02": "adota o protocolo com roteiro e sequencia padronizada",
    "MRCAT-03": "confirma a medida com quantificacao e mensuracao das grandezas",
    "MRCAT-04": "reforca as responsabilidades e competencias da unidade",
    "MRCAT-05": "reposiciona o estoque e o fornecimento de suprimentos",
    "MRCAT-06": "complementa o dado e a informacao bruta coletada",
    "MRCAT-07": "organiza o fluxo de tarefas e a rotina de operacao",
    "MRCAT-08": "entrega o produto entregavel como resultado final",
    "MRCAT-09": "atualiza o padrao com requisito e referencia de conformidade",
    "MRCAT-10": "conclui dentro do prazo com cronograma e vencimento previsto",
    "MRCAT-11": "enfrenta risco de contingencia com ameaca identificada",
    "MRCAT-12": "confere qualidade com avaliacao de aceitacao e aptidao",
}

FALSE_PREFIXES = ["nao ", "sem "]


def make_base_fact(topic_token, cat, filler):
    return "O %s %s de %s." % (topic_token, DEF_CLAUSE[cat], filler)


def make_new_fact(topic_token, cat, variant, negate):
    nucleus = NEW_NUCLEUS[cat]
    if variant == 1:
        nucleus += " de forma uniforme"
    if negate:
        body = FALSE_PREFIXES[0] + nucleus
    else:
        body = nucleus
    return "O %s %s." % (topic_token, body)


def verify_classification(text, clf, intended):
    cat, _conf = clf.classify(text)
    if cat == intended:
        return text, True
    clauses = re.split(r"[,.!;]", text)
    clauses = [c.strip() for c in clauses if c.strip()]
    if len(clauses) >= 2:
        clauses[0], clauses[-1] = clauses[-1], clauses[0]
        cand = " ".join(clauses) + "."
        if clf.classify(cand)[0] == intended:
            return cand, True
    return text, False


def make_v2_paraphrase(topic_token, cat, base_fact):
    base_tok = sorted(fact_tokens(base_fact))
    cat_kws = sorted(fact_tokens(DEF_CLAUSE[cat]) & set(base_tok))
    others = [t for t in base_tok if t not in cat_kws]
    picks = (cat_kws[:2] + others[:2])[:4]
    body = ", ".join(picks)
    return "Para o caso, %s sao mantidos no %s de forma uniforme." % (body, topic_token)


def main():
    rng = np.random.default_rng(SEED_CASEGEN)
    clf = make_classifier()

    cases = {}
    issues = []

    for case_idx in range(N_CASES):
        case_id = "CASE-%03d" % (case_idx + 1)
        topics = [str(t) for t in rng.choice(TOPIC_POOL, size=3, replace=False)]
        topic_token = topics[0]
        fillers = topics[1:]

        # Subconjunto base: 9 de 12 categorias (G0); complemento = 3 categorias novas.
        base_cats = [str(c) for c in rng.choice(ALL_CATS, size=9, replace=False)]
        new_cats = [c for c in ALL_CATS if c not in base_cats]

        base_facts = []
        for j, cat in enumerate(base_cats):
            filler = fillers[j % len(fillers)]
            text = make_base_fact(topic_token, cat, filler)
            text, ok = verify_classification(text, clf, cat)
            if not ok:
                issues.append("%s base %s -> %s" % (case_id, cat, clf.classify(text)[0]))
            base_facts.append(text)

        g0, _g0cats = reconstruct_facts(base_facts)

        v1_pool = []
        v3_pool = []
        for cat in new_cats:
            for variant in (0, 1):
                v1_text = make_new_fact(topic_token, cat, variant, negate=False)
                v1_text, ok1 = verify_classification(v1_text, clf, cat)
                v3_text = make_new_fact(topic_token, cat, variant, negate=True)
                v3_text, ok3 = verify_classification(v3_text, clf, cat)
                if not ok1:
                    issues.append("%s V1 %s -> %s" % (case_id, cat, clf.classify(v1_text)[0]))
                if not ok3:
                    issues.append("%s V3 %s -> %s" % (case_id, cat, clf.classify(v3_text)[0]))
                v1_pool.append({
                    "candidate_id": "%s-V1-%s-%d" % (case_id, cat, variant),
                    "text": v1_text,
                    "intended_category": cat,
                    "is_true": True,
                    "pool": "V1",
                    "pair_id": "%s-%s-%d" % (case_id, cat, variant),
                })
                v3_pool.append({
                    "candidate_id": "%s-V3-%s-%d" % (case_id, cat, variant),
                    "text": v3_text,
                    "intended_category": cat,
                    "is_true": False,
                    "pool": "V3",
                    "pair_id": "%s-%s-%d" % (case_id, cat, variant),
                })

        # Candidatos V2: paráfrases entailadas de 6 fatos-base distintos.
        v2_pool = []
        for j in range(6):
            cat = base_cats[j]
            v2_text = make_v2_paraphrase(topic_token, cat, base_facts[j])
            v2_text, ok2 = verify_classification(v2_text, clf, cat)
            if not ok2:
                issues.append("%s V2 %s -> %s" % (case_id, cat, clf.classify(v2_text)[0]))
            v2_pool.append({
                "candidate_id": "%s-V2-%s" % (case_id, cat),
                "text": v2_text,
                "intended_category": cat,
                "is_true": True,
                "pool": "V2",
                "pair_id": None,
            })

        cases[case_id] = {
            "case_idx": case_idx,
            "seed_casegen": SEED_CASEGEN,
            "topic_tokens": list(topics),
            "topic_token": topic_token,
            "base_cats": base_cats,
            "new_cats": new_cats,
            "base_facts": base_facts,
            "g0": graph_view(g0),
            "pools": {"V1": v1_pool, "V2": v2_pool, "V3": v3_pool},
        }

    os.makedirs(INPUTS, exist_ok=True)
    out_path = os.path.join(INPUTS, "cases.yaml")
    with open(out_path, "w", encoding="utf-8") as f:
        yaml.safe_dump({"seed_casegen": SEED_CASEGEN, "n_cases": N_CASES,
                        "cases": cases}, f, allow_unicode=True, sort_keys=False)

    print("Casos gerados: %d (seed_casegen=%d)" % (N_CASES, SEED_CASEGEN))
    print("Candidatos: V1=%d V2=%d V3=%d" % (24 * 6, 24 * 6, 24 * 6))
    print("Issues de classificação na geração: %d" % len(issues))
    for g in issues[:30]:
        print("  !", g)
    print("saved:", out_path)


if __name__ == "__main__":
    main()
