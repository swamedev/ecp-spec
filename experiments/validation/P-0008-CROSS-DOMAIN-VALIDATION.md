# P-0008 — Cross-Domain Validation Program

| Campo | Valor |
|---|---|
| **Tipo** | Programa de pesquisa (Validation Program) |
| **Status** | Aberto |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe (coordenação 2026-08-03) |
| **Governado por** | [ECP-012](../../ECP/ECP-012.md), [AD-007](../../04-governance/AD-007.md), [P-0006](./P-0006-LAW-DISCOVERY.md), [P-0007](./P-0007-INDEPENDENCE.md), [RESEARCH-CHARTER](./RESEARCH-CHARTER.md) |
| **Referências** | [DISCOVERY-LOG](./DISCOVERY-LOG.md), [SX-001](./independence/SX-001/README.md), [SHADOW-EXPERIMENTS](./independence/SHADOW-EXPERIMENTS.md), [SX-SELECTION](./independence/SX-SELECTION.md), [SIGNAL-SCHEMA](./signals/SIGNAL-SCHEMA.yaml), [LAW-CRITERIA](./laws/LAW-CRITERIA.md), [METHODOLOGICAL-DEBT](./METHODOLOGICAL-DEBT.md) |

## O que motivou este programa

Até o SX-001, a validação do ECP era:

```
ECP → gera experimentos → os experimentos confirmam o ECP
```

Um ciclo inevitavelmente **endógeno**.

Com o SX-001 (Challenger), o fluxo mudou:

```
Caso histórico (Challenger) → Atomic Facts → Kernel → Reconstrução → Comparação com Rogers Commission
```

O mundo passou a ser a referência. Isso muda o **status epistemológico** do
projeto: o ECP passou a ser confrontado com uma realidade independente da sua
própria especificação. O SX-001 produziu **uma** observação promissora
(`EAR(Challenger) = 0.775`, e o achado `Evidence → Decision` em
[DISCOVERY-LOG](./DISCOVERY-LOG.md)). Um caso não calibra métrica nem
estabelece universalidade.

> **Pergunta que abre o programa:** o SX-001 pode ter sido um caso
> especialmente favorável ao ECP. Precisamos descobrir se a mesma estrutura
> emerge espontaneamente em domínios completamente diferentes.

## Objetivo

> **Construir o Atlas da Engenharia — não descobrir novas leis.**

O P-0008 não se limita a medir estabilidade. Ele constrói um **mapa comparativo**
da estrutura cognitiva emergente em múltiplos domínios. Depois de alguns
experimentos, deixamos de ter apenas experimentos isolados: passamos a ter um
**Atlas** — e esse mapa provavelmente vale mais que qualquer lei individual.

Estrutura de registro por domínio:

```
Domínio
  ↓
Entidades emergentes
  ↓
Topologia cognitiva
  ↓
EAR
  ↓
EER
  ↓
Signals
  ↓
Hipóteses concorrentes
  ↓
Status
```

Vista comparativa (objetivo):

```
Domínio       Topologia        EER    EAR
Challenger    P→G→K→A→E→D      7/10   0.775
Apollo 13     ...              ...    ...
Medicina      ...              ...    ...
Construção    ...              ...    ...
```

A pergunta central permanece:

> **"Esta mesma estrutura emerge espontaneamente em domínios completamente
> diferentes?"**

— e, agora, com a segunda pergunta do programa (ver §"Duas perguntas"):
> **"Ela explica melhor do que explicações alternativas?"**

## Anti-viés de seleção (RC-2 — Experimental Diversity)

O conjunto de casos **não** pode ser dominado por grandes desastres amplamente
estudados — isso inflaria a aparente eficácia do ECP, pois esses casos já
tiveram sua estrutura causal reconstruída por especialistas. Conforme
[RESEARCH-CHARTER](./RESEARCH-CHARTER.md), o programa incluirá deliberadamente:

- projetos **pequenos**;
- casos de **sucesso pouco documentados**;
- **falhas sem investigação oficial**;
- iniciativas de **pequenas empresas**;
- projetos conduzidos por **equipes reduzidas**.

Se a estrutura emergir nesses contextos, a hipótese de que o ECP captura
regularidades da engenharia fica muito mais forte.

## Domínios-alvo

```
Software
  ↓
Aeronáutica          (SX-001 — Challenger ✓)
  ↓
Medicina
  ↓
Construção Civil     (ex.: Hyatt Regency)
  ↓
Finanças
  ↓
Política Pública
  ↓
Pesquisa Científica
  ↓
...
```

A seleção de cada caso segue o **protocolo congelado**
[SX-SELECTION](./independence/SX-SELECTION.md) — nunca por preferência.

## Candidatos imediatos (origens independentes já verificadas em SX-CANDIDATES)

| Caso | Domínio | Tipo |
|---|---|---|
| **Apollo 13** | Aeroespacial | Postmortem |
| **Deepwater Horizon** | Energia/Indústria | Postmortem |
| **Hyatt Regency** (passarelas) | Construção Civil | Postmortem |
| **Genoma Humano** | Pesquisa Científica | Projeto real |
| **Operation Warp Speed** | Saúde Pública | Projeto real |
| **Chernobyl** | Energia Nuclear | Postmortem |
| **Ebola** | Saúde Pública | Resposta |

> Estes casos já passaram pela etapa 5 (acessibilidade de fontes) do
> SX-SELECTION. A seleção definitiva de SX-002..SX-00n é do protocolo, não deste
> programa.

## Critério de seleção: maximizar diversidade (não repetir casos)

O objetivo **não** é repetir casos semelhantes — é **maximizar a diversidade
experimental**. A seleção de SX-002 não assume Apollo 13 apenas porque ele veio
em primeiro lugar na lista de candidatos; o protocolo procura a combinação de
maior diversidade em relação ao SX-001 e aos já executados.

Matriz de diversidade (objetivo):

```
SX      Domínio          Tipo de Engenharia   Natureza
SX-001  Aeroespacial     Física               Falha
SX-002  Saúde            Biomédica            Sucesso
SX-003  Infraestrutura   Civil                Colapso
SX-004  Pesquisa         Científica           Sucesso
SX-005  Logística        Industrial           Sucesso
SX-006  Energia          Petróleo             Falha
```

A diversidade é avaliada em três eixos: **domínio** (setor), **tipo de
engenharia** (física, biomédica, civil, científica, industrial) e **natureza**
(falha/colapso vs. sucesso). O SX-002 deve ser escolhido de modo a maximizar a
distância nos três eixos em relação ao Challenger — por exemplo, um **sucesso**
em um domínio **não-aeroespacial** com **tipo de engenharia diferente**.

## Duas perguntas (não apenas uma)

O programa mede **duas** coisas, nesta ordem:

> **Pergunta 1 — A estrutura aparece?** ("Esta mesma estrutura emerge
> espontaneamente em domínios completamente diferentes?")

> **Pergunta 2 — Ela explica melhor?** ("Ela aparece melhor do que explicações
> alternativas?")

A Pergunta 2 é a mais importante: um programa científico não precisa apenas
**explicar** — precisa **explicar melhor** que as hipóteses concorrentes
(sociologia organizacional, teoria da decisão clássica, análise de causa-raiz
tradicional, viés do executor, ...). Toda observação registrada no
[DISCOVERY-LOG](./DISCOVERY-LOG.md) carrega, obrigatoriamente, suas
`explicações concorrentes` e `hipóteses concorrentes`.

## Método (por caso)

Cada caso segue o mesmo pipeline do SX-001 (congelado — sem alterações
metodológicas durante a execução):

1. **Narrativa Original** — zero ECP.
2. **Atomic Facts** — fatos mínimos, sem interpretação.
3. **Reconstrução Cega** — só Atomic Facts + Kernel; entidades emergem.
4. **Alignment Analysis** — MATCH / PARTIAL_MATCH / NOT_EXPLAINED / NEW_INSIGHT.
5. **Signals** — só os suportados pelo alignment.
6. **`EAR(<caso>)`** — observação, não conclusão.
7. **Topologia do grafo cognitivo** — o que importa não é só o EAR: é se a
   cadeia `Problem → Goal → Knowledge → Assumption → Evidence → Decision`
   **continua emergindo**, ou se surge algo **diferente**. Uma cadeia diferente
   vale mais que qualquer EAR — pode sinalizar uma entidade ausente no Kernel.

Limitações do método encontradas **durante** a execução → registradas em
[METHODOLOGICAL-DEBT](./METHODOLOGICAL-DEBT.md), para a v1.1. **Nunca**
corrigidas no meio do experimento (Princípio da Suficiência Metodológica).

## O que o programa mede

Para cada caso: `EAR(caso)`, a **topologia** do grafo emergente, e a
presença/ausência das entidades da cadeia. Depois de vários casos:

| Pergunta | Resposta possível |
|---|---|
| `EAR(Apollo 13)` ≈ `EAR(Challenger)`? | Estabilidade entre domínios. |
| O elo `Evidence → Decision` reaparece? | Consolida ou refuta DL-001. |
| As ausências (Problem/Risk/validação) reaparecem? | Consolida ou refuta DL-002. |
| A cadeia emerge em todos os domínios? | Consolida ou refuta DL-003. |
| A cadeia é a **mesma** ou muda de topologia? | Sinal de entidade ausente no Kernel. |
| A leitura ECP explica **melhor** que as concorrentes? | Base para promoção (Pergunta 2). |
| A EER acumula padrão entre casos? | Base empírica ontologia vs. implementação. |

## Uso dos resultados

Os resultados **alimentam** a frente Inferência Científica apenas quando os
critérios objetivos forem satisfeitos:

- **SIG-001** — "decisão justificável depende de conhecimento": se aparecer em
  ≥2 domínios de origens independentes **e** explicar melhor que as
  concorrentes, torna-se admissível (RA-SIG-001).
- **SIG-002 / SIG-003** — candidatos: idem.
- **Nenhuma LAW-H é escrita com base em um único caso.** A pergunta "até onde
  essa estrutura é realmente universal?" só pode ser respondida com a
  distribuição — que é exatamente o que este programa constrói.

> **Anti-armadilha (coordenação):** não promover `Evidence → Decision` a LAW-H
> agora. A hipótese concorrente — *"o Challenger é um caso especialmente
> favorável ao ECP"* — só pode ser refutada por evidência cross-domain.

## Relação com os demais programas

| Programa | Relação |
|---|---|
| P-0006 (Law Discovery) | P-0008 produz a distribuição; P-0006 usa os critérios de promoção. |
| P-0007 (Independence) | P-0008 garante que cada caso seja de origem **independente** do ECP (exógena). |
| DISCOVERY-LOG | Cada caso atualiza as observações DL-### (status Observação → Confirmado → …). |
| P-0009 (Competitive Theory Validation) | Após um conjunto consistente de casos, P-0009 acrescenta o eixo comparativo: a leitura ECP deve explicar **mais** que rivais (STAMP, Swiss Cheese, FRAM, RCA, OODA, Systems Thinking) nos mesmos casos — base para promoção, não apenas evidência interna. |
| P-0010 (Reproducibility) | Gate **antes** da expansão: a etapa Narrativa → Atomic Facts → Reconstrução deve ser estável entre avaliadores independentes. SX-002+ só são comparáveis ao SX-001 se o protocolo — não o executor — produzir o mesmo conjunto de fatos ([P-0010](./P-0010-REPRODUCIBILITY.md)). |

## Regra do programa (preservada)

> **Não se descobre lei por acumulação de casos favoráveis; descobre-se
> estabilidade por comparação entre domínios. Se a estrutura continuar surgindo
> em contextos radicalmente diferentes, a discussão deixa de ser "o ECP funciona
> neste caso?" e passa a ser "até onde essa estrutura é realmente universal?".**

> **Regra comparativa (P-0009):** a pergunta final não é "o ECP explica?" — é
> "o ECP explica **melhor**?". A evidência interna do Atlas (Pergunta 1) habilita
> a Pergunta 2 (melhor que rivais), executada pelo [P-0009](./P-0009-COMPETITIVE-THEORY-VALIDATION.md).

## Ordem de trabalho

```
1. SX-001 (Challenger) — concluído (EAR(Challenger) = 0.775, observação)
2. ESTUDO DE REPRODUTIBILIDADE (P-0010): validar a estabilidade da etapa
   Narrativa → Atomic Facts → Reconstrução entre avaliadores independentes
   (humanos e/ou LLMs diferentes) — medir cobertura/divergência/concordância/
   conflitos; AFR como observação
3. Selecionar SX-002 pelo protocolo congelado com critério de DIVERSIDADE
   MÁXIMA em relação ao SX-001 (domínio × tipo de engenharia × natureza) e
   evitando o caso mais famoso (anti memória coletiva — coordenação)
4. Executar o pipeline completo do SX-002 (incluindo topologia do grafo)
5. Comparar EAR, topologia e entidades entre SX-001 × SX-002
6. Registrar no DISCOVERY-LOG (incluindo EER observacional) e nos Signals
7. Repetir para SX-003..SX-00n sempre maximizando diversidade (matriz §acima),
   incluindo deliberadamente casos de baixa documentação / pequenas equipes
   (anti-viés de seleção — RESEARCH-CHARTER)
8. Só então: avaliar a distribuição, a EER e eventual consolidação de
   DL-###/SIG-### (explicando melhor que as hipóteses concorrentes)
9. Após um conjunto consistente de casos: iniciar a execução do
   [P-0009](./P-0009-COMPETITIVE-THEORY-VALIDATION.md) (matriz EAR(ECP) ×
   EAR(rivais)) — nenhuma promoção de LAW-H com base apenas em evidência interna
```

## Meta dos próximos 10 experimentos (coordenação)

> **Durante os próximos 10 experimentos, a teoria deve mudar o mínimo possível.**

O objetivo é colocar o ECP sob pressão: encontrar casos que ele **explica mal**
e descobrir onde ele **quebra**. Se, após uma bateria diversificada de
experimentos independentes, a maior parte da estrutura permanecer estável, a
teoria terá sido conquistada não porque evitou ser testada, mas porque
**sobreviveu repetidamente a tentativas de refutação** (RC-5, RESEARCH-CHARTER).

Casos que o ECP explica mal não são falhas do experimento — são **dívida de
teoria** (RC-4).

## Status atual

- **Aberto:** 2026-08-03, após o SX-001.
- **SX-002:** pendente de seleção automática pelo protocolo congelado, com
  critério de diversidade máxima (Saúde + Sucesso + Biomédica é o alvo da
  matriz, sujeito à decisão do protocolo).
- **Sem novas leis, schemas, critérios ou métricas** — P-0008 é um programa de
  experimentação, não de construção (Regra 1 do P-0006 preservada). A EER é uma
  observação no [DISCOVERY-LOG](./DISCOVERY-LOG.md), **não** uma métrica
  oficial.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Abertura do Cross-Domain Validation Program (coordenação pós-SX-001). Objetivo: medir estabilidade, não descobrir leis. Candidatos Apollo 13, Deepwater Horizon, Hyatt Regency, Genoma, Warp Speed, Chernobyl, Ebola. Regra anti-promoção precoce. |
| 1.1 | 2026-08-03 | Duas perguntas (aparece? + explica **melhor**?); detalhe na topologia do grafo cognitivo como achado prioritário; critério de **diversidade máxima** (matriz domínio×tipo×natureza) para seleção de SX-002+; EER observacional referenciada ao DISCOVERY-LOG. |
| 1.2 | 2026-08-03 | Objetivo ampliado: **Atlas da Engenharia** (mapa comparativo: domínio → entidades → topologia → EAR → EER → Signals → hipóteses concorrentes → status). Anti-viés de seleção (casos pequenos/pouco documentados). Governado por RESEARCH-CHARTER. Meta dos próximos 10 experimentos (teoria muda o mínimo possível; explicações ruins = dívida de teoria). |
| 1.3 | 2026-08-03 | Estudo de reprodutibilidade (P-0010) inserido como passo 2 antes do SX-002; regra anti memória coletiva na seleção do SX-002 (evitar o caso mais famoso); relação com P-0010 adicionada. |
