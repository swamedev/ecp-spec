# GO-8D — RELATÓRIO FINAL DO PROJETO

**Status:** **CLOSED** — hipótese C3 rejeitada
**Data de encerramento:** 2026-08-14
**Aprovação:** decisão formal da governança (2026-08-14)
**Executores:** ciclo confirmatório completo — pré-registro v1.0, Lock, execução, validação e análise estatística

---

## 1. Resumo Executivo

O GO-8D executou o estudo confirmatório N=12 da hipótese de utilidade da taxonomia C3 como
intervenção na reconstrução de BIPs (Blueprint Interpretability Protocol) sob a DV_confirm
(`DV_confirm = (conf + ged_ref + ent)/3`, pesos 1:1:1). Foram executadas **108 reconstruções**
(12 BIPs × 3 condições × 3 seeds determinísticas, `seed_master = 20260815`), todas com **PASS**
(108/108), validação de dados **9/9 checks PASS** e gates D-04 (parseabilidade) 12/12 BIPs.

**Resultado central:** a taxonomia C3 (condição B) **reduziu** a DV_confirm em relação à condição
cega pura (condição A) em **todos os 12 BIPs** (Cliff δ = 1.000). Não há evidência de utilidade da
C3; a hipótese de utilidade é **rejeitada** com conclusão negativa.

## 2. Resultados Estatísticos (pré-registro §6; `study-output/STATISTICAL-REPORT-G8D.md`)

| Teste | Resultado | Decisão |
|---|---|---|
| Friedman (df=2, α=0.05) | χ²_F = 18.5000, **p = 0.000096** | **Rejeita H₀** |
| Kendall's W | **0.7708** (IC95% bootstrap (0.5833, 1.0000)) | Efeito grande |
| Wilcoxon + Holm (3 pares) | **3/3 rejeitados**: A−B p=0.0005, B−C p=0.0024, A−C p=0.0034 | Todas rejeitadas |
| TOST Δ=0.05 (D-06) | A−C IC=(−0.0501, −0.0171); A−B IC=(−0.0988, −0.0721); B−C IC=(0.0288, 0.0740) | **Nenhum par equivalente** |
| Sensibilidade (drop 1 caso) | todos p<0.05 (p∈[0.0001, 0.0003]) | Robusta |

**Medianas da DV_confirm por condição:** A = 0.7134 · B = 0.6220 · C = 0.6843 (IC exato da
mediana: A [0.6873, 0.7216] · B [0.6035, 0.6357] · C [0.6474, 0.7017]).

## 3. Interpretação

- **B < A em todos os 12 BIPs:** a adição da taxonomia C3 à condição cega pura reduz
  sistematicamente a fidelidade da reconstrução sob a DV_confirm (r_rb = −1.000, Cliff δ = 1.000
  para o par A−B, sinal r_rb negativo = B abaixo de A).
- **A > C (p=0.0034):** a condição cega pura também supera a não-cega (narrativa completa).
- **C > B (p=0.0024):** a narrativa completa supera a cega + C3, mas permanece abaixo da cega pura.
- **Equivalência A−C não demonstrada** dentro de Δ=0.05 (IC marginal: limite inferior −0.0501
  excede −0.05 por 0.0001); reportado com cautela (pré-registro §9).
- **Go/No-Go metodológico:** **GO** (12/12 casos válidos ≥ 10, matriz N×3 completa, 108/108 PASS).

## 4. Limitações

1. **DV_confirm não captura utilidade da C3:** a redução observada em B pode refletir limitação da
   métrica composta (conf/ged_ref/ent) para mensurar o valor de uma taxonomia ontológica; a C3
   adiciona informação que a DV_confirm trata como ruído, não como melhoria semântica.
2. **N=12 (suficiente para Friedman, potência ≈ 0.999 pré-registrada),** mas o efeito negativo
   grande (δ=1.000) torna irrelevante qualquer subtamanho amostral para a direção observada.
3. **Equivalência marginal A−C:** o limite inferior do IC (0.0001 além de −0.05) impede conclusão
   forte de equivalência; sem decisão unilateral (R3-04).
4. **Sem modelo misto (STAT-09):** a sensibilidade usou drop de 1 caso por vez; BIPs não foram
   modelados como efeito aleatório (deliberadamente excluído no pré-registro).
5. **Sinalização da direção da hipótese:** o pré-registro §9 assumia B > A como ganho; o desfecho
   B < A foi interpretado como falha de utilidade (não estava previsto como cenário de sucesso).
6. **Validade ecológica:** reconstruções simuladas por engine determinística; a extrapolação para
   reconstruções humanas/organizacionais reais é limitada.

## 5. Conclusão e Recomendação

**Conclusão:** a hipótese de utilidade da taxonomia C3 como intervenção é **rejeitada**. A C3
reduziu a DV_confirm em todos os 12 BIPs em relação à condição cega pura, e a equivalência com a
condição não-cega não foi demonstrada dentro de Δ=0.05.

**Recomendação (decisão da governança):** **não utilizar a C3 como intervenção em futuros ciclos,
salvo nova justificativa teórica.** Nenhum novo ciclo (GO-8E) é aberto neste momento. Os artefatos
(pipeline reprojetado, pré-registro, seeds, resultados e análise) ficam disponíveis para reuso ou
auditoria, incluindo a possibilidade de uma hipótese alternativa de utilidade da C3 a ser
formalizada em ciclo futuro.

## 6. Decisão Formal da Governança (2026-08-14)

1. Os resultados são **aprovados**.
2. O GO-8D é **encerrado** com conclusão negativa para a hipótese C3.
3. Recomendação: não utilizar C3 como intervenção em futuros ciclos, salvo nova justificativa teórica.
4. Nenhum novo ciclo (GO-8E) é aberto neste momento.

---

**Fim do relatório final. GO-8D CLOSED (2026-08-14).**