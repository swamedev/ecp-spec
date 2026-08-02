# CHANGELOG

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) com versionamento [SemVer](https://semver.org/lang/pt-BR/).

## [0.13.0] — 2026-08-02

### Adicionado

- **`04-governance/AD-001.md` — Decisão de Arquitetura Nº 001** (Aprovado): **feature freeze** do ECP-SPEC e início do programa **Fase B — Runtime**. Nenhum módulo grande novo (Quality/Learning/Certification) é iniciado enquanto a Fase B não produzir evidência. Define o **ECP Reference Runtime (ERR)** como implementação canônica (CPython para Python), **agnóstico de implementador** (Execution Unit / Execution Provider em vez de Capability), o **ECP Kernel** com cinco responsabilidades (`Problem`, `Goal`, `Decision`, `Contract`, `Graph`) e a missão da primeira versão: executar com integridade, rastreabilidade e reprodutibilidade a cadeia `Problem → Goal → Knowledge → Assumption → Evidence → Decision`.

### Alterado

- `ROADMAP.md`: seção **Fase B — Runtime** adicionada; Camada 2 marcada como congelada; Quality/Learning/Certification marcados como adiados pelo AD-001.
- `README.md`: estado atual atualizado — Camada 2 congelada, Fase B em andamento, lema do programa.

## [0.12.0] — 2026-08-02

### Adicionado

- **`04-governance/ECP-500.md` — Quality (Rascunho)**: esboço das métricas de qualidade da engenharia sob ECP — completude de evidência (E-1/E-2), rastreabilidade de decisão (D-1/D-2), tempestividade (T-1/T-2), robustez a suposições (R-1/R-2); padrões de evidência; regras ECP-500.1..500.3; interface com Runtime e Governance; índice de qualidade. *Nota: módulo adiado pelo AD-001 (feature freeze), documento mantido como esboço.*

## [0.11.0] — 2026-08-02

### Adicionado

- **`04-governance/ECP-400.md` — Governance (Rascunho)**: modelo de autoridade (actor/scope/role/source/constraint), herança e delegação, decisão coletiva com consenso pré-registrado; processo de mudança (proposta → revisão → aprovação → deprecação) que declara e preserva invariantes; regras ECP-400.1..400.4; gramática em `schemas/` (`governance`, `change_proposal`, `change_review`, `change_approval`).
- **Gramática do Governance** em `schemas/`: `governance.schema.json`, `change_proposal.schema.json`, `change_review.schema.json`, `change_approval.schema.json`.
- **Exemplos do ciclo de mudança**: proposta válida (ECP-003-CHG-001, autoridade coletiva + preservação de INV-1), revisão, aprovação e falsificação (proposta que quebra invariante sem preservação).

### Alterado

- `scripts/validate_contracts.py`: suporte aos kinds `governance`/`change_proposal`/`change_review`/`change_approval`; checagens semânticas ECP-400.1..400.4 (authority.source papel/delegação, invariantes com `preserved_by`, delegação com ref/escopo/prazo).
- `schemas/README.md`: documenta os schemas de governance e o linter.

## [0.10.0] — 2026-08-02

### Adicionado

- **`03-runtime/ECP-300.md` — Motor de Execução sobre o Grafo (Runtime)** (Rascunho): tupla do motor `R=(G,Q,M,P)` — grafo (fonte da verdade), fila de reavaliação, máquina de estados e memória persistente; contratos assinados viram nós conectados a goals/suposições/evidência; **propagação de invalidação** (marcar suspeitos → priorizar → enfileirar → acordar, sem transicionar — RNF-3); tratamento de falhas (`FAILURE` → `go_to`/`retry`/`escalate`, falha sem tratamento **bloqueia**); sessão e memória persistente entre contratos; interface com a máquina de estados (ECP-100); regras ECP-300.1..300.4; NFRs RNF-1..RNF-3 no cabeçalho.
- **Tipos de runtime na gramática** em `schemas/`:
  - `runtime_event.schema.json` — evento que entra na fila de reavaliação; **não possui** campo `transition` de propósito (RNF-3).
  - `runtime_reaval.schema.json` — reavaliação: `reavaliado` exige Decision Record; `sem_reacao` exige justificativa (ECP-100.2).
  - `runtime_session.schema.json` — contexto de sessão e memória persistente (estado observável, autoridade, contratos ativos).
  - `runtime_scenario.schema.json` — roteiro de execução simulada (event, invalidate, reaval, transition, failure).
- **Simulador `scripts/simulate_runtime.py`**: verifica os invariantes do motor passo a passo (evento não transiciona; reavaliação é decisão; falha sem tratamento bloqueia; invalidação sem dependentes é erro; transição exige autoridade e Decision Record).
- **Exemplos sintéticos**: 3 eventos, 3 reavaliações, 3 sessões e 3 cenários (ERP: evento regulatório + invalidação A-1 reabre Planning; Game: evento de mercado com não-reação justificada por limiar; Hospital: violação de SLA escalada com supervisão).

### Alterado

- `scripts/validate_contracts.py`: suporte aos tipos `runtime_event`/`runtime_reaval`/`runtime_session`/`runtime_scenario` (dispatcher por `kind`); checagens semânticas ECP-300 (evento não reavaliado antes de transição; invalidação sem dependentes; falha sem `FAILURE` resolvida).
- `schemas/README.md`: documenta os schemas de runtime e o simulador.
- `ECP-GLOSSARY`: novos termos SESSÃO e REAVALIAÇÃO (origem ECP-300).
- `ROADMAP`: seção 03 — Runtime marcada com ECP-300 e tipos de runtime concluídos.

### Validação

- Linter: **38/38 documentos conformes** (15 contratos + 3 perfis + 5 mapeamentos + 3 negociações + 12 documentos de runtime).
- Simulador: **12 documentos positivos conformes; 5 falsificações detectadas** — evento que transiciona (schema: campo `transition` + cenário: transição sem reavaliação), decisões suspeitas sem reavaliação (ECP-300.4), falha sem `FAILURE` resolvida (ECP-300.2), invalidação sem dependentes (ECP-300 §3).

## [0.9.0] — 2026-08-02

### Adicionado

- **`02-core/ECP-200.md` — Capability Engine** (Rascunho): capacidades atômicas (`read`, `write`, `execute`, `verify`, `research`, `remember`); mapeamento capacidade → contrato; protocolo de negociação (descoberta → declaração → matching → fallback → assinatura), cada ato uma decisão registrada (Lei L-0); regras ECP-200.1..200.4; perfis heterogêneos (humano, LLM, sistema legado).
- **Gramática do Capability Engine** em `schemas/`:
  - `capability.schema.json` — perfil de capacidades de uma entidade.
  - `contract_capability.schema.json` — mapeamento contrato → capacidades mínimas.
  - `negotiation.schema.json` — registro de negociação (candidates, chosen, fallback, decision).
- **Exemplos sintéticos**: perfis `humano_engenheiro` / `llm_assistente` / `sistema_legado`, mapeamentos dos 5 contratos e 3 negociações por CASE (ERP → sistema legado executa; Game → LLM valida; Hospital → legado parcial com supervisão, exercitando fallback + autoridade).

### Alterado

- `scripts/validate_contracts.py`: suporte aos tipos `entity_capability`/`contract_capability`/`negotiation` (dispatcher por `kind`); checagens semânticas ECP-200 (write mínimo, can_sign × atômicas, negociação sem fallback).
- `schemas/README.md`: documenta os novos schemas e o linter de capacidades.
- `ECP-GLOSSARY` CAPABILITY: origem estendida para ECP-200; declaração verificável pela gramática.

### Validação

- Linter: **26/26 documentos conformes** (15 contratos + 3 perfis + 5 mapeamentos + 3 negociações).
- Falsificação: perfil sem `write` + `can_sign` inconsistente (2 erros ECP-200.1/200.3) e negociação escolhendo candidato parcial sem fallback (ECP-200.2) são detectados.

## [0.8.0] — 2026-08-02

### Adicionado

- **Gramática formal dos contratos** (`schemas/`, ciclo construção → falsificação → consolidação):
  - `schemas/contract.base.schema.json` — estrutura comum (contract, state, exit, failure obrigatório — P-7 —, evidence mín. 1, authority opcional).
  - `schemas/contracts/*.schema.json` — refino por tipo: `discovery`, `research`, `planning`, `execution`, `validation` (inputs/outputs/required de cada estado do ECP-100 §7).
  - `schemas/grammar.ebnf` — gramática da DSL textual (ECP-001 §7).
  - `schemas/examples/` — 15 contratos sintéticos dos CASES ERP (1), Game (3) e Hospital (12); `game/research` exercita EXIT probabilístico (RNF-1), `hospital/planning` exercita autoridade coletiva (RNF-2).
  - `scripts/validate_contracts.py` — linter mínimo (JSON Schema draft 2020-12 + checagens semânticas: evidence ∈ outputs, EXIT probabilístico completo, authority válida).

### Alterado

- `schemas/README.md`: documenta estrutura, garantias e uso do linter.
- `ECP-001` §7.4: gramática formal passa a existir em `schemas/` (antes "será definida").
- `ECP-100` §7: referência à forma validável por máquina em `schemas/`.
- `ROADMAP`: item "Gramática formal de contratos" concluído.

### Validação

- Linter: **15/15 contratos conformes**; teste de falsificação com contrato inválido detecta 9 violações (nome de arquivo, inputs ausentes, evidence órfã, EXIT probabilístico incompleto, authority sem actor/consenso).

## [0.7.0] — 2026-08-02

### Adicionado

- **Camada 2 iniciada** — retomada por `ECP-010` + `ECP-100`, conforme estratégia acordada:
  - `00-foundation/ECP-010.md` — **Ciclo de Vida Cognitivo**: máquina de estados conceitual (Discovery, Research, Planning, Execution, Validation, Learning), ainda abstrata e sem gramática de contratos; transições autorizadas por decisão (Lei L-0); regra `ECP-010.1` (decisão sob incerteza); tabela de transições com critérios mínimos. *Status: Rascunho.*
  - `02-core/ECP-100.md` — **Máquina de Estados Formal**: implementação do ECP-010 com a sintaxe de contratos do ECP-001 §7; tupla `M = (S, s0, T, autoridade)`; campo `autoridade`/ator + co-autoria (RNF-2); gatilhos externos reavaliam e nunca transicionam (RNF-3); EXIT probabilístico pré-registrado (RNF-1); contratos `discovery`, `research`, `planning`, `execution`/`validation`; regras ECP-100.1/100.2/100.3. *Status: Rascunho.*
- **NFRs da Fase V0 registradas como requisitos não-funcionais** no cabeçalho de ECP-010 e ECP-100 (não ficam mais como lembretes soltos):
  - `RNF-1` — inferência estatística como evidência (CASO 10)
  - `RNF-2` — autoridade e decisões coletivas (CASOS 12, 14, 18)
  - `RNF-3` — interface com contrato comercial/gatilhos externos (CASO 20)

### Alterado

- `README.md`: índice com ECP-010 (Rascunho) e Camada 2 iniciada com ECP-100.
- `ROADMAP.md`: ECP-010 concluído; 02-core refletindo ECP-100 rascunhado e ECP-101..104 como refinamentos.
- `ECP-001` §10: referência cruzada a ECP-010 e ECP-100.
- `ECP-CASES` Rodada 3: validação do par ECP-010 + ECP-100 contra CASOS 1 (ERP), 3 (Game) e 12 (Hospital); 3/3 PASSA, zero regressões.

## [0.6.0] — 2026-08-02

### Adicionado

- **Fase V0 concluída** — rodada de correção das pendências (método por item: localizar princípio/modelo → emenda → teste contra o contraexemplo → impacto nos casos → GLOSSARY → invariantes):
  - **Regra `ECP-003.3`** (migração de problema raiz): deprecação do Problem Record + reencadeamento da cadeia por Decision Record (fecha pendência L-1).
  - **Regra `ECP-009.3`** (agregação de decisões de baixo impacto): lote reconstruível (diário de obra) para decisões triviais; médio/alto impacto permanecem individuais (fecha pendência P-4).
  - **Notas de escopo** em `ECP-000` §5 (decisão × processamento; registro a posteriori — L-0), §5.1 (exploração não é projeto — L-1) e §6.1 (P-1 protótipo como evidência, P-2 serendipidade, P-7 cultura de erro, P-9 conformidade × veracidade, P-12 problemas não funcionais); `P-3` reescrito.
  - **Notas em `ECP-008`** §2.2 (autoridade × fonte verificável — P-5; conformidade estrutural × veracidade — P-9).
  - **Notas em `ECP-INVARIANTS`** INV-2 (registro a posteriori) e INV-3 (autoridade × fonte).
  - **Termos `PROCESSAMENTO` e `EXPLORAÇÃO`** no `ECP-GLOSSARY` (16 termos).
- **ECP-PROOF Rodada 2**: re-teste das 11 pendências contra as emendas; **11/11 resolvidas, 0 alvos derrubados**; contagem corrigida (9 → 11).
- **ECP-CASES Rodada 2**: fechamento das 7 descobertas (4 resolvidas, 3 abertas para a Camada 2); Livro e Filme `PARCIAL → PASSA`; **19 PASSA, 1 PARCIAL, 0 NÃO PASSA**; zero regressões.

### Alterado

- Placar corrigido no `ECP-CASES` Rodada 1 (17 PASSA, não 18).
- Versionamento: ECP-000 → 0.5.0; ECP-003, ECP-008 → 0.4.0; ECP-009 → 0.4.0; instrumentos de validação → 0.2.0.

## [0.5.0] — 2026-08-02

### Adicionado

- **Fase V0 — Validation** (`01-validation/`, por decisão do Arquiteto-Chefe: congelar a fundação para falsificação antes de novas RFCs):
  - `ECP-PROOF.md` — tentativa de falsificação de L-0, L-1 e P-1..P-12; rodada 1 com 14 alvos, 11 pendências, **0 derrubadas**.
  - `ECP-CASES.md` — laboratório de aplicação: 20 projetos (ERP, PDV, game, SaaS, API, app, agente de IA, curso, embarcado, pesquisa, livro, hospital, obra civil, militar, startup, filme, faturamento hospitalar, open source, produto físico, consultoria); **17 PASSA, 3 PARCIAL, 0 NÃO PASSA**; 7 descobertas alimentando a fundação.
  - `ECP-GLOSSARY.md` — semântica formal congelada (14 termos; regra anti-sinônimo; tabela de consistência).
  - `ECP-INVARIANTS.md` — 7 invariantes imutáveis (`INV-1`..`INV-7`) com forma lógica, origem e verificação.
- **Regra de avanço da Camada 2** no ROADMAP: nenhuma RFC da Camada 2 chega a `Versão Candidata` sem a Fase V0 concluída (PROOF + casos representativos + invariantes).

### Alterado

- **Estrutura de diretórios**: `01-state-machine/` e `02-capabilities/` fundidos em `02-core/`; criada `01-validation/`. Novas fases: `00-foundation → 01-validation → 02-core → 03-runtime → … → 08-reference`.
- `ECP-001`: Fase V0 documentada (§2.1); faixas ECP-100..299 apontando para `02-core/`; árvore de diretórios (§8) atualizada.
- `README.md`: árvore e estado atual com a Fase V0 e o índice dos documentos de validação.

## [0.4.0] — 2026-08-02

### Adicionado

- `00-foundation/ECP-003.md` — **Modelo de Problema (Problem)**: nova raiz da cadeia; *Problem Record* (id, description, root_cause, business_impact, owner, evidence, severity, constraints, status, resolved_by); regras ECP-003.1 (todo projeto inicia com Problem Record aprovado) e ECP-003.2 (soluções imaginadas não substituem problemas). *Status: Rascunho.*
- `00-foundation/ECP-005.md` — **Modelo de Claims (Claim)**: afirmações críticas registradas e sustentadas por evidência; *Claim Record* (proposition, goal, scope, strength_required, evidence, assumptions, confidence, status); regras ECP-005.1 e ECP-005.2. *Status: Rascunho.*
- **Lei `L-1`** (ECP-000 §5.1) e princípio `P-12`: rastreabilidade total até o Problem Record — Goal resolve Problem, Claim sustenta Goal, Evidence sustenta Claim/Assumption, Decision contribui para Goal, Artifact rastreia Decision e Problem.

### Alterado

- **Cadeia congelada**: `Problem → Goal → Claims → Knowledge → Assumption → Evidence → Decision → State → Artifacts → Validation → Learning`.
- **Fundação renumerada** (v0.4.0): `003` Problem, `004` Goal, `005` Claim, `006` Knowledge, `007` Assumption, `008` Evidence, `009` Decision, `010` Lifecycle (planejado). O antigo `ECP-003` (Goal) virou `ECP-004`; o antigo `ECP-004` (Knowledge) virou `ECP-006`; o antigo `ECP-005` (Assumption) virou `ECP-007`; o antigo `ECP-006` (Evidence) virou `ECP-008`; o antigo `ECP-007` (Decision) virou `ECP-009`.
- `ECP-004` (ex-003): Goal Record com campo `problem`; regra ECP-004.1 (todo Goal referencia Problem); sucesso alinhado ao problema.
- `ECP-006` (ex-004): Knowledge referenciando Goals e Problems; regra ECP-006.1.
- `ECP-007` (ex-005): Assumption vinculada a Goals; regras ECP-007.1/ECP-007.2.
- `ECP-008` (ex-006): Evidence no escopo de Claims (ECP-005) e Problems (ECP-003); regras ECP-008.1/ECP-008.2; ciclo de calibração mantido.
- `ECP-009` (ex-007): Decision Record com `problem`, `claims_sustentados` e rastreio à Lei `L-1`; regras ECP-009.1/ECP-009.2.
- `ECP-000`: definição formal com `P` (problema); Leis L-0/L-1; princípio `P-12`; grafo congelado; glossário com Problema e Claim.
- `ECP-001`: entidades Problem/Claim no grafo; arestas da Lei `L-1`; contrato de exemplo com `problem`.
- `ROADMAP.md` e `README.md`: índice, cadeia e estado atual atualizados.

## [0.3.0] — 2026-08-02

### Adicionado

- `00-foundation/ECP-003.md` — **Modelo de Objetivo e Intenção (Goal & Intent)**: estrutura Goal → Outcome → Requirements → Constraints → Success Criteria → Metrics → Acceptance; o artefato *Goal Record*; hierarquia de objetivos. *Status: Rascunho.*
- `00-foundation/ECP-005.md` — **Modelo de Suposições (Assumption)**: a quarta entidade da cadeia; *Assumption Record*; ciclo de vida; invalidação reavalia decisões dependentes. *Status: Rascunho.*

### Alterado

- **Estrutura em duas camadas**: Camada 1 — Cognição (ECP-000..099); Camada 2 — Engenharia (ECP-100..799); apoio (ECP-800..899). Diretórios renomeados (`01-state-machine`, `02-capabilities`, `03-runtime`, `06-learning`, `07-certification`, `08-reference`).
- **Grafo de conhecimento** como modelo estrutural do ECP (ECP-001 §3, ECP-000 §4.4): entidades conectadas por dependências; o runtime pergunta *"qual entidade precisa evoluir?"*.
- **Fundação renumerada** na sequência natural do projeto: `003` Goal & Intent, `004` Knowledge, `005` Assumption, `006` Evidence, `007` Decision, `008` Lifecycle. O antigo `ECP-003` (Decisão) virou `ECP-007`; o antigo `ECP-005` (Evidência) virou `ECP-006`.
- `ECP-000`: princípio `P-11` (decisão dirigida por objetivo); grafo de conhecimento; glossary com Goal e Suposição.
- `ECP-007` (ex-003): Decision Record com campos `goal` e `suposições_utilizadas`.
- `ECP-004`: regra de suposição movida para ECP-005; vinculação com objetivos.
- `ECP-006` (ex-005): ciclo de calibração **mantido** neste modelo, conforme decisão do arquiteto.
- `ROADMAP.md`: apresentado como sistema operacional em duas camadas, com 100 State Machine → 700 Certification.
- `README.md`: estrutura, índice e cadeia de rastreabilidade atualizados.

## [0.2.0] — 2026-08-02

### Adicionado

- `00-foundation/ECP-003.md` — **Modelo Universal de Decisão**: a decisão como causa do fluxo, procedimento universal de decisão (7 etapas), tipos de decisão (avançar/coletar/retroceder/escalar/parar) e o artefato *Decision Record*. *Status: Rascunho.*
- `00-foundation/ECP-004.md` — **Modelo de Conhecimento e Contexto**: as quatro perguntas do conhecimento, categorias de conhecimento, mapa de lacunas, priorização impacto × custo e registro de suposições. *Status: Rascunho.*
- `00-foundation/ECP-005.md` — **Modelo de Evidência, Confiança e Risco**: atributos e hierarquia de evidência, confiança calculada e calibrada, avaliação de risco e *Evidence Record*. *Status: Rascunho.*

### Alterado

- `ECP-000`: adicionada a **Lei Zero (`L-0`)** — nenhuma transição ocorre por sequência, apenas por decisão verificável — e a fundamentação decisão-primeiro (Seções 4.3 e 5).
- `ECP-001`: arquitetura reorientada por decisão; semântica de contratos passou a exigir decisão autorizada; relação completa com ECP-003..006.
- `ROADMAP.md`: nova sequência da fundação (`000 → 006`, decisão antes de fluxo); `ECP-100` redefinido como Máquina de Estados Formal (implementação do `ECP-006`).
- `README.md`: índice atualizado e destaque da Lei Zero.

## [0.1.0] — 2026-08-02

### Adicionado

- Estrutura oficial de diretórios da especificação (`00-foundation` … `assets`).
- `00-foundation/ECP-000.md` — **O que é Engenharia**: definição fundamental, modelo cognitivo invertido (objetivo → entendimento → artefato) e os dez princípios fundacionais. *Status: Rascunho.*
- `00-foundation/ECP-001.md` — **Arquitetura da Especificação**: sistema de numeração, quatro tipos de documento, anatomia obrigatória, ciclo de vida e sintaxe canônica de contratos. *Status: Rascunho.*
- `00-foundation/ECP-002.md` — **Critérios de Admissão de Regras**: as cinco perguntas obrigatórias e o template canônico de regra. *Status: Rascunho.*
- `README.md`, `LICENSE` (CC BY 4.0), `ROADMAP.md`.
