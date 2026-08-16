#!/usr/bin/env python3
"""
GO-8B Power Simulation (06-STATISTICAL-PROTOCOL.md, sec. 5)
================================================================
Reproducibility script. Implements the PRE-SPECIFIED Monte Carlo power
simulation registered in Deliverable 06 (R5 M-3) EXACTLY as documented:

  - Test:              scipy.stats.friedmanchisquare (df = k-1 = 2)
  - alpha:             0.05
  - k (conditions):    3 (A = blind-pure, B = blind + C3, C = non-blind)
  - Seeds per cell:    3 seeds per (BIP x condition)
  - Aggregation:       cell_value = median(seed_1, seed_2, seed_3)
  - N grid (BIPs):     5, 6, 7, 8, 9, 10, 12, 14, 16, 20, 28
  - Replications (B):  5000 per N
  - Seed:              20260811 (uint64), isolated stream (06 sec. 9.2)
  - Variability:       sigma_b = 0.12, sigma_e = 0.08, sigma_s = 0.06
  - Scenarios:         S0_NULL (0.55, 0.55, 0.55); S1_PRIMARY (0.50, 0.60, 0.66)

DGM (06 sec. 5.1):
    X_ij   = mu_j + b_i + e_ij        b_i ~ N(0, sigma_b^2); e_ij ~ N(0, sigma_e^2)
    y_ijk  = X_ij + s_ijk             s_ijk ~ N(0, sigma_s^2); k = 1..3
    cell_ij = clip(median(y_ij1..y_ij3), 0, 1)

This is a METHODOLOGICAL simulation: no experimental data, no experimental
observations, and it is NOT the experiment. Deviation from the values
registered in 06 sec. 5.2 must be reported as a governance finding; the
protocol/results are NEVER adjusted to make numbers coincide.

Output: table with N, power (S1_PRIMARY) / type-I error (S0_NULL),
Monte Carlo SE, Wilson 95% CI, mean Kendall's W.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.stats import friedmanchisquare

# --- Configuration (registered, do not edit without a governance decision) ---
SEED: int = 20260811
ALPHA: float = 0.05
N_GRID: list[int] = [5, 6, 7, 8, 9, 10, 12, 14, 16, 20, 28]
B: int = 5000
SIGMA_B: float = 0.12
SIGMA_E: float = 0.08
SIGMA_S: float = 0.06
N_SEEDS: int = 3
S0_NULL: tuple[float, float, float] = (0.55, 0.55, 0.55)
S1_PRIMARY: tuple[float, float, float] = (0.50, 0.60, 0.66)
Z_95: float = 1.959963984540054  # standard normal 97.5% quantile


def wilson_ci(p_hat: float, n: int, z: float = Z_95) -> tuple[float, float]:
    """Wilson 95% interval for a binomial proportion."""
    denom = 1.0 + z**2 / n
    center = (p_hat + z**2 / (2.0 * n)) / denom
    half = z * math.sqrt(p_hat * (1.0 - p_hat) / n + z**2 / (4.0 * n**2)) / denom
    return max(0.0, center - half), min(1.0, center + half)


def run_scenario(
    mu: tuple[float, float, float], n_bips: int, rng: np.random.Generator
) -> tuple[float, float]:
    """One N value, B replications. Returns (rejection rate, mean Kendall's W)."""
    mu_arr = np.asarray(mu, dtype=float)
    k = len(mu_arr)
    rejected = 0
    w_sum = 0.0
    for _ in range(B):
        cells = np.empty((n_bips, k), dtype=float)
        for i in range(n_bips):
            b_i = rng.normal(0.0, SIGMA_B)
            for j in range(k):
                e_ij = rng.normal(0.0, SIGMA_E)
                x_ij = mu_arr[j] + b_i + e_ij
                s_ijk = rng.normal(0.0, SIGMA_S, size=N_SEEDS)
                cells[i, j] = float(np.clip(np.median(x_ij + s_ijk), 0.0, 1.0))
        chi2, p_value = friedmanchisquare(cells[:, 0], cells[:, 1], cells[:, 2])
        w_sum += chi2 / (n_bips * (k - 1))
        if p_value < ALPHA:
            rejected += 1
    return rejected / B, w_sum / B


def main() -> None:
    # Single isolated stream; grid consumed sequentially (one stream, one pass).
    rng = np.random.default_rng(SEED)

    for label, mu in (("S0_NULL", S0_NULL), ("S1_PRIMARY", S1_PRIMARY)):
        print(f"\n=== {label} (mu={mu}) | alpha={ALPHA} | B={B} | seed={SEED} ===")
        print(f"{'N':>4} | {'p_hat':>7} | {'MC SE':>6} | {'Wilson 95% CI':>20} | {'W_mean':>7}")
        for n in N_GRID:
            p_hat, w_mean = run_scenario(mu, n, rng)
            se = math.sqrt(p_hat * (1.0 - p_hat) / B)
            lo, hi = wilson_ci(p_hat, B)
            print(
                f"{n:>4} | {p_hat:>7.3f} | {se:>6.3f} | ({lo:>8.3f}, {hi:>8.3f}) | {w_mean:>7.3f}"
            )


if __name__ == "__main__":
    main()
