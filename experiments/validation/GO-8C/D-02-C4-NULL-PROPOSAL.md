# GO-8C — D-02 PROPOSTA TÉCNICA — C4 / NULL (Incompatibilidade de Namespace)

**Data:** 2026-08-13
**Ciclo:** GO-8C
**Status:** **PROPOSTA** — PENDING GOVERNANCE DECISION (nenhuma implementação executada)
**Escopo:** dívida D-02 (C4/NULL — incompatibilidade entre namespace NULL e o pipeline de grafos). Somente leitura do GO-8B; nenhum arquivo do GO-8B alterado.

---

## 1. Artefatos Lidos (somente leitura)

| Artefato | Relevância |
|---|---|
| `experiments/validation/GO-8B/04-GRAPH-FROM-RECONSTRUCTION.md` | §1.1 (NULL não processado), §2.1 (schema, `syn_category` sem padrão para NULL), §3.2 (passo 1 — validação de namespace), T-GFR-18 |
| `scripts/go8b/operational/graph_from_reconstruction.py` | linhas 84-85: `if ns == "NULL": raise ValueError("NAMESPACE_MIX")` |
| `experiments/validation/GO-8B/decisions/NAMESPACE-OPERATIONAL-DECISION.md` | decisão operacional A=CAT / B=SYN / C=CAT |
| `experiments/validation/GO-8B/02-C2-PERMUTATION.md` | §1 (tabela C1–C4), §8 (uso de CAT na reconstrução cega) |
| `experiments/validation/GO-8B/03-SYNTHETIC-TAXONOMY-C3.md` | namespace SYN exclusivo da condição C3 |
| `experiments/validation/GO-8B/05-WL-KERNEL.md` | `emb_synth(label)` consulta taxonomia da condição (C2/C3); NULL sem fonte de embeddings |
| `experiments/validation/GO-8B/06-STATISTICAL-PROTOCOL.md` | S0_NULL = calibração de erro tipo I (não é namespace NULL) |
| `experiments/validation/GO-8B/07-FAILURE-CRITERIA.md` | FR-03 (NAMESPACE_MIX), exigência de reconstruções válidas por condição (07 §8) |
| `experiments/validation/GO-8B/08-PRE-REGISTRATION.md` | §3.5 condições A/B/C; §5 hipóteses B>A, C>A, C≥B |
| `experiments/validation/GO-8B/pilot-input/P5-PRODUCTION-MANIFEST.md` | A = só atomic facts; B = atomic facts + C3 (SYN); C = narrativa completa |
| `scripts/go8b/operational/p3_tests_gfr.py` | T-GFR-18 (NULL rejeitado), T-GFR-14..21 (isolamento de namespace) |
| `scripts/go8b/operational/p4_generate_embeddings.py` | linha 56: `"namespaces": ["ECP", "SYN", "CAT"]` — NULL ausente também da geração de embeddings |
| `scripts/go8b/operational/wl_kernel.py` | `emb_function(label)` — embeds qualquer label; S_struct é topológica (anonimizada) |

---

## 2. Causa Raiz da Incompatibilidade

A incompatibilidade tem **duas camadas**, e a implementação do parser **não é um bug** — é uma implementação fiel da especificação congelada.

### 2.1 Camada de especificação (design)

- O entregável congelado `04-GRAPH-FROM-RECONSTRUCTION.md` §1.1 define C4/T_NULL como "nenhuma taxonomia fixa" e afirma **explicitamente**:
  > "Para `NULL`, não existe taxonomia fixa para ancorar categorias sintéticas; a reconstrução C4 **não** produz grafo no espaço sintético e **não é processada por este parser**."
- §2.1 (schema): o `pattern` de `syn_category` é `^(CAT-\d{2}|SYN-\d+|Problem|Goal|Claim|...|Artifact)$` — **não existe sintaxe de rótulo para NULL** (nenhum padrão `NULL-XX` ou rótulo livre é definido).
- §3.2 (passo 1 do algoritmo): `NULL → C4=T_NULL não possui taxonomia fixa; NÃO produz grafo sintético; não processado por este parser`.
- `08-PRE-REGISTRATION.md` §3: namespaces `C1=ECP · C2=CAT · C3=SYN · C4=NULL` — sem alteração dessa fronteira.
- `05-WL-KERNEL.md`: `emb_synth(label)` consulta a taxonomia da **condição** (C2 ou C3). Para NULL não há taxonomia a consultar; `p4_generate_embeddings.py` gera embeddings apenas para `{ECP, SYN, CAT}`.

**Conclusão:** a especificação congelada define NULL como **placeholder teórico não-operacional** no pipeline de grafos. Não há caminho de processamento previsto para ele. Não há erro na especificação — há uma fronteira de escopo deliberada.

### 2.2 Camada de implementação

- `graph_from_reconstruction.py:84-85`:
  ```python
  if ns == "NULL":
      raise ValueError("NAMESPACE_MIX")  # C4/T_NULL not processed by this parser
  ```
  O parser rejeita `NULL` com `NAMESPACE_MIX` porque, sem taxonomia fixa, **não há como validar `syn_category`** (o namespace declarado não corresponde a nenhum padrão de rótulo). Isso é coerente com a especificação, não uma divergência.

### 2.3 A incompatibilidade real (nível de desenho experimental)

- A governança indicou originalmente **A=NULL, B=SYN, C=NULL** (condições A/C sem taxonomia fixa — "cega pura" e "não-cega").
- Mas o pipeline exige um namespace processável para gerar o grafo → sem grafo não há S_struct → A/C teriam **zero observações**, violando a exigência de matriz completa (07 §8: ≥ 5 casos válidos; reconstrução por condição).
- O piloto resolveu **operacionalmente** (decisão GO-8B de 2026-08-13): **A=CAT, B=SYN, C=CAT**, preservando as 63 execuções.

**Causa raiz em uma frase:** existe um **gap de desenho** entre a intenção experimental de usar NULL nas condições A/C e a fronteira de processabilidade do pipeline (que só processa `ECP`/`CAT`/`SYN`). O parser está correto; a resolução foi uma decisão operacional ad hoc cuja **formalização definitiva** é a dívida D-02.

---

## 3. É Possível Alterar o Parser no GO-8C Para Aceitar NULL?

**Tecnicamente sim** (o GO-8C pode criar artefatos corrigidos próprios). **Porém, sem violar a especificação congelada: NÃO.** Aceitar NULL no parser significa **reverter uma decisão explícita e congelada** (04 §1.1, R5 M-1: "NULL não é processado"). Seria uma **mudança de desenho**, não uma correção de erro.

Mesmo no GO-8C, processar NULL exige definir, antes de qualquer linha de código:

1. **Sintaxe de rótulo sob NULL:** não existe. Seria necessário criar um padrão (ex.: `FREE-XXX` por reconstrução, ou `syn_category` livre/ausente). Isso **muda o schema** do `ReconstructionInput`.
2. **Fonte de embeddings (`emb_synth`) para NULL:** a taxonomia C2/C3 fornece os rótulos neutros; sob NULL não há taxonomia. Seria necessário embutir o rótulo livre diretamente no LM neutro (`all-MiniLM-L6-v2`), o que é possível, mas muda o significado de `S_sem`.
3. **Cardinalidade e comparabilidade:** C2 tem **no máximo 9** categorias (fixas); C3 tem **12** (fixas). Sob codificação livre (NULL), a cardinalidade é **ilimitada e dependente da granularidade do avaliador**. Isso introduz um **confundimento na DV primária S_struct** (o número de nós/arestas varia sistematicamente por condição, não pela manipulação experimental).

**Consequência crítica:** se A/C passarem a usar NULL com codificação livre, os resultados deixam de ser comparáveis às 63 execuções validadas do GO-8B (que usaram CAT) e o estudo confirmatório N=12 teria de ser tratado como **estudo novo**, com nova pré-registro e nova validação.

---

## 4. Opções de Solução

### Opção 1 — Reprojetar o parser para processar NULL (codificação livre) e usar NULL em A/C

**Descrição:** estender o schema e o parser para aceitar `taxonomy_namespace=NULL` com categorias livres por reconstrução (ex.: `FREE-XXX`); criar caminho de embeddings direto para rótulos livres; usar NULL nas condições A e C.

| Prós | Contras |
|---|---|
| Honra a intenção original de A/C "sem taxonomia fixa" (máxima fidelidade ao ideal de cegueira pura). | Contradiz a especificação congelada (04 §1.1) — é mudança de desenho, não correção. |
| Condição A vs C ganha contraste mais "puro". | Quebra comparabilidade com as 63 execuções validadas do GO-8B (A/C usaram CAT). |
| | **Confundimento na DV primária:** cardinalidade livre → S_struct influenciada pela granularidade do avaliador, não pela condição. |
| | Requer: novo schema, novo parser, novo caminho de embeddings, novos testes, revalidação completa. |
| | N=12 seria estudo novo (perde continuidade com N=7 e a análise de potência existente). |
| | Custo alto e risco metodológico elevado para o benefício incerto. |

### Opção 2 — Formalizar o uso de CAT para A/C como decisão operacional definitiva

**Descrição:** promover a decisão operacional do GO-8B (A=CAT, B=SYN, C=CAT) a **decisão de desenho definitiva no GO-8C**, documentando formalmente que C4/NULL é placeholder **não processável** (conforme a própria especificação 04 §1.1). Sem mudança no parser.

| Prós | Contras |
|---|---|
| Consistente com a especificação congelada: 04 §1.1 já declara NULL não processável — a formalização respeita essa fronteira em vez de violá-la. | A/C ficam com codificação por taxonomia fixa (CAT) em vez de codificação livre — o ideal de "nenhuma taxonomia" não é realizado. |
| **Cegueira preservada:** `CAT-XX` são rótulos permutados opacos (02 §3); o avaliador não conhece a correspondência com ECP. A manipulação cega permanece íntegra. | Exige documentar explicitamente a fronteira (aceitação de limitação metodológica). |
| **Continuidade total:** 63 resultados validados e o plano N=12 permanecem comparáveis; análise de potência (06 §5) inalterada. | A decisão precisa ser registrada formalmente (novo Decision Record GO-8C + nota no artefato corrigido). |
| **Zero risco no parser:** nenhuma mudança em `graph_from_reconstruction.py`; GO-8B intacto. | |
| Custo mínimo e imediato; desbloqueia D-03 e D-04. | |

### Opção 3 — Híbrida: formalizar CAT para A/C agora + registrar sonda de viabilidade para NULL (futuro)

**Descrição:** adotar a **Opção 2** como resolução definitiva da D-02 (continuidade para N=12) e, em paralelo, registrar como **linha de pesquisa futura (fora de N=12)** uma sonda de viabilidade para a condição NULL/codificação livre — avaliando confundimento de cardinalidade, pipeline de embeddings livres e pré-registro próprio.

| Prós | Contras |
|---|---|
| Resolve a dívida sem risco e sem bloquear N=12. | A sonda é trabalho adicional (fora do escopo N=12). |
| Preserva o espaço de design: NULL continua documentado como evolução possível, avaliada com rigor. | O ideal de "cegueira pura sem taxonomia" permanece adiado. |
| Dá à governança decisão explícita e informada sobre quando/por que mudar para NULL. | |

**Observação (variante 3b):** uma alternativa intermediária de NULL seria usar um **conjunto de rótulos neutros fixos mas não-ECP** (ex.: `NULL-XX` dedicados) — porém isso é funcionalmente equivalente a CAT (taxonomia fixa opaca) e não traria o ganho da codificação livre, apenas acrescentaria complexidade. Não recomendado.

---

## 5. Recomendação

**Recomendação: Opção 2** (formalizar `A=CAT, B=SYN, C=CAT` como decisão de desenho definitiva do GO-8C), com registro da **Opção 3 como item de roadmap** (sonda de viabilidade de NULL para ciclo futuro).

**Fundamentação:**

1. **O parser não está errado.** A especificação congelada declara NULL não processável (04 §1.1). A "correção" de D-02 não é técnica — é de **governança/documentação**: transformar uma decisão operacional ad hoc em decisão de desenho formal.
2. **A cegueira não é comprometida.** CAT-XX são rótulos permutados opacos; usá-los em A/C não vaza semântica ECP. A manipulação A/B/C da pré-registro (08 §5: B>A, C>A, C≥B) permanece testável exatamente como pré-registrada.
3. **A continuidade é decisiva para D-04 (N=12).** As 63 execuções validadas usaram CAT/SYN/CAT; N=12 só é comparável mantendo o mesmo mapeamento. Alterar para NULL implicaria descartar a comparabilidade e re-executar potência/pré-registro.
4. **Custo-benefício:** Opção 1 tem custo alto (parser, schema, embeddings, testes) e risco metodológico (confundimento de cardinalidade em S_struct) com benefício incerto; Opção 2 resolve a dívida com custo mínimo e zero risco.
5. **Coerência com o papel do GO-8C:** o GO-8C corrige dívidas e prepara N=12. A Opção 2 desbloqueia D-03 (NT-05) e D-04 (N=12) imediatamente.

---

## 6. Impacto nos Artefatos e Testes

### Se aprovada a Opção 2

| Artefato | Impacto |
|---|---|
| `graph_from_reconstruction.py` (GO-8B) | **Nenhum** — intacto (regra de imutabilidade). |
| `C2_PERMUTATION.yaml/.json` (GO-8C/scripts) | Nenhuma mudança estrutural; os namespaces C1–C4 já constam. Pode-se adicionar campo documental `namespace_operacional: {A: CAT, B: SYN, C: CAT}` + nota sobre C4/NULL. |
| `03-SYNTHETIC-TAXONOMY-C3.md` (GO-8B) | Nenhum (referência). Sem cópia corrigida necessária. |
| `04-GRAPH-FROM-RECONSTRUCTION.md` (GO-8B) | Nenhum. No GO-8C, registrar a fronteira em nota própria (não reescrever o congelado). |
| Testes GFR (T-GFR-14..21) | **Inalterados** — T-GFR-18 continua PASS (NULL rejeitado **por desenho**, não por falha). |
| Novos testes GO-8C (D-02) | **T-D-02-01:** mapeamento operacional `A=CAT, B=SYN, C=CAT` presente no artefato operacional GO-8C (YAML). **T-D-02-02:** `NULL` continua rejeitado pelo parser (regressão documental) — espelha T-GFR-18 sem alterá-lo. **T-D-02-03:** CAT continua processável para A/C (grafo construído, rótulos `CAT-XX`) — espelha T-GFR-15. |
| D-04 (N=12) | Namespace congelado em `A=CAT, B=SYN, C=CAT`; análise de potência e pré-registro inalterados. |

### Se aprovada a Opção 1 (para contraste)

| Artefato | Impacto |
|---|---|
| Schema `ReconstructionInput` | Novo padrão de `syn_category` para NULL (ex.: `FREE-XXX` ou livre). |
| `graph_from_reconstruction.py` (cópia GO-8C) | Novo ramo `ns == "NULL"` (substitui `raise NAMESPACE_MIX`). |
| `wl_kernel.py` / `p4_generate_embeddings.py` (cópia GO-8C) | Caminho de embeddings para rótulos livres; namespace NULL adicionado. |
| T-GFR-18 (cópia GO-8C) | Semântica invertida (NULL agora processado) — nova suíte e revalidação. |
| Resultados piloto GO-8B | **Incomparáveis** (A/C mudam de CAT para NULL) — N=12 vira estudo novo. |
| C3_TAXONOMY / C2_PERMUTATION | Sem impacto direto, mas a comparabilidade do design é afetada. |

---

## 7. Impacto no Estudo Confirmatório N=12 (D-04)

- **Opção 2:** N=12 executa com `A=CAT, B=SYN, C=CAT` — idêntico ao N=7 piloto. Continuidade total: mesmos namespaces, mesma DV (S_struct), mesma análise (Friedman + pós-hoc), mesma potência (≥ 0.80 com N=12, 06 §5). **Caminho mais curto e mais limpo para D-04.**
- **Opção 1:** A/C mudariam para NULL/codificação livre → N=12 não comparável com N=7. Exigiria: novo pré-registro, nova análise de potência (cardinalidade livre muda o modelo), nova validação — e o resultado N=12 não acumularia com N=7. Atraso e custo adicionais sem ganho claro.
- **Opção 3:** N=12 segue a Opção 2; a sonda NULL seria estudo paralelo, sem contaminar a análise confirmatória.

---

## 8. Próximos Passos (se aprovada a Opção 2)

1. **Decisão de governança GO-8C** — registrar `decisions/D-02-C4-NULL-DECISION.md` (DECIDED, Opção 2).
2. **Artefato de desenho GO-8C** — criar nota/documento de fronteira de namespace (ex.: `04-GRAPH-FROM-RECONSTRUCTION-CORRECTED.md` ou apêndice) declarando: C4/NULL = placeholder não processável (conforme 04 §1.1 congelado); operacional A=CAT / B=SYN / C=CAT; justificativa formal.
3. **Artefato operacional GO-8C** — atualizar `C2_PERMUTATION.yaml/.json` (GO-8C) com `namespace_operacional` e nota sobre NULL.
4. **Testes GO-8C** — criar `p_d02_namespace_test.py` com T-D-02-01..03 (mapeamento operacional, regressão NULL rejeitado, CAT processável) e executar (ALL PASS).
5. **Registrar validação** em `decisions/D-02-C4-NULL-VALIDATION.md` e atualizar `TODO-GO-8C.md` (D-02 → DONE) e `ACTION-REGISTER.md`.
6. **Próxima dívida:** D-03 (NT-05) e depois D-04 (N=12) com namespace congelado A=CAT/B=SYN/C=CAT.

---

## 9. Referências

- `experiments/validation/GO-8B/04-GRAPH-FROM-RECONSTRUCTION.md` §1.1, §2.1, §3.2, T-GFR-18
- `scripts/go8b/operational/graph_from_reconstruction.py:84-85`
- `experiments/validation/GO-8B/decisions/NAMESPACE-OPERATIONAL-DECISION.md`
- `experiments/validation/GO-8B/02-C2-PERMUTATION.md` §1/§8 · `03-SYNTHETIC-TAXONOMY-C3.md` §1
- `experiments/validation/GO-8B/05-WL-KERNEL.md` §4.1 · `06-STATISTICAL-PROTOCOL.md` · `07-FAILURE-CRITERIA.md` FR-03/§8 · `08-PRE-REGISTRATION.md` §3.5/§5
- `scripts/go8b/operational/p3_tests_gfr.py` · `p4_generate_embeddings.py:56` · `wl_kernel.py`
- Hash do manifesto GO-8B (referência histórica): `c55799d895a4f73888713a8538c6b9a6c5df1d7cde71c88141e16b9e9b216636`

---

**Fim da proposta. Nenhuma implementação executada. Nenhum arquivo do GO-8B alterado. Nenhum Lock gerado.**
