# PROTOCOLO NT-05-AUTOMATED-INDEPENDENT-REVIEW

**Data:** 2026-08-12
**Origem:** Decisão NC-01 (HUMAN-REVIEW SUBSTITUTION) — 2026-08-12
**Status do protocolo:** v1 — PRIMEIRA EXECUÇÃO

---

## 1. Objetivo

Verificar objetivamente os artefatos operacionais que estariam sujeitos ao gate NT-05 (revisão humana de 3 validadores independentes), mediante auditoria automatizada independente com dupla execução e critérios PASS/FAIL objetivos.

**Esta auditoria NÃO substitui a revisão humana.** É um mecanismo operacional limitado e auditável, sem equivalência epistemológica com a revisão humana de três validadores independentes.

---

## 2. Regra de Independência (Obrigatória)

- A auditoria será executada **DUAS VEZES** em contextos independentes.
- Se possível, usar modelos/ferramentas diferentes. Caso contrário: zerar contexto, usar prompts ligeiramente distintos, executar separadamente.
- **Divergência entre as duas execuções = STOP imediato** (não votação, não média).
- Qualquer divergência deve ser reportada e investigada antes de prosseguir.
- Esta execução = **PRIMEIRA EXECUÇÃO**. A segunda será agendada após revisão desta.

---

## 3. Áreas de Verificação e Critérios PASS/FAIL

### 3.1 C2 — Permutação e Mapping

| Item | Verificação | Critério PASS | Evidência esperada |
|---|---|---|---|
| C2-01 | Reproduzir `C2_PERMUTATION.yaml` a partir do JSON §6 de `02-C2-PERMUTATION.md` | Arquivo reproduzido byte-a-byte | Hash SHA-256 coincide com `scripts/go8b/operational/C2_PERMUTATION.yaml` |
| C2-02 | Verificar mapping canônico → opaco | 9 entradas, biunívoco, `[1,5,6,3,7,0,4,8,2]` | Lista impressa = esperada |
| C2-03 | Verificar inversa verdadeira (opaco → canônico) | `[5,0,8,3,6,1,2,4,7]` | Lista impressa = esperada |
| C2-04 | Verificar namespaces C1(ECP)/C2(CAT)/C3(SYN)/C4(NULL) | Presentes e corretos | YAML contém os 4 namespaces |
| C2-05 | Confirmar P1-C2-01 implementado (tabela/JSON §6 como fonte) | `derived_from: 02-C2-PERMUTATION.md §6 (frozen)` presente | Campo presente no YAML |
| C2-06 | NÃO reabrir decisão P1-C2-01 | Nenhuma alteração no YAML que contradiga Opção A | Verificação negativa = PASS |

---

### 3.2 C3 — Taxonomia Sintética e BIP-VAL

| Item | Verificação | Critério PASS | Evidência esperada |
|---|---|---|---|
| C3-01 | Validar isolamento SYN | Namespace `SYN-XXX` exclusivo; sem categorias `CAT-XX` no YAML | Zero referências `CAT-` no `C3_TAXONOMY.yaml` |
| C3-02 | Ausência de mapping ECP↔SYN | Zero referências a ECP/ECP-000..010/C1/CAT no YAML | Zero ocorrências |
| C3-03 | Validar taxonomia contra especificação congelada | Estrutura DAG válida; 12 nós / 13 arestas; labels `SYN-XXX` | Schema validation PASS |
| C3-04 | Registrar FINDING-BIP-VAL-01 sem apagá-lo | `FINDING-BIP-VAL-01` referenciado ou preservado | Menção no relatório ou arquivo intacto |
| C3-05 | NT-01..04 confirmados PASS | `BIP-VAL_REPORT.yaml` → NT-01..04 = PASS | YAML mostra PASS |
| C3-06 | NT-05 status = PENDING (substituído por este protocolo) | `BIP-VAL_REPORT.yaml` → NT-05 = PENDING com nota de substituição | YAML mostra PENDING |

---

### 3.3 GFR — GraphFromReconstruction

| Item | Verificação | Critério PASS | Evidência esperada |
|---|---|---|---|
| GFR-01 | Executar `p3_tests_gfr.py` (T-GFR-01..21) | 21/21 PASS | Log de testes |
| GFR-02 | Verificar `taxonomy_namespace` em outputs | Apenas `SYN-XXX` (zero `CAT-`, zero `ECP-`) | Output inspecionado |
| GFR-03 | Verificar rejeição de `NAMESPACE_MIX` | Testes de rejeição PASS | Log de testes |

---

### 3.4 WL — Kernel e Embeddings

| Item | Verificação | Critério PASS | Evidência esperada |
|---|---|---|---|
| WL-01 | Executar `p4_tests_wl.py` (T-WL-01..12) | 12/12 PASS | Log de testes |
| WL-02 | Verificar anonimização | Node labels = neutros; edge labels = in/out | Output inspecionado |
| WL-03 | Verificar separação S_struct / S_sem | Duas métricas computadas separadamente | Código/log mostra separação |
| WL-04 | Ausência de dependência indevida de ECP | Zero referências a ECP/ECP-000..010 no código/output | Zero ocorrências |

---

### 3.5 Materiais de Entrada (P5 — 7 BIPs)

| Item | Verificação | Critério PASS | Evidência esperada |
|---|---|---|---|
| MAT-01 | 7/7 BIPs têm materiais | BIP-001..007 diretórios existem com narrativa + atomic facts | Lista de diretórios |
| MAT-02 | Hashes das fontes registrados | `00-index.md` tem SHA-256 de cada fonte bruta | Tabela SHA-256 preenchida |
| MAT-03 | Rastreabilidade dos atomic facts | Cada fato termina com `[ref]` válido em `00-index.md` | 100% traceabilidade |
| MAT-04 | Validações lexicais zero ECP | `validate_bip00*.py` → 0 hits ECP (52 termos) | Log PASS |
| MAT-05 | FINDING-BIP-VAL-01 registrado e NÃO apagado | Arquivo `decisions/FINDING-BIP-VAL-01.md` existe intacto | Arquivo existe |

---

### 3.6 Reprodutibilidade

| Item | Verificação | Critério PASS | Evidência esperada |
|---|---|---|---|
| REP-01 | Reexecutar `p_run_consolidated.py` | 5/5 suítes PASS (P1..P4) | Log consolidado |
| REP-02 | Comparar resultados com execução anterior | Hashes dos outputs operacionais coincidem | SHA-256 coincidem |
| REP-03 | Registrar hashes dos outputs operacionais | SHA-256 de `C2_PERMUTATION.yaml`, `C3_TAXONOMY.yaml`, `BIP-VAL_REPORT.yaml`, `EMBEDDINGS.npy`, etc. | Lista de hashes |
| REP-04 | Confirmar ausência de acesso a dados fora do escopo | Zero leitura de dados experimentais reais; apenas sintéticos | Verificação de imports/IO |

---

## 4. Critérios PASS/FAIL Globais

| Resultado | Condição |
|---|---|
| **PASS** | TODOS os itens das 6 áreas = PASS |
| **FAIL** | QUALQUER item = FAIL → STOP imediato, reporte detalhado |
| **DIVERGÊNCIA** | Segunda execução discorda da primeira → STOP, não votação |

---

## 5. Formato do Relatório de Execução

Para cada área, reportar:

```
ÁREA: [C2 / C3 / GFR / WL / MATERIAIS / REPRODUTIBILIDADE]
STATUS: [PASS / FAIL]
ITENS:
  - [ITEM-ID]: [PASS/FAIL] — evidência/resumo
  ...
OBSERVAÇÕES: [se houver]
```

Ao final:
```
RESULTADO PRIMEIRA EXECUÇÃO: [PASS / FAIL]
PRÓXIMO PASSO: [SEGUNDA EXECUÇÃO AGENDADA / STOP E INVESTIGAÇÃO]
```

---

## 6. Regras Inabaláveis

- Núcleo congelado (00–08) intocável.
- Todas as escritas em diretórios fora do núcleo (`scripts/go8b/operational/`, `experiments/validation/GO-8B/decisions/`, `experiments/validation/GO-8B/pilot-input/`).
- Registrar cada passo em `decisions/ACTION-REGISTER.md`.
- **Não executar segunda auditoria** até revisão desta execução.
- **Não atribuir equivalência** entre esta auditoria e revisão humana NT-05 original.