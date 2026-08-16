# BIP-002 — Hyatt Regency Walkways

**Caso:** Colapso das passarelas suspensas do átrio do Hyatt Regency, Kansas City, Missouri (1981)
**Status (P5):** MATERIAIS PRODUZIDOS (condições A/B/C) — aguarda validação pós-produção
**Escopo da coleta:** 2 origens primárias obtidas; demais fontes do plano facultativas em ciclo posterior.

## Conteúdo

- `sources/00-index.md` — fronteira pré/pós gate + registros e checksums das fontes
- `sources/01-origem-dos-documentos.md` — proveniência EI (SC-5)
- `sources/raw/` — 2 fontes brutas (1 PDF, 1 HTML) com checksum
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
| `nbs-01-bss143` | National Bureau of Standards, *Investigation of the Kansas City Hyatt Regency Walkways Collapse*, Building Science Series 143, maio de 1982 |
| `vlex-02-duncan` | Duncan v. Missouri Board for Architects, Professional Engineers and Land Surveyors, No. 52655, 744 S.W.2d 524 (Mo. App. 1988), julgado em 26/01/1988 (espelho público vLex Case Law) |

## Regras

- Zero termos ECP (vocabulário ECP-000..010, 52 termos).
- Rastreabilidade 100% → `sources/01-origem-dos-documentos.md`.
- Nenhum conteúdo de SX-001/002/003 importado.

## Autoridade

DECISION P5-INPUT-MATERIAIS; produção em ordem do manifest §3 (BIP-002).
