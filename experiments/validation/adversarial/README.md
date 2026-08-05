# Fase C — Adversarial Validation

| Campo | Valor |
|---|---|
| **Tipo** | Fase do Validation Program |
| **Status** | Aberta (Congelamento da fundação experimental) |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe |
| **Referências** | [ECP-012](../../ECP/ECP-012.md), [AD-007](../../04-governance/AD-007.md), [ECP-AUDIT-001](../audit/ECP-AUDIT-001.md), [CANONICAL-FAILURES](./CANONICAL-FAILURES.md), [HOSTILE-EXPERIMENTS](./HOSTILE-EXPERIMENTS.md), [LAW-CRITERIA](../laws/LAW-CRITERIA.md), [P-0007 — Independence Program](../P-0007-INDEPENDENCE.md) |

## A pergunta muda

Até a Fase B, o Validation Program perguntava:

> **Quais leis existem?**

A partir desta fase, o ECP passa a perguntar:

> **Quais leis sobrevivem quando tentamos destruí-las?**

Não é mais provar que funciona. É **provar que resiste**. Leis universais
sobrevivem a ambientes hostis — não a ambientes favoráveis.

## Congelamento da fundação experimental

**Decisão:** a fundação experimental está **congelada**.

> **Nenhuma nova RFC, AD, lei, entidade ou schema será adicionada** enquanto a
> Fase C estiver em andamento.

O risco que motivou a decisão: se continuarmos adicionando artefatos, **a
fundação nunca termina**. O que existe hoje é suficiente para ser testado,
atacado e — se resistir — consolidado.

## Endogeneidade — o risco central

O maior perigo desta fase é reconhecido desde o início:

> **O protocolo gera experimentos que validam o próprio protocolo, com
> ferramentas feitas pelo protocolo, seguindo critérios definidos pelo
> protocolo.**

Isso é **inevitável no começo**. Mas precisa acabar. A Fase C existe para
quebrar esse ciclo: a validade do ECP deve passar a vir de **fora** do ECP.

## A cadeia epistemológica (H-009)

```
Conhecimento
      ▲
      │
Artefato
      ▲
      │
Instrumento
      ▲
      │
Ferramenta
      ▲
      │
Especificação
```

Cada camada **dá validade** à camada acima. A Fase C testa essa cadeia de cima
para baixo — tentando remover a validade de cada camada.

## As novas eras do projeto

```
Validation Program
      ↓
Adversarial Validation      ← ESTAMOS AQUI
      ↓
External Validation
      ↓
Industrial Validation
```

- **Validation Program** — descoberta interna (Fase B).
- **Adversarial Validation** — tentativa deliberada de destruição (Fase C).
- **External Validation** — validação por sistemas/domínios fora do controle
  dos autores (EXP-007 e além).
- **Industrial Validation** — validação em produção/uso real.

## O funil científico da Fase C

A Fase C não roda como uma lista, mas como um **funil** — cada estágio reduz o
conjunto candidato:

```
Fase C
  ↓
H-001 Hostile Experiments
  ↓
Corpus atualizado
  ↓
Signals            ← camada de evidência recorrente (Inferência Científica)
  ↓
Patterns
  ↓
LAW-H
  ↓
Hostile novamente
  ↓
Observation Independence (Exogenous Evidence)  ← P-0007 / LC-9
  ↓
LAW-C
  ↓
External Validation
  ↓
LAW
  ↓
LAW Strength (LSI)
  ↓
Industrial Validation
  ↓
LAW-F
```

A camada **Signals** e as métricas **LSI / Predictive Index** são formalizadas
na frente [Inferência Científica](../signals/README.md) e em
[LAW-METRICS](../laws/LAW-METRICS.md). O gate **Observation Independence** é
governado pelo [P-0007 — Independence Program](../P-0007-INDEPENDENCE.md)
(LC-9 em [LAW-CRITERIA](../laws/LAW-CRITERIA.md)): a promoção exige Endogenous
**e** Exogenous Evidence — a hipótese deve sobreviver aos hostis **e** emergir
em contexto que nunca usou o ECP.

## Resistance Index (RI / Protocol Robustness Index)

Novo indicador da Fase C:

> **Quanto do protocolo permaneceu válido depois de uma tentativa deliberada de
> quebrá-lo?**

```
RI = critérios do protocolo que permaneceram válidos / critérios testados no ataque
```

- **RI por experimento hostil** — medido ao final de cada ataque (H-001..H-006).
- **RI acumulado** — mínimo e média entre experimentos hostis. O **mínimo**
  importa mais: resistência é binária por critério.
- **RI deve subir de experimento para experimento** — cada ataque sobrevivido
  fortalece a robustez; cada falha vira critério refinado ou lei refutada.

O RI vale mais do que quantidade de testes: mede **sobrevivência a hostilidade**,
não cobertura de cenários favoráveis.

## Onde os ataques vivem

- [HOSTILE-EXPERIMENTS.md](./HOSTILE-EXPERIMENTS.md) — especificações dos
  experimentos hostis H-001..H-006.
- [CANONICAL-FAILURES.md](./CANONICAL-FAILURES.md) — registro oficial de falhas
  humanas canônicas (OBS-0016 e futuras).
- Resultados de cada ataque: `HOSTILE-REPORT-###.yaml`. **H-001 executado**:
  ataque à LB-001 falhou (RI 1.0) — [HOSTILE-REPORT-H-001.yaml](./HOSTILE-REPORT-H-001.yaml).
  Critérios de julgamento: [LAW-CRITERIA v1.0](../laws/LAW-CRITERIA.md) (congelados
  antes da execução).

## Como executar um ataque

1. Escolher um experimento hostil (H-001..H-006).
2. Preparar o projeto adversarial no ambiente hostil (fora do controle do
   protocolo, quando possível).
3. Rodar o protocolo completo contra ele (mineração → revisão ontológica →
   auditoria).
4. Medir **RI**; registrar falhas no `CANONICAL-FAILURES.md`.
5. Decidir: ajustar o protocolo, refinar critérios, ou registrar lei refutada.

## Notas

- **Sem LLM como juiz:** os ataques e a medição de RI seguem as mesmas regras
  do restante do Validation Program — auditáveis e reproduzíveis.
- **A Fase C não constrói:** não cria entidades, leis, runtimes ou schemas.
  Apenas tenta quebrar.
