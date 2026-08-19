# MR-C7-REPORT-V2

## Gate MR-C7 (v2) — Validade Discriminante de Valor (DV-REDESIGN)
**Status da decisão:** **FAIL**

## 1. Identificação

| Item | Valor |
|------|-------|
| Pré-registro | `MR-C7-PROTOCOLO-PREREGISTRO-V2.md` (hash `5a926b77c8baaf722a8eea1eccba43320ce00b676306f3d0042f4b7c1bb2627f`) |
| Correção do gerador | `C-GENERATOR-FIX-V2-PARAPHRASE.md` (hash `d4a5b1b361137b42a7037ec885e8a217da99fd8bf8ef41cf767b9333ae8efa7b`) |
| `generate_cases.py` (corrigido) | `1340e462520ef73d1765cec34d7ad3b109b8876cc41a9459d7d2e68f0c108c9d` |
| `cases.yaml` (v2, regenerado) | `479692d5d4a20a010fe0ac71e238c39f40ef990aa881b3e02555c80269ba7184` |
| Addendum (consenso algorítmico) | `C-MODEL-SUBSTITUTION-ADDENDUM.md` (hash `4ce9fa87f0cd4fa6c0b33ffe2cc4ee5d27e3d998c142fce1c5ac60a9f13b4dc5`) |
| Casos | 24 sintéticos (N=24; seed_casegen=20260818) |
| Estados | V0 (baseline), V1 (correta+relevante), V2 (correta+redundante), V3 (falsa/ruidosa) |
| K_additional | 3 por estado (seed_draw=20260818) |
| seed_master reconstruções | 20260818 (3 seeds por caso, procedimento `generate_seeds.py` congelado) |
| δ_eq | 0.05 (banda de equivalência e piso de efeito) |
| α | 0.05 |

## 2. Nota interpretativa (registrada conforme determinação da governança)

> ged_ref tem limitação conhecida: a referência DATA-DRIVEN é construída só a partir de V0, então tende a não discriminar bem V1 de V3 — achado da v1, não corrigido nesta v2 (fora de escopo). Reportado por componente; não é sinal novo.

## 3. Ground truth — limitação (§5 e §5.1)

> O ground truth deste gate é **consenso algorítmico determinístico** (S-A/S-B/S-C), **ainda mais fraco** que consenso de IA. **Qualquer PASS é PROVISÓRIO**, pendente de reverificação com modelos de IA reais (três provedores distintos, versões correntes) antes de qualquer decisão de governança sobre o GO-8E.

## 4. Resumo executivo

| Métrica | Resultado |
|---------|-----------|
| Decisão | **FAIL** |
| compliance_rate | 0.0000 (exigência ≥ 0.80) |
| Invariância a seed | OK |
| Fidelidade §6.2 | PASS (média\|nós V1−V3\|=0.2500; média\|arestas V1−V3\|=0.2917) |
| Sinal residual tipo-C (§7.5.1c) | AUSENTE (0/72 fatos ΔV2 com overlap espúrio) |

### Valores médios por estado (composto e componentes, §7.5)

| Estado | DV (média) | conf (média) | ged_ref (média) | div_metric (média) |
|--------|------------|--------------|-----------------|--------------------|
| V0 | 0.893175 | 1.000000 | 0.682918 | 0.996605 |
| V1 | 0.903479 | 1.000000 | 0.712877 | 0.997561 |
| V2 | 0.874216 | 0.972470 | 0.682681 | 0.967497 |
| V3 | 0.868105 | 0.898809 | 0.710917 | 0.994588 |

## 5. Resultados por par (P1–P5)

| Par | Relação | Wilcoxon W | p | Holm PASS | N efetivo (≥15) |
|-----|---------|-----------|----|-----------|-----------------|
| P1 | V1 > V0 | 300.000 | 0.000004 | PASS | 24 |
| P2 | V1 > V2 | 300.000 | 0.000009 | PASS | 24 |
| P4 | V3 < V0 | 300.000 | 0.000008 | PASS | 24 |
| P5 | V3 < V2 | 285.000 | 0.000057 | PASS | 24 |

**P3 (TOST, δ_eq=0.05, V2 ≈ V0):** p_baixo=0.000009 (Wilcoxon W=0.000), p_alto=0.000009 (W=300.000) → **PASS**

## 5.1 Penalidade residual de conf(V2) via cadeia `follows` (§7.4 v2)

A verdade de V2 (G0 + self-loop do pai, excluída a cadeia `follows`) prevê penalidade residual de conf(V2) restrita às arestas `follows` não-entailed (~3/caso). Medido: média de arestas `follows` extras = **2.4583/caso**; penalidade média em conf = **0.021900** (conf(V2) = 0.972470; conf(V2) sem a penalidade = 0.994371). Δconf(V2)−V0 = **0.027530** (banda δ_eq = 0.05) → **dentro da banda**.

## 6. Compliance (§8.2)

compliance_rate = **0.0000** (exigência ≥ 0.80). Casos conformes: 0/24.

## 7. Pisos de efeito (§8.3, exigência > 0.05)

| Gap | Mediana | Exigência |
|-----|---------|-----------|
| mediana(DV(V1)-DV(V0)) | 0.009449 | > 0.05 → FAIL |
| mediana(DV(V1)-DV(V2)) | 0.029878 | > 0.05 → FAIL |
| mediana(DV(V0)-DV(V3)) | 0.024194 | > 0.05 → FAIL |
| mediana(DV(V2)-DV(V3)) | 0.006924 | > 0.05 → FAIL |

## 8. Controles

- **Fidelidade estrutural (§6.2):** PASS — média|nós V1−V3|=0.2500 (≤1.5), média|arestas V1−V3|=0.2917 (≤3.0), por caso |nós|≤3: OK
- **Invariância a seed (§7.5):** OK (saída idêntica nos 3 seeds derivados de seed_master=20260818).
- **Não-circularidade (§6.4):** rótulos fixados pelo gerador+consenso antes de qualquer cálculo de DV; decisão de §7.4 pré-registrada, irrevogável após inspeção de DV.

## 9. Vetos (§11)

| Veto | Condição | Status |
|------|----------|--------|
| V-A — Cegueira ao valor | ≥50% casos com \|DV(V1)−DV(V0)\|≤δ e \|DV(V3)−DV(V0)\|≤δ | ACIONADO (24/24 casos, 100.0%) |
| V-B — Integridade do rótulo | inspeção de código (addendum §5.3) | não acionado (inspeção PASS) |
| V-C — Controle quebrado | fidelidade §6.2 | não acionado |

### Checklist de inspeção de código (addendum §5.3)

Grafo de importação por script (módulos de fase4-v2 e externos):
- `generate_cases.py` → imports: os, re, sys, numpy, yaml, reconstruction
- `labelers.py` → imports: os, re, numpy, yaml, collections
- `reconstruction.py` → imports: os, re, json, hashlib, numpy, yaml
- `metric.py` → imports: os, json, math, sys, wl_kernel
- `analysis.py` → imports: os, re, json, math, hashlib, numpy, yaml, scipy, collections

Proibições verificadas: labelers.py não importa metric.py/reconstruction.py; metric.py não importa labelers.py; nenhum símbolo `def` de labelers.py é chamado em metric.py.
Símbolos compartilhados labelers×metric: **nenhum**

## 10. Regra de decisão (§8.4)

| Condição | Resultado |
|----------|-----------|
| P1-P5_Holm | PASS |
| P3_TOST | PASS |
| N_efetivo_ge_15 | PASS |
| compliance_ge_0.80 | FAIL |
| pisos_de_efeito | FAIL |
| fidelidade_6.2 | PASS |
| sem_veto | FAIL |
| sem_violacao_procedimento | PASS |
| **DECISÃO** | **FAIL** |

### Diagnóstico de causa (§7.5.1)

> Causa declarada: **(b)** — FAIL-tipo-B — diluição de agregação
>
> Suporte numérico: mediana(conf(V1)−conf(V3)) = 0.100840; mediana(DV(V1)−DV(V3)) = 0.033801 (piso δ_eq = 0.05).
>
> Verificação de sinal residual de FAIL-tipo-C (§7.5.1c): 0/72 fatos ΔV2 com overlap ≥ 2 em fatos-base não-pai → AUSENTE — resultado pode ser aceito como definitivo.
>
> Recomendação: revisar o esquema de agregação/pesos (§7.5.1), não os componentes. GO-8E permanece NÃO AUTORIZADO.

## 11. Hashes (SHA-256)

### Scripts (hash-lock antes da execução)

| Script | SHA-256 |
|--------|---------|
| `generate_cases.py` | `1340e462520ef73d1765cec34d7ad3b109b8876cc41a9459d7d2e68f0c108c9d` |
| `labelers.py` | `4664c0e693be33c9d09836cd986605c6345cab9aaac7ee9171ac15dd06825dfa` |
| `reconstruction.py` | `e337ce0b4bb8a25e7070889650541546a0c04f2cb77c356d0e07fcb677e7314e` |
| `metric.py` | `b2742d63e585bfc349a3e6cc3f14108de82c39badb4d6a2b33a788ac918829b4` |
| `analysis.py` | `c0bd7e13ac704fe1f1a6f73f99212f8c7100e17dfb2a1d75923562dc15762ca2` |

### Inputs e saídas intermediárias

| Artefato | SHA-256 |
|----------|---------|
| `cases.yaml` | `479692d5d4a20a010fe0ac71e238c39f40ef990aa881b3e02555c80269ba7184` |
| `states.yaml` | `b63c07e83adee6a1a9fc4546f7a4f58ab7a08d58dd773babd5cde2d60a77c985` |
| `consensus_registry.yaml` | `17d3a463e55cc5493e491978bc9100d1fcf8f16ee9b9a5d27837c09df86433b3` |
| `reconstruction_graphs.json` | `32998b993fdf00295df76cb6034db827de85aa820c701118e1b2fb61f8e80385` |
| `dv_values.json` | `fd9adbc7cf0287954422a711ac5d7beff6c9555771a013c10b2120496a934f99` |

### Artefatos de relatório (§13)

| Artefato | SHA-256 |
|----------|---------|
| `MR-C7-REPORT-V2.json` | `93e587dc9c40528da44f66c63dcc98ad4a681de42b0d84eae9c50d799a027584` |
| `MR-C7-CASE-REGISTRY-V2.yaml` | `61860c048ba3da8ea9e70c61350621bbb6d30411271b967e7fcccdaa5d79ce27` |
| `MR-C7-REPORT-V2.md` | (hash deste relatório — registrado externamente após a escrita) |

## 12. Consequências (§14)

Resultado válido e definitivo para este pré-registro (§9), **condicionado à verificação de sinal residual tipo-C** (§7.5.1c). GO-8E permanece NÃO AUTORIZADO. Redesenho recomendado conforme diagnóstico de causa mediante novo pré-registro.

**Assinatura:** Execução de gate MR-C7 v2 (consenso algorítmico, addendum 4ce9fa87...)
**Data:** 2026-08-19
