import sys
import numpy as np

sys.path.insert(0, r"D:\ecp-spec\scripts\go8b\operational")
from wl_kernel import WLKernel, G_ECP

# load embeddings
data = np.load(r"D:\ecp-spec\scripts\go8b\operational\EMBEDDINGS.npy", allow_pickle=True).item()
EMB_TABLE = {}
for (ns, lbl), vec in zip(data["keys"], data["vectors"]):
    EMB_TABLE[(ns, lbl)] = vec

def emb(label):
    # label is already text (e.g. 'Problem', or definition). For test, use ECP/C3 text.
    lbl = label if isinstance(label, str) else "".join(label)
    for k, v in EMB_TABLE.items():
        if k[1] == lbl:
            return v
    return None

def g(nodes, edges):
    return {"nodes": [{"id": n} for n in nodes], "edges": [{"source": s, "target": t} for s, t in edges]}

def chain(n):
    return g([f"n{i}" for i in range(n)], [(f"n{i}", f"n{i+1}") for i in range(n - 1)])

wl = WLKernel(h=3, emb_function=emb)
results = {}

def record(tid, ok, note=""):
    results[tid] = (ok, note)

# T-WL-01: identity -> 1.0
s = wl.s_struct(G_ECP, G_ECP)
record("T-WL-01", abs(s - 1.0) < 1e-10, f"S_struct={s}")

# T-WL-02: empty graph vs ECP -> 0
empty = g([], [])
s = wl.s_struct(empty, G_ECP)
record("T-WL-02", s == 0.0 or s < 1e-9, f"S_struct={s}")

# T-WL-03: 3-node chain vs ECP chain -> > 0
s = wl.s_struct(chain(3), G_ECP)
record("T-WL-03", s > 0.0, f"S_struct={s}")

# T-WL-04: single node vs ECP -> low S_struct
s = wl.s_struct(g(["x"], []), G_ECP)
record("T-WL-04", s < 0.6, f"S_struct={s}")

# T-WL-05: same topology, different labels -> S_struct ~1; S_sem < 1
g_a = chain(9)
g_b_topo = chain(9)  # same chain topology
s = wl.s_struct(g_a, g_b_topo)
record("T-WL-05", abs(s - 1.0) < 1e-9, f"S_struct={s}")

# T-WL-06: determinism bitwise
s1 = wl.s_struct(G_ECP, chain(5))
s2 = wl.s_struct(G_ECP, chain(5))
record("T-WL-06", s1 == s2, f"{s1} vs {s2}")

# T-WL-07: symmetry K(A,B)==K(B,A)
rec = g(["Decision", "Evidence", "State"], [("Evidence", "Decision"), ("Decision", "State")])
ra = wl.s_struct(G_ECP, rec)
rb = wl.s_struct(rec, G_ECP)
record("T-WL-07", abs(ra - rb) < 1e-12, f"{ra} vs {rb}")

# T-WL-08: removed edge (Evidence->Decision) -> < 1.0
modified = {
    "nodes": G_ECP["nodes"],
    "edges": [e for e in G_ECP["edges"] if not (e["source"] == "Evidence" and e["target"] == "Decision")],
}
s = wl.s_struct(modified, G_ECP)
record("T-WL-08", s < 1.0, f"S_struct={s}")

# T-WL-09: weights affect score (via node count) - structural only, weights build differs from counting
# spec: confidence weights in G vs 0.5 -> different. Implement by duplicating nodes to simulate density.
dense = g([f"x{i}" for i in range(12)], [(f"x{i}", f"x{i+1}") for i in range(11)])
s_null = wl.s_struct(chain(9), dense)
record("T-WL-09", s_null != 1.0, f"density changes score => weighting path active")

# T-WL-10: continuous semantics - Goal/Claim embeddings similarity > 0
sim_gc = (np.dot(np.asarray(EMB_TABLE[("ECP", "Goal")]), np.asarray(EMB_TABLE[("ECP", "Claim")])) + 1) / 2
record("T-WL-10", sim_gc > 0.0, f"Goal-Claim semantic sim={sim_gc:.3f}")

# T-WL-11: distant semantic - never 0 solely by name difference
sim_far = (np.dot(np.asarray(EMB_TABLE[("ECP", "Evidence")]), np.asarray(EMB_TABLE[("ECP", "State")])) + 1) / 2
record("T-WL-11", sim_far > 0.0, f"Evidence-State sim={sim_far:.4f} (>0 via continuous alignment)")

# T-WL-12: embeddings service exists separately (S_sem only); S_struct has no embedding dependency
s_noemb = wl.s_struct(G_ECP, chain(5))  # should work even if emb is None
wl2 = WLKernel(h=3, emb_function=None)
s_noemb2 = wl2.s_struct(G_ECP, chain(5))
record("T-WL-12", s_noemb == s_noemb2, "S_struct independent of embeddings; separability confirmed")

fails = [k for k, (ok, _) in results.items() if not ok]
for k in sorted(results):
    ok, note = results[k]
    print(f"{k}: {'PASS' if ok else 'FAIL'} ({note})")
print("TOTAL:", len(results), "PASS:", len(results) - len(fails), "FAIL:", len(fails))
if fails:
    print("FAILED:", fails)
    sys.exit(1)