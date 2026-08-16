# BIP-005 — Ever Given / Suez: Fronteira e Indexamento

**Caso:** Ever Given — Canal de Suez (2021)
**Data de produção:** 2026-08-12
**Escopo de produção (DECIDED):** produção de materiais (ordem manifest §3 — BIP-005)

---

## Fronteira pré/pós gate

| Fase | Escopo permitido |
|---|---|
| **Pré-gate (produção P5)** | Coleta, rastreamento e registro de fontes brutas primárias; produção de narrativa (condição C) e atomic facts (condições A/B), ambos com **zero termos ECP**, com rastreabilidade às fontes. |
| **Pós-gate (execução experimental)** | Apenas reconstrução anonimizada (labels neutros, arestas in/out, sem ECP) e análise conforme 04/06. **Não altera estes materiais.** |

## Fontes registradas

| ref | Arquivo (raw) | Tipo | Origem causal (grupo) |
|---|---|---|---|
| `pma-01-ever-given` | `pma-01-final-investigation-ever-given.pdf` | relatório oficial de investigação (68 p.) | Autoridade Marítima do Panamá (estado de bandeira) |
| `ukpandi-01-media` | `ukpandi-01-ever-given-media-statement.html` | declarações públicas sequenciais | UK P&I Club (seguradora P&I do navio) |

> Coleta inicial do piloto BIP-005: 2 origens causais primárias independentes obtidas.
> Complementos facultativos em ciclo posterior: comunicações da SCA, cobertura de imprensa contemporânea, dados de satélite.

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `pma-01-final-investigation-ever-given.pdf` | `a459508e312307417f2bafadc7cdb8fba46a7a667483d6d6bf35dea2e05bc9fb` |
| `ukpandi-01-ever-given-media-statement.html` | `ec59841084b406234c5ce0e860158733bd321e801077ecf6fa9045db028914cd` |

## Conformidade

- Apenas fontes brutas primárias; nenhuma narrativa/atomic-facts/reconstrução de SX-001/002/003 importada.
- Rastreabilidade: cada atomic fact e cada bloco narrativo referenciam os `refs` acima.
