# schemas/ — Gramática formal dos contratos ECP

Gramática **validável por máquina** da linguagem de contratos do ECP (ECP-001 §7 e ECP-100 §7). O ECP-200 (Capability Engine) consumirá esta gramática como interface: uma capacidade declara *quais contratos executa* e um contrato é *a forma verificável* dessa execução. O ECP-300 (Runtime) a estende com os tipos de execução simulada: eventos, reavaliação, sessão e cenários.

## Estrutura

```
schemas/
├── README.md                      ← este documento
├── grammar.ebnf                   ← gramática da DSL textual (EBNF)
├── contract.base.schema.json      ← estrutura comum a todo contrato
├── capability.schema.json         ← perfil de capacidades de uma entidade (ECP-200 §2)
├── contract_capability.schema.json← mapeamento contrato→capacidades (ECP-200 §3)
├── negotiation.schema.json        ← registro de negociação (ECP-200 §4)
├── runtime_event.schema.json      ← evento que entra na fila de reavaliação (ECP-300 §2.1)
├── runtime_reaval.schema.json     ← reavaliação (ECP-300 §3 e §7.4)
├── runtime_session.schema.json    ← sessão e memória persistente (ECP-300 §5)
├── runtime_scenario.schema.json   ← roteiro de execução simulada (ECP-300 §3–§4)
├── governance.schema.json         ← registro de autoridade (ECP-400 §2)
├── change_proposal.schema.json    ← proposta de mudança governada (ECP-400 §3)
├── change_review.schema.json      ← revisão de proposta de mudança (ECP-400 §3)
├── change_approval.schema.json    ← aprovação de proposta de mudança (ECP-400 §3)
├── contracts/                     ← refino por tipo de contrato
│   ├── discovery.schema.json      ← Discovery: problem + goal (ECP-100 §7.1)
│   ├── research.schema.json       ← Research: conhecimento/evidência (ECP-100 §7.2)
│   ├── planning.schema.json       ← Planning: decisões + autoridade (ECP-100 §7.3)
│   ├── execution.schema.json      ← Execution: artefatos rastreáveis (ECP-100 §7.4)
│   └── validation.schema.json     ← Validation: veredito (ECP-100 §7.4)
├── examples/                      ← contratos sintéticos dos CASES (Rodada 3)
│   ├── erp/                       ← CASO 1 (5 contratos + negotiation)
│   ├── game/                      ← CASO 3 (5 contratos + negotiation)
│   ├── hospital/                  ← CASO 12 (5 contratos + negotiation)
│   ├── capabilities/
│   │   ├── entities/              ← perfis: humano_engenheiro, llm_assistente, sistema_legado
│   │   └── contracts/             ← mapeamento dos 5 contratos → capacidades
│   └── runtime/                   ← execução simulada (ECP-300)
│       ├── events/                ← eventos externos/invalidação/falha (ev-erp-reg, …)
│       ├── reavals/               ← reavaliações (re-erp-reg, …)
│       ├── sessions/              ← sessões e memória (ss-erp, …)
│       └── scenarios/             ← cenários dos CASES (sc-erp-01, sc-game-01, sc-hosp-01)
└── negative/runtime/              ← falsificações (não lidas pelo linter padrão)
    ├── events/                    ← evento com campo 'transition' (viola RNF-3)
    └── scenarios/                 ← cenários que violam os invariantes do motor
```

## O que a gramática garante

1. **Estrutura canônica** — `contract`, `state`, `exit`, `failure` (obrigatório, `P-7`) e `evidence` (mín. 1) em todo contrato.
2. **Tipos por estado** — cada `contracts/<tipo>.schema.json` exige os `inputs`/`outputs`/`required` do estado (ex.: `discovery` exige `problem` e `goal`; `planning` exige `every_decision_has_authority`).
3. **RNFs da Fase V0** — `exit` probabilístico exige `method` + `threshold` pré-registrados (RNF-1 / ECP-100.3); `authority` exige `actor` e, em co-autoria, `consensus` (RNF-2 / ECP-100.1).
4. **Rastreabilidade semântica** — cada item de `evidence` precisa existir em `outputs` (linter).
5. **Capability Engine (ECP-200)** — perfil declara conjunto atômico + `can_sign` consistente (capacidade não se presume, ECP-200.1); entidade sem `write` é não conforme (ECP-200.3); negociação escolhida sem fallback quando não há candidato pleno é erro (ECP-200.2).
6. **Runtime (ECP-300)** — evento de mundo real **não possui** campo `transition` (RNF-3); reavaliação `reavaliado` exige Decision Record e `sem_reacao` exige justificativa (ECP-300.4 / ECP-100.2); sessão referencia decisão de entrada e autoridade; cenário com transição enquanto há evento não reavaliado é erro.

## Como validar

```bash
# valida todos os exemplos em schemas/examples/ (contratos + capacidades + negociações + runtime)
python scripts/validate_contracts.py

# valida arquivos ou diretórios específicos
python scripts/validate_contracts.py schemas/examples/erp schemas/examples/capabilities

# qualquer violação → saída de erro e exit code 1
```

O linter usa JSON Schema (draft 2020-12) via `jsonschema` + `referencing`, e adiciona checagens semânticas que o schema não captura. O tipo de documento é identificado por `contract` (contrato) ou `kind` (entity_capability | contract_capability | negotiation | runtime_event | runtime_reaval | runtime_session | runtime_scenario).

## Como simular o runtime

```bash
# executa os cenários sobre o grafo e verifica os invariantes do motor (ECP-300)
python scripts/simulate_runtime.py

# saída: 12 documentos positivos conformes; 5 falsificações detectadas.
# exit code 0 somente se os positivos não violarem e os negativos violarem.
```

O simulador verifica passo a passo: evento externo não transiciona (RNF-3); reavaliação é decisão registrada ou não-reação justificada (ECP-300.4); falha sem `FAILURE` declarado bloqueia em vez de resolver (ECP-300.2); invalidação sem dependentes é sinal de grafo mal ligado; transição exige autoridade e Decision Record (ECP-100.1 / L-0).

## Formas canônicas

- **Canônica para máquina:** documentos JSON validados por `contracts/<tipo>.schema.json` (é o que o linter e o runtime consomem).
- **Canônica textual:** DSL do ECP-001 §7, descrita em `grammar.ebnf` (usada na escrita de contratos em texto).

As duas formas são equivalentes e rastreáveis uma à outra; a conversão é definida quando a gramática atingir `Versão Candidata`.
