# CLOSURE-DECISION-GO-8D-NC

**Decisión de Cierre — GO-8D-NC**
**Fecha:** 2026-08-15
**Estado:** **CLOSED**

---

## 1. Estado Final

| Fase | Estado | Detalle |
|------|--------|---------|
| **F1 — Generación de Seeds** | PASS | 270 seeds únicas, seed_master = 20260816 |
| **F2 — Ejecución de Reconstrucciones** | PASS | 270/270 PASS, 0 FAIL |
| **F3 — Análisis Estadístico** | COMPLETE | 30/30 BIPs válidos → GO |
| **Lock Metodológico** | ÍNTEGRO | 14/14 hashes conferen |
| **Pré-registro** | v1.0 FINAL | SHA-256: `12fef4f74431b94fa0eacc8a170e2ad16192c871bc524464d5ddf0535fa5fcd1` |
| **Cierre** | **CLOSED** | — |

---

## 2. Conclusión Principal

**Hipótesis primaria CONFIRMADA bajo métrica DV3:**

> **B < A** (p = 2.61 × 10⁻⁸, Cliff Δ = 0.936)

La condición **A (cega pura)** produce reconstrucciones de mayor calidad DV3 que **B (cega + C3)**, con un efecto **muy grande** (Cliff Δ = 0.936). El orden observado es **A > B > C**.

**TOST A–C (Δ = 0.05): NO EQUIVALENTE** — IC 95% [−0.0999, −0.0533] está completamente fuera de [−0.05, 0.05].

**Análisis complementaria C < B:** CONFIRMADA (p = 0.0310, Cliff Δ = 0.240).

---

## 3. Interpretación Causal: NO AFIRMADA

| Aspecto | Declaración |
|---------|-------------|
| **Causalidad** | **NO AFIRMADA** — Diseño observacional dentro de pipeline fijo |
| **Verdad absoluta** | **NO AFIRMADA** — Resultados limitados a métrica DV3 |
| **Generalización** | **NO AFIRMADA** — 30 BIPs, pipeline específico, métrica DV3 |
| **Utilidad práctica** | **NO AFIRMADA** — DV3 ≠ utilidad operativa |

**El resultado es: "Bajo métrica DV3, A > B > C en calidad de reconstrucción interna."**

---

## 4. Pregunta para Futuro (GO-8E+)

> **"¿Por qué C3 reduce la DV3? ¿Pérdida real de información o limitación de la métrica?"**

El hallazgo contraintuitivo (A > B, es decir, ceguera pura > ceguera + taxonomía C3) plantea dos hipótesis no mutuamente excluyentes:

1. **Pérdida real:** La taxonomía C3 introduce ruido o restricciones que degradan la reconstrucción bajo DV3.
2. **Limitación de DV3:** La métrica DV3 (basada en ECP canónico) penaliza el uso de categorías SYN (C3), favoreciendo artificiosamente la condición A (CAT nativo).

**Esta pregunta define la agenda de GO-8E.**

---

## 5. Integridad de Locks (Confirmada)

| Lock | SHA-256 | Estado |
|------|---------|--------|
| `GO-8D-NC-LOCK-MANIFEST.yaml` | `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058` | ✅ Íntegro |
| 14/14 artefactos congelados | Hashes conferidos | ✅ Íntegros |
| Pré-registro | `12fef4f74431b94fa0eacc8a170e2ad16192c871bc524464d5ddf0535fa5fcd1` | ✅ Íntegro |
| Pipeline (C2/C3/DV3) | Hashes conferidos | ✅ Íntegros |
| Seeds | `e7dd39648743023393042668484d3458042cbe34e196e08dcdcb74b578746275` | ✅ Íntegro |

**Ningún artefacto congelado alterado durante F1, F2, F3.**

---

## 6. Productos de Cierre Entregados

| Documento | Ruta | Estado |
|-----------|-------|--------|
| `AUDIT-REPRODUCTION.md` | `GO-8D-NC/AUDIT-REPRODUCTION.md` | ✅ Entregado |
| `AUDIT-PREREG-ADHERENCE.md` | `GO-8D-NC/AUDIT-PREREG-ADHERENCE.md` | ✅ Entregado |
| `INTERPRETATION-GOVERNANCE.md` | `GO-8D-NC/INTERPRETATION-GOVERNANCE.md` | ✅ Entregado |
| `CLOSURE-DECISION-GO-8D-NC.md` | `GO-8D-NC/CLOSURE-DECISION-GO-8D-NC.md` | ✅ Entregado (este documento) |

---

## 7. Decisión Final

**GO-8D-NC: CLOSED**

- ✅ Hipótesis primaria confirmada bajo DV3 (B < A, efecto muy grande)
- ✅ TOST A–C no equivalente (Δ = 0.05)
- ✅ 30/30 BIPs válidos → GO confirmatorio
- ✅ Lock metodológico íntegro (14/14)
- ✅ Pré-registro v1.0 FINAL respetado sin desviaciones
- ✅ Auditoría de reproducción: PASS (efectos idénticos, decisiones idénticas)
- ✅ Auditoría de adherencia: PASS (0 desviaciones)
- ✅ Interpretación: Limitada a DV3, sin causalidad afirmada
- ✅ Pregunta para GO-8E formulada: "¿Por qué C3 reduce la DV3?"

**No se autoriza GO-8E en esta decisión.** Se requiere nueva autorización de gobernanza.

---

**Firmado:** Cierre Oficial GO-8D-NC  
**Fecha:** 2026-08-15  
**Lock Manifest:** `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`  
**Autoridad:** Gobernanza GO-8D-NC