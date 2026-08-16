# GO-8B PILOT — EVIDENCE & STOP REPORT (before statistical analysis)

**Status: STOP** — two anomalies block authorization for statistical analysis.
Rule applied: *"núcleo congelado intocável, zero atalhos, qualquer anomalia = STOP e reporte"* (PILOT-AUTHORIZED-GO-8B.md).
No statistical analysis was run. No frozen protocol file was modified.

---

## 1. Evidence item 1 — CSV sample (first 10 lines)

Source: `experiments/validation/GO-8B/pilot-output/pilot_results.csv` (63 rows).

| bip_id | condition | seed_num | seed_value | status | s_struct | s_sem | nodes | edges | namespace | validation |
|--------|-----------|----------|------------|--------|----------|-------|-------|-------|-----------|------------|
| BIP-001 | A | 1 | AC3467ED2EF4DEA7 | PASS | 0.5875 | 0.5534 | 9 | 51 | CAT | PASS |
| BIP-001 | A | 2 | ... | PASS | ... | ... | 9 | ... | CAT | PASS |
| BIP-001 | A | 3 | ... | PASS | ... | ... | 9 | ... | CAT | PASS |
| BIP-001 | B | 1 | ... | PASS | 0.58 | 0.5558 | 6 | ... | SYN | PASS |
| BIP-001 | B | 2 | ... | PASS | ... | ... | 6 | ... | SYN | PASS |
| BIP-001 | B | 3 | ... | PASS | ... | ... | 6 | ... | SYN | PASS |
| BIP-001 | C | 1 | ... | PASS | 0.5721 | 0.5474 | 9 | 40 | CAT | PASS |
| BIP-001 | C | 2 | ... | PASS | ... | ... | 9 | ... | CAT | PASS |
| BIP-001 | C | 3 | ... | PASS | ... | ... | 9 | ... | CAT | PASS |
| BIP-002 | A | 1 | ... | PASS | 0.5875 | 0.5527 | 9 | ... | CAT | PASS |

---

## 2. Evidence item 1 — means table per BIP × condition (median-of-3 = cells used by stats, mean shown here)

| BIP | Cond A s_sem | Cond B s_sem | Cond C s_sem | Cond A s_struct | Cond B s_struct | Cond C s_struct |
|-----|--------------|--------------|--------------|-----------------|-----------------|-----------------|
| BIP-001 | 0.5534 | 0.5558 | 0.5474 | 0.5875 | 0.5800 | 0.5721 |
| BIP-002 | 0.5527 | 0.5507 | 0.5513 | 0.5875 | 0.5905 | 0.5875 |
| BIP-003 | 0.5533 | 0.5606 | 0.5482 | 0.5875 | 0.5950 | 0.5676 |
| BIP-004 | 0.5491 | 0.5526 | 0.5439 | 0.5875 | 0.7500 | 0.5866 |
| BIP-005 | 0.5484 | 0.5528 | 0.5527 | 0.6828 | 0.5721 | 0.5676 |
| BIP-006 | 0.5546 | 0.5551 | 0.5591 | 0.5875 | 0.6364 | 0.5676 |
| BIP-007 | 0.5477 | 0.5518 | 0.5534 | 0.6383 | 0.5875 | 0.5821 |

---

## 3. Evidence item 1 — no-identical-values check (within same condition, across BIPs)

- **s_sem (all conditions): PASS** — all 21 cells distinct (0.5439–0.5606). No identical values between different BIPs in the same condition.
- **s_struct cond B: PASS** — 7 distinct values.
- **s_struct cond A: FAIL** — value **0.5875** repeats in BIP-001, BIP-002, BIP-003, BIP-004, BIP-006 (5 of 7 BIPs identical).
- **s_struct cond C: FAIL** — value **0.5676** repeats in BIP-003, BIP-005, BIP-006.

**Anomaly 1:** identical s_struct values between different BIPs in the same condition, explicitly forbidden by governance requirement 01 ("confirme que não há valores idênticos entre BIPs diferentes na mesma condição"). Noted: s_struct is the primary confirmatory DV per 06 §1.2.

---

## 4. Evidence item 2 — namespace confirmation

Namespace counts in CSV (63 rows):

| namespace | count | present in conditions |
|-----------|-------|-----------------------|
| CAT | 42 | A, C |
| SYN | 21 | B |
| NULL | 0 | — |
| ECP | 0 | — |

**Anomaly 2 (BLOCKING):** governance asserts **A = NULL, C = NULL, B = SYN**.
CSV shows A = CAT, C = CAT, B = SYN.

The current mapping originates in `pilot_engine.py build_graph()`:
- condition A -> (`"CAT"`, `"T_PERM-v1"`)
- condition B -> (`"SYN"`, `"C3_TAXONOMY-v1"`)
- condition C -> (`"CAT"`, `"T_PERM-v1"`)

This follows the **frozen** taxonomy protocol:
- `02-C2-PERMUTATION.md`: C1=T_ECP→ECP, **C2=T_PERM→CAT**, C3=T_SYNTH→SYN, C4=T_NULL→NULL.
- `04-GRAPH-FROM-RECONSTRUCTION.md` §1.1: C4/T_NULL **"não produz grafo no espaço sintético e não é processada por este parser"**.
- `graph_from_reconstruction.py` lines 84–85: `if ns == "NULL": raise ValueError("NAMESPACE_MIX")`.

**Direct contradiction:** governance now requires A=NULL and C=NULL, but the frozen, untouchable parser rejects NULL with `NAMESPACE_MIX` and produces no graph/metrics for those conditions. Applying NULL to A/C as-is would yield 0 graphs and 0 rows — no s_sem/s_struct at all. The frozen core is "intocável" (untouchable). This cannot be corrected without either (a) violating the frozen protocol or (b) re-generating conditions A/C under a different namespace decision.

---

## 5. Evidence item 3 — code evidence (compute_s_metrics + embeddings)

`pilot_engine.py`:

```python
def compute_s_metrics(graph, condition, ent_vectors=None):
    ...
    wl = WLKernel(h=3, emb_function=label_emb)
    # Content vector per reconstructed node = mean of its entities' real text vectors
    node_labels_rec = {}
    for nd in nodes:
        src_ids = nd.get("source_entities", [])
        if ent_vectors and src_ids:
            vecs = [ent_vectors[s] for s in src_ids if s in ent_vectors]
            if vecs:
                node_labels_rec[nd["node_id"]] = _norm(np.mean(vecs, axis=0))
                continue
        node_labels_rec[nd["node_id"]] = label_emb(nd["syn_category"])
    node_labels_ecp = {nd["id"]: nd["label"] for nd in G_ECP["nodes"]}
    ...
    s_struct = wl.s_struct(graph_data, G_ECP)
    s_sem = wl.semantic_similarity(graph_data, G_ECP, node_labels_rec, ...)
```

Embedding engine (`text_emb`, lines ~174–206): lazy-loaded
`sentence-transformers/all-MiniLM-L6-v2` via `get_model()` with `_MODEL`/`_EMB_CACHE`;
applied to real reconstructed text (Atomic Facts content / narrative text).
Confirmed against the standalone model test: same real text pair -> cos ≈ 0.368 (model-based),
while the old token-hash `text_emb` produced cos = 1.0 (broken, replaced).
So s_sem genuinely varies from real BIP content (19/21 distinct cells), not a constant fallback.

---

## 6. Decision requested

Because governance rule 02 ("namespace NULL") conflicts with the frozen parser rule
(04 §1.1 + `graph_from_reconstruction.py:84-85` raising `NAMESPACE_MIX` for NULL),
and because anomaly 1 (identical s_struct within conditions) is an explicit non-authorization
condition, **statistical analysis is NOT authorized at this point**.

I stop and request an explicit governance decision on:

1. **Namespace resolution:** Should the frozen protocol's C2/T_PERM→CAT apply to conditions A/C
   (as currently implemented and as the docs' only processing path), i.e. keep A=CAT, C=CAT?
   Or does governance intend NULL to mean "no taxonomy namespace recorded but still produce
   the graph under the existing parser" (requires a reinterpretation)? A direct A=NULL/C=NULL
   execution is impossible without touching the frozen parser.
2. **s_struct duplicate handling:** whether the identical s_struct within condition A/C is
   acceptable (structural metric invariance for same-topology cases) or mandates a change.

Awaiting decision — no further execution performed.