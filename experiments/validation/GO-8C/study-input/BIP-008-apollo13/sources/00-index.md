# BIP-008 — Apollo 13: Fronteira e Indexamento

**Caso:** Missão Apollo 13, acidente e retorno seguro da tripulação (1970)
**Data de produção:** 2026-08-14
**Escopo de produção (DECIDED D-04.2):** produção de materiais (fases P1–P4)

---

## Fronteira pré/pós gate

| Fase | Escopo permitido |
|---|---|
| **Pré-gate (produção P1–P4)** | Coleta, rastreamento e registro de fontes brutas primárias; produção de narrativa (condição C) e atomic facts (condições A/B), ambos com **zero termos ECP**, com rastreabilidade às fontes. |
| **Pós-gate (execução experimental)** | Apenas reconstrução anonimizada (labels neutros, arestas in/out, sem ECP) e análise conforme 04/06. **Não altera estes materiais.** |

## Fontes registradas

| ref | Arquivo (raw) | Tipo | Origem causal (grupo) |
|---|---|---|---|
| `nasa-01-a13-mission-report` | `nasa-01-a13-mission-report.pdf` | relatório oficial de missão (NASA Manned Spacecraft Center, MSC-02654, "Apollo 13 Mission Report", setembro de 1970; 158 p.) | NASA (agência espacial federal dos EUA) |
| `nasa-02-a13-review-board` | `nasa-02-a13-review-board.pdf` | relatório oficial de investigação (NASA, "Report of Apollo 13 Review Board", 15 de junho de 1970; 250 p.) | NASA (painel de investigação nomeado pela agência) |

> Ambas as origens são do acervo público da NASA via NASA Technical Reports Server (NTRS).

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `nasa-01-a13-mission-report.pdf` | `f6941eaeabf8d611d3da88853923d7e85a8f578c577b02b7e65ba9d92bb54988` |
| `nasa-02-a13-review-board.pdf` | `8804b8ccbb69abe4eb239a73f22b9581be3a67c484aa43284efcd71b9da30391` |

## Conformidade

- Apenas fontes brutas primárias; nenhuma narrativa/atomic-facts/reconstrução de SX-001/002/003 importada.
- Rastreabilidade: cada atomic fact e cada bloco narrativo referenciam os `refs` acima.
