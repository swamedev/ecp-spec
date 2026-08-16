# D-MV-03 — GOVERNANCE DESIGN DECISION

**Data:** 2026-08-15
**Gate:** D-MV-03 (Governance Design Decision) — antes do pré-registro do novo ciclo
**Status:** **APPROVED** (decisão formal da governança)
**Antecedentes:** D-MV-01 (DV confirmatória aprovada) · D-MV-02 (recálculo de potência com DV3)

---

## 1. Decisão de Desenho

| Parâmetro | Decisão |
|---|---|
| **DV confirmatória** | **DV3 = (conf + ged_ecp + ent_n12)/3** (pesos 1:1:1) |
| **Referência GED** | **ECP comum** (grafo canônico de 9 nós) |
| **Denominador entropia** | **log(12)** comum |
| **Teste confirmatório** | **TOST A−C com Δ = 0.05** |
| **N** | **N = 30 BIPs** (30 × 3 condições × 3 seeds = **270 execuções**) |
| **Testes adicionais** | Friedman (df=2, α=0.05), Wilcoxon+Holm (pares B−A, A−C, B−C), tamanhos de efeito |
| **Novos BIPs** | **18 adicionais** (além dos 12 existentes do GO-8C/GO-8D) |

## 2. Justificativa para N=30

1. **TOST A−C confirmatório** exige N=30 para poder ≥ 0.80 sob o cenário de efeito observado DV3
   (S1): poder = 0.804 em N=30 vs 0.703 em N=24 e 0.441 em N=12 (D-MV-02, B=3.000 simulações).
2. **O efeito A−C observado (0.0368) está dentro de Δ=0.05** — a equivalência é a decisão mais
   difícil e a que define o N; reduzir o N comprometeria a pergunta confirmatória.
3. **Superioridade (B<A)** fica coberta com folga: Wilcoxon B−A ≈ 1.000 e Friedman ≈ 1.000 em N=30.
4. **Cobertura de cenários:** N=30 atende poder ≥ 0.80 também sob S2 (conservador) e S3 (mínimo
   de interesse) para os três testes.
5. **Não reduzir para N=10–14:** isso alteraria a pergunta confirmatória (equivalência A−C deixaria
   de ser testável com poder adequado), não sendo aceito pela governança.

## 3. Justificativa para Manter TOST A−C como Confirmatório

- A pergunta original do programa (GO-8C) envolve comparar a condição cega pura (A) com a não-cega
  (C) e a cega + C3 (B); a **equivalência A−C dentro de uma margem clinicamente/pragmaticamente
  relevante (Δ=0.05)** é uma inferência de não-inferioridade que complementa o teste de
  superioridade B<A.
- O TOST evita a falácia de interpretar "ausência de significância" como equivalência; com Δ
  formalmente definido (D-06 do GO-8D, Δ=0.05), o desenho mantém coerência com o programa.
- DV3 recalibrada mostra A−C mediano = +0.0368 (< Δ=0.05) — a equivalência é **empiricamente
  plausível** e testável, tornando o TOST informativo e não fútil.

## 4. Impacto

### 4.1 Recursos de Dados

- **18 novos BIPs** além dos 12 existentes (Deepwater, Hyatt, OWS, Genoma, EverGiven, I-35W,
  Ebola, Apollo13, Chernobyl, TacomaNarrows, Dominos, Eyjafjallajökull).
- Cada BIP exige: narrativa-fonte, atomic facts parseáveis (gate D-04), validação de domínio e
  disponibilidade de fontes primárias.
- **Custo de aquisição a ser planejado** — autorizado o planejamento, **não** a execução da coleta.

### 4.2 Execuções

- **270 execuções determinísticas** (30 BIPs × 3 condições × 3 seeds, seed_master a definir no
  pré-registro do novo ciclo — distinct do 20260815 do GO-8D).

### 4.3 Tempo/Ordem

- A aquisição dos 18 BIPs deve ocorrer **antes** da execução; o cronograma do ciclo futuro deverá
  contemplar: aquisição → validação de parseabilidade → Lock → execução → análise.

## 5. Autorizações

1. **Autorizado:** planejamento da aquisição dos 18 novos BIPs (definição de critérios, fontes,
  pipeline de entrada, orçamento/lista).
2. **NÃO autorizado (ainda):** coleta efetiva dos novos BIPs, pré-registro final, Lock do novo
  ciclo, execução experimental.

## 6. Próximo Passo

1. Preparar o **pré-registro (08-PRE-REGISTRATION)** do novo ciclo com:
   - DV3 congelada (conf + ged_ecp + ent_n12)/3, pesos 1:1:1;
   - N = 30 BIPs (270 execuções);
   - TOST A−C Δ=0.05 confirmatório;
   - Friedman + Wilcoxon+Holm + tamanhos de efeito;
   - **lista dos 18 novos BIPs para aprovação da governança**;
   - especificação operacional completa (referência ECP comum, denominador log(12), clamp [0,1],
     unidade = BIP, célula = mediana das seeds) e limitações de ged_ecp.

---

**Fim do documento. D-MV-03 APPROVED (2026-08-15). Sem coleta, sem pré-registro, sem Lock, sem
experimento — Lock GO-8D intocado.