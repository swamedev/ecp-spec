# SX-QUEUE — Fila de Experimentos Atuais

| Campo | Valor |
|-------|-------|
| **Tipo** | Documento operacional (não-AD, não-RFC, não-lei, não-enteidade) |
| **Status** | Operacional — derivado do protocolo congelado (FASE E) |
| **Data** | 2026-08-04 |
| **Autor** | Coordenação (visão do Arquiteto-Chefe) |
| **Governado por** | [SX-SELECTION](./independence/SX-SELECTION.md), [SX-REAUDIT.yaml](./independence/SX-REAUDIT.yaml), [SX-CANDIDATES.md](./independence/SX-CANDIDATES.md) |
| **Referências** | [ROADMAP](../../ROADMAP.md) (FASE E), [P-0010](./P-0010-REPRODUCIBILITY.md) |

## Propósito

> **O SX-QUEUE.md é a fonte para decidir *qual* experimento executar a seguir, segundo o protocolo congelado.**
> Não define metodologia, não define ciência, não altera prioridades. É uma projeção operacional da ordem produzida pelo protocolo.

## Apenas uma coisa

> **A fila não escolhe experimentos. Ela registra a ordem produzida pelo protocolo congelado.**

Este documento não possui identificadores científicos permanentes. Seu conteúdo é operacional e pode mudar conforme o estado dos experimentos, desde que continue derivável dos documentos de origem.

## Gate metodológico (ordem obrigatória)

A FASE E estabelece que **a reprodutibilidade precede a expansão** (P-0010). Nenhum SX além do SX-001 é liberado como dependente do executor antes que o AFR do SX-001 seja validado entre avaliadores independentes.

```
gate P-0010 (AFR do SX-001)
        ↓
   SX-002
        ↓
   SX-003 … SX-010
```

## Fila

| SX | Domínio | Categoria | Origens | Status | Razão Operacional |
|----|---------|-----------|---------|--------|-------------------|
| SX-001 | Aeroespacial | Falha | Challenger STS-51-L (Rogers Commission + registros NASA + imprensa) | ✅ Concluído | Baseline externo (primeiro caso, selecionado pelo protocolo) |
| — | Repro | Repro | SX-001 (mesmas fontes, mesmos avaliadores independentes) | ⏳ Gate P-0010 | Validar que o resultado não depende do executor |
| SX-002 | A definir pelo protocolo | A definir pelo protocolo | A definir pelo protocolo | ⏳ Seleção | Cobrir domínio ainda não observado |
| SX-003 | A definir pelo protocolo | A definir pelo protocolo | A definir pelo protocolo | 📋 Planejado | Produzir ocorrência independente |
| SX-004 | A definir pelo protocolo | A definir pelo protocolo | A definir pelo protocolo | 📋 Planejado | Expandir tipo de engenharia (ex.: sucesso) |
| SX-005 | A definir pelo protocolo | A definir pelo protocolo | A definir pelo protocolo | 📋 Planejado | Aumentar diversidade organizacional |
| SX-006 | A definir pelo protocolo | A definir pelo protocolo | A definir pelo protocolo | 📋 Planejado | Expandir domínio distante |
| SX-007 | A definir pelo protocolo | A definir pelo protocolo | A definir pelo protocolo | 📋 Planejado | Produzir ocorrência independente |
| SX-008 | A definir pelo protocolo | A definir pelo protocolo | A definir pelo protocolo | 📋 Planejado | Testar gestão/sucesso (não-falha) |
| SX-009 | A definir pelo protocolo | A definir pelo protocolo | A definir pelo protocolo | 📋 Planejado | Expandir diversidade organizacional |
| SX-010 | A definir pelo protocolo | A definir pelo protocolo | A definir pelo protocolo | 📋 Planejado | Fechar a primeira distribuição (conjunto SX-001..010) |

## Legenda de Status

- **✅ Concluído:** pipeline executado, Atlas e Discovery Log atualizados.
- **⏳ Gate P-0010:** rodada de reprodutibilidade do SX-001 em andamento/autorizada (AFR).
- **⏳ Seleção:** autorizado a ser escolhido pelo protocolo após o gate (etapa 4/5 do SX-SELECTION).
- **📋 Planejado:** posição reservada na fila; aguarda o protocolo escolher o caso concreto.

## Estado da fila

- **Pipeline:** Congelado (FASE E — sem modificações metodológicas).
- **Critério de seleção:** [SX-SELECTION](./independence/SX-SELECTION.md) (congelado em 2026-08-03).
- **Elegibilidade:** [SX-REAUDIT.yaml](./independence/SX-REAUDIT.yaml) (veredito final após re-auditoria).
- **Gate antes de SX-002:** [P-0010](./P-0010-REPRODUCIBILITY.md) — AFR validado.

## Objetivo

Produzir evidência para o **Atlas** — apenas.

## Regras de governança

1. O SX-QUEUE.md **nunca** cria RFCs, ADs, leis ou critérios.
2. O SX-QUEUE.md **nunca** avalia "potencial científico" de um caso.
3. Os casos entram na fila apenas por se enquadrarem na matriz SC-1..SC-6 e sobreviverem à re-auditoria SX-REAUDIT.
4. Nada além disso.

## Instruções de operação (por SX)

1. Ler o SX-QUEUE.md no início de cada sprint.
2. Identificar o SX autorizado (gate satisfeito → `⏳ Seleção`).
3. Executar o pipeline congelado:
   ```
   1. Seleção do caso (protocolo)
   2. Coleta de fontes
   3. Narrativa Original
   4. Atomic Facts
   5. Reconstrução Cega
   6. Alignment Analysis
   7. EAR
   8. Signals
   9. Atlas
   10. Discovery Log
   11. Encerrar SX
   ```
4. Atualizar o Discovery Log (DL-###).
5. **Atualizar o SX-QUEUE.md** (avançar o status e abrir a próxima posição).

> É só isso. Sem revisão científica adicional, sem refatoração, sem novos documentos — apenas executar o pipeline que já está escrito.

## Fonte de Verdade

Este documento nunca possui autoridade própria. Toda informação aqui deve ser derivável de:

- [SX-SELECTION](./independence/SX-SELECTION.md)
- [SX-REAUDIT.yaml](./independence/SX-REAUDIT.yaml)
- [SX-CANDIDATES.md](./independence/SX-CANDIDATES.md)
- [P-0010](./P-0010-REPRODUCIBILITY.md)
- [ROADMAP](../../ROADMAP.md)

Em caso de divergência, os documentos acima prevalecem.

## Histórico de revisão

| Versão | Data | Mudança |
|--------|------|---------|
| 1.0 | 2026-08-04 | Criação como documento operacional da FASE E. Domínios neutros ("a definir pelo protocolo"); status ✅/⏳/📋; Fonte de Verdade; "a fila não escolhe experimentos"; gate P-0010 antes do SX-002. |