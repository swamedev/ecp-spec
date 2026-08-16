# GO-8B — CONTINUITY MASTER

**VERSION:** v2 (2026-08-12) — substitui o v1 (que parava no STOP P1-C2-01 e não incorporava o BIP-007).
**Para novas IAs/chats:** leia este documento primeiro e siga `10-GO-8B-RECOVERY-PROTOCOL.md` e `12-GO-8B-RESUME-PROMPTS.md`.

## 0. Purpose

Este pacote preserva a continuidade operacional, metodológica e de governança do projeto GO-8B entre conversas, sessões, operadores ou IAs diferentes.

**Regra fundamental:** este pacote é um instrumento de continuidade, não uma autorização automática para executar, alterar ou decidir.

Quando houver conflito:
1. artefato LOCKED/FROZEN e seu Lock Record prevalecem sobre este pacote;
2. decisão explicitamente `DECIDED` prevalece sobre recomendação;
3. `DECISION REQUIRED` nunca deve ser resolvido silenciosamente;
4. divergência operacional exige STOP antes de correção;
5. **`DECIDED` não pode ser reconvertido em `DECISION REQUIRED` por recomendação de IA**; e
6. **materiais de entrada prontos (7/7) NÃO são autorização para executar reconstruções/experimento.**

---

## 1. Identidade

- Projeto: GO-8B
- Finalidade: validação piloto metodológica conforme núcleo documental 00–08.
- Núcleo: `experiments/validation/GO-8B/`
- Camada computacional: `scripts/go8b/`
- Estado do núcleo: **LOCKED / FROZEN**
- Artefatos congelados: **13**
- `manifest_sha256`: `c55799d895a4f73888713a8538c6b9a6c5df1d7cde71c88141e16b9e9b216636`
- Experimento: **NOT EXECUTED**
- Dados reais: **NONE**
- Commit: **NONE**

---

## 2. Estado atual

### Gate
**GOVERNANCE / PILOT EXECUTION**

### Sub-gate atual
**P2 (BIP-VAL, NT-05 humano) → P5 (inputs completos) → execução piloto**

### Estado atual
**BLOQUEADO POR GATES HUMANOS — MATERIAIS DE ENTRADA 7/7 PRONTOS; EXECUÇÃO NÃO AUTORIZADA**

### Histórico resolvido

**P1-C2-01 — RESOLVIDO POR GOVERNANÇA / DECIDED — Opção A** (2026-08-12).
- `decisions/P1-C2-01-DECISION.md` → **DECIDED — Opção A**.
- `decisions/ACTION-REGISTER.md` → **A0 = DECIDED**; A1 `C2_PERMUTATION.yaml/.json` **PRODUCED e VALIDATED (7/7 PASS)**.
- A tabela/JSON §6 de `02-C2-PERMUTATION.md` é a **fonte operacional autoritativa**.
- Seed operacional: **`258915`**.
- Seed original (`11473621728585666159`) permanece **`REGISTERED-NON-REPRODUCING`** (não apagada nem "corrigida retroativamente"); reparação seed↔configuração **explicitamente adiada**.
- `INFRA-VALIDATION-REPORT.md` registra **P1 como resolvido por governança**.
- **Isto NÃO libera todo o pre-flight.**

> **Nota de continuidade (v2):** o v1 descrevia P1 como STOP/DECISION REQUIRED por ter sido escrito antes da decisão. A v2 reflete o registro oficial. **Não reabrir P1-C2-01.**

### Documentos de fontes primárias (bases da v2, não reconstruídos da conversa)

- `experiments/validation/GO-8B/decisions/P1-C2-01-DECISION.md`
- `experiments/validation/GO-8B/decisions/ACTION-REGISTER.md` (A0..A5)
- `scripts/go8b/operational/INFRA-VALIDATION-REPORT.md`
- `scripts/go8b/operational/BIP-VAL_REPORT.yaml`
- `experiments/validation/GO-8B/pilot-input/VALIDATION-REPORT.md`
- `experiments/validation/GO-8B/decisions/FINDING-BIP-VAL-01.md`

---

## 3. Estado de segurança

### É permitido agora
- ler artefatos;
- auditar;
- comparar documentação com arquivos;
- preparar e registrar decisões de governança;
- atualizar registros operacionais (ACTION-REGISTER, FINDING, VALIDATION-REPORT);
- **usar os materiais de entrada 7/7 como fonte para as reconstruções A/B/C quando o gate de execução for LIBERADO**;
- preparar plano não executável;
- **preparar a execução/agendamento do NT-05 (humano)**.

### Não é permitido agora
- editar `02-C2-PERMUTATION.md` (nem qualquer artefato congelado);
- reabrir/reverter P1-C2-01 (já DECIDED — Opção A);
- produzir/alimentar o experimento a partir da simples existência dos materiais 7/7;
- **executar as reconstruções A/B/C ou o experimento piloto** (exige gates humanos NT-05 + auditoria + autorização explícita);
- coletar dados reais;
- alterar N, seeds, testes, hipóteses ou parâmetros;
- criar novo Lock;
- alterar qualquer artefato congelado in-place.

---

## 4. Artefatos LOCKED / FROZEN

Núcleo metodológico:
1. `00-GO-8B-R1-DECISION-RECORD.md`
2. `00-GO-8B-R5-GOVERNANCE-DECISION-RECORD.md`
3. `01-CASES-BIPS.md`
4. `02-C2-PERMUTATION.md`
5. `03-SYNTHETIC-TAXONOMY-C3.md`
6. `04-GRAPH-FROM-RECONSTRUCTION.md`
7. `05-WL-KERNEL.md`
8. `06-STATISTICAL-PROTOCOL.md`
9. `07-FAILURE-CRITERIA.md`
10. `08-PRE-REGISTRATION.md`

Reprodutibilidade:
11. `scripts/go8b/go8b_power_sim.py`
12. `scripts/go8b/go8b_statistical_analysis.py`
13. `scripts/go8b/requirements.txt`

Controle:
- `GO-8B-LOCK-MANIFEST.yaml`
- `GO-8B-LOCK-RECORD.yaml`

Os dois artefatos de controle não contam entre os 13 hashes de conteúdo segundo o relatório de Lock; o Lock Record contém o hash do manifesto.

---

## 5. Artefatos operacionais produzidos (P1–P5)

Produzidos e validados (fora do escopo congelado; HASH STATUS: PENDING LOCK PROTOCOL):

- `scripts/go8b/operational/C2_PERMUTATION.yaml` + `.json` — **P1 (7/7 PASS)**
- `scripts/go8b/operational/C3_TAXONOMY.yaml` + `.json` — **P2 (NT-01..04 PASS; NT-05 PENDING)**
- `scripts/go8b/operational/BIP-VAL_REPORT.yaml` — **verdict PENDING (NT-05)**
- `scripts/go8b/operational/graph_from_reconstruction.py` — **P3 (T-GFR 21/21 PASS)**
- `scripts/go8b/operational/wl_kernel.py` + `EMBEDDINGS.npy` (dim 384, 30 vetores) — **P4 (T-WL 12/12 PASS)**
- `experiments/validation/GO-8B/pilot-input/BIP-001..BIP-007` — **materiais de entrada 7/7 (narrativa + atomic facts; zero ECP)**
- `pilot-input/VALIDATION-REPORT.md` — **7/7 VALIDADOS**
- `pilot-input/validate_bip00*.py` — roteiros de validação léxica (52 termos ECP)

Detalhes: `scripts/go8b/operational/INFRA-VALIDATION-REPORT.md`.

> **Atenção (v2):** `BIP-007` (Ebola) foi validado como material de entrada em `pilot-input/BIP-007-ebola/` (narrativa `narrative_pt.md`, 90 atomic facts, zero ECP, extração de 5 PDFs registrada). Isso **NÃO autoriza execução** — ver §8.

---

## 6. Risco de contaminação de materiais

O pre-flight identificou:
- BIP-004 Genoma = SX-003, com camada interpretativa contaminada por GO-4B/GO-5A.
- BIP-007 Ebola = SX-002, legado do pipeline antigo.

Reutilização como entrada do GO-8B exige decisão explícita, pois o desenho exige novas narrativas/atomic facts sob as condições A/B/C.

---

## 7. Regras imutáveis

Após Lock:
- qualquer alteração em artefato congelado = nova versão;
- nova versão exige decisão/auditoria;
- novo hash;
- novo ciclo de Lock;
- nunca edição in-place silenciosa.

Durante hashing:
- divergência = STOP;
- não corrigir e continuar na mesma operação.

Normalização definida:
- UTF-8 sem BOM;
- LF;
- exatamente um newline final;
- whitespace preservado.

---

## 8. Próxima ação correta

**Não executar P1 ainda.**

A próxima ação é uma **decisão de governança sobre P1-C2-01**.

Depois da decisão:
1. registrar `DECIDED`;
2. verificar se a decisão é compatível com o Lock;
3. se exigir mudança do congelado, iniciar novo ciclo/versionamento;
4. se a decisão usar o JSON §6 congelado como autoridade sem alterar 02, produzir `C2_PERMUTATION.yaml` exatamente conforme a decisão;
5. validar o artefato;
6. só então avançar para P2.

---

# 9. Regra de retomada

Uma nova IA deve primeiro:
- ler este documento;
- confirmar o gate;
- confirmar o blocker;
- listar decisões `DECISION REQUIRED`;
- não executar nada irreversível.

