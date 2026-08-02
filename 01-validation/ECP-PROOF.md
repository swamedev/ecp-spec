# ECP-PROOF — Tentativa de Falsificação da Fundação

| Campo | Valor |
|---|---|
| **Tipo** | Documento de Validação (`VALID`) |
| **Fase** | V0 — Validation |
| **Status** | Rascunho |
| **Versão** | 0.2.0 |
| **Data** | 2026-08-02 |
| **Autores** | ECP Contributors |
| **Objetivo** | Tentar provar que o ECP está errado |

> Este documento **não defende** o ECP. Ele o **ataca**. Cada Lei e cada princípio da fundação é submetido a contraexemplos reais, um por um. O resultado de cada tentativa é registrado como `PASSOU` ou `FALHOU`. Uma falha não é um fracasso do projeto: é uma descoberta — ou o protocolo muda, ou o contraexemplo é afastado com justificativa registrada.

---

## 1. Regras do exercício

1. Toda tentativa deve nomear um **alvo** (uma Lei ou princípio), um **contraexemplo** e o **mecanismo** pelo qual o contraexemplo violaria o alvo.
2. O contraexemplo só vale se for **plausível** — um caso que poderia ocorrer em engenharia real, não um caso patológico construído artificialmente.
3. O veredito é coletivo: `PASSOU` (o alvo resistiu), `FALHOU` (o alvo caiu — exige revisão da fundação) ou `EM ANÁLISE` (o contraexemplo expôs uma zona cinzenta).
4. Um `FALHOU` abre um registro de correção: alterar a fundação ou criar uma RFC que a refine.
5. Ao final, a **barreira de avanço** (ver ROADMAP) só é transposta se Leis e princípios resistirem ou forem corrigidos com evidência.

Formato de entrada:

```
ALVO:     <identificador>
CONTRAEXEMPLO:
    <descrição do cenário>
MECANISMO DE VIOLAÇÃO:
    <como o cenário quebra o alvo>
VEREDITO:  <PASSOU | FALHOU | EM ANÁLISE>
NOTA:      <justificativa, quando houver>
```

---

## 2. Falsificação das Leis

### 2.1 `L-0` — Nenhum estado muda sem decisão verificável

CONTRAEXEMPLO 1 — *Urgência operacional*
    Um alarme de segurança dispara e um operador precisa agir em
    segundos. Registrar um Decision Record completo (alternativas,
    critérios, evidências, confiança) antes de fechar o registro de
    gás é inviável no tempo disponível.
MECANISMO DE VIOLAÇÃO:
    A Lei exigiria uma decisão verificável e registrada antes da
    transição; a urgência torna a verificação impossível.
VEREDITO:  EM ANÁLISE
NOTA:
    Distinguir **decisão** de **processamento**: a decisão de atuar é
    tomada e registrada *depois* como registro a posteriori. A Lei
    deveria explicitar que o registro pode ser tardio desde que
    identificável e reconstruível. Isso indica necessidade de
    esclarecimento na fundação — não derrubada.

CONTRAEXEMPLO 2 — *Transições automáticas determinísticas*
    Um scheduler decide por regra fixa ("se X, avance") sem nenhuma
    ponderação. A decisão existe, mas é mecânica.
MECANISMO DE VIOLAÇÃO:
    Nenhum — a decisão existe e pode ser verificada. O caso não viola
    a Lei; apenas mostra que a "decisão" pode ser trivial.
VEREDITO:  PASSOU

CONTRAEXEMPLO 3 — *Estado inicial*
    A entrada do protocolo (estado inicial) não é alcançada por
    decisão alguma — ninguém "decide" entrar no protocolo.
MECANISMO DE VIOLAÇÃO:
    Pareceria violar "todo estado é alcançado por decisão".
VEREDITO:  PASSOU
NOTA:
    A Lei já é interpretada corretamente: o estado inicial não é uma
    transição. O ECP-009 (Q3 de ECP-009.1) já trata isso. Confirmado.

### 2.2 `L-1` — Toda entidade é rastreável a um Problem Record

CONTRAEXEMPLO 1 — *Pesquisa pura / exploração*
    Um pesquisador explora um fenômeno sem problema formalizado — a
    curiosidade é o motor. Exigir um Problem Record aprovado seria
    burocrático e inibidor.
MECANISMO DE VIOLAÇÃO:
    A Lei exige problema de origem para toda entidade; a exploração
    não tem problema a priori.
VEREDITO:  EM ANÁLISE
NOTA:
    Há distinção entre **projeto** (deve ter problema) e **exploração**
    (aquisição de conhecimento pré-problema). O próprio fluxo do ECP
    trata isso: a exploração reduz lacunas e *produz* o problema. A
    Lei deve ganhar nota de que "exploração não é projeto" — a
    formalização do problema é o critério de entrada.

CONTRAEXEMPLO 2 — *Manutenção trivial*
    Corrigir um typo não deveria exigir rastreio a um problema raiz.
MECANISMO DE VIOLAÇÃO:
    A cadeia Artifact → Decision → Goal → Problem parece pesada para
    uma correção de um caractere.
VEREDITO:  PASSOU
NOTA:
    O rastreio é transitivo: o artefato herda o problema do goal pai
    do projeto em que está. Nenhuma entidade nova é criada; a
    exigência é satisfeita pelo encadeamento, não por um Problem Record
    novo por correção. Confirmado.

CONTRAEXEMPLO 3 — *Projeto cujo problema muda no meio*
    O problema original é invalidado pela realidade; o projeto já tem
    dezenas de artefatos. Manter o rastreio ao problema original falso
    violaria a verdade; re-rastrear tudo é caro.
MECANISMO DE VIOLAÇÃO:
    A Lei não define o que acontece com a cadeia quando o problema raiz
    muda.
VEREDITO:  EM ANÁLISE
NOTA:
    Exige uma regra de **migração de raiz**: o Problem Record original
    é deprecado, um novo é criado, e a cadeia é reencadeada por decisão
    (não por edição). Deve virar regra na fundação.

---

## 3. Falsificação dos princípios

### 3.1 `P-1` — Entendimento precede artefato

CONTRAEXEMPLO 1 — *Prototipagem como forma de entender*
    Construir um protótipo descartável é, muitas vezes, a única forma
    de entender o problema. O artefato precede o entendimento completo.
MECANISMO DE VIOLAÇÃO:
    O princípio diz "nenhum artefato material antes de evidência de
    compreensão"; o protótipo viola isso por construção.
VEREDITO:  EM ANÁLISE
NOTA:
    O protótipo não é o *artefato do projeto* — é **evidência de
    entendimento** (Experiment → Evidence). A fundação deve explicitá-lo
    como instrumento de Discovery, não como produto. Distinção
    conceitual importante; requer nota.

CONTRAEXEMPLO 2 — *Mimetismo*
    Copiar um artefato conhecido (biblioteca, padrão) sem entender é a
    única forma em alguns domínios (ex.: adotar um framework).
MECANISMO DE VIOLAÇÃO:
    A adoção de tecnologia pré-existente não exige "entendimento
    completo".
VEREDITO:  PASSOU
NOTA:
    O ECP não exige entender *tudo* — exige evidência de compreensão
    do **objetivo e restrições**, não do mecanismo interno. Adotar um
    framework é uma decisão com evidência (documentação, avaliação).
    Confirmado.

### 3.2 `P-2` — Engenharia é decisão sob restrições

CONTRAEXEMPLO 1 — *Trabalho artístico / criativo*
    Um filme ou um livro são decididos ou são "expressão"? Se forem
    expressão, o P-2 não se aplica — mas o ECP pretende ser universal.
MECANISMO DE VIOLAÇÃO:
    A universalidade do P-2 seria falsa para produção criativa.
VEREDITO:  PASSOU
NOTA:
    A produção criativa *também* é feita de decisões sob restrições
    (orçamento, prazo, direção). O que muda é o critério de
    "verdade" — mas a estrutura de decisão permanece. O caso precisa
    ser exercitado em ECP-CASES (Livro, Filme) para confirmação.

CONTRAEXEMPLO 2 — *Acaso / serendipidade*
    Alguns resultados valiosos não são decididos — são encontrados
    por acaso.
MECANISMO DE VIOLAÇÃO:
    Se o resultado não foi decidido, o P-2 o excluiria da engenharia.
VEREDITO:  EM ANÁLISE
NOTA:
    Serendipidade é **geração de alternativa** (mais opções), não
    ausência de decisão. A decisão de *seguir* o achado permanece.
    Requer nota sobre o papel da descoberta como entrada do espaço de
    alternativas.

### 3.3 `P-3` — Conhecimento é o produto; código é subproduto

CONTRAEXEMPLO 1 — *Sistemas legados críticos*
    Em sistemas embarcados de segurança, o "produto" é o binário
    validado, não o conhecimento. O conhecimento sem o binário não salva
    vidas.
MECANISMO DE VIOLAÇÃO:
    O P-3 afirmaria que o conhecimento é o produto durável; para um
    regulador, o produto é o sistema certificado.
VEREDITO:  EM ANÁLISE
NOTA:
    O P-3 diz o que **sobrevive** e o que **direciona o esforço**, não
    o que é comercialmente entregue. O binário é artefato; a
    certificação exige o conhecimento *e* o artefato. Redação do P-3
    deve ser mais precisa para não parecer que artefatos são descartáveis.

CONTRAEXEMPLO 2 — *Consultoria entregando código*
    Um cliente paga por código, não por conhecimento.
MECANISMO DE VIOLAÇÃO:
    Aparente contradição entre o valor do cliente e o princípio.
VEREDITO:  PASSOU
NOTA:
    O cliente paga pelo artefato; o conhecimento é o que permite
    mantê-lo. Não há contradição: o P-3 regula o foco do *processo de
    engenharia*, não a troca comercial. Confirmado.

### 3.4 `P-4` — Toda decisão é rastreável

CONTRAEXEMPLO 1 — *Decisões difusas de design*
    Decisões estéticas (cor de um botão) registradas como Decision
    Record são desperdício.
MECANISMO DE VIOLAÇÃO:
    Obrigar rastreio a toda decisão trivial.
VEREDITO:  PASSOU
NOTA:
    O P-4 exige rastreabilidade **quando a decisão altera o caminho do
    objetivo**; decisões triviais são cobertas pela decisão do
    artefato que as contém. Alinhado ao Q3 de ECP-004.2. Confirmado.

CONTRAEXEMPLO 2 — *Decisões negociais orais*
    Em obra civil, decisões de campo são tomadas oralmente no canteiro.
MECANISMO DE VIOLAÇÃO:
    Registrar toda decisão de campo é inviável em ritmo de obra.
VEREDITO:  EM ANÁLISE
NOTA:
    Exige política de **agregação de decisões**: decisões de baixo
    impacto podem ser registradas em lote (diário de obra), desde que
    reconstruíveis. Requer nota na fundação.

### 3.5 `P-5` — Validade exige evidência

CONTRAEXEMPLO 1 — *Conhecimento matemático*
    Uma prova matemática é válida sem "evidência observável" no sentido
    empírico.
MECANISMO DE VIOLAÇÃO:
    A evidência no ECP é definida como observação registrada; a prova
    formal não é observação.
VEREDITO:  PASSOU
NOTA:
    A derivação lógica documentada é evidência de nível 4 na hierarquia
    do ECP-008. A definição de evidência já cobre raciocínio verificável.
    Confirmado.

CONTRAEXEMPLO 2 — *Autoridade*
    "O especialista disse" é tratado como evidência em muitas
    organizações.
MECANISMO DE VIOLAÇÃO:
    Se o ECP rejeita autoridade, precisa afastar explicitamente o
    argumento de autoridade.
VEREDITO:  EM ANÁLISE
NOTA:
    O ECP-008 classifica "citação rastreável a fonte confiável" como
    nível 3 — a autoridade *com fonte verificável* é admissível como
    contexto. A relação com o invariante "evidência nunca é inferida
    por autoridade" (ECP-INVARIANTS) precisa ser reconciliada.

### 3.6 `P-6` — Restrições são informação

CONTRAEXEMPLO 1 — *Restrição desconhecida*
    Em pesquisa de fronteira, as restrições não são conhecidas a
    priori — o que o P-6 faria com isso?
MECANISMO DE VIOLAÇÃO:
    O princípio pressupõe restrições declaradas; a pesquisa as descobre.
VEREDITO:  PASSOU
NOTA:
    Restrições desconhecidas são lacunas (ECP-006), não ausência de
    restrições. O P-6 trata das declaradas; as desconhecidas entram
    pelo mapa de lacunas. Confirmado.

CONTRAEXEMPLO 2 — *Contornar restrição*
    "Sempre exploramos a restrição, nunca a contornamos" — mas em
    emergências, contorna-se.
MECANISMO DE VIOLAÇÃO:
    Emergências violariam o "nunca contornar".
VEREDITO:  PASSOU
NOTA:
    Contornar uma restrição é uma **decisão** que renegocia a
    restrição, não uma violação silenciosa — desde que registrada e
    autorizada. O P-6 proíbe contornar *sem decisão*, não renegociar.
    Confirmado.

### 3.7 `P-7` — Erro é dado de entrada

CONTRAEXEMPLO 1 — *Erro destrutivo*
    Um erro que corrompe dados de produção é "dado de entrada" para
    aprendizado, mas a prioridade é a recuperação, não a análise.
MECANISMO DE VIOLAÇÃO:
    Pareceria instrumentalizar o erro.
VEREDITO:  PASSOU
NOTA:
    P-7 regula o **sistema de processos**, não a resposta operacional.
    Recuperar primeiro; analisar depois. A transição `FAILURE` cobre o
    caminho. Confirmado.

CONTRAEXEMPLO 2 — *Erro sem registro*
    Erros negados ou escondidos (cultura punitiva) não viram dado.
MECANISMO DE VIOLAÇÃO:
    Se o erro não é registrado, o P-7 não opera.
VEREDITO:  EM ANÁLISE
NOTA:
    Requer invariante cultural do protocolo: nenhuma sanção por erro
    registrado em boa fé. Não é violação do princípio, mas condição de
    aplicabilidade. Nota recomendada.

### 3.8 `P-8` — Neutralidade de implementador

CONTRAEXEMPLO 1 — *Limites cognitivos humanos*
    Humanos não conseguem manter um grafo de conhecimento inteiro em
    memória ativa como um agente de IA.
MECANISMO DE VIOLAÇÃO:
    Se a neutralidade for interpretada como "o mesmo processo para
    todos", humanos não conseguiriam cumprir o protocolo.
VEREDITO:  PASSOU
NOTA:
    A neutralidade é sobre **não pressupor** implementador, não sobre
    impor o mesmo processo. O ECP é neutro; a *execução* pode ter
    adaptações de memória (cadernos, sistemas). Confirmado.

CONTRAEXEMPLO 2 — *Entidades sem capacidades de registro*
    Um executor puro que não tem ferramenta de registro.
MECANISMO DE VIOLAÇÃO:
    A exigência de registros violaria a neutralidade.
VEREDITO:  PASSOU
NOTA:
    Se a entidade não pode registrar, não pode exercer decisão
    verificável — e portanto não é entidade ECP. A capacidade mínima de
    registro é precondição de conformidade. Confirmado.

### 3.9 `P-9` — Conformidade verificável automaticamente

CONTRAEXEMPLO 1 — *Regras qualitativas*
    Regras de "qualidade do entendimento" não são mecanicamente
    verificáveis.
MECANISMO DE VIOLAÇÃO:
    O ECP proíbe regras não verificáveis; se todas as regras
    importantes caem nessa classe, o ECP não teria conteúdo.
VEREDITO:  PASSOU
NOTA:
    A verificação é sobre **condições avaliáveis** (`EXIT`, `REQUIRED`,
    registros), não sobre a substância. O "entendimento" é verificado
    por evidência de compreensão, não por leitura de mentes. Confirmado.

CONTRAEXEMPLO 2 — *Contraexemplo do linter*
    Um linter detecta a presença do campo, não a veracidade do campo.
MECANISMO DE VIOLAÇÃO:
    Automação verifica presença, não verdade — a conformidade poderia
    ser formalmente satisfeita com conteúdo falso.
VEREDITO:  EM ANÁLISE
NOTA:
    Este é o **limite real do P-9**: o ECP verifica conformidade
    estrutural, e a *veracidade* é verificada por evidência e
    auditoria humana/independente (Fase de Certification). A distinção
    conformidade × veracidade deve ser explícita. Nota crítica.

### 3.10 `P-10` — O padrão sobrevive a qualquer implementação

CONTRAEXEMPLO 1 — *Implementação que simplifica demais*
    Uma implementação que reduz o ECP a um checklist é uma
    implementação, mas destrói o propósito.
MECANISMO DE VIOLAÇÃO:
    Se "qualquer implementação" inclui a fraudulenta, o P-10 seria falso.
VEREDITO:  PASSOU
NOTA:
    P-10 diz que o *contrato* não depende da implementação — não que
    toda implementação seja conforme. Implementações que omitem
    decisões são não conformes. Confirmado.

CONTRAEXEMPLO 2 — *Sem implementação de referência*
    Sem uma implementação de referência, o padrão é inutilizável na
    prática.
MECANISMO DE VIOLAÇÃO:
    P-10 não garante existência de implementação — garantia de
    aplicabilidade seria exigida.
VEREDITO:  PASSOU
NOTA:
    A implementação de referência é planejada em 08-reference; sua
    ausência não invalida o princípio, apenas atrasa a adoção.
    Confirmado.

### 3.11 `P-11` — Toda decisão é dirigida por um objetivo

CONTRAEXEMPLO 1 — *Decisões operacionais de rotina*
    Escolher o algoritmo de cache não serve a um objetivo no sentido
    de Goal Record.
MECANISMO DE VIOLAÇÃO:
    A decisão infraestrutural não referencia um goal.
VEREDITO:  PASSOU
NOTA:
    O próprio ECP-004.2 (Q3) já afasta decisões puramente
    infraestruturais do runtime. Decisões *de projeto* servem a goals;
    as instrumentais herdam o goal do projeto. Confirmado.

CONTRAEXEMPLO 2 — *Decisão de interesse pessoal*
    Um stakeholder decide por interesse próprio, contrariando o goal.
MECANISMO DE VIOLAÇÃO:
    A decisão não é dirigida pelo objetivo formal, mas por outra coisa.
VEREDITO:  PASSOU
NOTA:
    Isso é **não conformidade detectável** — a auditoria (P-9) a
    flagra pela divergência entre Decision Record e Goal Record. O ECP
    não impede má-fé; ele a torna visível. Confirmado.

### 3.12 `P-12` — Todo trabalho responde a um problema

CONTRAEXEMPLO 1 — *Projetos impositivos*
    Um projeto ordenado por lei/regulador não "responde a um problema"
    escolhido — é imposto.
MECANISMO DE VIOLAÇÃO:
    O problema existiria mesmo assim (conformidade legal é o problema),
    mas o trabalho não é uma "resposta" voluntária.
VEREDITO:  PASSOU
NOTA:
    "Responder a um problema" inclui problemas impostos; conformidade
    regulatória é um problema verificável. Confirmado.

CONTRAEXEMPLO 2 — *Trabalho de deleite / luxo*
    Um produto de luxo não resolve "problema" nenhum no sentido
    funcional.
MECANISMO DE VIOLAÇÃO:
    P-12 exigiria problema onde só há desejo.
VEREDITO:  EM ANÁLISE
NOTA:
    O "problema" pode ser de natureza emocional/estética (status,
    prazer), e é verificável enquanto condição motivadora. Requer
    discussão se o ECP admite problemas não funcionais — decisão de
    escopo a registrar.

---

## 4. Síntese

| Alvo | Vereditos | Pendências registradas |
|---|---|---|
| `L-0` | 1 EM ANÁLISE, 2 PASSOU | Registro tardio de decisão em urgência |
| `L-1` | 2 EM ANÁLISE, 1 PASSOU | Exploração pré-problema; migração de raiz |
| `P-1` | 1 EM ANÁLISE, 1 PASSOU | Protótipo como evidência de entendimento |
| `P-2` | 1 EM ANÁLISE, 1 PASSOU | Serendipidade como geração de alternativa |
| `P-3` | 1 EM ANÁLISE, 1 PASSOU | Redação sobre valor dos artefatos |
| `P-4` | 1 EM ANÁLISE, 1 PASSOU | Agregação de decisões de baixo impacto |
| `P-5` | 1 EM ANÁLISE, 1 PASSOU | Autoridade com fonte verificável × invariante |
| `P-6` | 2 PASSOU | — |
| `P-7` | 1 EM ANÁLISE, 1 PASSOU | Cultura de registro de erro |
| `P-8` | 2 PASSOU | — |
| `P-9` | 1 EM ANÁLISE, 1 PASSOU | Conformidade estrutural × veracidade |
| `P-10` | 2 PASSOU | — |
| `P-11` | 2 PASSOU | — |
| `P-12` | 1 EM ANÁLISE, 1 PASSOU | Problemas não funcionais (escopo) |

**Nenhuma Lei ou princípio foi derrubado nesta rodada.** Onze pendências exigem nota ou regra na fundação — todas de clarificação, nenhuma de colapso. Próximo passo: exercitar as pendências em ECP-CASES e fechá-las no ECP-GLOSSARY.

---

## 5. Rodada 2 — Re-teste das pendências contra as emendas

Cada pendência da Rodada 1 foi re-testada contra a emenda aplicada à fundação (ECP-000, ECP-003, ECP-008, ECP-009, ECP-INVARIANTS, ECP-GLOSSARY). Regra: se a emenda afasta o mecanismo de violação do contraexemplo, o alvo resiste e a pendência fecha.

| Pendência | Emenda aplicada | Re-teste | Veredito |
|---|---|---|---|
| `L-0` urgência (registro tardio) | ECP-000 §5 (decisão × processamento; registro a posteriori) + ECP-009.3 + INV-2 nota + GLOSSARY `PROCESSAMENTO` | A ação de emergência é **processamento** autorizado por uma decisão que existe, é identificável e reconstruível; o registro é adiado, não omitido. A transição continua exigindo decisão verificável. | RESOLVIDA |
| `L-1` exploração pré-problema | ECP-000 §5.1 (exploração não é projeto) + ECP-003.1 + GLOSSARY `EXPLORAÇÃO` | Exploração não gera entidades sujeitas à L-1; a formalização do Problem Record é o critério de entrada. O contraexemplo não viola a Lei — opera fora dela. | RESOLVIDA |
| `L-1` migração de problema raiz | ECP-003.3 (deprecação + reencadeamento por decisão) | O problema original é deprecado, o sucessor criado e a cadeia reencadeada por Decision Record — sem elos órfãos e sem edição silenciosa. L-1 permanece íntegra. | RESOLVIDA |
| `P-1` protótipo como evidência | ECP-000 §6.1 `P-1` | Protótipo é evidência de entendimento (instrumento de Discovery), não artefato do projeto. O princípio proíbe o artefato *do projeto* sem entendimento, não a prototipagem. | RESOLVIDA |
| `P-2` serendipidade | ECP-000 §6.1 `P-2` | Descoberta gera alternativa; a decisão de *seguir* o achado permanece sujeita ao P-2. O acaso amplia o espaço de opções, não dispensa a decisão. | RESOLVIDA |
| `P-3` redação sobre valor dos artefatos | ECP-000 `P-3` reescrito | O P-3 diz o que direciona o esforço e o que sobrevive; o artefato é consequência material — parte do resultado quando o objetivo exige entrega, nunca finalidade. Binário de segurança não é tratado como descartável. | RESOLVIDA |
| `P-4` agregação de decisões de baixo impacto | ECP-009.3 (lote em diário de obra, reconstruível) | Decisões de baixo impacto podem ser registradas em lote; médio/alto impacto permanecem individuais. Rastreabilidade preservada via janela/escopo/autor. | RESOLVIDA |
| `P-5` autoridade com fonte × invariante | ECP-008 §2.2 nota + INV-3 nota | A evidência é a observação referenciada, não o prestígio do emissor; citação rastreável é nível 3. "Autoridade garante" sem fonte é nível 5 (inadmissível). INV-3 preservado. | RESOLVIDA |
| `P-7` cultura de registro de erro | ECP-000 §6.1 `P-7` | A aplicabilidade exige condição cultural: nenhuma sanção por erro registrado em boa fé. Registrado como condição, não como violação. | RESOLVIDA |
| `P-9` conformidade estrutural × veracidade | ECP-008 §2.2 nota + INV-3 nota | Automação verifica conformidade estrutural; veracidade é estabelecida por evidência e auditoria independente (Fase de Certification). Limite explícito, não falha. | RESOLVIDA |
| `P-12` problemas não funcionais | ECP-000 §6.1 `P-12` | O problema pode ser estético/emocional/status desde que verificável como condição motivadora; o ECP governa o processo de decisão, não o mérito da estética. | RESOLVIDA |

**Resultado da Rodada 2: 11/11 pendências resolvidas, 0 alvos derrubados.** As emendas não alteraram nenhum enunciado de Lei, princípio ou invariante — apenas fixaram escopo e criaram regras operacionais (ECP-003.3, ECP-009.3). A fundação atravessa a barreira de avanço da Fase V0 com os alvos `PASSOU`.

---

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 0.2.0 | 2026-08-02 | Rodada 2 de re-teste: 11 pendências testadas contra as emendas da fundação; 11/11 resolvidas; 0 alvos derrubados. Contagem corrigida (9 → 11). |
| 0.1.0 | 2026-08-02 | Rodada 1 de falsificação: L-0, L-1, P-1..P-12; 14 alvos, 11 pendências, 0 derrubadas. |
