# ECP-GLOSSARY — Semântica Formal Congelada

| Campo | Valor |
|---|---|
| **Tipo** | Documento de Validação (`VALID`) |
| **Fase** | V0 — Validation |
| **Status** | Rascunho |
| **Versão** | 0.2.0 |
| **Data** | 2026-08-02 |
| **Autores** | ECP Contributors |
| **Objetivo** | Congelar o significado formal de cada entidade do ECP |

> **Regra do documento:** não se aceita sinônimo. Cada termo tem **um** significado. Se dois documentos usarem o mesmo termo com sentidos diferentes, este documento vence até que a fundação seja corrigida.
>
> **Vida útil:** o ECP-GLOSSARY evolui junto com a fundação. Quando congelado (ex.: versão 1.0), uma cópia estável migra para `08-reference/`; a versão editável permanece aqui durante o desenvolvimento.

Formato canônico de cada entrada:

```
TERMO
É:            <definição formal, única>
NÃO É:        <negações explícitas>
RELACIONAMENTOS: <arestas do grafo em que o termo participa>
EXEMPLOS:     <ocorrências positivas>
CONTRAEXEMPLOS: <ocorrências que parecem mas NÃO são o termo>
RFC DE ORIGEM:  <documento que define o termo>
VERSÃO:       <semver do termo>
```

---

## Entidades da cadeia congelada

### PROBLEM

```
É:            Uma condição verificável, com causa e impacto, que
              motiva a existência de um projeto. Formalizado em um
              Problem Record (P-…).
NÃO É:        Uma solução desejada. Não é um sintoma não investigado.
RELACIONAMENTOS: Goal RESOLVE Problem; Claim rastreia Problem;
              Evidence PROVA Problem; Decision contribui para Goal
              (e, por ele, ao Problem).
EXEMPLOS:     "Fechamento do caixa leva 4 horas (medido, com causa)."
CONTRAEXEMPLOS: "Quero um ERP." (solução imaginada, não problema);
              "O sistema é lento" (sintoma sem causa).
RFC DE ORIGEM:  ECP-003
VERSÃO:       0.1.0
```

### GOAL

```
É:            Um estado de mundo desejado, observável e verificável,
              que RESPONDE a um Problem. Formalizado em um Goal
              Record (G-…) com campo `problem` obrigatório.
NÃO É:        Um rótulo de projeto. Não é um desejo sem critério de
              verificação. Não existe sem um Problem de origem.
RELACIONAMENTOS: Problem → Goal (resolução); Goal → Claim (claims o
              servem); Goal → Decision (decisões o servem); Goal é
              verificado por Evidence via success criteria.
EXEMPLOS:     "Reduzir fechamento do caixa para < 15 min em 90% dos
              dias."
CONTRAEXEMPLOS: "Fazer um ERP."; "Melhorar o sistema." (sem métrica);
              "Ser a empresa líder de mercado" (não observável como
              estado de projeto).
RFC DE ORIGEM:  ECP-004
VERSÃO:       0.2.0
```

### CLAIM

```
É:            Uma proposição declarada, avaliável como verdadeira ou
              falsa, que sustenta decisões e exige suporte de
              evidência. Formalizado em um Claim Record (C-…) com
              campos `problem` e `goal`.
NÃO É:        Uma opinião (sem pretensão de verdade). Não é um fato
              assumido (conhecimento ou suposição). Não é uma decisão
              (o Claim é a afirmação; a decisão é consequência).
RELACIONAMENTOS: Claim SUSTENTA Decision; Evidence SUSTENTA Claim;
              Claim pode DEPENDER de Assumption; Goal é alvo de Claims.
EXEMPLOS:     "A latência da chamada é < 100 ms."
CONTRAEXEMPLOS: "Acho que essa arquitetura é melhor." (sem claim
              declarada); "O framework é popular" (fato de contexto).
RFC DE ORIGEM:  ECP-005
VERSÃO:       0.2.0
```

### KNOWLEDGE

```
É:            Informação suportada por evidência avaliável,
              organizada em função dos goals. Distingue-se de Claim
              por ser aceita (não em disputa). Lacunas são ausências
              de conhecimento, não conhecimento.
NÃO É:        Crença não verificada. Não é a totalidade do que se
              "sabe informalmente". Não é Claim em disputa.
RELACIONAMENTOS: Knowledge alimenta Decision; lacunas de Knowledge
              GERAM Assumption; Knowledge distingue fato de Claim.
EXEMPLOS:     "A legislação exige NF-e para esta operação" (com
              fonte citada).
CONTRAEXEMPLOS: "Todo mundo sabe que X funciona" (sem evidência
              avaliável).
RFC DE ORIGEM:  ECP-006
VERSÃO:       0.3.0
```

### ASSUMPTION

```
É:            Afirmação tratada como verdadeira SEM evidência plena,
              registrada, classificada por impacto e monitorada.
              Um risco declarado, não conhecimento. Formalizado em um
              Assumption Record (A-…).
NÃO É:        Conhecimento. Não é erro (é decisão consciente de
              progredir com incerteza declarada). Não é Claim
              (o Claim exige suporte; a suposição é assumida).
RELACIONAMENTOS: Knowledge INCOMPLETO → Assumption; Assumption
              SUSTENTA Claim e Decision; invalidação de Assumption
              TORNA Decision SUSPEITA; Assumption referencia Goal.
EXEMPLOS:     "A legislação fiscal não muda durante o projeto."
CONTRAEXEMPLOS: "A legislação fiscal não muda" assumido SEM registro.
RFC DE ORIGEM:  ECP-007
VERSÃO:       0.2.0
```

### CONSTRAINT

```
É:            Limite que vincula as soluções possíveis: tempo, custo,
              recursos, normas, escopo. É informação sobre o espaço de
              decisão — explorada, não contornada (P-6).
NÃO É:        Desculpa para não decidir. Não é restrição secreta não
              declarada. Contornar com registro e autorização é
              renegociação (decisão), não violação.
RELACIONAMENTOS: Decision respeita Constraint; Goal define estado
              dentro de Constraints; renegociação de Constraint é uma
              Decision.
EXEMPLOS:     "Prazo: 8 semanas." "Orçamento: R$ 120k." "IEC 62304."
CONTRAEXEMPLOS: "Vamos entregar quando der." (prazo implícito não
              declarado).
RFC DE ORIGEM:  ECP-000 (definição formal) / ECP-004 (declaração)
VERSÃO:       0.1.0
```

### ALTERNATIVE

```
É:            Uma opção real considerada explicitamente em uma
              decisão. Toda decisão deve considerar pelo menos duas
              alternativas. A alternativa descartada é tão rastreável
              quanto a escolhida.
NÃO É:        Uma opção de fachada incluída só para cumprir o modelo.
              Não é a escolha final. Não é variação semântica da mesma
              opção.
RELACIONAMENTOS: Decision AVALIA Alternative por critérios; Evidence
              alimenta os critérios; serendipidade GERA alternative.
EXEMPLOS:     "SaaS vs. on-premise", "REST vs. gRPC".
CONTRAEXEMPLOS: "Fazer X vs. não fazer X" sem justificativa real;
              alternativas idênticas renomeadas.
RFC DE ORIGEM:  ECP-009 (componente obrigatório da decisão)
VERSÃO:       0.3.0
```

### EVIDENCE

```
É:            Observação registrada e avaliável que sustenta uma
              afirmação (Claim ou Assumption). Classificada por força
              (hierarquia ECP-008). Confiança é calculada A PARTIR de
              evidência — nunca declarada.
NÃO É:        Opinião de especialista sem fonte. Não é intenção. Não é
              "confiança subjetiva". Não é prova por autoridade
              (citação com fonte rastreável é nível 3, contexto).
RELACIONAMENTOS: Evidence SUSTENTA Claim e Assumption; Evidence
              ALIMENTA Confidence e Risk; Evidence PROVA Problem;
              Decision registra evidências utilizadas.
EXEMPLOS:     "Teste de 30 dias com 90% dos fechamentos < 15 min."
CONTRAEXEMPLOS: "O especialista garantiu que funciona."
RFC DE ORIGEM:  ECP-008
VERSÃO:       0.3.0
```

### DECISION

```
É:            Escolha deliberada entre alternativas, justificada por
              um goal, restrições e evidências, e registrada como
              Decision Record (D-…) com campos `problem`, `goal`,
              `claims_sustentados`, `suposições_utilizadas`,
              `evidências_utilizadas`, `confiança`, `risco`,
              `decisão`, `resultado_observado`.
NÃO É:        O fluxo (a decisão é a causa; o fluxo é consequência —
              L-0). Não é reflexo (sem alternativas). Não é preferência
              sem critérios. Não é opinião não registrada.
RELACIONAMENTOS: Decision É autorizada por Evidence+Confidence; é
              dirigida por Goal; sustenta-se em Claim/Assumption;
              muda State; gera Artifact; é rastreável a Problem (L-1).
EXEMPLOS:     "Avançar para Planning (confiança 0.92, evidência E-014)."
CONTRAEXEMPLOS: "Seguimos o fluxo porque é o passo 3." (sem decisão).
RFC DE ORIGEM:  ECP-009
VERSÃO:       0.3.0
```

### ARTIFACT

```
É:            Produto material de decisões: código, plano, modelo,
              documento, teste, contrato. Sem a decisão que o
              justifica, um artefato é dívida (P-4). Todo artefato é
              rastreável a Decision → Goal → Problem (L-1).
NÃO É:        O produto do projeto (o produto durável é o
              conhecimento validado — P-3). Não é o objetivo. Não é
              finalidade em si.
RELACIONAMENTOS: Artifact É consequência de Decision; rastreia a
              Goal e Problem; Knowledge sobrevive ao Artifact.
EXEMPLOS:     Build, protótipo, contrato, documentação, relatório.
CONTRAEXEMPLOS: Código gerado sem decisão registrada (dívida);
              "o entregável é o objetivo" (inversão de finalidade).
RFC DE ORIGEM:  ECP-000 (P-2, P-3, P-4) / ECP-001 (contratos)
VERSÃO:       0.1.0
```

---

## Entidades de apoio

### RISK

```
É:            Combinação de impacto × probabilidade de consequência
              adversa de uma decisão. Sempre avaliado em par: risco da
              transição e risco do não-avanço.
NÃO É:        Um sentimento de apreensão. Não é uma suposição (o risco
              é quantificado; a suposição é assumida como verdade).
RELACIONAMENTOS: Decision AVALIA Risk; Risk deriva de Evidence e
              supõe consequências; supõe apetite de risco declarado.
EXEMPLOS:     "Risco 0.3 × 0.4 = 0.12 com mitigação → residual 0.02."
CONTRAEXEMPLOS: "Isso é arriscado, acho melhor não." (sem
              quantificação).
RFC DE ORIGEM:  ECP-008
VERSÃO:       0.3.0
```

### STATE

```
É:            Condição verificável do grafo de conhecimento em um ponto
              do tempo — uma PROJEÇÃO observável, não o modelo
              subjacente. Nenhum estado é alcançado por sequência
              (L-0).
NÃO É:        O modelo do projeto (o grafo é o modelo). Não é um
              roteiro a percorrer.
RELACIONAMENTOS: State É alcançado por Decision; State é projeção do
              grafo; contratos definem EXIT/FAILURE do estado.
EXEMPLOS:     Discovery, Research, Planning, Execution, Validation.
CONTRAEXEMPLOS: "O próximo estado é sempre Planning." (fila, não
              decisão).
RFC DE ORIGEM:  ECP-000 (Seção 4) / ECP-001 (contratos)
VERSÃO:       0.1.0
```

### CAPABILITY

```
É:            O que uma entidade pode fazer, declarado de forma
              verificável (ler, escrever, executar, verificar,
              pesquisar, lembrar). A capacidade mínima de registro é
              precondição de conformidade.
NÃO É:        Um atributo de pessoa ou modelo de IA. Não é
              afirmação de qualidade ("bom em X").
RELACIONAMENTOS: Capability mapeia para Contract executável;
              entidade assume capacidades declaradas.
EXEMPLOS:     "Executar testes", "acessar a API", "registrar decisões".
CONTRAEXEMPLOS: "Raciocina bem", "entende o negócio" (não verificável).
RFC DE ORIGEM:  ECP-001 (Camada 2, 02-core)
VERSÃO:       0.1.0
```

### CONTRACT

```
É:            Especificação de entradas, saídas, invariantes e
              condições de saída de um estado. Unidade fundamental de
              comportamento do ECP, com `PRECONDITIONS`, `INPUTS`,
              `OUTPUTS`, `REQUIRED`, `EXIT`, `FAILURE` (obrigatório) e
              `EVIDENCE`. `EXIT` é avaliado por decisão, nunca por
              sequência.
NÃO É:        Um prompt. Não é uma instrução de estilo. Não é um
              template de resposta.
RELACIONAMENTOS: Contract define STATE; EXIT alimenta Decision;
              FAILURE define transição de falha (P-7).
EXEMPLOS:     CONTRACT discovery (ECP-001 §7.3).
CONTRAEXEMPLOS: "Antes de responder, pense passo a passo." (prompt).
RFC DE ORIGEM:  ECP-001 (Seção 7)
VERSÃO:       0.1.0
```

### PROCESSAMENTO

```
É:            Execução mecânica determinística de uma regra fixa
              (algoritmo, protocolo, reflexo treinado) que não exige
              escolha entre alternativas. Não é governado pela Lei
              Zero: não gera Decision Record.
NÃO É:        Decisão (escolha deliberada entre alternativas — L-0).
              Não é ausência de controle (todo processamento é
              executado dentro de uma decisão que o autorizou).
RELACIONAMENTOS: Decision AUTORIZA Processamento; Processamento NÃO
              autoriza transições; Processamento executa o efeito de
              uma decisão já tomada.
EXEMPLOS:     Aplicar um patch já aprovado; rodar um build já
              autorizado; executar a rotina de backup.
CONTRAEXEMPLOS: "Avançar para Execution" (transição, exige decisão);
              "Escolhi entre REST e gRPC" (decisão).
RFC DE ORIGEM:  ECP-000 (Seção 5, nota de escopo L-0)
VERSÃO:       0.1.0
```

### EXPLORAÇÃO

```
É:            Aquisição de conhecimento sem goal formalizado —
              atividade pré-projeto que produz o Problem Record de
              entrada. A formalização do problema é o critério de
              entrada no protocolo (ECP-003.1).
NÃO É:        Projeto (não gera entidades sujeitas à L-1). Não é
              pesquisa dentro do projeto (essa já tem goal). Não é
              não-registro (a exploração produz conhecimento
              utilizável, mesmo que pré-entidades).
RELACIONAMENTOS: Exploração PRODUZ Problem Record; Problem formaliza
              o início do projeto; exploração usa Capability de
              pesquisa.
EXEMPLOS:     Estudo de viabilidade inicial; entrevistas de
              descoberta antes de existir problema formal.
CONTRAEXEMPLOS: "Estou explorando" como desculpa para não formalizar
              problema em projeto aprovado.
RFC DE ORIGEM:  ECP-000 (Seção 5.1, nota de escopo L-1) / ECP-003.1
VERSÃO:       0.1.0
```

---

## Tabela de consistência

| Termo | Não é | Distinto de |
|---|---|---|
| Problem | solução desejada | Goal (resposta) |
| Goal | rótulo | Problem (causa) |
| Claim | opinião | Knowledge (aceito), Assumption (assumido) |
| Knowledge | crença | Claim (em disputa) |
| Assumption | conhecimento | Knowledge (tem evidência) |
| Constraint | desculpa | Risk (adverso) |
| Alternative | fachada | Variantes de mesma opção |
| Evidence | autoridade | Knowledge (aceito), Claim (proposição) |
| Decision | fluxo | Claim (afirmação) |
| Artifact | produto do projeto | Knowledge (produto durável) |
| Risk | suposição | Constraint (limite) |
| State | modelo do projeto | Grafo (modelo) |
| Capability | qualidade | Habilidade verificável |
| Contract | prompt | Instrução de estilo |
| Processamento | decisão | Reflexo (autorizado por decisão) |
| Exploração | projeto | Pesquisa (com goal formalizado) |

---

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 0.2.0 | 2026-08-02 | Novos termos PROCESSAMENTO (nota L-0) e EXPLORAÇÃO (nota L-1); tabela de consistência atualizada. |
| 0.1.0 | 2026-08-02 | Congelamento da semântica: 14 termos (cadeia congelada + apoio); regra anti-sinônimo; tabela de consistência. |
