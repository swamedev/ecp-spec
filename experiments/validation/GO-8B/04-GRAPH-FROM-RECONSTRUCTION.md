# GO-8B Entregável 4 — Especificação do GraphFromReconstruction

**Status:** REVISED — PENDING GOVERNANCE AUDIT
**Revisão:** R1 (aplicação do Decision Record 00-GO-8B-R1) + R3 (DECISION R3-01) + R2 (R2-C4) + R5 (M-1, GO-8B-R5)
**Data original:** 2026-08-10
**Objetivo:** Definir o contrato JSON, algoritmo e testes unitários para transformar a saída da Reconstrução Cega (entidades codificadas na taxonomia sintética da condição + relações) em um grafo de conhecimento rotulado no espaço sintético da condição, pronto para a análise comparativa (Entregável 5). O contrato é **orientado pelo schema**, não por cardinalidade esperada.
**Entradas:** Reconstrução Cega (OBS-SCHEMA + taxonomia da condição C2/C3) — rótulos opacos no namespace local
**Saída:** Grafo direcionado rotulado (nodes, edges) **no espaço sintético da condição**, pronto para o WL Kernel (§5)
**Princípio:** O número de nós **não** constitui critério de conformidade com ECP. Nenhum mapeamento C3→ECP é introduzido no parser.

**Namespace local (DECISION R3-01 + R5 M-1):** o parser trata a taxonomia recebida pela condição como **namespace local da condição**, declarado obrigatoriamente pelo campo `taxonomy_namespace`. O schema distingue **inequivocamente** as quatro condições do pipeline:

| Condição | Taxonomia | Namespace (`taxonomy_namespace`) |
|---|---|---|
| **C1** | T_ECP | `ECP` (labels canônicos ECP) |
| **C2** | T_PERM | `CAT` (`CAT-XX`) |
| **C3** | T_SYNTH | `SYN` (`SYN-XXX`) |
| **C4** | T_NULL | `NULL` (nenhuma taxonomia fixa) |

**Nenhum mapping entre namespaces é criado** (não há equivalência `CAT`↔`SYN`, `SYN`↔`ECP`, `ECP`↔`CAT`, nem qualquer tradução de rótulos entre namespaces). Cada reconstrução opera **exclusivamente** no namespace declarado. A mistura de dois ou mais namespaces dentro da mesma reconstrução é **rejeitada** (erro `NAMESPACE_MIX`). Para `NULL`, não existe taxonomia fixa para ancorar categorias sintéticas; a reconstrução C4 **não** produz grafo no espaço sintético e não é processada por este parser. Nenhum mapping SYN → ECP é criado nesta fase.

---

## 1. Visão Geral do Pipeline

```
Reconstrução Cega (Avaliador)
       ↓
Entidades observadas + Relações (codificadas no namespace local da condição: C2→CAT-XX | C3→SYN-XXX)
       ↓
[GraphFromReconstruction]  ← Taxonomia da condição (namespace local)
       ↓
Grafo Reconhecido G_rec = (V_rec, E_rec, λ_V, λ_E)  <-- em espaço sintético da condição
       ↓
WL Kernel / Análise Comparativa (Entregável 5) <-- comparação C3↔ECP somente NESSA FASE
```

**Nota:** O mapeamento/alignment entre a taxonomia sintética e ECP é realizado **apenas na fase de análise** (Entregável 5), depois da reconstrução. O parser **não** contém mapeamento para ECP. O namespace é local à condição: a mesma execução do parser nunca mistura `CAT-XX` e `SYN-XXX`.

---

## 2. Contrato JSON (Schema)

### 2.1 Entrada: `ReconstructionInput`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ReconstructionInput",
  "type": "object",
  "required": ["case_id", "reconstruction_version", "entities", "relations", "taxonomy_version", "taxonomy_namespace"],
  "properties": {
    "case_id": { "type": "string", "pattern": "^SX-\\d{3}$" },
    "reconstruction_version": { "type": "string", "format": "date-time" },
    "taxonomy_version": { "type": "string", "description": "Referência à taxonomia da condição (C1=T_ECP, C2=T_PERM, C3=T_SYNTH; C4=T_NULL sem taxonomia); hash só no Lock Protocol" },
    "taxonomy_namespace": {
      "type": "string",
      "enum": ["ECP", "CAT", "SYN", "NULL"],
      "description": "Namespace local da condição, OBRIGATÓRIO. Distingue inequivocamente: C1→ECP, C2→CAT, C3→SYN, C4→NULL. Exclusivo por reconstrução; nenhum mapping entre namespaces (DECISION R3-01 + R5 M-1)"
    },
    "entities": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["entity_id", "syn_category", "confidence", "source_af_ids"],
        "properties": {
          "entity_id": { "type": "string", "pattern": "^ENT-\\d{4}$" },
          "syn_category": { "type": "string", "pattern": "^(CAT-\\d{2}|SYN-\\d+|Problem|Goal|Claim|Knowledge|Assumption|Evidence|Decision|State|Artifact)$", "description": "Rótulo no namespace declarado por taxonomy_namespace: CAT-XX (C2), SYN-XXX (C3) ou label canônico ECP (C1). NULL (C4) não possui taxonomia fixa e não é processado por este parser" },
          "confidence": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
          "source_af_ids": {
            "type": "array",
            "items": { "type": "string", "pattern": "^AF-\\d{3}$" },
            "minItems": 1
          },
          "attributes": {
            "type": "object",
            "additionalProperties": { "type": "string" },
            "description": "Atributos livres da entidade (ex.: timestamp, ator, descrição neutra)"
          }
        }
      }
    },
    "relations": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["relation_id", "source", "target", "relation_type", "confidence"],
        "properties": {
          "relation_id": { "type": "string", "pattern": "^REL-\\d{4}$" },
          "source": { "type": "string", "pattern": "^ENT-\\d{4}$" },
          "target": { "type": "string", "pattern": "^ENT-\\d{4}$" },
          "relation_type": { "type": "string" },
          "confidence": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
          "evidence_af_ids": {
            "type": "array",
            "items": { "type": "string", "pattern": "^AF-\\d{3}$" }
          }
        }
      }
    }
  }
}
```

**Cardinalidade dinâmica:** não há `minItems`/`maxItems` fixo em `entities`/`relations` além do mínimo para uma reconstrução não-vazia; categorias e relações são lidas do JSON efetivamente produzido. Nenhuma cardinalidade alvo (ex.: 27) é imposta.

**Namespace local (R3-01 + R5 M-1):** o campo `taxonomy_namespace` é **obrigatório** e declara o namespace da condição (`ECP` para C1=T_ECP; `CAT` para C2=T_PERM; `SYN` para C3=T_SYNTH; `NULL` para C4=T_NULL). O parser valida que **todos** os `syn_category` da reconstrução pertencem ao namespace declarado — nunca mistura dois namespaces distintos (`ECP`/`CAT`/`SYN`/`NULL` → erro `NAMESPACE_MIX`). Ausência do campo `taxonomy_namespace` → erro `SCHEMA_INVALID` (campo obrigatório).

### 2.2 Saída: `RecognizedGraph` (em espaço sintético da condição)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "RecognizedGraph",
  "type": "object",
  "required": ["case_id", "graph_version", "nodes", "edges", "metadata"],
  "properties": {
    "case_id": { "type": "string", "pattern": "^SX-\\d{3}$" },
    "graph_version": { "type": "string", "format": "date-time" },
    "nodes": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["node_id", "syn_category", "confidence", "source_entities"],
        "properties": {
          "node_id": { "type": "string", "pattern": "^N-\\d{4}$" },
          "syn_category": { "type": "string", "pattern": "^(CAT-\\d{2}|SYN-\\d+|Problem|Goal|Claim|Knowledge|Assumption|Evidence|Decision|State|Artifact)$" },
          "confidence": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
          "source_entities": {
            "type": "array",
            "items": { "type": "string", "pattern": "^ENT-\\d{4}$" },
            "description": "Entidades da reconstrução que colapsaram neste nó sintético"
          },
          "merged": { "type": "boolean", "description": "True se múltiplas entidades do namespace colapsaram no mesmo nó" }
        }
      }
    },
    "edges": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["edge_id", "source", "target", "relation_type", "confidence", "source_relations"],
        "properties": {
          "edge_id": { "type": "string", "pattern": "^E-\\d{4}$" },
          "source": { "type": "string", "pattern": "^N-\\d{4}$" },
          "target": { "type": "string", "pattern": "^N-\\d{4}$" },
          "relation_type": { "type": "string" },
          "confidence": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
          "source_relations": {
            "type": "array",
            "items": { "type": "string", "pattern": "^REL-\\d{4}$" }
          }
        }
      }
    },
    "metadata": {
      "type": "object",
      "required": ["num_nodes", "num_edges", "syn_categories_used", "unmapped_entities"],
      "properties": {
        "num_nodes": { "type": "integer", "minimum": 0 },
        "num_edges": { "type": "integer", "minimum": 0 },
        "syn_categories_used": {
          "type": "array",
          "items": { "type": "string", "pattern": "^(CAT-\\d{2}|SYN-\\d+)$" }
        },
        "unmapped_entities": {
          "type": "array",
          "items": { "type": "string", "pattern": "^ENT-\\d{4}$" }
        }
      }
    }
  }
}
```

**Semântica de `num_nodes`:** derivado do JSON efetivamente produzido. **O número de nós não constitui critério de conformidade com ECP.**

---

## 3. Algoritmo GraphFromReconstruction

### 3.1 Entradas Necessárias (Registradas Antes da Execução)

| Artefato | Versão | Fonte |
|---|---|---|
| Taxonomia da condição (C2=T_PERM ou C3=T_SYNTH) | `C2_PERMUTATION.yaml` / `C3_TAXONOMY.yaml` (HASH STATUS: PENDING LOCK PROTOCOL) | Entregáveis 2/3 |
| Reconstrução Cega | `ReconstructionInput` (schema §2.1) | Pipeline de reconstrução |

**Nenhum mapeamento para ECP é entrada deste parser.** O parser opera no **namespace local da condição** (declarado obrigatoriamente por `taxonomy_namespace`; C1→ECP, C2→CAT, C3→SYN, C4→NULL). Alinhamento semântico sintético↔ECP ocorre somente na fase de análise (Entregável 5). Nenhum mapping entre namespaces é criado.

### 3.2 Passos do Algoritmo

```
FUNCTION GraphFromReconstruction(input: ReconstructionInput) -> RecognizedGraph:

  1. VALIDAÇÃO DE ENTRADA
     - Validar input contra schema ReconstructionInput
     - Verificar versão da taxonomia (taxonomy_version)
     - Verificar namespace local (OBRIGATÓRIO — R5 M-1):
       * taxonomy_namespace presente; ausente → erro "SCHEMA_INVALID"
       * taxonomy_namespace ∈ {ECP, CAT, SYN, NULL} (C1→ECP, C2→CAT, C3→SYN, C4→NULL)
       * TODOS os syn_category devem pertencer AO MESMO namespace declarado:
         - ECP → labels canônicos ECP (Problem, Goal, Claim, Knowledge,
           Assumption, Evidence, Decision, State, Artifact)
         - CAT → CAT-XX (C2=T_PERM)
         - SYN → SYN-XXX (C3=T_SYNTH)
         - NULL → C4=T_NULL não possui taxonomia fixa; NÃO produz grafo
           sintético; não processado por este parser
       * Mistura de dois ou mais namespaces distintos → erro "NAMESPACE_MIX"
     - Falha → erro "SCHEMA_INVALID"

  2. AGRUPAMENTO POR CATEGORIA SINTÉTICA (Nível de Entidade)
     PARA cada entity EM input.entities:
       syn_cat = entity.syn_category      # rótulo opaco no namespace local da condição
       CRIAR/ATUALIZAR nó sintético N(syn_cat):
         - Agregar confiança: média ponderada por entity.confidence
         - Acumular source_entities: [entity.entity_id]
         - merged = (count(source_entities) > 1)
     RESULTADO: nodes_map {syn_category → NodeData}
     # Cardinalidade: len(nodes_map) é DERIVADA do JSON, nunca pré-fixada

  3. CONSTRUÇÃO DE ARESTAS (Nível de Relação)
     PARA cada relation EM input.relations:
       source_node = nodes_map[entities[relation.source].syn_category]
       target_node = nodes_map[entities[relation.target].syn_category]
       SE source_node OU target_node NÃO EXISTE: CONTINUAR
       rel_type = relation.relation_type
       CRIAR/ATUALIZAR aresta E(source_node, target_node, rel_type):
         - Agregar confiança: média ponderada por relation.confidence
         - Acumular source_relations: [relation.relation_id]
     RESULTADO: edges_list

  4. NORMALIZAÇÃO DE CONFIANÇA
     - Para cada nó: confidence = mean(entity.confidence for entity in source_entities)
     - Para cada aresta: confidence = mean(relation.confidence for relation in source_relations)

  5. CONSTRUÇÃO METADATA
     - num_nodes = len(nodes_map)
     - num_edges = len(edges_list)
     - syn_categories_used = keys(nodes_map)
     - unmapped_entities = []  # o espaço sintético da condição não possui mapping externo aqui

  6. RETORNO RecognizedGraph com todos os campos preenchidos
```

**Nota de cardinalidade:** o parser aceita **qualquer número válido** de entidades, categorias, subcategorias, arestas e relações, conforme o schema. Não assume `9 × 3 = 27` nem qualquer tamanho obrigatório. Se supercategorias e subcategorias forem representadas como nós, o total é derivado do JSON produzido.

---

## 4. Testes Unitários Planejados

| Teste ID | Descrição | Entrada | Critério Pass |
|---|---|---|---|
| **T-GFR-01** | Schema validation: input válido | ReconstructionInput válido | Zero erros de validação JSON Schema |
| **T-GFR-02** | Schema validation: input inválido (falta campo obrigatório) | Input sem `entities` | Erro `SCHEMA_INVALID` com mensagem clara |
| **T-GFR-03** | Version mismatch detection | taxonomy_version inexistente | Erro `VERSION_MISMATCH` |
| **T-GFR-04** | Cardinalidade variável | Entradas com 5, 8, 12 categorias distintas | num_nodes deriva do JSON (5, 8, 12); sem erro |
| **T-GFR-05** | Múltiplas entidades SYN → mesmo nó (merge) | 3 entidades mesma SYN → 1 nó | node único, merged=true, confidence=média ponderada |
| **T-GFR-06** | Entidade com categoria ausente no schema (unmapped) | Entidade com SYN fora do schema | Registrada em metadata; não cria nó |
| **T-GFR-07** | Construção de arestas entre nós | Relação ENT-0001 → ENT-0002 | Aresta E(N-source, N-target, rel_type) criada |
| **T-GFR-08** | Aresta com fonte inexistente (ignorada) | Relação ENT-0001 → ENT-9999 | Aresta NÃO criada; sem erro |
| **T-GFR-09** | Agregação de confiança em arestas múltiplas | 3 relações mesma origem/destino | Aresta única confidence = média |
| **T-GFR-10** | Metadata completa e consistente | Grafo resultante | Todos campos metadata preenchidos; contagens batem |
| **T-GFR-11** | Determinismo: mesma entrada → mesma saída | Executar 2x com mesmo input | Outputs idênticos |
| **T-GFR-12** | Grafo vazio (todas entidades inválidas) | Input sem entidades válidas | 0 nós, 0 arestas, metadata consistente |
| **T-GFR-13** | Ausência de mapping para ECP | Saída do parser | Nenhum campo `ecp_category` presente; rótulos permanecem no namespace local da condição (ECP/CAT/SYN) |
| **T-GFR-14** | Namespace isolado C2 vs C3 | Input com `taxonomy_namespace=SYN` mas entidade `CAT-01` | Erro `NAMESPACE_MIX`; parser não cria grafo misto |
| **T-GFR-15** | Namespace declarado C2 | Input `taxonomy_namespace=CAT` com `CAT-00..CAT-08` | Grafo construído; rótulos permanecem `CAT-XX` |
| **T-GFR-16** | Namespace obrigatório (R5 M-1) | Input sem o campo `taxonomy_namespace` | Erro `SCHEMA_INVALID` (campo obrigatório) |
| **T-GFR-17** | Namespace ECP — C1/T_ECP (R5 M-1) | Input `taxonomy_namespace=ECP` com labels canônicos ECP (`Problem`, `Goal`, …) | Grafo construído no namespace ECP; rótulos permanecem canônicos; sem mapping para outro namespace |
| **T-GFR-18** | Namespace NULL — C4/T_NULL (R5 M-1) | Input `taxonomy_namespace=NULL` | Nenhuma taxonomia fixa → parser NÃO constrói grafo sintético; rejeição de mistura com qualquer outro namespace |
| **T-GFR-19** | Mistura ECP+SYN rejeitada (R5 M-1) | Input `taxonomy_namespace=SYN` com entidade `Problem` | Erro `NAMESPACE_MIX` |
| **T-GFR-20** | Mistura ECP+CAT rejeitada (R5 M-1) | Input `taxonomy_namespace=ECP` com entidade `CAT-01` | Erro `NAMESPACE_MIX` |
| **T-GFR-21** | Enum de namespace exige condição válida (R5 M-1) | Input `taxonomy_namespace=XYZ` (fora do enum) | Erro `SCHEMA_INVALID` (valor fora de `{ECP, CAT, SYN, NULL}`) |

---

## 5. Interface de Integração (Para WL Kernel / Análise)

O `RecognizedGraph` é a **entrada** da análise comparativa (Entregável 5). Formato: grafo direcionado rotulado `(V, E, λ_V, λ_E)` onde:

- `V` = nodes (com `syn_category` como label λ_V)
- `E` = edges (com `relation_type` como label λ_E)
- Atributos `confidence` em nós e arestas → pesos

O alinhamento semântico entre a taxonomia da condição (C2/C3) e ECP (usando embeddings/continuum) é realizado **na fase de análise**, não aqui.

---

## 6. Dívida Metodológica Conhecida

| Item | Descrição | Mitigação GO-8B |
|---|---|---|
| **DEBT-GFR-01** | Alinhamento sintético↔ECP é semântico e pode ter subjetividade residual | Ocorre apenas na fase de análise com similaridade contínua; registro no DISCOVERY-LOG |
| **DEBT-GFR-02** | Perda de granularidade quando entidades colapsam em nós | Metadata `merged` + `source_entities` preserva rastreabilidade |
| **DEBT-GFR-03** | `relation_type` é livre (não enumerado) | Validado pela taxonomia da condição e schema geral; relação semântica definida na análise |

---

## GO-8B CHANGE LOG

### GO-8B-R1 (aplicado)
- Decision Record: 00-GO-8B-R1-DECISION-RECORD.md
- Revisão: R1
- Alterações principais:
  - Parser passa a ser **orientado por schema**, aceitando qualquer número válido de entidades/categorias/subcategorias/arestas/relações.
  - Removida a suposição de cardinalidade obrigatória `9 × 3 = 27`.
  - **Removido o mapeamento C3→ECP do parser** (seção "Regras de Mapeamento SYN → ECP" eliminada).
  - Saída `RecognizedGraph` rotulada no espaço sintético da condição (não mais `ecp_category`).
  - Adicionado explicitamente: "O número de nós não constitui critério de conformidade com ECP."
  - Removidas afirmações de hash congelado (HASH STATUS: PENDING LOCK PROTOCOL).
- Alterações metodológicas:
  - Comparação C3/ECP deslocada para a fase de análise (Entregável 5); parser neutro.
- Itens ainda pendentes:
  - Implementação e validação dos testes T-GFR-01..21.

### GO-8B-R3 (aplicado — DECISION R3-01; R2-C4)
- Parser passa a tratar a taxonomia recebida pela condição como **namespace local da condição** (campo `taxonomy_namespace`).
- Schema aceita `CAT-XX` (C2=T_PERM) e `SYN-XXX` (C3=T_SYNTH), mas **proíbe mistura** na mesma reconstrução (novo erro `NAMESPACE_MIX`).
- Novos testes T-GFR-14/T-GFR-15 cobrem isolamento de namespace.
- **R2-C4:** corrigida a tipografia `SYM/SYN` para rótulos `CAT/SYN` no T-GFR-13.
- Status: REVISED — PENDING GOVERNANCE AUDIT

### GO-8B-R5 (aplicado — M-1, GO-8B-R5)
- **`taxonomy_namespace` adicionado ao conjunto de campos OBRIGATÓRIOS** do schema `ReconstructionInput` (R5 M-1).
- Enum do namespace expandido para **`["ECP", "CAT", "SYN", "NULL"]`**, distinguindo inequivocamente **C1→ECP, C2→CAT, C3→SYN, C4→NULL**.
- `syn_category` passa a aceitar também os **labels canônicos ECP** (para o namespace `ECP`); `NULL` (C4) não possui taxonomia fixa e **não é processado** por este parser (sem grafo sintético).
- **Rejeição de mistura de namespaces** documentada e testada para qualquer par de namespaces (`NAMESPACE_MIX`): novos testes T-GFR-16..T-GFR-21 (campo obrigatório, ECP, NULL, ECP+SYN, ECP+CAT, enum inválido).
- **Nenhum mapping entre namespaces criado** (sem equivalência `CAT`↔`SYN`, `SYN`↔`ECP`, `ECP`↔`CAT`).
- Não foram alteradas a definição da unidade experimental nem a métrica primária.
- Status: REVISED — PENDING GOVERNANCE AUDIT
