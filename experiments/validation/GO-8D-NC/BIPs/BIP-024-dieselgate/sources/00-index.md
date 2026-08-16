# BIP-024-dieselgate - Fronteira e Indexamento

**Caso:** Dieselgate - Volkswagen (2015)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, 50 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `epa-nov-2015-09-18` | EPA NOV Volkswagen 18/09/2015 | https://www.epa.gov/sites/default/files/2015-10/documents/vw-nov-caa-09-18-15.pdf | 2026-08-15 | `epa-nov-2015-09-18.pdf` | acessivel |
| `epa-nov-2015-11-02` | EPA NOV Volkswagen/Audi/Porsche 02/11/2015 | https://www.epa.gov/sites/default/files/2015-11/documents/vw-nov-2015-11-02.pdf | 2026-08-15 | `epa-nov-2015-11-02.pdf` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `epa-nov-2015-09-18.pdf` | `850d8f790d7119f385fdfe11b4defbec2dd0e3d550be83a4c956f48028c1ddb0` |
| `epa-nov-2015-11-02.pdf` | `3ec62b5f09da75acbbf22ed795c8c0f188c1487ee38a085b1d595a985fec9735` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.
