# MR-C7-REPORT

## Gate MR-C7 — Validade Discriminante de Valor (DV-REDESIGN)
**Status da decisão:** **FAIL**

## 1. Identificação

| Item | Valor |
|------|-------|
| Pré-registro | `MR-C7-PROTOCOLO-PREREGISTRO.md` (hash `380fc1281f685c9baaefa46c6ef69aaff2d88dc844ad37ae250a50ae90acefe3`) |
| Addendum (consenso algorítmico) | `C-MODEL-SUBSTITUTION-ADDENDUM.md` (hash `4ce9fa87f0cd4fa6c0b33ffe2cc4ee5d27e3d998c142fce1c5ac60a9f13b4dc5`) |
| Casos | 24 sintéticos (N=24; seed_casegen=20260818) |
| Estados | V0 (baseline), V1 (correta+relevante), V2 (correta+redundante), V3 (falsa/ruidosa) |
| K_additional | 3 por estado (seed_draw=20260818) |
| seed_master reconstruções | 20260818 (3 seeds por caso, procedimento `generate_seeds.py` congelado) |
| δ_eq | 0.05 (banda de equivalência e piso de efeito) |
| α | 0.05 |

## 2. Nota interpretativa (registrada conforme determinação da governança)

> S-C vota no eixo de relevância usando novidade estrutural, portanto casos rotulados V1 tendem a ter estrutura nova vs G0. Se ged_ref reagir a 'qualquer novidade estrutural' (V1 e V3 igualmente) em vez de distinguir novidade correta da ruidosa, isso NÃO é falha de S-C — é o próprio fenômeno que o gate existe para detectar. Faz parte do resultado, não do desenho.

## 3. Ground truth — limitação (§5 e §5.1)

> O ground truth deste gate é **consenso algorítmico determinístico** (S-A/S-B/S-C), **ainda mais fraco** que consenso de IA. **Qualquer PASS é PROVISÓRIO**, pendente de reverificação com modelos de IA reais (três provedores distintos, versões correntes) antes de qualquer decisão de governança sobre o GO-8E.

## 4. Resumo executivo

| Métrica | Resultado |
|---------|-----------|
| Decisão | **FAIL** |
| compliance_rate | 0.0000 (exigência ≥ 0.80) |
| Invariância a seed | OK |
| Fidelidade §6.2 | PASS (média\|nós V1−V3\|=0.2500; média\|arestas V1−V3\|=0.2917) |

### Valores médios de DV por estado

| Estado | DV (média) |
|--------|------------|
| V0 | 0.893175 |
| V1 | 0.903479 |
| V2 | 0.842263 |
| V3 | 0.868105 |

## 5. Resultados por par (P1–P5)

| Par | Relação | Wilcoxon W | p | Holm PASS | N efetivo (≥15) |
|-----|---------|-----------|----|-----------|-----------------|
| P1 | V1 > V0 | 300.000 | 0.000004 | PASS | 24 |
| P2 | V1 > V2 | 300.000 | 0.000009 | PASS | 24 |
| P4 | V3 < V0 | 300.000 | 0.000008 | PASS | 24 |
| P5 | V3 < V2 | 0.000 | 0.999991 | FAIL | 24 |

**P3 (TOST, δ_eq=0.05, V2 ≈ V0):** p_baixo=0.000009 (Wilcoxon W=0.000), p_alto=0.812200 (W=119.000) → **FAIL**

## 6. Compliance (§8.2)

compliance_rate = **0.0000** (exigência ≥ 0.80). Casos conformes: 0/24.

## 7. Pisos de efeito (§8.3, exigência > 0.05)

| Gap | Mediana | Exigência |
|-----|---------|-----------|
| mediana(DV(V1)-DV(V0)) | 0.009449 | > 0.05 → FAIL |
| mediana(DV(V1)-DV(V2)) | 0.061155 | > 0.05 → PASS |
| mediana(DV(V0)-DV(V3)) | 0.024194 | > 0.05 → FAIL |
| mediana(DV(V2)-DV(V3)) | -0.026554 | > 0.05 → FAIL |

## 8. Controles

- **Fidelidade estrutural (§6.2):** PASS — média|nós V1−V3|=0.2500 (≤1.5), média|arestas V1−V3|=0.2917 (≤3.0), por caso |nós|≤3: OK
- **Invariância a seed (§7.5):** OK (saída idêntica nos 3 seeds derivados de seed_master=20260818).
- **Não-circularidade (§6.4):** rótulos fixados pelo gerador+consenso antes de qualquer cálculo de DV; nenhum rótulo revisado após inspeção de DV.

## 9. Vetos (§11)

| Veto | Condição | Status |
|------|----------|--------|
| V-A — Cegueira ao valor | ≥50% casos com \|DV(V1)−DV(V0)\|≤δ e \|DV(V3)−DV(V0)\|≤δ | ACIONADO (24/24 casos, 100.0%) |
| V-B — Integridade do rótulo | inspeção de código (addendum §5.3) | não acionado (inspeção PASS) |
| V-C — Controle quebrado | fidelidade §6.2 | não acionado |

### Checklist de inspeção de código (addendum §5.3)

Grafo de importação por script (módulos de fase4 e externos):
- `generate_cases.py` → imports: os, re, numpy, yaml, reconstruction
- `labelers.py` → imports: os, re, numpy, yaml, collections
- `reconstruction.py` → imports: os, re, json, hashlib, numpy, yaml
- `metric.py` → imports: os, json, math, sys, wl_kernel
- `analysis.py` → imports: os, re, json, math, hashlib, numpy, yaml, scipy

Proibições verificadas: labelers.py não importa metric.py/reconstruction.py; metric.py não importa labelers.py; nenhum símbolo `def` de labelers.py é chamado em metric.py.
Símbolos compartilhados labelers×metric: **nenhum**

## 10. Regra de decisão (§8.4)

| Condição | Resultado |
|----------|-----------|
| P1-P5_Holm | FAIL |
| P3_TOST | FAIL |
| N_efetivo_ge_15 | PASS |
| compliance_ge_0.80 | FAIL |
| pisos_de_efeito | FAIL |
| fidelidade_6.2 | PASS |
| sem_veto | FAIL |
| sem_violacao_procedimento | PASS |
| **DECISÃO** | **FAIL** |

### Diagnóstico de causa (§7.5.1)

> Causa declarada: **(b)** — FAIL por diluição de agregação
>
> Suporte numérico: mediana(conf(V1)−conf(V3)) = 0.100840; mediana(DV(V1)−DV(V3)) = 0.033801 (piso δ_eq = 0.05).
>
> Recomendação: revisar o esquema de agregação/pesos (§7.5.1), não os componentes. GO-8E permanece NÃO AUTORIZADO.

## 11. Hashes (SHA-256)

### Scripts (hash-lock antes da execução)

| Script | SHA-256 |
|--------|---------|
| `generate_cases.py` | `4fc038adc479f09b749c4b16d50651c20ba034349f9f3788326ea5a9f254541d` |
| `labelers.py` | `4664c0e693be33c9d09836cd986605c6345cab9aaac7ee9171ac15dd06825dfa` |
| `reconstruction.py` | `98f7c6b951723a1e6b61dec9269a6fe91fa285d9046e7a1781973f20943e7a82` |
| `metric.py` | `e3b4769a12525749c7b0173a8a627717cc0ad04322448f9e2f9f88a5e8dfe62e` |
| `analysis.py` | `770e025979c476ab2a48fb91eb1edd41296e3de0e3473c378a19fc6846495403` |

### Inputs e saídas intermediárias

| Artefato | SHA-256 |
|----------|---------|
| `cases.yaml` | `020205473d5459941d7e4e5d4e254e2a6760ba1ef47e28354675eaa0c2523c85` |
| `states.yaml` | `786ad723e913d7993d8b341273253da7e22f40f079ef559ae71f1be8023d0688` |
| `consensus_registry.yaml` | `83ac4f823a9272e5460bc63ddffd6fe4e129b0cc4d3a3cf37c0b96a692046c9a` |
| `reconstruction_graphs.json` | `df0b7d36930e400d0b604539bc2c015f2311d69cb6fd0f3739052acff6b9ee66` |
| `dv_values.json` | `f11be1ef3ca52499d9a3a377c80b3fdfbdac69024b54015746163d9920e4fdd7` |

### Artefatos de relatório (§13)

| Artefato | SHA-256 |
|----------|---------|
| `MR-C7-REPORT.json` | `044197eebd2e32f883d419b35bc66df8ed144123c900b31d9d00c7c809af54ef` |
| `MR-C7-CASE-REGISTRY.yaml` | `ea0e358245c43f2db9d74ec5eba02be5e5b4578f7af654b8e3e93e05ca95ab41` |
| `MR-C7-REPORT.md` | (hash deste relatório — registrado externamente após a escrita) |

## 12. Consequências (§14)

Resultado válido e definitivo para este pré-registro (§9). GO-8E permanece NÃO AUTORIZADO. Redesenho recomendado conforme diagnóstico de causa (§7.5.1) mediante novo pré-registro.

**Assinatura:** Execução de gate MR-C7 (consenso algorítmico, addendum 4ce9fa87...)
**Data:** 2026-08-19
