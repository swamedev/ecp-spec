# C-NOMENCLATURE-CORRECTION

## Correção de Nomenclatura — Critérios de Mensuração (M-REDESIGN-01)

**Data:** 2026-08-18
**Status:** CORREÇÃO NÃO INVASIVA REGISTRADA (nenhum arquivo travado por hash foi alterado)
**Tipo:** Documento de governança de nomenclatura (leitura canônica sobre documentos existentes)

---

## 1. Motivo da Correção

Existe uma **colisão de nomenclatura** entre dois usos distintos do identificador **"C3"** dentro
do programa de mensuração:

| Uso | Significado | Onde aparece |
|-----|-------------|--------------|
| **Critério de mensuração "C3"** | Robustez a pesos (ordem estável em ≥ 80% das variações de peso) | `MEASUREMENT-REDESIGN-PROPOSAL.md` §6.1; `M-REDESIGN-01-SPEC-A.md` §6.1; `MEASUREMENT-GATE-CONSOLIDATION.md` (tabela C1–C6); `PHASE-B-REPORT.md` (tabela C1–C6) |
| **Taxonomia/condição experimental "C3"** | Taxonomia sintética (12 nós, namespace SYN) testada como intervenção nos ciclos GO-8D/GO-8D-NC (condição B) | `FINAL-PROJECT-REPORT-GO-8D.md`; `M-REDESIGN-01-SPEC-A.md` §3.1 (referência SYN); `MEASUREMENT-REDESIGN-PROPOSAL.md` §4.1; arquivo travado `C3_TAXONOMY.yaml` |

A colisão torna ambígua qualquer referência futura a "C3" (por exemplo, "a C3 passou" pode
significar "o critério de robustez a pesos passou" ou "a taxonomia C3 foi validada"). Como os
documentos originais estão **travados por hash** e **não podem ser editados**, esta correção
cria um documento de leitura canônica que resolve a ambiguidade **sem tocar em nenhum arquivo
existente**.

---

## 2. Mapeamento Canônico — Critérios de Mensuração

A partir desta data, os critérios de validação da métrica `DV-REDESIGN` (família
M-REDESIGN-01) passam a ser referidos **sempre** com o prefixo **`MR-`**:

| Identificador antigo | Identificador canônico | Critério | Limiar (congelado) |
|----------------------|------------------------|----------|--------------------|
| C1 | **MR-C1** | Validade convergente | ρ ≥ 0.7 |
| C2 | **MR-C2** | Ausência de viés estrutural | bias_score < 0.5 |
| C3 | **MR-C3** | Robustez a pesos | ordem estável ≥ 80% |
| C4 | **MR-C4** | Robustez a agregação | CV ≤ 0.15 (decimal) |
| C5 | **MR-C5** | Sensibilidade (detecta degradação) | detecta degradação injetada |
| C6 | **MR-C6** | Interpretabilidade | agreement_rate ≥ 0.80 |

**Convenção:** o identificador sem prefixo **"C3"** fica **reservado exclusivamente** para a
taxonomia/condição experimental do GO-8D (taxonomia sintética SYN, 12 nós). Qualquer menção a
"C3" em contexto de mensuração de critérios deve ser interpretada como **MR-C3**.

Qualquer critério futuro da família M-REDESIGN segue a convenção `MR-C<k>` (ex.: **MR-C7**).

---

## 3. Documentos Originais Referenciados (NÃO ALTERADOS)

A correção é **não invasiva**: os documentos abaixo permanecem exatamente como estavam, com seus
hashes SHA-256 verificados nesta data (2026-08-18):

| Documento | SHA-256 (verificado) | Papel na correção |
|-----------|----------------------|-------------------|
| `M-REDESIGN-01-SPEC-A.md` | `e1fa24479636a02058b3107328320fadb3f74641e20649abd5f69484b2b18965` | Define C1–C6 (§6.1) — origem do mapeamento; também usa "C3/SYN" (§3.1) |
| `GOV-M-REDESIGN-01-GATE.md` | `ff1593d8f85fe8a5e41c2473f44af481477d03d4585c047f153001be6c19642c` | Governança do gate; critérios C1–C5 referidos |
| `MEASUREMENT-GATE-CONSOLIDATION.md` | `604f3e1aea453ca9673f0938732445709ffed684af399d00d431bfa235f4e1be` | Consolidação do gate; tabela C1–C6 |
| `PHASE-B-REPORT.md` | `66aa2ecfcf709bb13836360ea45a98b86f935b30b2467515fc31893d33c38799` | Relatório Fase B; tabela C1–C6 |
| `EVALUATION_SUMMARY.md` | `e4b1bd8c4a30da609b29cd2f22adf214026b3315c79b9c7861f90391b7ae97df` | Fase C; critério C6 (agora MR-C6) |
| `MEASUREMENT-REDESIGN-PROPOSAL.md` | `f32ef6b8b02408069461aae42b96482fe8f077e4a329d56a09945c5e92a3e486` | §6.1 define C1–C6 (origem do mapeamento) |
| `FINAL-PROJECT-REPORT-GO-8D.md` | `4d40f5c5dee0146ff3e28bf63447503196515554643381a0be20e9a956c91e3e` | Hipótese "C3" (taxonomia) — uso reservado |
| `GO-8D-NC-LOCK-MANIFEST.yaml` | (manifesto de lock, 14 artefatos) | Trava `C3_TAXONOMY.yaml` (sha256 `5ba63db7a81c454d7432873c184d2171741f8676e70d94cc538594627819bec8`) |

**Rastreabilidade:** o mapeamento desta seção refere-se **exclusivamente** a estes hashes. Se
algum destes documentos for alterado no futuro, o mapeamento desta correção deixa de ser
válido para a versão alterada — isso deve ser tratado como mudança de especificação, conforme
regra de congelamento do GOV-M-REDESIGN-01-GATE.md §7.

---

## 4. Registro da Correção

| Campo | Valor |
|-------|-------|
| **Data** | 2026-08-18 |
| **Motivo** | Colisão de nomenclatura "C3" (critério MR-C3 × taxonomia experimental C3 do GO-8D) |
| **Tipo de ação** | Não invasiva — criação de documento canônico de leitura; **nenhum arquivo travado editado** |
| **Escopo** | Nomes de critérios de mensuração; NÃO altera critérios, limiares, pesos, referências, seeds, agregadores ou regras de decisão |
| **Convenção resultante** | Critérios: `MR-C1`…`MR-C6` (+ `MR-C7` se criado). "C3" sem prefixo: exclusivamente taxonomia/condição experimental do GO-8D |
| **Documentos afetados** | Nenhum (nenhuma edição); apenas a leitura canônica de documentos existentes muda |
| **Verificação de integridade** | Hashes SHA-256 dos documentos §3 conferidos nesta data (ver §3) |

---

## 5. Declaração de Integridade

> Nenhum arquivo travado por hash foi criado, editado, movido ou removido para produzir esta
> correção. Os hashes da Seção 3 foram verificados antes e permanecem íntegros após o registro
> desta correção. Esta correção não altera critérios, limiares, pesos, referências, seeds,
> agregadores, regras de decisão, nem o estado dos ciclos (GO-8B…GO-8D-NC CLOSED/LOCKED,
> GO-8E NÃO AUTORIZADO).

---

**Assinatura:** Governança ECP
**Data:** 2026-08-18
**Base:** Lock Manifest GO-8D-NC (`9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`)