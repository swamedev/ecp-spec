# BIP-028-enron - Fronteira e Indexamento

**Caso:** Enron - falencia e fraude (2001-2002)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, 50 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `senate-psi-enron` | Senate Committee Print 107-75 Financial Oversight of Enron (2002) | https://www.govinfo.gov/content/pkg/CPRT-107SPRT82147/pdf/CPRT-107SPRT82147.pdf | 2026-08-15 | `senate-psi-enron.pdf` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `senate-psi-enron.pdf` | `4bd4087aa84305d96f3a0629a8f796d28fa19df011f6b9e810a730d942c753a1` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.
