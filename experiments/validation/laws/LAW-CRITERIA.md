# LAW-CRITERIA — Critérios de Aceitação de Leis

| Campo | Valor |
|---|---|
| **Tipo** | Documento científico de trabalho (não-RFC, não-AD) |
| **Status** | Congelado |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe |
| **Governado por** | [P-0006 — Law Discovery Program](../P-0006-LAW-DISCOVERY.md), [P-0007 — Independence Program](../P-0007-INDEPENDENCE.md) |
| **Referências** | [LAW-BACKLOG](./LAW-BACKLOG.md), [LAW-METRICS](./LAW-METRICS.md), [ECP-012](../../ECP/ECP-012.md) |

## A pergunta

> **Quando podemos afirmar que descobrimos uma lei?**

Não basta sobreviver a experimentos. Uma lei precisa possuir **propriedades**.

## Por que este documento está congelado

Os critérios de aceitação são definidos **antes dos resultados, nunca depois**.
Congelá-los antes do primeiro experimento hostil impede que sejam ajustados
*post hoc* para acomodar achados. É um princípio fundamental da boa ciência.

## Critérios

### LC-1 — Universalidade

A lei deve sobreviver em **domínios distintos**. Não basta Software: precisa
sobreviver em Engenharia, Jogos, IA, Pesquisa, Civil, Robótica, etc.

### LC-2 — Independência

A lei **não pode depender de tecnologia**. Se amanhã surgir outra linguagem,
framework ou ferramenta, ela continua válida.

### LC-3 — Necessidade

A pergunta mais importante:

> **Se a lei for falsa, o projeto ainda consegue existir?**

Se sim, provavelmente **não é lei**.

### LC-4 — Predição

Ela precisa **prever algo**, não apenas explicar o passado (Predictive Index —
[LAW-METRICS](./LAW-METRICS.md)).

### LC-5 — Refutabilidade

Precisa existir um **experimento capaz de destruí-la**. Caso contrário, é
filosofia, não ciência.

### LC-6 — Reprodutibilidade

Outro pesquisador deve conseguir **chegar à mesma conclusão** a partir dos
mesmos artefatos (avaliadores independentes).

### LC-7 — Minimalidade

Ela **não pode ser consequência** de outra lei já aceita (parcimônia).

### LC-8 — Não circularidade

Uma lei **nunca pode depender dela própria** — nem ser verdadeira apenas por
definição do modelo que a contém.

### LC-9 — Observation Independence (Independência Observacional)

A hipótese precisa ter evidência de **pelo menos um contexto** onde o
**observador** não conhece o ECP, o **executor** não conhece o ECP e o
**projeto** não segue o ECP. Sem evidência exógena, uma "lei" pode ser apenas
verdade por definição (analítica — descoberta do H-001; [P-0007](../P-0007-INDEPENDENCE.md)).

### LC-10 — Evidence Independence (Independência de Evidência) — **HIPÓTESE**

> Uma hipótese de lei somente pode ser fortalecida quando as evidências
> utilizadas possuem **origem causal independente**. Fontes derivadas de um mesmo
> evento documental contam como **uma única origem** de evidência.

**Status: hipótese** (não integra o gate obrigatório até validação na prática).
Exemplo: Apollo 13 — NASA, Wikipédia e um livro são três fontes, mas uma única
origem (relatório da NASA). Evita inflar artificialmente a confiança.
Regras operacionais em [P-0007.1 — Independence Framework](../P-0007.1-INDEPENDENCE-FRAMEWORK.md)
(RA-EI-001..005).

## Regras de aplicação

1. Para promover uma hipótese a **Candidate Universal Law**, **todos** os
   critérios **LC-1..LC-9** devem ser atendidos. **LC-10 é hipótese** e só
   entra no gate quando validada na prática (SX-001+).
2. A ausência de qualquer critério **impede a promoção** — não há promoção
   parcial por compensação.
3. A promoção exige **ambas** as evidências:
   - **Endogenous Evidence** — sobreviveu aos experimentos hostis (funil interno);
   - **Exogenous Evidence** — emerge fora do ECP (Observation Independence, LC-9);
   - **≥ 3 domínios independentes** para LAW-C (Domain Independence — RA-DI-003).
4. Os critérios permanecem congelados até que um experimento demonstre uma
   **lacuna real** (Regra 1 — [P-0006](../P-0006-LAW-DISCOVERY.md)).

## Nota

Estes critérios são **os axiomas de aceitação** do programa. Assim como a
matemática parte de axiomas, o ECP parte de critérios de aceitação — e é contra
eles que toda lei candidata será julgada, inclusive nas tentativas deliberadas
de destruí-la (Fase C). A partir da v1.1, toda LAW-H também responde **duas
perguntas**: (1) sobrevive aos experimentos hostis? e (2) continua verdadeira se
o ECP desaparecer? — governadas pelo [P-0007](../P-0007-INDEPENDENCE.md).

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Versão inicial (**Congelado antes do H-001**). Critérios LC-1..LC-8. |
| 1.1 | 2026-08-03 | **LC-9 — Observation Independence** adicionado (por decisão do Arquiteto-Chefe, após descoberta LC-8 no H-001). Regra de promoção exige Endogenous **e** Exogenous Evidence (Candidate Universal Law). Abertura do Independence Program (P-0007). |
| 1.2 | 2026-08-03 | **LC-10 — Evidence Independence** registrada como **hipótese** (origens causais independentes; fontes derivadas do mesmo evento contam como uma origem). Não integra o gate até validação. LAW-C exige ≥ 3 domínios independentes (RA-DI-003). Governado pelo P-0007.1 — Independence Framework. |
