# D-01 — AUDITORIA DA MÉTRICA S_struct (VIÉS ESTRUTURAL)

**Ciclo:** GO-8D (DIAGNÓSTICO) — dívida D-01
**Status do ciclo:** GO-8C **CLOSED** · GO-8D **NOT YET OPENED**
**Fase:** DIAGNÓSTICO DE MÉTRICA (pré-abertura formal)
**Data:** 2026-08-14
**Escopo:** Auditoria de viés estrutural de `S_struct` (DV confirmatória do GO-8C)
**Executor:** Governança (auditoria de dados/artefatos congelados — somente leitura)

---

## 0. Compliance com as restrições

| Restrição | Cumprida |
|---|---|
| NÃO abrir formalmente o GO-8D | ✔ (ciclo permanece NOT YET OPENED) |
| NÃO criar novos arquivos de governança (exceto este relatório) | ✔ (único arquivo gravado = este relatório) |
| NÃO alterar artefatos GO-8B/GO-8C | ✔ (nenhum artefato existente modificado) |
| NÃO coletar novos dados | ✔ (apenas leitura/reprodução sobre dados existentes) |
| NÃO executar novo experimento | ✔ (reprodução diagnóstica do pipeline congelado, sem novos dados) |
| NÃO modificar o pipeline | ✔ (`scripts/go8b/operational/*` intactos, importados somente-leitura) |

Reprodução diagnóstica executada com os módulos congelados do GO-8B
(`pilot_engine.py`, `wl_kernel.py`, `graph_from_reconstruction.py`, `C3_TAXONOMY.yaml`,
`C2_PERMUTATION.yaml`, `EMBEDDINGS.npy`) e os artefatos do GO-8C
(`pilot_results_n12.csv`, `STATISTICAL-REPORT-N12.md`, `FINAL-PROJECT-REPORT-GO-8C.md`,
`study-input/`, `scripts/C3_TAXONOMY.yaml`). Scripts de diagnóstico temporários em
`%TEMP%\opencode\`, fora do repositório.

---

## 1. Resumo executivo

**S_struct não é uma medida de similaridade de conteúdo ao ECP.** A implementação congelada
(`wl_kernel.py:30`) **anonimiza todos os rótulos** dos nós reconstruídos para `"neutral"`
antes do kernel WL (h=3) e compara o histograma de labels WL resultante com o grafo ECP fixo
(de 9 nós em cadeia). Como os labels WL hasheados dos grafos reconstruídos **nunca coincidem**
com os labels WL da cadeia ECP (colisão SHA-256 ≈ 0), a única sobreposição real entre os dois
histogramas é o componente `"neutral"` da iteração 0, cuja massa é **o número de nós** (n² no
produto interno). O resultado é que:

> **S_struct ≈ n² / √( (n² + 3n) · 176 )** para grafos genéricos de n nós (labels WL todos
> distintos, sem colisão com ECP), onde **176 = ‖hist(ECP)‖²** (constante fixa).

Esse baseline por contagem de nós reproduz **bit a bit** os valores observados:
- **S_base(9) = 0.5875120888504802** — idêntico para todos os 5 BIPs da condição A do
  piloto GO-8B (BIP-001, 002, 003, 004, 006) e para 6 das 12 células A do N=12
  (BIP-001/002/003/004/006/010). **Este é o mecanismo das "duplicações" 0.5875.**
- 13 das 36 células do N=12 coincidem com S_base(nós) a 4 casas (resíduo ≈ 0).

Consequências:
1. **Sensibilidade baixíssima a conteúdo**: BIPs com 51 vs 115 arestas (BIP-001-A vs BIP-002-A)
   produzem **exatamente** o mesmo valor. A condição A tem apenas **5 valores distintos em 12 células**
   (mediana 0.5875 = S_base(9)).
2. **A anonimização uniforme elimina todo o sinal de rótulo/categoria**; o conteúdo só entra
   indiretamente, via quantas categorias foram usadas (contagem de nós) e via degenerescência WL
   (repetição de labels por topologia), não via qual categoria/qual semântica.
3. **A topologia é amplamente determinada pelo parser**: as arestas `follows` (sequência temporal
   `ENT-i → ENT-i+1`, artefato de parser, não semântica) são dominantes (37–55 das arestas por
   célula) e as arestas `relates` dependem apenas de um limiar cru de co-ocorrência de ≥2 termos-chave.
   O teste de backbone (BIP-001-A) mostra não-monotonicidade: `full=0.587512`, `follows-only=0.582147`,
   `relates-only=0.635380` — remover arestas pode **aumentar** a pontuação.
4. **Seeds são vestigiais** para esta DV: as 3 seeds por célula produzem saídas **bit-idênticas**
   (o valor da seed nunca entra no cálculo). As 108 linhas do N=12 contêm apenas **36 valores únicos**.

**Achado adicional (governança):** a condição B do N=12 **não é reproduzível** com o engine
congelado atual **sem injeção da taxonomia**. A execução do GO-8C usou a taxonomia **corrigida**
`C3_TAXONOMY.yaml` (decision D-03.7: definições de SYN-001 e SYN-012 alteradas), mas o engine
congelado lê por padrão a versão **não corrigida** de `scripts/go8b/operational/C3_TAXONOMY.yaml`.
Ao injetar a versão corrigida, reproduzem-se **7/7 células B** do CSV N=12 exatamente
(BIP-001..007, incluindo BIP-007-B = 10 nós/84 arestas/0.5950). **Não há inconsistência interna
de execução no GO-8C**: o N=12 usou a corrigida de forma uniforme; a lacuna é de
**rastreabilidade** (o engine congelado não registra qual taxonomia foi usada).

---

## 2. Método da auditoria

1. Leitura dos artefatos congelados: CSV N=12, relatório estatístico, relatório final GO-8C,
   Lock manifest, `pilot_results.csv` do GO-8B, engine/pipeline congelado.
2. Reprodução da métrica sobre os dados do GO-8B (21 células, BIP-001..007) **com o engine
   congelado**: 21/21 células **idênticas** ao `pilot-output/pilot_results.csv` do GO-8B
   (validação do método de reprodução).
3. Reprodução da condição B do N=12 com a taxonomia corrigida (D-03.7): 7/7 células B idênticas
   ao CSV N=12 (BIP-001..007), confirmando o uso uniforme da corrigida no GO-8C (ver §1/§4-E5).
4. Decomposição do kernel WL: impressão dos histogramas WL por célula, comparação com o
   histograma ECP, derivação da fórmula S_base(n) e verificação da igualdade bit a bit.
5. Testes de sensibilidade dirigida: baseline por contagem de nós; ablação follows/relates;
   contagem de valores distintos; verificação do caráter vestigial das seeds.

---

## 3. Mecanismo do platô 0.5875 (duplicações dentro da condição A)

### 3.1 Por que o valor se repete

No kernel WL congelado (`wl_kernel.py:21-56`):
- Todos os nós do grafo reconstruído recebem o rótulo `"neutral"` (`wl_kernel.py:30`).
- 4 iterações (h=3) acumulam `hist_all`: iteração 0 ⇒ n ocorrências de `"neutral"`;
  iterações 1..3 ⇒ 3n labels hasheados.
- O grafo ECP (9 nós, cadeia) tem histograma fixo: `{"neutral": 9, ...15 labels hasheados...}`
  com ‖hist(ECP)‖² = 176.

Para um grafo reconstruído com n nós cujos labels WL são **todos distintos entre si** e
**não colidem** com os labels da cadeia ECP (caso típico dos grafos colapsados de 9 nós),
o produto interno é **apenas n²** (sobreposição exclusiva em `"neutral"`):
‖v_rec‖² = n² + 3n (9² + 27 = 108 para n=9). Portanto:

**cos = n² / √((n²+3n) · 176)**, com valores: n=8 → 0.514259 · n=9 → **0.587512** ·
n=10 → 0.661107 · n=11 → 0.734968 · n=12 → 0.809040.

Verificação empírica: `cos` calculado em precisão total é **0.5875120888504802** (bit a bit
idêntico) para BIP-001-A, BIP-002-A, BIP-003-A, BIP-004-A e BIP-006-A, apesar de arestas de
51 a 115. Os histogramas WL dessas células são **diferentes entre si**, mas todos têm a mesma
estrutura de massa (9 `"neutral"` + 27 labels únicos, nenhum compartilhado com o ECP), de modo
que o cosseno colapsa ao mesmo valor.

### 3.2 Não é um bug de dados

Não se trata de linhas duplicadas no CSV nem de erro de agregação: os grafos são distintos
(histogramas diferentes, arestas diferentes). É **degenerescência da métrica**: o valor
0.5875 é o *baseline* de qualquer grafo de 9 nós "genérico" segundo esta definição de kernel.
Células acima do baseline (ex.: BIP-005-A=0.6828, BIP-007-A=0.6383) correspondem a grafos com
**degenerescência WL** (labels repetidos ⇒ ‖v_rec‖² < n²+3n), não a maior fidelidade semântica.

---

## 4. Evidências de viés estrutural

### E1 — A anonimização uniforme elimina o sinal semântico (S_base)

`wl_kernel.py:30` (`labels = {n: "neutral" for n in nodes}`) descarta **toda** a informação de
rótulo dos nós reconstruídos (CAT-xx / SYN-xx). Como a sobreposição com o ECP se reduz ao
componente `"neutral"` (contagem de nós), a métrica **não mede "o quanto o grafo reconstruído
se parece com o ECP"** em termos de tipos de categoria — mede basicamente contagem de nós +
degenerescência topológica. A correlação de S_struct com o número de nós é 0.346 (todas as 36
células); 13/36 células coincidem com S_base(nós) a 4 casas (resíduo ≈ 0).

### E2 — Sensibilidade insuficiente a diferenças de conteúdo

- Condição A do N=12: **5 valores distintos em 12 células**; mediana = 0.5875 = S_base(9).
- Condição B: 9 valores distintos; mediana 0.6348; nós 8–11.
- Condição C: 8 valores distintos; mediana 0.5821; nós 5–9.
- Duas células com a **mesma** contagem de nós mas conteúdos muito diferentes podem dar o mesmo
  valor (BIP-001-A, 51 arestas, vs BIP-002-A, 115 arestas ⇒ ambos 0.5875).
- O teste de backbone (BIP-001-A) evidencia não-monotonicidade e dominância do parser:
  `full (51 arestas) = 0.587512` · `follows-only (37) = 0.582147` · `relates-only (14) = 0.635380`.
  Remover arestas **aumenta** a pontuação, o que é incompatível com uma leitura de "fidelidade".

### E3 — A topologia é determinada pelo parser + pelo binning da taxonomia, não pelo conteúdo

- As arestas `follows` (sequência temporal de unidades) são construídas **sem nenhum conteúdo**
  (`pilot_engine.py:260-268`) e dominam a adjacência após o colapso por categoria.
- As arestas `relates` dependem de co-ocorrência bruta de ≥2 tokens-chave (`fact_tokens`),
  um bag-of-words sem relações semânticas tipadas.
- O colapso em nós é dado pelo **número de slots da taxonomia**: A/C usam 9 slots CAT
  (grafos tipicamente com 8–9 nós), B usa 12 slots SYN (grafos com 8–11 nós). A granularidade
  da taxonomia **altera diretamente o baseline por contagem de nós** e, portanto, S_struct.

### E4 — Seeds vestigiais (sem variação amostral)

O valor da seed nunca entra no cálculo (passado como metadado apenas); `text_emb`, classificação
e construção de grafo são determinísticos. As 3 seeds de cada célula produzem **exatamente** o
mesmo `s_struct`/`s_sem`. As 108 linhas do N=12 contêm 36 valores únicos. A "mediana das 3 seeds"
é o valor único determinístico — **não há re-amostragem**; as 108 execuções não acrescentam
variância amostral para esta DV. (Não é erro inferencial — a unidade de análise é o caso/BIP —
mas enfraquece a interpretação de "3 seeds = robustez".)

### E5 — Rastreabilidade da taxonomia da condição B comprometida (achado de governança)

O engine congelado lê `scripts/go8b/operational/C3_TAXONOMY.yaml` (hardcoded). A execução do
GO-8C usou a taxonomia **corrigida** `experiments/validation/GO-8C/scripts/C3_TAXONOMY.yaml`
(D-03.7), que difere nas **definições** de SYN-001 ("Atividade elementar" → "Procedimento basico")
e SYN-012 ("Ajuste local" → "Resposta do comportamento"). Como o classificador da condição B
atribui fatos a slots SYN por cosseno com as **definições**, essa mudança de 2 palavras
re-roteia fatos e altera materialmente S_struct (ver §5). Reproduzindo com a versão corrigida,
**7/7 células B** do N=12 são reproduzidas exatamente (BIP-001..007, inclusive BIP-007-B =
10 nós/84 arestas/0.5950). **Não há inconsistência entre células**: a execução do N=12 usou a
corrigida de forma uniforme; o problema é que o engine congelado não registra a taxonomia usada
por execução, criando uma lacuna de rastreabilidade (fechar em D-03).

---

## 5. Sensibilidade da condição B à taxonomia C3 (D-03.7)

Impacto de trocar apenas 2 definições (frozen → corrigida) nos 7 BIPs reexecutados
(reprodução com engine congelado + taxonomia):

| BIP | S_struct frozen | S_struct corrigida | nós/arestas frozen | nós/arestas corrigida | CSV N=12 |
|---|---|---|---|---|---|
| 001 | 0.5800 | **0.5866** | 8/36 | 8/40 | 0.5866 ✔ corrigida |
| 002 | 0.5905 | **0.6439** | 10/100 | 11/101 | 0.6439 ✔ corrigida |
| 003 | 0.5950 | **0.5950** | 10/80 | 10/87 | 0.5950 ✔ corrigida |
| 004 | 0.7500 | **0.7081** | 9/30 | 8/29 | 0.7081 ✔ corrigida |
| 005 | 0.5721 | **0.6833** | 8/36 | 8/33 | 0.6833 ✔ corrigida |
| 006 | 0.6364 | **0.6820** | 10/70 | 11/73 | 0.6820 ✔ corrigida |
| 007 | 0.5875 | 0.5950 | 9/78 | 10/84 | **0.5950 ✔ corrigida** |

Evidências:
- **A métrica S_struct é altamente sensível à redação das definições da taxonomia** (não ao
  conteúdo dos materiais): a mudança de 2 palavras move células B em até ~0.11 (BIP-005).
- **A execução N=12 usou a taxonomia corrigida de forma uniforme** na condição B (7/7 células
  reproduzidas exatamente; CSV BIP-007-B = 10/84/0.5950 = corrigida). O engine congelado
  commitado, hoje, **não** reproduz o CSV N=12 na condição B **sem injeção** da taxonomia
  corrigida (default = congelada) — lacuna de rastreabilidade, não inconsistência de execução.
- A validade da inferência A vs B depende, portanto, de qual versão de taxonomia se assume.

---

## 6. Impacto potencial sobre os resultados A vs B (e B vs C)

1. **Confundimento por granularidade da taxonomia.** A mediana de A = 0.5875 é **exatamente**
   S_base(9) (grafos de 9 nós). A condição B, com taxonomia de 12 slots, produz grafos com 8–11
   nós e maior diversidade topológica, elevando a pontuação (mediana 0.6348; células 10–11 nós
   em S_base(10)=0.661 / S_base(11)=0.735). Parte do "ganho" de B é um **artefato mecânico** de
   ter mais slots (mais nós possíveis), não uma maior fidelidade estrutural validada.
2. **O sinal de "fidelidade" não é medido.** Como dot(rec, ECP) ≈ n² para a maioria das células,
   S_struct não consegue atestar que B "se parece mais com o ECP" do que A. A direção B>A
   (r_rb=0.667, p=0.0537) e a robustez do Friedman (p=0.0075; sensibilidades p<0.05) atestam
   diferenças entre **distribuições de S_struct**, não entre **fidelidades estruturais**.
3. **B vs C** é ainda mais confundido: além da granularidade (12 vs 9 slots), as condições usam
   **inputs diferentes** (atomic facts vs narrativa integral) e C possui células com grafos densos
   pequenos (ex.: BIP-011-C, 5 nós/26 arestas, S=0.6048 vs baseline 0.298) cuja degenerescência WL
   infla o escore — um fator não relacionado à estrutura ECP.
4. **Conclusão da auditoria:** o viés estrutural de S_struct é **material** para a comparação
   A vs B. Os achados inferenciais do GO-8C (Friedman significativo, B>C pós-Holm) permanecem
   descritivamente válidos sobre a métrica, mas **não devem ser interpretados como evidência de
   que a taxonomia C3 produz reconstruções estruturalmente mais fiéis ao ECP**, porque a métrica
   não mede fidelidade ao ECP — mede contagem de nós + degenerescência topológica do grafo
   colapsado, fortemente influenciada pelo parser e pela granularidade da taxonomia.

---

## 7. Recomendação

### S_struct é robusta? **NÃO.** Precisa de correção. **SIM** (ou substituição).

S_struct, como implementada (anonimização uniforme + kernel WL não rotulado vs cadeia ECP fixa),
tem baixa sensibilidade, alta degenerescência (valores bit-idênticos para grafos distintos) e é
confundida por contagem de nós/granularidade de taxonomia/topologia de parser. **Não deve
permanecer como DV confirmatória única** sem correção. Correções mínimas possíveis (para
validação em D-02):
- **Não anonimizar** a informação de categoria no kernel (usar labels CAT/SYN no WL) — restaura o
  sinal de tipo; ou
- **Normalizar pelo baseline** por contagem de nós (S_struct − S_base(n), ou razão) para remover o
  confundimento mecânico de granularidade; ou
- **Trocar a referência:** comparar o grafo reconstruído à **própria taxonomia** da condição
  (C3-DAG para B, T_PERM para A/C) em vez de à cadeia ECP fixa — comparação justa dentro do
  namespace; e
- Adicionar diagnóstico obrigatório de sensibilidade por célula (nº de valores distintos,
  detecção de platô, correlação com nº de nós).

### Recomendações para D-02 (métricas alternativas) — prioridades

1. **Métrica sensível a rótulo/tipo** (kernel WL **rotulado** ou GED ponderada por categoria e
   tipo de relação) — ataca diretamente o viés E1/E2.
2. **S_sem refinada** (já alinhada por Hungarian; reforçar peso de nós com embeddings de rótulo
   e incluir labels de aresta) — é a direção mais promissora já presente no pipeline; e
   acrescentar métricas de **alinhamento fato→slot ECP** (fidelidade conceitual por fato),
   interpretáveis e independentes de topologia.
3. **Similaridade de grafo com features de nó** (embeddings por nó como atributos do kernel WL)
   — compatível com o pipeline congelado.
4. **Fidelidade por fato (fração de atomic facts atribuídos ao slot ECP "correto")** — DV
   direta, auditável, não sensível à contagem de nós.
   Regra de governança: toda candidata deve passar pelo mesmo diagnóstico de platô/valores
   distintos e por um teste de sensibilidade a conteúdo (swap de materiais) antes de ser
   aceita como DV confirmatória.

### Recomendações para D-03 (refinamento da taxonomia C3)

1. **Fixar a versão exata da taxonomia por execução** e registrar hash na saída; o engine não
   deve depender de um caminho global que possa divergir da versão lockada (o engine atual lê a
   versão não corrigida por padrão; o N=12 usou a corrigida via injeção — lacuna de
   rastreabilidade, não inconsistência de execução).
2. **Protocolo de estabilidade da taxonomia:** registrar distâncias de embedding das definições
   e verificar estabilidade da atribuição top-1 de cada fato sob perturbação de redação
   (ex.: re-avaliar o efeito D-03.7: 2 palavras moveram células B em até ~0.11).
3. **Remover o confundimento de granularidade** antes de interpretar ganhos de B: padronizar o
   nº de slots ou usar métrica normalizada por contagem de nós.
4. **Registrar a taxonomia efetivamente usada por execução** (hash do C3_TAXONOMY injetado) no
   output do engine — encerra a lacuna de rastreabilidade da condição B.

---

## 8. Confirmação de integridade

**Nenhum artefato existente foi alterado.** A auditoria foi exclusivamente de leitura:
- Arquivos do GO-8B/GO-8C lidos (CSVs, relatórios, Locks, pipeline, taxonomias, study-input);
- Reproduções executadas importando os módulos congelados sem escrita no repositório;
- Scripts de diagnóstico gravados apenas em `%TEMP%\opencode\`;
- **Único arquivo gravado neste repositório: `experiments/validation/GO-8C/decisions/D-01-SSTRUCT-AUDIT.md`** (este relatório).
- Nenhuma decisão de governança criada; Lock GO-8B/GO-8C intactos; GO-8D permanece NÃO aberto.

---

**Fim do relatório de diagnóstico D-01 (auditoria S_struct). 2026-08-14.**