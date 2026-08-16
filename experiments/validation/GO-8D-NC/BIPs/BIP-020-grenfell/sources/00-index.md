# BIP-020-grenfell - Fronteira e Indexamento

**Caso:** Incendio Grenfell Tower (2017)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, 200 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `grenfell-phase1-exec` | Grenfell Tower Inquiry Phase 1 Report - Executive Summary (2019) | https://assets.publishing.service.gov.uk/media/66d82294a399e0dcf5200b2f/Grenfell_Tower_Inquiry_-_Phase_1_report_Executive_Summary.pdf | 2026-08-15 | `grenfell-phase1-exec.pdf` | acessivel |
| `grenfell-phase1-vol1` | Grenfell Tower Inquiry Phase 1 Report - Volume 1 (2019) | https://assets.publishing.service.gov.uk/media/66d822a87a73423428aa2ee7/Grenfell_Tower_Inquiry_-_Phase_1_report_-_volume_1.pdf | 2026-08-15 | `grenfell-phase1-vol1.pdf` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `grenfell-phase1-exec.pdf` | `9a8e5d48eb93620e6b6033c361bbff1c5e8eeae46eb763a23387098867bbde6a` |
| `grenfell-phase1-vol1.pdf` | `9f5042005add7226ef208fd666ff7527919478a3c7443b2d1824a3b02f46d82f` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.
