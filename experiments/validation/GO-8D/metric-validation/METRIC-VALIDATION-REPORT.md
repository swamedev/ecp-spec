# GO-8D — RELATÓRIO DE VALIDAÇÃO DA MÉTRICA (METRIC VALIDATION / CALIBRATION)

**Data:** 2026-08-14
**Fase:** METRIC VALIDATION — M-01..M-04 (sem novo experimento, sem coleta, sem novo Lock)
**Input:** `study-output/pilot_results_g8d.csv` + re-derivação determinística dos grafos das 36 células
**Scripts:** `metric-validation/calibrate_metrics.py`, `metric-validation/eval_criteria.py`
**Outputs:** `metric-validation/calibration_cells.json`, `metric-validation/criteria_eval.json`

**Validação da re-derivação (reprodutibilidade):** max|conf−conf_csv|=0.0, max|ged−ged_csv|=0.0,
max|ent−ent_csv|=0.0 → a re-derivação reproduz **exatamente** os valores do estudo confirmatório
(36 células; 108 linhas determinísticas). A calibração é, portanto, calculada sobre os **mesmos
dados** do GO-8D.

---

## 1. Definições das DVs Candidatas (M-04)

| DV | ent | ged_ref | Descrição |
|---|---|---|---|
| **DV0 (original)** | `ent_orig` = H/log(n_slots), n_slots=9 (A/C) ou 12 (B) | `ged_orig` (CAT_REF 9n vs SYN_REF 12n) | Como no estudo confirmatório |
| **DV1** | `ent_n12` = H/log(12) (denominador comum) | `ged_orig` | Entropia recalibrada (M-01/M-03) |
| **DV2** | `ent_orig` | `ged_ecp` (ECP_REF comum 9n) | GED recalibrada (M-02) |
| **DV3** | `ent_n12` | `ged_ecp` | Recalibração completa |

Todas com `conf` inalterado e média aritmética 1:1:1; clamp [0,1].

## 2. Tabela Comparativa das DVs (medianas de célula, N=12)

| DV | A | B | C | Δ B−A | B<A (n/12) | Friedman χ² (df=2) | p |
|---|---|---|---|---|---|---|---|
| **DV0 original** | 0.7134 | 0.6220 | 0.6843 | −0.0793 | 12/12 | 18.50 | 0.000096 |
| **DV1** (ent_n12) | 0.6770 | 0.6220 | 0.6536 | −0.0428 | 12/12 | 14.00 | 0.000912 |
| **DV2** (ged_ecp) | 0.6566 | 0.5890 | 0.6193 | −0.0716 | 12/12 | 15.17 | 0.000509 |
| **DV3** (completa) | 0.6205 | 0.5890 | 0.5885 | −0.0374 | **11/12** | 10.17 | 0.006199 |

> **Atenção:** NÃO se seleciona métrica pelo melhor p-valor (regra da etapa). DV0 tem o menor p,
> mas viola os critérios de cardinalidade/referência (ver §4). Todas rejeitam a hipótese nula.

## 3. Análise de Componentes Individuais (não apenas a média)

| Componente | A | B | C | Δ B−A | B<A (n/12) | Observação |
|---|---|---|---|---|---|---|
| conf | 0.7343 | 0.7369 | 0.7222 | −0.0010 | 7/12 | **neutra** (sem assimetria) |
| ged_orig | 0.4721 | 0.4172 | 0.4949 | −0.0590 | 11/12 | assimetria de referência (SYN 12n) |
| **ged_ecp** | 0.3171 | 0.3132 | 0.3138 | −0.0236 | 8/12 | referência comum; Δ pequeno e inconsistente |
| ent_orig | 0.9089 | 0.7297 | 0.8004 | −0.1985 | 12/12 | domina a queda; assimetria de n_slots |
| **ent_n12** | 0.8037 | 0.7297 | 0.7078 | −0.0897 | 11/12 | denominador comum; Δ reduzido ~55% |
| ent_n9 | 0.9089 | 0.8253 | 0.8004 | −0.1014 | 11/12 | denominador comum alternativo |
| ent_eff | 0.9331 | 0.8066 | 0.8963 | −0.1115 | 12/12 | evenness p/ suporte observado |
| H (bits) | 1.9971 | 1.8134 | 1.7587 | −0.2228 | 11/12 | entropia bruta — diferença real |
| k_obs | 9 | 9 | 8 | +0.5 | 4/12 | **suporte observado quase igual (9/9/8)** |

**Leituras críticas:**
1. **`k_obs` é praticamente igual entre A (9) e B (9)** — a queda de `ent` em B **não** vem de menos
   categorias distintas usadas, mas de distribuição **menos uniforme** dentro do mesmo suporte
   (H bruta B=1.8134 < A=1.9971). Logo há um **componente real** de concentração em B, independente
   do denominador.
2. **`ent_n12` reduz o Δ de −0.1985 para −0.0897** (55%) — metade da penalidade de `ent` era
   **artefato de denominador** (n_slots 12 vs 9); a outra metade é **real** (H mais baixa).
3. **`ged_ecp` quase elimina a vantagem de A** (Δ B−A −0.0236, 8/12) — a maior parte da diferença de
   `ged_orig` (−0.0590) era **assimetria de tamanho da referência** (SYN 12 nós vs CAT 9 nós);
   sob referência comum, A e B quase empatam estruturalmente.
4. **`conf` não contribui** para B<A (neutra em ambos os sentidos).

## 4. Avaliação dos 7 Critérios Pré-registrados

| Critério | DV0 (orig) | DV1 | DV2 | DV3 |
|---|---|---|---|---|
| **1. Invariância de escala entre condições** | ❌ (ent spread 0.281; n_slots 9/12) | ⚠️ (spread 0.249; denom comum) | ⚠️ | ⚠️→✅ |
| **2. Mesma cardinalidade de referência** | ❌ (n_slots 9 vs 12; refs 9n/12n) | ✅ ent (12) / ❌ ged (refs distintas) | ⚠️ ent / ✅ ged | ✅✅ |
| **3. Ausência de vantagem estrutural conhecida** | ❌ (SYN ref maior → B deflacionada; n_slots 12 → B penalizada) | ✅ ent / ❌ ged | ⚠️ ent / ✅ ged | ✅✅ |
| **4. Interpretabilidade** | ✅ (mas viés não transparente) | ✅ | ✅ | ✅ |
| **5. Estabilidade por BIP** | ⚠️ (ged std A=0.051) | ⚠️ | ✅ (ged_ecp std A=0.032) | ✅ |
| **6. Distinguir melhor/pior** | ✅ (mas inflado por viés) | ✅ | ⚠️ (ged_ecp range estreito 0.22–0.40) | ⚠️ |
| **7. Comportamento em dados sintéticos** | ⚠️ | ✅ (perfect>flat>collapse) | ✅ | ✅ |

**Testes sintéticos (critério 7) — ent_n12/ged_ecp:**
| Cenário | conf | ged_ecp | ent_n12 | ent_eff |
|---|---|---|---|---|
| perfect (1:1 ECP) | 1.000 | 1.000 | 0.884 | 1.000 |
| noisy (labels CAT, conf 0.5) | 0.500 | 0.443 | 0.884 | 1.000 |
| flat (2 categorias) | 0.900 | 0.562 | 0.276 | 0.991 |
| collapse (1 categoria) | 0.900 | 0.573 | **0.000** | **0.000** |

- `ent_n12`: monotonicidade correta perfect > flat > collapse (0.884 > 0.276 > 0.000). ✅
- `ent_eff`: **defeito** — `flat` (2 categorias uniformes) → 0.991 ≈ perfect, pois normaliza pelo
  suporte observado; **não distingue** reconstruções pobres que usam poucas categorias. ❌
- `ged_ecp`: perfect > noisy (1.0 > 0.44) ✅; mas flat/collapse ≈ 0.56–0.57 (estrutura dominante,
  labels pouco discriminam no espaço ECP) ⚠️.

## 5. Decisão de Recomendação

**Critérios atendidos por DV (contagem):**

| DV | ✅ totais (sobre 7) | ❌ | ⚠️ |
|---|---|---|---|
| DV0 original | 3 (4,6,7) | 3 (1,2,3) | 1 (5) |
| DV1 | 4 (2,3-ent,4,7) | 1 (2-ged,3-ged) | 2 |
| DV2 | 4 (2-ged,3-ged,4,7) | 1 (2-ent,3-ent) | 2 |
| **DV3** | **5** (1,2,3,4,5) | 0 | 2 (6) |

**Recomendação: a DV3 (recalibração completa: `conf + ged_ecp + ent_n12`)** é a **única** que
satisfaz simultaneamente os critérios de **invariância de escala (C1), cardinalidade de referência
comum (C2) e ausência de vantagem estrutural (C3)** — os três critérios específicos do problema
detectado na auditoria. Limitações: (a) `ged_ecp` tem faixa estreita (0.22–0.40) porque as
similaridades CAT/SYN→ECP por texto são baixas (0.12–0.28) — discriminação estrutural limitada;
(b) p=0.0062 (menor que DV0) — o que **não** deve ser usado como critério de escolha.

**Alternativas:**
- **DV1** se a governança julgar o mapeamento CAT/SYN→ECP (via text_emb) insuficientemente
  discriminativo: corrige o viés dominante (entropia), mantém o GED original (que, embora
  assimétrico, é o que teve validação no GO-8B).
- **Nenhuma DV é descartada por comportamento sintético**, mas `ent_eff` como componente é
  **rejeitada** (não distingue reconstruções pobres).

## 6. Impacto no Desenho Futuro

1. **Componente `ent`:** usar **denominador comum** — justificativa: (a) `k_obs` é 9/9/8 entre
   condições (suporte observado quase idêntico), então a diferença de `n_slots` (9 vs 12) não
   reflete a tarefa; (b) n_slots=12 (o maior) evita favorecer qualquer condição e mantém [0,1]
   realizável para todas; (c) documentar H bruta ao lado como diagnóstico.
2. **Componente `ged_ref`:** usar **referência comum** (ECP canônico de 9 nós) — remove a vantagem
   estrutural de tamanho; porém **melhorar o mapeamento de rótulos CAT/SYN→ECP** (embeddings
   diretos treinados/ajustados, não apenas `text_emb` das definições) para aumentar a
   discriminação semântica da GED.
3. **`conf`:** manter (neutra, estável, interpretável), mas reconhecer que carrega pouco sinal de
   condição — não deve ser o componente decisivo.
4. **Pesos 1:1:1:** reavaliar em ciclo futuro dado que `ent` concentrava 72.9% da queda; com a
   recalibração o desbalanço cai, mas uma ponderação baseada em discriminância empírica (não em
   p-valor) é recomendada.
5. **Interpretação qualitativa do GO-8D (B<A) permanece robusta:** mesmo na DV3 (a menos
   favorecida a A), B<A ocorre em 11/12 BIPs e Friedman p=0.006 — a conclusão "C3 não demonstrou
   utilidade" sobrevive à recalibração, embora com magnitude menor (Δ B−A −0.0793 → −0.0374).

## 7. Conclusão

- **DV0 (original) é problemática** — confirma o achado do POST-STUDY AUDIT (viés de calibração
  desfavorável a B, concentrado em `ent` por n_slots e em `ged` por tamanho de referência).
- **DV3 é a métrica calibrada recomendada** para futuras comparações A/B/C: atende 5/7 critérios
  plenamente e 0 violações diretas, com a ressalva de discriminação limitada do `ged_ecp`.
- **A conclusão qualitativa do estudo (C3 sem utilidade) é mantida** sob todas as métricas
  recalibradas — o efeito é real, porém a **magnitude** original era inflada.

---

**Fim do relatório. Etapa METRIC VALIDATION concluída — nenhum novo experimento, nenhuma coleta,
nenhum Lock criado/alteração de artefatos congelados (Lock GO-8D validado PASS, 95/95); arquivos
novos apenas em `metric-validation/`.