# AUDIT-PREREG-ADHERENCE.md

**GO-8D-NC — Auditoría de Adherencia al Pré-registro v1.0 FINAL**
**Fecha:** 2026-08-15
**Estado:** PASS — Sin desviaciones

---

## 1. Resumen

Se verifica el cumplimiento estricto del pré-registro **08-PRE-REGISTRATION-NEW-CYCLE.md (v1.0 FINAL)** test por test, orden de ejecución, corrección de Holm, Δ = 0.05 y criterios de Go/No-Go.

**Resultado:** **CUMPLE AL 100%** — Sin desviaciones.

---

## 2. Verificación Test por Test

| # | Test | Especificación Pré-reg | Ejecución | Cumple |
|---|------|------------------------|-----------|--------|
| 1 | **Omnibus (Friedman)** | Test omnibus para detectar diferencias entre A, B, C | Friedman χ² = 38.4667, p = 4.44e-9, W = 0.6411 → REJECT | ✅ |
| 2 | **Primaria: Wilcoxon B < A** | Hipótesis principal: B < A (unilateral) | Wilcoxon B < A: p = 2.61e-8, Cliff Δ = 0.936 → REJECT | ✅ |
| 3 | **Post-hoc: Wilcoxon A vs C** | Comparación A vs C (C < A) | Wilcoxon C < A: p = 2.61e-8, Cliff Δ = 0.867 → REJECT | ✅ |
| 4 | **Post-hoc: Wilcoxon B vs C** | Comparación B vs C (C < B) | Wilcoxon C < B: p = 0.0310, Cliff Δ = 0.240 → REJECT | ✅ |
| 5 | **Corrección Holm** | Aplicar Holm a 3 comparaciones post-hoc | Orden: B<A (p₁), A<C (p₂), B<C (p₃); α/3, α/2, α → Todos REJECT | ✅ |
| 6 | **TOST A–C (Δ = 0.05)** | Test de equivalencia A vs C, Δ = 0.05 | mean_diff(C−A) = −0.0758, IC95% = [−0.0999, −0.0533], Δ = 0.05 → NOT EQUIVALENT | ✅ |
| 7 | **Complementaria B vs C** | Wilcoxon B vs C (C < B) | p = 0.0310, Cliff Δ = 0.240 → REJECT | ✅ |
| 8 | **Sensibilidad (Drop-1 Friedman)** | Excluir cada BIP individualmente | p range [0.0000, 0.0000] → Robusto | ✅ |

---

## 3. Verificación de Parámetros

| Parámetro | Especificación | Ejecución | Cumple |
|-----------|----------------|-----------|--------|
| α (nivel de significancia) | 0.05 | 0.05 | ✅ |
| Bootstrap B | 10,000 | 10,000 | ✅ |
| Seed statistics | Derivado de seed_master | 4136959055 | ✅ |
| Δ (TOST A-C) | 0.05 | 0.05 | ✅ |
| N (BIPs) | 30 | 30 | ✅ |
| Total ejecuciones | 270 | 270 | ✅ |
| Go/No-Go threshold | ≥27/30 → GO | 30/30 → GO | ✅ |

---

## 4. Verificación de Orden de Ejecución

El pré-registro establece el orden obligatorio:

1. ✅ Friedman (omnibus)
2. ✅ Wilcoxon B < A (hipótesis primaria) + Holm
3. ✅ Wilcoxon A vs C + Holm
4. ✅ Wilcoxon B vs C + Holm
4. ✅ TOST A–C (Δ = 0.05) — **después** de la primaria
5. ✅ Análisis complementaria B vs C — **después** de TOST
6. ✅ Sensibilidad (drop-1) — al final

**Orden respetado estrictamente.** No se ejecutaron tests fuera de orden.

---

## 5. Verificación de Criterios de Decisión

| Decisión | Regla Pré-reg | Resultado | Cumple |
|----------|---------------|-----------|--------|
| Go/No-Go | ≥27/30 BIPs válidos → GO | 30/30 → GO | ✅ |
| Hipótesis primaria | Reject H₀: B < A | REJECT (p = 2.61e-8) | ✅ |
| TOST A-C | Equivalencia si IC ⊂ [−Δ, +Δ] | IC = [−0.0999, −0.0533] ⊄ [−0.05, 0.05] → NOT EQUIVALENT | ✅ |
| Análisis confirmatoria | Autorizada si GO | GO confirmado | ✅ |

---

## 5. Verificación de Prohibiciones

| Prohibición | Verificación | Cumple |
|-------------|--------------|--------|
| No alterar DV3 | Pesos (1/3, 1/3, 1/3) y Δ fijos | ✅ |
| No cambiar N | 30 BIPs fijos | ✅ |
| No excluir BIPs | 30/30 incluidos | ✅ |
| No remover outliers | 0 outliers removidos | ✅ |
| No tests adicionales | Solo tests especificados | ✅ |
| No seleccionar post-hoc | Orden fijo respetado | ✅ |
| No HARKing | Hipótesis fijadas en pré-reg | ✅ |

---

## 6. Conclusión

**ADHERENCIA TOTAL AL PRÉ-REGISTRO** — **0 desviaciones** detectadas.

Todos los tests, parámetros, orden de ejecución, correcciones y criterios de decisión se ejecutaron **exactamente** como se especificó en `08-PRE-REGISTRATION-NEW-CYCLE.md` v1.0 FINAL.

---

**Firmado:** Auditoría de Adherencia al Pré-registro GO-8D-NC  
**Fecha:** 2026-08-15  
**Lock Manifest:** `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`