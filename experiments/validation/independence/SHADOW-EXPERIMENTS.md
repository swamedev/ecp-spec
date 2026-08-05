# SHADOW-EXPERIMENTS — Shadow Experiments (EXP-X)

| Campo | Valor |
|---|---|
| **Tipo** | Método e especificação de experimentos de observação |
| **Status** | Aberto (especificação v1.0 — SX-001 pendente de seleção) |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe |
| **Governado por** | [P-0007](../P-0007-INDEPENDENCE.md) |
| **Referências** | [SX-SELECTION](./SX-SELECTION.md), [OBS-SCHEMA](../corpus/OBS-SCHEMA.yaml), [SIGNAL-SCHEMA](../signals/SIGNAL-SCHEMA.yaml), [SIGNALS-REGISTRY](../signals/SIGNALS-REGISTRY.yaml), [LAW-BACKLOG](../laws/LAW-BACKLOG.md), [LAW-CRITERIA](../laws/LAW-CRITERIA.md) |

## Princípio

Observar projetos reais **sem** aplicar, ensinar ou mencionar o ECP. Depois
**reconstruir** o que aconteceu **usando** o ECP. Se as entidades do ECP
emergirem do comportamento observado, a lei descreve a realidade — não impõe
uma forma de pensar.

> Uma boa teoria não cria os fenômenos que explica; ela os reconhece onde eles
> já existem.

## Pipeline (com reconstrução cega)

```
Projeto
  ↓
Narrativa Original      (coleta neutra; fontes primárias)
  ↓
Reconstrução Cega       (quem reconstrói NÃO conhece a narrativa oficial)
  ↓
Comparação              (reconstrução cega × narrativa original; presença/ausência das entidades)
  ↓
Signals
```

Quem reconstrói o projeto **não deve conhecer a narrativa oficial** antes.
Só depois comparamos. Isso reduz drasticamente o viés de confirmação.

## Regras de observação (anti-viés)

1. **Sem vocabulário ECP** durante a coleta — nenhum termo de ECP-000..010 é
   usado para coletar dados (nada de perguntar "qual era o seu objetivo /
   hipótese / evidência").
2. **Perguntas neutras** aos participantes: "como vocês decidiram?", "o que
   vocês sabiam naquele momento?", "o que foi anotado/registrado?", "por que
   escolheram esta opção em vez da outra?".
3. **Fontes primárias preferidas:** artefatos reais (e-mails, atas, listas de
   tarefas, commits, postmortems), não memórias enviesadas.
4. **Ausência é dado:** entidades que o ECP prediz e que **não** aparecem devem
   ser registradas explicitamente (negative evidence por entidade).
5. **Reconstrução é etapa separada** da observação: primeiro coleta neutra,
   depois mapeamento para OBS, depois interpretação.
6. **Observador externo:** quando possível, a coleta é feita por quem não
   defende o ECP.
7. **Reconstrução cega:** quem reconstrói não lê a narrativa oficial antes de
   registrar suas próprias OBS e a presença/ausência das entidades. A
   comparação com a narrativa original acontece **depois**, como passo explícito.

## Condições de Independência Observacional

Para cada hipótese (LB-###), ao menos um contexto deve satisfazer:

| Condição | Exigência |
|---|---|
| Observador | não conhece o ECP |
| Executor | não conhece o ECP |
| Projeto | não segue o ECP |

## Método (etapas)

1. **Seleção** — pelo protocolo congelado [SX-SELECTION](./SX-SELECTION.md):
   projeto real, não-toy, sem exposição ao ECP; critérios SC-1..SC-6; matriz de
   elegibilidade; exclusões EC-1..EC-7.
2. **Narrativa Original** — coletar artefatos/entrevistas em linguagem neutra
   (regras 1–2). Zero vocabulário ECP.
3. **Reconstrução Cega** — mapear o traço bruto para OBS (OBS-SCHEMA), reconhecer
   entidades (Problem, Goal, Knowledge, Assumption, Evidence, Decision) e a
   cadeia, **sem** ler a narrativa oficial.
4. **Comparação** — reconstrução cega × narrativa original; entidades
   presentes/ausentes; fidelidade da cadeia; achados negativos.
5. **Registro** — `SHADOW-REPORT-###.md` com a conclusão; atualizar Signals
   (ocorrência independente) e LAW-BACKLOG.

## SX-001 — Shadow Experiment 001

- **Pergunta central (não é LB-001):** **as entidades do ECP emergem
  espontaneamente** em um projeto conduzido sem qualquer influência do ECP?
- **Escopo do SX-001:** responder à emergência espontânea. Só **depois** de uma
  resposta afirmativa é que os achados são usados para fortalecer a LB-001 —
  nunca antes.
- **Objetivo de bônus:** mapear quais entidades aparecem, quais **não** aparecem
  (ausência é dado — regra 4) e a fidelidade da cadeia.
- **Domínio alvo:** **fora de Software** (categorias A–E do
  [SX-SELECTION](./SX-SELECTION.md)); preferência por **postmortem público**.
- **Seleção do projeto:** decidida pelo [SX-SELECTION](./SX-SELECTION.md)
  (ver [SX-CANDIDATES](./SX-CANDIDATES.md)) — o protocolo decide, não o gosto.
- **Saídas esperadas:** (a) veredito de emergência espontânea; (b) presença/
  ausência por entidade; (c) se afirmativa, possível ocorrência independente
  para SIG-001 (RA-SIG-001).
- **Status:** **EXECUTADO (2026-08-03)** — pipeline completo
  (Narrativa → Atomic Facts → Reconstrução Cega → Alignment → Signals → EAR);
  `EAR(Challenger) = 0.775` (observação) e achado Evidence→Decision em
  [DISCOVERY-LOG](../../DISCOVERY-LOG.md). Próximos casos: P-0008
  (Cross-Domain Validation).

## Registro de resultados

`SHADOW-REPORT-###.md` — relatório por experimento, no padrão dos demais
artefatos de validação (reconstruível, auditável). Resultados só existem após a
execução.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Versão inicial (Aprovado). Método de shadow experiments; SX-001 especificado; aguarda seleção do projeto-alvo. |
| 1.1 | 2026-08-03 | Pipeline com **Narrativa Original → Reconstrução Cega → Comparação**; regra anti-viés 7 (reconstrução cega); SX-001 refocada na **emergência espontânea** (não LB-001 direto); seleção delegada ao protocolo congelado [SX-SELECTION](./SX-SELECTION.md). |
