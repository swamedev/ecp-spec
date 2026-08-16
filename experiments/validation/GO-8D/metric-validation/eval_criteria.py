# -*- coding: utf-8 -*-
"""
GO-8D METRIC VALIDATION — M-04 comparison + 7 criteria + synthetic sanity checks.
Reads metric-validation/calibration_cells.json.
"""
import json
import sys
import math
import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, r"D:\ecp-spec\scripts\go8b\operational")
from wl_kernel import G_ECP
ECP_REF = {"nodes": [{"id": n["id"]} for n in G_ECP["nodes"]],
           "edges": [{"source": e["source"], "target": e["target"]} for e in G_ECP["edges"]]}

rows = json.load(open(r"D:\ecp-spec\experiments\validation\GO-8D\metric-validation\calibration_cells.json", encoding="utf-8"))
rows = [r for r in rows if r["ok"]]
df = pd.DataFrame(rows)
COND = ["A", "B", "C"]

DVS = ["dv0", "dv1", "dv2", "dv3"]
DV_NAMES = {
    "dv0": "DV0 original  (ent_orig n_slots 9/12 + ged_orig CAT/SYN)",
    "dv1": "DV1 ent recalibrada (ent_n12 denom comum + ged_orig)",
    "dv2": "DV2 ged recalibrada (ged_ecp ref comum ECP + ent_orig)",
    "dv3": "DV3 completa (ent_n12 + ged_ecp)",
}
COMP = {"conf": "conf", "ged_orig": "ged_orig", "ged_ecp": "ged_ecp",
        "ent_orig": "ent_orig", "ent_n12": "ent_n12", "ent_n9": "ent_n9", "ent_eff": "ent_eff",
        "H": "H", "k_obs": "k_obs"}

def med(sub, col):
    return float(sub[col].median())

def bminusa(df, col):
    a = df[df.cond == "A"].set_index("bip")[col]
    b = df[df.cond == "B"].set_index("bip")[col]
    return (b - a).dropna()

def n_neg(s):
    return int((s < 0).sum())

print("=== per-condition medians: DVs ===")
for dv in DVS:
    d = bminusa(df, dv)
    print("  %-5s A=%.4f B=%.4f C=%.4f | B-A=%.4f (B<A: %d/12)" % (
        dv, med(df[df.cond=='A'], dv), med(df[df.cond=='B'], dv), med(df[df.cond=='C'], dv),
        d.median(), n_neg(d)))

print("\n=== per-condition medians: components ===")
for comp in ["conf", "ged_orig", "ged_ecp", "ent_orig", "ent_n12", "ent_n9", "ent_eff", "H", "k_obs"]:
    d = bminusa(df, comp)
    print("  %-9s A=%.4f B=%.4f C=%.4f | B-A=%.4f (B<A: %d/12)" % (
        comp, med(df[df.cond=='A'], comp), med(df[df.cond=='B'], comp), med(df[df.cond=='C'], comp),
        d.median(), n_neg(d)))

# Friedman per candidate DV (same as study pipeline, cell-level, N=12)
def friedman_p(df, col):
    mat = np.zeros((12, 3))
    for i, bip in enumerate(sorted(df.bip.unique())):
        for j, c in enumerate(COND):
            mat[i, j] = df[(df.bip == bip) & (df.cond == c)][col].iloc[0]
    chi2, p = stats.friedmanchisquare(*[mat[:, j] for j in range(3)])
    return chi2, float(p)

print("\n=== Friedman per candidate DV (df=2) ===")
for dv in DVS:
    chi2, p = friedman_p(df, dv)
    print("  %-5s chi2=%.2f p=%.6f  reject=%s" % (dv, chi2, p, p < 0.05))

# CRITERIA
print("\n=== CRITERIA ===")
crit = {}

# C1 invariance of scale between conditions (component ranges comparable)
print("\nC1. Scale invariance between conditions (component min/max per cond):")
c1 = {}
for comp in ["conf", "ged_orig", "ged_ecp", "ent_orig", "ent_n12"]:
    ranges = {c: (df[df.cond==c][comp].min(), df[df.cond==c][comp].max()) for c in COND}
    spread = max(r[1]-r[0] for r in ranges.values())
    overlap = True
    c1[comp] = {c: [round(ranges[c][0],3), round(ranges[c][1],3)] for c in COND}
    print("  %-9s ranges A%s B%s C%s  max_spread=%.3f" % (comp,
          str(c1[comp]["A"]), str(c1[comp]["B"]), str(c1[comp]["C"]), spread))
crit["C1"] = c1

# C2 same reference cardinality
print("\nC2. Same reference cardinality A/B/C:")
print("  ent: n_slots_orig A/C=9 B=12 (FAIL); ent_n12 all=12 (PASS); ent_eff all=log(k_obs) (PASS if k comparable)")
print("  ged: ged_orig CAT(9n) vs SYN(12n) (FAIL); ged_ecp ECP(9n) all (PASS)")
crit["C2"] = {"ent_orig": "n_slots 9 vs 12 (FAIL)", "ent_n12": "common 12 (PASS)",
              "ged_orig": "CAT 9n vs SYN 12n (FAIL)", "ged_ecp": "ECP 9n common (PASS)"}

# C3 no known structural advantage
print("\nC3. Absence of known structural advantage:")
# for ent: max possible entropy normalized depends on denominator; check ceiling
print("  ent_n12 max possible = 1.0 for all (no advantage); ent_orig max = log(9)/log(9)=1 for A/C, log(12)/log(12)=1 for B but H max differs")
print("  ent_eff: max=1.0 for all by construction (normalizes by observed support)")
print("  ged_ecp: same reference for all (no size advantage); ged_orig: SYN ref larger -> B deflated (known advantage)")
crit["C3"] = {"ent_n12": "no size advantage (PASS)", "ent_eff": "normalizes by observed support (PASS)",
              "ged_ecp": "common ref (PASS)", "ged_orig": "SYN 12n vs CAT 9n (FAIL)"}

# C4 interpretability
print("\nC4. Interpretability:")
print("  ent_n12: entropy as fraction of log(12) categories; interpretable as 'how spread across the 12-slot taxonomy'")
print("  ent_eff: entropy / log(observed support) = 1 for uniform over observed; interpretable as 'evenness'")
print("  ged_ecp: structural+semantic similarity to canonical ECP; interpretable")
crit["C4"] = {"ent_n12": "spread over 12-slot taxonomy", "ent_eff": "evenness over observed support",
              "ged_ecp": "similarity to canonical ECP"}

# C5 stability per BIP (variance of component across BIPs within cond)
print("\nC5. Stability per BIP (within-cond std across 12 BIPs):")
c5 = {}
for comp in ["conf", "ged_orig", "ged_ecp", "ent_orig", "ent_n12"]:
    stds = {c: float(df[df.cond==c][comp].std()) for c in COND}
    c5[comp] = stds
    print("  %-9s std A=%.4f B=%.4f C=%.4f" % (comp, stds["A"], stds["B"], stds["C"]))
crit["C5"] = c5

# C6 ability to distinguish better/worse reconstructions
print("\nC6. Distinguishing ability:")
# use synthetic ground truth below + discrimination = correlation with H/conf range; here:
# report coefficient of variation per DV across all cells
for dv in DVS:
    cv = df[dv].std() / df[dv].mean()
    print("  %-5s CV(all 36 cells)=%.4f" % (dv, cv))
# Friedman separability of conditions as discrimination proxy
for dv in DVS:
    chi2, p = friedman_p(df, dv)
    print("  %-5s Friedman chi2=%.2f p=%.6f" % (dv, chi2, p))
crit["C6"] = "see Friedman chi2 per DV + synthetic checks below"

# C7 synthetic known data behavior (below)

# ---- SYNTHETIC SANITY CHECKS ----
print("\n=== C7. SYNTHETIC BEHAVIOR (known data) ===")
from scipy.optimize import linear_sum_assignment

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

def label_emb_corrected(label):
    import sys
    sys.path.insert(0, r"D:\ecp-spec\scripts\go8b\operational")
    import pilot_engine as pe
    import yaml
    C3 = yaml.safe_load(open(r"D:\ecp-spec\experiments\validation\GO-8C\scripts\C3_TAXONOMY.yaml", encoding="utf-8"))
    SYN_D = {n["id"]: n["definition"] for n in C3["taxonomy"]["nodes"]}
    C2 = yaml.safe_load(open(r"D:\ecp-spec\scripts\go8b\operational\C2_PERMUTATION.yaml", encoding="utf-8"))
    CANON = C2["canonical_order"]; O2C = C2["opaque_to_canonical"]
    if isinstance(label, np.ndarray):
        return pe._norm(label)
    if not isinstance(label, str):
        return np.zeros(384)
    if label in CANON:
        return pe._norm(pe.EMB_TABLE.get(("ECP", label)))
    if label in O2C:
        return pe.text_emb(pe.CAT_NEUTRAL_DEFS[O2C[label]])
    if label in SYN_D:
        return pe.text_emb(SYN_D[label])
    return np.zeros(384)

def fake_cell(cond, kind):
    """Synthetic graph with known structure. kind: 'perfect','noisy','flat','collapse'."""
    sys.path.insert(0, r"D:\ecp-spec\scripts\go8b\operational")
    import pilot_engine as pe
    import yaml
    C3 = yaml.safe_load(open(r"D:\ecp-spec\experiments\validation\GO-8C\scripts\C3_TAXONOMY.yaml", encoding="utf-8"))
    SYN_D = {n["id"]: n["definition"] for n in C3["taxonomy"]["nodes"]}
    C2 = yaml.safe_load(open(r"D:\ecp-spec\scripts\go8b\operational\C2_PERMUTATION.yaml", encoding="utf-8"))
    O2C = C2["opaque_to_canonical"]; CANON = C2["canonical_order"]
    ref = ECP_REF
    n = 9
    ids = ["n%d" % i for i in range(n)]
    # perfect: nodes map 1:1 to ECP canonical ids, chain edges
    if kind == "perfect":
        labels = {ids[i]: CANON[i] for i in range(n)}
        edges = [(ids[i], ids[i+1]) for i in range(n-1)]
        confs = [1.0]*n
    elif kind == "noisy":
        labels = {ids[i]: ("CAT-%02d" % i) for i in range(n)}  # CAT opaque labels
        edges = [(ids[i], ids[i+1]) for i in range(n-1)]
        confs = [0.5]*n
    elif kind == "flat":
        labels = {ids[i]: CANON[i % 2] for i in range(n)}  # only 2 categories
        edges = [(ids[i], ids[i+1]) for i in range(n-1)]
        confs = [0.9]*n
    elif kind == "collapse":
        labels = {ids[i]: CANON[0] for i in range(n)}  # all same category
        edges = [(ids[i], ids[i+1]) for i in range(n-1)]
        confs = [0.9]*n
    g = {"nodes": [{"id": i} for i in ids], "edges": [{"source": s, "target": t} for s, t in edges]}
    lab = {i: labels[i] for i in ids}
    cat_counts = {labels[i]: 0 for i in ids}
    from collections import Counter
    cc = Counter(labels.values())
    p = np.array([cc[c] for c in cc], float) / n
    H = float(-(p*np.log(p)).sum())
    k_obs = len(cc)
    ent_n12 = H/math.log(12); ent_n9 = H/math.log(9); ent_eff = H/math.log(k_obs) if k_obs > 1 else 0.0
    emb_rec = {i: label_emb_corrected(labels[i]) for i in ids}
    emb_ref = {nd["id"]: label_emb_corrected(nd["id"]) for nd in ref["nodes"]}
    ged_ecp = ged_similarity(g, ref, emb_rec, emb_ref)
    conf = float(np.mean(confs))
    return {"conf": conf, "ged_ecp": ged_ecp, "ent_n12": ent_n12, "ent_n9": ent_n9,
            "ent_eff": ent_eff, "H": H, "k_obs": k_obs, "kind": kind, "cond": cond}

import math
print("\nSynthetic expectations:")
print("  perfect > noisy (conf, ged),  perfect > flat > collapse (ent)")
syn_rows = []
for kind in ["perfect", "noisy", "flat", "collapse"]:
    r = fake_cell("A", kind)
    syn_rows.append(r)
    print("  %-9s conf=%.3f ged_ecp=%.3f ent_n12=%.3f ent_eff=%.3f H=%.3f k_obs=%d" % (
        kind, r["conf"], r["ged_ecp"], r["ent_n12"], r["ent_eff"], r["H"], r["k_obs"]))
crit["C7"] = syn_rows

json.dump({"criteria": crit},
          open(r"D:\ecp-spec\experiments\validation\GO-8D\metric-validation\criteria_eval.json", "w", encoding="utf-8"),
          indent=2, ensure_ascii=False)
print("\nsaved metric-validation/criteria_eval.json")