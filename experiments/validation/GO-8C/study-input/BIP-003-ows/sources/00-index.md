# BIP-003 — Operation Warp Speed: Fronteira e Indexamento

**Caso:** Operation Warp Speed — aceleração do desenvolvimento e da distribuição de vacinas contra a COVID-19 nos Estados Unidos (2020–2021)
**Data de produção:** 2026-08-12
**Escopo de produção (DECIDED):** produção de materiais (ordem manifest §3 — BIP-003)

---

## Fronteira pré/pós gate

| Fase | Escopo permitido |
|---|---|
| **Pré-gate (produção P5)** | Coleta, rastreamento e registro de fontes brutas primárias; produção de narrativa (condição C) e atomic facts (condições A/B), ambos com **zero termos ECP**, com rastreabilidade às fontes. |
| **Pós-gate (execução experimental)** | Apenas reconstrução anonimizada (labels neutros, arestas in/out, sem ECP) e análise conforme 04/06. **Não altera estes materiais.** |

## Fontes registradas

| ref | Arquivo (raw) | Tipo | Origem causal (grupo) |
|---|---|---|---|
| `gao-01-21-319` | `gao-01-21-319.pdf` | relatório de auditoria federal (GAO-21-319; 47 p.) | Government Accountability Office (órgão de controle do Congresso dos EUA) |
| `dod-02-fact-sheet` | `dod-02-fact-sheet-ows.pdf` | ficha oficial conjunta HHS/DoD "Explaining Operation Warp Speed" (5 p.) | Department of Health and Human Services / Department of Defense (Poder Executivo dos EUA) |
| `crs-01-in11560` | `crs-01-in11560.pdf` | relatório breve do Congressional Research Service (IN11560, v.7; 4 p.) | Congressional Research Service (serviço de pesquisa do Congresso dos EUA) |

> Coleta inicial do piloto BIP-003: 3 origens causais primárias independentes obtidas (auditoria do GAO; ficha oficial do Executivo; análise do serviço de pesquisa do Congresso).
> Complementos facultativos em ciclo posterior: relatórios do GAO de direitos subsequentes, decisões da FDA e estudos pós-licença.
>
> **Captura registrada sem uso de conteúdo:** `hhs-01-factory-to-frontlines.pdf` (516 bytes) é resposta "Access Denied" de media.defense.gov salva com extensão .pdf; registrada para rastreamento, sem conteúdo aproveitado. Não consta nas fontes efetivas.

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `gao-01-21-319.pdf` | `78e386d3efc7e316f0eec46c202140ff6efc8034729cdf1828ffd2e1bb93b6ea` |
| `dod-02-fact-sheet-ows.pdf` | `1591189d38c77ee77b077ea341684b8a4ee9abedf72d028210262f3a0dab90ce` |
| `crs-01-in11560.pdf` | `5d61ae863a273bfc8887464a764ab47d5aa6eacae5ea2ee508893ce52e6c8221` |

## Conformidade

- Apenas fontes brutas primárias; nenhuma narrativa/atomic-facts/reconstrução de SX-001/002/003 importada.
- Rastreabilidade: cada atomic fact e cada bloco narrativo referenciam os `refs` acima.
- Nota de canal: o PDF do GAO (gao.gov) e a ficha HHS (hhs.gov) devolveram HTTP 403 ao acesso automatizado e foram capturados, respectivamente, pelo repositório público Wayback Machine e por espelho público da secretaria; o CRS foi capturado diretamente em congress.gov.
