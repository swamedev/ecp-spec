# GO-8C — ACTION REGISTER (Registro de Ações)

**Data:** 2026-08-13
**Ciclo:** GO-8C — **GO-8C CLOSED (2026-08-14)** — estudo confirmatório N=12 concluído; encerramento formal aprovado pela governança.
**Regra:** nenhuma alteração em arquivos do GO-8B (CLOSED / LOCKED / FROZEN); todas as operações dentro de `experiments/validation/GO-8C/`.

---

## Ações

| ID | Descrição | Status | Artefato(s) | Validação |
|---|---|---|---|---|
| **D-01** | Decisão de governança D-01: aprovar correção da seed C2 — seed oficial `258915` (hex `0x3f363`), tabela `[1,5,6,3,7,0,4,8,2]` inalterada, inversa verdadeira `[5,0,8,3,6,1,2,4,7]`, seed antiga `11473621728585666159` → `HISTORICAL-NON-REPRODUCING` | **DECIDED** | `decisions/D-01-C2-DECISION.md` | Proposta D-01 aprovada; GO-8B intacto; referência P1-C2-01 (Opção A, GO-8B) |
| **D-01.1** | Criação do artefato corrigido do entregável 02 (seed oficial, inversa verdadeira, JSON §6 corrigido, proveniência GO-8C) | **PRODUCED** | `02-C2-PERMUTATION-CORRECTED.md` | Tabela/mapping idênticos ao GO-8B §5/§6; seed `0x3f363`; `seed_registrada_historica` → `HISTORICAL-NON-REPRODUCING` |
| **D-01.2** | Criação das cópias operacionais corrigidas em `GO-8C/scripts/` | **PRODUCED** | `scripts/C2_PERMUTATION.yaml` · `scripts/C2_PERMUTATION.json` · `scripts/p1_c2_test.py` | `seed_operacional=258915`; `seed_historica=11473621728585666159`; `inversa_verdadeira=[5,0,8,3,6,1,2,4,7]`; `derived_from: GO-8B 02-C2-PERMUTATION.md §6 (frozen), corrected in GO-8C` |
| **D-01.3** | Execução da suíte de testes `p1_c2_test.py` no GO-8C | **ALL PASS** (7/7) | `scripts/p1_c2_test.py` · `decisions/D-01-C2-VALIDATION.md` | T-C2-01 (seed oficial reproduz SS5) PASS; T-C2-08 (regressão seed antiga não reprodutora) PASS; T-C2-09 (oficialidade YAML) PASS; TOTAL 7 PASS 0 FAIL |
| **D-01.4** | Registro formal do resultado da validação | **PRODUCED** | `decisions/D-01-C2-VALIDATION.md` | ALL PASS (7/7); ambiente Python 3.11.9 / numpy 1.26.4 / PyYAML 6.0.2; GO-8B intacto |
| **D-02** | Decisão de governança D-02: formalizar o uso de **CAT** como namespace operacional das condições A/C (Opção 2) — NULL permanece não processável (04 §1.1); sem equivalência NULL≡CAT nem CAT≡SYN/ECP; Opção 3 registrada como roadmap | **DECIDED** | `D-02-C4-NULL-PROPOSAL.md` · `decisions/D-02-C4-NULL-DECISION.md` | Proposta D-02 aprovada (Opção 2); parser intocado; T-GFR-18 permanece PASS; GO-8B intacto |
| **D-02.1** | Criação da suíte de testes de namespace (T-D-02-01..03) e registro do mapeamento operacional no artefato operacional | **PRODUCED** | `scripts/test_d02_namespace.py` · `scripts/C2_PERMUTATION.yaml` · `.json` (campo `namespace_operacional`) | `namespace_operacional = {A: CAT, B: SYN, C: CAT}` + `namespace_note` (sem equivalências NULL≡CAT/CAT≡SYN/ECP) |
| **D-02.2** | Execução da suíte de testes `test_d02_namespace.py` no GO-8C | **ALL PASS** (3/3) | `scripts/test_d02_namespace.py` · `decisions/D-02-C4-NULL-VALIDATION.md` | T-D-02-01 (NULL rejeitado) PASS; T-D-02-02 (CAT produz grafo) PASS; T-D-02-03 (A/B/C = CAT/SYN/CAT) PASS; regressão D-01 7/7 PASS |
| **D-03** | Decisão de governança D-03: substituição **parcial** de NT-05 (Alternativa B) — determinístico automatizado + gate semântico mínimo de **1 revisor humano independente** com rubrica pré-registrada; critério "≤ 0 violações semânticas não capturadas"; sem equivalência com revisão humana | **DECIDED** | `D-03-NT05-PROPOSAL.md` · `decisions/D-03-NT05-DECISION.md` | Proposta D-03 aprovada (Alternativa B); escopo limitado ao NT-05; GO-8B intacto |
| **D-03.1** | Criação do protocolo de revisão semântica mínima | **PRODUCED** | `decisions/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` | 1 revisor humano independente; rubrica pré-registrada (Cat. 1 isolamento SYN / Cat. 2 paráfrase ECP / Cat. 3 viés estrutural); critério ≤ 0; formulário objetivo por item |
| **D-03.2** | Harmonização do artefato BIP-VAL do GO-8C | **PRODUCED** | `scripts/BIP-VAL_REPORT.yaml` | `NT-05: SUBSTITUTED_PARTIAL (1 human reviewer)`; `verdict: PASS_PENDING_HUMAN_REVIEW`; NT-01..04 PASS preservados; FINDING-BIP-VAL-01 preservado; GO-8B intocado |
| **D-03.3** | Criação e execução da suíte de testes `test_d03_nt05.py` no GO-8C | **ALL PASS** (3/3) | `scripts/test_d03_nt05.py` · `decisions/D-03-NT05-VALIDATION.md` | T-D-03-01 (NT-01..04 PASS) PASS; T-D-03-02 (protocolo exige 1 revisor humano independente) PASS; T-D-03-03 (BIP-VAL reflete substituição parcial) PASS; regressões D-01 7/7 e D-02 3/3 PASS |
| **D-03.4** | Preparação do pacote de revisão semântica mínima do NT-05 (Alternativa B) — SEM executar a revisão | **PRODUCED** | `review/README-REVIEW.md` · `review/protocol/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` (cópia somente leitura) · `review/REVIEW-ITEMS.md` · `review/REVIEW-FORM.md` | Pacote pronto para revisor independente; 12 categorias C3 (P-1) + 14 arquivos de materiais (S-1..S-7, narrativa+atomic facts); BIP-003-warpspeed fora do escopo; GO-8B intocado; `BIP-VAL_REPORT.yaml` NÃO atualizado |
| **D-03.5** | Atualização D-03 (painel de IAs): decisão e protocolo revisados para **painel de 2 IAs independentes em três abas separadas com acesso restrito**; formulários por via (MODEL-1/MODEL-2); limitação registrada | **DECIDED/PRODUCED** | `decisions/D-03-NT05-DECISION.md` · `decisions/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` · `review/REVIEW-FORM-MODEL-1.md` · `review/REVIEW-FORM-MODEL-2.md` | Substituição "1 revisor humano" → painel de 2 IAs (abas separadas); acesso restrito a `review/`; unanimidade PASS; divergência = STOP; sem votação por maioria; agente executor NÃO participa como revisor |
| **D-03.6** | Formalização do método de três abas e preparação do ambiente de revisão | **PRODUCED** | `review/REVIEW-PANEL-PROCEDURE.md` · `review/materials/` (15 cópias de leitura) · `review/REVIEW-ITEMS.md` (caminhos relativos a `review/`) · `review/README-REVIEW.md` (atualizado) | Passo a passo das três abas; prompts padrão (§4.1/§4.2); modelos sugeridos (GLM-4.5 Flash / Nemotron 3 Ultra, com substituição permitida); itens acessíveis localmente em `review/materials/`; originais GO-8B intocados; revisão NÃO executada |
| **D-03.7** | Correção da taxonomia C3 do GO-8C após revisão semântica (Opção 1): substituição das definições de **SYN-001** e **SYN-012** por redação neutra não parafrástica | **CORRECTED** | `scripts/C3_TAXONOMY.yaml` (criado; cópia corrigida do GO-8B) · registro em `decisions/ACTION-REGISTER.md` | SYN-001 "Atividade elementar" → "Procedimento basico" (remove paráfrase de "Funcao"); SYN-012 "Ajuste local" → "Resposta do comportamento" (remove paráfrase de "Adaptacao"); estrutura/arestas/metadados idênticos ao GO-8B; verificação léxica+semântica limpa; GO-8B intocado |
| **D-03.8** | Consolidação da D-03 após painel de revisão semântica independente (unanimidade PASS) | **DONE** | `decisions/D-03-NT05-PANEL-RESULT.md` · `scripts/BIP-VAL_REPORT.yaml` (atualizado) · `scripts/test_d03_nt05.py` (atualizado) · `TODO-GO-8C.md` (D-03 DONE) · `decisions/ACTION-REGISTER.md` | Painel: Revisor 1 (GLM 4.5 Flash) PASS + Revisor 2 (Gemini 3.6 Flash) PASS — 0 violações em 26 itens (12 primários + 14 secundários); `NT-05: PASS_AI_PANEL (unanimous)`; `verdict: PASS`; NT-05 parcial VALIDADO; limitação declarada (sem equivalência com revisão humana); D-03 DONE |
| **D-04** | Decisão de governança D-04: aprovar o desenho do estudo confirmatório **N=12** (proposta `D-04-N12-PROPOSAL.md`) — lista dos 12 BIPs; re-execução dos 7 BIPs (nenhum dado do GO-8B reutilizado); Go/No-Go ≥10 de 12 (salvo pré-registro); produção dos 5 novos autorizada após plano de trabalho; NT-05 estendido (painel D-03) | **DECIDED** | `D-04-N12-PROPOSAL.md` · `decisions/D-04-N12-DECISION.md` | Proposta D-04 aprovada (5 decisões formalizadas); execução experimental NÃO autorizada; GO-8B intacto |
| **D-04.1** | Criação da estrutura de diretórios do estudo N=12 e cópia dos 7 BIPs existentes para `study-input/` (proveniência registrada, originais intocados) | **PRODUCED** | `study-input/` (BIP-001..007, 71 arquivos) · `study-output/` (criado) · `study-input/README-STUDY-INPUT.md` | 7 BIPs copiados com hashes SHA-256 idênticos ao GO-8B (ALL COPIES INTACT: True); BIP-003-warpspeed não copiado (fora do escopo); GO-8B intocado |
| **D-04.2** | Aprovação do plano de trabalho (D-04-N12-WORKPLAN.md) para produção dos 5 novos BIPs (008–012) | **DECIDED** | `decisions/D-04-N12-DECISION.md` · `D-04-N12-WORKPLAN.md` | P1–P4 autorizados (coleta → validação); execução experimental NÃO autorizada; GO-8B intocado |
| **D-04.3** | P1–P2 dos 5 novos BIPs: coleta, indexação e proveniência de fontes brutas primárias | **PRODUCED** | `study-input/BIP-008..012/sources/raw/` (10 PDFs/HTM) · `sources/00-index.md` · `sources/01-origem-dos-documentos.md` | 10 fontes brutas baixadas; checksums SHA-256 registrados; proveniência EI/SC-5 por BIP; BIP-010 WSDoT PDF escaneado substituído por fonte de texto (htm) |
| **D-04.4** | P3: produção de narrativa (cond C) e atomic facts (cond A/B), zero-ECP, para os 5 novos BIPs | **PRODUCED** | `study-input/BIP-008..012/narrative/01-narrativa-original.md` · `atomic-facts/02-atomic-facts.md` · `README.md` | 5 narrativas + 5 listas de atomic facts; 0 termos ECP; rastreabilidade a refs por fato/parágrafo |
| **D-04.5** | P4: validação lexical (52 termos ECP) e rastreabilidade dos 5 novos BIPs | **ALL PASS (5/5)** | `scripts/validate_bip.py` (temp) · `study-input/BIP-008..012/` | LEXICON PASS + TRACE PASS em 5/5 BIPs (008, 009, 010, 011, 012); correções aplicadas e revalidadas; GO-8B intocado |
| **D-04.6** | Preparação do pacote de revisão semântica **NT-05 estendido** aos 5 novos BIPs — SEM executar a revisão | **PRODUCED** | `review/nt05-extended/protocol/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` (cópia somente leitura) · `review/nt05-extended/materials/` (12 cópias de leitura) · `review/nt05-extended/REVIEW-ITEMS.md` · `review/nt05-extended/REVIEW-FORM-MODEL-1.md` · `review/nt05-extended/REVIEW-FORM-MODEL-2.md` | Pacote pronto para o painel D-03 (2 IAs independentes); 22 itens (12 categorias C3 + 10 materiais: 5 narrativas + 5 atomic facts); ALL COPIES INTACT: True (12/12); formulários em branco aguardando revisores; GO-8B e materiais originais GO-8C intocados |
| **D-04.7** | Consolidação do **NT-05 estendido** após divergência no painel (Revisor 1 REJEITADO / Revisor 2 PASS) — aceite da divergência com justificativa (Opção B1) | **DONE** | `decisions/D-04-NT05-DIVERGENCE-ANALYSIS.md` · `scripts/BIP-VAL_REPORT.yaml` (atualizado) · `TODO-GO-8C.md` (NT-05 extended DONE) · `decisions/ACTION-REGISTER.md` | Revisor 1 (GLM) falso positivo: labels `Funcao`/`Adaptacao` não constam na lista ECP (52 termos), são vocabulário FRAM/STAMP permitido por N-3, NT-01 determinístico = 0 hits, D-03.7/D-03.8 já resolveram definições/labels; `NT-05 extended: PASS_AI_PANEL (divergence justified)`; `verdict: PASS`; divergência registrada para auditoria; GO-8B e materiais intocados |
| **D-04.8** | Criação do **pré-registro N=12** do GO-8C (replicando 06/07/08 do GO-8B, com N=12) — SEM geração de seeds nem Lock | **PRODUCED** | `08-PRE-REGISTRATION-N12.md` · `decisions/ACTION-REGISTER.md` | Desenho fixado: N=12, 3 condições (A/B/C), 3 seeds por célula, 12×3×3=108 execuções; S_struct primária + S_sem exploratória; Friedman (df=2, α=0.05) → Wilcoxon bilateral + Holm → W/r_rb/Cliff δ; bootstrap B=10.000; TOST não vigente; Go/No-Go **≥ 10 de 12**; gate de autorização = aprovação do pré-registro → Lock GO-8C → execução; consistência com GO-8B verificada (§13); seed C2 corrigida (D-01); namespace operacional (D-02); seeds/hashes PENDING LOCK PROTOCOL |
| **D-04.9** | Aprovação formal do **pré-registro N=12** pela governança GO-8C | **DECIDED** | `decisions/D-04-PREREG-N12-APPROVED.md` · `08-PRE-REGISTRATION-N12.md` | `08-PRE-REGISTRATION-N12.md` APROVADO (2026-08-14); adaptações confirmadas corretas: N=12 (D-04), Go/No-Go ≥10 de 12 (D-04), seed C2 `258915` (D-01), namespace A→CAT/B→SYN/C→CAT (D-02); Lock GO-8C, seeds e execução experimental **NÃO autorizados** nesta decisão; GO-8B intocado |
| **D-04.10** | **Lock do GO-8C** executado (autorização da governança 2026-08-14): normalização in-place dos textos do GO-8C (UTF-8 sem BOM, LF, newline final) + hash SHA-256 de 151 artefatos + manifesto e Lock Record gerados | **LOCKED** | `GO-8C-LOCK-MANIFEST.yaml` · `GO-8C-LOCK-RECORD.yaml` | Manifesto: 151 arquivos (108 study_material · 12 review_artifact · 11 decision_record · 8 docs raiz · 7 scripts GO-8C · 5 engine/reprodutibilidade); hash do manifesto `f59591a0…2027c0`; hash do pré-registro `4cdacb11…bf8ead`; validação independente re-hash 0 mismatch; GO-8B intocado; seeds e execução (108 reconstruções) permanecem BLOQUEADOS |
| **D-04.11** | **Correção do formato do BIP-009** (autorização da governança após STOP/investigação): conversão do `02-atomic-facts.md` de tabela markdown → `## Fatos` + lista numerada (72 fatos, texto/refs/ordem preservados byte-a-byte) + **re-Lock** do artefato + registro do gate gap | **CORRECTED / RELOCKED** | `study-input/BIP-009-chernobyl/atomic-facts/02-atomic-facts.md` (sha256 `b1142dfa…6195f`) · `GO-8C-LOCK-MANIFEST.yaml` (atualizado) · `GO-8C-LOCK-RECORD.yaml` (atualizado) · `decisions/D-04-GATE-GAP-ENGINE-PARSEABILITY.md` | Conversão verificada: 72 fatos, 0 mismatch de texto/ref/ordem, parser do engine parseia 72/72; re-hash do Lock **PASS** (0 mismatch, record↔manifest consistent); BIP-009 A/B re-executado e aprovado; GO-8B e demais arquivos do Lock intocados |
| **D-04.12** | **Análise estatística do estudo N=12** (autorização da governança 2026-08-14, pós-Lock): execução do script estatístico congelado (`go8b_statistical_analysis.py`) sobre os dados finais (108 execuções válidas) + geração do relatório | **DONE** | `study-output/stats_input_sstruct_n12.csv` · `study-output/STATISTICAL-REPORT-N12.md` | Friedman χ²=9.7826 df=2 p=0.0075 (REJEITA H₀); W=0.4076; post-hoc: B>C significativo após Holm (p=0.0093); A vs B não significativo pós-Holm (p=0.0537, direção B>A); sensibilidades todas p<0.05; TOST não executado; **Go/No-Go: GO (12/12 ≥ 10)**; Lock GO-8C íntegro |
| **D-04.13** | **Encerramento formal do ciclo GO-8C** (aprovação da governança 2026-08-14): relatório final + pacote de encerramento + registro de CLOSED | **CLOSED** | `FINAL-PROJECT-REPORT-GO-8C.md` · `GO-8C-CLOSURE-PACKAGE.zip` · `decisions/ACTION-REGISTER.md` · `TODO-GO-8C.md` | **GO — concluído (12/12 ≥ 10)**; relatório final com interpretação (B>C robusto; A vs B inconclusivo/limítrofe) e limitações; pacote zip com relatório, dados (108 execuções), relatório estatístico, Lock (manifest+record) e 13 decisões; Lock GO-8C validado PASS (0 mismatch); GO-8B intacto |

---

## Detalhe D-01 — Decisão de Governança (DECIDED)

- **Decisor:** Governança GO-8C
- **Decisão:** aprovar correção da seed C2 conforme proposta D-01 (`D-01-C2-PROPOSAL.md`).
- **Conteúdo:**
  - Seed oficial: `258915` (hex `0x3f363`) — reproduz a tabela congelada sob PCG64 + Fisher-Yates.
  - Tabela de permutação `[1, 5, 6, 3, 7, 0, 4, 8, 2]` **inalterada**.
  - Inversa verdadeira corrigida: `[5, 0, 8, 3, 6, 1, 2, 4, 7]`.
  - Seed antiga `11473621728585666159` → **`HISTORICAL-NON-REPRODUCING`** no contexto do GO-8C.
- **Referência GO-8B:** `P1-C2-01` resolvido no GO-8B como **Opção A**; GO-8C corrige definitivamente a dívida (vínculo seed→permutação).
- **Restrições:** nenhum arquivo do GO-8B alterado; nenhum Lock/manifesto gerado nesta etapa.

## Detalhe D-01.2 — Artefatos Operacionais (PRODUCED)

- `scripts/C2_PERMUTATION.yaml`:
  - `seed_operacional.value = 258915` (status OFFICIAL, hex `0x3f363`)
  - `seed_historica.value = 11473621728585666159` (status `HISTORICAL-NON-REPRODUCING`)
  - `inversa_verdadeira = [5, 0, 8, 3, 6, 1, 2, 4, 7]`
  - `derived_from: GO-8B 02-C2-PERMUTATION.md §6 (frozen), corrected in GO-8C`
- `scripts/C2_PERMUTATION.json`: correspondente ao YAML.
- `scripts/p1_c2_test.py`: suíte de testes GO-8C (T-C2-01..05, T-C2-08, T-C2-09).

## Detalhe D-01.3 — Validação (ALL PASS)

- Comando: `python p1_c2_test.py` (workdir `experiments/validation/GO-8C/scripts/`).
- Resultado: **TOTAL: 7 PASS: 7 FAIL: 0 — ALL PASS: True**.
- T-C2-01 (determinismo seed oficial): PASS.
- T-C2-08 (regressão — seed antiga NÃO reproduz tabela): PASS (documental, `HISTORICAL-NON-REPRODUCING`).
- T-C2-09 (oficialidade do YAML — `seed_operacional=258915`, inversa correta): PASS.
- Evidência completa: `decisions/D-01-C2-VALIDATION.md`.

## Detalhe D-02 — Decisão de Governança (DECIDED, Opção 2)

- **Decisor:** Governança GO-8C
- **Decisão:** formalizar o uso de **CAT** (C2) como namespace operacional das condições **A** e **C**; condição **B** usa **SYN** (C3).
- **Justificativa:** NULL é rejeitado pelo parser (`graph_from_reconstruction.py:84-85`) e a especificação congelada 04 §1.1 declara NULL não processável; CAT-XX são rótulos opacos que preservam a cegueira; continuidade com o piloto GO-8B e com N=12.
- **Limites explícitos:**
  - Parser `graph_from_reconstruction.py` **inalterado**; T-GFR-18 permanece PASS.
  - **NULL continua significando "não processável"**.
  - **Sem equivalência NULL ≡ CAT** e **sem equivalência CAT ≡ SYN/ECP** (CAT = representação operacional, não equivalência semântica).
  - Decisão vale para o GO-8C e para o estudo confirmatório derivado (N=12).
  - **Opção 3 (sonda de viabilidade para NULL)** registrada como roadmap, sem prazo e sem execução; mudança futura exigirá novo ciclo decisório e nova validação.
- **Ressalva:** D-02 **não desbloqueia automaticamente** D-03/D-04; cada dívida é decisão independente. N=12 só será fixado após desenho operacional estabilizado.

## Detalhe D-02.1 — Artefatos Operacionais (PRODUCED)

- `scripts/test_d02_namespace.py`: T-D-02-01 (NULL rejeitado com NAMESPACE_MIX), T-D-02-02 (CAT produz grafo válido), T-D-02-03 (A/B/C = CAT/SYN/CAT no YAML).
- `scripts/C2_PERMUTATION.yaml` / `.json`: adicionados `namespace_operacional: {A: CAT, B: SYN, C: CAT}` e `namespace_note` (sem equivalências NULL≡CAT / CAT≡SYN/ECP).

## Detalhe D-02.2 — Validação (ALL PASS)

- Comando: `python test_d02_namespace.py` (workdir `experiments/validation/GO-8C/scripts/`).
- Resultado: **TOTAL: 3 PASS: 3 FAIL: 0 — ALL PASS: True**.
- T-D-02-01 (NULL → NAMESPACE_MIX): PASS.
- T-D-02-02 (CAT → grafo válido, rótulos CAT-XX): PASS.
- T-D-02-03 (namespace_operacional A/B/C = CAT/SYN/CAT): PASS.
- Regressão: `python p1_c2_test.py` → **ALL PASS (7/7)** (YAML editado sem regressão).
- Evidência completa: `decisions/D-02-C4-NULL-VALIDATION.md`.

## Detalhe D-03 — Decisão de Governança (DECIDED, Alternativa B)

- **Decisor:** Governança GO-8C
- **Decisão:** substituição **parcial** do requisito humano NT-05:
  - Componentes determinísticos (NT-01..04 e suítes operacionais) permanecem **automatizados**.
  - **Gate semântico mínimo humano mantido:** **1 revisor independente**, com rubrica pré-registrada.
  - **Critério de aprovação:** ≤ 0 (nenhuma) violação semântica não capturada pelos testes automatizados; qualquer ocorrência → correção e revalidação.
  - Harmonizar `BIP-VAL_REPORT.yaml` do GO-8C: `NT-05: SUBSTITUTED_PARTIAL (1 human reviewer)`; `verdict: PASS_PENDING_HUMAN_REVIEW` (até a revisão ser executada).
- **Escopo:** exclusivamente NT-05; não altera outros gates, métricas, critérios de caso ou Go/No-Go.
- **Limites explícitos:** **sem equivalência** auditoria automatizada × revisão humana; NENHUM arquivo do GO-8B alterado; D-03 não desbloqueia automaticamente D-04.
- **Próximo passo pendente (etapa subsequente):** execução da revisão semântica humana (1 revisor independente); após aprovação com zero violações, `verdict` → `PASS`.

## Detalhe D-03.1 — Protocolo de Revisão Semântica Mínima (PRODUCED)

- `decisions/NT-05-SEMANTIC-REVIEW-PROTOCOL.md`: objetivo (detectar contaminação conceitual por paráfrase não capturada por checks lexicais); escopo (SYN-001..SYN-012 + amostra/ total dos materiais de entrada); rubrica pré-registrada (Cat. 1 violação de isolamento SYN; Cat. 2 paráfrase de termo ECP; Cat. 3 viés estrutural que comprometa a cegueira); critério ≤ 0; formulário objetivo com veredito por item; cegueira/independência do revisor.

## Detalhe D-03.2 — BIP-VAL do GO-8C harmonizado (PRODUCED)

- `scripts/BIP-VAL_REPORT.yaml`: `nt05_mode: SUBSTITUTED_PARTIAL`; `NT-05: SUBSTITUTED_PARTIAL (1 human reviewer)`; `verdict: PASS_PENDING_HUMAN_REVIEW`; `verdict_note` e `nt05_mode_note` registram a **não equivalência**; NT-01..04 PASS preservados; FINDING-BIP-VAL-01 preservado (nota de harmonização GO-8C); GO-8B intocado.

## Detalhe D-03.3 — Validação (ALL PASS)

- Comando: `python test_d03_nt05.py` (workdir `experiments/validation/GO-8C/scripts/`).
- Resultado: **TOTAL: 3 PASS: 3 FAIL: 0 — ALL PASS: True**.
- T-D-03-01 (NT-01..04 continuam PASS): PASS.
- T-D-03-02 (protocolo exige 1 revisor humano independente): PASS.
- T-D-03-03 (BIP-VAL_REPORT.yaml reflete substituição parcial): PASS.
- Regressões: `python p1_c2_test.py` → **ALL PASS (7/7)**; `python test_d02_namespace.py` → **ALL PASS (3/3)**.
- Evidência completa: `decisions/D-03-NT05-VALIDATION.md`.

## Detalhe D-03.4 — Pacote de Revisão Semântica (PRODUCED, sem execução)

- A governança aprovou a etapa de implementação (D-03) e determinou a execução da revisão semântica mínima; foi **preparado o pacote** para o revisor independente (humano ou agente com contexto limpo).
- Conteúdo de `review/`:
  - `README-REVIEW.md` — explica o que é a revisão (Alternativa B), instruções ao revisor, rubrica resumida, condições de cegueira/independência e escopo de escrita (somente `review/`).
  - `protocol/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` — cópia **somente leitura** do protocolo.
  - `REVIEW-ITEMS.md` — lista de itens com caminhos relativos: alvo primário = 12 categorias `SYN-001..012` (`scripts/go8b/operational/C3_TAXONOMY.yaml`, somente leitura); alvo secundário = 14 arquivos de materiais (narrativas + atomic facts dos BIP-001..007, exceto BIP-003-warpspeed que só tem `sources/`).
  - `REVIEW-FORM.md` — formulário de evidências: cabeçalho (hash anônimo, data, cobertura, declaração de cegueira), veredito por item (P-1.a..l; S-1a..S-7b) e veredito global (PASS/REJEITADO; regra ≤ 0 violações).
- **A revisão NÃO foi executada** — formulário permanece vazio, aguardando revisor independente.
- **`BIP-VAL_REPORT.yaml` do GO-8C NÃO foi atualizado** nesta etapa; será atualizado apenas após a entrega e análise do formulário.
- Nenhum arquivo do GO-8B alterado; nenhum Lock gerado.

## Detalhe D-03.5 — Atualização para Painel de IAs (DECIDED/PRODUCED)

- A governança reconheceu a **indisponibilidade de revisor humano** e formalizou o gate semântico como **painel de 2 IAs independentes**:
  - Substituído "1 revisor humano independente" por "painel de 2 IAs independentes (abas separadas) com acesso restrito".
  - **Critério:** AMBAS retornam PASS em todas as categorias, sem nenhuma violação; **divergência = STOP**; proibida votação por maioria.
  - **Limitação registrada:** *"NT-05 substituído por painel de IAs independentes por indisponibilidade humana. Não há equivalência epistemológica com revisão humana."*
  - **Agente executor NÃO participa como revisor** (atua apenas na preparação/consolidação).
- Artefatos: `decisions/D-03-NT05-DECISION.md` (atualizado), `decisions/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` (atualizado), `review/REVIEW-FORM-MODEL-1.md` e `review/REVIEW-FORM-MODEL-2.md`.

## Detalhe D-03.6 — Ambiente de Revisão em Três Abas (PRODUCED)

- **`review/REVIEW-PANEL-PROCEDURE.md`:** formaliza o método de **três abas separadas** (Executor + Revisor 1 + Revisor 2); papéis (executor não revisa); passos; modelos sugeridos (GLM-4.5 Flash / Nemotron 3 Ultra; substituição por outro modelo de arquitetura/provedor distinto se indisponível); **prompts padrão** (§4.1 Revisor 1 / §4.2 Revisor 2) com restrição de leitura; salvamento e comparação dos formulários; regras de governança (unanimidade, STOP, acesso restrito).
- **`review/materials/`:** **15 cópias de leitura** — `C3_TAXONOMY.yaml` + narrativa/atomic facts dos BIPs 001..007 (14 arquivos) — para que os revisores **não precisem acessar outras pastas**. BIP-003-warpspeed excluído (resíduo vazio). **Originais GO-8B não alterados.**
- **`review/REVIEW-ITEMS.md`:** caminhos atualizados para **relativos a `review/`** (itens em `review/materials/`), com nota de identidade inequívoca do BIP-003 (OWS).
- **`review/README-REVIEW.md`:** atualizado (método de três abas, acesso restrito, conteúdo do pacote).
- **Revisão NÃO executada** — formulários vazios; `BIP-VAL_REPORT.yaml` (GO-8C) não atualizado; GO-8B intocado.

## Detalhe D-03.7 — Correção da Taxonomia C3 (CORRECTED, Opção 1)

- **Motivo:** a revisão semântica independente (painel de 2 IAs) identificou **2 violações de Categoria 2 (paráfrase de termo ECP)** nas definições do GO-8C C3:
  - **SYN-001:** "Atividade elementar" → parafraseia **"Funcao"** (termo ECP/FRAM).
  - **SYN-012:** "Ajuste local" → parafraseia **"Adaptacao"** (termo ECP).
- **Decisão da governança:** **Opção 1** — corrigir as definições e revalidar.
- **Substituições aplicadas (somente `definition`):**
  - **SYN-001:** `Atividade elementar que transforma entradas em saidas dentro de um processo sociotecnico, conforme FRAM.` → `Procedimento basico que transforma entradas em saidas dentro de um processo sociotecnico, conforme FRAM.` (descarta "atividade", sinônimo direto de "funcao"; "procedimento" é semântica neutra de unidade elementar).
  - **SYN-012:** `Ajuste local do comportamento das funcoes frente a condicoes variantes, tipico de sistemas resilientes.` → `Resposta do comportamento das funcoes frente a condicoes variantes, tipico de sistemas resilientes.` (descarta "ajuste", sinônimo direto de "adaptacao"; "resposta" descreve o comportamento sem paráfrase do termo ECP).
- **Artefato:** criado `scripts/C3_TAXONOMY.yaml` (GO-8C) como cópia corrigida do GO-8B (padrão C2_PERMUTATION); fonte congelada `scripts/go8b/operational/C3_TAXONOMY.yaml` **intocada**; cópia de leitura `review/materials/C3_TAXONOMY.yaml` preservada como evidência da versão revisada.
- **Verificação (script `verify_c3_fix.py`):**
  - Nós 12/12, arestas 13/13, chaves de topo, ordem de nós, `parent_ids`, `source_refs` e metadados **idênticos** ao GO-8B.
  - `changed definitions: ['SYN-001', 'SYN-012']` — **somente as 2 definições** foram alteradas.
  - **Léxica:** nenhuma nova ocorrência de termos ECP flagrados ("atividade", "ajuste") nas definições; palavras remanescentes em SYN-012 ("funcoes", "comportamento", "sistemas", "resiliente") já existiam antes e são vocabulário de domínio FRAM, não gatilhos de paráfrase.
  - **Semântica básica:** conjuntos de sinônimos de "Funcao" (atividade/operacao/acao/tarefa) e "Adaptacao" (ajuste/modificacao/alteracao/mudanca/adequacao) **sem ocorrência** nas novas definições (SYN-001 e SYN-012 ambos `adapt-syn: []`; SYN-001 `funcao-syn: []`).
- **Status:** **CORRECTED** — pronto para reexecução da revisão semântica (painel de 2 IAs, três abas) e posterior atualização do `BIP-VAL_REPORT.yaml` (GO-8C) apenas após aprovação com zero violações.

## Detalhe D-03.8 — Consolidação da D-03 (DONE)

- **Painel de revisão semântica independente (executado em abas novas com contexto limpo, lendo somente `review/materials/` atualizados):**
  - **Revisor 1 (GLM 4.5 Flash):** **PASS** — 0 violações.
  - **Revisor 2 (Gemini 3.6 Flash):** **PASS** — 0 violações.
  - **Unanimidade PASS em 26 itens** (12 primários P-1.a..l + 14 secundários S-1a..S-7b).
- **Resultado formal:** `decisions/D-03-NT05-PANEL-RESULT.md` (data 2026-08-14; tipo: resultado de painel de revisão semântica; modelos GLM 4.5 Flash / Gemini 3.6 Flash; critério unanimidade PASS; limitação declarada — revisão por painel de IAs independentes, sem revisão humana; conclusão: **NT-05 parcial do GO-8C VALIDADO**).
- **`scripts/BIP-VAL_REPORT.yaml` (GO-8C) atualizado:**
  - `NT-05: PASS_AI_PANEL (unanimous)`; `verdict: PASS`.
  - `reviewers`: `revisor_1_glm_4.5_flash` + `revisor_2_gemini_3.6_flash`.
  - `nt05_mode_note` e `verdict_note` atualizados (limitação registrada; referência ao PANEL-RESULT).
- **`scripts/test_d03_nt05.py` atualizado** para o estado consolidado (T-D-03-02: painel de 2 IAs; T-D-03-03: `PASS_AI_PANEL (unanimous)` + `verdict PASS` + 2 revisores): **ALL PASS (3/3)**.
- **`TODO-GO-8C.md`:** D-03 → **DONE** (CONSOLIDATED).
- **GO-8B intocado** (nenhum arquivo alterado; apenas os arquivos congelados mantêm a versão original das definições, conforme evidência histórica).
- **D-04 (N=12) NÃO iniciado** — permanece `PENDING GOVERNANCE REVIEW`, sem nenhuma implementação ou alteração.

## Detalhe D-04 — Decisão da governança (DECIDED)

- **DECISION D-04 (N=12)** criada em `decisions/D-04-N12-DECISION.md` (2026-08-14).
- **5 decisões formalizadas:** (1) lista dos 12 BIPs aprovada; (2) **re-execução dos 7 BIPs** (materiais copiados, **nenhum dado do GO-8B reutilizado** como observação); (3) **Go/No-Go ≥ 10 de 12** casos válidos (pré-registro prevalece em caso de conflito); (4) produção dos 5 novos materiais autorizada **após aprovação do plano de trabalho**; (5) **NT-05 estendido** (painel D-03, mesmos critérios/modelos).
- Execução experimental (108 reconstruções) **NÃO autorizada** nesta decisão.

## Detalhe D-04.1 — Estrutura e cópia dos 7 BIPs (PRODUCED)

- Criados `experiments/validation/GO-8C/study-input/` e `study-output/`.
- **7 BIPs copiados** de `GO-8B/pilot-input/` → `study-input/` (BIP-001-deepwater, BIP-002-hyatt, BIP-003-ows, BIP-004-genoma, BIP-005-evergiven, BIP-006-i35w, BIP-007-ebola — 71 arquivos).
- **Verificação:** SHA-256 de cada arquivo vs. origem → **ALL COPIES INTACT: True** (originais GO-8B intocados).
- **BIP-003-warpspeed não copiado** (diretório residual vazio; fora do escopo).
- Proveniência registrada em `study-input/README-STUDY-INPUT.md` (`derived_from: GO-8B pilot-input (frozen), copied in GO-8C (D-04)`).

## Detalhe D-04.2 — Plano de trabalho dos 5 novos BIPs (PROPOSTA)

- **`D-04-N12-WORKPLAN.md`** (2026-08-14) — plano proposto para produção de BIP-008..012.
- Estrutura confirmada (idêntica ao P5/GO-8B); fontes-alvo por BIP; fases P0–P5; cronograma 7 dias úteis (produção 5–8 dias); critérios de qualidade e gate de autorização.
- **Aguardando aprovação da governança** para executar P1–P4 (coleta → validação).

## Detalhe D-04.2 — Aprovação do plano de trabalho (DECIDED)

- **Decisor:** Governança GO-8C
- **Decisão:** aprovar `D-04-N12-WORKPLAN.md` e autorizar a execução de **P1–P4** (coleta → validação) para os 5 novos BIPs (008–012).
- **Escopo autorizado:** produção de materiais apenas; **execução experimental (108 reconstruções) permanece NÃO autorizada**.
- **Limites:** nenhum arquivo do GO-8B alterado; todos os escritos em `study-input/BIP-008..012/`.

## Detalhe D-04.3 — P1–P2: coleta e indexação das fontes (PRODUCED)

- **10 fontes brutas primárias baixadas** e registradas em `study-input/BIP-008..012/sources/` (checksums SHA-256 em cada `00-index.md`; proveniência EI/SC-5 em cada `01-origem-dos-documentos.md`):
  - BIP-008 (Apollo 13): `nasa-01-a13-mission-report.pdf` (Mission Report MSC-02654) · `nasa-02-a13-review-board.pdf` (Review Board Report).
  - BIP-009 (Chernobyl): `iaea-02-insag1.pdf` (INSAG-1, 1986) · `iaea-01-insag7.pdf` (INSAG-7, 1992).
  - BIP-010 (Tacoma Narrows): `caltech-01-tacoma.pdf` · `wsdot-02-design-construction.pdf` + `wsdot-02-lessons-history.htm` (fonte de texto; o PDF é escaneado — 0 chars em 34 páginas, sem OCR disponível — e foi mantido como matéria-prima, com nota de limitação nos índices).
  - BIP-011 (Domino's): `sec-01-10k-2009.pdf` · `sec-02-10k-2010.pdf`.
  - BIP-012 (Eyjafjallajökull): `icao-01-journal-2010.pdf` (ICAO Journal 65-4) · `iata-02-ash-plume.pdf` (IATA Economic Briefing).
- **Conformidade P1–P2:** fronteira pré/pós-gate em cada `00-index.md`; apenas fontes brutas primárias (nenhum material de SX-001/002/003 importado); refs cronológicos por BIP.

## Detalhe D-04.4 — P3: produção de materiais zero-ECP (PRODUCED)

- Para cada BIP-008..012 foram produzidos (padrão P5):
  - `narrative/01-narrativa-original.md` (condição C, não-cega) — narrativa em português, linhas em ordem histórica, `[ref]` por parágrafo.
  - `atomic-facts/02-atomic-facts.md` (condições A/B) — lista de proposições atômicas, `[ref]` por fato.
  - `README.md` — índice do BIP com as fontes efetivas.
- **Zero termos ECP** em todas as narrativas e atomic facts (52 termos ECP via `\bterm\b`, NFD).
- Rastreabilidade: cada fato/parágrafo referencia `refs` registrados nos respectivos `00-index.md`.

## Detalhe D-04.5 — P4: validação lexical + rastreabilidade (ALL PASS 5/5)

- Validador: `validate_bip.py` (léxico 52 termos ECP + rastreabilidade de refs vs. `00-index.md`).
- Resultado por BIP:
  - **BIP-008-apollo13:** LEXICON PASS + TRACE PASS (correções: `objetivo`→propósito, `capacidade`→remoção).
  - **BIP-009-chernobyl:** LEXICON PASS + TRACE PASS (correção: `estado`→situação, 2 ocorrências).
  - **BIP-010-tacomanarrows:** LEXICON PASS + TRACE PASS (correções: `estado`, `capacidade`, literal `[refs...]` no cabeçalho).
  - **BIP-011-dominos:** LEXICON PASS + TRACE PASS.
  - **BIP-012-eyjafjallajokull:** LEXICON PASS + TRACE PASS (correções: `capacidade`→oferta, `decisão`→opção).
- **RESULT: PASS em 5/5 BIPs.** Materiais prontos para o gate NT-05 (painel D-03) no pós-gate.

## Detalhe D-04.6 — Pacote de revisão NT-05 estendido (PRODUCED, sem execução)

- A governança autorizou **preparar** (não executar) o pacote de revisão semântica **NT-05 estendido** aos 5 novos BIPs, usando o mesmo painel de 2 IAs independentes da D-03.
- **`review/nt05-extended/` criado** (raiz do pacote; acesso restrito aos revisores):
  - `protocol/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` — cópia **somente leitura** do protocolo.
  - `materials/` — **12 cópias de leitura**: `C3_TAXONOMY.yaml` (GO-8C, versão corrigida D-03.7) + 5 narrativas + 5 atomic facts dos BIPs 008–012. Os revisores **não precisam acessar outras pastas**.
  - `REVIEW-ITEMS.md` — 22 itens: alvo primário (12 categorias `SYN-001..012`, com nota sobre a correção D-03.7); alvo secundário (10 materiais: `S-1a..S-5a` narrativas, `S-1b..S-5b` atomic facts).
  - `REVIEW-FORM-MODEL-1.md` / `REVIEW-FORM-MODEL-2.md` — formulários **em branco** (via MODEL-1 / MODEL-2), aguardando os revisores; critério PASS somente com ≤ 0 violações.
- **Verificação:** hashes SHA-256 das 12 cópias vs. originais → **ALL COPIES INTACT: True**.
- **Originais intocados:** nenhum arquivo do GO-8B alterado; materiais originais do GO-8C (`study-input/BIP-008..012/`) e `scripts/C3_TAXONOMY.yaml` não modificados.
- **A revisão NÃO foi executada** — formulários vazios; `BIP-VAL_REPORT.yaml` do GO-8C não atualizado; atualização apenas após a análise do painel.

## Detalhe D-04.7 — Consolidação do NT-05 estendido (DONE, divergência justificada)

- **Painel estendido NT-05 (executado em abas novas com contexto limpo, lendo somente `review/nt05-extended/materials/`):**
  - **Revisor 1 (GLM 4.5 Flash):** **REJEITADO** — 2 violações alegadas na taxonomia C3 (labels `SYN-001=Funcao`, `SYN-012=Adaptacao`).
  - **Revisor 2 (Gemini 3.6 Flash):** **PASS** — 0 violações.
  - **Regra aplicada:** divergência = STOP; investigação antes de decidir.
- **Análise técnica** (`decisions/D-04-NT05-DIVERGENCE-ANALYSIS.md`, 2026-08-14):
  - Lista ECP (52 termos, congelada em `GO-8B/pilot-input/validate_bip007.py` e `GO-8C/scripts/C3_TAXONOMY.yaml`) **não contém** `funcao`/`function` nem `adaptacao`/`adaptation` (verificação programática).
  - Labels são **vocabulário FRAM/STAMP** — fontes externas permitidas pela regra **N-3** (`03-SYNTHETIC-TAXONOMY-C3.md`), não termos ECP.
  - **NT-01 determinístico** = 0 hits dos 52 termos ECP (labels/definitions/source_refs) — registrado no próprio `C3_TAXONOMY.yaml`.
  - **D-03.7** corrigiu apenas as definições (paráfrases removidas); **D-03.8** já havia aprovado os labels (painel base GLM + Gemini, PASS).
  - Revisor 1 flagrou 2 de 12 categorias com a mesma natureza FRAM/STAMP — interpretação não sistemática.
- **Decisão da governança (Opção B1):** aceitar a divergência com justificativa formal; **NT-05 estendido consolidado como PASS**. A divergência fica **registrada para auditoria futura**; a decisão não enfraquece o processo (divergência resolvida por análise da governança, como previsto).
- **`scripts/BIP-VAL_REPORT.yaml` (GO-8C) atualizado:**
  - `NT-05: PASS_AI_PANEL (divergence justified)`; `verdict: PASS`.
  - Detalhes e `nt05_mode_note` atualizados com a divergência e a justificativa (referência ao DIVERGENCE-ANALYSIS).
- **`TODO-GO-8C.md`:** subtarefa **NT-05 extended → DONE** (com nota de divergência).
- **GO-8B intocado**; taxonomia `C3_TAXONOMY.yaml` e materiais dos BIPs 008–012 **não alterados**.

## Detalhe D-04.8 — Pré-registro N=12 (PRODUCED, sem seeds/Lock)

- **`08-PRE-REGISTRATION-N12.md`** (2026-08-14) criado na raiz do GO-8C.
- **Desenho pré-registrado (fixado):**
  - **N = 12 BIPs** (001–012: 7 reexecutados + 5 novos).
  - **Condições:** 3 — A (cega pura), B (cega + C3), C (não-cega).
  - **Seeds:** 3 por célula, geradas deterministicamente com `PCG64(seed_master)` (seed_master `PENDING LOCK PROTOCOL`); **não geradas** nesta etapa.
  - **Total de execuções:** **12 × 3 × 3 = 108**.
- **Métricas:** `S_struct` (primária/confirmatória) e `S_sem` (exploratória), conforme 04/05 do GO-8B.
- **Análise estatística:** Friedman global (df=2, α=0.05); se p<0.05 → Wilcoxon signed-rank pareado bilateral + Holm-Bonferroni; Kendall W, rank-biserial r, Cliff δ; bootstrap B=10.000 (IC percentil + IC exato da mediana ao lado); **TOST não vigente** (sem Δ aprovada).
- **Critério de sucesso:** **≥ 10 de 12 casos válidos** (D-04 decisão 3; prevalência do pré-registro — valor fixado em 10).
- **Gate de autorização:** aprovação formal do pré-registro → **Lock GO-8C** (etapa separada) → decisão explícita de execução. Nada executado nesta etapa.
- **Consistência com o GO-8B (§13):** replicado de 06/07/08 com as únicas adaptações aprovadas — N=12, Go/No-Go ≥10 de 12 (D-04), seed C2 corrigida (D-01: `258915`), namespace operacional (D-02: A→CAT, B→SYN, C→CAT). Nenhum parâmetro metodológico novo.
- **GO-8B intocado; artefatos 06/07/08 do GO-8B não alterados.**

## Detalhe D-04.9 — Aprovação do pré-registro N=12 (DECIDED)

- **Decisor:** Governança GO-8C
- **Decisão:** **APROVAR** o `08-PRE-REGISTRATION-N12.md` (2026-08-14).
- **Adaptações confirmadas corretas:** N=12 (D-04) · Go/No-Go ≥ 10 de 12 (D-04) · seed C2 corrigida `258915` hex `0x3f363` (D-01; antiga → `HISTORICAL-NON-REPRODUCING`) · namespace operacional A→CAT / B→SYN / C→CAT (D-02).
- **Registro formal:** `decisions/D-04-PREREG-N12-APPROVED.md` (status **DECIDED**).
- **NÃO autorizado nesta decisão:** geração de seeds; Lock GO-8C (requer nova autorização, etapa separada); execução experimental (108 reconstruções); análise estatística.
- **Próximo passo (mediante nova autorização):** preparar e executar o **Lock GO-8C** (manifesto + hashes); depois autorização explícita de execução.
- **GO-8B intocado; seeds/hashes permanecem `PENDING LOCK PROTOCOL`.**

## Detalhe D-04.10 — Lock do GO-8C (LOCKED)

- **Autorização:** Governança GO-8C, 2026-08-14 (após pré-registro aprovado em D-04.9).
- **Procedimento (script `gen_lock.py`):**
  1. **Normalização in-place** dos textos de propriedade do GO-8C (UTF-8 sem BOM, LF, exatamente um newline final, whitespace preservado) — 96 arquivos reescritos.
  2. **Hash SHA-256** de cada artefato: textos GO-8C = conteúdo normalizado; binários (`*.pdf`, `*.npy`) = bytes como estão; scripts do lado GO-8B (`scripts/go8b/operational/*.py`) = bytes originais **sem reescrita** (imutabilidade do GO-8B preservada).
  3. Geração de `GO-8C-LOCK-MANIFEST.yaml` e `GO-8C-LOCK-RECORD.yaml`.
- **Manifesto — escopo congelado (151 arquivos):**
  - `study_material: 108` (estudo N=12 inteiro em `study-input/`, 12 BIPs + README).
  - `review_artifact: 12` (pacotes de revisão, excluindo `materials/**` duplicatas).
  - `decision_record: 11` (todas as decisões, exceto `ACTION-REGISTER.md` — documento vivo).
  - 8 docs raiz: `GO-8C-OPENING-DECISION.md`, `02-C2-PERMUTATION-CORRECTED.md`, `08-PRE-REGISTRATION-N12.md`, 5 propostas (D-01..D-04 + WORKPLAN).
  - 7 arquivos de `scripts/` (4 configs + 3 suítes de teste).
  - 5 engine/reprodutibilidade: `scripts/go8b/operational/{pilot_engine.py, wl_kernel.py, graph_from_reconstruction.py, EMBEDDINGS.npy}` + `scripts/go8b/requirements.txt` (`go8b_power_sim.py` e `go8b_statistical_analysis.py` já constam do Lock GO-8B e foram excluídos).
- **Hashes:**
  - `preregistration.sha256` = `4cdacb118547eb01f6dd1b95c3d904f6dd0d1ff821ebfea4e2907eb1a7bf8ead` (08-PRE-REGISTRATION-N12.md).
  - `manifest.sha256` = `f59591a0a8768dc34dbb86c94894ce9f1a1b35cb5b7a67dbb9a96e69502027c0` (registrado no Lock Record).
- **Validação independente (`validate_lock.py`):** parse YAML OK (manifesto + record); re-hash de todos os 151 arquivos → **0 mismatch / 0 missing**; `record.manifest.sha256` == re-hash do manifesto → **consistent: True**; todos os textos GO-8C no disco normalizados → **0 pendentes**. **RESULT: PASS.**
- **Exclusões documentadas no manifesto (scope_notes):** `TODO-GO-8C.md` e `decisions/ACTION-REGISTER.md` (documentos vivos, atualizados pós-Lock); `review/materials/**` e `review/nt05-extended/materials/**` (duplicatas byte-idênticas de `study-input/` + `C3_TAXONOMY.yaml`); `scripts/go8b/operational/{seeds_dict.py, generate_seeds.py}` (stream de seeds do piloto GO-8B; GO-8C usa novo `seed_master`, PENDING LOCK PROTOCOL); configs do lado GO-8B `C2_PERMUTATION.yaml/.json`, `C3_TAXONOMY.yaml`, `BIP-VAL_REPORT.yaml` (superadas pelas versões corrigidas do GO-8C, D-01/D-03).
- **Regras registradas no Lock Record:** nenhuma modificação in-place de artefato congelado após o primeiro hash; qualquer divergência → **STOP** (sem correção/re-cálculo); experimento/coleta/análise **NÃO executados**; **nenhum arquivo do GO-8B alterado**; execução (108 reconstruções) **BLOQUEADA** até autorização explícita pós-Lock.
- **GO-8B intacto;** Lock GO-8B e seus 13 artefatos não foram recalculados nem alterados.

## Detalhe D-04.11 — Correção do formato do BIP-009 + re-Lock (CORRECTED / RELOCKED)

- **Contexto:** durante a execução do estudo (108 reconstruções), 6 células falharam (BIP-009 condições A/B). **STOP** reportado à governança; investigação concluiu erro **isolado**: `02-atomic-facts.md` do BIP-009 produzido em **formato tabela markdown** na fase P3 (D-04.4) — o parser congelado (`pilot_engine.py:126-153`) exige `## Fatos` + lista numerada terminando em `]`/`]`` → 0 fatos parseados → `ValueError("no units parsed")`. Conteúdo validado semanticamente (NT-05 PASS), apenas o contêiner não é máquina-parseável.
- **Autorização:** Governança GO-8C, 2026-08-14 — aprova a **Opção recomendada**: corrigir o formato, re-Lock e re-executar as 6 células.
- **Conversão (puramente estrutural, auditável):**
  - Tabela `| # | Atomic fact | Fonte |` → `## Fatos` + lista numerada `N. <texto> \`[ref]\``.
  - Verificação: **72 fatos** extraídos; texto + refs + ordem **idênticos** (0 mismatch); sequência 1..72; parser do engine parseia **72/72**; zero termos ECP mantidos.
  - Diff antes/depois gerado para auditoria (temp); novo hash SHA-256 = `b1142dfa6696980c0dcb954447ca0a29860bf7cfa97d557c8b4f6f7e09a6195f`.
- **Re-Lock do artefato:**
  - `GO-8C-LOCK-MANIFEST.yaml`: sha256 do arquivo atualizado (`f45ae520…1958` → `b1142dfa…6195f`).
  - `GO-8C-LOCK-RECORD.yaml`: `manifest.sha256` atualizado → `8a68a6582e4183018fded19db0a6dfad3b794abf275825f89e061491e64884f2`.
  - Validação independente (`validate_lock.py`) → **PASS**: 0 mismatch / 0 missing; record↔manifest consistent; 0 arquivos GO-8C não normalizados.
- **Re-execução:** BIP-009 condições A/B, 3 seeds cada (6 células) → **PASS (6/6)**; CSV do estudo atualizado.
- **Gate gap registrado:** `decisions/D-04-GATE-GAP-ENGINE-PARSEABILITY.md` — validador de produção D-04.5 não verificava parseabilidade pelo engine; recomendação de check em ciclos futuros.
- **GO-8B e todos os demais 150 artefatos do Lock intocados.**

## Detalhe D-04.12 — Análise estatística do estudo N=12 (DONE)

- **Autorização:** Governança GO-8C, 2026-08-14 (pós-Lock vigente, dados finais 108/108 PASS).
- **Execução:** script estatístico congelado do GO-8B (`scripts/go8b/go8b_statistical_analysis.py`) executado sobre `study-output/stats_input_sstruct_n12.csv` (108 observações; `case_id` mapeado: Deepwater, Hyatt, WarpSpeed, Genoma, Suez, I-35W, Ebola, Apollo13, Chernobyl, TacomaNarrows, Dominos, Eyjafjallajokull).
- **Resultados (protocolo 06 §7 / pré-registro N=12):**
  - **Data check:** 108/108 PASS; 36 células × 3 seeds completas; range [0.5539, 0.7081] ∈ [0,1]; N=12.
  - **Friedman (primário):** χ²_F=9.7826, df=2, **p=0.0075** → **REJEITA H₀**; Kendall W=0.4076 (IC95% bootstrap (0.1267, 0.7622)).
  - **Post-hoc (Wilcoxon bilateral + Holm):** B vs C **REJEITA** (p=0.0093; r_rb=−0.821; Cliff δ=0.701); A vs B não rejeita (p=0.0537; r_rb=0.667; IC dif. medianas (0.002,0.095) exclui 0 — direção B>A); A vs C não rejeita (p=0.3086).
  - **Sensibilidade:** sem outliers N=9 p=0.0200; drops de domínio (Hyatt/I-35W/Ebola/WarpSpeed) todos p<0.05 — omnibus **robusto**.
  - **TOST não executado** (sem Δ aprovada); sem winsorização; sem modelo misto (STAT-09).
  - **Medianas:** A=0.5875 · B=0.6348 · C=0.5843 (S_struct); S_sem A=0.5495 · B=0.5532 · C=0.5478.
- **Go/No-Go (pré-registro §8):** **GO** — 12/12 casos válidos ≥ 10; matriz completa; nenhum FAIL-PILOT.
- **Relatório:** `study-output/STATISTICAL-REPORT-N12.md`.
- **Lock íntegro:** nenhum arquivo do Lock alterado nesta etapa; validação do Lock permanece PASS.

## Detalhe D-04.13 — Encerramento formal do ciclo GO-8C (CLOSED)

- **Autorização:** Governança GO-8C, 2026-08-14 — aprova o encerramento formal do ciclo após análise estatística concluída.
- **Ações executadas:**
  1. **Relatório final** criado: `FINAL-PROJECT-REPORT-GO-8C.md` (título, data 2026-08-14, status **GO — concluído**; resumo executivo; metodologia N=12/3 condições/3 seeds/108 execuções; resultados estatísticos; interpretação B>C robusto e A vs B inconclusivo/limítrofe; limitações; recomendações para GO-8D).
  2. **Pacote de encerramento** gerado: `GO-8C-CLOSURE-PACKAGE.zip` (20 entradas — relatório final, `study-output/pilot_results_n12.csv`, `study-output/STATISTICAL-REPORT-N12.md`, `stats_input_sstruct_n12.csv`, `seeds_n12.py`, `GO-8C-LOCK-MANIFEST.yaml`, `GO-8C-LOCK-RECORD.yaml`, 13 decisões de `decisions/`).
  3. **ACTION-REGISTER** atualizado com `GO-8C CLOSED` (D-04.13).
  4. **TODO-GO-8C** atualizado: ciclo **CLOSED** + pendências listadas para GO-8D.
- **Integridade confirmada:**
  - **GO-8B intacto** (CLOSED/LOCKED/FROZEN — nenhum arquivo alterado).
  - **GO-8C Lock íntegro** (`validate_lock.py` → **PASS**: 0 mismatch, 0 missing, record↔manifest consistent).
- **Status final do ciclo:** **GO-8C CLOSED.**

---

**Regras inabaláveis aplicadas:**
- GO-8B CLOSED / LOCKED / FROZEN — nenhum arquivo alterado, nenhum hash/Lock recalculado.
- Todas as escritas em `experiments/validation/GO-8C/`.
- Nenhum Lock do GO-8C gerado nesta etapa (aguardando autorização para etapa de manifestação/Lock).

**Fim do ACTION-REGISTER (GO-8C). D-01, D-02 e D-03 registrados como DONE (D-03 consolidado em 2026-08-14); correção D-03.7 registrada (CORRECTED); D-04 DECIDED (estrutura + cópia dos 7 BIPs PRODUCED; plano de trabalho dos 5 novos DECIDED; P1–P4 dos BIPs 008–012 PRODUCED e VALIDATED — ALL PASS 5/5; pacote NT-05 estendido PRODUCED em D-04.6; NT-05 estendido CONSOLIDADO como PASS em D-04.7 — divergência justificada em D-04-NT05-DIVERGENCE-ANALYSIS.md; pré-registro N=12 PRODUCED em D-04.8 e **APROVADO em D-04.9 — 08-PRE-REGISTRATION-N12.md DECIDED; **Lock GO-8C EXECUTADO em D-04.10 — `GO-8C-LOCK-MANIFEST.yaml` (151 artefatos, sha256 `f59591a0…2027c0`) + `GO-8C-LOCK-RECORD.yaml` (lock_status LOCKED, validado PASS); seeds e execução experimental permanecem BLOQUEADOS até autorização explícita pós-Lock; **D-04.11 — correção do formato do BIP-009 (tabela → `## Fatos`, 72 fatos, hash `b1142dfa…6195f`) + re-Lock (manifest sha256 `8a68a658…84f2`, validado PASS) + gate gap registrado; BIP-009 A/B re-executado PASS (6/6)**).**