# ROADMAP

Evolução do ECP como um **sistema operacional** de engenharia, em duas camadas. Uma subdivisão inicia somente quando a anterior estabilizou seus documentos em `Versão Candidata` ou `Aprovado`.

```
┌─────────────────────────────────────────────┐
│ CAMADA 1 — COGNIÇÃO   (00-foundation)       │
│ como uma entidade pensa; antes da execução  │
│   ECP-000 → 010                             │
├─────────────────────────────────────────────┤
│ FASE V0 — VALIDAÇÃO (01-validation)         │
│ o ECP é verdadeiro? PROOF/CASES/GLOSSARY/   │
│   INVARIANTS (sem números ECP-*)            │
├─────────────────────────────────────────────┤
│ CAMADA 2 — ENGENHARIA  (02-core → 07)       │
│ como o projeto é executado e certificado    │
│   ECP-100 → 799                             │
├─────────────────────────────────────────────┤
│ APOIO          (08-reference, schemas,      │
│                 examples, assets)           │
└─────────────────────────────────────────────┘
```

## CAMADA 1 — Cognição (em andamento)

Estabelecer a base conceitual. Se essa base estiver errada, todo o restante fica comprometido.

A ordem acompanha a lógica natural de qualquer projeto: **defina o problema → defina o objetivo → registre as claims → entenda o conhecimento → registre as suposições → colete evidência e confiança → decida → execute o ciclo cognitivo → represente como máquina de estados**.

- [x] `ECP-000` — O que é Engenharia (princípios, Leis L-0/L-1, grafo de conhecimento)
- [x] `ECP-001` — Arquitetura da Especificação
- [x] `ECP-002` — Critérios de Admissão de Regras
- [x] `ECP-003` — Modelo de Problema (Problem Model)
- [x] `ECP-004` — Modelo de Objetivo e Intenção (Goal & Intent)
- [x] `ECP-005` — Modelo de Claims (Claim Model)
- [x] `ECP-006` — Modelo de Conhecimento e Contexto
- [x] `ECP-007` — Modelo de Suposições
- [x] `ECP-008` — Modelo de Evidência, Confiança e Risco
- [x] `ECP-009` — Modelo Universal de Decisão
- [x] `ECP-010` — Ciclo de Vida Cognitivo (máquina de estados conceitual; regra ECP-010.1 decisão sob incerteza; NFRs RNF-1..RNF-3 no cabeçalho)

**Critérios de saída da camada:** ECP-000 a 010 aprovados e um caso de uso real validado contra eles.

## FASE V0 — Validation (concluída)

A fundação foi **congelada por decisão do Arquiteto-Chefe**: nenhuma RFC nova é escrita enquanto ela não for testada. O objetivo é **falsificar**, não defender. Ordem de trabalho: **PROOF → CASES → GLOSSARY → INVARIANTS → correção das pendências**.

- [x] `ECP-PROOF` — tentativa de derrubar L-0, L-1 e P-1..P-12 com contraexemplos (rodada 1: 0 derrubadas, 11 pendências; rodada 2: 11/11 resolvidas, 0 derrubadas)
- [x] `ECP-CASES` — 20 projetos de domínios diversos (rodada 1: 17 PASSA, 3 PARCIAL; rodada 2: 19 PASSA, 1 PARCIAL, 0 NÃO PASSA)
- [x] `ECP-GLOSSARY` — semântica formal congelada (16 termos, regra anti-sinônimo)
- [x] `ECP-INVARIANTS` — 7 invariantes imutáveis do protocolo (notas INV-2 e INV-3 adicionadas)
- [x] Fechar as **pendências** levantadas em PROOF/CASES na fundação (ECP-003.3, ECP-009.3, notas de escopo em ECP-000/ECP-008/INVARIANTS)
- [ ] Promover `ECP-GLOSSARY` para `08-reference/` quando congelado (v1.0)

### Regra de avanço da Camada 2

> **Nenhuma nova RFC da Camada 2 poderá ser considerada estável enquanto a fundação não passar pelo ECP-PROOF, pelos casos representativos (ECP-CASES) e pela validação dos invariantes (ECP-INVARIANTS).**

**Barreira transposta em 2026-08-02 (Fase V0 concluída):** PROOF rodada 2 com 0 alvos derrubados; 19/20 casos conformes; invariantes validados. RFCs da Camada 2 podem agora atingir `Versão Candidata`. Ficam registradas como recomendações abertas para a Camada 2: inferência estatística como evidência (ECP-008), decisões coletivas e governança de hierarquia (Governance), interface contrato comercial (ECP-001/ECP-004).

## VALIDATION PROGRAM (em andamento, feature freeze)

**Decisão AD-001 (2026-08-02):** o ECP-SPEC entra em **feature freeze**.
**Decisão AD-002 (2026-08-02):** a Fase B evolui para um programa **permanente**
de evidência — o **Validation Program**. Em vez de seguir direto a Certification,
conduzimos **experimentos numerados** sobre projetos reais (`experiments/EXP-*.md`).
Cada experimento responde objetivamente: **o ECP ajudou? ou não?** A evolução de
`Quality`/`Learning`/`Certification` é destravada por acumulo transversal de
evidência de múltiplos experimentos — nunca de um único.

### Runtime (fundação do programa)

**AD-001/AD-002:** construir o **ECP Reference Runtime (ERR)**, a implementação
canônica, usando o próprio ECP (Bootstrap — `EXP-001`).

- [x] Repositório `ecp-runtime` criado em paralelo a `ecp-spec`
- [x] **ECP Kernel** implementado com cinco responsabilidades: `Problem`, `Goal`, `Decision`, `Contract`, `Graph` (sem IA, sem API, sem banco)
- [x] Cadeia executável: `Problem → Goal → Knowledge → Assumption → Evidence → Decision` (íntegra, rastreável e reproduzível)
- [x] **EXP-001** — primeiro caso real conduzido pelo runtime: modelar `P-0001`/`G-0001` do próprio Bootstrap e gerar o **Decision Graph**
- [ ] Comparação com processo tradicional (tempo, rastreabilidade, facilidade de revisão)

### Seqüência de experimentos (Validation Program)

| EXP | Projeto | Pergunta | Status |
|---|---|---|---|
| [EXP-001](experiments/EXP-001.md) | Bootstrap Runtime | O ECP conduz sua própria referência do início ao fim? | Em execução |
| EXP-002 | ERP | O ECP escala para um sistema grande com muitas entidades? | Planejado |
| EXP-003 | API | O ECP orienta decisões de interface/contrato? | Planejado |
| EXP-004 | Game | O ECP lida com produto de intenção aberta/iterativa? | Planejado |
| EXP-005 | Agente | O ECP guia um artefato com múltiplas capacidades? | Planejado |
| EXP-006 | Aplicativo | O ECP abrange app mobile/web de ponta a ponta? | Planejado |
| EXP-007 | Projeto externo | O ECP funciona fora do controle dos autores? | Planejado |

**Critério de saída do programa:** evidência transversal de múltiplos
experimentos, incluindo ao menos um domínio não controlado (EXP-007), antes de
destravar plenamente `Quality`/`Learning`/`Certification`.

### Fase C — Adversarial Validation (aberta em 2026-08-03)

**Decisão (Arquiteto-Chefe):** a fundação experimental está **congelada** —
nenhuma nova RFC, AD, lei, entidade ou schema enquanto a Fase C estiver em
andamento. O objetivo deixa de ser *provar que funciona* e passa a ser *provar
que resiste*: "Quais leis sobrevivem quando tentamos destruí-las?"

- [x] Congelamento da fundação experimental (decisão oficial)
- [x] Risco de **endogeneidade** documentado (o protocolo validando o próprio protocolo)
- [x] **Resistance Index (RI)** definido — critérios que permaneceram válidos / critérios testados
- [x] Abertura de [`validation/adversarial/`](experiments/validation/adversarial/README.md)
- [x] Frente **Inferência Científica** aberta — camada `OBS → SIGNAL → PATTERN → LAW-H` ([signals](experiments/validation/signals/README.md))
- [x] **SIGNAL-SCHEMA** (evidência recorrente mensurável) + critérios objetivos de promoção Signal → Pattern
- [x] **Law Strength Index (LSI)** e **Predictive Index (PI)** definidos ([LAW-METRICS](experiments/validation/laws/LAW-METRICS.md))
- [x] **LAW-CRITERIA v1.0 congelado** — critérios LC-1..LC-8 definidos **antes** dos resultados hostis (anti-hindsight) ([LAW-CRITERIA](experiments/validation/laws/LAW-CRITERIA.md))
- [x] **H-001 executado** contra a LB-001 (vetor: decisão justificável sem conhecimento) — ataque falhou, RI 1.0, negative evidence registrada; LB-001 **sobreviveu** mas **não** foi promovida (faltam LC-1/LC-6) ([HOSTILE-REPORT-H-001](experiments/validation/adversarial/HOSTILE-REPORT-H-001.yaml))
- [x] **Primeiro Signal preliminar** registrado — SIG-001 (EXP-001 + H-001; ainda sem ocorrência independente, RA-SIG-001 pendente) ([SIGNALS-REGISTRY](experiments/validation/signals/SIGNALS-REGISTRY.yaml))
- [x] **Descoberta LC-8 (2026-08-03):** o H-001 revelou risco de verdade analítica — o ECP *define* decisão justificável com evidência/conhecimento. O sistema impediu a promoção precoce. Abre o **Independence Program (P-0007)**.
- [x] **LAW-CRITERIA v1.1** — **LC-9 Observation Independence** adicionado; promoção exige Endogenous **e** Exogenous Evidence
- [ ] **Shadow Experiment 001 (SX-001)** — observação pura de projeto não-ECP (sem EXP-002 ainda); reconstrução → comparação → Signals
- [ ] Execução dos experimentos hostis H-002..H-006 (especificados em [HOSTILE-EXPERIMENTS](experiments/validation/adversarial/HOSTILE-EXPERIMENTS.md))
- [ ] Consolidação das primeiras LAW-H a partir de Signals/Patterns reais
- [ ] Evolução para **External Validation** e depois **Industrial Validation**

**Funil científico:** `Hostile → Corpus atualizado → Signals → Patterns → LAW-H → Hostile novamente → Observation Independence (Exogenous Evidence) → Candidate Universal Law → External → LAW → LSI → Industrial → LAW-F`.

> **Gate de independência:** a promoção a Candidate Universal Law exige **ambas**
> as evidências — sobreviver aos hostis (endógena) **e** emergir fora do ECP
> (exógena, LC-9).

```
Validation Program → Adversarial Validation (Fase C) → External Validation → Industrial Validation
```

### Fase C1 → C2 — Infraestrutura Congelada → Produção de Evidência (coordenação 2026-08-03)

**Decisão (Arquiteto-Chefe):** o **Framework está fechado** — não perfeito,
fechado. A sucessão Validation → Corpus → Audit → Signals → Hostile →
Independence → ... criou o risco de **Methodological Drift**: "sempre existe
mais um gate antes do experimento". Isso é o oposto da filosofia do ECP.
Nenhuma teoria científica esperou ficar perfeita antes do primeiro experimento
externo.

**Princípio da Suficiência Metodológica** (registrado como coordenação; AD
futuro):

> Uma metodologia deixa de evoluir temporariamente quando seu poder preditivo
> passa a ser mais importante que seu refinamento interno.

**Prioridade muda oficialmente:** o objetivo deixa de ser melhorar o protocolo e
passa a ser **descobrir se o protocolo funciona**.

- [x] **FASE C1 — Infrastructure Frozen:** nenhum gate novo, critério, métrica,
      RFC, AD, lei ou schema **até o SX-001 terminar**. Qualquer limitação
      descoberta durante o SX-001 é registrada como **dívida metodológica para a
      v1.1** — nunca corrigida no meio do experimento.
- [x] **FASE C2 — Evidence Production:** toda energia passa a produzir evidência,
      não documentação. Ordem oficial da coordenação:
      1. Congelar a infraestrutura metodológica.
      2. Executar a **verificação automática** dos 9 candidatos SELECTABLE.
      3. O **protocolo escolhe automaticamente** o SX-001 (sem votação, sem
         preferência, sem gosto pessoal).
      4. Executar o SX-001 **sem modificar nenhuma regra metodológica**.
      5. Registrar todas as limitações encontradas como **dívida metodológica
         para v1.1**.
- [x] Registro de **dívida metodológica v1.1** aberto (ver
      [METHODOLOGICAL-DEBT](experiments/validation/METHODOLOGICAL-DEBT.md)) —
      DEBT-001..DEBT-005 registrados (executor único, EAR post hoc, camada
      Atomic Facts, caso único, confiança SIG-001 estimada)

### P-0006 — Law Discovery Program (aberto em 2026-08-03)

**Decisão (Arquiteto-Chefe):** o **P-0005A termina aqui** — há infraestrutura
suficiente. A missão muda de *construir infraestrutura* para *produzir
conhecimento novo*: descobrir **leis da engenharia**, não ferramentas.

- [x] P-0005A encerrado (infraestrutura concluída)
- [x] **Regra 1** — gate de ferramentas: nenhuma ferramenta sem pergunta científica (hipótese → experimento → ferramenta)
- [x] **LAW-BACKLOG** aberto — apenas perguntas científicas priorizadas, sem respostas antecipadas ([LAW-BACKLOG](experiments/validation/laws/LAW-BACKLOG.md))
- [x] **Genealogia** de hipóteses: LAW-H deve registrar os Signals de origem (OBS → SIGNAL → PATTERN → LAW-H)
- [x] **Negative Evidence** — ausência de evidência registrada explicitamente
- [x] **Programa de Diversidade Experimental** — evolução exige sobrevivência em domínios radicalmente diferentes
- [x] Naming corrigido: **Candidate Universal Law** → **Universal Engineering Law** (somente após validação industrial)
- [x] **LAW-CRITERIA v1.0** congelado (LC-1..LC-8) — critérios antes dos resultados
- [x] **H-001** executado contra a LB-001 → LB-001 sobreviveu (RI 1.0); **não** promovida
- [x] **SIG-001** registrado como primeiro Signal preliminar (RA-SIG-001 pendente)
- [x] **LAW-CRITERIA v1.1** — LC-9 Observation Independence (decisão pós-LC-8)
- [ ] Fechar a **LC-8** da LB-001 via **Shadow Experiment 001** (evidência exógena — ver [P-0007](#p-0007--independence-program-aberto-em-2026-08-03))
- [ ] Promover apenas Signals que atenderem rigorosamente aos critérios → Pattern
- [ ] Escolher **uma única LAW-H** e concentrar energia em destruí-la

### P-0007 — Independence Program (aberto em 2026-08-03)

**Decisão (Arquiteto-Chefe):** a descoberta mais valiosa desde o AD-007 não foi a
LB-001 — foi o protocolo detectando que o H-001 poderia validar uma **verdade
analítica** (LC-8: o ECP define decisão justificável com evidência/conhecimento).
O sistema impediu a comemoração precoce de uma "lei". Por isso: **não** é hora de
EXP-002 nem H-007; é hora de garantir que nenhuma lei derive apenas das
definições internas do ECP.

- [x] **P-0007 aberto** — charter completo ([P-0007](experiments/validation/P-0007-INDEPENDENCE.md))
- [x] **Duas perguntas de toda LAW-H:** (1) sobrevive aos hostis? (2) continua verdadeira **se o ECP desaparecer?**
- [x] **Classificação:** Endogenous Evidence / Exogenous Evidence — promoção a Candidate Universal Law exige **ambas**
- [x] **Observation Independence (LC-9)** — hipótese precisa de contexto onde observador, executor e projeto não conhecem/não seguem o ECP
- [x] **Shadow Experiments especificados** ([SHADOW-EXPERIMENTS v1.1](experiments/validation/independence/SHADOW-EXPERIMENTS.md)) — pipeline Narrativa Original → Reconstrução Cega → Comparação; SX-001 focada na emergência espontânea
- [x] **SX-SELECTION congelado** — protocolo de seleção (SC-1..SC-6, matriz, exclusões EC-1..EC-7) definido **antes** de qualquer candidato ([SX-SELECTION](experiments/validation/independence/SX-SELECTION.md))
- [x] **SX-CANDIDATES aplicado** — 20 candidatos fora de software; protocolo decidiu 14 elegíveis, 6 inelegíveis; nenhuma escolha antecipada ([SX-CANDIDATES](experiments/validation/independence/SX-CANDIDATES.md))
- [x] **P-0007.1 — Independence Framework congelado** — gate metodológico **antes** do SX-001; três eixos (Observation / Evidence / Domain Independence), LC-10 (hipótese), definição de ocorrência independente, critérios mínimos Signal→Pattern→LAW-H→LAW-C ([P-0007.1](experiments/validation/P-0007.1-INDEPENDENCE-FRAMEWORK.md))
- [x] **P-0007.2 — Candidate Re-Audit** — regras de veredito congeladas; reauditoria aplicada ([SX-REAUDIT.yaml](experiments/validation/independence/SX-REAUDIT.yaml)): **9 SELECTABLE, 4 ELIGIBLE, 1 REJECTED** (RFID Walmart — EI); estágios Elegível→Auditado→Selecionável→Selecionado ([P-0007.2](experiments/validation/P-0007.2-CANDIDATE-REAUDIT.md))
- [x] **LB-005** registrada — princípio "decisões deriváveis de critérios pré-congelados" (candidata a lei forte); **LB-006** registrada — previsão pós-SX-001 (lei explica falhas de engenharia)
- [x] **Verificar fontes** dos 9 SELECTABLE (procedimento etapa 5) — todos acessíveis; **SX-001 selecionado automaticamente** pelo protocolo: **Challenger STS-51-L** ([SHADOW-REPORT-001](experiments/validation/independence/SHADOW-REPORT-001.md))
- [x] **Shadow Experiment 001 executado** — pipeline completo: Narrativa Original → Atomic Facts → Reconstrução Cega → Alignment Analysis → Signals → EAR ([SX-001](experiments/validation/independence/SX-001/README.md)); **`EAR(Challenger) = 0.775`** (observação experimental) e achado central **Evidence → Decision** registrados em [DISCOVERY-LOG](experiments/validation/DISCOVERY-LOG.md)
- [ ] Só então retomar **EXP-002** e **H-007**

> **Regra do teste:** uma boa teoria não cria os fenômenos que explica; ela os
> reconhece onde eles já existem.

### P-0008 — Cross-Domain Validation (aberto em 2026-08-03)

**Decisão (Arquiteto-Chefe):** com o SX-001, a validação deixou de ser um ciclo
endógeno (`ECP → experimentos → confirmação`) e passou a ser confrontada com o
**mundo como referência** (Challenger → Atomic Facts → Kernel → Reconstrução →
Rogers Commission). Isso muda o status epistemológico do projeto. Mas um único
caso não calibra métrica nem estabelece universalidade — o `EAR` passa a ser
escrito como observação (`EAR(Challenger)`), e o programa de pesquisa muda de
**Law Discovery** para **Cross-Domain Validation**:

> **A pergunta deixa de ser "qual lei existe?" e passa a ser "esta mesma
> estrutura emerge espontaneamente em domínios completamente diferentes?".**

- [x] **P-0008 aberto** — charter completo ([P-0008](experiments/validation/P-0008-CROSS-DOMAIN-VALIDATION.md)); objetivo: **Atlas da Engenharia** (mapa comparativo), não descobrir leis
- [x] **DISCOVERY-LOG aberto** — diário científico (não-AD, não-RFC, não-LAW); DL-001 (Evidence→Decision), DL-002 (ausências), DL-003 (emergência da cadeia) ([DISCOVERY-LOG](experiments/validation/DISCOVERY-LOG.md))
- [x] **EAR renomeado** para `EAR(<caso>)` — observação, não conclusão ([06-relatorio-ear](experiments/validation/independence/SX-001/report/06-relatorio-ear.md))
- [x] **Regra de Ouro da Evolução Científica** — *nenhuma parte da teoria pode evoluir mais rápido que o conjunto de evidências que a sustenta*; primeiro nasce evidência, depois teoria ([DISCOVERY-LOG](experiments/validation/DISCOVERY-LOG.md))
- [x] **RESEARCH-CHARTER aberto** — governança científica (não-AD, não-RFC): **RC-1 Evidence First**, **RC-2 Experimental Diversity**, **RC-3 Competing Explanations**, **RC-4 Theory Debt** (o experimento nunca falha; quem falha é a capacidade de explicá-lo), **RC-5 Asymmetry** ([RESEARCH-CHARTER](experiments/validation/RESEARCH-CHARTER.md))
- [x] **P-0008 v1.2** — objetivo: **Atlas da Engenharia** (Domínio→Entidades→Topologia→EAR→EER→Signals→Hipóteses concorrentes→Status); anti-viés de seleção (casos pequenos/pouco documentados/equipes reduzidas); **meta dos próximos 10 experimentos: a teoria muda o mínimo possível**
- [ ] **Selecionar SX-002** pelo protocolo congelado (critério: diversidade máxima em relação ao SX-001 — ex.: Saúde + Sucesso + Biomédica; **evitando o caso mais famoso** — anti memória coletiva)
- [ ] **Executar SX-002..SX-00n** (Hyatt Regency, Genoma, Warp Speed, ...) com o pipeline congelado
- [ ] **Comparar EAR/topologia/entidades entre domínios** — alimentar DISCOVERY-LOG, EER e Signals
- [ ] **Nenhuma LAW-H** até existir distribuição cross-domain e a leitura ECP explicar **melhor** que as concorrentes (anti-armadilha: Challenger pode ser caso favorável)

### P-0010 — Reproducibility Program (FASE D — prioridade atual, aberto em 2026-08-03)

**Decisão (Arquiteto-Chefe):** o gargalo do programa não é produzir mais
experimentos — é garantir que **qualquer pesquisador produza praticamente o
mesmo conjunto de Atomic Facts**. Sem isso, o restante do pipeline perde
comparabilidade (executor A → 46 fatos, B → 61, C → 38). A primeira pergunta de
um instrumento científico nunca é "os resultados são interessantes?", mas sim
**"pesquisadores independentes obtêm os mesmos resultados usando o mesmo
procedimento?"**.

- [x] **P-0010 aberto** — charter completo ([P-0010](experiments/validation/P-0010-REPRODUCIBILITY.md)); missão: *medir a estabilidade do pipeline — não do ECP, do pesquisador*
- [x] **Pergunta científica** — 10 pesquisadores + mesma Narrativa Original + mesmas fontes + protocolo congelado → mesmo Atomic Facts?
- [x] **Experimento definido** — Narrativa → 3+ avaliadores independentes (humanos e/ou LLMs diferentes) → medir **cobertura, divergência, concordância, conflitos**
- [x] **AFR (Atomic Facts Reproducibility)** — tratado como **observação do programa**, não métrica oficial (mesmo tratamento da EER)
- [x] **Gate de execução** — reprodutibilidade satisfatória **antes** do SX-002; só então atribuir o resultado ao protocolo ("não foi o Claude / o GPT / o executor — foi o protocolo")
- [x] **Regra SX-002 reforçada** — manter Saúde + Sucesso + Biomédica, mas **não escolher o caso mais famoso** (narrativa consolidada → risco de reconstrução por memória coletiva; preferir documentação abundante + investigação técnica sem narrativa única)
- [x] **DISCOVERY-LOG v2.3** — DL-008 (reprodutibilidade do Atomic Facts é o novo gargalo)
- [ ] **Rodada de reprodutibilidade** — executar com 3+ avaliadores sobre o SX-001
- [ ] **SX-002 após o gate** — domínio biomédico/saúde metodologicamente distinto do Challenger

### FASE E — Estabilidade (acordo interno, coordenação 2026-08-04)

**Decisão (Arquiteto-Chefe):** o projeto deixou de ser um framework e virou um
**laboratório**. Uma observação direta: cada nova ideia arquitetural acrescenta
pouca ciência e muito risco. O retorno marginal de mudanças estruturais caiu —
o que sobra é o valor da **evidência**.

> **Acordo interno, válido até o SX-010:**
> **Nenhuma mudança estrutural. Só evidência, só experimentos, só observações,
> só comparação.**

O que **fica proibido** até o SX-010:

- Nenhum novo programa, AD, RFC, lei, entidade, schema ou critério.
- Nenhuma mudança no pipeline congelado (Narrativa → Atomic Facts → Reconstrução
  → Alignment → EAR → Signals).
- Nenhuma migração estrutural (ex.: DISCOVERY-LOG para banco/grafo) nem
  reorganização em Theory/Runtime/Lab.

O que **fica permitido** (e é a missão):

- Executar SX-002..SX-010 com o protocolo congelado, maximizando diversidade.
- Medir reprodutibilidade (P-0010 / AFR) e comparabilidade entre casos.
- Registrar observações no DISCOVERY-LOG (DL-###) e alimentar o Atlas (P-0008).
- Acumular evidência comparativa para o P-0009 — sem executar ainda a fase 3.

> **Nova missão do programa (substitui "descobrir a teoria"):**
> **"Tentar sobreviver sem mudar a teoria."**

Um programa científico maduro não demonstra força criando uma hipótese nova a
cada experimento — demonstra força quando **a mesma estrutura explica fenômenos
muito diferentes sem ser constantemente modificada**. A métrica observada pela
coordenação nos próximos meses é justamente essa: se após SX-002..SX-010 o ECP
continuar explicando casos radicalmente distintos com alterações mínimas na
teoria, teremos evidência mais convincente do que qualquer documentação ou novo
artefato metodológico.

### Princípio da Conservação da Teoria (coordenação — NÃO entra na especificação)

O maior risco do programa daqui para frente é o **Theory Drift**: ajustar a
teoria a cada novo experimento para acomodar os resultados. O resultado final é
uma teoria que explica tudo **porque foi modificada para explicar tudo** — perde
poder científico.

> **Princípio da Conservação da Teoria:**
> **A teoria deve mudar mais lentamente que as evidências.**

| Ritmo | Mudança permitida |
|---|---|
| 1 experimento | nenhuma |
| 2 experimentos | provavelmente nenhuma |
| 5 experimentos | talvez uma observação |
| 10 experimentos | talvez uma hipótese |
| dezenas de experimentos | talvez uma revisão da teoria |

Evidência acumula rápido; teoria muda devagar. É exatamente isso que faz teorias
maduras sobreviverem.

### Orçamento de mudanças (disciplina da coordenação — não é artefato)

Até o SX-010:

```
Novas leis:      0
Novas entidades: 0
Novos critérios: 0
Novos schemas:   0
Novas RFCs:      0
Novos ADs:       0
```

O único ativo que pode crescer é: **experimentos, observações, Atlas,
Discovery Log.** Nada mais.

### Unidade de análise: o conjunto, não o caso (coordenação)

A unidade de análise deixa de ser o caso isolado (`SX-001`) e passa a ser o
**Conjunto SX-001..SX-010**. Ciência trabalha com **distribuição**, não com
exemplos isolados. Nenhum SX individual calibra nada; a leitura só é feita sobre
a distribuição acumulada.

### Atlas da Engenharia = principal produto científico (coordenação)

O Atlas deixa de ser documentação e passa a ser o **principal produto científico
do ECP**. Quando alguém perguntar "onde está a evidência?", a resposta não será
um AD nem uma LAW — será "olhe o Atlas". Ele mostra, caso a caso: entidades que
emergiram / não emergiram, EAR, EER, explicações concorrentes, contraexemplos e
estabilidade — o equivalente ao conjunto de resultados experimentais de um
laboratório.

### Declaração oficial (coordenação)

> **A Fase de Arquitetura terminou.** Daqui para frente, o projeto não é mais
> conduzido principalmente por arquitetos — é conduzido por **pesquisadores**. E
> pesquisadores passam muito mais tempo coletando dados do que inventando
> estruturas. A FASE E, como está, é a primeira fase do projeto considerada
> "industrializável" do ponto de vista científico — e deve permanecer **inalterada
> até o SX-010**.

> **Nota (indicador de coordenação):** a coordenação acompanha informalmente um
> **TSI (Theory Stability Index)** — quantas vezes seguidas executamos experimentos
> sem precisar mudar a teoria. **Não é oficial, não é documentado como métrica,
> não existe no projeto** — é apenas o critério mental de liderança para a FASE E.

> **Nota (previsão da coordenação):** a coordenação prevê que entre SX-004 e
> SX-006 aparecerá um caso que o ECP explicará mal. **Esta previsão não entra no
> projeto** — fica apenas como critério de leitura: quando (e se) ocorrer, esse
> será provavelmente o experimento mais valioso do programa, pois mostrará onde
> termina o domínio de validade da teoria.

### Postura da equipe (coordenação — não registrado na especificação)

- **Vocabulário:** trocar *implementar / desenvolver / construir / criar* por
  *observar / medir / reproduzir / comparar / falsificar*.
- **Compromisso anti-identidade:** se o Atlas mostrar, de forma consistente, que
  uma teoria concorrente explica melhor um conjunto de casos do que o ECP, o
  objetivo não será **defender** o ECP — será **entender por quê**. Isso protege
  o programa de transformar uma hipótese em identidade.
- **P-0010 lido como** *Reprodutibilidade da inferência científica*: não se
  verifica se duas pessoas produzem os mesmos Atomic Facts, mas se **duas
  inferências independentes, submetidas ao mesmo método, convergem para a mesma
  representação observacional** — formulação que permanece válida mesmo que os
  Atomic Facts evoluam para outra representação.
- **Era da Generalização** (conceitual): a última era — *"qual é exatamente o
  domínio de validade da teoria?"* — **não começa agora**; começa depois do
  SX-010. O ciclo científico (Observação → Experimento → Reprodutibilidade →
  Adversarial → Independência → Comparação → Atlas → Generalização) já está
  completo e não faltam peças.

Observações associadas: [DL-009](experiments/validation/DISCOVERY-LOG.md)
(divisão mental Theory / Runtime / Lab), [DL-010](experiments/validation/DISCOVERY-LOG.md)
(Discovery Log → grafo científico) e [DL-011](experiments/validation/DISCOVERY-LOG.md)
(Princípio da Conservação da Teoria) no DISCOVERY-LOG.

### P-0009 — Competitive Theory Validation (charter aberto em 2026-08-03)

**Decisão (Arquiteto-Chefe):** o SX-001 mediu apenas "quanto o ECP reconstrói"
(`EAR(Challenger) = 0.775`), não "quanto teorias concorrentes reconstruiriam".
Sem comparação, um EAR alto não discrimina o ECP de STAMP, Swiss Cheese, FRAM,
RCA, OODA ou Systems Thinking. A pergunta científica deixa de ser **"o ECP
explica?"** e passa a ser **"o ECP explica melhor?"** — a evidência deve ser
comparativa, não interna.

- [x] **P-0009 aberto** — charter completo ([P-0009](experiments/validation/P-0009-COMPETITIVE-THEORY-VALIDATION.md)); missão: *nunca avaliar o ECP sozinho, sempre contra rivais*
- [x] **Matriz comparativa definida** — `EAR(ECP) × EAR(STAMP) × EAR(FRAM) × EAR(RCA) × ...` por caso; empate não é derrota, mas remove poder de evidência
- [x] **Taxonomia provisória de leis** (conceito de pesquisa, NÃO artefato): Estrutural / Dinâmica / Epistêmica / Institucional — deve emergir dos dados, não ser assumida
- [x] **Hipótese leis × restrições** registrada (observacional): talvez o ECP descubra restrições invariantes ("violar isto → deixa de ser justificável"), não leis "A → B"; **nada muda agora**, apenas observação (DL-007)
- [x] **Regra de gate comparativa** — nenhuma LAW-H avança com base apenas em evidência interna; exige explicar melhor que os rivais (RC-3/RC-5)
- [x] **DISCOVERY-LOG v2.2** — DL-005 (evidência interna ≠ comparativa), DL-006 (taxonomia de leis), DL-007 (leis × restrições) ([DISCOVERY-LOG](experiments/validation/DISCOVERY-LOG.md))
- [ ] **Execução adiada** — começa na etapa 3 da ordem de coordenação: após SX-002/003/004 e um Atlas consistente; **nenhum AD/RFC/entidade novo criado** (a fundação é rica o suficiente)

## CAMADA 2 — Engenharia (congelada)

### 02-core — State Machine (ECP-100..199)

- [x] `ECP-100` — Máquina de Estados Formal: implementação do ciclo cognitivo do `ECP-010`; define também os contratos `discovery`, `research`, `planning`, `execution`/`validation` (rascunho)
- [ ] `ECP-101` — Refinamento do contrato `Discovery` (entendimento do objetivo)
- [ ] `ECP-102` — Refinamento do contrato `Research` (aquisição de conhecimento)
- [ ] `ECP-103` — Refinamento do contrato `Planning` (hipóteses, decisões e plano)
- [ ] `ECP-104` — Refinamento dos contratos `Execution` / `Validation`
- [x] Gramática formal de contratos em `schemas/` (JSON Schema por tipo + EBNF + linter; validada contra os CASES ERP, Game, Hospital)

### 02-core — Capability Engine (ECP-200..299)

- [x] `ECP-200` — Declaração de capacidades de uma entidade (leitura, escrita, execução, verificação, pesquisa, memória); mapeamento capacidade → contrato; protocolo de negociação (descoberta, declaração, matching, fallback, assinatura); gramática em `schemas/` como interface (rascunho)
- [ ] Negociação de capacidades entre entidades (detalhamento das regras de composição e hierarquia)
- [ ] Mapeamento capacidade → contrato executável (extensões da tabela para contratos futuros)

### 03 — Runtime (ECP-300..399)

- [x] `ECP-300` — Motor de Execução sobre o Grafo: tupla `R=(G,Q,M,P)` (grafo, fila de reavaliação, máquina de estados, memória); contratos assinados como nós; propagação de invalidação (marcar suspeitos → priorizar → enfileirar → acordar, sem transicionar); tratamento de falhas (`FAILURE` → `go_to`/`retry`/`escalate`, bloqueio sem tratamento); sessão e memória persistente; regras ECP-300.1..300.4 (rascunho)
- [x] Tipos de runtime na gramática em `schemas/` (`runtime_event`, `runtime_reaval`, `runtime_session`, `runtime_scenario`) + simulador `scripts/simulate_runtime.py` (12 documentos positivos conformes; 5 falsificações detectadas)
- [ ] Implementação de referência do motor (comportamento vivo sobre o grafo)

### 04 — Governance (ECP-400..499)

- [ ] Processo formal de mudança da especificação
- [ ] Deprecação e remoção de documentos
- [ ] Critérios de `Aprovado`

### 05 — Quality (ECP-500..599) — adiado pelo AD-001 (feature freeze)

- [ ] Métricas de qualidade da engenharia executada sob ECP
- [ ] Padrões de evidência e auditoria de conformidade (lê Decision/Evidence/Goal Records)

### 06 — Learning (ECP-600..699) — adiado pelo AD-001 (feature freeze)

- [ ] Calibração contínua de confiança (curvas por entidade)
- [ ] Retroalimentação de resultados observados para decisões futuras
- [ ] Reutilização de conhecimento entre projetos

### 07 — Certification (ECP-700..799) — adiado pelo AD-001 (feature freeze)

- [ ] Certificação de conformidade de uma entidade ao ECP
- [ ] Auditoria independente de projetos executados sob ECP
- [ ] Selo de conformidade e relatórios públicos

## APOIO

### 08 — Reference (ECP-800..899)

- [ ] Casos de uso completos
- [ ] Implementação de referência (agente de demonstração)
- [ ] Glossário consolidado e traduções (en)

## Previsão de longo prazo

Se o rigor se mantiver, o ECP tende a deixar de ser descrito como "protocolo" e passar a ser reconhecido como um **meta-modelo para desenvolvimento de projetos** — a descrição de como qualquer sistema racional, humano ou artificial, conduz um projeto de forma auditável, justificável e iterativa.
