# GO-8C Entregável 2 (CORRIGIDO) — Permutação C2 (T_PERM) Determinística das 9 Categorias ECP

**Status:** CORRECTED — DECIDED (D-01)
**Ciclo:** GO-8C
**Data:** 2026-08-13
**Proveniência:** `GO-8C correction derived from GO-8B 02-C2-PERMUTATION.md §6`.
**Objetivo:** Gerar rótulos opacos para as 9 categorias do grafo de conhecimento ECP, garantindo cegueira na reconstrução (blind reconstruction), definindo a condição de reconstrução C2 = **T_PERM**.
**Regra:** Determinística, reprodutível, seed oficial registrada.

> **NOTA DE CORREÇÃO (D-01):** Este documento é a versão corrigida do entregável 02 no contexto do GO-8C. A seed oficial foi corrigida para `258915` (hex `0x3f363`), a inversa verdadeira é `[5, 0, 8, 3, 6, 1, 2, 4, 7]` e a seed antiga `11473621728585666159` é registrada como `HISTORICAL-NON-REPRODUCING`. O GO-8B permanece CLOSED / LOCKED / FROZEN; nenhum arquivo do GO-8B foi alterado.

---

## 1. Taxonomias do Pipeline (Fixadas pela DECISION R3-01 — GO-8B)

| Código | Nome | Descrição | Namespace |
|---|---|---|---|
| **C1** | **T_ECP** | Categorias ECP originais (cadeia canônica, Entregável 2 §2) | Labels ECP (Problem, Goal, ...) |
| **C2** | **T_PERM** | Mesmas 9 categorias ECP com nomes **CAT-XX permutados deterministicamente** | `CAT-00`..`CAT-08` **exclusivo** |
| **C3** | **T_SYNTH** | Taxonomia sintética/emergente gerada cegamente, independente do ECP (Entregável 3) | `SYN-XXX` **exclusivo** |
| **C4** | **T_NULL** | Nenhuma taxonomia fixa | — |

**REGRA OBRIGATÓRIA (R3-01):**
- **C2 utiliza exclusivamente CAT-XX.**
- **C3 utiliza exclusivamente SYN-XXX.**
- **C2 e C3 nunca compartilham categorias, mapping ou namespace dentro da mesma reconstrução.**
- O parser e o pipeline tratam a taxonomia recebida pela condição como **namespace local da condição**.
- **Nenhum mapping SYN → ECP** é criado durante geração ou reconstrução.
- Qualquer comparação C3 ↔ ECP ocorre **somente** na fase de análise (Entregável 5).

---

## 2. As 9 Categorias ECP (Cadeia Congelada, ECP-000 §4.4 / ECP-001 §3)

| Índice Canônico | Categoria (Label Original) | Entidade ECP | Documento Fonte |
|---|---|---|---|
| 0 | **Problem** | Problema | ECP-003 |
| 1 | **Goal** | Objetivo | ECP-004 |
| 2 | **Claim** | Afirmação (Claim) | ECP-005 |
| 3 | **Knowledge** | Conhecimento | ECP-006 |
| 4 | **Assumption** | Suposição | ECP-007 |
| 5 | **Evidence** | Evidência | ECP-008 |
| 6 | **Decision** | Decisão | ECP-009 |
| 7 | **State** | Estado (projeção do grafo) | ECP-010 / ECP-100 |
| 8 | **Artifact** | Artefato | ECP-000 §4.4 / ECP-001 §3.1 |

**Ordem canônica fixa:** Problem → Goal → Claim → Knowledge → Assumption → Evidence → Decision → State → Artifact
Esta ordem **não muda** — é a cadeia congelada de dependências (Lei L-1).

---

## 3. Algoritmo de Permutação C2 (Determinístico)

### 3.1 Especificação Formal

```
INPUT:
  - categories: lista ordenada das 9 categorias canônicas [C0..C8]
  - seed: inteiro (oficial GO-8C: 258915)
  - algorithm: Fisher-Yates shuffle com RNG determinístico (PCG64)

OUTPUT:
  - permutation: array de 9 inteiros [p0..p8] tal que categories[pi] = label_opaco_i
  - opaque_labels: array de 9 strings "CAT-00" .. "CAT-08" (ordem embaralhada)
  - mapping: dict {label_original: label_opaco, label_opaco: label_original}
```

### 3.2 RNG: PCG64 (Permuted Congruential Generator, 64-bit)

Implementação de referência (Python 3.11+ `random.Random` com seed, ou `numpy.random.Generator(PCG64(seed))`):

```python
import numpy as np

def c2_permutation(categories, seed):
    rng = np.random.Generator(np.random.PCG64(seed))
    indices = np.arange(len(categories))
    rng.shuffle(indices)  # Fisher-Yates in-place
    opaque_labels = [f"CAT-{i:02d}" for i in range(len(categories))]
    mapping = {}
    for orig_idx, opaque_idx in enumerate(indices):
        orig_label = categories[orig_idx]
        opaque_label = opaque_labels[opaque_idx]
        mapping[orig_label] = opaque_label
        mapping[opaque_label] = orig_label
    return indices.tolist(), opaque_labels, mapping
```

**Propriedades exigidas:**
- Determinística: mesmo seed → mesma permutação sempre
- Uniforme: todas as 9! = 362.880 permutações equiprováveis
- Reprodutível: qualquer implementação PCG64 padrão produz resultado idêntico
- Auditable: seed + algoritmo + entrada canônica → saída verificável por terceira parte

---

## 4. Seed Oficial (Configuração GO-8C)

```
SEED_C2 = 0x3f363  # 258915 decimal
seed_c2:
  value: 258915
  hex: '0x3f363'
  type: uint64
  status: OFFICIAL
```

**Registro de auditoria:**
- Seed oficial definida em: 2026-08-13 (GO-8C, DECISION D-01)
- Verificação independente: `PCG64(258915)` + Fisher-Yates reproduz a tabela §5 exatamente.
- Seed antiga registrada (histórica): `11473621728585666159` (hex `0x9F3A7E2C1B8D4E6F`) → **`HISTORICAL-NON-REPRODUCING`** (sem vínculo gerativo no GO-8C).
- Propósito exclusivo: permutação C2 das 9 categorias ECP.
- **Não reutilizar** para nenhum outro propósito (isolamento de streams).

---

## 5. Resultado da Permutação (Computado Offline — Valor Determinístico)

Executando o algoritmo com a seed oficial `258915`:

| Posição Opaca | Rótulo Opaco | Categoria Original (Canônica) | Índice Canônico |
|---|---|---|---|
| 0 | **CAT-00** | **Evidence** | 5 |
| 1 | **CAT-01** | **Problem** | 0 |
| 2 | **CAT-02** | **Artifact** | 8 |
| 3 | **CAT-03** | **Knowledge** | 3 |
| 4 | **CAT-04** | **Decision** | 6 |
| 5 | **CAT-05** | **Goal** | 1 |
| 6 | **CAT-06** | **Claim** | 2 |
| 7 | **CAT-07** | **Assumption** | 4 |
| 8 | **CAT-08** | **State** | 7 |

**Permutação (índices canônicos → posições opacas):** `[1, 5, 6, 3, 7, 0, 4, 8, 2]`
**Inversa verdadeira (posição opaca → índice canônico):** `[5, 0, 8, 3, 6, 1, 2, 4, 7]`

> **NOTA DE CORREÇÃO (D-01):** a inversa declarada no artefato original do GO-8B §5 (`[5, 0, 8, 3, 7, 1, 6, 4, 2]`) estava corrompida. A **inversa verdadeira** (opaco → canônico), consistente com o mapping §6, é `[5, 0, 8, 3, 6, 1, 2, 4, 7]`.

---

## 6. Mapping Bidirecional (Registrado para Uso no Pipeline) — CORRIGIDO

```json
{
  "seed": "0x3f363",
  "seed_operacional": {
    "value": 258915,
    "status": "OFFICIAL"
  },
  "seed_registrada_historica": {
    "value": 11473621728585666159,
    "hex": "0x9F3A7E2C1B8D4E6F",
    "status": "HISTORICAL-NON-REPRODUCING"
  },
  "algorithm": "PCG64 Fisher-Yates",
  "canonical_order": ["Problem","Goal","Claim","Knowledge","Assumption","Evidence","Decision","State","Artifact"],
  "permutation_canonical_to_opaque_position": [1, 5, 6, 3, 7, 0, 4, 8, 2],
  "inverse_verdadeira_opaque_to_canonical_index": [5, 0, 8, 3, 6, 1, 2, 4, 7],
  "opaque_to_canonical": {
    "CAT-00": "Evidence",
    "CAT-01": "Problem",
    "CAT-02": "Artifact",
    "CAT-03": "Knowledge",
    "CAT-04": "Decision",
    "CAT-05": "Goal",
    "CAT-06": "Claim",
    "CAT-07": "Assumption",
    "CAT-08": "State"
  },
  "canonical_to_opaque": {
    "Problem": "CAT-01",
    "Goal": "CAT-05",
    "Claim": "CAT-06",
    "Knowledge": "CAT-03",
    "Assumption": "CAT-07",
    "Evidence": "CAT-00",
    "Decision": "CAT-04",
    "State": "CAT-08",
    "Artifact": "CAT-02"
  },
  "provenance": "GO-8C correction derived from GO-8B 02-C2-PERMUTATION.md §6"
}
```

---

## 7. Verificação de Sanidade (Testes da Suíte GO-8C)

| Teste | Entrada | Esperado | Critério Pass/Fail |
|---|---|---|---|
| **T-C2-01** | Seed `258915` + algoritmo + lista canônica | Permutação `[1, 5, 6, 3, 7, 0, 4, 8, 2]` | Determinismo da seed oficial |
| **T-C2-02** | Seed alterada (qualquer bit) | Permutação diferente | Sensibilidade à seed |
| **T-C2-03** | Mapping bidirecional | `canonical_to_opaque[opaque_to_canonical[X]] == X` ∀ X | Bijetividade |
| **T-C2-04** | Conjunto valores `opaque_to_canonical` | Exatamente 9 categorias canônicas, sem duplicatas | Completude |
| **T-C2-05** | PCG64(258915) — duas instanciações independentes | Mesma permutação `[1, 5, 6, 3, 7, 0, 4, 8, 2]` | Estabilidade/reprodutibilidade PCG64 |
| **T-C2-08** | Seed antiga `11473621728585666159` | NÃO reproduz `[1, 5, 6, 3, 7, 0, 4, 8, 2]` | Regressão (documental: não reprodutora) |
| **T-C2-09** | Artefato YAML `C2_PERMUTATION.yaml` | `seed_operacional=258915` e inversa `[5, 0, 8, 3, 6, 1, 2, 4, 7]` | Oficialidade do YAML |

---

## 8. Uso no Pipeline GO-8C (Documental)

**Condição C2 = T_PERM.** As etapas abaixo descrevem exclusivamente o uso de `CAT-XX` quando a condição de reconstrução é C2. O namespace `CAT-XX` é **local à condição C2** e não é compartilhado com C3 (`SYN-XXX`).

1. **Fase de Reconstrução Cega (condição C2):** O avaliador recebe apenas os rótulos opacos (`CAT-00`..`CAT-08`) e a definição neutra de cada categoria da taxonomia T_PERM (sem nomes ECP). Nenhum outro esquema de rótulos é usado nesta condição.
2. **Fase de Alignment:** Após reconstrução, o mapping bidirecional é aplicado para comparar com a cadeia canônica.
3. **Nenhum vazamento:** O mapping **não** é disponibilizado durante a reconstrução cega. Só é usado na etapa de comparação (Alignment Analysis).
4. **Isolamento de namespace:** `CAT-XX` (C2) e `SYN-XXX` (C3) não se misturam; cada condição opera no seu próprio namespace. Nenhum mapping SYN → ECP é criado em C2.

---

## 9. Isolamento de Stream (Regra Metodológica)

- A seed oficial `258915` **só** serve para a permutação C2 das 9 categorias ECP.
- Qualquer outro uso (embaralhamento de casos, amostragem, splits) **deve** usar seeds independentes, registradas separadamente.
- Violação → contaminação de cegueira → exclusão automática (ver Entregável 7).

---

## GO-8C CHANGE LOG

### GO-8C D-01 (aplicado — DECISION D-01)
- Seed oficial C2 corrigida para `258915` (hex `0x3f363`) — reproduz a tabela §5 sob PCG64.
- Seed antiga `11473621728585666159` registrada como **`HISTORICAL-NON-REPRODUCING`**.
- Inversa verdadeira corrigida para `[5, 0, 8, 3, 6, 1, 2, 4, 7]` (a inversa declarada do GO-8B §5 estava corrompida).
- JSON §6 corrigido com `seed: 0x3f363` e campos `seed_operacional` / `seed_registrada_historica`.
- Tabela de permutação e mapping bidirecional **inalterados** (idênticos ao GO-8B §5/§6).
- Proveniência registrada: `GO-8C correction derived from GO-8B 02-C2-PERMUTATION.md §6`.
- Referência ao GO-8B: `P1-C2-01` resolvido como Opção A; GO-8C corrige definitivamente a dívida.
- Nenhum arquivo do GO-8B alterado. Nenhum Lock gerado nesta etapa.
- Status: CORRECTED — DECIDED (D-01)
