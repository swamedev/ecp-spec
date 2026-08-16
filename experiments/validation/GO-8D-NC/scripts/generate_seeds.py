# -*- coding: utf-8 -*-
"""
GO-8D-NC — Generate 270 deterministic study seeds.

seed_master = 20260816 (D-MV-04 governance decision; distinct from GO-8D 20260815).
PCG64 via SeedSequence(20260816, spawn_key=(bip_idx, cond_idx)), 3 uint64 per cell.
Writes: GO-8D-NC/scripts/seeds_nc.py  (structure seeds[bip][cond] = {seed1,seed2,seed3})

Per D-MV-04: final seeds are generated only AFTER this script is run with governance
authorization. The script is provided now; it is NOT executed during Lock Phase 1.
"""
import os
import numpy as np

SEED_MASTER = 20260816
CONDITIONS = ["A", "B", "C"]
BIPS = ["BIP-%03d" % i for i in range(1, 31)]

seeds = {}
for bi, bip in enumerate(BIPS):
    seeds[bip] = {}
    for ci, cond in enumerate(CONDITIONS):
        ss = np.random.SeedSequence(SEED_MASTER, spawn_key=(bi, ci))
        rng = np.random.Generator(np.random.PCG64(ss))
        vals = [int.from_bytes(rng.bytes(8), "little") for _ in range(3)]
        seeds[bip][cond] = {"seed%d" % j: v for j, v in enumerate(vals, start=1)}

all_seeds = [v for c in seeds.values() for s in c.values() for v in s.values()]
assert len(all_seeds) == 270, "expected 270 seeds"
assert len(set(all_seeds)) == 270, "seeds not unique"

HERE = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(HERE, "seeds_nc.py")
lines = ["# GO-8D-NC study seeds - PCG64(seed_master=20260816), isolated streams per (bip, cond)",
         "", "SEED_MASTER = 20260816", "", "seeds = {"]
for bip in BIPS:
    lines.append("    %r: {" % bip)
    for cond in CONDITIONS:
        s = seeds[bip][cond]
        lines.append("        %r: {%r: %d, %r: %d, %r: %d}," %
                     (cond, "seed1", s["seed1"], "seed2", s["seed2"], "seed3", s["seed3"]))
    lines.append("    },")
lines.append("}")

with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print("Generated 270 unique seeds (seed_master=20260816)")
print("saved:", out_path)
