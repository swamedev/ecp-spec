# GO-8D-NC — TODO

## Concluído ✅

- [x] OPEN-00: Abertura formal GO-8D-NC (governança 2026-08-15)
- [x] BATCH-01: Produção BIPs 013–017 (5/5 PASS)
- [x] BATCH-02: Produção BIPs 018–022 (5/5 PASS)
- [x] BATCH-03: Produção BIPs 023–027 (5/5 PASS; Dieselgate via PNGs)
- [x] BATCH-04: Produção BIPs 028–030 (3/3 PASS)
- [x] SAN-01: Saneamento 6 BIPs GO-8C bloqueadores (6/6 PASS)
- [x] PRE-FLIGHT-01: Validação 30/30 BIPs (PASS)
- [x] F1: Geração 270 seeds (seed_master=20260816) — PASS
- [x] F2: Execução 270 reconstruções (270/270 PASS)
- [x] F3: Análise estatística (Friedman + Wilcoxon + Holm + TOST + complementar) — COMPLETE
- [x] AUDIT-01: Reprodução análise a partir de dados congelados — PASS
- [x] AUDIT-02: Adesão ao pré-registro v1.0 FINAL — PASS (0 desvios)
- [x] INT-01: Interpretação sob governança (limitação a DV3)
- [x] D-GO8E-01: Diagnóstico "Por que C3 reduz a DV3?" — COMPLETE
  - Decomposição DV3 (conf, ged_ecp, ent_n12)
  - TS-1 (Referência Neutra)
  - TS-2 (Grade de Pesos: 19/19 inversões)
  - TS-3 (Métricas Geométrica/Harmônica)
  - TS-4 (Contrafactual C3)
  - Classificação: **H3 (Interação)** — Score 7 vs 1/1
  - Recomendação: **Decompor DV3; não usar média composta**
- [x] CLS-01: Encerramento D-GO8E-01 — CLOSED
  - DV3 composta **aposentada** para inferência confirmatória
  - conf, ged_ecp, ent_n12 como desfechos separados
  - Regras para futuro definidas
- [x] CLS-02: Encerramento GO-8D-NC — CLOSED
  - Lock LOCKED (14/14 hashes íntegros)
  - 30/30 BIPs válidos
  - DV3 composta aposentada
  - GO-8E NÃO AUTORIZADO
- [x] RED-01: Fase 1 Redesign (Validação Componentes) — COMPLETE
  - conf: CONDITIONAL (convergência fraca)
  - ged_ecp: CONDITIONAL (viés CAT/SYN)
  - ent_n12: CONDITIONAL (viés cardinalidade)
  - Recomendação: PROCEED para Fase 2
- [x] RED-02: Fase 2 Redesign (GED + Diversidade) — COMPLETE
  - TS-1: Referências GED (CAT, SYN, UNION, NEUTRAL, DATA-DRIVEN, SYN_REAL)
  - TS-2: Métricas diversidade (Shannon, Hill, Simpson, Riqueza) — todas monotônicas em ent_n12
  - TS-3: Grade de pesos (10/10 invertem A>B>C)
  - TS-4: Contrafactual (igualar ged_ecp não restaura ordem)
  - Classificação: **H3 (Interação)** — Score 7 vs 1/1
  - Recomendação: Decompor DV3; não usar média composta
- [x] RED-03: Encerramento Redesign — CLOSED
  - DV3 1:1:1 aposentada para inferência confirmatória
  - conf, ged_ecp, ent_n12 como desfechos separados
  - Regras para futuro definidas
  - Nenhuma nova métrica composta adotada

---

## Cancelado (Não Autorizado) 🚫

- [x] REDESIGN-03: Fase 3 (coleta K, grafos reais, validação ground truth) — **CANCELLED**
- [x] POWER-01: Cálculo de potência com novos componentes — **CANCELLED**
- [x] PREREG-01: Pré-registro GO-8E — **CANCELLED**
- [x] EXP-01: Experimento GO-8E — **CANCELLED**
- [x] Coleta de 18 novos BIPs (para GO-8E) — **CANCELLED**

---

## Bloqueados (Não Autorizados) 🚫

- [ ] Novo experimento (GO-8E) sem redesign + autorização
- [ ] Novos BIPs sem autorização
- [ ] Alteração de Locks (GO-8D-NC, GO-8C, GO-8B)
- [ ] Alteração de DV3 nos dados experimentais congelados
- [ ] Uso de TS-2 para seleção de pesos retrospectivamente
- [ ] Uso de resultado A > B para escolha de métrica

---

## Estado Final

| Item | Status |
|------|--------|
| **GO-8D-NC** | **CLOSED / LOCKED** (14/14 hashes íntegros) |
| **DV3 1:1:1** | **APOSENTADA** para inferência confirmatória |
| **Desfechos** | `conf`, `ged_ecp`, `ent_n12` (separados) |
| **D-GO8E-01** | **CLOSED** — H3 (Interação) confirmado |
| **Redesign Mensuração** | **CLOSED** (Fase 2 completa; Fase 3 cancelada) |
| **GO-8E** | **NÃO AUTORIZADO** — aguarda redesign + nova decisão |

---

**Última atualização:** 2026-08-16
**Lock Manifest:** `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`