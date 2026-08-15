# -*- coding: utf-8 -*-
"""
GO-8D D-03 — redesigned-pipeline simulation on GO-8C N=12 data (read-only).
Tests the redesigned metric components (de-anonymized WL, corrected CAT/SYN
embeddings, weighted GED, fact fidelity, coverage/entropy) on the 36 existing
cells. Writes nothing to GO-8B/GO-8C. Output to stdout only.
"""
import sys, os, csv, math, hashlib
from collections import Counter
import numpy as np

OP = r"D:\ecp-spec\scripts\go8b\operational"
sys.path.insert(0, OP)
import yaml
import pilot_engine as pe
from wl_kernel import WLKernel, G_ECP, _wl_hash
from scipy.optimize import linear_sum_assignment

GO8C_TAX = r"D:\ecp-spec\experiments\validation\GO-8C\scripts\C3_TAXONOMY.yaml"
with open(GO8C_TAX, encoding="utf-8") as f:
    C3_CORR = yaml.safe_load(f)
SYN_ID2DEF_CORR = {n["id"]: n["definition"] for n in C3_CORR["taxonomy"]["nodes"]}
SYN_EDGES = [(e["from"], e["to"]) for e in C3_CORR["taxonomy"]["edges"]]
SYN_IDS = [n["id"] for n in C3_CORR["taxonomy"]["nodes"]]

with open(r"D:\ecp-spec\scripts\go8b\operational\C2_PERMUTATION.yaml", encoding="utf-8") as f:
    C2 = yaml.safe_load(f)
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

# ---------------- corrected label embeddings (redesign deliverable) ----------------
def label_emb_corrected(label):
    """CAT -> neutral PT definition; SYN -> corrected definition; ECP -> frozen name emb."""
    if isinstance(label, np.ndarray):
        return pe._norm(label)
    if not isinstance(label, str):
        return np.zeros(384)
    if label in CANON:
        return pe._norm(pe.EMB_TABLE.get(("ECP", label)))
    if label in O2C:                                   # CAT-XX
        return pe.text_emb(pe.CAT_NEUTRAL_DEFS[O2C[label]])
    if label in SYN_ID2DEF_CORR:                       # SYN-XX
        return pe.text_emb(SYN_ID2DEF_CORR[label])
    return np.zeros(384)

def _cos(a, b):
    a = np.asarray(a, float).flatten(); b = np.asarray(b, float).flatten()
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    return float(np.dot(a, b) / (na * nb)) if na and nb else 0.0

# ---------------- labeled WL kernel (de-anonymized; normalized option) ----------------
def wl_hist(graph, labels, h=3, normalize=False):
    nodes = [n["id"] for n in graph["nodes"]]
    adj_in = {n: [] for n in nodes}; adj_out = {n: [] for n in nodes}
    for e in graph["edges"]:
        adj_out.setdefault(e["source"], []).append(e["target"])
        adj_in.setdefault(e["target"], []).append(e["source"])
    cur = {n: labels.get(n, "neutral") for n in nodes}
    hist = Counter()
    for _ in range(h + 1):
        hist.update(cur.values())
        new = {}
        for v in nodes:
            ms = [(cur.get(u, "neutral"), "in") for u in adj_in[v]] + \
                 [(cur.get(w, "neutral"), "out") for w in adj_out[v]]
            new[v] = _wl_hash((cur[v], sorted(ms)))
        cur = new
    if normalize:
        tot = sum(hist.values())
        return {k: v / tot for k, v in hist.items()} if tot else {}
    return dict(hist)

def cos_hist(h1, h2):
    keys = set(h1) | set(h2)
    v1 = np.array([h1.get(k, 0.0) for k in keys], float)
    v2 = np.array([h2.get(k, 0.0) for k in keys], float)
    if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
        return 0.0
    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

# ---------------- weighted GED (redesign: corrected embeddings) ----------------
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

# ---------------- corrected S_sem (Hungarian + corrected embeddings) ----------------
def s_sem_corrected(g_rec, g_ref, lab_rec, lab_ref, emb_fn, edge_lab_rec, edge_lab_ref, w_E=0.5):
    rn = [n["id"] for n in g_rec["nodes"]]
    en = [n["id"] for n in g_ref["nodes"]]
    sim = np.zeros((len(rn), len(en)))
    for i, r in enumerate(rn):
        e_r = emb_fn(lab_rec.get(r, ""))
        for j, e in enumerate(en):
            e_e = emb_fn(lab_ref.get(e, ""))
            sim[i, j] = (_cos(e_r, e_e) + 1) / 2.0
    ri, ci = linear_sum_assignment(-sim)
    mean_v = float(np.mean(sim[ri, ci])) if len(ri) else 0.0
    re = [(e["source"], e["target"]) for e in g_rec["edges"]]
    ee = [(e["source"], e["target"]) for e in g_ref["edges"]]
    mean_e = 0.0
    if re and ee:
        es = np.zeros((len(re), len(ee)))
        for a, ra in enumerate(re):
            era = emb_fn(edge_lab_rec.get(ra, ""))
            for b, eb in enumerate(ee):
                eeb = emb_fn(edge_lab_ref.get(eb, ""))
                es[a, b] = (_cos(era, eeb) + 1) / 2.0
        ea, eb2 = linear_sum_assignment(-es)
        mean_e = float(np.mean(es[ea, eb2]))
    return (mean_v + w_E * mean_e) / (1.0 + w_E)

# ---------------- data ----------------
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

def taxonomy_sha():
    return hashlib.sha256(open(GO8C_TAX, "rb").read()).hexdigest()[:16]

def cell(bip, bip_dir, cond):
    saved = (pe.SYN_ID2DEF, pe.SYN_NODES, pe.SYN_ID2LABEL)
    if cond == "B":
        pe.SYN_ID2DEF = SYN_ID2DEF_CORR
        pe.SYN_NODES = C3_CORR["taxonomy"]["nodes"]
        pe.SYN_ID2LABEL = {n["id"]: n["label"] for n in pe.SYN_NODES}
    try:
        narr, af = resolve(bip_dir)
        units = pe.parse_atomic_facts(af) if cond in ("A", "B") else pe.parse_narrative(narr)
        entities, relations, ent_vectors = pe.build_entities_relations(units, cond)
        graph = pe.build_graph(entities, relations, cond, bip)
        nodes, edges = graph["nodes"], graph["edges"]
        gd = {"nodes": [{"id": n["node_id"]} for n in nodes],
              "edges": [{"source": e["source"], "target": e["target"]} for e in edges]}
        lab = {n["node_id"]: n["syn_category"] for n in nodes}
        ref = CAT_REF if cond in ("A", "C") else SYN_REF
        ref_labels = {nd["id"]: nd["id"] for nd in ref["nodes"]}

        # granularity-standardized components
        cov_slots = len(set(lab.values()))
        n_slots = 9 if cond in ("A", "C") else 12
        coverage = cov_slots / n_slots
        confs = [e["confidence"] for e in entities]
        mean_conf = float(np.mean(confs))
        cat_counts = Counter(e["syn_category"] for e in entities)
        p = np.array([cat_counts[c] for c in cat_counts], float) / len(entities)
        H = float(-(p * np.log(p)).sum())
        entropy_n = H / math.log(n_slots) if n_slots > 1 else 0.0

        emb_rec = {nd["node_id"]: label_emb_corrected(nd["syn_category"]) for nd in nodes}
        emb_ref = {nd["id"]: label_emb_corrected(nd["id"]) for nd in ref["nodes"]}
        emb_ecp = {e["id"]: label_emb_corrected(e["id"]) for e in G_ECP["nodes"]}

        r2_raw = cos_hist(wl_hist(gd, lab), wl_hist(ref, ref_labels))
        r2_norm = cos_hist(wl_hist(gd, lab, normalize=True), wl_hist(ref, ref_labels, normalize=True))
        s4_ged_ecp = ged_similarity(gd, ECP_REF, emb_rec, emb_ecp)
        s4_ged_ref = ged_similarity(gd, ref, emb_rec, emb_ref)
        edge_lab_rec = {(e["source"], e["target"]): e["relation_type"] for e in edges}
        edge_lab_ref = {(e["source"], e["target"]): "precedes" for e in ref["edges"]}
        s5_ssem = s_sem_corrected(gd, G_ECP, lab, {nd["id"]: nd["id"] for nd in G_ECP["nodes"]},
                                  label_emb_corrected, edge_lab_rec,
                                  {(e["source"], e["target"]): e["label"] for e in G_ECP["edges"]})

        return {
            "bip": bip, "cond": cond, "nodes": len(nodes), "edges": len(gd["edges"]),
            "cov": coverage, "conf": mean_conf, "ent": entropy_n,
            "wl_raw": r2_raw, "wl_norm": r2_norm,
            "ged_ecp": s4_ged_ecp, "ged_ref": s4_ged_ref, "ssem_corr": s5_ssem,
            "tax_sha": taxonomy_sha(),
        }
    finally:
        pe.SYN_ID2DEF, pe.SYN_NODES, pe.SYN_ID2LABEL = saved

rows = []
for bip_dir in BIPS:
    bip = "BIP-" + bip_dir.split("-")[1]
    for cond in CONDITIONS:
        rows.append(cell(bip, bip_dir, cond))

import json
json.dump(rows, open(r"D:\ecp-spec\experiments\validation\GO-8D\analysis\redesign_cells.json", "w", encoding="utf-8"),
          indent=2, ensure_ascii=False)
print("saved: GO-8D/analysis/redesign_cells.json  (cells=%d)" % len(rows))

# taxonomy hash traceability (BIP-007-B fix)
shas = {}
for r in rows:
    shas.setdefault((r["cond"], r["tax_sha"]), []).append(r["bip"])
print("\nTaxonomy hash (traceability):")
for k, v in sorted(shas.items()):
    print("  cond=%s sha=%s -> %d cells (BIP-007-B included: %s)" % (k[0], k[1], len(v), "BIP-007" in v))

metrics = ["cov", "conf", "ent", "wl_raw", "wl_norm", "ged_ecp", "ged_ref", "ssem_corr"]
print("\nmetric      | cond | med    | distinct/12 | min    | max    | range")
for m in metrics:
    for cond in CONDITIONS:
        vals = sorted(r[m] for r in rows if r["cond"] == cond)
        print("%-11s  %s   med=%.4f  distinct=%2d/12  min=%.4f  max=%.4f  range=%.4f" %
              (m, cond, np.median(vals), len(set(vals)), vals[0], vals[-1], vals[-1] - vals[0]))

def friedman(mat):
    X = np.array(mat, float)
    N, k = X.shape
    ranks = np.zeros_like(X)
    for i in range(N):
        order = np.argsort(X[i]); rk = np.empty(k); rk[order] = np.arange(1, k + 1); ranks[i] = rk
    Rbar = ranks.mean(axis=0)
    return 12 * N / (k * (k + 1)) * sum((Rbar[j] - (k + 1) / 2) ** 2 for j in range(k))

bip_ids = ["BIP-%03d" % i for i in range(1, 13)]
print("\nmetric      | Friedman Q | corr(nodes)")
for m in metrics:
    mat = np.array([[r[m] for r in rows if r["bip"] == b] for b in bip_ids])
    Q = friedman(mat)
    nc = np.array([r["nodes"] for r in rows], float)
    vv = np.array([r[m] for r in rows], float)
    corr = float(np.corrcoef(nc, vv)[0, 1]) if np.std(vv) > 0 else float("nan")
    print("%-11s  %7.2f   %+.3f" % (m, Q, corr))

# composite candidates (standardized, all in [0,1])
def zclip(x):
    return max(0.0, min(1.0, x))

def composite(row, w):
    comps = [row["cov"], row["conf"], zclip(row["ged_ecp"]), row["ent"]]
    return sum(w[i] * comps[i] for i in range(4)) / sum(w)

print("\nComposite candidates (weights cov, conf, ged_ecp, ent):")
for name, w in [("EQ-1", [1, 1, 1, 1]), ("GED-2", [1, 1, 2, 1]), ("FID-3", [1, 2, 1, 1])]:
    for cond in CONDITIONS:
        vals = sorted(composite(r, w) for r in rows if r["cond"] == cond)
        print("  %-6s %s med=%.4f distinct=%2d/12" % (name, cond, np.median(vals), len(set(vals))))
    mat = np.array([[composite(r, w) for r in rows if r["bip"] == b] for b in bip_ids])
    print("  %-6s Friedman Q=%.2f" % (name, friedman(mat)))
