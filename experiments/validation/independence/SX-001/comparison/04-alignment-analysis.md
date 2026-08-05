# SX-001 / comparison — Etapa 4: Alignment Analysis

| Campo | Valor |
|---|---|
| **Experimento** | EXP-SX001 |
| **Etapa** | 4 — Alignment Analysis |
| **Compara** | [Narrativa Original](../narrative/01-narrativa-original.md) × [Reconstrução Cega](../reconstruction/03-reconstrucao-cega.md) |
| **Categorias** | `MATCH` \| `PARTIAL_MATCH` \| `NOT_EXPLAINED` \| `NEW_INSIGHT` |
| **Data** | 2026-08-03 |

> **Pergunta central desta etapa:** a reconstrução cega — que usou **apenas** os
> Atomic Facts + Kernel, sem o vocabulário ECP na coleta e sem consultar o
> relatório oficial — reproduz a estrutura do caso Challenger que a narrativa
> histórica descreve? E explica algo que a narrativa não dizia?

## Categorias

| Categoria | Definição |
|---|---|
| `MATCH` | A reconstrução reproduz fielmente o que a narrativa descreve, sem acréscimo nem perda. |
| `PARTIAL_MATCH` | Concorda parcialmente: há coincidência estrutural, mas omitiu ou acrescentou um aspecto. |
| `NOT_EXPLAINED` | O elemento está na narrativa, mas a reconstrução não o alcança (nem acerta nem erra). |
| `NEW_INSIGHT` | A reconstrução diz algo que a narrativa não dizia — surpresa ou explicação nova. |

## Perguntas estruturantes (do plano)

- **Apareceu algo novo?** → `NEW_INSIGHT`
- **Perdeu informação?** → falha de `MATCH`/`PARTIAL_MATCH` (informação da narrativa não reproduzida)
- **Inventou algo?** → item que a narrativa não contém (falso positivo)
- **Condensou?** → `PARTIAL_MATCH` (reconstruiu menos que a narrativa)
- **Generalizou?** → `NEW_INSIGHT` se explicou além; senão `PARTIAL_MATCH`

---

## Tabela de alinhamento

| # | Elemento (da narrativa ou da reconstrução) | Reconstrução | Categoria |
|---|---|---|---|
| 1 | Missão STS-51-L, 25º voo, Challenger (AF-007) | Reconstruiu o Goal da missão | **MATCH** |
| 2 | Plano: satélite, Halley, McAuliffe (AF-008) | Reconstruiu o Goal (estado desejado) | **MATCH** |
| 3 | Histórico do defeito (1977–1985) (AF-001..006) | Reconstruiu Knowledge + lacuna | **MATCH** |
| 4 | Lacuna: "sem dados abaixo de 53 °F" (AF-018) | Reconstruiu como conhecimento-negativo | **MATCH** |
| 5 | Previsão de frio recorde (AF-016) | Usada como matéria-prima de risco; não nomeada | **PARTIAL_MATCH** |
| 6 | Teleconferência 27/01 (AF-017) | Não reconstruída como etapa (só decisões) | **NOT_EXPLAINED** (perdeu o processo de reunião) |
| 7 | Recomendação de não lançar (AF-019) | Reconstruída como Decision (engenharia) | **MATCH** |
| 8 | Reação de Mulloy/Hardy (AF-020/021) | Reconstruída como pressão sobre a suposição | **PARTIAL_MATCH** (não nomeia os indivíduos, mas reproduz a dinâmica) |
| 9 | Mudança de posição da gerência (AF-022) | Reconstruída como Assumption A-1/A-2 | **MATCH** |
| 10 | McDonald não assina (AF-023/024) | Reconstruída como Decision (desacordo e exigência de assinatura) | **MATCH** |
| 11 | Omissão dos O-rings ao Aldrich (AF-025) | Reconstruída como Decision de omitir | **MATCH** |
| 12 | Medições de 8 °F/25 °F não comunicadas (AF-026/027) | Reconstruída como Assumption (A-3) | **MATCH** |
| 13 | Gelo na torre; Rockwell inseguro (AF-028) | Reconstruída como matéria-prima de risco (não calculado) | **PARTIAL_MATCH** |
| 14 | Decisão de prosseguir apesar do gelo (AF-029/030) | Reconstruída como Decision | **MATCH** |
| 15 | Lançamento 11h38, 36 °F (AF-015/031) | Reconstruída como Execution | **MATCH** |
| 16 | Fumaça negra / wind shear / pluma (AF-032/034/035) | Reconstruída como Evidence em voo | **MATCH** |
| 17 | Desintegração, 7 mortos (AF-010/011/036) | Reconstruída como Validação de falha | **MATCH** |
| 18 | Investigação, suspensão, reprojeto (AF-037..046) | Reconstruída como Learning | **MATCH** |
| 19 | Causa técnica exata (qual junta/O-ring) | **Não alcançada** pela reconstrução | **NOT_EXPLAINED** |
| 20 | Motivação dos decisores | **Não alcançada** pela reconstrução | **NOT_EXPLAINED** |

---

## Checklist das perguntas

### 1. Apareceu algo novo? → **SIM (2 tópicos)**

### 2. Perdeu informação? → **SIM (3 itens)**

- A teleconferência (item 6): a narrativa descreve a reunião em 3 vias; a
  reconstrução só registrou a decisão, não o processo. Condensou ao nível de
  "suporte da soberania".
- Causa técnica física exata (item 19): a narrativa traz a Rogers Commission; a
  reconstrução admite não tocá-la.
- O contexto motivacional (por que a NASA faz missões, por que a pressão
  programática) não foi reconstruído (mas também não estava nos AFs).

### 3. Inventou algo? → **Não.** Nenhuma entidade foi reconhecida sem suporte
factual. A reconstrução marcou explicitamente Problem e Risk como **não
emergentes** (ver §3) em vez de inventá-los. Isto é o oposto de inventar:
é honestidade epistemológica.

### 4. Condensou? → **Sim (itens 5, 8, 13)**

A reconstrução condensou o contexto (reuniões, motivo das reações, gelo como
fator à parte) em algumas entidades. Nada essencial foi perdido para a
causalidade — exceto o contexto da reunião (item 6, NOT_EXPLAINED).

### 5. Generalizou? → **Sim (1, forte)**

A reconstrução produziu uma **generalização causal**: detectou que a falha
ocorreu **no elo `Evidence → Decision`** — a decisão de lançar foi tomada **sem
evidência suficiente** (AF-018) e **com base em suposições** (A-1/A-2/A-3).
Isto **não é dito** na narrativa como tal; é uma estrutura que a reconstrução
**extraiu** dos fatos. → **`NEW_INSIGHT`**.

---

## NEW_INSIGHT — o achado principal

> **NI-001 — "Decisão autorizada sem evidência" (elo quebrado Evidence → Decision)**

A reconstrução cega, apenas com os fatos e o Kernel, identificou que o evento
falhou **na exata transição que o Kernel declara obrigatória** (L-0, ECP-008):
uma decisão de avanço (lançar) foi autorizada **sem** evidência suficiente para
o risco envolvido e apoiada **apenas em suposições não validadas**.

A narrativa (Rogers Commission) chega à mesma conclusão por outros nomes:
"decisão de lançamento baseada em informação incompleta e enganosa", "conflito
entre dados de engenharia e julgamento gerencial". **A reconstrução chegou à
mesma estrutura usando apenas os fatos + Kernel** — esta convergência é o dado
central do experimento.

> **Item2 — Ausência como sinal (Problem/risco que NÃO aparecem).** A
> reconstrução registrou que **Problem e Risk não emergiram** dos fatos. Leitura:
> a narrativa também **não** os registra como artefatos — os participantes
> operaram **sem** causa-raiz formal e **sem** cálculo de risco explícito. Isto
> é um `NEW_INSIGHT`: o ECP não apenas não viu uma suposição, viu a **falta de
> infraestrutura cognitiva** que o Kernel exige. Uma boa teoria explica também o
> que estava faltando.

---

## Veredito quantitativo (itens 1–20 + 2 achados)

| Categoria | Itens | Contagem |
|---|---|---|
| MATCH | 1, 2, 3, 4, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18 | 14 |
| PARTIAL_MATCH | 5, 8, 13 | 3 |
| NOT_EXPLAINED | 6, 19, 20 | 3 |
| NEW_INSIGHT | NI-001, NI-002 | 2 |
| **Total avaliado** | | **22** |

> É a mesma contagem usada em [06-relatorio-ear.md](../report/06-relatorio-ear.md):
> 14 MATCH + 3 PARTIAL + 3 NOT_EXPLAINED + 2 NEW_INSIGHT = 22 aliamentos.

## Histórico de revisão

| Versão | Data | Mudando |
|---|---|---|
| 1.0 | 2026-08-03 | Alignment Analysis: Narrativa × Reconstrução Cega. 22 elementos, 4 categorias. 2 NEW_INSIGHT (transição Evidence→Decision; ausência Problem/Risk). |