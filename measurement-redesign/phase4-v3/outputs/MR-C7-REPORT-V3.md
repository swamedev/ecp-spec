# MR-C7-REPORT-V3

## Gate MR-C7 (v3) — Validade Discriminante de Valor (DV-REDESIGN)
**Status da decisão:** **FAIL**

## 1. Identificação

| Item | Valor |
|------|-------|
| Pré-registro | `MR-C7-PROTOCOLO-PREREGISTRO-V3.md` (hash `26986e473d3ee7245810945af619ab945db545fed35d90185defe998e7ed440b`) |
| Correção do gerador (v2, herdada) | `C-GENERATOR-FIX-V2-PARAPHRASE.md` (hash `d4a5b1b361137b42a7037ec885e8a217da99fd8bf8ef41cf767b9333ae8efa7b`) |
| `generate_cases.py` (corrigido) | `1340e462520ef73d1765cec34d7ad3b109b8876cc41a9459d7d2e68f0c108c9d` |
| Addendum (consenso algorítmico) | `C-MODEL-SUBSTITUTION-ADDENDUM.md` (hash `4ce9fa87f0cd4fa6c0b33ffe2cc4ee5d27e3d998c142fce1c5ac60a9f13b4dc5`) |
| Casos | 24 sintéticos NOVOS (N=24; seed_casegen=20260819) — nenhum compartilhado com v1/v2 |
| Estados | V0 (baseline), V1 (correta+relevante), V2 (correta+redundante), V3 (falsa/ruidosa) |
| K_additional | 3 por estado (seed_draw=20260819) |
| seed_master reconstruções | 20260819 (3 seeds por caso, procedimento `generate_seeds.py` congelado) |
| Esquema P (decisório) | `DV_P = 0.6·conf + 0.2·ged_ref + 0.2·div_metric` |
| Esquema Q (diagnóstico) | `DV_Q = 0.7·conf + 0.3·div_metric` — anexo, nunca decisório |
| δ_eq | 0.05 (banda de equivalência e piso de efeito) |
| α | 0.05 |

## 2. Nota da governança sobre o que a v3 mede

> Nota da governança sobre o que a v3 mede: o piso de efeito V1−V3 já é matematicamente garantido pelo peso de conf sozinho (0.6 × ~0.10 ≈ 0.06 > 0.05), independente dos proxies estruturais. O teste real da v3 é se ged_ref/div_metric, com peso 0.2 cada, ainda distorcem o suficiente para derrubar compliance, pisos ou vetos em P3/P5 — não se conf funciona (estabelecido pela v2). Nenhum critério pré-registrado foi alterado.

## 3. Nota interpretativa (registrada conforme determinação da governança)

> ged_ref tem limitação conhecida: a referência DATA-DRIVEN é construída só a partir de V0, então tende a não discriminar bem V1 de V3 — achado da v1, não corrigido (fora de escopo). Reportado por componente; não é sinal novo.

## 4. Ground truth — limitação (§5 e §5.1)

> O ground truth deste gate é **consenso algorítmico determinístico** (S-A/S-B/S-C), **ainda mais fraco** que consenso de IA. **Qualquer PASS é PROVISÓRIO**, pendente de reverificação com modelos de IA reais (três provedores distintos, versões correntes) antes de qualquer decisão de governança sobre o GO-8E.

## 5. Resumo executivo

| Métrica | Resultado |
|---------|-----------|
| Decisão | **FAIL** |
| compliance_rate (DV_P) | 0.0000 (exigência ≥ 0.80) |
| Invariância a seed | OK |
| Fidelidade §6.2 | PASS (média\|nós V1−V3\|=0.1250; média\|arestas V1−V3\|=0.5417) |
| Sinal residual tipo-C (§7.5.1c) | AUSENTE (0/72 fatos ΔV2 com overlap espúrio) |

### Valores médios por estado (composto e componentes, §7.5)

| Estado | DV_P (média) | conf (média) | ged_ref (média) | div_metric (média) | DV_Q (média) |
|--------|--------------|--------------|-----------------|--------------------|--------------|
| V0 | 0.944935 | 1.000000 | 0.728309 | 0.996368 | 0.998910 |
| V1 | 0.953009 | 1.000000 | 0.769779 | 0.995264 | 0.998579 |
| V2 | 0.920374 | 0.970498 | 0.725678 | 0.964695 | 0.968757 |
| V3 | 0.894121 | 0.901306 | 0.771920 | 0.994768 | 0.929345 |

## 6. Resultados por par (P1–P5, sobre DV_P)

| Par | Relação | Wilcoxon W | p | Holm PASS | N efetivo (≥15) |
|-----|---------|-----------|----|-----------|-----------------|
| P1 | V1 > V0 | 299.000 | 0.000009 | PASS | 24 |
| P2 | V1 > V2 | 300.000 | 0.000009 | PASS | 24 |
| P4 | V3 < V0 | 300.000 | 0.000006 | PASS | 24 |
| P5 | V3 < V2 | 300.000 | 0.000009 | PASS | 24 |

**P3 (TOST, δ_eq=0.05, V2 ≈ V0):** p_baixo=0.000009 (Wilcoxon W=0.000), p_alto=0.000009 (W=300.000) → **PASS**

## 6.1 Penalidade residual de conf(V2) via cadeia `follows` (§7.4)

Média de arestas `follows` extras = **2.6250/caso**; penalidade média em conf = **0.023212** (conf(V2) = 0.970498; sem a penalidade = 0.993710). Δconf(V2)−V0 = **0.029502** (banda δ_eq = 0.05) → **dentro da banda**.

## 7. Compliance (§8.2, sobre DV_P)

compliance_rate = **0.0000** (exigência ≥ 0.80). Casos conformes: 0/24.

## 8. Pisos de efeito (§8.3, exigência > 0.05, sobre DV_P)

| Gap | Mediana | Exigência |
|-----|---------|-----------|
| mediana(DV_P(V1)-DV_P(V0)) | 0.007563 | > 0.05 → FAIL |
| mediana(DV_P(V1)-DV_P(V2)) | 0.033312 | > 0.05 → FAIL |
| mediana(DV_P(V0)-DV_P(V3)) | 0.050689 | > 0.05 → PASS |
| mediana(DV_P(V2)-DV_P(V3)) | 0.025822 | > 0.05 → FAIL |

## 9. Controles

- **Fidelidade estrutural (§6.2):** PASS — média|nós V1−V3|=0.1250 (≤1.5), média|arestas V1−V3|=0.5417 (≤3.0), por caso |nós|≤3: OK
- **Invariância a seed (§7.5):** OK (saída idêntica nos 3 seeds derivados de seed_master=20260819).
- **Não-circularidade (§6.4):** rótulos fixados pelo gerador+consenso antes de qualquer cálculo de DV; pesos e decisão de §7.4 pré-registrados, irrevogáveis após inspeção de DV.

## 10. Vetos (§11)

| Veto | Condição | Status |
|------|----------|--------|
| V-A — Cegueira ao valor | ≥50% casos com \|DV(V1)−DV(V0)\|≤δ e \|DV(V3)−DV(V0)\|≤δ | não acionado (4/24 casos, 16.7%) |
| V-B — Integridade do rótulo | inspeção de código (addendum §5.3) | não acionado (inspeção PASS) |
| V-C — Controle quebrado | fidelidade §6.2 | não acionado |

### Checklist de inspeção de código (addendum §5.3)

Grafo de importação por script (módulos de phase4-v3 e externos):
- `generate_cases.py` → imports: os, re, sys, numpy, yaml, reconstruction
- `labelers.py` → imports: os, re, numpy, yaml, collections
- `reconstruction.py` → imports: os, re, json, hashlib, numpy, yaml
- `metric.py` → imports: os, json, math, sys, wl_kernel
- `analysis.py` → imports: os, re, json, math, hashlib, numpy, yaml, scipy

Proibições verificadas: labelers.py não importa metric.py/reconstruction.py; metric.py não importa labelers.py; nenhum símbolo `def` de labelers.py é chamado em metric.py.
Símbolos compartilhados labelers×metric: **nenhum**

## 11. Regra de decisão (§8.4)

| Condição | Resultado |
|----------|-----------|
| P1-P5_Holm | PASS |
| P3_TOST | PASS |
| N_efetivo_ge_15 | PASS |
| compliance_ge_0.80 | FAIL |
| pisos_de_efeito | FAIL |
| fidelidade_6.2 | PASS |
| sem_veto | PASS |
| sem_violacao_procedimento | PASS |
| **DECISÃO** | **FAIL** |

### Diagnóstico de causa (§7.5.1)

> Causa declarada: **(b)*** — FAIL-tipo-B* — agregação nos testes de nível (V1 vs V0/V2); par V1×V3 discriminado por conf e pelo composto
>
> Suporte numérico: mediana(conf(V1)−conf(V3)) = 0.100840; mediana(DV_P(V1)−DV_P(V3)) = 0.058252 (piso δ_eq = 0.05).
>
> Verificação de sinal residual de FAIL-tipo-C (§7.5.1c): 0/72 fatos ΔV2 com overlap ≥ 2 em fatos-base não-pai → AUSENTE — resultado pode ser aceito como definitivo.
>
> Recomendação: revisar o esquema de agregação/pesos e a referência GED (os testes de nível V1 vs V0/V2 falham; o par V1×V3 é discriminado por conf). GO-8E permanece NÃO AUTORIZADO.

## 12. Anexo diagnóstico — Esquema Q (§7.1 v3; NUNCA decisório)

> Anexo diagnóstico exclusivamente; NUNCA fundamenta PASS/FAIL (§7.1/§13 v3).

| Estado | DV_Q (média) |
|--------|--------------|
| V0 | 0.998910 |
| V1 | 0.998579 |
| V2 | 0.968757 |
| V3 | 0.929345 |

| Gap DV_Q | Mediana |
|----------|---------|
| mediana(DV_Q(V1)-DV_Q(V0)) | 0.000000 |
| mediana(DV_Q(V1)-DV_Q(V2)) | 0.031333 |
| mediana(DV_Q(V0)-DV_Q(V3)) | 0.070588 |
| mediana(DV_Q(V2)-DV_Q(V3)) | 0.038688 |

## 13. Hashes (SHA-256)

### Scripts (hash-lock antes da execução)

| Script | SHA-256 |
|--------|---------|
| `generate_cases.py` | `0df9b05cd31d572cde90ec9d44eebb804c83d302353467e16a18c8ecb10b8012` |
| `labelers.py` | `844b4195bc335a886d88423ac0d7e22f49ad9f4d7bffa672839efc325c8d3531` |
| `reconstruction.py` | `f4212c454cad1d2e20cbc03b4bf1fc79b5cd23be95d823358a18db5b0d9f8349` |
| `metric.py` | `eceea6abb540edb59605ca0fbfb2059c993ad9404099faed2f433d608797daaa` |
| `analysis.py` | `2679ba0356bbd6813f7d6b655b3055a712b743d1a4625a77e6f6728d17bd5445` |

### Inputs e saídas intermediárias

| Artefato | SHA-256 |
|----------|---------|
| `cases.yaml` | `fab904cb62eb90b8b01f32444ebfbcf193825ab60183c728f10e6b0c0a4b856e` |
| `states.yaml` | `fe62f4c40f497185c3daf78acc3346eb5b5ae299ba43271f65eeef36603935db` |
| `consensus_registry.yaml` | `941dc8098dc4d306f4bd06566d0db98b9eedce3570f5db29e6db84298c9ea28b` |
| `reconstruction_graphs.json` | `0150563c34308840576d64fb70b7e7651377f0194d995df172c3fe0d62ba67e5` |
| `dv_values.json` | `cb78f7fdacc627061ec362aadd09bd06f549a85da77f4e1e6c779afdcc615403` |

### Artefatos de relatório (§13)

| Artefato | SHA-256 |
|----------|---------|
| `MR-C7-REPORT-V3.json` | `b9441e2bd700f47ef415e0697dc76137550046b604fb3ae61bab0367bf82d09d` |
| `MR-C7-CASE-REGISTRY-V3.yaml` | `fe188a98d1bc3c944b74097a76b7a8d0d44d7eac555be90b597c171564c7f55d` |
| `MR-C7-REPORT-V3.md` | (hash deste relatório — registrado externamente após a escrita) |

## 14. Consequências (§14)

Resultado válido e definitivo para este pré-registro (§9), **condicionado à verificação de sinal residual tipo-C** (§7.5.1c). GO-8E permanece NÃO AUTORIZADO. Redesenho recomendado conforme diagnóstico de causa mediante novo pré-registro.

**Assinatura:** Execução de gate MR-C7 v3 (consenso algorítmico, addendum 4ce9fa87...)
**Data:** 2026-08-19
