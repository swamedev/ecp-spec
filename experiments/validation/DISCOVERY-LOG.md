# DISCOVERY-LOG — Diário Científico do Validation Program

| Campo | Valor |
|---|---|
| **Tipo** | Diário científico (observações) — **NÃO é** AD, RFC, LAW, schema nem critério |
| **Status** | Ativo |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe (coordenação 2026-08-03) |
| **Governado por** | [ROADMAP — Fase C2](../ROADMAP.md), [P-0006](./P-0006-LAW-DISCOVERY.md), [P-0007](./P-0007-INDEPENDENCE.md), [P-0008](./P-0008-CROSS-DOMAIN-VALIDATION.md), [RESEARCH-CHARTER](./RESEARCH-CHARTER.md) |

## Propósito

Registrar **observações científicas** produzidas pelos experimentos (EXP-*,
SX-*), **antes** de qualquer consolidação em lei. É o "caderno de laboratório"
do Validation Program — e, desde a coordenação de 2026-08-03, o **centro do
projeto**: a evidência nasce aqui, antes da teoria.

> **Regra central:** uma observação promissora **não** vira teoria por
> entusiasmo. Ela é anotada aqui, com `Status: Observação`, e só evolui quando
> **evidência independente** a sustentar (múltiplos domínios, múltiplas
> ocorrências). Isso evita o erro clássico de projetos científicos: transformar
> rapidamente uma observação promissora em uma teoria consolidada.

## Regra de Ouro da Evolução Científica

> **Nenhuma parte da teoria pode evoluir mais rápido que o conjunto de
> evidências que a sustenta.**

| Na prática | Proibido |
|---|---|
| Nasce **evidência** primeiro | Nasce **LAW** porque um caso deu certo |
| Nasce **evidência** primeiro | Nasce **entidade** porque ela "faz sentido" |
| Nasce **evidência** primeiro | Nasce **RFC** porque surgiu uma ideia boa |

O fluxo é sempre:

```
Novo experimento → novos dados → nova observação → Discovery Log → (esperar)
→ outro experimento → comparação → somente então mudar a teoria
```

## Estrutura de um registro

```
DL-###
origem:              # experimento(s) que produziram a observação
domínio:             # domínio do caso (Aeronáutica, Saúde, Infraestrutura, ...)
observação:          # o que foi observado
explicações concorrentes:   # outras explicações possíveis para o mesmo fato
hipóteses concorrentes:     # hipóteses que competem com a leitura ECP
generalização proibida:     # o que NÃO se pode concluir deste caso isolado
evidência:           # onde está o dado bruto (arquivo:seção)
status:              # Observação | Confirmado (≥2 domínios) | Consolidado (padrão)
exigência:           # o que é preciso para evoluir o status
contraexemplos:      # ocorrências que contradizem (RA-SIG-004)
```

> **Por que `hipóteses concorrentes`?** Isto força honestidade científica: toda
> leitura via Kernel compete com explicações alternativas. Um programa científico
> não precisa apenas **explicar**; precisa **explicar melhor**.

## Registros

### DL-001 — Evidence → Decision emergiu espontaneamente (SX-001)

```
DL-001
origem:              EXP-SX001 (Challenger STS-51-L)
domínio:             Aeroespacial / Aeronáutica
observação:          A reconstrução cega — usando apenas os Atomic Facts e o
                     Kernel, sem o vocabulário ECP na coleta e sem consultar o
                     relatório oficial — localizou sozinha a falha no elo
                     Evidence → Decision: as decisões de lançamento foram
                     autorizadas com base em suposições (A-1/A-2/A-3) e sem
                     evidência suficiente para o risco (AF-018).
explicações concorrentes:
                     - Narrativa histórica: "decisão baseada em informação
                       incompleta e enganosa" (Rogers Commission).
                     - Sociologia organizacional: pressão programática e cultura
                       de segurança.
                     - Teoria da decisão clássica: custos de adiamento vs.
                       benefício esperado mal calculado.
hipóteses concorrentes:
                     - H-A: a estrutura Evidence→Decision é uma regularidade
                       universal da engenharia (leitura ECP).
                     - H-B: o Challenger é um caso favorável — a leitura ECP
                       coincidiu porque o caso é extremo e documentado.
                     - H-C: a reconstrução foi contaminada pelo executor que
                       também produziu a narrativa (viés do mesmo autor).
generalização proibida:
                     - NÃO concluir que "toda falha de engenharia vem do elo
                       Evidence→Decision".
                     - NÃO promover isto a LAW-H com um único caso.
evidência:           experiments/validation/independence/SX-001/reconstruction/
                     03-reconstrucao-cega.md §2;
                     experiments/validation/independence/SX-001/comparison/
                     04-alignment-analysis.md (NI-001);
                     experiments/validation/independence/SX-001/report/
                     06-relatorio-ear.md §3.2
status:              Observação
exigência:           Confirmar em pelo menos 2 domínios radicalmente diferentes
                     (ex.: Deepwater Horizon, Hyatt Regency) via P-0008, E
                     superar as hipóteses concorrentes (explicar melhor que
                     H-B e H-C).
contraexemplos:      Nenhum até agora.
```

### DL-002 — Ausência de infraestrutura cognitiva é observável (SX-001)

```
DL-002
origem:              EXP-SX001 (Challenger STS-51-L)
domínio:             Aeroespacial / Aeronáutica
observação:          O ECP explicou também o que FALTAVA: Problem não declarado,
                     Risk não calculado, validação pré-decisão ausente, registro
                     de decisão incompleto. As ausências emergiram do traço, não
                     foram inferidas depois.
explicações concorrentes:
                     - A ausência pode ser artefato da documentação histórica
                       (o que não foi registrado ≠ o que não existia).
hipóteses concorrentes:
                     - H-A: ausência de infraestrutura cognitiva correlaciona
                       com falha (leitura ECP).
                     - H-B: a documentação pública de postmortems omite
                       deliberadamente esses artefatos.
generalização proibida:
                     - NÃO concluir que "falta de Problem/Risk causa falha".
                     - NÃO concluir que "ausência observada = ausência real"
                       sem cruzar com fontes internas.
evidência:           .../SX-001/reconstruction/03-reconstrucao-cega.md §3
status:              Observação
exigência:           Confirmar a ausência observável em outro domínio de falha
                     (ex.: Deepwater Horizon, Hyatt Regency), controlando a
                     hipótese H-B (ausência documental).
contraexemplos:      Nenhum até agora.
```

### DL-003 — Cadeia cognitiva emerge sem o vocabulário ECP (SX-001)

```
DL-003
origem:              EXP-SX001 (Challenger STS-51-L)
domínio:             Aeroespacial / Aeronáutica
observação:          As entidades centrais do Kernel emergiram dos fatos de um
                     projeto que nunca usou o ECP (EAR(Challenger) = 0.775,
                     falso positivo zero). Entidades ausentes também foram
                     detectadas.
explicações concorrentes:
                     - A cadeia é uma leitura plausível entre muitas; outra
                       taxonomia (ex.: análise de causa-raiz tradicional) poderia
                       descrever os mesmos fatos.
hipóteses concorrentes:
                     - H-A: a cadeia é uma regularidade da engenharia.
                     - H-B: a cadeia é onipresente porque é genérica demais —
                       qualquer processo pode ser "lido" em Goal→Decision.
generalização proibida:
                     - NÃO concluir que a cadeia é universal por 1 caso.
                     - NÃO descartar H-B (genericidade) até a EER comparar com
                       alternativas.
evidência:           .../SX-001/reconstruction/03-reconstrucao-cega.md §1–§5;
                     .../SX-001/report/06-relatorio-ear.md §3.1
status:              Observação
exigência:           Repetir em domínios de origens independentes (P-0008) e
                     comparar a emergência da cadeia com a de taxonomias
                     alternativas. Consolidação alimentaria SIG-003 (RA-SIG-001).
contraexemplos:      Nenhum até agora.
```

### DL-004 — Mudança de categoria do projeto (coordenação)

```
DL-004
origem:              Coordenação 2026-08-03 (não-experimental)
domínio:             Governança científica do Validation Program
observação:          O ECP deixou de ser descrito como especificação ou sistema
                     operacional e passou a ser um PROGRAMA DE PESQUISA SOBRE
                     ENGENHARIA JUSTIFICÁVEL. Consequência: o sucesso do projeto
                     passa a depender da qualidade das evidências, não dos
                     documentos.
explicações concorrentes:
                     - Pode ser apenas um renomeio sem efeito prático.
hipóteses concorrentes:
                     - H-A: a mudança de categoria muda a alocação de esforço
                       (evidência > documentação).
                     - H-B: é cosmética; o comportamento do projeto não muda.
generalização proibida:
                     - NÃO concluir que a mudança "funciona" sem medir a
                       alocação de esforço nos próximos ciclos.
evidência:           RESEARCH-CHARTER.md; ROADMAP — Fase C2/P-0008
status:              Observação
exigência:           Verificar nos próximos ciclos se a produção de evidência
                     superou a produção de documentação (falsificável).
contraexemplos:      Nenhum até agora.
```

### DL-005 — Evidência atual é interna, não comparativa (coordenação)

```
DL-005
origem:              Coordenação 2026-08-03 (não-experimental); SX-001
domínio:             Governança científica do Validation Program
observação:          O SX-001 mediu apenas "quanto o ECP reconstrói"
                     (EAR(Challenger) = 0.775). Não mediu "quanto teorias
                     concorrentes reconstruiriam o mesmo caso". Sem essa
                     comparação, um EAR alto não discrimina o ECP de STAMP,
                     Swiss Cheese, FRAM, RCA, OODA ou Systems Thinking.
explicações concorrentes:
                     - Talvez os rivais também alcancem EAR comparável — a
                       vantagem do ECP seria ilusória (viés de confirmação).
hipóteses concorrentes:
                     - H-A: o ECP explica MELHOR que os rivais nos casos SX
                       (a ser medido).
                     - H-B: os rivais explicam tão bem quanto — EAR alto é
                       propriedade do caso, não da teoria.
generalização proibida:
                     - NÃO tratar EAR(Challenger) = 0.775 como evidência de
                       superioridade sem matriz comparativa.
                     - NÃO interpretar "o ECP explica" como "o ECP explica
                       mais" (P-0009).
evidência:           experiments/validation/P-0009-COMPETITIVE-THEORY-VALIDATION.md
status:              Observação
exigência:           Executar P-0009 (fase 3) após conjunto consistente de casos:
                     construir a matriz EAR(ECP) × EAR(rivais) e exigir
                     evidência comparativa para qualquer promoção de LAW-H.
contraexemplos:      Nenhum até agora.
```

### DL-006 — Taxonomia provisória de leis (conceito de pesquisa)

```
DL-006
origem:              Coordenação 2026-08-03 (não-experimental)
domínio:             Epistemologia do Validation Program
observação:          As futuras generalizações podem ser lidas por uma lente
                     provisória de 4 classes: Estrutural (o que deve existir —
                     Problem/Goal/Decision), Dinâmica (como interagem no tempo),
                     Epistêmica (condições de justificabilidade — Knowledge/
                     Evidence antes de decidir) e Institucional (múltiplos
                     agentes, organizações, governança).
explicações concorrentes:
                     - As classes podem não ser exaustivas nem disjuntas nos
                       dados reais; podem se sobrepor ou deixar lacunas.
hipóteses concorrentes:
                     - H-A: as classes emergem naturalmente dos dados dos SX.
                     - H-B: são categorias impostas; os dados não se encaixam
                       bem nelas.
generalização proibida:
                     - NÃO criar artefato (schema/critério/regra) com base nesta
                       lente agora.
                     - NÃO classificar leis até existirem leis reais para
                       classificar.
evidência:           experiments/validation/P-0009-COMPETITIVE-THEORY-VALIDATION.md
                     §"Taxonomia provisória de leis"
status:              Observação
exigência:           Quando houver generalizações candidatas reais (pós-SX-002..00n),
                     classificar cada uma nesta lente e verificar se a
                     distribuição confirma ou refuta a taxonomia.
contraexemplos:      Nenhum até agora.
```

### DL-007 — Leis × Restrições (hipótese filosófica)

```
DL-007
origem:              Coordenação 2026-08-03 (não-experimental)
domínio:             Epistemologia do Validation Program
observação:          Talvez o ECP não descubra LEIS ("A implica B"), mas
                     RESTRIÇÕES INVARIANTES ("qualquer engenharia que viole isto
                     deixa de ser justificável"). A formulação como restrição
                     aproxima o ECP de áreas maduras (invariantes, propriedades
                     fundamentais).
explicações concorrentes:
                     - "Lei" e "restrição" podem ser formulações do mesmo
                       conteúdo — sem diferença observável.
hipóteses concorrentes:
                     - H-A: os dados dos próximos SX apontam para restrições
                       (violações → perda de justificabilidade).
                     - H-B: apontam para implicações causais (A → B).
                     - H-C: a distinção não produz diferença observável.
generalização proibida:
                     - NÃO mudar nada agora: não renomear LAW, não alterar
                       LAW-CRITERIA, não criar artefato.
evidência:           experiments/validation/P-0009-COMPETITIVE-THEORY-VALIDATION.md
                     §"Leis × Restrições"
status:              Observação
exigência:           Ao longo dos próximos SX, registrar qual formulação os
                     dados favorecem. Se favorecer restrições, discutir o
                     impacto na nomenclatura (pós-coleção de casos).
contraexemplos:      Nenhum até agora.
```

### DL-008 — Repro­dutibilidade do Atomic Facts é o novo gargalo (coordenação)

```
DL-008
origem:              Coordenação 2026-08-03 (não-experimental); P-0010
domínio:             Governança científica do Validation Program
observação:          A etapa Narrativa → Atomic Facts ainda depende do executor:
                     quem escolhe os fatos, onde começa e termina, quando um
                     parágrafo vira 1 ou 5 fatos. Sem controle, executor A/B/C
                     produzem 46/61/38 fatos — todos honestos, todos diferentes —
                     e o restante do pipeline perde comparabilidade. O gargalo do
                     programa não é produzir mais experimentos; é garantir que
                     qualquer pesquisador produza praticamente o mesmo conjunto
                     de Atomic Facts.
explicações concorrentes:
                     - A variação pode ser inerente à linguagem (dois leitores
                       legítimos do mesmo texto podem granularizar diferente).
hipóteses concorrentes:
                     - H-A: a variação é controlável pelo protocolo congelado —
                       AFR alto entre avaliadores independentes.
                     - H-B: a variação é dominada pelo executor — AFR baixo, e o
                       pipeline precisa de regras de granularidade explícitas.
generalização proibida:
                     - NÃO atribuir nenhum resultado de SX a "o protocolo"
                       enquanto a reprodutibilidade (AFR) não for medida.
                     - NÃO tratar AFR como métrica oficial — é observação.
evidência:           experiments/validation/P-0010-REPRODUCIBILITY.md
status:              Observação
exigência:           Rodada de reprodutibilidade (3+ avaliadores — humanos e/ou
                     LLMs diferentes) sobre o mesmo caso; medir cobertura,
                     divergência, concordância e conflitos. Gate: SX-002 só após
                     evidência satisfatória.
contraexemplos:      Nenhum até agora.
```

### DL-009 — O projeto deixou de ser um framework; virou três produtos (coordenação)

```
DL-009
origem:              Coordenação 2026-08-04 (não-experimental)
domínio:             Governança científica do Validation Program
observação:          O ECP hoje parece um LABORATÓRIO, não um framework: Runtime,
                     Kernel, Experimentos, Corpus, Signals, Patterns, LAW-H,
                     LAW-C, LAW, Discovery Log, Independence, Adversarial,
                     Competitive Validation. Para pensar com clareza, divide-se
                     mentalmente em três produtos:
                     - ECP THEORY (a ciência — leis, observações, experimentos,
                       Discovery Log, Research Charter, Validation Program;
                       nunca executa, nunca depende de tecnologia — o "paper
                       vivo");
                     - ECP RUNTIME (a engenharia — implementa a teoria; não
                       descobre leis, não muda o protocolo);
                     - ECP LAB (o laboratório — SX, EAR, Atlas, Comparative
                       Validation, AFR, Hostile Experiments, Independence,
                       ferramentas).
                     Pertencimento de artefatos: Signal → Lab; EAR → Lab;
                     Atomic Facts → Lab; Shadow → Lab; Competitive Validation →
                     Lab.
explicações concorrentes:
                     - A divisão em três produtos pode ser apenas heurística
                       mental — os artefatos continuam no mesmo repositório.
hipóteses concorrentes:
                     - H-A: a divisão organiza o projeto e protege a Theory de
                       acoplamento tecnológico.
                     - H-B: é cosmética; não altera decisões práticas.
generalização proibida:
                     - NÃO criar três repositórios/estruturas agora (acordo de
                       estabilidade até SX-010 — coordenação).
                     - NÃO mover artefatos entre pastas com base nesta divisão.
evidência:           ROADMAP — FASE E; DISCOVERY-LOG DL-009
status:              Observação
exigência:           Manter como lente mental durante os SX-002..010; só avaliar
                     uma separação física de Theory/Runtime/Lab após SX-010 e com
                     base em evidência de que isso melhora a reprodutibilidade.
contraexemplos:      Nenhum até agora.
```

### DL-010 — O Discovery Log evoluirá de diário para grafo científico (observação)

```
DL-010
origem:              Coordenação 2026-08-04 (não-experimental)
domínio:             Governança científica do Validation Program
observação:          O DISCOVERY-LOG começou como um diário e já funciona como um
                     banco de conhecimento científico (Observation → Evidence →
                     Experiment → Domains → Counterexamples → Status → Links).
                     Em algum momento ele deixará de ser markdown e virará um
                     grafo de observações — um grafo científico.
explicações concorrentes:
                     - O markdown estruturado pode permanecer suficiente por
                       muito tempo; a estruturação em campos já é quase um grafo.
hipóteses concorrentes:
                     - H-A: um grafo formalizado (banco de observações) é
                       inevitável à medida que DL-### cresce e os links entre
                       experimentos se multiplicam.
                     - H-B: o formato atual absorve o crescimento; migração
                       desnecessária.
generalização proibida:
                     - NÃO migrar o DISCOVERY-LOG para banco/grafo agora (acordo
                       de estabilidade até SX-010).
                     - NÃO criar schema de observações como artefato.
evidência:           experiments/validation/DISCOVERY-LOG.md (estrutura de campos)
status:              Observação
exigência:           Observar o crescimento do DL-### durante SX-002..010. Se a
                     navegação/rastreabilidade exigir estrutura formal, propor a
                     migração pós-SX-010 com base em evidência, não em previsão.
contraexemplos:      Nenhum até agora.
```

### DL-011 — Princípio da Conservação da Teoria (coordenação)

```
DL-011
origem:              Coordenação 2026-08-04 (não-experimental)
domínio:             Governança científica do Validation Program
observação:          O maior risco do programa é o Theory Drift: ajustar a
                     teoria a cada novo experimento para acomodar os resultados.
                     O resultado é uma teoria que explica tudo porque foi
                     modificada para explicar tudo — perde poder científico.
                     Proteção: Princípio da Conservação da Teoria — a teoria
                     deve mudar mais lentamente que as evidências.
                     Ritmo: 1 experimento → nenhuma mudança; 2 → provavelmente
                     nenhuma; 5 → talvez uma observação; 10 → talvez uma
                     hipótese; dezenas → talvez uma revisão. Orçamento de
                     mudanças até SX-010: 0 leis, 0 entidades, 0 critérios, 0
                     schemas, 0 RFCs, 0 ADs. Apenas experimentos, observações,
                     Atlas e Discovery Log podem crescer.
explicações concorrentes:
                     - A conservação pode ser exagerada: um programa que nunca
                       ajusta a teoria pode manter erros indefinidamente.
hipóteses concorrentes:
                     - H-A: a conservação protege a teoria do Theory Drift e
                       aumenta o valor das revisões (só mudar por base robusta).
                     - H-B: o congelamento excessivo adia revisões necessárias.
generalização proibida:
                     - NÃO inserir este princípio na especificação (é disciplina
                       da coordenação, não artefato).
                     - NÃO usar o orçamento para impedir registro de observação
                       contrária — contraexemplos nunca são ocultados.
evidência:           ROADMAP — FASE E (Princípio da Conservação da Teoria;
                     Orçamento de mudanças)
status:              Observação
exigência:           Manter o orçamento de mudanças até o SX-010; se alguma
                     revisão for exigida antes, justificar com base em evidência
                     acumulada (não em caso isolado) e registrar no diário.
contraexemplos:      Nenhum até agora.
```

### DL-012 — Era da Generalização e compromisso anti-identidade (coordenação)

```
DL-012
origem:              Coordenação 2026-08-04 (não-experimental)
domínio:             Governança científica do Validation Program
observação:          O projeto passou por cinco eras coerentes: Protocolo
                     (como pensar), Runtime (como executar), Validação (como
                     provar), Independência (como evitar autoengano) e
                     Estabilidade (como impedir deriva da teoria). Existe uma
                     única era restante — a Era da Generalização — que NÃO deve
                     começar agora, e sim depois do SX-010. Pergunta central:
                     "qual é exatamente o domínio de validade da teoria?"
                     Compromisso anti-identidade: se o Atlas mostrar de forma
                     consistente que uma teoria concorrente explica melhor um
                     conjunto de casos, o objetivo não será defender o ECP, mas
                     entender por quê. Vocabulário: trocar implementar/
                     desenvolver/construir/criar por observar/medir/reproduzir/
                     comparar/falsificar.
explicações concorrentes:
                     - O compromisso anti-identidade é impossível de garantir
                       por escrito; depende de cultura.
hipóteses concorrentes:
                     - H-A: o compromisso protege o programa de transformar a
                       hipótese em identidade — o maior risco de um programa de
                       pesquisa.
                     - H-B: é retórico; na prática a defesa do ECP prevalecerá.
generalização proibida:
                     - NÃO iniciar a Era da Generalização antes do SX-010.
                     - NÃO registrar este compromisso na especificação (é
                       disciplina da coordenação).
evidência:           ROADMAP — FASE E; RESEARCH-CHARTER §Conservação da Teoria
status:              Observação
exigência:           Quando a comparação com rivais (P-0009) mostrar derrota
                     consistente do ECP em um subconjunto de casos, o registro
                     deve ser de investigação ("por que essa teoria explica
                     melhor?"), nunca de defesa.
contraexemplos:      Nenhum até agora.
```

### DL-013 — Estágio do programa e sequência analítica pós-SX-010 (coordenação)

```
DL-013
origem:              Coordenação 2026-08-04 (não-experimental)
domínio:             Governança científica do Validation Program
observação:          O ECP deixou de ser apenas um protocolo de engenharia e
                     passou a ser um PROGRAMA DE PESQUISA voltado à descoberta e
                     validação de princípios gerais de engenharia, sustentado
                     por um runtime experimental, governança metodológica e um
                     processo explícito de produção, auditoria e comparação de
                     evidências. Isto não significa que já há leis universais —
                     essa continua sendo uma hipótese em investigação — mas a
                     infraestrutura para testá-la já é, por si só, um resultado.
                     O maior risco epistemológico restante: o ECP ainda tenta
                     explicar o mundo usando apenas o próprio ECP (mitigado por
                     Shadow/Independence/Competitive Validation, mas não extinto).
                     Por isso o P-0009 pode ser hoje mais importante que o SX-002:
                     a pergunta correta não é "o ECP explica Challenger?", mas
                     "explica MELHOR que STAMP/FRAM/Swiss Cheese/RCA/OODA/Systems
                     Thinking? Em que aspectos? Onde explica pior?".
explicações concorrentes:
                     - A primazia dada ao P-0009 pode adiar evidências do Atlas
                       caso seja executado cedo demais (por isso fica após casos).
hipóteses concorrentes:
                     - H-A: a comparação com rivais transforma o ECP de teoria
                       interessante em teoria competitiva.
                     - H-B: toda a prioridade deve permanecer só na coleta de
                       evidências do Atlas até o SX-010.
generalização proibida:
                     - NÃO tratar o domínio universal do ECP como concluído —
                       segue hipótese em investigação.
                     - NÃO promover LAW-H antes da sequência analítica pós-SX-010.
evidência:           ROADMAP — FASE E; P-0009 (Competitive Theory Validation)
status:              Observação
exigência:           Após SX-010, e com o Atlas + Discovery Log completos, realizar
                     a pausa analítica longa: quais observações apareceram em TODOS
                     os casos? quais desapareceram? quais rivais explicam melhor
                     determinados tipos de problemas? existe realmente uma Lei
                     Candidata? Somente então avaliar a promoção de LAW-H.
contraexemplos:      Nenhum até agora.
```

### DL-014 — O valor científico depende do conjunto de casos, não da sofisticação do protocolo

```
DL-014
origem:              Coordenação 2026-08-04 (não-experimental)
domínio:             Governança científica do Validation Program
observação:          À medida que a quantidade de evidências cresce, o valor
                     científico do ECP dependerá cada vez menos da sofisticação
                     do protocolo e cada vez mais da QUALIDADE DO CONJUNTO DE
                     CASOS estudados. No início, quase todo ganho vinha de
                     melhorar o método (pipeline, auditoria, independência,
                     hostile, corpus, shadow). Hoje isso mudou:
                     - Antes: melhor protocolo → melhor ciência.
                     - Agora: mesmo protocolo + mais diversidade experimental →
                       melhor ciência.
                     Comparação: 100 experimentos com pipeline igual produzem,
                     provavelmente, conhecimento mais confiável que 10
                     experimentos com pipeline perfeito — não por um protocolo
                     melhor, mas por uma evidência muito maior. O principal ativo
                     do projeto passa a ser o Atlas Experimental.
explicações concorrentes:
                     - O nível do protocolo importa sempre; a comparação assume
                       um mínimo de qualidade metodológica já garantido.
                     - Qualidade (diversidade e reprodutibilidade) pode pesar
                       mais que quantidade crua.
hipóteses concorrentes:
                     - H-A: a quantidade e a diversidade dos casos passam a ser
                       o fator dominante para a confiabilidade da inferência.
                     - H-B: uma quantidade grande de casos com baixa
                       reprodutibilidade (AFR baixo) não agrega valor.
generalização proibida:
                     - NÃO reduzir o investimento em reprodutibilidade (P-0010/
                       AFR) só porque "quantidade importa" — casos ruins não se
                       acumulam bem.
                     - NÃO tratar isto como lei; é observação do estágio atual.
evidência:           ROADMAP — FASE E; P-0008 (Atlas da Engenharia)
status:              Observação
exigência:           Priorizar ao longo dos SX-002..010 a DIVERSIDADE e a
                     QUALIDADE do conjunto (controle de reprodutibilidade), de
                     modo que o Atlas acumule evidência extensa e confiável —
                     a base das perguntas: quais estruturas em todos os domínios?
                     quais só em engenharia física? quais só em saúde? quais
                     desaparecem? onde o ECP explica melhor/pior? onde um rival
                     supera o ECP?
contraexemplos:      Nenhum até agora.
```

### DL-015 — Auditoria estratégica: continuidade e infraestrutura de pesquisa (revisão interna)

```
DL-015
origem:              Coordenação 2026-08-04 (não-experimental; revisão interna)
domínio:             Governança científica do Validation Program
observação:          Auditoria estratégica — PERGUNTA: "se o coordenador
                     desaparecesse hoje, outro grupo conseguiria continuar
                     exatamente de onde paramos?". Objeto da auditoria não é o
                     Runtime/Corpus/Signals — é o PRÓPRIO PROGRAMA CIENTÍFICO.
                     Checklist de estado (revisão interna, nenhum artefato novo):
                     - Pergunta científica claramente definida ........ ✅
                     - Hipóteses separadas de observações ............. ✅
                     - Pipeline congelado ............................. ✅
                     - Critérios pré-registrados ..................... ✅
                     - Dados reproduzíveis ........................... Em andamento (P-0010)
                     - Comparação com teorias rivais ................. Planejada (P-0009)
                     - Diversidade experimental ..................... Em construção
                     - Risco de viés documentado .................... ✅
                     - Dívida metodológica registrada .............. ✅
                     - Contraexemplos preservados .................. ✅
                     Enquadramento: o projeto começa a ser uma
                     INFRAESTRUTURA PARA PESQUISA EM ENGENHARIA (permite que
                     diferentes teorias sejam testadas), e não apenas uma teoria
                     (que responde perguntas) — o ECP ainda busca sua própria
                     teoria, mas já constrói a infraestrutura para testá-la.
explicações concorrentes:
                     - A auditoria pode ser apenas autoavaliação; não mede a
                       reprodutibilidade real (depende de outra liderança).
hipóteses concorrentes:
                     - H-A: o checklist confirma adesão ao método declarado.
                     - H-B: há lacunas — dados reproduzíveis (P-0010) e
                       comparação rival (P-0009) ainda pendentes; no SX-002 devem
                       ser as máximas prioridades.
generalização proibida:
                     - NÃO criar P-0011/AD/RFC/schema/critério a partir desta
                       auditoria.
                     - NÃO tratar o passe em itens sem verificar executabilidade
                       por outrem.
evidência:           ROADMAP — FASE E; P-0008; P-0009; P-0010; DISCOVERY-LOG
status:              Observação
exigência:           Reauditar o mesmo checklist após cada bloco de experimentos
                     (ex.: pós-SX-003, pós-SX-006, pós-SX-010); o marco decisivo
                     é responder, só com o Atlas: quais estruturas aparecem em
                     quase todos os domínios? quais específicas? onde o ECP é
                     superior/equivalente/inferior aos rivais? — sem precisar
                     modificar a teoria.
contraexemplos:      Nenhum até agora.
```

### DL-016 — Maturidade, Atlas como experimento e Dashboard científico (coordenação)

```
DL-016
origem:              Coordenação 2026-08-04 (não-experimental; avaliação de estágio)
domínio:             Governança científica do Validation Program
observação:          Avaliação de MATURIDADE (não de qualidade) do programa:
                     - Arquitetura ........ 9.8/10
                     - Governança ........ 10/10
                     - Rastreabilidade .. 10/10
                     - Reprodução ....... 8/10 (P-0010 em andamento)
                     - Evidência Exp. ... 4/10
                     - Diversidade de domínios 2/10
                     - Comp. rival ...... 1/10
                     - Generalização ... 0/10 (corretamente).
                     Não é crítica: é o que se espera de um programa saudável —
                     infraestrutura construída antes de grandes afirmações. O
                     gargalo mudou: não é mais "como melhorar o protocolo?", e
                     sim "como produzir evidência suficientemente diversa?". O
                     ATLAS é o experimento (não um produto): é onde hipóteses
                     sobrevivem ou morrem — ex.: se Knowledge aparece em 100% dos
                     casos, Execution Intent em 18%, Observation só em domínios
                     regulados, essa distribuição vale mais que dezenas de
                     discussões teóricas.
explicações concorrentes:
                     - A nota baixa em evidência/diversidade é esperada nesta
                       fase e não indica falha — indica onde está o trabalho.
hipóteses concorrentes:
                     - H-A: o Atlas (distribuições EAR/EER/entidades) torna-se a
                       principal base de inferência do programa.
                     - H-B: sem controle de reprodutibilidade (AFR), as
                       distribuições podem ser artefato do executor.
generalização proibida:
                     - NÃO construir Atlas Dashboard agora (é desperdício nesta
                       fase; deve ser a principal interface só após 10–20 casos
                       — pós-SX-010).
                     - NÃO transformar a futura pergunta preditiva ("o que o ECP
                       prevê antes que um humano perceba?") em objetivo atual.
evidência:           ROADMAP — FASE E; P-0008 (Atlas da Engenharia)
status:              Observação
exigência:           Pós-SX-010: avaliar a criação de um ATLAS DASHBOARD CIENTÍFICO
                     (não-operacional): Domínios, Casos, EAR médio, EAR por domínio,
                     Entidades emergentes, Topologias recorrentes, Contraexemplos,
                     Rivais vencedores/empatados, Domínio de validade, Hipóteses
                     sobreviventes. E, com o Atlas rico, priorizar a pergunta
                     preditiva sobre a retrospectiva.
contraexemplos:      Nenhum até agora.
```

### DL-017 — Desafio científico, foco das observações e arquitetura futura (coordenação)

```
DL-017
origem:              Coordenação 2026-08-04 (não-experimental)
domínio:             Governança científica do Validation Program
observação:          O maior desafio do ECP deixou de ser técnico e passou a ser
                     CIENTÍFICO — o que muda até o perfil das pessoas: de bom
                     engenheiro de software para pesquisador + metodologista +
                     filósofo da ciência + estatístico + engenheiro ao mesmo
                     tempo. Dois futuros reconhecidos (especulação, não
                     arquitetura agora):
                     (a) ARQUITETURA FUTURA EM DUAS CAMADAS: Camada Científica
                     (Leis Universais → Ontologia) separada da Camada Operacional
                     (Heurísticas → Contratos → Runtime → Ferramentas). Hoje é
                     especulação; depois do Atlas, pode ser consequência natural
                     dos dados. Não criar agora.
                     (b) MIGRAÇÃO DO FOCO DO DIÁRIO: observações sobre o ECP
                     devem gradualmente ceder espaço a observações SOBRE A
                     ENGENHARIA (ex.: "projetos com alta incerteza tendem a
                     produzir cadeias Knowledge→Evidence→Decision mais longas").
explicações concorrentes:
                     - A separação ciência × aplicação pode não se materializar;
                     a ontologia pode permanecer suficiente para o operacional.
hipóteses concorrentes:
                     - H-A: a proporção observações-sobre-o-ECP ×
                       observações-sobre-engenharia migra ao longo do tempo
                       (Ano1 90/10 → Ano2 50/50 → Ano3 20/80), sinal de
                       maturidade.
                     - H-B: o foco pode permanecer metodológico por muito tempo
                       (o programa continua validando o próprio método).
generalização proibida:
                     - NÃO criar a segunda camada (operacional) agora — não há
                       LAW-F; seria especulação.
                     - NÃO registrar observações "sobre engenharia" forçadamente;
                       a transição deve ser natural.
evidência:           ROADMAP — FASE E; P-0008 (Atlas da Engenharia)
status:              Observação
exigência:           Monitorar a proporção do foco do diário (indicador de
                     maturidade). A arquitetura em duas camadas só deve ser
                     considerada depois do Atlas, se os dados a exigirem. A
                     tensão metodológica (abstração ↑ → generalização ↑ →
                     poder operacional ↓) permanece como item monitorado pela
                     coordenação, SEM registro formal.
contraexemplos:      Nenhum até agora.
```

### DL-018 — Infraestrutura para descoberta científica: proteger os dados acima das ideias (coordenação)

```
DL-018
origem:              Coordenação 2026-08-04 (não-experimental)
domínio:             Governança científica do Validation Program
observação:          O ECP está se tornando uma INFRAESTRUTURA PARA DESCOBERTA
                     CIENTÍFICA EM ENGENHARIA — não para provar uma teoria, mas
                     para permitir que QUALQUER teoria seja testada. A evolução
                     de categoria: projeto de software → framework → protocolo →
                     programa de pesquisa → infraestrutura para descoberta
                     científica. O objetivo de um programa maduro não é
                     "descobrir leis", mas "produzir testes confiáveis" — as
                     leis são consequência. O teste que será histórico: dois
                     grupos independentes, sem contato, mesmo protocolo, mesmo
                     caso, mesmo Atlas → se chegarem a observações
                     aproximadamente iguais, o conhecimento produzido depende
                     mais do MÉTODO do que do PESQUISADOR. O Atlas pode ser mais
                     importante que a teoria: teorias mudam, dados permanecem.
                     Princípio: proteger os dados mais do que as ideias.
explicações concorrentes:
                     - A convergência entre grupos independentes pode nunca ser
                       testada (custosa); o valor seria aproximado por
                       reprodutibilidade intra-laboratório (AFR).
hipóteses concorrentes:
                     - H-A: o Atlas é o ativo mais durável do programa — evidência
                       organizada sobrevive à substituição parcial da teoria.
                     - H-B: sem reprodutibilidade verificada, o Atlas é apenas
                       uma coleção de interpretações.
generalização proibida:
                     - NÃO registrar a "Lei Zero" do programa (o valor do ECP
                       será medido pela confiabilidade com que mostra que uma
                       hipótese é falsa ou verdadeira) — permanece apenas como
                       bússola mental da coordenação, SEM documento.
                     - NÃO registrar o marco silencioso (dias sem discutir
                       mudanças no ECP, só fenômenos) — observação informal.
                     - NÃO usar o princípio "protejam os dados" para descuidar
                       da reprodutibilidade (dados mal reproduzidos não são
                       protegidos, são descartáveis).
evidência:           ROADMAP — FASE E; P-0010; P-0008 (Atlas da Engenharia)
status:              Observação
exigência:           Tratar o Atlas e os dados brutos como o ativo mais protegido
                     do projeto (auditoria, reprodução, preservação); manter o
                     foco do diário em produzir evidência confiável e
                     comparável. O teste intergrupo independente é o objetivo de
                     longo prazo da reprodutibilidade.
contraexemplos:      Nenhum até agora.
```

### DL-019 — Oito eras e gargalo estatístico: distribuição antes de estabilidade (coordenação)

```
DL-019
origem:              Coordenação 2026-08-04 (não-experimental; avaliação de estágio)
domínio:             Governança científica do Validation Program
observação:          O projeto pode ser dividido em oito eras:
                     - Runtime .................. construir o ECP ..... ✅ encerrada
                     - Validation ............... validar entidades ... ✅ encerrada
                     - Law Discovery ............ descobrir leis ...... 🟡 em andamento
                     - Independence ............. eliminar endogeneidade 🟡 em andamento
                     - Adversarial .............. tentar destruir hipóteses 🟡 em andamento
                     - Reproducibility .......... outro pesquisador chega ao mesmo resultado 🔴 GARGALO ATUAL
                     - Cross Domain ............. estabilidade entre domínios 🔴 início
                     - Competitive Validation ... comparar com STAMP/FRAM/etc 🔴 futuro
                     O projeto não sofre mais de "falta de arquitetura" — sofre
                     de FALTA DE EVIDÊNCIA (excelente problema). O maior risco
                     mudou: gastar meses refinando infraestrutura quando ela já
                     é suficiente — mais protocolo não significa mais ciência.
                     O gargalo real não é metodológico, é ESTATÍSTICO: hoje há
                     praticamente só SX-001; só com SX-001..SX-010 surge
                     DISTRIBUIÇÃO, e sem distribuição não há estabilidade, e sem
                     estabilidade não há universalidade.
explicações concorrentes:
                     - A falta de evidência é esperada nesta fase; o problema
                       seria se a infraestrutura continuasse a crescer sem novos
                       casos.
hipóteses concorrentes:
                     - H-A: a curva de evidência (SX-002..010) muda o caráter do
                       programa, habilitando estabilidade e universalidade.
                     - H-B: mesmo com 10 casos, sem controle de reprodutibilidade
                       (AFR) a "distribuição" pode não ser confiável.
generalização proibida:
                     - NÃO criar mais nenhuma camada metodológica antes do SX-010.
                     - NÃO transformar a pergunta "as estruturas do ECP são
                       propriedades da engenharia ou apenas uma boa linguagem de
                       descrição?" em hipótese formal ainda (correto deixar de
                       fora; só muitos casos separam os dois mundos).
evidência:           ROADMAP — FASE E; P-0008; P-0010
status:              Observação
exigência:           Prioridade = produzir a distribuição (SX-002..010) com o
                     mesmo rigor do SX-001 e controle de reprodutibilidade;
                     promover hipóteses de lei só depois de avaliar padrões
                     recorrentes, contraexemplos e desempenho comparativo no Atlas.
contraexemplos:      Nenhum até agora.
```

### DL-020 — Ponto de inflexão: fator limitante é a evidência; três linhas de trabalho (coordenação)

```
DL-020
origem:              Coordenação 2026-08-04 (não-experimental; avaliação de estágio)
domínio:             Governança científica do Validation Program
observação:          Pela primeira vez, o fator limitante do projeto deixa de ser
                     o método e passa a ser a PRODUÇÃO DE EVIDÊNCIA — sinal de
                     maturidade. Avaliação de estado:
                     - Arquitetura do ECP ........ ✅ madura
                     - Pipeline científico ....... ✅ maduro
                     - Governança ............... ✅ muito madura
                     - Controle de viés .......... ✅ muito maduro
                     - Descoberta de leis ........ 🟡 preparada, sem base estatística suficiente
                     - Evidência experimental ... 🔴 ainda insuficiente
                     - Comparação com rivais ..... 🔴 ainda insuficiente
                     - Generalização ............. ⛔ ainda não permitida
                     A pergunta operacional muda de "o que falta implementar?"
                     para "qual é o próximo dado que falta produzir?". Divisão do
                     trabalho em três linhas (orientação de execução, não
                     artefatos): Linha 1 — Produção de Evidência (SX-002..010,
                     prioridade máxima); Linha 2 — Qualidade da Evidência
                     (apenas P-0010, auditorias, verificações independentes);
                     Linha 3 — Registro Científico (Discovery Log, Atlas,
                     resultados, contraexemplos).
explicações concorrentes:
                     - As três linhas são heurísticas de organização; não mudam
                       o orçamento de mudanças da FASE E.
hipóteses concorrentes:
                     - H-A: a prioridade na produção de evidência é o que mais
                       aumenta o valor científico do projeto neste momento.
                     - H-B: sem qualidade (AFR) e registro, a produção pura não
                       agrega distribuição confiável.
generalização proibida:
                     - NÃO criar novos índices/programas/RFCs/ADs/entidades antes
                       do SX-010 (listas: novas leis, critérios, índices,
                       programas, RFCs, ADs, entidades — todas evitadas).
                     - NÃO iniciar estudo prospectivo antes do SX-010 (ver
                       Parking Lot).
evidência:           ROADMAP — FASE E; P-0010; P-0008
status:              Observação
exigência:           Executar na ordem: Linha 1 (SX-002..010 com diversidade) +
                     Linha 2 (reprodutibilidade) + Linha 3 (registro no Atlas).
                     Após SX-010, o centro passa de "o que observamos?" para "o
                     que a distribuição dos casos mostra?".
contraexemplos:      Nenhum até agora.
```

### DL-021 — O Atlas como Data Warehouse científico e mecanismo de planejamento (coordenação)

```
DL-021
origem:              Coordenação 2026-08-04 (não-experimental)
domínio:             Governança científica do Validation Program
observação:          O Atlas pode ser visto maior do que um documento: um DATA
                     WAREHOUSE CIENTÍFICO, um banco de conhecimento científico
                     contendo Shadow Experiments, Atomic Facts, Entities, Signals,
                     Discovery Log, EAR, EER, Counterexamples e Rival Theories.
                     Com muitos casos, a direção do fluxo se inverte: hoje é
                     "caso → Atlas"; amanhã será "Atlas → perguntas → próximo
                     experimento". O Atlas começará a apontar lacunas de
                     evidência: "ainda não existe experimento de engenharia
                     agrícola", "há poucos sucessos biomédicos", "todos os casos
                     são falhas", "nenhum caso tem equipes < 5 pessoas". O fluxo
                     correto torna-se um ciclo científico fechado:
                     Experimento → Atlas → Lacunas de Evidência → Próximo
                     Experimento. O Atlas deixa de ser armazenamento passivo e
                     vira o MECANISMO DE PLANEJAMENTO DA PESQUISA.
explicações concorrentes:
                     - A inversão do fluxo depende de volume de casos e de
                       metadados estruturados (domínio, tamanho da equipe,
                       natureza, etc.) no Atlas; sem eles, não há "perguntas".
hipóteses concorrentes:
                     - H-A: o Atlas orientador de lacunas melhora a diversidade
                       deliberada (RC-2) e a cobertura do anti-viés de seleção.
                     - H-B: a curadoria das lacunas pode enviesar a seleção
                       (perseguir lacunas em vez de perguntas científicas).
generalização proibida:
                     - NÃO transformar o Atlas em banco/Data Warehouse agora —
                       é evolução pós-SX-010 (mesma disciplina do DL-010).
                     - NÃO automatizar a "detecção de lacunas" antes do volume
                       de casos justificar (seria ferramenta sem pergunta).
evidência:           P-0008 (Atlas da Engenharia); ROADMAP — FASE E
status:              Observação
exigência:           Após os primeiros conjuntos de casos, avaliar a estruturação
                     do Atlas como banco de conhecimento (não documento) e o uso
                     das lacunas de evidência para orientar a seleção do próximo
                     SX — preservando a diversidade e o anti-viés de seleção.
contraexemplos:      Nenhum até agora.
```

### DL-022 — Risco operacional e a regra de ganho de informação do Atlas (coordenação)

```
DL-022
origem:              Coordenação 2026-08-04 (não-experimental)
domínio:             Governança científica do Validation Program
observação:          Surge um novo tipo de risco — OPERACIONAL, não metodológico:
                     produzir dez Shadow Experiments completos é caro (seleção,
                     fontes, Atomic Facts, reconstrução cega, comparação,
                     Signals, relatório, reprodução, auditoria). O gargalo deixa
                     de ser intelectual e passa a ser CAPACIDADE DE EXECUÇÃO.
                     Meta para a equipe: cada novo experimento deve AUMENTAR A
                     INFORMAÇÃO DO ATLAS, não apenas aumentar o número de casos.
                     Exemplo: Apollo 13 e Challenger são ambos aeroespaciais — um
                     caso hospitalar ou agrícola agrega mais informação do que um
                     terceiro acidente aeroespacial. A seleção dos próximos SX
                     torna-se um problema de MAXIMIZAÇÃO DE GANHO DE INFORMAÇÃO
                     (cobertura da matriz diversidade × natureza), não de
                     conveniência ou fama. Refinamento do Atlas (pós-SX-010):
                     além de "Data Warehouse", ele tende a ser o INSTRUMENTO DE
                     OBSERVAÇÃO do programa — os Shadow Experiments observam o
                     mundo; o Atlas observa os Shadow Experiments (cobertura por
                     domínio, distribuição de entidades, frequência de
                     contraexemplos, lacunas experimentais).
explicações concorrentes:
                     - "Ganho de informação" é qualitativo; sem metadados
                       estruturados no Atlas, a escolha depende de julgamento.
hipóteses concorrentes:
                     - H-A: maximizar ganho de informação aumenta a diversidade
                       real do conjunto (RC-2) a um custo controlado.
                     - H-B: o custo fixo por SX é alto e pode limitar o número
                       total alcançável — priorizar diversidade pode exigir menos
                       casos em mais domínios.
generalização proibida:
                     - NÃO priorizar fama/conveniência do caso sobre o ganho de
                       informação na seleção do SX-002+.
                     - NÃO criar "métrica de ganho de informação" como artefato
                       agora — é critério de seleção, não índice oficial.
evidência:           P-0008 (Atlas da Engenharia — matriz de diversidade);
                     ROADMAP — FASE E
status:              Observação
exigência:           Aplicar a regra de ganho de informação na seleção de cada SX;
                     esperar do Atlas pós-SX-010: estruturas consistentes em quase
                     todos os domínios, estruturas dependentes de contexto, onde
                     rivais explicam melhor, onde o ECP acrescenta poder
                     explicativo e quais hipóteses merecem ser candidatas a lei.
contraexemplos:      Nenhum até agora.
```

### DL-023 — Rodada parcial de reprodutibilidade (P-0010), avaliação A×C (provisório)

```
DL-023
origem:              P-0010 (Reproducibility Program) — rodada parcial sobre o
                      SX-001 (Challenger STS-51-L); comparação Avaliador Oficial
                      (A) × Avaliador C.
domínio:             Aeroespacial / Aeronáutica (SX-001)
observação:          Resultado do estudo de reprodutibilidade — INCOMPLETO (não é
                      resultado do ECP). Na comparação A×C observou-se:
                      - Cobertura: 100% dos Atomic Facts oficiais presentes em C.
                      - Concordância de granularidade: 95,7%.
                      - Conflitos factuais: 0.
                      - Divergências observadas correspondem apenas a decomposição
                        mais fina de determinados fatos (C decompõe contexto de
                        engenharia do veículo em mais fatos: 56 vs. 46).
                      - Fatos exclusivos de C: construção do veículo (2 SRBs,
                        juntas de campo, 2 O-rings, função de vedação),
                        preocupação dos engenheiros com a elasticidade da borracha,
                        concordância Mulloy/Aldrich em prosseguir.
explicações concorrentes:
                      - A elevada convergência pode reflectir apenas que o caso
                        (Challenger) tem granularidade estável e documentação
                        rica — não uma propriedade geral do protocolo.
                      - A variação de granularidade pode ser inerente à linguagem
                        (leitores legítimos do mesmo texto granularizam diferente).
hipóteses concorrentes:
                      - H-A (hipótese de trabalho, NÃO confirmada): a maior fonte
                        de variabilidade entre avaliadores independentes pode ser
                        a granularidade da decomposição dos Atomic Facts, e não a
                        identificação dos acontecimentos.
                      - H-B: em outro domínio (hospital, agricultura, negócios)
                        podem surgir divergências de seleção, causalidade ou
                        temporalidade — o comportamento pode não ser geral.
                      - H-C: sem um Avaliador B verdadeiramente independente, a
                        convergência A×C pode ser coincidência ou efeito de
                        exposição prévia aos resultados.
conclusão proibida:
                      - NÃO afirmar que o protocolo é reproduzível a partir
                        desta rodada parcial.
                      - Apenas registrar: A e C apresentaram elevada convergência
                        neste caso (A×C).
                      - NÃO tratar H-A como confirmada; depende de B e de novos
                        SX (matriz de comparação A×B, B×C pendente).
evidência:           experiments/validation/independence/SX-001/narrative/
                      01-narrativa-original.md;
                      experiments/validation/independence/SX-001/reconstruction/
                      02-atomic-facts.md (referência — 46 AFs);
                      rodada P-0010 (Avaliador C, 56 AFs — ver contexto da
                      coordenação 2026-08-04)
status:              Observação (rodada parcial, PROVISÓRIO)
exigência:           - Obter um Avaliador B genuinamente independente (novo
                        chat, contexto cego) e calcular AFR(A,B), AFR(B,C).
                      - Completar a matriz de comparação e responder: "quais
                        diferenças surgem naturalmente entre avaliadores
                        independentes?" (ruído esperado × variação de
                        granularidade × inconsistência do protocolo × divergência
                        real de interpretação).
                      - Repetir o procedimento nos próximos SX para testar H-B.
contraexemplos:      Nenhum até agora.
```

### DL-024 — Estudo de reprodutibilidade completo (P-0010), matriz A×B×C — Gate SATISFEITO

```
DL-024
origem:              P-0010 (Reproducibility Program) — estudo completo sobre o
                      SX-001 (Challenger STS-51-L); três avaliadores independentes
                      (A, B, C), mesma Narrativa Original, mesmas fontes, protocolo
                      congelado.
domínio:             Aeroespacial / Aeronáutica (SX-001)
observação:          Matriz de comparação tríplice concluída com contabilidade
                      fechada (partição exaustiva, sem ambiguidade). Resultados:
                      - A×B: 34 match_1_1, 10 decomp_1_N, 2 group_N_1, 0 diverg,
                        0 excl_A, 16 excl_B
                      - A×C: 33 match_1_1, 11 decomp_1_N, 2 group_N_1, 0 diverg,
                        0 excl_A, ~15 excl_C
                      - B×C: 52 match_1_1, 7 decomp_1_N (lado B), 2 group_N_1
                        (lado B), 0 diverg, 0 excl_B, 2 excl_C
                      Eixo 1 (relação entre avaliadores): **zero divergências
                      factuais em todos os três pares**.
                      Eixo 2 (propriedades intra-avaliador): redundâncias
                      intra-avaliador identificadas separadamente — B: 7 pares/grupos
                      (14 AFs); C: 1 par (C-008/061 — óbito). A redundância do
                      óbito (desintegração+morte) aparece **independentemente** em
                      B e em C — padrão de extração, não coincidência.
                      Exclusivos de C limitados a 2 fatos, ambos rastreáveis à
                      narrativa (função dos O-rings; "53°F menor temperatura de
                      lançamento já realizada").
explicações concorrentes:
                      - A convergência pode reflectir granularidade estável deste
                        caso específico + documentação rica, não propriedade geral
                        do protocolo.
                      - A variabilidade de granularidade pode ser inerente à
                        linguagem (leitores legítimos granularizam diferente).
hipóteses concorrentes:
                      - H-A: a principal fonte de variabilidade entre avaliadores
                        independentes é a granularidade da decomposição, não a
                        identificação dos acontecimentos (sustentada por 3 pares).
                      - H-B: em outros domínios podem surgir divergências de
                        seleção, causalidade ou temporalidade — o padrão pode não
                        ser geral.
                      - H-C: o desenho do estudo (mesmo executor para narrativa e
                        reconstrução em algumas rodadas) pode subestimar a
                        variabilidade real.
conclusão proibida:
                      - NÃO generalizar para outros domínios. A afirmação é
                        limitada a: **neste caso (Challenger), entre estes três
                        avaliadores, a variabilidade observada concentrou-se na
                        granularidade da decomposição dos Atomic Facts, e não
                        foram observadas divergências factuais.**
                      - NÃO promover AFR a métrica oficial — permanece observação
                        do programa (DL-008).
evidência:           experiments/validation/p0010/input/evaluator-A.md (46 AFs);
                      experiments/validation/p0010/input/evaluator-B.md (75 AFs);
                      experiments/validation/p0010/input/evaluator-C.md (73 AFs);
                      experiments/validation/p0010/comparison/analysis-AxB.md;
                      experiments/validation/p0010/comparison/analysis-AxC.md;
                      auditoria contábil B×C (partição exaustiva 75+73 AFs)
status:              Confirmado (≥3 comparações independentes, mesmo caso)
exigência:           Gate P-0010 = SATISFEITO. Próximo: seleção formal do SX-002
                      via protocolo SX-SELECTION congelado (domínio
                      biomédico/saúde, não caso mais famoso). Repetir estudo de
                      reprodutibilidade no SX-002 antes de SX-003.
contraexemplos:      Nenhum até agora.
```

## Parking Lot — ideias metodológicas adiadas para pós-SX-010 (coordenação)

> **Disciplina da coordenação (FASE E):** qualquer nova ideia metodológica é
> apenas **anotada aqui** para revisão após o SX-010. Nenhuma camada nova é
> criada antes disso.
>
> **Regra simples:** se a ideia é necessária para executar o próximo experimento,
> ela entra; se não é, ela espera. Isto protege contra o risco de otimizar
> continuamente o método em vez de produzir evidência.

**Itens adiados (revisar após SX-010):**

- **Estudo prospectivo (coordenação 2026-08-04)** — todos os Shadow Experiments até
  aqui são retrospectivos (eventos já ocorridos). Após completar os dez casos,
  aplicar o ECP a um projeto EM ANDAMENTO e registrar previsões antes do desfecho.
  Se algumas previsões forem confirmadas, testa-se capacidade PREDITIVA, não apenas
  explicativa. NÃO antes do SX-010 — apenas direção natural da fase seguinte.
- A coordenação também monitora a tensão metodológica (abstração × poder operacional)
  e a pergunta "estruturas vs. linguagem de descrição" como itens não-formais; se
  surgirem ideias metodológicas concretas, serão registradas aqui primeiro.

## Entity Emergence Rate (EER) — observação provisória

> **Nota da coordenação:** EER **não é um artefato oficial** — ainda. É uma
> métrica **observada** aqui no diário, sem teoria, para ver se aparece um
> padrão depois de vários experimentos.

**Definição provisória (apenas observacional):** para cada caso SX-00X, marca-se
quais entidades do Kernel **emergiram** (✔) e quais **não** (✖). Após ~8–12
experimentos, a distribuição pode revelar entidades "fundacionais" (aparecem em
quase todos) vs. "de implementação" (contextuais).

### EER — SX-001 (Challenger, Aeroespacial, Falha)

```
Problem            ✔ (ausência observada como dado)
Goal               ✔
Knowledge          ✔
Evidence           ✔
Assumption         ✔
Decision           ✔
Observation        ✔ (via falha/validação)
Execution Intent   ✖
Provider           ✖
Risk               ✖ (não calculado — ausência)
```

> Sem teoria. Apenas observação. Depois de dez experimentos, talvez apareça um
> padrão — e então, **somente então**, discutimos se a EER merece virar métrica.

## Previsão de trabalho (coordenação 2026-08-03)

> **Hipótese de trabalho, registrada explicitamente como previsão:** entre 8 e
> 12 experimentos em domínios muito diferentes, espera-se:
> - algumas entidades aparecerão em praticamente todos os casos;
> - outras surgirão apenas em contextos específicos;
> - algumas talvez nunca apareçam de forma espontânea.

Se isso ocorrer, teremos base empírica para distinguir **ontologia fundamental**
de **mecanismo de implementação** — e a discussão sobre leis/ontologia passará
de argumentos conceituais para evidência acumulada em múltiplos domínios. Esta é
uma previsão falsificável; o P-0008 existe para testá-la.

## Regras do diário

1. **Status sempre conservador:** começa em `Observação`; `Confirmado` exige
   ≥2 domínios; `Consolidado` exige padrão (RA-SIG-005).
2. **Nenhuma lei é escrita a partir de um único registro.** A passagem de um
   registro para a frente Inferência Científica só ocorre quando os critérios
   objetivos (SIGNAL-SCHEMA, LAW-CRITERIA) forem satisfeitos.
3. **Contraexemplos nunca são ocultados** (RA-SIG-004).
4. **Hipóteses concorrentes são obrigatórias** em todo registro — sem elas, o
   registro está incompleto (RC-3, RESEARCH-CHARTER).
5. **A teoria só muda depois do registro** — uma entrada nova nunca edita a
   teoria no mesmo ciclo (RC-1, Evidence First).
6. Este arquivo **não** é um artefato metodológico: não pode gerar regra,
   gate, schema ou métrica. Apenas documenta observações (a EER aqui é
   observação, não métrica oficial).

## Relação com os programas

- **P-0006 (Law Discovery)** — o diário alimenta a descoberta, mas não decide
  promoções.
- **P-0007 (Independence)** — as observações aqui nascem de casos independentes
  do ECP (exógenas).
- **P-0008 (Cross-Domain Validation)** — é o programa que transforma as
  observações DL-001..DL-003 em afirmações cross-domain, ou as refuta; e onde a
  EER observacional se acumula até formar (ou não) um padrão.
- **P-0009 (Competitive Theory Validation)** — acrescenta o eixo comparativo:
  transforma DL-005 em evidência discriminante (o ECP explica **mais** que
  rivais?). DL-006 e DL-007 alimentam a leitura das futuras generalizações.
- **P-0010 (Reproducibility)** — gate antes da expansão: mede se o conjunto de
  Atomic Facts (e a Reconstrução) é estável entre avaliadores independentes;
  DL-008 é a observação que o motiva (AFR como observação, não métrica).
- **RESEARCH-CHARTER** — os RC-1..RC-5 regem como uma observação evolui (ou não)
  para teoria; o diário é onde isso é registrado.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Diário científico aberto (coordenação 2026-08-03). DL-001 (Evidence→Decision), DL-002 (ausências), DL-003 (emergência da cadeia). |
| 2.0 | 2026-08-03 | Regra de Ouro da Evolução Científica adicionada. Entradas reestruturadas (Origem/Domínio/Observação/Explicações concorrentes/Hipóteses concorrentes/Generalização proibida/Status). EER observacional (provisória, não-oficial). Previsão de trabalho (8–12 experimentos) registrada. |
| 2.1 | 2026-08-03 | DL-004 (mudança de categoria do projeto — programa de pesquisa). Regras vinculadas ao RESEARCH-CHARTER (RC-1 Evidence First, RC-3 Competing Explanations). |
| 2.2 | 2026-08-03 | DL-005 (evidência interna não é comparativa — risco de autorreferência), DL-006 (taxonomia provisória de leis como conceito), DL-007 (leis × restrições, hipótese observacional). Vínculo ao P-0009 (Competitive Theory Validation). |
| 2.3 | 2026-08-03 | DL-008 (reprodutibilidade do Atomic Facts é o novo gargalo). Vínculo ao P-0010 (Reproducibility Program, FASE D). AFR como observação, não métrica. |
| 2.4 | 2026-08-04 | DL-009 (divisão mental em três produtos: Theory / Runtime / Lab — o ECP virou um laboratório) e DL-010 (Discovery Log evoluirá de diário para grafo científico). Vínculo ao acordo de estabilidade FASE E (até SX-010, sem mudanças estruturais). |
| 2.5 | 2026-08-04 | DL-011 (Princípio da Conservação da Teoria — Theory Drift como principal risco; orçamento de mudanças até SX-010: 0 leis/entidades/critérios/schemas/RFCs/ADs). |
| 2.6 | 2026-08-04 | DL-012 (Era da Generalização conceitual pós-SX-010; compromisso anti-identidade — se um rival explicar melhor, entender por quê, não defender; vocabulário da equipe: observar/medir/reproduzir/comparar/falsificar). |
| 2.7 | 2026-08-04 | DL-013 (estágio do programa: de protocolo a programa de pesquisa; risco epistemológico remanescente — ECP explicando o mundo só com o ECP; P-0009 possivelmente mais importante que SX-002 isolado; sequência analítica pós-SX-010 definida). |
| 2.8 | 2026-08-04 | DL-014 (o valor científico depende do conjunto de casos, não da sofisticação do protocolo; principal ativo passa a ser o Atlas Experimental; observação do estágio atual — não é lei). |
| 2.9 | 2026-08-04 | DL-015 (auditoria estratégica — continuidade "se eu desaparecesse hoje?"; checklist de estado do programa; enquadramento como infraestrutura para pesquisa; marco decisivo do Atlas). Revisão interna, sem novos artefatos. |
| 2.10 | 2026-08-04 | DL-016 (avaliação de maturidade — nota por dimensão; gargalo mudou para produção de evidência diversa; o Atlas é o experimento, não um produto; Atlas Dashboard como recomendação anotada pós-SX-010; pergunta preditiva como objetivo futuro). |
| 2.11 | 2026-08-04 | DL-017 (desafio científico sobre o técnico; arquitetura futura em duas camadas como especulação — não agora; indicador: proporção observações sobre o ECP × sobre engenharia; tensão metodológica abstração × poder operacional como item monitorado, sem registro formal). |
| 2.12 | 2026-08-04 | DL-018 (ECP como infraestrutura para descoberta científica — testar qualquer teoria, não provar uma; objetivo = produzir testes confiáveis; teste histórico intergrupo independente; proteger os dados mais que as ideias). "Lei Zero" e marco silencioso permanecem como bússolas mentais não-documentadas. |
| 2.13 | 2026-08-04 | DL-019 (oito eras do programa; gargalo é estatístico — falta distribuição; mais protocolo não significa mais ciência; pergunta estruturas × linguagem permanece não-formal). Seção Parking Lot criada — ideias metodológicas adiadas para pós-SX-010, apenas anotadas, nunca criadas antes. |
| 2.14 | 2026-08-04 | DL-020 (ponto de inflexão: fator limitante passa a ser a produção de evidência; avaliação de estado; três linhas de trabalho — Produção/Qualidade/Registro; pergunta muda para "qual o próximo dado?"). Parking Lot atualizado: estudo prospectivo (preditivo) adiado para pós-SX-010. |
| 2.15 | 2026-08-04 | DL-021 (Atlas como Data Warehouse científico — banco de conhecimento, não documento; inversão do fluxo: Atlas passa a orientar a pesquisa apontando lacunas de evidência; ciclo fechado Experimento → Atlas → Lacunas → Próximo Experimento; Atlas como mecanismo de planejamento pós-SX-010). |
| 2.16 | 2026-08-04 | DL-022 (risco operacional — custo de execução dos SX; regra: cada experimento deve aumentar a informação do Atlas, não só o número de casos; seleção por maximização de ganho de informação; Atlas como instrumento de observação — segunda camada: o Atlas observa os Shadow Experiments). |
| 2.17 | 2026-08-04 | DL-023 (rodada parcial de reprodutibilidade P-0010, avaliação A×C — PROVISÓRIO; resultado do estudo, não do ECP: cobertura 100%, concordância 95,7%, 0 conflitos, divergência só de granularidade; hipótese de trabalho não confirmada sobre granularidade como principal fonte de variabilidade; banida conclusão de reprodutibilidade até Avaliador B independente; matriz A×B/B×C pendente). |
