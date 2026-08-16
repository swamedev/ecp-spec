# BIP-003 — Operation Warp Speed (OWS)

**Caso:** Aceleração do desenvolvimento e da distribuição de vacinas contra a COVID-19 nos Estados Unidos — Operation Warp Speed (2020–2021)
**Status (P5):** MATERIAIS PRODUZIDOS (condições A/B/C) — aguarda validação pós-produção
**Escopo da coleta:** 3 origens primárias obtidas; complementos facultativos em ciclo posterior.

## Conteúdo

- `sources/00-index.md` — fronteira pré/pós gate + registros e checksums das fontes
- `sources/01-origem-dos-documentos.md` — proveniência EI (SC-5)
- `sources/raw/` — 3 PDFs oficiais com checksum
- `narrative/01-narrativa-original.md` — condição C (zero ECP)
- `atomic-facts/02-atomic-facts.md` — condições A/B (zero ECP, fatos mínimos)

> Nota: `sources/raw/` registra também `hhs-01-factory-to-frontlines.pdf` — captura "Access Denied" (516 bytes) de media.defense.gov, sem conteúdo aproveitado; não é fonte efetiva (ver `00-index.md` e `01-origem-dos-documentos.md`).

## Entrada por condição

| Condição | Entrada |
|---|---|
| A (cega pura) | `atomic-facts/02-atomic-facts.md` |
| B (cega + C3) | `atomic-facts/02-atomic-facts.md` + `scripts/go8b/operational/C3_TAXONOMY.yaml` |
| C (não-cega) | `narrative/01-narrativa-original.md` |

## Fontes (origens independentes, SC-5)

| ref | Fonte |
|---|---|
| `gao-01-21-319` | GAO, Operation Warp Speed: Accelerated COVID-19 Vaccine Development Status and Efforts to Address Manufacturing Challenges (GAO-21-319), 2021 |
| `dod-02-fact-sheet` | HHS/DoD, Explaining Operation Warp Speed — ficha oficial conjunta do Poder Executivo |
| `crs-01-in11560` | Congressional Research Service, Accelerating COVID-19 Vaccine Development (IN11560, v.7) |

## Regras

- Zero termos ECP (vocabulário ECP-000..010, 52 termos).
- Rastreabilidade 100% → `sources/01-origem-dos-documentos.md`.
- Nenhum conteúdo de SX-001/002/003 importado.

## Autoridade

DECISION P5-INPUT-MATERIALS; produção em ordem do manifest §3 (BIP-003).