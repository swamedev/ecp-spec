# GO-8B Entregável 6 — Protocolo Estatístico Completo

**Status:** REVISED — PENDING GOVERNANCE AUDIT
**Revisão:** R1 (aplicação do Decision Record 00-GO-8B-R1) + R3 (DECISION R3-03, R3-04) + R5 (M-2, M-3, GO-8B-R5) + R6 (R5-GOV-01..04)
**Data original:** 2026-08-10
**Objetivo:** Definir o plano de análise estatística inferencial para o piloto metodológico GO-8B, incluindo teste omnibus (Friedman), pós-hoc (Wilcoxon + Holm), tamanho de efeito, intervalos de confiança, e pontos de validação. **Friedman é o teste global primário (R5 M-2); RM-ANOVA, quando mencionada, é exclusivamente análise suplementar/robustez.**
**Design:** Medidas repetidas.

---

## 1. Variáveis e Design Experimental

### 1.1 Variável Dependente Principal
- **S_struct** = Score estrutural do WL Kernel (Entregável 5, métrica confirmatória) ∈ [0, 1]
- S_sem é **exploratória** — não entra na análise inferencial confirmatória.
- Contínua, limitada, não-necessariamente normal

### 1.2 Fatores (Within-Subject)
| Fator | Níveis | Descrição |
|---|---|---|
| **Caso/BIP** | 7 | Deepwater, Hyatt, Warp Speed, Genoma, Suez, I-35W, Ebola (Entregável 1) |
| **Condição de Reconstrução** | 3 | (A) Cega pura (só Atomic Facts) • (B) Cega + Taxonomia C3 • (C) Não-cega (narrativa completa) |

**Avaliador e seeds são repetições intra-unidade, NÃO blocos de análise.**

### 1.3 Unidade Experimental (Fixada pela R1)

> **Unidade experimental = BIP/Caso.**

> **N = número de BIPs válidos** (após critérios do Entregável 7).

**Nunca:** `N = BIPs × avaliadores`.  
**Nunca:** `N = BIPs × seeds`.

- Seeds são **repetições intra-unidade** (ex.: múltiplas seeds de avaliação, múltiplos avaliadores, múltiplas execuções).
- Se houver múltiplas seeds: `Caso × Condição → mediana das seeds` — e **somente então** essa observação entra na análise inferencial.

### 1.3.1 Seeds Pré-especificadas (FIXADO pelo R5 M-3)

> **Número de seeds por célula = 3 seeds por (BIP × condição)** — desenho já estabelecido em GO-8A; **não** será aumentado nem reduzido com base em resultados.

Definições formais:

```
cell_value(caso_i, condição_j) = median(seed_1, seed_2, seed_3)
seed = observação repetida dentro de BIP × condição
```

- **Seeds NÃO constituem unidades experimentais independentes.**
- A agregação por **mediana** é obrigatória; `N` permanece igual ao número de BIPs válidos (3 seeds por célula **não** multiplicam `N`).
- O número de seeds (3) é **dado de configuração pré-especificado** e entra como tal no pré-registro (`08-PRE-REGISTRATION.md` — a criar em etapa posterior).
- Seeds de análise estatística e seed da simulação de potência são **streams isolados** (§9.1 e §5.3).

### 1.3.2 Design Estatístico Final (Consistência R5 M-2)

| Elemento | Especificação (FIXADA) |
|---|---|
| **Objetivo** | Comparar S_struct entre as 3 condições de reconstrução sobre os BIPs válidos |
| **Hipótese** | H₀: distribuições idênticas nas 3 condições; H₁: pelo menos uma difere (§2.1) |
| **Teste global (primário)** | **Friedman** (teste global PRIMÁRIO; §3) |
| **RM-ANOVA** | **Suplementar/robustez somente** — nunca substitui o teste global pré-especificado (§3.5) |
| **Pós-hoc** | Wilcoxon signed-rank pareado, bilateral, com Holm-Bonferroni (§4) |
| **α** | 0.05 (global e família pós-hoc) |
| **Unidade estatística** | BIP/Caso; observação inferencial = mediana das 3 seeds por (caso, condição) |
| **Célula** | mediana das 3 seeds (§1.3.1) |

Não há decisão estatística unilateral possível após a observação dos resultados (DECISION R3-04).

### 1.4 Estrutura dos Dados (Após Agregação)

```
S_struct[caso_i, condição_j]   →   N_casos × 3 matriz (Friedman)
```

- **Unidade de observação:** Caso/BIP válido.
- **Observação inferencial:** mediana das 3 seeds por `(caso, condição)`.

---

## 2. Hipóteses (Pré-Registradas)

### 2.1 Hipótese Primária (Omnibus)
> **H₀:** A distribuição de S_struct é idêntica nas 3 condições de reconstrução (A, B, C), sobre o conjunto de BIPs válidos.  
> **H₁:** Pelo menos uma condição difere.

### 2.2 Hipóteses Secundárias (Pós-Hoc, Condicionadas à Rejeição de H₀)
| Comparação | Hipótese | Justificativa |
|---|---|---|
| **B vs A** | S_struct(B) > S_struct(A) | Taxonomia C3 adiciona estrutura → melhor alinhamento |
| **C vs A** | S_struct(C) > S_struct(A) | Narrativa completa remove ambiguidade → upper bound |
| **C vs B** | S_struct(C) ≥ S_struct(B) | Narrativa completa ≥ taxonomia sintética |

### 2.3 Hipóteses Exploratórias (Não Confirmatórias)
- Interação Caso × Condição: efeito da taxonomia varia por domínio?
- Efeito do avaliador (humano vs LLM): reprodutibilidade (P-0010)?
- S_sem como diagnóstico (mediana por caso×condição; sem teste inferencial confirmatório)

---

## 3. Teste Omnibus: Friedman (TESTE GLOBAL PRIMÁRIO)

> **Friedman é o teste global PRIMÁRIO e pré-especificado para a comparação das condições (R5 M-2).**
> Nenhuma alternativa paramétrica (ex.: RM-ANOVA) substitui este teste global pré-especificado. A RM-ANOVA, se executada, é **exclusivamente** análise suplementar/robustez (§3.5) — não altera o teste global, a decisão de α, nem a interpretação.

### 3.1 Entrada
Matriz **N_casos × N_condições**:

```text
             A       B       C
BIP-01       x11     x12     x13
BIP-02       x21     x22     x23
...
BIP-N        xN1     xN2     xN3
```

- As linhas são os **BIPs/casos válidos** (N = nº de BIPs válidos).
- As colunas são as **3 condições** (A = cega pura, B = cega + Taxonomia C3, C = não-cega).
- Avaliadores **não** são linhas/blocos.
- **N não é multiplicado artificialmente** (nem por avaliadores, nem por seeds).

### 3.2 Estatística de Teste
```
χ²_F = (12 / (N * k * (k+1))) * Σ(R_j²) - 3 * N * (k+1)
Onde:
  N = número de BIPs válidos (unidade experimental fixa)
  k = número de condições = 3
  R_j = soma dos ranks na condição j
```
Distribuição assintótica: χ² com df = k-1 = 2.  
Para N pequeno: distribuição exata ou aproximação de Iman-Davenport (F_F).

### 3.3 Critério de Decisão
- α = 0.05
- Rejeitar H₀ se p < 0.05

### 3.4 Tamanho de Efeito
- **Kendall's W**: W = χ²_F / (N · (k − 1)) ∈ [0, 1]
- Interpretação: W ≈ 0.1 (pequeno), 0.3 (médio), 0.5 (grande)

### 3.5 RM-ANOVA — Análise Suplementar/Robustez SOMENTE (R5 M-2)

A RM-ANOVA **não** é alternativa implícita ao Friedman e **não** substitui o teste global pré-especificado. Se, e somente se, for executada, aplicam-se:

- É **suplementar/robustez** (sensitividade), rotulada como tal no relatório;
- Não decide a hipótese primária; a decisão de α (0.05) e a interpretação permanecem vinculadas ao Friedman;
- Condicionalmente a ela, os testes de Shapiro-Wilk (normalidade) e Mauchly (esfericidade) são **diagnósticos da robustez**, nunca gate do teste global;
- Qualquer divergência entre Friedman e RM-ANOVA é reportada como discrepância de robustez, **sem** trocar o teste global.

---

## 4. Testes Pós-Hoc: Wilcoxon Signed-Rank + Holm-Bonferroni

### 4.1 Procedimento
1. Para cada par de condições (A-B, A-C, B-C): teste **Wilcoxon signed-rank pareado** (as unidades são os **mesmos BIPs**; mesmas N observações por par).
2. Obter 3 p-values: p_AB, p_AC, p_BC.
3. Testes **bilaterais**.
4. Aplicar correção **Holm-Bonferroni** (step-down):
   - Ordenar p-values: p_(1) ≤ p_(2) ≤ p_(3)
   - Comparar p_(1) com α/3, p_(2) com α/2, p_(3) com α/1
   - Rejeitar H₀ para todas as comparações até a primeira não-rejeição

### 4.2 Tamanho de Efeito
- **Rank-biserial correlation (r_rb)**: r_rb = 1 − (2 · U) / (n₁ · n₂); |r| ≈ 0.1 (pequeno), 0.3 (médio), 0.5 (grande)
- **Cliff's δ** (alternativa robusta): δ = P(X > Y) − P(X < Y)

### 4.3 Intervalos de Confiança (IC 95%)
| Parâmetro | Método | Implementação |
|---|---|---|
| **Mediana por condição** | Bootstrap percentil (B=10.000) | `np.percentile(bootstrap_medians, [2.5, 97.5])` |
| **Diferença de medianas (pares)** | Bootstrap pareado (B=10.000) | Diferença das medianas em cada reamostragem |
| **Kendall's W** | Bootstrap (B=10.000) | Percentil da distribuição bootstrap de W |
| **r_rb / Cliff's δ** | Bootstrap pareado (B=10.000) | Percentil da distribuição bootstrap |

**Nota:** Bootstrap **pareado** — reamostrar unidades (BIPs) com reposição.

### 4.3.1 Cobertura do Bootstrap — Simulação Metodológica (STAT-08, R5-GOV-04)

> **Análise metodológica independente, autorizada por R5-GOV-04.** Nenhum dado experimental; nenhum parâmetro do estudo alterado.

**Configuração (pré-especificada):** DGM idêntico ao da simulação de potência (§5.1: σ_b=0.12, σ_e=0.08, σ_s=0.06; μ=(0.50, 0.60, 0.66); 3 seeds/célula; agregação por mediana); IC 95% **percentil**, B_boot=10.000; MC reps=1.500; **seed `20260812`** (stream isolado). Alvos: mediana cond. A=0.50, cond. B=0.60, diferença B−A=0.10.

**Resultado — cobertura empírica do IC 95% (nominal = 0.95):**

| N | Mediana cond. A | Mediana cond. B | Diferença pareada (B−A) |
|---|---|---|---|
| 5 | 0.941 | 0.935 | 0.920 |
| 6 | 0.941 | 0.939 | 0.930 |
| **7** | **0.884** | **0.870** | **0.931** |
| 8 | 0.934 | 0.935 | 0.954 |
| 10 | 0.937 | 0.944 | 0.970 |
| 12 | 0.940 | 0.934 | 0.973 |
| 14 | 0.930 | 0.943 | 0.977 |
| 20 | 0.941 | 0.935 | 0.982 |

**Interpretação (registrada):**
- **B=10.000 é suficiente** — o erro Monte Carlo das reamostragens é desprezível; a cobertura observada **não** se deve a B insuficiente.
- A **mediana por condição** apresenta **cobertura sub-nominal** no piloto **N=7** (≈ 0.87–0.88), decorrente do **método percentil + N pequeno** (discretude da mediana como estatística de ordem), não do nº de reamostragens.
- A **diferença pareada de medianas** mantém cobertura ≈ 0.93 em N=7 (próxima do nominal), e ≥ 0.95 para N ≥ 10.
- **Mitigação (documental, sem alterar método pré-especificado):** reportar, junto ao IC percentil da mediana, o **IC exato da mediana (estatística de ordem)**; interpretar o IC percentil da mediana com cautela em N=7; as decisões inferenciais (Friedman/Wilcoxon/Holm) **não** dependem desses ICs descritivos.

---

## 5. Análise de Potência Monte Carlo (Pré-Experimental — EXECUTADA no R5 M-3)

> **A simulação de potência NÃO é o experimento científico.** É análise metodológica prévia para justificar o tamanho amostral. Nenhum dado real foi usado; nenhuma observação foi coletada; nenhum parâmetro foi ajustado após observar os resultados.

### 5.1 Configuração da Simulação (Pré-especificada)

| Parâmetro | Valor | Justificativa |
|---|---|---|
| **Teste** | Friedman (`scipy.stats.friedmanchisquare`), df = k−1 = 2 | Teste global primário (§3) |
| **α** | 0.05 | Pré-registrado (R3-04) |
| **k (condições)** | 3 (A = cega pura, B = cega + C3, C = não-cega) | Número real de condições |
| **Seeds por célula** | 3 seeds por (BIP × condição) | Desenho GO-8A (§1.3.1) |
| **Agregação** | `cell_value = median(seed_1, seed_2, seed_3)` | §1.3.1 |
| **N avaliado (BIPs)** | 5, 6, 7, 8, 9, 10, 12, 14, 16, 20, 28 | Curva de potência em torno do piloto (7) e do mínimo de análise (5) |
| **Replicações (B)** | 5.000 por N | Precisão MC adequada (SE ≤ 0.007) |
| **Seed da simulação** | `20260811` (uint64) | Stream isolado; não reutilizado (isolação de streams, Entregável 2 §9) |

**Modelo gerador de dados (sem dados reais):**

```
X_ij = μ_j + b_i + e_ij        # score latente do BIP i na condição j
  b_i  ~ N(0, σ_b²)            # efeito aleatório do BIP (entre-unidades)
  e_ij ~ N(0, σ_e²)            # ruído intra-unidade entre condições
y_ijk = X_ij + s_ijk           # k = 1..3 seeds dentro da célula (i, j)
  s_ijk ~ N(0, σ_s²)           # ruído de seed (intra-célula)
cell_ij = clip(median(y_ij1, y_ij2, y_ij3), 0, 1)   # agregação por mediana, [0,1]
```

**Parâmetros de variabilidade/correlação (pré-especificados):**

| Parâmetro | Valor | Significado |
|---|---|---|
| **σ_b** | 0.12 | Variabilidade entre BIPs |
| **σ_e** | 0.08 | Ruído intra-unidade entre condições |
| **σ_s** | 0.06 | Ruído de seed (intra-célula) |
| **ICC (condições dentro de BIP)** | σ_b²/(σ_b²+σ_e²) = **0.692** | Correlação intra-unidade esperada |

**Cenários de efeito (pré-especificados):**

| Cenário | μ (A, B, C) | Finalidade |
|---|---|---|
| **S0_NULL** | (0.55, 0.55, 0.55) | Calibração de erro tipo I (esperado ≈ 0.05) |
| **S1_PRIMARY** | (0.50, 0.60, 0.66) | Efeito moderado/grande: B > A e C ≥ B (hipótese §2.2); W médio ≈ 0.49 |

### 5.2 Resultados (N = BIPs válidos)

**S0_NULL — erro tipo I (rejeição sob H₀ verdadeira, α = 0.05):**

| N | Rejeição | MC SE |
|---|---|---|
| 5 | 0.039 | 0.003 |
| 7 | 0.050 | 0.003 |
| 10 | 0.049 | 0.003 |
| 14 | 0.055 | 0.003 |
| 20 | 0.051 | 0.003 |

Calibração aceitável: taxa de rejeição ≈ α dentro do erro Monte Carlo.

**S1_PRIMARY — potência (rejeição sob efeito pré-especificado):**

| N | Potência (p̂) | MC SE | IC 95% (Wilson) | W médio |
|---|---|---|---|---|
| **5** | 0.413 | 0.007 | (0.399, 0.426) | 0.527 |
| 6 | 0.553 | 0.007 | (0.539, 0.566) | 0.508 |
| **7** | **0.630** | 0.007 | (0.617, 0.644) | 0.487 |
| 8 | 0.696 | 0.006 | (0.683, 0.708) | 0.480 |
| 9 | 0.789 | 0.006 | (0.778, 0.800) | 0.477 |
| 10 | 0.798 | 0.006 | (0.787, 0.809) | 0.463 |
| 12 | 0.895 | 0.004 | (0.886, 0.903) | 0.454 |
| 14 | 0.934 | 0.004 | (0.927, 0.940) | 0.444 |
| 16 | 0.969 | 0.002 | (0.964, 0.974) | 0.445 |
| 20 | 0.987 | 0.002 | (0.983, 0.989) | 0.436 |
| 28 | 0.999 | 0.000 | (0.998, 1.000) | 0.427 |

### 5.3 Interpretação e Decisão Necessária

- **N = 7 (piloto atual): potência ≈ 0.63** (IC 95% 0.617–0.644) sob o cenário S1_PRIMARY — **abaixo do limiar usual de 0.80**.
- **N = 5 (mínimo metodológico de análise, Entregável 7 §8): potência ≈ 0.41**.
- **N = 12** é o menor N da grade com potência ≥ 0.80 (0.895; IC 95% 0.886–0.903) sob S1_PRIMARY.
- **Incerteza:** erro Monte Carlo ≤ 0.007 para N ≤ 10 e ≤ 0.004 para N ≥ 12; ICs Wilson reportados na tabela.
- O cenário S1_PRIMARY implica **W médio ≈ 0.49 (efeito grande)**; portanto, **mesmo um efeito grande não atinge 0.80 de potência no piloto (N=7)**. A alegação anterior de potência para N=7 **não é sustentada** pela simulação sob este cenário.
- **Não foi corrigido silenciosamente o número de casos.** A decisão sobre qualquer ajuste na banda de casos é **DECISION REQUIRED** (ver §5.4).
- **DECIDIDO (R5-GOV-01):** a governança **manteve N = 7** como piloto oficial. A potência ≈ 0.63 é reportada como **limitação pré-registrada**, com mitigação vigente abaixo.
- **Mitigação vigente (inalterada):** reportar ICs amplos; interpretar não-significância com cautela; **não** concluir "ausência de efeito" a partir de não-significância (ver §8).

### 5.4 Banda de Casos — Separação de Papéis (DECIDIDO R5-GOV-02)

Os números de casos têm **papéis distintos** e **não** devem ser alterados automaticamente para satisfazer potência:

| Papel | N (BIPs) | Fonte | Natureza |
|---|---|---|---|
| **Mínimo metodológico** | 4 elegíveis (FP-01) / **5 válidos para análise** (§8) | Entregável 7 | Go/No-Go metodológico; limiar marcado `PRE-SPECIFICATION DEBT` |
| **Recomendado para piloto** | **7** | Entregável 1 | Desenho GO-8A; piloto metodológico |
| **Necessário para potência inferencial** | **12** (potência ≥ 0.80) ou **14** (0.93) sob S1_PRIMARY | §5.2 | Potência sob o cenário de efeito pré-especificado |

> **DECIDIDO (R5-GOV-02):** a governança **mantém a banda separada** — mínimo 5 válidos / piloto 7 / potência 12. Nenhum dos três números será alterado sem nova decisão explícita.
- Qualquer alteração nesses números (mínimo, recomendado ou necessário) deve ser proposta como **DECISION REQUIRED** — nunca aplicada silenciosamente.
- O piloto prossegue com **N=7** (R5-GOV-01), reportando a potência insuficiente (≈0.63) como limitação pré-registrada (§5.3, §8, §10).

---

## 6. Pontos Estatísticos que Ainda Precisam de Decisão/Validação

| # | Ponto | Status | Ação Necessária |
|---|---|---|---|
| **STAT-01** | **Normalidade de S_struct** | ✅ **FIXADO (R5 M-2)** | Normalidade é **diagnóstico**, NÃO decisória. Friedman é o teste global primário em qualquer caso. RM-ANOVA (se executada) é exclusivamente suplementar/robustez (§3.5); Shapiro-Wilk só informa essa robustez |
| **STAT-02** | **Esfericidade / compostos simétricos** | ✅ **FIXADO (R5 M-2)** | Esfericidade é irrelevante para Friedman (teste global primário). Mauchly aplica-se **somente** à RM-ANOVA suplementar/robustez, se executada (§3.5) |
| **STAT-03** | **Dependência entre múltiplas seeds intra-unidade** | ✅ **FIXADO (R5 M-3)** | **3 seeds por (BIP × condição)**; `cell_value = median(seed_1, seed_2, seed_3)`; seeds são repetições intra-unidade, não unidades independentes (§1.3.1) |
| **STAT-04** | **Outliers em S_struct** | ✅ **FIXADO (R5-GOV-04)** | **DECIDIDO:** **NÃO winsorizar**; reportar análises com/sem outliers; sensibilidade sem outliers já planejada (Plano de Análise, passo 7) |
| **STAT-05** | **Tamanho de amostra (N=7 BIPs)** | ⚠️ Limitado (DECIDIDO R5-GOV-01) | **DECIDIDO: N = 7** mantido como piloto oficial; potência ≈0.63 reportada como limitação pré-registrada; N fixo = BIPs válidos; banda oficial §5.4 |
| **STAT-06** | **Múltiplas comparações exploratórias** | ✅ **FIXADO (R5-GOV-04)** | **DECIDIDO:** exploratório **sem controle formal de família**; separar confirmatório (3 pares) vs exploratório, com rótulo explícito no relatório |
| **STAT-07** | **Transformação** | ❌ Não verificada | Decisão: NÃO transformar; S_struct já em [0, 1] |
| **STAT-08** | **Validação do bootstrap (N pequeno)** | ✅ **FIXADO (R5-GOV-04)** | **DECIDIDO:** simulação metodológica de cobertura **executada** (§4.3.1); B=10.000 suficiente (erro MC desprezível); cobertura sub-nominal da mediana por condição em N=7 decorre do método percentil + N pequeno; mitigação: reportar IC exato da mediana ao lado do IC percentil |
| **STAT-09** | **Dependência entre casos (mesmo domínio)** | ✅ **FIXADO (R5-GOV-04)** | **DECIDIDO:** sensibilidade excluindo **1 caso por par dependente** (Hyatt OU I-35W; Ebola OU Warp Speed); **não** introduzir modelo misto (Plano de Análise, passo 7) |
| **STAT-10** | **Pré-registro do α pós-hoc** | ✅ **FIXADO (DECISION R3-04)** | `α = 0.05`; pós-hoc **bilaterais**; Wilcoxon signed-rank pareado; Holm-Bonferroni; Friedman como teste global; **nenhuma decisão unilateral posterior aos resultados** |

---

## 7. Plano de Análise (Ordem de Execução)

```
1. DATA CHECK
   - Completude: N_casos × 3 condições = todas células preenchidas?
   - Range check: S_struct ∈ [0, 1] para todas observações
   - Identificar missings (ex.: avaliador não completou condição)

2. AGREGAÇÃO INTRA-UNIDADE
   - Para cada (caso, condição): mediana das 3 seeds (pré-especificado R5 M-3) → 1 observação
   - Registrar nº de seeds (3) e desvio intra-célula (diagnóstico, não inferencial)

3. DESCRITIVA
   - Mediana, IQR, min, max de S_struct por condição (tabela + boxplot)
   - Mediana, IQR por caso (variabilidade entre domínios)

4. TESTE OMNIBUS (Friedman) sobre N_casos × 3
   - χ²_F, df=2, p-value, Kendall's W + IC 95% bootstrap
   - Se p ≥ 0.05: PARAR (não prosseguir para pós-hoc confirmatório)

5. PÓS-HOC (se omnibus significativo)
   - 3 testes Wilcoxon signed-rank pareados (sobre os MESMOS N BIPs)
   - Holm-Bonferroni
   - r_rb + IC 95% bootstrap para cada par significativo
   - Cliff's δ como robustez

6. EXPLORATÓRIO (sempre executado, rotulado como tal)
   - Interação Caso × Condição: descrição (Friedman por caso → descritivo)
   - Correlação Spearman S_struct × estimativas auxiliares (se disponíveis)
   - S_sem: mediana por caso×condição (diagnóstico)

7. SENSIBILIDADE
   - Repetir Friedman/Wilcoxon sem outliers (IQR×1.5)
   - **Dependência de domínio (STAT-09, DECIDIDO R5-GOV-04):** reexecutar Friedman excluindo
     **1 caso por par dependente** (Hyatt OU I-35W — Civil; Ebola OU Warp Speed — Saúde),
     2 execuções de sensibilidade; **sem modelo misto**
   - Registrar impactos; N nunca é alterado

8. RELATÓRIO
   - Tabela consolidada: estatística, p, tamanho de efeito, IC 95%
   - Gráfico: boxplot S_struct por condição + pontos individuais (caso)
   - Narrativa: utilidade da taxonomia C3
```

---

## 8. Interpretação de Equivalência — SECUNDÁRIA / OPCIONAL (DECISION R3-03 + DECIDIDO R5-GOV-03)

**Regra eliminada:** não existe regra do tipo `p > 0.20 ⇒ equivalência`. Não-significância **não** implica equivalência.

**Status (DECISION R3-03; confirmado DECIDIDO R5-GOV-03):** a equivalência **NÃO é hipótese primária do GO-8B**. O TOST é classificado como:

> **SECONDARY / OPTIONAL EQUIVALENCE ANALYSIS**
> **DECIDIDO (R5-GOV-03):** status quo mantido — **TOST não será executado no piloto**; nenhuma Δ aprovada.

1. **Nenhum TOST poderá ser executado sem margem Δ previamente especificada e justificada.**
2. **Nenhuma margem Δ é pré-aprovada.** A diretriz **não inventa Δ**; em particular, **Δ = 0.10 não está aprovada** e não deve aparecer como decisão vigente.
3. Enquanto nenhuma Δ justificada estiver registrada, a análise de equivalência **não é executada**; apenas a superioridade (H₁) é avaliada.
4. Se, no futuro, uma Δ for proposta, ela deve ser especificada e justificada **antes da coleta**, marcada explicitamente como análise secundária/opcional, e registrada no DISCOVERY-LOG.

---

## 9. Software e Reprodutibilidade

| Item | Especificação |
|---|---|
| **Linguagem** | Python 3.11+ |
| **Bibliotecas** | `scipy.stats` (friedmanchisquare, wilcoxon), `numpy`, `pandas`, `scikit-posthocs` (Holm), `bootstrap` (custom ou `arch.bootstrap`) |
| **Seed** | Ver bloco `seed_statistics` abaixo |
| **Ambiente** | `requirements.txt` / `pyproject.toml` com versões fixas |
| **Script** | `go8b_statistical_analysis.py` (determinístico, seed fixa) |
| **Simulação de potência** | `go8b_power_sim.py` (R5 M-3; executada com B=5.000, seed `20260811`; ver §5) |

### 9.1 Seed Estatística (Configuração — Correção 6)

```yaml
seed_statistics:
  value: 1879048193
  type: uint64
```

- Valor registrado como **inteiro válido** (substitui o literal hexadecimal anterior).
- Seed tratada como **dado de configuração**, não como literal inventado.
- Seeds são **repetições intra-unidade**: múltiplas execuções com seeds distintas → mediana por `(caso, condição)`; apenas essa mediana entra na análise inferencial. **N** permanece igual ao número de BIPs válidos.

### 9.2 Seed da Simulação de Potência (Stream Isolado — R5 M-3)

```yaml
seed_power_simulation:
  value: 20260811
  type: uint64
  uso: exclusivamente a simulação Monte Carlo de potência (go8b_power_sim.py, §5)
```

- **Stream isolado**: não reutilizada para análise estatística (`seed_statistics`) nem para a permutação C2 (`seed_c2`, Entregável 2 §9).
- Registrada como **dado de configuração**; a simulação foi executada **uma única vez** com esta seed; nenhum parâmetro foi ajustado após observar os resultados (§5).

---

## 10. Critérios de Interpretação (Decision Rules)

| Cenário | Interpretação | Ação GO-8B |
|---|---|---|
| Friedman p < 0.05 **E** B>A significativo (Holm) | Taxonomia C3 **melhora** reconstrução vs cega pura | Evidência a favor da utilidade de C3 |
| Friedman p < 0.05 **E** C>A significativo **MAS** B≈A | Narrativa completa ajuda; C3 **não** adiciona valor além de cega | C3 não justificada; rever design |
| Friedman p ≥ 0.05 | **Nenhuma evidência** de diferença entre condições; NÃO é equivalência | Reportar limitação de potência (N=7 → ≈0.63 sob cenário pré-especificado; §5); não concluir ausência de efeito |
| Friedman p < 0.05 **MAS** direção oposta (A > B) | Taxonomia C3 **prejudica** reconstrução | Falha crítica; investigar viés de C3 |
| Equivalência (secundária/opcional — R3-03; **DECIDIDO R5-GOV-03**) | TOST apenas com Δ especificada e justificada antes da coleta; **nenhuma Δ pré-aprovada**; **não executar TOST no piloto**; senão análise de equivalência não executada | Não executar TOST no piloto; manter apenas H₁ (superioridade) |

---

## GO-8B CHANGE LOG

### GO-8B-R1 (aplicado)
- Decision Record: 00-GO-8B-R1-DECISION-RECORD.md
- Revisão: R1
- Alterações principais:
  - Unidade experimental fixada em **BIP/Caso**; `N` = nº de BIPs válidos.
  - Eliminadas as formas `N = BIPs × avaliadores` e `N = BIPs × seeds`; seeds são repetições intra-unidade com agregação por mediana.
  - Friedman opera sobre matriz **N_casos × N_condições**; avaliadores não são blocos; N não é multiplicado artificialmente.
  - Pós-hoc: Wilcoxon signed-rank pareado, bilateral, Holm-Bonferroni.
  - Eliminada regra `p > 0.20 ⇒ equivalência`; formalizado TOST com Δ pré-registrada ou `DECISION REQUIRED`.
  - Seed substituída por inteiro válido `1879048193` (`uint64`), tratada como dado de configuração.
  - DV confirmatória passou a ser S_struct (S_sem exploratória).
- Alterações metodológicas:
  - Análise inferencial opera nas observações agregadas (mediana por caso×condição), preservando N = BIPs.
- Itens ainda pendentes:
  - Verificação de potência Monte Carlo a documentar.

### GO-8B-R3 (aplicado — DECISION R3-03, R3-04)
- **DECISION R3-03:** equivalência reclassificada como **SECONDARY / OPTIONAL EQUIVALENCE ANALYSIS**; não é hipótese primária do GO-8B; nenhum TOST sem Δ especificada e justificada antes da coleta; **nenhuma margem Δ pré-aprovada (Δ=0.10 não vigente)**; atualizado §8 e §10.
- **DECISION R3-04 (STAT-10 FIXADO):** `α = 0.05`; pós-hoc **bilaterais**; Wilcoxon signed-rank pareado; Holm-Bonferroni; Friedman como teste global; **nenhuma decisão unilateral posterior aos resultados** (§6 tabela).
- Status: REVISED — PENDING GOVERNANCE AUDIT

### GO-8B-R5 (aplicado — M-2, M-3, GO-8B-R5)
- **M-2 — Friedman fixado como TESTE GLOBAL PRIMÁRIO:** rm-anova removida como alternativa implícita; RM-ANOVA reclassificada como **suplementar/robustez somente** (§3.5); STAT-01 (normalidade) e STAT-02 (esfericidade) marcados **FIXADOS** como diagnósticos, não gates do teste global; matriz §3.1 alinhada aos rótulos de condição A/B/C; adicionado bloco de consistência final (§1.3.2: objetivo, hipótese, teste global, pós-hoc, α, unidade).
- **M-3 — Seeds pré-especificadas:** **3 seeds por (BIP × condição)**, `cell_value = median(seed_1, seed_2, seed_3)`, `seed = observação repetida dentro de BIP × condição`; seeds **não** constituem unidades experimentais independentes (§1.3.1, STAT-03 FIXADO).
- **M-3 — Potência Monte Carlo EXECUTADA:** simulação pré-especificada e executada **uma vez** (sem dados reais; nenhum parâmetro ajustado após resultados); §5 reescrito com configuração completa, resultados S0_NULL e S1_PRIMARY, erro Monte Carlo, ICs Wilson e interpretação; N=7 → potência ≈ 0.63; N=12 → ≥ 0.80.
- **M-3 — Banda de casos separada** (§5.4): mínimo metodológico (5 válidos para análise), recomendado piloto (7), necessário para potência (12); qualquer alteração = **DECISION REQUIRED**, nunca aplicada silenciosamente.
- Seed isolada da simulação de potência registrada (§9.2).
- Status: REVISED — PENDING GOVERNANCE AUDIT

### GO-8B-R6 (aplicado — DECISIONS R5-GOV-01..04)
- **R5-GOV-01:** **N = 7 mantido** como piloto oficial (§5.3, §5.4, STAT-05); potência ≈0.63 permanece limitação pré-registrada.
- **R5-GOV-02:** banda oficial **mínimo 5 válidos / piloto 7 / potência 12** mantida separada (§5.4).
- **R5-GOV-03:** status quo do TOST confirmado (§8) — secondary/optional, **sem Δ aprovada**, **não executar TOST no piloto**.
- **R5-GOV-04:** STAT-04 (não winsorizar + sensibilidade sem outliers), STAT-06 (exploratório, sem controle formal de família), STAT-09 (sensibilidade excluindo 1 caso por par dependente; sem modelo misto, Plano de Análise passo 7) → **FIXADOS**; STAT-08 → **simulação metodológica de cobertura do bootstrap executada** (§4.3.1; seed `20260812`, B_boot=10.000, MC=1.500): B=10.000 suficiente; mediana por condição com cobertura sub-nominal (~0.87–0.88) em N=7 (método percentil + N pequeno); diferença pareada ≈0.93; mitigação = reportar IC exato da mediana ao lado do percentil.
- Status: REVISED — PENDING GOVERNANCE AUDIT
