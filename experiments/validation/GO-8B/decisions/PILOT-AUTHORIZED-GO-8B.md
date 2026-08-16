# PILOT AUTHORIZED — GO-8B

**Data:** 2026-08-12
**Decisor:** Governança GO-8B
**Status:** **AUTHORIZED**
**Hash do manifesto:** `c55799d895a4f73888713a8538c6b9a6c5df1d7cde71c88141e16b9e9b216636`

---

## 1. Contexto

O piloto GO-8B é uma execução controlada do pipeline metodológico de reconstrução de casos históricos, utilizando apenas dados sintéticos e evitando qualquer acesso a dados experimentais reais. O piloto está estritamente limitado aos artefatos congelados 00–08 e à permutação operacional C2 (tabela §5 de `02-C2-PERMUTATION.md`), conforme decisão NC-01 e NC-04.

---

## 2. Decisão

**A governança GO-8B autoriza formalmente a execução do piloto GO-8B**, com as seguintes condições e restrições:

---

## 3. Escopo do Piloto

- **Número de casos (N):** 7 (BIP-001, BIP-002, BIP-003, BIP-004, BIP-005, BIP-006, BIP-007)
- **Condições por caso:** 3 (A, B, C)
  - **Condição A:** atomic facts (condição de cegueira A)
  - **Condição B:** atomic facts (condição de cegueira B)
  - **Condição C:** narrativa (condição não-cega)
- **Seeds por célula:** 3 (3 execuções de reconstrução independentes)
- **Total de execuções:** 7 BIPs × 3 condições × 3 seeds = **63 execuções**

---

## 4. Restrições e Limitações

### 4.1 Núcleo Congelado (00–08) — INTOCÁVEL

- Todos os artefatos congelados do núcleo metodológico permanecem imutáveis.
- Não é permitida qualquer modificação em:
  - `00-METHODOLOGY-REVISIONS.md` (versão do núcleo)
  - `01-VALIDATION-SCHEMES.md`
  - `02-C2-PERMUTATION.md`
  - `03-SYNTHETIC-TAXONOMY-C3.md`
  - `04-ANONYMIZATION-SCHEME.md`
  - `05-SIMULATION-FRAMEWORK.md`
  - `06-TESTING-PROTOCOL.md`
  - `07-REPRODUCIBILITY-REQUIREMENTS.md`
  - `08-FAILURE-MODELS.md`

### 4.2 Dados — SINTÉTICOS EXCLUSIVAMENTE

- Zero acesso a dados experimentais reais.
- Todos os dados são sintéticos, gerados conforme especificações congeladas.
- Zero transcrição ou extração de documentos históricos reais.

### 4.3 Artefatos Operacionais — Permissíveis

- **C2_PERMUTATION.yaml** — gerado conforme `02-C2-PERMUTATION.md §6` (frozen)
- **C3_TAXONOMY.yaml** — gerado conforme `03-SYNTHETIC-TAXONOMY-C3.md`
- **BIP-VAL_REPORT.yaml** — gerado conforme testes NT-01..NT-05
- **EMBEDDINGS.npy** — embeddings sintéticos gerados conforme `05-SIMULATION-FRAMEWORK.md`
- **Graphs/** — grafos reconstruídos conforme `04-ANONYMIZATION-SCHEME.md`
- **Materiais de entrada (pilot-input/)** — narrativa e atomic facts produzidos conforme especificações

### 4.4 Gate NT-05 — SUBSTITUÍDO

- O gate NT-05 (revisão humana de 3 validadores independentes) foi substituído por auditoria automatizada independente NT-05-AUTOMATED-INDEPENDENT-REVIEW.
- A auditoria foi executada em duas execuções independentes, sem divergência, com resultado **PASS**.
- O gate NT-05 substituído é considerado **VALIDATED** para os fins do piloto (sem equivalência epistemológica à revisão humana original).

---

## 5. Processo Operacional

### 5.1 Sequência do Piloto

1. **Pre-flight final** (conforme NC-07) — verificar todos os itens do checklist
2. **Geração de 63 seeds** (conforme NC-06) — registro em `SEEDS-PILOT-GO-8B.md`
3. **Execução controlada do piloto** — pipeline operacional `p_run_consolidated.py` para cada BIP/condição/seed
4. **Geração de relatórios** — outputs operacionais conforme `07-REPRODUCIBILITY-REQUIREMENTS.md`
5. **Validação dos resultados** — BIP-VAL_REPORT.yaml com NT-01..NT-05
6. **Análise e conclusão** — reporte final do piloto

### 5.2 Execução Controlada

- O pipeline operacional `p_run_consolidated.py` deve ser executado conforme a sequência de seeds.
- Cada execução deve gerar artefatos de saída no diretório `scripts/go8b/operational/` e `experiments/validation/GO-8B/pilot-output/`.
- Nenhum artefato deve ser escrito em diretórios do núcleo congelado (00–08).

### 5.3 Registros

- Cada passo do piloto deve ser registrado em `decisions/ACTION-REGISTER.md`.
- Seeds devem ser registradas em `decisions/SEEDS-PILOT-GO-8B.md`.
- Relatórios operacionais devem ser registrados com hashes SHA-256 para rastreabilidade.

---

## 6. Condições de Conclusão

O piloto GO-8B estará considerado **CONCLUÍDO** quando todos os 63 execuções forem concluídas com:
- Zero falhas no pipeline operacional
- Zero divergências entre as 3 execuções por célula
- BIP-VAL_REPORT.yaml com NT-01..NT-05 = PASS
- Todos os relatórios operacionais gerados e validados
- Pre-flight final confirmando todos os itens

---

## 7. Referências

- `decisions/NC-01-HUMAN-REVIEW-SUBSTITUTION.md` (decisão de substituir NT-05 por auditoria automatizada)
- `decisions/NT-05-AUTOMATED-INDEPENDENT-REVIEW-RESULT.md` (resultado da auditoria, NT-05 VALIDATED)
- `decisions/PILOT-AUTHORIZED-GO-8B.md` (este arquivo — autorização formal)
- `decisions/SEEDS-PILOT-GO-8B.md` (registros de seeds)
- `decisions/ACTION-REGISTER.md` (registro de ações)
- `00-METHODOLOGY-REVISIONS.md` (versão do núcleo congelado)
- `02-C2-PERMUTATION.md` §3/§4/§5/§6 (permutação operacional)
- `03-SYNTHETIC-TAXONOMY-C3.md` (taxonomia sintética)
- `04-ANONYMIZATION-SCHEME.md` (anonimização)
- `05-SIMULATION-FRAMEWORK.md` (framework de simulação)
- `06-TESTING-PROTOCOL.md` (protocolo de teste)
- `07-REPRODUCIBILITY-REQUIREMENTS.md` (requisitos de reprodutibilidade)
- `08-FAILURE-MODELS.md` (modelos de falha)
- Hash do manifesto vigente: `c55799d895a4f73888713a8538c6b9a6c5df1d7cde71c88141e16b9e9b216636`

---

**Fim da autorização. Nenhum artefato congelado alterado. Nenhum dado experimental produzido antes do pre-flight final PASS.**