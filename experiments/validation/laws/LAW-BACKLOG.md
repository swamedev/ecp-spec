# LAW-BACKLOG — Backlog Científico

| Campo | Valor |
|---|---|
| **Tipo** | Registro de perguntas científicas |
| **Status** | Ativo |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe |
| **Governado por** | [P-0006 — Law Discovery Program](../P-0006-LAW-DISCOVERY.md) |
| **Referências** | [LAW-CRITERIA](./LAW-CRITERIA.md) (critérios congelados), [LAW-METRICS](./LAW-METRICS.md) |

## O que este backlog NÃO é

- ❌ **Não** são leis.
- ❌ **Não** são hipóteses.
- ❌ **Não** contêm respostas antecipadas.

## O que é

Perguntas científicas **priorizadas**, sem resposta pré-concebida. Cada item é
investigado por experimentos; só a evidência decide.

## Formato de item

```
LB-NNN — Pergunta
  Domínios alvo:
  Status:        Investigando | Sem evidências | Desconhecido | Em refutação | Consolidada
  Signals de apoio:
  Positive Evidence:
  Negative Evidence:
  Contraexemplos:
  Genealogia:    → LAW-H-### (quando a evidência suportar)
```

## Itens

### LB-001 — Toda decisão justificável depende de conhecimento?

- **Domínios alvo:** Software, ERP, App, IA.
- **Status:** Investigando.
- **Signals de apoio:** SIG-001 (preliminar — de EXP-001 OBS-0011 + H-001;
  ainda não satisfaz RA-SIG-001, sem ocorrência independente).
- **Positive Evidence:** H-001 — remover conhecimento de uma decisão a degrada
  para "preferência" (sem critérios) ou a invalida (sem evidência, P-5). Para
  ser justificável, o agente é obrigado a adquirir conhecimento mínimo.
- **Negative Evidence:** Nenhum caso de decisão justificável sem conhecimento
  encontrado (EXP-001, H-001). Tentamos provar Decision sem Knowledge → nada.
- **Contraexemplos:** 0 encontrados.
- **Próximo ataque — Pergunta 2 (P-0007):** "continua verdadeira se o ECP
  desaparecer?". O H-001 revelou risco de **verdade analítica** (LC-8): o ECP
  define decisão justificável como dependente de evidência, e evidência
  pressupõe conhecimento. Por isso esta hipótese precisa de **Exogenous
  Evidence** — via [Shadow Experiment 001](../P-0007-INDEPENDENCE.md), em
  projeto que **nunca** usou o ECP (observador, executor e projeto sem
  exposição). Somente com endógena + exógena ela pode virar Candidate Universal
  Law ([LAW-CRITERIA v1.1, LC-9](./LAW-CRITERIA.md)).

### LB-002 — Objetivos podem existir sem problemas?

- **Domínios alvo:** Pesquisa Científica, Game, Projeto artístico (H-002).
- **Status:** Sem evidências.
- **Signals de apoio:** (nenhum ainda).
- **Negative Evidence:** (a preencher).
- **Contraexemplos:** (a preencher).

### LB-003 — Toda engenharia altera algum estado do mundo?

- **Domínios alvo:** Engenharia Civil, Robótica, Sistema Embarcado, Site.
- **Status:** Investigando.
- **Signals de apoio:** (a preencher).
- **Negative Evidence:** (a preencher).
- **Contraexemplos:** (a preencher).

### LB-004 — Existe projeto sem hipótese?

- **Domínios alvo:** Projeto artístico (H-002), Aplicativo.
- **Status:** Desconhecido.
- **Signals de apoio:** (a preencher).
- **Negative Evidence:** (a preencher).
- **Contraexemplos:** (a preencher).

### LB-005 — Decisões metodológicas devem ser derivadas de critérios pré-congelados?

> **Princípio registrado (P-0007.2, 2026-08-03):** "Nenhuma decisão metodológica
> deve depender do julgamento do autor quando ela puder ser derivada de critérios
> previamente congelados."

- **Domínios alvo:** Metodologia científica (meta), Governança, Engenharia.
- **Status:** Investigando — candidata a uma das primeiras **leis realmente
  fortes** (origem: disciplina recorrente de pré-registro).
- **Signals de apoio:** padrão recorrente — critérios congelados **antes** dos
  resultados em LAW-CRITERIA (LC-1..LC-9, anti-hindsight), SX-SELECTION
  (SC-1..SC-6 antes da lista), P-0007.1 (framework antes do SX-001), P-0007.2
  (vereditos antes da aplicação). Ocorrências ainda não independentes.
- **Positive Evidence:** o pré-registro impediu comemoração precoce de lei
  (H-001/LC-8) e decidiu re-auditorias sem julgamento do autor.
- **Negative Evidence:** (a preencher).
- **Contraexemplos:** (a preencher).

### LB-006 — Uma lei universal explica também por que a engenharia falhou? (previsão)

- **Domínios alvo:** Todos.
- **Status:** Previsão registrada (2026-08-03) — a testar **após o SX-001**.
- **Contexto:** não basta uma lei aparecer em projetos bem-sucedidos; uma lei
  verdadeiramente universal também deve **explicar por que um projeto fracassou**.
  Se confirmada, o ECP deixa de ser apenas protocolo para engenharia justificável
  e passa a se comportar como **teoria explicativa da engenharia**.
- **Signals de apoio:** (nenhum ainda — previsão).
- **Negative Evidence:** (a preencher).
- **Contraexemplos:** (a preencher).

---

## Regras

- **Sem respostas antecipadas:** o backlog registra perguntas, não crenças.
- **Negative Evidence obrigatória:** todo item registra o que **não** foi
  encontrado.
- **Prioridade por Diversidade Experimental** ([P-0006](../P-0006-LAW-DISCOVERY.md)):
  itens testáveis em domínios radicalmente diferentes têm prioridade.
- **Genealogia:** quando um item consolidar para LAW-H, registrar a cadeia
  OBS → SIGNAL → PATTERN → LAW-H.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Versão inicial (Aprovado). Abertura do backlog científico com LB-001..LB-004. |
| 1.1 | 2026-08-03 | LB-001 atualizada com resultados do H-001 (positive/negative evidence, SIG-001 preliminar, próximo ataque LC-8). |
| 1.2 | 2026-08-03 | LB-001 passa a exigir **Exogenous Evidence** (Pergunta 2 / P-0007) via Shadow Experiment 001; promoção depende de LC-9 (Observation Independence). |
| 1.3 | 2026-08-03 | Abertura de **LB-005** (decisões deriváveis de critérios pré-congelados — candidata a lei forte, origem P-0007.2) e **LB-006** (previsão: lei explica falhas de engenharia, a testar pós-SX-001). |
