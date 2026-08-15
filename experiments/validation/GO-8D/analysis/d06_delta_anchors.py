import json, numpy as np
rows = json.load(open(r'D:\ecp-spec\experiments\validation\GO-8D\analysis\redesign_cells.json', encoding='utf-8'))

def zclip(x):
    return max(0.0, min(1.0, x))

def comp(r):
    return (r['conf'] + zclip(r['ged_ref']) + r['ent']) / 3.0

by = {c: [comp(r) for r in rows if r['cond'] == c] for c in ['A', 'B', 'C']}
for c in ['A', 'B', 'C']:
    v = np.array(sorted(by[c]))
    print(f"{c}: median={np.median(v):.4f} mean={v.mean():.4f} sd={v.std():.4f} iqr={v[-6]-v[0]:.4f} n={len(v)}")

pairs = [('A', 'B'), ('B', 'C'), ('A', 'C')]
print("\nPairwise median differences (scale 0..1):")
for a, b in pairs:
    va = np.array(by[a]); vb = np.array(by[b])
    # paired differences (same BIP)
    ab = {r['bip']: comp(r) for r in rows if r['cond'] == a}
    bb = {r['bip']: comp(r) for r in rows if r['cond'] == b}
    diffs = np.array([ab[k] - bb[k] for k in ab if k in bb])
    print(f"  {a}-{b}: med_diff={np.median(diffs):+.4f} |mean_diff|={abs(diffs.mean()):.4f} "
          f"sd_diff={diffs.std():.4f} range_diff={diffs.max()-diffs.min():.4f}")

# Cohen-style anchors on pooled SD
allv = np.array([comp(r) for r in rows])
print(f"\nGlobal: mean={allv.mean():.4f} sd={allv.std():.4f}")
for f in [0.2, 0.25, 0.33, 0.5]:
    print(f"  {f}*global_sd = {f*allv.std():.4f}")
for f in [0.05, 0.075, 0.10, 0.15]:
    print(f"  fraction_of_scale {f} = {f:.3f}")
