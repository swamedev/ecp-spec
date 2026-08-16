# BIP-006 — I-35W Bridge

**Caso:** Colapso da ponte I-35W sobre o rio Mississippi, Minneapolis (2007)
**Status (P5):** MATERIAIS PRODUZIDOS (condições A/B/C) — aguarda validação pós-produção
**Escopo da coleta:** 2 origens primárias obtidas; demais fontes do plano facultativas em ciclo posterior.

## Conteúdo

- `sources/00-index.md` — fronteira pré/pós gate + registros e checksums das fontes
- `sources/01-origem-dos-documentos.md` — proveniência EI (SC-5)
- `sources/raw/` — 2 PDFs oficiais com checksum
- `narrative/01-narrativa-original.md` — condição C (zero ECP)
- `atomic-facts/02-atomic-facts.md` — condições A/B (zero ECP, fatos mínimos)

## Entrada por condição

| Condição | Entrada |
|---|---|
| A (cega pura) | `atomic-facts/02-atomic-facts.md` |
| B (cega + C3) | `atomic-facts/02-atomic-facts.md` + `scripts/go8b/operational/C3_TAXONOMY.yaml` |
| C (não-cega) | `narrative/01-narrativa-original.md` |

## Fontes (origens independentes, SC-5)

| ref | Fonte |
|---|---|
| `ntsb-01-har0803` | NTSB, Collapse of I-35W Highway Bridge, Minneapolis, Minnesota, August 1, 2007 (NTSB/HAR-08/03), 2008 |
| `mngov-01-gpm` | Gray Plant Mooty, Investigative Report to Joint Committee to Investigate the I-35W Bridge Collapse, 2008 (encomendado pela legislatura de Minnesota) |

## Regras

- Zero termos ECP (vocabulário ECP-000..010, 52 termos).
- Rastreabilidade 100% → `sources/01-origem-dos-documentos.md`.
- Nenhum conteúdo de SX-001/002/003 importado.

## Autoridade

DECISION P5-INPUT-MATERIALS; produção em ordem do manifest §3 (BIP-006).
