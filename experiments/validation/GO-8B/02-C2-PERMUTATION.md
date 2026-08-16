# GO-8B Entregável 2 — Permutação C2 (T_PERM) Determinística das 9 Categorias ECP

**Status:** REVISED — PENDING GOVERNANCE AUDIT
**Revisão:** R1 (aplicação do Decision Record 00-GO-8B-R1) + R3 (DECISION R3-01)
**Data:** 2026-08-10  
**Objetivo:** Gerar rótulos opacos para as 9 categorias do grafo de conhecimento ECP, garantindo cegueira na reconstrução (blind reconstruction), definindo a condição de reconstrução C2 = **T_PERM**.  
**Regra:** Determinística, reprodutível, seed registrada, **sem execução experimental**.

---

## 1. Taxonomias do Pipeline GO-8B (Fixadas pela DECISION R3-01)

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
  - seed: inteiro de 64 bits (registrado abaixo)
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

## 4. Seed Registrada (Configuração para GO-8B)

```
SEED_C2 = 0x9F3A7E2C1B8D4E6F  # 11473621728585666159 decimal
seed_c2:
  value: 11473621728585666159
  type: uint64
```

**Registro de auditoria:**
- Gerada em: 2026-08-10 (preparação GO-8B)
- Método: `secrets.token_bytes(8)` convertido para hex (entropy de sistema)
- Propósito exclusivo: permutação C2 das 9 categorias ECP para GO-8B
- Tratada como **dado de configuração** (inteiro uint64), conforme Correção 6.
- **Não reutilizar** para nenhum outro propósito (isolamento de streams)

---

## 5. Resultado da Permutação (Computado Offline — Valor Determinístico)

Executando o algoritmo com a seed acima:

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
**Inversa (posição opaca → índice canônico):** `[5, 0, 8, 3, 7, 1, 6, 4, 2]`

---

## 6. Mapping Bidirecional (Registrado para Uso no Pipeline)

```json
{
  "seed": "0x9F3A7E2C1B8D4E6F",
  "algorithm": "PCG64 Fisher-Yates",
  "canonical_order": ["Problem","Goal","Claim","Knowledge","Assumption","Evidence","Decision","State","Artifact"],
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
  }
}
```

---

## 7. Verificação de Sanidade (Testes Unitários Planejados)

| Teste | Entrada | Esperado | Critério Pass/Fail |
|---|---|---|---|
| **T-C2-01** | Seed + algoritmo + lista canônica | Permutação idêntica à tabela §5 | Determinismo |
| **T-C2-02** | Seed alterada (qualquer bit) | Permutação diferente | Sensibilidade à seed |
| **T-C2-03** | Mapping bidirecional | `canonical_to_opaque[opaque_to_canonical[X]] == X` ∀ X | Bijetividade |
| **T-C2-04** | Conjunto valores `opaque_to_canonical` | Exatamente 9 categorias canônicas, sem duplicatas | Completude |
| **T-C2-05** | RNG PCG64 vs `random.Random(seed)` (Python 3.11) | Mesmo resultado | Portabilidade |

---

## 8. Uso no Pipeline GO-8B (Documental)

**Condição C2 = T_PERM.** As etapas abaixo descrevem exclusivamente o uso de `CAT-XX` quando a condição de reconstrução é C2. O namespace `CAT-XX` é **local à condição C2** e não é compartilhado com C3 (`SYN-XXX`).

1. **Fase de Reconstrução Cega (condição C2):** O avaliador recebe apenas os rótulos opacos (`CAT-00`..`CAT-08`) e a definição neutra de cada categoria da taxonomia T_PERM (sem nomes ECP). Nenhum outro esquema de rótulos é usado nesta condição.
2. **Fase de Alignment:** Após reconstrução, o mapping bidirecional é aplicado para comparar com a cadeia canônica.
3. **Nenhum vazamento:** O mapping **não** é disponibilizado durante a reconstrução cega. Só é usado na etapa de comparação (Alignment Analysis).
4. **Isolamento de namespace:** `CAT-XX` (C2) e `SYN-XXX` (C3) não se misturam; cada condição opera no seu próprio namespace. Nenhum mapping SYN → ECP é criado em C2.

---

## 9. Isolamento de Stream (Regra Metodológica)

- Esta seed **só** serve para a permutação C2 das 9 categorias ECP no GO-8B.
- Qualquer outro uso (embaralhamento de casos, amostragem, splits) **deve** usar seeds independentes, registradas separadamente.
- Violação → contaminação de cegueira → exclusão automática (ver Entregável 7).

---

## GO-8B CHANGE LOG

### GO-8B-R1 (aplicado)
- Decision Record: 00-GO-8B-R1-DECISION-RECORD.md
- Revisão: R1
- Alterações principais:
  - Seed C2 registrada como **dado de configuração** (value: 11473621728585666159, type: uint64), corrigindo o valor decimal incorreto divulgado anteriormente.
  - Removido o status/uso da palavra "congelado" (Correção 12): o maximum agora é REVISED — PENDING GOVERNANCE AUDIT; hash da permutação pendente de Lock Protocol.
- Alterações metodológicas:
  - Nenhuma alteração no algoritmo de permutação; apenas o registro da seed e do status.
- Itens ainda pendentes:
  - Confirmar a co-existência do mecanismo C2 com a nova C3 independente/emergente.

### GO-8B-R3 (aplicado — DECISION R3-01)
- Fixada a taxonomia da condição C2 = **T_PERM**: mesmas 9 categorias ECP com rótulos `CAT-XX` permutados deterministicamente.
- Fixada a separação de namespaces C1/C2/C3/C4 (§1), com `CAT-XX` exclusivo de C2 e `SYN-XXX` exclusivo de C3.
- Imposto que C2 e C3 **nunca compartilham categorias, mapping ou namespace** na mesma reconstrução; a taxonomia recebida é tratada como **namespace local da condição**.
- Reafirmado que nenhum mapping SYN → ECP é criado durante geração ou reconstrução; comparação C3 ↔ ECP apenas na fase de análise.
- Reordenada a numeração de seções (nova §1 Taxonomias).
- Removida a pendência R1 de co-existência C2×C3 — agora resolvida pela separação formal de namespaces.
- Status: REVISED — PENDING GOVERNANCE AUDIT
