# BIP-002 — Hyatt Regency Walkways: Fronteira e Indexamento

**Caso:** Colapso das passarelas suspensas do átrio do Hyatt Regency, Kansas City, Missouri (1981)
**Data de produção:** 2026-08-12
**Escopo de produção (DECIDED):** produção de materiais (ordem manifest §3 — BIP-002)

---

## Fronteira pré/pós gate

| Fase | Escopo permitido |
|---|---|
| **Pré-gate (produção P5)** | Coleta, rastreamento e registro de fontes brutas primárias; produção de narrativa (condição C) e atomic facts (condições A/B), ambos com **zero termos ECP**, com rastreabilidade às fontes. |
| **Pós-gate (execução experimental)** | Apenas reconstrução anonimizada (labels neutros, arestas in/out, sem ECP) e análise conforme 04/06. **Não altera estes materiais.** |

## Fontes registradas

| ref | Arquivo (raw) | Tipo | Origem causal (grupo) |
|---|---|---|---|
| `nbs-01-bss143` | `nbs-01-bss143.pdf` | relatório oficial de investigação técnica (NBS Building Science Series 143; 378 p.) | National Bureau of Standards (agência federal de padrões/engenharia, EUA) |
| `vlex-02-duncan` | `vlex-02-duncan.html` | acórdão judicial publicado (Missouri Court of Appeals, Eastern District, No. 52655; 744 S.W.2d 524, 1988) | Poder Judiciário do Missouri (via espelho público vLex Case Law) |

> Coleta inicial do piloto BIP-002: 2 origens causais primárias independentes obtidas (investigação técnica federal + decisão judicial).
> Complementos facultativos em ciclo posterior: relatório suplementar NBSIR 82-2465A; outras decisões dos litígios civis pós-colapso.

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `nbs-01-bss143.pdf` | `5f75a7b2c28883e3f989afc9bd89f0aa8d2c04dbf1ddc10f851978b45cae0fc3` |
| `vlex-02-duncan.html` | `cb2ee3caa4a449282b5c21a375b94aae8ef7c3c78eb00b5b03a5cf5e37aeba9c` |

## Conformidade

- Apenas fontes brutas primárias; nenhuma narrativa/atomic-facts/reconstrução de SX-001/002/003 importada.
- Rastreabilidade: cada atomic fact e cada bloco narrativo referenciam os `refs` acima.
