# GO-8D — STATE

**Ciclo:** GO-8D
**Atualizado em:** 2026-08-14
**Status do ciclo:** **OPENED / DIAGNOSTIC PHASE — NO EXPERIMENT AUTHORIZED**

---

## Estado consolidado

| Ciclo | Status |
|---|---|
| **GO-8B** | **CLOSED / LOCKED / FROZEN** (registro histórico imutável) |
| **GO-8C** | **CLOSED** — estudo confirmatório N=12 concluído (Go/No-Go GO, 12/12); Lock GO-8C LOCKED (151 artefatos, validado PASS) |
| **GO-8D** | **OPENED** — fase de diagnóstico das dívidas D-01..D-07; **nenhum experimento autorizado** |

---

## Dívidas em aberto (GO-8D)

| ID | Dívida | Bloco | Estado |
|----|--------|-------|--------|
| D-01 | S_struct — viés estrutural | 1 — Validade da medida | **DIAGNOSED** (relatório: `experiments/validation/GO-8C/decisions/D-01-SSTRUCT-AUDIT.md`) |
| D-02 | Métricas alternativas | 1 — Validade da medida | **DIAGNOSED** (relatório: `experiments/validation/GO-8D/decisions/D-02-METRICS-ANALYSIS.md`) |
| D-03 | Reprojeto do pipeline / taxonomia C3 | 1 — Validade da medida | **DIAGNOSED / PROPOSED** (relatório: `experiments/validation/GO-8D/decisions/D-03-PIPELINE-REDESIGN.md`; DV recomendada `conf+ged_ref+ent`) |
| D-04 | Gate de parseabilidade | 2 — Validade do desenho | **PENDING** |
| D-05 | Gate semântico híbrido | 2 — Validade do desenho | **PENDING** |
| D-06 | Definição de Δ para TOST | 2 — Validade do desenho | **PENDING** |
| D-07 | Recalcular N após estabilizar a métrica | 3 — Poder estatístico | **PENDING** (bloqueado por D-02/D-03) |

---

## Regras vigentes

- Nenhum arquivo do GO-8B ou do GO-8C pode ser alterado por este ciclo.
  (Exceção única já registrada: correção factual do relatório de diagnóstico
  `GO-8C/decisions/D-01-SSTRUCT-AUDIT.md` sobre o BIP-007-B — não é artefato do Lock.)
- Nenhuma dívida é executada sem autorização formal e explícita por etapa.
- Nenhum experimento novo é autorizado até D-01..D-07 concluídos e aprovados.
- Próximo passo aguardando autorização: **D-07 (novo pré-registro com a DV `conf+ged_ref+ent`,
  recálculo de N e novo Lock)** — revisão da governança sobre o desenho proposto na D-03.

---

**Fim do estado. GO-8D OPENED (2026-08-14).