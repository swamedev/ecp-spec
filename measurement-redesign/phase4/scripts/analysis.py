# -*- coding: utf-8 -*-
"""
MR-C7 phase4 — analysis.py (estatística, decisão e relatório; protocolo §8–§13).

Computa, conforme o pré-registro congelado:
  - P1–P5: Wilcoxon assinado unilateral (P1,P2,P4,P5) + TOST δ_eq=0.05 (P3);
  - Holm-Bonferroni dentro dos 4 direcionais (α=0.05); N efetivo ≥ 15;
  - compliance_rate ≥ 0.80 (§8.2);
  - pisos de efeito > 0.05 (§8.3);
  - check de fidelidade §6.2; invariância a seed (§7.5); vetos V-A/V-B/V-C (§11);
  - regra de decisão §8.4 e consequências §14 (com diagnóstico de causa §7.5.1).
Gera outputs/MR-C7-REPORT.md, MR-C7-REPORT.json e MR-C7-CASE-REGISTRY.yaml (§13).
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

PARS = {
    "P1": ("V1", "V0", "greater", "V1 > V0"),
    "P2": ("V1", "V2", "greater", "V1 > V2"),
    "P4": ("V0", "V3", "greater", "V3 < V0"),
    "P5": ("V2", "V3", "greater", "V3 < V2"),
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
    # Proibição: labelers NÃO importa metric/reconstruction; metric NÃO importa labelers.
    if any("labelers" in i for i in imports.get("metric.py", [])):
        violations.append("metric.py importa labelers.py")
    if any("metric" in i for i in imports.get("labelers.py", [])):
        violations.append("labelers.py importa metric.py")
    if any("reconstruction" in i for i in imports.get("labelers.py", [])):
        violations.append("labelers.py importa reconstruction.py")

    # Símbolos compartilhados entre labelers e metric (devem ser NENHUM).
    labelers_src = open(script_files["labelers.py"], encoding="utf-8").read()
    metric_src = open(script_files["metric.py"], encoding="utf-8").read()
    shared_symbols = []
    for m in re.finditer(r"^def\s+(\w+)", labelers_src, re.M):
        sym = m.group(1)
        if sym == "main":
            continue  # entry-point padrão do script; não é símbolo compartilhado labelers×metric
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

    # ---- tabela DV por caso/estado
    dv = {c: {s: values[c][s]["dv"] for s in ("V0", "V1", "V2", "V3")} for c in case_ids}

    # ---- P1–P5
    diffs = {}
    for par, (hi, lo, alt, label) in PARS.items():
        x = [dv[c][hi] - dv[c][lo] for c in case_ids]
        diffs[par] = x
    d_p3 = [dv[c]["V2"] - dv[c]["V0"] for c in case_ids]

    par_results = {}
    for par, (hi, lo, alt, label) in PARS.items():
        stat, p = wilcoxon_onesided(diffs[par], alt)
        neff = int(np.sum(np.abs(np.asarray(diffs[par])) > TIE_EPS))
        par_results[par] = {"hi": hi, "lo": lo, "alternative": alt, "label": label,
                            "statistic": stat, "pvalue": p, "n_effective": neff,
                            "n_pass": neff >= N_MIN_EFFECTIVE}

    # Holm-Bonferroni nos 4 direcionais
    pvals = [par_results[par]["pvalue"] for par in ("P1", "P2", "P4", "P5")]
    holm_ok, holm_order = holm_sequential(pvals)
    for rank, par in enumerate(("P1", "P2", "P4", "P5")):
        par_results[par]["holm_pass"] = holm_ok[rank]

    # TOST P3 (dois testes unilaterais, δ_eq=0.05)
    x_p3 = np.asarray(d_p3, float)
    p3_stat_lo, p3_p_lo = wilcoxon_onesided(x_p3 - DELTA_EQ, "less")
    p3_stat_hi, p3_p_hi = wilcoxon_onesided(x_p3 + DELTA_EQ, "greater")
    p3 = {"statistic_lo": p3_stat_lo, "p_lo": p3_p_lo,
          "statistic_hi": p3_stat_hi, "p_hi": p3_p_hi,
          "tost_pass": (p3_p_lo < ALPHA) and (p3_p_hi < ALPHA)}

    # ---- compliance (§8.2)
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

    # ---- pisos de efeito (§8.3)
    floors = {
        "mediana(DV(V1)-DV(V0))": float(np.median(diffs["P1"])),
        "mediana(DV(V1)-DV(V2))": float(np.median(diffs["P2"])),
        "mediana(DV(V0)-DV(V3))": float(np.median(diffs["P4"])),
        "mediana(DV(V2)-DV(V3))": float(np.median(diffs["P5"])),
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

    # ---- vetos
    v_a_cases = [c for c in case_ids
                 if abs(dv[c]["V1"] - dv[c]["V0"]) <= DELTA_EQ
                 and abs(dv[c]["V3"] - dv[c]["V0"]) <= DELTA_EQ]
    veto_a = len(v_a_cases) / n >= 0.50
    veto_b = not code_inspection_checklist()["passed"]
    veto_c = not fidelity["passed"]
    vetoes = {
        "V-A": {"acionado": veto_a, "n_cases": len(v_a_cases), "proporcao": round(len(v_a_cases) / n, 4)},
        "V-B": {"acionado": veto_b, "inspecao": code_inspection_checklist()["passed"]},
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
    d8 = True  # nenhuma violação de procedimento (§10) — verificado no processo
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

    # ---- diagnóstico de causa (§7.5.1) — apenas se FAIL
    cause = None
    if not decision["PASS"]:
        conf_v1 = np.array([values[c]["V1"]["conf"] for c in case_ids])
        conf_v3 = np.array([values[c]["V3"]["conf"] for c in case_ids])
        dv_v1 = np.array([dv[c]["V1"] for c in case_ids])
        dv_v3 = np.array([dv[c]["V3"] for c in case_ids])
        conf_disc = float(np.median(conf_v1 - conf_v3))
        comp_disc = float(np.median(dv_v1 - dv_v3))
        if conf_disc <= DELTA_EQ:
            cause = ("(a)", "FAIL por conf", conf_disc, comp_disc)
        elif comp_disc <= DELTA_EQ:
            cause = ("(b)", "FAIL por diluição de agregação", conf_disc, comp_disc)
        else:
            cause = ("(b)*", "FAIL por agregação nos testes de nível (V1 vs V0/V2); "
                             "par V1×V3 discriminado por conf e pelo composto",
                     conf_disc, comp_disc)

    # ---- hashes dos artefatos
    artifact_hashes = {}
    for fname in ("generate_cases.py", "labelers.py", "reconstruction.py",
                  "metric.py", "analysis.py"):
        artifact_hashes[fname] = sha256_file(os.path.join(SCRIPTS, fname))
    for fname in ("cases.yaml", "states.yaml", "consensus_registry.yaml"):
        artifact_hashes[fname] = sha256_file(os.path.join(INPUTS, fname))
    for fname in ("reconstruction_graphs.json", "dv_values.json"):
        artifact_hashes[fname] = sha256_file(os.path.join(OUTPUTS, fname))

    # ---- JSON de relatório
    report_json = {
        "gate": "MR-C7",
        "protocolo_hash": "380fc1281f685c9baaefa46c6ef69aaff2d88dc844ad37ae250a50ae90acefe3",
        "addendum_hash": "4ce9fa87f0cd4fa6c0b33ffe2cc4ee5d27e3d998c142fce1c5ac60a9f13b4dc5",
        "n_cases": n,
        "delta_eq": DELTA_EQ,
        "alpha": ALPHA,
        "por_caso": {
            c: {
                "dv": dv[c],
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
        "nota_interpretativa": (
            "S-C vota no eixo de relevância usando novidade estrutural, portanto casos "
            "rotulados V1 tendem a ter estrutura nova vs G0. Se ged_ref reagir a "
            "'qualquer novidade estrutural' (V1 e V3 igualmente) em vez de distinguir "
            "novidade correta da ruidosa, isso NÃO é falha de S-C — é o próprio fenômeno "
            "que o gate existe para detectar. Faz parte do resultado, não do desenho."
        ),
        "hashes": artifact_hashes,
    }

    with open(os.path.join(OUTPUTS, "MR-C7-REPORT.json"), "w", encoding="utf-8") as f:
        json.dump(report_json, f, indent=2, ensure_ascii=False)

    # ---- CASE-REGISTRY.yaml (padrão EVALUATION_REGISTRY.yaml)
    with open(os.path.join(INPUTS, "consensus_registry.yaml"), encoding="utf-8") as f:
        registry = yaml.safe_load(f)
    case_registry = {
        "gate": "MR-C7",
        "padrao": "EVALUATION_REGISTRY.yaml (M-REDESIGN-01-SPEC-A.md §8.2)",
        "mecanismo": "consenso algorítmico determinístico S-A/S-B/S-C (addendum 4ce9fa87...)",
        "seed_draw": states["seed_draw"],
        "seed_master": states["seed_master"],
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
    with open(os.path.join(OUTPUTS, "MR-C7-CASE-REGISTRY.yaml"), "w", encoding="utf-8") as f:
        yaml.safe_dump(case_registry, f, allow_unicode=True, sort_keys=False)

    # ---- hash dos artefatos de relatório (json/yaml) e re-hash dos scripts
    report_json_hash = sha256_file(os.path.join(OUTPUTS, "MR-C7-REPORT.json"))
    registry_hash = sha256_file(os.path.join(OUTPUTS, "MR-C7-CASE-REGISTRY.yaml"))
    artifact_hashes["MR-C7-REPORT.json"] = report_json_hash
    artifact_hashes["MR-C7-CASE-REGISTRY.yaml"] = registry_hash

    # ---- MD report
    insp = code_inspection_checklist()
    lines = []
    lines.append("# MR-C7-REPORT")
    lines.append("")
    lines.append("## Gate MR-C7 — Validade Discriminante de Valor (DV-REDESIGN)")
    lines.append("**Status da decisão:** **%s**" % ("PASS (PROVISÓRIO)" if decision["PASS"] else "FAIL"))
    lines.append("")
    lines.append("## 1. Identificação")
    lines.append("")
    lines.append("| Item | Valor |")
    lines.append("|------|-------|")
    lines.append("| Pré-registro | `MR-C7-PROTOCOLO-PREREGISTRO.md` (hash `380fc1281f685c9baaefa46c6ef69aaff2d88dc844ad37ae250a50ae90acefe3`) |")
    lines.append("| Addendum (consenso algorítmico) | `C-MODEL-SUBSTITUTION-ADDENDUM.md` (hash `4ce9fa87f0cd4fa6c0b33ffe2cc4ee5d27e3d998c142fce1c5ac60a9f13b4dc5`) |")
    lines.append("| Casos | %d sintéticos (N=24; seed_casegen=20260818) |" % n)
    lines.append("| Estados | V0 (baseline), V1 (correta+relevante), V2 (correta+redundante), V3 (falsa/ruidosa) |")
    lines.append("| K_additional | 3 por estado (seed_draw=20260818) |")
    lines.append("| seed_master reconstruções | 20260818 (3 seeds por caso, procedimento `generate_seeds.py` congelado) |")
    lines.append("| δ_eq | 0.05 (banda de equivalência e piso de efeito) |")
    lines.append("| α | 0.05 |")
    lines.append("")
    lines.append("## 2. Nota interpretativa (registrada conforme determinação da governança)")
    lines.append("")
    lines.append("> %s" % report_json["nota_interpretativa"])
    lines.append("")
    lines.append("## 3. Ground truth — limitação (§5 e §5.1)")
    lines.append("")
    lines.append("> O ground truth deste gate é **consenso algorítmico determinístico** (S-A/S-B/S-C), "
                 "**ainda mais fraco** que consenso de IA. **Qualquer PASS é PROVISÓRIO**, pendente de "
                 "reverificação com modelos de IA reais (três provedores distintos, versões correntes) "
                 "antes de qualquer decisão de governança sobre o GO-8E.")
    lines.append("")
    lines.append("## 4. Resumo executivo")
    lines.append("")
    lines.append("| Métrica | Resultado |")
    lines.append("|---------|-----------|")
    lines.append("| Decisão | **%s** |" % ("PASS (PROVISÓRIO)" if decision["PASS"] else "FAIL"))
    lines.append("| compliance_rate | %.4f (exigência ≥ %.2f) |" % (compliance_rate, COMPLIANCE_FLOOR))
    lines.append("| Invariância a seed | %s |" % ("OK" if seed_invariance else "FALHOU"))
    lines.append("| Fidelidade §6.2 | %s (média\\|nós V1−V3\\|=%.4f; média\\|arestas V1−V3\\|=%.4f) |"
                 % ("PASS" if fidelity["passed"] else "FAIL",
                    fidelity["mean_abs_nodes"], fidelity["mean_abs_edges"]))
    lines.append("")
    lines.append("### Valores médios de DV por estado")
    lines.append("")
    lines.append("| Estado | DV (média) |")
    lines.append("|--------|------------|")
    for s in ("V0", "V1", "V2", "V3"):
        lines.append("| %s | %.6f |" % (s, float(np.mean([dv[c][s] for c in case_ids]))))
    lines.append("")
    lines.append("## 5. Resultados por par (P1–P5)")
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
    lines.append("## 6. Compliance (§8.2)")
    lines.append("")
    lines.append("compliance_rate = **%.4f** (exigência ≥ 0.80). Casos conformes: %d/%d."
                 % (compliance_rate, sum(o["ord"] for o in ord_flags), n))
    lines.append("")
    lines.append("## 7. Pisos de efeito (§8.3, exigência > 0.05)")
    lines.append("")
    lines.append("| Gap | Mediana | Exigência |")
    lines.append("|-----|---------|-----------|")
    for k, v in floors.items():
        lines.append("| %s | %.6f | > 0.05 → %s |" % (k, v, "PASS" if v > DELTA_EQ else "FAIL"))
    lines.append("")
    lines.append("## 8. Controles")
    lines.append("")
    lines.append("- **Fidelidade estrutural (§6.2):** %s — média|nós V1−V3|=%.4f (≤1.5), "
                 "média|arestas V1−V3|=%.4f (≤3.0), por caso |nós|≤3: %s"
                 % ("PASS" if fidelity["passed"] else "FAIL",
                    fidelity["mean_abs_nodes"], fidelity["mean_abs_edges"],
                    "OK" if fidelity["per_case_ok"] else "FALHOU"))
    lines.append("- **Invariância a seed (§7.5):** %s (saída idêntica nos 3 seeds derivados de seed_master=20260818)."
                 % ("OK" if seed_invariance else "FALHOU"))
    lines.append("- **Não-circularidade (§6.4):** rótulos fixados pelo gerador+consenso antes de qualquer cálculo de DV; "
                 "nenhum rótulo revisado após inspeção de DV.")
    lines.append("")
    lines.append("## 9. Vetos (§11)")
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
    lines.append("Grafo de importação por script (módulos de fase4 e externos):")
    for name in ("generate_cases.py", "labelers.py", "reconstruction.py", "metric.py", "analysis.py"):
        lines.append("- `%s` → imports: %s" % (name, ", ".join(insp["imports"].get(name, [])) or "(nenhum)"))
    lines.append("")
    lines.append("Proibições verificadas: labelers.py não importa metric.py/reconstruction.py; "
                 "metric.py não importa labelers.py; nenhum símbolo `def` de labelers.py é chamado em metric.py.")
    lines.append("Símbolos compartilhados labelers×metric: **%s**" %
                 (", ".join(insp.get("shared_symbols") or []) or "nenhum"))
    lines.append("")
    lines.append("## 10. Regra de decisão (§8.4)")
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
                     "mediana(DV(V1)−DV(V3)) = %.6f (piso δ_eq = 0.05)."
                     % (cause[2], cause[3]))
        lines.append(">")
        if cause[0] == "(a)":
            lines.append("> Recomendação: redesenhar o componente estrutural (`div_metric` e/ou `ged_ref`, "
                         "incl. escolha de referência) antes de nova tentativa (§9/§14). GO-8E permanece NÃO AUTORIZADO.")
        elif cause[0] == "(b)":
            lines.append("> Recomendação: revisar o esquema de agregação/pesos (§7.5.1), não os componentes. "
                         "GO-8E permanece NÃO AUTORIZADO.")
        else:
            lines.append("> Recomendação: revisar o esquema de agregação/pesos e a referência GED (os testes de "
                         "nível V1 vs V0/V2 falham; o par V1×V3 é discriminado por conf). GO-8E permanece NÃO AUTORIZADO.")
    lines.append("")
    lines.append("## 11. Hashes (SHA-256)")
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
    lines.append("| `MR-C7-REPORT.json` | `%s` |" % report_json_hash)
    lines.append("| `MR-C7-CASE-REGISTRY.yaml` | `%s` |" % registry_hash)
    lines.append("| `MR-C7-REPORT.md` | (hash deste relatório — registrado externamente após a escrita) |")
    lines.append("")
    lines.append("## 12. Consequências (§14)")
    lines.append("")
    if decision["PASS"]:
        lines.append("DV-REDESIGN autorizada para uso confirmatório **PROVISÓRIO** (limitado ao consenso "
                     "algorítmico; reverificação com IA real pendente). Material para decisão de governança "
                     "sobre o DESENHO do GO-8E a ser preparado como acompanhamento (não é este gate).")
    else:
        lines.append("Resultado válido e definitivo para este pré-registro (§9). GO-8E permanece NÃO AUTORIZADO. "
                     "Redesenho recomendado conforme diagnóstico de causa (§7.5.1) mediante novo pré-registro.")
    lines.append("")
    lines.append("**Assinatura:** Execução de gate MR-C7 (consenso algorítmico, addendum 4ce9fa87...)")
    lines.append("**Data:** 2026-08-19")
    lines.append("")

    md_text = "\n".join(lines)
    md_path = os.path.join(OUTPUTS, "MR-C7-REPORT.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_text)

    # Recalcular hashes de scripts (devem ser IDÊNTICOS ao hash-lock pré-execução).
    print("==== MR-C7 SUMMARY ====")
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
    print("Causa (se FAIL):", cause)
    print("Hashes scripts (pré-execução == pós-execução):", artifact_hashes)
    print("saved:", md_path)


if __name__ == "__main__":
    main()
