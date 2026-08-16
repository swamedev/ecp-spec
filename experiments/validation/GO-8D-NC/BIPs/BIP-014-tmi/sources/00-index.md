# BIP-014-tmi - Fronteira e Indexamento

**Caso:** Three Mile Island (1979)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, 195 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `gao-emd-80-109` | GAO EMD-80-109 - Three Mile Island: A Need for Change (1980) | https://www.gao.gov/assets/emd-80-109.pdf | 2026-08-15 | `gao-emd-80-109-tmi-1980.pdf` | acessivel |
| `kemeny-commission-report-1979` | Report of the President's Commission on the Accident at TMI (Kemeny, out/1979) - copia GPO via OSTI | https://www.osti.gov/servlets/purl/6986994 | 2026-08-15 | `kemeny-commission-report-1979.pdf` | acessivel |
| `kemeny-report` | Kemeny Commission Report (NRC ADAMS ML19275A948) | https://www.nrc.gov/docs/ML1927/ML19275A948.pdf | 2026-08-15 | `kemeny-report.pdf` | acessivel |
| `kemeny-tatf-vol1` | Kemeny Technical Assessment Task Force Vol I (INL archive) | https://tmi2kml.inl.gov/Documents/2a-Kemeny/Presidents%20Commission,%20Technical%20Assessment%20Task%20Force,%20Vol.%20I%20(1979-10-30).pdf | 2026-08-15 | `(sem arquivo)` | falha_com_alternativa |
| `nrc-nureg-0600` | NUREG-0600 - Investigation into the 3/28/1979 TMI Accident by the Office of Inspection & Enforcement (1979) | https://tmi2kml.inl.gov/Documents/2c-L2-NUREG/NUREG-0600,%20Investigation%20into%20the%2003-28-1979%20TMI%20Accident%20by%20the%20Office%20of%20IE%20(1979-08).pdf | 2026-08-15 | `nrc-nureg-0600-1979.pdf` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `gao-emd-80-109-tmi-1980.pdf` | `0a1e53f16f694fc2dea785700a1a1a11505bcea30afbb58b8a7f962cd6b9cd04` |
| `kemeny-commission-report-1979.pdf` | `bd6aeda24e0abe3244ec19c2d020b22418ef5c2aaf0790c0e8a56be3278f2a70` |
| `kemeny-report.pdf` | `c03ee2ee3fc19d333d85d3f0cfca490b764827838bc4ac86fc6e313075afda16` |
| `nrc-nureg-0600-1979.pdf` | `7f208783053fd96ddc3455aebf419ab837bd8803457530e5e9c5f93d724db235` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.

## Notas

- TATF Vol I indisponivel (INL tmi2kml.inl.gov fora do ar, HTTP 502 persistente). Alternativa efetiva coletada: kemeny-report.pdf (relatorio Kemeny completo via NRC ADAMS) e kemeny-commission-report-1979.pdf (OSTI).
- Mirror do INL (tmi2kml.inl.gov); arquivo obtido antes da indisponibilidade do host.
