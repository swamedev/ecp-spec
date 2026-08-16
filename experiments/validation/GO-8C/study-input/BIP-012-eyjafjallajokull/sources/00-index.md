# BIP-012 — Eyjafjallajökull: Fronteira e Indexamento

**Caso:** Erupção do vulcão Eyjafjallajökull e interrupção do transporte aéreo europeu (2010)
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
| `icao-01-journal-2010` | `icao-01-journal-2010.pdf` | publicação oficial (ICAO Journal, Vol. 65, No. 4, 2010 — "Safety as a Guiding Priority", edição dedicada à crise das cinzas vulcânicas de 2010; 40 p.) | International Civil Aviation Organization (ICAO) |
| `iata-02-ash-plume` | `iata-02-ash-plume.pdf` | nota econômica oficial (IATA Economics, "The Impact of Eyjafjallajokull's Volcanic Ash Plume", maio de 2010; 4 p.) | International Air Transport Association (IATA) |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `icao-01-journal-2010.pdf` | `ed4aa60034290b022835fb15d92a5fd65be64f4cb42eb1deafae8f06e34245b2` |
| `iata-02-ash-plume.pdf` | `40f577721c56765340e53c149ca9cc81eb1a560490bb5cf4fadd10ec093d6539` |

## Conformidade

- Apenas fontes brutas primárias; nenhuma narrativa/atomic-facts/reconstrução de SX-001/002/003 importada.
- Rastreabilidade: cada atomic fact e cada bloco narrativo referenciam os `refs` acima.
