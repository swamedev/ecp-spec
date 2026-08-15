# -*- coding: utf-8 -*-
"""GO-8D D-07 — power under task-stated effects (paired diffs A-B=0.079, B-C=0.069).
MU set so paired effects match the task; sigma_e from both empirical and conservative."""
import json
import numpy as np
from scipy.stats import friedmanchisquare, wilcoxon

ROWS = json.load(open(r"D:\ecp-spec\experiments\validation\GO-8D\analysis\redesign_cells.json",
                      encoding="utf-8"))
rng = np.random.default_rng(20260814)


def zclip(x):
    return max(0.0, min(1.0, x))


def dv(row):
    return (row["conf"] + zclip(row["ged_ref"]) + row["ent"]) / 3.0


BIPS = ["BIP-%03d" % i for i in range(1, 13)]
MAT = np.array([[dv(r) for r in ROWS if r["bip"] == b] for b in BIPS])
MED = np.median(MAT, axis=0)
SIGMA_B = MAT.mean(axis=1).std(ddof=1)
dBC = (MAT[:, 1] - MAT[:, 2]).std(ddof=1)
SIGMA_E_BC = dBC / np.sqrt(2.0)
SIGMA_E_EMP = np.sqrt(np.mean([np.var(MAT[i] - MED) for i in range(12)]))
SIGMA_S = 0.002

A0 = MED[0]
MU_TASK = np.array([A0, A0 - 0.079, A0 - 0.079 + 0.069])  # A-B=0.079, B-C=0.069, A-C=0.010
print("Task-stated effects: A-B=0.079, B-C=0.069, A-C=0.010")
print("MU =", np.round(MU_TASK, 4), " sb=%.4f se_emp=%.4f se_BC=%.4f" %
      (SIGMA_B, SIGMA_E_EMP, SIGMA_E_BC))


def gen_one(N, se, mu):
    b = rng.normal(0.0, SIGMA_B, size=N)
    lat = mu[None, :] + b[:, None] + rng.normal(0.0, se, size=(N, 3))
    seeds = rng.normal(0.0, SIGMA_S, size=(N, 3, 3)) + lat[:, :, None]
    return np.clip(np.median(seeds, axis=2), 0.0, 1.0)


def wilcox_p(x, y):
    d = np.asarray(x) - np.asarray(y)
    d = d[d != 0.0]
    if len(d) < 3:
        return 1.0
    return wilcoxon(d, alternative="two-sided").pvalue


def tost_equiv_vec(x, y, delta, B=400):
    d = np.asarray(x) - np.asarray(y)
    n = len(d)
    idx = rng.integers(0, n, size=(B, n))
    boot = d[idx].mean(axis=1)
    lo, hi = np.percentile(boot, [2.5, 97.5])
    return lo > -delta and hi < delta


N_GRID = [8, 10, 12, 14, 16, 18]
REPS = 3000
out = {}
for se_name, se in [("emp", SIGMA_E_EMP), ("BC", SIGMA_E_BC)]:
    for N in N_GRID:
        c_f = c_ab = c_bc = c_ac = c_eq_ac = 0
        for _ in range(REPS):
            M = gen_one(N, se, MU_TASK)
            if friedmanchisquare(M[:, 0], M[:, 1], M[:, 2])[1] < 0.05:
                c_f += 1
            ps = [wilcox_p(M[:, 0], M[:, 1]), wilcox_p(M[:, 1], M[:, 2]), wilcox_p(M[:, 0], M[:, 2])]
            order = sorted(range(3), key=lambda k: ps[k])
            sig = [False, False, False]
            for i, k in enumerate(order):
                if ps[k] <= 0.05 / (3 - i):
                    sig[k] = True
                else:
                    break
            c_ab += sig[0]; c_bc += sig[1]; c_ac += sig[2]
            if tost_equiv_vec(M[:, 0], M[:, 2], 0.05):  # A-C true effect 0.010 < Delta
                c_eq_ac += 1
        out[(se_name, N)] = {"friedman": c_f/REPS, "AB": c_ab/REPS, "BC": c_bc/REPS,
                             "AC": c_ac/REPS, "tost_equiv_AC": c_eq_ac/REPS}
        print("se=%s N=%2d F=%.3f AB=%.3f BC=%.3f AC=%.3f eqAC=%.3f" %
              (se_name, N, c_f/REPS, c_ab/REPS, c_bc/REPS, c_ac/REPS, c_eq_ac/REPS), flush=True)

print()
for se_name in ["emp", "BC"]:
    mn = min(N for N in N_GRID if out[(se_name, N)]["BC"] >= 0.80)
    print("Min N (pw B-C >= 0.80) under %s: %d" % (se_name, mn))
print("Executions N x 3 x 3:", {N: N*9 for N in N_GRID})
json.dump({("task_%s_%d" % k): v for k, v in out.items()},
          open(r"D:\ecp-spec\experiments\validation\GO-8D\analysis\d07_power_results_task.json",
               "w", encoding="utf-8"), indent=2)
print("saved: GO-8D/analysis/d07_power_results_task.json")
