# GO-8B — REPRODUCIBILITY

## Frozen scripts

- `scripts/go8b/go8b_power_sim.py`
- `scripts/go8b/go8b_statistical_analysis.py`
- `scripts/go8b/requirements.txt`

## Power simulation

Frozen parameters:
- Friedman df=2
- α=0.05
- k=3
- 3 seeds/cell
- median + clip [0,1]
- N=5..28
- B=5000
- seed 20260811
- σb=.12, σe=.08, σs=.06
- S0=(.55,.55,.55)
- S1=(.50,.60,.66)

R9 reproduction:
- differences within reported MC uncertainty;
- determinism verified;
- no experimental data access.

## Statistical executor

Input is CSV via command line.
Validated synthetically:
- data checks;
- aggregation;
- Friedman;
- Kendall W;
- bootstrap;
- Wilcoxon + Holm;
- exploratory analysis;
- outlier sensitivity;
- dependency sensitivity;
- no TOST.

## Environment

`requirements.txt` fixes:
- numpy==1.26.4
- scipy==1.15.3
- pandas==3.0.5

R9 accepted pandas environment as residual observation, not methodological inconsistency.
