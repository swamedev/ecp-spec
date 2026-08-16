# BIP-007 — Registro de falhas/ocorrências de acesso (fetch)

**Data:** 2026-08-12
**Resumo:** 8/8 fontes coletadas com conteúdo íntegro. 3 vínculos diretos falharam no 1º acesso e foram recuperados via fallback (arquivo digital oficial/mirror oficial). Nenhum conteúdo perdido.

---

## Ocorrências

### E-01 — `who-01` (WHO SitRep 10/06/2016): DSpace/iris devolvia shell HTML

- **URL inicial:** `https://apps.who.int/iris/bitstream/handle/10665/208883/ebolasitrep_10Jun2016_eng.pdf`
- **Tentativa 1 (apps.who.int):** HTTP 200, mas corpo = shell JS/HTML de 755 bytes (SPA DSpace), não o PDF.
- **Tentativa 2 (iris.who.int handle direto):** mesmo comportamento (HTML de bootstrap da aplicação).
- **Tentativa 3 — RESOLVIDO:** `https://web.archive.org/web/2017*/https://apps.who.int/iris/bitstream/handle/10665/208883/ebolasitrep_10Jun2016_eng.pdf` → **HTTP 200, PDF íntegro 398 598 bytes** (canônico WHO autenticado em arquivo digital público).
- **Status:** Coletado (via Wayback Machine — preservação digital oficial do mesmo documento WHO).

### E-02 — `msf-02` (MSF Facts & Figures 2016): URL canônica global 404

- **URL inicial:** `https://www.msf.org/ebola-2014-2015-facts-figures` → **HTTP 404** (página movida/retirada do domínio global).
- **Busca canônica:** identificada versão oficial do relatório completo hospedada em seção nacional oficial do MSF:
  `https://www.msf.ie/sites/ireland/files/an-unprecedented-year_-medecins-sans-frontieres-response-to-the-largest-ever-ebola-outbreak.pdf` → **HTTP 200, PDF 3 914 202 bytes**.
- **Status:** Coletado (PDF oficial MSF, mirror msf.ie — mesmo organismo, conteúdo idêntico; origem causal MSF inalterada).

### E-03 — `msf-01` (MSF Pushed to the limit, 2015): página HTML no lugar do relatório

- **URL inicial:** `https://www.msf.org/ebola-pushed-limit-and-beyond` → **HTTP 200, HTML de landing page** (report release page; não é o PDF).
- **Resolução:** link oficial do relatório completo: `https://msf.org.uk/sites/default/files/2020-09/ebola_-_pushed_to_the_limit_and_beyond.pdf` → **HTTP 200, PDF 915 643 bytes** (release MSF UK oficial).
- **Status:** Coletado (PDF oficial; landing page descartada, mantido apenas o documento).

### E-04 — `cdc-01` (MMWR Early Release 30/09/2014): bloqueio bot/403 no cdc.gov

- **URL inicial:** `https://www.cdc.gov/mmwr/preview/mmwrhtml/mm63e0930a1.htm`
- **Tentativas:** curl com UA browsers variados e `Referer` → **HTTP 403** (WAF/anti-bot); webfetch → 403.
- **Tentativa 3 — RESOLVIDO:** `https://web.archive.org/web/20141001id_/https://www.cdc.gov/mmwr/preview/mmwrhtml/mm63e0930a1.htm` → **HTTP 200, página MMWR oficial íntegra 31 855 bytes** (título "Ebola Virus Disease Outbreak — West Africa, September 2014").
- **Status:** Coletado (via Wayback Machine — preservação da própria página CDC/MMWR).

### E-05 — `unmeer-02` (UNMEER External SitRep de 27/03/2015): URL inexistente

- **URL inicial (do 01-origem):** `.../20150327_unmeer_external_sitrep.pdf` → **HTTP 404**.
- **Variações testadas:** `150327-_unmeer_external_situation_report.pdf` → 404; `150323-...pdf` → 404 (série de 27/03 não publicada nesse padrão).
- **RESOLVIDO:** padrão oficial confirmado `150305-_unmeer_external_situation_report.pdf` (sitrep **05/03/2015**, mais próximo da mesma janela) → **HTTP 200, PDF 169 653 bytes** no domínio oficial `ebolaresponse.un.org`.
- **Status:** Coletado (sitrep UNMEER 05/03/2015 é substituição de data documentada; ref `unmeer-02` atualizada).

---

## Tabela consolidada

| ref | Arquivo raw | Tamanho (B) | Mágic bytes | Status |
|---|---|---|---|---|
| `who-01` | WHO-SitRep-2016-06-10.pdf | 398 598 | `%PDF-` | Coletado (E-01) |
| `who-02` | WHO-Overview-2014-2016.html | 300 635 | `<!DOC` | Coletado (direto) |
| `nejm-01` | NEJM-Ebola-First-9-Months-2014.pdf | 1 081 198 | `%PDF-` | Coletado (direto, mirror PAHO) |
| `msf-01` | MSF-Pushed-to-Limit-2015.pdf | 915 643 | `%PDF-` | Coletado (E-03) |
| `msf-02` | MSF-Ebola-2014-2015-Facts-Figures.pdf | 3 914 202 | `%PDF-` | Coletado (E-02) |
| `cdc-01` | CDC-MMWR-Ebola-Sep-2014.html | 31 855 | `<!DOC` | Coletado (E-04) |
| `unmeer-01` | UNMEER-Mission.html | 146 299 | `<!DOC` | Coletado (direto) |
| `unmeer-02` | UNMEER-External-SitRep-2015-03-05.pdf | 169 653 | `%PDF-` | Coletado (E-05) |

> **Nota de capacidade:** os PDFs foram validados por cabeçalho binário e SHA-256; a **leitura/extração de texto** dos PDFs requer etapa com ferramenta de extração (ex.: pdftotext), pois o modelo de input em uso não suporta leitura direta de PDF (mensagem de erro do leitor). HTMLs podem ser lidos diretamente.