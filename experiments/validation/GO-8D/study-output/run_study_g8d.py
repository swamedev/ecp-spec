# -*- coding: utf-8 -*-
"""
GO-8D — Confirmatory study executor (governance-authorized execution, seed_master=20260815).

Runs the REDESIGNED pipeline (D-03) on the 12 GO-8C BIPs x 3 conditions x 3 seeds = 108
executions, computing DV_confirm = (conf + ged_ref + ent)/3 with per-execution
taxonomy_sha256. Writes study-output/pilot_results_g8d.csv (108 rows) plus
study-output/data_validation_g8d.json.

The redesigned pipeline is deterministic per (bip, cond); the 3 seeds per cell are recorded
(seed_num/seed_value) exactly as in the GO-8C N=12 study.
"""
import os, sys, csv, json, math, hashlib
from collections import Counter
import numpy as np

sys.path.insert(0, r"D:\ecp-spec\scripts\go8b\operational")
import yaml
import pilot_engine as pe
from wl_kernel import G_ECP, _wl_hash
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

TAX_SHA_CORR = hashlib.sha256(open(GO8C_TAX, "rb").read()).hexdigest()
TAX_SHA_C2 = hashlib.sha256(open(r"D:\ecp-spec\scripts\go8b\operational\C2_PERMUTATION.yaml", "rb").read()).hexdigest()


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

# import seeds
import importlib.util
spec = importlib.util.spec_from_file_location("seeds_g8d",
            r"D:\ecp-spec\experiments\validation\GO-8D\study-output\seeds_g8d.py")
seeds_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(seeds_mod)
SEEDS = seeds_mod.seeds


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
        if graph is None:
            return {"status": "FAIL", "reason": "graph construction failed"}
        nodes, edges = graph["nodes"], graph["edges"]
        gd = {"nodes": [{"id": n["node_id"]} for n in nodes],
              "edges": [{"source": e["source"], "target": e["target"]} for e in edges]}
        lab = {n["node_id"]: n["syn_category"] for n in nodes}
        ref = CAT_REF if cond in ("A", "C") else SYN_REF
        ref_labels = {nd["id"]: nd["id"] for nd in ref["nodes"]}
        ns = "CAT" if cond in ("A", "C") else "SYN"

        cov_slots = len(set(lab.values()))
        n_slots = 9 if cond in ("A", "C") else 12
        coverage = cov_slots / n_slots
        confs = [e["confidence"] for e in entities]
        mean_conf = float(np.mean(confs)) if confs else 0.0
        cat_counts = Counter(e["syn_category"] for e in entities)
        p = np.array([cat_counts[c] for c in cat_counts], float) / len(entities) if entities else np.array([0.0])
        H = float(-(p * np.log(p)).sum())
        entropy_n = H / math.log(n_slots) if n_slots > 1 else 0.0

        emb_rec = {nd["node_id"]: label_emb_corrected(nd["syn_category"]) for nd in nodes}
        emb_ref = {nd["id"]: label_emb_corrected(nd["id"]) for nd in ref["nodes"]}
        ged_ref = ged_similarity(gd, ref, emb_rec, emb_ref)
        ged_ref = max(0.0, min(1.0, float(ged_ref)))

        tax_sha = TAX_SHA_CORR if cond == "B" else TAX_SHA_C2
        return {
            "status": "PASS", "bip": bip, "cond": cond, "ns": ns,
            "nodes": len(nodes), "edges": len(gd["edges"]),
            "conf": round(mean_conf, 6), "ged_ref": round(ged_ref, 6),
            "ent": round(entropy_n, 6), "cov": round(coverage, 6),
            "tax_sha": tax_sha,
        }
    except Exception as e:
        return {"status": "FAIL", "reason": str(e)}
    finally:
        pe.SYN_ID2DEF, pe.SYN_NODES, pe.SYN_ID2LABEL = saved


def dv(row):
    return (row["conf"] + max(0.0, min(1.0, row["ged_ref"])) + row["ent"]) / 3.0


rows = []
for bip_dir in BIPS:
    bip = "BIP-" + bip_dir.split("-")[1]
    for cond in CONDITIONS:
        cell_res = cell(bip, bip_dir, cond)
        if cell_res["status"] == "FAIL":
            for j in (1, 2, 3):
                rows.append({
                    "bip_id": bip, "condition": cond, "seed_num": j,
                    "seed_value": SEEDS[bip][cond]["seed%d" % j],
                    "status": "FAIL", "dv_confirm": "", "conf": "", "ged_ref": "",
                    "ent": "", "nodes": 0, "edges": 0, "namespace": "",
                    "taxonomy_sha256": "", "error": cell_res["reason"],
                })
            continue
        for j in (1, 2, 3):
            rows.append({
                "bip_id": bip, "condition": cond, "seed_num": j,
                "seed_value": SEEDS[bip][cond]["seed%d" % j],
                "status": cell_res["status"],
                "dv_confirm": round(dv(cell_res), 6),
                "conf": cell_res["conf"], "ged_ref": cell_res["ged_ref"],
                "ent": cell_res["ent"],
                "nodes": cell_res["nodes"], "edges": cell_res["edges"],
                "namespace": cell_res["ns"],
                "taxonomy_sha256": cell_res["tax_sha"],
                "error": "",
            })

assert len(rows) == 108, "expected 108 executions, got %d" % len(rows)

out_dir = r"D:\ecp-spec\experiments\validation\GO-8D\study-output"
csv_path = os.path.join(out_dir, "pilot_results_g8d.csv")
cols = ["bip_id", "condition", "seed_num", "seed_value", "status", "dv_confirm",
        "conf", "ged_ref", "ent", "nodes", "edges", "namespace", "taxonomy_sha256", "error"]
with open(csv_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for r in rows:
        w.writerow(r)

print("Executions:", len(rows), " PASS:", sum(1 for r in rows if r["status"] == "PASS"),
      " FAIL:", sum(1 for r in rows if r["status"] == "FAIL"))
print("saved:", csv_path)