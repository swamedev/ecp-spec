# SX-003 / comparison — Etapa 4: Alignment Analysis

| Campo | Valor |
|---|---|
| **Experimento** | EXP-SX003 |
| **Etapa** | 4 — Alignment Analysis |
| **Compara** | [Narrativa Original](../narrative/01-narrativa-original.md) × [Reconstrução Cega](../reconstruction/03-reconstrucao-cega.md) |
| **Categorias** | `MATCH` \| `PARTIAL_MATCH` \| `NOT_EXPLAINED` \| `NEW_INSIGHT` |
| **Data** | 2026-08-09 |

> **Pergunta central desta etapa:** a reconstrução cega — que usou **apenas** os
> Atomic Facts + Kernel, sem o vocabulário ECP na coleta e sem consultar a
> narrativa histórica — reproduz a estrutura do evento que a narrativa descreve?
> E explica algo que a narrativa não dizia?

> **Especial para o SX-003:** é um caso de **sucesso**. A pergunta reversa da
> DEBT-009 não é feita aqui (é da revisão pós-experimento); aqui a própria
> comparação só registra o que emergiu.

## Categorias

| Categoria | Definição |
|---|---|
| `MATCH` | A reconstrução reproduz fielmente o que a narrativa descreve, sem acréscimo nem perda. |
| `PARTIAL_MATCH` | Concorda parcialmente: há coincidência estrutural, mas omitiu ou acrescentou um aspecto. |
| `NOT_EXPLAINED` | O elemento está na narrativa, mas a reconstrução não o alcança (nem acerta nem erra). |
| `NEW_INSIGHT` | A reconstrução diz algo que a narrativa não dizia — surpresa ou explicação nova. |

## Perguntas estruturantes (do plano)

- **Apareceu algo novo?** → `NEW_INSIGHT`
- **Perdeu informação?** → falha de `MATCH`/`PARTIAL_MATCH`
- **Inventou algo?** → item que a narrativa não contém (falso positivo)
- **Condensou?** → `PARTIAL_MATCH` (reconstruiu menos que a narrativa)
- **Generalizou?** → `NEW_INSIGHT` se explicou além; senão `PARTIAL_MATCH`

---

## Tabela de alinhamento

| # | Elemento (da narrativa ou da reconstrução) | Reconstrução | Categoria |
|---|---|---|---|
| 1 | HGP: esforço internacional; primeira sequência (AF-001) | Goal emergente | **MATCH** |
| 2 | Período 1990–2003, 13 anos (AF-002/003) | Execution/contexto (não entidade) | **PARTIAL_MATCH** |
| 3 | Coordenado por DOE/NIH (AF-004) | Contexto institucional (Knowledge) | **PARTIAL_MATCH** |
| 4 | Comitê da NAS define objetivos em 1988 (AF-005/006) | Problem ex-ante + Goal | **MATCH** |
| 5 | Organismos-alvo: E. coli, levedura, etc. (AF-010) | Knowledge (escopo) | **MATCH** |
| 6 | Custo ~US$3 bi e prazo 15 anos (AF-011/012) | Projection + meta temporal | **MATCH** |
| 7 | Plano estratégico atualizado (AF-013) | Não citado como entidade | **NOT_EXPLAINED** |
| 8 | 20 centros em 6 países (AF-014/015) | Execution (organização) | **MATCH** |
| 9 | IHGSC surgiu como consórcio-sequenciador (AF-016/017) | Execution (estrutura) | **MATCH** |
| 10 | Financiamento público + Wellcome + etc. (AF-018..020) | Knowledge/contexto | **PARTIAL_MATCH** |
| 11 | Celera entrou na corrida (AF-021) | Contexto competitivo (Execution) | **PARTIAL_MATCH** |
| 12 | Celera: mais rápido/barato, shotgun, Venter (AF-022..025) | Assumptions A-2 | **MATCH** |
| 13 | Corrida público×privado acelerou decisões (AF-026) | Interpretado como context; não explícito | **PARTIAL_MATCH** |
| 14 | Bermuda Principles 1996 (AF-027..029) | Decision (compartilhar) | **MATCH** |
| 15 | Compartilhamento imediato e legado (AF-030/031) | Execution + Learning (parcial) | **PARTIAL_MATCH** |
| 16 | Questões éticas/sociais (seguros, emprego) (AF-032/033) | Matéria-prima de risco social | **PARTIAL_MATCH** |
| 17 | Programa ELSI e mandato de 5% (AF-034/035) | Decision (governança ética) | **MATCH** |
| 18 | Draft em jun/2000 na Casa Branca (AF-036/037/038) | Evidence de resultado (90%, gaps) | **MATCH** |
| 19 | Publicações em Nature e Science, fev/2001 (AF-039/040) | Evidence formalizada + Validation (peer review) | **MATCH** |
| 20 | Conclusão abril/2003 (92%, <400 gaps, mais preciso) (AF-041..044) | Evidence final + Validation | **MATCH** |
| 21 | Concluído 2 anos antes (AF-045) | Validation (superação) | **MATCH** |
| 22 | T2T 2022 completa lacunas (AF-046) | Evidência posterior (não entidade central) | **NOT_EXPLAINED** |
| 23 | Sucesso: superou objetivos, além do possível de 1988 (AF-048/049) | Validation reforçada | **MATCH** |
| 24 | Ganhos econômicos/biotecnologia (AF-050) | Learning/efeito | **MATCH** |
| 25 | Risk formal **ausente** nos fatos — governança no lugar | **NEW_INSIGHT (NI-001)** — a reconstrução destaca que um grande empreendimento *de sucesso* não formalizou Risk (risco tratado, não calculado). | **NEW_INSIGHT** |
| 26 | Ausência de Risk formal documentado entre os fatos de decisão | **NEW_INSIGHT (NI-002)** — ausência registrada mesmo sendo sucesso | **NEW_INSIGHT** |

---

## Checklist das perguntas

### 1. Apareceu algo novo? → **SIM (2 tópicos)**

NI-001 e NI-002 (ver abaixo).

### 2. Perdeu informação? → **SIM (2–3 itens)**

- Itens 7 (atualização de planos), 13 (a aceleração de decisões pela corrida —
  interpretado como contexto), e parcialmente 3/10 (detalhe institucional
  financiador). Itens 2/3 condensados.

### 3. Inventou algo? → **Não.**

Nenhuma entidade foi reconhecida sem suporte factual. As inferências (Assumption
A-1/A-2, Risk ausente) foram **explicitamente marcadas** como inferidas e **não
contadas** como emergência plena.

### 4. Condensou? → **Sim (itens 2, 3, 10, 13)**

Contexto institucional e competição condensados em entidades genéricas
(Execution/Knowledge) — sem perda causal.

### 5. Generalizou? → **Sim (2, fortes)** — ver abaixo.

---

## NEW_INSIGHT — os achados da reconstrução

> **NI-001 — O problema/objetivo declarado É o "por que" do projeto; e o risco
> formal não emerge nem num sucesso.**

A narrativa descreve o HGP como um esforço que "superou metas". A reconstrução
acrescenta: a **presença ex-ante** de Problem/Goal no registro (AF-005/006,
AF-047) é **estrutural** para diferenciar este caso dos de crise — e, mesmo
neste caso bem-sucedido, o cálculo formal de risco (impacto×probabilidade) não
aparece nos fatos; o risco foi tratado **por governança** (ELSI), não por
cálculo. A reconstrução converte "o projeto começou com metas" em um dado de
estrutura comparável (frente a frente com os casos de crise).

> **NI-002 — Ausência de Risk formal documentado em decisão (dado mesmo em
> sucesso).**

A reconstrução expõe que nenhum fato registra um risco calculado antes da
decisão de iniciar: há matéria-prima (custo AF-012, riscos sociais AF-032/033),
mas não um artefato "Risk". Isto é um dado neutro: mesmo num caso de sucesso o
Kernel não faz emergir Risk — enquanto Problem/Goal emergem. A reconstrução não
comparou (não pode, a etapa 3 é cega); apenas registrou a ausência.

---

## Veredito quantitativo

| Categoria | Itens | Contagem |
|---|---|---|
| MATCH | 1, 4, 5, 6, 8, 9, 12, 14, 17, 18, 19, 20, 21, 23, 24 | 15 |
| PARTIAL_MATCH | 2, 3, 10, 11, 13, 15, 16 | 7 |
| NOT_EXPLAINED | 7, 22 | 2 |
| NEW_INSIGHT | NI-001, NI-002 | 2 |
| **Total avaliado** | | **26** |

> Pergunta de consistência: contagem usada em
> [06-relatorio-ear.md](../report/06-relatorio-ear.md): 15 MATCH + 7 PARTIAL +
> 2 NOT_EXPLAINED + 2 NEW_INSIGHT = 26 itens (24 da tabela + 2 NI).

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-09 | Alignment Analysis: Narrativa × Reconstrução Cega. 26 elementos, 4 categorias. 2 NEW_INSIGHT (NI-001: Goal/Problem ex-ante + Risk ausente com governança; NI-002: ausência de Risk formal). |