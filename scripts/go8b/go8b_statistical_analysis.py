#!/usr/bin/env python3
"""
GO-8B Statistical Analysis Executor (06-STATISTICAL-PROTOCOL.md, sec. 7)
========================================================================
Executes the PRE-REGISTERED analysis plan EXACTLY as specified in Deliverable
06 (no protocol change to accommodate this script):

  1. DATA CHECK          completeness (N x 3), range [0,1], missings
  2. AGGREGATION         cell_value = median of the 3 seeds per (case, condition)
  3. DESCRIPTIVE         median, IQR, min, max per condition and per case
  4. OMNIBUS (Friedman)  chi2_F, df=2, p, Kendall's W + bootstrap 95% CI
                         if p >= 0.05: STOP (no confirmatory post-hoc)
  5. POST-HOC (if sig.)  3 x Wilcoxon signed-rank two-sided; Holm-Bonferroni;
                         r_rb + CI; Cliff's delta as robustness
  6. EXPLORATORY         case x condition description; Spearman S_struct x aux;
                         S_sem diagnostic median (if provided)
  7. SENSITIVITY         re-run Friedman/Wilcoxon WITHOUT outliers (IQR x 1.5);
                         domain dependency: exclude 1 case per dependent pair
                         (Hyatt OR I-35W; Ebola OR Warp Speed) -> 2 runs;
                         NO mixed model
  8. REPORT              consolidated table + narrative fields

Protocol-fixed settings (06):
  - unit: BIP/Case; N = number of valid BIPs (NEVER multiplied)
  - alpha = 0.05 (global and post-hoc family)
  - Friedman = global PRIMARY test; RM-ANOVA, if run, is supplemental only
  - post-hoc: Wilcoxon paired two-sided + Holm; NO unilateral decisions
  - bootstrap: percentile, B = 10_000, PAIRED (resample BIPs)
  - TOST: NOT executed (no delta approved; delta = 0.10 NOT approved)
  - STAT-04: NO winsorization; sensitivity without outliers
  - STAT-09: domain-dependency sensitivity; NO mixed model
  - seed_statistics = 1879048193 (uint64), isolated stream (06 sec. 9.1)

Input : CSV with columns: case_id, condition, value
        (one row per seed observation; 3 seeds per (case, condition))
        Optional columns: aux_value, s_sem  -> used ONLY in exploratory step.
Output: console + optional --out <file> report (plain text).

This script does NOT access experimental data paths; it reads ONLY the file
passed via --input. It is the reproducibility executor of the protocol.
"""

from __future__ import annotations

import argparse
import math
import sys

import numpy as np
import pandas as pd
from scipy import stats

# --- Protocol-fixed configuration (do not edit without governance decision) ---
ALPHA: float = 0.05
BOOTSTRAP_B: int = 10_000
N_SEEDS_PER_CELL: int = 3
SEED_STATISTICS: int = 1879048193  # uint64 (06 sec. 9.1)
PAIR_DEPENDENCIES: list[tuple[str, str, str]] = [
    ("civil", "Hyatt", "I-35W"),
    ("saude", "Ebola", "WarpSpeed"),
]
CONDITION_ORDER: list[str] = ["A", "B", "C"]


def _bootstrap_rng() -> np.random.Generator:
    """Isolated RNG for bootstrap only (seed_statistics)."""
    return np.random.default_rng(SEED_STATISTICS)


def wilcoxon_pairwise(
    df_agg: pd.DataFrame,
) -> tuple[dict[str, float], dict[str, float]]:
    """Paired Wilcoxon two-sided on the SAME BIPs for all condition pairs.

    Returns dicts: raw p-values and signed matched-pairs rank-biserial r_rb
    (positive = second condition > first), keyed "A-B", "A-C", "B-C".
    """
    piv = df_agg.pivot(index="case_id", columns="condition", values="value")
    pairs = {"A-B": ("A", "B"), "A-C": ("A", "C"), "B-C": ("B", "C")}
    pvals: dict[str, float] = {}
    rrb: dict[str, float] = {}
    for key, (c1, c2) in pairs.items():
        x = piv[c1].to_numpy(dtype=float)
        y = piv[c2].to_numpy(dtype=float)
        if len(x) != len(y) or len(x) < 3:
            pvals[key] = float("nan")
            rrb[key] = float("nan")
            continue
        try:
            stat, p = stats.wilcoxon(x, y, alternative="two-sided", correction=True)
            pvals[key] = float(p)
            rrb[key] = signed_rank_biserial(x, y)
        except ValueError:
            pvals[key] = float("nan")
            rrb[key] = float("nan")
    return pvals, rrb


def signed_rank_biserial(x: np.ndarray, y: np.ndarray) -> float:
    """Matched-pairs rank-biserial correlation (signed).

    d = y - x; ranks of |d| (ties -> average); Wplus/Wminus sums for d>0 / d<0.
    r_rb = (Wplus - Wminus) / (Wplus + Wminus); positive => y > x.
    """
    d = y - x
    nz = d[d != 0]
    if nz.size == 0:
        return float("nan")
    abs_d = np.abs(nz)
    ranks = stats.rankdata(abs_d, method="average")
    w_plus = float(ranks[nz > 0].sum())
    w_minus = float(ranks[nz < 0].sum())
    denom = w_plus + w_minus
    return (w_plus - w_minus) / denom if denom > 0 else float("nan")


def holm_bonferroni(pvals: dict[str, float]) -> dict[str, bool]:
    """Holm-Bonferroni step-down on 3 comparisons (06 sec. 4.1)."""
    n = len(pvals)
    order = sorted(pvals.keys(), key=lambda k: pvals[k])
    rejected: dict[str, bool] = {}
    threshold = ALPHA
    for i, key in enumerate(order):
        p = pvals[key]
        if math.isnan(p):
            rejected[key] = False
            continue
        threshold = ALPHA / (n - i)
        if p <= threshold:
            rejected[key] = True
        else:
            rejected[key] = False
            for later in order[i + 1:]:
                rejected[later] = False
            break
    return rejected


def cliff_delta(x: np.ndarray, y: np.ndarray) -> float:
    """Cliff's delta = P(X>Y) - P(X<Y)."""
    gt = (x[:, None] > y[None, :]).sum()
    lt = (x[:, None] < y[None, :]).sum()
    n = x.size * y.size
    return (gt - lt) / n


def bootstrap_paired_ci(
    x: np.ndarray,
    y: np.ndarray,
    metric: str,
    rng: np.random.Generator,
    b: int = BOOTSTRAP_B,
) -> tuple[float, float]:
    """Bootstrap percentile 95% CI, PAIRED (resample BIP indices with replacement)."""
    n = x.size
    vals = np.empty(b)
    for i in range(b):
        idx = rng.integers(0, n, size=n)
        if metric == "median_diff":
            vals[i] = np.median(y[idx]) - np.median(x[idx])
        elif metric == "cliff":
            vals[i] = cliff_delta(x[idx], y[idx])
        else:  # r_rb
            vals[i] = signed_rank_biserial(x[idx], y[idx])
    return float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))


def friedman_analysis(
    df_agg: pd.DataFrame,
) -> tuple[float, float, float, float, float]:
    """Friedman omnibus: chi2, df=2, p, Kendall's W, bootstrap CI of W."""
    piv = df_agg.pivot(index="case_id", columns="condition", values="value")
    n = piv.shape[0]
    k = piv.shape[1]
    arr = [piv[c].to_numpy(dtype=float) for c in CONDITION_ORDER]
    chi2, p = stats.friedmanchisquare(*arr)
    w = chi2 / (n * (k - 1)) if n * (k - 1) > 0 else float("nan")
    rng = _bootstrap_rng()
    w_boot = np.empty(BOOTSTRAP_B)
    ranks = piv.rank(axis=1).to_numpy(dtype=float)
    for i in range(BOOTSTRAP_B):
        idx = rng.integers(0, n, size=n)
        sample = ranks[idx, :]
        rj = sample.sum(axis=0)
        chi2_b = (12.0 / (n * k * (k + 1))) * float((rj**2).sum()) - 3.0 * n * (k + 1)
        w_boot[i] = chi2_b / (n * (k - 1))
    ci = (float(np.percentile(w_boot, 2.5)), float(np.percentile(w_boot, 97.5)))
    return chi2, 2.0, p, w, ci


def iqr_outliers(series: np.ndarray) -> np.ndarray:
    """Boolean mask of outliers (IQR x 1.5). No winsorization (STAT-04)."""
    q1, q3 = np.percentile(series, [25, 75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return (series < lo) | (series > hi)


def run_analysis(
    df: pd.DataFrame, out: object
) -> None:
    """Executes protocol sec. 7 plan step by step."""
    conditions = sorted(df["condition"].unique())
    cases = sorted(df["case_id"].unique())
    out(f"GO-8B Statistical Analysis Executor — protocol 06 sec.7")
    out(f"cases={len(cases)} conditions={conditions} rows={len(df)}")
    out(f"alpha={ALPHA} bootstrap_B={BOOTSTRAP_B} seed_statistics={SEED_STATISTICS}")
    out("")

    # --- 1. DATA CHECK ---
    out("== 1. DATA CHECK ==")
    missing = df["value"].isna().sum()
    out(f"  missing values: {missing}")
    out(f"  range check: min={df['value'].min():.4f} max={df['value'].max():.4f}")
    assert df["value"].between(0, 1).all(), "range check FAILED: value outside [0,1]"
    cell_count = df.groupby(["case_id", "condition"]).size().unstack(fill_value=0)
    incomplete = (cell_count < N_SEEDS_PER_CELL).any().any()
    out(f"  completeness (>= {N_SEEDS_PER_CELL} seeds/cell): {'OK' if not incomplete else 'INCOMPLETE'}")
    if incomplete:
        out("  ** FAIL-CASE / insufficient data risk (07 FR-02..06) **")
    out("")

    # --- 2. AGGREGATION (median of seeds per case x condition) ---
    out("== 2. AGGREGATION (median per case x condition) ==")
    df_agg = (
        df.groupby(["case_id", "condition"])["value"]
        .median()
        .reset_index()
        .rename(columns={"value": "value"})
    )
    n_valid = df_agg["case_id"].nunique()
    out(f"  N (valid BIPs after aggregation) = {n_valid}")
    out("")

    # --- 3. DESCRIPTIVE ---
    out("== 3. DESCRIPTIVE (per condition) ==")
    desc = df_agg.groupby("condition")["value"].agg(
        median="median", q1=lambda s: s.quantile(0.25),
        q3=lambda s: s.quantile(0.75), min="min", max="max",
    )
    for c in CONDITION_ORDER:
        if c in desc.index:
            r = desc.loc[c]
            out(f"  cond {c}: median={r['median']:.4f} IQR=[{r['q1']:.4f},{r['q3']:.4f}] "
                f"min={r['min']:.4f} max={r['max']:.4f}")
    out("  per-case medians:")
    for c in cases:
        sub = df_agg[df_agg["case_id"] == c].set_index("condition")["value"]
        vals = {cc: f"{sub.get(cc, float('nan')):.4f}" for cc in CONDITION_ORDER}
        out(f"    {c}: " + "  ".join(f"{cc}={v}" for cc, v in vals.items()))
    out("")

    # --- 4. OMNIBUS (Friedman) ---
    out("== 4. OMNIBUS — Friedman (GLOBAL PRIMARY TEST) ==")
    chi2, dof, p, w, w_ci = friedman_analysis(df_agg)
    out(f"  chi2_F={chi2:.4f} df={dof:.0f} p={p:.4f}")
    out(f"  Kendall's W={w:.4f}  [bootstrap 95% CI: ({w_ci[0]:.4f}, {w_ci[1]:.4f})]")
    sig = p < ALPHA
    out(f"  decision: {'REJECT H0 (p<0.05)' if sig else 'NO REJECTION (p>=0.05) -> STOP post-hoc'}")
    if not sig:
        out("  per protocol: report power limitation (N=7 -> ~0.63); do NOT conclude no effect")
    out("")

    if not sig:
        out("== 5. POST-HOC — SKIPPED (omnibus not significant; protocol sec. 7 step 4/5) ==")
        return

    # --- 5. POST-HOC ---
    out("== 5. POST-HOC — Wilcoxon paired two-sided + Holm-Bonferroni ==")
    pvals, rrb = wilcoxon_pairwise(df_agg)
    rejected = holm_bonferroni(pvals)
    rng = _bootstrap_rng()
    piv = df_agg.pivot(index="case_id", columns="condition", values="value")
    for key, (c1, c2) in {"A-B": ("A", "B"), "A-C": ("A", "C"), "B-C": ("B", "C")}.items():
        x = piv[c1].to_numpy(dtype=float)
        y = piv[c2].to_numpy(dtype=float)
        cd = cliff_delta(x, y)
        med_ci = bootstrap_paired_ci(x, y, "median_diff", rng)
        cliff_ci = bootstrap_paired_ci(x, y, "cliff", rng)
        mark = "REJECT" if rejected[key] else "not rej."
        out(f"  {c1} vs {c2}: p={pvals[key]:.4f} [{mark}] "
            f"r_rb={rrb[key]:.3f} Cliff_delta={cd:.3f} "
            f"median_diff_CI=({med_ci[0]:.3f},{med_ci[1]:.3f}) "
            f"cliff_CI=({cliff_ci[0]:.3f},{cliff_ci[1]:.3f})")
    out("")

    # --- 6. EXPLORATORY ---
    out("== 6. EXPLORATORY (non-confirmatory) ==")
    if "aux_value" in df.columns and df["aux_value"].notna().any():
        aux = df.drop_duplicates("case_id")[["case_id", "aux_value"]]
        merged = df_agg.merge(aux, on="case_id")
        rho, p_rho = stats.spearmanr(merged["value"], merged["aux_value"])
        out(f"  Spearman S_struct x aux: rho={rho:.3f} p={p_rho:.4f} (exploratory)")
    if "s_sem" in df.columns and df["s_sem"].notna().any():
        diag = df.groupby(["case_id", "condition"])["s_sem"].median().reset_index()
        out("  S_sem diagnostic median per case x condition (exploratory):")
        for c in cases:
            sub = diag[diag["case_id"] == c].set_index("condition")["s_sem"]
            vals = {cc: f"{sub.get(cc, float('nan')):.4f}" for cc in CONDITION_ORDER}
            out(f"    {c}: " + "  ".join(f"{cc}={v}" for cc, v in vals.items()))
    out("")

    # --- 7. SENSITIVITY ---
    out("== 7. SENSITIVITY ==")
    # 7a. without outliers (IQR x 1.5) — STAT-04; NO winsorization
    mask = df_agg.groupby("condition")["value"].transform(
        lambda s: ~iqr_outliers(s.to_numpy())
    )
    df_no_out = df_agg[mask]
    if len(df_no_out) < len(df_agg):
        complete = df_no_out.groupby("case_id")["condition"].nunique()
        keep_ids = complete[complete >= len(CONDITION_ORDER)].index
        df_complete = df_no_out[df_no_out["case_id"].isin(keep_ids)]
        n_complete = len(keep_ids)
        if n_complete >= 3:
            chi2_o, _, p_o, w_o, _ = friedman_analysis(df_complete)
            out(f"  without outliers (IQR x 1.5): N={n_complete} "
                f"Friedman p={p_o:.4f} W={w_o:.4f}")
        else:
            out(f"  without outliers (IQR x 1.5): matrix INCOMPLETE after removal "
                f"(N complete={n_complete}) -> Friedman not computable; report as limitation")
    else:
        out("  without outliers: none flagged")
    # 7b. domain dependency — exclude 1 case per dependent pair (STAT-09) — 2 runs
    for domain, c1, c2 in PAIR_DEPENDENCIES:
        for drop in (c1, c2):
            keep = df_agg[df_agg["case_id"] != drop]
            if keep["case_id"].nunique() >= 3:
                chi2_d, _, p_d, w_d, _ = friedman_analysis(keep)
                out(f"  domain {domain}: drop {drop} -> N={keep['case_id'].nunique()} "
                    f"Friedman p={p_d:.4f} W={w_d:.4f}")
            else:
                out(f"  domain {domain}: drop {drop} -> insufficient cases")
    out("  NO mixed model (protocol STAT-09: explicitly excluded).")
    out("")

    out("== 8. REPORT ==\n"
        "  TOST NOT executed (no delta approved; delta=0.10 explicitly NOT approved).\n"
        "  No winsorization. No transformation. No unilateral decisions.\n"
        "  N is NEVER multiplied (unit = BIP/Case; N = valid BIPs).")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="GO-8B statistical analysis executor")
    parser.add_argument("--input", required=True, help="CSV: case_id, condition, value[, aux_value, s_sem]")
    parser.add_argument("--out", default=None, help="optional plain-text report file")
    args = parser.parse_args(argv)

    df = pd.read_csv(args.input)
    required = {"case_id", "condition", "value"}
    if not required.issubset(df.columns):
        sys.exit(f"ERROR: input CSV must contain columns {required}")
    if "condition" not in df.columns or df["condition"].dtype == object:
        df["condition"] = df["condition"].astype(str).str.strip()

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            run_analysis(df, lambda s: fh.write(s + "\n"))
        print(f"Report written to {args.out}")
    else:
        run_analysis(df, print)


if __name__ == "__main__":
    main()
