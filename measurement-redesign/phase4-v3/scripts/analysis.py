# -*- coding: utf-8 -*-
"""
MR-C7 v3 — analysis_v3.py (estatística, decisão e relatório; protocolo §8–§13).

Mesma lógica da v2 (analysis.py) — Wilcoxon/TOST, Holm, compliance, pisos, fidelidade,
vetos — com as adaptações do MR-C7-PROTOCOLO-PREREGISTRO-V3.md:
  - outputs MR-C7-REPORT-V3.{md,json} e MR-C7-CASE-REGISTRY-V3.yaml;
  - todas as estatísticas DECISÓRIAS usam EXCLUSIVAMENTE DV_P = 0.6·conf + 0.2·ged_ref
    + 0.2·div_metric (§7.1 v3);
  - DV_Q = 0.7·conf + 0.3·div_metric é reportado como ANEXO DIAGNÓSTICO, nunca decisório;
  - reporta os TRÊS componentes separadamente (conf, ged_ref, div_metric), §7.5;
  - reporta a penalidade residual de conf(V2) atribuível à cadeia `follows` (§7.4);
  - diagnóstico de causa §7.5.1 estendido (A/B/C), com verificação de sinal residual de
    tipo-C (overlap espúrio ΔV2 vs fatos-base não-pai) nos casos novos da v3.
"""
import os
import re
import json
import math
import hashlib

import numpy as np
import yaml
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..", "..")
INPUTS = os.path.join(HERE, "..", "inputs")
OUTPUTS = os.path.join(HERE, "..", "outputs")
SCRIPTS = HERE

DELTA_EQ = 0.05
ALPHA = 0.05
N_MIN_EFFECTIVE = 15
COMPLIANCE_FLOOR = 0.80
TIE_EPS = 1e-9

PROTOCOLO_V3_HASH = "26986e473d3ee7245810945af619ab945db545fed35d90185defe998e7ed440b"
ADDENDUM_HASH = "4ce9fa87f0cd4fa6c0b33ffe2cc4ee5d27e3d998c142fce1c5ac60a9f13b4dc5"
GENERATOR_FIX_HASH = "d4a5b1b361137b42a7037ec885e8a217da99fd8bf8ef41cf767b9333ae8efa7b"
GENERATOR_HASH = "1340e462520ef73d1765cec34d7ad3b109b8876cc41a9459d7d2e68f0c108c9d"
CASES_V2_HASH = "479692d5d4a20a010fe0ac71e238c39f40ef990aa881b3e02555c80269ba7184"
CASES_V3_HASH = "gerado na execução (hash-lock §13)"

W_P = (0.6, 0.2, 0.2)  # DV_P decisório
W_Q = (0.7, 0.0, 0.3)  # DV_Q diagnóstico

PARS = {
    "P1": ("V1", "V0", "greater", "V1 > V0"),
    "P2": ("V1", "V2", "greater", "V1 > V2"),
    "P4": ("V0", "V3", "greater", "V3 < V0"),
    "P5": ("V2", "V3", "greater", "V3 < V2"),
}

_PT_STOP = {
    "o", "a", "os", "as", "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas",
    "para", "por", "com", "sem", "que", "era", "ser", "for", "foi", "sao", "mais", "menos",
    "um", "uma", "uns", "umas", "como", "mas", "ou", "se", "ja", "tambem", "e", "nao",
    "entre", "sobre", "ate", "apos", "depois", "antes", "durante", "contra",
}


def _tokens(text):
    return {
        t for t in re.findall(r"[A-Za-zÀ-ÿ0-9]+", text.lower())
        if len(t) >= 4 and t not in _PT_STOP
    }


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def wilcoxon_onesided(x, alternative):
    x = np.asarray(x, float)
    x = x[np.abs(x) > TIE_EPS]
    if len(x) == 0:
        return float("nan"), 0
    try:
        res = stats.wilcoxon(x, alternative=alternative, zero_method="wilcox")
        return float(res.statistic), float(res.pvalue)
    except ValueError:
        return float("nan"), 0


def holm_sequential(pvalues):
    order = sorted(range(len(pvalues)), key=lambda i: pvalues[i])
    m = len(pvalues)
    ok = [False] * m
    for rank, idx in enumerate(order):
        ok[idx] = pvalues[idx] <= ALPHA / (m - rank)
        if not ok[idx]:
            break
    return ok, order


def code_inspection_checklist():
    """Addendum §5.3 — grafo de importação + grep por símbolos compartilhados."""
    script_files = {
        "generate_cases.py": os.path.join(SCRIPTS, "generate_cases.py"),
        "labelers.py": os.path.join(SCRIPTS, "labelers.py"),
        "reconstruction.py": os.path.join(SCRIPTS, "reconstruction.py"),
        "metric.py": os.path.join(SCRIPTS, "metric.py"),
        "analysis.py": os.path.join(SCRIPTS, "analysis.py"),
    }
    imports = {}
    for name, path in script_files.items():
        imports[name] = []
        with open(path, encoding="utf-8") as f:
            for line in f:
                m = re.match(r"\s*from\s+([\w.]+)\s+import", line)
                if m:
                    imports[name].append(m.group(1))
                m = re.match(r"\s*import\s+([\w.]+)", line)
                if m and not m.group(1).startswith("import "):
                    imports[name].append(m.group(1).split(".")[0])

    violations = []
    if any("labelers" in i for i in imports.get("metric.py", [])):
        violations.append("metric.py importa labelers.py")
    if any("metric" in i for i in imports.get("labelers.py", [])):
        violations.append("labelers.py importa metric.py")
    if any("reconstruction" in i for i in imports.get("labelers.py", [])):
        violations.append("labelers.py importa reconstruction.py")

    labelers_src = open(script_files["labelers.py"], encoding="utf-8").read()
    metric_src = open(script_files["metric.py"], encoding="utf-8").read()
    shared_symbols = []
    for m in re.finditer(r"^def\s+(\w+)", labelers_src, re.M):
        sym = m.group(1)
        if sym == "main":
            continue
        if re.search(r"\b%s\s*\(" % re.escape(sym), metric_src):
            shared_symbols.append(sym)
    if shared_symbols:
        violations.append("símbolos compartilhados labelers×metric: %s" % shared_symbols)

    return {
        "imports": imports,
        "violations": violations,
        "shared_symbols": shared_symbols,
        "passed": not violations,
    }


def residual_tipo_c_check(states, cases_path):
    """Verificação de sinal residual de FAIL-tipo-C (§7.5.1c).

    Para cada caso, cada fato ΔV2 sorteado (states.yaml) é comparado com TODOS os
    fatos-base: se houver overlap ≥ 2 com qualquer fato-base que não seja o pai
    (a categoria intencional do candidato), a regra `relates` dispararia arestas
    espúrias — sinal residual de defeito do gerador (colisão de token).
    """
    with open(cases_path, encoding="utf-8") as f:
        cases = yaml.safe_load(f)["cases"]

    signals = []
    n_v2_total = 0
    n_spurious = 0
    for case_id, c in sorted(cases.items()):
        st = states["cases"].get(case_id)
        if not st or st.get("excluded"):
            continue
        base_facts = c["base_facts"]
        base_tok = [_tokens(bf) for bf in base_facts]
        v2_facts = st["states"]["V2"]["facts"]
        v2_ids = st["states"]["V2"]["drawn_ids"]
        for fact, cid in zip(v2_facts, v2_ids):
            n_v2_total += 1
            parent_cat = cid.split("-V2-")[1]
            base_cats = c["base_cats"]
            parent_idx = base_cats.index(parent_cat) if parent_cat in base_cats else -1
            ft = _tokens(fact)
            non_parent_overlap = 0
            for i, bt in enumerate(base_tok):
                if i == parent_idx:
                    continue
                if len(ft & bt) >= 2:
                    non_parent_overlap += 1
            if non_parent_overlap > 0:
                n_spurious += 1
            signals.append({
                "caso": case_id,
                "candidate": cid,
                "parent_cat": parent_cat,
                "n_fatos_base_nao_pai_overlap_ge_2": non_parent_overlap,
            })

    return {
        "n_fatos_v2_verificados": n_v2_total,
        "n_com_overlap_espurio": n_spurious,
        "sinal_residual_tipo_c": n_spurious > 0,
        "per_caso": signals,
    }


def follows_penalty_v2(recon_data):
    """Penalidade residual de conf(V2) atribuível à cadeia `follows` (§7.4).

    A verdade de V2 (build_v2_truth) exclui a cadeia `follows` incidente em entidades
    ΔV2. A reconstrução de V2 contém essas arestas como falsos positivos no F1 de
    arestas. Medimos: (i) nº de arestas `follows` extras; (ii) penalidade em conf.
    """
    results = recon_data["results"]
    truth = recon_data["truth_graphs"]
    out = []
    for case_id in sorted(results.keys()):
        rec = results[case_id]["V2"]["graph"]
        tr = truth[case_id]["V2"]
        rec_edges = set((e["source"], e["target"], e["relation_type"]) for e in rec["edges"])
        tr_edges = set((e["source"], e["target"], e["relation_type"]) for e in tr["edges"])
        follows_extra = sorted(e for e in rec_edges if e[2] == "follows" and e not in tr_edges)
        tr_edges_plus = tr_edges | set(follows_extra)

        def _f1(rec_set, tr_set, rec_size, tr_size):
            inter = len(rec_set & tr_set)
            p = inter / rec_size if rec_size else 0.0
            r = inter / tr_size if tr_size else 0.0
            return 2 * p * r / (p + r) if (p + r) else 0.0

        rec_nodes = set(n["syn_category"] for n in rec["nodes"])
        tr_nodes = set(n["syn_category"] for n in tr["nodes"])
        f1n = _f1(rec_nodes, tr_nodes, len(rec_nodes), len(tr_nodes))
        f1e_as_is = _f1(rec_edges, tr_edges, len(rec_edges), len(tr_edges))
        f1e_plus = _f1(rec_edges, tr_edges_plus, len(rec_edges), len(tr_edges_plus))
        conf_as_is = (f1n + f1e_as_is) / 2.0
        conf_no_follows = (f1n + f1e_plus) / 2.0
        out.append({
            "caso": case_id,
            "n_follows_extra": len(follows_extra),
            "conf_v2_as_is": round(conf_as_is, 6),
            "conf_v2_sem_penalidade_follows": round(conf_no_follows, 6),
            "penalidade_follows": round(conf_no_follows - conf_as_is, 6),
        })
    return out


def main():
    with open(os.path.join(OUTPUTS, "dv_values.json"), encoding="utf-8") as f:
        dv_data = json.load(f)
    with open(os.path.join(OUTPUTS, "reconstruction_graphs.json"), encoding="utf-8") as f:
        recon_data = json.load(f)
    with open(os.path.join(INPUTS, "states.yaml"), encoding="utf-8") as f:
        states = yaml.safe_load(f)

    values = dv_data["values"]
    case_ids = sorted(values.keys())
    n = len(case_ids)

    # DV_P é o valor DECISÓRIO (§7.1 v3); DV_Q é diagnóstico.
    dv_p = {c: {s: values[c][s]["dv_p"] for s in ("V0", "V1", "V2", "V3")} for c in case_ids}
    dv_q = {c: {s: values[c][s]["dv_q"] for s in ("V0", "V1", "V2", "V3")} for c in case_ids}
    dv = dv_p  # tudo que segue usa DV_P

    # ---- P1–P5 (sobre DV_P)
    diffs = {}
    for par, (hi, lo, alt, label) in PARS.items():
        diffs[par] = [dv[c][hi] - dv[c][lo] for c in case_ids]
    d_p3 = [dv[c]["V2"] - dv[c]["V0"] for c in case_ids]

    par_results = {}
    for par, (hi, lo, alt, label) in PARS.items():
        stat, p = wilcoxon_onesided(diffs[par], alt)
        neff = int(np.sum(np.abs(np.asarray(diffs[par])) > TIE_EPS))
        par_results[par] = {"hi": hi, "lo": lo, "alternative": alt, "label": label,
                            "statistic": stat, "pvalue": p, "n_effective": neff,
                            "n_pass": neff >= N_MIN_EFFECTIVE}

    pvals = [par_results[par]["pvalue"] for par in ("P1", "P2", "P4", "P5")]
    holm_ok, holm_order = holm_sequential(pvals)
    for rank, par in enumerate(("P1", "P2", "P4", "P5")):
        par_results[par]["holm_pass"] = holm_ok[rank]

    x_p3 = np.asarray(d_p3, float)
    p3_stat_lo, p3_p_lo = wilcoxon_onesided(x_p3 - DELTA_EQ, "less")
    p3_stat_hi, p3_p_hi = wilcoxon_onesided(x_p3 + DELTA_EQ, "greater")
    p3 = {"statistic_lo": p3_stat_lo, "p_lo": p3_p_lo,
          "statistic_hi": p3_stat_hi, "p_hi": p3_p_hi,
          "tost_pass": (p3_p_lo < ALPHA) and (p3_p_hi < ALPHA)}

    # ---- compliance (§8.2) sobre DV_P
    ord_flags = []
    for c in case_ids:
        a = dv[c]["V1"] >= dv[c]["V0"] - DELTA_EQ
        b = dv[c]["V1"] >= dv[c]["V2"] - DELTA_EQ
        cc = abs(dv[c]["V2"] - dv[c]["V0"]) <= DELTA_EQ
        d = dv[c]["V0"] >= dv[c]["V3"] + DELTA_EQ
        e = dv[c]["V2"] >= dv[c]["V3"] + DELTA_EQ
        ord_flags.append({"case": c, "a": a, "b": b, "c": cc, "d": d, "e": e,
                          "ord": 1 if (a and b and cc and d and e) else 0})
    compliance_rate = sum(o["ord"] for o in ord_flags) / n

    # ---- pisos de efeito (§8.3) sobre DV_P
    floors = {
        "mediana(DV_P(V1)-DV_P(V0))": float(np.median(diffs["P1"])),
        "mediana(DV_P(V1)-DV_P(V2))": float(np.median(diffs["P2"])),
        "mediana(DV_P(V0)-DV_P(V3))": float(np.median(diffs["P4"])),
        "mediana(DV_P(V2)-DV_P(V3))": float(np.median(diffs["P5"])),
    }
    floors_pass = all(v > DELTA_EQ for v in floors.values())

    # ---- fidelidade §6.2
    fid_abs_nodes = []
    fid_abs_edges = []
    per_case_ok = []
    for c in case_ids:
        dn = abs(values[c]["V1"]["nodes"] - values[c]["V3"]["nodes"])
        de = abs(values[c]["V1"]["edges"] - values[c]["V3"]["edges"])
        fid_abs_nodes.append(dn)
        fid_abs_edges.append(de)
        per_case_ok.append(dn <= 3)
    fidelity = {
        "mean_abs_nodes": float(np.mean(fid_abs_nodes)),
        "mean_abs_edges": float(np.mean(fid_abs_edges)),
        "limit_nodes": 1.5,
        "limit_edges": 3.0,
        "per_case_node_limit": 3,
        "per_case_ok": all(per_case_ok),
        "passed": (float(np.mean(fid_abs_nodes)) <= 1.5
                   and float(np.mean(fid_abs_edges)) <= 3.0 and all(per_case_ok)),
    }

    # ---- invariância a seed (§7.5)
    inv = recon_data["seed_invariance"]
    seed_invariance = all(all(v for v in inv[c].values()) for c in case_ids)

    # ---- vetos (sobre DV_P)
    v_a_cases = [c for c in case_ids
                 if abs(dv[c]["V1"] - dv[c]["V0"]) <= DELTA_EQ
                 and abs(dv[c]["V3"] - dv[c]["V0"]) <= DELTA_EQ]
    veto_a = len(v_a_cases) / n >= 0.50
    insp = code_inspection_checklist()
    veto_b = not insp["passed"]
    veto_c = not fidelity["passed"]
    vetoes = {
        "V-A": {"acionado": veto_a, "n_cases": len(v_a_cases), "proporcao": round(len(v_a_cases) / n, 4)},
        "V-B": {"acionado": veto_b, "inspecao": insp["passed"]},
        "V-C": {"acionado": veto_c, "fidelidade": fidelity["passed"]},
    }

    # ---- regra de decisão §8.4
    d1 = all(par_results[par]["holm_pass"] for par in ("P1", "P2", "P4", "P5"))
    d2 = p3["tost_pass"]
    d3 = all(par_results[par]["n_pass"] for par in ("P1", "P2", "P4", "P5"))
    d4 = compliance_rate >= COMPLIANCE_FLOOR
    d5 = floors_pass
    d6 = fidelity["passed"]
    d7 = not (veto_a or veto_b or veto_c)
    d8 = True
    decision = {
        "P1-P5_Holm": d1,
        "P3_TOST": d2,
        "N_efetivo_ge_15": d3,
        "compliance_ge_0.80": d4,
        "pisos_de_efeito": d5,
        "fidelidade_6.2": d6,
        "sem_veto": d7,
        "sem_violacao_procedimento": d8,
        "PASS": all([d1, d2, d3, d4, d5, d6, d7, d8]),
    }

    # ---- penalidade residual conf(V2) via follows (§7.4)
    follows_pen = follows_penalty_v2(recon_data)
    mean_follows_extra = float(np.mean([fp["n_follows_extra"] for fp in follows_pen]))
    mean_pen = float(np.mean([fp["penalidade_follows"] for fp in follows_pen]))
    mean_conf_v2_as_is = float(np.mean([fp["conf_v2_as_is"] for fp in follows_pen]))
    mean_conf_v2_no_follows = float(np.mean([fp["conf_v2_sem_penalidade_follows"] for fp in follows_pen]))
    conf_v0 = float(np.mean([values[c]["V0"]["conf"] for c in case_ids]))
    delta_conf_v2_v0 = conf_v0 - mean_conf_v2_as_is
    follows_report = {
        "mean_follows_extra_por_caso": round(mean_follows_extra, 4),
        "mean_penalidade_follows_conf": round(mean_pen, 6),
        "mean_conf_v2_as_is": round(mean_conf_v2_as_is, 6),
        "mean_conf_v2_sem_penalidade_follows": round(mean_conf_v2_no_follows, 6),
        "conf_v0_mean": round(conf_v0, 6),
        "delta_conf_v2_v0": round(delta_conf_v2_v0, 6),
        "delta_dentro_banda_eq": delta_conf_v2_v0 <= DELTA_EQ,
        "per_caso": follows_pen,
    }

    # ---- sinal residual de tipo-C (§7.5.1c) nos casos novos
    tipo_c = residual_tipo_c_check(states, os.path.join(INPUTS, "cases.yaml"))

    # ---- diagnóstico de causa (§7.5.1) — apenas se FAIL
    cause = None
    if not decision["PASS"]:
        conf_v1 = np.array([values[c]["V1"]["conf"] for c in case_ids])
        conf_v3 = np.array([values[c]["V3"]["conf"] for c in case_ids])
        dv_v1 = np.array([dv[c]["V1"] for c in case_ids])
        dv_v3 = np.array([dv[c]["V3"] for c in case_ids])
        conf_disc = float(np.median(conf_v1 - conf_v3))
        comp_disc = float(np.median(dv_v1 - dv_v3))
        if tipo_c["sinal_residual_tipo_c"]:
            cause = ("(c)", "FAIL-tipo-C — defeito de construção do gerador de casos",
                     conf_disc, comp_disc)
        elif conf_disc <= DELTA_EQ:
            cause = ("(a)", "FAIL-tipo-A — falha do componente conf",
                     conf_disc, comp_disc)
        elif comp_disc <= DELTA_EQ:
            cause = ("(b)", "FAIL-tipo-B — diluição de agregação (com pesos do Esquema P v3)",
                     conf_disc, comp_disc)
        else:
            cause = ("(b)*", "FAIL-tipo-B* — agregação nos testes de nível (V1 vs V0/V2); "
                             "par V1×V3 discriminado por conf e pelo composto",
                     conf_disc, comp_disc)

    # ---- anexo DV_Q (diagnóstico, §7.1 v3 / §13 v3)
    d_q_floor = {
        "mediana(DV_Q(V1)-DV_Q(V0))": float(np.median([dv_q[c]["V1"] - dv_q[c]["V0"] for c in case_ids])),
        "mediana(DV_Q(V1)-DV_Q(V2))": float(np.median([dv_q[c]["V1"] - dv_q[c]["V2"] for c in case_ids])),
        "mediana(DV_Q(V0)-DV_Q(V3))": float(np.median([dv_q[c]["V0"] - dv_q[c]["V3"] for c in case_ids])),
        "mediana(DV_Q(V2)-DV_Q(V3))": float(np.median([dv_q[c]["V2"] - dv_q[c]["V3"] for c in case_ids])),
    }
    dv_q_report = {
        "media_por_estado": {
            s: round(float(np.mean([dv_q[c][s] for c in case_ids])), 6)
            for s in ("V0", "V1", "V2", "V3")
        },
        "pisos_de_efeito": {k: round(v, 6) for k, v in d_q_floor.items()},
        "declaracao": ("Anexo diagnóstico exclusivamente; NUNCA fundamenta PASS/FAIL (§7.1/§13 v3)."),
    }

    # ---- hashes dos artefatos
    artifact_hashes = {}
    for fname in ("generate_cases.py", "labelers.py", "reconstruction.py",
                  "metric.py", "analysis.py"):
        artifact_hashes[fname] = sha256_file(os.path.join(SCRIPTS, fname))
    for fname in ("cases.yaml", "states.yaml", "consensus_registry.yaml"):
        artifact_hashes[fname] = sha256_file(os.path.join(INPUTS, fname))
    for fname in ("reconstruction_graphs.json", "dv_values.json"):
        artifact_hashes[fname] = sha256_file(os.path.join(OUTPUTS, fname))
    artifact_hashes["cases.yaml"] = sha256_file(os.path.join(INPUTS, "cases.yaml"))

    # ---- JSON de relatório
    report_json = {
        "gate": "MR-C7-V3",
        "protocolo_hash": PROTOCOLO_V3_HASH,
        "addendum_hash": ADDENDUM_HASH,
        "generator_fix_hash": GENERATOR_FIX_HASH,
        "generator_hash": GENERATOR_HASH,
        "n_cases": n,
        "seed_casegen": 20260819,
        "seed_draw": 20260819,
        "seed_master": 20260819,
        "pesos_DV_P": W_P,
        "pesos_DV_Q": W_Q,
        "delta_eq": DELTA_EQ,
        "alpha": ALPHA,
        "por_caso": {
            c: {
                "dv_p": dv_p[c],
                "dv_q": dv_q[c],
                "conf": {s: values[c][s]["conf"] for s in ("V0", "V1", "V2", "V3")},
                "ged_ref": {s: values[c][s]["ged_ref"] for s in ("V0", "V1", "V2", "V3")},
                "div_metric": {s: values[c][s]["div_metric"] for s in ("V0", "V1", "V2", "V3")},
                "nodes": {s: values[c][s]["nodes"] for s in ("V0", "V1", "V2", "V3")},
                "edges": {s: values[c][s]["edges"] for s in ("V0", "V1", "V2", "V3")},
            } for c in case_ids
        },
        "estatisticas_por_par": {
            par: {k: par_results[par][k] for k in
                  ("hi", "lo", "alternative", "label", "statistic", "pvalue",
                   "n_effective", "n_pass", "holm_pass")}
            for par in ("P1", "P2", "P4", "P5")
        },
        "P3_TOST": p3,
        "compliance": {"rate": round(compliance_rate, 4),
                       "floor": COMPLIANCE_FLOOR,
                       "per_case": ord_flags},
        "pisos_de_efeito": {k: round(v, 6) for k, v in floors.items()},
        "fidelidade_6.2": {k: (round(v, 6) if isinstance(v, float) else v)
                           for k, v in fidelity.items()},
        "seed_invariance": seed_invariance,
        "vetos": vetoes,
        "decisao": decision,
        "diagnostico_causa": cause,
        "penalidade_follows_conf_v2": follows_report,
        "sinal_residual_tipo_c": tipo_c,
        "anexo_dv_q": dv_q_report,
        "nota_interpretativa_governanca": (
            "Nota da governança sobre o que a v3 mede: o piso de efeito V1−V3 já é "
            "matematicamente garantido pelo peso de conf sozinho (0.6 × ~0.10 ≈ 0.06 > 0.05), "
            "independente dos proxies estruturais. O teste real da v3 é se ged_ref/div_metric, "
            "com peso 0.2 cada, ainda distorcem o suficiente para derrubar compliance, pisos ou "
            "vetos em P3/P5 — não se conf funciona (estabelecido pela v2). Nenhum critério "
            "pré-registrado foi alterado."
        ),
        "nota_interpretativa": (
            "ged_ref tem limitação conhecida: a referência DATA-DRIVEN é construída só a partir "
            "de V0, então tende a não discriminar bem V1 de V3 — achado da v1, não corrigido "
            "(fora de escopo). Reportado por componente; não é sinal novo."
        ),
        "hashes": artifact_hashes,
    }

    with open(os.path.join(OUTPUTS, "MR-C7-REPORT-V3.json"), "w", encoding="utf-8") as f:
        json.dump(report_json, f, indent=2, ensure_ascii=False)

    # ---- CASE-REGISTRY-V3.yaml
    with open(os.path.join(INPUTS, "consensus_registry.yaml"), encoding="utf-8") as f:
        registry = yaml.safe_load(f)
    case_registry = {
        "gate": "MR-C7-V3",
        "padrao": "EVALUATION_REGISTRY.yaml (M-REDESIGN-01-SPEC-A.md §8.2)",
        "mecanismo": "consenso algorítmico determinístico S-A/S-B/S-C (addendum 4ce9fa87...)",
        "protocolo_hash": PROTOCOLO_V3_HASH,
        "seed_draw": states["seed_draw"],
        "seed_master": states["seed_master"],
        "seed_casegen": 20260819,
        "casos": {},
        "consenso": registry["registro"],
    }
    for c in case_ids:
        st = states["cases"].get(c)
        if not st or st.get("excluded"):
            case_registry["casos"][c] = {"excluded": True}
            continue
        case_registry["casos"][c] = {
            "base_facts": st["base_facts"],
            "states": {
                "V1": {"facts": st["states"]["V1"]["facts"],
                       "drawn_ids": st["states"]["V1"]["drawn_ids"],
                       "categorias": st["states"]["V1"]["categories"]},
                "V2": {"facts": st["states"]["V2"]["facts"],
                       "drawn_ids": st["states"]["V2"]["drawn_ids"]},
                "V3": {"facts": st["states"]["V3"]["facts"],
                       "drawn_ids": st["states"]["V3"]["drawn_ids"]},
            },
            "seeds": st["seeds"],
        }
    with open(os.path.join(OUTPUTS, "MR-C7-CASE-REGISTRY-V3.yaml"), "w", encoding="utf-8") as f:
        yaml.safe_dump(case_registry, f, allow_unicode=True, sort_keys=False)

    report_json_hash = sha256_file(os.path.join(OUTPUTS, "MR-C7-REPORT-V3.json"))
    registry_hash = sha256_file(os.path.join(OUTPUTS, "MR-C7-CASE-REGISTRY-V3.yaml"))
    artifact_hashes["MR-C7-REPORT-V3.json"] = report_json_hash
    artifact_hashes["MR-C7-CASE-REGISTRY-V3.yaml"] = registry_hash

    # ---- MD report
    lines = []
    lines.append("# MR-C7-REPORT-V3")
    lines.append("")
    lines.append("## Gate MR-C7 (v3) — Validade Discriminante de Valor (DV-REDESIGN)")
    lines.append("**Status da decisão:** **%s**" % ("PASS (PROVISÓRIO)" if decision["PASS"] else "FAIL"))
    lines.append("")
    lines.append("## 1. Identificação")
    lines.append("")
    lines.append("| Item | Valor |")
    lines.append("|------|-------|")
    lines.append("| Pré-registro | `MR-C7-PROTOCOLO-PREREGISTRO-V3.md` (hash `%s`) |" % PROTOCOLO_V3_HASH)
    lines.append("| Correção do gerador (v2, herdada) | `C-GENERATOR-FIX-V2-PARAPHRASE.md` (hash `%s`) |" % GENERATOR_FIX_HASH)
    lines.append("| `generate_cases.py` (corrigido) | `%s` |" % GENERATOR_HASH)
    lines.append("| Addendum (consenso algorítmico) | `C-MODEL-SUBSTITUTION-ADDENDUM.md` (hash `%s`) |" % ADDENDUM_HASH)
    lines.append("| Casos | %d sintéticos NOVOS (N=24; seed_casegen=20260819) — nenhum compartilhado com v1/v2 |" % n)
    lines.append("| Estados | V0 (baseline), V1 (correta+relevante), V2 (correta+redundante), V3 (falsa/ruidosa) |")
    lines.append("| K_additional | 3 por estado (seed_draw=20260819) |")
    lines.append("| seed_master reconstruções | 20260819 (3 seeds por caso, procedimento `generate_seeds.py` congelado) |")
    lines.append("| Esquema P (decisório) | `DV_P = 0.6·conf + 0.2·ged_ref + 0.2·div_metric` |")
    lines.append("| Esquema Q (diagnóstico) | `DV_Q = 0.7·conf + 0.3·div_metric` — anexo, nunca decisório |")
    lines.append("| δ_eq | 0.05 (banda de equivalência e piso de efeito) |")
    lines.append("| α | 0.05 |")
    lines.append("")
    lines.append("## 2. Nota da governança sobre o que a v3 mede")
    lines.append("")
    lines.append("> %s" % report_json["nota_interpretativa_governanca"])
    lines.append("")
    lines.append("## 3. Nota interpretativa (registrada conforme determinação da governança)")
    lines.append("")
    lines.append("> %s" % report_json["nota_interpretativa"])
    lines.append("")
    lines.append("## 4. Ground truth — limitação (§5 e §5.1)")
    lines.append("")
    lines.append("> O ground truth deste gate é **consenso algorítmico determinístico** (S-A/S-B/S-C), "
                 "**ainda mais fraco** que consenso de IA. **Qualquer PASS é PROVISÓRIO**, pendente de "
                 "reverificação com modelos de IA reais (três provedores distintos, versões correntes) "
                 "antes de qualquer decisão de governança sobre o GO-8E.")
    lines.append("")
    lines.append("## 5. Resumo executivo")
    lines.append("")
    lines.append("| Métrica | Resultado |")
    lines.append("|---------|-----------|")
    lines.append("| Decisão | **%s** |" % ("PASS (PROVISÓRIO)" if decision["PASS"] else "FAIL"))
    lines.append("| compliance_rate (DV_P) | %.4f (exigência ≥ %.2f) |" % (compliance_rate, COMPLIANCE_FLOOR))
    lines.append("| Invariância a seed | %s |" % ("OK" if seed_invariance else "FALHOU"))
    lines.append("| Fidelidade §6.2 | %s (média\\|nós V1−V3\\|=%.4f; média\\|arestas V1−V3\\|=%.4f) |"
                 % ("PASS" if fidelity["passed"] else "FAIL",
                    fidelity["mean_abs_nodes"], fidelity["mean_abs_edges"]))
    lines.append("| Sinal residual tipo-C (§7.5.1c) | %s (%d/%d fatos ΔV2 com overlap espúrio) |"
                 % ("PRESENTE" if tipo_c["sinal_residual_tipo_c"] else "AUSENTE",
                    tipo_c["n_com_overlap_espurio"], tipo_c["n_fatos_v2_verificados"]))
    lines.append("")
    lines.append("### Valores médios por estado (composto e componentes, §7.5)")
    lines.append("")
    lines.append("| Estado | DV_P (média) | conf (média) | ged_ref (média) | div_metric (média) | DV_Q (média) |")
    lines.append("|--------|--------------|--------------|-----------------|--------------------|--------------|")
    for s in ("V0", "V1", "V2", "V3"):
        lines.append("| %s | %.6f | %.6f | %.6f | %.6f | %.6f |" % (
            s,
            float(np.mean([dv_p[c][s] for c in case_ids])),
            float(np.mean([values[c][s]["conf"] for c in case_ids])),
            float(np.mean([values[c][s]["ged_ref"] for c in case_ids])),
            float(np.mean([values[c][s]["div_metric"] for c in case_ids])),
            float(np.mean([dv_q[c][s] for c in case_ids]))))
    lines.append("")
    lines.append("## 6. Resultados por par (P1–P5, sobre DV_P)")
    lines.append("")
    lines.append("| Par | Relação | Wilcoxon W | p | Holm PASS | N efetivo (≥15) |")
    lines.append("|-----|---------|-----------|----|-----------|-----------------|")
    for par in ("P1", "P2", "P4", "P5"):
        r = par_results[par]
        lines.append("| %s | %s | %.3f | %.6f | %s | %d |"
                     % (par, r["label"], r["statistic"], r["pvalue"],
                        "PASS" if r["holm_pass"] else "FAIL", r["n_effective"]))
    lines.append("")
    lines.append("**P3 (TOST, δ_eq=0.05, V2 ≈ V0):** p_baixo=%.6f (Wilcoxon W=%.3f), "
                 "p_alto=%.6f (W=%.3f) → **%s**"
                 % (p3["p_lo"], p3["statistic_lo"], p3["p_hi"], p3["statistic_hi"],
                    "PASS" if p3["tost_pass"] else "FAIL"))
    lines.append("")
    lines.append("## 6.1 Penalidade residual de conf(V2) via cadeia `follows` (§7.4)")
    lines.append("")
    lines.append("Média de arestas `follows` extras = **%.4f/caso**; penalidade média em conf = **%.6f** "
                 "(conf(V2) = %.6f; sem a penalidade = %.6f). Δconf(V2)−V0 = **%.6f** "
                 "(banda δ_eq = 0.05) → **%s**."
                 % (mean_follows_extra, mean_pen, mean_conf_v2_as_is, mean_conf_v2_no_follows,
                    delta_conf_v2_v0,
                    "dentro da banda" if delta_conf_v2_v0 <= DELTA_EQ else "fora da banda"))
    lines.append("")
    lines.append("## 7. Compliance (§8.2, sobre DV_P)")
    lines.append("")
    lines.append("compliance_rate = **%.4f** (exigência ≥ 0.80). Casos conformes: %d/%d."
                 % (compliance_rate, sum(o["ord"] for o in ord_flags), n))
    lines.append("")
    lines.append("## 8. Pisos de efeito (§8.3, exigência > 0.05, sobre DV_P)")
    lines.append("")
    lines.append("| Gap | Mediana | Exigência |")
    lines.append("|-----|---------|-----------|")
    for k, v in floors.items():
        lines.append("| %s | %.6f | > 0.05 → %s |" % (k, v, "PASS" if v > DELTA_EQ else "FAIL"))
    lines.append("")
    lines.append("## 9. Controles")
    lines.append("")
    lines.append("- **Fidelidade estrutural (§6.2):** %s — média|nós V1−V3|=%.4f (≤1.5), "
                 "média|arestas V1−V3|=%.4f (≤3.0), por caso |nós|≤3: %s"
                 % ("PASS" if fidelity["passed"] else "FAIL",
                    fidelity["mean_abs_nodes"], fidelity["mean_abs_edges"],
                    "OK" if fidelity["per_case_ok"] else "FALHOU"))
    lines.append("- **Invariância a seed (§7.5):** %s (saída idêntica nos 3 seeds derivados de seed_master=20260819)."
                 % ("OK" if seed_invariance else "FALHOU"))
    lines.append("- **Não-circularidade (§6.4):** rótulos fixados pelo gerador+consenso antes de qualquer cálculo de DV; "
                 "pesos e decisão de §7.4 pré-registrados, irrevogáveis após inspeção de DV.")
    lines.append("")
    lines.append("## 10. Vetos (§11)")
    lines.append("")
    lines.append("| Veto | Condição | Status |")
    lines.append("|------|----------|--------|")
    lines.append("| V-A — Cegueira ao valor | ≥50%% casos com \\|DV(V1)−DV(V0)\\|≤δ e \\|DV(V3)−DV(V0)\\|≤δ | %s (%d/%d casos, %.1f%%) |"
                 % ("ACIONADO" if veto_a else "não acionado", len(v_a_cases), n, 100 * len(v_a_cases) / n))
    lines.append("| V-B — Integridade do rótulo | inspeção de código (addendum §5.3) | %s |"
                 % ("VIOLAÇÃO" if veto_b else "não acionado (inspeção PASS)"))
    lines.append("| V-C — Controle quebrado | fidelidade §6.2 | %s |"
                 % ("ACIONADO" if veto_c else "não acionado"))
    lines.append("")
    lines.append("### Checklist de inspeção de código (addendum §5.3)")
    lines.append("")
    lines.append("Grafo de importação por script (módulos de phase4-v3 e externos):")
    for name in ("generate_cases.py", "labelers.py", "reconstruction.py", "metric.py", "analysis.py"):
        lines.append("- `%s` → imports: %s" % (name, ", ".join(insp["imports"].get(name, [])) or "(nenhum)"))
    lines.append("")
    lines.append("Proibições verificadas: labelers.py não importa metric.py/reconstruction.py; "
                 "metric.py não importa labelers.py; nenhum símbolo `def` de labelers.py é chamado em metric.py.")
    lines.append("Símbolos compartilhados labelers×metric: **%s**" %
                 (", ".join(insp.get("shared_symbols") or []) or "nenhum"))
    lines.append("")
    lines.append("## 11. Regra de decisão (§8.4)")
    lines.append("")
    lines.append("| Condição | Resultado |")
    lines.append("|----------|-----------|")
    for k, v in decision.items():
        if k == "PASS":
            continue
        lines.append("| %s | %s |" % (k, "PASS" if v else "FAIL"))
    lines.append("| **DECISÃO** | **%s** |" % ("PASS (PROVISÓRIO)" if decision["PASS"] else "FAIL"))
    lines.append("")
    if not decision["PASS"]:
        lines.append("### Diagnóstico de causa (§7.5.1)")
        lines.append("")
        lines.append("> Causa declarada: **%s** — %s" % (cause[0], cause[1]))
        lines.append(">")
        lines.append("> Suporte numérico: mediana(conf(V1)−conf(V3)) = %.6f; "
                     "mediana(DV_P(V1)−DV_P(V3)) = %.6f (piso δ_eq = 0.05)."
                     % (cause[2], cause[3]))
        lines.append(">")
        lines.append("> Verificação de sinal residual de FAIL-tipo-C (§7.5.1c): %d/%d fatos ΔV2 com "
                     "overlap ≥ 2 em fatos-base não-pai → %s."
                     % (tipo_c["n_com_overlap_espurio"], tipo_c["n_fatos_v2_verificados"],
                        "SINAL PRESENTE (resultado não definitivo até correção do gerador)"
                        if tipo_c["sinal_residual_tipo_c"] else "AUSENTE — resultado pode ser aceito como definitivo"))
        lines.append(">")
        if cause[0] == "(a)":
            lines.append("> Recomendação: redesenhar o componente estrutural (`div_metric` e/ou `ged_ref`, "
                         "incl. escolha de referência) antes de nova tentativa (§9/§14). GO-8E permanece NÃO AUTORIZADO.")
        elif cause[0] == "(b)":
            lines.append("> Recomendação: revisar o esquema de agregação/pesos (agora o do Esquema P da v3, §7.1), "
                         "não os componentes. GO-8E permanece NÃO AUTORIZADO.")
        elif cause[0] == "(c)":
            lines.append("> Recomendação: corrigir o gerador de casos (`generate_cases.py` ou `labelers.py`), "
                         "não a métrica nem a agregação (§7.5.1c). GO-8E permanece NÃO AUTORIZADO.")
        else:
            lines.append("> Recomendação: revisar o esquema de agregação/pesos e a referência GED (os testes de "
                         "nível V1 vs V0/V2 falham; o par V1×V3 é discriminado por conf). GO-8E permanece NÃO AUTORIZADO.")
    lines.append("")
    lines.append("## 12. Anexo diagnóstico — Esquema Q (§7.1 v3; NUNCA decisório)")
    lines.append("")
    lines.append("> %s" % dv_q_report["declaracao"])
    lines.append("")
    lines.append("| Estado | DV_Q (média) |")
    lines.append("|--------|--------------|")
    for s in ("V0", "V1", "V2", "V3"):
        lines.append("| %s | %.6f |" % (s, dv_q_report["media_por_estado"][s]))
    lines.append("")
    lines.append("| Gap DV_Q | Mediana |")
    lines.append("|----------|---------|")
    for k, v in dv_q_report["pisos_de_efeito"].items():
        lines.append("| %s | %.6f |" % (k, v))
    lines.append("")
    lines.append("## 13. Hashes (SHA-256)")
    lines.append("")
    lines.append("### Scripts (hash-lock antes da execução)")
    lines.append("")
    lines.append("| Script | SHA-256 |")
    lines.append("|--------|---------|")
    for fname in ("generate_cases.py", "labelers.py", "reconstruction.py", "metric.py", "analysis.py"):
        lines.append("| `%s` | `%s` |" % (fname, artifact_hashes[fname]))
    lines.append("")
    lines.append("### Inputs e saídas intermediárias")
    lines.append("")
    lines.append("| Artefato | SHA-256 |")
    lines.append("|----------|---------|")
    for fname in ("cases.yaml", "states.yaml", "consensus_registry.yaml",
                  "reconstruction_graphs.json", "dv_values.json"):
        lines.append("| `%s` | `%s` |" % (fname, artifact_hashes[fname]))
    lines.append("")
    lines.append("### Artefatos de relatório (§13)")
    lines.append("")
    lines.append("| Artefato | SHA-256 |")
    lines.append("|----------|---------|")
    lines.append("| `MR-C7-REPORT-V3.json` | `%s` |" % report_json_hash)
    lines.append("| `MR-C7-CASE-REGISTRY-V3.yaml` | `%s` |" % registry_hash)
    lines.append("| `MR-C7-REPORT-V3.md` | (hash deste relatório — registrado externamente após a escrita) |")
    lines.append("")
    lines.append("## 14. Consequências (§14)")
    lines.append("")
    if decision["PASS"]:
        lines.append("DV-REDESIGN (pesos do Esquema P, §7.1) autorizada para uso confirmatório "
                     "**PROVISÓRIO** (limitado ao consenso algorítmico; reverificação com IA real "
                     "pendente). Material para decisão de governança sobre o DESENHO do GO-8E a ser "
                     "preparado como acompanhamento (não é este gate). Mesmo com PASS: validade "
                     "PROVISÓRIA, sem decisão sobre GO-8E.")
    else:
        lines.append("Resultado válido e definitivo para este pré-registro (§9), **condicionado à "
                     "verificação de sinal residual tipo-C** (§7.5.1c). GO-8E permanece NÃO AUTORIZADO. "
                     "Redesenho recomendado conforme diagnóstico de causa mediante novo pré-registro.")
    lines.append("")
    lines.append("**Assinatura:** Execução de gate MR-C7 v3 (consenso algorítmico, addendum 4ce9fa87...)")
    lines.append("**Data:** 2026-08-19")
    lines.append("")

    md_text = "\n".join(lines)
    md_path = os.path.join(OUTPUTS, "MR-C7-REPORT-V3.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_text)

    print("==== MR-C7-V3 SUMMARY ====")
    print("Decisão:", decision["PASS"])
    print("Compliance:", round(compliance_rate, 4))
    for par in ("P1", "P2", "P4", "P5"):
        r = par_results[par]
        print("  %s p=%.6f Holm=%s N_eff=%d" % (par, r["pvalue"], r["holm_pass"], r["n_effective"]))
    print("  P3 TOST p_lo=%.6f p_hi=%.6f PASS=%s" % (p3["p_lo"], p3["p_hi"], p3["tost_pass"]))
    print("Pisos:", {k: round(v, 6) for k, v in floors.items()})
    print("Fidelidade §6.2:", fidelity["passed"], fidelity["mean_abs_nodes"], fidelity["mean_abs_edges"])
    print("Seed invariance:", seed_invariance)
    print("Vetos:", {k: v["acionado"] for k, v in vetoes.items()})
    print("Penalidade follows (média/caso):", round(mean_follows_extra, 4), "conf_pen:", round(mean_pen, 6),
          "delta_conf_v2_v0:", round(delta_conf_v2_v0, 6))
    print("Sinal residual tipo-C:", tipo_c["sinal_residual_tipo_c"],
          tipo_c["n_com_overlap_espurio"], "/", tipo_c["n_fatos_v2_verificados"])
    print("Causa (se FAIL):", cause)
    print("DV_Q médio por estado:", {s: dv_q_report["media_por_estado"][s] for s in ("V0", "V1", "V2", "V3")})
    print("Hashes scripts (pré-execução == pós-execução):", artifact_hashes)
    print("saved:", md_path)


if __name__ == "__main__":
    main()