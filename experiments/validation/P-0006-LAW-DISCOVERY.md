# P-0006 — Law Discovery Program

| Campo | Valor |
|---|---|
| **Tipo** | Programa de pesquisa (Validation Program) |
| **Status** | Aberto |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe |
| **Governado por** | [ECP-012](../../ECP/ECP-012.md), [AD-007](../../04-governance/AD-007.md), [RESEARCH-CHARTER](./RESEARCH-CHARTER.md) |
| **Referências** | [LAW-BACKLOG](./laws/LAW-BACKLOG.md), [LAW-CRITERIA](./laws/LAW-CRITERIA.md), [adversarial](./adversarial/README.md), [signals](./signals/README.md), [LAW-METRICS](./laws/LAW-METRICS.md), [P-0007 — Independence Program](./P-0007-INDEPENDENCE.md), [P-0008 — Cross-Domain Validation](./P-0008-CROSS-DOMAIN-VALIDATION.md) |

## O que muda

**P-0005A termina aqui.** Não porque acabou, mas porque já existe infraestrutura
suficiente:

```
ANTES (P-0005A):  construir infraestrutura → descobrir padrões
AGORA (P-0006):   produzir conhecimento novo → descobrir leis
```

O objetivo daqui para frente é **produzir leis da engenharia**, não construir
mais ferramentas.

## Regra 1 — gate de ferramentas (obrigatória)

> **Nunca desenvolver uma ferramenta sem que exista uma pergunta científica que
> ela responda.**

Nada de schema "porque parece útil", nada de RFC "porque ficou bonita", nada de
índice novo sem necessidade. Sempre nesta ordem:

```
Existe uma hipótese?
   ↓
Existe um experimento?
   ↓
Precisamos de uma ferramenta para responder isso?
   ↓
Então construímos.
```

**Infraestrutura metodológica congelada:** nenhum novo schema, RFC ou índice,
exceto se um experimento demonstrar uma lacuna real.

## Regra de Ouro da Evolução Científica (coordenação 2026-08-03)

> **Nenhuma parte da teoria pode evoluir mais rápido que o conjunto de
> evidências que a sustenta.**

Não nasce LAW porque um caso deu certo; não nasce entidade porque "faz
sentido"; não nasce RFC porque surgiu uma ideia boa. Primeiro nasce evidência —
registrada no [DISCOVERY-LOG](./DISCOVERY-LOG.md) —, depois teoria. Esta regra
tem peso análogo à Lei Zero para a evolução do protocolo: é o freio que impede
o projeto de comemorar cedo demais.

## Candidata a Lei Universal → Lei Universal de Engenharia

O termo **"Lei da Engenharia"** é substituído por **Candidate Universal Law**
até a validação industrial. Somente depois do estágio industrial a lei pode ser
chamada de **Universal Engineering Law**.

Isso evita que o projeto afirme certezas antes da hora — a honestidade
epistemológica é uma exigência, não um adorno.

## Genealogia das hipóteses (LAW-H)

Toda hipótese de lei deve registrar **de onde veio** — nunca nasce do nada:

```
LAW-H-001
  Originou-se dos Signals:
  S-003, S-005, S-014, S-021
  Domínios cobertos: ...
  Pergunta do backlog de origem: LB-...
```

A genealogia dá **rastreabilidade científica**: OBS → SIGNAL → PATTERN → LAW-H,
com cada salto auditável.

## Negative Evidence

A **ausência de evidência também é informação.** Experimentos que não produzem
o caso esperado devem ser registrados explicitamente:

> Tentamos provar **Decision sem Knowledge**.
> Resultado: **nenhum caso encontrado.**

Negative evidence é registrada por backlog item e por LAW-H, junto de
contraexemplos. Ciência registra o que **não** foi encontrado, não apenas o que
foi.

## Programa de Diversidade Experimental

Uma lei só pode evoluir se sobreviver a domínios **radicalmente diferentes**:

```
Software | ERP | Game | Sistema Embarcado | IA | Site | Aplicativo
Pesquisa Científica | Engenharia Civil | Robótica
```

**Regra de evolução:** cada avanço de uma lei (Signal → Pattern → LAW-H → LAW-C
→ LAW-V → LAW-F) exige sobrevivência em domínios **distintos** — nunca em
múltiplos projetos do mesmo domínio.

> Sobreviver em cinco projetos de software mede **repetição**, não
> **universalidade**.

## Foco em uma única hipótese

Em vez de criar várias hipóteses paralelas, o programa concentra a energia em
**uma única hipótese por vez**:

1. Escolher uma LAW-H.
2. Tentar **destruí-la** (hostile, diversidade de domínios, negative evidence).
3. Só então partir para a próxima.

## Ordem de trabalho

1. **Congelar** completamente a infraestrutura metodológica (Regra 1).
2. Abrir o [LAW-BACKLOG](./laws/LAW-BACKLOG.md) — apenas perguntas científicas
   priorizadas, **sem respostas antecipadas**.
3. **Congelar** os [LAW-CRITERIA](./laws/LAW-CRITERIA.md) (LC-1..LC-8) **antes**
   de qualquer resultado hostil — critérios nunca se ajustam ao achado.
4. Executar **H-001** e gerar o primeiro conjunto de dados hostis.
5. Extrair os primeiros **Signals reais** (não ilustrativos).
6. Promover apenas Signals que atenderem rigorosamente aos critérios → Pattern.
7. Escolher **uma única LAW-H** e concentrar a energia em destruí-la.

**Estado atual (2026-08-03):** passos 1–3 concluídos; **H-001 executado** contra
a LB-001 (ataque falhou, RI 1.0 — ver
[HOSTILE-REPORT-H-001](./adversarial/HOSTILE-REPORT-H-001.yaml)); **SIG-001**
registrado como primeiro Signal preliminar (RA-SIG-001 pendente — aguarda
ocorrência independente). LB-001 **não** promovida.

> **Descoberta LC-8 / Independence Program:** o H-001 revelou o risco de verdade
> analítica (o ECP define decisão justificável com evidência). A partir de
> 2026-08-03, a prioridade passa a ser o [P-0007 — Independence Program](./P-0007-INDEPENDENCE.md):
> evidência exógena (shadow experiments) **antes** de EXP-002. A ordem de
> trabalho dos passos 6–7 é substituída: Shadow Experiment 001 → reconstrução →
> comparação → Signals → só então EXP-002/H-007.

## Identidade — Scientific Discovery Engine → ECP

> **Engineering Discovery Engine** é o nome forte do motor de descoberta
> científica. O ECP é uma instância concreta do **Scientific Discovery Engine** —
> um modelo de dois níveis: o *engine* é o método de descobrir leis da
> engenharia; o ECP é a especificação operacional que instancia esse método.

```
Scientific Discovery Engine   ← o motor (método, critérios, funil)
        └── Engineering Cognition Protocol (ECP)  ← a instância operacional
```

Isto responde "o que é o ECP?": **não** é uma teoria com leis consolidadas, é o
**protocolo operacional do motor de descoberta** — o conjunto de critérios,
experimentos e procedimentos pelos quais o motor produz leis. É um **programa de
pesquisa sobre as leis da engenharia** — um método rigoroso para descobrir,
testar, refutar e consolidar leis ao longo do tempo. Se o método produzir leis
que resistem à falsificação em diferentes domínios e por avaliadores
independentes, o ECP evolui naturalmente para uma **teoria operacional da
engenharia** — como consequência das evidências, nunca como declaração
antecipada.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Versão inicial (Aprovado). P-0005A encerrado; P-0006 aberto; Regra 1 (gate de ferramentas); naming Candidate Universal Law; genealogia LAW-H; Negative Evidence; Programa de Diversidade Experimental; foco em hipótese única. |
| 1.1 | 2026-08-03 | LAW-CRITERIA v1.0 congelado; H-001 executado (RI 1.0, LB-001 sobreviveu); SIG-001 preliminar registrado; identidade em dois níveis (Scientific Discovery Engine → ECP). |
| 1.2 | 2026-08-03 | Descoberta LC-8 (risco de verdade analítica no H-001) → prioridade passa ao P-0007 (Independence Program); ordem de trabalho revisada (evidência exógena antes de EXP-002). |
| 1.3 | 2026-08-03 | Regra de Ouro da Evolução Científica adicionada (nenhuma parte da teoria evolui mais rápido que as evidências; primeiro nasce evidência no DISCOVERY-LOG, depois teoria). |
