# D-MV-02 — RECÁLCULO DE POTÊNCIA com DV3 congelada

**Data:** 2026-08-14
**Gate:** D-MV-02 (após D-MV-01 APPROVED)
**DV congelada:** `DV3 = (conf + ged_ecp + ent_n12)/3` (pesos 1:1:1; referência ECP comum; denom. log(12))
**Método:** Simulação de Monte Carlo calibrada com dados GO-8D (matriz DV3 real, 12 BIPs × 3 condições)
**Artefatos:** `metric-validation/power_dv3.py`, `power_calibration.json`, `power_summary.json`, `power_dv3_results.npy`
**Regras:** sem novo experimento; sem Lock; sem pré-registro ainda (aguarda N).

---

## 1. Modelo de Simulação (calibrado)

Unidade de análise = **BIP** (célula = mediana das seeds). Modelo de efeitos pareados por BIP,
calibrado nos dados DV3 reais do GO-8D:

```
A_i ~ N(0.6205, 0.0175)          # mediana A e SD entre BIPs observados
delta_BA_i ~ N(delta_BA, 0.0312) # SD pareado B−A observado
delta_CA_i ~ N(delta_CA, 0.0288) # SD pareado C−A observado
B_i = A_i + delta_BA_i
C_i = A_i + delta_CA_i
clamp [0,1]
```

**Parâmetros calibrados (DV3, GO-8D):** mediana A=0.6205, B=0.5890, C=0.5885; Δ B−A = −0.0374
(sd 0.0312); Δ A−C = +0.0368 (sd 0.0288); SD entre BIPs A=0.0175.

**Configuração:** B=3.000 simulações por (N, cenário); α=0.05; Δ=0.05; teste TOST pareado
(two one-sided t-tests); Wilcoxon signed-rank pareado bilateral (par B−A, superioridade B<A);
Friedman df=2 (omnibus). RNG `default_rng(20260814)`.

## 2. Cenários

| Cenário | δ_BA | δ_CA | Justificativa |
|---|---|---|---|
| **S1 — Efeito observado** | −0.0374 | −0.0368 | Magnitude real DV3 (estudo GO-8D) |
| **S2 — Efeito conservador** | −0.0280 | −0.0280 | 75% do efeito observado (C<A similar a B<A) |
| **S3 — Efeito mínimo de interesse** | −0.0500 | 0.0000 | |B−A| = Δ=0.05 (limite de interesse); A≈C (equivalência) |

## 3. Resultados — Poder por N (proporção de rejeição)

### S1 — Efeito observado

| N | Friedman | Wilcoxon B−A | TOST A−C |
|---|---|---|---|
| 6 | 0.668 | 0.488 | 0.241 |
| 8 | 0.815 | 0.773 | 0.319 |
| 10 | 0.912 | 0.900 | 0.359 |
| **12** | **0.970** | **0.946** | 0.441 |
| 14 | 0.987 | 0.979 | 0.499 |
| 20 | 0.999 | 0.997 | 0.628 |
| **30** | 1.000 | 1.000 | **0.804** |
| 36 | 1.000 | 1.000 | 0.856 |

**N mínimo (poder ≥ 0.80):** Friedman **8** · Wilcoxon B−A **10** · TOST A−C **30**

### S2 — Efeito conservador

| N | Friedman | Wilcoxon B−A | TOST A−C |
|---|---|---|---|
| 12 | 0.821 | 0.768 | 0.795 |
| **14** | 0.852 | **0.857** | **0.860** |
| 16 | 0.932 | 0.897 | 0.905 |

**N mínimo (poder ≥ 0.80):** Friedman **12** · Wilcoxon B−A **14** · TOST A−C **14**

### S3 — Efeito mínimo de interesse

| N | Friedman | Wilcoxon B−A | TOST A−C |
|---|---|---|---|
| 6 | 0.732 | 0.713 | 0.948 |
| **8** | 0.851 | **0.944** | 0.996 |
| 10 | 0.915 | 0.990 | 0.998 |

**N mínimo (poder ≥ 0.80):** Friedman **8** · Wilcoxon B−A **8** · TOST A−C **6**

## 4. N Recomendado

**Recomendação: N = 30 BIPs** (30×3=90 células × 3 seeds = **270 execuções**).

**Justificativa:**
1. **Teste mais exigente = TOST A−C com efeito observado** (S1): com N=30, poder de equivalência
   = **0.804 ≥ 0.80**; com N=24, apenas 0.703. O TOST é o teste com menor poder nos dados DV3
   porque o efeito A−C observado (0.0368) está **dentro** de Δ=0.05 — a equivalência é difícil de
   demonstrar quando o efeito verdadeiro é próximo do limite.
2. **Superioridade (B<A)** está coberta com folga: N=30 → Wilcoxon B−A poder ≈ 1.000 (vs ≥0.80
   já em N=10).
3. **Cobertura de cenários:** N=30 satisfaz poder≥0.80 para TOST também sob S2 (conservador)
   e S3; é o único N que garante os três testes simultaneamente no cenário mais desafiador.
4. **Custo operacional:** 270 execuções determinísticas (~mesmo pipeline) — viável; não é um
   aumento de ordem de grandeza.
5. **Cautela (não-calculada como teste, apenas operacional):** como a unidade é o BIP, N=30 exige
   **30 BIPs**; o GO-8C/GO-8D tem 12. Ciclo futuro precisará de **18 novos BIPs** (ou reuso com
   pool maior). Este é um custo de aquisição de dados a considerar na viabilidade.

**Alternativas:**
- **N=14** se a governança priorizar o cenário conservador (S2) e aceitar TOST A−C sob efeito
  observado com poder < 0.80 (0.499 em N=14) — **não recomendado** se equivalência for objetivo.
- **N=24** como meio-termo (superioridade ~1.0; TOST 0.703) — abaixo do limiar de 0.80 para TOST.

## 5. Impacto no Desenho Futuro

1. **N = 30 BIPs** (ou 24 se equivalência rebaixada a secundária) — o N dependerá do **objetivo
   primário**: se o objetivo é **detectar B<A (superioridade)**, N=10–14 basta; se inclui
   **demonstrar equivalência A−C dentro de Δ=0.05**, N=30 é necessário.
2. **Componente de equivalência A−C:** dados DV3 mostram efeito real A−C=0.0368 (<Δ=0.05) — há
   chance realista de equivalência, mas é marginal; o estudo deve **pré-especificar** se TOST é
   objetivo primário ou secundário (afeta o N).
3. **Recursos de dados:** 30 BIPs → 18 novos além dos 12 existentes; o desenho deve prever a
   expansão do corpus de BIPs (ou restringir o escopo).
4. **Pipeline determinístico:** célula = mediana de 3 seeds; o número de seeds pode ser reavaliado
   (mais seeds reduzem o ruído da célula, potencialmente reduzindo o N — não testado aqui para
   manter coerência com GO-8D).
5. **Sensibilidade ao modelo:** assumimos normalidade das diferenças pareadas e SDs fixos
   (calibrados); em ciclos futuros, recomenda-se revalidar com os dados reais.

## 6. Conclusão

- **N recomendado = 30 BIPs** para poder ≥ 0.80 em **todos** os testes (Friedman, Wilcoxon+Holm
  B−A, TOST A−C) sob o cenário de efeito observado DV3.
- Se a equivalência A−C for **secundária**, **N=14** atende superioridade sob cenário conservador.
- **Próximo passo:** preparar o pré-registro do novo ciclo com **DV3 congelada** e **N=30**
  (ou N definido pela governança conforme o objetivo primário), incluindo a especificação
  operacional completa da DV3 e as limitações de ged_ecp.

---

**Fim do relatório. D-MV-02 concluído — nenhum experimento novo, nenhum Lock, nenhum pré-registro
criado; Lock GO-8D intocado (PASS 95/95); novos arquivos apenas em `metric-validation/`.