# -*- coding: utf-8 -*-
"""GO-8D D-03 — supplementary: entity-level labeled WL + within-category coherence."""
import sys, os, math
from collections import Counter, defaultdict
import numpy as np
import json

sys.path.insert(0, r"D:\ecp-spec\scripts\go8b\operational")
import yaml
import pilot_engine as pe
from wl_kernel import _wl_hash

GO8C_TAX = r"D:\ecp-spec\experiments\validation\GO-8C\scripts\C3_TAXONOMY.yaml"
C3_CORR = yaml.safe_load(open(GO8C_TAX, encoding="utf-8"))
SYN_ID2DEF_CORR = {n["id"]: n["definition"] for n in C3_CORR["taxonomy"]["nodes"]}
C2 = yaml.safe_load(open(r"D:\ecp-spec\scripts\go8b\operational\C2_PERMUTATION.yaml", encoding="utf-8"))
O2C = C2["opaque_to_canonical"]

def label_emb_corrected(label):
    if label in O2C:
        return pe.text_emb(pe.CAT_NEUTRAL_DEFS[O2C[label]])
    if label in SYN_ID2DEF_CORR:
        return pe.text_emb(SYN_ID2DEF_CORR[label])
    return pe._norm(pe.EMB_TABLE.get(("ECP", label)))

def wl_hist(graph, labels, h=3, normalize=False):
    nodes = list(graph.keys())
    adj_in = defaultdict(list); adj_out = defaultdict(list)
    for (s, t) in graph["edges"]:
        adj_out[s].append(t); adj_in[t].append(s)
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

STUDY = r"D:\ecp-spec\experiments\validation\GO-8C\study-input"
BIPS = ["BIP-001-deepwater", "BIP-002-hyatt", "BIP-003-ows", "BIP-004-genoma",
        "BIP-005-evergiven", "BIP-006-i35w", "BIP-007-ebola", "BIP-008-apollo13",
        "BIP-009-chernobyl", "BIP-010-tacomanarrows", "BIP-011-dominos", "BIP-012-eyjafjallajokull"]

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

rows = []
for bip_dir in BIPS:
    bip = "BIP-" + bip_dir.split("-")[1]
    saved = (pe.SYN_ID2DEF, pe.SYN_NODES)
    pe.SYN_ID2DEF = SYN_ID2DEF_CORR
    pe.SYN_NODES = C3_CORR["taxonomy"]["nodes"]
    try:
        narr, af = resolve(bip_dir)
        for cond in ["A", "B", "C"]:
            units = pe.parse_atomic_facts(af) if cond in ("A", "B") else pe.parse_narrative(narr)
            entities, relations, ent_vectors = pe.build_entities_relations(units, cond)
            # entity-level graph (NO collapse)
            g = {"nodes": [e["entity_id"] for e in entities],
                 "edges": [(r["source"], r["target"]) for r in relations]}
            lab = {e["entity_id"]: e["syn_category"] for e in entities}
            # WL on entity-level graph, labels = category
            wl_e = wl_hist(g, lab, normalize=True)
            # reference: category-collapsed graph of THIS cell (best possible within-namespace)
            cats_used = sorted(set(lab.values()))
            gc = {"nodes": cats_used, "edges": []}
            for (s, t) in g["edges"]:
                cs, ct = lab[s], lab[t]
                if cs != ct and (cs, ct) not in gc["edges"]:
                    gc["edges"].append((cs, ct))
            wl_c = wl_hist(gc, {c: c for c in cats_used}, normalize=True)
            entity_level_score = cos_hist(wl_e, wl_c)  # label-aware, no taxonomy needed
            # within-category coherence (label-aware, reference-free)
            by_cat = defaultdict(list)
            for e in entities:
                by_cat[e["syn_category"]].append(ent_vectors[e["entity_id"]])
            sims_in = []
            for c, vs in by_cat.items():
                if len(vs) > 1:
                    for i in range(len(vs)):
                        for j in range(i + 1, len(vs)):
                            sims_in.append(float(np.dot(vs[i], vs[j])))
            allv = [ent_vectors[e["entity_id"]] for e in entities]
            sims_cross = []
            for i in range(len(allv)):
                for j in range(i + 1, len(allv)):
                    if lab[entities[i]["entity_id"]] != lab[entities[j]["entity_id"]]:
                        sims_cross.append(float(np.dot(allv[i], allv[j])))
            mean_in = float(np.mean(sims_in)) if sims_in else 0.0
            mean_cross = float(np.mean(sims_cross)) if sims_cross else 0.0
            rows.append({"bip": bip, "cond": cond,
                         "wl_entity_norm": entity_level_score,
                         "coh_in": mean_in, "coh_cross": mean_cross,
                         "coh_delta": max(0.0, mean_in - mean_cross)})
    finally:
        pe.SYN_ID2DEF, pe.SYN_NODES = saved

json.dump(rows, open(r"D:\ecp-spec\experiments\validation\GO-8D\analysis\redesign_cells2.json", "w", encoding="utf-8"),
          indent=2, ensure_ascii=False)

for m in ["wl_entity_norm", "coh_in", "coh_cross", "coh_delta"]:
    for cond in ["A", "B", "C"]:
        vals = sorted(r[m] for r in rows if r["cond"] == cond)
        print("%-14s %s med=%.4f distinct=%2d/12 min=%.4f max=%.4f" %
              (m, cond, np.median(vals), len(set(round(v, 4) for v in vals)), vals[0], vals[-1]))

def friedman(mat):
    X = np.array(mat, float); N, k = X.shape
    ranks = np.zeros_like(X)
    for i in range(N):
        order = np.argsort(X[i]); rk = np.empty(k); rk[order] = np.arange(1, k + 1); ranks[i] = rk
    Rbar = ranks.mean(axis=0)
    return 12 * N / (k * (k + 1)) * sum((Rbar[j] - (k + 1) / 2) ** 2 for j in range(k))

bips = ["BIP-%03d" % i for i in range(1, 13)]
print("\nFriedman Q (A/B/C):")
for m in ["wl_entity_norm", "coh_in", "coh_cross", "coh_delta"]:
    mat = np.array([[r[m] for r in rows if r["bip"] == b] for b in bips])
    print("  %-14s Q=%.2f" % (m, friedman(mat)))
