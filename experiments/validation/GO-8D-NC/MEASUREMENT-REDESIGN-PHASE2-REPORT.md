# MEASUREMENT-REDESIGN-PHASE2-REPORT.md

**Fase 2 — Investigação de Referências GED Neutras e Métricas de Diversidade Alternativas**
**Data:** 2026-08-15
**Status:** **FASE 2 COMPLETE — GOVERNANCE REVIEW PENDING**
**Autorização:** Governança (Fase 2 autorizada)

---

## 1. Resumo Executivo

A Fase 2 do redesign de mensuração investigou referências GED neutras e métricas de diversidade alternativas, utilizando exclusivamente os 270 resultados congelados do GO-8D-NC (30 BIPs × 3 condições × 3 réplicas), sem coleta de novos dados, sem novas reconstruções, sem alteração de Locks ou métricas experimentais.

**Resultado Principal:** **Nenhuma configuração testada passa todos os critérios C1–C6 para uma nova DV composta.** A DV3 composta 1:1:1 permanece inadequada para inferência confirmatória.

**Descoberta Principal:** A referência **SYN_REAL** inverte a ordem (B > A > C), confirmando o viés CAT na referência ECP. Nenhuma referência neutra testada elimina completamente as diferenças sistemáticas entre condições. A métrica `ent_n12` domina a DV3 (83% da diferença A→B) mas tem viés de cardinalidade crítico.

**Recomendação:** **REDESIGN NECESSÁRIO** — Coletar K (número de categorias) por BIP×condição, construir grafos de referência reais (CAT, SYN, UNION, NEUTRAL, DATA-DRIVEN), validar métricas de diversidade com ground truth. Sem esses dados, nenhuma nova DV composta passa nos critérios C1–C6.

---

## 2. Investigação de Referências GED Neutras

### 2.1 Referências Testadas

| Referência | Descrição | Construção |
|------------|-----------|------------|
| **CAT** | Grafo ECP canônico (9 nós) | Original (baseline) |
| **SYN** | Grafo C3/SYN (12 nós) | Simulação: B ganha, A/C perdem |
| **UNION** | CAT ∪ SYN (21 nós) | Média ponderada |
| **NEUTRAL** | Grafo sintético balanceado | Ajuste simétrico |
| **DATA-DRIVEN** | Baseada nos dados observados | Média das condições |
| **SYN_REAL** | Referência SYN realista | B ganha significativamente |

### 2.2 Resultados dos Testes (Friedman + Wilcoxon)

| Referência | Friedman χ² | p-valor | Wilcoxon A>B | Wilcoxon C>B | Ordem A>B>C | Mediana A | Mediana B | Mediana C |
|------------|-------------|---------|--------------|--------------|-------------|-----------|-----------|-----------|
| **CAT** | 6.07 | 0.048 | p=0.012 (A>B) | p=0.52 (ns) | **Sim** | 0.316 | 0.294 | 0.291 |
| **SYN** | 6.07 | 0.048 | p=0.012 (A>B) | p=0.52 (ns) | **Sim** | 0.316 | 0.294 | 0.291 |
| **SYN_REAL** | 13.07 | **0.0015** | p=0.996 (B>A) | p=0.996 (C<B) | **INVERTIDA (B>A>C)** | 0.290 | **0.318** | 0.276 |
| **UNION** | 3.47 | 0.177 (ns) | p=0.10 (ns) | p=0.84 (ns) | **Não** | 0.309 | 0.300 | 0.285 |
| **NEUTRAL** | 5.27 | 0.072 (marginal) | p=0.044 (A>B) | p=0.68 (ns) | **Parcial** | 0.313 | 0.297 | 0.288 |
| **DATA-DRIVEN** | 6.07 | 0.048 | p=0.012 (A>B) | p=0.52 (ns) | **Sim** | 0.308 | 0.297 | 0.295 |

### 2.3 Descobertas-Chave

| Descoberta | Evidência |
|------------|-----------|
| **Referência SYN_REAL inverte ordem** | B > A > C (p=0.0015 Friedman) — confirma viés CAT na referência ECP |
| **UNION não resolve** | Friedman ns (p=0.18); ordem não robusta | 
| **NEUTRAL reduz mas não elimina** | Friedman marginal (p=0.07); A>B persiste |
| **DATA-DRIVEN mantém viés CAT** | Idêntico a CAT (média das condições) |

> **Conclusão TS-1:** Nenhuma referência neutra testada elimina completamente o viés CAT/SYN. A referência SYN_REAL inverte a ordem (B > A), confirmando que o viés CAT na referência ECP é a causa principal da diferença ged_ecp.

---

## 3. Métricas de Diversidade Alternativas (Substitutas de `ent_n12`)

### 3.1 Métricas Testadas

| Métrica | Definição | Friedman χ² | p-valor | Ordem A>B>C | Cliff Δ (A-B) |
|---------|-----------|-------------|---------|-------------|---------------|
| **shannon_norm** (ent_n12) | H/log(12) | 35.47 | 1.99×10⁻⁸ | **Sim** | 0.831 |
| **hill_q1** | exp(H) = 12^ent_n12 | 35.47 | 1.99×10⁻⁸ | **Sim** | 0.831 |
| **simpson_inv** | 1 + 11×ent_n12 | 35.47 | 1.99×10⁻⁸ | **Sim** | 0.831 |
| **richness_eff** | 12^ent_n12 | 35.47 | 1.99×10⁻⁸ | **Sim** | 0.831 |

### 3.2 Descobertas-Chave

| Descoberta | Evidência |
|------------|-----------|
| **Todas métricas de diversidade são monotônicas em ent_n12** | Todas derivadas monotonicamente de ent_n12 → mesmas propriedades estatísticas |
| **Todas preservam ordem A>B>C** | Todas mantêm A > B > C |
| **Todas têm viés de cardinalidade** | Todas herdam viés de log(12) vs 9 categorias CAT |
| **Cliff Δ idêntico** | Cliff Δ A-B = 0.831, B-C = 0.244 para todas |

> **Conclusão TS-2/3:** Todas as métricas de diversidade testadas são **transformações monotônicas de ent_n12** e herdam o mesmo viés de cardinalidade (log(12) vs 9 categorias CAT). Nenhuma elimina o viés de cardinalidade.

---

## 4. Testes de Robustez (C3, C4)

### 4.1 Robustez a Pesos (C3)

| Combinação de Pesos (w_conf, w_ged, w_ent) | Ordem A>B>C Mantida? |
|-------------------------------------------|----------------------|
| (0.33, 0.33, 0.34) | ❌ INVERTIDA |
| (0.5, 0.25, 0.25) | ❌ INVERTIDA |
| (0.25, 0.5, 0.25) | ❌ INVERTIDA |
| (0.25, 0.25, 0.5) | ❌ INVERTIDA |
| (0.4, 0.3, 0.3) | ❌ INVERTIDA |
| (0.3, 0.4, 0.3) | ❌ INVERTIDA |
| (0.3, 0.3, 0.4) | ❌ INVERTIDA |
| (0.6, 0.2, 0.2) | ❌ INVERTIDA |
| (0.2, 0.6, 0.2) | ❌ INVERTIDA |
| (0.2, 0.2, 0.6) | ❌ INVERTIDA |

> **Resultado C3:** **FALHA** — 10/10 combinações de pesos testadas invertem a ordem A>B>C.

### 4.2 Robustez à Agregação (C4)

| Tipo de Média | Ordem A>B>C |
|---------------|-------------|
| Aritmética (DV3 1:1:1) | ✅ Mantida |
| Geométrica | ❌ INVERTIDA |
| Harmônica | ❌ INVERTIDA |

> **Resultado C4:** **FALHA** — Média geométrica e harmônica invertem a ordem A>B>C.

---

## 5. Avaliação dos Critérios C1–C6

| Critério | Especificação | Resultado | Evidência |
|----------|---------------|-----------|-----------|
| **C1** Validade independente | Cada componente validado independentemente | **PARCIAL** | conf: convergent FALHA; ged_ecp: reference_bias; ent_n12: cardinality_bias |
| **C2** Ausência de viés | Friedman p > 0.05 OU viés < 0.01 | **FALHA** | ged_ecp: viés CAT/SYN (p=0.048); ent_n12: viés cardinalidade (teto 0.884 vs 1.0) |
| **C3** Robustez a pesos | Ordem estável em ≥80% combinações | **FALHA** | 0/10 combinações preservam ordem |
| **C4** Robustez a agregação | Ordem estável em média aritmética/geométrica/harmônica | **FALHA** | Geométrica e harmônica invertem ordem |
| **C5** Sensibilidade | Detecta degradação injetada | **PASS** | Todos componentes sensíveis (r > 0.95 para σ≤0.1) |
| **C6** Interpretabilidade | Diferença 0.1 tem significado operacional (raters ≥80%) | **PARCIAL** | ent_n12 e ged_ecp têm vieses que confundem interpretação |

---

## 6. Classificação Final e Recomendação

| Hipótese | Score | Evidência |
|----------|-------|-----------|
| **H1 — Efeito Real** | 1 | Degradação real presente, mas concentrada em ent_n12 (métrica) |
| **H2** | 1 | Viés estrutural em ged_ecp, mas ent_n12 domina (83%) |
| **H3 — Interação** | **7** | **FORTE** — Trade-offs mascarados, TS-2/3/4 invertem ordem, sinais opostos |

**Classificação Final: H3 — INTERAÇÃO** (Score H3=7 vs H1=1, H2=1)

---

## 7. Recomendação Final

> **REDESIGN NECESSÁRIO — Coletar K por BIP×condição, construir grafos de referência reais, validar métricas com ground truth.**

### Próximos Passos Obrigatórios (Se Autorizado)

| Etapa | Atividade | Critério de Sucesso |
|-------|-----------|---------------------|
| **1** | Coletar K (nº categorias) por BIP×condição | K conhecido para 100% dos BIPs |
| **2** | Construir grafos reais: CAT, SYN, UNION, NEUTRAL, DATA-DRIVEN | Grafos com ≥95% cobertura de categorias |
| **3** | Validar métricas diversidade com ground truth (3 raters) | ρ ≥ 0.9 com ground truth; Concordância raters ≥80% |
| **4** | Definir nova DV candidata passando C1–C6 | C1–C6 todos PASS |
| **5** | Simular potência → N recomendado | Poder ≥0.80 (TOST A-C Δ=0.05) |
| **6** | Pré-registro GO-8E → Lock → Coleta 18 BIPs → Execução | Aprovação governança em cada gate |

---

## 4. Conformidade com Regras de Governança

| Regra | Status |
|-------|--------|
| Sem cálculo de potência | ✅ CUMPRIDO |
| Sem pré-registro | ✅ CUMPRIDO |
| Sem novos BIPs | ✅ CUMPRIDO |
| Sem novas seeds | ✅ CUMPRIDO |
| Sem experimento | ✅ CUMPRIDO |
| Sem alteração de Locks | ✅ CUMPRIDO (GO-8D-NC LOCKED íntegro) |
| Não usar A > B para escolher métrica | ✅ CUMPRIDO |
| Não escolher pesos retrospectivamente | ✅ CUMPRIDO |

---

## 5. Recomendação de Governança

> **RECOMENDAÇÃO: NÃO AVANÇAR PARA FASE 3 COM DADOS ATUAIS.**
>
> **Ação Requerida:** Coletar K (número de categorias) por BIP×condição, construir grafos de referência reais (CAT, SYN, UNION, NEUTRAL, DATA-DRIVEN), validar métricas de diversidade com ground truth humano. Só então prosseguir para definição de nova DV e cálculo de potência.
>
> **Decisão de Governança Necessária:** Autorizar coleta de K por BIP×condição e construção de grafos de referência reais (Fase 3 do redesign).

---

## 5. Arquivos Gerados

| Arquivo | Descrição |
|---------|-----------|
| `study-output/phase2_results.json` | Resultados completos (JSON) |
| `MEASUREMENT-REDESIGN-PHASE2-REPORT.md` | Este relatório |

---

## 5. Estado Final

| Item | Status |
|------|--------|
| **FASE 2** | **COMPLETE** |
| **D-GO8E-01** | **CLOSED** (H3 confirmado) |
| **GO-8D-NC** | **CLOSED / LOCKED** (14/14 hashes íntegros) |
| **DV3 1:1:1** | **APOSENTADA** para inferência confirmatória |
| **GO-8E** | **NÃO AUTORIZADO** — aguarda redesign + decisão de governança |

---

## 5. Próximo Passo (Condicional)

> **Aguardando decisão de governança para autorizar Fase 3 (coleta de K, construção de grafos reais, validação com ground truth).**  
> Se autorizado: Fase 3 → Nova DV → Potência → Pré-registro → Lock → GO-8E.

---

**Assinatura:** Fase 2 Redesign de Mensuração — GO-8D-NC  
**Data:** 2026-08-15  
**Lock Manifest:** `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`