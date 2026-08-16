# BIP-029-takata - Fronteira e Indexamento

**Caso:** Takata - airbags (2017)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, 60 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `doj-takata-press` | DOJ - Takata guilty plea $1B (2017) | https://web.archive.org/web/2021id_/https://www.justice.gov/archives/opa/pr/takata-corporation-agrees-plead-guilty-and-pay-1-billion-criminal-penalties-airbag-scheme | 2026-08-15 | `doj-takata-press.html` | acessivel |
| `nhtsa-takata-recall` | NHTSA - Takata Recall Spotlight | https://www.nhtsa.gov/equipment/takata-recall-spotlight | 2026-08-15 | `nhtsa-takata-recall.html` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `doj-takata-press.html` | `7c700ce0db0d9e14856b471ef89742e363bafe9432334bb60d8ce7a8b96d22be` |
| `nhtsa-takata-recall.html` | `b460913241e4b6c1a8d035b084f94ca32c6381f0b403ce486dd36504f93d4c39` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.
