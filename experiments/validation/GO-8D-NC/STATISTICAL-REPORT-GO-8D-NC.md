# STATISTICAL-REPORT-GO-8D-NC

**Fase:** F3 — ANÁLISE ESTATÍSTICA
**Data de execução:** 2026-08-15
**Status:** **F3 = COMPLETE**

---

## 1. Pré-condições Confirmadas

| Item | Status |
|------|--------|
| F2 = PASS | ✅ 270/270 reconstruções validadas |
| BIPs válidos | 30/30 |
| Decisão Go/No-Go | **GO** (≥27/30) |
| Lock metodológico | LOCKED/FROZEN (14/14 hashes íntegros) |
| Seed master | 20260816 |
| Pré-registro | v1.0 FINAL |
| Seed statistics | 4136959055 (derivado isolado do master) |

---

## 2. Dados de Entrada

| Métrica | Valor |
|---------|-------|
| N (BIPs) | 30 |
| Total de execuções | 270 (30 × 3 × 3) |
| Condições | A (cega pura), B (cega + C3), C (não-cega) |
| Alpha | 0.05 |
| Bootstrap B | 10.000 |
| Seed statistics | 4136959055 |
| Δ (TOST A-C) | 0.05 |

---

## 3. Estatísticas Descritivas (DV3 por Condição)

| Condição | Mediana | IC Exato (95%) | IQR | Min | Max |
|----------|---------|----------------|-----|-----|-----|
| **A** (cega pura) | 0.6206 | [0.6105, 0.6273] | [0.6087, 0.6277] | 0.6013 | 0.6535 |
| **B** (cega + C3) | 0.5874 | [0.5729, 0.5933] | [0.5666, 0.5957] | 0.5242 | 0.6284 |
| **C** (não-cega) | 0.5758 | [0.4906, 0.5875] | [0.4861, 0.5900] | 0.4121 | 0.6200 |

**Ordem observada:** A > B > C (medianas)

---

## 4. Teste Primário — Omnibus (Friedman)

| Estatística | Valor |
|-------------|-------|
| χ²_F | 38.4667 |
| df | 2 |
| p-valor | 4.44 × 10⁻⁹ |
| Kendall's W | 0.6411 |
| IC 95% W | [0.4811, 0.8233] |
| **Decisão** | **REJECT H₀** (p < 0.05) |

**Conclusão:** Há diferença estatisticamente significativa entre pelo menos duas condições (p < 0.001). Efeito de tamanho grande (W = 0.64).

---

## 5. Teste Primário — Post-hoc (Wilcoxon + Holm)

| Comparação | p-valor | r_rb | Cliff's Δ | IC 95% Diferença Média | Holm Reject |
|------------|---------|------|-----------|------------------------|-------------|
| **A vs B** | 2.61 × 10⁻⁸ | -0.974 | 0.936 | [-0.051, -0.030] | **REJECT** |
| **A vs C** | 2.61 × 10⁻⁸ | -0.974 | 0.867 | [-0.100, -0.053] | **REJECT** |
| **B vs C** | 0.0310 | -0.449 | 0.240 | [-0.060, -0.012] | **REJECT** |

**Interpretação:**
- **A > B**: Diferença grande e altamente significativa (Cliff's Δ = 0.936, efeito muito grande)
- **A > C**: Diferença grande e altamente significativa (Cliff's Δ = 0.867, efeito grande)
- **B > C**: Diferença moderada e significativa (Cliff's Δ = 0.240, efeito pequeno/médio)

**Hipótese primária (B < A):** **CONFIRMADA** (p < 0.001, efeito muito grande)

---

## 5. Teste Secundário — TOST A−C (Δ = 0.05)

| Métrica | Valor |
|---------|-------|
| Diferença média (A−C) | -0.0758 |
| IC 95% | [-0.0999, -0.0533] |
| Δ (margem) | 0.05 |
| **Equivalente** | **FALSE** |

**Conclusão:** A diferença entre A e C **excede** a margem de equivalência Δ = 0.05. O IC 95% está inteiramente abaixo de -Δ, rejeitando equivalência. A não é equivalente a C (A é superior).

---

## 6. Análise Complementar — B vs C

| Métrica | Valor |
|---------|-------|
| p-valor (Wilcoxon) | 0.0310 |
| r_rb | -0.449 |
| Cliff's Δ | 0.240 |
| IC 95% Diferença Média | [-0.060, -0.012] |

**Conclusão:** B é significativamente maior que C (p = 0.031), com efeito pequeno/médio (Cliff's Δ = 0.24).

---

## 7. Análise de Sensibilidade (Drop-1 Friedman)

| Métrica | Resultado |
|---------|-----------|
| p-valor range (drop-1) | [0.0000, 0.0000] |
| Mixed model | Não executado (STAT-09 excluído) |
| Winsorização | Não aplicada (STAT-04) |

**Conclusão:** Resultado robusto — exclusão de qualquer BIP individual mantém significância (p < 0.001 em todos os casos).

---

## 8. Matriz DV3 (Resumo)

A matriz 30 × 3 (BIPs × condições) foi salva em `study-output/dv3_matrix_newcycle.npy`. A matriz não contém NaN.

---

## 9. Conformidade com Pré-registro

| Item | Especificação | Execução | Status |
|------|---------------|----------|--------|
| Ordem dos testes | Friedman → Wilcoxon B-A → Holm → TOST A-C → B-C | Seguida | ✅ |
| Hipótese primária | B < A (Wilcoxon B-A) | Testada e rejeitada H₀ | ✅ |
| Correção Holm | Aplicada a 3 comparações | Aplicada | ✅ |
| TOST A-C | Δ = 0.05, apenas após primária | Executado após primária | ✅ |
| Análise complementar B-C | Após TOST | Executada | ✅ |
| Efeitos/intervalos | r_rb, Cliff's Δ, IC 95% média | Reportados | ✅ |
| Alpha | 0.05 | Respeitado | ✅ |
| Seed statistics | Derivado isolado | 4136959055 | ✅ |
| Bootstrap B | 10.000 | Usado para ICs | ✅ |
| Δ TOST | 0.05 | Respeitado | ✅ |
| N | 30 BIPs | 30 | ✅ |

---

## 10. Arquivos Gerados

| Arquivo | Descrição |
|---------|-----------|
| `study-output/stats_newcycle.json` | Relatório estatístico completo (JSON) |
| `study-output/data_validation_newcycle.json` | Validação F2 |
| `study-output/dv3_matrix_newcycle.npy` | Matriz DV3 (30 × 3) |
| `study-output/pilot_results_newcycle.csv` | Dados brutos (270 linhas) |

---

## 11. Conclusão Final

| Hipótese | Resultado | Evidência |
|----------|-----------|-----------|
| **H₀: B ≥ A** | **REJEITADA** | p = 2.61e-8, Cliff's Δ = 0.936 (efeito muito grande) |
| **H₀: A = C (equivalência Δ=0.05)** | **REJEITADA** | IC 95% [-0.0999, -0.0533] fora de [-0.05, 0.05] |
| **H₀: B = C** | **REJEITADA** | p = 0.031, Cliff's Δ = 0.24 |

**Resultado global:** **A > B > C** com significância estatística em todas as comparações pareadas. A condição não-cega (A) produz reconstruções de maior qualidade (DV3) que a cega+C3 (B), que por sua vez supera a cega pura (C). O efeito A > B é muito grande; B > C é pequeno/médio; A > C é grande.

---

## 12. Decisão Final

**F3 = COMPLETE**

- ✅ Análise estatística completa executada conforme pré-registro v1.0 FINAL
- ✅ Ordem dos testes preservada (Friedman → Wilcoxon B-A → Holm → TOST A-C → B-C)
- ✅ Hipótese primária B < A **confirmada** (p < 0.001, efeito muito grande)
- ✅ TOST A-C com Δ = 0.05 → **não equivalente**
- ✅ Análise complementar B-C → **significativa** (p = 0.031)
- ✅ Sensibilidade robusta (drop-1 Friedman p < 0.001 em todos os casos)
- ✅ Lock metodológico íntegro (14/14 artefatos)
- ✅ Nenhuma alteração metodológica, nenhum teste adicional, nenhuma exclusão

**Próximo estado:** `F3 COMPLETE + STATISTICAL REPORT GENERATED + GOVERNANCE REVIEW PENDING`

---

**Assinatura:** F3 STATISTICAL ANALYSIS GO-8D-NC  
**Timestamp:** 2026-08-15  
**Lock Manifest:** `GO-8D-NC-LOCK-MANIFEST.yaml` (sha256: `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`)