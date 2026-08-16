# BIP-025-wellsfargo - Fronteira e Indexamento

**Caso:** Wells Fargo - contas falsas (2016)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, 120 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `cfpb-consent-order` | CFPB Consent Order Wells Fargo 2016-CFPB-0015 | https://files.consumerfinance.gov/f/documents/092016_cfpb_WFBconsentorder.pdf | 2026-08-15 | `cfpb-consent-order.pdf` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `cfpb-consent-order.pdf` | `5faaae40ee44613a8e446e23852dc57ccfe1f227199b1e8c90f2a6faf1950d0c` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.
