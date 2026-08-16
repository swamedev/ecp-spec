# BIP-017-katrina - Fronteira e Indexamento

**Caso:** Katrina / Nova Orleans (2005)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, 290 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `dhs-oig-06-32` | DHS OIG-06-32 - A Review of FEMA's Hurricane Response to Hurricane Katrina (2006) | https://www.oig.dhs.gov/sites/default/files/assets/Mgmt/OIG_06-32_Mar06.pdf | 2026-08-15 | `dhs-oig-fema-katrina-review-2006.pdf` | acessivel |
| `usace-ipet-vol1` | USACE IPET Vol I Exec Summary (2006) | https://www.nytimes.com/packages/pdf/national/20060601_ARMYCORPS_SUMM.pdf | 2026-08-15 | `usace-ipet-vol1.pdf` | acessivel |
| `usace-ipet-vol1-final-2009` | USACE IPET - Performance Evaluation of the New Orleans & Southeast Louisiana Hurricane Protection System, Volume I (Final, 2009) | https://biotech.law.lsu.edu/katrina/ipet/Volume%20I%20FINAL%2023Jun09%20mh.pdf | 2026-08-15 | `usace-ipet-vol1-execsum-2009.pdf` | acessivel |
| `usace-ipet-vol5` | USACE IPET Vol V Levees/Floodwalls (2006) | https://biotech.law.lsu.edu/katrina/ipet/gpo/Vol%20V%20The%20Performance%20Levees%20and%20Floodwalls%20-%20maintext.pdf | 2026-08-15 | `usace-ipet-vol5.pdf` | acessivel |
| `whitehouse-katrina` | The Federal Response to Hurricane Katrina: Lessons Learned (2006) | https://www.govinfo.gov/content/pkg/GOVPUB-PREX-PURL-LPS67263/pdf/GOVPUB-PREX-PURL-LPS67263.pdf | 2026-08-15 | `whitehouse-katrina.pdf` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `dhs-oig-fema-katrina-review-2006.pdf` | `35dfd9fc10ac4f1a170ffc84bdbc1b4412c0c07c7f17441121ec7070243698fa` |
| `usace-ipet-vol1.pdf` | `e447bb66c6e2d70bdad7e5db1ae42e7803ee4d8d22741e61efebd10b1020ab2a` |
| `usace-ipet-vol1-execsum-2009.pdf` | `37589945cba4fa90e2f7a12907cdc8172045eec8838a17c84c8fea5b5184d664` |
| `usace-ipet-vol5.pdf` | `6ef977585fa2d3b49d5596ecb1953dac382abd69b30c55bd1323d02107b8d2c8` |
| `whitehouse-katrina.pdf` | `83879fed9623206e2da3bbc567763482a866079d582acfbc9ff47d05b8e5e61c` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.

## Notas

- oig.dhs.gov bloqueia crawling (HTTP 403); URL canonica confirmada por indice publico.
- Apesar do nome do arquivo, e o texto completo do Vol I Final (2009). usace-ipet-vol1.pdf e o resumo executivo do rascunho de 2006 (via NYT).
