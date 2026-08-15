# GO-8D — TODO (Backlog de Dívidas Técnicas)

**Data:** 2026-08-14
**Ciclo:** GO-8D — **OPENED (DIAGNOSTIC PHASE)** — abertura formal em continuidade ao diagnóstico D-01.
**Status geral:** **GO-8D OPENED** · GO-8C **CLOSED** · GO-8B **CLOSED/LOCKED/FROZEN** · **Nenhum experimento autorizado até D-01..D-07 concluídos e aprovados.**

**Regra:** nenhuma dívida é resolvida pela abertura. Cada item passa por
`OBSERVAÇÃO → ANÁLISE → OPÇÕES → DECISÃO DE GOVERNANÇA → IMPLEMENTAÇÃO AUTORIZADA → VALIDAÇÃO`.

---

## Check-list

## Bloco 1 — Validade da medida

- [x] **D-01 — S_struct (viés estrutural)** — Auditoria da métrica confirmatória do GO-8C.
  - STATUS = **DIAGNOSED** (2026-08-14) — diagnóstico concluído na fase pré-abertura.
  - Achados: métrica mede essencialmente contagem de nós + degenerescência WL do grafo colapsado
    (não fidelidade ao ECP); anonimização uniforme elimina sinal de categoria; topologia dominada
    pelo parser; seeds vestigiais (108 linhas = 36 valores únicos); condição B do N=12 exige a
    taxonomia corrigida (D-03.7); BIP-007-B no CSV = corrigida (execução uniforme; lacuna é de
    rastreabilidade, não inconsistência — corrigido 2026-08-14, ver D-02 §6).
  - Artefatos:
    - `experiments/validation/GO-8C/decisions/D-01-SSTRUCT-AUDIT.md` (relatório de diagnóstico)
  - **Aguardando decisão de governança sobre como incorporar os achados em D-02/D-03.**
- [x] **D-02 — Métricas alternativas** — Avaliar métricas que preservem o sinal de
  rótulo/tipo/categoria (ex.: kernel WL rotulado, GED ponderada, S_sem refinada, fidelidade por
  fato, embeddings de nó no kernel).
  - STATUS = **DIAGNOSED** (2026-08-14) — diagnóstico executado sobre as 36 células do N=12.
  - Resultado: M0 confirma D-01 (A = 5/12 valores distintos); **M1 (correção por nº de nós)
    torna a separação A/B/C não significativa (Q=5.17)**; M2 degenerada; **M3 (GED ponderada) é
    a única candidata sólida** (12/12 valores distintos, Q=18.00) mas não comparável entre
    namespaces; M4 (S_sem refinada) degenerada por construção (tabela de embeddings CAT = nomes
    canônicos ECP); M5/M6 úteis como diagnóstico, não DV.
  - **Conclusão:** nenhuma candidata é DV confirmatória válida no pipeline atual; a correção exige
    reprojeto do pipeline (D-03/D-05): desanonimizar WL, corrigir embeddings CAT, padronizar
    granularidade, referenciar a taxonomia da condição.
  - Artefatos:
    - `experiments/validation/GO-8D/decisions/D-02-METRICS-ANALYSIS.md` (relatório)
    - `experiments/validation/GO-8D/analysis/metrics_candidates.py` (diagnóstico reproduzível)
  - **Aguardando decisão de governança sobre o reprojeto da métrica (D-03/D-05).**
- [x] **D-03 — Refinamento da taxonomia C3 / reprojeto do pipeline** — Reprojetar os componentes
  para permitir uma DV confirmatória válida.
  - STATUS = **DIAGNOSED / PROPOSED** (2026-08-14) — simulações sobre as 36 células do N=12.
  - Resultado: **DV recomendada `conf+ged_ref+ent` (Q=18.50, 12/12 valores distintos, corr(nós)=+0.19)**;
    desanonimizar o WL é necessário mas não suficiente (WL rotulado sozinho degenerado, A=2/12);
    **o ganho do M3-GED da D-02 era artefato dos embeddings CAT colapsados** (com corrigidos,
    GED vs ECP cai para Q=2.17 n.s.); GED **vs taxonomia da condição** (ged_ref) é o componente
    estrutural robusto; embeddings CAT passam a usar definições neutras PT; gravar
    `taxonomy_sha256` por execução (fecha lacuna BIP-007-B).
  - **Decisões necessárias:** novo pré-registro (DV, pesos, hipóteses, Δ TOST) + recálculo de N
    (D-07) + novo Lock; GO-8B/GO-8C imutáveis.
  - Artefatos:
    - `experiments/validation/GO-8D/decisions/D-03-PIPELINE-REDESIGN.md` (relatório)
    - `experiments/validation/GO-8D/analysis/pipeline_redesign_sim.py` (simulação)
    - `experiments/validation/GO-8D/analysis/pipeline_redesign_sim2.py` (suplementar)
  - **Aguardando decisão de governança sobre o novo desenho (pré-registro D-07).**

## Bloco 2 — Validade do desenho

- [x] **D-04 — Gate de parseabilidade** — Fechar o gate gap: adicionar check de parseabilidade
  dos materiais pelo engine ao validador de produção (referência:
  `experiments/validation/GO-8C/decisions/D-04-GATE-GAP-ENGINE-PARSEABILITY.md`).
  - STATUS = **DIAGNOSED** (2026-08-14) — validador + suíte de testes implementados; **5/5 PASS**
    (tabela→FAIL, padrão→PASS, sem `## Fatos`→FAIL, <15 fatos→FAIL, regressão 12/12 BIPs do
    GO-8C→PASS). Gate gap fechado: formatos divergentes rejeitados antes do Lock.
  - Artefatos:
    - `experiments/validation/GO-8D/decisions/D-04-PARSEABILITY.md` (relatório)
    - `experiments/validation/GO-8D/scripts/validate_parseability.py` (validador)
    - `experiments/validation/GO-8D/scripts/test_d04_parseability.py` (testes)
  - **Aguardando aceite da governança (dívida independente da DV, executada em paralelo).**
- [x] **D-05 — Gate semântico híbrido** — Fortalecer o gate semântico: revisor humano em
  complemento ao painel de IAs quando houver disponibilidade (limitação epistemológica do NT-05
  por painel de IAs registrada no GO-8C).
  - STATUS = **PROPOSED** (2026-08-14) — protocolo em 3 camadas desenhado:
    **L1** auditoria automatizada obrigatória (ALL PASS; parseabilidade D-04, lexical, estrutura,
    rastreabilidade, hashes, `taxonomy_sha256`); **L2** painel de ≥2 IAs de arquiteturas
    distintas, obrigatório, contexto limpo, veredito unânime, votação proibida,
    divergência=STOP, rejeição=revalidação completa; **L3** amostra humana **opcional** (ativação
    condicional por disponibilidade + priorização por risco), sem equivalência epistemológica.
  - Artefato: `experiments/validation/GO-8D/decisions/D-05-HYBRID-SEMANTIC-GATE.md`
  - **Pré-registrado como desenho; execução apenas na produção do próximo ciclo (antes do Lock D-07).**
- [x] **D-06 — Definição de Δ para TOST** — Definir formalmente a margem Δ de equivalência para
  TOST; manter TOST não vigente até a governança aprovar a margem (R3-03 + R5-GOV-03).
  - STATUS = **APPROVED** (2026-08-14) — governança aprova **Δ = 0.05** (5% da escala da
    DV_confirm ∈ [0,1]); 0.10 rejeitada (R5-GOV-03); âncoras 0.2–0.5·SD (0.008–0.021) rejeitadas
    por estrita demais; efeitos de hipótese primária observados (A vs B = 0.079, B vs C = 0.069)
    ficam **acima** de Δ; TOST vigente apenas no contexto GO-8D, condicionado a D-07.
  - Artefatos:
    - `experiments/validation/GO-8D/decisions/D-06-TOST-DELTA.md` (proposta)
    - `experiments/validation/GO-8D/decisions/D-06-TOST-DELTA-APPROVED.md` (decisão formal)
    - `experiments/validation/GO-8D/analysis/d06_delta_anchors.py` (cálculo das âncoras)
  - **Concluído — pré-requisito do recálculo de N (D-07) liberado.**

## Bloco 3 — Poder estatístico

- [x] **D-07 — Recalcular N** — Após estabilizar a métrica (D-02/D-03) e o desenho (D-04..D-06),
  reexecutar a análise de potência com o efeito observado no N=12 (r_rb=0.667, dif. de medianas
  ≈ 0.047) para dimensionar N do próximo estudo; inclui novo pré-registro da DV_confirm
  `(conf + ged_ref + ent)/3` e novo Lock do GO-8D.
  - STATUS = **APPROVED** (2026-08-14) — **N recomendado = 12** (execuções 108 =
    12×3×3). MC (REPS=3.000, seed `20260814`): cenário fiel ao enunciado (A−B=0.079, B−C=0.069,
    σ_e=0.0296) → Friedman 0.999, Wilcoxon+Holm A−B 0.999, B−C 0.996, TOST equiv A−C 0.919;
    N=8 satisfaz superioridade (B−C 0.897) mas **não** potência de equivalência (0.788); N=6 é
    estruturalmente incapaz de significância Holm (menor p Wilcoxon 0.03125 > 0.0167); robustez
    com σ_e empírico satura ≥0.99. **Pré-registro formal v1.0 APROVADO** (2026-08-14): N=12,
    DV_confirm `(conf+ged_ref+ent)/3`, Friedman + Wilcoxon/Holm, TOST Δ=0.05, Go/No-Go ≥10/12,
    gates D-04/D-05, `taxonomy_sha256` por execução; tabela de diferenças vs GO-8C.
  - Artefatos:
    - `experiments/validation/GO-8D/decisions/D-07-POWER-N-RECALC.md` (relatório)
    - `experiments/validation/GO-8D/08-PRE-REGISTRATION-GO-8D.md` (pré-registro v1.0)
    - `experiments/validation/GO-8D/analysis/d07_power_recalc*.py`, `d07_power_results*.json`
  - **Aprovado pela governança (2026-08-14) — autoriza preparação do Lock GO-8D.**
- [x] **D-08 — Lock do GO-8D** — Congelar o núcleo do estudo: pré-registro, decisões
  (D-02..D-07), scripts reprojetados, taxonomia corrigida (C3_TAXONOMY.yaml), BIPs e referências
  externas do engine (GO-8B/GO-8C), com normalização UTF-8-no-BOM/LF/trailing-newline.
  - STATUS = **LOCKED** (2026-08-14) — **95 artefatos** congelados; 95/95 re-hash OK;
    record.manifest.sha256 = `b25dabcf…9f946f`; validação independente **PASS**
    (parse YAML, re-hash, normalização, consistência record↔manifest).
  - Artefatos:
    - `experiments/validation/GO-8D/GO-8D-LOCK-MANIFEST.yaml` (95 arquivos)
    - `experiments/validation/GO-8D/GO-8D-LOCK-RECORD.yaml`
    - `experiments/validation/GO-8D/analysis/d08_lock_build.json` (build info)
  - **Após o Lock, nenhum artefato incluído pode ser modificado; aguarda autorização de execução.**
- [x] **D-09 — Seed master GO-8D** — Decisão formal da governança do valor de `seed_master`.
  - STATUS = **APPROVED** (2026-08-14) — **seed_master = 20260815** (uint64), distinto do GO-8C
    (20260814); método PCG64 (SeedSequence(20260815, spawn_key=(bip, cond))) → 108 seeds únicas;
    `seed_statistics` = 14233797184859982032 (stream isolado).
  - Artefato: `experiments/validation/GO-8D/decisions/GO-8D-SEED-MASTER.md`
  - **Habilita a execução autorizada do estudo confirmatório.**
- [x] **EXEC-01 — Execução do estudo confirmatório (108 reconstruções)** — Autorizada pela
  governança (pré-registro v1.0 + Lock validado + seed_master aprovado).
  - STATUS = **EXECUTED** (2026-08-14) — **108/108 PASS**; validação **9/9 checks PASS**
    (schema, 36 células × 3 seeds, range [0,1], namespaces, taxonomy_sha256, D-04 12/12);
    **Go/No-Go = GO (12/12 casos ≥ 10)**.
  - Artefatos: `study-output/seeds_g8d.py`, `study-output/pilot_results_g8d.csv`,
    `study-output/data_validation_g8d.json`, `study-output/run_study_g8d.py`,
    `study-output/validate_data_g8d.py`.
  - **Próximo: análise estatística (§6) + relatório.**
- [x] **EXEC-02 — Análise estatística + relatório final** — Friedman df=2 α=0.05;
  Wilcoxon+Holm; TOST Δ=0.05; tamanhos de efeito.
  - STATUS = **DONE** (2026-08-14) — Friedman **p=0.000096** (W=0.7708); Wilcoxon+Holm
    **3/3 pares rejeitados** (A−B 0.0005, B−C 0.0024, A−C 0.0034); TOST Δ=0.05 **nenhum par
    equivalente** (A−C IC=(−0.0501,−0.0171) marginal); sensibilidade robusta.
  - Artefato: `study-output/STATISTICAL-REPORT-G8D.md`
  - **Decisão: GO metodológico; taxonomia C3 (B) com efeito negativo vs A na DV_confirm
    (todos os 12 BIPs) — sem evidência de utilidade da C3; equivalência A−C não demonstrada.**
  - [x] **CLS-01 — Encerramento formal do GO-8D** — Decisão final da governança (2026-08-14).
  - STATUS = **CLOSED** — resultados aprovados; hipótese C3 **rejeitada** (B<A em 12/12 BIPs);
    recomendação: não usar C3 como intervenção em futuros ciclos; nenhum GO-8E aberto.
  - Artefatos: `FINAL-PROJECT-REPORT-GO-8D.md`, `GO-8D-CLOSURE-PACKAGE.zip` (26 arquivos).

---

**ROADMAP (próximo gate):** **revisão de desenho concluída (D-03-DESIGN-REVIEW.md)** — **Opção C
aprovada pela governança** (D-04 ✓, D-06 ✓, D-05 ✓, D-07 ✓).
**D-04 concluído (5/5 PASS)** — gate de parseabilidade fechado. **D-06 APROVADO (Δ=0.05)** —
margem TOST formal. **D-05 PROPOSED** — protocolo do gate semântico híbrido desenhado.
**D-07 APROVADO** — **N recomendado = 12** (108 execuções); pré-registro v1.0 formal
(`08-PRE-REGISTRATION-GO-8D.md`) com DV_confirm + Δ=0.05 + gates D-04/D-05 + Go/No-Go ≥10/12.
**D-08 LOCKED** — **GO-8D LOCK MANIFEST/RECORD criados e validados (95 artefatos)**.
**D-09 APROVADO** — **seed_master = 20260815** (decisão formal da governança).
**EXEC-01 EXECUTED** — **108/108 reconstruções PASS**; validação 9/9; **Go/No-Go = GO (12/12)**.
**EXEC-02 DONE** — **Friedman p=0.000096**; **3/3 pares rejeitados pós-Holm**; TOST Δ=0.05
**nenhum par equivalente**; relatório `study-output/STATISTICAL-REPORT-G8D.md`.
**CLS-01 CLOSED** — **decisão final da governança: resultados aprovados; hipótese C3 rejeitada
(B<A em 12/12 BIPs); GO-8D ENCERRADO; recomendação: não usar C3 como intervenção; nenhum GO-8E.
Relatório final: `FINAL-PROJECT-REPORT-GO-8D.md`; pacote: `GO-8D-CLOSURE-PACKAGE.zip`.**

**Nota:** decisões GO-8D devem seguir o mesmo fluxo de governança
(proposta → decisão → pré-registro → Lock → execução → análise).
GO-8B e GO-8C permanecem CLOSED/LOCKED/FROZEN.

Nenhuma implementação, correção, coleta de dados, alteração de parâmetros, hash ou Lock
pode ocorrer até autorização formal por etapa.

---

**Fim do TODO — GO-8D CLOSED (2026-08-14). Dívidas DIAGNOSED/PROPOSED: D-01, D-02, D-03
(incl. revisão de desenho D-03.REV), D-04 (DIAGNOSED), D-05 (PROPOSED), D-06 (APPROVED),
D-07 (APPROVED), D-08 (LOCKED), D-09 (APPROVED), EXEC-01 (EXECUTED), EXEC-02 (DONE),
CLS-01 (CLOSED). Ciclo GO-8D encerrado; nenhum GO-8E aberto.