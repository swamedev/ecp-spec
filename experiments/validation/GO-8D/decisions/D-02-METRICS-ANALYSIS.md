# D-02 — Análise de Métricas Alternativas à S_struct

**Data:** 2026-08-14
**Ciclo:** GO-8D — DIAGNOSTIC PHASE
**Tipo:** relatório de diagnóstico (métricas candidatas para DV confirmatória)
**Base:** `experiments/validation/GO-8C/decisions/D-01-SSTRUCT-AUDIT.md`
**Artefatos de suporte:** `experiments/validation/GO-8D/analysis/metrics_candidates.py` (diagnóstico reproduzível) · `experiments/validation/GO-8D/analysis/metrics_cells.json` (36 células)

---

## 1. Objetivo

Avaliar métricas candidatas para **substituir ou corrigir** a `S_struct` como variável dependente
confirmatória, incorporando os achados da auditoria D-01 (anonimização uniforme, confundimento
por contagem de nós, topologia dominada pelo parser, seeds vestigiais). **Fase de diagnóstico:
sem novo experimento, sem coleta de dados, sem alteração do pipeline congelado.**

## 2. Método

1. **Reconstrução das 36 células do N=12** (12 BIPs × A/B/C) a partir de `GO-8C/study-input`,
   usando as funções do engine congelado (`pilot_engine.py`, `wl_kernel.py`,
   `graph_from_reconstruction.py`) sem modificação. Para a condição B foi injetada a taxonomia
   **corrigida** (GO-8C, D-03.7), como feito no estudo.
2. **Validação da reconstrução:** `S_struct` (M0) reproduz **36/36 células** do
   `pilot_results_n12.csv` exatamente (bit a bit, `mismatch=0`). Isto também corrige a conclusão
   da D-01 sobre o BIP-007-B (ver Anexo).
3. **Métricas computadas por célula** (1 valor determinístico por célula — as 3 seeds são
   bit-idênticas, ver D-01 §E4):
   - **M0 — S_struct atual** (referência da auditoria; kernel WL anonimizado vs cadeia ECP).
   - **M1 — S_struct corrigida:** `M0 − S_base(n)`, removendo o confundimento mecânico de
     contagem de nós (D-01 §3).
   - **M2 — Kernel WL rotulado (mesmo namespace):** WL (h=3) com rótulos de categoria, comparado
     à **taxonomia da própria condição** (cadeia T_PERM/CAT para A/C; DAG C3 para B), em vez da
     cadeia ECP.
   - **M3 — GED ponderada (embeddings + edição):** distância de edição de grafo entre a
     reconstrução e o grafo ECP; substituição de nós via cosseno de embeddings de rótulo
     (tabela `EMBEDDINGS.npy`, Hungarian), arestas dirigidas com custo 0.5; normalizada em [0,1].
   - **M4 — S_sem refinada (Hungarian com embeddings de rótulo):** fórmula atual de S_sem, mas com
     `label_emb(syn_category)` como vetor de nó (em vez de média de conteúdo) — a direção
     recomendada pela D-01 §7.
   - **M5 — Fidelidade por fato (confiança de atribuição):** confiança média do classificador por
     fato atribuído a um slot da taxonomia.
   - **M6 — Entropia de atribuição (Shannon normalizada):** quão espalhados os fatos ficam entre
     os slots; normalizada por log(nº de slots do namespace) — 9 para A/C, 12 para B.
4. **Critérios de avaliação** (por condição, 12 células): nº de valores distintos (degenerescência),
   mediana, amplitude, correlação com nº de nós, e separação A/B/C por **Friedman** (emparelhado
   por BIP).

## 3. Resultados

### 3.1 Tabela resumo por condição (12 células cada)

| Métrica | Cond | Mediana | Valores distintos/12 | Min | Max | Amplitude |
|---|---|---|---|---|---|---|
| **M0 S_struct** | A | 0.5875 | **5/12** | 0.5721 | 0.6828 | 0.1107 |
| | B | 0.6348 | 9/12 | 0.5785 | 0.7081 | 0.1296 |
| | C | 0.5843 | 8/12 | 0.5539 | 0.6277 | 0.0738 |
| **M1 S_struct corr** | A | 0.0254 | **5/12** | -0.0000 | 0.0953 | 0.0953 |
| | B | 0.0427 | 9/12 | -0.0911 | 0.1938 | 0.2849 |
| | C | 0.1134 | 8/12 | -0.0054 | 0.3068 | 0.3122 |
| **M2 WL rotulado** | A | 0.2500 | **2/12** | 0.2357 | 0.2500 | 0.0143 |
| | B | 0.2162 | 3/12 | 0.2041 | 0.2394 | 0.0353 |
| | C | 0.2357 | 5/12 | 0.1863 | 0.2500 | 0.0637 |
| **M3 GED** | A | 0.4722 | **12/12** | 0.4035 | 0.5647 | 0.1612 |
| | B | 0.3060 | **12/12** | 0.2371 | 0.3821 | 0.1450 |
| | C | 0.4949 | 11/12 | 0.4231 | 0.5429 | 0.1198 |
| **M4 S_sem refinada** | A | 0.8333 | **1/12** | 0.8333 | 0.8333 | 0.0000 |
| | B | 0.5429 | 11/12 | 0.5415 | 0.5462 | 0.0047 |
| | C | 0.8333 | **1/12** | 0.8333 | 0.8333 | 0.0000 |
| **M5 Fidelidade** | A | 0.7343 | 12/12 | 0.7150 | 0.7493 | 0.0343 |
| | B | 0.7369 | 12/12 | 0.7143 | 0.7451 | 0.0308 |
| | C | 0.7222 | 12/12 | 0.7069 | 0.7441 | 0.0372 |
| **M6 Entropia** | A | 0.9089 | 12/12 | 0.8483 | 0.9781 | 0.1298 |
| | B | 0.7289 | 12/12 | 0.5885 | 0.7991 | 0.2106 |
| | C | 0.8004 | 12/12 | 0.6419 | 0.9234 | 0.2815 |

### 3.2 Separabilidade e confundimento

| Métrica | Friedman Q (A/B/C, df=2) | Corr. com nº de nós (36 células) |
|---|---|---|
| M0 S_struct | 9.50 | +0.346 |
| **M1 S_struct corr** | **5.17 (n.s.)** | **−0.897** |
| M2 WL rotulado | 10.67 | +0.594 |
| **M3 GED** | **18.00** | −0.338 |
| M4 S_sem refinada | 24.00 | −0.388 |
| M5 Fidelidade | 15.50 | +0.317 |
| M6 Entropia | 16.67 | +0.215 |

(Q crítica χ²(2, α=0.05)=5.99; Q≥5.99 ⇒ p<0.05. M1: 5.17 ⇒ **não significativo**.)

## 4. Leitura dos resultados

1. **M0 confirma a D-01:** condição A tem 5/12 valores distintos (plató 0.5875) e o teste de
   separação reproduz o achado do GO-8C (Q=9.50 vs χ²=9.78 do estudo).
2. **M1 é o resultado mais importante:** removido o confundimento de contagem de nós, a
   separação A/B/C **deixa de ser significativa (Q=5.17, p>0.05)**. Ou seja, o efeito estatístico
   do GO-8C (Friedman p=0.0075; B>C pós-Holm) é **majoritariamente um artefato mecânico da
   granularidade da taxonomia** (mais slots ⇒ mais nós ⇒ S_base maior). Além disso, M1 fica
   fortemente correlacionado **negativamente** com o nº de nós (−0.897): a correção linear
   simples sobre-corrige. **Nenhuma inferência confirmatória do GO-8C sobrevive à correção do
   confundimento.**
3. **M2 (WL rotulado intra-namespace) degenera** (A=2/12, B=3/12 valores distintos): os grafos
   reconstruídos são esparsos (poucos slots usados), produzindo histogramas WL quase idênticos
   contra a taxonomia de referência, com valores baixos (~0.19–0.25) e domínio do componente
   neutro. Não serve como DV.
4. **M3 (GED ponderada) é a melhor candidata técnica:** discriminação quase perfeita
   (12/12, 12/12, 11/12 valores distintos), separação A/B/C significativa (Q=18.00), correlação
   baixa com nº de nós (−0.338). **Mas** sua comparabilidade entre condições é limitada: para
   A/C os rótulos CAT correspondem a nomes canônicos ECP (substituição ≈ identidade), enquanto
   para B os rótulos SYN são definições distantes do ECP — a leitura é "B está estruturalmente
   mais distante da cadeia ECP", não um aumento de fidelidade. Serviria como **diagnóstico
   intra-namespace ou como covariável**, não como DV confirmatória transversal.
5. **M4 (S_sem refinada) está degenerada por construção:** A e C têm **1 único valor (0.8333)
   para as 12 células**. Causa: na tabela `EMBEDDINGS.npy`, os vetores CAT são os **nomes
   canônicos ECP** (`p4_generate_embeddings.py`: `texts[("CAT",cat)] = canon_name`), de modo que
   cada nó CAT casa com o seu slot ECP com cosseno 1.0 — o termo de nós satura e a métrica
   não vê conteúdo. Para B, o range é 0.0047 (constante). **A direção "refinar S_sem com
   embeddings de rótulo" é inviável com a tabela atual** e exigiria embeddings CAT baseados nas
   definições neutras (dívida de pipeline a tratar em D-03/D-05).
6. **M5 e M6 são diagnósticos úteis, não DVs:** ambos discriminam 12/12 células (nenhuma
   degenerescência) e separam condições, mas não medem fidelidade estrutural ao ECP. M5
   (confiança média ≈ 0.72–0.74) e M6 (entropia de atribuição) descrevem **como os fatos se
   distribuem na taxonomia** — bons para caracterizar amostras, não para testar a hipótese.

## 5. Recomendação

**Nenhuma métrica candidata, nas condições atuais do pipeline, é uma DV confirmatória válida.**

| Critério | M0 | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|---|
| Não degenerada (valores distintos) | ✖ | ✖ | ✖ | ✅ | ✖ | ✅ | ✅ |
| Sem confundimento de nº de nós | ✖ | ✖ (sobre-corrige) | ✖ | ✅ | ✅ | ✅ | ✅ |
| Mede fidelidade ao ECP/taxonomia | ✖ | ✖ | ✖ | ~ | ✖ | ✖ | ✖ |
| Comparável entre namespaces | ~ | ~ | ✅ (intra) | ✖ | ✖ | ✅ | ~ |
| Interpretável/auditável | ~ | ✅ | ✅ | ✅ | ~ | ✅ | ✅ |

**Conclusão:**
- A D-01 é **confirmada e ampliada**: a S_struct não é apenas degenerada — **o sinal estatístico
  do estudo GO-8C desaparece quando se controla o confundimento de contagem de nós (M1)**.
- **Não existe métrica pronta para reutilização** no engine congelado: M3 (GED) é a única
  candidata tecnicamente sólida, mas como diagnóstico, não como DV transversal.
- **A correção da DV exige reprojeto do pipeline** (D-03/D-05): (a) desanonimizar o WL usando
  rótulos de categoria; (b) corrigir a tabela de embeddings CAT (definições neutras, não nomes
  canônicos); (c) padronizar a granularidade da taxonomia ou normalizar corretamente por
  contagem de nós; (d) referenciar a taxonomia da condição (DAG C3 / T_PERM), não a cadeia ECP.
- Enquanto isso, os resultados inferenciais do GO-8C devem ser reclassificados como
  **exploratórios** sobre a métrica, não confirmatórios sobre fidelidade estrutural.

## 6. Anexo — Correção do BIP-007-B na D-01

A auditoria D-01 concluíra que o CSV BIP-007-B (9 nós/78 arestas/0.5875) correspondia à taxonomia
**congelada** e que havia "inconsistência interna de execução" no GO-8C. **Reexame direto do CSV**
`pilot_results_n12.csv` mostra BIP-007-B = **10 nós/84 arestas/0.5950**, que é exatamente o
resultado da taxonomia **corrigida** (D-03.7). Com a injeção da corrigida em **todas** as células
B (incluindo BIP-007), a reconstrução reproduz **36/36 células** bit a bit.

**Conclusão corrigida:** o N=12 usou a taxonomia corrigida de forma **uniforme** na condição B;
não há inconsistência entre células. A lacuna real é de **rastreabilidade** (o engine congelado
não registra qual taxonomia usou). O relatório D-01 foi atualizado em 2026-08-14 para refletir
isto (§1, §4-E5, §5, §7).

## 7. Confirmação de integridade

- **Nenhum artefato congelado foi alterado.** GO-8B (CLOSED/LOCKED/FROZEN) e GO-8C (CLOSED,
  Lock de 151 artefatos, validado PASS) permanecem intactos (verificado por `git status`).
- Arquivos criados: `GO-8D/analysis/metrics_candidates.py` (diagnóstico), `metrics_cells.json`
  (dados), este relatório.
- Único arquivo do GO-8C tocado: `decisions/D-01-SSTRUCT-AUDIT.md` — **correção factual da
  conclusão sobre o BIP-007-B** (não é artefato do Lock; documento de diagnóstico do GO-8D).
- Reprodução executada com os módulos congelados importados por leitura; nenhuma escrita no
  pipeline.

---

**Fim do relatório D-02. 2026-08-14.**
