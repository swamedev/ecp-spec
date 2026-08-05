# EXP-SX001 — Challenger STS-51-L (Shadow Experiment 001)

| Campo | Valor |
|---|---|
| **Tipo** | Experimento científico (EXP-SX001) — Shadow Experiment 001 |
| **Status** | Em execução |
| **Data** | 2026-08-03 |
| **Autor** | Coordenação do Arquiteto-Chefe (execução: North Mini Code) |
| **Governado por** | [SHADOW-EXPERIMENTS](../SHADOW-EXPERIMENTS.md), [SHADOW-REPORT-001](../SHADOW-REPORT-001.md), [SX-SELECTION](../SX-SELECTION.md) |
| **Fase** | C2 — Evidence Production (infraestrutura metodológica **congelada**) |

> **Declaração do experimento:** submeter o Kernel do ECP a um problema complexo,
> histórico e **independente da sua própria especificação**. Medir o poder
> explicativo do ECP sobre o desastre do Challenger (STS-51-L) **sem** que o
> experimento dependa do vocabulário do ECP para coletar dados.

## Principio (reformulado pela coordenação 2026-08-03)

O SX-001 **não** responde "o Challenger confirma o ECP?". Responde:

> **Quanto do Challenger o ECP consegue explicar sem conhecer previamente a
> explicação oficial?**

Esta é a pergunta que o [SHADOW-EXPERIMENTS](../SHADOW-EXPERIMENTS.md) define
como a emergência espontânea das entidades. Tudo o que o SX-001 produz
**pertence ao experimento**, não ao framework. Nenhum artefato metodológico
(AD, RFC, LAW, schema, critério) é criado durante a execução. Limitações → 
[METHODOLOGICAL-DEBT](../../METHODOLOGICAL-DEBT.md).

## Estrutura

```
SX-001/
├── sources/          # Fontes primárias verificadas (Etapa 0)
├── narrative/        # Etapa 1 — Narrativa Original (zero ECP)
├── reconstruction/   # Etapa 2+3 — Atomic Facts + Reconstrução Cega
├── comparison/       # Etapa 4 — Alignment Analysis
├── signals/          # Etapa 5 — Signals suportados pelo alignment
├── report/           # Etapa 6 — EAR + conclusão
└── README.md         # Este manifesto
```

## Pipeline oficial (sequência congelada para este experimento)

```
Narrativa Original
      ↓
Atomic Facts
      ↓
Reconstrução Cega
      ↓
Alignment Analysis
      ↓
Signals
      ↓
EAR + Relatório
```

| Etapa | Artefato | Regra |
|---|---|---|
| 1 | `narrative/01-narrativa-original.md` | Fatos históricos. **Zero** vocabulário ECP. |
| 2 | `reconstruction/02-atomic-facts.md` | Decomposição em fatos mínimos. Sem interpretação. |
| 3 | `reconstruction/03-reconstrucao-cega.md` | Usa **só** os Atomic Facts + Kernel. Entidades **emergem**, não são impostas. |
| 4 | `comparison/04-alignment-analysis.md` | Narrativa × Reconstrução. MATCH/PARTIAL/NOT_EXPLAINED/NEW_INSIGHT. |
| 5 | `signals/05-signals.yaml` | Só Signals suportados pelo alignment. |
| 6 | `report/06-relatorio-ear.md` | EAR + conclusão. |

## Restrições (FASE C2 — infraestrutura congelada)

1. **Nada de LAW-H, LB, RFC, AD, schema ou critério novo** durante o SX-001.
2. Limitações do método → registradas **apenas** em
   [METHODOLOGICAL-DEBT.md](../../METHODOLOGICAL-DEBT.md), para a v1.1.
3. A especificação (ECP-000..ECP-010, schemas, critérios) **não é alterada**
   durante o experimento.
4. Observação e reconstrução usam vocabulário **neutro**; o mapeamento para
   entidades acontece **depois** (Etapa 3+).

## Resultado esperado

- Veredito de emergência espontânea das entidades do ECP no caso Challenger.
- Presença/ausência por entidade (ausência é dado).
- **`EAR(Challenger)`** — observação experimental de alinhamento (não conclusão;
  calibração é escopo do [P-0008 — Cross-Domain Validation](../../P-0008-CROSS-DOMAIN-VALIDATION.md)).
- Signals **candidatos** (Challenger é UMA ocorrência; RA-SIG-001 exige ≥2
  independentes).

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Manifesto do EXP-SX001. Estrutura sources/narrative/reconstruction/comparison/signals/report. Pipeline Narrativa → Atomic Facts → Reconstrução Cega → Alignment → Signals → EAR. |

---
> **Regra do teste:** uma boa teoria não cria os fenômenos que explica; ela os
> reconhece onde eles já existem.
