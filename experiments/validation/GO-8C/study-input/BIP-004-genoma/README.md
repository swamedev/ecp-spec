# BIP-004 — Genoma Humano

**Caso:** Projeto Genoma Humano (1990–2003)
**Status (P5):** MATERIAIS PRODUZIDOS (condições A/B/C) — aguarda validação pós-produção

## Conteúdo

- `sources/00-index.md` — fronteira pré/pós gate + registros e checksums das fontes
- `sources/01-origem-dos-documentos.md` — proveniência EI (SC-5)
- `sources/raw/` — 8 arquivos brutos (HTML) com checksum
- `narrative/01-narrativa-original.md` — condição C (zero ECP)
- `atomic-facts/02-atomic-facts.md` — condições A/B (zero ECP, fatos mínimos)

## Entrada por condição

| Condição | Entrada |
|---|---|
| A (cega pura) | `atomic-facts/02-atomic-facts.md` |
| B (cega + C3) | `atomic-facts/02-atomic-facts.md` + `scripts/go8b/operational/C3_TAXONOMY.yaml` |
| C (não-cega) | `narrative/01-narrativa-original.md` |

## Regras

- Zero termos ECP (vocabulário ECP-000..010, 52 termos).
- Rastreabilidade 100% → `sources/01-origem-dos-documentos.md`.
- Nenhum conteúdo de SX-001/002/003 importado.

## Autoridade

DECISION P5-INPUT-MATERIALS; escopo de produção DECIDED (piloto BIP-004).
