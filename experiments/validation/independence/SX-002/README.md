# EXP-SX002 — Resposta à Epidemia de Ebola na África Ocidental (Shadow Experiment 002)

| Campo | Valor |
|---|---|
| **Tipo** | Experimento científico (EXP-SX002) — Shadow Experiment 002 |
| **Status** | Em execução |
| **Data** | 2026-08-04 |
| **Autor** | Coordenação (Seleção formal pelo [SX-SELECTION](../../SX-SELECTION.md); execução sob pipeline congelado) |
| **Governado por** | [SHADOW-EXPERIMENTS](../../SHADOW-EXPERIMENTS.md), [SX-SELECTION](../../SX-SELECTION.md), [SX-REAUDIT.yaml](../../SX-REAUDIT.yaml), [P-0010](../../P-0010-REPRODUCIBILITY.md) (gate satisfeito) |
| **Fase** | E — Stability (pipeline congelado; só produção de evidência) |

> **Declaração do experimento:** submeter o Kernel do ECP a um caso complexo,
> histórico e independente da especificação, em domínio **distinto** do
> Challenger (Saúde/Biomédica), selecionado **pelo protocolo congelado** após a
> satisfação do gate P-0010 (reprodutibilidade). Medir o poder explicativo do ECP
> sobre a resposta à epidemia de Ebola na África Ocidental (2014–2016) **sem** que
> o experimento dependa do vocabulário do ECP para coletar dados.

## Princípio

O SX-002 **não** responde "o Ebola confirma o ECP?". Responde:

> **O que o protocolo produz quando aplicado a um caso independente de outro
> domínio?**

A pergunta central é a da **emergência espontânea das entidades** — agora em um
domínio metodologicamente distinto do Challenger (saúde pública / resposta de
emergência, não falha de engenharia física). O caso foi selecionado **pelo
protocolo** (SX-SELECTION) entre os candidatos re-auditados (SELECTABLE), com
direção de domínio imposta pelo gate do P-0010 (Saúde + redundante biomédico,
sem o caso mais famoso).

## Estrutura

```
SX-002/
├── sources/          # Etapa 0 — Fontes primárias verificadas
├── narrative/        # Etapa 1 — Narrativa Original (zero ECP)
├── reconstruction/   # Etapa 2+3 — Atomic Facts + Reconstrução Cega
├── comparison/       # Etapa 4 — Alignment Analysis
├── signals/          # Etapa 5 — Signals
├── report/           # Etapa 6 — EAR + conclusão
└── README.md         # Este manifesto
```

## Pipeline oficial (sequência congelada)

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
| 0 | `sources/00-fontes.md` | Fontes primárias verificadas e públicas. |
| 1 | `narrative/01-narrativa-original.md` | Fatos históricos. **Zero** vocabulário ECP. |
| 2 | `reconstruction/02-atomic-facts.md` | Decomposição em fatos mínimos. Sem interpretação. |
| 3 | `reconstruction/03-reconstrucao-cega.md` | Usa **só** os Atomic Facts + Kernel. Entidades **emergem**, não são impostas. |
| 4 | `comparison/04-alignment-analysis.md` | Narrativa × Reconstrução. MATCH/PARTIAL/NOT_EXPLAINED/NEW_INSIGHT. |
| 5 | `signals/05-signals.yaml` | Só Signals suportados pelo alignment. |
| 6 | `report/06-relatorio-ear.md` | EAR + conclusão. |

## Restrições (FASE E — pipeline congelado)

1. Nenhuma metodologia, ferramenta, schema, métrica ou infraestrutura nova criada.
2. Nenhum protocolo congelado alterado (SX-SELECTION, SX-REAUDIT, SX-QUEUE,
   P-0010, SHADOW-EXPERIMENTS).
3. Não utilizar o resultado do P-0010 como hipótese a confirmar; não forçar o
   caso a reproduzir o padrão do Challenger; não procurar deliberadamente
   divergências nem convergências.
4. Trabalhar exclusivamente com **evidência efetivamente disponível** para o
   caso; preservar a proveniência.
5. Observações registradas **depois** de executar as etapas correspondentes;
   resultados não são alterados posteriormente para melhorar coerência.
6. Dificuldade metodológica real → registrar como **observação** (DL), não mudar
   o protocolo durante a execução.

## Resultado esperado

- Veredito de emergência espontânea das entidades do ECP no caso Ebola (novo
  domínio: saúde pública / resposta de emergência).
- Presença/ausência por entidade (ausência é dado).
- **`EAR(Ebola)`** — observação experimental de alinhamento (não conclusão).
- Signals e ocorrências registradas conforme RA-SIG-001 (sem promoção).

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-04 | Manifesto do EXP-SX002. Seleção pelo protocolo após gate P-0010 satisfeito. Estrutura de pipeline replicada do SX-001. |