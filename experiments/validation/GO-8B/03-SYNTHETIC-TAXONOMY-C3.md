# GO-8B Entregável 3 — Especificação da Taxonomia Sintética C3

**Status:** REVISED — PENDING GOVERNANCE AUDIT
**Revisão:** R1 (aplicação do Decision Record 00-GO-8B-R1) + R3 (DECISION R3-01)
**Data original:** 2026-08-10
**Objetivo:** Definir uma **taxonomia sintética independente** para codificação de entidades observadas na reconstrução cega, correspondente à condição **C3 = T_SYNTH**. A taxonomia é gerada sob procedimento cego; sua cardinalidade, nomes, hierarquia e estrutura são **variáveis emergentes** — não pré-fixadas.
**Regra:** A taxonomia **não** pode conter termos, conceitos ou estrutura derivados do ECP (ECP-000..010). O gerador C3 **não recebe qualquer informação sobre o ECP**. Qualquer comparação C3/ECP ocorre **somente** na fase de análise, depois da reconstrução, nunca como restrição de geração.

---

## 1. Princípios de Neutralidade

**Condição C3 = T_SYNTH (DECISION R3-01).** C3 usa **exclusivamente** rótulos `SYN-XXX`. O namespace `SYN-XXX` é **local à condição C3** e nunca compartilha categorias, mapping ou namespace com C2 (`CAT-XX`) na mesma reconstrução. Nenhum mapping SYN → ECP é criado durante geração ou reconstrução; a comparação C3 ↔ ECP ocorre somente na fase de análise.

| Princípio | Exigência | Verificação |
|---|---|---|
| **N-1 Independência Conceitual** | Zero termos do vocabulário ECP-000..010 (Problem, Goal, Claim, Knowledge, Assumption, Evidence, Decision, State, Artifact, L-0, L-1, P-1..P-12) | Varredura léxica automatizada |
| **N-2 Independência Estrutural** | A hierarquia/taxonomia não pode espelhar nenhuma estrutura do ECP (não há cardinalidade, profundidade ou arranjo pré-fixado que replique a cadeia do ECP) | Comparação topológica (isomorfismo de grafos) pós-geração |
| **N-3 Origem Externa** | Taxonomia derivada de literatura de engenharia geral, classificação de falhas, ontologias de domínio (ex.: ISO 15288, SysML, STAMP, FRAM) — não do ECP | Rastreabilidade de fontes |
| **N-4 Cegueira de Geração** | O gerador C3 não conhece: o ECP, o mapping C2, nem os resultados da reconstrução cega | Procedimento de geração cega (§3) |
| **N-5 Validação Independente** | Neutralidade validada por parte que não participou da geração (BIP-VAL) | BIP separado obrigatório |

**Natureza da estrutura:** C3 é um **grafo direcionado acíclico (DAG)** de categorias sintéticas cujo **número de nós, níveis, aridade, nomes e hierarquia são emergentes** do procedimento de geração cega. Não há cardinalidade obrigatória de categorias, supercategorias ou subcategorias. Não há mapeamento pré-definido SYN → ECP.

---

## 2. Estrutura Emergente da Taxonomia C3

A taxonomia C3 é descrita da seguinte forma:

> Taxonomia sintética independente, gerada sob procedimento cego, cuja cardinalidade, nomes, hierarquia e estrutura são variáveis emergentes.

- **Tipo:** grafo direcionado acíclico (DAG) de categorias sintéticas
- **Cardinalidade:** **emergente** — determinada pelo procedimento de geração (§3), não imposta a priori
- **Profundidade / níveis:** **emergente** (não fixada em 3; pode variar por galho)
- **Aridade:** cada nó pode ter múltiplos pais (polihierarquia permitida)
- **Rótulos:** códigos alfanuméricos opacos `SYN-XXX` (sequenciais) + label descritivo neutro
- **Schema:** o schema valida **estrutura e tipos**, não um número específico de nós — qualquer cardinalidade válida é aceita

**Importante:** nenhuma cardinalidade (ex.: 9 categorias, 3 níveis, 27 nós) é fixada. A existência de uma estrutura específica no ECP **não** justifica, e **não** limita, a estrutura de C3.

---

## 3. Procedimento de Geração Cega (Blind Generation Procedure)

### 3.1 Participantes e Papéis

| Papel | Responsabilidade | Restrição de Conhecimento |
|---|---|---|
| **Gerador (G)** | Produz a taxonomia C3 a partir de fontes externas, sem pré-definição de cardinalidade | **Não** conhece: ECP, mapping C2, resultados SX-001, hipóteses ECP, pipeline GO-8B |
| **Validador (V)** | Executa BIP-VAL (neutralidade) | **Não** conhece: identidade do Gerador, mapping C2 |
| **Auditor (A)** | Registra o artefato final (sem congelamento nesta etapa) | Acesso total pós-validação |

### 3.2 Passos do Procedimento

```
1. PREPARAÇÃO (Auditor)
   1.1 Selecionar corpus de fontes externas (mínimo 5, domínios diversos):
       - ISO 15288 (Systems Engineering)
       - SysML v1.6 (Modeling Language)
       - STAMP/STPA (Leveson)
       - FRAM (Hollnagel)
       - ISO 9001:2015 (Quality Management)
       - INCOSE Systems Engineering Handbook
       - NASA Systems Engineering Handbook
       - DoD Architecture Framework (DoDAF)
   1.2 Extrair vocabulário de entidades/estados/decisões de cada fonte
   1.3 Entregar corpus ao Gerador (sem metadados ECP; sem qualquer referência a ECP)

2. GERAÇÃO CEGA (Gerador)
   2.1 Ler corpus; identificar recorrências de conceitos transversais
   2.2 Agrupar em estrutura emergente — NÃO fixar número de categorias/níveis;
       a cardinalidade e a hierarquia emergem da análise do corpus (ex.: clustering,
       critério de cobertura + distinção semântica)
   2.3 Atribuir códigos SYN-XXX sequenciais à estrutura gerada
   2.4 Produzir arquivo `C3_TAXONOMY.yaml` com:
       - nodes: [{id, label, parent_ids[], source_refs[]}]
       - edges: [{from, to, relation_type}]
       - metadata: {generator_id, timestamp, corpus_hash, seed_generation, cardinality_notes}
   2.5 Entregar ao Auditor (sem revelar identidade ao Validador)

3. REGISTRO (Auditor)
   3.1 Verificar conformidade com o schema (§2): DAG, rótulos opacos, source_refs
       (validação estrutural, sem cardinalidade alvo)
   3.2 Registrar arquivo (HASH STATUS: PENDING LOCK PROTOCOL — nenhum hash congelado)
   3.3 Registrar em log de auditoria; entregar ao Validador para BIP-VAL
```

**Nenhuma etapa do gerador recebe, consulta ou deriva informações do ECP.** Não há mapeamento SYN→ECP definido nesta etapa.

### 3.3 Seed de Geração (Configuração, Para Reprodutibilidade do Procedimento)

```
seed_generation:
  value: 12088763053434307680
  type: uint64
  uso: reprodução do procedimento cego (apenas se o Gerador empregar algoritmo estocástico)
```

A seed é **dado de configuração**. Se o procedimento for determinístico (sem estocasticidade), a seed não é aplicada. A seed não codifica nenhuma relação com o ECP.

---

## 4. Validação de Neutralidade (BIP-VAL — Obrigatório, Separado)

### 4.1 BIP-VAL — Blind Inference Protocol para Validação da Taxonomia

| Campo | Valor |
|---|---|
| **BIP-ID** | BIP-VAL |
| **Objeto** | `C3_TAXONOMY.yaml` (produzido pelo procedimento cego) |
| **Pergunta** | A taxonomia C3 é neutra/independente em relação ao ECP? (N-1..N-5) |
| **Executores** | Validador (V) + 2 revisores independentes (R1, R2) |
| **Cegueira** | Validadores **não** conhecem mapping C2, nem resultados SX-001, nem hipóteses ECP |

### 4.2 Testes de Neutralidade (Automatizados + Humanos)

| Teste | Método | Critério Pass |
|---|---|---|
| **NT-01 Léxico** | Varredura por termos ECP-000..010 (lista fixa de 47 termos) | **Zero ocorrências** em labels, definitions, source_refs |
| **NT-02 Estrutural Independente** | Isomorfismo de grafos: C3 DAG vs qualquer estrutura ECP (incluindo a cadeia canônica) | **Não isomórfico** para nenhuma estrutura ECP conhecida |
| **NT-03 Origem de Fonte** | Verificar `source_refs` de cada nó → mapear para corpus externo | **100% dos nós** têm ≥1 referência a corpus externo; **0%** referenciam ECP |
| **NT-04 Independência de Geração** | Auditoria do procedimento: evidenciar que o gerador não teve acesso a material ECP | Registro de cegueira (log de acessos/entregas) + declaração assinada |
| **NT-05 Julgamento Humano** | 3 validadores independentes classificam cada categoria C3: "derivado de ECP?" (Sim/Não/Incerto) | **≤ 1 "Sim" por categoria** (maioria "Não") |

**Nota metodológica:** Nenhum teste aqui impõe cardinalidade, alinhamento 1:1 ou mapeamento C3↔ECP. A conformidade de C3 é definida pela **independência**, não por um tamanho ou correspondência com o ECP.

### 4.3 Critério de Aprovação BIP-VAL

**APROVADO** se e somente se: **Todos** NT-01..NT-04 = Pass **E** NT-05 = Pass.

**REJEITADO** → Taxonomia descartada; novo ciclo de geração cega com corpus expandido/modificado; nova seed (se aplicável).

### 4.4 Registro de BIP-VAL

Resultado salvo em `BIP-VAL_REPORT.yaml`:

```yaml
bip_id: BIP-VAL
taxonomy_file: C3_TAXONOMY.yaml
validator_id: <hash_anonimo>
reviewers: [<hash_r1>, <hash_r2>]
tests:
  NT-01: {status: PASS, details: "0 ocorrências de 47 termos ECP"}
  NT-02: {status: PASS, details: "C3 não isomórfico a nenhuma estrutura ECP"}
  NT-03: {status: PASS, details: "100% nós com source_refs externos; 0 referências ECP"}
  NT-04: {status: PASS, details: "Registro de cegueira confirma ausência de acesso ECP"}
  NT-05: {status: PASS, details: "R1: 0 Sim; R2: 1 Sim; R3: 0 Sim"}
verdict: PENDING (não congelado nesta etapa)
timestamp: <pendente>
```

---

## 5. Uso no Pipeline GO-8B

**Condição C3 = T_SYNTH.** A taxonomia C3 opera em **namespace local da condição** (`SYN-XXX`), sem compartilhar categorias, mapping ou namespace com C2 (`CAT-XX`) na mesma reconstrução.

1. **Geração:** Taxonomia C3 gerada **antes** de qualquer reconstrução cega dos casos GO-8B.
2. **Codificação Cega (condição C3):** Avaliadores da reconstrução usam **apenas** rótulos `SYN-XXX` para codificar entidades observadas. Nenhum outro namespace é misturado nesta condição.
3. **Comparação (fase de análise):** Somente **depois** da reconstrução, e na fase de análise, C3 pode ser comparado com ECP — via alinhamento semântico contínuo (Entregável 5), **nunca** como restrição de geração e **não** como mapeamento pré-definido SYN→ECP.
4. **BIP-VAL** executado **uma vez** após registro da taxonomia, **antes** do primeiro caso GO-8B.

---

## 6. Testes Unitários Planejados (Para Implementação)

| Teste | Entrada | Esperado |
|---|---|---|
| **T-C3-01** | `C3_TAXONOMY.yaml` | Schema válido (DAG, rótulos opacos, source_refs; **qualquer cardinalidade válida aceita**) |
| **T-C3-02** | Taxonomia + lista 47 termos ECP | NT-01 = 0 matches |
| **T-C3-03** | Taxonomia + estruturas ECP conhecidas | NT-02 = não isomórfico |
| **T-C3-04** | `source_refs` de todos os nós | NT-03 = 100% externo, 0% ECP |
| **T-C3-05** | Registro de cegueira do procedimento | NT-04 = sem acesso a material ECP |
| **T-C3-06** | BIP-VAL report | Verdict registrado; PENDING até auditoria |

---

## 7. Dívida Metodológica Conhecida (Registro, Não Correção)

| Item | Descrição | Mitigação GO-8B |
|---|---|---|
| **DEBT-C3-01** | Risco de convergência semântica espúria entre C3 e ECP posteriormente na análise | Comparação C3/ECP restrita à fase de análise; BIP-VAL humano; registro no DISCOVERY-LOG |
| **DEBT-C3-02** | Gerador pode ter viés implícito se conhece literatura de engenharia de sistemas (sobreposição com ECP) | Corpus amplo (≥8 fontes); cegueira total sobre ECP/GO-8B; validação independente |
| **DEBT-C3-03** | Cardinalidade emergente dificulta planejamento de análises que assumiam tamanho fixo | Contrato orientado por schema e cardinalidade real do JSON, não por tamanho esperado (ver Entregável 4) |

---

## GO-8B CHANGE LOG

### GO-8B-R1 (aplicado)
- Decision Record: 00-GO-8B-R1-DECISION-RECORD.md
- Revisão: R1
- Alterações principais:
  - Removidas cardinalidade obrigatória de 9 categorias, 9 supercategorias e 3 subcategorias por supercategoria.
  - Removida a tabela pré-definida de 9 supercategorias com labels neutros fixos.
  - Removida qualquer correspondência 1:1 com ECP e qualquer referência a categorias ECP durante a geração.
  - Removido o mapeamento pré-definido SYN → ECP; comparação C3/ECP passa a ocorrer **somente** na fase de análise, pós-reconstrução.
  - Estrutura descrita como emergente (cardinalidade/nomes/hierarquia variáveis), orientada por schema.
  - Seed de geração registrada como dado de configuração (uint64).
  - Removidas afirmações de hash congelado (HASH STATUS: PENDING LOCK PROTOCOL).
- Alterações metodológicas:
  - C3 agora é, por construção, independente e emergente; o gerador não recebe informações sobre ECP.
- Itens ainda pendentes:
  - BIP-VAL a executar após registro; hash a calcular no Lock Protocol.

### GO-8B-R3 (aplicado — DECISION R3-01)
- Fixada a taxonomia da condição C3 = **T_SYNTH** (§1), com namespace `SYN-XXX` **exclusivo**.
- Imposto o isolamento de namespace: C3 (`SYN-XXX`) e C2 (`CAT-XX`) **nunca compartilham categorias, mapping ou namespace** na mesma reconstrução; a taxonomia da condição é tratada como **namespace local da condição**.
- Reafirmado que nenhum mapping SYN → ECP é criado durante geração ou reconstrução; comparação C3 ↔ ECP apenas na fase de análise.
- Status: REVISED — PENDING GOVERNANCE AUDIT
