# BIP-007 — Registro de ocorrências de extração de texto (PDF → TXT)

**Fase:** BIP-007 Fase 1 — extração de texto dos 5 PDFs de `sources/raw/`.
**Data:** 2026-08-12
**Ferramenta:** PyMuPDF (`fitz`) — `pdftotext` indisponível no ambiente; usado equivalente com extração por página.
**Resultado geral:** **5/5 extrações bem-sucedidas; nenhum erro não recuperado.**

---

## Resumo das extrações

| PDF fonte | TXT gerado | Status | Observação |
|---|---|---|---|
| `WHO-SitRep-2016-06-10.pdf` | `WHO-SitRep-2016-06-10.txt` | **OK** | Texto integral por página; sessão de tabela de indicadores preservada. |
| `NEJM-Ebola-First-9-Months-2014.pdf` | `NEJM-Ebola-First-9-Months-2014.txt` | **OK** | Texto extenso (artigo científico); tabelas/figuras apresentadas como texto. |
| `MSF-Pushed-to-Limit-2015.pdf` | `MSF-Pushed-to-Limit-2015.txt` | **OK** | Texto integral; citações e números preservados. |
| `MSF-Ebola-2014-2015-Facts-Figures.pdf` | `MSF-Ebola-2014-2015-Facts-Figures.txt` | **OK** | Texto integral; gráficos convertidos em texto (valores numéricos preservados). |
| `UNMEER-External-SitRep-2015-03-05.pdf` | `UNMEER-External-SitRep-2015-03-05.txt` | **OK** | Texto integral de relatório de situação. |

## Ocorrências

- **Nenhuma falha de extração registrada.** Todos os 5 arquivos geraram texto não vazio (verificações de comprimento de conteúdo passaram).
- SHA-256 dos arquivos `.txt` registrados na coluna "Texto extraído SHA-256" do `sources/00-index.md`.

## Conformidade

- Extração limitada ao conteúdo textual público dos PDFs; nenhum material interpretativo importado.
- Rastreabilidade: cada `.txt` corresponde 1:1 ao PDF de mesma base de nome.
