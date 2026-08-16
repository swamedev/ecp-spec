# BIP-003 — Operation Warp Speed: Origem dos Documentos (Proveniência)

**Data:** 2026-08-12
**Autoridade:** DECISION P5-INPUT-MATERIAIS; manifest §5.
**Regra aplicada:** nenhuma importação de narrativa/atomic-facts/reconstrução dos SX. Fontes são públicas e primárias.

---

## Registro de proveniência

| ref | Origem (quem) | O quê | Quando | Canal | Tipo EI (SC-5) |
|---|---|---|---|---|---|
| `gao-01-21-319` | Government Accountability Office (GAO) — órgão de auditoria do Congresso dos EUA | *Operation Warp Speed: Accelerated COVID-19 Vaccine Development Status and Efforts to Address Manufacturing Challenges*, GAO-21-319, relatório aos destinatários do Congresso (47 p.) | emitido 11/02/2021 | PDF público do GAO (captura via Wayback Machine; gao.gov respondeu HTTP 403 a acesso automatizado) | órgão federal de auditoria independente do Poder Legislativo |
| `dod-02-fact-sheet` | Department of Health and Human Services (HHS) e Department of Defense (DOD) — Poder Executivo dos EUA | ficha oficial conjunta *Explaining Operation Warp Speed* (5 p.) | versão 12/08/2020 | PDF público (captura via espelho da secretaria; hhs.gov respondeu HTTP 403 a acesso automatizado) | Poder Executivo federal; condutores do programa OWS |
| `crs-01-in11560` | Congressional Research Service (CRS) — serviço de pesquisa do Congresso dos EUA | *Operation Warp Speed Contracts for COVID-19 Vaccines and Ancillary Vaccination Materials*, CRS Insight IN11560, versão 7 (4 p.) | atualizado 01/03/2021 | congress.gov (PDF público) | serviço de pesquisa não partidário do Poder Legislativo |

> Nota de canal (SC-5): as fontes são obras de governo dos EUA, públicas e reproduzíveis; os espelhos usados (Wayback Machine; espelho da ficha; congress.gov) preservam o conteúdo oficial integralmente.

## Independência das origens (SC-5)

Três origens causais independentes entre si:
1. **GAO (auditoria do Legislativo)** — verificação independente do desenvolvimento das vacinas e dos desafios de manufatura; metodologia própria (questionários às empresas, TRLs).
2. **HHS/DoD (Executivo)** — ficha oficial do programa; metas, estrutura de parceria, ações de desenvolvimento/manufatura/distribuição e liderança.
3. **CRS (pesquisa do Legislativo)** — consolidação de contratos e valores por empresa, incluindo materiais de apoio à vacinação.

Cada uma produziu conteúdo por conta própria e a partir de fontes primárias próprias; o CRS e o GAO referenciam-se entre si apenas como material de contexto, mas os dados contratuais e as avaliações são independentes.

## Estado de coleta

- Coleta inicial concluída: 3 origens primárias baixadas para `raw/`, checksums registrados em `00-index.md`.
- **Captura sem uso de conteúdo:** `hhs-01-factory-to-frontlines.pdf` (516 bytes) contém apenas a resposta HTTP "Access Denied" de media.defense.gov, salva com extensão .pdf; registrada para fins de rastreamento, sem conteúdo aproveitado nos materiais.
- Pendente (ciclo posterior, facultativo): relatórios GAO de acompanhamento (GAO-21-207, GAO-21-265), documentos da FDA (decisões de EUA) e divulgações das empresas.

## Conformidade

- Nada importado de SX-001/002/003.
- Fontes brutas obtidas de canais públicos (Wayback Machine de PDF oficial; espelho da ficha HHS/DoD; congress.gov); matéria-prima primária, não interpretativa.
