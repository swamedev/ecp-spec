# F2 Execution Script - GO-8D-NC
# Executes 270 reconstructions (30 BIPs x 3 conditions x 3 seeds)

import sys
import os
sys.path.insert(0, r"D:\ecp-spec\experiments\validation\GO-8D-NC\scripts")

from pilot_engine import run_study, cell
from seeds_nc import seeds
import csv

# BIP directories - two locations
GO8C_STUDY_INPUT = r"D:\ecp-spec\experiments\validation\GO-8C\study-input"
GO8D_STUDY_INPUT = r"D:\ecp-spec\experiments\validation\GO-8D-NC\BIPs"
OUTPUT_DIR = r"D:\ecp-spec\experiments\validation\GO-8D-NC\study-output"

# BIP directories in each location
GO8C_BIPS = [f"BIP-{i:03d}" for i in range(1, 13)]  # 001-012
GO8D_BIPS = [f"BIP-{i:03d}" for i in range(13, 31)]  # 013-030

print("=" * 60)
print("F2 EXECUTION - GO-8D-NC")
print("=" * 60)
print(f"Seed master: 20260816")
print(f"Total BIPs: 30 (12 GO-8C + 18 GO-8D-NC)")
print(f"Total executions planned: 270")
print(f"Seeds loaded: {len(seeds)} BIPs")
print(f"Output directory: {OUTPUT_DIR}")
print("=" * 60)

# Run GO-8C BIPs (001-012)
print("\n[Phase 1] Executing GO-8C BIPs (001-012)...")
rows_8c = []
for bip_dir in GO8C_BIPS:
    bip = "BIP-" + bip_dir.split("-")[1]
    for cond in ("A", "B", "C"):
        # Import the cell function and run directly
        from pilot_engine import cell, dv3
        cell_res = cell(bip, bip_dir, cond, GO8C_STUDY_INPUT)
        for j in (1, 2, 3):
            if cell_res["status"] == "FAIL":
                rows_8c.append({
                    "bip_id": bip, "condition": cond, "seed_num": j,
                    "seed_value": seeds[bip][cond][f"seed{j}"],
                    "status": "FAIL", "dv3": "", "conf": "", "ged_ecp": "",
                    "ent_n12": "", "nodes": 0, "edges": 0, "namespace": "",
                    "taxonomy_sha256": "", "error": cell_res["reason"],
                })
            else:
                from pilot_engine import dv3
                rows_8c.append({
                    "bip_id": bip, "condition": cond, "seed_num": j,
                    "seed_value": seeds[bip][cond][f"seed{j}"],
                    "status": "PASS",
                    "dv3": round(dv3(cell_res), 6),
                    "conf": cell_res["conf"], "ged_ecp": cell_res["ged_ecp"],
                    "ent_n12": cell_res["ent_n12"],
                    "nodes": cell_res["nodes"], "edges": cell_res["edges"],
                    "namespace": cell_res["ns"],
                    "taxonomy_sha256": cell_res["tax_sha"],
                    "error": "",
                })

print(f"  Completed GO-8C: {len(rows_8c)} rows")

# Run GO-8D-NC BIPs (013-030)
print("\n[Phase 2] Executing GO-8D-NC BIPs (013-030)...")
rows_8d = []
for bip_dir in GO8D_BIPS:
    bip = "BIP-" + bip_dir.split("-")[1]
    for cond in ("A", "B", "C"):
        from pilot_engine import cell, dv3
        cell_res = cell(bip, bip_dir, cond, GO8D_STUDY_INPUT)
        for j in (1, 2, 3):
            if cell_res["status"] == "FAIL":
                rows_8d.append({
                    "bip_id": bip, "condition": cond, "seed_num": j,
                    "seed_value": seeds[bip][cond][f"seed{j}"],
                    "status": "FAIL", "dv3": "", "conf": "", "ged_ecp": "",
                    "ent_n12": "", "nodes": 0, "edges": 0, "namespace": "",
                    "taxonomy_sha256": "", "error": cell_res["reason"],
                })
            else:
                rows_8d.append({
                    "bip_id": bip, "condition": cond, "seed_num": j,
                    "seed_value": seeds[bip][cond][f"seed{j}"],
                    "status": "PASS",
                    "dv3": round(dv3(cell_res), 6),
                    "conf": cell_res["conf"], "ged_ecp": cell_res["ged_ecp"],
                    "ent_n12": cell_res["ent_n12"],
                    "nodes": cell_res["nodes"], "edges": cell_res["edges"],
                    "namespace": cell_res["ns"],
                    "taxonomy_sha256": cell_res["tax_sha"],
                    "error": "",
                })

print(f"  Completed GO-8D-NC: {len(rows_8d)} rows")

# Combine and write
all_rows = rows_8c + rows_8d
total_rows = len(all_rows)
pass_count = sum(1 for r in all_rows if r["status"] == "PASS")
fail_count = sum(1 for r in all_rows if r["status"] == "FAIL")

print(f"\nTotal executions: {total_rows}")
print(f"PASS: {pass_count}")
print(f"FAIL: {fail_count}")

# Write combined CSV
os.makedirs(r"D:\ecp-spec\experiments\validation\GO-8D-NC\study-output", exist_ok=True)
csv_path = r"D:\ecp-spec\experiments\validation\GO-8D-NC\study-output\pilot_results_newcycle.csv"
cols = ["bip_id", "condition", "seed_num", "seed_value", "status", "dv3",
        "conf", "ged_ecp", "ent_n12", "nodes", "edges", "namespace",
        "taxonomy_sha256", "error"]

with open(csv_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=[
        "bip_id", "condition", "seed_num", "seed_value", "status", "dv3",
        "conf", "ged_ecp", "ent_n12", "nodes", "edges", "namespace",
        "taxonomy_sha256", "error"
    ])
    w.writeheader()
    for r in all_rows:
        w.writerow(r)

print(f"\nResults saved to: {csv_path}")
print(f"Total: {len(all_rows)}  PASS: {sum(1 for r in all_rows if r['status'] == 'PASS')}  FAIL: {sum(1 for r in all_rows if r['status'] == 'FAIL')}")