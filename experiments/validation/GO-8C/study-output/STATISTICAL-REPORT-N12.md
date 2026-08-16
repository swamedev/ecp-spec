# GO-8C — RELATÓRIO ESTATÍSTICO do Estudo Confirmatório N=12 (S_struct)

**Data:** 2026-08-14
**Executor:** script estatístico congelado `scripts/go8b/go8b_statistical_analysis.py` (GO-8B), executado sobre os dados finais do GO-8C (108 execuções válidas).
**Input:** `study-output/stats_input_sstruct_n12.csv` (108 observações: 12 BIPs × 3 condições × 3 seeds)
**Protocolo:** `08-PRE-REGISTRATION-N12.md` (replica `06-STATISTICAL-PROTOCOL.md` §7 do GO-8B)
**DV confirmatória:** `S_struct` (mediana das 3 seeds por célula — R5 M-3). `S_sem` = exploratória.
**Configuração:** α=0.05 · Bootstrap B=10.000 (percentil, pareado) · seed_statistics=1879048193 · **TOST não executado** (nenhuma Δ aprovada).

---

## 1. Data Check e Agregação (passos 1–2)

- 108/108 linhas, todas `PASS` (nenhum `FAIL`; validação de dados: schema OK, 36 células × 3 seeds, 0 mismatches de seeds, range [0,1], namespaces A/C→CAT e B→SYN, 0 NAMESPACE_MIX).
- 36 células (12 BIPs × 3 condições) completas com 3 seeds — **OK**.
- Range `S_struct`: min=0.5539, max=0.7081 — dentro de [0,1].
- Sem missings. **N (válidos) = 12** (nunca multiplicado).

## 2. Medianas por Condição (descritivas — passo 3)

### S_struct (DV confirmatória)

| Condição | Mediana (células) | IC 95% exato da mediana | IQR | Min | Max |
|----------|-------------------|------------------------|-----|-----|-----|
| **A** (cega pura) | **0.5875** | [0.5785, 0.6383] | [0.5853, 0.6002] | 0.5721 | 0.6828 |
| **B** (cega + C3) | **0.6348** | [0.5950, 0.6823] | [0.5950, 0.6821] | 0.5785 | 0.7081 |
| **C** (não-cega) | **0.5843** | [0.5676, 0.6048] | [0.5676, 0.5918] | 0.5539 | 0.6277 |

> IC exato da mediana (STAT-08) reportado ao lado do percentil; distribuição livre, cobertura ≈ 0.9614.

Medianas por caso (célula = mediana das seeds):

| Caso | A | B | C |
|------|-------|-------|-------|
| Apollo13 | 0.5785 | 0.5950 | 0.5539 |
| Chernobyl | 0.6383 | 0.6348 | 0.5875 |
| Deepwater | 0.5875 | 0.5866 | 0.5721 |
| Dominos | 0.5721 | 0.6348 | 0.6048 |
| Ebola | 0.6383 | 0.5950 | 0.5821 |
| Eyjafjallajokull | 0.5785 | 0.5785 | 0.6277 |
| Genoma | 0.5875 | 0.7081 | 0.5866 |
| Hyatt | 0.5875 | 0.6439 | 0.5875 |
| I-35W | 0.5875 | 0.6820 | 0.5676 |
| Suez | 0.6828 | 0.6833 | 0.5676 |
| TacomaNarrows | 0.5875 | 0.6823 | 0.6277 |
| WarpSpeed | 0.5875 | 0.5950 | 0.5676 |

### S_sem (exploratória)

| Condição | Mediana (células) |
|----------|-------------------|
| A | 0.5495 |
| B | 0.5532 |
| C | 0.5478 |

## 3. Teste Omnibus — Friedman (passo 4, teste global PRIMÁRIO)

| Estatística | Valor |
|---|---|
| **χ²_F** | **9.7826** |
| **df** | **2** |
| **p** | **0.0075** |
| **Kendall's W** | **0.4076** (efeito médio, W≈0.4) |
| **IC 95% bootstrap de W** | **(0.1267, 0.7622)** |

**Decisão (α=0.05):** p < 0.05 → **REJEITA H₀** — pelo menos uma condição difere.
→ Post-hoc confirmatório **AUTORIZADO** (passo 5).

## 4. Post-hoc — Wilcoxon pareado bilateral + Holm-Bonferroni (passo 5)

| Par | p (bruto) | Holm | r_rb | Cliff δ | IC95% dif. mediana | IC95% Cliff |
|-----|-----------|------|------|---------|--------------------|-------------|
| A vs B | 0.0537 | não rejeita | 0.667 | −0.486 | (0.002, 0.095) | (−0.819, −0.125) |
| A vs C | 0.3086 | não rejeita | −0.364 | 0.368 | (−0.036, 0.013) | (−0.139, 0.792) |
| **B vs C** | **0.0093** | **REJEITA** | **−0.821** | **0.701** | (−0.105, −0.008) | (0.361, 0.958) |

> Holm-Bonferroni (α=0.05, 3 comparações): ordenar p → B-C (0.0093 ≤ 0.05/3=0.0167): **rejeitada**;
> A-B (0.0537 > 0.05/2=0.025): **não rejeitada**; A-C: não rejeitada.

**Interpretação:** única comparação significativa pós-correção é **B > C**
(diferença de medianas negativa = C menor que B; r_rb=−0.821; Cliff δ=0.701 — efeito grande).
A vs B não é significativo após Holm (p=0.0537), mas a direção favorece B
(r_rb=0.667; mediana B > mediana A em 0.0473), com IC de diferença de medianas (0.002, 0.095) **não contendo 0**.

## 5. Exploratório (passo 6 — não confirmatório)

- Interação Caso × Condição: comportamento heterogêneo por domínio
  (ex.: Genoma B=0.7081 é o pico; Suez A=0.6828; TacomaNarrows B=0.6823).
- S_sem (diagnóstico): variação mínima entre condições (0.5478–0.5532); exploratória, entra no relatório sem decisão inferencial.
- Spearman S_struct × aux: não executado (sem `aux_value` no input).

## 6. Sensibilidade (passo 7)

| Análise | N | Friedman p | Kendall W |
|---------|-----|-----------|-----------|
| Sem outliers (IQR×1.5) | 9 | 0.0200 | 0.4346 |
| Domínio Civil — drop Hyatt | 11 | 0.0142 | 0.3869 |
| Domínio Civil — drop I-35W | 11 | 0.0179 | 0.3658 |
| Domínio Saúde — drop Ebola | 11 | 0.0088 | 0.4307 |
| Domínio Saúde — drop WarpSpeed | 11 | 0.0179 | 0.3658 |

Todas as sensibilidades Mantêm p < 0.05 → a rejeição omnibus é **robusta**.
Sem modelo misto (STAT-09: explicitamente excluído). Sem winsorização (STAT-04).

## 7. TOST / Equivalência — NÃO executado

Conforme R3-03 + R5-GOV-03: nenhuma margem Δ aprovada; Δ=0.10 explicitamente NÃO aprovada;
TOST **não** executado neste estudo.

## 8. Decisão Final — Go/No-Go (08-PRE-REGISTRATION-N12 §8)

| Critério (pré-registro N12) | Limiar | Observado | Status |
|---|---|---|---|
| Casos válidos | ≥ 10 de 12 | 12 | **PASS** |
| Matriz N×3 completa | = N_casos | 36/36 células | **PASS** |
| Nenhum FAIL-PILOT | — | nenhum | **PASS** |

**Go/No-Go metodológico (pré-registro §8): GO — 12/12 casos válidos ≥ 10 → análise estatística procede e é válida.**

**Decisão inferencial (pré-registro §9):** Friedman significativo (p=0.0075, W=0.41 — efeito médio).
Taxonomia C3 (B) **não demonstra melhoria estatisticamente significativa** vs cega pura (A) em S_struct
após Holm (p=0.0537; direção B>A favorecida, r_rb=0.667, IC da diferença de medianas (0.002, 0.095) exclui 0).
Comparação significativa após correção é apenas **B > C** (r_rb=−0.821, Cliff δ=0.701 — efeito grande).
Narrativa completa (C) apresenta menor S_struct estrutural mediano (0.5843), com potência N=12 ≈ 0.895 (adequada).

## 9. Conclusão

- Variação entre condições presente e estatisticamente significativa (Friedman p=0.0075),
  robusta a sensibilidades (todas p<0.05).
- **Evidência a favor da utilidade C3 (B>A) NÃO alcança significância pós-correção** nesta amostra
  (p=0.0537), embora a direção favoreça B e o IC da diferença de medianas exclua 0 — resultado limítrofe,
  a interpretar como tendência, não como confirmação.
- Condição C (não-cega) estruturalmente MENOR que B (p=0.0093, efeito grande) — achado robusto.
- Potência pré-registrada N=12 ≈ 0.895; não se conclui "ausência de efeito" para A vs B.

---
**Fim do relatório. Nenhum artefato congelado (GO-8B ou GO-8C Lock) alterado. TOST não executado.**
