# -*- coding: utf-8 -*-
"""
GO-8D-NC — Data validation for pilot_results_newcycle.csv.

Validates: 270 rows, schema, status all PASS, seed cells complete (3/cell), bounds [0,1],
namespace per condition, taxonomy_sha256 per condition, matrix 30x3 median aggregation,
and Go/No-Go by valid-BIP count (pre-registration v1.0 §5.1).

Go/No-Go (Decisão da governança, 2026-08-15):
  N_válidos >= 27  -> GO  (confirmatory analysis)
  10 <= N <= 26    -> NO-GO confirmatório (exploratório/descritivo only)
  N < 10           -> STOP (no planned inferential analysis)
"""
import os
import csv
import json
import hashlib
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(os.path.dirname(HERE), "study-output", "pilot_results_newcycle.csv")
OUT = os.path.join(os.path.dirname(HERE), "study-output", "data_validation_newcycle.json")

EXPECTED_NS = {"A": "CAT", "B": "SYN", "C": "CAT"}
EXPECTED_TAX = {
    "B": hashlib.sha256(open(os.path.join(HERE, "C3_TAXONOMY.yaml"), "rb").read()).hexdigest(),
    "A": hashlib.sha256(open(os.path.join(HERE, "C2_PERMUTATION.yaml"), "rb").read()).hexdigest(),
}
EXPECTED_TAX["C"] = EXPECTED_TAX["A"]

N_BIPS = 30
N_SEEDS = 3

rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
n = len(rows)
checks = {}
ok = True

# 1. row count
checks["row_count"] = {"expect": N_BIPS * 3 * N_SEEDS, "actual": n, "pass": n == N_BIPS * 3 * N_SEEDS}
ok &= n == N_BIPS * 3 * N_SEEDS

# 2. schema/columns
req = ["bip_id", "condition", "seed_num", "seed_value", "status", "dv3",
       "conf", "ged_ecp", "ent_n12", "nodes", "edges", "namespace",
       "taxonomy_sha256", "error"]
missing = [c for c in req if c not in rows[0]]
checks["schema"] = {"missing_columns": missing, "pass": not missing}
ok &= not missing

# 3. status all PASS
st_pass = sum(1 for r in rows if r["status"] == "PASS")
checks["status"] = {"pass_rows": st_pass, "total": n, "pass": st_pass == n}
ok &= st_pass == n

# 4. seed uniqueness + count per cell
cells = {}
for r in rows:
    cells.setdefault((r["bip_id"], r["condition"]), []).append(int(r["seed_value"]))
checks["seed_cells"] = {"cells": len(cells),
                        "per_cell": [len(v) for v in cells.values()],
                        "unique_global": len(set(s for v in cells.values() for s in v)),
                        "pass": len(cells) == N_BIPS * 3 and all(len(v) == N_SEEDS for v in cells.values())}
ok &= len(cells) == N_BIPS * 3 and all(len(v) == N_SEEDS for v in cells.values())

# 5. DV3 and components in [0,1]
bnd_issues = []
for r in rows:
    for k in ("dv3", "conf", "ged_ecp", "ent_n12"):
        v = float(r[k])
        if not (0.0 <= v <= 1.0):
            bnd_issues.append((r["bip_id"], r["condition"], k, v))
checks["bounds_0_1"] = {"issues": bnd_issues[:10], "n_issues": len(bnd_issues),
                        "pass": len(bnd_issues) == 0}
ok &= len(bnd_issues) == 0

# 6. namespace per condition
ns_issues = [(r["bip_id"], r["condition"], r["namespace"]) for r in rows
             if r["namespace"] != EXPECTED_NS[r["condition"]]]
checks["namespace"] = {"issues": ns_issues[:10], "n_issues": len(ns_issues), "pass": not ns_issues}
ok &= not ns_issues

# 7. taxonomy_sha256 per condition
tx_issues = [(r["bip_id"], r["condition"], r["taxonomy_sha256"][:16]) for r in rows
             if r["taxonomy_sha256"] != EXPECTED_TAX[r["condition"]]]
checks["taxonomy_sha256"] = {"issues": tx_issues[:10], "n_issues": len(tx_issues),
                             "pass": not tx_issues,
                             "expected_B": EXPECTED_TAX["B"][:16],
                             "expected_A_C": EXPECTED_TAX["A"][:16]}
ok &= not tx_issues

# 8. valid-BIP count + Go/No-Go (pre-registration §5.1)
bips = ["BIP-%03d" % i for i in range(1, N_BIPS + 1)]
conds = ["A", "B", "C"]
valid = 0
for b in bips:
    sub = [r for r in rows if r["bip_id"] == b and r["status"] == "PASS"]
    if len(sub) == N_SEEDS * 3:
        valid += 1
if valid >= 27:
    decision = "GO"
elif valid >= 10:
    decision = "NO-GO (exploratorio/descritivo)"
else:
    decision = "STOP"
checks["gonogo"] = {"valid_bips": valid, "total": N_BIPS, "decision": decision,
                    "pass": valid >= 27}
ok &= valid >= 27

# 9. matrix Nx3 (median of 3 seeds)
mat = np.zeros((N_BIPS, 3))
for i, b in enumerate(bips):
    for j, c in enumerate(conds):
        vals = sorted(float(r["dv3"]) for r in rows if r["bip_id"] == b and r["condition"] == c)
        mat[i, j] = vals[1] if len(vals) == N_SEEDS else np.nan
checks["matrix"] = {"shape": list(mat.shape), "has_nan": bool(np.isnan(mat).any()),
                    "pass": list(mat.shape) == [N_BIPS, 3] and not np.isnan(mat).any()}
ok &= list(mat.shape) == [N_BIPS, 3] and not np.isnan(mat).any()

np.save(os.path.join(os.path.dirname(HERE), "study-output", "dv3_matrix_newcycle.npy"), mat)

summary = {"result": "PASS" if ok else "FAIL", "rows": n, "gonogo": decision,
           "checks": checks}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(summary, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("VALIDATION:", "PASS" if ok else "FAIL", "(%d checks)" % len(checks))
for k, v in checks.items():
    print("  %-18s pass=%s %s" % (k, v.get("pass"), {kk: vv for kk, vv in v.items() if kk != "pass"}))
print("saved:", OUT)
print("matrix saved: study-output/dv3_matrix_newcycle.npy")
