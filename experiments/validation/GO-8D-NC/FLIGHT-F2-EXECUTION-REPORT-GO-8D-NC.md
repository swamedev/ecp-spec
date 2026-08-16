# FLIGHT-F2-EXECUTION-REPORT-GO-8D-NC

**Fase:** F2 — EXECUÇÃO DAS 270 RECONSTRUÇÕES
**Data de início:** 2026-08-15 18:45:59
**Data de término:** 2026-08-15 18:46:30
**Status:** **F2 = PASS**

---

## 1. Resumo da Execução

| Métrica | Valor |
|---------|-------|
| Total planejado | 270 execuções (30 BIPs × 3 condições × 3 réplicas) |
| Total executado | 270 |
| PASS | 270 |
| FAIL | 0 |
| Taxa de sucesso | 100% |

---

## 2. Configuração

| Item | Valor |
|------|-------|
| Seed master | 20260816 |
| Artefato de seeds | `scripts/seeds_nc.py` (SHA-256: `e7dd39648743023393042668484d3458042cbe34e196e08dcdcb74b578746275`) |
| Pipeline | `pilot_engine.py` (LOCKED/FROZEN) |
| C2 | `C2_PERMUTATION.yaml` (SHA-256: `c91fecfeae83d9edb88dd16f2d1827283e308b53fdd6bf0a02c4b636a376b2a2`) |
| C3 | `C3_TAXONOMY.yaml` (SHA-256: `5ba63db7a81c454d7432873c184d2171741f8676e70d94cc538594627819bec8`) |
| DV3 | `clamp((conf + ged_ecp + ent_n12) / 3)` |
| Modelo de embedding | `sentence-transformers/all-MiniLM-L6-v2` |
| Pré-registro | v1.0 FINAL (SHA-256: `12fef4f74431b94fa0eacc8a170e2ad16192c871bc524464d5ddf0535fa5fcd1`) |
| Lock manifest | `GO-8D-NC-LOCK-MANIFEST.yaml` (SHA-256: `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`) |

---

## 3. Estrutura dos BIPs Executados

| Conjunto | BIPs | Diretórios | Execuções |
|----------|------|------------|-----------|
| GO-8C (herdados) | 001–012 | 12 (ex: `BIP-001-deepwater`, `BIP-002-hyatt`, ...) | 108 |
| GO-8D-NC (novos) | 013–030 | 18 (ex: `BIP-013-bhopal`, `BIP-014-tmi`, ...) | 162 |
| **Total** | **30** | **30** | **270** |

### Condições por BIP
- **A (cega pura):** atomic facts (`02-atomic-facts.md`)
- **B (cega + C3):** atomic facts (`02-atomic-facts.md`) + taxonomia C3
- **C (não-cega):** narrativa (`01-narrativa-original.md`)

---

## 4. Resultados por BIP (Resumo)

| BIP | Condição A | Condição B | Condição C | Status |
|-----|------------|------------|------------|--------|
| 001-deepwater | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 002-hyatt | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 003-ows | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 004-genoma | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 005-evergiven | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 006-i35w | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 007-ebola | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 008-apollo13 | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 009-chernobyl | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 010-tacomanarrows | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 011-dominos | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 012-eyjafjallajokull | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 013-bhopal | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 014-tmi | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 015-challenger | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 016-columbia | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 017-katrina | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 018-flint | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 019-fukushima | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 020-grenfell | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 021-vajont | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 022-max8 | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 023-mariana | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 024-dieselgate | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 025-wellsfargo | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 026-theranos | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 027-opioids | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 028-enron | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 029-takata | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |
| 030-concordia | PASS (3/3) | PASS (3/3) | PASS (3/3) | PASS |

---

## 5. Validação dos Outputs (`validate_data.py`)

```
VALIDATION: PASS (9 checks)
  row_count          pass=True {'expect': 270, 'actual': 270}
  schema             pass=True {'missing_columns': []}
  status             pass=True {'pass_rows': 270, 'total': 270}
  seed_cells         pass=True {'cells': 90, 'per_cell': [3, 3, ...], 'unique_global': 270}
  bounds_0_1         pass=True {'issues': [], 'n_issues': 0}
  namespace          pass=True {'issues': [], 'n_issues': 0}
  taxonomy_sha256    pass=True {'issues': [], 'n_issues': 0, 'expected_B': '5ba63db7a81c454d', 'expected_A_C': 'c91fecfeae83d9ed'}
  gonogo             pass=True {'valid_bips': 30, 'total': 30, 'decision': 'GO'}
  matrix             pass=True {'shape': [30, 3], 'has_nan': False}
```

### Arquivos de Validação Gerados
- `study-output/data_validation_newcycle.json`
- `study-output/dv3_matrix_newcycle.npy`

---

## 6. Integridade das Seeds

| Verificação | Resultado |
|-------------|-----------|
| Quantidade total | 270 (30 × 3 × 3) |
| Unicidade global | 270/270 únicas (0 duplicatas) |
| Associação BIP × cond × réplica | Determinística confirmada |
| Seed master | 20260816 confirmado |
| Intervalo uint64 | Todas em [0, 2⁶⁴-1] |

---

## 7. Integridade do Lock (GO-8D-NC)

| Artefato | SHA-256 | Status |
|----------|---------|--------|
| `C2_PERMUTATION.yaml` | `c91fecfeae83d9edb88dd16f2d1827283e308b53fdd6bf0a02c4b636a376b2a2` | OK |
| `C3_TAXONOMY.yaml` | `5ba63db7a81c454d7432873c184d2171741f8676e70d94cc538594627819bec8` | OK |
| `analyze.py` | `138b28979c57fe5349e87f93cc238661d060615aacc8af6bf7b0f663c97b19a6` | OK |
| `pilot_engine.py` | `3b56e50712fd95375b12c0d2949c4ce1798c461a11dd7c4769e98898959191ac` | OK |
| `wl_kernel.py` | `fcec435824da4650c5e9614215c2f2329b7b8e1c7ae4eabc24f23b783601ad40` | OK |
| `graph_from_reconstruction.py` | `7f2df2b81ecad6e5175399ad2db847e87541770bb33dcfcf0d7068e043c8a4ca` | OK |
| `validate_data.py` | `15f9e783d9f55597ba92e60b14f1bed49548884edd070324586134ae7164f4c8` | OK |
| `test_conformity.py` | `661032dcf885fc4359081ecdeb1ef4101f17ab644a3612005159719126958602` | OK |
| `generate_seeds.py` | `36aa66bb349b6994bcf077407458dec5f90b28ec6eb28d4c3b11e3d58442b3fd` | OK |
| `calibration_fixture.json` | `ed11ab9b65ac60d19d77b6775caa573b5633647765fd1806034140d7213e74eb` | OK |
| `D-MV-04-NEW-CYCLE-EXECUTION-PACKAGE.md` | `4cc8f98dc9d81414539cc375c8d4cd3385f0b2bbb085e1d590a305b5cc16c4a6` | OK |
| `SEED-MASTER-DECISION.md` | `dc187a2cab6f67e6b61fbb8f6b361586e8af7c5ed5989e905c154b53d1646d28` | OK |
| `08-PRE-REGISTRATION-NEW-CYCLE.md` | `12fef4f74431b94fa0eacc8a170e2ad16192c871bc524464d5ddf0535fa5fcd1` | OK |

**Manifest SHA-256:** `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058` — **OK**
**Lock Status:** `LOCKED` — **íntegro, sem alterações**

---

## 8. Go/No-Go Decision

| Critério | Resultado |
|----------|-----------|
| BIPs válidos (≥27/30) | **30/30 = GO** |
| Decisão pré-registrada | **GO** — análise confirmatória autorizável |

---

## 9. Arquivos de Output Gerados

| Arquivo | Descrição |
|---------|-----------|
| `study-output/pilot_results_newcycle.csv` | 270 linhas × 14 colunas (resultados brutos) |
| `study-output/data_validation_newcycle.json` | Relatório de validação (9 checks PASS) |
| `study-output/dv3_matrix_newcycle.npy` | Matriz DV3 (30 BIPs × 3 condições) |

---

## 10. Conformidade com Regras de Governança

| Regra | Status |
|-------|--------|
| Nenhuma seed gerada durante F2 | OK |
| Nenhuma regeneração de seeds | OK |
| Nenhuma alteração de pipeline | OK |
| Nenhuma alteração de C2/C3/DV3 | OK |
| Nenhuma alteração de BIPs | OK |
| Nenhuma alteração de pré-registro | OK |
| Nenhuma alteração de artefatos LOCKED | OK |
| Nenhuma execução de análise estatística | OK |
| Nenhuma correção silenciosa | OK |
| Todos os erros registrados | OK (0 erros) |
| Rastreabilidade BIP × cond × réplica × seed | Mantida |

---

## 10. Decisão Final

**F2 = PASS**

- 270 reconstruções completadas e outputs validados
- 30/30 BIPs válidos → **GO** para análise confirmatória
- Nenhuma divergência detectada
- Lock íntegro, seeds íntegras, pipeline íntegro
- Análise estatística **PENDING GOVERNANCE AUTHORIZATION**

---

## Próximo Estado

```
EXECUTION COMPLETE
+
OUTPUTS VALIDATED
+
ANALYSIS PENDING GOVERNANCE AUTHORIZATION
```

**Ação requerida:** Aguardar autorização explícita da governança para iniciar F3 (análise estatística).

---

**Assinatura:** F2 EXECUTION VALIDATION GO-8D-NC  
**Timestamp:** 2026-08-15 18:46:30  
**Lock Manifest:** `GO-8D-NC-LOCK-MANIFEST.yaml` (sha256: `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`)