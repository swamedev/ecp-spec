# GO-8C — D-02 VALIDAÇÃO — C4 / NULL (Namespace Operacional das Condições A/C)

**Data da execução:** 2026-08-13
**Ciclo:** GO-8C
**Decisão de referência:** `D-02-C4-NULL-DECISION.md` (DECIDED 2026-08-13, Opção 2)
**Ambiente:** Python 3.11.9, numpy 1.26.4, PyYAML 6.0.2
**Comando:** `python test_d02_namespace.py` (workdir: `experiments/validation/GO-8C/scripts/`)

---

## 1. Resultado da Suíte

**RESULTADO GERAL: ALL PASS (3/3)**

| Teste | Resultado | Descrição |
|---|---|---|
| **T-D-02-01** | **PASS** | parser rejeita `NULL` com `NAMESPACE_MIX` (conforme especificação 04 §1.1) |
| **T-D-02-02** | **PASS** | parser aceita `CAT` e produz grafo válido (2 nós) com rótulos `CAT-XX` |
| **T-D-02-03** | **PASS** | namespaces operacionais A/B/C no artefato GO-8C = `CAT`, `SYN`, `CAT` |

## 2. Saída Bruta da Execução

```
T-D-02-01: PASS (NULL rejected with NAMESPACE_MIX (expected NAMESPACE_MIX))
T-D-02-02: PASS (CAT graph built: 2 nodes, all CAT-XX labels)
T-D-02-03: PASS (namespace_operacional = {'A': 'CAT', 'B': 'SYN', 'C': 'CAT'} (expected {'A': 'CAT', 'B': 'SYN', 'C': 'CAT}))

TOTAL: 3 PASS: 3 FAIL: 0
ALL PASS: True
```

## 3. Verificações-Chave Confirmadas

1. **NULL permanece não processável** — `graph_from_reconstruction.py` (intacto, GO-8B) rejeita `taxonomy_namespace=NULL` com `NAMESPACE_MIX` (T-D-02-01). Fiel à especificação congelada 04 §1.1.
2. **CAT é processável e preserva a cegueira** — o parser constrói grafo válido com rótulos opacos `CAT-XX` (T-D-02-02).
3. **Mapeamento operacional formalizado** — o artefato `C2_PERMUTATION.yaml` (GO-8C) declara `namespace_operacional = {A: CAT, B: SYN, C: CAT}`, com nota de que **não há equivalência NULL≡CAT nem CAT≡SYN/ECP** (T-D-02-03).

## 4. Reexecução da Suíte D-01 (regressão)

A edição do `C2_PERMUTATION.yaml` (adição de `namespace_operacional`/`namespace_note`) foi verificada pela suíte `p1_c2_test.py`:

```
T-C2-01..05, T-C2-08, T-C2-09: ALL PASS (7/7)
ALL PASS: True
```

Nenhuma regressão introduzida pela decisão D-02.

## 5. Conclusão

A decisão D-02 (Opção 2) está **VALIDADA**: NULL segue rejeitado por desenho, CAT permanece operacional para A/C com cegueira preservada, e o mapeamento A=CAT / B=SYN / C=CAT está formalizado no artefato operacional do GO-8C. **ALL PASS (3/3)** + regressão D-01 **ALL PASS (7/7)**.

## 6. Referências

- `experiments/validation/GO-8C/decisions/D-02-C4-NULL-DECISION.md`
- `experiments/validation/GO-8C/D-02-C4-NULL-PROPOSAL.md`
- `experiments/validation/GO-8C/scripts/test_d02_namespace.py`
- `experiments/validation/GO-8C/scripts/C2_PERMUTATION.yaml` / `.json`
- `scripts/go8b/operational/graph_from_reconstruction.py:84-85` (referência, NÃO alterado)
- `experiments/validation/GO-8B/04-GRAPH-FROM-RECONSTRUCTION.md` §1.1 (congelado, NÃO alterado)

---

**Fim da validação. D-02 VALIDATED. Nenhum arquivo do GO-8B alterado. Nenhum Lock gerado nesta etapa.**
