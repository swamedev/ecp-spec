import hashlib
import numpy as np
from collections import Counter


def _wl_hash(label):
    if isinstance(label, tuple):
        label = str(label)
    h = hashlib.sha256(str(label).encode("utf-8")).digest()[:8]
    return h.hex()


class WLKernel:
    """05-WL-KERNEL.md: S_struct (WL subtree kernel, anonymized) + S_sem (semantic, Hungarian)."""

    def __init__(self, h=3, emb_function=None):
        self.h = h
        self.emb_function = emb_function  # callable(label) -> 384-dim vector or None

    # ---------------- S_struct ----------------
    def structural_features(self, graph):
        # graph: {"nodes": [{"id": ...}], "edges": [{"source","target"}]}
        nodes = [n["id"] for n in graph["nodes"]]
        adj_in = {n: [] for n in nodes}
        adj_out = {n: [] for n in nodes}
        for e in graph["edges"]:
            adj_out.setdefault(e["source"], []).append(e["target"])
            adj_in.setdefault(e["target"], []).append(e["source"])

        labels = {n: "neutral" for n in nodes}  # anonymization: uniform neutral
        hist_all = Counter()

        for _ in range(self.h + 1):
            hist_all.update(labels.values())
            new_labels = {}
            for v in nodes:
                ms = []
                for u in adj_in[v]:
                    ms.append((labels.get(u, "neutral"), "in"))
                for w in adj_out[v]:
                    ms.append((labels.get(w, "neutral"), "out"))
                ms_sorted = sorted(ms)
                new_labels[v] = _wl_hash((labels[v], ms_sorted))
            labels = new_labels

        # Convert to regular dict and ensure all values are valid floats
        result = {}
        for k, v in hist_all.items():
            if isinstance(v, Counter):
                v = v[0]  # Get first element
            if isinstance(v, (int, float)) and not (np.isnan(v) or np.isinf(v)):
                result[k] = float(v)
            else:
                result[k] = 0.0

        return result

    def s_struct(self, g1, g2):
        f1 = self.structural_features(g1)
        f2 = self.structural_features(g2)
        keys = set(f1) | set(f2)
        v1 = [f1.get(k, 0.0) for k in keys]
        v2 = [f2.get(k, 0.0) for k in keys]
        dot = sum(a * b for a, b in zip(v1, v2))
        n1 = sum(a * a for a in v1) ** 0.5
        n2 = sum(b * b for b in v2) ** 0.5
        if n1 == 0 or n2 == 0:
            return 0.0
        return dot / (n1 * n2)

    # ---------------- S_sem ----------------
    def _cos(self, a, b):
        import numpy as np
        a = np.asarray(a, dtype=float).flatten()
        b = np.asarray(b, dtype=float).flatten()

        # Check for NaN or infinite values
        if np.any(np.isnan(a)) or np.any(np.isinf(a)):
            return 0.0
        if np.any(np.isnan(b)) or np.any(np.isinf(b)):
            return 0.0

        na, nb = np.linalg.norm(a), np.linalg.norm(b)
        if na == 0 or nb == 0:
            return 0.0
        result = float(np.dot(a, b) / (na * nb))

        # Check for NaN or infinite result
        if np.isnan(result) or np.isinf(result):
            return 0.0

        return result

    def semantic_similarity(self, g_rec, g_ecp, node_labels_rec, node_labels_ecp, edge_labels_rec, edge_labels_ecp):
        import numpy as np
        emb = self.emb_function
        rec_nodes = [n["id"] for n in g_rec["nodes"]]
        ecp_nodes = [n["id"] for n in g_ecp["nodes"]]

        # node similarity matrix (continuous, no hard constraint)
        sim = np.zeros((len(rec_nodes), len(ecp_nodes)))
        for i, rn in enumerate(rec_nodes):
            e_r = emb(node_labels_rec[rn])
            for j, en in enumerate(ecp_nodes):
                e_e = emb(node_labels_ecp[en])
                s = (self._cos(e_r, e_e) + 1) / 2.0
                sim[i, j] = s

        # Hungarian: maximize sum
        from scipy.optimize import linear_sum_assignment
        cost = -sim
        ri, ci = linear_sum_assignment(cost)
        matched_node_sims = sim[ri, ci]

        # edge similarity (reduced weight, diagnostic only)
        rec_edges = [(e["source"], e["target"]) for e in g_rec["edges"]]
        ecp_edges = [(e["source"], e["target"]) for e in g_ecp["edges"]]
        matched_edge_sims = []
        if rec_edges and ecp_edges:
            e_sim = np.zeros((len(rec_edges), len(ecp_edges)))
            for a, ra in enumerate(rec_edges):
                e_ra = emb(edge_labels_rec.get(ra, ""))
                if e_ra is None:
                    continue
                for b, eb in enumerate(ecp_edges):
                    e_eb = emb(edge_labels_ecp.get(eb, ""))
                    if e_eb is None:
                        continue
                    e_sim[a, b] = (self._cos(e_ra, e_eb) + 1) / 2.0
            ea, eb2 = linear_sum_assignment(-e_sim)
            matched_edge_sims = e_sim[ea, eb2]

        w_V, w_E = 1.0, 0.5
        mean_v = float(np.mean(matched_node_sims)) if len(matched_node_sims) else 0.0
        mean_e = float(np.mean(matched_edge_sims)) if matched_edge_sims is not None and len(matched_edge_sims) > 0 else 0.0
        return (w_V * mean_v + w_E * mean_e) / (w_V + w_E)

    def semantic_similarity_with_af_ids(self, g_rec, g_ecp, node_labels_rec, node_labels_ecp, edge_labels_rec, edge_labels_ecp, node_af_ids, emb_function):
        """
        Compute semantic similarity using AF IDs instead of labels to get variation between BIPs.
        
        Args:
            g_rec: graph from GraphFromReconstruction
            g_ecp: ECP reference graph
            node_labels_rec: dict mapping node_id to syn_category (labels)
            node_labels_ecp: dict mapping ECP node_id to ECP labels
            edge_labels_rec: dict mapping (source, target) to relation_type
            edge_labels_ecp: dict mapping ECP (source, target) to ECP edge labels
            node_af_ids: dict mapping node_id to list of AF IDs (for embedding)
            emb_function: function to generate embeddings from AF IDs
        """
        import numpy as np
        
        rec_nodes = [n["id"] for n in g_rec["nodes"]]
        ecp_nodes = [n["id"] for n in g_ecp["nodes"]]
        
        # node similarity matrix using AF IDs for embedding
        sim = np.zeros((len(rec_nodes), len(ecp_nodes)))
        for i, rn in enumerate(rec_nodes):
            af_ids = node_af_ids.get(rn, [])
            if af_ids:
                # Use average embedding of first AF ID if available
                emb_rec = emb_function(af_ids[0])
            else:
                emb_rec = np.array([0.0] * 768)
            
            for j, en in enumerate(ecp_nodes):
                e_ecp = emb_function(node_labels_ecp.get(en, ""))
                if np.any(np.isnan(e_ecp)) or np.any(np.isinf(e_ecp)):
                    sim[i, j] = 0.0
                    continue
                
                s = (self._cos(emb_rec, e_ecp) + 1) / 2.0
                sim[i, j] = s
        
        # Hungarian: maximize sum
        from scipy.optimize import linear_sum_assignment
        cost = -sim
        ri, ci = linear_sum_assignment(cost)
        matched_node_sims = sim[ri, ci]
        
        # edge similarity (reduced weight, diagnostic only)
        rec_edges = [(e["source"], e["target"]) for e in g_rec["edges"]]
        ecp_edges = [(e["source"], e["target"]) for e in g_ecp["edges"]]
        matched_edge_sims = []
        if rec_edges and ecp_edges:
            e_sim = np.zeros((len(rec_edges), len(ecp_edges)))
            for a, ra in enumerate(rec_edges):
                af_ids = node_af_ids.get(ra, [])
                if af_ids:
                    emb_rec = emb_function(af_ids[0])
                else:
                    emb_rec = np.array([0.0] * 768)
                
                for b, eb in enumerate(ecp_edges):
                    e_eb = emb_function(edge_labels_ecp.get(eb, ""))
                    if np.any(np.isnan(e_eb)) or np.any(np.isinf(e_eb)):
                        e_sim[a, b] = 0.0
                        continue
                    
                    e_sim[a, b] = (self._cos(emb_rec, e_eb) + 1) / 2.0
            ea, eb2 = linear_sum_assignment(-e_sim)
            matched_edge_sims = e_sim[ea, eb2]
        
        w_V, w_E = 1.0, 0.5
        mean_v = float(np.mean(matched_node_sims)) if len(matched_node_sims) else 0.0
        mean_e = float(np.mean(matched_edge_sims)) if matched_edge_sims is not None and len(matched_edge_sims) > 0 else 0.0
        return (w_V * mean_v + w_E * mean_e) / (w_V + w_E)

    def combined(self, s_struct, s_sem, alpha=0.6):
        return alpha * s_struct + (1 - alpha) * s_sem


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