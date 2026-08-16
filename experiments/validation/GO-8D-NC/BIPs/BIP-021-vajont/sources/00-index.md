# BIP-021-vajont - Fronteira e Indexamento

**Caso:** Desastre do Vajont (1963)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, 145 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `parlamento-vajont` | Senato della Repubblica - Comunicazione sulla catastrofe del Vajont (1963) | https://www.parlamento.it/service/PDF/PDFServer/DF/320334.pdf | 2026-08-15 | `parlamento-vajont.pdf` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `parlamento-vajont.pdf` | `3f2e8e096bd062cf6ebd424b378dbc6d9c1d64a6870561736621f31244871dac` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.
