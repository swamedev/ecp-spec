# MR-C7-PROTOCOLO-PREREGISTRO-V2

## Gate MR-C7 — Validade Discriminante de Valor
## Protocolo de Pré-Registro — V2 (CONGELADO ANTES DE QUALQUER EXECUÇÃO)

**Documento:** MR-C7-PROTOCOLO-PREREGISTRO-V2
**Versão:** 2 (segundo pré-registro do gate MR-C7)
**Fase:** Pré-registro (congelamento)
**Data:** 2026-08-19
**Status:** **CONGELADO — NÃO EXECUTADO.** Este documento congela o desenho, as estatísticas,
os limiares, os controles e as regras de decisão do gate **MR-C7** (tentativa v2) antes da
execução. Qualquer alteração posterior a este congelamento é **MUDANÇA DE ESPECIFICAÇÃO** e
exige nova decisão de governança (análogo a GOV-M-REDESIGN-01-GATE.md §7).
**Relação com o v1:** o v1 (`MR-C7-PROTOCOLO-PREREGISTRO.md`, hash
`380fc1281f685c9baaefa46c6ef69aaff2d88dc844ad37ae250a50ae90acefe3`) permanece como registro
histórico **INTOCADO** (nada foi alterado nos arquivos hash-locked de v1). Este documento herda
do v1 tudo o que não é explicitamente alterado nas seções §3.1, §7.4 e §7.5.1.
**Nomenclatura:** conforme `C-NOMENCLATURE-CORRECTION.md` (critérios com prefixo `MR-`; "C3" sem
prefixo reservado exclusivamente para a taxonomia experimental do GO-8D).

---

## 1. Objetivo

Testar a **validade discriminante de valor** da métrica `DV-REDESIGN` — ou seja, se a métrica
reconhece **valor semântico real** quando ele existe, permanece indiferente a **redundância**
correta e penaliza **informação incorreta/ruidosa**.

Motivação e fundamentação do gap: `GAP-VALIDADE-DISCRIMINANTE-MR-C7.md`. Os critérios
MR-C1–MR-C6 comprovaram neutralidade e robustez (incl. sensibilidade a degradação, MR-C5); o
eixo "valor" nunca foi testado, e a ausência desse teste torna o GO-8E não interpretável.

A v1 executou e resultou em **FAIL** (`MR-C7-REPORT.md`, histórico inalterado). A causa raiz
diagnosticada foi um **defeito de construção do gerador de casos** (colisão espúria de tokens no
caminho V2 — 83% da estrutura extra de V2 era espúria, não redundância genuína), não a métrica.
O gerador foi corrigido (`C-GENERATOR-FIX-V2-PARAPHRASE.md`) e a v2 pré-registra a re-execução do
gate com o gerador corrigido e uma revisão pontual do grafo de verdade de V2 (§7.4).

---

## 2. Hipótese do Gate

**H_MR-C7:** Para casos sintéticos/contrafactuais com 4 estados de informação adicional, a
métrica `DV-REDESIGN` reproduz a ordem esperada:

| Estado | Informação adicional | Valor esperado |
|--------|----------------------|----------------|
| **V0** | Nenhuma (baseline) | nenhum (referência) |
| **V1** | Correta e relevante | **positivo** (score sobe) |
| **V2** | Correta porém redundante | **~zero** (score não muda) |
| **V3** | Incorreta/ruidosa | **negativo** (score cai) |

**Ordem a ser distinguida:** `V1 > V2 ≈ V0 > V3`. A exigência é sobre a **ordem**, não sobre
magnitudes fixas. A equivalência V2 ≈ V0 é definida por banda de equivalência (δ_eq), ver §8.

---

## 3. Conjunto de Casos (congelado)

- **N = 24 casos-base sintéticos.** N é uma **decisão de desenho** (escala consistente com o
  programa: GO-8D N=12, GO-8D-NC N=30, Fase C 50 casos). **Nenhum cálculo de potência foi
  realizado** — cálculo de potência é proibido neste programa (SESSION-CLOSURE-2026-08-18).
- Geração **procedural e determinística** por gerador sintético com semente fixa
  (`seed_casegen = 20260818`), implementado em `measurement-redesign/phase4/scripts/generate_cases.py`
  (**corrigido — ver §3.1**) e **hash-locked ANTES de rodar** (o conjunto de casos fica
  totalmente determinado pela semente + script; não há seleção posterior de casos).
- **Perfil estrutural dos casos-base** (herdado de M-REDESIGN-01-SPEC-A.md §4.3): 8–10 fatos
  verdadeiros; grafo de verdade com 9–12 nós; densidade média de arestas ≈ 0.15 arestas/nó;
  distribuição de categorias compatível com o corpus.
- Cada caso-base tem um **grafo de verdade** G0 (fatos verdadeiros, relações verdadeiras,
  categorias intencionais) definido pelo gerador, **independente** de qualquer componente da
  métrica (ver §6.3 para a garantia de não-circularidade).
- **Namespace:** namespace procedural neutro e próprio do gate (categorias sintéticas
  `MRCAT-01…MRCAT-12`), **desacoplado do vocabulário ECP/C3** — ver §6.1 (desacoplamento de
  superfície). A reconstrução é gerada por um pipeline espelho do engine congelado, com o mesmo
  algoritmo (classificação por embedding, colapso por categoria, relações "follows"/"relates"),
  implementado nos scripts de fase 4 e hash-locked antes da execução.
- **Exclusões:** um caso é excluído (registrado) se algum estado não tiver pool consensual de
  fatos adicionais (ver §7.3). **Análise completa de casos:** exige ≥ 20 de 24 casos com os 4
  estados íntegros; abaixo disso o gate é **FAIL por dados insuficientes** (regra pré-congelada).

### 3.1 Correção do gerador aplicada à v2 (nova seção)

A v2 reutiliza o mesmo desenho procedural da v1 com **uma correção** aplicada ao gerador de
casos:

- **Correção:** `C-GENERATOR-FIX-V2-PARAPHRASE.md` (hash `d4a5b1b361137b42a7037ec885e8a217da99fd8bf8ef41cf767b9333ae8efa7b`).
  A função `make_v2_paraphrase` em `generate_cases.py` (Opção A) foi corrigida para que cada
  fato V2 contenha **apenas os tokens específicos da categoria/conteúdo** do fato-base
  parafraseado — sem o token temático do caso e sem os fillers compartilhados. Consequência
  verificada: a regra `relates` (engine intocado) só gera relação forte com o fato-base
  **pai** (overlap ≥ 2 apenas com o pai, **9/9**; overlap com qualquer outro fato-base = 0 em
  9/9), eliminando a colisão espúria que dominava a v1.
- **Novo hash do gerador:** `measurement-redesign/phase4/scripts/generate_cases.py` (corrigido) =
  `1340e462520ef73d1765cec34d7ad3b109b8876cc41a9459d7d2e68f0c108c9d`. (O hash v1
  `4fc038adc479f09b749c4b16d50651c20ba034349f9f3788326ea5a9f254541d` permanece como registro
  histórico.)
- **Regeneração (somente geração, sem métrica):**
  `measurement-redesign/phase4-v2/inputs/cases.yaml` (hash
  `479692d5d4a20a010fe0ac71e238c39f40ef990aa881b3e02555c80269ba7184`), gerado com o mesmo
  `seed_casegen = 20260818`.
- **Nota de rastreabilidade:** o `cases.yaml` da v2 foi gerado com o mesmo
  `seed_casegen = 20260818`; **V1/V3 idênticos à v1 (24/24 pools); apenas o caminho de geração
  V2 foi alterado.** Os demais scripts (`reconstruction.py`, `metric.py`, `labelers.py`,
  `analysis.py`) permanecem com os mesmos hashes da v1, exceto pela implementação da decisão de
  §7.4 (ver §7.5 para o hash-lock de execução).

---

## 4. Construção exata dos estados V0–V3 (congelada)

### 4.1 Princípio geral
Os 4 estados de cada caso compartilham o **mesmo caso-base**. A diferença entre estados é
**exclusivamente a adição de K_additional = 3 fatos adicionais** ao conjunto de fatos de entrada:

| Estado | Entrada | Fatos adicionais |
|--------|---------|------------------|
| **V0** | F_base | nenhum |
| **V1** | F_base + ΔV1 | 3 fatos **verdadeiros e relevantes** (consenso IA) |
| **V2** | F_base + ΔV2 | 3 fatos **verdadeiros e redundantes** (consenso IA) |
| **V3** | F_base + ΔV3 | 3 fatos **falsos ou irrelevantes/ruidosos** (consenso IA) |

### 4.2 Geração dos fatos candidatos (gerador, mecânica)
O gerador produz, por caso, um **pool de candidatos em pares estruturais casados**:
- **Par (V1, V3):** 1 candidato V1 (verdadeiro, relevante, estrutura aditiva) + 1 candidato V3
  (falso/irrelevante, **mesma pegada estrutural**: mesmo nº de novas entidades, nº similar de
  novas relações, mesma aridade). A pegada estrutural é casada por construção para controlar
  "mais valor" × "mais coisas" (§6.2).
- **Candidatos V2:** verdadeiros e **entailados** pelos fatos do caso-base (redundância por
  construção: paráfrases, subsumidos, instâncias já implicadas). O caminho de geração V2 foi
  corrigido para a v2 — ver §3.1.
- Volume: 6 pares (V1,V3) + 6 candidatos V2 por caso (18 candidatos/caso).

### 4.3 Rotulação por consenso de IA (ground truth do gate)
Para cada candidato, os três avaliadores de IA do programa (mesmos modelos da Fase C:
`claude-3-opus-20240229`, `gpt-4-2024-08-06`, `gemini-1.5-pro-20240801`) rotulam,
**independentemente e às cegas**, duas dimensões:
1. **Correção** (o conteúdo é verdadeiro conforme o caso-base?): `verdadeiro` / `falso`
2. **Relevância** (o conteúdo agrega informação ao núcleo estrutural do caso?): `relevante` / `redundante` / `irrelevante`

**Regra de consenso:** o rótulo de um candidato é adotado se **≥ 2 de 3** avaliadores concordam
em **ambas** as dimensões. Candidato sem consenso em qualquer dimensão é **excluído** do pool.

**Atribuição de estado (por consenso):**
| Pool | Condição (rótulo consensual) |
|------|------------------------------|
| ΔV1 | correção = `verdadeiro` **E** relevância = `relevante` |
| ΔV2 | correção = `verdadeiro` **E** relevância = `redundante` |
| ΔV3 | correção = `falso` **OU** relevância = `irrelevante` |

### 4.4 Seleção dos fatos adicionais (semente fixa)
De cada pool consensual, selecionar **exatamente 3** candidatos por **sorteio determinístico**
(`seed_draw = 20260818`), registrado no relatório. Cardinalidade controlada:
`|ΔV1| = |ΔV2| = |ΔV3| = 3` (igual em todos os estados e casos).
Se um pool tiver < 3 candidatos consensuais, o caso é excluído (ver §3).

### 4.5 Registro do consenso
Todas as rotulações são registradas em registro estruturado (modelo, versão, timestamp, prompt
exato, resposta bruta, decisão, justificativa) — mesmo padrão de `EVALUATION_REGISTRY.yaml`
(M-REDESIGN-01-SPEC-A.md §8.2).

---

## 5. Ground truth — declaração de limitação (congelada)

> **O ground truth do gate MR-C7 é por CONSENSO DE IA (Claude, GPT, Gemini), NÃO por avaliador
> humano independente.**
>
> A verdade factual objetiva (o que é verdadeiro/falso) é ancorada pelo gerador sintético; as
> decisões semânticas que definem os estados (relevante × redundante × irrelevante) são
> atribuídas por consenso entre modelos de IA. **Não há avaliador humano independente** para
> esse julgamento semântico.
>
> Consequência registrada com a mesma honestidade de P-0010 ("generalização proibida — limitado
> a este caso/avaliadores") e M-REDESIGN-01 Fase C ("avaliação por IA não é ground truth
> científico"): **a validade de constructo demonstrada pelo gate é condicional ao consenso de IA
> e não deve ser generalizada como verdade científica independente.** O PASS deste gate
> autoriza a métrica para uso confirmatório **condicionado** a essa limitação declarada.

### 5.1 Ressalva adicional — ground truth algorítmico (emenda aprovada em 2026-08-18)

Por determinação da governança, e dado que **nenhuma API de LLM externa é utilizável no ambiente
de execução** (ver `C-MODEL-SUBSTITUTION-ADDENDUM.md` §2), os rótulos V0–V3 são produzidos por
**consenso algorítmico determinístico de três sinais independentes** (relevância temática por
sobreposição de tokens, redundância lexical/entailment, novidade estrutural vs G0), com correção
ancorada ao gerador sintético. A regra ≥2/3 e todas as demais etapas do protocolo permanecem
inalteradas (desvio de método registrado como adendo controlado).

> **Este ground truth é AINDA MAIS FRACO que "consenso de IA": nenhum modelo de IA participa da
> rotulação** (nem os três nomeados no §4.3, nem quaisquer outros). Trata-se de **consenso
> algorítmico determinístico**.
>
> Portanto, **qualquer PASS obtido neste gate é PROVISÓRIO** e permanece pendente de
> **reverificação com modelos de IA reais** (três provedores distintos, versões correntes)
> **antes de qualquer decisão de governança sobre o GO-8E**. Um PASS algorítmico autoriza apenas
> a **continuidade do processo de mensuração**, não o uso confirmatório definitivo da métrica.

Nota: esta emenda é adição **interpretativa de validade** — não altera limiares, critérios de
decisão, estatística, casos, controles, referência, agregação ou regra de veto.

---

## 6. Controles obrigatórios (congelados)

### 6.1 Desacoplamento de superfície
O teste **não pode** premiar similaridade lexical nem densidade estrutural por si:
- **Não-lexical:** os estados são construídos por **adição semântica de fatos**, não por
  manipulação lexical do texto-base; o namespace é neutro (`MRCAT-*`), desacoplado do vocabulário
  ECP/C3; a premiação por similaridade lexical seria detectada como **falha de P3** (V2 ≈ V0,
  redundância com alta sobreposição lexical não pode ser premiada).
- **Não-estrutural:** a premiação por densidade estrutural seria detectada como **falha de
  P4/P5** (V3, com pegada estrutural casada à de V1, precisa pontuar **abaixo** de V0 e de V2).
- Operacionalização: os testes P1–P5 (§8) **são** o mecanismo de desacoplamento de superfície.

### 6.2 Cardinalidade controlada (V1 × V3)
`|ΔV1| = |ΔV3| = 3` em todos os casos (§4.4) **e** pegada estrutural casada por construção
(§4.2). Check de fidelidade no relatório: `média(|nós(V1) − nós(V3)|) ≤ 1.5` e
`média(|arestas(V1) − arestas(V3)|) ≤ 3.0`; por caso, `|nós(V1) − nós(V3)| ≤ 3`. Violação
**de qualquer** desses limites = **FAIL do gate por controle quebrado** (resultado
ininterpretável; não há re-seleção de casos).

### 6.3 Complexidade estrutural comparável (V1 × V3)
Garantida por construção (§4.2: pares com mesma aridade e nº de novas entidades) e verificada
pelo check de fidelidade §6.2. O objetivo é que qualquer diferença de score entre V1 e V3 seja
atribuível a **valor semântico**, não a tamanho/densidade.

### 6.4 Não-circularidade (independência rótulo ↔ métrica)
- Os rótulos V0–V3 de cada caso são fixados pelo **gerador + consenso de IA ANTES de qualquer
  cálculo de `DV-REDESIGN`** sobre esses casos.
- É **proibido** atribuir, revisar ou confirmar qualquer rótulo após a inspeção de valores de
  `DV-REDESIGN` (Veto V-B, §11).
- É **proibido** selecionar casos, fatos ou candidatos sabendo de antemão qual resultado
  favorecem.
- Não se usam casos reais escolhidos retrospectivamente ("sabemos que C3 ajuda aqui") — isso
  recriaria a circularidade que o redesign eliminou.
- **Decisão de §7.4 (estender a verdade de V2) é pré-registrada neste documento e NÃO pode ser
  reconsiderada após a inspeção de valores de `DV-REDESIGN`** (ver §7.4 e §15).

---

## 7. Métrica — definição herdada da Fase B/C (congelada)

### 7.1 Fórmula
```
DV_REDESIGN = (conf + ged_ref + div_metric) / 3
```
pesos **1:1:1**, agregação **aritmética** (M-REDESIGN-01-SPEC-A.md §5.3) — agregação primária.

### 7.2 Componentes (definições congeladas da especificação)
| Componente | Definição (fonte congelada) | Operacionalização no gate |
|------------|-----------------------------|---------------------------|
| **conf** | Média da qualidade de reconstrução = acurácia contra ground truth (§7.1) | F1 entre o grafo da reconstrução (nós = categorias; arestas = relações) e o **grafo de verdade do estado** (§7.4). F1 = média(F1 nós, F1 arestas) |
| **ged_ref** | `1 − GED(reconstrução, referência) / GED_max` (§2.2) | Similaridade estrutural do engine congelado (WL-kernel) contra a **referência DATA-DRIVEN** (§7.3); direção: maior = mais próximo |
| **div_metric** | Shannon / log(K), K = nº de categorias distintas (§7.3) | H/log(K); se K ≤ 1, div = 0 |
| **Normalização** | Componentes em [0,1] antes da agregação (§7.4) | Conforme especificação |

### 7.3 Referência GED — herança da Fase B
A Fase B selecionou a referência **DATA-DRIVEN** (grafo consenso MST, regra de desempate
congelada). Para o espaço sintético do gate, a referência DATA-DRIVEN é construída **pelo mesmo
método da Fase B** (consenso MST de reconstruções, ponderado por confiança) sobre as
**reconstruções V0 dos 24 casos-base**. Adaptação operacional declarada: a referência é
computada no espaço sintético (namespace neutro) porque a referência DATA-DRIVEN da Fase B
(vocabulário real ECP/C3) não é comparável a reconstruções sintéticas. **Método herdado; grafos
distintos por espaço; pré-registrado, não decidido após o resultado.**

### 7.4 Grafos de verdade por estado (para conf) — REVISADO PARA V2 (decisão pré-registrada)

| Estado | Grafo de verdade usado no F1 |
|--------|------------------------------|
| V0 | G0 (caso-base) |
| V1 | G0 estendido com os 3 fatos verdadeiros de ΔV1 |
| V2 | **G0 estendido com a estrutura genuinamente entailed pelos fatos de ΔV2** (arestas `relates` entre cada entidade ΔV2 e o fato-base **pai**; colapsam no self-loop `(cat_pai, cat_pai, relates)` quando ΔV2 é classificado na categoria do pai). A cadeia `follows` e as relações entre os próprios fatos ΔV2 **não** são entailed e permanecem fora da verdade |
| V3 | G0 (fatos de ΔV3 são falsos — não pertencem à verdade) |

**Decisão de desenho (tomada ANTES de qualquer execução — 2026-08-19).**

A v1 manteve a verdade de V2 = G0 com a justificativa de que estender G0→V2 seria **circular**,
pois validaria arestas NÃO entailed pelos fatos redundantes. Na v1, 83% da estrutura extra de V2
era **colisão espúria de tokens** (C-GENERATOR-FIX-V2-PARAPHRASE.md §1) — não redundância
genuína — e, por isso, estender a verdade teria validado arestas que o fato redundante não
entail.

Para a v2, com o gerador corrigido (§3.1), o resíduo estrutural de V2 (média ~4,9/caso em estado
completo) decompõe-se em:
- **self-loop do pai (~2,5/caso):** redundância **GENUÍNA** — o fato ΔV2 é paráfrase do
  fato-base pai e o overlap (≥ 2) ocorre **somente** com o pai (verificação funcional do fix:
  9/9). Essa aresta **É entailed** pelo fato redundante.
- **cadeia `follows` (~3/caso):** artefato **mecânico** do pipeline de reconstrução (relação de
  ordenação entre unidades consecutivas, gerada para qualquer adição de fatos) — **não é
  entailed** semanticamente pelo fato redundante.

**Decisão: estender a verdade de V2 com a estrutura genuinamente entailed (self-loop do pai),
mas NÃO com a cadeia `follows`.** Justificativa:
1. O princípio fixado na investigação da v1 (C-GENERATOR-FIX-V2-PARAPHRASE.md §1; MR-C7-REPORT
   v1 §10): estender a verdade é circular se validar arestas **NÃO entailed** pelo fato
   redundante. A condição que impedia a extensão na v1 (estrutura espúria) deixou de existir
   para o self-loop do pai na v2: a aresta `relates` ΔV2→pai é entailed por construção.
2. Sem a extensão, a métrica penalizaria a redundância genuína como erro de reconstrução —
   recriando, em menor magnitude, o mecanismo (a2) que na v1 colapsou `conf(V2)` em direção a
   `conf(V3)` e quebrou P3, P5 e a compliance.
3. A cadeia `follows` permanece **fora** da verdade porque é artefato de representação
   (ordenação), não semântica — incluí-la seria circular (validaria estrutura não entailed).
4. Consequência esperada (não decisória): a penalidade de `conf(V2)` fica restrita à cadeia
   `follows` (~3/caso) e a P3/P5 passam a testar se essa penalidade residual permanece dentro da
   banda δ_eq — exatamente o que o gate deve medir.
5. Operacionalização: a verdade de V2 é construída reconstruindo `(base_facts + ΔV2)` e retendo
   G0 **+** as arestas `relates` cujo endpoint é uma entidade ΔV2 e o outro é uma entidade base
   (a relação com o pai). São **excluídas** as arestas `follows` incidentes em entidades ΔV2 e
   as arestas `relates` entre duas entidades ΔV2. A implementação em script é hash-locked antes
   da execução (§7.5).

Esta decisão é um ajuste de **desenho da referência de verdade** (§7.4) tomado por pré-registro
antes de qualquer execução — **NÃO é um ajuste pós-resultado**. Nenhum limiar, estatística,
peso, caso ou regra de decisão foi alterado.

### 7.5 Execução das reconstruções
- Reconstruções geradas pelo pipeline espelho do engine congelado (§3), **determinístico**.
- 3 seeds determinísticos derivados de `seed_master = 20260818` (via procedimento do
  `generate_seeds.py` congelado), verificando **invariância a seed** (a saída do engine é
  determinística, como observado no CSV congelado do GO-8D-NC: linhas idênticas entre seeds).
  `conf` é a média dos 3 seeds conforme §7.1 da especificação; se a invariância falhar, a média
  ainda é aplicada e a não-invariância é reportada.
- **Análise por componente** (conf, ged_ref, div_metric separadamente) é **diagnóstica e não
  decisória** (não entra no PASS/FAIL).
- Para a v2, a decisão de §7.4 (verdade estendida de V2) é implementada nos scripts de
  execução, os quais são **hash-locked ANTES de rodar** (SHA-256 registrado antes de qualquer
  execução; §13). O pipeline de reconstrução em si permanece idêntico ao do v1; apenas a
  construção da verdade de V2 segue o §7.4 da v2.

#### 7.5.1 Distinção interpretativa de causa de FAIL (adendo da governança — 2026-08-18; estendido para a v2 em 2026-08-19)

Em caso de **MR-C7 = FAIL**, o relatório deve diagnosticar e declarar explicitamente qual das
três causas abaixo (ou combinação delas) explica o resultado, **antes** de qualquer recomendação
de redesenho:

> **(a) FAIL-tipo-A — falha do componente `conf`:** o componente `conf` isoladamente já não
> discrimina V1 de V3 acima do piso de efeito (§8.3) — indica problema real na medida de
> confiança de reconstrução.
>
> **(b) FAIL-tipo-B — diluição de agregação:** `conf` isoladamente discrimina V1 de V3 acima do
> piso de efeito, mas o composto (média 1:1:1 com `ged_ref` e/ou `div_metric`) cai abaixo do
> piso — indica que o **peso 1:1:1 está diluindo um sinal real**, não que os componentes
> individuais estão errados.
>
> **(c) FAIL-tipo-C — defeito de construção do gerador de casos:** a assimetria estrutural entre
> estados não reflete a propriedade semântica pretendida (valor/redundância/ruído), mas sim um
> artefato de como os candidatos são gerados (ex: colisão de token, template compartilhado).
> Diferente de A e B, este tipo exige correção no gerador (`generate_cases.py` ou `labelers.py`),
> não na métrica nem na agregação. **Já ocorreu uma vez nesta linha de investigação (v1 → v2)** —
> reportar explicitamente se há qualquer sinal residual desse tipo antes de aceitar um PASS/FAIL
> da v2 como definitivo.

A recomendação de "redesenhar o componente estrutural" (§14) só se aplica ao cenário (a). No
cenário (b), a recomendação correta é revisar o **esquema de agregação/pesos**, não os
componentes. No cenário (c), a recomendação correta é corrigir o **gerador de casos** (não a
métrica nem a agregação); a v2 já incorpora UMA correção dessa natureza
(`C-GENERATOR-FIX-V2-PARAPHRASE.md`), e qualquer sinal residual de tipo-C deve ser reportado
explicitamente antes de aceitar o resultado da v2 como definitivo.

Nota: este adendo é uma adição **interpretativa** sobre como ler um resultado ainda não
produzido. **Não altera** nenhum limiar, critério de decisão, estatística, caso ou controle já
congelado neste protocolo.

---

## 8. Estatística de teste e limiares (congelados)

### 8.1 Comparações primárias (N = 24 casos pareados)
| Par | Relação esperada | Teste | α |
|-----|------------------|-------|---|
| **P1** | V1 > V0 | Wilcoxon assinado unilateral (1 lado) | 0.05 |
| **P2** | V1 > V2 | Wilcoxon assinado unilateral (1 lado) | 0.05 |
| **P3** | V2 ≈ V0 | **TOST** (dois testes unilaterais) com δ_eq = 0.05 | 0.05 (cada lado) |
| **P4** | V3 < V0 | Wilcoxon assinado unilateral (1 lado) | 0.05 |
| **P5** | V3 < V2 | Wilcoxon assinado unilateral (1 lado) | 0.05 |

- **Controle de multiplicidade:** Holm-Bonferroni **dentro dos 4 testes direcionais**
  (P1, P2, P4, P5), família α = 0.05. P3 (equivalência) é avaliado **independentemente** a α=0.05.
- **N efetivo mínimo:** cada teste direcional exige ≥ 15 pares **não-empates** (≥ 62.5% de 24);
  abaixo disso o teste é **FAIL** (métrica sem resposta discriminativa suficiente).

### 8.2 Taxa de conformidade de ordem (compliance)
Para cada caso i (com os 4 estados íntegros), definir:
```
ord_i = 1  se TODAS:
  (a) DV_i(V1) ≥ DV_i(V0) − δ_eq
  (b) DV_i(V1) ≥ DV_i(V2) − δ_eq
  (c) |DV_i(V2) − DV_i(V0)| ≤ δ_eq
  (d) DV_i(V0) ≥ DV_i(V3) + δ_eq
  (e) DV_i(V2) ≥ DV_i(V3) + δ_eq
      senão ord_i = 0
```
`compliance_rate = média(ord_i)`.
**Exigência:** `compliance_rate ≥ 0.80` (≥ 20 de 24 casos — alinhado ao padrão de ≥80% do
programa, ver MR-C3/MR-C4).

### 8.3 Pisos de efeito (tamanho mínimo de efeito)
`δ_eq = 0.05` é a **banda de equivalência** (V2≈V0) e o **piso mínimo de efeito** direcional
(convenção Δ=0.05 do programa, ver TOST do GO-8D):
- `mediana(DV(V1) − DV(V0)) > δ_eq`
- `mediana(DV(V1) − DV(V2)) > δ_eq`
- `mediana(DV(V0) − DV(V3)) > δ_eq`
- `mediana(DV(V2) − DV(V3)) > δ_eq`

O ganho de valor e a perda por ruído precisam exceder a banda dentro da qual a redundância é
considerada equivalente — evita "significativo estatisticamente, porém sem efeito".

### 8.4 Regra de decisão — PASS/FAIL (congelada)
**MR-C7 = PASS** se e somente se **TODAS**:
1. P1, P2, P4, P5 PASS após Holm-Bonferroni;
2. P3 (TOST, δ_eq=0.05) PASS;
3. N efetivo ≥ 15 em cada teste direcional;
4. `compliance_rate ≥ 0.80`;
5. Pisos de efeito (§8.3) atendidos;
6. Check de fidelidade estrutural §6.2 atendido;
7. Nenhum veto (§11) acionado;
8. Nenhuma violação de procedimento (§10).

**Qualquer** condição não atendida ⇒ **MR-C7 = FAIL** (resultado válido e definitivo para este
pré-registro; ver §9).

---

## 9. Tratamento de resultado negativo (congelado)

- **MR-C7 FAIL é um resultado válido.** Não é reformulado como sucesso parcial nem "salvo" por
  ajuste pós-hoc de limiares, casos, pesos ou estatística.
- Recomendação documentada em caso de FAIL: **redesenhar o componente de diversidade/estrutura**
  (`div_metric` e/ou `ged_ref`, incluindo a escolha de referência GED) e submeter nova tentativa
  **após nova pré-registro**, nunca re-executar com limiares alterados.
- Se a causa do FAIL for **controle quebrado** (§6.2), **violação de procedimento** (§10) ou
  **defeito residual do gerador** (FAIL-tipo-C, §7.5.1c), o resultado é FAIL sem diagnóstico de
  métrica (não interpretável como falha da métrica); novo desenho (gerador e/ou métrica) é
  requerido.
- GO-8E permanece **NÃO AUTORIZADO** em qualquer cenário de FAIL.

---

## 10. Proibições absolutas (congeladas, herdadas da governança)

| Proibição | Sanção |
|-----------|--------|
| Alterar qualquer arquivo travado por hash | **INVALIDA** o gate |
| Escolher limiar depois de ver o resultado | **INVALIDA** o gate |
| Selecionar casos/fatos/candidatos sabendo o resultado que favorecem | **INVALIDA** o gate |
| Atribuir/revisar rótulos após inspeção de DV | **INVALIDA** o gate (Veto V-B) |
| Ajustar casos, pesos, estatística ou referência pós-hoc | **INVALIDA** o gate |
| Reconsiderar a decisão de §7.4 (verdade de V2) após inspeção de DV | **INVALIDA** o gate |
| Calcular potência estatística | **PROIBIDO** (fora de escopo deste gate) |
| Escrever pré-registro do GO-8E | **PROIBIDO** (fora de escopo deste gate) |
| Coletar BIPs novos | **PROIBIDO** (fora de escopo deste gate) |
| Abrir GO-8E | **PROIBIDO** (exige autorização separada) |

---

## 11. Regra de veto (congelada)

| Veto | Condição de acionamento | Consequência |
|------|-------------------------|--------------|
| **V-A — Cegueira ao valor** | Proporção de casos com `|DV(V1)−DV(V0)| ≤ δ_eq` **E** `|DV(V3)−DV(V0)| ≤ δ_eq` ≥ 50% | **FAIL imediato** (métrica indiferente a ganho e a perda) |
| **V-B — Integridade do rótulo** | Qualquer rótulo atribuído/revisado após inspeção de DV, desvio do protocolo de consenso, ou seleção por resultado esperado | **FAIL imediato** + reporte à governança |
| **V-C — Controle quebrado** | Check de fidelidade §6.2 violado | **FAIL imediato** (resultado ininterpretável) |

---

## 12. Piloto exploratório com casos reais (não decisório, congelado)

- Após o gate confirmatório sintético, **no máximo 5 casos reais** (BIPs do corpus existente)
  são selecionados por **sorteio determinístico** (semente fixa), **não** por resultado esperado.
- Para cada um, os rótulos V0–V3 são construídos pelo mesmo protocolo de consenso de IA (§4.3)
  e a métrica é aplicada.
- Esse piloto é **exclusivamente de face validity exploratória**: relatado em anexo separado do
  relatório, **nunca** utilizado como fundamento de PASS/FAIL. Se especialistas humanos
  estiverem disponíveis para esses casos, seus rótulos são registrados como complementares.
- Se o piloto não for executável (falta de material/rotulação), é omitido com nota.

---

## 13. Artefatos e relatório (congelados)

Execução em `measurement-redesign/phase4-v2/` (input `inputs/cases.yaml` já regenerado com o
gerador corrigido — §3.1):
- `scripts/` — scripts de geração, rotulação, reconstrução e análise; **hash-lock ANTES de
  rodar** (SHA-256 registrado antes de qualquer execução), incluindo a implementação da decisão
  de §7.4 (verdade de V2 estendida).
- `inputs/` — casos-base (v2), pools de candidatos, rótulos consensuais (registro completo).
- `outputs/`:
  - `MR-C7-REPORT-V2.md` — relatório final em texto (padrão PHASE-B-REPORT.md) com **hash
    SHA-256** registrado;
  - `MR-C7-REPORT-V2.json` — dados por caso, estatísticas por par, compliance, pisos, decisão,
    vetos;
  - `MR-C7-CASE-REGISTRY-V2.yaml` — casos, estados, rótulos, seeds, consenso (padrão
    EVALUATION_REGISTRY.yaml).

O relatório registra: dados brutos por estado; resultados P1–P5 (estatística e p-valores);
compliance_rate; pisos de efeito; check de fidelidade §6.2; verificação de invariância a seed;
decisão final (PASS/FAIL), vetos e diagnóstico de causa (§7.5.1, incluindo a verificação
explícita de sinal residual de FAIL-tipo-C). **Nenhum ajuste retroativo é permitido após a
execução.**

---

## 14. Consequências da decisão (congeladas)

| Decisão | Consequência |
|---------|--------------|
| **MR-C7 PASS** | Documentar que `DV-REDESIGN` está autorizada para **uso confirmatório** (com a limitação de ground truth por consenso de IA declarada). Preparar material para **decisão de governança sobre o DESENHO do GO-8E** (o desenho em si não é este gate; a execução do GO-8E continua exigindo autorização separada) |
| **MR-C7 FAIL** | Documentar como resultado válido. Recomendar **redesenho do componente de diversidade/estrutura** (causa A) e/ou revisão de **agregação/pesos** (causa B) e/ou **correção do gerador** (causa C) conforme diagnóstico de §7.5.1, antes de nova tentativa. **Não** tentar "salvar" a métrica atual. GO-8E permanece NÃO AUTORIZADO |

---

## 15. Declaração de congelamento

> Este protocolo congela, **antes de qualquer execução**: o conjunto de casos (geração procedural,
> N=24, semente `20260818`, gerador corrigido conforme §3.1), a construção exata de V0–V3 (K=3,
> pares estruturais casados, consenso de IA ≥2/3), a referência GED (DATA-DRIVEN por método,
> Fase B) e a agregação (aritmética 1:1:1, Fase B/C), a estatística de teste (P1–P5, Wilcoxon +
> TOST, Holm), os limiares (δ_eq = 0.05, α = 0.05, compliance ≥ 0.80, pisos de efeito, N efetivo
> ≥ 15), o tratamento de empates (§8), o tratamento de resultado negativo (§9), a regra de veto
> (§11), a **decisão de §7.4 (verdade de V2 estendida com a estrutura entailed — self-loop do
> pai — excluída a cadeia `follows`)** e as consequências da decisão (§14).
>
> **Nenhum arquivo travado por hash de v1 foi ou será alterado.** Todos os hashes da Seção de
> referências foram verificados antes deste congelamento. A decisão de §7.4 é **irrevogável
> após a inspeção de valores de `DV-REDESIGN`** (Veto V-B/V-C e §10).
>
> **Nenhuma execução ocorre até aprovação explícita da governança sobre este protocolo.**

---

## 16. Documentos de referência (hashes verificados em 2026-08-19)

| Documento | SHA-256 |
|-----------|---------|
| `M-REDESIGN-01-SPEC-A.md` | `e1fa24479636a02058b3107328320fadb3f74641e20649abd5f69484b2b18965` |
| `GOV-M-REDESIGN-01-GATE.md` | `ff1593d8f85fe8a5e41c2473f44af481477d03d4585c047f153001be6c19642c` |
| `MEASUREMENT-GATE-CONSOLIDATION.md` | `604f3e1aea453ca9673f0938732445709ffed684af399d00d431bfa235f4e1be` |
| `PHASE-B-REPORT.md` | `66aa2ecfcf709bb13836360ea45a98b86f935b30b2467515fc31893d33c38799` |
| `EVALUATION_SUMMARY.md` | `e4b1bd8c4a30da609b29cd2f22adf214026b3315c79b9c7861f90391b7ae97df` |
| `MEASUREMENT-REDESIGN-PROPOSAL.md` | `f32ef6b8b02408069461aae42b96482fe8f077e4a329d56a09945c5e92a3e486` |
| `FINAL-PROJECT-REPORT-GO-8D.md` | `4d40f5c5dee0146ff3e28bf63447503196515554643381a0be20e9a956c91e3e` |
| `C-NOMENCLATURE-CORRECTION.md` | `082e51cfe14d15b3255824c222cc8facea9acf4b22164928bdd4c9c09431eab5` |
| `GAP-VALIDADE-DISCRIMINANTE-MR-C7.md` | `052effb5ff94928a656a1d98f9ce41cdf520be1f7bc35ee7781b01d24c449f41` |
| `C-MODEL-SUBSTITUTION-ADDENDUM.md` | `4ce9fa87f0cd4fa6c0b33ffe2cc4ee5d27e3d998c142fce1c5ac60a9f13b4dc5` |
| `MR-C7-PROTOCOLO-PREREGISTRO.md` (v1, histórico) | `380fc1281f685c9baaefa46c6ef69aaff2d88dc844ad37ae250a50ae90acefe3` |
| `MR-C7-REPORT.md` (v1, histórico) | `registrado no relatório de execução v1` |
| `C-GENERATOR-FIX-V2-PARAPHRASE.md` | `d4a5b1b361137b42a7037ec885e8a217da99fd8bf8ef41cf767b9333ae8efa7b` |
| `measurement-redesign/phase4/scripts/generate_cases.py` (corrigido) | `1340e462520ef73d1765cec34d7ad3b109b8876cc41a9459d7d2e68f0c108c9d` |
| `measurement-redesign/phase4-v2/inputs/cases.yaml` (regenerado) | `479692d5d4a20a010fe0ac71e238c39f40ef990aa881b3e02555c80269ba7184` |
| Lock Manifest GO-8D-NC | `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058` |

---

**Assinatura:** Governança ECP
**Data:** 2026-08-19
**Status:** PRÉ-REGISTRO V2 CONGELADO — AGUARDANDO REVISÃO E APROVAÇÃO ANTES DA EXECUÇÃO