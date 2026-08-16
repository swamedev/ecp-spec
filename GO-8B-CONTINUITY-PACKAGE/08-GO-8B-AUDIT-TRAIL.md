# GO-8B — AUDIT TRAIL SUMMARY

## R1
Initial methodological preparation and Decision Record basis.

## R2
Audit found:
- missing R1 Decision Record;
- C2×C3 integration ambiguity;
- no blocker in S_struct/S_sem;
- TOST decision required;
- no invented hashes.

Verdict:
STOP / DECISION REQUIRED.

## R3
Decision Record reconstructed; C2/C3 namespace isolation applied; TOST and STAT-10 handled.

Status:
STOP / PENDING AUDIT.

## R4
Audit found 3 MAJORs:
- M-1 schema;
- M-2 global test;
- M-3 seeds/power.

## R5
Resolved M-1/M-2/M-3.
Power simulation:
- 5k MC;
- seed 20260811;
- 3 seeds/cell;
- N=7 power ≈0.63;
- N=12 ≈0.90.

Remaining governance decisions were R5-GOV-01..04.

## R6
R5 decisions applied.
Bootstrap coverage simulation authorized and executed:
- seed 20260812;
- B_boot=10,000;
- MC=1,500.
Verdict:
CLEAN / PASS.

## R7
Pre-registration 08 audited against 00–07.
Verdict:
PASS / CLEAN.

## R8
Lock readiness audit.
Found missing scripts/dependencies.
Decision/response led to R9 reproducibility audit.

## R9
Scripts registered:
- power simulation;
- statistical executor;
- requirements.
Power reproduction confirmed within MC error.
No experimental data.
Verdict:
PASS / CLEAN.

## Lock
Phase 1:
- pycache divergence caused STOP;
- authorized removal and clean re-run;
- 13/13 canonical byte checks passed.

Phase 2:
- 13 SHA-256 hashes;
- manifest;
- independent verification;
- Lock Record;
- final verification.
Verdict:
LOCKED / FROZEN.

## Post-lock
Pilot authorization granted.
Pre-flight found missing operational artifacts and contamination risk.

## Current
P1-C2-01 STOP.
