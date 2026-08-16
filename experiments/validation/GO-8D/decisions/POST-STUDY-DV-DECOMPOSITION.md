# GO-8D — POST-STUDY AUDIT: DECOMPOSIÇÃO DA DV_confirm

**Data:** 2026-08-14
**Fase:** POST-STUDY AUDIT (read-only sobre artefatos GO-8D; nenhum experimento novo)
**Input:** `study-output/pilot_results_g8d.csv` (108 linhas; células determinísticas — 3 seeds idênticas por célula)
**Script de análise:** `analysis/post_study_dv_audit.json` (análise auxiliar; novo artefato de auditoria, não congelado)

**DV_confirm = (conf + ged_ref + ent)/3** — conf: fidelidade por fato (média de confiança das
entidades); ged_ref: similaridade GED ponderada (w_edge=0.5) do grafo reconstruído vs grafo de
referência; ent: entropia normalizada da distribuição de categorias sintéticas
(`entropy_n = H / log(n_slots)`).

---

## 1. Tabela por Componente × Condição (medianas de célula, N=12)

| Componente | A (cega) | B (cega+C3) | C (não-cega) | Δ B−A (mediana) | B<A (n/12) |
|---|---|---|---|---|---|
| **conf** | 0.7343 | 0.7369 | 0.7222 | **−0.0010** | 7/12 |
| **ged_ref** | 0.4721 | 0.4172 | 0.4949 | **−0.0590** | 11/12 |
| **ent** | 0.9089 | 0.7298 | 0.8004 | **−0.1985** | **12/12** |
| **DV_confirm** | 0.7134 | 0.6220 | 0.6843 | −0.0793 | 12/12 |

**Escala observada (min–max por condição):**
- conf: A [0.715, 0.749] · B [0.714, 0.745] · C [0.707, 0.744] — **quase idêntica entre condições**.
- ged_ref: A [0.404, 0.565] · B [0.372, 0.486] · C [0.423, 0.543] — B comprimida para baixo.
- ent: A [0.848, 0.978] · B [0.588, 0.799] · C [0.642, 0.923] — B bem mais baixa.

## 2. Contribuição de Cada Componente para B<A (share do |Δ| médio)

| Componente | Mean \|B−A\| | Share da queda | Correlação com DV (36 células) |
|---|---|---|---|
| conf | 0.0041 | **1.6%** | r = 0.107 |
| ged_ref | 0.0681 | **25.5%** | r = 0.663 |
| ent | 0.1947 | **72.9%** | r = 0.920 |

**→ A `ent` domina a queda de B** (72.9% do |Δ| médio; 12/12 BIPs negativos; componente dominante
por \|Δ\| em 11/12 BIPs — única exceção BIP-010, onde ged_ref domina). `conf` é praticamente neutra.

## 3. Consistência entre BIPs

- **DV_confirm:** B<A em **12/12 BIPs** (Δ mediana −0.079; range −0.132 a −0.052) — efeito **uniforme**, não dominado por casos extremos.
- **ent:** B<A em **12/12 BIPs** (Δ mediana −0.1985; range −0.333 a −0.065) — o mais consistente.
- **ged_ref:** B<A em **11/12 BIPs** (única exceção BIP-003, Δ=+0.043).
- **conf:** B<A em apenas **7/12** e com magnitude desprezível (±0.013) — **inconsistente/irrelevante**.
- BIPs com B<A em **todos os 3 componentes**: 6/12 (BIP-002, 004, 005, 007, 011, 012).

**Conclusão de consistência:** o resultado B<A é consistente entre BIPs (não dominado por poucos
casos); ent e ged_ref são os motores, conf é neutra.

## 4. Assimetrias Estruturais da Métrica (achado principal)

### 4.1 `ent` — normalização com `n_slots` distinto entre condições (`run_study_g8d.py:170`)

```
n_slots = 9 if cond in ("A", "C") else 12
entropy_n = H / log(n_slots)
```

- A/C são normalizadas por **log(9)=2.197**; B por **log(12)=2.485** (taxonomia C3 tem 12 nós; C2 tem 9).
- Como o denominador de B é **13% maior**, o mesmo H produz um `ent` **menor** para B — **penalização de calibração** embutida.
- **Quantificação (denominador comum log(9)):**

| Métrica | Original (9 vs 12) | Re-normalizado log(9) p/ todos |
|---|---|---|
| ent mediana B | 0.7298 | **0.8253** |
| Δ ent B−A (mediana) | −0.1985 | **−0.1014** |
| negativos | 12/12 | 11/12 |
| Δ DV_confirm B−A (mediana) | −0.0793 | **−0.0463** |
| DV B<A | 12/12 | 12/12 |

- **Entropia bruta H:** A=1.9971, B=1.8134 (Δ B−A = −0.184) — há uma **diferença real** de entropia
  (B produz distribuição mais concentrada), mas a normalização distinta **amplifica ~2×** o Δ de `ent`
  (−0.1985 → −0.1014 com denominador comum).

### 4.2 `ged_ref` — referência com tamanho distinto entre condições (`run_study_g8d.py:37-40`)

- A/C usam `CAT_REF` (9 nós, 8 arestas); B usa `SYN_REF` (12 nós, 13 arestas).
- `ged_similarity` divide o custo pelo `max_cost = (n+m) + w_edge·(rec_edges+ref_edges)`.
- Com reconstrução típica (n=9, rec_edges=12): max_cost CAT=28.0 vs SYN=33.5 → **~16–17% maior
  para B** → similaridade **deflacionada** para B por construção, mesmo com o mesmo custo bruto.

### 4.3 `conf` — sem assimetria estrutural

Nenhuma diferença de denominador/referência; B e A praticamente empatam (Δ −0.001).

## 5. Conclusão sobre a Validade da DV_confirm

1. **A DV_confirm, como construída, é problemática para comparação entre condições:**
   as duas componentes mais influentes (ent 72.9% + ged_ref 25.5% = **98.4% da queda B−A**) carregam
   **assimetrias estruturais de calibração** que penalizam B: `n_slots` 12 vs 9 na entropia
   normalizada e referência SYN 12 nós vs CAT 9 nós na GED.
2. **O efeito B<A é parcialmente artefato métrico:** com normalização comum (log(9)) o Δ de DV
   cai de −0.0793 para −0.0463 (~42% do efeito desaparece).
3. **Porém o efeito não é integralmente artefato:** mesmo com denominador comum, ent (H real Δ
   −0.184) e ged_ref seguem negativos e B<A persiste em 12/12 (DV) e 11/12 (ent). Há um **componente
   real** de menor diversidade de categorias e menor similaridade estrutural em B.
4. **conf não é o motivo** da queda — é neutra.
5. **Consistência:** o sinal B<A é uniforme entre os 12 BIPs (não dominado por casos extremos),
   mas a **magnitude** reportada no estudo confirmatório é **inflada** pelas assimetrias.

## 6. Recomendação para a Governança

**DEC-A (recomendada):** declarar a **DV_confirm problemática para comparação entre condições
(viés de calibração favorável a A/C e desfavorável a B)**. Recomendações de mitigação (para
futuro ciclo, **sem** reexecução agora):

1. Padronizar `n_slots` da entropia (denominador comum por condição) ou usar entropia não
   normalizada H.
2. Padronizar a referência da GED (mesmo conjunto de nós/arestas de referência entre condições,
   ou normalizar max_cost pelo mínimo comum).
3. Reconsiderar o peso de `ent` (atualmente 1/3) dado que ela concentra 72.9% da queda e é a
   componente mais sensível ao tamanho da taxonomia.
4. Opcionalmente reportar DV com e sem correção de assimetrias em ciclos futuros.

**Decisão formal da governança:** a ser registrada após este relatório (DEC-A / DEC-B / DEC-C em
`POST-STUDY-AUDIT-DECISION.md`). Nenhum novo ciclo experimental é aberto.

---

**Fim do relatório. Auditoria read-only — nenhum artefato congelado (GO-8B, GO-8C, Lock GO-8D)
foi alterado; nenhum arquivo untracked foi modificado ou commitado.