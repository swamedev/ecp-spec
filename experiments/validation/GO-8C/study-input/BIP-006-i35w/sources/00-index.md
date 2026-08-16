# BIP-006 — I-35W Bridge: Fronteira e Indexamento

**Caso:** Colapso da ponte I-35W sobre o rio Mississippi, Minneapolis (2007)
**Data de produção:** 2026-08-12
**Escopo de produção (DECIDED):** produção de materiais (ordem manifest §3 — BIP-006)

---

## Fronteira pré/pós gate

| Fase | Escopo permitido |
|---|---|
| **Pré-gate (produção P5)** | Coleta, rastreamento e registro de fontes brutas primárias; produção de narrativa (condição C) e atomic facts (condições A/B), ambos com **zero termos ECP**, com rastreabilidade às fontes. |
| **Pós-gate (execução experimental)** | Apenas reconstrução anonimizada (labels neutros, arestas in/out, sem ECP) e análise conforme 04/06. **Não altera estes materiais.** |

## Fontes registradas

| ref | Arquivo (raw) | Tipo | Origem causal (grupo) |
|---|---|---|---|
| `ntsb-01-har0803` | `ntsb-01-har0803.pdf` | relatório oficial de investigação de acidente rodoviário (NTSB/HAR-08/03; 178 p.) | National Transportation Safety Board (autoridade federal de segurança) |
| `mngov-01-gpm` | `mngov-01-gpm-investigative.pdf` | relatório investigativo independente encomendado pelo legislativo (126 p.) | Gray Plant Mooty / Joint Committee da legislatura de Minnesota (poder legislativo estadual) |

> Coleta inicial do piloto BIP-006: 2 origens causais primárias independentes obtidas.
> Complementos facultativos em ciclo posterior: resposta formal do MnDOT ao NTSB, relatórios USFA/FEMA e da Universidade de Minnesota.

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `ntsb-01-har0803.pdf` | `394dd568979e0bc14b22aa8c3da62bd4467ed580e779c3aaec02929293549dea` |
| `mngov-01-gpm-investigative.pdf` | `81717a1d8d9c6b63c5ca23a1b2d9f6b0f6c5c9ee80ffd2bb152468dfb1db0707` |

## Conformidade

- Apenas fontes brutas primárias; nenhuma narrativa/atomic-facts/reconstrução de SX-001/002/003 importada.
- Rastreabilidade: cada atomic fact e cada bloco narrativo referenciam os `refs` acima.
