# GO-8D — Pré-registro do estudo confirmatório (v1.0 — APROVADO)

**Status:** **APROVADO** (governança GO-8D, 2026-08-14) · HASH STATUS: **PENDING LOCK PROTOCOL**
**Data:** 2026-08-14
**Versão:** 1.0
**Ciclo:** GO-8D
**Governado por:** D-03 (reprojeto do pipeline + DV_confirm) · D-03.REV (revisão de desenho — Opção C aprovada) · D-04 (gate de parseabilidade) · D-05 (gate semântico híbrido) · D-06-TOST-DELTA-APPROVED (Δ=0.05) · D-07 (recálculo de N)

> Este documento é o **pré-registro formal aprovado** do estudo confirmatório GO-8D. **Não contém
> hashes finais; não constitui execução experimental; não gera seeds nem aplica o Lock Protocol.**
> Substitui o desfecho primário do GO-8C (S_struct) pela DV_confirm.

---

## 1. Declaração de Não-Execução

- **Nenhum experimento foi executado** para elaborar este esboço.
- **Nenhum dado experimental foi criado ou coletado.**
- **Nenhuma seed foi gerada** (valores de seed permanecem `PENDING LOCK PROTOCOL`; somente o
  método de geração é pré-especificado).
- **Nenhum hash final foi gerado.** Todos os hashes permanecem `PENDING LOCK PROTOCOL`.
- **Lock Protocol não aplicado.**
- As simulações metodológicas (D-02, D-03, D-07 — seeds `20260814` e anteriores) **não** entram
  como observações deste estudo.

---

## 2. Contexto e Objetivo

Comparar a **fidelidade da reconstrução semântica** entre as 3 condições de reconstrução (A/B/C),
sobre os **12 BIPs válidos**, usando a **DV_confirm** como desfecho primário — corrigindo os
viéses estruturais da S_struct do GO-8C (D-01/D-02) e o artefato de embeddings CAT (D-03).

**Mudança de paradigma:** em vez de similaridade topológica anonimizada vs ECP fixo (S_struct),
mede-se a fidelidade da reconstrução à **taxonomia da própria condição**, por 3 componentes
interpretáveis (fidelidade por fato, edição de grafo, entropia de atribuição).

---

## 3. Desenho Experimental (Pré-registrado — Fixado no esboço)

| Parâmetro | Especificação | Fonte |
|---|---|---|
| **Unidade experimental** | **BIP/Caso** | GO-8B 06 §1.3 |
| **N (tamanho de amostra)** | **12 BIPs** (001–012); análise prossegue com ≥ 10 válidos | D-07; GO-8C D-04 |
| **Seeds por célula** | **3 seeds por (BIP × condição)** | GO-8B 06 §1.3.1 |
| **Agregação** | `cell_value = median(seed_1, seed_2, seed_3)` | GO-8B 06 §1.3.1 |
| **Condições** | **3** — (A) Cega pura (só Atomic Facts) · (B) Cega + Taxonomia C3 · (C) Não-cega (narrativa completa) | GO-8B 06 §1.2 |
| **N nunca é multiplicado** por avaliadores ou seeds | `N = nº de BIPs válidos` | GO-8B 06 §1.3 |
| **Total de execuções** | **12 × 3 × 3 = 108 reconstruções** | D-07; mesmo volume do GO-8C |

**BIPs (12):** os mesmos 12 do GO-8C (BIP-001..012) — **sem coleta nova**; materiais existentes
submetidos aos gates D-04 (parseabilidade) e D-05 (semântico híbrido) na produção.

**Taxonomia da condição (referência da métrica, P3/P4 do D-03):**
- **A e C:** cadeia CAT T_PERM (9 nós/8 arestas) — derivada de `C2_PERMUTATION.yaml`
  (`canonical_order` + `canonical_to_opaque`).
- **B:** DAG C3 corrigido (12 nós/13 arestas) — `C3_TAXONOMY.yaml` (corrigida).
- **Namespace operacional:** A → CAT, B → SYN, C → CAT (inalterado do GO-8C, D-02).
- **Rastreabilidade:** cada execução registra `taxonomy_sha256` (P5/D-03); esperado
  `5ba63db7a81c454d...` para a corrigida.

---

## 4. Variáveis (redesenhadas — D-03)

| Variável | Papel | Definição |
|---|---|---|
| **DV_confirm** | **Primária / confirmatória** | `DV_confirm = (conf + ged_ref + ent) / 3 ∈ [0,1]` |
| **conf** | componente | Confiança média do classificador por fato (fidelidade) |
| **ged_ref** | componente | GED ponderada **vs taxonomia da condição** (substituição por cosseno de embeddings corrigidos; arestas dirigidas peso 0.5; normalizada em [0,1]) |
| **ent** | componente | Entropia de atribuição normalizada (Shannon / log nº slots da condição) |

**Embeddings corrigidos (P2):** CAT-XX → definição neutra PT (`CAT_NEUTRAL_DEFS`); SYN-XX →
definição corrigida; ECP → nome congelado. **Nenhum cosseno fixo 1.0** (correção do colapso da
S_sem/D-02 M4).

**Pesos:** **1:1:1** (congelado no pré-registro; aprovado na revisão D-03.REV).

---

## 5. Hipóteses (Pré-registradas)

### 5.1 Omnibus (primária)
> **H₀:** A distribuição de DV_confirm é idêntica nas 3 condições (A, B, C) sobre os BIPs válidos.
> **H₁:** Pelo menos uma condição difere.

### 5.2 Pós-hoc (condicionadas à rejeição de H₀)
| Comparação | Hipótese | Tipo |
|---|---|---|
| A vs B | DV_confirm(A) ≠ DV_confirm(B) — efeito da taxonomia C3 | **Primária** |
| B vs C | DV_confirm(B) ≠ DV_confirm(C) — efeito da narrativa completa | **Primária** |
| A vs C | descritiva | Secundária |

### 5.3 Equivalência (secundária — TOST, Δ=0.05 aprovado na D-06)
| Par | Hipótese de equivalência |
|---|---|
| A vs C | DV_confirm(A) ≈ DV_confirm(C) dentro de Δ=0.05 (IC ⊂ (−0.05, +0.05)) |
| (demais pares) | equivalência não é hipótese; TOST apenas reporta IC vs Δ |

---

## 6. Plano de Análise Estatística (Pré-registrado)

| Elemento | Especificação |
|---|---|
| **Teste global (primário)** | **Friedman** (df = 2), α = 0.05 |
| **Pós-hoc** | **Wilcoxon signed-rank pareado, bilateral** (3 pares) |
| **Correção** | **Holm-Bonferroni** (3 comparações) |
| **Tamanho de efeito** | Kendall's W (omnibus); r_rb e Cliff's δ (pós-hoc) |
| **ICs 95%** | Bootstrap percentil B=10.000 (pareado); **IC exato da mediana reportado ao lado** (mitigação STAT-08) |
| **TOST / equivalência** | **VIGENTE**: Δ=0.05 (D-06 aprovado); equivalência se IC 95% da diferença pareada ⊂ (−0.05, +0.05); bootstrap pareado; aplicado nos pares após Holm |
| **Nenhuma decisão unilateral** após resultados | proibido (R3-04) |

**Ordem de execução** (GO-8B 06 §7 adaptado): data check → agregação (mediana das 3 seeds) →
descritiva → Friedman → pós-hoc (se H₀ rejeitada) → TOST (equivalência, secundária) →
sensibilidade → relatório.

**Sensibilidade (inalterada do GO-8C):** STAT-04 (não winsorizar; reportar com/sem outliers) ·
STAT-06 (exploratório sem controle formal de família) · STAT-08 (B=10.000; IC exato da mediana ao
lado) · STAT-09 (excluir 1 caso por par dependente; sem modelo misto).

---

## 7. Potência (Pré-registrada — recálculo D-07)

- **N=12 recomendado (D-07).** Sob o cenário fiel ao enunciado (efeitos pareados A−B=0.079,
  B−C=0.069, A−C=0.010; σ_e=0.0296 conservador; α=0.05; REPS=3.000; seed `20260814`):
  - Friedman: **0.999**;
  - Wilcoxon+Holm A−B: **0.999**; B−C: **0.996**;
  - TOST equivalência A−C: **0.919**.
- Todos os critérios ≥ 0.80 com folga. N=8 satisfaz superioridade mas **não** a potência de
  equivalência (0.788 < 0.80); N=10 é o mínimo; N=12 é o recomendado (comparabilidade com o
  GO-8C e reaproveitamento integral dos 12 BIPs).
- Análise de robustez: sob σ_e empírico (0.0189) a potência satura (≥0.99); sob σ_e conservador
  com efeitos de mediana (A−B=0.091, B−C=0.062) a potência primária permanece ≥ 0.95 em N=12.

---

## 8. Critérios de Exclusão e Go/No-Go

- **Exclusões automáticas:** mesmos critérios FP/FC/FE/FR do GO-8B 07, com adaptações de N=12
  (D-04 do GO-8C); **nenhuma exclusão manual**.
- **Go/No-Go para análise:** **≥ 10 de 12 casos válidos**; matriz N×3 completa.
- **Insuficiência:** < 10 casos válidos → "STUDY INCONCLUSIVE — insufficient data".
- **Gates de produção (GO-8D):** os 12 BIPs devem passar em **D-04 (parseabilidade)** e
  **D-05 (gate semântico híbrido)** antes do Lock; falha em qualquer gate → correção + revalidação.

---

## 9. Critérios de Interpretação (Decision Rules)

| Cenário | Interpretação |
|---|---|
| Friedman p<0.05 **E** B−A significativo (Holm) | Evidência de efeito da taxonomia C3 na fidelidade |
| Friedman p<0.05 **E** B−C significativo (Holm) | Evidência de efeito da narrativa completa |
| Friedman p≥0.05 | Nenhuma evidência; **NÃO** é equivalência; reportar potência N=12 (0.999) |
| TOST: IC A−C ⊂ (−0.05, +0.05) | Equivalência A−C dentro de Δ=0.05 (secundária) |
| TOST: IC A−B ou B−C ⊂ Δ | Reportado com cautela (efeito verdadeiro observado > Δ) |

---

## 10. Configurações de Reprodutibilidade (Método — sem hashes/valores finais)

```yaml
seed_method: PCG64(seed_master)
seed_master:
  value: PENDING LOCK PROTOCOL      # a definir/aprovar pela governança antes do Lock
  type: uint64
derivation: |
  Para cada (bip, condicao), 3 seeds geradas deterministicamente a partir de
  seed_master via PCG64, em stream isolado por (bip, condicao).
  Total: 12 x 3 x 3 = 108 seeds (3 por célula).
seed_statistics:
  value: PENDING LOCK PROTOCOL      # stream isolado da análise estatística
  type: uint64
seed_power_simulation: { value: 20260814, type: uint64 }  # metodológica D-07
taxonomy_sha256:
  value: 5ba63db7a81c454d...        # corrigida (D-03 P5); a gravar por execução
  type: sha256
```

**Software:** Python 3.11+; `scipy.stats` (friedmanchisquare, wilcoxon), `numpy`, `pandas`,
`scikit-posthocs` (Holm); pipeline do GO-8D (embeddings corrigidos, ged_ref, entropy).

---

## 11. Compromissos Pré-Registrados

**Comprometido:** DV_confirm primária (pesos 1:1:1); Friedman df=2 α=0.05; Wilcoxon bilateral +
Holm; unidade BIP; N=12; 3 seeds/célula; mediana; **TOST com Δ=0.05**; Go/No-Go ≥ 10 de 12;
Kendall W, r_rb, Cliff δ; bootstrap B=10.000; IC exato da mediana ao lado; rastreabilidade de
taxonomia por execução; gates D-04/D-05 pré-Lock.

**Proibido:** winsorização; transformação da DV_confirm; modelo misto; tuning de parâmetros
pós-resultados; decisões unilaterais; correção de N por resultados; tratar simulações
metodológicas como observações; preencher hashes fora do Lock Protocol; **gerar seeds antes da
autorização; aplicar Lock antes da autorização**; alterar GO-8B/GO-8C.

---

## 12. Gate de Autorização

- **Este pré-registro foi aprovado pela governança (2026-08-14)** e entra no Lock GO-8D.
- **Seeds e hashes finais:** preenchidos **apenas sob Lock Protocol em etapa autorizada**.
- **Lock GO-8D:** etapa separada, somente após aprovação do pré-registro e autorização explícita.
- **Execução (108 reconstruções) e análise:** somente após o Lock GO-8D e autorização por etapa.

---

## 13. Diferenças em relação ao pré-registro do GO-8C

| Item | GO-8C (N=12) | GO-8D (esboço) |
|---|---|---|
| **Desfecho primário** | S_struct (WL anonimizado vs ECP fixo) | **DV_confirm = (conf + ged_ref + ent)/3** vs taxonomia da condição |
| **Referência da métrica** | Cadeia ECP fixa (9 nós) | **Taxonomia da condição** (T_PERM p/ A/C; DAG C3 p/ B) |
| **Embeddings CAT** | nome canônico ECP (cosseno 1.0 — degenerado) | **definições neutras PT** (corrigido, D-03 P2) |
| **Anonimização WL** | `"neutral"` (uniforme) | **não usada na DV** (componentes usam categorias reais) |
| **TOST / equivalência** | **NÃO vigente** (sem Δ) | **VIGENTE**: Δ=0.05 aprovado (D-06) |
| **Potência** | ≈ 0.895 (S1_PRIMARY do GO-8B) | **0.999** Friedman / 0.996 B−C / 0.919 TOST (D-07, cenário C) |
| **N** | 12 (D-04) | **12** (D-07 recálculo — mínimo 10; recomendado 12) |
| **Rastreabilidade de taxonomia** | ausente (lacuna BIP-007-B) | **`taxonomy_sha256` por execução** (P5/D-03) |
| **Gates de produção** | parseabilidade ausente (gap BIP-009) | **D-04 (parseabilidade) + D-05 (semântico híbrido)** pré-Lock |
| **Hipóteses de equivalência** | nenhuma | **A vs C dentro de Δ=0.05** (secundária) |

---

## 14. Status e Próximos Passos

- **Status:** **APROVADO** (2026-08-14). HASH STATUS: todos os artefatos e o próprio pré-registro
  permanecem **PENDING LOCK PROTOCOL** até a etapa de Lock em etapa autorizada.
- **Próxima parada:** **Lock GO-8D** (manifesto + hashes) em etapa autorizada pela governança.
- Após o Lock: autorização explícita de execução (108 reconstruções), depois validação (D-04/D-05),
  análise (plano §6), relatório e encerramento.

---

**Fim do pré-registro GO-8D (v1.0 APROVADO). Nenhum experimento executado. Nenhuma seed gerada.
Nenhum dado experimental coletado. Nenhum hash final gerado. Lock Protocol a ser aplicado em
etapa autorizada.
