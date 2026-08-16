# Independent Reconstruction Protocol v1.1 (IRP-v1.1)

**Especificação completa — desenho corretivo pós-auditoria FAIL**

| Campo | Valor |
|---|---|
| **Comando** | GO-7 — AUTORIZAR REDISENHO DO INDEPENDENT RECONSTRUCTION PROTOCOL v1.1 |
| **Tipo** | Especificação normativa de método (candidata a P-0007.x v1.1) |
| **Status** | **PROPOSTA — aguarda revisão da coordenação + auditoria adversarial independente** |
| **Data** | 2026-08-09 |
| **Autor** | Arquiteto de Protocolo Experimental (GO-7) |
| **Base** | IRP v1.0 (GO-6) + Relatório de Auditoria Independente (FAIL) |
| **Governado por** | P-0007.1 (RA-OI-003), SHADOW-EXPERIMENTS (regra 7), METHODOLOGICAL-DEBT (DEBT-001/006) |
| **Restrições** | Não altera SX-001/002/003, P-0010, SX-SELECTION, protocolos congelados; sem experimento, sem promoção, sem commit |

---

## 1. Objetivo e Escopo

### 1.1 Objetivo

Garantir que a **reconstrução cega** de um experimento Shadow (SX-###) satisfaça **condições verificáveis de cegamento** — não apenas declarações de intenção.

> **Definição operacional de cegamento verificável:**
> Para cada execução, existe um conjunto de evidências auditáveis que, coletivamente, **demonstram** que o Reconstructor não pôde acessar, inferir ou ser contaminado por informação proveniente da Narrative Package, do caso, ou de experimentos anteriores — **antes** do Freeze.

### 1.2 Escopo

- Aplica-se a **todos** os Shadow Experiments futuros (SX-004+)
- Pode ser validado via **experimento-piloto de método** (re-execução isolada de camada de reconstrução) antes de virar padrão
- Não resolve retrospectivamente o SX-003 (permanece PARADO — GO-5A)

### 1.3 Fora de escopo

- Execução de SX-004 ou novo experimento científico
- Promoção de Signals, Patterns, LAW-H
- Análise transversal SX-001/002/003
- Alteração de protocolos congelados

---

## 2. Modelo de Ameaça

| Ator | Capacidades | Objetivo Adversarial |
|---|---|---|
| **Producer** (honesto mas descuidado) | Acesso total ao NP; deriva BIP; pode vazar via metadados, seleção, instruções | — |
| **Reconstructor** (malicioso, competente) | Recebe BIP; controle total sobre seu ambiente; pode sondar filesystem, rede, ferramentas, timestamps, hashes, variáveis, clipboard, histórico, processos, git, LSP | Reconstruir narrativa original, identificar caso, inferir exclusões, acessar NP |
| **Auditor** (malicioso ou capturado) | Acesso a todos os artefactos, logs, trilhas; pode aprovar indevidamente, omitir falhas, vazar informação entre papéis | Aprovar execução comprometida; coordenar com Producer/Reconstructor |
| **Operador Humano** (mesmo humano para múltiplos papéis) | Coordenação implícita, comunicação informal, conhecimento prévio de SX-001/002/003, DEBT-009, Kernel ECP | Burlar isolamento sem violar letras das regras |
| **Ambiente Compartilhado** | Filesystem, clipboard, env vars, shell history, ferramentas, git, LSP, rede, cache, processos irmãos | Vazar estado entre papéis via canais laterais |

**Pressuposto:** O adversário **não** viola instruções literais (ex.: "não leia arquivo X"), mas explora **tudo o que não é tecnicamente impedido**.

---

## 3. Definição Formal de Independência

### 3.1 Independência como Propriedade Verificável

> **Independência (IRP-v1.1):** Uma reconstrução *R* é independente da narrativa *N* se e somente se existe um conjunto de evidências *E* tal que:
>
> 1. **E** é produzido **durante** a execução (não pós-hoc)
> 2. **E** é **imutável** após Freeze (hash-commitment)
> 3. **E** é **verificável por terceiros** sem acesso a segredos
> 4. **E** demonstra que, no intervalo [Início da Reconstrução, Freeze]:
>    - O Reconstructor **não teve acesso** a *N* nem a qualquer derivação semântica de *N*
>    - O Reconstructor **não pôde inferir** estrutura, conteúdo ou identidade de *N* via metadados, canais laterais ou conhecimento prévio
>    - O ambiente de execução **não compartilhou estado** com Producer ou Auditor
>    - A comunicação entre papéis foi **restrita a artefactos selados**

### 3.2 Níveis de Independência (Revisados)

| Nível | Critério | Verificável? | Status IRP-v1.1 |
|---|---|---|---|
| **I** | Instrução "não consulte" | ❌ | **Proibido** |
| **II** | Separação de arquivos + ACL | ⚠️ Parcial | **Insuficiente** |
| **III** | Ambientes isolados + manifesto + hash + audit trail | ⚠️ Parcial (v1.0) | **Base necessária** |
| **IV** | **Entidades distintas + ambientes isolados + BIP anonimizado + commitment scheme + auditor independente + atestação de ambiente + controles adversariais** | ✅ **Sim** | **Obrigatório** |

> **IRP-v1.1 implementa Nível IV.** Nível III (v1.0) foi classificado FAIL.

---

## 4. Papéis e Entidades

| Papel | Entidade Requerida | Isolamento Mínimo |
|---|---|---|
| **Narrative Producer (P)** | Modelo/Instância **A** (ex.: `gpt-4o-producer-v1`) | Container/VM `prod-env` — filesystem dedicado, sem rede, sem clipboard |
| **Independent Reconstructor (R)** | Modelo/Instância **B ≠ A** (ex.: `claude-3.5-reconstructor-v1`) | Container/VM `recon-env` — filesystem dedicado, sem rede, sem clipboard, **estado inicial limpo** |
| **Isolation Auditor (Aud)** | Entidade **C ∉ {A,B}** — terceiro independente (modelo diferente, ou humano sem conhecimento do caso) | Container/VM `audit-env` — apenas leitura de artefactos selados |
| **Sealer (Sel)** | Função determinística (script) — **não** agente cognitivo | Executa em `prod-env` após P; selo imutável |
| **Orchestrator (Orch)** | Função determinística (script) — coordena fluxo, não decide conteúdo | Executa em host isolado; apenas move artefactos selados entre ambientes |

**Regra de Ouro:** `A ≠ B ≠ C` — **entidades cognitivas distintas**. Mesmo modelo com pesos diferentes aceito; mesma instância **rejeitada**. Mesmo humano operando múltiplos papéis **rejeitado**.

---

## 5. Boundary Entre Producer / Reconstructor / Auditor

```
┌─────────────────────────────────────────────────────────────────────┐
│                        ORCHESTRATOR (host)                          │
│  • Move artefactos selados entre ambientes                          │
│  • Enforça sequência temporal (sequencer determinístico)            │
│  • Não inspeciona conteúdo                                          │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ artefactos selados (read-only)
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│  PRODUCER     │  │ RECONSTRUCTOR │  │ AUDITOR       │
│  (prod-env)   │  │ (recon-env)   │  │ (audit-env)   │
│               │  │               │  │               │
│ • Sources     │  │ • BIP apenas  │  │ • Selos       │
│ • Narrative   │  │ • Instruções  │  │ • FRZ         │
│ • AFs         │  │   universais  │  │ • Audit trail │
│ • Deriva BIP  │  │ • Produz R    │  │ • Veredito    │
│ • Sela NP     │  │ • Sela FRZ    │  │   (PASS/FAIL) │
│ • Commit H(NP)│  │               │  │               │
└───────┬───────┘  └───────┬───────┘  └───────┬───────┘
        │                  │                  │
        │ NP.seal          │ BIP              │ FRZ, logs
        ▼                  ▼                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    EVIDENCE STORE (append-only, WORM)               │
│  • NP.seal, BIP, FRZ, Audit_Report, Attestation, Commitments       │
│  • Imutável após escrita; hash-chain encadeado                      │
└─────────────────────────────────────────────────────────────────────┘
```

**Propriedades da boundary:**
- **Nenhum** canal de dados direto entre `prod-env`, `recon-env`, `audit-env`
- Todo fluxo mediado por **Orchestrator** via artefactos selados (arquivos imutáveis com hash)
- `recon-env` **nunca** recebe NP, Narrative, AFs brutos, identificadores de caso
- `audit-env` **apenas lê** artefactos no Evidence Store; não executa código dos outros

---

## 6. Arquitetura de Ambientes Isolados

### 6.1 Especificação de Isolamento (Obrigatória)

| Recurso | prod-env | recon-env | audit-env |
|---|---|---|---|
| **Filesystem** | Dedicado (volume próprio) | Dedicado (volume próprio) | Dedicado (read-only Evidence Store) |
| **Rede** | Desabilitada | Desabilitada | Desabilitada (apenas mount Evidence Store) |
| **Clipboard** | Desabilitado | Desabilitado | Desabilitado |
| **Variáveis de Ambiente** | Apenas `PROD_ENV=1`, `SESSION_ID` | Apenas `RECON_ENV=1`, `SESSION_ID` | Apenas `AUDIT_ENV=1`, `SESSION_ID` |
| **Shell History** | Desabilitado (`HISTFILE=/dev/null`) | Desabilitado | Desabilitado |
| **Ferramentas/Editor/LSP** | Conjunto mínimo dedicado | Conjunto mínimo dedicado | Apenas verificadores (hash, diff, grep) |
| **GPU/Compute** | Isolado (sem memória compartilhada) | Isolado | CPU only |
| **Processos Irmãos** | Nenhum | Nenhum | Nenhum |
| **Git** | Desabilitado | Desabilitado | Desabilitado |
| **Timestamps** | Relógio monotônico local | Relógio monotônico local | Relógio monotônico local |

### 6.2 Atestação de Ambiente (Obrigatória)

Cada ambiente, ao iniciar, produz **Environment Attestation** assinada:

```yaml
# attestation-prod-<session_id>.yaml
environment: "prod-env"
session_id: "sx004-prod-20260809-143022-a7f3"
timestamp_monotonic_ns: 1234567890123456789
hostname_hash: "sha256(hostname) = a1b2c3..."
mounts:
  - "/workspace: rw, private"
  - "/evidence-store: ro, private"
network_interfaces: []
clipboard: disabled
env_vars:
  PROD_ENV: "1"
  SESSION_ID: "sx004-prod-20260809-143022-a7f3"
tools_installed:
  - "python3.11 (hash: ...)"
  - "sha256sum (hash: ...)"
  - "jq (hash: ...)"
process_list_hash: "sha256(ps aux) = ..."
git_available: false
lsp_running: false
signature: "ed25519(orchestrator_key, payload)"
```

**Verificação:** Auditor valida que `attestation-recon` prova isolamento **antes** de aceitar FRZ.

---

## 7. Blind Input Package (BIP) — v1.1

### 7.1 Princípio

> O BIP é **o único** artefacto que cruza a boundary `prod-env → recon-env`.
> Ele contém **apenas** fato autorizados, **sem** metadados vazadores, **sem** identificadores semânticos.

### 7.2 Estrutura do BIP (Entregue ao Reconstructor)

```json
{
  "bip_version": "1.1",
  "session_id": "sx004-recon-20260809-143022-a7f3",
  "facts": [
    { "id": "f-7a3f", "claim": "O projeto teve duração aproximada de 15 anos." },
    { "id": "f-9k2m", "claim": "O orçamento total foi cerca de 3 bilhões de dólares." },
    { "id": "f-b1c4", "claim": "Houve um anúncio público formal de início em 1990." }
    // ... apenas claims factuais, sem ordem semântica
  ],
  "instructions": "UNIVERSAL_INSTRUCTIONS_v1.1",
  "bip_hash": "sha256(canonical_json(facts + instructions)) = ...",
  "np_commitment": "sha256(np_seal) = ..."
}
```

**O que NÃO está no BIP (diferente do v1.0):**
- ❌ `af_ids` originais (AF-011, AF-012...)
- ❌ `exclusions` (o que foi deixado de fora)
- ❌ `digests` por AF (hashes individuais)
- ❌ `sources` (origens causais, hashes de documentos)
- ❌ Identificador do caso (SX-003, Genoma, Challenger, Ebola)
- ❌ Domínio, número do experimento, qualquer metadado semântico

### 7.3 Instruções Universais Fixas (`UNIVERSAL_INSTRUCTIONS_v1.1`)

> **Idênticas para TODOS os experimentos.** Não adaptadas ao caso.

```
Você é um Reconstructor Independente. Sua tarefa:

1. Receba uma lista de claims factuais (facts). Cada fact tem um ID opaco e um texto.
2. Para cada fact, determine se ele suporta a presença de alguma das seguintes entidades:
   Problem, Goal, Knowledge, Assumption, Evidence, Decision, Validation, Risk, Learning, Project.
3. Registre sua determinação como: PRESENT / ABSENT / INFERRED / AMBIGUOUS.
4. Se INFERRED, explique brevemente o raciocínio usando APENAS o fact citado.
5. Não compare com outros experimentos. Não use vocabulário de projetos anteriores.
6. Não tente identificar o projeto, domínio, ou número do experimento.
7. Sua saída é um JSON com a estrutura especificada.
8. Ao finalizar, seu output será congelado (hash + timestamp). Não edite após congelamento.
```

### 7.4 Derivação do BIP (Producer → Sealer)

1. Producer cria NP completo (sources, narrative, AFs com IDs canônicos)
2. Sealer executa **deterministicamente**:
   - Extrai claims factuais dos AFs (strip de metadados ECP, IDs canônicos)
   - Embaralha ordem dos facts (seed = `session_id`)
   - Atribui IDs opacos aleatórios (`f-<hex8>`)
   - Remove qualquer fact marcado como "interpretativo" (critério fixo, não decisão humana)
   - Anexas `UNIVERSAL_INSTRUCTIONS_v1.1`
   - Calcula `bip_hash`
   - Lê `np_commitment = H(NP.seal)` do Evidence Store
   - Emite `BIP.json` + `BIP.seal` (hash + timestamp + assinatura Orchestrator)
3. Orchestrator move `BIP.seal` para `recon-env` (via Evidence Store)

---

## 8. Anonimização

| Elemento v1.0 | Tratamento v1.1 | Justificativa |
|---|---|---|
| `af_ids` canônicos | **IDs opacos aleatórios** `f-<hex8>` | Impede reconstrução de ordem, granularidade, gaps |
| `exclusions` | **Removido do BIP** (apenas Auditor vê no NP.seal) | Elimina mapa do que é "interpretativo" |
| `digests` por AF | **Apenas `bip_hash` + `np_commitment`** | Impede inversão de hash de claims de baixa entropia |
| `sources` / origens | **Removido do BIP** | Impede inferência de domínio via proveniência |
| Identificador do caso | **Nunca entregue ao Reconstructor** | Impede conhecimento prévio (SX-003, Genoma, etc.) |
| Ordem dos facts | **Embaralhada** (seed = `session_id`) | Impede reconstrução de fluxo narrativo |
| Tamanho do BIP | **Padding para tamanho fixo** (ex.: 50 facts + ruído) | Oculta % de exclusão e complexidade |

---

## 9. Controle de Metadados

### 9.1 Metadados Proibidos no BIP

| Metadado | Ação |
|---|---|
| Contagem original de AFs | Não entregue (padding fixo) |
| Hashes individuais de AFs | Não entregues |
| Timestamps de criação dos AFs | Não entregues |
| Estrutura de diretórios NP | Não entregue (BIP = arquivo único JSON) |
| Nomes de arquivos fonte | Não entregues |
| Domínio / taxonomia | Não entregue |

### 9.2 Metadados Permitidos (Apenas Auditor)

Entregues via `NP.seal` no Evidence Store (audit-env read-only):
- `af_ids` canônicos + mapeamento para IDs opacos
- `exclusions` com justificativa por fact
- `sources` + proveniência (RA-EI-004)
- `np_seal` (hash + timestamp + assinatura)

---

## 10. Controle Temporal

### 10.1 Ruído Temporal Obrigatório

| Evento | Atraso Adicionado | Propósito |
|---|---|---|
| `NP.seal` → `BIP` disponível | `Uniform(30s, 300s)` | Oculta complexidade de derivação |
| Início Reconstructor → Leitura BIP | `Uniform(5s, 60s)` | Oculta latência de inicialização |
| Fim Reconstructor → `FRZ` | `Uniform(10s, 120s)` | Oculta tempo de processamento |

**Implementação:** Orchestrator injeta `sleep` aleatório (seed = `session_id`) antes de mover artefactos.

### 10.2 Relógio Monotônico

Todos os timestamps usam `clock_gettime(CLOCK_MONOTONIC)` — **não** relógio de parede. Evita correlação com logs externos.

---

## 11. Comunicação

### 11.1 Canais Permitidos

| De → Para | Canal | Conteúdo |
|---|---|---|
| Orchestrator → prod-env | Artefacto selado | `SESSION_ID`, `UNIVERSAL_INSTRUCTIONS` |
| prod-env → Evidence Store | Artefacto selado | `NP.seal`, `BIP.seal` |
| Evidence Store → recon-env | Artefacto selado | `BIP.seal` |
| recon-env → Evidence Store | Artefacto selado | `FRZ.seal`, `Reconstruction.json` |
| Evidence Store → audit-env | Mount read-only | Todos artefactos selados |
| audit-env → Evidence Store | Artefacto selado | `AUDIT_REPORT.seal` |

### 11.2 Canais Proibidos (Enforced by Architecture)

- ❌ Comunicação direta entre ambientes (sockets, pipes, arquivos compartilhados)
- ❌ Comunicação humana informal (Slack, email, verbal, tickets, comentários PR)
- ❌ Variáveis de ambiente compartilhadas
- ❌ Clipboard, selection buffer, drag-and-drop
- ❌ Processos pai/filho compartilhando memória

### 11.3 Silêncio Operacional

Durante a execução (`SESSION_ID` ativo):
- Nenhum log externo sobre progresso
- Nenhuma notificação "BIP pronto", "FRZ gerado"
- Orchestrator **não** emite eventos observáveis externamente
- Auditoria de silêncio: `ps aux`, `netstat`, `lsof` em todos os ambientes mostram zero conexões externas

---

## 12. Freeze (Congelamento)

### 12.1 Mecanismo

1. Reconstructor finaliza `Reconstruction.json`
2. Orchestrator calcula:
   - `frz_hash = sha256(Reconstruction.json)`
   - `frz_timestamp = monotonic_now()`
   - `frz_commitment = sha256(frz_hash || frz_timestamp || session_id)`
3. Orchestrator escreve `FRZ.seal` (JSON + assinatura) no Evidence Store
4. **A partir deste instante**, `Reconstruction.json` é **imutável** — qualquer modificação requer nova versão (`FRZ-v2.seal`) com evidência de motivo

### 12.2 Commitment Scheme (Prevents Post-Hoc)

- `np_commitment = H(NP.seal)` incluído no BIP **antes** da reconstrução
- `frz_commitment` inclui `np_commitment` implicitamente via `session_id` encadeado
- Auditor verifica: `H(NP.seal)` no BIP == `H(NP.seal)` no Evidence Store
- Qualquer alteração no NP após `BIP` deriva `np_commitment` divergente → detecção imediata

### 12.3 Freeze Verificável (C-FRZ)

| Check | Verificação |
|---|---|
| C-FRZ-01 | `FRZ.seal` existe no Evidence Store com assinatura Orchestrator válida |
| C-FRZ-02 | `frz_hash` = `sha256(Reconstruction.json)` no Evidence Store |
| C-FRZ-3 | `frz_timestamp` > `bip_delivery_timestamp` (ordem causal) |
| C-FRZ-04 | Nenhum `FRZ-vN.seal` posterior sem justificativa registrada e assinada |

---

## 13. Hash / Commitment

| Artefacto | Hash | Commitment | Verificação |
|---|---|---|---|
| `NP.seal` | `sha256(NP_bundle)` | `np_commitment` no BIP | Auditor compara |
| `BIP` | `sha256(BIP.json)` | `bip_hash` no BIP + `BIP.seal` | Reconstructor + Auditor |
| `Reconstruction` | `sha256(Reconstruction.json)` | `frz_hash` em `FRZ.seal` | Auditor |
| `FRZ.seal` | `sha256(FRZ.seal payload)` | `frz_commitment` | Auditor |
| `AUDIT_REPORT` | `sha256(report)` | `audit_commitment` | Orchestrator |
| **Chain** | `H(prev || current)` | Hash-chain encadeado | Auditor verifica integridade total |

---

## 14. Atestação de Ambiente

### 14.1 Atestações Obrigatórias (Uma por Ambiente)

| Atestação | Produtor | Verificador | Critério PASS |
|---|---|---|---|
| `attestation-prod` | Orchestrator (início prod-env) | Auditor | Isolamento §6.1 comprovado |
| `attestation-recon` | Orchestrator (início recon-env) | Auditor | Isolamento §6.1 + estado limpo comprovado |
| `attestation-audit` | Orchestrator (início audit-env) | Orchestrator (auto) | Read-only Evidence Store |

### 14.2 Evidências Incluídas

- `mounts` (mostra volumes dedicados, sem compartilhamento)
- `network_interfaces: []` (rede desabilitada)
- `clipboard: disabled`
- `env_vars` (apenas permitidas)
- `tools_installed` + hashes (ferramentas fixas, sem LSP/indexador)
- `process_list_hash` (sem processos irmãos)
- `git_available: false`
- `lsp_running: false`
- `memory_shared: false` (verificação `ipcs -m` vazio)

### 14.3 Falha de Atestação → FAIL Imediato

Se qualquer atestação não passar verificação do Auditor → execução classificada **FAIL**, sem prosseguir para Reveal.

---

## 15. Audit Trail

### 15.1 Trilha Mínima Obrigatória (Imutável, Hash-Chain)

| Evento | Artefacto | Conteúdo Mínimo |
|---|---|---|
| E-01 | `NP.seal` | `session_id`, `np_hash`, `timestamp`, `producer_id`, `attestation-prod` ref |
| E-02 | `BIP.seal` | `session_id`, `bip_hash`, `np_commitment`, `timestamp`, `sealer_id` |
| E-03 | `BIP_delivery` | `session_id`, `bip_hash`, `timestamp`, `orchestrator_id` |
| E-04 | `Recon_start` | `session_id`, `reconstructor_id`, `attestation-recon` ref, `timestamp` |
| E-05 | `FRZ.seal` | `session_id`, `frz_hash`, `frz_timestamp`, `frz_commitment`, `reconstructor_id` |
| E-06 | `Reveal_trigger` | `session_id`, `timestamp`, `orchestrator_id` (após Auditor PASS) |
| E-07 | `AUDIT_REPORT.seal` | `session_id`, `verdict`, `evidence_refs`, `timestamp`, `auditor_id` |

### 15.2 Verificação de Cadeia

Auditor verifica: `H(E-01) → H(E-02) → ... → H(E-07)` encadeados. Qualquer lacuna → FAIL.

---

## 16. Reveal (Revelação da Narrativa)

### 16.1 Gatilho

**Somente após** Auditor emitir `AUDIT_REPORT.seal` com `verdict: PASS`.

Orchestrator então move `NP.seal` (narrativa + AFs canônicos) para `audit-env` e/ou `Alignment` stage.

### 16.2 Reveal Não Retrocontamina

- `FRZ.seal` já existe e é imutável
- Reconstructor **não** recebe a narrativa (já finalizou)
- Alignment é executado por **entidade D ≠ A,B,C** (ou Auditor em papel separado, com nova atestação)
- Reconstructor **não** participa de Alignment

---

## 17. Alignment

### 17.1 Separação Estrita

| Fase | Executor | Input | Output |
|---|---|---|---|
| Reconstruction | Reconstructor (B) | BIP apenas | `Reconstruction.json` (congelado em FRZ) |
| Alignment | **Alignment Analyst (D)** | `FRZ.seal` + `NP.seal` (revelado) | `Alignment_Report.json` |

### 17.2 Alignment Analyst (D)

- Entidade **distinta** de Producer, Reconstructor, Auditor
- Mesmo isolamento de ambiente (`align-env`)
- Não conhece BIP, não conhece Reconstructor
- Recebe **após** FRZ + Auditor PASS

### 17.3 Retrocontaminação Impossível

- `Reconstruction.json` já congelado (hash-chain)
- Alignment Analyst não pode alterar FRZ
- Qualquer discrepância registrada em `Alignment_Report` (não na reconstrução)

---

## 18. Controles C-01 em Diante (Verificáveis)

| ID | Claim | Mecanismo | Evidência | Auditoria | Veredito |
|---|---|---|---|---|---|
| **C-01** | BIP contém apenas facts autorizados | Derivação determinística do Sealer + `bip_hash` | `BIP.seal`, `NP.seal` (auditor) | Comparar facts no BIP vs NP (via mapeamento opaco) | PASS/FAIL |
| **C-02** | BIP sem prosa interpretativa / refs SX-### | Validação de schema + grep por padrões proibidos | `BIP.json` | Automatizado: zero matches | PASS/FAIL |
| **C-03** | Reconstructor sem acesso a NP | Atestação `attestation-recon` + trilha de acesso | `attestation-recon`, `access_log_recon` | Verificar: mounts, network, env, processes, zero NP paths | PASS/FAIL |
| **C-04** | FRZ antes de Reveal (ordem causal) | Timestamps monotônicos + hash-chain | `FRZ.seal`, `Reveal_trigger` | `frz_timestamp < reveal_timestamp` | PASS/FAIL |
| **C-05** | Texto congelado sem termos-âncora da narrativa | Grep automatizado (lista de termos extraída do NP) | `Reconstruction.json`, `NP.seal` | Zero matches de n-gramas > 3 palavras | PASS/FAIL |
| **C-06** | Sem edit pós-freeze sem versão | Hash-chain imutável | `FRZ.seal`, `FRZ-vN.seal` (se houver) | Verificar chain; versões têm justificativa assinada | PASS/FAIL |
| **C-07** | Veredito de cegamento antes do Reveal | `AUDIT_REPORT.seal` antes de `Reveal_trigger` | Trilha E-06, E-07 | `audit_timestamp < reveal_timestamp` | PASS/FAIL |
| **C-08** | Entidades distintas (P ≠ R ≠ Aud) | Registro de IDs de modelo/instância | `producer_id`, `reconstructor_id`, `auditor_id` | Verificar desigualdade | PASS/FAIL |
| **C-09** | Ambientes isolados (§6.1) | Atestações assinadas | `attestation-prod`, `attestation-recon`, `attestation-audit` | Verificação completa §14 | PASS/FAIL |
| **C-10** | BIP anonimizado (IDs opacos, sem exclusões, sem hashes individuais) | Validação de schema BIP v1.1 | `BIP.json` | Schema check + ausência de campos proibidos | PASS/FAIL |
| **C-11** | Reconstructor sem identificador de caso | Ausência de campos semânticos no BIP + atestação | `BIP.json`, prompt do Reconstructor | Verificar: BIP sem case_id, prompt sem menção | PASS/FAIL |
| **C-12** | Auditor independente | `auditor_id` ∉ {producer_id, reconstructor_id} + atestação | Registro de entidades | Verificar distinção + atestação-audit | PASS/FAIL |
| **C-13** | Silêncio operacional | Ausência de logs externos durante sessão | Logs de sistema, rede, processos | Verificar: zero eventos observáveis | PASS/FAIL |
| **C-14** | Ruído temporal injetado | Delays registrados vs esperados | `BIP_delivery` timestamp, `FRZ` timestamp | Verificar: delays dentro de `Uniform(min,max)` | PASS/FAIL |
| **C-15** | Commitment scheme (NP → BIP → FRZ) | Hash-chain verificada | `np_commitment` no BIP, `frz_commitment` no FRZ | Verificar encadeamento | PASS/FAIL |
| **C-16** | Alignment separado (D ≠ A,B,C) | `alignment_analyst_id` distinto | Registro de entidades | Verificar distinção | PASS/FAIL |
| **C-17** | Zero retrocontaminação | FRZ imutável antes de Alignment | `FRZ.seal` timestamp < `Alignment_start` | Verificar ordem causal | PASS/FAIL |

---

## 19. Critérios PASS / CONDITIONAL PASS / FAIL

### PASS (Execução válida para evidência científica)

**TODOS** C-01..C-17 = PASS.

### CONDITIONAL PASS (Execução com ressalvas — não serve para promoção)

- C-01..C-07 = PASS (controles base)
- C-08..C-17: **até 2** = FAIL, desde que:
  - Falha documentada com evidência
  - Não compromete isolamento cognitivo central (ex.: ruído temporal fora da faixa mas ambientes isolados)
  - Coordenação aprova explicitamente

### FAIL (Execução inválida — não entra no corpus)

Qualquer um:
- C-01..C-07 = FAIL
- C-08 (entidades distintas) = FAIL
- C-09 (ambientes isolados) = FAIL
- C-10 (BIP anonimizado) = FAIL
- C-12 (auditor independente) = FAIL
- Evidência de colusão, vazamento, ou violação de silêncio

---

## 20. Matriz BR-01..BR-15 × Controles

| Brecha | Controles que Mitigam | Status v1.1 |
|---|---|---|
| **BR-01 Selection Leakage** | C-10 (sem `exclusions` no BIP), C-14 (padding + embaralhamento), C-10 (IDs opacos) | ✅ **Resolvido** |
| **BR-02 Identity Leakage** | C-08 (entidades distintas obrigatórias), C-09 (ambientes isolados) | ✅ **Resolvido** |
| **BR-03 Metadata Leakage** | C-10 (sem contagens, sem hashes individuais, sem sources), C-14 (padding fixo) | ✅ **Resolvido** |
| **BR-04 Input Leakage** | C-10 (instruções universais fixas), C-11 (sem case_id) | ✅ **Resolvido** |
| **BR-05 Filename/Path Leakage** | C-10 (BIP = JSON único, sem paths), C-09 (ambiente isolado sem `ls` NP) | ✅ **Resolvido** |
| **BR-06 Memory Contamination** | C-08 (entidades distintas — pesos/memória separados), C-11 (sem case_id no prompt) | ✅ **Resolvido** |
| **BR-07 Shared-Environment** | C-09 (isolação completa §6.1), C-13 (silêncio operacional) | ✅ **Resolvido** |
| **BR-08 Temporal Leakage** | C-14 (ruído temporal obrigatório), C-10 (relógio monotônico) | ✅ **Mitigado** (residual: análise de distribuição de delays) |
| **BR-09 Post-Hoc Contamination** | C-04, C-07 (ordem causal FRZ < Reveal < Alignment), C-17 (retrocontaminação impossível) | ✅ **Resolvido** |
| **BR-10 Alignment Leakage** | C-16, C-17 (Alignment Analyst D distinto, após FRZ) | ✅ **Resolvido** |
| **BR-11 Audit Manipulation** | C-12 (Auditor independente C ≠ A,B), C-15 (commitment scheme), C-09 (audit-env isolado) | ✅ **Resolvido** |
| **BR-12 Executor Collusion** | C-08, C-12 (entidades distintas), C-13 (silêncio operacional) | ✅ **Resolvido** |
| **BR-13 Human Communication** | C-13 (silêncio operacional enforçado), C-09 (ambientes isolados) | ✅ **Resolvido** |
| **BR-14 Tool/Environment** | C-09 (ferramentas dedicadas, sem LSP/git), C-13 | ✅ **Resolvido** |
| **BR-15 Hash/Manifesto Leakage** | C-10 (sem `exclusions`, sem hashes individuais no BIP), C-15 (commitment scheme) | ✅ **Resolvido** |

---

## 21. Ataque Adversarial (v1.1)

| Vetor | Tentativa | Resultado v1.1 |
|---|---|---|
| Ler `af_ids` no BIP | **Impossível** — BIP tem apenas `f-<hex8>` opacos | ❌ Bloqueado (C-10) |
| `wc -c BIP` vs `wc -c NP` | **Impossível** — Reconstructor não tem NP; BIP tem padding fixo | ❌ Bloqueado (C-09, C-10) |
| Timestamps `seal` vs `FRZ` | **Ruído temporal** (Uniform 30-300s) oculta correlação | ⚠️ **Mitigado** (residual estatístico) |
| Inversão de hash de AF | **Impossível** — hashes individuais não no BIP; `np_commitment` = H(NP) não H(AF) | ❌ Bloqueado (C-10, C-15) |
| `tree Evidence_Archive` | **Impossível** — recon-env não monta Evidence Archive; só recebe BIP.seal | ❌ Bloqueado (C-09) |
| Ordem dos facts | **Embaralhada** (seed = session_id) | ❌ Bloqueado (C-10) |
| `git log` | **Impossível** — git desabilitado em recon-env | ❌ Bloqueado (C-09) |
| Variáveis de ambiente | **Apenas `RECON_ENV=1`, `SESSION_ID`** — sem NP_PATH | ❌ Bloqueado (C-09) |
| Nomes de processos | **Isolado** — sem processos irmãos, `ps` mostra apenas Reconstructor | ❌ Bloqueado (C-09) |
| Ferramentas/LSP/git | **Desabilitados** — conjunto mínimo fixo sem indexador | ❌ Bloqueado (C-09) |
| Histórico Git | **Desabilitado** | ❌ Bloqueado (C-09) |
| Prompt "SX-003 Genoma" | **Impossível** — prompt universal fixo, sem case_id | ❌ Bloqueado (C-11) |
| Comunicação humana | **Silêncio operacional** — nenhum canal, logs mostram zero tráfego | ❌ Bloqueado (C-13) |
| Campo `exclusions` | **Não entregue ao Reconstructor** — só Auditor vê no NP.seal | ❌ Bloqueado (C-10) |
| Instruções "neutras" | **Universais fixas** — idênticas para todo experimento | ❌ Bloqueado (C-10) |

**Conclusão:** Ataques viáveis em v1.0 são **bloqueados ou mitigados a residual estatístico** em v1.1.

---

## 22. Procedimento de Auditoria

### 22.1 Papel do Auditor (Independente)

1. **Pré-execução:** Valida `attestation-prod`, `attestation-recon`, `attestation-audit`
2. **Durante:** Monitora Evidence Store (read-only) — verifica sequência E-01..E-05
3. **Pós-FRZ:** Executa C-01..C-17 automatizados + revisão manual de evidências
4. **Veredito:** Emite `AUDIT_REPORT.seal` com `verdict: PASS | CONDITIONAL_PASS | FAIL`
5. **Somente se PASS:** Orchestrator dispara Reveal (E-06)

### 22.2 Checklist de Auditoria (Executável)

```bash
#!/bin/bash
# audit_verify.sh — roda em audit-env

verify_c01() { # BIP ≡ NP (via mapeamento opaco)
  jq -r '.facts[].id' BIP.json | sort > bip_ids.txt
  jq -r '.opaque_map[]' NP.seal | sort > np_opaque.txt
  diff bip_ids.txt np_opaque.txt && echo "C-01 PASS" || echo "C-01 FAIL"
}

verify_c02() { # BIP sem prosa/refs
  ! grep -iE '(sx-00[0-9]|challenger|ebola|genoma|interpretativo|conclusivo)' BIP.json \
    && echo "C-02 PASS" || echo "C-02 FAIL"
}

verify_c03() { # Recon sem acesso NP
  # attestation-recon já validada; verificar access_log_recon
  ! grep -q "narrative_package\|NP.seal" access_log_recon.txt \
    && echo "C-03 PASS" || echo "C-03 FAIL"
}

verify_c04() { # FRZ < Reveal
  frz_ts=$(jq -r '.frz_timestamp' FRZ.seal)
  rev_ts=$(jq -r '.timestamp' Reveal_trigger.seal)
  [[ $frz_ts -lt $rev_ts ]] && echo "C-04 PASS" || echo "C-04 FAIL"
}

verify_c05() { # Sem termos-âncora
  # extrai n-gramas do NP (narrative), busca no Reconstruction
  python3 check_ngrams.py NP.seal Reconstruction.json \
    && echo "C-05 PASS" || echo "C-05 FAIL"
}

# ... C-06 a C-17 similarmente automatizados

main() {
  for c in {01..17}; do
    "verify_c${c}"
  done
}
```

### 22.3 Evidências Obrigatórias para Auditoria

| Evidência | Origem | Formato |
|---|---|---|
| `attestation-prod/recon/audit` | Orchestrator | YAML assinado |
| `NP.seal` | Sealer | JSON + assinatura |
| `BIP.seal` | Sealer | JSON + assinatura |
| `FRZ.seal` | Orchestrator | JSON + assinatura |
| `Reconstruction.json` | Reconstructor | JSON |
| `AUDIT_REPORT.seal` | Auditor | JSON + assinatura |
| `access_log_recon` | recon-env (kernel audit) | CSV (path, timestamp, pid) |
| `hash_chain.log` | Orchestrator | JSONL (evento, hash_prev, hash_curr) |
| `timing_log` | Orchestrator | JSON (evento, monotonic_ns, delay_injected) |

---

## 23. Failure Conditions (Classificação Automática FAIL)

| Condição | Ação |
|---|---|
| Qualquer `attestation-*` falha validação | **FAIL imediato** — não prossegue |
| C-08, C-09, C-10, C-12 = FAIL | **FAIL** — isolamento central comprometido |
| Hash-chain quebrada (gap em E-01..E-07) | **FAIL** |
| `np_commitment` no BIP ≠ `H(NP.seal)` no Evidence Store | **FAIL** — NP alterado após derivação |
| `FRZ` timestamp ≥ `Reveal` timestamp | **FAIL** — ordem causal violada |
| Reconstructor acessou path fora de `/workspace/BIP` | **FAIL** (via `access_log_recon`) |
| Auditor `auditor_id` ∈ {`producer_id`, `reconstructor_id`} | **FAIL** |
| Qualquer comunicação detectada (rede, clipboard, env var compartilhada) | **FAIL** |

---

## 24. Perguntas Abertas (Para Coordenação)

1. **Validação do IRP-v1.1:** Executar **experimento-piloto de método** (re-execução isolada da camada de reconstrução do SX-003) antes de adotar para SX-004+?
2. **Entidades distintas:** Exigir **modelos fundamentalmente diferentes** (ex.: GPT vs Claude vs humano) ou aceitar **instâncias isoladas do mesmo modelo** (pesos idênticos, contexto limpo)?
3. **Auditor independente:** Quem exerce? Modelo terceiro? Humano sem conhecimento do caso? Comité rotativo?
4. **Tamanho fixo do BIP (padding):** Qual tamanho padrão? (Ex.: 64 facts — padroniza todos os experimentos)
5. **Seed de embaralhamento:** `session_id` como seed é determinístico e auditável — aceitar?
6. **Ruído temporal:** Faixas `Uniform(30,300)`, `Uniform(5,60)`, `Uniform(10,120)` — calibrar?
7. **Alinhamento (Alignment Analyst D):** Mesmo modelo que Auditor? Modelo quarto? Humano?
8. **Formalização v1.1:** IRP vira seção de `SHADOW-EXPERIMENTS` v1.1, novo `P-0007.2`, ou documento autônomo `P-0011`?
9. **Critério CONDITIONAL_PASS:** Até 2 falhas em C-08..C-17 — confirmar limite?
10. **Transição SX-003:** Após IRP-v1.1 validado, re-executar **apenas** a reconstrução do SX-003 sob IRP-v1.1 para resolver contaminação (GO-5A alt. B)?

---

## 25. Histórico de Revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-09 | IRP v1.0 (GO-6) — classificado FAIL por auditoria independente |
| **1.1** | **2026-08-09** | **IRP v1.1 (GO-7) — redesenho completo pós-FAIL: Nível IV, entidades distintas, ambientes isolados, BIP anonimizado, commitment scheme, auditor independente, atestação de ambiente, silêncio operacional, ruído temporal, Alignment separado, 17 controles verificáveis C-01..C-17, matriz BR×C resolvida, procedimento de auditoria automatizado. PROPOSTA — PARAR para revisão + auditoria adversarial independente.** |

---

**FIM DA ESPECIFICAÇÃO — PARAR**

> Próximo passo (decisão da coordenação): aprovar/ajustar IRP v1.1 → comissionar **auditoria adversarial independente** (terceira IA) → se PASS: validar via experimento-piloto de método → adotar para SX-004+ → só então tratar camada contaminada SX-003 → GO-5 transversal.