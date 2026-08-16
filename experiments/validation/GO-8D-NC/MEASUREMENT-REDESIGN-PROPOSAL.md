# MEASUREMENT-REDESIGN-PROPOSAL.md

**Proposta de Redesign de Mensuração — GO-8E (Pré-Proposta)**
**Data:** 2026-08-15
**Status:** PROPOSTA (não executada, não autorizada para execução)

---

## 1. Contexto

| Item | Status |
|------|--------|
| **GO-8D-NC** | CLOSED / LOCKED (14/14 artefatos íntegros) |
| **D-GO8E-01** | CLOSED — H3 (Interação) confirmado |
| **DV3 1:1:1** | **APOSENTADA** para inferência confirmatória |
| **Desfechos atuais** | `conf`, `ged_ecp`, `ent_n12` (separados) |
| **GO-8E** | **NÃO AUTORIZADO** — aguarda redesign + decisão de governança |

### Síntese do Diagnóstico (D-GO8E-01)

| Hipótese | Resultado |
|----------|-----------|
| **H1 — Efeito Real** | Moderada (degradação real em componentes) |
| **H2 — Artefato DV3** | Moderada + Estrutural (viés CAT em ged_ecp) |
| **H3 — Interação** | **FORTE** (Score 7) — Trade-offs mascarados pela média 1:1:1 |

**Conclusão do Diagnóstico:** A DV3 composta (média 1:1:1) **não é robusta** para inferência comparativa. Os três componentes movem-se em direções opostas (73% A→B, 67% B→C), a ordem A>B>C não é robusta a pesos/agregação/contrafactuais, e a ent_n12 domina a diferença (83%) sem necessariamente refletir qualidade real.

---

## 2. Objetivos do Redesign

| Objetivo | Descrição |
|----------|-----------|
| **O1** | Validar independentemente cada componente (`conf`, `ged_ecp`, `ent_n12`) |
| **O2** | Eliminar viés estrutural CAT/SYN no componente de similaridade estrutural |
| **O3** | Substituir `ent_n12` por métrica de diversidade validada independentemente |
| **O4** | Definir nova DV (ou conjunto de DVs) com validade de construto demonstrada |
| **O5** | Estabelecer critérios de aceitação prévios, sem usar resultado A>B para seleção |

---

## 3. Plano de Validação Independente dos Componentes

### 3.1 Componente `conf` (Confiança de Classificação)

| Atividade | Método | Critério de Aceitação |
|-----------|--------|----------------------|
| **Validade convergente** | Correlacionar `conf` com acurácia contra anotação ouro (se disponível) ou consistência bootstrap (1000 resamples) | ρ ≥ 0.7 com ground truth OU IC 95% bootstrap não inclui 0 |
| **Validade discriminante** | Verificar se `conf` distingue reconstruções "boas" vs "ruins" (injetar ruído controlado) | AUC ≥ 0.85 |
| **Estabilidade** | ICC entre réplicas (3 seeds) por BIP×condição | ICC ≥ 0.80 |
| **Sensibilidade a ruído** | Injetar ruído incremental nas narrativas/atomic facts; medir decaimento de `conf` | Decaimento monótono e suave |

### 3.2 Componente `ged_ecp` (Similaridade Estrutural)

| Atividade | Método | Critério de Aceitação |
|-----------|--------|----------------------|
| **Viés CAT/SYN** | Comparar `ged_ecp` (ref ECP/CAT) vs `ged_syn` (ref SYN) vs `ged_union` (ref união) | Diferença média entre referências < 0.02 |
| **Validade convergente** | Correlacionar com similaridade semântica humana (amostra de 50 pares julgados por 3 experts) | ρ ≥ 0.6 com julgamento humano |
| **Sensibilidade a perturbação** | Remover/adicionar arestas aleatoriamente (5%, 10%, 20%); medir sensibilidade | Curva suavemente decrescente; R² ≥ 0.9 |
| **Invariância a isomorfismo** | Aplicar permutações aleatórias de IDs de nós; `ged` deve ser invariante | Diferença = 0 (exato) |

### 3.3 Componente `ent_n12` (Diversidade Normalizada)

| Atividade | Método | Critério de Aceitação |
|-----------|--------|----------------------|
| **Sensibilidade a cardinalidade** | Testar com cardinalidades fixas vs variáveis; medir viés | Viés < 0.05 entre cardinalidades 9 vs 12 |
| **Alternativas** | Testar Shannon normalizado, Simpson inverso, riqueza bruta, Hill numbers (q=0,1,2) | Correlação ≥ 0.9 com pelo menos uma alternativa robusta |
| **Sensibilidade a raros** | Adicionar categorias raras (freq 1); medir impacto | Impacto proporcional à frequência |
| **Interpretabilidade** | Verificar se diferença de 0.1 em `ent` corresponde a diferença perceptível em diversidade | Experimento com 3 raters; concordância ≥ 80% |

---

## 4. Análise da Referência GED (Eliminação de Viés CAT/SYN)

### 4.1 Problema Identificado
- `ged_ecp` usa grafo de referência ECP (CAT, 9 nós) como padrão
- Condição B usa taxonomia SYN (12 nós) → dissimilaridade inerente
- C3 introduz categorias SYN → `ged_ecp` cai artificialmente

### 4.2 Referências Candidatas a Testar

| Referência | Construção | Hipótese |
|------------|------------|----------|
| **ECP (CAT)** | Grafo canônico ECP (9 nós) | Baseline (viés CAT) |
| **SYN** | Grafo C3/SYN (12 nós) | Viés SYN |
| **UNION** | União ECP ∪ SYN (21 nós) | Neutra? |
| **INTERSECTION** | ECP ∩ SYN (comum) | Conservadora |
| **NEUTRAL** | Grafo sintético balanceado (ex.: 10 nós, grau médio 3) | Neutra por construção |
| **DATA-DRIVEN** | Grafo consenso de todas as reconstruções (MST) | Empírica |

### 4.3 Protocolo de Teste

1. Para cada referência, recalcular `ged_ref` para todas as 270 execuções
2. Calcular DV3* = (conf + ged_ref + ent_n12) / 3
3. Testar Friedman + Wilcoxon para cada referência
4. **Critério:** Referência "neutra" se:
   - Friedman p > 0.05 (sem diferença sistemática A vs B vs C) OU
   - Ordem A>B>C **não** é universal (varia com pesos)

### 4.4 Critério de Decisão

| Resultado | Ação |
|-----------|------|
| Existe referência neutra com Friedman p > 0.05 | Adotar referência neutra; manter estrutura DV3 |
| Nenhuma referência neutra; viés inerente | Abandonar `ged` como componente único; usar ensemble de referências |
| `ged` irrelevante (peso → 0 em otimização) | Remover `ged`; usar apenas `conf` + diversidade |

---

## 5. Estudo de Diversidade (Substituição de `ent_n12`)

### 5.1 Problemas com `ent_n12`

| Problema | Evidência |
|----------|-----------|
| Sensibilidade a cardinalidade | 9 slots (CAT) vs 12 slots (SYN) → viés |
| Sensibilidade a categorias raras | Categorias com freq=1 reduzem entropia desproporcionalmente |
| Normalização log(12) | Arbitrária; assume 12 categorias máximas |
| Interpretação | Diferença de 0.1 não tem significado operacional claro |

### 5.2 Candidatas a Testar

| Métrica | Fórmula | Propriedades |
|---------|---------|--------------|
| **Shannon normalizado** | H / log(K) | Padrão; sensível a raros |
| **Simpson inverso** | 1 / Σ pᵢ² | Robusto a raros; peso em dominantes |
| **Hill q=1 (exp Shannon)** | exp(H) | Número efetivo de categorias |
| **Hill q=2 (inv Simpson)** | 1/Σpᵢ² | Ênfase em dominantes |
| **Riqueza bruta** | K (nº categorias usadas) | Simples; ignora frequências |
| **Chao1 / ACE** | Estimadores de riqueza | Corrigem subamostragem |
| **Rao's quadratic entropy** | ΣΣ dᵢⱼ pᵢ pⱼ | Incorpora dissimilaridade entre categorias |

### 5.3 Protocolo de Validação

1. Calcular todas as métricas para 270 execuções
2. Correlacionar com `ent_n12` (ρ de Spearman)
3. Testar viés CAT/SYN (Friedman por métrica)
4. **Critério de seleção:**
   - ρ ≥ 0.9 com `ent_n12` (continuidade) **E**
   - Friedman p > 0.05 (sem viés CAT/SYN) **OU** viés < 0.01
   - Interpretabilidade operacional (teste com 3 raters)

---

## 6. Critérios Pré-Especificados para Nova DV

### 6.1 Requisitos Obrigatórios

| Critério | Descrição |
|----------|-----------|
| **C1 — Validade independente** | Cada componente validado independentemente (Seção 3) |
| **C2 — Sem viés estrutural** | Friedman p > 0.05 OU viés CAT/SYN < 0.01 |
| **C3 — Robustez a pesos** | Ordem A/B/C estável em ≥ 80% de combinações de pesos (grid 0.2–5.0) |
| **C4 — Robustez a agregação** | Ordem estável em média aritmética, geométrica, harmônica |
| **C5 — Sensibilidade** | Detecta degradação injetada (ruído, omissão, permutação) |
| **C6 — Interpretabilidade** | Diferença de 0.1 tem significado operacional claro (raters ≥ 80% concordância) |

### 6.2 Proibições Absolutas

| Proibição | Sanção |
|-----------|--------|
| Usar resultado A > B para escolher métrica | **INVALIDA** a proposta |
| Escolher pesos retrospectivamente (pós-hoc) | **INVALIDA** a proposta |
| Otimizar para maximizar significância | **INVALIDA** a proposta |
| Excluir BIPs/outliers pós-hoc | **INVALIDA** a proposta |

### 6.3 Processo de Seleção

1. **Fase 1:** Validar componentes independentemente (Seção 3) → Go/No-Go por componente
2. **Fase 2:** Testar referências GED (Seção 4) → Selecionar referência ou ensemble
3. **Fase 3:** Selecionar métrica de diversidade (Seção 5) → Substituir `ent_n12`
4. **Fase 4:** Testar combinações de componentes (grid de pesos + agregações) → Aplicar C1–C6
5. **Fase 5:** Se ≥1 combinação passa C1–C6 → Documentar como **Nova DV Candidata**
5. **Fase 6:** Simular potência com Nova DV → Definir N para GO-8E

---

## 7. Sequência Futura (Roadmap)

| Etapa | Atividade | Entrada | Saída | Gate |
|-------|-----------|---------|-------|------|
| **1** | Validação independente componentes | Dados GO-8D-NC congelados | Relatório validação C1 | C1 PASS |
| **2** | Análise referência GED + diversidade | Dados GO-8D-NC + simulações | Referência GED + Métrica diversidade | C2 PASS |
| **3** | Busca de nova DV candidata | Componentes validados | Nova DV candidata + pesos | C3–C6 PASS |
| **4** | Simulação de potência | Nova DV + efeitos observados | N recomendado | Poder ≥ 0.80 (TOST) |
| **5** | Pré-registro GO-8E | Nova DV + N | `08-PRE-REGISTRATION-GO-8E.md` v1.0 | Aprovação governança |
| **6** | Lock GO-8E | Pré-registro + scripts + taxonomia | `GO-8E-LOCK-MANIFEST.yaml` | Lock validado |
| **6** | Aquisição BIPs | Lista 18 BIPs | 18 novos BIPs no GO-8E | Autorização |
| **7** | Execução GO-8E | Lock + BIPs + seeds | 270 reconstruções | F2 PASS |
| **8** | Análise GO-8E | Dados GO-8E | Relatório estatístico | F3 COMPLETE |

---

## 8. Regras de Governança (Incorporadas)

| Regra | Origem | Status |
|-------|--------|--------|
| Não usar A > B para escolher métrica | D-GO8E-01 Closure | **ABSOLUTA** |
| Não escolher pesos retrospectivamente | D-GO8E-01 Closure | **ABSOLUTA** |
| Não calcular potência antes de validação | Esta proposta | **ABSOLUTA** |
| Não elaborar pré-registro antes de Lock | Esta proposta | **ABSOLUTA** |
| Não coletar BIPs antes de Lock | Esta proposta | **ABSOLUTA** |
| Não executar experimento sem Lock | Esta proposta | **ABSOLUTA** |
| Não alterar Locks anteriores | Governança | **ABSOLUTA** |
| Não abrir GO-8E sem decisão | Governança | **ABSOLUTA** |

---

## 9. Recomendação de Governança

### Recomendação

> **AUTORIZAR A FASE 1 (Validação Independente dos Componentes)**

### Justificativa

1. **Necessidade comprovada:** D-GO8E-01 confirmou H3 (Interação) — a DV3 composta falha em robustez
2. **Risco zero:** Fase 1 usa apenas dados congelados do GO-8D-NC; sem novos dados, sem experimento
3. **Decisão informada:** Resultados da Fase 1 determinarão se vale prosseguir para Fases 2–4
4. **Conformidade:** Não viola nenhuma regra de governança (sem potência, sem pré-registro, sem Lock, sem experimento)

### Recursos Necessários (Fase 1)

| Recurso | Estimativa |
|-----------|------------|
| Tempo | 2–3 semanas |
| Equipe | 1 estatístico + 1 engenheiro + 1 domain expert |
| Computação | CPU only (sem GPU); ~4h de processamento |
| Dados | `pilot_results_newcycle.csv`, `dv3_matrix_newcycle.npy` (já existentes) |

---

## 10. Próximos Passos (Se Autorizado)

| Ação Imediata | Responsável | Prazo |
|---------------|-------------|-------|
| Criar script `validate_components.py` (Seção 3) | Engenheiro | Semana 1 |
| Executar validação conf/ged_ecp/ent_n12 | Estatístico | Semana 1 |
| Produzir relatório Fase 1 | Estatístico + Engenheiro | Semana 2 |
| Apresentar à governança | Líder técnico | Semana 2 |

---

## 11. Decisão de Governança Solicitada

> **SOLICITAÇÃO:** Autorizar **Fase 1 — Validação Independente dos Componentes** (conf, ged_ecp, ent_n12) conforme Seção 3 desta proposta.
>
> **NÃO AUTORIZA:** Fases 2–6, cálculo de potência, pré-registro, Lock, coleta, experimento.

---

**Assinatura:** Proposta de Redesign de Mensuração — GO-8E  
**Data:** 2026-08-15  
**Lock Manifest (GO-8D-NC):** `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`  
**Dependências:** D-GO8E-01 CLOSED, GO-8D-NC CLOSED/LOCKED