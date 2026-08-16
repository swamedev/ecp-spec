# PRE-FLIGHT-REPORT-GO-8D-NC

**Data**: 2026-08-15
**Status**: FAIL
**Governança**: Autorização exclusiva PRE-FLIGHT OPERACIONAL (GO-8D-NC)

---

## 1. Verificação dos 30 BIPs (12 herdados + 18 novos)

### 18 BIPs novos (013–030) — GO-8D-NC
| BIP | Caso | Narrativa | Atomic Facts | Lexicon (ECP) | Traceability | Status |
|-----|------|-----------|--------------|---------------|--------------|--------|
| 013 | Bhopal (1984) | 8 seções | 188 fatos | PASS (0) | PASS | **PASS** |
| 014 | Three Mile Island (1979) | 9 seções | 195 fatos | PASS (0) | PASS | **PASS** |
| 015 | Challenger (1986) | 9 seções | 147 fatos | PASS (0) | PASS | **PASS** |
| 016 | Columbia (2003) | 8 seções | 221 fatos | PASS (0) | PASS | **PASS** |
| 017 | Katrina / Nova Orleans (2005) | 11 seções | 290 fatos | PASS (0) | PASS | **PASS** |
| 018 | Flint Water Crisis (2014–16) | 11 seções | 160 fatos | PASS (0) | PASS | **PASS** |
| 019 | Fukushima Daiichi (2011) | 12 seções | 240 fatos | PASS (0) | PASS | **PASS** |
| 020 | Grenfell Tower (2017) | 11 seções | 200 fatos | PASS (0) | PASS | **PASS** |
| 021 | Vajont Dam (1963) | 9 seções | 145 fatos | PASS (0) | PASS | **PASS** |
| 022 | Boeing 737 MAX (2018–19) | 12 seções | 211 fatos | PASS (0) | PASS | **PASS** |
| 023 | Mariana Dam (2015) | 8 seções | 150 fatos | PASS (0) | PASS | **PASS** |
| 024 | Dieselgate / Volkswagen (2015) | 5 seções | 50 fatos | PASS (0) | PASS | **PASS** |
| 025 | Wells Fargo (2016) | 8 seções | 120 fatos | PASS (0) | PASS | **PASS** |
| 026 | Theranos (2018) | 6 seções | 110 fatos | PASS (0) | PASS | **PASS** |
| 027 | Opioides / Purdue (2020) | 10 seções | 100 fatos | PASS (0) | PASS | **PASS** |
| 028 | Enron (2001–02) | 8 seções | 50 fatos | PASS (0) | PASS | **PASS** |
| 029 | Takata Airbags (2017) | 7 seções | 60 fatos | PASS (0) | PASS | **PASS** |
| 030 | Costa Concordia (2012) | 9 seções | 63 fatos | PASS (0) | PASS | **PASS** |

**Subtotal novos**: 18/18 PASS — **zero ECP terms**, **100% traceability**.

---

### 12 BIPs herdados (001–012) — GO-8C/study-input
| BIP | Caso | Narrativa | Atomic Facts | Lexicon (ECP) | Traceability | Status |
|-----|------|-----------|--------------|---------------|--------------|--------|
| 001 | Deepwater Horizon (2010) | ✓ | ✓ | PASS (0) | **FAIL** (`refs...`) | **FAIL** |
| 002 | Hyatt Regency (1981) | ✓ | ✓ | PASS (0) | **FAIL** (`refs...`) | **FAIL** |
| 003 | OWS (2011) | ✓ | ✓ | PASS (0) | PASS | **PASS** |
| 004 | Genoma (2000) | ✓ | ✓ | PASS (0) | **FAIL** (`refs...`) | **FAIL** |
| 005 | Ever Given (2021) | ✓ | ✓ | PASS (0) | **FAIL** (`refs...`) | **FAIL** |
| 006 | I-35W Bridge (2007) | ✓ | ✓ | PASS (0) | **FAIL** (`refs...`) | **FAIL** |
| 007 | Ebola (2014) | **AUSENTE** | **AUSENTE** | — | — | **FAIL** |
| 008 | Apollo 13 (1970) | ✓ | ✓ | PASS (0) | PASS | **PASS** |
| 009 | Chernobyl (1986) | ✓ | ✓ | PASS (0) | PASS | **PASS** |
| 010 | Tacoma Narrows (1940) | ✓ | ✓ | PASS (0) | PASS | **PASS** |
| 011 | Domino's (2009) | ✓ | ✓ | PASS (0) | PASS | **PASS** |
| 012 | Eyjafjallajökull (2010) | ✓ | ✓ | PASS (0) | PASS | **PASS** |

**Detalhes das falhas de traceabilidade (BIPs 001, 002, 004, 005, 006)**:
- O arquivo `atomic-facts/02-atomic-facts.md` contém no cabeçalho o placeholder literal `[refs...]` (linha 6: `cada fato termina com \`[refs...]\``) que **não corresponde a nenhum `ref` no `00-index.md`**.
- Os fatos individuais usam refs válidos (ex.: `[csb-01-macondo-v1]`), mas o placeholder no cabeçalho é detectado pelo validador como ref ausente.

**BIP-007-ebola**: Completamente ausente (sem diretório, sem narrativa, sem atomic facts, sem index).

**Subtotal herdados**: 6/12 PASS, 6/12 FAIL.

---

### Resumo consolidado (30 BIPs)
| Categoria | Total | PASS | FAIL |
|-----------|-------|------|------|
| Novos (013–030) | 18 | 18 | 0 |
| Herdados (001–012) | 12 | 6 | 6 |
| **TOTAL** | **30** | **24** | **6** |

---

## 2. Pipeline e Dependências

| Item | Verificação | Resultado |
|------|-------------|-----------|
| Scripts autocontidos | `scripts/analyze.py`, `pilot_engine.py`, `graph_from_reconstruction.py`, `wl_kernel.py`, `validate_data.py`, `test_conformity.py`, `generate_seeds.py`, `calibration_fixture.json` | **OK** — todos presentes em `GO-8D-NC/scripts/` |
| `requirements.txt` | Versões fixadas (numpy==1.26.4, scipy==1.15.3, pandas==3.0.5, PyYAML==6.0.2, jsonschema==4.25.0, sentence-transformers==3.3.1) | **OK** — hash SHA-256 confere com lock manifest: `a5b89472b8ad341bc9308a9dfcd4e7ba3a8dd182dd3e56b6f0a6e4933ef851c5` |
| C2 (CAT) — `C2_PERMUTATION.yaml` | Proveniência: SS6 (GO-8B lock), `seed_operacional=258915`, mapeamento bijetivo validado (T-C2-MAP-01..07 PASS) | **OK** — hash confere: `c91fecfeae83d9edb88dd16f2d1827283e308b53fdd6bf0a02c4b636a376b2a2` |
| C3 (SYN) — `C3_TAXONOMY.yaml` | DAG 12 nós / 13 arestas, corpus FRAM/STAMP/ISO, `seed_generation_applied: false`, validações NT-01..04 PASS | **OK** — hash confere: `5ba63db7a81c454d7432873c184d2171741f8676e70d94cc538594627819bec8` |
| Pré-registro | `GO-8D/08-PRE-REGISTRATION-NEW-CYCLE.md` v1.0 FINAL | **OK** — hash confere: `12fef4f74431b94fa0eacc8a170e2ad16192c871bc524464d5ddf0535fa5fcd1` |

---

## 3. Ausência de Transitórios

| Tipo | Verificação | Resultado |
|------|-------------|-----------|
| `__pycache__` | Busca recursiva em `GO-8D-NC/` e `GO-8C/` | **OK** — nenhum encontrado |
| Arquivos `*.log` | Busca em `GO-8D-NC/` | **OK** — nenhum encontrado |
| Arquivos `*.tmp` / `*.temp` | Busca em `GO-8D-NC/` | **OK** — nenhum encontrado |
| Diretórios temporários | `C:\Users\swame\AppData\Local\Temp\opencode\` (fora do escopo LOCKED) | **OK** — apenas artefatos de extração/render, não transitórios de execução |

---

## 4. Capacidade do Ambiente (30 × 3 × 3 = 270 execuções)

| Requisito | Verificação | Resultado |
|-----------|-------------|-----------|
| 30 BIPs com narrativa + atomic facts | 24/30 completos (6 herdados com falha) | **PARCIAL** — 18 novos OK, 6 herdados OK, 6 herdados FAIL |
| 3 condições (A, B, C) | Scripts `analyze.py`, `pilot_engine.py`, `graph_from_reconstruction.py` suportam C1/C2/C3 | **OK** — código preparado |
| 3 seeds | `generate_seeds.py` presente; `C2_PERMUTATION.yaml` define `seed_operacional=258915` e `seed_registrada`; C3 `seed_generation_applied: false` | **OK** — infraestrutura de seeds existente |
| Dependências Python | `requirements.txt` fixo; `numpy`, `scipy`, `pandas`, `sentence-transformers` disponíveis no Python 3.11.9 | **OK** |

**Nota**: A capacidade teórica de 270 execuções existe no código, mas a falha nos 6 BIPs herdados bloqueia a execução completa até correção da traceabilidade.

---

## 5. Ausência de Seeds Geradas

| Verificação | Resultado |
|-------------|-----------|
| Diretório `GO-8D-NC/seeds/` | **OK** — inexistente |
| Arquivos `*.seed`, `*seed*.json`, `*seed*.csv` em `GO-8D-NC/` | **OK** — nenhum encontrado |
| Script `generate_seeds.py` executado? | **OK** — sem evidência de execução (sem outputs, sem logs) |

---

## 6. Integridade dos Artefatos Congelados (LOCK)

| Verificação | Resultado |
|-------------|-----------|
| `GO-8D-NC-LOCK-MANIFEST.yaml` — 14 artefatos | **OK** — manifest presente, `lock_status: LOCKED` |
| SHA-256 de todos os 14 arquivos | **OK** — todos conferem (verificados: `C2_PERMUTATION.yaml`, `C3_TAXONOMY.yaml`, `requirements.txt`, `08-PRE-REGISTRATION-NEW-CYCLE.md`, `analyze.py`, `pilot_engine.py`, `wl_kernel.py`, `graph_from_reconstruction.py`, `validate_data.py`, `test_conformity.py`, `generate_seeds.py`, `calibration_fixture.json`, `D-MV-04-NEW-CYCLE-EXECUTION-PACKAGE.md`, `SEED-MASTER-DECISION.md`) |
| Pré-registro não alterado | **OK** — hash SHA-256 confere com lock manifest |
| Decisões de governança não alteradas | **OK** — hashes conferem |

---

## 7. Conformidade com Regras de STOP

> **REGRA DE STOP**: "Qualquer divergência → STOP imediato e reporte. Não corrigir dentro do pre-flight."

### Divergências detectadas (6 no total):

1. **BIP-007-ebola** (herdado) — **COMPLETAMENTE AUSENTE** (sem narrativa, sem atomic facts, sem index)
2. **BIP-001-deepwater** — **TRACEABILITY FAIL**: placeholder `[refs...]` no cabeçalho do atomic-facts não está no index
3. **BIP-002-hyatt** — **TRACEABILITY FAIL**: placeholder `[refs...]` no cabeçalho do atomic-facts não está no index
4. **BIP-004-genoma** — **TRACEABILITY FAIL**: placeholder `[refs...]` no cabeçalho do atomic-facts não está no index
5. **BIP-005-evergiven** — **TRACEABILITY FAIL**: placeholder `[refs...]` no cabeçalho do atomic-facts não está no index
6. **BIP-006-i35w** — **TRACEABILITY FAIL**: placeholder `[refs...]` no cabeçalho do atomic-facts não está no index

**Nenhuma correção foi aplicada** dentro deste pre-flight (conforme regra de STOP).

---

## 8. Decisão Final

**PRE-FLIGHT GO-8D-NC → FAIL**

### Justificativa
Embora os 18 BIPs novos (013–030) estejam **totalmente conformes** (zero ECP, 100% traceabilidade), e a infraestrutura de pipeline, dependências, ausência de transitórios, capacidade de ambiente, ausência de seeds e integridade do lock estejam **todas OK**, a existência de **6 divergências nos 12 BIPs herdados** (1 ausente + 5 com falha de traceabilidade por placeholder `[refs...]`) aciona a **REGRA DE STOP**.

### Próximos passos (fora do pre-flight)
1. Corrigir/criar BIP-007-ebola (narrativa + atomic facts + index) no GO-8C/study-input.
2. Remover ou substituir o placeholder `[refs...]` pelos refs válidos nos cabeçalhos de `atomic-facts/02-atomic-facts.md` dos BIPs 001, 002, 004, 005, 006.
3. Re-rodar validação completa até `RESULT: PASS` para todos os 30 BIPs.
4. Nova decisão de governança para autorizar FLIGHT OPERACIONAL.

---

**Assinatura**: PRE-FLIGHT OPERACIONAL GO-8D-NC  
**Timestamp**: 2026-08-15  
**Lock Manifest**: `GO-8D-NC-LOCK-MANIFEST.yaml` (sha256 do manifest: `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`)