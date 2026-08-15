# GO-8D — RELATÓRIO ESTATÍSTICO do Estudo Confirmatório N=12 (DV_confirm)

**Data:** 2026-08-14
**Executor:** `GO-8D/study-output/analyze_g8d.py` (plano inferencial do pré-registro v1.0 §6; espelha
o executor congelado `go8b_statistical_analysis.py` do GO-8B, adaptado para DV_confirm + TOST Δ=0.05)
**Input:** `study-output/pilot_results_g8d.csv` (108 observações: 12 BIPs × 3 condições × 3 seeds)
**Protocolo:** `08-PRE-REGISTRATION-GO-8D.md` v1.0 (APROVADO) · D-06-TOST-DELTA-APPROVED (Δ=0.05) · D-07 (N=12)
**DV confirmatória:** `DV_confirm = (conf + ged_ref + ent)/3` (mediana das 3 seeds por célula — R5 M-3).
**Configuração:** α=0.05 · Bootstrap B=10.000 (percentil, pareado) · seed_statistics=14233797184859982032
(stream isolado, derivado de `SeedSequence(20260815, spawn_key=(0,))`) · **TOST EXECUTADO com Δ=0.05** (D-06).

---

## 1. Data Check e Agregação (passos 1–2)

- 108/108 linhas, todas `PASS` (validação: schema OK, 36 células × 3 seeds, seeds únicas, range [0,1],
  namespaces A/C→CAT e B→SYN, `taxonomy_sha256` por condição: B=`5ba63db7a81c454d…` (C3 corrigida),
  A/C=`c91fecfeae83d9ed…` (C2 T_PERM); gate D-04 revalidado 12/12 BIPs).
- 36 células (12 BIPs × 3 condições) completas com 3 seeds — **OK**.
- Range `DV_confirm`: min=0.5932, max=0.7356 — dentro de [0,1]. Sem missings. **N (válidos) = 12** (nunca multiplicado).

## 2. Medianas por Condição (descritivas — passo 3)

| Condição | Mediana (células) | IC 95% exato da mediana | IQR | Min | Max |
|----------|-------------------|------------------------|-----|-----|-----|
| **A** (cega pura) | **0.7134** | [0.6873, 0.7216] | [0.6900, 0.7200] | 0.6872 | 0.7356 |
| **B** (cega + C3) | **0.6220** | [0.6035, 0.6357] | [0.6097, 0.6331] | 0.5977 | 0.6569 |
| **C** (não-cega) | **0.6843** | [0.6474, 0.7017] | [0.6558, 0.7005] | 0.5932 | 0.7042 |

> IC exato da mediana (STAT-08) reportado ao lado do percentil; distribuição livre, cobertura ≈ 0.9614.

Medianas por caso (célula = mediana das seeds):

| Caso | A | B | C |
|------|-------|-------|-------|
| BIP-001 Deepwater | 0.7180 | 0.6102 | 0.6828 |
| BIP-002 Hyatt | 0.7154 | 0.6323 | 0.7001 |
| BIP-003 OWS | 0.6878 | 0.6357 | 0.6474 |
| BIP-004 Genoma | 0.7356 | 0.6035 | 0.7041 |
| BIP-005 EverGiven | 0.7195 | 0.6119 | 0.6857 |
| BIP-006 I-35W | 0.7324 | 0.6569 | 0.6575 |
| BIP-007 Ebola | 0.6873 | 0.6317 | 0.7017 |
| BIP-008 Apollo13 | 0.6872 | 0.6264 | 0.6509 |
| BIP-009 Chernobyl | 0.6941 | 0.5977 | 0.6978 |
| BIP-010 TacomaNarrows | 0.7216 | 0.6486 | 0.6815 |
| BIP-011 Dominos | 0.6907 | 0.6176 | 0.5932 |
| BIP-012 Eyjafjallajokull | 0.7115 | 0.6081 | 0.7042 |

## 3. Teste Omnibus — Friedman (passo 4, teste global PRIMÁRIO)

| Estatística | Valor |
|---|---|
| **χ²_F** | **18.5000** |
| **df** | **2** |
| **p** | **0.000096** |
| **Kendall's W** | **0.7708** (efeito grande, W≈0.77) |
| **IC 95% bootstrap de W** | **(0.5833, 1.0000)** |

**Decisão (α=0.05):** p < 0.05 → **REJEITA H₀** — pelo menos uma condição difere.
→ Post-hoc confirmatório **AUTORIZADO** (passo 5).

## 4. Post-hoc — Wilcoxon pareado bilateral + Holm-Bonferroni (passo 5)

| Par | p (bruto) | Holm (α=0.05/3) | r_rb | Cliff δ | IC95% dif. mediana | IC95% Cliff |
|-----|-----------|-----------------|------|---------|--------------------|-------------|
| **A vs B** | **0.0005** | **REJEITA** (≤0.0167) | −1.000 | 1.000 | (−0.108, −0.059) | (1.000, 1.000) |
| **A vs C** | **0.0034** | **REJEITA** (≤0.0500) | −0.897 | 0.653 | (−0.049, 0.004) | (0.250, 0.917) |
| **B vs C** | **0.0024** | **REJEITA** (≤0.0250) | 0.923 | −0.792 | (0.025, 0.090) | (−1.000, −0.458) |

> Holm-Bonferroni (α=0.05, 3 comparações), p ordenados: A−B (0.0005 ≤ 0.0167) **rejeitada**;
> B−C (0.0024 ≤ 0.0250) **rejeitada**; A−C (0.0034 ≤ 0.0500) **rejeitada**. Todas as 3 rejeitadas.

**Interpretação (sinal da DV_confirm = fidelidade da reconstrução):**
- **A vs B:** rejeita H₀. Direção: **A > B** (mediana A 0.7134 > B 0.6220; r_rb=−1.000; Cliff δ=1.000;
  IC da diferença de medianas (−0.108, −0.059) exclui 0). A condição cega pura (A) tem **maior**
  DV_confirm que a cega + taxonomia C3 (B) — efeito **negativo** da taxonomia C3 na fidelidade medida.
- **A vs C:** rejeita H₀. Direção: **A > C** (r_rb=−0.897; Cliff δ=0.653). A cega pura supera a
  não-cega (narrativa completa) na DV_confirm.
- **B vs C:** rejeita H₀. Direção: **C > B** (r_rb=0.923; Cliff δ=−0.792). A narrativa completa (C)
  supera a cega + C3 (B).

## 5. TOST / Equivalência — Δ=0.05 (D-06 APROVADO, secundária; passo 5/6)

| Par | Dif. média | IC 95% pareado (bootstrap) | Δ=0.05 | Equivalência (IC ⊂ (−0.05, +0.05)) |
|-----|-----------|---------------------------|--------|-------------------------------------|
| A vs B | −0.0850 | (−0.0988, −0.0721) | 0.05 | **NÃO** (IC inteiramente fora) |
| A vs C | −0.0328 | (−0.0501, −0.0171) | 0.05 | **NÃO** (limite inferior −0.0501 < −0.05, marginal) |
| B vs C | +0.0522 | (0.0288, 0.0740) | 0.05 | **NÃO** |

- **A vs C (hipótese de equivalência pré-registrada §5.3):** IC 95% da diferença pareada
  (−0.0501, −0.0171) **não** está inteiramente contido em (−0.05, +0.05) — o limite inferior
  (−0.0501) excede Δ em 0.0001. **Equivalência NÃO demonstrada** dentro de Δ=0.05 (marginal; efeito
  observado ≈ 0.033 próximo do Δ). Reportado com cautela (pré-registro §9: TOST não-equivalente
  perto do limiar → sem conclusão forte).
- A vs B e B vs C: efeitos > Δ em magnitude; TOST corretamente **rejeita** equivalência
  (consistente com potência de rejeição ~1.0 pré-registrada).

## 6. Sensibilidade (passo 7)

| Análise | N | Friedman p | Kendall W |
|---------|-----|-----------|-----------|
| Sem outliers (IQR×1.5) | 12 | nenhum flag | — |
| Drop BIP-001..006, 008, 010, 012 | 11 | 0.0003 | 0.7521 |
| Drop BIP-007 ou 009 | 11 | 0.0001 | 0.8264 |
| Drop BIP-011 | 11 | 0.0001 | 0.8512 |

Todas as sensibilidades (drop de 1 caso por vez — STAT-09, sem domínios no GO-8D) mantêm p < 0.05
→ a rejeição omnibus é **robusta**. Sem modelo misto (STAT-09). Sem winsorização (STAT-04).

## 7. Decisão Final — Go/No-Go (pré-registro §8)

| Critério (pré-registro GO-8D §8) | Limiar | Observado | Status |
|---|---|---|---|
| Casos válidos | ≥ 10 de 12 | 12 | **PASS** |
| Matriz N×3 completa | = N_casos | 36/36 células | **PASS** |
| Nenhum FAIL de execução | — | 108/108 PASS | **PASS** |
| Gates D-04 (parseabilidade) + D-05 (semântico) | PASS pré-Lock | 12/12 BIPs (D-04) | **PASS** |

**Go/No-Go metodológico (pré-registro §8): GO — 12/12 casos válidos ≥ 10 → análise estatística
procede e é válida.**

## 8. Decisão inferencial (pré-registro §9 — Decision Rules)

- **Friedman p=0.000096 < 0.05** → **rejeita H₀ omnibus** (evidência de que pelo menos uma condição difere).
- **B−A (p=0.0005) e B−C (p=0.0024) significativos pós-Holm** → gatilho das regras de interpretação
  §9 acionado. Porém a **direção** do efeito da taxonomia C3 é **contrária à hipótese de utilidade**:
  mediana B (0.6220) < A (0.7134), com efeito pareado A−B ≈ −0.079 (r_rb=−1.000, Cliff δ=1.000).
  → **A taxonomia C3 NÃO demonstra melhoria na DV_confirm; o efeito observado é negativo**
  (a condição cega pura A é sistematicamente superior em todos os 12 BIPs).
- **C vs B:** narrativa completa (C) supera B (p=0.0024; r_rb=0.923) → efeito da informação completa
  presente, mas **C ainda fica abaixo de A** (A > C, p=0.0034).
- **Equivalência A−C:** **não demonstrada** dentro de Δ=0.05 (IC marginal; efeito ≈ 0.033 próximo de Δ).

## 9. Conclusão

1. **Go/No-Go: GO** (12/12 válidos; matriz completa; 108/108 execuções PASS; gates pré-Lock PASS).
2. **Omnibus:** diferença entre condições presente e estatisticamente significativa (Friedman
   p=0.000096, W=0.77 — efeito grande), robusta a sensibilidades.
3. **Contra a hipótese de utilidade da C3:** a taxonomia C3 (B) **reduz** a DV_confirm em relação à
   cega pura (A) — significativo pós-Holm em todos os 12 BIPs (Cliff δ=1.000). Não há evidência de
   que C3 melhore a fidelidade da reconstrução sob a DV_confirm.
4. **Narrativa completa (C)** supera B, mas permanece abaixo de A — a adição de informação não
   recupera o nível da condição cega pura.
5. **Equivalência A−C** não é demonstrada (IC marginal em Δ=0.05); sem decisão unilateral (R3-04).
6. Potência pré-registrada N=12 (Friedman 0.999) confere adequação; não se conclui "ausência de
   efeito" — o efeito A−B observado (≈0.079) está acima do Δ e é estatisticamente significativo.

---

**Fim do relatório. Nenhum artefato congelado (GO-8B, GO-8C ou Lock GO-8D) alterado. Execução,
validação e análise do estudo confirmatório GO-8D concluídas conforme pré-registro v1.0.