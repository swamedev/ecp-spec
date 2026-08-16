# BIP-001 — Deepwater Horizon / Macondo

**Caso:** Deepwater Horizon / Macondo (2010)
**Status (P5):** MATERIAIS PRODUZIDOS (condições A/B/C) — aguarda validação pós-produção
**Escopo da coleta:** 3 origens primárias obtidas; demais fontes do plano facultativas em ciclo posterior.

## Conteúdo

- `sources/00-index.md` — fronteira pré/pós gate + registros e checksums das fontes
- `sources/01-origem-dos-documentos.md` — proveniência EI (SC-5)
- `sources/raw/` — 3 PDFs oficiais com checksum
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
| `ncom-01-gulf` | Comissão Nacional sobre a BP Deepwater Horizon (EUA), 2011 — GovInfo |
| `csb-01-macondo-v1` | CSB, Investigation Report Vol. 1 (nº 2010-10-I-OS), 2014 — csb.gov |
| `jit-01-report` | JIT BOEMRE/USCG, Report Regarding the Causes of the Macondo Well Blowout, 2011 — BSEE |

## Regras

- Zero termos ECP (vocabulário ECP-000..010, 52 termos).
- Rastreabilidade 100% → `sources/01-origem-dos-documentos.md`.
- Nenhum conteúdo de SX-001/002/003 importado.

## Autoridade

DECISION P5-INPUT-MATERIALS; escopo de produção DECIDED (avançar BIP-001 + piloto BIP-004).