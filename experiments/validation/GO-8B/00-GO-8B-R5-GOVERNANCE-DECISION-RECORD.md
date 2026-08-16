# GO-8B-R5 GOVERNANCE DECISION RECORD — DECISIONS CONSUMADAS (R5-GOV-01..04)

**Status:** DECIDED — RECORDED AND APPLIED IN R6
**Tipo:** DECISION RECORD (decisões consumadas pela governança)
**Data da decisão:** 2026-08-11
**Gate:** GOVERNANCE GATE R5 → R6
**Governado por:** GO-8B-R5; R6 application order
**Escopo autorizado:** registrar decisões R5-GOV-01..04; refletir em `06-STATISTICAL-PROTOCOL.md`; executar apenas a simulação metodológica autorizada (STAT-08); AUDITORIA R6.

---

## 1. Proveniência

Este registro documenta a deliberação do GOVERNANCE GATE R5 e a aplicação **R6**. Nenhuma decisão aqui registrada foi tomada por este registro; todas foram emitidas pela governança e são reproduzidas **literalmente** na seção 2. Nenhum parâmetro do protocolo foi alterado além do que estas decisões determinam.

**Conformidade (nada executado fora da autorização):**
- `08-PRE-REGISTRATION.md` — NÃO criado
- Hashes finais — NÃO gerados
- Lock Protocol — NÃO aplicado
- Experimento com dados reais — NÃO executado
- Coleta de dados — NÃO realizada
- Commit — NÃO realizado
- Única execução: **simulação metodológica de cobertura do bootstrap** (STAT-08, autorizada por R5-GOV-04), sem dados experimentais

---

## 2. Decisões Consumadas (reprodução literal)

### R5-GOV-01 — Tamanho de amostra
> **DECIDIDO: (a) N = 7.**

### R5-GOV-02 — Banda oficial de casos
> **DECIDIDO: (a) manter banda separada: mínimo 5 válidos / piloto 7 / potência 12.**

### R5-GOV-03 — Tratamento definitivo de TOST/Δ
> **DECIDIDO: (a) manter status quo: TOST secondary/optional, sem Δ aprovada, não executar TOST no piloto.**

### R5-GOV-04 — Auditoria STAT-04/06/08/09
> **DECIDIDO:**
> - **STAT-04** = não winsorizar + análise de sensibilidade sem outliers;
> - **STAT-06** = exploratório, sem controle formal de família;
> - **STAT-08** = AUTORIZADA apenas simulação metodológica de cobertura do bootstrap, sem dados experimentais;
> - **STAT-09** = sensibilidade excluindo um caso por par dependente; não introduzir modelo misto.

---

## 3. Aplicação em R6

| Decisão | Reflexo documental | Arquivo | Status |
|---|---|---|---|
| R5-GOV-01 (N=7) | §5.3 mantém N=7 como piloto oficial; potência ≈0.63 reportada como limitação pré-registrada | `06-STATISTICAL-PROTOCOL.md` | APLICADO |
| R5-GOV-02 (banda 5/7/12) | §5.4 banda oficial = mínimo 5 válidos / piloto 7 / potência 12 | `06-STATISTICAL-PROTOCOL.md` | APLICADO |
| R5-GOV-03 (TOST status quo) | §8 e §10: TOST secondary/optional, sem Δ aprovada, não executar no piloto | `06-STATISTICAL-PROTOCOL.md` | APLICADO |
| R5-GOV-04 STAT-04 | §6 STAT-04 → FIXADO (não winsorizar + sensibilidade sem outliers) | `06-STATISTICAL-PROTOCOL.md` | APLICADO |
| R5-GOV-04 STAT-06 | §6 STAT-06 → FIXADO (exploratório, sem controle formal de família) | `06-STATISTICAL-PROTOCOL.md` | APLICADO |
| R5-GOV-04 STAT-08 | §6 STAT-08 → FIXADO; §4.3.1 simulação de cobertura executada (B=10.000, seed isolada) | `06-STATISTICAL-PROTOCOL.md` | APLICADO |
| R5-GOV-04 STAT-09 | §6 STAT-09 → FIXADO; §7 sensibilidade excluindo 1 caso por par dependente; sem modelo misto | `06-STATISTICAL-PROTOCOL.md` | APLICADO |

**`07-FAILURE-CRITERIA.md`:** **não alterado** — nenhuma regra operacional depende diretamente das decisões (N=7 e mínimo 5 válidos para análise já vigentes; sensibilidade STAT-09 não altera exclusões nem o Go/No-Go).

**`08-PRE-REGISTRATION.md`:** **NÃO criado** (aguarda autorização separada).

---

## 4. Simulação metodológica executada (STAT-08)

- **Objeto:** cobertura nominal do IC 95% bootstrap percentil (B=10.000) para mediana por condição e diferença de medianas pareadas.
- **Configuração:** DGM idêntico à simulação de potência R5 M-3 (σ_b=0.12, σ_e=0.08, σ_s=0.06; μ=(0.50, 0.60, 0.66); 3 seeds/célula; mediana); MC reps=1.500; **seed `20260812`** (stream isolado, distinta da seed de potência `20260811`).
- **Resultado principal (N=7, piloto):** cobertura mediana cond. A ≈ **0.884**, cond. B ≈ **0.870**, diferença pareada ≈ **0.931**.
- **Interpretação:** B=10.000 é suficiente (erro MC desprezível); a cobertura sub-nominal da **mediana por condição** decorre do **método percentil + N pequeno** (discretude da mediana em N=7), não do nº de reamostragens. Mitigação documental: reportar também o IC exato da mediana (estatística de ordem) ao lado do IC percentil; interpretar o IC percentil da mediana com cautela em N=7 (ver `06 §4.3.1`).
- **Natureza:** análise metodológica independente; nenhum dado experimental; nenhum parâmetro do estudo alterado.

---

## 5. Itens NÃO alterados nesta etapa

- Seeds (3/célula), α=0.05, Friedman primário, Wilcoxon bilateral + Holm, unidade BIP/Caso — **inalterados**.
- Nenhum parâmetro alterado silenciosamente.
- Sem hashes, sem Lock, sem commit, sem experimento, sem coleta.

---

## 6. Próximo passo

1. AUDITORIA R6 (rastreabilidade, consistência 01–07, unidade, N=7, 3 seeds, Friedman, Wilcoxon/Holm, TOST, ausência de alteração silenciosa, ausência de hashes/Lock, ausência de dados).
2. Se CLEAN/PASS → relatório R6; aguardar **autorização separada** para elaboração do `08-PRE-REGISTRATION.md`.
3. Se MAJOR/DECISION REQUIRED novo → STOP.

---

**Fim do Decision Record.** Status: **DECIDED — RECORDED AND APPLIED IN R6**. Estado esperado: `STOP / PENDING R6 AUDIT`.
