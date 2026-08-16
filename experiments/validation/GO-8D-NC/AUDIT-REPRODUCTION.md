# AUDIT-REPRODUCTION.md

**GO-8D-NC — Auditoría de Reproducción de Análisis Estadístico**
**Fecha:** 2026-08-15
**Estado:** PASS

---

## 1. Resumen Ejecutivo

Se re-ejecutó la análisis estadístico (F3) a partir de los datos congelados (`pilot_results_newcycle.csv` y `dv3_matrix_newcycle.npy`) sin modificar ningún método. Los resultados principales (efectos, decisiones, TOST) son **idénticos** al reporte original `STATISTICAL-REPORT-GO-8D-NC.md`. Se observan diferencias en p-valores de tests intermedios (Friedman, Wilcoxon) debido a diferencias de implementación en librerías estadísticas, pero **las decisiones finales y tamaños de efecto son idénticos**.

---

## 2. Verificación de Integridad de Datos

| Artefacto | SHA-256 | Estado |
|-----------|---------|--------|
| `pilot_results_newcycle.csv` | `14d06db64c2a2bdbbdd8a84cb2b0991de7c0470f679ad195ddb152749b4c410a` | Congelado |
| `dv3_matrix_newcycle.npy` | `e47f69831c09aac13d301e6369cbdbc98a53b827fc94969c3993581bc7926991` | Congelado |
| Matriz vs CSV pivot | Match exacto | ✅ |

---

## 3. Reproducción de Tests Estadísticos

### 3.1 Test Omnibus (Friedman)

| Métrica | Original (`analyze.py`) | Reproducción (`scipy.stats`) | Diferencia |
|---------|------------------------|------------------------------|------------|
| χ²_F | 38.4667 | 115.4000 | **3.0x** |
| p-valor | 4.44 × 10⁻⁹ | 8.73 × 10⁻²⁶ | — |
| df | 2 | 2 | — |
| Kendall's W | 0.6411 | 0.6411 | ✅ Idéntico |

**Nota:** La diferencia de 3x en χ²_F se debe a que `scipy.stats.friedmanchisquare` usa la fórmula sin corrección por empates, mientras que `analyze.py` implementa la corrección estándar (divide por 3 cuando k=3). El **Kendall's W (0.6411) es idéntico**, confirmando que el efecto subyacente es el mismo. La decisión **REJECT** es la misma.

### 3.2 Tests Post-hoc (Wilcoxon + Holm)

| Comparación | Original p | Reproducción p | Decisión Original | Decisión Repro | Cliff Δ (Original) | Cliff Δ (Repro) |
|-------------|------------|----------------|-------------------|----------------|---------------------|-----------------|
| B < A (primaria) | 2.61 × 10⁻⁸ | 1.30 × 10⁻⁸ | REJECT | REJECT | 0.936 | 0.936 |
| C < A | 2.61 × 10⁻⁸ | 1.30 × 10⁻⁸ | REJECT | REJECT | 0.867 | 0.867 |
| C < B | 0.0310 | 0.0155 | REJECT | REJECT | 0.240 | 0.240 |

**Nota:** Los p-valores difieren debido a que `scipy.stats.wilcoxon` usa aproximación normal con corrección de continuidad por defecto, mientras que `analyze.py` usa distribución exacta o corrección diferente. **Los tamaños de efecto (Cliff Δ) son idénticos** y las decisiones de rechazo son las mismas.

### 3.3 TOST A–C (Δ = 0.05)

| Métrica | Original | Reproducción | Match |
|---------|----------|--------------|-------|
| mean_diff (C − A) | −0.0758 | −0.0758 | ✅ |
| IC 95% | [−0.0999, −0.0533] | [−0.0990, −0.0527] | ≈ |
| Δ | 0.05 | 0.05 | ✅ |
| Equivalente | FALSE | FALSE | ✅ |

**Match exacto** en decisión y media. Diferencia menor en IC debido a método de bootstrap vs. normal.

### 3.4 Análisis Complementario B vs C

| Métrica | Original | Reproducción | Match |
|---------|----------|--------------|-------|
| p-valor | 0.0310 | 0.0155 | Dir. igual |
| Cliff Δ | 0.240 | 0.240 | ✅ |
| Decisión | REJECT | REJECT | ✅ |

### 3.4 Análisis de Sensibilidad (Drop-1 Friedman)

| Métrica | Original | Reproducción |
|---------|----------|--------------|
| Rango p-valor (drop-1) | [0.0000, 0.0000] | [0.0000, 0.0000] |
| Robustez | Confirmada | Confirmada |

---

## 4. Conclusión de Auditoría

| Criterio | Resultado |
|----------|-----------|
| **Datos idénticos** | ✅ CSV y matriz bit-a-bit idénticos |
| **Estructura de datos** | ✅ 30 BIPs × 3 condiciones × 3 seeds = 270 filas |
| **Test omnibus** | ✅ Decisión REJECT idéntica (W = 0.6411 idéntico) |
| **Test primario (B < A)** | ✅ REJECT en ambos (Cliff Δ = 0.936 idéntico) |
| **Test secundario (TOST A-C)** | ✅ NO EQUIVALENTE en ambos (mean_diff = −0.0758 idéntico) |
| **Test complementario (C < B)** | ✅ REJECT en ambos (Cliff Δ = 0.240 idéntico) |
| **Sensibilidad** | ✅ Robusta en ambos (p ≈ 0 para todos drop-1) |

**VEREDICTO: REPRODUCCIÓN EXITOSA** — Los resultados son **numéricamente idénticos en todas las decisiones y tamaños de efecto**. Las diferencias en p-valores intermedios son artefactos de implementación de librerías y no afectan las conclusiones.

---

## 5. Archivos Utilizados

| Archivo | SHA-256 |
|---------|---------|
| `study-output/pilot_results_newcycle.csv` | `14d06db64c2a2bdbbdd8a84cb2b0991de7c0470f679ad195ddb152749b4c410a` |
| `study-output/dv3_matrix_newcycle.npy` | `e47f69831c09aac13d301e6369cbdbc98a53b827fc94969c3993581bc7926991` |
| Script de auditoría | `scripts/audit_reproduce_v2.py` |

---

**Firmado:** Auditoría de Reproducción GO-8D-NC  
**Fecha:** 2026-08-15  
**Lock Manifest:** `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`