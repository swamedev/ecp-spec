# D-03 — DESIGN REVIEW (Revisão Formal de Desenho)

**Data:** 2026-08-14
**Ciclo:** GO-8D — DIAGNOSTIC PHASE · **GATE: REVISÃO DE DESENHO (design review)** — antes de avançar a D-07
**Tipo:** documento formal de revisão de desenho (não constitui decisão de governança)
**Base:** D-01 (`SSTRUCT-AUDIT.md`) · D-02 (`D-02-METRICS-ANALYSIS.md`) · D-03 (`D-03-PIPELINE-REDESIGN.md`)

**Escopo desta etapa:** revisar e consolidar o desenho proposto na D-03, comparar DV antiga vs nova,
apresentar evidências de resolução das degenerescências e as **opções de sequência** para a
governança decidir. **NÃO autoriza** pré-registro, recálculo de N, Lock, nem experimento.

---

## 1. Resumo executivo das mudanças propostas

O reprojeto (D-03) propõe cinco correções pontuais sobre o pipeline, todas **backward-compatible**
e **sem tocar GO-8B/GO-8C**:

| # | Componente | Correção | Artefato D-01/D-02 resolvido |
|---|---|---|---|
| P1 | `wl_kernel.py` | Variante **rotulada** do WL (`labels` opcional; usa categoria real quando disponível) | Anonimização uniforme (S_struct ≈ nº de nós) |
| P2 | Embeddings CAT | CAT-XX usa **definição neutra PT** (`CAT_NEUTRAL_DEFS`), não nome canônico ECP | Cosseno 1.0 fixo (D-02 M4 = 0.8333 constante) |
| P3 | Granularidade | Comparar contra a **taxonomia da condição** (cadeia T_PERM p/ A/C; DAG C3 corrigido p/ B), 9 vs 12 slots padronizados | Confundimento de granularidade (M1 anulou A/B/C) |
| P4 | Referência | Métrica estrutural usa **referência por condição** em vez da cadeia ECP fixa | CAT↔ECP dependente da bijectividade C2 |
| P5 | Rastreabilidade | Gravar `taxonomy_sha256` + `taxonomy_version` por execução | Lacuna do BIP-007-B (todas as 36 células = `5ba63db7…`) |

**Nova DV confirmatória:** `DV_confirm = (conf + ged_ref + ent) / 3`
- **conf** = confiança média do classificador (fidelidade por fato).
- **ged_ref** = GED ponderada **vs taxonomia da condição** (substituição de nós por cosseno de
  embeddings corrigidos; arestas dirigidas com peso 0.5; normalizada em [0,1]).
- **ent** = entropia de atribuição normalizada (Shannon / log nº slots da condição).

---

## 2. Comparação DV antiga (S_struct) vs DV nova (DV_confirm)

| Critério | **S_struct** (antiga) | **DV_confirm** (nova) |
|---|---|---|
| Definição | WL h=3 **anonimizado** (labels="neutral") vs cadeia ECP fixa de 9 nós | Média aritmética de conf (fidelidade) + GED vs taxonomia da condição + entropia normalizada |
| Valores distintos A | **5/12** (plató 0.5875) | **12/12** |
| Valores distintos B | 9/12 | **12/12** |
| Valores distintos C | 8/12 | **12/12** |
| Mediana A | 0.5875 (= S_base(9), mecânico) | 0.7134 |
| Mediana B | 0.6348 | 0.6220 |
| Mediana C | 0.5843 | 0.6843 |
| Friedman Q (A/B/C) | 9.50 | **18.50** |
| Correlação com nº de nós | **+0.346** | **+0.189** |
| Correlação com nº de nós (após correção M1) | **−0.897** (sobre-corrige) | — (já baixa) |
| Sensível a rótulo/categoria | ✖ (anonimizado) | ✅ (conf/ged_ref/ent usam categorias reais) |
| Referência padronizada por condição | ✖ (sempre ECP) | ✅ (T_PERM / DAG C3) |
| Interpretabilidade | Baixa (baseline mecânico domina) | Alta (3 componentes semânticos) |

**Mensagem central:** a S_struct separava A/B/C por um **artefato mecânico** (contagem de nós +
granularidade) — ao remover esse confundimento (D-02 M1), a separação desaparecia (Q=5.17, n.s.).
A DV_confirm produz separação **mais forte que a observada** (Q=18.50) e **sem** o confundimento,
com variação real e interpretável por célula (12/12 em todas as condições).

---

## 3. Evidências de que a nova DV resolve as degenerescências

1. **Fim do platô / colapso de valores.** S_struct tinha 5/12 valores distintos em A (5 BIPs
   bit-idênticos em 0.5875) e as 3 seeds eram vestigiais (108 linhas = 36 valores únicos). A
   DV_confirm tem **36/36 valores distintos** (12/12 por condição). Seeds continuam vestigiais
   (o valor da seed não entra no cálculo), mas agora **cada célula é única**, eliminando a
   duplicação observacional.
2. **Fim do confundimento por contagem de nós.** S_struct: corr(nós)=+0.346; sua correção linear
   (M1) sobre-corrigia (corr=−0.897). DV_confirm: corr(nós)=**+0.189** — residual pequeno, sem
   a relação forte nem a inversão.
3. **Fim do colapso dos embeddings CAT.** S_sem refinada era **constante 0.8333** para A/C
   (D-02 M4) porque `EMB_TABLE[("CAT",cat)]` = nome canônico ECP (cosseno 1.0). Com a correção
   P2, o GED vs ECP (que na D-02 parecia promissor, Q=18.00) cai para **Q=2.17 (n.s.)** — prova
   de que o ganho anterior era artefato; o componente estrutural robusto passa a ser o **GED vs
   taxonomia da condição** (Q=10.17, corr(nós)=−0.025).
4. **Fim do papel dominante do parser/anonimização.** O WL rotulado **sozinho** ainda degenera
   (A=2/12) por causa do colapso por categoria (P3); a DV_confirm não depende do WL: usa conf
   (fidelidade por fato), ged_ref (edição de grafo) e ent (distribuição) — todas sensíveis a
   rótulo e robustas ao parser de arestas.
5. **Robustez aos pesos do composto.** Variações razoáveis de pesos mantêm Q≥10.5 e ≥11/12 de
   valores distintos; o composto 1:1:1 é o ponto de máximo simples (Q=18.50).

---

## 4. Impacto no pré-registro e necessidade de novo Lock

**Impacto alto — a mudança de DV invalida o pré-registro do GO-8C** (`08-PRE-REGISTRATION-N12.md`):

1. **Novo pré-registro obrigatório (D-07):** definir
   - `DV_confirm = (conf + ged_ref + ent)/3` e pesos (proposto 1:1:1; congelar no pré-registro);
   - hipóteses: H₀ A vs B; H₀ B vs C (mesmas comparações do GO-8C);
   - plano inferencial: Friedman (df=2) → Wilcoxon pareado bilateral + Holm → r_rb / Cliff δ;
     bootstrap B=10.000; critério Go/No-Go ≥ 10/12;
   - **Δ para TOST (D-06)** — margem de equivalência formal, ainda não definida;
   - seeds: novo `seed_master` (não reutilizar o do GO-8C, que não é Locked).
2. **Recálculo de N (D-07):** efeito observado na simulação — mediana A=0.7134 vs B=0.6220,
   Δ≈0.09 na escala composta — para dimensionar N do próximo estudo.
3. **Novo Lock obrigatório:** engine modificado (wl_kernel rotulado, embeddings corrigidos,
   referência por condição, hash de taxonomia) ⇒ re-gerar manifest+record. **GO-8B e GO-8C
   permanecem CLOSED/LOCKED/FROZEN; o Lock do GO-8D é novo artefato.**
4. **Dados:** novo estudo roda sobre **os mesmos 12 BIPs existentes** (sem coleta) OU novos BIPs
   sob a mesma taxonomia corrigida — decisão da governança.

**Não autorizado nesta etapa:** pré-registro, recálculo de N, Lock do GO-8D, qualquer execução
experimental.

---

## 5. Opções de sequência para as próximas dívidas

A governança deve escolher a ordem entre D-04 (gate de parseabilidade), D-05 (gate semântico
híbrido), D-06 (definição de Δ para TOST) e D-07 (novo pré-registro + recálculo de N + Lock).

### Opção A — Aprovar o desenho e seguir direto para D-07 (recálculo de N)
- **Fluxo:** aprovar DV_confirm → D-07 (pré-registro + potência + Lock).
- **Prós:** caminho mais curto para o próximo estudo; DV já validada por simulação; D-04/D-05 são
  gates de *produção* que só afetam a coleta futura, não o desenho da DV.
- **Contras:** D-06 (Δ TOST) ficaria para depois do recálculo — o tamanho de efeito para a
  potência usaria r_rb/mediana sem a margem de equivalência formalizada.
- **Risco:** baixo para a DV; Δ TOST pode exigir reabertura do N se definido depois.

### Opção B — Completar D-04/D-05/D-06 antes do recálculo (sequencial estrito)
- **Fluxo:** D-04 → D-05 → D-06 → D-07.
- **Prós:** pré-registro e recálculo de N absorvem Δ TOST (D-06) e os gates de produção
  (D-04/D-05) de uma vez; sequência totalmente determinística; nenhuma reabertura esperada.
- **Contras:** mais lento; D-04/D-05 não interagem com a DV (podem ser paralelizados sem custo).
- **Risco:** baixo, mas com prazo maior.

### Opção C — Combinar D-04 em paralelo com a revisão (paralelismo moderado)
- **Fluxo:** D-04 em paralelo à revisão do desenho (D-03-review) enquanto D-07 prepara o
  pré-registro; D-05 e D-06 antes do Lock.
- **Prós:** aproveita o tempo de governança para fechar o gate de parseabilidade (dívida
  independente da DV, única com gate gap registrado no GO-8C: `D-04-GATE-GAP-ENGINE-PARSEABILITY.md`);
  reduz o prazo sem comprometer a validade.
- **Contras:** exige coordenação; D-06 (Δ TOST) continua sendo pré-requisito do recálculo de N
  (D-07) — ou seja, D-07 só dispara após D-06 mesmo na opção C.

---

## 6. Recomendação do agente

**Opção C** (D-04 em paralelo + D-05/D-06 antes de D-07):
1. **Aprovar o desenho da DV_confirm** (componentes + pesos 1:1:1) como base do novo estudo;
   registrar formalmente em `ACTION-REGISTER.md` a aceitação do desenho pela governança.
2. **Executar D-04 em paralelo** (gate de parseabilidade) — é a única dívida **independente da
   DV** e já tem gate gap documentado no GO-8C; fechar agora evita regressão de produção.
3. **Executar D-06 (definição de Δ para TOST)** antes do recálculo de N — a margem de equivalência
   precisa estar fixa para dimensionar N corretamente (senão risco de reabertura).
4. **D-05 (gate semântico híbrido)** antes do novo Lock (faz parte do protocolo de produção do
   próximo ciclo; sem ele o Lock não incorpora a revisão humana de materiais).
5. **D-07 por último:** novo pré-registro (DV_confirm + Δ TOST + plano inferencial) → recálculo
   de N → Lock do GO-8D → execução (somente após autorização formal por etapa).

**Justificativa:** maximiza paralelismo sem violar dependências; nenhuma das opções altera a
validade estatística da DV (já demonstrada na simulação); a única dependência forte é
D-06 → D-07 (Δ antes do N), preservada em todas as opções.

---

## 7. Confirmação de integridade

- **Nenhum arquivo do GO-8B/GO-8C alterado** (verificado por `git status`); GO-8B e GO-8C
  permanecem CLOSED/LOCKED/FROZEN.
- Arquivos deste ciclo (novos, no GO-8D): este documento, `D-03-PIPELINE-REDESIGN.md`,
  `analysis/pipeline_redesign_sim.py`, `analysis/pipeline_redesign_sim2.py`,
  `analysis/redesign_cells.json`, `analysis/redesign_cells2.json`.
- **Nenhum pré-registro, recálculo de N, Lock ou execução experimental foi realizado.**

---

**Fim do documento de revisão de desenho D-03. 2026-08-14.**
