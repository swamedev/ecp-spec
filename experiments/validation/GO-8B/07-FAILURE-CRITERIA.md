# GO-8B Entregável 7 — Critérios Formais de Falha / Exclusão Automática

**Status:** REVISED — PENDING GOVERNANCE AUDIT
**Revisão:** R1 (aplicação do Decision Record 00-GO-8B-R1) + R3 (R2-C5)
**Data original:** 2026-08-10
**Objetivo:** Definir regras determinísticas, auditáveis e **não negociáveis** para exclusão automática de casos, avaliadores, reconstruções ou do piloto inteiro. Sem discrição humana no momento da execução.
**Princípio:** "O protocolo decide; o executor apenas aplica."

**Exigência R1 (Correção 10):** cada critério deve ser **objetivo, determinístico, reproduzível e verificável por código ou regra documental explícita**. Cada critério registra: `ID → condição → ação → justificativa → momento de aplicação`. Nenhum critério pode ser adaptado após observar resultados. Thresholds sem justificativa suficiente são marcados `PRE-SPECIFICATION DEBT` — não se finge fundamento empírico.

---

## 1. Taxonomia de Falhas (Níveis de Gravidade)

| Nível | Código | Escopo | Consequência |
|---|---|---|---|
| **CRÍTICO** | `FAIL-PILOT` | Piloto inteiro | **PARAR GO-8B**; escalar para coordenação; não prosseguir |
| **BLOQUEANTE** | `FAIL-CASE` | Caso individual (SX-###) | Excluir caso do piloto; registrar; continuar com demais |
| **BLOQUEANTE** | `FAIL-EVALUATOR` | Avaliador individual | Excluir avaliador; redistribuir carga; continuar |
| **BLOQUEANTE** | `FAIL-RECON` | Reconstrução individual | Marcar como inválida; não entra na análise estatística |
| **AVISO** | `WARN-*` | Qualidade degradada | Registrar no log; não exclui automaticamente; revisar pós-hoc |

**Formato padrão de todo critério (R1):**

```
ID → condição (avaliação automática) → ação → justificativa → momento de aplicação
```

---

## 2. Falhas Críticas do Piloto (FAIL-PILOT)

| ID | Condição (Automática) | Detecção | Ação | Justificativa | Momento de Aplicação |
|---|---|---|---|---|---|
| **FP-01** | **< 4 casos elegíveis** após verificação de fontes | Contagem de casos com status `SELECTABLE` e fontes confirmadas | PARAR; revisar SX-CANDIDATES; não executar | N mínimo pré-definido pelo protocolo de seleção | Antes da execução |
| **FP-02** | **Diversidade insuficiente**: < 4 domínios distintos entre casos SELECTABLE | Contagem de domínios únicos (RA-DI-003) | PARAR | DDS mínimo pré-registrado (P-0007.1) | Antes da execução |
| **FP-03** | **Taxonomia C3 REJEITADA** no BIP-VAL | `BIP-VAL_REPORT.yaml: verdict = REJECTED` | PARAR; nova geração cega | C3 deve ser independente do ECP (Entregável 3) | Antes da execução |
| **FP-04** | **Mapping C2 inválido**: seed não reproduz permutação, ou mapping não bijetivo | Testes T-C2-01..05 falham | PARAR; corrigir seed/algoritmo | Integridade do mecanismo de cegueira | Antes da execução |
| **FP-05** | **GraphFromReconstruction falha em > 50% dos casos-teste unitários** (T-GFR-01..21) | Suite de testes unitários (CI) | PARAR | Contrato do parser deve ser confiável (Entregável 4) | Antes da execução |
| **FP-06** | **WL Kernel falha em testes de sanidade** (T-WL-01..12) | Suite de testes unitários (CI) | PARAR | Métrica comparativa deve ser determinística (Entregável 5) | Antes da execução |
| **FP-07** | **Violação de cegueira confirmada**: avaliador acessou narrativa oficial antes da reconstrução | Auditoria de logs / declaração assinada | PARAR; caso comprometido; investigar | Regra de cegueira é inegociável | Durante/pós reconstrução |
| **FP-08** | **Conflito de interesse não declarado**: autor do ECP participou como avaliador/executor | Verificação de afiliações (auto-declaração + checagem) | PARAR; exclusão imediata | Independência metodológica | Antes e durante execução |

---

## 3. Falhas de Caso (FAIL-CASE) — Exclusão Automática de SX-###

| ID | Condição (Automática) | Detecção | Ação | Justificativa | Momento de Aplicação |
|---|---|---|---|---|---|
| **FC-01** | **Fontes inacessíveis**: ≥ 1 fonte primária declarada retorna 404/paywall sem alternativa | Script de verificação HTTP (HEAD) + cache | Excluir caso; registrar em `CASE_EXCLUSION_LOG` | Evidência pública é requisito (SC-2) | Antes da execução |
| **FC-02** | **EC-1 detectado post-hoc**: núcleo é engenharia de software | Análise de Atomic Facts: > 50% AFs referenciam código/API/framework | Excluir caso; registrar (contaminação SX-001) | Risco de contaminação ECP | Pós Atomic Facts |
| **FC-03** | **EC-4 confirmado**: narrativa única incontestada | Análise de proveniência: ≥ 80% AFs derivam de 1 origem causal (RA-EI-002) | Excluir caso; registrar | Requisito multi-origem (SC-5) | Pós Atomic Facts |
| **FC-04** | **SC-3 ou SC-4 = Não** na reavaliação final | Re-auditoria final (SX-REAUDIT v2) | Excluir caso; registrar | Critérios obrigatórios do protocolo | Pós seleção |
| **FC-05** | **Caso duplicado de domínio já selecionado** (viola DDS mínimo) | Verificação de domínio taxonômico | Excluir caso; protocolo escolhe próximo no ranking | Diversidade pré-registrada | Antes da execução |
| **FC-06** | **Atomic Facts < 15** para o caso | Contagem de AFs na narrativa original | Excluir caso; registrar | Granularidade mínima de evidência — **PRE-SPECIFICATION DEBT** (limiar baseado em SX-001; sem fundamento empírico formal) | Pós Atomic Facts |
| **FC-07** | **Reconstrução cega não produzida** (avaliador não entregou no prazo) | Ausência de arquivo `reconstruction/03-reconstrucao-cega.md` | Excluir caso; redistribuir se tempo | Completude de dados | Pós prazo de reconstrução |

---

## 4. Falhas de Avaliador (FAIL-EVALUATOR)

| ID | Condição (Automática) | Detecção | Ação | Justificativa | Momento de Aplicação |
|---|---|---|---|---|---|
| **FE-01** | **Taxa de completude < 80%**: avaliador não entregou ≥ 2 de 3 condições (A, B, C) | Contagem de entregas por avaliador | Excluir avaliador; redistribuir casos pendentes | Completude pré-definida | Pós coleta |
| **FE-02** | **Violação de cegueira** | Log de acesso a narrativa oficial antes de reconstrução; ou declaração | Excluir avaliador; **todos os seus dados** marcados `COMPROMISED` | Cegueira é inegociável | Durante/pós reconstrução |
| **FE-03** | **Tempo de resposta anômalo**: reconstrução em < 10% do tempo mediano dos demais | Análise de timestamps | Flag `WARN-SPEED`; revisar qualidade; **não** exclui automaticamente | Sinal de qualidade, não falha objetiva | Pós coleta |
| **FE-04** | **ICC < 0.40** com demais avaliadores | ICC two-way random, absolute agreement | Flag `WARN-ICC`; não exclui; reportar no DISCOVERY-LOG | **PRE-SPECIFICATION DEBT** — limiar heurístico sem fundamento formal | Pós coleta |
| **FE-05** | **Conflito de interesse descoberto post-hoc** | Verificação de afiliações / publicações prévias sobre o caso | Excluir avaliador; dados marcados `COMPROMISED` | Independência metodológica | Pós coleta |

---

## 5. Falhas de Reconstrução Individual (FAIL-RECON) — Por Unidade (Caso, Condição)

Unidade de análise por **BIP/Caso**; seeds/avaliadores são repetições intra-unidade (Entregável 6 §1.3; **3 seeds por célula pré-especificadas — R5 M-3**). Os critérios abaixo aplicam-se a cada reconstrução individual antes da agregação por mediana.

| ID | Condição (Automática) | Detecção | Ação | Justificativa | Momento de Aplicação |
|---|---|---|---|---|---|
| **FR-01** | **Schema inválido**: `ReconstructionInput` falha validação JSON | Validador automático (`jsonschema`) | Marcar `INVALID`; não entra no GraphFromReconstruction | Contrato orientado a schema (Entregável 4) | Imediata pós-reconstrução |
| **FR-02** | **Reconstrução vazia no nível de coleção**: array `entities` vazio **OU** array `relations` vazio | Contagem de arrays após desserialização | Marcar `EMPTY`; não entra na análise | Reconstrução sem conteúdo é inválida | Imediata pós-reconstrução |
| **FR-03** | **Violação de schema no nível de registro**: algum `entity`/`relation` individual viola o schema (ex.: `syn_category` fora do namespace declarado `taxonomy_namespace`, `confidence` fora de [0,1], **mistura de dois ou mais namespaces distintos** (`ECP`/`CAT`/`SYN`/`NULL`) → `NAMESPACE_MIX`, ids fora do padrão, ausência do campo obrigatório `taxonomy_namespace`) | Validação automática por item (`jsonschema` por registro) | Marcar `SCHEMA_VIOLATION`; excluir | Contrato orientado por schema (Entregável 4); namespace é local da condição (R3-01 + R5 M-1) | Imediata pós-reconstrução |
| **FR-04** | **Entidades sem `source_af_ids`** (rastreabilidade quebrada) | Verificação de `entities[].source_af_ids` non-empty | Marcar `UNTRACEABLE`; flagged | Rastreabilidade evidência→entidade | Imediata pós-reconstrução |
| **FR-05** | **S_struct = NaN / None / erro de computação** | Try/except no pipeline WL | Marcar `ERROR`; excluir da análise estatística | Integridade da métrica | Durante análise |
| **FR-06** | **Reconstrução incompleta** (campos obrigatórios ausentes) | Validação automática | Marcar `INVALID`; não entra | Completude do registro | Imediata pós-reconstrução |

**Nota R1:** critérios baseados em "taxa de mapeamento SYN→ECP" e em "cobertura de categorias ECP" foram **removidos** — o parser não contém mapeamento C3→ECP (Entregável 4) e a compatibilidade ECP não é penalidade estrutural (Entregável 5).

**Distinção operacional FR-02 × FR-03 (R2-C5):** FR-02 atua no **nível de coleção** (arrays vazios = reconstrução sem conteúdo) e é verificado imediatamente após a desserialização, antes de qualquer validação por item. FR-03 atua no **nível de registro** (cada `entity`/`relation` individual violando o schema, incluindo mistura de namespace `CAT-XX`+`SYN-XXX`). A ordem de aplicação é: desserializar → FR-02 (coleção) → FR-01/FR-03 (validação por item) → FR-04 (rastreabilidade).

---

## 6. Regras de Agregação e Decisão Final (Por Caso)

Para cada caso SX-###, após todas as reconstruções válidas por condição:

```
Unidade experimental = BIP/Caso.
Para cada (caso, condição): mediana das 3 seeds/reconstruções válidas (R5 M-3) → 1 observação.

SE (reconstruções válidas por condição) < 1 PARA QUALQUER condição:
    → CASO EXCLUÍDO (insuficiência de dados) — FAIL-CASE implícito

SE (observações válidas por condição, após agregação) < 3:
    → CASO EXCLUÍDO — FAIL-CASE implícito (Friedman exige todas as colunas preenchidas)

SE caso NÃO excluído:
    → S_struct por condição = mediana (per Entregável 6)
    → Entrar na análise estatística (N = nº de BIPs válidos)
```

---

## 7. Registro de Exclusões (Audit Trail)

Toda exclusão automática gera entrada em `EXCLUSION_LOG.yaml`:

```yaml
- exclusion_id: EXC-001
  timestamp: "<pendente>"
  level: FAIL-CASE
  rule_id: FC-01
  target: "SX-003"
  details: "Fonte primária inacessível (404); sem alternativa"
  automatic: true
  reviewer: "system"
  data_snapshot: {case_id: "SX-003", sources_checked: 5, accessible: 4}
```

**Regra:** Nenhuma exclusão manual. Todas automáticas via regras acima.  
Revisão humana **apenas** para confirmar que a regra foi aplicada corretamente (auditoria), não para decidir.

---

## 8. Critérios de Sucesso Mínimo do Piloto (Go/No-Go para Análise)

O piloto GO-8B **prossegue para análise estatística** se e somente se:

| Critério | Limiar | Justificativa |
|---|---|---|
| Casos válidos (não excluídos) | **≥ 5** de 7 | Mínimo para Friedman com 3 colunas; **PRE-SPECIFICATION DEBT** — limiar heurístico |
| Domínios distintos representados | **≥ 4** | DDS (P-0007.1) |
| Observações válidas por condição (após agregação) | **= N_casos válidos** | Friedman exige matriz completa N×3 |
| Nenhum `FAIL-PILOT` disparado | — | Regras §§2 determinísticas |

**Se falhar:** Relatório final = "PILOT INCONCLUSIVE — insufficient data"; não executar análise estatística; escalar para coordenação.

---

## 9. Dívida Metodológica Conhecida (Exclusão)

| Item | Descrição | Decisão GO-8B |
|---|---|---|
| **DEBT-EXC-01** | Limiares (ex.: 15 AFs — FC-06; ICC 0.40 — FE-04; ≥5 casos — §8) são heurísticos | Marcados `PRE-SPECIFICATION DEBT`; **não** ajustados post hoc; revisão em versão futura |
| **DEBT-EXC-02** | Exclusão por ICC baixo não é automática | Mantido como `WARN`; exclusão só por violação objetiva (FE-01, FE-02, FE-05) |
| **DEBT-EXC-03** | Caso com domínio duplicado (FC-05) — ranking pode não refletir diversidade real | Ranking pré-registrado é a regra; não há discrição |
| **DEBT-EXC-04** | Critérios que dependiam de mapeamento SYN→ECP removidos | Substituídos por validação orientada a schema (FR-03/FR-06) |

---

## GO-8B CHANGE LOG

### GO-8B-R1 (aplicado)
- Decision Record: 00-GO-8B-R1-DECISION-RECORD.md
- Revisão: R1
- Alterações principais:
  - Cada critério reformulado no formato `ID → condição → ação → justificativa → momento de aplicação`.
  - Thresholds sem fundamento empírico formal marcados `PRE-SPECIFICATION DEBT` (FC-06, FE-04, ≥5 casos).
  - Removidos critérios baseados em "taxa de mapeamento SYN→ECP" e "cobertura de categorias ECP" (incompatíveis com Correção 2/3: parser neutro, S_struct sem ECP).
  - Regras de agregação alinhadas à unidade experimental BIP/Caso (mediana, N = BIPs válidos).
  - Proibida adaptação de critérios após observar resultados.
- Alterações metodológicas:
  - Exclusão tornada 100% determinística e verificável; nenhuma discrição em execução.
- Itens ainda pendentes:
  - Justificativa formal para os limites marcados `PRE-SPECIFICATION DEBT` (ou aceitação explícita).

### GO-8B-R3 (aplicado — R2-C5)
- **R2-C5:** FR-02 e FR-03 diferenciados operacionalmente: FR-02 = nível de coleção (arrays vazios, `EMPTY`), FR-03 = nível de registro (violação por item, incluindo mistura de namespace `NAMESPACE_MIX`); ordem de aplicação definida na Nota R1.
- FR-03 incorpora a validação de namespace local (DECISION R3-01, Entregável 4): `syn_category` deve pertencer ao `taxonomy_namespace` declarado.
- Status: REVISED — PENDING GOVERNANCE AUDIT

### GO-8B-R5 (aplicado — M-1, GO-8B-R5)
- FP-05 atualizado para a suite completa de testes T-GFR-01..21.
- FR-03 generalizado: mistura de **dois ou mais namespaces distintos** (`ECP`/`CAT`/`SYN`/`NULL`) → `NAMESPACE_MIX`; ausência do campo obrigatório `taxonomy_namespace` → violação de schema (R5 M-1).
- Status: REVISED — PENDING GOVERNANCE AUDIT
