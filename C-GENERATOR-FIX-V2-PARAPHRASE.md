# C-GENERATOR-FIX-V2-PARAPHRASE

Correção do gerador de casos para o MR-C7 v2 — assimetria estrutural ΔV2 vs ΔV3 por colisão espúria de tokens.

**Data:** 2026-08-19
**Escopo:** `generate_cases.py` (somente o caminho de geração V2). Nenhum outro arquivo de execuções anteriores foi alterado.

---

## 1. Diagnóstico (Tarefa 1 — confirmado, sem alteração de código)

A investigação de causa raiz em `§7.5.1` do `MR-C7-REPORT.md` (v1) mostrou que cada fato redundante de V2 compartilhava o **token temático do caso** + um **filler comum** (apenas 2 valores para 9 fatos-base), disparando a regra `relates` (`|overlap| ≥ 2`, `reconstruction.py:139-151`, cópia fiel do engine congelado) com **4–6 fatos-base NÃO relacionados** — não só com o único fato que deveria ser parafraseado.

Decomposição (24 casos, dados v1, somente leitura):

| Nível | Métrica | Valor |
|-------|---------|-------|
| Entidade | `relates` com o fato-base **pai** (redundância genuína) | **3.00/caso** |
| Entidade | `relates` com fatos-base **não relacionados** (colisão espúria) | **10.21/caso** |
| Entidade | `relates` entre fatos V2 (template) | 2.00/caso |
| Colapsado | Arestas extras vs G0 = self-loop do pai | 2.08/caso (16.6%) |
| Colapsado | Arestas extras vs G0 = não-self (colisão espúria) | 10.46/caso (83.4%) |

**Conclusão da governança:** a maioria (≈83%) é colisão espúria, não redundância genuína → estender a verdade G0→V2 em `metric.py` seria circular. O defeito é do gerador; corrigir na origem.

## 2. Correção (Tarefa 2 — Opção A, isolada ao caminho V2)

**Estratégia:** cada fato V2 passa a conter **apenas os tokens específicos da categoria/conteúdo** do fato-base parafraseado — sem o token temático do caso e sem os fillers compartilhados. Assim a regra `relates` do engine (intacta) só gera relação forte com o fato-base efetivamente parafraseado (overlap ≥ 2 só com o pai). `reconstruction.py` não foi tocado; V0/V1/V3 inalterados.

### Antes

```python
def make_v2_paraphrase(topic_token, cat, base_fact):
    base_tok = sorted(fact_tokens(base_fact))
    cat_kws = sorted(fact_tokens(DEF_CLAUSE[cat]) & set(base_tok))
    others = [t for t in base_tok if t not in cat_kws]
    picks = (cat_kws[:2] + others[:2])[:4]
    body = ", ".join(picks)
    return "Para o caso, %s sao mantidos no %s de forma uniforme." % (body, topic_token)
```

### Depois

```python
def make_v2_paraphrase(topic_token, cat, base_fact):
    """Paráfrase redundante (V2) SEM o token temático do caso nem os fillers
    compartilhados (C-GENERATOR-FIX-V2-PARAPHRASE.md, Opção A). ..."""
    base_tok = sorted(fact_tokens(base_fact))
    cat_kws = sorted(fact_tokens(DEF_CLAUSE[cat]) & set(base_tok))
    picks = cat_kws[:4]
    if len(picks) < 4:
        picks += [t for t in base_tok if t not in picks and t != topic_token][:4 - len(picks)]
    body = ", ".join(picks)
    return "Para o caso, %s sao mantidos de forma uniforme." % body
```

Mudanças: (a) `others` (que incluíam token temático + fillers) removido dos `picks`; (b) template sem `"no %s" % topic_token`; (c) `picks` = até 4 palavras-chave da própria categoria (todas as 12 categorias têm ≥ 4). Adicionalmente, `main()` ganhou **saída parametrizada** (`argv[1]` opcional) para a v2 não sobrescrever `inputs/cases.yaml` da v1 (histórico).

### Verificação funcional do fix

- overlap com o fato-base **pai** ≥ 2: **9/9**
- overlap com **qualquer outro** fato-base: < 2 (**9/9**, valor observado máximo = 0)
- classificação direta no pai: 8/9 (MRCAT-09 → MRCAT-08; limitação conhecida do embedding hash, presente também na v1 — log de issue, não filtra)

## 3. Hash SHA-256 (scripts)

| Arquivo | SHA-256 |
|---------|---------|
| `measurement-redesign/phase4/scripts/generate_cases.py` (corrigido) | `1340e462520ef73d1765cec34d7ad3b109b8876cc41a9459d7d2e68f0c108c9d` |
| `measurement-redesign/phase4-v2/inputs/cases.yaml` (regenerado, seed 20260818) | `479692d5d4a20a010fe0ac71e238c39f40ef990aa881b3e02555c80269ba7184` |

Nota: o hash v1 de `generate_cases.py` era `4fc038adc479f09b749c4b16d50651c20ba034349f9f3788326ea5a9f254541d` (registrado no `MR-C7-REPORT.md` v1 — histórico inalterado).

## 4. Verificação da regeneração (Tarefa 3 — só geração)

Mesma seed (`seed_casegen = 20260818`), saída em `phase4-v2/inputs/cases.yaml`.

| Métrica | v1 | v2 |
|---------|----|----|
| `base_facts` idênticos (v1==v2) | — | 24/24 |
| Pools V1 idênticos (v1==v2) | — | 24/24 |
| Pools V3 idênticos (v1==v2) | — | 24/24 |
| Issues de classificação na geração | 106 | 49 |
| V1 extra vs G0 (média/caso, nível de pool) | 1.028 | 1.028 |
| V2 extra vs G0 (média/caso, nível de pool) | 4.187 | **1.944** (−53.6%) |
| V3 extra vs G0 (média/caso, nível de pool) | 1.028 | 1.028 |
| V2 extra vs G0 (média/caso, estado completo 3 fatos) | 13.08 | **4.88** (−62.7%) |
| Self-loop do pai (estado completo) | 1.88/caso | 2.54/caso (redundância genuína preservada) |

Conclusão: a estrutura extra espúria de V2 foi eliminada; o resíduo (~4.9/caso em estado completo) é o esperado — cadeia `follows` do engine (~3) + self-loop do fato-pai (redundância genuína, ~2.5). V1 e V3 permanecem com o mesmo perfil exato da v1 (a correção não os afeta; determinismo preservado).

**Nota de rastreabilidade:** nenhum limiar, teste estatístico ou artefato hash-locked da v1 foi alterado (v1 permanece como registro histórico). A correção é documentada antes de qualquer redesenho/re-execução.