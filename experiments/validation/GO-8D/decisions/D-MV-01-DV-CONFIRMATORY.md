# D-MV-01 — Aprovação da DV Confirmatória (análise decisória, sem execução experimental)

**Data:** 2026-08-14
**Gate:** D-MV-01 — METRIC VALIDATION → aprovação da DV candidata
**Estado:** GO-8D CLOSED · Metric Validation COMPLETE · DV0 rejeitada · **DV3 candidata principal**
**Análise:** `metric-validation/calibration_cells.json`, `metric-validation/criteria_eval.json` (re-derivação validada com erro 0.0 vs CSV)
**Regra da etapa:** não escolher métrica por p-valor; sem novo experimento; sem recálculo de potência; Lock GO-8D intocado.

---

## 1. Avaliação da DV3 como Candidata Confirmatória

**DV3 = (conf + ged_ecp + ent_n12)/3** — `conf` fidelidade por fato (inalterado); `ged_ecp`
similaridade GED vs referência comum ECP canônica (9 nós); `ent_n12` entropia com denominador
comum log(12).

### 1.1 Sensibilidade discriminativa de cada componente (share do |Δ B−A| médio)

| Componente | mean \|B−A\| | Share | corr(comp, DV3) |
|---|---|---|---|
| conf | 0.0041 | **3.2%** | 0.307 |
| ged_ecp | 0.0308 | **23.6%** | 0.485 |
| ent_n12 | 0.0952 | **73.2%** | 0.874 |

- `ent_n12` continua o principal motor (73%), mas **sem o artefato de denominador** (era 0.1985 →
  0.0952 de |Δ| médio com denominador comum; a metade restante é real — H bruta B<A).
- `ged_ecp` contribui 23.6% e é a componente que **neutraliza a vantagem estrutural de A**
  (Δ B−A −0.0236; B<A 8/12).
- `conf` é praticamente inerte para a decisão de condição (3.2%).

### 1.2 Distribuição por condição (N=12)

| Componente | A (mediana) | B | C | Observação |
|---|---|---|---|---|
| conf | 0.7343 | 0.7369 | 0.7222 | B≈A; C menor |
| ged_ecp | 0.3171 | 0.3132 | 0.3138 | A,B,C ≈ empatadas |
| ent_n12 | 0.8037 | 0.7297 | 0.7078 | A > B > C |
| **DV3** | **0.6205** | **0.5890** | **0.5885** | A > B ≈ C |

Distribuições: `dv3` A [0.603, 0.654], B [0.558, 0.628], C [0.517, 0.620] — **sobreposição parcial
entre condições** (diferente da DV0 onde as faixas eram separadas), refletindo que grande parte do
hiato era viés. B<A em **11/12 BIPs** (única exceção BIP-010, Δ=+0.0224). DV3 por BIP não mostra
caso dominante — a diferença é difusa, não dominada por poucos BIPs.

### 1.3 Comportamento sob dados sintéticos conhecidos

| Cenário | conf | ged_ecp | ent_n12 | DV3 (1:1:1) |
|---|---|---|---|---|
| perfect (1:1 ECP) | 1.000 | 1.000 | 0.884 | 0.961 |
| noisy (labels CAT, conf 0.5) | 0.500 | 0.443 | 0.884 | 0.609 |
| flat (2 categorias) | 0.900 | 0.562 | 0.276 | 0.579 |
| collapse (1 categoria) | 0.900 | 0.573 | 0.000 | 0.491 |

- Ordenação correta: **perfect > noisy > flat > collapse** — DV3 distingue reconstruções
  melhores/piores e penaliza forte o colapso de categorias (ent_n12=0) e baixa fidelidade (noisy).
- `ged_ecp` isolado não distingue flat de collapse (0.56 vs 0.57) — mas a composição com `ent_n12`
  resolve isso. ✅ comportamento adequado.

## 2. Justificativa dos Pesos 1:1:1

**Análise de sensibilidade a pesos (DV3 com alternativas):**

| Pesos (conf:ged:ent) | Δ B−A | B<A (n/12) | C<A (n/12) |
|---|---|---|---|
| **1:1:1 (0.333)** | **−0.0374** | **11/12** | 10/12 |
| 0.4:0.2:0.4 | −0.0397 | 11/12 | 10/12 |
| 0.25:0.5:0.25 (ged heavy) | −0.0297 | 10/12 | 11/12 |
| 0.2:0.2:0.6 (ent heavy) | −0.0580 | 11/12 | 10/12 |
| 0.6:0.2:0.2 (conf heavy) | −0.0207 | 10/12 | 10/12 |

**Avaliação:**
- **A decisão de condição (B<A) é robusta à ponderação** — varia apenas entre 10/12 e 11/12 em
  todas as combinações razoáveis. Nenhum conjunto de pesos razoável inverte a conclusão qualitativa
  (C3 não melhora vs A).
- **Os pesos 1:1:1 são defensáveis e recomendados:**
  1. **Princípio de não-arbitrariedade** — não há base empírica pré-registrada para pesos
     assimétricos; definir pesos pela magnitude do efeito (ex.: ent heavy porque ent tem maior
     |Δ|) introduziria **circularidade** (escolher a métrica/ponderação pelo resultado que ela
     produz — proibido pela regra da etapa).
  2. **Simetria teórica** — as três componentes medem dimensões distintas e complementares da
     fidelidade (fato, estrutura/semântica, distribuição); sem hipótese a priori de dominância,
     pesos iguais são a escolha neutra.
  3. **Estabilidade** — 1:1:1 está no meio do espectro (Δ −0.0374), não é nem o extremo ent-heavy
     (−0.0580) nem conf-heavy (−0.0207); não maximiza nem minimiza o efeito.
  4. **Interpretabilidade** — DV média de três subíndices [0,1] é transparente e auditável.
- **Recomendação:** **manter 1:1:1**. Registrar a análise de sensibilidade como evidência de que a
  conclusão não depende da escolha de pesos. Em futuro ciclo, poderá ser feita análise de
  pesos com base em dados de validação externa (discriminância de rótulos de qualidade), não na
  magnitude do efeito de condição.

## 3. Análise da Faixa Estreita de ged_ecp

**Fatos:**
- Faixa observada: **0.219 – 0.395** (IQR 0.303–0.341; 14 bins de 0.01 distintos em 36 células).
- A faixa é estreita e deslocada para baixo porque as similaridades **CAT/SYN → ECP** são obtidas
  por `text_emb` das definições textuais (cos ≈ 0.12–0.28 entre rótulos e nós canônicos ECP) —
  não há embeddings semânticos fortes mapeando as taxonomias opacas/sintéticas ao ECP canônico.
- Estruturalmente, `ged_ecp` **não** discrimina flat de collapse no teste sintético (0.56 vs 0.57)
  — é o componente mais fraco isoladamente.

**Avaliação (aceitável vs. exige melhoria):**

| Critério | Status |
|---|---|
| Viés de cardinalidade/referência | **Eliminado** (referência comum — era o objetivo do gate) |
| Discriminação de condição | Adequada dentro da faixa (Δ B−A −0.0236; 8/12; contribui 23.6%) |
| Discriminação absoluta (qualidade) | **Limitada** — faixa estreita comprime diferenças de qualidade |
| Comportamento sintético (flat vs collapse) | **Falho isoladamente** (compensado por ent_n12 na composição) |
| Papel no conjunto | Complementar — compensa o viés de `ent` no sentido oposto |

**Veredito:** a faixa estreita de `ged_ecp` é uma **limitação aceitável para a decisão de condição
atual** (remove o viés que motivou o gate; não distorce a comparação A/B/C), **porém não aceitável
como componente de qualidade absoluta isolado** — exige melhoria antes de um futuro estudo que use
a DV para ranking absoluto de reconstruções.

**Recomendação de melhoria (para futuro, fora deste gate):**
1. Treinar/ajustar embeddings CAT→ECP e SYN→ECP (ex.: projeção aprendida sobre definições,
   alinhamento por pares conhecidos) para elevar e alargar a faixa de similaridade.
2. Alternativa: usar `S_sem` (GED + alinhamento de rótulos) com pesos de aresta calibrados em
   dados sintéticos.
3. Reportar sempre `ged_ecp` e `ent_n12` separadamente (transparência) e a faixa observada.

## 4. Decisões (as três perguntas do gate)

| # | Pergunta | Decisão |
|---|---|---|
| 1 | DV3 aceita como candidata confirmatória? | **SIM** — atende os critérios de validade (escala, cardinalidade comum, sem vantagem estrutural), comportamento sintético correto e robustez qualitativa (B<A 11/12; Friedman p=0.006). |
| 2 | Pesos 1:1:1 justificados? | **SIM** — mantidos por não-arbitrariedade, simetria teórica e estabilidade; sensibilidade mostra robustez da conclusão (10–11/12 em qualquer ponderação razoável). |
| 3 | Faixa estreita de ged_ecp aceitável? | **PARCIALMENTE** — aceitável para comparação de condições (objetivo do gate); **exige melhoria** antes de uso como medida absoluta de qualidade em futuro estudo. |

## 5. Recomendação Final para a Governança

**DV3 está pronta para congelamento como DV confirmatória do próximo ciclo**, com as condições:

1. **Congelar** DV3 = `(conf + ged_ecp + ent_n12)/3`, pesos 1:1:1, com as definições operacionais
   documentadas (referência ECP comum; denominador log(12); clamp [0,1]).
2. **Documentar** as limitações registradas (faixa estreita de ged_ecp; ent_n12 concentra 73% do
   sinal) como notas de validade no pré-registro do futuro ciclo.
3. **Melhorar o mapeamento CAT/SYN→ECP** antes de um estudo que dependa de qualidade absoluta
   (item 3 da seção anterior) — sem bloquear o ciclo atual de comparação de condições.
4. **Próximo passo (se aprovada):** recálculo de potência com a DV3 congelada (N para Friedman
   e TOST Δ=0.05), e em seguida elaboração do pré-registro do novo ciclo.
   **Se rejeitada:** reformular a métrica (ex.: novos embeddings ECP, pesos alternativos
   justificados por validação externa) antes de qualquer potência.

---

**Fim do documento. Análise decisória read-only — nenhum experimento executado, nenhuma potência
recalculada, Lock GO-8D intocado (validado PASS, 95/95), nenhum arquivo congelado/untracked
alterado.