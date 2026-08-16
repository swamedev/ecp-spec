# BIP-009 — Chernobyl Unidade 4: Fronteira e Indexamento

**Caso:** Acidente da unidade 4 da Usina Nuclear de Chernobyl (1986)
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
| `iaea-02-insag1` | `iaea-02-insag1.pdf` | relatório oficial de revisão pós-acidente (IAEA Safety Series No. 75-INSAG-1, "Summary Report on the Post-Accident Review Meeting on the Chernobyl Accident", 1986; 123 p.) | International Atomic Energy Agency (IAEA) — International Nuclear Safety Advisory Group (INSAG) |
| `iaea-01-insag7` | `iaea-01-insag7.pdf` | relatório oficial de atualização (IAEA Safety Series No. 75-INSAG-7, "The Chernobyl Accident: Updating of INSAG-1", 1992; 148 p.) | IAEA — INSAG |

> A ordem de `ref` reflete a cronologia do conteúdo (INSAG-1 de 1986 precede INSAG-7 de 1992), independentemente da ordem de download.

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `iaea-02-insag1.pdf` | `6dfcabfd525bbe91ab6a6ac81f427e14cddcbff82100c31cff328664a18c1c3b` |
| `iaea-01-insag7.pdf` | `75627db871b8cec591eaf9443ef32da70e6ccb72c34c38b01c18933e21152455` |

## Conformidade

- Apenas fontes brutas primárias; nenhuma narrativa/atomic-facts/reconstrução de SX-001/002/003 importada.
- Rastreabilidade: cada atomic fact e cada bloco narrativo referenciam os `refs` acima.
