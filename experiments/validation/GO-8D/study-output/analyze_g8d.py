# -*- coding: utf-8 -*-
"""
GO-8D — Statistical analysis executor (pre-registration v1.0 §6).
DV_confirm = (conf + ged_ref + ent)/3 (cell = median of 3 seeds).
Plan: data check -> aggregation -> descriptive -> Friedman (df=2, a=0.05) ->
Wilcoxon paired two-sided + Holm-Bonferroni -> effect sizes (Kendall W, r_rb,
Cliff d) -> bootstrap B=10,000 paired percentile CIs + exact median CI (STAT-08)
-> TOST with Delta=0.05 (D-06 approved; equivalence if paired-diff CI subset
(-0.05,+0.05)) -> sensitivity (STAT-04 no winsorize, STAT-09 drop 1 case).
seed_statistics isolated stream from SeedSequence(20260815, spawn_key=(0,)).
"""
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import rankdata
import json

ALPHA = 0.05
BOOT_B = 10_000
SEED_STATISTICS = 14233797184859982032
DELTA = 0.05
COND = ["A", "B", "C"]

rng = np.random.default_rng(SEED_STATISTICS)

# ---------- helpers (mirror GO-8B frozen executor) ----------
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
            rejected[key] = False; continue
        if p <= ALPHA / (n - i):
            rejected[key] = True
        else:
            rejected[key] = False
            for later in order[i+1:]:
                rejected[later] = False
            break
    return rejected

def exact_median_ci(vals):
    """Exact median CI (STAT-08; nonparametric order-statistic CI, coverage ~0.9614)."""
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

# ---------- load + aggregate ----------
df = pd.read_csv(r"D:\ecp-spec\experiments\validation\GO-8D\study-output\pilot_results_g8d.csv")
df = df[df["status"] == "PASS"].copy()
df["dv"] = df["dv_confirm"].astype(float)
assert df["dv"].between(0, 1).all(), "DV outside [0,1]"

# cell = median of 3 seeds
agg = df.groupby(["bip_id", "condition"])["dv"].median().reset_index()
bips = sorted(agg["bip_id"].unique())
N = len(bips)
mat = np.zeros((N, 3))
for i, b in enumerate(bips):
    for j, c in enumerate(COND):
        mat[i, j] = agg[(agg["bip_id"] == b) & (agg["condition"] == c)]["dv"].iloc[0]

print("cases=%d rows=%d conditions=%s" % (N, len(df), COND))
print("alpha=%s bootstrap_B=%d seed_statistics=%d delta=%s" % (ALPHA, BOOT_B, SEED_STATISTICS, DELTA))

# ---------- 1. data check ----------
print("\n== 1. DATA CHECK ==")
print("  missing: %d  range: [%.4f, %.4f]" % (df["dv"].isna().sum(), df["dv"].min(), df["dv"].max()))
cells = df.groupby(["bip_id", "condition"]).size()
print("  completeness 3 seeds/cell: %s" % ("OK" if (cells == 3).all() else "INCOMPLETE"))

# ---------- 2. aggregation ----------
print("\n== 2. AGGREGATION ==")
print("  N (valid BIPs) = %d" % N)

# ---------- 3. descriptive ----------
print("\n== 3. DESCRIPTIVE (per condition) ==")
desc = {}
for j, c in enumerate(COND):
    v = mat[:, j]
    em = exact_median_ci(v)
    q1, q3 = np.percentile(v, [25, 75])
    desc[c] = {"median": float(np.median(v)), "ci_exact": em,
               "iqr": [float(q1), float(q3)], "min": float(v.min()), "max": float(v.max())}
    print("  cond %s: median=%.4f exactCI=[%.4f,%.4f] IQR=[%.4f,%.4f] min=%.4f max=%.4f" %
          (c, desc[c]["median"], em[0], em[1], q1, q3, v.min(), v.max()))
print("  per-case medians (DV_confirm):")
for i, b in enumerate(bips):
    print("    %s: A=%.4f B=%.4f C=%.4f" % (b, mat[i, 0], mat[i, 1], mat[i, 2]))

# ---------- 4. omnibus ----------
print("\n== 4. OMNIBUS — Friedman (df=2) ==")
chi2, p_f, w, w_ci = friedman_analysis(mat)
sig = p_f < ALPHA
print("  chi2_F=%.4f df=2 p=%.6f" % (chi2, p_f))
print("  Kendall W=%.4f [bootstrap 95%% CI: (%.4f, %.4f)]" % (w, w_ci[0], w_ci[1]))
print("  decision: %s" % ("REJECT H0 (p<0.05)" if sig else "NO REJECTION (p>=0.05) -> STOP post-hoc"))

# ---------- 5. post-hoc ----------
pairs = [("A", "B"), ("A", "C"), ("B", "C")]
if sig:
    print("\n== 5. POST-HOC — Wilcoxon paired two-sided + Holm ==")
    pvals = {}; rrb = {}; cd = {}; med_ci = {}; mdiff_ci = {}; cliff_ci = {}
    for (a, b) in pairs:
        x = mat[:, COND.index(a)]; y = mat[:, COND.index(b)]
        try:
            _, p = stats.wilcoxon(x, y, alternative="two-sided", correction=True)
        except ValueError:
            p = float("nan")
        pvals["%s-%s" % (a, b)] = float(p)
        rrb["%s-%s" % (a, b)] = signed_rank_biserial(x, y)
        cd["%s-%s" % (a, b)] = cliff_delta(x, y)
        med_ci["%s-%s" % (a, b)] = boot_paired_ci(x, y, "median_diff")
        mdiff_ci["%s-%s" % (a, b)] = boot_paired_ci(x, y, "mean_diff")
        cliff_ci["%s-%s" % (a, b)] = boot_paired_ci(x, y, "cliff")
    keys = list(pvals.keys())
    rejected = holm(pvals, keys)
    for k in keys:
        mark = "REJECT" if rejected[k] else "not rej."
        print("  %s vs %s: p=%.4f [%s] r_rb=%.3f Cliff=%.3f medDiffCI=(%.3f,%.3f) meanDiffCI=(%.3f,%.3f) cliffCI=(%.3f,%.3f)" %
              (k[0], k[2], pvals[k], mark, rrb[k], cd[k], med_ci[k][0], med_ci[k][1],
               mdiff_ci[k][0], mdiff_ci[k][1], cliff_ci[k][0], cliff_ci[k][1]))
    print("  Holm thresholds: %s" % {k: ("%.4f" % (ALPHA / (3 - i))) for i, k in enumerate(sorted(keys, key=lambda kk: pvals[kk]))})

# ---------- 6. TOST (Delta=0.05, D-06) ----------
print("\n== 6. TOST / EQUIVALENCE (Delta=0.05, D-06 APPROVED) ==")
tost = {}
for (a, b) in pairs:
    x = mat[:, COND.index(a)]; y = mat[:, COND.index(b)]
    lo, hi = mdiff_ci["%s-%s" % (a, b)]
    eq = lo > -DELTA and hi < DELTA
    tost["%s-%s" % (a, b)] = {"mean_diff": float(np.mean(y) - np.mean(x)),
                              "ci": [lo, hi], "delta": DELTA, "equivalent": eq}
    print("  %s vs %s: meanDiff=%.4f CI95%%=(%.4f,%.4f) delta=%.3f -> %s" %
          (a, b, tost["%s-%s" % (a, b)]["mean_diff"], lo, hi, DELTA,
           "EQUIVALENT" if eq else "not equivalent"))

# ---------- 7. sensitivity (STAT-04 no winsorize; STAT-09 drop 1 case) ----------
print("\n== 7. SENSITIVITY ==")
# 7a. without outliers (IQR x 1.5)
out_mask = np.zeros(N, bool)
for j in range(3):
    v = mat[:, j]
    q1, q3 = np.percentile(v, [25, 75]); iqr = q3 - q1
    out_mask |= (v < q1 - 1.5 * iqr) | (v > q3 + 1.5 * iqr)
if out_mask.any():
    keep = ~out_mask
    if keep.sum() >= 3:
        c2, p2, w2, _ = friedman_analysis(mat[keep])
        print("  without outliers (IQR x1.5): N=%d Friedman p=%.4f W=%.4f" % (keep.sum(), p2, w2))
    else:
        print("  without outliers: matrix INCOMPLETE after removal (N=%d)" % keep.sum())
else:
    print("  without outliers: none flagged")
# 7b. domain dependency: no domain metadata in GO-8D; drop each single case (STAT-09 spirit)
p_drops = {}
for drop in range(N):
    keep = np.ones(N, bool); keep[drop] = False
    c2, p2, w2, _ = friedman_analysis(mat[keep])
    p_drops[bips[drop]] = float(p2)
    print("  drop %s -> N=%d Friedman p=%.4f W=%.4f" % (bips[drop], int(keep.sum()), p2, w2))
print("  NO mixed model (STAT-09: explicitly excluded). No winsorization (STAT-04).")

# ---------- report json ----------
report = {
    "N": N, "rows": int(len(df)), "alpha": ALPHA, "bootstrap_B": BOOT_B,
    "seed_statistics": SEED_STATISTICS, "delta": DELTA,
    "descriptive": desc, "friedman": {"chi2": chi2, "df": 2, "p": p_f,
                                       "kendall_W": w, "W_ci": list(w_ci),
                                       "reject": sig},
    "posthoc": {k: {"p": pvals[k], "r_rb": rrb[k], "cliff_delta": cd[k],
                     "med_diff_ci": list(med_ci[k]), "mean_diff_ci": list(mdiff_ci[k]),
                     "cliff_ci": list(cliff_ci[k]), "holm_reject": rejected[k]}
                for k in keys} if sig else None,
    "tost": tost,
    "sensitivity": {"drops": p_drops},
    "matrix": mat.round(6).tolist(),
}
json.dump(report, open(r"D:\ecp-spec\experiments\validation\GO-8D\study-output\stats_g8d.json", "w",
                       encoding="utf-8"), indent=2, ensure_ascii=False)
print("\nsaved: GO-8D/study-output/stats_g8d.json")