# GO-8B — STATISTICAL REPORT (Análise Estatística do Piloto)

**Data:** 2026-08-13
**Executor:** `scripts/go8b/go8b_statistical_analysis.py` (script congelado, determinístico)
**Input:** `pilot-output/stats_input_sstruct.csv` (63 observações: 7 BIPs × 3 condições × 3 seeds)
**Protocolo:** `06-STATISTICAL-PROTOCOL.md` §7 + `08-PRE-REGISTRATION.md`
**DV confirmatória:** `S_struct` (mediana das 3 seeds por célula — R5 M-3). `S_sem` = exploratória.
**Configuração:** α=0.05 · Bootstrap B=10.000 (percentil, pareado) · seed_statistics=1879048193 · **TOST não executado** (nenhuma Δ aprovada).

---

## 1. Data Check e Agregação (passos 1–2)

- 63/63 linhas, todas `PASS`.
- 21 células (7 BIPs × 3 condições) completas com 3 seeds — **OK**.
- Range `S_struct`: min=0.5676, max=0.7500 — dentro de [0,1].
- Sem missings. N (válidos) = **7** (nunca multiplicado).

## 2. Médidas por Condição (descritivas — passo 3)

### S_struct (DV confirmatória)

| Condição | Mediana (células) | IQR | Min | Max |
|----------|-------------------|-----|-----|-----|
| **A** (cega pura) | **0.5875** | [0.5875, 0.6129] | 0.5875 | 0.6828 |
| **B** (cega + C3) | **0.5905** | [0.5837, 0.6157] | 0.5721 | 0.7500 |
| **C** (não-cega) | **0.5721** | [0.5676, 0.5843] | 0.5676 | 0.5875 |

Medianas por caso (célula = mediana das seeds):

| Caso | A | B | C |
|------|-------|-------|-------|
| Deepwater | 0.5875 | 0.5800 | 0.5721 |
| Hyatt | 0.5875 | 0.5905 | 0.5875 |
| WarpSpeed | 0.5875 | 0.5950 | 0.5676 |
| Genoma | 0.5875 | 0.7500 | 0.5866 |
| Suez | 0.6828 | 0.5721 | 0.5676 |
| I-35W | 0.5875 | 0.6364 | 0.5676 |
| Ebola | 0.6383 | 0.5875 | 0.5821 |

### S_sem (exploratória)

| Condição | Mediana (células) |
|----------|-------------------|
| A | 0.5527 |
| B | 0.5528 |
| C | 0.5513 |

## 3. Teste Omnibus — Friedman (passo 4, teste global PRIMÁRIO)

| Estatística | Valor |
|---|---|
| **χ²_F** | **9.5556** |
| **df** | **2** |
| **p** | **0.0084** |
| **Kendall's W** | **0.6825** (efeito grande, W≈0.5+) |
| **IC 95% bootstrap de W** | **(0.5510, 0.8776)** |

**Decisão (α=0.05):** p < 0.05 → **REJEITA H₀** — pelo menos uma condição difere.
→ Post-hoc confirmatório **AUTORIZADO** (passo 5).

## 4. Post-hoc — Wilcoxon pareado bilateral + Holm-Bonferroni (passo 5)

| Par | p (bruto) | Holm | r_rb | Cliff δ | IC95% dif. mediana | IC95% Cliff |
|-----|-----------|------|------|---------|--------------------|-------------|
| A vs B | 1.0000 | não rejeita | 0.000 | 0.000 | (−0.058, 0.049) | (−0.714, 0.694) |
| A vs C | 0.0312 | não rejeita | −1.000 | 0.898 | (−0.071, −0.001) | (0.633, 1.000) |
| **B vs C** | **0.0156** | **REJEITA** | **−1.000** | **0.714** | (−0.069, −0.004) | (0.449, 1.000) |

> Holm-Bonferroni (α=0.05, 3 comparações): ordenar p → B-C (0.0156 ≤ 0.05/3=0.0167): **rejeitada**;
> A-C (0.0312 > 0.05/2=0.025): **não rejeitada**; A-B: não rejeitada.

**Interpretação:** única comparação significativa pós-correção é **B > C**
(diferença de medianas negativa = C menor que B). A e B não diferem
(p=1.00; r_rb=0; Cliff δ≈0). A > C não é significativo após Holm.

## 5. Exploratório (passo 6 — não confirmatório)

- Interação Caso × Condição: presença de comportamento heterogêneo por domínio
  (ex.: Genoma B=0.7500 é o pico; Suez A=0.6828 > demais).
- S_sem (diagnóstico): variação mínima entre condições (0.5513–0.5528);
  exploratória, entra no relatório sem decisão inferencial.
- Spearman S_struct × aux: não executado (sem `aux_value` no piloto atual).

## 6. Sensibilidade (passo 7)

| Análise | N | Friedman p | Kendall W |
|---------|-----|-----------|-----------|
| Sem outliers (IQR×1.5) | 5 | 0.0363 | 0.6632 |
| Domínio Civil — drop Hyatt | 6 | 0.0111 | 0.7500 |
| Domínio Civil — drop I-35W | 6 | 0.0191 | 0.6594 |
| Domínio Saúde — drop Ebola | 6 | 0.0147 | 0.7029 |
| Domínio Saúde — drop WarpSpeed | 6 | 0.0191 | 0.6594 |

Todas as sensibilidades Mantêm p < 0.05 → a rejeição omnibus é **robusta**.
Sem modelo misto (STAT-09: explicitamente excluído). Sem winsorização (STAT-04).

## 7. TOST / Equivalência — NÃO executado

Conforme R3-03 + R5-GOV-03: nenhuma margem Δ aprovada; Δ=0.10 explicitamente NÃO aprovada;
TOST **não** executado no piloto.

## 8. Decisão Final — Go/No-Go (07-FAILURE-CRITERIA.md §8)

| Critério (07 §8) | Limiar | Observado | Status |
|---|---|---|---|
| Casos válidos | ≥ 5 de 7 | 7 | **PASS** |
| Domínios distintos | ≥ 4 | 7 | **PASS** |
| Matriz N×3 completa | = N_casos | 21/21 células | **PASS** |
| Nenhum FAIL-PILOT | — | nenhum | **PASS** |

**Go/No-Go metodológico (07 §8): GO — dados suficientes para análise.**

**Decisão inferencial (06 §10):** Friedman significativo (p=0.0084, W=0.68 — grande).
Taxonomia C3 (B) **não** demonstra melhoria vs cega pura (A) em S_struct (p=1.00);
comparação significativa após Holm é apenas **B > C**. Narrativa completa (C)
apresenta menor S_struct estrutural médio, mas o poder é limitado (N=7 → potência ≈ 0.63).

## 9. Conclusão

- Variação entre condições presente e estatisticamente significativa (Friedman p=0.0084),
  robusta a sensibilidades.
- **Evidência a favor da utilidade C3 (B>A) NÃO encontrada** nesta amostra (p=1.00).
- Condição C (não-cega) estruturalmente MENOR que B — resultado a monitorar em expansão.
- Potência pré-registrada (N=7 ≈ 0.63) é limitação; não se conclui "ausência de efeito"
  para comparações não rejeitadas.

---
**Fim do relatório. Nenhum artefato congelado (00–08) alterado. TOST não executado.