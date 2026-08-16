# BIP-011 — Domino's Turnaround: Fronteira e Indexamento

**Caso:** Reviravolta da Domino's Pizza (2009–2010)
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
| `sec-01-10k-2009` | `sec-01-10k-2009.htm` | arquivamento regulatório oficial (Form 10-K da Domino's Pizza, Inc., ano fiscal encerrado em 3 de janeiro de 2010, arquivado em 2 de março de 2010; documento principal d10k.htm) | SEC (U.S. Securities and Exchange Commission) — EDGAR |
| `sec-02-10k-2010` | `sec-02-10k-2010.htm` | arquivamento regulatório oficial (Form 10-K da Domino's Pizza, Inc., ano fiscal encerrado em 2 de janeiro de 2011, arquivado em 1 de março de 2011; documento principal d10k.htm) | SEC (U.S. Securities and Exchange Commission) — EDGAR |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `sec-01-10k-2009.htm` | `9a466a70c5810178055fc3dab8dbf6e2882fbffcb0f6ac5fd2ced04f84a45931` |
| `sec-02-10k-2010.htm` | `2c12f9f865c6100a7c499510abf3aa739224edacfcbaf436806f7a898bf8fd02` |

## Conformidade

- Apenas fontes brutas primárias; nenhuma narrativa/atomic-facts/reconstrução de SX-001/002/003 importada.
- Rastreabilidade: cada atomic fact e cada bloco narrativo referenciam os `refs` acima.
