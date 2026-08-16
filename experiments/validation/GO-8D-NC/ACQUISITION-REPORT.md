# GO-8D-NC — Relatório da Coleta de Fontes (BIPs 013–030)

**Data:** 2026-08-15
**Autorização:** governança GO-8D-NC (coleta e registro de fontes brutas primárias; sem narrativa/atomic facts nesta etapa)
**Plano:** `GO-8D-NC/BIP-ACQUISITION-PLAN.md` (BIP Acquisition Plan v1; gate 30/30)
**Escopo:** 18 BIPs novos (BIP-013 … BIP-030)

---

## 1. Resumo executivo

- **18/18 BIPs** com coleta concluída e `sources/00-index.md` gerado.
- **39 fontes registradas** (`_coleta_completa.json`), **38 arquivos** em `sources/raw/` (38 fontes `acessivel` + 1 fonte `falha_com_alternativa` sem arquivo).
- **0 arquivos órfãos** em `raw/`; **0 divergências de hash** entre registro e disco.
- **Lock GO-8D-NC íntegro** (14/14 artefatos + manifest sha256 `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`; `lock_status: LOCKED`).
- **Nenhum commit** realizado.

## 2. Inventário por BIP

| BIP | Caso | Fontes | Arquivos raw | Status |
|---|---|---|---|---|
| BIP-013-bhopal | Bhopal (1984) | 6 | 6 | 6 acessivel |
| BIP-014-tmi | Three Mile Island (1979) | 5 | 4 | 4 acessivel + 1 falha_com_alternativa |
| BIP-015-challenger | Challenger (1986) | 1 | 1 | 1 acessivel |
| BIP-016-columbia | Columbia (2003) | 1 | 1 | 1 acessivel |
| BIP-017-katrina | Katrina / Nova Orleans (2005) | 5 | 5 | 5 acessivel |
| BIP-018-flint | Crise da água de Flint (2014-2016) | 1 | 1 | 1 acessivel |
| BIP-019-fukushima | Fukushima Daiichi (2011) | 2 | 2 | 2 acessivel |
| BIP-020-grenfell | Incêndio Grenfell Tower (2017) | 2 | 2 | 2 acessivel |
| BIP-021-vajont | Desastre do Vajont (1963) | 1 | 1 | 1 acessivel |
| BIP-022-max8 | Boeing 737 MAX (2018-2019) | 2 | 2 | 2 acessivel |
| BIP-023-mariana | Barragem de Fundão / Samarco - Mariana (2015) | 2 | 2 | 2 acessivel |
| BIP-024-dieselgate | Dieselgate - Volkswagen (2015) | 2 | 2 | 2 acessivel |
| BIP-025-wellsfargo | Wells Fargo - contas falsas (2016) | 1 | 1 | 1 acessivel |
| BIP-026-theranos | Theranos - fraude (2018) | 1 | 1 | 1 acessivel |
| BIP-027-opioids | Opioides - Purdue Pharma (2020) | 2 | 2 | 2 acessivel |
| BIP-028-enron | Enron - falência e fraude (2001-2002) | 1 | 1 | 1 acessivel |
| BIP-029-takata | Takata - airbags (2017) | 2 | 2 | 2 acessivel |
| BIP-030-concordia | Costa Concordia (2012) | 2 | 2 | 2 acessivel |
| **Total** | | **39** | **38** | **38 acessivel + 1 falha_com_alternativa** |

## 3. Fonte não coletada (falha com alternativa)

- **`kemeny-tatf-vol1`** (BIP-014) — Kemeny Technical Assessment Task Force Vol I (INL archive `tmi2kml.inl.gov`, HTTP 502 persistente).
  **Alternativa efetiva coletada:** `kemeny-report.pdf` (relatório Kemeny completo via NRC ADAMS, 45,5 MB) e `kemeny-commission-report-1979.pdf` (cópia GPO via OSTI, 1,68 MB).

## 4. Correções aplicadas durante a coleta

1. **rogers-vol1** (BIP-015): URL NTRS antiga redirecionava para HTML; corrigida para NTRS API
   (`https://ntrs.nasa.gov/api/citations/19860015255/downloads/19860015255.pdf`); arquivo real em PDF (25,1 MB).
2. **doj-purdue-press** (BIP-027) e **doj-takata-press** (BIP-029): páginas `justice.gov` bloqueadas por intersticial Akamai;
   corrigidas via snapshot Wayback (`https://web.archive.org/web/2021id_/<url>`).
3. **Deduplicação** por hash (removidos duplicados byte-idênticos, mantidos nomes canônicos):
   - BIP-013: `bgdrc-icmr-technical-report.pdf` (= `icmr-bgdrc.pdf`), `varadarajan-csir-report-1985.pdf` (= `varadarajan-csir.pdf`).
   - BIP-015: `rogers-commission-report-1986.pdf` (= `rogers-vol1.pdf`).
   - BIP-016: `caib-report-vol1-2003.pdf` (= `caib-vol1.pdf`).
   - BIP-017: `whitehouse-federal-response-katrina-2006.pdf` (= `whitehouse-katrina.pdf`).
4. **Órfãos registrados com URL oficial confirmada** (hash comparado com origem):
   - BIP-013: `gom-bhopal-cabinet-2010-pib.html` (PIB relid=67257); `gom-bhopal-minutes-2010.pdf` (mirror bhopal.net, hash idêntico);
     `ntis-pb89115380-record.html` (NTRL).
   - BIP-014: `gao-emd-80-109-tmi-1980.pdf` (gao.gov, hash idêntico); `kemeny-commission-report-1979.pdf` (OSTI, hash idêntico);
     `nrc-nureg-0600-1979.pdf` (mirror INL).
   - BIP-017: `dhs-oig-fema-katrina-review-2006.pdf` (URL canônica OIG-06-32, host bloqueia crawling);
     `usace-ipet-vol1-execsum-2009.pdf` (= texto completo do Vol I Final 2009, LSU, hash idêntico; ver nota no índice).

## 5. Rastreabilidade e integridade

- Registro consolidado: `GO-8D-NC/BIPs/_coleta_completa.json` (39 entradas; campos bip, id, desc, url, acesso, status, arquivo, sha256, bytes, nota).
- Índices por BIP: `GO-8D-NC/BIPs/BIP-013..030/sources/00-index.md` (tabela id_fonte | descricao | url | data_acesso | arquivo | status + checksums).
- Validação automatizada: **0 órfãos** em `raw/`; **0 registros** sem arquivo em disco; **0 divergências de hash**.
- Scripts de coleta/consolidação desta sessão: `collect2.py`, `collect34.py`, `collect_fix2.py`, `consolidate.py` (temp local, reproduzíveis).

## 6. Verificação do Lock GO-8D-NC

- **14/14** artefatos congelados com SHA-256 conferindo.
- Manifest sha256 (normalizado UTF-8-no-BOM/LF/trailing-newline): `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058` — **inalterado**.
- `lock_status: LOCKED`.
- Nenhum artefato congelado modificado nesta sessão; nenhum commit.

## 7. Conformidade e próximos passos

- Nesta etapa: somente coleta/registro de fontes brutas. **Nenhuma** narrativa/atomic-facts/reconstrução produzida.
- Próximas etapas (fora do escopo desta sessão): produção de `01-narrativa-original.md` e `02-atomic-facts.md` por BIP,
  validação ECP/lexicon (condições A/B zero termos ECP), rastreabilidade fato→fonte e gate 30/30 com revisores independentes.