# -*- coding: utf-8 -*-
"""
GO-8D METRIC VALIDATION / CALIBRATION (M-01..M-04) — no new experiment, no new Lock.

Re-derives the deterministic reconstruction graphs for the 36 cells (same inputs as the
confirmatory run; cell output is deterministic per (bip, cond) since the 3 seeds are recorded
but do not affect the pipeline), then computes:
  - ent: raw entropy H, and renormalized entropy with common n_slots (12 and 9 variants)
  - ged_ref: GED vs a single common reference (ECP canonical 9-node chain) for A/B/C
  - candidate DVs: DV0 original, DV1 ent-recalibrated, DV2 ged-recalibrated, DV3 full
  - per-component analysis + 7 pre-registered criteria + synthetic sanity checks

Read-only: uses GO-8D existing data + re-derivation; writes only into metric-validation/.
"""
import os, sys, json, math
from collections import Counter
import numpy as np

sys.path.insert(0, r"D:\ecp-spec\scripts\go8b\operational")
import yaml
import pilot_engine as pe
from wl_kernel import G_ECP, _wl_hash
from scipy.optimize import linear_sum_assignment

# ---- references ----
C3 = yaml.safe_load(open(r"D:\ecp-spec\experiments\validation\GO-8C\scripts\C3_TAXONOMY.yaml", encoding="utf-8"))
SYN_ID2DEF_CORR = {n["id"]: n["definition"] for n in C3["taxonomy"]["nodes"]}
SYN_EDGES = [(e["from"], e["to"]) for e in C3["taxonomy"]["edges"]]
SYN_IDS = [n["id"] for n in C3["taxonomy"]["nodes"]]

C2 = yaml.safe_load(open(r"D:\ecp-spec\scripts\go8b\operational\C2_PERMUTATION.yaml", encoding="utf-8"))
CANON = C2["canonical_order"]
O2C = C2["opaque_to_canonical"]
CAN2OPQ = C2["canonical_to_opaque"]
CAT_IDS = sorted(O2C.keys())
CAT_CHAIN = [CAN2OPQ[c] for c in CANON]
CAT_REF = {"nodes": [{"id": c} for c in CAT_IDS],
           "edges": [{"source": CAT_CHAIN[i], "target": CAT_CHAIN[i + 1]} for i in range(len(CAT_CHAIN) - 1)]}
SYN_REF = {"nodes": [{"id": s} for s in SYN_IDS],
           "edges": [{"source": s, "target": t} for s, t in SYN_EDGES]}
ECP_REF = {"nodes": [{"id": n["id"]} for n in G_ECP["nodes"]],
           "edges": [{"source": e["source"], "target": e["target"]} for e in G_ECP["edges"]]}

# common reference for ALL conditions (M-02): ECP canonical 9-node chain
COMMON_REF = ECP_REF

def label_emb_corrected(label):
    if isinstance(label, np.ndarray):
        return pe._norm(label)
    if not isinstance(label, str):
        return np.zeros(384)
    if label in CANON:
        return pe._norm(pe.EMB_TABLE.get(("ECP", label)))
    if label in O2C:
        return pe.text_emb(pe.CAT_NEUTRAL_DEFS[O2C[label]])
    if label in SYN_ID2DEF_CORR:
        return pe.text_emb(SYN_ID2DEF_CORR[label])
    return np.zeros(384)

def _cos(a, b):
    a = np.asarray(a, float).flatten(); b = np.asarray(b, float).flatten()
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    return float(np.dot(a, b) / (na * nb)) if na and nb else 0.0

def ged_similarity(g_rec, g_ref, emb_rec, emb_ref, w_edge=0.5):
    rec = [n["id"] for n in g_rec["nodes"]]
    ref = [n["id"] for n in g_ref["nodes"]]
    n, m = len(rec), len(ref)
    C = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            C[i, j] = 1.0 - _cos(emb_rec[rec[i]], emb_ref[ref[j]])
    ri, ci = linear_sum_assignment(C)
    subst = float(sum(C[ri, ci]))
    node_cost = subst + (n - len(ri)) + (m - len(ri))
    mapping = {rec[i]: ref[j] for i, j in zip(ri, ci)}
    rec_edges = set((e["source"], e["target"]) for e in g_rec["edges"])
    ref_edges = set((e["source"], e["target"]) for e in g_ref["edges"])
    mapped = set((mapping.get(s, s), mapping.get(t, t)) for (s, t) in rec_edges)
    edge_del = len(mapped - ref_edges); edge_add = len(ref_edges - mapped)
    edge_cost = w_edge * (edge_del + edge_add)
    max_cost = (n + m) + w_edge * (len(rec_edges) + len(ref_edges))
    return 1.0 - (node_cost + edge_cost) / max_cost if max_cost else 1.0

STUDY = r"D:\ecp-spec\experiments\validation\GO-8C\study-input"
BIPS = ["BIP-001-deepwater", "BIP-002-hyatt", "BIP-003-ows", "BIP-004-genoma",
        "BIP-005-evergiven", "BIP-006-i35w", "BIP-007-ebola", "BIP-008-apollo13",
        "BIP-009-chernobyl", "BIP-010-tacomanarrows", "BIP-011-dominos", "BIP-012-eyjafjallajokull"]
CONDITIONS = ["A", "B", "C"]

def resolve(bip_dir):
    d = os.path.join(STUDY, bip_dir)
    narr = os.path.join(d, "narrative", "01-narrativa-original.md")
    if not os.path.exists(narr):
        narr = os.path.join(d, "narrative", "narrative_pt.md")
    if not os.path.exists(narr):
        narr = os.path.join(d, "narrative", "narrative.md")
    af = os.path.join(d, "atomic-facts", "02-atomic-facts.md")
    if not os.path.exists(af):
        af = os.path.join(d, "atomic-facts", "atomic_facts.md")
    return narr, af

def rebuild_cell(bip_dir, cond):
    saved = (pe.SYN_ID2DEF, pe.SYN_NODES, pe.SYN_ID2LABEL)
    if cond == "B":
        pe.SYN_ID2DEF = SYN_ID2DEF_CORR
        pe.SYN_NODES = C3["taxonomy"]["nodes"]
        pe.SYN_ID2LABEL = {n["id"]: n["label"] for n in pe.SYN_NODES}
    try:
        narr, af = resolve(bip_dir)
        units = pe.parse_atomic_facts(af) if cond in ("A", "B") else pe.parse_narrative(narr)
        entities, relations, ent_vectors = pe.build_entities_relations(units, cond)
        graph = pe.build_graph(entities, relations, cond, bip_dir)
        if graph is None:
            return None
        nodes, edges = graph["nodes"], graph["edges"]
        gd = {"nodes": [{"id": n["node_id"]} for n in nodes],
              "edges": [{"source": e["source"], "target": e["target"]} for e in edges]}
        lab = {n["node_id"]: n["syn_category"] for n in nodes}
        return gd, lab, entities
    finally:
        pe.SYN_ID2DEF, pe.SYN_NODES, pe.SYN_ID2LABEL = saved

rows = []
for bip_dir in BIPS:
    bip = "BIP-" + bip_dir.split("-")[1]
    for cond in CONDITIONS:
        r = rebuild_cell(bip_dir, cond)
        if r is None:
            rows.append({"bip": bip, "cond": cond, "ok": False})
            continue
        gd, lab, entities = r
        # entropy components (mirror run_study_g8d.py: uses entity syn_category)
        cat_counts = Counter(e["syn_category"] for e in entities)
        k_obs = len(cat_counts)                       # distinct categories observed
        p = np.array([cat_counts[c] for c in cat_counts], float) / len(entities) if entities else np.array([0.0])
        H = float(-(p * np.log(p)).sum())
        n_slots_orig = 9 if cond in ("A", "C") else 12
        ent_orig = H / math.log(n_slots_orig) if n_slots_orig > 1 else 0.0
        ent_n12 = H / math.log(12) if 12 > 1 else 0.0
        ent_n9 = H / math.log(9) if 9 > 1 else 0.0
        ent_eff = H / math.log(k_obs) if k_obs > 1 else 0.0
        # conf
        confs = [e["confidence"] for e in entities]
        conf = float(np.mean(confs)) if confs else 0.0
        # ged: original reference (per-cond) vs common ECP reference
        ref = CAT_REF if cond in ("A", "C") else SYN_REF
        emb_rec = {nd["id"]: label_emb_corrected(lab[nd["id"]]) for nd in gd["nodes"]}
        emb_ref_orig = {nd["id"]: label_emb_corrected(nd["id"]) for nd in ref["nodes"]}
        emb_ref_ecp = {nd["id"]: label_emb_corrected(nd["id"]) for nd in COMMON_REF["nodes"]}
        ged_orig = max(0.0, min(1.0, ged_similarity(gd, ref, emb_rec, emb_ref_orig)))
        ged_ecp = max(0.0, min(1.0, ged_similarity(gd, COMMON_REF, emb_rec, emb_ref_ecp)))
        rows.append({
            "bip": bip, "cond": cond, "ok": True,
            "nodes": len(gd["nodes"]), "edges": len(gd["edges"]),
            "k_obs": k_obs, "H": H, "conf": conf,
            "ent_orig": ent_orig, "ent_n12": ent_n12, "ent_n9": ent_n9, "ent_eff": ent_eff,
            "ged_orig": ged_orig, "ged_ecp": ged_ecp,
        })

# candidate DVs (clamp all to [0,1])
def clamp(v): return max(0.0, min(1.0, float(v)))
for r in rows:
    if not r["ok"]:
        continue
    r["dv0"] = clamp((r["conf"] + r["ged_orig"] + r["ent_orig"]) / 3.0)
    r["dv1"] = clamp((r["conf"] + r["ged_orig"] + r["ent_n12"]) / 3.0)
    r["dv2"] = clamp((r["conf"] + r["ged_ecp"] + r["ent_orig"]) / 3.0)
    r["dv3"] = clamp((r["conf"] + r["ged_ecp"] + r["ent_n12"]) / 3.0)

json.dump(rows, open(r"D:\ecp-spec\experiments\validation\GO-8D\metric-validation\calibration_cells.json",
                     "w", encoding="utf-8"), indent=2, ensure_ascii=False)

# ---- verify re-derivation matches CSV (conf/ged_orig/ent_orig) ----
import pandas as pd
csv = pd.read_csv(r"D:\ecp-spec\experiments\validation\GO-8D\study-output\pilot_results_g8d.csv")
csv = csv[csv["status"] == "PASS"]
csv = csv.groupby(["bip_id", "condition"])[["conf", "ged_ref", "ent"]].first().reset_index()
print("=== RE-DERIVATION CONSISTENCY vs CSV ===")
max_conf = max_ged = max_ent = 0.0
for r in rows:
    if not r["ok"]: continue
    c = csv[(csv.bip_id == r["bip"]) & (csv.condition == r["cond"])].iloc[0]
    max_conf = max(max_conf, abs(r["conf"] - c["conf"]))
    max_ged = max(max_ged, abs(r["ged_orig"] - c["ged_ref"]))
    max_ent = max(max_ent, abs(r["ent_orig"] - c["ent"]))
print("  max |conf  - conf_csv | = %.6f" % max_conf)
print("  max |ged   - ged_csv   | = %.6f" % max_ged)
print("  max |ent   - ent_csv   | = %.6f" % max_ent)
print("  (should be ~0; tiny fp ok)")