# BIP-019-fukushima - Fronteira e Indexamento

**Caso:** Fukushima Daiichi (2011)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, 240 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `iaea-dg-report` | IAEA - The Fukushima Daiichi Accident: Report by the Director General (2015) | https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1710-ReportByTheDG-Web.pdf | 2026-08-15 | `iaea-dg-report.pdf` | acessivel |
| `naiic-report` | NAIIC - The National Diet of Japan Fukushima Report (2012) | https://gnssn.iaea.org/actionplan/Shared%20Documents/Action%2001%20-%20Safety%20Assessments/The%20National%20Diet%20of%20Japan.pdf | 2026-08-15 | `naiic-report.pdf` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `iaea-dg-report.pdf` | `f55f046ae83d3634f32141fd51f7809c72b43270986a0cefa04d62a2dbbfd33c` |
| `naiic-report.pdf` | `96987f4d9983ddc61f5f44137520d03376c3016c39ef2070c98aaea65f963580` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.
