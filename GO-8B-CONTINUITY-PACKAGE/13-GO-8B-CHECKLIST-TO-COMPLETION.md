# GO-8B — CHECKLIST TO COMPLETION

## Phase 0 — Governance
- [ ] Resolve P1-C2-01.
- [ ] Record decision as DECIDED.
- [ ] Determine whether frozen 02 remains authoritative without change.
- [ ] If frozen 02 must change: new version + audit + re-lock.

## Phase 1 — C2
- [ ] Produce C2_PERMUTATION.yaml according to DECIDED rule.
- [ ] Validate mapping/inverse/namespaces.
- [ ] Record provenance.
- [ ] Freeze operational artifact if required.

## Phase 2 — C3
- [ ] Produce C3_TAXONOMY.yaml.
- [ ] Produce BIP-VAL_REPORT.yaml.
- [ ] Validate namespace isolation.
- [ ] Validate no C2↔C3 equivalence.

## Phase 3 — Computational pipeline
- [ ] GraphFromReconstruction implementation.
- [ ] Schema validation.
- [ ] NAMESPACE_MIX rejection tests.
- [ ] WL Kernel implementation.
- [ ] Structural metric validation.
- [ ] Semantic metric validation.
- [ ] Embeddings artifact.
- [ ] No experimental data yet unless gate explicitly permits.

## Phase 4 — Inputs
- [ ] Verify 7 BIPs.
- [ ] Verify narratives and atomic facts.
- [ ] Resolve Genoma/SX-003 contamination.
- [ ] Resolve Ebola/SX-002 legacy contamination.
- [ ] Ensure A/B/C material generation complies with frozen protocol.

## Phase 5 — Operational dry run
- [ ] Synthetic end-to-end test.
- [ ] No real experimental data.
- [ ] Validate 3 seeds/cell.
- [ ] Validate aggregation.
- [ ] Validate output schema.
- [ ] Audit.

## Phase 6 — Pilot execution
- [ ] Explicit pilot authorization confirmed.
- [ ] All preconditions PASS.
- [ ] Generate A/B/C × 3 seeds.
- [ ] Record provenance.
- [ ] Collect data.
- [ ] Do not alter frozen protocol.

## Phase 7 — Data validation
- [ ] Apply 07.
- [ ] FP/FC/FE/FR rules.
- [ ] Confirm ≥5 valid cases.
- [ ] Confirm required domain coverage.
- [ ] Record exclusions.

## Phase 8 — Analysis
- [ ] Run frozen executor.
- [ ] Friedman primary.
- [ ] Stop if global p≥.05 before post-hoc.
- [ ] Wilcoxon + Holm if allowed.
- [ ] Effects and ICs.
- [ ] Sensitivity analyses.
- [ ] No TOST.

## Phase 9 — Audit
- [ ] Reconcile data vs protocol.
- [ ] Audit deviations.
- [ ] Audit seeds.
- [ ] Audit outputs.
- [ ] Confirm no silent methodological changes.

## Phase 10 — Governance closure
- [ ] Review results.
- [ ] Decide interpretation.
- [ ] Record limitations.
- [ ] Produce final report.
- [ ] Preserve immutable audit trail.

## Completion criterion

GO-8B is not “complete” merely because the experiment ran.

Completion requires:
- execution traceable;
- data validated;
- analysis reproducible;
- deviations documented;
- governance reviewed;
- final status recorded.
