# CLOSURE-DECISION-MEASUREMENT-REDESIGN.md

**Decisão de Encerramento — Redesign de Mensuração (GO-8E)**
**Data:** 2026-08-16
**Status:** **CLOSED**

---

## 1. Decisão

**Redesign de Mensuração = ENCERRADO após Fase 2.**

- Nenhuma nova métrica composta será adotada.
- Nenhum novo dado será coletado.
- Nenhum GO-8E será aberto com as métricas atuais.
- O GO-8D-NC permanece **CLOSED** e **LOCKED**.
- A conclusão técnica é: para qualquer estudo comparativo futuro, será necessário um novo projeto com coleta de K, grafos de referência reais e validação com ground truth.

---

## 2. Justificativa Técnica

### Contexto
- GO-8D-NC **CLOSED / LOCKED** (14/14 artefatos íntegros, Manifest SHA-256: `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`)
- D-GO8E-01 **CLOSED** — H3 (Interação) confirmado (Score H3=7 vs H1=1, H2=1)
- DV3 1:1:1 **APOSENTADA** para inferência confirmatória
- Desfechos atuais: `conf`, `ged_ecp`, `ent_n12` (separados)

### Evidência Consolidada (Fase 1 + Fase 2)

| Componente | Validade | Problema Principal |
|------------|----------|-------------------|
| **conf** | CONDITIONAL | Baixa convergência com DV3 (r=0.53) |
| **ged_ecp** | CONDITIONAL | **Viés CAT/SYN** — referência ECP favorece A/C |
| **ent_n12** | CONDITIONAL | **Viés cardinalidade** — teto 0.884 (CAT) vs 1.0 (SYN) |

### Testes de Robustez (Fase 2)

| Teste | Resultado | Implicação |
|-------|-----------|------------|
| **TS-1: Referências GED** | Nenhuma referência neutra elimina viés CAT; SYN_REAL inverte ordem (B>A>C) | Viés CAT inerente à referência ECP |
| **TS-2: Métricas Diversidade** | Todas monotônicas em ent_n12; herdam viés cardinalidade | ent_n12 domina DV3 (83%) mas não valida |
| **TS-3: Pesos (C3)** | **10/10** combinações invertem ordem A>B>C | Média 1:1:1 não robusta a pesos |
| **TS-4: Contrafactual (C4)** | Igualar ged_ecp não restaura ordem | Queda não explicada apenas por ged_ecp |
| **Sinais Opostos** | 22/30 (A→B) e 20/30 (B→C) com sinais opostos | Trade-offs mascarados pela média 1:1:1 |

### Avaliação C1–C6 (Nenhuma Nova DV Passa)

| Critério | Status | Evidência |
|----------|--------|-----------|
| **C1** Validade independente | **PARCIAL** | Componentes CONDITIONAL |
| **C2** Ausência de viés | **FALHA** | ged_ecp: viés CAT; ent_n12: viés cardinalidade |
| **C3** Robustez a pesos | **FALHA** | 10/10 pesos invertem A>B>C |
| **C4** Robustez a agregação | **FALHA** | Geométrica/Harmônica invertem |
| **C5** Sensibilidade | **PASS** | Todos sensíveis |
| **C6** Interpretabilidade | **PARCIAL** | Vieses confundem interpretação |

### Classificação Final do Diagnóstico

| Hipótese | Score | Status |
|----------|-------|--------|
| **H1 — Efeito Real** | 1 | Degradação real mas concentrada em métrica |
| **H2 — Artefato DV3** | 1 | Viés CAT em ged_ecp, mas ent_n12 domina (83%) |
| **H3 — Interação** | **7** | **FORTE** — Trade-offs mascarados, TS-2/3/4 invertem ordem |

**Classificação Final: H3 — INTERAÇÃO** (Score H3=7 vs H1=1, H2=1)

---

## 3. Conclusão Final

> **A DV3 composta 1:1:1 NÃO é adequada para inferência confirmatória.**
>
> A média composta 1:1:1 mascara trade-offs entre componentes (ent_n12 cai 93%, ged_ecp 73%, conf sobe 57% em B). A ordem A>B>C não é robusta a pesos, agregação geométrica/harmônica, nem contrafactuais.
>
> **Nenhuma configuração testada passa todos os critérios C1–C6 para uma nova DV composta.**
>
> **Conclusão técnica:** Para qualquer estudo comparativo futuro, será necessário um novo projeto com:
> 1. Coleta de K (número de categorias) por BIP×condição
> 2. Construção de grafos de referência reais (CAT, SYN, UNION, NEUTRAL, DATA-DRIVEN)
> 3. Validação de métricas de diversidade com ground truth (anotadores humanos)
> 4. Redesign completo da métrica composta ou adoção de desfechos separados

---

## 4. Regras Fixadas

| Regra | Status |
|-------|--------|
| Separação obrigatória: `conf`, `ged_ecp`, `ent_n12` | **OBRIGATÓRIO** |
| Redesign de mensuração antes de potência | **OBRIGATÓRIO** |
| Não reutilizar TS-2 para seleção de pesos | **PROIBIDO** |
| Não usar A > B para escolher métrica | **PROIBIDO** |
| Não abrir GO-8E sem nova decisão | **PROIBIDO** |
| Não reabrir ciclos anteriores (GO-8D-NC, D-GO8E-01) | **PROIBIDO** |

---

## 5. Estado Final dos Ciclos

| Ciclo | Status | Lock |
|-------|--------|------|
| **GO-8B** | CLOSED / LOCKED / FROZEN | Íntegro |
| **GO-8C** | CLOSED / LOCKED | Íntegro |
| **GO-8D** | CLOSED / LOCKED | Íntegro (14/14 hashes) |
| **GO-8D-NC** | **CLOSED / LOCKED** | **ÍNTEGRO** (14/14 hashes, SHA-256: `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`) |
| **D-GO8E-01** | **CLOSED** | Diagnóstico completo (H3 confirmado) |
| **Redesign Mensuração** | **CLOSED (Fase 2)** | Fase 2 completa; Fase 3 **NÃO AUTORIZADA** |
| **GO-8E** | **NÃO AUTORIZADO** | Aguarda redesign + decisão de governança |

---

## 4. Locks e Integridade (Confirmados)

| Lock | Status | SHA-256 Manifest |
|------|--------|------------------|
| **GO-8D-NC** | **LOCKED** (14/14 artefatos) | `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058` |
| GO-8D | LOCKED | `b25dabcf...` |
| GO-8C | LOCKED | Íntegro |
| GO-8B | LOCKED/FROZEN | Íntegro |

---

## 5. Documentos de Referência

| Documento | Caminho |
|-----------|---------|
| CLOSURE-DECISION-GO-8D-NC.md | `CLOSURE-DECISION-GO-8D-NC.md` |
| CLOSURE-DECISION-D-GO8E-01.md | `CLOSURE-DECISION-D-GO8E-01.md` |
| DIAGNOSTIC-REPORT-GO8E-01.md | `DIAGNOSTIC-REPORT-GO8E-01.md` |
| MEASUREMENT-REDESIGN-PHASE1-REPORT.md | `MEASUREMENT-REDESIGN-PHASE1-REPORT.md` |
| MEASUREMENT-REDESIGN-PHASE2-REPORT.md | `MEASUREMENT-REDESIGN-PHASE2-REPORT.md` |
| AUDIT-REPRODUCTION.md | `AUDIT-REPRODUCTION.md` |
| AUDIT-PREREG-ADHERENCE.md | `AUDIT-PREREG-ADHERENCE.md` |
| INTERPRETATION-GOVERNANCE.md | `INTERPRETATION-GOVERNANCE.md` |
| MEASUREMENT-REDESIGN-PROPOSAL.md | `MEASUREMENT-REDESIGN-PROPOSAL.md` |
| MEASUREMENT-REDESIGN-PHASE1-REPORT.md | `MEASUREMENT-REDESIGN-PHASE1-REPORT.md` |
| MEASUREMENT-REDESIGN-PHASE2-REPORT.md | `MEASUREMENT-REDESIGN-PHASE2-REPORT.md` |
| D-GO8E-01-PROPOSAL.md | `D-GO8E-01-PROPOSAL.md` |
| GO-8D-NC-LOCK-MANIFEST.yaml | `GO-8D-NC-LOCK-MANIFEST.yaml` |

---

## 5. Decisão Final

**REDESIGN DE MENSURAÇÃO = ENCERRADO (Fase 2)**

- ✅ H3 (Interação) confirmado
- ✅ DV3 composta 1:1:1 aposentada para inferência confirmatória
- ✅ Componentes `conf`, `ged_ecp`, `ent_n12` estabelecidos como desfechos separados
- ✅ GO-8D-NC permanece CLOSED e LOCKED
- ✅ Nenhum GO-8E autorizado

**Próximo passo (fora deste ciclo):** Proposta de redesign de mensuração, se a governança autorizar.

---

**Assinatura:** Encerramento Oficial Redesign de Mensuração — GO-8E  
**Data:** 2026-08-16  
**Lock Manifest GO-8D-NC:** `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`  
**Autoridade:** Governança GO-8D-NC