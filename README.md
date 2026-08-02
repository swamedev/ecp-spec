# ECP — Engineering Cognition Protocol

> O ECP define como **qualquer entidade capaz de desenvolver um projeto** — humana ou artificial — deve conduzir o trabalho de engenharia: da identificação do problema à produção de artefatos, com validação e aprendizado.

O ECP **não é** um prompt, um framework ou um template. É uma **especificação**: um padrão de engenharia reutilizável, à maneira de HTTP, TCP/IP, POSIX e OpenAPI.

---

## 1. O problema que motivou o ECP

Os agentes de IA atuais operam no modelo:

```
Prompt
  ↓
Resposta
```

O ECP inverte esse modelo. O fluxo canônico passa a ser:

```
Problema → Objetivo → Perguntas → Conhecimento → Modelo Mental → Hipóteses
    → Decisões → Plano → Execução → Validação → Aprendizado
```

**O primeiro artefato produzido nunca é código. É o problema — e depois o entendimento.**

Código é apenas um artefato. Engenharia é um processo de **tomada de decisão sob restrições**. Essa distinção é a base de toda a especificação (ver [ECP-000](00-foundation/ECP-000.md)).

## 2. A quem se destina

O ECP é escrito para **qualquer entidade capaz de desenvolver um projeto**:

- um humano
- um assistente de IA (ChatGPT, Claude, Gemini, Cursor, Copilot, etc.)
- um agente autônomo (OpenCode, OpenHands, Devin, etc.)
- um agente local
- um sistema futuro ainda não inventado

Por isso o ECP **não é escrito para IA** — ele é escrito para o **processo de engenharia**, que é neutro em relação ao implementador.

## 3. Tipos de documento

O ECP possui exatamente **quatro tipos** de documento:

| Tipo | Código | Função | Estabilidade |
|---|---|---|---|
| Princípio | `PRIN` | Definem fundamentos que nunca mudam | Permanente |
| Protocolo | `PROT` | Definem comportamento e processos | Evolutiva |
| Contrato | `CONT` | Definem entradas e saídas verificáveis | Evolutiva |
| Referência | `REF` | Exemplos, glossários e materiais de apoio | Livre |

Nada além disso entra na especificação.

## 4. Contratos em vez de prompts

A inovação central do ECP: regras de comportamento não são escritas como instruções textuais, e sim como **contratos** — blocos estruturados com estados, entradas, saídas e condições de saída verificáveis.

Em vez de *"antes de responder, pense…"*, o ECP escreve:

```
STATE: Discovery
INPUTS:
    problem
    goal
OUTPUTS:
    problem_model
REQUIRED:
    goal_understood
EXIT:
    confidence >= 0.90
FAILURE:
    go_to Research
```

A sintaxe canônica é definida em [ECP-001](00-foundation/ECP-001.md).

### 4.1 As Leis do ECP

> **`L-0` — Nenhum estado do protocolo pode ser alcançado apenas porque o fluxo o determina. Todo estado deve ser alcançado porque uma decisão verificável autorizou a transição.**

O fluxo é consequência; a decisão é a causa. Entre `Discovery` e `Planning` existe sempre o julgamento *há evidência suficiente?* — e ele é registrado, não assumido. Ver [ECP-000 §5](00-foundation/ECP-000.md).

> **`L-1` — Toda entidade do ECP deve ser rastreável, em última instância, a um Problem Record aprovado. Nenhuma meta, afirmação, decisão ou artefato pode existir desconectado de um problema que a justifique.**

O objetivo resolve um problema; a decisão contribui para o objetivo; o artefato rastreia a decisão e o problema. Ver [ECP-000 §5.1](00-foundation/ECP-000.md).

### 4.2 Grafo, não fila

O ECP modela um projeto como um **grafo de conhecimento** — problemas, objetivos, claims, suposições, evidências, decisões, riscos, estados, capacidades e artefatos conectados por dependências. O runtime nunca pergunta *"qual o próximo estado?"*, e sim *"qual entidade do grafo precisa evoluir?"*. Ver [ECP-001 §3](00-foundation/ECP-001.md).

### 4.3 Cadeia de rastreabilidade

Cada artefato obrigatório depende do anterior — `Problem Record → Goal Record → Claim → Knowledge → Assumption → Evidence → Decision`. Se uma suposição é invalidada, as decisões que dela dependem ficam suspeitas e são reavaliadas. Ver [ECP-007](00-foundation/ECP-007.md).

## 5. Critério de admissão de regras

Toda regra que entrar no ECP deve responder **cinco perguntas obrigatórias**:

1. Qual problema esta regra resolve?
2. Quando ela deve ser aplicada?
3. Quando ela **não** deve ser aplicada?
4. Como verificar automaticamente que foi seguida?
5. Quais evidências demonstram conformidade?

Se uma regra não responder a essas perguntas, ela **não entra** no ECP. Esse filtro é definido em [ECP-002](00-foundation/ECP-002.md).

## 6. Estrutura da especificação

```
ecp-spec/
├── README.md               ← este documento
├── LICENSE                 ← CC BY 4.0
├── CHANGELOG.md            ← histórico de revisões
├── ROADMAP.md              ← fases de evolução
│
│   CAMADA 1 — COGNIÇÃO
├── 00-foundation/          ← ECP-000..099
│
│   FASE V0 — VALIDAÇÃO
├── 01-validation/          ← PROOF, CASES, GLOSSARY, INVARIANTS
│
│   CAMADA 2 — ENGENHARIA
├── 02-core/                ← ECP-100..299 (State Machine + Capabilities)
├── 03-runtime/             ← ECP-300..399
├── 04-governance/          ← ECP-400..499
├── 05-quality/             ← ECP-500..599
├── 06-learning/            ← ECP-600..699
├── 07-certification/       ← ECP-700..799
│
│   APOIO
├── 08-reference/           ← ECP-800..899
├── schemas/                ← gramáticas formais (YAML/JSON/AST)
├── examples/               ← exemplos executáveis
└── assets/                 ← diagramas e mídia
```

## 7. Metodologia de elaboração

Nenhum documento entra na especificação sem passar pelo ciclo:

```
Pesquisa → Primeira versão → Crítica → Revisão
    → Versão candidata → Validação → Aprovado
```

Cada documento declara seu `Status` no front matter. Nada em `Rascunho` é norma; apenas documentos `Aprovado` têm força normativa.

## 8. Estado atual

**Camada 1 — Cognição (em rascunho).** **Fase V0 — Validação (concluída):** a fundação foi congelada, falsificada (PROOF), exercitada (CASES) e corrigida; a barreira de avanço da Camada 2 foi transposta. **Camada 2 — Engenharia (iniciada):** `ECP-100` rascunha a máquina de estados formal que implementa o `ECP-010`. Ver [ROADMAP.md](ROADMAP.md) e [CHANGELOG.md](CHANGELOG.md).

| Documento | Título | Tipo | Status |
|---|---|---|---|
| [ECP-000](00-foundation/ECP-000.md) | O que é Engenharia (princípios, Leis L-0/L-1, grafo) | Princípio | Rascunho |
| [ECP-001](00-foundation/ECP-001.md) | Arquitetura da Especificação | Protocolo | Rascunho |
| [ECP-002](00-foundation/ECP-002.md) | Critérios de Admissão de Regras | Protocolo | Rascunho |
| [ECP-003](00-foundation/ECP-003.md) | Modelo de Problema | Protocolo | Rascunho |
| [ECP-004](00-foundation/ECP-004.md) | Modelo de Objetivo e Intenção | Protocolo | Rascunho |
| [ECP-005](00-foundation/ECP-005.md) | Modelo de Claims | Protocolo | Rascunho |
| [ECP-006](00-foundation/ECP-006.md) | Modelo de Conhecimento e Contexto | Protocolo | Rascunho |
| [ECP-007](00-foundation/ECP-007.md) | Modelo de Suposições | Protocolo | Rascunho |
| [ECP-008](00-foundation/ECP-008.md) | Modelo de Evidência, Confiança e Risco | Protocolo | Rascunho |
| [ECP-009](00-foundation/ECP-009.md) | Modelo Universal de Decisão | Protocolo | Rascunho |
| [ECP-010](00-foundation/ECP-010.md) | Ciclo de Vida Cognitivo | Protocolo | Rascunho |

**Camada 2 — Engenharia** (iniciada com a Fase V0 concluída):

| Documento | Título | Tipo | Status |
|---|---|---|---|
| [ECP-100](02-core/ECP-100.md) | Máquina de Estados Formal (contratos discovery/research/planning/execution/validation) | Protocolo | Rascunho |

**Fase V0 — Validação** (documentos de trabalho, sem força normativa):

| Documento | Função | Status |
|---|---|---|
| [ECP-PROOF](01-validation/ECP-PROOF.md) | Tentativa de falsificação de L-0, L-1, P-1..P-12 (rodada 2: 11/11 pendências resolvidas, 0 derrubadas) | Rascunho |
| [ECP-CASES](01-validation/ECP-CASES.md) | 20 projetos-testes de domínios diversos (rodada 2: 19 PASSA, 1 PARCIAL, 0 NÃO PASSA) | Rascunho |
| [ECP-GLOSSARY](01-validation/ECP-GLOSSARY.md) | Semântica formal congelada das entidades (16 termos) | Rascunho |
| [ECP-INVARIANTS](01-validation/ECP-INVARIANTS.md) | Leis imutáveis do protocolo | Rascunho |

## 9. Licença

Distribuído sob [CC BY 4.0](LICENSE).
