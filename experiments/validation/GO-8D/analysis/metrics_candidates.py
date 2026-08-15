# -*- coding: utf-8 -*-
"""
GO-8D D-02 — diagnostic: candidate metrics on GO-8C N=12 data (read-only).
Rebuilds the study graphs from GO-8C study-input using the frozen engine logic,
then computes candidate metrics. Writes nothing to GO-8B/GO-8C. Output only to stdout.
"""
import sys, os, csv, hashlib, math
from collections import Counter
import numpy as np

OP = r"D:\ecp-spec\scripts\go8b\operational"
sys.path.insert(0, OP)
import yaml
import pilot_engine as pe
from wl_kernel import WLKernel, G_ECP, _wl_hash
from graph_from_reconstruction import GraphFromReconstruction
from scipy.optimize import linear_sum_assignment

wl = WLKernel(h=3, emb_function=pe.label_emb)

# ---------------------------------------------------------------- corrected taxonomy
GO8C_TAX = r"D:\ecp-spec\experiments\validation\GO-8C\scripts\C3_TAXONOMY.yaml"
FROZEN_TAX = r"D:\ecp-spec\scripts\go8b\operational\C3_TAXONOMY.yaml"
with open(GO8C_TAX, encoding="utf-8") as f:
    C3_CORR = yaml.safe_load(f)
with open(FROZEN_TAX, encoding="utf-8") as f:
    C3_FROZEN = yaml.safe_load(f)

SYN_NODES_CORR = C3_CORR["taxonomy"]["nodes"]
SYN_ID2DEF_CORR = {n["id"]: n["definition"] for n in SYN_NODES_CORR}
SYN_ID2DEF_FROZEN = {n["id"]: n["definition"] for n in C3_FROZEN["taxonomy"]["nodes"]}
SYN_EDGES = [(e["from"], e["to"]) for e in C3_CORR["taxonomy"]["edges"]]
SYN_IDS = [n["id"] for n in SYN_NODES_CORR]

# ---------------------------------------------------------------- C2 mapping
with open(r"D:\ecp-spec\scripts\go8b\operational\C2_PERMUTATION.yaml", encoding="utf-8") as f:
    C2 = yaml.safe_load(f)
CANON = C2["canonical_order"]                 # 9 ECP order
O2C = C2["opaque_to_canonical"]               # CAT-XX -> ECP name
CAN2OPQ = C2["canonical_to_opaque"]           # ECP name -> CAT-XX
CAT_IDS = sorted(O2C.keys())                  # CAT-00..CAT-08
# CAT reference: chain following canonical order, mapped to opaque ids
CAT_CHAIN = [CAN2OPQ[c] for c in CANON]
CAT_REF = {
    "nodes": [{"id": c} for c in CAT_IDS],
    "edges": [{"source": CAT_CHAIN[i], "target": CAT_CHAIN[i + 1]} for i in range(len(CAT_CHAIN) - 1)],
}
SYN_REF = {
    "nodes": [{"id": s} for s in SYN_IDS],
    "edges": [{"source": s, "target": t} for s, t in SYN_EDGES],
}
ECP_REF = {"nodes": [{"id": n["id"]} for n in G_ECP["nodes"]],
           "edges": [{"source": e["source"], "target": e["target"]} for e in G_ECP["edges"]]}

# ---------------------------------------------------------------- labeled WL kernel
def wl_hist_labeled(graph, labels):
    nodes = [n["id"] for n in graph["nodes"]]
    adj_in = {n: [] for n in nodes}
    adj_out = {n: [] for n in nodes}
    for e in graph["edges"]:
        adj_out.setdefault(e["source"], []).append(e["target"])
        adj_in.setdefault(e["target"], []).append(e["source"])
    cur = {n: labels.get(n, "neutral") for n in nodes}
    hist = Counter()
    for _ in range(wl.h + 1):
        hist.update(cur.values())
        new = {}
        for v in nodes:
            ms = [(cur.get(u, "neutral"), "in") for u in adj_in[v]] + \
                 [(cur.get(w, "neutral"), "out") for w in adj_out[v]]
            new[v] = _wl_hash((cur[v], sorted(ms)))
        cur = new
    return dict(hist)

def cos_hist(h1, h2):
    keys = set(h1) | set(h2)
    v1 = np.array([h1.get(k, 0.0) for k in keys], float)
    v2 = np.array([h2.get(k, 0.0) for k in keys], float)
    if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
        return 0.0
    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

# ---------------------------------------------------------------- GED (assignment-based, weighted)
def _cos(a, b):
    a = np.asarray(a, float).flatten()
    b = np.asarray(b, float).flatten()
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return float(np.dot(a, b) / (na * nb))

def ged_similarity(g_rec, g_ecp, emb_rec, emb_ecp, w_edge=0.5):
    rec = [n["id"] for n in g_rec["nodes"]]
    ecp = [n["id"] for n in g_ecp["nodes"]]
    n, m = len(rec), len(ecp)
    C = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            C[i, j] = 1.0 - _cos(emb_rec[rec[i]], emb_ecp[ecp[j]])
    ri, ci = linear_sum_assignment(C)
    subst = float(sum(C[ri, ci]))
    node_cost = subst + (n - len(ri)) + (m - len(ri))     # unmatched -> del/ins cost 1.0
    mapping = {rec[i]: ecp[j] for i, j in zip(ri, ci)}
    rec_edges = set((e["source"], e["target"]) for e in g_rec["edges"])
    ecp_edges = set((e["source"], e["target"]) for e in g_ecp["edges"])
    mapped = set((mapping.get(s, s), mapping.get(t, t)) for (s, t) in rec_edges)
    edge_del = len(mapped - ecp_edges)
    edge_add = len(ecp_edges - mapped)
    edge_cost = w_edge * (edge_del + edge_add)
    max_cost = (n + m) + w_edge * (len(rec_edges) + len(ecp_edges))
    if max_cost == 0:
        return 1.0
    return 1.0 - (node_cost + edge_cost) / max_cost

def label_emb_for(node_id, cat):
    return pe.label_emb(cat)

# ---------------------------------------------------------------- per-cell build
STUDY = r"D:\ecp-spec\experiments\validation\GO-8C\study-input"
BIPS = [
    "BIP-001-deepwater", "BIP-002-hyatt", "BIP-003-ows", "BIP-004-genoma",
    "BIP-005-evergiven", "BIP-006-i35w", "BIP-007-ebola", "BIP-008-apollo13",
    "BIP-009-chernobyl", "BIP-010-tacomanarrows", "BIP-011-dominos", "BIP-012-eyjafjallajokull",
]
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

def cell(bip, bip_dir, cond):
    # taxonomy override: condition B uses corrected (canonical GO-8C) for all cells
    saved = (pe.SYN_ID2DEF, pe.SYN_NODES, pe.SYN_ID2LABEL)
    if cond == "B":
        pe.SYN_ID2DEF = SYN_ID2DEF_CORR
        pe.SYN_NODES = SYN_NODES_CORR
        pe.SYN_ID2LABEL = {n["id"]: n["label"] for n in pe.SYN_NODES}
    try:
        narr, af = resolve(bip_dir)
        units = pe.parse_atomic_facts(af) if cond in ("A", "B") else pe.parse_narrative(narr)
        entities, relations, ent_vectors = pe.build_entities_relations(units, cond)
        graph = pe.build_graph(entities, relations, cond, bip)
        nodes, edges = graph["nodes"], graph["edges"]
        gd = {"nodes": [{"id": n["node_id"]} for n in nodes],
              "edges": [{"source": e["source"], "target": e["target"]} for e in edges]}
        # labels per reconstructed node = its syn_category
        lab = {n["node_id"]: n["syn_category"] for n in nodes}
        # per-entity confidence (fidelity M5)
        confs = [e["confidence"] for e in entities]
        cat_counts = Counter(e["syn_category"] for e in entities)
        n_slots = 9 if cond in ("A", "C") else 12
        p = np.array([cat_counts[c] for c in cat_counts], float) / len(entities)
        H = float(-(p * np.log(p)).sum())
        ent_norm = H / math.log(n_slots) if n_slots > 1 else 0.0

        s_struct, s_sem = pe.compute_s_metrics(graph, cond, ent_vectors)
        n = len(nodes)
        ecp_n2 = sum(v * v for v in wl.structural_features(ECP_REF).values())
        s_base = n * n / np.sqrt((n * n + 3 * n) * ecp_n2)
        m1 = s_struct - float(s_base)

        # M2 labeled WL same-namespace
        ref = CAT_REF if cond in ("A", "C") else SYN_REF
        ref_labels = {nd["id"]: nd["id"] for nd in ref["nodes"]}
        m2 = cos_hist(wl_hist_labeled(gd, lab), wl_hist_labeled(ref, ref_labels))

        # embeddings for GED / refined S_sem
        emb_rec = {nd["node_id"]: pe.label_emb(nd["syn_category"]) for nd in nodes}
        emb_ecp = {e["id"]: pe.label_emb(e["id"]) for e in G_ECP["nodes"]}
        m3 = ged_similarity(gd, ECP_REF, emb_rec, emb_ecp)

        node_labels_rec = emb_rec
        node_labels_ecp = emb_ecp
        edge_labels_rec = {(e["source"], e["target"]): e["relation_type"] for e in edges}
        edge_labels_ecp = {(e["source"], e["target"]): e["label"] for e in G_ECP["edges"]}
        m4 = wl.semantic_similarity(gd, G_ECP, node_labels_rec, node_labels_ecp,
                                    edge_labels_rec, edge_labels_ecp)

        m5 = float(np.mean(confs))
        return {
            "bip": bip, "cond": cond, "nodes": n, "edges": len(gd["edges"]),
            "M0_sstruct": round(s_struct, 4), "M1_sstruct_corr": round(m1, 4),
            "M2_labWL": round(m2, 4), "M3_ged": round(m3, 4),
            "M4_ssem_ref": round(m4, 4), "M5_fid": round(m5, 4), "M6_ent": round(ent_norm, 4),
        }
    finally:
        pe.SYN_ID2DEF, pe.SYN_NODES, pe.SYN_ID2LABEL = saved

rows = []
for bip_dir in BIPS:
    bip = "BIP-" + bip_dir.split("-")[1]
    for cond in CONDITIONS:
        rows.append(cell(bip, bip_dir, cond))

# validate M0 against CSV
csvm = {}
with open(r"D:\ecp-spec\experiments\validation\GO-8C\study-output\pilot_results_n12.csv", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        if r["seed_num"] == "1":
            csvm[(r["bip_id"], r["condition"])] = (float(r["s_struct"]), int(r["nodes"]), int(r["edges"]))
mismatch = [(r["bip"], r["cond"], r["M0_sstruct"], csvm[(r["bip"], r["cond"])]) for r in rows
            if (r["bip"], r["cond"]) in csvm and abs(r["M0_sstruct"] - csvm[(r["bip"], r["cond"])][0]) > 1e-9]
print("M0 vs CSV: cells=", len(rows), " mismatch=", len(mismatch))
for mm in mismatch:
    print("   MISMATCH", mm)

import json
with open(r"D:\ecp-spec\experiments\validation\GO-8D\analysis\metrics_cells.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=2, ensure_ascii=False)
print("saved: GO-8D/analysis/metrics_cells.json")

# ---------------- aggregation
metrics = ["M0_sstruct", "M1_sstruct_corr", "M2_labWL", "M3_ged", "M4_ssem_ref", "M5_fid", "M6_ent"]
print("\nmetric | cond | median | distinct/12 | min | max | range")
agg = {}
for m in metrics:
    agg[m] = {}
    for cond in CONDITIONS:
        vals = sorted(r[m] for r in rows if r["cond"] == cond)
        agg[m][cond] = vals
        print(f"{m:16s} {cond}  med={np.median(vals):.4f}  distinct={len(set(vals)):2d}/12  "
              f"min={vals[0]:.4f}  max={vals[-1]:.4f}  range={vals[-1]-vals[0]:.4f}")

# Friedman across conditions (paired by BIP)
def friedman(matrix):
    X = np.array(matrix, float)
    N, k = X.shape
    ranks = np.zeros_like(X)
    for i in range(N):
        order = np.argsort(X[i])
        rk = np.empty(k)
        rk[order] = np.arange(1, k + 1)
        ranks[i] = rk
    Rbar = ranks.mean(axis=0)
    Q = 12 * N / (k * (k + 1)) * sum((Rbar[j] - (k + 1) / 2) ** 2 for j in range(k))
    return Q

print("\nmetric | Friedman Q (paired across A/B/C) | corr with node count (all cells)")
for m in metrics:
    mat = np.array([[r[m] for r in rows if r["bip"] == b] for b in ["BIP-%03d" % i for i in range(1, 13)]])
    Q = friedman(mat)
    nc = np.array([r["nodes"] for r in rows], float)
    vv = np.array([r[m] for r in rows], float)
    corr = float(np.corrcoef(nc, vv)[0, 1]) if np.std(vv) > 0 else float("nan")
    print(f"{m:16s}  Q={Q:7.2f}  corr(nodes)={corr:+.3f}")
