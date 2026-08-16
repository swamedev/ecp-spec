# D-GO8E-01-PROPOSAL.md

**Proposta Diagnóstica — GO-8E**
**Referência:** D-GO8E-01
**Data:** 2026-08-15
**Status:** PROPOSTA (não executada)

---

## 1. Contexto

O ciclo GO-8D-NC foi encerrado com status **CLOSED**.

### Resumo do Resultado GO-8D-NC

| Item | Resultado |
|------|-----------|
| Hipótese primária (B < A) | **CONFIRMADA** sob DV3 (p = 2.61 × 10⁻⁸, Cliff Δ = 0.936) |
| Ordem observada | **A > B > C** (medianas DV3: 0.6206 > 0.5874 > 0.5758) |
| TOST A–C (Δ = 0.05) | **NÃO EQUIVALENTE** |
| Go/No-Go | **GO** (30/30 BIPs válidos) |
| Lock metodológico | **ÍNTEGRO** (14/14 hashes) |

### Interpretação Atual (Limitada a DV3)

> Sob a métrica DV3, a condição **A (cega pura)** produz reconstruções de maior qualidade que **B (cega + C3)**, que por sua vez supera **C (não-cega)**. O efeito A > B é **muito grande** (Cliff Δ = 0.936); B > C é **pequeno/médio** (Cliff Δ = 0.240).

**Interpretação causal: NÃO AFIRMADA.** O resultado é estritamente limitado à métrica DV3.

---

## 2. Pergunta Central

> **"Por que C3 reduz a DV3? Perda real ou limitação da métrica?"**

O resultado contraintuitivo (cega pura > cega + taxonomia) exige investigação diagnóstica antes de qualquer decisão sobre GO-8E.

---

## 3. Hipóteses Formalmente Separadas

| Hipótese | Descrição | Previsão Principal |
|----------|-----------|---------------------|
| **H1 — Efeito Real** | C3 introduz restrições/informação que **pioram** a reconstrução real (não apenas a métrica). A taxonomia C3 adiciona ruído, viés ou restrições inadequadas que degradam a qualidade real da reconstrução. | Decomposição da DV3 mostra queda em componentes ligados à fidelidade real (ex.: ged_ecp). Validação externa confirma perda. |
| **H2 — Artefato da DV3** | A queda decorre **exclusivamente** de propriedades da métrica DV3: composição 1:1:1, penalização de categorias SYN, ent_n12, ou ged_ecp referenciado a ECP canônico. Não há perda real de qualidade. | Decomposição mostra queda concentrada em componentes arbitrários da métrica (ex.: ent_n12 penaliza diversidade SYN). ged_ecp favorece CAT por definição. Validação externa não confirma perda. |
| **H3 — Interação** | C3 **melhora alguns aspectos e piora outros**, mascarados pela média composta 1:1:1. Ex.: melhora conf mas piora ged_ecp; ou melhora ent_n12 mas piora conf. | Decomposição mostra sinais opostos entre componentes. Soma composta mascara trade-offs. |

> **As três hipóteses são mutuamente exclusivas e exaustivas** para a pergunta central.

---

## 4. Plano de Investigação Diagnóstica (Sem Coleta Nova)

### 4.1 Princípios Gerais

| Regra | Descrição |
|-------|-----------|
| **Sem novos BIPs** | Usar apenas os 30 BIPs e 270 execuções já existentes |
| **Sem novo experimento** | Análises offline nos dados congelados (CSV, matriz, seeds) |
| **Locks intocáveis** | GO-8D-NC Lock, C2, C3, DV3, pré-registro permanecem congelados |
| **Sem viés de confirmação** | Critérios de decisão pré-definidos para H1/H2/H3 |

### 4.2 Decomposição Pré-especificada da DV3

A DV3 = clamp((conf + ged_ecp + ent_n12) / 3). Investigar cada componente separadamente:

| Componente | Definição | Pergunta Diagnóstica |
|------------|-----------|----------------------|
| **conf** | Confiança média de classificação | C3 reduz a confiança das classificações? |
| **ged_ecp** | Similituded ao grafo ECP canônico (CAT) | ged_ecp penaliza categorias SYN (C3) por construção? |
| **ent_n12** | Entropia normalizada log(12) de categorias | C3 aumenta diversidade (SYN + CAT) mas ent_n12 penaliza dispersão? |

**Entregável:** Tabela 30 × 3 × 3 componentes (conf, ged_ecp, ent_n12) por BIP × condição × réplica.

### 4.3 Validação Independente dos Componentes

| Componente | Método de Validação | Critério de Sucesso |
|------------|---------------------|---------------------|
| **conf** | Comparar com acurácia contra anotação ouro (se disponível) ou consistência interna bootstrap | Correlação com qualidade percebida |
| **ged_ecp** | Testar com referência neutra (não ECP) e com grafo SYN | Verificar se viés CAT é inerente |
| **ent_n12** | Simular métricas de diversidade alternativas (Shannon, Simpson, riqueza) | Verificar se ent_n12 é adequada |

### 4.4 Testes Sintéticos de Comportamento da Métrica

| Teste | Descrição | Hipótese Alvo |
|-------|-----------|---------------|
| **TS-1: Referência Neutra** | Substituir `ged_ecp` (referência ECP) por `ged_syn` (referência SYN) e `ged_union` (referência união). Recalcular DV3. | H2: se DV3 inverte ordem, ged_ecp é viés CAT |
| **TS-2: Pesos Variados** | Variar pesos (w1, w2, w3) em grid {0.5, 1, 2} × {0.5, 1, 2} × {0.5, 1, 2} normalizados. Observar estabilidade da ordem A > B > C. | H3: se ordem inverte com pesos, efeito é mascarado por média 1:1:1 |
| **TS-3: Métrica Sem Compressão** | Usar média geométrica ou harmônica em vez de aritmética. Testar DV3* = (conf^w1 × ged_ecp^w2 × ent_n12^w3)^(1/3). | H3: se média geométrica inverte, componentes interagem não-linearmente |
| **TS-4: Contrafactual C3** | Gerar reconstruções sintéticas onde C3 é "perfeito" (mapeamento 1:1 CAT→SYN) vs "ruidoso". Testar sensibilidade. | H1: se DV3 ainda cai com C3 perfeito, métrica é problemática |

### 4.5 Critérios Prévios para Evidência

| Hipótese | Evidência Forte (≥2) | Evidência Moderada (1) | Evidência Fraca (0) |
|----------|---------------------|------------------------|---------------------|
| **H1** | Queda concentrada em ged_ecp/conf com validação externa; TS-1/TS-4 não invertem | Queda em ≥2 componentes; TS-1 inverte parcialmente | Queda apenas em ent_n12; TS-1 inverte |
| **H2** | TS-1 inverte ordem A/B; queda concentrada em ged_ecp (viés CAT); TS-1 inverte totalmente | TS-1 inverte parcialmente; queda em ged_ecp sem validação | Queda apenas em ent_n12; TS-1 não inverte |
| **H3** | Componentes mostram sinais opostos (ex.: conf ↑, ged_ecp ↓); TS-2/TS-3 invertem ordem | Sinais opostos em ≥1 BIP; TS-2 inverte | Sinais opostos apenas em agregado |

**Regra de Decisão:** Hipótese com maior pontuação (≥4/6 evidências fortes/moderadas) vence. Empate → H3 (mais conservadora).

---

## 4.6 Cronograma e Entregáveis

| Etapa | Atividade | Prazo | Responsável |
|-------|-----------|-------|-------------|
| 1 | Extração de componentes (conf, ged_ecp, ent_n12) dos 270 outputs | Semana 1 | Equipe técnica |
| 2 | Análise descritiva e testes de sinal por componente | Semana 1-2 | Estatístico |
| 3 | Testes sintéticos TS-1 a TS-4 | Semana 2 | Equipe técnica |
| 4 | Validação independente (bootstrap, simulação) | Semana 2-3 | Estatístico |
| 5 | Aplicação de critérios de decisão H1/H2/H3 | Semana 3 | Líder técnico |
| 6 | Relatório diagnóstico final | Semana 3 | Líder técnico |

**Entregável Final:** `DIAGNOSTIC-REPORT-GO8E-01.md` com conclusão H1/H2/H3 e recomendação.

---

## 5. Decisão Explícita sobre Métrica DV3

Com base no diagnóstico, a proposta deve incluir **uma das três recomendações**:

| Resultado Diagnóstico | Recomendação |
|----------------------|--------------|
| **H1 confirmada** | Manter DV3; investigar melhoria real em GO-8E com nova hipótese |
| **H2 confirmada** | **Substituir DV3** por métrica sem viés CAT (ex.: DV4 com referência neutra + pesos otimizados) |
| **H3 confirmada** | **Decompor DV3** em componentes reportados separadamente; não usar média composta |

> **Regra de Ouro:** NÃO usar o resultado A > B para escolher a métrica. A decisão sobre DV3 deve basear-se **exclusivamente** na evidência diagnóstica da decomposição e testes sintéticos.

---

## 6. Regras de Governança (Reafirmadas)

| Proibição | Status |
|-----------|--------|
| Usar resultado A > B para escolher métrica | **PROIBIDO** |
| Coletar novos BIPs | **PROIBIDO** |
| Executar experimento (GO-8E) | **PROIBIDO** — apenas diagnóstico |
| Alterar Locks anteriores (GO-8D-NC, C2, C3, DV3) | **PROIBIDO** |
| Abrir GO-8E formalmente | **PROIBIDO** — requer nova autorização após diagnóstico |

---

## 7. Relatório de Decisão de Governança

### Resumo da Proposta

| Item | Detalhe |
|------|---------|
| **Documento** | `D-GO8E-01-PROPOSAL.md` |
| **Pergunta Central** | "Por que C3 reduz a DV3? Perda real ou limitação da métrica?" |
| **Hipóteses** | H1 (efeito real), H2 (artefato DV3), H3 (interação) |
| **Metodologia** | Decomposição DV3 + testes sintéticos + validação independente — **sem novos dados** |
| **Critérios de Decisão** | Pré-especificados, baseados em evidência de decomposição e testes sintéticos |
| **Resultado Esperado** | Recomendação: manter DV3, substituir DV3, ou decompor DV3 |
| **Próximo Passo** | Aguardar autorização de governança para execução do diagnóstico (não GO-8E) |

### Recomendação de Governança

> **RECOMENDAÇÃO:** Autorizar a execução do plano diagnóstico D-GO8E-01 (sem abrir GO-8E). O diagnóstico é pré-requisito para qualquer decisão informada sobre GO-8E. O resultado dirá se:
>
> 1. **H1** → Prosseguir para GO-8E com hipótese de melhoria real
> 2. **H2** → Redesenhar métrica antes de qualquer GO-8E
> 3. **H3** → Reportar componentes separadamente; repensar métrica composta

---

## 8. Arquivos Relacionados

| Arquivo | Descrição |
|---------|-----------|
| `CLOSURE-DECISION-GO-8D-NC.md` | Contexto de encerramento GO-8D-NC |
| `STATISTICAL-REPORT-GO-8D-NC.md` | Resultados estatísticos completos |
| `AUDIT-REPRODUCTION.md` | Auditoria de reprodução |
| `AUDIT-PREREG-ADHERENCE.md` | Auditoria de aderência ao pré-registro |
| `INTERPRETATION-GOVERNANCE.md` | Interpretação oficial limitada a DV3 |
| `GO-8D-NC-LOCK-MANIFEST.yaml` | Lock manifesto (SHA-256: `9247abcc...`) |

---

**Caminho da Proposta:** `D:\ecp-spec\experiments\validation\GO-8D-NC\D-GO8E-01-PROPOSAL.md`

**Assinatura:** Proposta Diagnóstica GO-8E  
**Data:** 2026-08-15  
**Lock Manifest:** `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`