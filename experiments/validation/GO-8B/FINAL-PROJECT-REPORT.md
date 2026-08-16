# Relatório Final do Piloto GO-8B

**Data:** 2026-08-13
**Status:** **GO — concluído com sucesso**
**Decisor:** Governança GO-8B
**Hash do manifesto (núcleo congelado):** `c55799d895a4f73888713a8538c6b9a6c5df1d7cde71c88141e16b9e9b216636`

---

## 1. Resumo Executivo

### 1.1 Objetivo do piloto

O piloto GO-8B avaliou a utilidade da **taxonomia sintética C3** na reconstrução cega de
casos históricos, comparando a similaridade estrutural `S_struct` do grafo reconstruído
(espaço sintético da condição) com o grafo canônico ECP, entre **3 condições de
reconstrução** sobre **7 BIPs válidos**.

### 1.2 Metodologia

- **Unidade experimental:** BIP/Caso (`N = 7`; nunca multiplicado).
- **Condições:** A = Cega pura (só Atomic Facts) · B = Cega + Taxonomia C3 · C = Não-cega (narrativa completa).
- **Seeds:** 3 seeds por (BIP × condição), agregação por **mediana** (R5 M-3).
- **Total de execuções:** 63 (7 × 3 × 3), todas `PASS`.
- **DV confirmatória:** `S_struct` (WL Kernel, anonimizado). `S_sem` = exploratória.
- **Teste global primário:** Friedman (df=2, α=0.05); pós-hoc Wilcoxon pareado bilateral +
  Holm-Bonferroni; Kendall W; r_rb; Cliff δ; bootstrap B=10.000 (percentil pareado);
  **TOST não executado** (nenhuma Δ aprovada — R3-03/R5-GOV-03).
- **Executor congelado:** `scripts/go8b/go8b_statistical_analysis.py` (seed_statistics=1879048193).

### 1.3 Resultados principais

| Teste | Estatística | Valor |
|---|---|---|
| **Friedman (omnibus)** | χ²_F, df | **9.5556**, df=2 |
| | p | **0.0084** |
| | Kendall's W (IC95% boot) | **0.6825** (0.5510–0.8776) |
| **Post-hoc A vs B** | p (Holm) | 1.0000 — **não significativo** |
| **Post-hoc A vs C** | p (Holm) | 0.0312 — **não significativo após Holm** |
| **Post-hoc B vs C** | p (Holm) | **0.0156 — SIGNIFICATIVO após Holm** |

Medianas por condição (`S_struct`): A = 0.5875 · B = 0.5905 · C = 0.5721.

### 1.4 Interpretação

- A condição **não-cega (C)** apresentou desempenho estrutural **inferior** à condição
  **cega + C3 (B)** (única comparação significativa após Holm, B > C).
- A taxonomia C3 (B) **não** demonstrou superioridade estatística sobre a cega pura (A)
  (p = 1.0000).
- Evidência **limitada pelo tamanho amostral pré-registrado** (N=7 → potência ≈ 0.63 sob o
  cenário S1_PRIMARY); não se conclui "ausência de efeito" para comparações não rejeitadas.
- A rejeição omnibus é **robusta**: todas as sensibilidades (sem outliers; exclusão de um
  caso por par dependente — Hyatt/I-35W, Ebola/WarpSpeed) mantiveram p < 0.05.

### 1.5 Decisão Go/No-Go

**GO.** Atende integralmente `07-FAILURE-CRITERIA.md` §8: 7/7 casos válidos, 7 domínios
distintos, matriz N×3 completa (21/21), nenhum `FAIL-PILOT`. A governança aprovou os
resultados da análise estatística e o encerramento do piloto.

---

## 2. Limitações

| Limitação | Detalhe |
|---|---|
| **N=7, potência ≈ 0.63** | Abaixo do limiar usual de 0.80; limitação pré-registrada (06 §5.3, 08 §9); N=12 necessário para potência ≥ 0.80. |
| **Substituição do NT-05** | Gate humano substituído por auditoria automatizada independente (NC-01), sem equivalência epistemológica. |
| **Namespace NULL** | `NULL` (C4) incompatível com o parser congelado (`graph_from_reconstruction.py:84-85` — `NAMESPACE_MIX`); uso operacional de `CAT` para A/C (decisão NAMESPACE-OPERATIONAL-DECISION). |
| **Duplicações parciais de s_struct** | Valores idênticos entre BIPs na mesma condição (invariância topológica da métrica estrutural anonimizada); aceita pela governança como limitação da métrica (NOTES-SSTRUCT-DUPLICATES). |

---

## 3. Conclusão e Recomendações

1. **O piloto cumpriu seus objetivos metodológicos** — pipeline operacional 63/63 PASS,
   análise estatística executada conforme pré-registro, decisão de encerramento GO.
2. **Recomenda-se um estudo confirmatório com N=12** para atingir a potência pré-especificada
   (≥ 0.80) sob o cenário S1_PRIMARY.
3. **Dívidas técnicas registradas para ciclo futuro:**
   - **Correção da seed C2** (`seed_registrada` marcada `REGISTERED-NON-REPRODUCING`; ver P1-C2-01).
   - **Revisão do namespace NULL** (C4): decidir se o parser congelado passa a processar NULL
     ou se o namespace operacional CAT permanece — requer nova decisão de governança + Lock.
   - **Reavaliação do requisito humano NT-05** (substituição por auditoria automatizada é
     válida para o piloto, sem equivalência epistemológica à revisão humana original).

---

## 4. Referências

- `pilot-output/pilot_results.csv` (63 execuções)
- `pilot-output/STATISTICAL-REPORT.md` (análise estatística)
- `pilot-output/EVIDENCE-AND-STOP-GO-8B.md` (auditoria de evidências)
- `decisions/NAMESPACE-OPERATIONAL-DECISION.md` · `decisions/NOTES-SSTRUCT-DUPLICATES.md`
- `decisions/ACTION-REGISTER.md` (A6–A10)
- Núcleo congelado: `GO-8B-LOCK-RECORD.yaml` / `GO-8B-LOCK-MANIFEST.yaml` (13 artefatos, 13/13 verificado)

---

**Fim do relatório final. Nenhum artefato congelado alterado.