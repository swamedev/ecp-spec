# BIP-022-max8 - Fronteira e Indexamento

**Caso:** Boeing 737 MAX (2018-2019)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP, refs `house-ti-737max` e `ntsb-asr1901`.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, refs `house-ti-737max` e `ntsb-asr1901`, 211 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `house-ti-737max` | House T&I Final Committee Report Boeing 737 MAX (2020) | https://www.govinfo.gov/content/pkg/GOVPUB-Y4_T68_2-PURL-gpo144993/pdf/GOVPUB-Y4_T68_2-PURL-gpo144993.pdf | 2026-08-15 | `house-ti-737max.pdf` | acessivel |
| `ntsb-asr1901` | NTSB Safety Recommendation Report ASR-19-01 MCAS/737 MAX (2019) | https://www.ntsb.gov/investigations/AccidentReports/Reports/ASR1901.pdf | 2026-08-15 | `ntsb-asr1901.pdf` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `house-ti-737max.pdf` | `ea7db59be6d3dd98fac89f4de99357eb7581bb6a7dd0f27c72b5dbd10b165915` |
| `ntsb-asr1901.pdf` | `f232ba85e2b174c9288f3132c502f83d5546364a05de555edc551c44fc4b22be` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.
