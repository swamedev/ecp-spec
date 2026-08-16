# GO-8C — TODO (Backlog de Dívidas Técnicas)

**Data:** 2026-08-13
**Ciclo:** GO-8C — **CLOSED (2026-08-14)** — estudo confirmatório N=12 concluído (Go/No-Go **GO**, 12/12); encerramento formal aprovado pela governança (D-04.13).
**Status geral:** **GO-8C CLOSED** — execução 108/108 PASS · análise estatística concluída (D-04.12) · relatório final + pacote de encerramento gerados · Lock GO-8C LOCKED e íntegro (validação PASS) · **pendências do ciclo transferidas para GO-8D**

**Regra:** nenhuma dívida é resolvida pela abertura. Cada item passa por
`OBSERVAÇÃO → ANÁLISE → OPÇÕES → DECISÃO DE GOVERNANÇA → IMPLEMENTAÇÃO AUTORIZADA → VALIDAÇÃO`.

---

## Check-list

- [x] **D-01 — C2 / P1-C2-01** — Correção da seed C2 registrada como `REGISTERED-NON-REPRODUCING`.
  - STATUS = **DONE** (DECIDED + VALIDATED — 2026-08-13, DECISION D-01)
  - Seed oficial: `258915` (hex `0x3f363`); seed antiga → `HISTORICAL-NON-REPRODUCING`; inversa verdadeira `[5,0,8,3,6,1,2,4,7]`.
  - Artefatos:
    - `decisions/D-01-C2-DECISION.md`
    - `02-C2-PERMUTATION-CORRECTED.md`
    - `decisions/D-01-C2-VALIDATION.md`
    - `scripts/C2_PERMUTATION.yaml` · `.json` · `scripts/p1_c2_test.py`
  - Validação: **ALL PASS (7/7)** — T-C2-01/02/03/04/05/08/09.
  - Nenhum arquivo do GO-8B alterado; nenhum Lock gerado nesta etapa.
- [x] **D-02 — C4 / NULL** — Revisar incompatibilidade entre namespace NULL (C4) e parser congelado (reprojeto / compatibilização / formalização do uso operacional de CAT).
  - STATUS = **DONE** (DECIDED + VALIDATED — 2026-08-13, DECISION D-02, **Opção 2**)
  - Decisão: condições A/C usam **CAT** como namespace operacional; B usa **SYN**; NULL permanece não processável (04 §1.1); **sem equivalência NULL≡CAT nem CAT≡SYN/ECP**.
  - Artefatos:
    - `D-02-C4-NULL-PROPOSAL.md`
    - `decisions/D-02-C4-NULL-DECISION.md`
    - `decisions/D-02-C4-NULL-VALIDATION.md`
    - `scripts/test_d02_namespace.py` · `scripts/C2_PERMUTATION.yaml` · `.json` (campo `namespace_operacional`)
  - Validação: **ALL PASS (3/3)** — T-D-02-01/02/03; regressão D-01 **ALL PASS (7/7)**.
  - ROADMAP (registrado, sem prazo, sem execução): **Opção 3** — sonda de viabilidade para processamento real de NULL (codificação livre) exigirá novo ciclo decisório e nova validação.
  - Ressalva: D-02 **não desbloqueia automaticamente** D-03/D-04 — cada dívida é decisão independente; N=12 (D-04) só será fixado após desenho operacional estabilizado.
  - Nenhum arquivo do GO-8B alterado; nenhum Lock gerado nesta etapa.
- [x] **D-03 — NT-05** — Formalizar e auditar a substituição do requisito humano por auditoria automatizada (rastreabilidade e critérios de validade).
  - STATUS = **DONE** (DECIDED + VALIDATED + CONSOLIDATED — 2026-08-14)
  - Decisão: substituição **parcial** de NT-05 — componentes determinísticos (NT-01..04 + suítes operacionais) automatizados; **gate semântico mínimo** por **painel de 2 IAs independentes** (três abas separadas, acesso restrito); critério "≤ 0 violações semânticas não capturadas"; **sem equivalência** com revisão humana original (limitação registrada).
  - Artefatos:
    - `D-03-NT05-PROPOSAL.md`
    - `decisions/D-03-NT05-DECISION.md`
    - `decisions/NT-05-SEMANTIC-REVIEW-PROTOCOL.md`
    - `decisions/D-03-NT05-VALIDATION.md`
    - `decisions/D-03-NT05-PANEL-RESULT.md` (resultado do painel — 2026-08-14)
    - `scripts/BIP-VAL_REPORT.yaml` (atualizado: `NT-05: PASS_AI_PANEL (unanimous)`; `verdict: PASS`)
    - `scripts/test_d03_nt05.py`
    - `review/` (pacote de revisão: procedimento, formulários, materiais)
  - Correção D-03.7: definições de SYN-001/SYN-012 corrigidas (paráfrases removidas) e revalidadas.
  - Painel de revisão semântica: **unanimidade PASS (0 violações em 26 itens)** — Revisor 1 (GLM 4.5 Flash) + Revisor 2 (Gemini 3.6 Flash).
  - Validação: **ALL PASS (3/3)** — T-D-03-01/02/03; regressões D-01 **ALL PASS (7/7)** e D-02 **ALL PASS (3/3)**.
  - **Conclusão:** NT-05 parcial do GO-8C **VALIDADO**; `verdict` → **PASS**.
  - Ressalva: D-03 resolve apenas NT-05; não altera outros gates nem critérios de caso/Go-No-Go; **não desbloqueia automaticamente** D-04.
  - Nenhum arquivo do GO-8B alterado; nenhum Lock gerado nesta etapa.
- [x] **D-04 — N=12** — Planejar estudo confirmatório com N=12 (considerando análise de potência do GO-8B).
  - STATUS = **DONE** (DECIDED + P1–P4 DONE + Lock + EXECUÇÃO 108/108 PASS + ANÁLISE ESTATÍSTICA D-04.12 — Go/No-Go GO; 2026-08-14, DECISION D-04; plano de trabalho APROVADO D-04.2; materiais dos BIPs 008–012 PRODUCED D-04.3/D-04.4 e VALIDATED D-04.5 — ALL PASS 5/5).
  - Decisões formalizadas:
    1. Lista dos 12 BIPs aprovada (001–007 reuso de materiais + 008 Apollo 13, 009 Chernobyl, 010 Tacoma Narrows, 011 Domino's Turnaround, 012 Eyjafjallajökull).
    2. **Re-execução dos 7 BIPs** no pipeline do GO-8C (materiais copiados; **nenhum dado do GO-8B reutilizado** como observação).
    3. **Go/No-Go: ≥ 10 de 12 casos válidos**, salvo se o pré-registro N=12 definir outro valor (pré-registro prevalece).
    4. Produção dos 5 novos materiais autorizada (padrão P5: fontes oficiais, narrativa + atomic facts, zero ECP, validação lexical) — **após aprovação do plano de trabalho**.
    5. **NT-05 estendido** aos 5 novos materiais (painel de 2 IAs da D-03, mesmos critérios/modelos).
  - Subtarefas pendentes:
    - [x] **Aprovar plano de trabalho dos 5 novos BIPs** (`D-04-N12-WORKPLAN.md` — cronograma e estrutura) — **APROVADO (2026-08-14, D-04.2)**.
    - [x] Produzir materiais dos 5 novos BIPs (BIP-008..012) + validação lexical/rastreabilidade/não-importação — **PRODUCED (D-04.3/D-04.4) + VALIDATED (D-04.5, ALL PASS 5/5)**.
    - [x] **NT-05 estendido aos 5 novos materiais** (painel de 2 IAs da D-03) — **DONE (2026-08-14)**. Painel estendido retornou divergência (Revisor 1 REJEITADO: 2 violações alegadas nos labels SYN-001/SYN-012; Revisor 2 PASS). Governança (B1) aceitou a divergência com justificativa formal: labels `Funcao`/`Adaptacao` não constam na lista ECP (52 termos), são vocabulário FRAM/STAMP permitido por N-3, NT-01 determinístico = 0 hits, D-03.7/D-03.8 já trataram definições/labels. **NT-05 estendido = PASS** (`BIP-VAL_REPORT.yaml` atualizado). Análise: `decisions/D-04-NT05-DIVERGENCE-ANALYSIS.md`. Divergência registrada para auditoria futura.
    - [x] **Pré-registro N=12 escrito e aprovado** (desenho, seeds, Go/No-Go, plano de análise — replicando 06/07/08 do GO-8B) — **ESCRITO (2026-08-14, `08-PRE-REGISTRATION-N12.md`, D-04.8)** e **APROVADO (2026-08-14, D-04.9, `decisions/D-04-PREREG-N12-APPROVED.md` — DECIDED)**. Adaptações confirmadas: N=12 (D-04), Go/No-Go ≥10 de 12 (D-04), seed C2 `258915` (D-01), namespace A→CAT/B→SYN/C→CAT (D-02). Seeds NÃO geradas.
    - [x] **Lock do GO-8C executado** (autorização da governança 2026-08-14) — `GO-8C-LOCK-MANIFEST.yaml` (151 artefatos; sha256 `f59591a0…2027c0`) + `GO-8C-LOCK-RECORD.yaml` (lock_status **LOCKED**); validação independente **PASS** (0 mismatch). Normalização in-place dos textos do GO-8C; scripts/engine do lado GO-8B hasheados como estão, **sem reescrita** (GO-8B intacto). Seeds/hashes do estudo permanecem `PENDING LOCK PROTOCOL`.
    - [x] **D-04.11 — correção do formato do BIP-009 + re-Lock** (2026-08-14) — durante a execução, 6 células falharam (BIP-009 A/B): `02-atomic-facts.md` em formato **tabela markdown** (produzido na P3/D-04.4), não parseável pelo engine congelado. Investiga-se e **converte-se** para `## Fatos` + lista numerada (72 fatos; texto/refs/ordem preservados; diff auditável) → novo hash `b1142dfa…6195f`; `GO-8C-LOCK-MANIFEST.yaml` + `GO-8C-LOCK-RECORD.yaml` **atualizados** (manifest sha256 `8a68a658…84f2`; validação **PASS**). Gate gap registrado em `decisions/D-04-GATE-GAP-ENGINE-PARSEABILITY.md`. BIP-009 A/B re-executado → **PASS (6/6)**. GO-8B e demais 150 artefatos do Lock intocados.
    - [x] **Execução do estudo N=12** (autorização da governança 2026-08-14, pós-Lock) — **108/108 reconstruções PASS (0 FAIL)**; CSV final validado (`study-output/pilot_results_n12.csv`): 36 células × 3 seeds completas, seeds uint64 corretos vs. `seeds_n12.py`, ranges ∈ [0,1], namespaces A/C→CAT e B→SYN, 0 NAMESPACE_MIX. Estudo íntegro.
    - [x] **Análise estatística + relatório + encerramento (D-04.12)** — script estatístico congelado do GO-8B executado sobre os dados finais → `study-output/STATISTICAL-REPORT-N12.md`. **Go/No-Go: GO (12/12 ≥ 10)**. Friedman χ²=9.7826 df=2 p=0.0075 (REJEITA H₀; W=0.4076); post-hoc Holm: B>C significativo (p=0.0093, r_rb=−0.821, Cliff δ=0.701); A vs B não significativo pós-Holm (p=0.0537, direção B>A); sensibilidades todas p<0.05 (robusto); TOST não executado. Lock GO-8C íntegro (validação PASS).
    - [x] **Encerramento formal do ciclo (D-04.13, 2026-08-14)** — **GO-8C CLOSED**. Relatório final `FINAL-PROJECT-REPORT-GO-8C.md` (status GO — concluído); pacote `GO-8C-CLOSURE-PACKAGE.zip` (20 entradas); ACTION-REGISTER atualizado (CLOSED); este TODO atualizado; Lock validado PASS; GO-8B intacto. Pendências transferidas para **GO-8D** (seção abaixo).
  - Artefatos:
    - `D-04-N12-PROPOSAL.md`
    - `decisions/D-04-N12-DECISION.md`
    - `study-input/` (12 BIPs: 7 copiados + 5 a produzir)
    - `study-output/` (a criar na execução autorizada)
  - Nenhum arquivo do GO-8B alterado; nenhum Lock gerado nesta etapa; GO-8B CLOSED/LOCKED/FROZEN.

---

**ROADMAP (próximo gate):** **GO-8C CLOSED (2026-08-14, D-04.13)** — estudo confirmatório N=12 concluído. Lock GO-8C EXECUTADO (D-04.10, 151 artefatos, validado PASS); **BIP-009 corrigido e re-Locked (D-04.11)** (hash `b1142dfa…6195f`; manifest sha256 `8a68a658…84f2`, validado PASS); **execução 108/108 PASS**; **análise estatística (D-04.12): Go/No-Go GO (12/12 ≥ 10)**, Friedman p=0.0075 (rejeita H₀), B>C significativo pós-Holm, robustez confirmada, TOST não executado; **relatório final `FINAL-PROJECT-REPORT-GO-8C.md` + pacote `GO-8C-CLOSURE-PACKAGE.zip`**. P1–P4 dos 5 novos BIPs CONCLUÍDOS; NT-05 estendido CONSOLIDADO como PASS (divergência justificada); gate gap de parseabilidade registrado. **Próximo gate: decisão da governança sobre GO-8D** (ver pendências abaixo).

**Roadmap de pesquisa (sem prazo, fora do experimento atual):** processamento real de NULL (C4) — sonda de viabilidade (codificação livre) requerendo novo ciclo decisório e nova validação (Opção 3, registrada em D-02).

---

## Pendências para GO-8D (ciclo futuro, se aprovado)

Pendências transferidas do fechamento do GO-8C (recomendações do `FINAL-PROJECT-REPORT-GO-8C.md` §6):

- [ ] **Reavaliar S_struct** — investigar o componente de duplicação/sobreposição estrutural e seu impacto na separação A vs B; documentar viés potencial da métrica.
- [ ] **Considerar métricas alternativas/complementares** — S_sem refinada, distância de edição estrutural ponderada (GED), avaliação semântica dirigida (embeddings) ou métrica de fidelidade conceitual por fato.
- [ ] **Possivelmente aumentar N além de 12** — a comparação A vs B ficou limítrofe (p=0.0537; r_rb=0.667; dif. de medianas ≈ 0.047); reexecutar análise de potência com o efeito observado para dimensionar N.
- [ ] **Refinar a taxonomia C3** — avaliar se as 12 categorias atuais são suficientemente discriminantes para capturar o ganho estrutural real da condição B.
- [ ] **Fechar o gate gap de parseabilidade** — adicionar check de parseabilidade pelo engine ao validador de produção (D-04.5) em futuros ciclos (ver `decisions/D-04-GATE-GAP-ENGINE-PARSEABILITY.md`).
- [ ] **Definir margem Δ para TOST** — manter TOST não vigente até a governança aprovar uma margem formal (equivalência).
- [ ] **Fortalecer o gate semântico** — revisor humano em complemento ao painel de IAs quando houver disponibilidade (limitação epistemológica do NT-05 por painel de IAs registrada).

> Nota: decisões GO-8D devem seguir o mesmo fluxo de governança (proposta → decisão → pré-registro → Lock → execução → análise). GO-8B e GO-8C permanecem CLOSED/LOCKED/FROZEN.

Nenhuma implementação, correção, coleta de dados, alteração de parâmetros, hash ou Lock
pode ocorrer até autorização formal por etapa.

---

**Fim do TODO — GO-8C CLOSED (2026-08-14). Nenhuma dívida do GO-8C permanece aberta no ciclo; pendências do estudo transferidas para GO-8D (ver seção acima).