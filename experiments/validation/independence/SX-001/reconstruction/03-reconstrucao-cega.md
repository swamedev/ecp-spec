# SX-001 / reconstruction — Etapa 3: Reconstrução Cega

| Campo | Valor |
|---|---|
| **Experimento** | EXP-SX001 |
| **Etapa** | 3 — Reconstrução Cega |
| **Entrada** | **Somente** [02-atomic-facts.md](./02-atomic-facts.md) + Kernel ECP-000..ECP-009 |
| **Proibido** | Consultar a [narrativa original](../narrative/01-narrativa-original.md) durante a reconstrução |
| **Data** | 2026-08-03 |

> **Protocolo de reconstrução:** (1) ler os Atomic Facts; (2) para cada fato,
> perguntar *"que papel esse fato desempenha na estrutura do evento?"*; (3)
> reconhecer uma entidade **somente quando** existir suporte factual direto
> (`AF-###`); (4) marcar como **inferida** qualquer categoria que exija
> interpretação sem suporte direto; (5) registrar **ausências** (entidades que
> o Kernel prediz e que não aparecem).

---

## 0. Declaração de cegueira

Esta reconstrução foi produzida **antes** de reler a Narrativa Original. As
entidades abaixo foram reconhecidas a partir dos **46 Atomic Facts** e do Kernel.
Onde o rótulo ECP não era claramente suportado pelos fatos, foi marcado como
**inferido** — e **não conta** como emergência espontânea.

> **Limitação de execução (registrada):** a reconstrução e a narrativa foram
> produzidas pelo mesmo executor (North Mini Code). A separação ideal (Pessoa A
> reconstrói, Pessoa B compara) não pôde ser aplicada nesta sessão. Para mitigar,
> a reconstrução cita **apenas** `AF-###`, nunca a narrativa. A limitação é
> registrada em [METHODOLOGICAL-DEBT.md](../../METHODOLOGICAL-DEBT.md).

## 1. Reconhecimento de entidades

### 1.1 Goal (Objetivo) — EMERGENTE

| Suporte | Fato |
|---|---|
| AF-007 | Missão STS-51-L: 25º voo do programa, 10º da Challenger. |
| AF-008 | Plano: implantar satélite, observar Halley, levar McAuliffe. |

O objetivo da missão **emerge diretamente dos fatos**: um estado desejado
observável (colocar carga e pessoas em órbita, executar o plano científico).
Não exigiu interpretação.

### 1.2 Knowledge (Conhecimento) — EMERGENTE

| Suporte | Fato |
|---|---|
| AF-001 | 1977 — dados de teste indicaram possibilidade de falha das vedações. |
| AF-002 | 1985 — erosão de O-ring em quase todos os voos. |
| AF-003 | STS-51-C: erosão nos O-rings primários de ambos os SRBs. |
| AF-004 | STS-51-B: erosão nos O-rings primário e secundário. |
| AF-005 | Memorando interno: falha poderia ser "catástrofe da mais alta ordem". |
| AF-006 | Cascos reprojetados encomendados para o ano seguinte. |

O conhecimento técnico sobre o defeito das vedações **existia e estava
registrado** antes do lançamento. Emergente.

### 1.3 Knowledge negativo (lacuna) — EMERGENTE

| Suporte | Fato |
|---|---|
| AF-018 | Engenheiros: sem dados suficientes para garantir selagem abaixo de 53 °F. |

A **lacuna** (não se sabe) emerge: os próprios engenheiros declaram o limite do
conhecimento. Isto é reconhecido pelo Kernel como conhecimento-negativo
(ECP-006: classificar o que se sabe e o que não se sabe).

### 1.4 Assumption (Suposição) — EMERGENTE

| Suporte | Fato |
|---|---|
| AF-022 | Após reunião privada: "as evidências eram inconclusivas" e "havia margem substancial mesmo em caso de erosão". |
| AF-029 | Engenheiros consultados: "o gelo não ameaçava a segurança". |
| AF-027 | Temperatura dos SRBs medida, não comunicada: tratada como irrelevante. |

Três suposições emergem dos fatos, todas **tratadas como verdadeiras sem
evidência plena**:
- **A-1** — "as evidências são inconclusivas" (portanto pode-se lançar);
- **A-2** — "há margem substancial de segurança mesmo com erosão";
- **A-3** — "o frio/gelo não invalida a operação".

É exatamente a definição de suposição em ECP-007: afirmação tratada como
verdadeira sem evidência plena, **registrada e monitorada** (aqui: registrada na
conversa, mas rejeitada).

### 1.5 Evidence (Evidência) — EMERGENTE (e a falta dela)

| Suporte | Fato |
|---|---|
| AF-018 | Engenheiros sem dados suficientes (ausência de evidência para decidir). |
| AF-032 | Fumaça negra na junta após ignição (observação em voo). |
| AF-034 | Wind shear em altitude (observação). |
| AF-035 | Pluma de chama no SRB direito (observação). |

A evidência emerge em duas formas: a **ausência** de evidência para a decisão
pré-voo (AF-018) e as **observações em voo** (AF-032, AF-034, AF-035). O Kernel
prevê: decisão de avanço exige evidência suficiente (ECP-008) — e aqui a decisão
de lançar foi tomada **sem** ela.

### 1.6 Decision (Decisão) — EMERGENTE

| Suporte | Fato |
|---|---|
| AF-019 | Recomendação de não lançar abaixo de 53 °F (decisão da engenharia). |
| AF-022 | Mudança de posição: recomendar lançar (decisão da gerência). |
| AF-024 | NASA exige recomendação por escrito; Kilminster assina (decisão). |
| AF-025 | Mulloy não menciona os O-rings a Aldrich (decisão de omitir). |
| AF-030 | Aldrich decide prosseguir apesar do gelo (decisão). |
| AF-015 | Lançamento às 11h38 (decisão de executar). |

Seis decisões emergem dos fatos, formando uma **cadeia de decisões**: engenharia
recomenda não lançar → gerência reverte → NASA exige confirmação → confirmação
assinada → informação crítica não transmitida → prossegue-se → executa-se.

### 1.7 Risk (Risco) — INFERIDO (limiar)

O Kernel prevê risco = impacto × probabilidade (ECP-008). Os fatos contêm a
matéria-prima: AF-005 ("catástrofe da mais alta ordem" — impacto), AF-016/017/018
(frio — probabilidade). Mas **nenhum fato** registra um cálculo de risco
explícito pelos participantes. O risco como entidade **não emerge como
artefato**; ele **emerge como ausência** — o cálculo que deveria ter sido feito
não aparece nos fatos. → Marcado como **ausência** (ver §3).

### 1.8 Problem (Problema) — NÃO EMERGE diretamente

O Kernel começa por Problem (causa raiz). Os fatos **não registram** a causa
raiz do projeto ("por que a NASA faz missões espaciais?"). A missão existe
(AF-007) e o plano existe (AF-008), mas a causa-raiz **não é declarada nos
fatos coletados**. → O Problem **não emerge dos Atomic Facts**; seria preciso
contexto externo. Marcado como **ausência no traço observado** (ver §3).

## 2. A cadeia reconstruída

Reunindo apenas o que emergiu dos fatos:

```
Goal (AF-008 — missão planejada)
  ↓
Knowledge (AF-001..006 — defeito conhecido) + lacuna (AF-018)
  ↓
Assumption (A-1, A-2, A-3 — evidência inconclusiva / margem / frio ok)
  ↓
Evidence (ausente na decisão pré-voo — AF-018; observada em voo — AF-032/034/035)
  ↓
Decision (AF-019 → AF-022 → AF-024 → AF-025 → AF-030 → AF-015)
  ↓
Execution (AF-015, AF-031)
  ↓
Validation (falha — AF-010/011, AF-036)
  ↓
Learning (AF-037..046 — investigação, suspensão, reprojeto)
```

**Observação central da reconstrução:** a cadeia emerge com um **elo
quebrado** no ponto `Evidence → Decision`. O Kernel diz que decisão de avanço
exige evidência suficiente (L-0, ECP-008). Os fatos mostram a decisão de lançar
tomada **apesar da ausência de evidência** (AF-018) e **com base em suposições**
(A-1, A-2, A-3). A reconstrução — sem nunca ter lido o relatório oficial —
detecta que o evento falhou **exatamente no elo que o Kernel considera
obrigatório**.

## 3. Ausências (negative evidence)

Entidades que o Kernel prevê e que **não aparecem** nos fatos:

| Entidade | Status nos fatos | Leitura |
|---|---|---|
| **Problem** | Não declarado | A causa raiz do programa não emerge; só a missão. |
| **Risk** | Não calculado | Impacto conhecido (AF-005), mas nenhum cálculo registrado. |
| **Validação pré-decisão** | Ausente | Nenhuma validação de que as vedações selariam a 36 °F. |
| **Registro de decisão completo** | Ausente | AF-045: reuniões-chave não gravadas; AF-025: informação omitida. |

Estas ausências são **dados** (regra 4 do SHADOW-EXPERIMENTS): o Kernel prediz
que um projeto bem conduzido teria Problem, Risk, Validação e Registro — e aqui
eles não aparecem no traço.

## 4. O que a reconstrução NÃO conseguiu (limites)

- **Não identificou a causa técnica exata** (a qual junta, a qual O-ring, a
  sequência física da falha) a partir dos fatos — isso exigiria análise de
  engenharia física (AF-037 pertence ao registro da investigação, não à
  reconstrução).
- **Não reconstruiu o relato dos decisores** (por que Mulloy/Hardy reagiram
  assim), pois o motivo não está nos fatos.

## 5. Resumo da Etapa 3

| Entidade | Emergência | Suporte |
|---|---|---|
| Goal | **Emergente** | AF-007, AF-008 |
| Knowledge | **Emergente** | AF-001..006 |
| Lacuna de conhecimento | **Emergente** | AF-018 |
| Assumption | **Emergente** | AF-022, AF-027, AF-029 |
| Evidence | **Emergente** | AF-018, AF-032, AF-034, AF-035 |
| Decision | **Emergente** | AF-019, AF-022, AF-024, AF-025, AF-030, AF-015 |
| Problem | Não emerge | — |
| Risk | Não emerge (só matéria-prima) | AF-005, AF-016..018 |
| Cadeia Goal→…→Decision→…→Learning | **Emerge** (com elo Evidence→Decision quebrado) | §2 |

> **Veredito preliminar da reconstrução cega:** a estrutura central do ECP —
> Goal, Knowledge, Lacuna, Assumption, Evidence, Decision e a cadeia até
> Validation/Learning — **emergiu dos fatos sem uso do vocabulário ECP na
> coleta**. As entidades ausentes (Problem, Risk calculado) e o elo quebrado
> também foram detectados. Este é o dado bruto para a Etapa 4.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Reconstrução cega a partir dos 46 Atomic Facts + Kernel. Emergência: Goal/Knowledge/Assumption/Evidence/Decision. Ausências: Problem, Risk, validação, registro. |
