# BIP-001 — Deepwater Horizon / Macondo: Fronteira e Indexamento

**Caso:** Deepwater Horizon / Macondo (2010)
**Data de produção:** 2026-08-12
**Escopo de produção (DECIDED):** avançar BIP-001 (coleta de fontes + produção de materiais)

---

## Fronteira pré/pós gate

| Fase | Escopo permitido |
|---|---|
| **Pré-gate (produção P5)** | Coleta, rastreamento e registro de fontes brutas primárias; produção de narrativa (condição C) e atomic facts (condições A/B), ambos com **zero termos ECP**, com rastreabilidade às fontes. |
| **Pós-gate (execução experimental)** | Apenas reconstrução anonimizada (labels neutros, arestas in/out, sem ECP) e análise conforme 04/06. **Não altera estes materiais.** |

## Fontes registradas

| ref | Arquivo (raw) | Tipo | Origem causal (grupo) |
|---|---|---|---|
| `ncom-01-gulf` | `ncom-01-gulf-oil-disaster-2011.pdf` | relatório oficial (398 p.) | Comissão Nacional (EUA) |
| `csb-01-macondo-v1` | `csb-01-macondo-vol1-2014.pdf` | relatório oficial (Vol. 1) | CSB (EUA) |
| `jit-01-report` | `jit-01-report-causes-macondo-2011.pdf` | relatório oficial (217 p.) | JIT BOEMRE/USCG (EUA) |

> Coleta inicial do piloto BIP-001: 3 origens causais primárias independentes obtidas.
> O restante do plano (auditoria interna BP, audiências do Congresso, imprensa contemporânea)
> permanece pendente e pode ser adicionado em ciclo posterior.

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `ncom-01-gulf-oil-disaster-2011.pdf` | `f0a242909914e4d00200005734ce9b240b1b4c58e0e8af04e95387717780b23c` |
| `csb-01-macondo-vol1-2014.pdf` | `89c1405abe04fb200c7c03804365dc35e193fa5fbbc36c1b0b9b91c0de64bed6` |
| `jit-01-report-causes-macondo-2011.pdf` | `7846d4409ae6ebfba7bc51197a471911c364afa1a4e0ad054e47f5afbf351c8d` |

## Conformidade

- Apenas fontes brutas primárias; nenhuma narrativa/atomic-facts/reconstrução de SX-001/002/003 importada.
- Rastreabilidade: cada atomic fact e cada bloco narrativo referenciam os `refs` acima.
