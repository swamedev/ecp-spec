# GO-8B — INFRAESTRUTURA OPERACIONAL P1–P4: RELATÓRIO DE VALIDAÇÃO

**Data:** 2026-08-12
**Autoridade:** DECISION — PILOT AUTHORIZED — GO-8B + DECISION P1-C2-01 (opção A) + P5-INPUT-MATERIALS
**Estado:** Infraestrutura reproduzível P1–P4 VALIDADA. Nenhum experimento executado. Nenhum artefato congelado alterado.

---

## 1. Resumo

| Item | Artefato | Resultado |
|---|---|---|
| **P1** | `C2_PERMUTATION.yaml` + `.json` | Validação de consistência: **7/7 PASS** (biunívoco, completo, namespace CAT, consistente com perm §5 e tabela de posições) |
| **P2** | `C3_TAXONOMY.yaml` + `.json` | **NT-01/02/03/04 PASS**; NT-05 **PENDING** (validadores humanos) |
| **P2** | `BIP-VAL_REPORT.yaml` | **Verdict PENDING** (conforme 03 §4.4: aprovação exige NT-05) |
| **P3** | `graph_from_reconstruction.py` | **T-GFR-01..21: 21/21 PASS** |
| **P4** | `wl_kernel.py` + `EMBEDDINGS.npy` (dim 384, 30 vetores) | **T-WL-01..12: 12/12 PASS** |

**Consolidado:** 5/5 suítes PASS (arena `p_run_consolidated.py`).

---

## 2. Achados (registrados, NÃO corrigidos no congelado)

| ID | Severidade | Descrição |
|---|---|---|
| **P1-C2-01** | DIVERGÊNCIA (parcial, resolvida por governance) | Seed registrada 11473621728585666159 **não reproduz** a tabela congelada §5/§6 sob PCG64 §3.1; `PCG64(258915)` reproduz. `DECISION P1-C2-01 opção A`: mapping §6 é a fonte operacional autoritativa; seed marcada `REGISTERED-NON-REPRODUCING`; array "inversa" §5 corrompido também não corrigido in-place. Reparação seed→permutação adiada a ciclo posterior. |
| **FINDING-BIP-VAL-01** | OBSERVAÇÃO | 03 §4.2 cita "lista fixa de 47 termos", mas nenhuma lista existe em artefato congelado. Compilação operacional do vocabulário ECP-000..010 → **52 termos**. Registrada; não forçada a 47. NT-01 validado sobre a lista compilada. |
| **FINDING-R9-01** (pré-existente) | OBSERVAÇÃO | Ambiente verificado: numpy 1.26.4, scipy 1.15.3, pandas 3.0.5, Python 3.11.9. Agregados nesta validação: PyYAML 6.0.2, scikit-learn 1.7.2, networkx 3.4.2, jsonschema 4.25.0, sentence-transformers 3.3.1 + `all-MiniLM-L6-v2` (frozen model). |

---

## 3. Nada de novo no núcleo congelado

- Nenhum arquivo de `experiments/validation/GO-8B/` (00–08) foi modificado.
- Nenhum hash congelado alterado; `HASH STATUS: PENDING LOCK PROTOCOL` mantido para os novos artefatos operacionais.
- Nenhum Lock novo aplicado.

---

## 4. Artefatos operacionais produzidos (fora do escopo congelado)

```
scripts/go8b/operational/
├── C2_PERMUTATION.yaml / .json         (P1)
├── C3_TAXONOMY.yaml / .json            (P2)
├── BIP-VAL_REPORT.yaml                 (P2)
├── graph_from_reconstruction.py        (P3)
├── wl_kernel.py                        (P4)
├── EMBEDDINGS.npy / EMBEDDINGS.yaml    (P4)
├── p1_c2_permutation.py                (gerador/validador P1)
├── p2_c3_taxonomy.py                   (gerador/validador P2)
├── p2_bip_val_report.py                (gerador BIP-VAL)
├── p3_tests_gfr.py                     (T-GFR-01..21)
├── p4_generate_embeddings.py           (gerador embeddings)
├── p4_tests_wl.py                      (T-WL-01..12)
└── p_run_consolidated.py               (suíte consolidada)
```

---

## 5. Bloqueadores restantes para EXECUÇÃO

| # | Item | Estado |
|---|---|---|
| 1 | **NT-05** (BIP-VAL) — 3 validadores humanos independentes | **PENDING** |
| 2 | **P5** — materiais de entrada dos 7 BIPs (reconstrução independente) | **AUSENTE** (5/7 sem material; decisão de governança: reconstruir) |
| 3 | `C2`/`C3` mecanismos validados por terceira parte (auditor) | Não realizado ainda |
| 4 | Registro das 3 seeds por célula (7 BIPs × 3 condições × 3 seeds) | Sem execução (depende de P5) |