# BIP-026-theranos - Fronteira e Indexamento

**Caso:** Theranos - fraude (2018)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, 110 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `sec-complaint` | SEC v. Holmes/Theranos - Complaint (2018) | https://www.sec.gov/files/litigation/complaints/2018/comp-pr2018-41-theranos-holmes.pdf | 2026-08-15 | `sec-complaint.pdf` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `sec-complaint.pdf` | `3ce565f81f038797a7803cef3f9370019c16676700c551ea31c639f2222e6826` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.
