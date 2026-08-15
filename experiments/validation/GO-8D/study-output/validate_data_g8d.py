# -*- coding: utf-8 -*-
"""GO-8D — Data validation for pilot_results_g8d.csv (governance-authorized execution)."""
import os, csv, sys, json
import numpy as np

CSV = r"D:\ecp-spec\experiments\validation\GO-8D\study-output\pilot_results_g8d.csv"
OUT = r"D:\ecp-spec\experiments\validation\GO-8D\study-output\data_validation_g8d.json"

EXPECTED_TAX = {"A": None, "B": None, "C": None}  # filled below from file hashes
import hashlib
EXPECTED_TAX["B"] = hashlib.sha256(
    open(r"D:\ecp-spec\experiments\validation\GO-8C\scripts\C3_TAXONOMY.yaml", "rb").read()).hexdigest()
EXPECTED_TAX["A"] = EXPECTED_TAX["C"] = hashlib.sha256(
    open(r"D:\ecp-spec\scripts\go8b\operational\C2_PERMUTATION.yaml", "rb").read()).hexdigest()

EXPECTED_NS = {"A": "CAT", "B": "SYN", "C": "CAT"}

rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
n = len(rows)
checks = {}
ok = True

# 1. row count
checks["row_count"] = {"expect": 108, "actual": n, "pass": n == 108}
ok &= n == 108

# 2. schema/columns
req = ["bip_id", "condition", "seed_num", "seed_value", "status", "dv_confirm",
       "conf", "ged_ref", "ent", "nodes", "edges", "namespace", "taxonomy_sha256", "error"]
missing = [c for c in req if c not in rows[0]]
checks["schema"] = {"missing_columns": missing, "pass": not missing}
ok &= not missing

# 3. status all PASS
st_pass = sum(1 for r in rows if r["status"] == "PASS")
checks["status"] = {"pass_rows": st_pass, "pass": st_pass == 108}
ok &= st_pass == 108

# 4. seed uniqueness + count per cell
cells = {}
for r in rows:
    cells.setdefault((r["bip_id"], r["condition"]), []).append(int(r["seed_value"]))
checks["seed_cells"] = {"cells": len(cells), "per_cell": [len(v) for v in cells.values()],
                        "unique_global": len(set(s for v in cells.values() for s in v)),
                        "pass": len(cells) == 36 and all(len(v) == 3 for v in cells.values())}
ok &= len(cells) == 36 and all(len(v) == 3 for v in cells.values())

# 5. DV and components in [0,1]
bnd_issues = []
for r in rows:
    for k in ("dv_confirm", "conf", "ged_ref", "ent"):
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
checks["taxonomy_sha256"] = {"issues": tx_issues[:10], "n_issues": len(tx_issues), "pass": not tx_issues,
                             "expected_B": EXPECTED_TAX["B"][:16], "expected_A_C": EXPECTED_TAX["A"][:16]}
ok &= not tx_issues

# 8. cell aggregation: median of 3 seeds per cell, matrix Nx3
bips = ["BIP-%03d" % i for i in range(1, 13)]
conds = ["A", "B", "C"]
mat = np.zeros((12, 3))
for i, b in enumerate(bips):
    for j, c in enumerate(conds):
        vals = sorted(float(r["dv_confirm"]) for r in rows if r["bip_id"] == b and r["condition"] == c)
        mat[i, j] = vals[1]  # median of 3
checks["matrix"] = {"shape": list(mat.shape), "has_nan": bool(np.isnan(mat).any()),
                    "pass": list(mat.shape) == [12, 3] and not np.isnan(mat).any()}
ok &= list(mat.shape) == [12, 3] and not np.isnan(mat).any()

np.save(r"D:\ecp-spec\experiments\validation\GO-8D\study-output\dv_matrix_g8d.npy", mat)

# 9. D-04 parseability gate re-check (study materials)
sys.path.insert(0, r"D:\ecp-spec\experiments\validation\GO-8D\scripts")
from validate_parseability import validate_study_input
res = validate_study_input()
n_pass = sum(1 for r in res if r["af"]["status"] == "PASS" and r["narr"]["status"] == "PASS")
checks["d04_parseability"] = {"bips_pass": n_pass, "total": len(res), "pass": n_pass == len(res) == 12}
ok &= n_pass == len(res) == 12

summary = {"result": "PASS" if ok else "FAIL", "rows": n, "checks": checks}
json.dump(summary, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("VALIDATION:", "PASS" if ok else "FAIL", "(%d checks)" % len(checks))
for k, v in checks.items():
    print("  %-18s pass=%s %s" % (k, v.get("pass"), {kk: vv for kk, vv in v.items() if kk != "pass"}))
print("saved:", OUT)
print("matrix saved: study-output/dv_matrix_g8d.npy")