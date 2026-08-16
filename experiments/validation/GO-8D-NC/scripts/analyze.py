# -*- coding: utf-8 -*-
"""
GO-8D-NC — Statistical analysis executor (pre-registration v1.0 FINAL §4, hierarchy).

Hypothesis hierarchy (governance decision, 2026-08-15):
  PRIMARY   : superiority B < A  -> Friedman (omnibus) + Wilcoxon B-A (+Holm)
  SECONDARY : TOST A-C with Delta=0.05 (equivalence) — interpreted only if primary done
  COMPLEMENTARY: Wilcoxon B-C (informative)

Go/No-Go by valid-BIP count (pre-registration §5.1):
  N_válidos >= 27 -> GO (confirmatory); 10-26 -> NO-GO (exploratory); <10 -> STOP.
DV3 cell = median of 3 seeds. seed_statistics isolated stream (derived, documented in
SEED-MASTER-DECISION.md; not the study master).
"""
import os
import json
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import rankdata

ALPHA = 0.05
BOOT_B = 10_000
DELTA = 0.05
COND = ["A", "B", "C"]
GO_MIN = 27
NOGO_MIN = 10

HERE = os.path.dirname(os.path.abspath(__file__))
STUDY_OUT = os.path.dirname(HERE)
CSV = os.path.join(STUDY_OUT, "study-output", "pilot_results_newcycle.csv")
OUT_JSON = os.path.join(STUDY_OUT, "study-output", "stats_newcycle.json")

SEED_STATISTICS = int(np.random.SeedSequence(20260816, spawn_key=(999,)).generate_state(1)[0])
rng = np.random.default_rng(SEED_STATISTICS)


def signed_rank_biserial(x, y):
    d = np.asarray(y) - np.asarray(x)
    nz = d[d != 0]
    if nz.size == 0:
        return float("nan")
    ranks = rankdata(np.abs(nz), method="average")
    wp = float(ranks[nz > 0].sum()); wm = float(ranks[nz < 0].sum())
    return (wp - wm) / (wp + wm) if (wp + wm) > 0 else float("nan")


def cliff_delta(x, y):
    x = np.asarray(x, float); y = np.asarray(y, float)
    gt = (x[:, None] > y[None, :]).sum()
    lt = (x[:, None] < y[None, :]).sum()
    return (gt - lt) / (x.size * y.size)


def holm(pvals, keys):
    n = len(keys)
    order = sorted(keys, key=lambda k: pvals[k])
    rejected = {}
    for i, key in enumerate(order):
        p = pvals[key]
        if np.isnan(p):
            rejected[key] = False
            continue
        if p <= ALPHA / (n - i):
            rejected[key] = True
        else:
            rejected[key] = False
            for later in order[i + 1:]:
                rejected[later] = False
            break
    return rejected


def exact_median_ci(vals):
    v = np.sort(np.asarray(vals, float))
    n = len(v)
    z = 1.959963984540054
    l = max(0, int(np.floor((n - z * np.sqrt(n)) / 2.0)) - 1)
    u = min(n - 1, int(np.ceil((n + z * np.sqrt(n)) / 2.0)) - 1)
    return float(v[l]), float(v[u])


def boot_paired_ci(x, y, metric, B=BOOT_B):
    x = np.asarray(x, float); y = np.asarray(y, float)
    n = len(x)
    vals = np.empty(B)
    for i in range(B):
        idx = rng.integers(0, n, size=n)
        if metric == "median_diff":
            vals[i] = np.median(y[idx]) - np.median(x[idx])
        elif metric == "cliff":
            vals[i] = cliff_delta(x[idx], y[idx])
        elif metric == "rrb":
            vals[i] = signed_rank_biserial(x[idx], y[idx])
        elif metric == "mean_diff":
            vals[i] = np.mean(y[idx]) - np.mean(x[idx])
    return float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))


def friedman_analysis(mat):
    chi2, p = stats.friedmanchisquare(*[mat[:, j] for j in range(3)])
    n, k = mat.shape
    w = chi2 / (n * (k - 1)) if n * (k - 1) > 0 else float("nan")
    ranks = pd.DataFrame(mat).rank(axis=1).to_numpy(float)
    wb = np.empty(BOOT_B)
    for i in range(BOOT_B):
        idx = rng.integers(0, n, size=n)
        rj = ranks[idx, :].sum(axis=0)
        chi2b = (12.0 / (n * k * (k + 1))) * float((rj**2).sum()) - 3.0 * n * (k + 1)
        wb[i] = chi2b / (n * (k - 1))
    ci = (float(np.percentile(wb, 2.5)), float(np.percentile(wb, 97.5)))
    return chi2, float(p), w, ci


# ---------------- load + aggregate ----------------
df = pd.read_csv(CSV)
df = df[df["status"] == "PASS"].copy()
df["dv"] = df["dv3"].astype(float)
assert df["dv"].between(0, 1).all(), "DV outside [0,1]"

bips_all = ["BIP-%03d" % i for i in range(1, 31)]
valid_bips = [b for b in bips_all
              if len(df[(df.bip_id == b)]) == 9]
N = len(valid_bips)

print("== GO/NO-GO ==")
print("  valid_bips=%d (>=27 GO, 10-26 NO-GO, <10 STOP)" % N)
if N >= GO_MIN:
    mode = "GO"
elif N >= NOGO_MIN:
    mode = "NO-GO (exploratorio)"
else:
    mode = "STOP"
print("  decision:", mode)

agg = df[df.bip_id.isin(valid_bips)].groupby(["bip_id", "condition"])["dv"].median().reset_index()
mat = np.zeros((N, 3))
for i, b in enumerate(valid_bips):
    for j, c in enumerate(COND):
        mat[i, j] = agg[(agg["bip_id"] == b) & (agg["condition"] == c)]["dv"].iloc[0]

print("cases=%d rows=%d conditions=%s" % (N, len(df), COND))
print("alpha=%s bootstrap_B=%d seed_statistics=%d delta=%s" % (ALPHA, BOOT_B, SEED_STATISTICS, DELTA))

desc = {}
print("\n== DESCRIPTIVE (per condition) ==")
for j, c in enumerate(COND):
    v = mat[:, j]
    em = exact_median_ci(v)
    q1, q3 = np.percentile(v, [25, 75])
    desc[c] = {"median": float(np.median(v)), "ci_exact": em,
               "iqr": [float(q1), float(q3)], "min": float(v.min()), "max": float(v.max())}
    print("  cond %s: median=%.4f exactCI=[%.4f,%.4f] IQR=[%.4f,%.4f] min=%.4f max=%.4f" %
          (c, desc[c]["median"], em[0], em[1], q1, q3, v.min(), v.max()))

report = {"N": N, "rows": int(len(df)), "mode": mode, "alpha": ALPHA,
          "bootstrap_B": BOOT_B, "seed_statistics": SEED_STATISTICS, "delta": DELTA,
          "descriptive": desc, "matrix": mat.round(6).tolist()}

# ---------------- hierarchy: primary -> secondary -> complementary ----------------
pairs = [("A", "B"), ("A", "C"), ("B", "C")]

if mode == "GO":
    # PRIMARY: omnibus
    print("\n== PRIMARIA — OMNIBUS (Friedman df=2) ==")
    chi2, p_f, w, w_ci = friedman_analysis(mat)
    sig = p_f < ALPHA
    print("  chi2_F=%.4f p=%.6f W=%.4f [CI (%.4f,%.4f)] decision=%s" %
          (chi2, p_f, w, w_ci[0], w_ci[1], "REJECT" if sig else "NO REJECTION"))
    report["primary_friedman"] = {"chi2": chi2, "df": 2, "p": p_f, "kendall_W": w,
                                  "W_ci": list(w_ci), "reject": sig}

    # PRIMARY: Wilcoxon B-A + Holm
    print("\n== PRIMARIA — POST-HOC WILCOXON + HOLM ==")
    pvals = {}; rrb = {}; cd = {}; mdiff_ci = {}
    for (a, b) in pairs:
        x = mat[:, COND.index(a)]; y = mat[:, COND.index(b)]
        try:
            _, p = stats.wilcoxon(x, y, alternative="two-sided", correction=True)
        except ValueError:
            p = float("nan")
        pvals["%s-%s" % (a, b)] = float(p)
        rrb["%s-%s" % (a, b)] = signed_rank_biserial(x, y)
        cd["%s-%s" % (a, b)] = cliff_delta(x, y)
        mdiff_ci["%s-%s" % (a, b)] = boot_paired_ci(x, y, "mean_diff")
    keys = list(pvals.keys())
    rejected = holm(pvals, keys)
    for k in keys:
        mark = "REJECT" if rejected[k] else "not rej."
        print("  %s vs %s: p=%.4f [%s] r_rb=%.3f Cliff=%.3f meanDiffCI=(%.3f,%.3f)" %
              (k[0], k[2], pvals[k], mark, rrb[k], cd[k], mdiff_ci[k][0], mdiff_ci[k][1]))
    report["posthoc"] = {k: {"p": pvals[k], "r_rb": rrb[k], "cliff_delta": cd[k],
                             "mean_diff_ci": list(mdiff_ci[k]), "holm_reject": rejected[k]}
                         for k in keys}

    # SECONDARY: TOST A-C (Delta=0.05)
    print("\n== SECUNDARIA — TOST A-C (Delta=0.05) ==")
    x = mat[:, 0]; y = mat[:, 2]
    lo, hi = mdiff_ci["A-C"]
    eq = lo > -DELTA and hi < DELTA
    tost_ac = {"mean_diff": float(np.mean(y) - np.mean(x)), "ci": [lo, hi],
               "delta": DELTA, "equivalent": eq}
    print("  A-C: meanDiff=%.4f CI95%%=(%.4f,%.4f) delta=%.3f -> %s" %
          (tost_ac["mean_diff"], lo, hi, DELTA, "EQUIVALENT" if eq else "not equivalent"))
    report["tost_A_C"] = tost_ac

    # COMPLEMENTARY: B-C
    print("\n== COMPLEMENTAR — B vs C ==")
    xb = mat[:, 1]; yc = mat[:, 2]
    try:
        _, p_bc = stats.wilcoxon(xb, yc, alternative="two-sided", correction=True)
    except ValueError:
        p_bc = float("nan")
    print("  B-C: p=%.4f r_rb=%.3f Cliff=%.3f" % (p_bc, signed_rank_biserial(xb, yc), cliff_delta(xb, yc)))
    report["complementar_B_C"] = {"p": float(p_bc),
                                  "r_rb": signed_rank_biserial(xb, yc),
                                  "cliff_delta": cliff_delta(xb, yc)}

    # sensitivity (STAT-04 no winsorize; STAT-09 drop 1 case)
    print("\n== SENSITIVIDADE ==")
    p_drops = {}
    for drop in range(N):
        keep = np.ones(N, bool); keep[drop] = False
        c2, p2, w2, _ = friedman_analysis(mat[keep])
        p_drops[valid_bips[drop]] = float(p2)
    report["sensitivity"] = {"drops": p_drops}
    print("  drop-1 Friedman p range: [%.4f, %.4f]" % (min(p_drops.values()), max(p_drops.values())))
    print("  NO mixed model (STAT-09 excluded). No winsorization (STAT-04).")
else:
    print("\n== MODO != GO: apenas relatorio exploratorio/descritivo ==")
    report["posthoc"] = None
    report["tost_A_C"] = None
    report["note"] = ("NO-GO/STOP: sem analise inferencial de decisao. "
                      "Apenas descritivos (ICs) e efeitos, sem testes confirmatorios.")

os.makedirs(STUDY_OUT, exist_ok=True)
json.dump(report, open(OUT_JSON, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("\nsaved:", OUT_JSON)
