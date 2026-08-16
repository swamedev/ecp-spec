# GO-8B — ACTION QUEUE

## A0 — Resolve P1-C2-01
Status: `DECISION REQUIRED`

Precondition:
governance decision A/B/C.

Output:
formal decision record update.

---

## A1 — Produce C2_PERMUTATION.yaml
Status: `BLOCKED BY A0`

Only execute after A0.

Validation:
- exact mapping;
- namespace;
- inverse;
- no silent seed substitution;
- provenance to frozen source.

---

## A2 — Produce C3_TAXONOMY.yaml + BIP-VAL_REPORT.yaml
Status: `BLOCKED/DEPENDENT`

Validate namespace isolation and BIP coverage.

---

## A3 — Operational parser
Status: pending

Implement/validate GraphFromReconstruction according to frozen 04.

---

## A4 — WL Kernel + embeddings
Status: pending

Implement/validate according to frozen 05.

---

## A5 — Inputs / contamination
Status: pending governance/operational review

Resolve treatment of Genoma and Ebola source materials before use.

---

## A6 — Pilot execution
Status: authorized in principle, but operationally blocked by A0–A5.

Execute only after all preconditions PASS.

---

## A7 — Data validation
Run 07 criteria before statistical analysis.

---

## A8 — Statistical analysis
Use 08 exactly.

---

## A9 — Post-experiment audit
Audit data, exclusions, analysis, deviations and report.

---

## A10 — Governance closure
Decide interpretation, limitations and final status.
