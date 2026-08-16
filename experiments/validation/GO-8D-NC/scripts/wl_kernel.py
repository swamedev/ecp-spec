# -*- coding: utf-8 -*-
"""
GO-8D-NC — wl_kernel (self-contained, D-03 redesign).

Redesigned WL kernel:
  P1 (D-03 §3.1): labeled WL variant — structural_features(graph, labels=None) uses real
  category labels when provided, falls back to "neutral" only when absent (backward-compatible).
  GED (D-03 §3.2 / DV3 M-02): ged_similarity() against a common reference graph (ECP chain).

No runtime dependency on GO-8B/GO-8C/GO-8D. Self-contained.
"""
import hashlib
import numpy as np


def _wl_hash(label):
    if isinstance(label, tuple):
        label = str(label)
    h = hashlib.sha256(str(label).encode("utf-8")).digest()[:8]
    return h.hex()


class WLKernel:
    """Weisfeiler-Lehman histogram kernel with optional real category labels."""

    def __init__(self, h=3, emb_function=None):
        self.h = h
        self.emb_function = emb_function  # callable(label) -> vector or None

    def structural_features(self, graph, labels=None):
        """P1 (D-03 §3.1): labeled WL. labels: dict node_id -> category label (or None)."""
        nodes = [n["id"] for n in graph["nodes"]]
        adj_in = {n: [] for n in nodes}
        adj_out = {n: [] for n in nodes}
        for e in graph["edges"]:
            adj_out.setdefault(e["source"], []).append(e["target"])
            adj_in.setdefault(e["target"], []).append(e["source"])

        cur = {n: (labels or {}).get(n, "neutral") for n in nodes}
        hist = {}
        for _ in range(self.h + 1):
            for v, lbl in cur.items():
                hist[lbl] = hist.get(lbl, 0.0) + 1.0
            new = {}
            for v in nodes:
                ms = [(cur.get(u, "neutral"), "in") for u in adj_in[v]] + \
                     [(cur.get(w, "neutral"), "out") for w in adj_out[v]]
                new[v] = _wl_hash((cur[v], sorted(ms)))
            cur = new
        return {k: float(v) for k, v in hist.items()}

    def s_struct(self, g1, g2, labels1=None, labels2=None):
        f1 = self.structural_features(g1, labels1)
        f2 = self.structural_features(g2, labels2)
        keys = set(f1) | set(f2)
        v1 = np.array([f1.get(k, 0.0) for k in keys], float)
        v2 = np.array([f2.get(k, 0.0) for k in keys], float)
        n1, n2 = np.linalg.norm(v1), np.linalg.norm(v2)
        if n1 == 0 or n2 == 0:
            return 0.0
        return float(np.dot(v1, v2) / (n1 * n2))


def _cos(a, b):
    a = np.asarray(a, float).flatten()
    b = np.asarray(b, float).flatten()
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    return float(np.dot(a, b) / (na * nb)) if na and nb else 0.0


def ged_similarity(g_rec, g_ref, emb_rec, emb_ref, w_edge=0.5):
    """GED-normalized similarity vs a reference graph (DV3 M-02: common ECP reference).

    Node substitution cost = 1 - cos(embedding); node ins/del = 1; edge ins/del weighted.
    Returns similarity in [0,1] (1 = identical under mapping).
    """
    from scipy.optimize import linear_sum_assignment
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
    edge_del = len(mapped - ref_edges)
    edge_add = len(ref_edges - mapped)
    edge_cost = w_edge * (edge_del + edge_add)
    max_cost = (n + m) + w_edge * (len(rec_edges) + len(ref_edges))
    return 1.0 - (node_cost + edge_cost) / max_cost if max_cost else 1.0


# Canonical ECP reference chain (9 nodes, 8 edges) — common reference for A/B/C (DV3 M-02).
G_ECP = {
    "nodes": [
        {"id": "Problem", "label": "Problem"},
        {"id": "Goal", "label": "Goal"},
        {"id": "Claim", "label": "Claim"},
        {"id": "Knowledge", "label": "Knowledge"},
        {"id": "Assumption", "label": "Assumption"},
        {"id": "Evidence", "label": "Evidence"},
        {"id": "Decision", "label": "Decision"},
        {"id": "State", "label": "State"},
        {"id": "Artifact", "label": "Artifact"},
    ],
    "edges": [
        {"source": "Problem", "target": "Goal", "label": "precedes"},
        {"source": "Goal", "target": "Claim", "label": "precedes"},
        {"source": "Claim", "target": "Knowledge", "label": "precedes"},
        {"source": "Knowledge", "target": "Assumption", "label": "precedes"},
        {"source": "Assumption", "target": "Evidence", "label": "precedes"},
        {"source": "Evidence", "target": "Decision", "label": "precedes"},
        {"source": "Decision", "target": "State", "label": "precedes"},
        {"source": "State", "target": "Artifact", "label": "precedes"},
    ],
}


def ecp_ref_graph():
    """Id-only graph view of G_ECP (used as the common DV3 reference)."""
    return {
        "nodes": [{"id": n["id"]} for n in G_ECP["nodes"]],
        "edges": [{"source": e["source"], "target": e["target"]} for e in G_ECP["edges"]],
    }
