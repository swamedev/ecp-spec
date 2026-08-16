# Relatório Final do Estudo Confirmatório GO-8C (N=12)

**Data:** 2026-08-14
**Status:** **GO — concluído**
**Ciclo:** GO-8C (estudo confirmatório N=12, derivado do GO-8B)
**Autorização:** governança GO-8C (D-04..D-04.12; encerramento aprovado 2026-08-14)
**Lock:** `GO-8C-LOCK-MANIFEST.yaml` (151 artefatos) · `GO-8C-LOCK-RECORD.yaml` (LOCKED) — validado PASS

---

## 1. Resumo Executivo

O estudo confirmatório **GO-8C (N=12)** foi executado integralmente conforme o pré-registro
(`08-PRE-REGISTRATION-N12.md`, replicando 06/07/08 do GO-8B com as adaptações aprovadas N=12,
Go/No-Go ≥10 de 12, seed C2 corrigida e namespace operacional A→CAT / B→SYN / C→CAT).

**108 reconstruções de 12 casos (BIPs) × 3 condições × 3 seeds — todas PASS (0 FAIL).**
O estudo atingiu o **Go/No-Go: GO** (12/12 casos válidos ≥ 10; matriz completa; nenhum FAIL-PILOT).

**Principais achados (S_struct, DV confirmatória):**
- Teste global de Friedman **rejeita H₀** (χ²_F=9.7826, df=2, **p=0.0075**; Kendall W=0.4076 — efeito médio);
- Post-hoc (Wilcoxon bilateral + Holm-Bonferroni): única comparação significativa é **B > C**
  (p=0.0093; r_rb=−0.821; Cliff δ=0.701 — efeito grande);
- **A vs B não é significativo pós-Holm** (p=0.0537), embora a direção favoreça B (r_rb=0.667;
  mediana B=0.6348 > mediana A=0.5875; IC da diferença de medianas (0.002, 0.095) exclui 0);
- Sensibilidades (sem outliers; drops por domínio) **todas p<0.05** — resultado omnibus robusto.

**Conclusão:** a comparação **B (cega+C3) vs C (não-cega) é robusta** (B estruturalmente maior).
A comparação **B vs A (cega pura) permanece inconclusiva/limítrofe** — tendência favorável a B,
sem significância após correção para comparações múltiplas nesta amostra N=12.

**TOST não executado** (nenhuma margem Δ aprovada; Δ=0.10 explicitamente não aprovada).

---

## 2. Metodologia

| Parâmetro | Valor |
|---|---|
| Desenho | Confirmatório, intra-caso, 3 condições pareadas |
| **N (casos/BIPs)** | **12** (001–007 reexecutados + 008 Apollo 13, 009 Chernobyl, 010 Tacoma Narrows, 011 Domino's, 012 Eyjafjallajökull) |
| Condições | A (cega pura) · B (cega + C3) · C (não-cega) |
| Namespaces operacionais | A→CAT, B→SYN, C→CAT (D-02) |
| Seeds | 3 por célula, determinísticas (PCG64, seed_master=20260814; `study-output/seeds_n12.py`) |
| Total de execuções | **12 × 3 × 3 = 108** |
| **DV confirmatória** | **S_struct** (estrutural) — mediana das 3 seeds por célula |
| DV exploratória | S_sem (semântica) |
| Teste global | Friedman (df=2, α=0.05) |
| Post-hoc | Wilcoxon signed-rank pareado bilateral + Holm-Bonferroni |
| Efeitos | Kendall W, rank-biserial r, Cliff δ |
| IC | Bootstrap B=10.000 (percentil, pareado; seed_statistics=1879048193) + IC exato da mediana (STAT-08) |
| Sensibilidade | sem outliers (IQR×1.5); drop 1 caso por par de domínio |
| **TOST** | **NÃO executado** (sem Δ aprovada) |
| Go/No-Go | **≥ 10 de 12 casos válidos** (pré-registro §8) |
| Potência pré-registrada | N=12 ≈ 0.895 |

**Pipeline:** materiais em `study-input/` (12 BIPs, zero-ECP, NT-05 validado por painel de 2 IAs) →
Lock (151 artefatos, 2026-08-14) → engine congelado (`pilot_engine.py`) → 108 reconstruções →
validação (07 adaptado ao N=12) → análise estatística (06 exato).

**Correção durante execução (D-04.11):** o `02-atomic-facts.md` do BIP-009 estava em formato de
tabela markdown, não parseável pelo engine (gate gap de parseabilidade); convertido para
`## Fatos` + lista numerada (72 fatos, texto/refs/ordem preservados), re-Locked e re-executado
— 6 células adicionais PASS (6/6).

---

## 3. Resultados Estatísticos

### 3.1 Descritivas (medianas por condição — S_struct)

| Condição | Mediana | IC 95% exato da mediana | IQR |
|----------|---------|------------------------|-----|
| **A** (cega pura) | 0.5875 | [0.5785, 0.6383] | [0.5853, 0.6002] |
| **B** (cega + C3) | **0.6348** | [0.5950, 0.6823] | [0.5950, 0.6821] |
| **C** (não-cega) | 0.5843 | [0.5676, 0.6048] | [0.5676, 0.5918] |

S_sem (exploratória): A=0.5495 · B=0.5532 · C=0.5478.

### 3.2 Teste Omnibus — Friedman (primário)

| Estatística | Valor |
|---|---|
| χ²_F | **9.7826** |
| df | 2 |
| **p** | **0.0075** |
| Kendall W | **0.4076** (efeito médio) |
| IC95% bootstrap de W | (0.1267, 0.7622) |

**Decisão:** p < 0.05 → **REJEITA H₀** (pelo menos uma condição difere) → post-hoc autorizado.

### 3.3 Post-hoc — Wilcoxon bilateral + Holm-Bonferroni

| Par | p (bruto) | Holm | r_rb | Cliff δ | IC95% dif. mediana | IC95% Cliff |
|-----|-----------|------|------|---------|--------------------|-------------|
| A vs B | 0.0537 | não rejeita | 0.667 | −0.486 | (0.002, 0.095) | (−0.819, −0.125) |
| A vs C | 0.3086 | não rejeita | −0.364 | 0.368 | (−0.036, 0.013) | (−0.139, 0.792) |
| **B vs C** | **0.0093** | **REJEITA** | **−0.821** | **0.701** | (−0.105, −0.008) | (0.361, 0.958) |

### 3.4 Sensibilidade

| Análise | N | Friedman p | W |
|---------|-----|-----------|-----|
| Sem outliers (IQR×1.5) | 9 | 0.0200 | 0.4346 |
| Civil — drop Hyatt | 11 | 0.0142 | 0.3869 |
| Civil — drop I-35W | 11 | 0.0179 | 0.3658 |
| Saúde — drop Ebola | 11 | 0.0088 | 0.4307 |
| Saúde — drop WarpSpeed | 11 | 0.0179 | 0.3658 |

Todas **p<0.05** → omnibus robusto.

### 3.5 Decisão Go/No-Go

| Critério | Limiar | Observado | Status |
|---|---|---|---|
| Casos válidos | ≥ 10 de 12 | **12** | **PASS** |
| Matriz N×3 completa | = N | 36/36 células | **PASS** |
| Nenhum FAIL-PILOT | — | nenhum | **PASS** |

**GO — 12/12 casos válidos ≥ 10 → análise estatística válida e concluída.**

---

## 4. Interpretação

1. **B > C (robusto):** a condição cega+C3 produz grafos estruturalmente superiores à condição
   não-cega (narrativa integral) — p=0.0093 pós-Holm, efeito grande (r_rb=−0.821; Cliff δ=0.701).
   O padrão sobrevive a todas as sensibilidades.
2. **A vs B (inconclusivo/limítrofe):** a evidência de que a taxonomia C3 melhora S_struct sobre a
   cega pura **não alcança significância** após Holm nesta amostra (p=0.0537), mas:
   - a direção favorece B (mediana B > A em 0.0473; r_rb=0.667);
   - o IC da diferença de medianas (0.002, 0.095) **exclui 0** (não contém 0);
   - trata-se de **tendência consistente, não confirmação**.
3. **Não se conclui "ausência de efeito"** para A vs B: potência N=12 ≈ 0.895 foi calculada para
   efeitos do tamanho observados no GO-8B; o resultado limítrofe sugere efeito real menor que o
   assumido ou variabilidade inter-caso maior.
4. **TOST:** sem margem Δ aprovada, nenhuma conclusão de equivalência foi emitida.

---

## 5. Limitações

1. **Poder estatístico ainda limitado** para a comparação A vs B em N=12 — resultado limítrofe
   (p=0.0537) impossibilita confirmação ou rejeição da utilidade C3 vs cega pura.
2. **Métrica S_struct com duplicações:** S_struct mede sobreposição estrutural de nós/arestas e pode
   inflar concordância via elementos duplicados/paráfrases estruturais não capturados pela taxonomia;
   sensibilidade limitada a diferenças semânticas finas.
3. **NT-05 por painel de IAs:** o gate semântico foi executado por painel de 2 IAs independentes
   (indisponibilidade de revisor humano), com limitação epistemológica registrada; houve divergência
   no NT-05 estendido (resolvida por análise da governança — `D-04-NT05-DIVERGENCE-ANALYSIS.md`).
4. **Gate gap de parseabilidade:** o validador de produção (D-04.5) não verificava a parseabilidade
   dos materiais pelo engine (erro do BIP-009 detectado apenas na execução); corrigido e registrado
   (`decisions/D-04-GATE-GAP-ENGINE-PARSEABILITY.md`) — check recomendado em ciclos futuros.
5. **Zero-ECP e rastreabilidade** dependem da lista ECP de 52 termos (congelada); vocabulário
   FRAM/STAMP permitido por N-3 pode conter semântica próxima não flagrada por checks lexicais.
6. **N nunca multiplicado** (unidade = caso/BIP), limitando o poder em comparações pareadas com
   variabilidade inter-domínio elevada.

---

## 6. Recomendações para Ciclos Futuros (GO-8D, se houver)

1. **Reavaliar S_struct** — investigar o componente de duplicação/sobreposição estrutural e sua
   influência na separação A vs B; documentar o viés potencial.
2. **Considerar métricas alternativas/complementares** — ex.: S_sem refinada, métricas de
   distância de edição estrutural (GED) ponderada, avaliação semântica dirigida (embeddings) ou
   métrica de fidelidade conceitual por fato.
3. **Possivelmente aumentar N além de 12** — para a comparação A vs B com efeito aparente menor
   que o assumido; atualizar a análise de potência com o efeito observado (p. ex. r_rb=0.667,
   dif. de medianas ≈ 0.047) para dimensionar N.
4. **Refinar a taxonomia C3** — avaliar se a definição atual (12 categorias) é discriminante o
   suficiente para capturar o ganho estrutural real da condição B; considerar expansão/calibração.
5. **Fechar o gate gap de parseabilidade** — adicionar check de parseabilidade (engine) ao
   validador de produção em futuros ciclos.
6. **Manter TOST não vigente** até aprovação de uma margem Δ formal (decisão da governança).
7. **Fortalecer o gate semântico** — recomenda-se revisor humano em complemento ao painel de IAs
   quando houver disponibilidade.

---

## 7. Encerramento

- Estudo GO-8C (N=12) **concluído** — **Status: GO**.
- Todos os artefatos estão sob o Lock GO-8C (151 arquivos, LOCKED, validado PASS).
- Pacote de encerramento: `GO-8C-CLOSURE-PACKAGE.zip`.
- GO-8B permanece CLOSED / LOCKED / FROZEN e **intacto**.

---

**Fim do Relatório Final GO-8C (N=12). 2026-08-14.**
