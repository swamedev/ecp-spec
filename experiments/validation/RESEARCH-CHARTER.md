# RESEARCH-CHARTER — Carta de Governança Científica do ECP

| Campo | Valor |
|---|---|
| **Tipo** | Governança científica — **NÃO é** AD, RFC, LAW, schema nem critério |
| **Status** | Ativo |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe (coordenação) |
| **Governado por** | [ROADMAP — Fase C2](../ROADMAP.md), [P-0006](./P-0006-LAW-DISCOVERY.md), [P-0007](./P-0007-INDEPENDENCE.md), [P-0008](./P-0008-CROSS-DOMAIN-VALIDATION.md) |
| **Referências** | [DISCOVERY-LOG](./DISCOVERY-LOG.md), [METHODOLOGICAL-DEBT](./METHODOLOGICAL-DEBT.md) |

## O que mudou na categoria do ECP

O ECP já foi descrito como:

- uma **especificação de engenharia**;
- depois, um **sistema operacional de engenharia**.

Hoje, a descrição correta é:

> **O ECP é um programa de pesquisa sobre engenharia justificável.**

Esta mudança de categoria importa porque o sucesso do projeto **não depende mais
da qualidade dos documentos** — depende da **qualidade das evidências**.

> **Prioridade nº 1:** a pergunta correta deixou de ser "como melhorar o ECP?"
> e passou a ser **"como aumentar a qualidade da evidência produzida?"**.

## Os cinco princípios

### RC-1 — Evidence First

> Nenhuma mudança na teoria pode anteceder novas evidências.

A teoria só evolui **depois** que o [DISCOVERY-LOG](./DISCOVERY-LOG.md) registra
a observação. A inversão é permanente:

```
experimento → dados → observação → DISCOVERY-LOG → (esperar) → outro experimento
→ comparação → somente então mudar a teoria
```

### RC-2 — Experimental Diversity

> Todo novo experimento deve aumentar a diversidade do conjunto.
> Nunca repetir domínio apenas porque é conveniente.

A diversidade é avaliada em domínio × tipo de engenharia × natureza (cf. matriz
do [P-0008](./P-0008-CROSS-DOMAIN-VALIDATION.md)). Repetir a mesma classe de
caso mede **repetição**, não **universalidade**.

### RC-3 — Competing Explanations

> Toda observação deve possuir pelo menos uma explicação concorrente plausível.

Toda entrada do DISCOVERY-LOG carrega, obrigatoriamente, suas `explicações
concorrentes` e `hipóteses concorrentes`. Uma observação sem rival não é uma
observação científica — é uma crença com um rótulo.

### RC-4 — Theory Debt

> Sempre que uma observação não puder ser explicada, a teoria acumula dívida,
> **não o experimento**.

O experimento nunca "falha". Quem falha é a nossa capacidade de explicá-lo.
Quando o Atlas da Engenharia apresentar um caso que o ECP explica mal, isso é
registrado como **dívida de teoria** em [METHODOLOGICAL-DEBT](./METHODOLOGICAL-DEBT.md)
— a teoria é que deve mudar, não o dado.

### RC-5 — Asymmetry

> São necessárias muitas observações para fortalecer uma hipótese; basta **um**
> contraexemplo robusto para obrigar sua revisão.

Esta é a assimetria popperiana. Ela é o freio da Regra de Ouro: dez casos
afirmativos não empladam uma lei; um contraexemplo bem-fundado a derruba.

## A Regra de Ouro, como consequência

> **Nenhuma parte da teoria pode evoluir mais rápido que o conjunto de
> evidências que a sustenta.**

A Regra de Ouro ([DISCOVERY-LOG](./DISCOVERY-LOG.md)) é a consequência direta
dos RC-1 e RC-5. As cinco princípios acima são a sua decomposição operacional.

## Anti-viés de seleção (protocolo do programa)

> **Risco:** se todos os casos forem famosos, altamente documentados, com
> investigações profundas, o ECP pode parecer mais eficaz **simplesmente porque
> esses casos já tiveram sua estrutura causal reconstruída por especialistas**.

Para mitigar, o programa incluirá deliberadamente, ao longo do P-0008:

- projetos **pequenos**;
- casos de **sucesso pouco documentados**;
- **falhas sem investigação oficial**;
- iniciativas de **pequenas empresas**;
- projetos conduzidos por **equipes reduzidas**.

Se a estrutura emergir também nesses contextos, a hipótese de que o ECP captura
regularidades da engenharia fica muito mais forte do que se fossem apenas
grandes desastres amplamente estudados.

## Meta dos próximos 10 experimentos

> **Durante os próximos 10 experimentos, a teoria deve mudar o mínimo possível.**

O objetivo é **colocar o ECP sob pressão**: encontrar casos que ele explica
mal e descobrir onde ele quebra. Se, após uma bateria diversificada de
experimentos independentes, a maior parte da estrutura permanecer estável,
então a teoria foi conquistada não porque evitou ser testada, mas porque
**sobreviveu repetidamente a tentativas de refutação** (RC-5).

### Acordo de estabilidade (FASE E, coordenação 2026-08-04)

A meta acima passa a ser a **missão central** do programa:

> **"Tentar sobreviver sem mudar a teoria."**

Um programa científico maduro demonstra força quando a **mesma estrutura explica
fenômenos muito diferentes sem ser constantemente modificada** — não quando cria
uma hipótese nova a cada experimento.

**Acordo interno até o SX-010:** nenhuma mudança estrutural (novos programas,
ADs, RFCs, leis, entidades, schemas ou critérios; nenhuma alteração no pipeline
congelado; nenhuma migração de estrutura — ex.: DISCOVERY-LOG → banco/grafo —
nem reorganização Theory/Runtime/Lab). Apenas evidência, experimentos,
observações e comparação.

A coordenação acompanha informalmente um **TSI (Theory Stability Index)** —
quantas vezes seguidas executamos experimentos sem mudar a teoria. **Não é
métrica oficial, não está documentado no projeto**; é o critério mental de
liderança que operacionaliza a FASE E.

## Princípio da Conservação da Teoria (coordenação — NÃO entra na especificação)

O maior risco do programa é o **Theory Drift**: ajustar a teoria a cada novo
experimento para acomodar os resultados — uma teoria que explica tudo **porque
foi modificada para explicar tudo** perde poder científico.

> **A teoria deve mudar mais lentamente que as evidências.**

| Ritmo | Mudança permitida |
|---|---|
| 1 experimento | nenhuma |
| 2 experimentos | provavelmente nenhuma |
| 5 experimentos | talvez uma observação |
| 10 experimentos | talvez uma hipótese |
| dezenas de experimentos | talvez uma revisão da teoria |

### Orçamento de mudanças (disciplina da coordenação — não é artefato)

Até o SX-010: **0 leis, 0 entidades, 0 critérios, 0 schemas, 0 RFCs, 0 ADs.**
O único ativo que pode crescer é: experimentos, observações, Atlas, Discovery
Log.

### Unidade de análise: o conjunto, não o caso

A unidade de análise deixa de ser o caso isolado e passa a ser o **Conjunto
SX-001..SX-010** — ciência trabalha com distribuição, não com exemplos isolados.

### Atlas da Engenharia = principal produto científico

O Atlas deixa de ser documentação e passa a ser o **principal produto científico
do ECP**: caso a caso — entidades emergidas/não-emergidas, EAR, EER, explicações
concorrentes, contraexemplos, estabilidade. "Onde está a evidência?" → **"Olhe o
Atlas."**

### Declaração oficial: fim da Fase de Arquitetura

> **A Fase de Arquitetura terminou.** O projeto não é mais conduzido
> principalmente por arquitetos — é conduzido por **pesquisadores**, que passam
> muito mais tempo coletando dados do que inventando estruturas. A FASE E
> permanece **inalterada até o SX-010**.

## Status atual

- **Aberto:** 2026-08-03.
- **Entrada em vigor:** imediata; aplica-se aos próximos experimentos do P-0008
  (SX-002 em diante).
- Nenhum AD/RFC/LAW/schema criado. A carta é governança, não é especificação.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Carta de governança científica: RC-1..RC-5, Regra de Ouro, anti-viés de seleção, meta dos próximos 10 experimentos. |
| 1.1 | 2026-08-04 | FASE E — Acordo de estabilidade até o SX-010: nenhuma mudança estrutural; missão central passa a ser "tentar sobreviver sem mudar a teoria". TSI (Theory Stability Index) como indicador informal de coordenação, não-métrico. |
| 1.2 | 2026-08-04 | Princípio da Conservação da Teoria (a teoria muda mais lentamente que as evidências); orçamento de mudanças até SX-010 (0 leis/entidades/critérios/schemas/RFCs/ADs); unidade de análise = Conjunto SX-001..SX-010; Atlas como principal produto científico; declaração oficial de fim da Fase de Arquitetura. |