# P-0005A.2a — Revisão Ontológica do Corpus

| Campo | Valor |
|---|---|
| **Tipo** | Relatório de incremento (Validation Program) |
| **Status** | Aprovado |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe |
| **Governado por** | [ECP-012](../../ECP/ECP-012.md), [AD-007](../../04-governance/AD-007.md) |
| **Referências** | P-0005A, [OBS-SCHEMA v1.2](../corpus/OBS-SCHEMA.yaml), [CORPUS-EXPERIMENTAL-v0](../corpus/CORPUS-EXPERIMENTAL-v0.yaml), [CORPUS-EXPERIMENTAL-v1](../corpus/CORPUS-EXPERIMENTAL-v1.yaml) |
| **Permanência** | Etapa **obrigatória** e permanente do Validation Program (aprovado pelo Arquiteto-Chefe) |

## Objetivo

Verificar se cada `Observation` do corpus representa um **fato ontológico** ou
apenas um **evento operacional** — e decidir se essa distinção exige novos tipos
de observação.

Este incremento **precede** a auditoria formal (P-0005A.2b). A auditoria só ganha
valor sobre um corpus cujo papel ontológico de cada observação é conhecido.

## Teste central aplicado

Para cada uma das 16 OBS, uma única pergunta:

> **Esta observação representa um fato ou representa apenas um evento?**

Complementada por:

- É fato ou é interpretação?
- É operacional ou é estrutural?
- É redundante?
- É derivável?
- É essencial?

## Classificação das 16 OBS

| OBS | Evento | Fato? | Interpretação? | Operacional? | Estrutural? | Redundante? | Derivável? | Essencial? | kind |
|---|---|---|---|---|---|---|---|---|---|
| OBS-0001 | Assumption A-0001 criada | Sim | Não | Sim | Não | Não (1º do tipo) | Não | Sim | operational |
| OBS-0002 | Assumption A-0002 criada | Sim | Não | Sim | Não | **Sim** (mesmo tipo do OBS-0001) | Não | Não | operational |
| OBS-0003 | Decision D-0001 criada | Sim | Não | Sim | Não | Não (1º do tipo) | Não | Sim | operational |
| OBS-0004 | Evidence E-0001 criada | Sim | Não | Sim | Não | Não (1º do tipo) | Não | Sim | operational |
| OBS-0005 | Goal G-0001 criada | Sim | Não | Sim | Não | Não (1º do tipo) | Não | Sim | operational |
| OBS-0006 | Knowledge K-0001 criada | Sim | Não | Sim | Não | Não (1º do tipo) | Não | Sim | operational |
| OBS-0007 | Problem P-0001 criada | Sim | Não | Sim | Não | Não (1º do tipo) | Não | Sim | operational |
| OBS-0008 | Relação `resolves` G-0001 → P-0001 | Sim | Não | Não | **Sim** | Não | Não | **Sim** | structural |
| OBS-0009 | Relação `serves` D-0001 → G-0001 | Sim | Não | Não | **Sim** | Não | Não | **Sim** | structural |
| OBS-0010 | Snapshot D-0002 criado | Sim | Não | Sim | Não | Não | Não | Parcial (contexto) | operational |
| OBS-0011 | Decision D-0002 autorizada (usa E-0021/E-0022) | Sim | Não | Não | **Sim** | Não | Não | **Sim** | structural |
| OBS-0012 | ExecutionIntent XI-0001 criado | Sim | Não | Sim | Não | Não (1º do tipo) | Não | Sim | operational |
| OBS-0013 | Provider python selecionado | Sim | Não | Sim | Não | Não | Não | Parcial (contexto) | operational |
| OBS-0014 | Observation OBS-0001 criada (auto-referência) | Sim | Não | Sim | Não | Meta-redundante | Não | Parcial | operational |
| OBS-0015 | Evidence E-00042 criada | Sim | Não | Sim | Não | **Sim** (mesmo tipo do OBS-0004) | Não | Não | operational |
| OBS-0016 | Modelo estrutural "validado": 32 cognitivas, 13 operacionais | **Não** | **Sim** | Não | Não | Não | **Sim** (derivada do grafo) | Não | derived |

## Descoberta principal — existem dois níveis de observação

A hipótese levantada antes da revisão foi **confirmada** pela própria inspeção:

### Observation Operacional (12)

Registra o que aconteceu durante a execução: instanciação de entidade, seleção,
snapshot, persistência. São fatos verificáveis, porém **singulares, datados e
amarrados a instâncias**.

> "Snapshot criado", "Provider python", "UUID", "Arquivo salvo".

### Observation Estrutural (3)

Registra uma **relação entre entidades que compõe a estrutura/ontologia**:
dependência, resolução, serviço, uso de evidência. São os candidatos mais
próximos de **futuras leis** (LAW-H).

> "Decision depende de Evidence", "Goal resolve Problem", "Execution nasce de
> Intent", "Knowledge antecede Decision".

As OBS-0008, OBS-0009 e OBS-0011 são **seeds estruturais**: instâncias
observáveis que sustentam os fatos de tipo:

| Seed estrutural | Fato de tipo emergente |
|---|---|
| OBS-0008 (`resolves` G→P) | `Goal` resolve `Problem` |
| OBS-0009 (`serves` D→G) | `Decision` serve `Goal` |
| OBS-0011 (D usa E-0021/E-0022) | `Decision` utiliza `Evidence` |

### Derivada / Interpretativa (1)

OBS-0016 não é um fato primário: é **agregação + julgamento** ("validado",
classificação "cognitivas/operacionais"). Viola **RA-OBS-001** e é integralmente
**derivável** dos demais registros do mesmo experimento.

## Redundância identificada

- **OBS-0002** — redundante com OBS-0001 (segundo `Assumption` criado; mesmo
  tipo, mesmo padrão de evento).
- **OBS-0015** — redundante com OBS-0004 (segundo `Evidence` criada).
- **OBS-0014** — meta-redundante: o próprio corpus já é a evidência de que uma
  `Observation` foi criada (auto-referência).

Padrão de fundo: para fins ontológicos, **um evento de instanciação por tipo é
suficiente**. Os demais repetem o mesmo fato estrutural ("a entidade X existe").

## Derivabilidade

- **OBS-0016** é totalmente derivável do grafo (contagens já presentes nos
  demais OBS).
- Os **fatos de tipo** (Goal→Problem, Decision→Goal, Decision→Evidence) são
  deriváveis dos seeds estruturais — e pertencem à camada de **Padrões
  (P-0005A.3)** / hipóteses (LAW-H), não ao corpus primário.

## OBS-0016 — caso canônico de não-observação

> **Isto parece uma observação, mas não é.**

OBS-0016 foi detectado pelo próprio processo como **falso positivo**: contém
julgamento ("validado") e classificação (cognitivas × operacionais), violando
RA-OBS-001, e é derivável do mesmo grafo.

Em vez de ser silenciosamente removido, foi registrado como **exemplo
permanente** de violação no schema e no corpus (`caso_canonico_violacao:
RA-OBS-001`). Um falso positivo encontrado pelo processo é evidência de que o
Validation Program está funcionando — e serve para treinar avaliadores e
calibrar auditorias futuras.

## Métrica — observation_profile

Proporção de observações por `kind` no corpus v1:

| kind | contagem | proporção |
|---|---|---|
| operational | 12 | 75% |
| structural | 3 | ~19% |
| derived | 1 | ~6% |

> **Leitura:** apenas ~19% das observações são estruturais. O conhecimento
> realmente útil para descobrir leis é **mais raro** do que os eventos
> registrados. Se a raridade relativa se repetir em outros experimentos, a
> proporção vira uma tendência a monitorar — e a métrica passa a acompanhar
> todo corpus congelado (RA-OBS-007).

## Essencialidade

**Essenciais (10):** OBS-0001, 0003, 0004, 0005, 0006, 0007, 0012 (primeiro do
tipo — evidência da existência da entidade) + OBS-0008, 0009, 0011 (seeds
estruturais).

**Parciais (3):** OBS-0010, 0013 (contexto operacional), OBS-0014
(auto-referência).

**Não essenciais (3):** OBS-0002, 0015 (redundantes), OBS-0016 (derivada).

**Resultado:** 16 OBS → **13 OBS preservam informação essencial** para o
pipeline.

## Decisão sobre novos tipos de Observation

1. **Sim — introduzir o campo `kind`** com valores `operational` | `structural`
   | `derived`. A distinção é real e observável no corpus atual (12/3/1).
2. **Não — criar uma entidade de primeira classe** "Observation Estrutural".
   Uma observation estrutural continua sendo uma `Observation`; muda apenas a
   classificação (`kind`).
3. **Derivadas/interpretações** (como OBS-0016) **não pertencem ao corpus
   primário**: violam RA-OBS-001. Devem ser movidas para a camada de derivados
   ou reescritas como fatos primários.
4. **Critérios objetivos de classificação** documentados (necessidade
   relacional, independência de implementação, impacto causal) para tornar a
   decisão "quem é estrutural?" reproduzível por avaliadores independentes — e
   não dependente do autor.

## Resultado — Corpus v1 (congelado)

- **16 OBS classificadas** uma a uma (fato/interpretação, nível,
  redundância, derivabilidade, essencialidade).
- **3 OBS redundantes** identificadas (0002, 0015 + meta 0014).
- **1 OBS derivável** identificada (0016).
- **10 OBS essenciais + 3 parciais** preservadas.
- **Necessidade de novos tipos decidida**: campo `kind`, sem nova entidade.
- **Corpus congelado** em `CORPUS-EXPERIMENTAL-v1.yaml`.

## Recomendações para a auditoria (P-0005A.2b)

- Auditar sobre o corpus **congelado v1**, que já carrega a classificação
  ontológica por OBS.
- As auditorias de reconstrução A/B devem operar **por nível**: verificar
  independentemente a classe de observações operacionais e a classe estrutural.
- OBS-0016 deve ser **excluída do corpus primário** ou reescrita como fato
  primário antes da auditoria de admissibilidade (RA-OBS-001).
- O campo `kind` passa a ser **obrigatório** em todo corpus congelado.
- **Objetivo adicional (decisão do Arquiteto-Chefe):** medir a **confiabilidade
  da classificação ontológica** — verificar se **dois avaliadores
  independentes** classificam as mesmas observações da mesma forma
  (operational, structural ou derived). Concordância alta fortalece a
  classificação; concordância baixa exige **refinar os critérios** antes de
  avançar para P-0005A.3.

## Permanência da etapa

A Revisão Ontológica deixa de ser um ajuste circunstancial e passa a ser uma
**fase obrigatória** do Validation Program:

```
Experimento → Extração → Revisão Ontológica → Auditoria → Padrões → LAW-H → Refutação → LAW
```

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.1 | 2026-08-03 | Caso canônico de não-observação (OBS-0016); métrica `observation_profile` (RA-OBS-007); critérios objetivos de classificação; etapa promovida a permanente; objetivo de concordância entre avaliadores adicionado à P-0005A.2b. |
| 1.0 | 2026-08-03 | Versão inicial (Aprovado). Revisão ontológica das 16 OBS; descoberta dos dois níveis de observação (operacional × estrutural); decisão do campo `kind`; identificação de redundantes/deriváveis/essenciais; Corpus v1 congelado. |
