# EXP-SX003 — Projeto Genoma Humano (Shadow Experiment 003)

| Campo | Valor |
|---|---|
| **Tipo** | Experimento científico (EXP-SX003) — Shadow Experiment 003 |
| **Status** | **PARADO (GO-5A decidido)** — NÃO PROMOVER · NÃO DESCARTAR · Transversal **BLOQUEADO**; SEM commit |
| **Data** | 2026-08-09 |
| **Autor** | Protocolo SX-SELECTION + direção de escopo pré-registrada (coordenação) |
| **Governado por** | [SHADOW-EXPERIMENTS](../SHADOW-EXPERIMENTS.md), [SX-SELECTION](../SX-SELECTION.md), [SX-REAUDIT.yaml](../SX-REAUDIT.yaml), [SHADOW-REPORT-003](../SHADOW-REPORT-003.md), [00-pre-registro.md](./00-pre-registro.md) |
| **Fase** | E — Stability (pipeline congelado; só produção de evidência) |
| **Dívida atacada** | [DEBT-009](../METHODOLOGICAL-DEBT.md) — amostra seletiva de casos de crise/falha |

> **Declaração do experimento:** submeter o Kernel do ECP a um caso de **desfecho
> classificado a priori como sucesso** (Projeto Genoma Humano, 1990–2003), em
> domínio distinto dos anteriores (Pesquisa Científica contra Aeroespacial e
> Saúde). Testar se a estrutura e as ausências observadas nos SX-001 e SX-002
> (crise/falha) também emergem em um sucesso — **sem** que o experimento dependa
> do vocabulário do ECP para coletar dados, e **sem** alterar nenhum critério de
> elegibilidade do SX-SELECTION.

## Princípio

O SX-003 **não** responde "o Genoma confirma o ECP?". Responde:

> **O que o protocolo produz quando aplicado a um caso cujo desfecho é
> pré-classificado como SUCCESS?**

É o **primeiro caso de sucesso** do programa (compare-se Challenger ≠ Ebola
até aqui). Objetivo
central: testar a fragilidade [DEBT-009](../METHODOLOGICAL-DEBT.md): nos dois
casos de crise/falha a estrutura ECP emergiu com ausências características;
em um sucesso, essa mesma estrutura emerge, reverte ou se rompe? Ausência é
dado. Não se procura deliberadamente divergência nem convergência.

## Fronteira GO-1 ↔ GO-2

```
GO-1 (concluído)  → 00-pre-registro.md + SHADOW-REPORT-003.md (seleção)
        ↓
[ PARAR — revisão da coordenação ]
        ↓
GO-2 (execução)   →  pipeline congelado (fontes → narrativa → AF → reconstrução
                     cega → alignment → signals → EAR → relatório → commit)
```

## GO-1 — Entregues

- `00-pre-registro.md` — direção (caso de sucesso) + **definição operacional de
  "sucesso" (SUC-1..SUC-3) fixadas ANTES da escolha**.
- Seleção registrada em [SHADOW-REPORT-003](../SHADOW-REPORT-003.md) —
  **Projeto Genoma Humano (1990–2003)**, domínio Pesquisa Científica.
- Fontes pré-gate já em [candidates/genoma-humano/sources](../candidates/genoma-humano/sources/)
  (promovem para `sources/` no GO-2).

## Estrutura (após GO-2)

```
SX-003/
├── sources/          # Etapa 0 — Fontes primárias verificadas
├── narrative/        # Etapa 1 — Narrativa Original (zero ECP)
├── reconstruction/   # Etapa 2+3 — Atomic Facts + Reconstrução Cega
├── comparison/       # Etapa 4 — Alignment Analysis
├── signals/          # Etapa 5 — Signals
├── report/           # Etapa 6 — EAR + conclusão
├── 00-pre-registro.md
└── README.md         # Este manifesto
```

## Pipeline oficial (sequência congelada — só no GO-2)

```
Narrativa Original → Atomic Facts → Reconstrução Cega → Alignment Analysis →
Signals → EAR + Relatório
```

## Restrições (FASE E — pipeline congelado)

1. Nenhuma metodologia, ferramenta, schema, métrica ou infraestrutura nova.
2. Nenhum protocolo congelado alterado (SX-SELECTION, SX-REAUDIT, SX-QUEUE,
   P-0010, SHADOW-EXPERIMENTS).
3. Não forçar o caso a reproduzir nem a contradizer o padrão dos SX-001/002;
   não trazer do desafio da DEBT-009 antes da coleta.
4. Trabalhar exclusivamente com **evidência efetivamente disponível**; preservar
   a proveniência.
5. Observações registradas **depois** de executar cada etapa; resultados não são
   alterados depois para melhorar coerência.
6. Dificuldade metodológica real → registrar como **observação** (DL), não mudar
   o protocolo durante a execução.

## Resultado esperado

- Veredito de emergência espontânea das entidades do ECP em um caso de
  **sucesso** (primeira observação deste tipo no programa).
- Presença/ausência por entidade **comparável** à dos SX-001/002 (teste direto
  da DEBT-009 / predição inversa de SIG-002).
- **`EAR(Genoma)`** — observação experimental de alinhamento (não conclusão;
  denominador a definir conforme etapa congelada, evitando repetir DEBT-007).
- Signals apoiados pelo alignment; **nenhuma promoção a Pattern/LAW-H** sem
  ocorrências suficientes e revisão formal.

## GO-5A — Decisão da coordenação (2026-08-09)

Veredito registrado em [report/10-decisao-coordenacao-go5a](./report/10-decisao-coordenacao-go5a.md):

- **SX-003: PARADO — NÃO PROMOVER — NÃO DESCARTAR.**
- **Transversal SX-001 × SX-002 × SX-003: BLOQUEADO** (GO-5 não autorizado).
- Camada **factual preservada** (EAR 0.77); camada **interpretativa comparativa
  comprometida** (GO-4B); vazamento mantido como registro.
- Próxima decisão da coordenação: tratamento da camada contaminada
  (recomendação: reexecução isolada — alt. B).
- **PARAR** para revisão da coordenação após este registro.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-09 | Manifesto do EXP-SX003. Direção: caso de sucesso (DEBT-009). Seleção: Genoma Humano pelo SX-SELECTION congelado. GO-1 concluído; GO-2 pendente de revisão. |
| 1.1 | 2026-08-09 | GO-5A decidido: PARADO — NÃO PROMOVER — NÃO DESCARTAR; transversal BLOQUEADO. Referência ao relatório 10. |