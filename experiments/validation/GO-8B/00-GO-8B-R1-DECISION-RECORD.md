# GO-8B-R1 DECISION RECORD — RECOVERED/RECONSTRUCTED GOVERNANCE RECORD

**Status:** RECONSTRUCTED — PENDING GOVERNANCE AUDIT
**Tipo de documento:** RECOVERED/RECONSTRUCTED GOVERNANCE RECORD
**Data de criação (deste arquivo):** 2026-08-11
**Governance Directive:** GO-8B-R3, DECISION R3-02

---

## 1. Declaração de Proveniência (OBRIGATÓRIA)

Este documento é um **registro de governança RECONSTRUÍDO**, **não** o arquivo original.

1. **O arquivo original `00-GO-8B-R1-DECISION-RECORD.md` não foi localizado** no repositório em 2026-08-11.
2. A reconstrução foi feita **somente** a partir da auditoria GO-8B-R2 e das decisões documentadas nos artefatos 01–07 do GO-8B.
3. **Não há hash original** deste documento. Nenhum hash foi inventado.
4. **Não há commit original** deste documento. Nenhum commit foi inventado.
5. **Não há datas, assinaturas ou conteúdo histórico** além daqueles explicitamente presentes nos artefatos 01–07 e na auditoria GO-8B-R2.
6. Este registro **não declara recuperação** do arquivo original; é uma reconstrução de governança, sujeita a auditoria.

---

## 2. Decisões R1 Refletidas nos Artefatos 01–07

A auditoria GO-8B-R2 identificou as seguintes decisões R1 como **efetivamente refletidas** nos artefatos. Esta lista é derivada dos Change Logs de cada artefato e do conteúdo vigente dos arquivos.

### 2.1 Decisão R1-D1 — Correção da seed estatística (Correção 6)
- **Problema:** valor decimal incorreto divulgado anteriormente / literal inválido.
- **Decisão:** seed registrada como **dado de configuração** (`value: 1879048193`, `type: uint64`).
- **Reflexo:** `06-STATISTICAL-PROTOCOL.md` §9.1; `02-C2-PERMUTATION.md` §3 (seed C2 em uint64).
- **Status:** REFLETIDA.

### 2.2 Decisão R1-D2 — Unidade experimental = BIP/Caso (pseudorreplicação)
- **Problema:** Friedman tratava seeds/avaliadores como blocos independentes (pseudorreplicação).
- **Decisão:** unidade experimental = **BIP/Caso**; `N` = nº de BIPs válidos; seeds/avaliadores = **repetições intra-unidade**; agregação por **mediana** por `(caso, condição)`.
- **Reflexo:** `06-STATISTICAL-PROTOCOL.md` §1.3, §3, §9.1; `07-FAILURE-CRITERIA.md` §5.
- **Status:** REFLETIDA.

### 2.3 Decisão R1-D3 — C3 independente/emergente vs isomórfica ao ECP
- **Problema:** C3 era isomórfica ao ECP (cardinalidade 9, nomes derivados, mapping SYN→ECP pré-definido).
- **Decisão:** C3 torna-se **taxonomia sintética independente/emergente**; cardinalidade/nomes/hierarquia variáveis; comparação C3↔ECP **somente na fase de análise**; sem mapping SYN→ECP.
- **Reflexo:** `03-SYNTHETIC-TAXONOMY-C3.md` integral; `04-GRAPH-FROM-RECONSTRUCTION.md` §4 (T-GFR-13); `05-WL-KERNEL.md` §1, §5.
- **Status:** REFLETIDA.

### 2.4 Decisão R1-D4 — S_struct sem semântica ECP (Correção 2/3)
- **Problema:** S_struct usava nomes/leis/mapeamentos/embeddings ECP como medida de aderência.
- **Decisão:** S_struct = similaridade **topológica** via WL Subtree Kernel com **anonimização uniforme** (`label_0 = "neutral"`) em ambos os grafos; sem categorias/leis/embeddings/penalidades ECP.
- **Reflexo:** `05-WL-KERNEL.md` §3; `07-FAILURE-CRITERIA.md` §5 Nota R1.
- **Status:** REFLETIDA.

### 2.5 Decisão R1-D5 — S_sem demovido a exploratório/secundário
- **Decisão:** S_sem é **SECUNDÁRIO/EXPLORATÓRIO**; matriz contínua; Hungarian permite cross-category; sem hard constraint; não é métrica confirmatória.
- **Reflexo:** `05-WL-KERNEL.md` §4; `06-STATISTICAL-PROTOCOL.md` §1.1.
- **Status:** REFLETIDA.

### 2.6 Decisão R1-D6 — Registro completo de parâmetros do WL (Correção 5)
- **Decisão:** cada parâmetro com valor, finalidade, justificativa, tipo e se alterável pós-coleta; **proibido tuning** após observar resultados.
- **Reflexo:** `05-WL-KERNEL.md` §6.
- **Status:** REFLETIDA.

### 2.7 Decisão R1-D7 — Critérios de exclusão no formato padronizado (Correção 10)
- **Decisão:** cada critério no formato `ID → condição → ação → justificativa → momento de aplicação`; thresholds sem fundamento formal marcados `PRE-SPECIFICATION DEBT`.
- **Reflexo:** `07-FAILURE-CRITERIA.md` integral.
- **Status:** REFLETIDA.

### 2.8 Decisão R1-D8 — Remoção do status "congelado" e de hashes inventados (Correção 12)
- **Decisão:** nenhum artefato declarado FROZEN; hashes substituídos por `HASH STATUS: PENDING LOCK PROTOCOL`.
- **Reflexo:** `02`, `03`, `04`, `05` — Change Logs e status `REVISED — PENDING GOVERNANCE AUDIT`.
- **Status:** REFLETIDA.

### 2.9 Decisão R1-D9 — Eliminação da regra `p > 0.20 ⇒ equivalência`
- **Decisão:** não-significância não implica equivalência; formalizado TOST com Δ pré-registrada ou `DECISION REQUIRED`.
- **Reflexo:** `06-STATISTICAL-PROTOCOL.md` §8.
- **Status:** REFLETIDA (evoluída pela DECISION R3-03 do GO-8B-R3).

---

## 3. Pendências Registradas na Reconstrução

3.1. O arquivo original não foi localizado; qualquer documento posterior que referencie este arquivo deve tratá-lo como **reconstrução**, não como original.
3.2. A reconstrução não cria hashes, commits, assinaturas nem datas históricas.
3.3. A rastreabilidade completa (mudança difusa de cada correção) depende da **auditoria de governança** deste registro.

---

## 4. Autoria e Vigência

- **Autor da reconstrução:** auditoria GO-8B-R2 (processo documental) + governance directive GO-8B-R3.
- **Vigência:** não constitui congelamento.
- **Próximo passo:** auditoria de governança para validar ou corrigir esta reconstrução.

---

**Fim do Decision Record reconstruído.** Nenhum experimento executado. Nenhuma estatística calculada. Nenhum hash final criado.
