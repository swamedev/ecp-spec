# P-0007 — Independence Program

| Campo | Valor |
|---|---|
| **Tipo** | Programa de pesquisa (Validation Program) |
| **Status** | Aberto |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe |
| **Governado por** | [ECP-012](../../ECP/ECP-012.md), [AD-007](../../04-governance/AD-007.md), [P-0006](./P-0006-LAW-DISCOVERY.md), [RESEARCH-CHARTER](./RESEARCH-CHARTER.md) |
| **Referências** | [LAW-CRITERIA](./laws/LAW-CRITERIA.md), [LAW-BACKLOG](./laws/LAW-BACKLOG.md), [SIGNALS-REGISTRY](./signals/SIGNALS-REGISTRY.yaml), [adversarial](./adversarial/README.md), [SHADOW-EXPERIMENTS](./independence/SHADOW-EXPERIMENTS.md), [SX-SELECTION](./independence/SX-SELECTION.md), [SX-CANDIDATES](./independence/SX-CANDIDATES.md), [P-0007.1 — Independence Framework](./P-0007.1-INDEPENDENCE-FRAMEWORK.md) |

## A descoberta que motivou este programa

O H-001 atacou "toda decisão justificável depende de conhecimento?" e o protocolo
respondeu **"espere."**

O motivo: o ECP **define** decisão justificável como dependente de evidência
([ECP-009](../../00-foundation/ECP-009.md) §3, P-5), e evidência pressupõe
conhecimento. Sobreviver ao H-001 poderia estar apenas **validando uma
definição** — uma verdade analítica, não uma descoberta.

Isto não é uma falha. É o **sistema de validação funcionando**: ele impediu o
projeto de comemorar uma "lei" cedo demais. A descoberta mais valiosa desta
rodada não foi a LB-001 — foi o protocolo detectando o próprio risco de
circularidade (**LC-8**).

## O problema que este programa resolve

> Uma Candidate Universal Law **não pode ser derivada apenas das definições
> internas do ECP.**

Se a "lei" só existe porque o protocolo a define, ela não é uma lei — é um
axioma do modelo.

## As duas perguntas de toda LAW-H

Toda LAW-H passa a responder **duas** perguntas:

```
Pergunta 1 — Ela sobrevive aos experimentos?
   H-001, H-002, H-003, ...

Pergunta 2 — Ela continua verdadeira se o ECP desaparecer?
```

A Pergunta 2 é mais difícil e mais valiosa. Exemplo: uma equipe que nunca ouviu
falar do ECP toma decisões todos os dias. **Eles conseguem justificar decisões
sem conhecimento?**

## Shadow Experiments (EXP-X)

Método: **observar** projetos reais sem aplicar, ensinar ou mencionar o ECP.
Depois **reconstruir** o que realmente aconteceu.

- Sem aplicar ECP.
- Sem ensinar ECP.
- Sem falar em leis.
- Observar o que realmente aconteceu.
- Perguntas de reconstrução: houve decisão? houve conhecimento? houve hipótese?
  houve objetivo? houve evidência?

Se essas entidades **aparecerem espontaneamente** no comportamento observado, a
hipótese ganha força — porque a lei deixa de depender do protocolo: ela
**emerge** do comportamento real. Isso **elimina o LC-8 na origem**.

- Método e pipeline (Narrativa Original → Reconstrução Cega → Comparação):
  [SHADOW-EXPERIMENTS.md](./independence/SHADOW-EXPERIMENTS.md).
- **Seleção do projeto é decidida por protocolo congelado**, nunca por escolha
  antecipada: [SX-SELECTION.md](./independence/SX-SELECTION.md) (SC-1..SC-6,
  matriz, exclusões EC-1..EC-7). Aplicação e candidatos:
  [SX-CANDIDATES.md](./independence/SX-CANDIDATES.md).

## Disciplina metodológica

O ECP está evoluindo de especificação → protocolo → ontologia → teoria →
**metodologia científica** (pré-registro de critérios, controle de viés,
evidência exógena, validação independente). Esse movimento é coerente, mas exige
disciplina:

> **Cada nova camada metodológica deve surgir porque um experimento revelou uma
> limitação real — nunca porque parece intelectualmente interessante.**

Esta é a extensão natural da Regra 1 (P-0006) para camadas metodológicas: se a
regra for mantida, o projeto cresce em profundidade sem se tornar excessivamente
complexo.

## Regra de Ouro da Evolução Científica

> **Nenhuma parte da teoria pode evoluir mais rápido que o conjunto de
> evidências que a sustenta.**

No Independence Program, isto significa: uma observação exógena (Shadow
Experiment) só alimenta a teoria quando sustentada por evidência independente e
comparada com hipóteses concorrentes (ver [DISCOVERY-LOG](./DISCOVERY-LOG.md)).

## Classificação de evidência

| Termo | Definição |
|---|---|
| **Endogenous Evidence** | Evidência produzida **dentro** do ECP (corpus EXP-*, experimentos hostis, auditoria). |
| **Exogenous Evidence** | Evidência observada **fora** do ECP (shadow experiments, projetos que nunca o usaram). |
| **Endogenous Law** | Lei sustentada apenas por evidência interna — risco de verdade analítica (LC-8). |
| **Exogenous Law** | Lei sustentada apenas por observação externa — sozinha não prova universalidade nem passa pelo funil hostil. |

**Regra de promoção:** somente quando **ambas** existirem — endógena (sobreviveu
aos experimentos hostis) **e** exógena (emerge fora do ECP) — uma hipótese pode
se tornar **Candidate Universal Law**.

## Observation Independence

Camada adicional ao modelo do motor de descoberta:

> Toda hipótese precisa nascer de pelo menos **um contexto** onde:
> - o **observador** não conhece o ECP;
> - o **executor** não conhece o ECP;
> - o **projeto** não segue o ECP.

Isto praticamente elimina o viés de confirmação e é a resposta estrutural à
**endogeneidade** (cadeia epistemológica H-009 da Fase C).

## A regra do teste

> **Uma boa teoria não cria os fenômenos que explica; ela os reconhece onde eles
> já existem.**

O próximo grande teste do ECP não é "o ECP funciona quando aplicado a um
projeto". É: **as estruturas que ele descreve emergem naturalmente em projetos
conduzidos sem qualquer influência do ECP?**

Se aparecerem repetidamente, o protocolo está descrevendo aspectos **reais** da
engenharia — e não apenas impondo uma forma particular de pensar.

## Ordem de trabalho (substitui a anterior)

```
1. Independence Program        (P-0007 — aberto)
2. Independence Framework      (P-0007.1 — gate metodológico congelado)
3. Shadow Experiment 001       (observação pura, sem ECP)
4. Reconstrução cega + comparação (OBS-SCHEMA → entidades → cadeia)
5. Atualização dos Signals     (ocorrência independente — RA-SIG-001)
6. Só então: EXP-002 (e H-007)
7. Cross-Domain Validation     (P-0008 — estabilidade entre domínios)
```

A ordem é **deliberada**: o gate metodológico (P-0007.1) é congelado **antes** do
primeiro experimento externo, para que o SX-001 rode sobre uma infraestrutura
estável — sem alterações metodológicas no meio do experimento.

> **Status (2026-08-03):** SX-001 executado (EAR(Challenger) = 0.775, observação).
> A etapa 7 substitui a anterior a partir de agora: a prioridade passa a ser
> [P-0008 — Cross-Domain Validation](./P-0008-CROSS-DOMAIN-VALIDATION.md) —
> medir a estabilidade da estrutura em domínios radicalmente diferentes antes de
> qualquer promoção de lei. Observações registradas em
> [DISCOVERY-LOG](./DISCOVERY-LOG.md).

## Regra 1 preservada

Este programa **não constrói** ferramentas. A observação é pura; a reconstrução
usa o ECP que já existe (OBS-SCHEMA, corpus, funil). Nenhuma nova entidade,
schema ou índice sem lacuna demonstrada.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Versão inicial (Aprovado). Abertura do Independence Program após a descoberta LC-8 no H-001; as duas perguntas de toda LAW-H; Shadow Experiments; classificação Endogenous/Exogenous; Observation Independence; nova ordem de trabalho. |
| 1.1 | 2026-08-03 | SX-SELECTION congelado (protocolo de seleção SC-1..SC-6) antes de qualquer candidato; SX-CANDIDATES aplicado (14 elegíveis, 6 inelegíveis); pipeline com reconstrução cega; seção "Disciplina metodológica". |
| 1.2 | 2026-08-03 | **P-0007.1 — Independence Framework** congelado (gate antes do SX-001): três eixos (Observation / Evidence / Domain Independence), definição de ocorrência independente, critérios mínimos de promoção. Ordem de trabalho revisada (framework antes do SX-001). |
| 1.3 | 2026-08-03 | SX-001 executado (EAR(Challenger) = 0.775, observação). Ordem de trabalho estendida com Cross-Domain Validation (P-0008). Regra de Ouro da Evolução Científica adicionada (evidência antes de teoria). |
