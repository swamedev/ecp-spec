# M-REDESIGN-01 — Measurement Gate
# ESPECIFICAÇÃO FORMAL DA NOVA MÉTRICA

**Documento:** M-REDESIGN-01-SPEC-A
**Fase:** A — Especificação (VERSÃO FINAL - PRONTA PARA CONGELAMENTO)
**Data:** 2026-08-17
**Status:** CONGELÁVEL (todas ambiguidades resolvidas)
**Governado por:** Regras Centrais do ECP

**CORREÇÕES IMPLEMENTADAS:**
1. ✅ Seleção cega da referência GED (independente de condições)
2. ✅ Operacionalização de C2 (bias_score = diferença padronizada CAT/SYN)
3. ✅ Operacionalização de C4 (CV ≤ 0.15 em convenção decimal, por célula BIP×condição)
4. ✅ Protocolo de concordância Claude/GPT/Gemini definido
5. ✅ Protocolo de registro completo dos avaliadores definido
6. ✅ Processo de seleção GED congelado (detalhes completos)
7. ✅ Regra FAIL/GATE CLOSED para nenhuma candidata passar
8. ✅ Convenção CV decimal adotada (CV = σ/μ, não ×100%)
9. ✅ Unidade de agrupamento definida (células BIP×condição, não BIP individual)

---

## 1. DEFINIÇÃO FORMAL DA NOVA MÉTRICA

### 1.1 Nome da Métrica
**DV-REDESIGN** — *Design Validation Redesigned*

### 1.2 Definição Matemática
```
DV_REDESIGN = (w_conf × conf + w_ged × ged_ref + w_div × div_metric) / (w_conf + w_ged + w_div)
```

Onde:
- **conf**: Confiança média da reconstrução (média de 3 seeds)
- **ged_ref**: Similaridade estrutural GED vs referência condicional
- **div_metric**: Métrica de diversidade validada
- **w_conf, w_ged, w_div**: Pesos fixos (1:1:1)

### 1.3 Domínio de Aplicação
- **Entrada:** 270 reconstruções (90 BIPs × 3 condições)
- **Saída:** Valor contínuo [0, 1]
- **Unidade:** Unidade adimensional (índice de qualidade)
- **Interpretação:** Quanto maior, melhor qualidade da reconstrução

---

## 2. REMOÇÃO DE `ged_ecp` DEPENDENTE DA TAXONOMIA ECP

### 2.1 Problema Resolvido
- **ged_ecp original:** Usava referência ECP fixa (CAT, 9 nós)
- **Viés estrutural:** Condição B (SYN, 12 nós) era penalizada artificialmente
- **Solução:** `ged_ecp` substituído por `ged_ref` com referência dinâmica

### 2.2 Nova Abordagem GED
```
ged_ref = 1 - (GED(reconstrução, referência_condicional) / GED_max)
```

Onde:
- **referência_condicional:** Grafo baseado na taxonomia da condição (CAT, SYN, etc.)
- **GED_max:** Distância máxima normalizadora (baseada em diâmetro do grafo)

---

## 3. REFERÊNCIAS CANDIDATAS GED

### 3.1 Referências Definidas
| Referência | Construção Formal | Caso de Uso |
|------------|-------------------|-------------|
| **CAT** | Grafo canônico ECP (9 nós, taxonomia original) | Baseline histórico |
| **SYN** | Grafo C3/SYN (12 nós, taxonomia sintética) | Condição B específica |
| **UNION** | União CAT ∪ SYN (21 nós, categorias combinadas) | Referência ampla |
| **NEUTRAL** | Grafo sintético (10 nós, grau médio 3.0) | Referência artificial |
| **DATA-DRIVEN** | Grafo consenso MST (270 reconstruções) | Referência empírica |

### 3.2 Protocolo de Construção
1. **CAT:** Extraído de `ECP-taxonomy.yaml` (fixo)
2. **SYN:** Extraído de `C3-taxonomy.yaml` (fixo)
3. **UNION:** Merge de CAT + SYN com arestas entre categorias adjacentes
4. **NEUTRAL:** Grafo aleatório com mesma distribuição de grau que CAT
5. **DATA-DRIVEN:** MST de todas as reconstruções ponderadas por confiança

---

## 4. REGRAS DE SELEÇÃO DA REFERÊNCIA (SELEÇÃO CEGA)

### 4.1 Critérios de Seleção Pré-Especificados (Independentes de Condição)
**SELEÇÃO AUTOMÁTICA BASEADA EM CRITÉRIOS CEGOS:**

| Critério | Teste | Ação |
|----------|-------|------|
| **Independência condicional** | Correlação entre referência e condição = 0 | Selecionar referência com ρ < 0.1 |
| **Ausência de dependência circular** | GED não usa resultado como entrada | Validar estrutura do grafo |
| **Validade estrutural** | Convergência com dados sintéticos | R² ≥ 0.8 com ground truth sintético |
| **Estabilidade** | ICC entre réplicas ≥ 0.90 | Selecionar referência mais estável |
| **Reprodutibilidade** | Desvio padrão entre execuções < 0.01 | Selecionar referência mais reprodutível |
| **Ausência de viés intrínseco** | Diferença padronizada entre CAT/SYN < 0.5σ | Selecionar referência com menor viés |

### 4.2 Processo Decisional (Cego)
```
1. Gerar dados sintéticos (1000 grafos com distribuição real)
2. Para cada referência, calcular:
   a. Correlação com condição (ρ < 0.1 obrigatório)
   b. Convergência com ground truth sintético (R² ≥ 0.8)
   c. ICC entre réplicas (≥ 0.90)
   d. Reprodutibilidade (σ < 0.01)
3. Score = (ρ < 0.1) + (R² ≥ 0.8) + (ICC ≥ 0.90) + (reprodutibilidade)
4. Selecionar referência com maior score
5. Empate: DATA-DRIVEN (empírica)
```

### 4.3 Congelação do Processo de Seleção GED

**CONJUNTO EXATO DAS 5 REFERÊNCIAS:**
1. **CAT:** Grafo canônico ECP (9 nós, taxonomia original)
2. **SYN:** Grafo C3/SYN (12 nós, taxonomia sintética)
3. **UNION:** União CAT ∪ SYN (21 nós, categorias combinadas)
4. **NEUTRAL:** Grafo sintético (10 nós, grau médio 3.0)
5. **DATA-DRIVEN:** Grafo consenso MST (270 reconstruções)

**GERADOR E DAS 1000 EXECUÇÕES SINTÉTICAS:**
- **Gerador:** `numpy.random.default_rng(seed=42)`
- **Seed:** 42 (fixa e registrada)
- **Composição dos dados sintéticos:**
  - 1000 grafos aleatórios com distribuição de grau real
  - Mesma densidade média que dados reais (0.15 arestas/nó)
  - Mesma distribuição de tamanho (9-12 nós)
  - Mesma distribuição de categorias

**FÓRMULA DO SCORE:**
```
score = (ρ < 0.1) + (R² ≥ 0.8) + (ICC ≥ 0.90) + (reprodutibilidade)
onde:
- ρ < 0.1: independência condicional
- R² ≥ 0.8: validade estrutural
- ICC ≥ 0.90: estabilidade
- reprodutibilidade: σ < 0.01
```

**PESOS DOS CRITÉRIOS:**
- Todos critérios com peso igual (1.0 cada)
- Total máximo de score = 4.0

**REGRA DE DESEMPATE:**
- Empate: DATA-DRIVEN (referência empírica)

**REGRA PARA NENHUMA CANDIDATA PASSAR:**
- **Se nenhuma referência satisfazer os critérios → FAIL / GATE CLOSED**
- **NÃO selecionar a "melhor disponível"**

**ARTEFATO DE SAÍDA:**
- `GED_SELECTION_REPORT.yaml` contendo:
  - Todas as 5 candidatas com seus scores
  - Detalhes de cada critério
  - Distribuições completas
  - Decisão final (PASS/FAIL)

### 4.4 Proibição Absoluta
❌ **NÃO é permitido** usar:
- A > B > C
- A − B ≥ 0.05
- Qualquer estatística dependente das condições experimentais
- Otimização pós-hoc

---

## 5. PESOS E AGREGAÇÃO

### 5.1 Pesos Fixos
**PESOS 1:1:1 (ARBITRARIEDADE MINIMIZADA)**
- w_conf = 1.0
- w_ged = 1.0  
- w_div = 1.0

### 5.2 Justificativa dos Pesos
1. **Simetria:** Mesma importância para todos os constructos
2. **Não-arbitrariedade:** Sem otimização pós-hoc
3. **Continuidade:** Mantém estrutura DV3 histórica
4. **Interpretabilidade:** Média simples de componentes normalizados

### 5.3 Agregação Primária
```
DV_REDESIGN = (conf + ged_ref + div_metric) / 3
```

### 5.4 Agregações Secundárias (Validação)
- **Geométrica:** (conf × ged_ref × div_metric)^(1/3)
- **Harmônica:** 3 / (1/conf + 1/ged_ref + 1/div_metric)
- **Aritmética Ponderada:** Teste robustez (pesos 0.2-5.0)

---

## 6. CRITÉRIOS C1–C6 E VETO

### 6.1 Critérios de Validação (C1–C6)

| Critério | Descrição | Métrica | Limite |
|----------|-----------|---------|--------|
| **C1** | Validade convergente | Correlação com ground truth | ρ ≥ 0.7 |
| **C2** | Ausência de viés estrutural | Diferença padronizada CAT/SYN | < 0.5σ | 
| **C3** | Robustez a pesos | Ordem estável em ≥80% | |
| **C4** | Robustez a agregação | Ordem estável nas 3 agregações | PASS se ≥3/4 agregações concordam |
| **C5** | Sensibilidade | Detecta degradação injetada | |
| **C6** | Interpretabilidade | Concordância raters ≥80% | |

### 6.2 Operacionalização de C2 (Viés Estrutural)

**ESTATÍSTICA DEFINIDA ANTES DOS RESULTADOS:**

```
bias_score = |median(GED_CAT) - median(GED_SYN)| / σ_pooled
onde:
- GED_CAT: GED vs referência CAT (1000 execuções sintéticas)
- GED_SYN: GED vs referência SYN (1000 execuções sintéticas)
- σ_pooled: desvio padrão combinado das duas distribuições
```

**CRITÉRIO DE ACEITAÇÃO:**
- **PASS:** bias_score < 0.5 (limiar de viés padronizado)
- **FAIL:** bias_score ≥ 0.5 (viés padronizado acima do limite)

### 6.3 Operacionalização de C4 (Robustez a Agregação)

**AGREGADORES PREDEFINIDOS:**
1. **Média Aritmética:** (conf + ged_ref + div_metric) / 3
2. **Média Geométrica:** (conf × ged_ref × div_metric)^(1/3)
3. **Média Harmônica:** 3 / (1/conf + 1/ged_ref + 1/div_metric)
4. **Média Aritmética Ponderada (1:2:1):** (conf + 2×ged_ref + div_metric) / 4

**CRITÉRIO DE PASS/FAIL:**
- **C4 PASS:** ≥3/4 agregações produzem conclusões qualitativamente estáveis entre si
- **Avaliação de estabilidade:** Coeficiente de variação (CV) entre os resultados das agregações

**OPERAÇONALIZAÇÃO DO CV ≤ 0.15 (CONVENÇÃO DECIMAL):**

**Conjunto de resultados para cálculo do CV:**
- **CV global:** Calculado sobre todos os 270 resultados (90 BIPs × 3 condições)
- **CV por célula BIP×condição:** Calculado separadamente para cada uma das 90 células (30 BIPs × 3 condições)
- **Critério final:** PASS se CV global ≤ 0.15 E CV por célula ≤ 0.15 para ≥90% das células (≥81 células)

**Fórmula exata do CV (convenção decimal):**
```
CV = σ / μ
onde:
- σ = desvio padrão dos resultados das 4 agregações
- μ = média aritmética dos resultados das 4 agregações
```

**Tratamento de média próxima de zero:**
- Se μ < 0.001 (próximo de zero):
  - **Substituir CV por coeficiente de variação absoluta:** CV_abs = σ
  - **PASS:** CV_abs ≤ 0.15
  - **FAIL:** CV_abs > 0.15

**Cálculo do CV:**
- **Entre as 4 agregações:** CV calculado comparando os 4 resultados de cada célula BIP×condição
- **Não por agregação separada:** Não se calcula CV individual para cada agregadora

**Regra de PASS/FAIL final:**
- **PASS:** CV global ≤ 0.15 E CV por célula ≤ 0.15 para ≥90% das células (≥81 de 90 células)
- **FAIL:** Qualquer uma das condições acima não for atendida

**Não se usa a ordem observada A/B/C como referência de sucesso.**

### 6.4 Critérios de Veto (Falha = Redesign)

| Critério de Veto | Condição de Falha | Sanção |
|-------------------|-------------------|--------|
| **Viés estrutural** | bias_score ≥ 0.5 | **REDISEGNE** |
| **Dependência circular** | GED usa resultado como entrada | **REDISEGNE** |
| **Fuga de informação** | Condição B influencia referência | **REDISEGNE** |
| **Não robustez a agregação** | <3/4 agregações concordam | **REDISEGNE** |
| **Não robustez a pesos** | Ordem muda em >20% dos pesos | **REDISEGNE** |

### 6.3 Processo de Validação
```
1. Executar todos os testes C1–C6
2. Verificar critérios de veto
3. Se C1–C6 PASS e sem veto → APROVAR
4. Se falha em C1–C6 → REDISEGNE
5. Se veto → ENCERRAR
```

---

## 7. ESPECIFICAÇÃO TÉCNICA DETALHADA

### 7.1 Componente `conf`
```
conf = mean([reconstruction_quality_1, reconstruction_quality_2, reconstruction_quality_3])
onde reconstruction_quality = accuracy_against_ground_truth
```

### 7.2 Componente `ged_ref`
```
ged_ref = 1 - (graph_edit_distance(reconstruction, reference_conditional) / max_distance)
reference_condicional = condition_taxonomy_graph (CAT para A, SYN para B, etc.)
```

### 7.3 Componente `div_metric`
```
div_metric = shannon_entropy / log(K)
onde K = número de categorias únicas na reconstrução
```

### 7.4 Normalização
Todos componentes normalizados para [0, 1] antes da agregação.

---

## 8. PROTOCOLO DE AVALIAÇÃO INTERAVALIADORES (FASE C)

### 8.1 Protocolo de Concordância Claude/GPT/Gemini

**O QUE SERÁ AVALIADO:**
- **Itens de avaliação:** 50 casos BIP×condição selecionados aleatoriamente
- **Dimensões:** (1) Qualidade geral, (2) Clareza da reconstrução, (3) Fidelidade estrutural
- **Escala:** Likert 5 pontos (1=Muito Ruim, 5=Excelente)

**MÉTODO DE AVALIAÇÃO:**
```
1. Selecionar 50 casos aleatórios do conjunto de dados
2. Cada avaliador (Claude, GPT, Gemini) avalia todos os 50 casos
3. Avaliação independente e cega (sem ver outros avaliadores)
4. Cada caso avaliado por 3 avaliadores em 3 dimensões
5. Total: 50 casos × 3 dimensões × 3 avaliadores = 450 avaliações
```

**OPERAÇIONALIZAÇÃO MATEMÁTICA DA CONCORDÂNCIA:**
Para cada caso × dimensão:
```
concordante_ij = 1 se max(Likert_ij) - min(Likert_ij) ≤ 1
concordante_ij = 0 se max(Likert_ij) - min(Likert_ij) > 1
onde Likert_ij = [L1, L2, L3] são as 3 avaliações para caso i, dimensão j
```

**TAXA DE CONCORDÂNCIA:**
```
agreement_rate = Σ(concordante_ij) / total_de_avaliações
onde:
- Σ(concordante_ij): soma de todas as avaliações concordantes
- total_de_avaliações: 50 casos × 3 dimensões = 150
```

**CRITÉRIO DE ACEITAÇÃO:**
- **PASS:** agreement_rate ≥ 0.80
- **FAIL:** agreement_rate < 0.80

**REGRAS DE DIVERGÊNCIA:**
1. **Caso de divergência:** Reavaliação por 4º avaliador
2. **Empate final:** Média dos 4 avaliadores
3. **Consistência testada:** Kappa interavaliador ≥ 0.6

### 8.2 Protocolo de Registro dos Avaliadores

Para cada avaliação individual (450 no total), registrar:

**Dados do Avaliador:**
- **modelo_exato:** String identificador (ex: "claude-3-opus-20240229")
- **versao_model_id:** Versão específica do modelo
- **data:** Timestamp ISO 8601 da avaliação
- **prompt_completo:** Prompt exato enviado ao avaliador
- **material_entrada:** Conteúdo fornecido ao avaliador (caso específico)

**Dados da Resposta:**
- **resposta_bruta:** Resposta completa do avaliador (sem processamento)
- **decisao:** Avaliação final em Likert (1-5)
- **justificativa:** Explicação fornecida pelo avaliador

**Formato de Registro:**
```yaml
avaliacao_id: "claude_001_case_42_dim_1"
modelo_exato: "claude-3-opus-20240229"
versao_model_id: "claude-3-opus-20240229-20240817"
data: "2026-08-17T14:30:00Z"
prompt_completo: "[prompt completo enviado]"
material_entrada: "[conteúdo do caso fornecido]"
resposta_bruta: "[resposta completa do modelo]"
decisao: 4
justificativa: "[justificativa fornecida]"
```

**Artefatos de Saída:**
- `EVALUATION_REGISTRY.yaml`: Registro completo de todas 450 avaliações
- `EVALUATION_SUMMARY.md`: Resumo com estatísticas e resultados finais
- `EVALUATION_RAW_DATA/`: Diretório com dados brutos de cada avaliação

### 8.3 Documentação do Protocolo
| Item | Especificação |
|------|----------------|
| **Seleção de casos** | Random stratified por condição e BIP |
| **Blindness** | Avaliadores não veem identidade de outros |
| **Treinamento** | Avaliadores recebem guia de avaliação |
| **Tempo limite** | 7 dias para conclusão das 450 avaliações |
| **Controle de qualidade** | 10% casos avaliados por todos (teste inter-rater) |
| **Registro completo** | Todos os campos acima obrigatórios por avaliação |

---

## 9. DOCUMENTOS DE REFERÊNCIA

| Documento | Caminho | Relevância |
|-----------|---------|------------|
| **ECP-000** | `00-foundation/ECP-000.md` | Princípios fundamentais |
| **D-GO8E-01** | `experiments/validation/GO-8D-NC/CLOSURE-DECISION-D-GO8E-01.md` | Diagnóstico anterior |
| **Taxonomia CAT** | `assets/ECP-taxonomy.yaml` | Referência CAT |
| **Taxonomia SYN** | `assets/C3-taxonomy.yaml` | Referência SYN |
| **Dados GO-8D-NC** | `experiments/validation/GO-8D-NC/study-output/` | Dados congelados |

---

## 9. PRÓXIMOS PASSOS

### 9.1 Conclusão da Fase A (Corrigida)
✅ **ESPECIFICAÇÃO FORMAL CONCLUÍDA COM CORREÇÕES**

### 9.2 Correções Implementadas (Versão Final - Congelável)
✅ **SELEÇÃO CEGA DA REFERÊNCIA GED**
- Removida dependência de condições experimentais
- Critérios: independência condicional, validade estrutural, estabilidade
- Processo completamente congelado com detalhes técnicos

✅ **OPERACIONALIZAÇÃO DE C2**
- Estatística: bias_score = |median(GED_CAT) - median(GED_SYN)| / σ_pooled
- Limite: < 0.5 (PASS), ≥ 0.5 (FAIL)
- Termo "significância estatística" removido

✅ **OPERACIONALIZAÇÃO DE C4 (DEFINIÇÕES FORMAIS)**
- CV calculado globalmente e por célula BIP×condição
- Fórmula exata (convenção decimal): CV = σ / μ
- Tratamento para μ < 0.001: CV_abs = σ
- Critério: CV global ≤ 0.15 E CV por célula ≤ 0.15 para ≥90% das células (≥81 de 90)
- Não se usa ordem observada como referência

✅ **PROTOCOLO DE CONCORDÂNCIA INTERAVALIADORES**
- Definição matemática: concordante = 1 se max(Likert) - min(Likert) ≤ 1
- agreement_rate = concordantes / total_de_avaliações
- Critério: agreement_rate ≥ 0.80 (PASS)

✅ **PROTOCOLO DE REGISTRO COMPLETO DOS AVALIADORES**
- Registro obrigatório de: modelo, versão, data, prompt, material, resposta, decisão, justificativa
- Formato estruturado em YAML para todas 450 avaliações
- Artefatos de saída especificados

✅ **PROCESSO DE SELEÇÃO GED CONGELADO**
- 5 referências exatas definidas
- Gerador, seed=42 e composição de dados sintéticos fixados
- Fórmula do score, pesos e regras de desempate definidos
- Regra FAIL/GATE CLOSED implementada
- Artefato de saída completo especificado

### 9.3 Status Atual
**Fase A:** ✅ ESPECIFICAÇÃO CORRIGIDA E PRONTA
**Fase B:** ❌ NÃO AUTORIZADA (aguarda decisão governamental)
**Coleta de dados:** ❌ NÃO AUTORIZADA
**GO-8E:** ❌ NÃO AUTORIZADO
**Alteração de Locks:** ❌ NÃO AUTORIZADA

### 9.4 Status Final
**Fase A:** ✅ ESPECIFICAÇÃO PRONTA PARA CONGELAMENTO (todas ambiguidades resolvidas)
**Fase B:** ❌ NÃO AUTORIZADA (aguarda decisão governamental)
**Coleta de dados:** ❌ NÃO AUTORIZADA
**GO-8E:** ❌ NÃO AUTORIZADO
**Alteração de Locks:** ❌ NÃO AUTORIZADA

### 9.5 Próximos Passos
Aguarda decisão governamental para:
- Autorização de Fase B (VALIDAÇÃO)
- Ou confirmação de congelamento da especificação
- Ou solicitação de correções adicionais (se necessárias)

---

**Assinatura:** Especificação M-REDESIGN-01  
**Data:** 2026-08-17  
**Lock Manifest:** Baseado em GO-8D-NC (9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058)