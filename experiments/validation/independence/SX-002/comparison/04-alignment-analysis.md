# SX-002 / comparison — Etapa 4: Alignment Analysis

| Campo | Valor |
|---|---|
| **Experimento** | EXP-SX002 |
| **Etapa** | 4 — Alignment Analysis |
| **Compara** | [Narrativa Original](../narrative/01-narrativa-original.md) × [Reconstrução Cega](../reconstruction/03-reconstrucao-cega.md) |
| **Categorias** | `MATCH` \| `PARTIAL_MATCH` \| `NOT_EXPLAINED` \| `NEW_INSIGHT` |
| **Data** | 2026-08-04 |

> **Pergunta central desta etapa:** a reconstrução cega — que usou **apenas** os
> Atomic Facts + Kernel, sem o vocabulário ECP na coleta e sem consultar a
> narrativa histórica — reproduz a estrutura do evento que a narrativa descreve?
> E explica algo que a narrativa não dizia?

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
| 1 | Origem dez/2013, Guéckédou, sintomas, Meliandou (AF-001..003) | Não citada como entidade | **NOT_EXPLAINED** |
| 2 | Agente não identificado inicialmente (AF-004) | Reconstruiu como Lacuna inicial | **MATCH** |
| 3 | Notificação da Guiné à OMS (AF-005) | Reconstruiu como Evidence de detecção + Decision de escalonamento | **MATCH** |
| 4 | Identificação do Zaire ebolavirus (AF-006) | Reconstruiu como Knowledge | **MATCH** |
| 5 | Transmissão por fluidos (AF-007) | Reconstruiu como Knowledge | **MATCH** |
| 6 | Rituais funerários (AF-008) | Não citado na reconstrução | **NOT_EXPLAINED** |
| 7 | Profissionais de saúde infectados (AF-009/010) | Reconstruiu como **matéria-prima de risco** (não entidade própria) | **PARTIAL_MATCH** |
| 8 | Dispersão multi-país + precedente (AF-011..013) | Reconstruiu como Knowledge/risco; geografia não nomeada | **PARTIAL_MATCH** |
| 9 | MSF monta centros de tratamento (AF-015) | Reconstruiu como **Goal** | **MATCH** |
| 10 | Alertas da MSF "fora de controle" (AF-016/017) | Reconstruiu como insuficiência/lacuna de escala (inferida) | **MATCH** |
| 11 | Resposta lenta e gradual (AF-018/019) | Reconstruiu como **suposição implícita A-1** | **MATCH** |
| 12 | PHEIC em 08/08/2014 (AF-020) | Reconstruiu como Decision | **MATCH** |
| 13 | UNMEER em set/2014 (AF-021/022) | Reconstruiu como Decision + Goal | **MATCH** |
| 14 | Contenção da Nigéria (AF-023..025) | Reconstruiu como Decision local + evidência de resultado | **MATCH** |
| 15 | Contenções Senegal/Mali (AF-026..029) | Reconstruiu os resultados como evidências de resultado | **MATCH** |
| 16 | Pico de casos set–nov/2014 (AF-030/031) | Reconstruiu como evidência de vigilância + base do "lag" | **MATCH** |
| 17 | Mortalidade 40–70% (AF-032/033) | Reconstruiu como **matéria-prima de risco** | **PARTIAL_MATCH** |
| 18 | Queda em 2015 com expansão da resposta (AF-034/035) | Reconstruiu como declínio pós-expansão (elo da cadeia) | **MATCH** |
| 19 | Declarações de "livre do vírus" por país (AF-036..038) | Reconstruiu como Goal + Validation/estado final | **MATCH** |
| 20 | Fim da PHEIC em 29/03/2016 (AF-039) | Reconstruiu como Decision de encerramento | **MATCH** |
| 21 | Totais agregados (AF-040..043) | Reconstruiu como Evidence agregada | **MATCH** |
| 22 | Lição "resposta tardia" (AF-044) | Reconstruiu como achado central do **lag** | **MATCH** |
| 23 | Sistemas frágeis e rituais/medo (AF-045, AF-047) | Não reconstruído como entidade | **NOT_EXPLAINED** |
| 24 | Falta de preparação (AF-046) | Reconstruiu como base da suposição A-1 | **MATCH** |
| 25 | OMS criticada + reformas + avanço (AF-048..051) | Reconstruiu como **Learning** | **MATCH** |

---

## Checklist das perguntas

### 1. Apareceu algo novo? → **SIM (2 tópicos)**

### 2. Perdeu informação? → **SIM (4 itens)**

- Contexto de origem (item 1): local, sintomas, vila — não reconstruído.
- Rituais funerários (item 6): via de transmissão cultural não nomeada.
- Sistemas frágeis e rituais/medo (item 23): fatores estruturais não
  convertidos em entidade.
- O detalhamento clínico (mortalidade como tabela, evitado).

### 3. Inventou algo? → **Não.**

Nenhuma entidade foi reconhecida sem suporte factual. Os elementos inferidos
(Assumption A-1, lacuna de escala, Risk) foram **explícitamente marcados
inferidos** e **não contados como emergência plena** — o oposto de inventar.

### 4. Condensou? → **Sim (itens 7, 8, 17)**

Profissionais infectados, dispersão geográfica e taxas de mortalidade foram
tornados **matéria-prima de risco** em vez de entidades próprias. Nada de
causal perdido (a narrativa também não explica *por que* eles ocorrem).

### 5. Generalizou? → **Sim (2, fortes)** — ver abaixo.

---

## NEW_INSIGHT — os achados da reconstrução

> **NI-001 — "Lentidão como suposição implícita (A-1), não como fato"**

A narrativa descreve a resposta internacional como **lenta** (fato). A
reconstrução explica **por que** esse atraso é estruturalmente relevante: o
comportamento lento implica uma **crença não registrada de que a epidemia podia
ser contida sem expansão imediata** — a suposição A-1. Isto é uma explicação
extra que a narrativa não formula. A reconstrução converte um adjetivo em um
**artefato cognitivo monitorável** (ECP-007).

> **NI-002 — A defasagem (lag) alerta → coordenação formal.**
> A reconstrução posicionou temporalmente os elementos que a narrativa lista
> sem explicitar a relação: o **pico de casos (set–nov 2014, AF-030)** ocorre
> **antes** de a coordenação formal (UNMEER, set/2014, AF-021) se consolidar, e
> o declínio **só segue a expansão** (AF-034/035). A estrutura emergente da
> reconstrução **explicita a ordem causal** (alerta existia, decisão tardia) que
> a narrativa apenas narra. Este é o espelho da descoberta do SX-001 — mas com o
> sinal invertido (ver §Veredito).

> **Correlação com o rapport (registro, não força):** no Challenger o elo quebrado
> foi **Evidence → Decision** (decisão sem evidência). No Ebola a reconstrução vê
> **Evidence/alerta presente → Decision tardia** (decisão com evidência já
> disponível, porém tardia). As duas reconstruções chegaram a padrões distintos
> — isso é um dado (diversidade de manifestação), **não** uma busca deliberada de
> divergência. Ver [05-signals.yaml](../signals/05-signals.yaml).

---

## Veredito quantitativo (itens 1–25 + 2 achados)

| Categoria | Itens | Contagem |
|---|---|---|
| MATCH | 2, 3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 24, 25 | 19 |
| PARTIAL_MATCH | 7, 8, 17 | 3 |
| NOT_EXPLAINED | 1, 6, 23 | 3 |
| NEW_INSIGHT | NI-001, NI-002 | 2 |
| **Total avaliado** | | **25** |

> É a mesma contagem usada em [06-relatorio-ear.md](../report/06-relatorio-ear.md):
> 19 MATCH + 3 PARTIAL + 3 NOT_EXPLAINED + 2 NEW_INSIGHT = 27 aliamentos (25
> tabela + 2 NI).

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-04 | Alignment Analysis: Narrativa × Reconstrução Cega. 25 elementos, 4 categorias. 2 NEW_INSIGHT (NI-001: lentidão como suposição implícita; NI-002: defasagem alerta→coordenação). |