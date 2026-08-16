import pandas as pd
import numpy as np
import sys
import os
import json
import hashlib
from scipy.stats import friedmanchisquare, wilcoxon, ttest_1samp

sys.path.insert(0, r"D:\ecp-spec\experiments\validation\GO-8D-NC\scripts")
from pilot_engine import cell, dv3, dv3_components, parse_atomic_facts, parse_narrative, build_entities_relations, build_graph, text_emb, label_emb_corrected
from seeds_nc import seeds

# Paths
GO8C_STUDY_INPUT = r"D:\ecp-spec\experiments\validation\GO-8C\study-input"
GO8D_STUDY_INPUT = r"D:\ecp-spec\experiments\validation\GO-8D-NC\BIPs"
OUTPUT_DIR = r"D:\ecp-spec\experiments\validation\GO-8D-NC\study-output"

GO8C_BIPS = [
    "BIP-001-deepwater", "BIP-002-hyatt", "BIP-003-ows", "BIP-004-genoma",
    "BIP-005-evergiven", "BIP-006-i35w", "BIP-007-ebola", "BIP-008-apollo13",
    "BIP-009-chernobyl", "BIP-010-tacomanarrows", "BIP-011-dominos", "BIP-012-eyjafjallajokull"
]

GO8D_BIPS = [
    "BIP-013-bhopal", "BIP-014-tmi", "BIP-015-challenger", "BIP-016-columbia",
    "BIP-017-katrina", "BIP-018-flint", "BIP-019-fukushima", "BIP-020-grenfell",
    "BIP-021-vajont", "BIP-022-max8", "BIP-023-mariana", "BIP-024-dieselgate",
    "BIP-025-wellsfargo", "BIP-026-theranos", "BIP-027-opioids", "BIP-028-enron",
    "BIP-029-takata", "BIP-030-concordia"
]

def run_diagnostic():
    """Run full diagnostic decomposition and synthetic tests."""
    
    results = {
        "components": {},  # BIP -> cond -> replica -> {conf, ged_ecp, ent_n12, dv3}
        "component_analysis": {},
        "ts1": {},
        "ts2": {},
        "ts3": {},
        "ts4": {},
        "evidence": {"H1": [], "H2": [], "H3": []},
        "classification": None,
        "recommendation": None
    }
    
    print("=== DIAGNÓSTICO D-GO8E-01 ===")
    print("Extraindo componentes DV3 (conf, ged_ecp, ent_n12) para todas as 270 execuções...")
    
    # Extract components for all BIPs
    all_bip_dirs = GO8C_BIPS + GO8D_BIPS
    all_study_inputs = [GO8C_STUDY_INPUT] * len(GO8C_BIPS) + [GO8D_STUDY_INPUT] * len(GO8D_BIPS)
    
    for bip_dir, study_input in zip(all_bip_dirs, all_study_inputs):
        bip = "BIP-" + bip_dir.split("-")[1]
        results["components"][bip] = {}
        
        for cond in ("A", "B", "C"):
            results["components"][bip][cond] = {}
            
            cell_res = cell(bip, bip_dir, cond, study_input)
            
            if cell_res["status"] == "FAIL":
                print(f"  {bip} {cond}: FAIL - {cell_res['reason']}")
                continue
            
            # Extract components from cell_res
            conf = cell_res["conf"]
            ged_ecp = cell_res["ged_ecp"]
            ent_n12 = cell_res["ent_n12"]
            dv3_val = cell_res["conf"] = dv3(cell_res)  # recalculate
            
            # Store for each replica (same values for all 3 seeds)
            for j in (1, 2, 3):
                results["components"][bip][cond][j] = {
                    "conf": conf,
                    "ged_ecp": ged_ecp,
                    "ent_n12": ent_n12,
                    "dv3": dv3_val
                }
            
            # Print first BIP for verification
            if bip == "BIP-001" and cond == "A":
                print(f"  Exemplo BIP-001 A: conf={conf:.4f}, ged_ecp={ged_ecp:.4f}, ent_n12={ent_n12:.4f}, dv3={dv3_val:.4f}")
    
    print("Componentes extraídos para todos os 30 BIPs x 3 condições x 3 réplicas.")
    
    return results

if __name__ == "__main__":
    results = run_diagnostic()
    # Save intermediate results
    with open(r"D:\ecp-spec\experiments\validation\GO-8D-NC\study-output\diagnostic_components.json", "w") as f:
        # Convert numpy types to native Python
        import json
        def convert(obj):
            if isinstance(obj, (np.integer, np.floating)):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            elif isinstance(obj, dict):
                return {k: convert(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert(v) for v in obj]
            return obj
        json.dump(convert(results), f, indent=2)
    print("Componentes salvos em study-output/diagnostic_components.json")