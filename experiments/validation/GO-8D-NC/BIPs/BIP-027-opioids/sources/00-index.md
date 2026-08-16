# BIP-027-opioids - Fronteira e Indexamento

**Caso:** Opioides - Purdue Pharma (2020)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, 100 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `doj-purdue-press` | DOJ Press Release - Purdue global resolution (2020) | https://web.archive.org/web/2021id_/https://www.justice.gov/archives/opa/pr/justice-department-announces-global-resolution-criminal-and-civil-investigations-opioid | 2026-08-15 | `doj-purdue-press.html` | acessivel |
| `doj-purdue-settlement` | DOJ Purdue Pharma Settlement Agreement (2020) | https://www.justice.gov/opa/press-release/file/1329571/dl | 2026-08-15 | `doj-purdue-settlement.pdf` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `doj-purdue-press.html` | `2ec05bf03c146f442dc268c6461c746d943b52bd18bac82352cab1cc21d7d429` |
| `doj-purdue-settlement.pdf` | `9356a8bd6b4b167ad4d7f561643e84e1a1caadf6c2f39e7e42a5b01b172a7316` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.
