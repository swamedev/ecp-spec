# GO-8B — NAMESPACE OPERATIONAL DECISION

**Data:** 2026-08-13
**Decisor:** Governança GO-8B
**Status:** **DECIDED** (operacional — não altera especificação congelada)
**Escopo:** condições de namespace do piloto GO-8B no CSV de resultados.

---

## 1. Contexto

A governança havia indicado condições A=NULL, B=SYN, C=NULL. Auditoria evidenciou que o
parser congelado `graph_from_reconstruction.py` rejeita o namespace `NULL` (C4/T_NULL):

- `04-GRAPH-FROM-RECONSTRUCTION.md` §1.1: C4/T_NULL "não produz grafo no espaço sintético
  e não é processado por este parser".
- `graph_from_reconstruction.py:84-85`: `if ns == "NULL": raise ValueError("NAMESPACE_MIX")`.

Manter A/C em `NULL` zeraria essas condições (nenhum grafo → nenhuma observação).

## 2. Evidência (CSV atual — `pilot_results.csv`)

| namespace | contagem | condições |
|-----------|----------|-----------|
| CAT | 42 | A, C |
| SYN | 21 | B |
| NULL | 0 | — |
| ECP | 0 | — |

## 3. Decisão

- **Condição A:** `CAT`
- **Condição B:** `SYN`
- **Condição C:** `CAT`

- `CAT` é aceito como **namespace operacional** para A/C, preservando as **63 execuções**
  e a matriz N×3 completa (07 §8: ≥ 5 casos válidos; 7 válidos).
- **Sem equivalência automática** entre namespaces (não há mapping C1–C4; 04 R5 M-1).
- Esta é uma **decisão operacional** para o CSV do piloto; **não altera** o núcleo congelado
  (04 §1.1 permanece: NULL não é processado).

## 4. Referências

- `04-GRAPH-FROM-RECONSTRUCTION.md` §1.1 (rejeição de C4/NULL)
- `graph_from_reconstruction.py:84-85` (NAMESPACE_MIX)
- `02-C2-PERMUTATION.md` §8 (C1=ECP, C2=CAT, C3=SYN, C4=NULL)
- `pilot-results.csv` (CAT=42 A/C, SYN=21 B)

---

**Fim da decisão. Nenhum artefato congelado alterado.