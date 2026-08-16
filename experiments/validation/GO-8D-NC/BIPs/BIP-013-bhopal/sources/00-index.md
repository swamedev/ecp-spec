# BIP-013-bhopal - Fronteira e Indexamento

**Caso:** Bhopal (1984)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, 188 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `gom-bhopal-minutes-2010` | Minutes do Grupo de Ministros (GoM) sobre o desastre de Bhopal, 18-21/06/2010 (documento divulgado pelo The Hindu; mirror bhopal.net) | https://www.bhopal.net/wp-content/uploads/2019/05/June-2010-research-centre-directive.pdf | 2026-08-15 | `gom-bhopal-minutes-2010.pdf` | acessivel |
| `gom-cabinet-pib-2010` | PIB - Cabinet approves additional Rs.71.28 crore for Bhopal Gas Leak victims (2010) | https://pib.gov.in/newsite/PrintRelease.aspx?relid=67257 | 2026-08-15 | `gom-bhopal-cabinet-2010-pib.html` | acessivel |
| `gom-pib` | PIB - Cabinet aprova recomendacoes GoM Bhopal (2010) | https://pib.gov.in/newsite/erelcontent.aspx?relid=62802 | 2026-08-15 | `gom-pib.html` | acessivel |
| `icmr-bgdrc` | ICMR BGDRC Technical Report (1985-1994) | https://www.icmr.gov.in/icmrobject/custom_data/1720338129_bgdrc-technical_report.pdf | 2026-08-15 | `icmr-bgdrc.pdf` | acessivel |
| `ntis-record-pb89115380` | NTIS/NTRL - registro bibliografico do relatorio PB89115380 (Varadarajan/CSIR, 1985) | https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/PB89115380.xhtml | 2026-08-15 | `ntis-pb89115380-record.html` | acessivel |
| `varadarajan-csir` | Relatorio Varadarajan/CSIR dez-1985 (NTIS PB89115380) | https://bhopalgasdisaster.files.wordpress.com/2014/12/csir-report-on-scientific-studies-december-1985.pdf | 2026-08-15 | `varadarajan-csir.pdf` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `gom-bhopal-minutes-2010.pdf` | `7c2069efb26289dbe6fc5cded7431fa062c880b91706236a69cd8c0e9644a2c8` |
| `gom-bhopal-cabinet-2010-pib.html` | `bbb2468e2018b83763872a3a970052e71ca37e8ae4dcbab0f21af2394ea8cdf8` |
| `gom-pib.html` | `5ef96f49c406cf276da921b17276e9f64e394c54c4980c2f87b380332163442e` |
| `icmr-bgdrc.pdf` | `6dd9eb54999377e40675f495302d3a1cf5cc35553f2f3cbe7b9d1dc543dee877` |
| `ntis-pb89115380-record.html` | `23029b13f620c14ee148f93af052c3430c7629bc9951fd50ccb5c6081bdbec0a` |
| `varadarajan-csir.pdf` | `2fcd71ebba64394547150ba9f67264fc917289f42200e5e1b3e5b5e4ada8bfd0` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.
