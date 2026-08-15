# D-03 — Pipeline Redesign (Reprojeto do Pipeline e da Taxonomia)

**Data:** 2026-08-14
**Ciclo:** GO-8D — DIAGNOSTIC PHASE
**Tipo:** proposta de reprojeto (simulações sobre dados existentes do GO-8C; sem novo experimento)
**Base:** D-01 (`SSTRUCT-AUDIT.md`) e D-02 (`D-02-METRICS-ANALYSIS.md`)
**Artefatos de suporte:** `GO-8D/analysis/pipeline_redesign_sim.py` · `GO-8D/analysis/pipeline_redesign_sim2.py` · `GO-8D/analysis/redesign_cells.json` · `redesign_cells2.json`

---

## 1. Objetivo

Reprojetar os componentes do pipeline para permitir uma **DV confirmatória válida**, eliminando
os artefatos de D-01/D-02: (i) anonimização uniforme do WL; (ii) embeddings CAT colapsados em
cosseno 1.0; (iii) granularidade de taxonomia despadronizada (9 vs 12 slots); (iv) referência
implícita da taxonomia; (v) lacuna de rastreabilidade do BIP-007-B. **Somente simulação sobre os
dados existentes; nenhuma alteração do engine congelado; nenhum dado novo.**

## 2. Análise do pipeline atual — pontos exatos de correção

| # | Ponto | Arquivo:linha | Problema (origem D-01/D-02) |
|---|---|---|---|
| P1 | Anonimização uniforme | `wl_kernel.py:30` `labels = {n: "neutral"}` | Elimina todo o sinal de categoria; S_struct ≈ contagem de nós. |
| P2 | Embeddings CAT = nomes canônicos | `p4_generate_embeddings.py:33-34` | `texts[("CAT",cat)] = canon_name` → cosseno 1.0 com ECP; S_sem degenerada (D-02 M4: constante 0.8333). |
| P3 | Granularidade despadronizada | `pilot_engine.py:288-293` (namespace/slots) + colapso por categoria (`graph_from_reconstruction.py:97-134`) | A/C: 9 slots CAT; B: 12 slots SYN. Confunde nº de nós; M1 (D-02) anula a separação A/B/C. |
| P4 | Referência fixa ao ECP | `wl_kernel.py:214-236` `G_ECP` + `compute_s_metrics` | Compara-se sempre à cadeia ECP de 9 nós, nunca à taxonomia da condição; CAT↔ECP só por bijectividade C2. |
| P5 | Taxonomia não registrada por execução | `pilot_engine.py:52-55` (load global) | Engine lê `C3_TAXONOMY.yaml` global; não grava hash/versão usada → lacuna BIP-007-B. |

## 3. Desenho revisado dos componentes

### 3.1 `wl_kernel.py` rotulado (P1)

- Novo método `structural_features(graph, labels=None)`: usa `labels` (nó→categoria real) se
  fornecido; cai para `"neutral"` apenas quando ausente (backward-compatible).
- Novo `s_struct_labeled(g1, g2, labels1, labels2)` = cosseno dos histogramas WL com rótulos
  reais de categoria.
- **Resultado de simulação:** o WL rotulado **sozinho permanece degenerado** no grafo colapsado
  (A=2/12 valores distintos; B=3–6/12): o colapso por categoria (P3) reduz o grafo a 5–11 nós e
  o kernel não recupera sinal. **Conclusão: desanonimizar o WL é necessário mas não suficiente**;
  sem corrigir o colapso, o WL rotulado não pode ser componente único da DV.

### 3.2 `graph_from_reconstruction.py` com granularidade padronizada (P3)

- Manter o colapso por categoria (é o desenho do estudo), mas **comparar contra a taxonomia da
  própria condição** (P4) em vez da cadeia ECP fixa. Isso padroniza a granularidade: cada condição
  é medida contra a estrutura que a taxonomia prescreve (T_PERM/CAT para A/C; DAG C3 para B).
- Referências explícitas:
  - A/C → cadeia CAT (`CAT-01→CAT-05→CAT-06→CAT-03→CAT-07→CAT-00→CAT-04→CAT-08→CAT-02`,
    derivada de `C2_PERMUTATION.yaml` `canonical_order` + `canonical_to_opaque`), 9 nós, 8 arestas.
  - B → DAG C3 (12 nós, 13 arestas) do `C3_TAXONOMY.yaml` **corrigido** (D-03.7).

### 3.3 `pilot_engine.py` com referência correta de taxonomia (P2, P4, P5)

- `label_emb_corrected(label)`: CAT-XX → embedding da **definição neutra em PT**
  (`CAT_NEUTRAL_DEFS`, não o nome canônico ECP); SYN-XX → embedding da definição **corrigida**
  (D-03.7); ECP → tabela congelada.
- `compute_s_metrics` recebe a referência da condição (T_PERM/DAG C3) e grava no resultado
  `taxonomy_sha256` (hash da taxonomia usada) — **fecha a lacuna do BIP-007-B**: verifica-se que
  todas as 36 células do N=12 usaram `sha256=5ba63db7a81c454d` (corrigida), ou seja, a "inconsistência"
  da D-01 era erro de leitura do CSV; o problema real era só a ausência de registro.

### 3.4 Nova DV confirmatória (composta, ponderada e pré-registrável)

**`DV_confirm = (conf + ged_ref + ent)/3`**, onde:
- **conf** — fidelidade por fato: confiança média do classificador (∈[0,1]).
- **ged_ref** — GED ponderada **vs taxonomia da condição** (substituição de nós por cosseno de
  embeddings corrigidos, arestas dirigidas com peso 0.5, normalizada em [0,1]).
- **ent** — entropia de atribuição normalizada (Shannon / log(nº slots da condição)).

Justificativa: cada componente é padronizado entre condições (frações/valores em [0,1],
denominador = nº de slots da própria condição), é sensível a rótulo (não anonimizado), é
interpretável e, em conjunto, passa nos critérios de D-01 §7 (variabilidade, ausência de platô,
correlação fraca com nº de nós).

## 4. Simulações sobre os dados existentes (36 células do N=12)

Método: mesmos materiais e classificador do GO-8C (engine congelado importado por leitura),
taxonomia corrigida injetada na condição B, embeddings corrigidos (§3.3).

### 4.1 Componentes isolados

| Métrica | Cond | Mediana | Distinct/12 | Range | Friedman Q | corr(nós) |
|---|---|---|---|---|---|---|
| **wl rotulado (raw)** | A | 0.2500 | 2 | 0.014 | — | +0.594 |
| | B | 0.2162 | 3 | 0.035 | 10.67 | |
| | C | 0.2357 | 5 | 0.064 | | |
| **wl rotulado (norm)** | A | 0.2500 | 2 | 0.014 | — | +0.594 |
| | B | 0.2162 | 6 | 0.035 | 10.67 | |
| | C | 0.2357 | 5 | 0.064 | | |
| **ssem_corr** (S_sem corrigida) | A | 0.5558 | 3 | 0.005 | 22.17 | −0.468 |
| | B | 0.5421 | 11 | 0.004 | | |
| | C | 0.5583 | 8 | 0.011 | | |
| **ged_ecp** (GED vs ECP) | A | 0.3171 | 11 | 0.098 | **2.17 (n.s.)** | −0.047 |
| | B | 0.3132 | 12 | 0.176 | | |
| | C | 0.3138 | 12 | 0.102 | | |
| **ged_ref** (GED vs tax. condição) | A | 0.4721 | 12 | 0.161 | **10.17** | **−0.025** |
| | B | 0.4172 | 12 | 0.114 | | |
| | C | 0.4949 | 11 | 0.120 | | |
| **conf** (fidelidade) | A | 0.7343 | 12 | 0.034 | 15.50 | +0.317 |
| | B | 0.7369 | 12 | 0.031 | | |
| | C | 0.7222 | 12 | 0.037 | | |
| **ent** (entropia) | A | 0.9089 | 12 | 0.130 | 16.67 | +0.215 |
| | B | 0.7289 | 12 | 0.211 | | |
| | C | 0.8004 | 12 | 0.282 | | |

**Achados críticos:**
1. **O WL rotulado não resolve sozinho** (degenerado: A=2/12). A causa é o colapso por categoria;
   correção exige revisar o próprio desenho de grafo (fora do escopo de uma métrica).
2. **A correção dos embeddings CAT muda a leitura do D-02:** o `ged_ecp` (GED vs ECP) que na
   D-02 dava Q=18.00 cai para **Q=2.17 (n.s.)** com embeddings corrigidos — o ganho aparente
   A/C era artefato do cosseno 1.0 (P2), não fidelidade real ao ECP.
3. **`ged_ref` (vs taxonomia da condição) é o componente estrutural robusto:** 12/12/11 valores
   distintos, Q=10.17, corr(nós)=−0.025 (sem confundimento de contagem de nós).
4. **`conf` e `ent`** são discriminativos (12/12) e medem fidelidade por fato e distribuição de
   atribuição, independentes de topologia.

### 4.2 Compostos candidatos

| Composto | Q (Friedman) | corr(nós) | distinct A/B/C |
|---|---|---|---|
| conf+ged_ref | 10.50 | +0.046 | 12/12/12 |
| conf+ged_ref+ent | **18.50** | **+0.189** | **12/12/12** |
| ged_ref+ent | 18.50 | +0.161 | 12/12/12 |
| conf+2·ged_ref+ent | 17.17 | +0.138 | 12/12/12 |

**Composto recomendado: `conf + ged_ref + ent`** (pesos 1:1:1): separação A/B/C forte
(Q=18.50, p≈0.001), nenhum platô (12/12 em todas as condições), correlação fraca com nº de nós
(+0.189), interpretável componente a componente.

## 5. Mudanças propostas — resumo

1. **`wl_kernel.py`**: adicionar variante rotulada (`labels` opcional). *(Backward-compatible;
   não altera a S_struct congelada quando `labels=None`.)*
2. **Embeddings corrigidos**: CAT-XX passam a usar as definições neutras PT
   (`CAT_NEUTRAL_DEFS`), não os nomes canônicos ECP — elimina o colapso de cosseno 1.0.
3. **Referência por condição**: métrica estrutural calculada contra a **taxonomia da condição**
   (cadeia T_PERM para A/C; DAG C3 corrigido para B), padronizando a granularidade (9 vs 12 slots).
4. **Rastreabilidade**: gravar `taxonomy_sha256` (e `taxonomy_version`) por execução no output;
   encerra a lacuna do BIP-007-B.
5. **Nova DV confirmatória**: `DV_confirm = (conf + ged_ref + ent)/3`, com pesos a serem
   congelados no pré-registro.

## 6. Impacto esperado nas métricas

- **S_struct atual** deixa de ser DV; mantida apenas como histórico.
- **S_sem refinada** (ssem_corr) descartada como DV: permanece quase constante para A (3/12) e
  fortemente correlacionada a nº de nós (corr −0.47).
- **WL rotulado** mantido como **diagnóstico**, não como DV (degenerado no grafo colapsado).
- **ged_ref + conf + ent** passam a compor a DV; separação A/B/C forte e ausência de platô.

## 7. Necessidade de novo pré-registro e Lock

**SIM — imprescindível.** A mudança da DV invalida o pré-registro N=12 do GO-8C
(`08-PRE-REGISTRATION-N12.md`):
1. **Novo pré-registro (D-07/N2):** fixar `DV_confirm = (conf + ged_ref + ent)/3`, pesos,
   hipóteses A vs B e B vs C, análises (Friedman → Wilcoxon+Holm → r_rb/Cliff δ), Δ para TOST
   (D-06), critérios de Go/No-Go, e novas seeds.
2. **Recálculo de N (D-07):** efeito observado na simulação (mediana A=0.7134 vs B=0.6220,
   Δ≈0.09 na escala composta) para dimensionar N.
3. **Novo Lock:** engine modificado (wl_kernel rotulado, embeddings corrigidos, referência por
   condição, hash de taxonomia) exige re-gerar o Lock; GO-8B/GO-8C permanecem imutáveis.
4. **Regra de execução:** novo estudo roda **apenas sobre os mesmos 12 BIPs existentes** (sem
   coleta) ou com novos BIPs sob a mesma taxonomia corrigida — decisão da governança em D-04/D-07.

## 8. Confirmação de integridade

- **Nenhum arquivo do GO-8B/GO-8C alterado** (verificado por `git status`); GO-8B e GO-8C
  permanecem CLOSED/LOCKED.
- Somente arquivos novos no GO-8D: `analysis/pipeline_redesign_sim.py`,
  `analysis/pipeline_redesign_sim2.py`, `analysis/redesign_cells.json`, `redesign_cells2.json` e
  este relatório. (Correção factual da D-01 sobre o BIP-007-B já registrada na D-02 §6.)
- Simulações executadas com módulos congelados importados por leitura; nenhuma escrita no pipeline.

---

**Fim do relatório D-03. 2026-08-14.**
