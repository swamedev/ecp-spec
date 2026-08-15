# D-04 — Gate de Parseabilidade (Parseability Gate)

**Data:** 2026-08-14
**Ciclo:** GO-8D — DIAGNOSTIC PHASE
**Tipo:** validação de gate (dívida D-04 — aprovada na Opção C da revisão de desenho)
**Base:** `GO-8C/decisions/D-04-GATE-GAP-ENGINE-PARSEABILITY.md` (gate gap do BIP-009)
**Artefatos:** `GO-8D/scripts/validate_parseability.py` (validador) · `GO-8D/scripts/test_d04_parseability.py` (testes) · `GO-8D/analysis/d04_test_results.json` · `GO-8D/analysis/d04_study_validation.json`

---

## 1. Problema que esta dívida fecha

No GO-8C, o validador de produção (P4/D-04.5) verificava apenas **LEXICON + TRACE** e **não**
verificava se o `02-atomic-facts.md` era parseável pelo engine congelado. O BIP-009-Chernobyl foi
produzido em **formato tabela markdown** (`| # | Fato | Fonte |`) → `parse_atomic_facts()` retornou
0 fatos → 6 células FAIL na execução. A correção foi feita **após** o Lock (D-04.11, re-Lock).

## 2. Solução implementada (somente no GO-8D)

`validate_parseability.py` adiciona o check de parseabilidade ao validador de produção. Para cada
`02-atomic-facts.md`:

1. **Detecção de formato divergente** (tabela / sem `## Fatos`) → **REJECT antes do Lock**;
2. **Parseabilidade pelo engine congelado**: `parse_atomic_facts()` com exigência de `>= 15` fatos;
3. **Consistência de ordem/texto** entre os fatos extraídos e a lista numerada da fonte.

Também valida narrativas (`parse_narrative` — condição C, não afetada pelo gap, mas coberta).

### Regras de formato formalizadas (exigência, não convenção)

- Cabeçalho `## Fatos` obrigatório;
- Cada fato em `N. <texto> [ref]` terminando em `]` ou ``]``;
- `>= 15` fatos;
- Linhas `|` (pipe) na seção Fatos → **REJECT** (formato tabela).

## 3. Testes e resultados (5/5 PASS)

| Teste | Descrição | Resultado |
|---|---|---|
| T-D-04-01 | Arquivo **tabela markdown** (modo de falha do BIP-009) → deve **FALHAR** | **PASS** (FAIL) |
| T-D-04-02 | Arquivo **padrão** (`## Fatos` + lista numerada) → deve **PASSAR** | **PASS** (PASS) |
| T-D-04-03 | Sem cabeçalho `## Fatos` → deve **FALHAR** | **PASS** (FAIL) |
| T-D-04-04 | `< 15` fatos → deve **FALHAR** | **PASS** (FAIL) |
| T-D-04-05 | Regressão de produção: **12/12 BIPs** do `GO-8C/study-input` parseáveis | **PASS** (True) |

**Resultado: 5/5 PASS.** O gate de parseabilidade fecha a lacuna documentada no GO-8C:
formatos divergentes (ex.: tabela) são rejeitados **antes** do Lock, e os 12 BIPs existentes
permanecem válidos (nenhum falso negativo).

## 4. Integração no fluxo de produção

- O validador passa a ser etapa obrigatória **entre a produção do material e o Lock** do próximo
  ciclo GO-8D (mesmo fluxo de P4/D-04.5, agora com o check de parseabilidade).
- Recomenda-se que `validate_study_input()` rode em **cada BIP** antes do pré-registro/Lock.
- Nenhuma alteração no engine congelado; o check usa `parse_atomic_facts()`/`parse_narrative()`
  importados por leitura de `scripts/go8b/operational/pilot_engine.py`.

## 5. Confirmação de integridade

- **Nenhum arquivo do GO-8B/GO-8C alterado**; GO-8B/GO-8C permanecem CLOSED/LOCKED/FROZEN.
- Arquivos criados apenas em `GO-8D/scripts/` e `GO-8D/analysis/` (este relatório).
- Nenhum pré-registro, Lock ou execução experimental realizado.

---

**Fim do relatório D-04. 2026-08-14. Status: VALIDATED (5/5 PASS).**
