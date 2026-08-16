# BIP-005 — Ever Given / Suez

**Caso:** Ever Given — Canal de Suez (2021)
**Status (P5):** MATERIAIS PRODUZIDOS (condições A/B/C) — aguarda validação pós-produção
**Escopo da coleta:** 2 origens primárias obtidas; demais fontes do plano facultativas em ciclo posterior.

## Conteúdo

- `sources/00-index.md` — fronteira pré/pós gate + registros e checksums das fontes
- `sources/01-origem-dos-documentos.md` — proveniência EI (SC-5)
- `sources/raw/` — 1 PDF oficial (PMA) + 1 HTML de declarações (UK P&I), com checksum
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
| `pma-01-ever-given` | Autoridade Marítima do Panamá, Marine Safety Investigation Report — Grounding of MV Ever Given (R-026-2021-DIAM, IMO 9811000), 2021/2023 |
| `ukpandi-01-media` | UK P&I Club, série de declarações públicas sobre o encalhe (2021-03-26 a 2021-06-23) |

## Regras

- Zero termos ECP (vocabulário ECP-000..010, 52 termos).
- Rastreabilidade 100% → `sources/01-origem-dos-documentos.md`.
- Nenhum conteúdo de SX-001/002/003 importado.

## Autoridade

DECISION P5-INPUT-MATERIALS; produção em ordem do manifest §3 (BIP-005).
