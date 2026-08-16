# MEASUREMENT-REDESIGN-PHASE1-REPORT.md

**Fase 1 — Validação Independente dos Componentes (conf, ged_ecp, ent_n12)**
**Data:** 2026-08-15
**Status:** **FASE 1 COMPLETE — GOVERNANCE REVIEW PENDING**
**Autorização:** Governança (D-GO8E-01 Fase 1 autorizada)

---

## 1. Resumo Executivo

A Fase 1 do redesign de mensuração validou independentemente os três componentes da DV3 composta aposentada (`conf`, `ged_ecp`, `ent_n12`), utilizando exclusivamente os 270 resultados congelados do GO-8D-NC (30 BIPs × 3 condições × 3 seeds), sem coleta de novos dados, sem geração de seeds, sem experimento.

**Resultado:** Todos os três componentes apresentam falhas de validade **CONDITIONAL** — cada um com problemas específicos que impedem o uso da DV3 composta 1:1:1 para inferência confirmatória.

**Recomendação:** **PROCEED para Fase 2** (investigação de GED com referências neutras + métricas de diversidade alternativas).

---

## 2. Resultados por Componente

### 2.1 Componente `conf` (Confiança de Classificação)

| Métrica | Resultado | Status |
|---------|-----------|--------|
| **Validade convergente** (correlação com DV3) | Pearson r = 0.53, Spearman ρ = 0.35 | **FRACA** |
| **Validade discriminante** (Friedman) | χ² = 36.6, p = 1.13×10⁻⁸ | **PASS** — distingue condições |
| **Wilcoxon A>B** | stat=176, p=0.88 | NS (A não > B) |
| **Wilcoxon B>C** | stat=446, p<0.001 | **PASS** (B > C) |
| **Wilcoxon A>C** | stat=463, p<0.001 | **PASS** (A > C) |
| **Estabilidade (ICC proxy A-B)** | r = 0.79 | **BOA** |
| **Sensibilidade a ruído** (σ=0.01→0.2) | r: 0.85 → 0.31 → 0.20 → -0.09 | **ACEITÁVEL** (decaimento suave) |
| **ICC proxy (A-B)** | r = 0.79 | **BOA** |

| Critério | Status |
|----------|--------|
| Validade convergente (ρ ≥ 0.7 com DV3) | **FALHA** (r=0.53) |
| Validade discriminante | **PASS** |
| Estabilidade | **PASS** |
| Sensibilidade a ruído | **PASS** |
| **Overall** | **CONDITIONAL** |

> **Problema:** `conf` tem baixa convergência com DV3 total (r=0.53), indicando que captura variância ortogonal à DV3 composta.

---

### 2.2 Componente `ged_ecp` (Similaridade Estrutural à Referência ECP)

| Métrica | Resultado | Status |
|---------|-----------|--------|
| **Medianas (A/B/C)** | 0.306 / 0.293 / 0.303 | — |
| **Friedman** | χ² = 6.07, p = 0.048 | **PASS** (marginal) |
| **Wilcoxon A>B** | stat=342, p=0.012 | **PASS** (A > B) |
| **Wilcoxon B>C** | stat=234, p=0.49 | NS |
| **Cliff Δ (A vs B)** | 0.28 | **PEQUENO/MÉDIO** |
| Correlação com DV3 | r = 0.58 | **MODERADA** |
| **Viés estrutural (CAT/SYN)** | ged_ecp usa referência ECP (CAT); B usa taxonomia SYN → **viés inerente a favor de A/C** | **FALHA CRÍTICA** |
| Sensibilidade a perturbação (5-20%) | r: 0.998 → 0.99 → 0.98 | **ESTÁVEL** |

| Critério | Status |
|----------|--------|
| Viés de referência (CAT vs SYN) | **FALHA** — viés inerente a favor de A/C |
| Validade discriminante | **PASS** (marginal) |
| Sensibilidade a perturbação | **PASS** |
| **Overall** | **CONDITIONAL** |

> **Problema crítico:** `ged_ecp` usa grafo de referência ECP (taxonomia CAT, 9 nós). Condição B usa taxonomia SYN (12 nós), criando **viés estrutural inerente** a favor de condições que usam CAT (A e C). Isso infla artificialmente a diferença A>B.

---

### 2.3 Componente `ent_n12` (Entropia Normalizada log(12))

| Métrica | Resultado | Status |
|---------|-----------|--------|
| **Medianas (A/B/C)** | 0.83 / 0.735 / 0.65 | — |
| **Friedman** | χ² = 35.47, p = 1.99×10⁻⁸ | **PASS** |
| **Wilcoxon A>B** | stat=455, p<0.001 | **PASS** (A > B) |
| **Wilcoxon B>C** | stat=339, p=0.014 | **PASS** (B > C) |
| **Cliff Δ (A vs B)** | 0.83 | **MUITO GRANDE** |
| **Cliff Δ (B vs C)** | 0.24 | **PEQUENO/MÉDIO** |
| Correlação com DV3 | r = 0.95 | **MUITO FORTE** |
| **Viés de cardinalidade** | log(12) normaliza para 12 slots; CAT máx=log(9)/log(12)=**0.884**; SYN máx=1.0 | **FALHA CRÍTICA** |
| Entropia máx CAT (9 cats) | 0.884 | — |
| Entropia máx SYN (12 cats) | 1.000 | — |

| Critério | Status |
|----------|--------|
| Viés de cardinalidade | **FALHA CRÍTICA** — teto artificial para CAT (0.884 vs 1.0) |
| Validade discriminante | **PASS** |
| Sensibilidade | **PASS** |
| Correlação com DV3 | **MUITO FORTE** (r=0.95) |
| **Overall** | **CONDITIONAL** |

> **Problema crítico:** `ent_n12` usa log(12) como normalizador fixo. Condição A (CAT, 9 categorias máx) tem teto teórico 0.884, enquanto B e C (SYN, até 12 categorias) podem atingir 1.0. Isso cria **viés de teto** que penaliza artificialmente a condição A e infla a diferença A-B (83% da queda DV3 vem de ent_n12).

---

## 3. Síntese de Validade

| Componente | Validade Convergente | Validade Discriminante | Estabilidade | Sensibilidade | Viés Estrutural | Overall |
|------------|---------------------|------------------------|--------------|---------------|-----------------|---------|
| **conf** | ❌ FALHA (r=0.53) | ✅ PASS | ✅ PASS | ✅ PASS | — | **CONDITIONAL** |
| **ged_ecp** | ⚠️ FRACA (r=0.58) | ⚠️ MARGINAL | ✅ PASS | ✅ PASS | ❌ **VIÉS CAT/SYN** | **CONDITIONAL** |
| **ent_n12** | ✅ FORTE (r=0.95) | ✅ PASS | ✅ PASS | ✅ PASS | ❌ **VIÉS CARDINALIDADE** | **CONDITIONAL** |

> **Conclusão:** **Nenhum componente atinge validade plena (PASS pleno)**. Todos são **CONDITIONAL** devido a falhas específicas:
> - `conf`: baixa convergência com DV3
> - `ged_ecp`: viés estrutural CAT/SYN (referência ECP)
> - `ent_n12`: viés de cardinalidade (log(12) vs 9 categorias CAT)

---

## 4. Recomendação para Fase 2

> **RECOMENDAÇÃO: PROCEED para Fase 2**
>
> **Justificativa:**
> 1. **ged_ecp** tem viés estrutural CAT/SYN confirmado (referência ECP = CAT)
> 2. **ent_n12** tem viés de cardinalidade crítico (teto 0.884 vs 1.0)
> 3. A média composta 1:1:1 falha em robustez (TS-2: 19/19 inversões; TS-3: geométrica/harmônica invertem; TS-4: contrafactual falha)
> 3. A decomposição confirma **H3 (Interação)**: trade-offs entre componentes mascarados pela média 1:1:1
>
> **Próximo passo:** Fase 2 — investigar referências GED neutras (CAT, SYN, UNION, NEUTRAL, DATA-DRIVEN) e métricas de diversidade alternativas a `ent_n12`.

---

## 5. Conformidade com Regras de Governança

| Regra | Status |
|-------|--------|
| Sem cálculo de potência | ✅ CUMPRIDO |
| Sem pré-registro | ✅ CUMPRIDO |
| Sem novos BIPs | ✅ CUMPRIDO |
| Sem novas seeds | ✅ CUMPRIDO |
| Sem experimento | ✅ CUMPRIDO |
| Sem alteração de Locks | ✅ CUMPRIDO (GO-8D-NC LOCKED íntegro) |
| Não usar A > B para escolher métrica | ✅ CUMPRIDO |
| Não escolher pesos retrospectivamente | ✅ CUMPRIDO |

---

## 6. Arquivos Gerados

| Arquivo | Descrição |
|---------|-----------|
| `study-output/phase1_validation_results.json` | Resultados completos (JSON) |
| `MEASUREMENT-REDESIGN-PHASE1-REPORT.md` | Este relatório |

---

## 7. Recomendação para Governança

> **FASE 1 COMPLETE — GOVERNANCE REVIEW PENDING**
>
> A Fase 1 identificou falhas de validade estruturais em `ged_ecp` (viés CAT/SYN) e `ent_n12` (viés de cardinalidade), confirmando a classificação **H3 (Interação)** do diagnóstico D-GO8E-01.
>
> **Recomendação:** **AUTORIZAR FASE 2** — investigar referências GED neutras (CAT, SYN, UNION, NEUTRAL, DATA-DRIVEN) e métricas de diversidade alternativas a `ent_n12` (Shannon, Simpson, Hill, Chao1, Rao QE), mantendo a proibição de usar A>B para seleção de métrica.

---

## 7. Estado Atual

| Item | Status |
|------|--------|
| **FASE 1** | **COMPLETE** |
| **D-GO8E-01** | **CLOSED** (H3 confirmado) |
| **GO-8D-NC** | **CLOSED / LOCKED** |
| **Próximo** | **Aguardando autorização para Fase 2** |

---

**Assinatura:** Fase 1 Validação Independente — GO-8D-NC Redesign  
**Data:** 2026-08-15  
**Lock Manifest:** `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`