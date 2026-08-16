# GO-8D-NC — ACTION REGISTER (Registro de Ações)

**Data:** 2026-08-15
**Ciclo:** GO-8D-NC — **CLOSED** (Lock LOCKED, 14 artefatos)
**Regra:** nenhuma alteração em artefatos LOCKED/FROZEN do GO-8D-NC; GO-8C permanece CLOSED; GO-8D (anterior) permanece CLOSED; nenhuma execução de experimento autorizada sem decisão de governança.

---

## Ações

| ID | Descrição | Status | Artefato(s) | Validação |
|---|---|---|---|---|
| **OPEN-00** | Abertura formal do ciclo GO-8D-NC (autorização da governança, 2026-08-15): produção autorizada de materiais de entrada (narrativa Condição C + atomic facts A/B) para 18 novos BIPs (013–030), conforme GO-8D-NC Acquisition Plan v1; gate 30/30; sem execução experimental, sem seeds, sem commit, sem alteração de artefatos congelados | **COMPLETED** | `GO-8D-NC-LOCK-MANIFEST.yaml` · `BIP-013-bhopal` a `BIP-030-concordia` (materiais) | 18/18 BIPs produzidos e validados (LEXICON PASS + TRACE PASS); Lock GO-8D-NC íntegro (14/14 hashes) |
| **BATCH-01** | Produção de materiais para BIPs 013–017 (Bhopal, TMI, Challenger, Columbia, Katrina) | **COMPLETED** | `BIP-013-bhopal` a `BIP-017-katrina` (narrative/, atomic-facts/, 00-index.md) | 5/5 BIPs: LEXICON PASS + TRACE PASS; BIP-013 (188 fatos), 014 (195), 015 (147), 016 (221), 017 (290) |
| **BATCH-02** | Produção de materiais para BIPs 018–022 (Flint, Fukushima, Grenfell, Vajont, MAX8) | **COMPLETED** | `BIP-018-flint` a `BIP-022-max8` | 5/5 BIPs: LEXICON PASS + TRACE PASS; 018 (160), 019 (240), 020 (200), 021 (145), 022 (211) |
| **BATCH-03** | Produção de materiais para BIPs 023–027 (Mariana, Dieselgate, Wells Fargo, Theranos, Opioids) — Dieselgate com PDFs image-only (PNGs renderizados) | **COMPLETED** | `BIP-023-mariana` a `BIP-027-opioids` | 5/5 BIPs: LEXICON PASS + TRACE PASS; 023 (150), 024 (50, PNGs), 025 (120), 026 (110), 027 (100) |
| **BATCH-04** | Produção de materiais para BIPs 028–030 (Enron, Takata, Costa Concordia) | **COMPLETED** | `BIP-028-enron` a `BIP-030-concordia` | 3/3 BIPs: LEXICON PASS + TRACE PASS; 028 (50), 029 (60), 030 (63) |
| **SAN-01** | Saneamento dos 6 BIPs bloqueadores do GO-8C (001, 002, 004, 005, 006, 007) — remoção de placeholders `[refs...]` e reconstrução do BIP-007-ebola | **COMPLETED** | `BIP-001-deepwater` a `BIP-007-ebola` (narrative/, atomic-facts/, 00-index.md) | 6/6 BIPs: LEXICON PASS + TRACE PASS; 12/12 GO-8C BIPs agora PASS |
| **PRE-FLIGHT-01** | Pre-flight operacional GO-8D-NC — validação completa dos 30 BIPs (12 herdados + 18 novos) | **PASS** | `PRE-FLIGHT-REPORT-GO-8D-NC.md` | 30/30 BIPs: LEXICON PASS + TRACE PASS; Lock íntegro; 0 seeds; 0 execuções |
| **F1** | Geração de 270 seeds (seed_master=20260816) via `generate_seeds.py` | **PASS** | `scripts/seeds_nc.py` (SHA-256: `e7dd39648743023393042668484d3458042cbe34e196e08dcdcb74b578746275`) | 270 seeds únicas; 30 BIPs × 3 cond × 3 seeds; associação determinística; seed_master=20260816 confirmado |
| **F2** | Execução das 270 reconstruções (30 BIPs × 3 cond × 3 seeds) via `pilot_engine.py` | **PASS** | `study-output/pilot_results_newcycle.csv` (270 PASS, 0 FAIL) | 270/270 PASS; validação 9/9 checks PASS (schema, schema, seeds, bounds, namespace, taxonomy_sha, Go/No-Go); 30/30 BIPs válidos → GO |
| **F3** | Análise estatística via `analyze.py` (Friedman + Wilcoxon + Holm + TOST Δ=0.05 + complementar) | **COMPLETE** | `study-output/stats_newcycle.json` · `STATISTICAL-REPORT-GO-8D-NC.md` | Friedman χ²=38.47, p=4.44e-9 (W=0.641); Primária B<A: p=2.61e-8 (Cliff Δ=0.936); TOST A-C Δ=0.05: NOT EQUIVALENT; Complementar B<C: p=0.031 (Cliff Δ=0.24); Sensibilidade robusta; GO confirmado (30/30) |
| **AUDIT-01** | Auditoria de reprodução — re-execução da análise a partir de CSV/matriz congelados | **PASS** | `AUDIT-REPRODUCTION.md` | Efeitos idênticos (Cliff Δ: 0.936, 0.867, 0.240); Decisões idênticas; Diferenças apenas em p-valores intermedios (implementação lib) |
| **AUDIT-02** | Auditoria de aderência ao pré-registro v1.0 FINAL | **PASS** | `AUDIT-PREREG-ADHERENCE.md` | 0 desvios; Ordem de testes respeitada; Holm aplicado; Δ=0.05; Go/No-Go ≥27/30; 0 testes adicionais |
| **INT-01** | Interpretação sob governança — limitação explícita a DV3 | **COMPLETED** | `INTERPRETATION-GOVERNANCE.md` | Resultado limitado a DV3; sem causalidade, verdade, generalização; pergunta GO-8E formulada |
| **D-GO8E-01** | Diagnóstico "Por que C3 reduz a DV3?" — decomposição DV3 + TS-1..TS-4 + classificação H1/H2/H3 | **COMPLETE** | `D-GO8E-01-PROPOSAL.md` · `DIAGNOSTIC-REPORT-GO8E-01.md` | **Classificação: H3 (Interação)**; Score H3=7 vs H1=1, H2=1; **Recomendação: Decompor DV3; não usar média composta** |
| **CLS-01** | Encerramento D-GO8E-01 — aposentadoria da DV3 composta; separação de componentes | **CLOSED** | `CLOSURE-DECISION-D-GO8E-01.md` | DV3 1:1:1 aposentada para inferência confirmatória; conf/ged_ecp/ent_n12 como desfechos separados; regras para futuro definidas |
| **CLS-02** | Encerramento GO-8D-NC — ciclo completo encerrado | **CLOSED** | `CLOSURE-DECISION-GO-8D-NC.md` (previamente) | GO-8D-NC CLOSED; Lock LOCKED; 30/30 BIPs válidos; Lock íntegro |

---

## Lock Status

| Lock | Status | SHA-256 Manifest |
|---|---|---|
| **GO-8D-NC** | **LOCKED** (14/14 artefatos íntegros) | `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058` |
| **GO-8C** | **CLOSED / Lock LOCKED** | `b25dabcf...` (GO-8D manifest) |
| **GO-8B** | **CLOSED / LOCKED / FROZEN** | N/A (referência histórica) |

---

## Próximas Ações (Condicionais à Governança)

| ID | Ação | Status | Condição |
|---|---|---|---|
| **REDESIGN-01** | Redesign de mensuração (Fase 1: validação componentes; Fase 2: GED + diversidade) | **COMPLETED** | Fase 1: PASS; Fase 2: H3 confirmado; Relatório: MEASUREMENT-REDESIGN-PHASE1-REPORT.md, MEASUREMENT-REDESIGN-PHASE2-REPORT.md |
| **REDESIGN-02** | Encerramento redesign após Fase 2 (sem Fase 3) | **COMPLETED** | `CLOSURE-DECISION-MEASUREMENT-REDESIGN.md`; DV3 1:1:1 aposentada; conf/ged_ecp/ent_n12 separados |
| **POWER-01** | Cálculo de potência com novos componentes | **CANCELLED** | Redesign encerrado sem Fase 3 |
| **PREREG-01** | Pré-registro GO-8E | **CANCELLED** | Redesign encerrado sem Fase 3 |
| **EXP-01** | Experimento GO-8E | **CANCELLED** | Redesign encerrado sem Fase 3 |

---

## Estado Atual do GO-8D-NC

| Item | Status |
|---|---|
| **Ciclo** | **CLOSED** |
| **Lock** | **LOCKED** (14/14 artefatos íntegros) |
| **BIPs válidos** | 30/30 (12 herdados + 18 novos) |
| **Validação** | LEXICON PASS + TRACE PASS (100%) |
| **DV3 composta** | **APOSENTADA** para inferência confirmatória |
| **Desfechos** | conf, ged_ecp, ent_n12 (separados) |
| **D-GO8E-01** | **CLOSED** — H3 confirmado |
| **GO-8E** | **NÃO AUTORIZADO** — aguarda redesign + decisão |

---

**Última atualização:** 2026-08-15  
**Lock Manifest:** `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`