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

## CAMADA 2 — Engenharia

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

### 05 — Quality (ECP-500..599)

- [ ] Métricas de qualidade da engenharia executada sob ECP
- [ ] Padrões de evidência e auditoria de conformidade (lê Decision/Evidence/Goal Records)

### 06 — Learning (ECP-600..699)

- [ ] Calibração contínua de confiança (curvas por entidade)
- [ ] Retroalimentação de resultados observados para decisões futuras
- [ ] Reutilização de conhecimento entre projetos

### 07 — Certification (ECP-700..799)

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
