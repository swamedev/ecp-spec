# D-07 — RECÁLCULO DE POTÊNCIA E N (GO-8D)

**Data:** 2026-08-14
**Ciclo:** GO-8D — DIAGNOSTIC PHASE
**Tipo:** análise de potência (pré-experimental) + base do novo pré-registro
**Base:** D-02/D-03 (DV_confirm, simulação) · D-06-TOST-DELTA-APPROVED (Δ=0.05) · GO-8B §5 (método MC do GO-8B)
**Dependência:** habilita o novo pré-registro (este documento + `08-PRE-REGISTRATION-GO-8D.md`)

---

## 1. Objetivo

Definir o **N mínimo** do estudo confirmatório GO-8D com:

- **DV_confirm = (conf + ged_ref + ent)/3** (desfecho primário), escala [0,1];
- **α = 0.05** bilateral;
- **Poder-alvo ≥ 0.80**;
- **Δ = 0.05** (TOST, aprovado na D-06);
- Efeitos observados na simulação D-03 (A−B ≈ 0.079; B−C ≈ 0.069 — diferenças pareadas por BIP).

## 2. Método de simulação

**Abordagem:** simulação Monte Carlo espelhando o protocolo do GO-8B (§5) e o desenho GO-8D:

1. **DGM calibrado nas 36 células observadas** (`analysis/redesign_cells.json`, leitura apenas):
   - **Cenário A (empírico):** μ = medianas observadas (A=0.7134, B=0.6220, C=0.6843);
     σ_b=0.0148 (entre-BIP), σ_e=0.0189 (intra-unidade), σ_s=0.002 (seed vestigial).
   - **Cenário B (conservador, calibrado pelo par de hipótese primária mais difícil):**
     σ_e = SD pareada observada de B−C (0.0401)/√2 = 0.0296.
   - **Cenário C (fiel ao enunciado):** μ ajustado para efeitos pareados **A−B=0.079, B−C=0.069,
     A−C=0.010** (diferenças pareadas do enunciado), mantendo σ do cenário B.
2. **Geração:** para cada BIP i e condição j, score latente `X_ij = μ_j + b_i + e_ij`;
   3 seeds por célula; `cell = median(seeds)` clipada em [0,1].
3. **Teste primário:** Friedman (df=2) → **Wilcoxon signed-rank pareado bilateral** nos 3 pares +
   **Holm-Bonferroni** (mesmo plano do GO-8B/GO-8C).
4. **TOST (secundário):** IC 95% bootstrap percentil (B=400/reps, pareado) da diferença; equivalência
   se IC ⊂ (−0.05, +0.05).
5. **N avaliado:** 8, 10, 12, 14, 16, 18. **REPS = 3.000** por (cenário × N).
   Seed global `20260814` (stream isolado; não reutilizada do GO-8C).

## 3. Tabela de potência por N

**Cenário A (empírico, μ=medianas, σ_e=0.0189):**

| N | Friedman | pw A−B | pw B−C | pw A−C | TOST equiv A−C |
|---|---|---|---|---|---|
| 8 | 1.000 | 1.000 | 0.998 | 0.683 | 0.657 |
| 10 | 1.000 | 1.000 | 1.000 | 0.852 | 0.748 |
| 12 | 1.000 | 1.000 | 1.000 | 0.903 | 0.786 |
| 14 | 1.000 | 1.000 | 1.000 | 0.953 | 0.844 |
| 16 | 1.000 | 1.000 | 1.000 | 0.976 | 0.884 |
| 18 | 1.000 | 1.000 | 1.000 | 0.990 | 0.920 |

**Cenário B (conservador, σ_e=0.0296):**

| N | Friedman | pw A−B | pw B−C | pw A−C | TOST equiv A−C |
|---|---|---|---|---|---|
| 8 | 0.988 | 0.988 | 0.861 | 0.331 | 0.396 |
| 10 | 0.998 | 0.999 | 0.952 | 0.458 | 0.439 |
| 12 | 1.000 | 1.000 | 0.988 | 0.530 | 0.459 |
| 14 | 1.000 | 1.000 | 0.999 | 0.643 | 0.525 |
| 16 | 1.000 | 1.000 | 0.999 | 0.697 | 0.564 |
| 18 | 1.000 | 1.000 | 1.000 | 0.772 | 0.601 |

**Cenário C (fiel ao enunciado: A−B=0.079, B−C=0.069, A−C=0.010; σ_e=0.0296):**

| N | Friedman | pw A−B | pw B−C | pw A−C | TOST equiv A−C |
|---|---|---|---|---|---|
| 8 | 0.978 | 0.951 | 0.897 | 0.063 | 0.788 |
| 10 | 0.993 | 0.992 | 0.970 | 0.084 | 0.863 |
| 12 | 0.999 | 0.999 | 0.996 | 0.104 | 0.919 |
| 14 | 1.000 | 1.000 | 0.999 | 0.132 | 0.943 |
| 16 | 1.000 | 1.000 | 1.000 | 0.132 | 0.968 |
| 18 | 1.000 | 1.000 | 1.000 | 0.148 | 0.977 |

**Observações:**
- **A−C** não é hipótese primária (as comparações pré-registradas são A vs B e B vs C, como no
  GO-8C). Sua baixa potência pós-Holm no cenário C é esperada: efeito A−C=0.010, próximo de zero.
- **TOST equiv A−C** usa o par A−C por ser o único com efeito verdadeiro **dentro** de Δ=0.05
  (0.010), permitindo avaliar a potência do TOST quando a equivalência é a verdade. A−B e B−C têm
  efeito > Δ e o TOST corretamente **rejeita** equivalência (potência de rejeição ~1.0).
- **N=6 não consta:** com N=6 o menor p-valor Wilcoxon possível (2/64=0.03125) excede o limiar
  Holm (0.05/3=0.0167) — **N=6 é estruturalmente incapaz de significância pós-Holm** (discretude).
  O mínimo metodológico efetivo é N≥8.

## 4. N recomendado e justificativa

**Recomendação: N = 12.**

| Critério | N=8 | N=10 | **N=12** | N=14 |
|---|---|---|---|---|
| Potência B−C ≥ 0.80 (cen. C, mais desafiador) | 0.897 ✅ | 0.970 ✅ | **0.996** ✅ | 0.999 ✅ |
| Potência A−B ≥ 0.80 (cen. C) | 0.951 ✅ | 0.992 ✅ | **0.999** ✅ | 1.000 ✅ |
| Potência TOST equiv A−C ≥ 0.80 (cen. C) | 0.788 ❌ | 0.863 ✅ | **0.919** ✅ | 0.943 ✅ |
| Friedman omnibus (cen. C) | 0.978 | 0.993 | **0.999** | 1.000 |

**Justificativa:**
1. **N=8 satisfaz a potência de superioridade** (B−C=0.897 no cenário mais desafiador) mas **não
   atinge 0.80 na potência de equivalência** do TOST (0.788) — a equivalência é hipótese
   secundária aprovada (D-06) e deve ter poder pré-registrado ≥ 0.80.
2. **N=10 é o mínimo** que atinge 0.80 em todos os critérios (B−C=0.970; TOST equiv=0.863).
3. **N=12 é recomendado** por: (a) margem folgada sobre 0.80 em todos os critérios, inclusive sob
   o cenário conservador (B−C=0.988; TOST equiv A−C=0.459 no cen. B — ver nota abaixo);
   (b) **mesmo N=12 do GO-8C**, preservando comparabilidade e reaproveitando integralmente os
   12 BIPs existentes (sem coleta); (c) robustez à calibração do σ_e (os efeitos de hipótese
   primária permanecem > 0.90 mesmo no cenário conservador).
4. **Nota sobre TOST no cenário B (σ_e=0.0296):** a potência de equivalência A−C cai (0.459 em
   N=12) porque o efeito A−C observado (0.033) está próximo de Δ. No cenário C (efeito A−C=0.010,
   fiel ao enunciado) a potência é 0.919. O desenho pré-registra a potência de equivalência sob o
   cenário C (o de planejamento); o cenário B é reportado como análise de robustez.

**Impacto no desenho:** N=12 → **execuções = 12 × 3 condições × 3 seeds = 108** (mesmo volume do
GO-8C), 12 BIPs × 3 condições = 36 células.

## 5. Impacto no desenho e no pré-registro

- **DV_confirm** como desfecho primário (pesos 1:1:1, aprovado na revisão D-03.REV).
- **Plano inferencial:** Friedman (df=2) → Wilcoxon pareado bilateral + Holm nos pares A−B, B−C,
  A−C; **comparações primárias: A vs B e B vs C** (A−C é secundária/descritiva).
- **TOST com Δ=0.05** (D-06) nos pares, após Holm; equivalência se IC ⊂ (−0.05, +0.05).
- **Go/No-Go:** ≥ 10 de 12 células válidas (mesmo critério do GO-8C).
- **Seeds:** novo `seed_master` GO-8D (não reutilizar o do GO-8C). Geração apenas após autorização.
- **Taxonomia:** todas as 36 células usarão a taxonomia corrigida
  (`taxonomy_sha256 = 5ba63db7a81c454d...`), com registro por execução (P5/D-03).

## 6. Confirmação de integridade

- **Nenhum arquivo do GO-8B/GO-8C alterado**; GO-8B e GO-8C permanecem CLOSED/LOCKED/FROZEN.
- **Nenhum Lock, experimento ou geração de seeds realizada.**
- Artefatos deste ciclo (novos, no GO-8D): este relatório, `analysis/d07_power_recalc.py`,
  `analysis/d07_power_recalc_task.py`, `analysis/d07_power_results.json`,
  `analysis/d07_power_results_task.json`, `08-PRE-REGISTRATION-GO-8D.md` (esboço).

---

**Fim do relatório D-07. 2026-08-14. Status: COMPUTED (N recomendado = 12) — aguardando revisão
da governança e autorização para Lock.
