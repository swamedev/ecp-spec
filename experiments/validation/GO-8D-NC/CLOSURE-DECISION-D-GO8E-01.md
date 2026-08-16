# CLOSURE-DECISION-D-GO8E-01

**Decisão de Encerramento — Diagnóstico D-GO8E-01**
**Data:** 2026-08-15
**Status:** **CLOSED**

---

## 1. Decisão

**D-GO8E-01 = CLOSED** — H3 CONFIRMADO / DV3 COMPOSITE RETIRED FOR COMPARATIVE INFERENCE.

---

## 2. Justificativa Técnica

### Resultado do Diagnóstico
- **Classificação:** H3 — INTERAÇÃO (Score H3=7 vs H1=1, H2=1)
- **Achado Central:** A DV3 composta (média 1:1:1 de conf + ged_ecp + ent_n12) **não é robusta** para inferência comparativa.

### Evidência Consolidada

| Teste | Resultado | Implicação |
|-------|-----------|------------|
| **Decomposição DV3** | ent_n12 = 83% da queda A→B; ged_ecp = 18%; conf = -1% | ent_n12 domina, mas não reflete qualidade real |
| **TS-1 (Referência Neutra)** | ged_ecp usa referência ECP (CAT); B usa SYN → viés inerente a A | Viés estrutural na métrica |
| **TS-2 (Grade de Pesos)** | **19/19** combinações invertem ordem A>B>C | Ordem **não robusta** a pesos |
| **TS-3 (Métricas Alt.)** | Geométrica/Harmônica invertem A>B>C | Ordem **não robusta** a agregação |
| **TS-4 (Contrafactual)** | Igualar ged_ecp(B)=A **não restaura** A>B>C | Queda não explicada apenas por ged_ecp |
| **Sinais Opostos** | 22/30 (A→B) e 20/30 (B→C) com sinais opostos entre componentes | Média composta **mascara trade-offs** |

### Classificação Final
**H3 — INTERAÇÃO** (Score H3=7 vs H1=1, H2=1)

A DV3 composta **não é adequada** como desfecho único para inferência comparativa confirmatória porque:
1. Média 1:1:1 **não é robusta** (falha em TS-2, TS-3, TS-4)
2. Componentes movem-se em **direções opostas** (73% A→B, 67% B→C)
3. **ent_n12 domina** (83% da diferença) mas reflete diversidade de categorias, não qualidade
4. **ged_ecp tem viés CAT** inerente (referência ECP)

---

## 3. Aposentadoria da DV3 Composta

**A DV3 1:1:1 (média aritmética simples) NÃO será usada como desfecho composto em futuras comparações confirmatórias.**

### Novos Desfechos Separados
Os três componentes passam a ser tratados como desfechos **separados** e **primários**:

| Desfecho | Definição | Interpretação |
|----------|-----------|---------------|
| **conf** | Confiança média de classificação | Consistência interna da reconstrução |
| **ged_ecp** | Similitude ao grafo ECP canônico | Fidelidade estrutural a ECP (CAT) |
| **ent_n12** | Entropia normalizada log(12) | Diversidade balanceada de categorias |

---

## 4. Regras para o Futuro

| Regra | Descrição |
|-------|-----------|
| **Separação dos componentes** | conf, ged_ecp, ent_n12 reportados separadamente; sem média composta |
| **Redesign de mensuração antes de potência** | Qualquer novo ciclo deve validar componentes independentemente antes de cálculo de potência |
| **Não reutilizar TS-2 para seleção de pesos** | Resultados de TS-2 **não** serão usados para escolher pesos retrospectivamente |
| **Não reutilizar DV3 composta** | DV3 1:1:1 aposentada para inferência confirmatória |
| **Validação independente de componentes** | Cada componente deve ser validado independentemente antes de uso |

---

## 5. Estado dos Ciclos Anteriores

| Ciclo | Status | Lock |
|-------|--------|------|
| **GO-8D-NC** | **CLOSED** | LOCKED (14/14 hashes íntegros, SHA-256: `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`) |
| **GO-8D-NC F1-F3** | COMPLETE | F1: 270 seeds, F2: 270 recon. PASS, F3: H3 confirmado |
| **D-GO8E-01** | **CLOSED** | Diagnóstico completo, H3 confirmado, DV3 aposentada |
| **GO-8E** | **NÃO AUTORIZADO** | Requer nova decisão de governança |

---

## 4. Locks e Integridade

| Artefato | Status |
|----------|--------|
| GO-8D-NC LOCK | ÍNTEGRO (14/14 hashes, SHA-256: `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`) |
| Pré-registro GO-8D-NC | v1.0 FINAL íntegro (`12fef4f74431b94fa0eacc8a170e2ad16192c871bc524464d5ddf0535fa5fcd1`) |
| D-GO8E-01 proposta | Aprovada e executada conforme especificação |
| Resultados F1-F3 | Íntegros, não reexecutados |

---

## 5. Próximos Passos (Condicionais à Governança)

| Ação | Status | Condição |
|------|--------|----------|
| Redesign de mensuração | **NÃO AUTORIZADO** | Requer nova decisão |
| Cálculo de potência | **NÃO AUTORIZADO** | Requer redesign de mensuração |
| Pré-registro GO-8E | **NÃO AUTORIZADO** | Requer nova decisão |
| Coleta de novos BIPs | **NÃO AUTORIZADO** | Requer nova decisão |
| Experimento GO-8E | **NÃO AUTORIZADO** | Requer nova decisão |

---

## 5. Documentos de Referência

| Documento | Caminho |
|-----------|---------|
| D-GO8E-01 Proposal | `D-GO8E-01-PROPOSAL.md` |
| Diagnostic Report | `DIAGNOSTIC-REPORT-GO8E-01.md` |
| Audit Reproduction | `AUDIT-REPRODUCTION.md` |
| Audit Prereg Adherence | `AUDIT-PREREG-ADHERENCE.md` |
| Interpretation Governance | `INTERPRETATION-GOVERNANCE.md` |
| GO-8D-NC Closure | `CLOSURE-DECISION-GO-8D-NC.md` |
| Lock Manifest | `GO-8D-NC-LOCK-MANIFEST.yaml` |

---

## 5. Decisão Final

**D-GO8E-01 = CLOSED**

- ✅ H3 (Interação) confirmado
- ✅ DV3 composta aposentada para inferência confirmatória
- ✅ Componentes (conf, ged_ecp, ent_n12) estabelecidos como desfechos separados
- ✅ GO-8D-NC permanece CLOSED e LOCKED
- ✅ Nenhum GO-8E autorizado

**Próximo passo (condicional):** Proposta de redesign de mensuração, se a governança autorizar.

---

**Assinatura:** Encerramento Oficial D-GO8E-01  
**Data:** 2026-08-15  
**Lock Manifest:** `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`