# -*- coding: utf-8 -*-
"""D-MV-02: Monte Carlo power for DV3 (frozen). Scenarios: observed, conservative,
minimal-of-interest. Tests: Friedman (omnibus), Wilcoxon+Holm (pair B-A superiority),
TOST Delta=0.05 (equivalence A-C). Unit = BIP (cell = median of seeds).

Model (calibrated on GO-8D DV3, 12 BIPs):
  A_i ~ Normal(mu_A=0.6205, sigma_between=0.0175)
  delta_BA_i ~ Normal(delta_BA, sd_BA=0.0312)
  delta_CA_i ~ Normal(delta_CA, sd_CA=0.0288)
  B_i = A_i + delta_BA_i ; C_i = A_i + delta_CA_i ; clamp [0,1]
"""
import numpy as np
import math
from scipy import stats

RNG = np.random.default_rng(20260814)
N_SIM = 3000
ALPHA = 0.05
DELTA = 0.05
SEED_STAT = 14233797184859982032  # stream de estatística do GO-8D (documentação)

MU_A, SD_A = 0.6205, 0.0175
SD_BA, SD_CA = 0.0312, 0.0288

SCENARIOS = {
    "S1_observado":               {"delta_BA": -0.0374, "delta_CA": -0.0368},
    "S2_conservador":             {"delta_BA": -0.0280, "delta_CA": -0.0280},
    "S3_minimo_interesse":        {"delta_BA": -0.0500, "delta_CA": 0.0000},
}

def clamp(v):
    return max(0.0, min(1.0, v))

def sim_cells(N, delta_BA, delta_CA, rng):
    A = rng.normal(MU_A, SD_A, N)
    dB = rng.normal(delta_BA, SD_BA, N)
    dC = rng.normal(delta_CA, SD_CA, N)
    B = A + dB
    C = A + dC
    A = np.clip(A, 0, 1); B = np.clip(B, 0, 1); C = np.clip(C, 0, 1)
    return A, B, C

def friedman_p(A, B, C):
    mat = np.stack([A, B, C], axis=1)
    chi2, p = stats.friedmanchisquare(mat[:, 0], mat[:, 1], mat[:, 2])
    return p

def wilcoxon_ba_p(A, B):
    # two-sided; signed-rank test H0: median(B-A)=0 ; we want B<A
    try:
        _, p = stats.wilcoxon(B, A, alternative="two-sided")
    except ValueError:
        return np.nan
    return p

def tost_ac_equivalent(A, C, delta=DELTA):
    """Two one-sided paired t-tests. Equivalent if |mean diff| < delta and both
    one-sided tests reject at alpha."""
    d = A - C
    n = len(d)
    m = d.mean(); s = d.std(ddof=1)
    se = s / math.sqrt(n) if n > 1 else np.inf
    if se == 0 or np.isinf(se) or np.isnan(se):
        return False
    t_lo = (m - (-delta)) / se   # H0: mean <= -delta  (test mean > -delta)
    t_hi = (delta - m) / se      # H0: mean >= +delta  (test mean < +delta)
    # upper-tail tests at alpha
    ok_lo = t_lo > stats.t.ppf(1 - ALPHA, n - 1)
    ok_hi = t_hi > stats.t.ppf(1 - ALPHA, n - 1)
    return bool(ok_lo and ok_hi)

def run_power(N, delta_BA, delta_CA):
    pow_f = pow_w = pow_tost = 0
    for _ in range(N_SIM):
        A, B, C = sim_cells(N, delta_BA, delta_CA, RNG)
        if friedman_p(A, B, C) < ALPHA:
            pow_f += 1
        p_ba = wilcoxon_ba_p(A, B)
        if not np.isnan(p_ba) and p_ba < ALPHA:
            pow_w += 1
        if tost_ac_equivalent(A, C):
            pow_tost += 1
    return pow_f / N_SIM, pow_w / N_SIM, pow_tost / N_SIM

NS = [6, 8, 10, 12, 14, 16, 18, 20, 24, 30, 36, 48]
print("=== D-MV-02 POWER (DV3) — power>=0.80 target ===\n")
results = {}
for sname, sc in SCENARIOS.items():
    print("## %s (delta_BA=%.4f, delta_CA=%.4f)" % (sname, sc["delta_BA"], sc["delta_CA"]))
    print("   %4s | %9s | %11s | %9s |" % ("N", "Friedman", "WilcoxonBA", "TOST A-C"))
    rows = []
    for N in NS:
        pf, pw, pt = run_power(N, sc["delta_BA"], sc["delta_CA"])
        rows.append({"N": N, "friedman": pf, "wilcoxon_BA": pw, "tost_AC": pt})
        print("   %4d | %9.3f | %11.3f | %9.3f |" % (N, pf, pw, pt))
    # minimal N >=0.80
    for metric in ["friedman", "wilcoxon_BA", "tost_AC"]:
        ok = [r for r in rows if r[metric] >= 0.80]
        n_min = ok[0]["N"] if ok else None
        print("   -> min N for %s >=0.80: %s" % (metric, n_min))
    results[sname] = rows
    print()

np.save(r"D:\ecp-spec\experiments\validation\GO-8D\metric-validation\power_dv3_results.npy",
        np.array([[r["N"], r["friedman"], r["wilcoxon_BA"], r["tost_AC"]] for r in results["S1_observado"]], float))
print("saved power_dv3_results.npy (S1)")