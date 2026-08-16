# BIP-007 — Resposta ao Ebola na África Ocidental (2014–2016)

**Caso:** Resposta internacional à epidemia de doença pelo vírus Ebola na África Ocidental (2014–2016)
**Status (P5):** MATERIAIS PRODUZIDOS (condições A/B/C) — **7/7 materiais de entrada do piloto prontos**
**Escopo da coleta:** 8 fontes obtidas cobrindo ≥4 origens causais independentes (OMS/NEJM; MSF; CDC; UNMEER).

## Conteúdo

- `sources/00-index.md` — fronteira pré/pós gate + registros, checksums e hashes do texto extraído
- `sources/01-origem-dos-documentos.md` — proveniência EI (SC-5)
- `sources/raw/` — 8 fontes brutas (5 PDF + 3 HTML) + 5 extrações `.txt` + `00-fetch-errors.md` + `00-extraction-errors.md`
- `narrative/narrative_pt.md` — condição C (zero ECP; 1.340 palavras)
- `atomic-facts/atomic_facts.md` — condições A/B (zero ECP; 90 fatos)

## Entrada por condição

| Condição | Entrada |
|---|---|
| A (cega pura) | `atomic-facts/atomic_facts.md` |
| B (cega + C3) | `atomic-facts/atomic_facts.md` + `scripts/go8b/operational/C3_TAXONOMY.yaml` |
| C (não-cega) | `narrative/narrative_pt.md` |

## Fontes (origens independentes, SC-5)

| ref | Fonte |
|---|---|
| `who-01-sitrep-jun2016` | WHO, *Ebola Situation Report — 10 June 2016* |
| `who-02-overview-2014-2016` | WHO, *Ebola outbreak 2014-2016 — West Africa* (página oficial) |
| `nejm-01-ebola-9months` | WHO Ebola Response Team, NEJM 2014;371:1481-1495 |
| `msf-01-pushed-limit` | MSF, *Pushed to the limit and beyond* (mar/2015) |
| `msf-02-facts-figures` | MSF, *Ebola 2014-2015 Facts & Figures* (mar/2016) |
| `cdc-01-mmwr-sep2014` | CDC/MMWR, *Ebola Virus Disease Outbreak — West Africa, September 2014* |
| `unmeer-01-mission` | UNMEER, página oficial da missão (ONU) |
| `unmeer-02-sitrep` | UNMEER, *External Situation Report* (05/03/2015) |

## Regras

- Zero termos ECP (vocabulário ECP-000..010, 52 termos).
- Rastreabilidade 100% → `sources/00-index.md`.
- Nenhum conteúdo de SX-001/002/003 importado.

## Autoridade

DECISION P5-INPUT-MATERIALS; produção em ordem do manifest §3 (BIP-007).