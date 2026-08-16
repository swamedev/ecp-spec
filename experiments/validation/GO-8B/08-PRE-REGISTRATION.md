# GO-8B Entregável 8 — Pré-Registro (Preregistration)

**Status:** PRÉ-REGISTRO — PENDING R7 AUDIT · HASH STATUS: **PENDING LOCK PROTOCOL**
**Data de elaboração:** 2026-08-11
**Versão:** 1.0 (R6)
**Governado por:** GO-8B-R5 (M-1..M-3) + GOVERNANCE GATE R5 (R5-GOV-01..04, aplicadas em R6) + Entregáveis 00–07
**Documento de referência de decisões:** `00-GO-8B-R5-GOVERNANCE-DECISION-RECORD.md`

> Este documento **pré-registra** o desenho e o plano de análise do piloto GO-8B, tal como **já decididos** em 00–07 e nas decisões R5-GOV-01..04. **Não introduz nenhum parâmetro novo, não contém hashes finais e não constitui execução experimental.**

---

## 1. Declaração de Não-Execução

- **Nenhum experimento foi executado** para elaborar este pré-registro.
- **Nenhum dado experimental foi criado ou coletado.**
- **As simulações metodológicas autorizadas (potência — seed `20260811`; cobertura do bootstrap — seed `20260812`) NÃO constituem coleta experimental e NÃO entram como observações do estudo.** São análises metodológicas prévias, distintas do experimento científico.
- **Nenhum hash final foi gerado.** Todos os hashes permanecem `PENDING LOCK PROTOCOL`.
- Lock Protocol **não** aplicado.

---

## 2. Contexto e Objetivo (referência: 06 §1.3.2)

Comparar a similaridade estrutural `S_struct` do grafo reconhecido (espaço sintético da condição) com o grafo canônico ECP, entre as **3 condições de reconstrução**, sobre os **BIPs válidos**, para avaliar a utilidade da taxonomia sintética C3 no piloto metodológico GO-8B.

---

## 3. Desenho Experimental (Pré-registrado — Fixado)

| Parâmetro | Especificação | Fonte |
|---|---|---|
| **Unidade experimental** | **BIP/Caso** | 06 §1.3 |
| **N (tamanho de amostra)** | **7 BIPs** (piloto); análise prossegue com ≥ 5 válidos | R5-GOV-01; 07 §8 |
| **Seeds por célula** | **3 seeds por (BIP × condição)** | R5-GOV-02/03; 06 §1.3.1 |
| **Agregação** | `cell_value = median(seed_1, seed_2, seed_3)` | 06 §1.3.1 |
| **Condições** | **3** — (A) Cega pura (só Atomic Facts) · (B) Cega + Taxonomia C3 · (C) Não-cega (narrativa completa) | 06 §1.2 |
| **Medida repetida** | seed = observação repetida dentro de BIP × condição; **não é unidade independente** | 06 §1.3.1 |
| **N nunca é multiplicado** por avaliadores ou seeds | `N = nº de BIPs válidos` | 06 §1.3 |

**BIPs (7, Entregável 1):** BIP-001 Deepwater Horizon · BIP-002 Hyatt Regency · BIP-003 Operation Warp Speed · BIP-004 Genoma Humano · BIP-005 Ever Given/Suez · BIP-006 I-35W Bridge · BIP-007 Resposta Ebola.

**Taxonomias e namespaces (referência: 02 §1, 04 R5 M-1):** C1=T_ECP (`ECP`) · C2=T_PERM (`CAT`) · C3=T_SYNTH (`SYN`) · C4=T_NULL (`NULL`). O campo `taxonomy_namespace` é **obrigatório** e exclusivo por reconstrução; mistura de namespaces → `NAMESPACE_MIX` (rejeição). Nenhum mapping entre namespaces.

---

## 4. Variáveis

| Variável | Papel | Definição | Fonte |
|---|---|---|---|
| **S_struct** | **Primária / confirmatória** | Similaridade topológica WL Subtree Kernel (anonimização `"neutral"`), ∈ [0,1] | 05 §3 |
| **S_sem** | **Exploratória** | Alinhamento semântico contínuo (Hungarian); **não confirmatória** | 05 §4 |
| **K = α·S_struct + (1−α)·S_sem** | Exploratória | α = 0.6 pré-especificado | 05 §6 |

---

## 5. Hipóteses (Pré-registradas — 06 §2)

### 5.1 Omnibus (primária)
> **H₀:** A distribuição de S_struct é idêntica nas 3 condições (A, B, C) sobre os BIPs válidos.
> **H₁:** Pelo menos uma condição difere.

### 5.2 Pós-hoc (condicionadas à rejeição de H₀)
| Comparação | Hipótese |
|---|---|
| B vs A | S_struct(B) > S_struct(A) — taxonomia C3 adiciona estrutura |
| C vs A | S_struct(C) > S_struct(A) — narrativa completa (upper bound) |
| C vs B | S_struct(C) ≥ S_struct(B) |

### 5.3 Exploratórias (não confirmatórias)
Interação Caso × Condição; efeito avaliador (P-0010); S_sem diagnóstico.

---

## 6. Plano de Análise Estatística (Pré-registrado — Fixado)

| Elemento | Especificação | Fonte |
|---|---|---|
| **Teste global (primário)** | **Friedman** (df = 2) | 06 §3; R5 M-2 |
| **α** | **0.05** | 06 §3.3; R3-04 |
| **Pós-hoc** | **Wilcoxon signed-rank pareado, bilateral** | 06 §4 |
| **Correção** | **Holm-Bonferroni** (3 comparações) | 06 §4.1 |
| **Tamanho de efeito** | Kendall's W (omnibus); r_rb e Cliff's δ (pós-hoc) | 06 §3.4, §4.2 |
| **ICs 95%** | Bootstrap percentil B=10.000 (pareado); **IC exato da mediana reportado ao lado** do IC percentil (mitigação STAT-08, R6) | 06 §4.3, §4.3.1 |
| **Nenhuma decisão unilateral** após resultados | proibido | R3-04 |

**Ordem de execução** (06 §7): data check → agregação (mediana das 3 seeds) → descritiva → Friedman → pós-hoc (se H₀ rejeitada) → exploratório → sensibilidade → relatório.

---

## 7. Análises de Sensibilidade (Pré-registradas — R6)

| Item | Especificação | Fonte |
|---|---|---|
| **STAT-04 (outliers)** | **NÃO winsorizar**; reportar com/sem outliers; reexecutar Friedman/Wilcoxon sem outliers (IQR×1.5) | R5-GOV-04 |
| **STAT-06 (exploratório)** | Exploratório **sem controle formal de família**; rotulado explicitamente | R5-GOV-04 |
| **STAT-08 (bootstrap)** | B=10.000 suficiente (erro MC desprezível); **mediana por condição** com cobertura sub-nominal em N=7 (≈0.87–0.88) — reportar IC exato da mediana ao lado; diferença pareada ≈0.93; limitação registrada | R5-GOV-04; 06 §4.3.1 |
| **STAT-09 (domínio)** | Sensibilidade excluindo **1 caso por par dependente** (Hyatt OU I-35W; Ebola OU Warp Speed); **sem modelo misto** | R5-GOV-04; 06 §7 |

---

## 8. Equivalência / TOST (Pré-registrado — Não Vigente)

> **DECIDIDO (R3-03 + R5-GOV-03):** TOST é **secondary/optional**; **nenhuma Δ aprovada**; **Δ = 0.10 explicitamente NÃO aprovada**; **TOST NÃO será executado no piloto**. Apenas a hipótese de superioridade (H₁) é avaliada.

---

## 9. Potência (Pré-registrada — Limitação, NÃO justificativa)

- **Potência do piloto (N=7): ≈ 0.63** (IC 95% 0.617–0.644) sob o cenário S1_PRIMARY pré-especificado (μ=(0.50, 0.60, 0.66); σ_b=0.12, σ_e=0.08, σ_s=0.06; 3 seeds/célula; mediana; Friedman; α=0.05; B=5.000; seed `20260811`). — **06 §5.2/§5.3.**
- **Esta é uma limitação pré-registrada do piloto**, reportada §10/§5.3/§5.4. A potência de N=12 (≈0.895) **NÃO será usada para justificar retroativamente N=7**: a decisão R5-GOV-01 **já fixou N=7** (banda: mínimo 5 / piloto 7 / potência 12).
- Nenhuma alteração de desenho decorre deste pré-registro; banda §5.4 de 06 é a oficial.

---

## 10. Critérios de Exclusão e Go/No-Go (referência: 07)

- Exclusões automáticas: FP-01..08 (piloto), FC-01..07 (caso), FE-01..05 (avaliador), FR-01..06 (reconstrução). Nenhuma exclusão manual.
- **Go/No-Go para análise (07 §8):** ≥ 5 casos válidos de 7; ≥ 4 domínios distintos; matriz N×3 completa; nenhum `FAIL-PILOT`.
- Insuficiência → "PILOT INCONCLUSIVE — insufficient data"; **não** executar análise estatística.

---

## 11. Critérios de Interpretação (Decision Rules — 06 §10)

| Cenário | Interpretação |
|---|---|
| Friedman p<0.05 **E** B>A (Holm) | Evidência a favor da utilidade de C3 |
| Friedman p<0.05 **E** C>A **MAS** B≈A | C3 não justificada; rever design |
| Friedman p≥0.05 | Nenhuma evidência; **NÃO** é equivalência; reportar limitação de potência (N=7 ≈0.63) |
| Friedman p<0.05 **MAS** A>B | C3 prejudica; falha crítica |
| TOST | **não executado** (sem Δ aprovada) |

---

## 12. Configurações de Reprodutibilidade (Registradas — sem hashes)

```yaml
seed_statistics:        { value: 1879048193, type: uint64 }   # análise estatística (06 §9.1)
seed_c2:                { value: 11473621728585666159, type: uint64 }  # permutação C2 (02 §4)
seed_generation:        { value: 12088763053434307680, type: uint64 }  # geração C3, se estocástico (03 §3.3)
seed_power_simulation:  { value: 20260811, type: uint64 }     # simulação de potência (06 §9.2) — metodológica
seed_coverage_bootstrap:{ value: 20260812, type: uint64 }     # simulação de cobertura STAT-08 (06 §4.3.1) — metodológica
```

**Isolamento de streams:** cada seed tem uso exclusivo; nenhuma reutilização entre streams.

**Software:** Python 3.11+; `scipy.stats` (friedmanchisquare, wilcoxon), `numpy`, `pandas`, `scikit-posthocs` (Holm); scripts `go8b_statistical_analysis.py`, `go8b_power_sim.py`.

---

## 13. Compromissos Pré-Registrados (O que está comprometido / proibido)

**Comprometido:** Friedman primário; Wilcoxon bilateral + Holm; α=0.05; unidade BIP/Caso; N=7; 3 seeds/célula; mediana; sensibilidade STAT-04/06/08/09; poder N=7 reportado como limitação.

**Proibido neste piloto:** TOST (sem Δ aprovada); winsorização; transformação de S_struct; modelo misto; tuning de parâmetros pós-resultados; decisões unilaterais; correção de N por resultados; tratar simulações metodológicas como observações experimentais; preencher hashes fora do Lock Protocol.

---

## 14. Status e Próximos Passos

- **HASH STATUS:** todos os artefatos e o próprio pré-registro permanecem **PENDING LOCK PROTOCOL**.
- **Próxima parada obrigatória:** **AUDITORIA R7** (consistência do pré-registro contra 00–07). **Não** é a execução do piloto.
- Após **PASS explícito da R7**, discutir o Lock Protocol em etapa separada.

---

**Fim do Entregável 8.** Nenhum experimento executado. Nenhum dado experimental coletado. Nenhum hash final gerado. Lock Protocol não aplicado.
