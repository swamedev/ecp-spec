# GO-8B — CURRENT BLOCKER

## P1-C2-01 — C2 seed / permutation divergence

### Observed

`02-C2-PERMUTATION.md` is internally coherent in §5 table, §5 permutation and §6 JSON, but the documented seed does not reproduce that permutation under the documented PCG64 algorithm.

### Values

Registered seed:
`11473621728585666159`

Hex:
`0x9F3A7E2C1B8D4E6F`

PCG64(seed registered):
`[1,5,0,4,3,8,6,2,7]`

Frozen permutation:
the table/§6 mapping.

PCG64(258915):
`[1,5,6,3,7,0,4,8,2]`
which reproduces the frozen table.

Declared inverse in §5:
`[5,0,8,3,7,1,6,4,2]`

True inverse:
`[5,0,8,3,6,1,2,4,7]`

§6 JSON:
reported as internally correct.

## Why STOP

The operator cannot choose silently between:
- authoritative frozen mapping;
- registered seed.

Neither should be changed without governance.

## Current options

### A — Frozen mapping as operational truth
Generate C2 artifact from §6 mapping; document seed discrepancy as residual repair debt requiring future version/Lock.

### B — Seed 258915 as operational truth
Requires formal correction to frozen configuration and a new version/Lock.

### C — Stop P1
Resolve the inconsistency through a correction cycle before producing C2.

No option is currently marked DECIDED in this continuity package.
