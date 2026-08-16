# EXECUTIVE-SUMMARY-FINAL.md

# Resumo Executivo Consolidado — Projeto GO-8
**Data:** 2026-08-16  
**Status:** **ENCERRADO** (sem GO-8E autorizado)

---

## Linha do Tempo Resumida

| Ciclo | Período | Objetivo Principal | Status Final |
|-------|---------|-------------------|--------------|
| **GO-8B** | Piloto metodológico | Definir pipeline base e métrica S_struct | CLOSED / LOCKED / FROZEN |
| **GO-8C** | Estudo N=12 com S_struct | Testar métrica S_struct em 12 BIPs | CLOSED / LOCKED |
| **GO-8D** | Reprojeto com DV_confirm | Redesign pipeline (C2/C3) + nova métrica DV_confirm | CLOSED / LOCKED |
| **GO-8D-NC** | Estudo confirmatório N=30 com DV3 | Execução confirmatória com DV3 (conf + ged_ecp + ent_n12) | **CLOSED / LOCKED** |

---

## Principais Conclusões

### 1. Resultado Confirmatório GO-8D-NC
- **Hipótese primária confirmada sob DV3:** B < A (p = 2,61 × 10⁻⁸, Cliff Δ = 0,936)
- **Ordem observada:** A > B > C (medianas DV3: 0,621 > 0,580 > 0,545)
- **TOST A–C (Δ = 0,05):** NÃO EQUIVALENTE (IC 95% [−0,0999, −0,0533])
- **Análise complementar B vs C:** Significativa (p = 0,031, Cliff Δ = 0,240)
- **Go/No-Go:** 30/30 BIPs válidos → **GO** confirmatório

### 2. Diagnóstico D-GO8E-01 (Por que C3 reduz a DV3?)
- **Classificação:** **H3 — INTERAÇÃO** (Score H3=7 vs H1=1, H2=1)
- **Descoberta central:** A ordem A > B > C **não é robusta** à decomposição/agregação da DV3
- **Mecanismo identificado (H3 — Interação):**
  - `ent_n12` domina a diferença DV3 (83% da queda A→B) mas tem **viés de cardinalidade** (teto 0,884 para CAT vs 1,0 para SYN)
  - `ged_ecp` tem **viés CAT/SYN** inerente (referência ECP = CAT)
  - `conf` tem baixa convergência com DV3 (r=0,53)
  - A média 1:1:1 **mascara trade-offs** entre componentes (73% A→B com sinais opostos)

### 3. Por que a DV3 1:1:1 foi Aposentada
| Critério | Resultado |
|----------|-----------|
| **C1** Validade independente | PARCIAL (componentes CONDITIONAL) |
| **C2** Ausência de viés | **FALHA** (ged_ecp: viés CAT; ent_n12: viés cardinalidade) |
| **C3** Robustez a pesos | **FALHA** (10/10 pesos invertem A>B>C) |
| **C4** Robustez a agregação | **FALHA** (geométrica/harmônica invertem) |
| **C5** Sensibilidade | PASS |
| **C6** Interpretabilidade | PARCIAL |

> **Conclusão:** A DV3 1:1:1 **não atende C1–C6** para inferência confirmatória. Foi aposentada.

### 4. Por que GO-8E NÃO Foi Autorizado
1. **Métrica atual não atende C1–C6** — Nenhuma configuração testada passa todos os critérios
2. **Fase 3 do redesign exigiria:**
   - Coleta de K (número de categorias) por BIP×condição
   - Construção de grafos de referência reais (CAT, SYN, UNION, NEUTRAL, DATA-DRIVEN)
   - Validação de métricas de diversidade com ground truth (anotadores humanos)
3. **Necessidade de redesign independente** antes de novo experimento — Não se pode usar A > B para escolher métrica

---

## Regras Fixadas para o Futuro

| Regra | Status |
|-------|--------|
| **Separação obrigatória:** `conf`, `ged_ecp`, `ent_n12` | **OBRIGATÓRIO** |
| **Redesign de mensuração antes de potência** | **OBRIGATÓRIO** |
| **Não reutilizar TS-2 para seleção de pesos** | **PROIBIDO** |
| **Não usar A > B para escolher métrica** | **PROIBIDO** |
| **Não abrir GO-8E sem nova decisão de governança** | **PROIBIDO** |

---

## Sequência Obrigatória para Futuro Ciclo (GO-8E+)

1. **Redesign** → Validação independente de componentes
2. **Validação** → Referências GED neutras + métricas de diversidade sem viés
2. **Potência** → Cálculo com nova DV validada
3. **Pré-registro** → Lock → Experimento

---

## Estado Final do Projeto GO-8

| Ciclo | Status | Lock |
|-------|--------|------|
| GO-8B | CLOSED | LOCKED / FROZEN |
| GO-8C | CLOSED | LOCKED |
| GO-8D | CLOSED | LOCKED |
| **GO-8D-NC** | **CLOSED** | **LOCKED** (14/14 hashes) |
| **D-GO8E-01** | **CLOSED** | H3 confirmado |
| **Redesign Mensuração** | **CLOSED** | Fase 2 completa; Fase 3 cancelada |
| **GO-8E** | **NÃO AUTORIZADO** | Aguarda redesign + decisão |

---

**Lock Manifest GO-8D-NC:** `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`  
**Data de Encerramento:** 2026-08-16  
**Status Final:** **PROJETO GO-8 ENCERRADO**