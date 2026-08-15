# -*- coding: utf-8 -*-
"""
GO-8D — Generate 108 deterministic study seeds (seed_master=20260815, governance-approved).
PCG64 via SeedSequence(20260815, spawn_key=(bip_idx, cond_idx)), 3 uint64 per cell.
Writes: study-output/seeds_g8d.py  (structure seeds[bip][cond] = {seed1,seed2,seed3})
"""
import os
import numpy as np

SEED_MASTER = 20260815
CONDITIONS = ["A", "B", "C"]
BIPS = ["BIP-%03d" % i for i in range(1, 13)]

seeds = {}
for bi, bip in enumerate(BIPS):
    seeds[bip] = {}
    for ci, cond in enumerate(CONDITIONS):
        ss = np.random.SeedSequence(SEED_MASTER, spawn_key=(bi, ci))
        rng = np.random.Generator(np.random.PCG64(ss))
        vals = [int.from_bytes(rng.bytes(8), "little") for _ in range(3)]
        seeds[bip][cond] = {"seed%d" % j: v for j, v in enumerate(vals, start=1)}

# uniqueness check
all_seeds = [v for c in seeds.values() for s in c.values() for v in s.values()]
assert len(all_seeds) == 108, "expected 108 seeds"
assert len(set(all_seeds)) == 108, "seeds not unique"

out_dir = r"D:\ecp-spec\experiments\validation\GO-8D\study-output"
os.makedirs(out_dir, exist_ok=True)
lines = ["# GO-8D study seeds - PCG64(seed_master=20260815), isolated streams per (bip, cond)",
         "", "SEED_MASTER = 20260815", "", "seeds = {"]
for bip in BIPS:
    lines.append("    %r: {" % bip)
    for cond in CONDITIONS:
        s = seeds[bip][cond]
        lines.append("        %r: {%r: %d, %r: %d, %r: %d}," %
                     (cond, "seed1", s["seed1"], "seed2", s["seed2"], "seed3", s["seed3"]))
    lines.append("    },")
lines.append("}")

with open(os.path.join(out_dir, "seeds_g8d.py"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print("Generated 108 unique seeds (seed_master=20260815)")
print("saved: GO-8D/study-output/seeds_g8d.py")
for bip in BIPS:
    print("  %s A=%d B=%d C=%d" % (bip, seeds[bip]["A"]["seed1"], seeds[bip]["B"]["seed1"], seeds[bip]["C"]["seed1"]))