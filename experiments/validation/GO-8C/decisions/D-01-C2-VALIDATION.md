# GO-8C — D-01 VALIDAÇÃO — C2 / P1-C2-01 (Seed da Permutação Corrigida)

**Data da execução:** 2026-08-13
**Ciclo:** GO-8C
**Decisão de referência:** `D-01-C2-DECISION.md` (DECIDED 2026-08-13)
**Artefato corrigido:** `02-C2-PERMUTATION-CORRECTED.md`
**Ambiente:** Python 3.11.9, numpy 1.26.4, PyYAML 6.0.2
**Comando:** `python p1_c2_test.py` (workdir: `experiments/validation/GO-8C/scripts/`)

---

## 1. Resultado da Suíte

**RESULTADO GERAL: ALL PASS (7/7)**

| Teste | Resultado | Descrição |
|---|---|---|
| **T-C2-01** | **PASS** | `PCG64(258915)` reproduz a permutação SS5 `[1, 5, 6, 3, 7, 0, 4, 8, 2]` |
| **T-C2-02** | **PASS** | alteração de 1 bit na seed produz permutação diferente (sensibilidade) |
| **T-C2-03** | **PASS** | bijetividade bidirecional do mapping SS6 |
| **T-C2-04** | **PASS** | completude: exatamente 9 categorias canônicas, sem duplicatas |
| **T-C2-05** | **PASS** | estabilidade/reprodutibilidade PCG64 (duas instanciações independentes) |
| **T-C2-08** | **PASS** | regressão: `PCG64(11473621728585666159)` → `[1, 5, 0, 4, 3, 8, 6, 2, 7]` NÃO reproduz a tabela SS5 (seed histórica = `HISTORICAL-NON-REPRODUCING`) |
| **T-C2-09** | **PASS** | oficialidade do YAML: `seed_operacional=258915`, `inversa_verdadeira=[5,0,8,3,6,1,2,4,7]`, inversa da permutação consistente, `seed_historica.status=HISTORICAL-NON-REPRODUCING` |

## 2. Saída Bruta da Execução

```
T-C2-01: PASS (PCG64(258915) reproduces SS5 permutation [1, 5, 6, 3, 7, 0, 4, 8, 2])
T-C2-02: PASS (single-bit seed change produces different permutation)
T-C2-03: PASS (bidirectional bijection SS6)
T-C2-04: PASS (9 categories, no duplicates)
T-C2-05: PASS (PCG64(258915) stable across independent instantiations (portability of PCG64))
T-C2-08: PASS (PCG64(11473621728585666159) -> [1, 5, 0, 4, 3, 8, 6, 2, 7] NOT equal to SS5 [1, 5, 6, 3, 7, 0, 4, 8, 2] (HISTORICAL-NON-REPRODUCING))
T-C2-09: PASS (YAML seed_operacional=True, inversa_verdadeira=True, true inverse of perm=True, seed_historica status=True)

TOTAL: 7 PASS: 7 FAIL: 0
ALL PASS: True
```

## 3. Verificações-Chave Confirmadas

1. **Seed oficial `258915`** (hex `0x3f363`) reproduz a tabela de permutação `[1, 5, 6, 3, 7, 0, 4, 8, 2]` sob PCG64 + Fisher-Yates — determinismo confirmado (T-C2-01).
2. **Inversa verdadeira `[5, 0, 8, 3, 6, 1, 2, 4, 7]`** é a inversa matemática da permutação e coincide com o YAML operacional (T-C2-09).
3. **Seed antiga `11473621728585666159`** NÃO reproduz a tabela — marcada `HISTORICAL-NON-REPRODUCING` no GO-8C (T-C2-08, documental; não falha a suíte).
4. Tabela de permutação e mapping bidirecional permanecem **idênticos** aos do GO-8B §5/§6 (tabela inalterada por decisão).

## 4. Conclusão

A correção da dívida D-01 (C2 / P1-C2-01) está **VALIDADA**: a seed oficial `258915` reproduz a permutação congelada, a inversa verdadeira está registrada e o artefato operacional (`C2_PERMUTATION.yaml` / `.json`) reflete a oficialidade. **ALL PASS (7/7)**.

## 5. Referências

- `experiments/validation/GO-8C/decisions/D-01-C2-DECISION.md`
- `experiments/validation/GO-8C/02-C2-PERMUTATION-CORRECTED.md`
- `experiments/validation/GO-8C/scripts/p1_c2_test.py`
- `experiments/validation/GO-8C/scripts/C2_PERMUTATION.yaml` / `.json`
- `experiments/validation/GO-8B/02-C2-PERMUTATION.md` (congelado, referência histórica — NÃO alterado)

---

**Fim da validação. D-01 VALIDATED. Nenhum arquivo do GO-8B alterado. Nenhum Lock gerado nesta etapa.**
