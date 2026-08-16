# GO-8B Entregável 5 — Especificação do WL Kernel (Weisfeiler-Lehman Kernel)

**Status:** REVISED — PENDING GOVERNANCE AUDIT
**Revisão:** R1 (aplicação do Decision Record 00-GO-8B-R1) + R3 (R2-C3, R2-C6)
**Data original:** 2026-08-10
**Objetivo:** Definir a comparação entre o Grafo Reconhecido (G_rec, saída do GraphFromReconstruction, no espaço sintético da condição C2/C3) e o Grafo Canônico ECP (G_ecp) — **na fase de análise**, depois da reconstrução. A comparação tem dois componentes: **S_struct** (estrutural, topológico, sem semântica ECP) e **S_sem** (semântico, **exploratório/secundário**, com alinhamento contínuo).
**Entrada:** Dois grafos direcionados rotulados `(V, E, λ_V, λ_E, w_V, w_E)` com pesos de confiança.

---

## 1. Visão Geral

- **S_struct**: Similaridade topológica/estrutural (WL subtree kernel) — **não utiliza semântica ECP**.
- **S_sem**: Similaridade semântica contínua dos rótulos — **exploratória/secundária**, alinhamento contínuo (sem hard constraint).

**Métrica primária (confirmatória):** `S_struct ∈ [0, 1]`.  
**Métrica exploratória:** `S_sem`, e combinação `K = α · S_struct + (1 − α) · S_sem` (α pré-especificado; ver §6).

**Princípio (Correção R1):**
- S_struct mede **estrutura**, não aderência ao ECP.
- S_struct **não** utiliza: categorias ECP, leis ECP, mapeamentos ECP, embeddings ECP ou penalidades derivadas de ECP.
- S_sem permite **scores intermediários** entre categorias diferentes (ex.: `Goal ↔ Claim = 0.72`); similaridade zero **não** ocorre apenas porque os nomes diferem.
- Nenhuma lei ECP é usada como **penalidade estrutural**.

---

## 2. Representação dos Grafos

### 2.1 Grafo Reconhecido (G_rec) — Saída do GraphFromReconstruction

Espaço da condição (**CAT-XX** para C2=T_PERM; **SYN-XXX** para C3=T_SYNTH), conforme DECISION R3-01. `syn_category` como λ_V; `relation_type` como λ_E. Cardinalidade variável.

### 2.2 Grafo Canônico ECP (G_ecp) — Referência Fixa (usado somente na fase de análise)

**Justificativa do escopo de 9 nós (R2-C3):** G_ecp corresponde à cadeia canônica de dependências do ECP (Lei L-1, ECP-001 §3) **limitada aos nós que podem ser expressos como entidades de reconstrução**: `Problem → Goal → Claim → Knowledge → Assumption → Evidence → Decision → State → Artifact`. Os nós `Validation` e `Learning` (ECP-001 §3) representam **fases pós-artefato** (avaliação e aprendizado), que não constituem entidades codificáveis na reconstrução cega de um caso e, portanto, estão **fora do escopo do contraste testado** (condições A/B/C sobre reconstrução). Nenhum nó além desses 9 é tratado pela métrica; a justificativa fica registrada neste documento e no DISCOVERY-LOG.

```python
G_ecp = {
    "nodes": [
        {"id": "Problem", "label": "Problem", "weight": 1.0},
        {"id": "Goal", "label": "Goal", "weight": 1.0},
        {"id": "Claim", "label": "Claim", "weight": 1.0},
        {"id": "Knowledge", "label": "Knowledge", "weight": 1.0},
        {"id": "Assumption", "label": "Assumption", "weight": 1.0},
        {"id": "Evidence", "label": "Evidence", "weight": 1.0},
        {"id": "Decision", "label": "Decision", "weight": 1.0},
        {"id": "State", "label": "State", "weight": 1.0},
        {"id": "Artifact", "label": "Artifact", "weight": 1.0}
    ],
    "edges": [
        {"source": "Problem", "target": "Goal", "label": "precedes", "weight": 1.0},
        {"source": "Goal", "target": "Claim", "label": "precedes", "weight": 1.0},
        {"source": "Claim", "target": "Knowledge", "label": "precedes", "weight": 1.0},
        {"source": "Knowledge", "target": "Assumption", "label": "precedes", "weight": 1.0},
        {"source": "Assumption", "target": "Evidence", "label": "precedes", "weight": 1.0},
        {"source": "Evidence", "target": "Decision", "label": "precedes", "weight": 1.0},
        {"source": "Decision", "target": "State", "label": "precedes", "weight": 1.0},
        {"source": "State", "target": "Artifact", "label": "precedes", "weight": 1.0}
    ]
}
```

**Referência:** este grafo é a referência canônica ECP **apenas para a fase de análise comparativa**. HASH STATUS: PENDING LOCK PROTOCOL (nenhum hash congelado nesta etapa).

---

## 3. Componente Estrutural: S_struct (WL Subtree Kernel)

### 3.1 Algoritmo WL (h iterações) — com anonimização de rótulos

**Procedimento de anonimização (documentado, exigido pela R1):** para calcular S_struct, os rótulos originais **não** são utilizados como semântica. Cada nó recebe um **rótulo inicial uniforme e neutro** (todas as dimensões de rótulo removidas; `label_0(v) = "neutral"` para **todos** os nós). A semântica de λ_V/λ_E de **ambos** os grafos é descartada para S_struct. Isso garante que S_struct reflita **apenas topologia** (estrutura de grafo), nunca aderência a categorias ECP.

```
FUNCTION WL_Structural_Similarity(G1, G2, h=3):
  # G1, G2: grafos com node labels; rótulos ANONIMIZADOS antes do WL

  0. ANONIMIZAÇÃO
     - Para cada nó v em G1 ∪ G2: label_0(v) = "neutral"   # uniforme; semântica removida
     - Registro: procedimento de anonimização aplicado simetricamente em ambos os grafos

  1. ITERAÇÕES WL (i = 1..h)
     PARA cada grafo G EM [G1, G2]:
       PARA cada nó v EM G:
         - Coletar multiset de labels dos vizinhos:
           M(v) = { (label_{i-1}(u), tipo_unitário) para u ∈ InNeighbors(v) } ∪
                  { (label_{i-1}(w), tipo_unitário) para w ∈ OutNeighbors(v) }
           # tipo_unitário: direção (in/out) sem semântica de relação
         - Novo label: label_i(v) = Hash( label_{i-1}(v) + sorted(M(v)) )
         # Hash determinístico (SHA-256 truncado 64 bits)

  2. CONTAGEM DE SUBÁRVORES
     - Para cada grafo, contar frequência de cada label_i único (i=0..h)
     - Vetor de contagem φ(G) = concatenação de histogramas por iteração

  3. KERNEL (produto interno normalizado)
     S_struct = <φ(G1), φ(G2)> / (||φ(G1)|| · ||φ(G2)||)

  RETORNO S_struct ∈ [0, 1]
```

**Propriedades R1:**
- S_struct mede **estrutura topológica**, não aderência ao ECP.
- Não utiliza categorias ECP, leis ECP, mapeamentos ECP, embeddings ECP ou penalidades derivadas de ECP.
- O resultado representa **estrutura**, não conformidade com ECP.

### 3.2 Parâmetros (Pré-especificados — ver §6)

| Parâmetro | Valor |
|---|---|
| `h` (iterações WL) | 3 |
| `Hash` | SHA-256 truncado 64 bits |
| Normalização | Cosseno (L2) |
| Anonimização de rótulos | Uniforme (`"neutral"`) em ambos os grafos |

---

## 4. Componente Semântico: S_sem (Exploratório, Alinhamento Contínuo)

**Status:** **SECUNDÁRIO / EXPLORATÓRIO** — não é critério confirmatório. Álcool de diagnóstico para interpretar resultados.

### 4.1 Embeddings de Rótulos (Modelo Neutro, Congelado)

Vetores normalizados L2, derivados de um modelo de linguagem **neutro** (`sentence-transformers/all-MiniLM-L6-v2`, versão congelada) aplicado aos **rótulos textuais neutros das categorias da condição** (taxonomia C2=T_PERM ou C3=T_SYNTH) e aos **nomes de categorias ECP**. **Não** se usam leis ECP como penalidade. O namespace é local à condição: os embeddings consultam a taxonomia da condição que produziu `G_rec`.

- `emb_synth(label)` — embedding do rótulo textual neutro da categoria da condição (definido na taxonomia C2 ou C3, conforme o namespace de `G_rec`).
- `emb_ECP(ecp_label)` — embedding do nome da categoria ECP (Problem, Goal, ...).

**HASH STATUS: PENDING LOCK PROTOCOL** para o arquivo de embeddings `EMBEDDINGS.npy`.

### 4.2 Cálculo de S_sem — Alinhamento Contínuo (sem hard constraint)

```
FUNCTION Semantic_Similarity(G_rec, G_ecp):
  1. NODE SIMILARITY MATRIX (CONTÍNUA)
     Para cada nó v1 ∈ G_rec, v2 ∈ G_ecp:
       S_V(v1, v2) = cos_sim(emb_synth(λ_V(v1)), emb_ECP(λ_V(v2))) ∈ [-1, 1]
       # Normalizado para [0, 1]: (S_V + 1) / 2
       # SEM hard constraint: categorias diferentes PODEM receber scores intermediários.
       # Ex.: Goal ↔ Claim = 0.72 é válido; 0 não ocorre apenas por nomes diferirem.

  2. EDGE SIMILARITY MATRIX (CONTÍNUA)
     Para cada aresta e1 ∈ G_rec, e2 ∈ G_ecp:
       S_E(e1, e2) = cos_sim(emb(λ_E(e1)), emb(λ_E(e2))), normalizado (S_E + 1) / 2

  3. ALINHAMENTO ÓTIMO (Hungarian Algorithm)
     - Construir matriz de similaridade contínua (acima).
     - PERMITIR matching entre categorias DIFERENTES (sem restrição de igualdade de rótulo).
     - PERMITIR scores intermediários.
     - Calcular matching ótimo que MAXIMIZA a soma das similaridades.
     - Algoritmo registrado: Hungarian/Kuhn-Munkres (atribuição linear, custo = −similaridade).
     - Nenhuma lei ECP usada como penalidade estrutural.

  4. SCORE FINAL
     S_sem = (w_V · mean(matched_node_sims) + w_E · mean(matched_edge_sims)) / (w_V + w_E)
     Pesos pré-especificados: w_V = 1.0, w_E = 0.5

  RETORNO S_sem ∈ [0, 1]
```

**Exemplo de aplicação (conceitual):** se `Goal` e `Claim` têm alta similaridade semântica no embedding, o matching pode pareá-los com score > 0 — permitido e esperado.

**Limitação registrada (R2-C6):** o componente de arestas de S_sem aplica `cos_sim` sobre embeddings de `relation_type`, que é um campo **livre** (não enumerado) na reconstrução (ver DEBT-GFR-03, Entregável 4). Como a semântica de `relation_type` é definida apenas na análise, esse termo tem interpretação **mal definida** e contribuição limitada ao score. Por isso a ponderação pré-especificada dá peso **reduzido** a arestas (`w_E = 0.5 < w_V = 1.0`), e o impacto é reportado apenas como diagnóstico. **Esta limitação não se aplica a S_struct**, que não utiliza `relation_type` (anonimização). S_sem permanece **secundária/exploratória** e não constitui métrica primária.

---

## 5. Legitimidade da Comparação com ECP (somente na Análise)

- Esta comparação ocorre **somente na fase de análise**, depois da reconstrução, para grafos vindos de qualquer condição (C2=T_PERM ou C3=T_SYNTH), cada um no seu namespace.
- **Nunca** como restrição de geração e **não** por mapeamento pré-definido SYN→ECP.
- Não há tabela fixa "SYN-XXX → ECP"; o alinhamento é **contínuo e semântico**.

---

## 6. Parâmetros do WL (Registro Completo — Correção 5)

Para cada parâmetro: valor, finalidade, justificativa metodológica, tipo (estrutural/semântico), e se pode ser alterado após a coleta. **Nenhum parâmetro poderá ser otimizado após observar resultados. Não há tuning.**

| Parâmetro | Valor | Finalidade | Justificativa metodológica | Tipo | Pode alterar pós-coleta? |
|---|---|---|---|---|---|
| `h` | 3 | Profundidade de iteração do WL | Pré-especificado; vizinhança de 3 saltos captura estrutura local relevante | Estrutural | **NÃO** |
| `Hash` (WL) | SHA-256 truncado 64 bits | Rótulo determinístico de subárvore | Determinístico, colisões improváveis | Estrutural (técnica) | **NÃO** |
| Normalização | Cosseno (L2) | Escala invariante | Independente da escala de contagens | Estrutural (técnica) | **NÃO** |
| Anonimização S_struct | Rótulo uniforme `"neutral"` | Remover semântica para medir topologia | Exigência R1: S_struct não usa semântica ECP | Estrutural | **NÃO** |
| `α` | 0.6 | Peso de S_struct na combinação K | Favorece estrutura; pré-especificado, não otimizado | Misto | **NÃO** |
| `w_V` | 1.0 | Peso de nós em S_sem | Rótulos de nós mais informativos que arestas | Semântico | **NÃO** |
| `w_E` | 0.5 | Peso de arestas em S_sem | Pré-especificado, não otimizado | Semântico | **NÃO** |
| Modelo de embeddings | all-MiniLM-L6-v2 (congelado) | Alinhamento semântico contínuo | Modelo neutro, versão fixa; aplicado a rótulos da condição (C2/C3) e ECP | Semântico | **NÃO** |
| Status S_sem | Exploratório/secundário | Diagnóstico interpretativo | Não confirmatório; não decide hipótese | Semântico | **NÃO** |

Regra: todas as alterações de parâmetro (mesmo que aprovadas) constituem nova versão do protocolo; **nenhuma** decisão sobre os valores pode basear-se em resultados observados.

---

## 7. Testes de Sanidade (Planejados)

| Teste ID | Descrição | Entrada | Critério Pass |
|---|---|---|---|
| **T-WL-01** | Identidade: G vs G | Mesmo grafo, 2x | S_struct = 1.0 (±1e-10) |
| **T-WL-02** | Grafo vazio vs G_ecp | Grafo vazio, G_ecp | S_struct = 0.0 (ou sem subárvores) |
| **T-WL-03** | Subgrafo encadeado | 3 nós encadeados vs G_ecp | S_struct > 0 (estrutura parcial preservada) |
| **T-WL-04** | Nó único | 1 nó vs G_ecp | S_struct baixo; S_sem reflete apenas similaridade semântica |
| **T-WL-05** | Topologia ≠ rótulos | Dois grafos mesma topologia, rótulos distintos | S_struct ≈ 1.0 (anonimização) ; S_sem < 1.0 |
| **T-WL-06** | Determinismo | Mesma entrada 2x | Scores idênticos (bitwise) |
| **T-WL-07** | Simetria | K(A,B) vs K(B,A) | Valores idênticos |
| **T-WL-08** | Aresta ausente (Evidence→Decision) | G_ecp sem respectiva aresta | S_struct < 1.0 (estrutura alterada) |
| **T-WL-09** | Pesos de confiança afetam score | G com weights 0.5 vs 1.0 | Scores diferentes (ponderação funciona) |
| **T-WL-10** | Semântica contínua | Rótulos Goal/Claim com embeddings | Similaridade contínua > 0 (sem hard constraint) |
| **T-WL-11** | Semântica distante | Labels com embeds distantes | Similaridade menor, mas NUNCA 0 só por nome diferente |
| **T-WL-12** | Sem frozen hash | Leitura de metadados | `HASH STATUS: PENDING LOCK PROTOCOL` |

---

## 8. Dívida Metodológica Conhecida

| Item | Descrição | Mitigação GO-8B |
|---|---|---|
| **DEBT-WL-01** | S_sem usa embeddings de nomes ECP na fase de análise — risco de circularidade é restrito à análise, não à geração | S_sem é exploratório; S_struct é primário e semântica-neutra; registrado no DISCOVERY-LOG |
| **DEBT-WL-02** | α = 0.6 arbitrário (não otimizado) | Pré-especificado; proibido tuning; sensibilidade registrada no DISCOVERY-LOG |
| **DEBT-WL-03** | WL kernel não captura isomorfismo exato (apenas aproximado) | Anonimização + h=3 definidos; limitação registrada |
| **DEBT-WL-04** | Alinhamento contínuo pode parear categorias conceitualmente distintas | S_sem exploratório; interpretação qualitativa; registro de matches plenos |
| **DEBT-WL-05** | `relation_type` livre (não enumerado) tem semântica mal definida no cos_sim de arestas de S_sem (R2-C6) | `w_E = 0.5 < w_V = 1.0`; impacto reportado só como diagnóstico; S_sem permanece secundária/exploratória; S_struct não afetado |

---

## GO-8B CHANGE LOG

### GO-8B-R1 (aplicado)
- Decision Record: 00-GO-8B-R1-DECISION-RECORD.md
- Revisão: R1
- Alterações principais:
  - **S_struct**: definido como estrutura topológica **sem semântica ECP**; rótulos anonimizados (uniforme `"neutral"`) em ambos os grafos; remoção de dependência de categorias/leis/embeddings/mapeamentos ECP e de penalidades derivadas de ECP.
  - **S_sem**: demovido a **exploratório/secundário**; eliminado o hard constraint "categoria diferente → similaridade 0"; alinhamento contínuo via Hungarian (matriz contínua, matching entre categorias diferentes, scores intermediários); algoritmo registrado; sem leis ECP como penalidade.
  - **Parâmetros do WL**: registrados em tabela (valor, finalidade, justificativa, tipo, alterável pós-coleta); **proibido otimizar/tuning** após observar resultados.
  - **Matriz de compatibilidade baseada em ECP removida** (penalidade estrutural derivada de ECP eliminada).
  - Comparação C3↔ECP restrita à fase de análise (sem mapeamento pré-definido SYN→ECP).
  - Afirmações de hash congelado substituídas por `HASH STATUS: PENDING LOCK PROTOCOL`.
- Alterações metodológicas:
  - Métrica confirmatória passa a ser S_struct; S_sem é diagnóstico.
  - S_sem permite pareamento Goal↔Claim = 0.72 (exemplo) — nunca 0 por rótulos diferentes.
- Itens ainda pendentes:
  - Implementação e testes de sanidade T-WL-01..12.
  - Registro/Freeze de embeddings e grafos no Lock Protocol.

### GO-8B-R3 (aplicado — R2-C3, R2-C6)
- **R2-C3:** justificado formalmente o escopo de 9 nós de G_ecp (§2.2) — os nós `Validation`/`Learning` são fases pós-artefato fora do escopo da reconstrução; justificativa registrada.
- **R2-C6:** documentada a limitação do `relation_type` livre no componente de arestas de S_sem (§4.2 e DEBT-WL-05); S_sem permanece secundária/exploratória, sem virar métrica primária.
- Alinhada a terminologia de espaços de grafos à DECISION R3-01 (C2/C3).
- `emb_C3` generalizado para `emb_synth` (§4.1), consultando a taxonomia da condição (C2 ou C3) conforme o namespace de `G_rec`.
- §5 renomeado para "Legitimidade da Comparação com ECP" — comparação na fase de análise para grafos de qualquer condição, cada um no seu namespace.
- Status: REVISED — PENDING GOVERNANCE AUDIT
