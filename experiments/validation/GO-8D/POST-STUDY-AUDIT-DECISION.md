# GO-8D — POST-STUDY AUDIT DECISION

**Data:** 2026-08-14
**Fase:** POST-STUDY AUDIT (pós-encerramento; nenhum ciclo experimental novo)
**Autor:** governança + executor (auditoria read-only sobre artefatos GO-8D)

---

## 1. Pergunta Central

**A DV_confirm é uma medida válida, ou penaliza sistematicamente a condição B
(cega + taxonomia C3)?**

Em outras palavras: a queda observada em B (mediana 0.6220 vs A 0.7134; B<A em 12/12 BIPs,
Cliff δ = 1.000) reflete um efeito real da taxonomia C3, ou é consequência de assimetrias
estruturais embutidas na métrica composta `(conf + ged_ref + ent)/3`?

## 2. Evidências Atuais

1. **Estudo confirmatório (CLOSED):** Friedman χ²=18.50, df=2, p=0.000096 (W=0.7708);
   Wilcoxon+Holm 3/3 pares rejeitados; TOST Δ=0.05 sem equivalência; B<A em 12/12 BIPs.
2. **Pipeline reprojetado (D-03):** DV_confirm = média de `conf` (fidelidade por fato),
   `ged_ref` (GED ponderada vs grafo de referência) e `ent` (entropia normalizada da
   distribuição de categorias sintéticas na reconstrução).
3. **Assimetria estrutural detectada (pré-análise de auditoria):**
   - `ent`: `n_slots` = **9** para A/C, **12** para B (`run_study_g8d.py:170`) — a normalização
     `H/log(n_slots)` usa denominadores **diferentes entre condições**.
   - `ged_ref`: `CAT_REF` (9 nós, 8 arestas) para A/C vs `SYN_REF` (12 nós, 13 arestas) para B —
     o denominador `max_cost` da GED é ~19–20% maior para B, deflacionando a similaridade.
   - `conf`: sem assimetria estrutural óbvia (mediana B≈A).

## 3. Critérios de Avaliação

| Critério | Operacionalização |
|---|---|
| C1. Dominância de componente | Qual componente contribui mais para B<A (share de \|Δ\| médio)? |
| C2. Consistência entre BIPs | B<A é consistente em 12/12 ou dominada por poucos casos? |
| C3. Assimetria estrutural de normalização | `ent` penaliza B por denominador distinto (log 9 vs log 12)? |
| C4. Assimetria estrutural de referência | `ged_ref` penaliza B por referência maior (12 nós vs 9)? |
| C5. Robustez qualitativa | B<A persiste após correção das assimetrias (denominador comum)? |

**Regra de decisão:**
- Se **C3 e/ou C4 confirmados** → a DV_confirm tem viés de calibração entre condições;
  o efeito B<A é **parcialmente artefato métrico** → DV_confirm **problemática** para comparação
  entre condições como construída.
- Se B<A **persistir** após renormalização (C5) → o efeito tem componente real, mas a
  **magnitude** reportada no GO-8D é **inflada**.

## 4. Possíveis Decisões

| Opção | Ação |
|---|---|
| **DEC-A (recomendada se assimetrias confirmadas)** | Declarar a DV_confirm **problemática para comparação entre condições**; reportar correção (denominador comum, referência padronizada); concluir que o efeito B<A é qualitativamente real porém **inflado na magnitude**; **sem** reabrir o ciclo (nenhum novo experimento). |
| **DEC-B** | Aceitar a DV_confirm como válida conforme desenhada (sem correção) — requer justificativa de que assimetrias são intencionais. |
| **DEC-C** | Auditoria aprofundada adicional (análise por subcomponente, por domínio, sensibilidade a pesos 1:1:1) antes de qualquer conclusão. |

---

**Decisão da governança (a ser registrada após o relatório de decomposição):**
`POST-STUDY-DV-DECOMPOSITION.md`.