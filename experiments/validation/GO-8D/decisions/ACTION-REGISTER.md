# GO-8D — ACTION REGISTER (Registro de Ações)

**Data:** 2026-08-14
**Ciclo:** GO-8D — **OPENED (DIAGNOSTIC PHASE)** — abertura formal em continuidade ao diagnóstico D-01.
**Regra:** nenhuma alteração em arquivos do GO-8B (CLOSED / LOCKED / FROZEN) nem do GO-8C (CLOSED / Lock LOCKED); todas as operações dentro de `experiments/validation/GO-8D/`.

---

## Ações

| ID | Descrição | Status | Artefato(s) | Validação |
|---|---|---|---|---|
| **OPEN-00** | Abertura formal do ciclo GO-8D (decisão da governança, 2026-08-14): tratativa das dívidas herdadas do GO-8C com prioridade para validade da métrica e da taxonomia; GO-8C permanece CLOSED; nenhum experimento autorizado até D-01..D-07 concluídos e aprovados | **OPENED** | `GO-8D-OPENING-DECISION.md` · `TODO-GO-8D.md` · `GO-8D-STATE.md` · `decisions/ACTION-REGISTER.md` | GO-8B CLOSED/LOCKED/FROZEN e GO-8C CLOSED (Lock 151 artefatos LOCKED, validado PASS) — intactos; GO-8D = OPENED / DIAGNOSTIC PHASE |
| **D-01** | **Auditoria da métrica S_struct** (viés estrutural) — executada na fase de diagnóstico pré-abertura; diagnóstico concluído e incorporado à abertura | **DIAGNOSED** | `experiments/validation/GO-8C/decisions/D-01-SSTRUCT-AUDIT.md` (relatório, 2026-08-14) | Achados incorporados: métrica ≈ contagem de nós + degenerescência WL; anonimização uniforme elimina sinal de categoria; topologia dominada pelo parser; seeds vestigiais; condição B do N=12 não reproduzível com engine congelado (taxonomia D-03.7 vs congelada; BIP-007-B inconsistente); GO-8B/GO-8C intactos |
| **D-02** | Métricas alternativas (sensíveis a rótulo/categoria; DV confirmatória substituta/corrigida) | **DIAGNOSED** | `experiments/validation/GO-8D/decisions/D-02-METRICS-ANALYSIS.md` (relatório, 2026-08-14) · `experiments/validation/GO-8D/analysis/metrics_candidates.py` (diagnóstico) | M0..M6 avaliados sobre as 36 células do N=12 (reprodução 36/36); nenhuma candidata é DV confirmatória válida; M3-GED melhor discriminabilidade; M4 degenerada; ver relatório |
| **D-03** | Refinamento da taxonomia C3 / reprojeto do pipeline (wl_kernel rotulado, embeddings CAT corrigidos, granularidade padronizada, referência por condição, rastreabilidade de taxonomia) | **DIAGNOSED / PROPOSED** | `experiments/validation/GO-8D/decisions/D-03-PIPELINE-REDESIGN.md` (relatório, 2026-08-14) · `experiments/validation/GO-8D/analysis/pipeline_redesign_sim.py` · `pipeline_redesign_sim2.py` (simulações) | DV recomendada: `conf+ged_ref+ent` (Q=18.50, 12/12 valores distintos, corr(nós)=+0.19); WL rotulado sozinho degenerado (A=2/12); ged_ecp (D-02 M3) era artefato de embeddings CAT colapsados (Q=2.17 n.s. após correção); novo pré-registro + Lock necessários (D-06/D-07) |
| **D-03.REV** | **Revisão formal de desenho** (gate de governança antes de D-07): consolidação do desenho DV_confirm, comparação DV antiga vs nova, evidências de resolução das degenerescências, impacto no pré-registro/Lock e opções de sequência | **REVIEWED** | `experiments/validation/GO-8D/decisions/D-03-DESIGN-REVIEW.md` (2026-08-14) | DV_confirm Q=18.50 vs S_struct Q=9.50; 36/36 valores distintos vs 5/12 em A; corr(nós) +0.189 vs +0.346; recomenda **Opção C** (D-04 em paralelo; D-05/D-06 antes de D-07); nada executado além da revisão |
| **D-04** | Gate de parseabilidade (check no validador de produção) | **DIAGNOSED** | `decisions/D-04-PARSEABILITY.md` (relatório, 2026-08-14) · `scripts/validate_parseability.py` (validador) · `scripts/test_d04_parseability.py` (testes) · `analysis/d04_test_results.json` | **5/5 PASS** (tabela→FAIL, padrão→PASS, sem `## Fatos`→FAIL, <15 fatos→FAIL, 12/12 BIPs do GO-8C→PASS); fecha o gate gap `D-04-GATE-GAP-ENGINE-PARSEABILITY.md`; GO-8B/GO-8C intactos |
| **D-05** | Gate semântico híbrido (humano + IA) | **PROPOSED** | `decisions/D-05-HYBRID-SEMANTIC-GATE.md` (protocolo, 2026-08-14) | Protocolo em 3 camadas: L1 auditoria automatizada obrigatória (ALL PASS), L2 painel de ≥2 IAs independentes obrigatório (PASS unânime; votação proibida; divergência=STOP), L3 amostra humana opcional (ativação condicional; sem equivalência epistemológica); veredito por formulário de evidências; execução apenas na produção do próximo ciclo |
| **D-06** | Definição formal de Δ para TOST | **APPROVED** | `decisions/D-06-TOST-DELTA.md` (proposta, 2026-08-14) · `decisions/D-06-TOST-DELTA-APPROVED.md` (decisão formal, 2026-08-14) · `analysis/d06_delta_anchors.py` | Governança aprova **Δ=0.05** (5% da escala DV_confirm ∈ [0,1]); 0.10 rejeitada (R5-GOV-03); âncoras SD rejeitadas (0.008–0.021) por estrita demais; efeitos primários 0.069–0.079 > Δ; TOST vigente apenas no contexto GO-8D, condicionado a D-07; sem retroação em GO-8B/GO-8C |
| **D-07** | Recalcular N após estabilizar a métrica e o desenho | **APPROVED** | `decisions/D-07-POWER-N-RECALC.md` (relatório, 2026-08-14) · `08-PRE-REGISTRATION-GO-8D.md` (pré-registro v1.0 APROVADO, 2026-08-14) · `analysis/d07_power_recalc.py` · `analysis/d07_power_recalc_task.py` · `analysis/d07_power_results.json` · `analysis/d07_power_results_task.json` | **N recomendado = 12** (execuções 108 = 12×3×3); cenário C (efeitos A−B=0.079, B−C=0.069): Friedman 0.999, A−B 0.999, B−C 0.996, TOST equiv A−C 0.919; N=8 satisfaz superioridade mas não TOST (0.788); N=6 incapaz de significância Holm (discretude Wilcoxon); pré-registro formal aprovado pela governança → autoriza preparação do Lock GO-8D |
| **D-08** | **Lock do GO-8D** — congelar o núcleo do estudo (pré-registro, decisões, scripts reprojetados, taxonomia corrigida, BIPs) e validar | **LOCKED** | `GO-8D-LOCK-MANIFEST.yaml` (95 artefatos) · `GO-8D-LOCK-RECORD.yaml` · `analysis/d08_lock_build.json` | **95/95 re-hash OK**; record.manifest.sha256 = `b25dabcf…9f946f`; normalização UTF-8-no-BOM/LF/trailing-newline OK; registros vivos (ACTION/TODO/STATE) excluídos do Lock (convenção GO-8C); GO-8B/GO-8C intactos; após Lock, nenhum artefato pode ser modificado |
| **D-09** | **Seed master GO-8D** — decisão formal da governança do valor de `seed_master` (pré-registro §10 PENDING LOCK PROTOCOL) | **APPROVED** | `decisions/GO-8D-SEED-MASTER.md` (2026-08-14) | **seed_master = 20260815** (uint64); distinto do GO-8C (20260814); método PCG64 via SeedSequence(20260815, spawn_key=(bip, cond)), 3 uint64/célula; total 108 seeds únicas |
| **EXEC-01** | **Execução do estudo confirmatório** — 108 reconstruções autorizadas (pré-registro v1.0 + Lock validado) | **EXECUTED** | `study-output/seeds_g8d.py` (108 seeds) · `study-output/run_study_g8d.py` · `study-output/pilot_results_g8d.csv` · `study-output/validate_data_g8d.py` · `study-output/data_validation_g8d.json` · `study-output/analyze_g8d.py` · `study-output/stats_g8d.json` · `study-output/dv_matrix_g8d.npy` | **108/108 PASS**; validação 9/9 checks PASS (schema, 36 células×3 seeds, range [0,1], namespaces, taxonomy_sha256 B=`5ba63db7…` A/C=`c91fecfe…`, D-04 12/12); **Go/No-Go = GO (12/12 ≥ 10)** |
| **EXEC-02** | **Análise estatística + relatório** (pré-registro §6) | **DONE** | `study-output/STATISTICAL-REPORT-G8D.md` (2026-08-14) | Friedman χ²=18.50, df=2, **p=0.000096** (W=0.7708, efeito grande); Wilcoxon+Holm: **3/3 pares rejeitados** (A−B p=0.0005, B−C p=0.0024, A−C p=0.0034); TOST Δ=0.05: **nenhum par equivalente** (A−C IC=(−0.0501,−0.0171) marginal); sensibilidade robusta (todas p<0.05) |

---

## Detalhe OPEN-00 — Abertura formal do ciclo (OPENED)

- **Decisor:** Governança GO-8D.
- **Decisão:** abrir formalmente o GO-8D para tratar as dívidas herdadas do GO-8C, com prioridade
  para validade da métrica e da taxonomia. GO-8C permanece CLOSED; nenhum artefato de
  GO-8B/GO-8C será alterado. Nenhum experimento novo será autorizado até D-01..D-07 concluídos
  e aprovados.
- **Restrições:** nenhum arquivo do GO-8B/GO-8C alterado; nenhum Lock gerado nesta etapa;
  nenhuma dívida (D-02..D-07) executada.

## Detalhe D-01 — Diagnóstico da métrica S_struct (DIAGNOSED)

- **Executor:** Governança (fase de diagnóstico pré-abertura).
- **Referência:** `experiments/validation/GO-8C/decisions/D-01-SSTRUCT-AUDIT.md` (2026-08-14).
- **Conteúdo resumido:**
  - Mecanismo do platô 0.5875: `S_base(n) = n²/√((n²+3n)·176)`; `S_base(9)=0.5875120888504802`
    bit-idêntico para 5/7 BIPs A do piloto GO-8B e 6 células A do N=12.
  - Viés estrutural: anonimização uniforme (`wl_kernel.py:30`) elimina sinal de categoria;
    produto interno com o ECP ≈ n² (só o componente "neutral" da iteração 0 sobrepõe).
  - Sensibilidade baixa: condição A com 5 valores distintos em 12 células.
  - Topologia dominada pelo parser (follows temporal + co-ocorrência crua).
  - Seeds vestigiais para a DV (108 linhas = 36 valores únicos).
  - Reproducibilidade da condição B: 7/7 células B do N=12 exigem a taxonomia corrigida (D-03.7);
    o CSV BIP-007-B (10 nós/84 arestas/0.5950) corresponde à corrigida — execução uniforme; a
    lacuna é de rastreabilidade (engine não registra a taxonomia usada). [Corrigido após
    verificação direta do CSV; ver `D-02-METRICS-ANALYSIS.md` §Anexo]
- **Impacto:** achados servem de base para D-02 e D-03; não constituem decisão de correção.

---

| **CLS-01** | **Encerramento formal do GO-8D** — decisão final da governança: resultados aprovados; conclusão negativa para a hipótese C3; recomendação de não usar C3 como intervenção; nenhum GO-8E aberto | **CLOSED** | `FINAL-PROJECT-REPORT-GO-8D.md` · `GO-8D-CLOSURE-PACKAGE.zip` (26 arquivos) | GO-8D **CLOSED** (2026-08-14); relatório final + pacote de encerramento gerados; hipótese C3 **rejeitada** (B<A em 12/12 BIPs, Cliff δ=1.000) |

---

## PÓS-ESTUDO — AUDITORIA + METRIC VALIDATION + DECISÃO DE DESENHO (GO-8D, sem novo experimento)

| Ação | Descrição | Status | Artefatos | Resultado |
|---|---|---|---|---|
| **AUD-01** | **Auditoria pós-estudo** — decompor DV_confirm (conf/ged_ref/ent) e investigar se penaliza B sistematicamente | **COMPLETE** | `POST-STUDY-AUDIT-DECISION.md` · `decisions/POST-STUDY-DV-DECOMPOSITION.md` · `analysis/post_study_dv_audit.json` | `ent` domina (72.9% da queda B−A); B<A em 12/12; **assimetrias estruturais**: ent n_slots 9 vs 12; ged ref 9n vs 12n — **DV_confirm problemática para comparação entre condições** |
| **MV-01** | **Metric validation/calibration** — padronizar cardinalidade (M-01), referência GED (M-02), recalibrar entropia (M-03), comparar DVs candidatas (M-04) | **COMPLETE** | `metric-validation/METRIC-VALIDATION-REPORT.md` · `calibration_cells.json` · `criteria_eval.json` · scripts | DV0 rejeitada; **DV3 = (conf + ged_ecp + ent_n12)/3** atende 5/7 critérios; re-derivação reproduz CSV (erro 0.0); sintético perfect>noisy>flat>collapse |
| **D-MV-01** | **Aprovação da DV confirmatória** — DV3 aceita como candidata; pesos 1:1:1 justificados; faixa de ged_ecp aceita c/ limitação | **APPROVED** | `decisions/D-MV-01-DV-CONFIRMATORY.md` · `decisions/D-MV-01-APPROVED.md` | DV3 aceita; pesos 1:1:1 mantidos; ged_ecp: aceitável p/ condição, melhoria antes de uso absoluto |
| **D-MV-02** | **Recálculo de potência com DV3** — Monte Carlo calibrado (B=3.000), Friedman/Wilcoxon+Holm/TOST Δ=0.05 | **COMPLETE** | `decisions/D-MV-02-POWER-RECALC.md` · `metric-validation/power_dv3.py` · `power_summary.json` | **N=30** p/ TOST A−C poder≥0.80 sob efeito observado (0.804); S1: Friedman 8, Wilcoxon B−A 10, TOST 30; S2: 12/14/14 |
| **D-MV-03** | **Governance design decision** — N=30; TOST confirmatório; Δ=0.05; DV3; 18 novos BIPs | **APPROVED** | `decisions/D-MV-03-GOVERNANCE-DESIGN-DECISION.md` | **Desenho assumido: N=30 BIPs (270 execuções)**, TOST A−C confirmatório; autorizado planejar aquisição de 18 BIPs (sem coleta); próximo: pré-registro do novo ciclo |
| **PR-REG-01** | **Pré-registro do novo ciclo** (DV3, N=30, TOST Δ=0.05, 18 novos BIPs) | **APPROVED** | `08-PRE-REGISTRATION-NEW-CYCLE.md` (v1.0 FINAL, 2026-08-15) | **APROVADO** (2026-08-15) — decisões da governança incorporadas: **Go/No-Go ≥27/30 GO · 10–26/30 NO-GO exploratório · <10/30 STOP**; **hierarquia primária B<A (Friedman + Wilcoxon B−A) → secundária TOST A−C Δ=0.05 → complementar B−C**; N=30 justificado pela hipótese primária; sem coleta, sem Lock, sem execução; Lock GO-8D intocado |

**Fim do registro de ações. GO-8D CLOSED (2026-08-14) + pós-estudo AUD/MV concluído (2026-08-15).
Nenhum arquivo do GO-8B/GO-8C ou Lock GO-8D alterado. Sem coleta/experimento; pré-registro do novo
ciclo APROVADO (PR-REG-01, v1.0 FINAL); próximo passo: Lock do novo ciclo após autorização.