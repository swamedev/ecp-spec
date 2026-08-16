# RELATÓRIO DE AUDITORIA DO PIPELINE — GO-8B

**Data:** 2026-08-12
**Decisor:** Auditor Independente (INDEPENDENT AUDITOR)
**Status:** **STOP IMEDIATO** — Limitação técnica identificada

---

## 1. Resultado da Auditoria do Pipeline

**Status:** ✅ **LIMITAÇÃO TÉCNICA IDENTIFICADA**

O pipeline atual `p_run_consolidated.py` **NÃO executa o piloto GO-8B**.

### O que o pipeline faz atualmente

O arquivo `scripts/go8b/operational/p_run_consolidated.py` (37 linhas):

```python
suites = {
    "C2 (P1)": "p1_c2_permutation.py",
    "C3 (P2)": "p2_c3_taxonomy.py",
    "BIP-VAL (P2)": "p2_bip_val_report.py",
    "GFR (P3)": "p3_tests_gfr.py",
    "WL (P4)": "p4_tests_wl.py",
}
```

**O pipeline apenas executa SUÍTES DE TESTES EXISTENTES**, que validam:
- C2_PERMUTATION.yaml (mapping, inversa, namespaces)
- C3_TAXONOMY.yaml (DAG, nodes/edges, ECP refs)
- BIP-VAL_REPORT.yaml (NT-01..NT-05)
- GFR tests (p3_tests_gfr.py)
- WL tests (p4_tests_wl.py)

**O pipeline NÃO:**
- Lê os materiais de entrada `pilot-input/BIP-XXX/narrative/` e `pilot-input/BIP-XXX/atomic-facts/`
- Aplica GraphFromReconstruction sobre as narrativas
- Aplica WL Kernel sobre os atomic facts
- Gera saídas diferentes para condições A, B, C
- Usa as 63 seeds registradas em SEEDS-PILOT-GO-8B.md

---

## 2. Estado dos Materiais de Entrada (Verificados)

✅ **Arquivos existentes e com conteúdo real:**

| BIP | Diretório | Narrative | Atomic Facts | Conteúdo Real |
|-----|-----------|-----------|--------------|---------------|
| BIP-001 | `BIP-001-deepwater/` | ✅ 78 linhas (01-narrativa-original.md) | ✅ 77 linhas (02-atomic-facts.md) | Deepwater Horizon incident |
| BIP-002 | `BIP-002-hyatt/` | ✅ | ✅ | Hyatt hotel incident |
| BIP-003 | `BIP-003-ows/` | ✅ | ✅ | OWS incident |
| BIP-003 | `BIP-003-warpspeed/` | ✅ | ✅ | Warp Speed incident |
| BIP-004 | `BIP-004-genoma/` | ✅ | ✅ | Genoma incident |
| BIP-005 | `BIP-005-evergiven/` | ✅ | ✅ | Ever Given incident |
| BIP-006 | `BIP-006-i35w/` | ✅ | ✅ | I35W bridge incident |
| BIP-007 | `BIP-007-ebola/` | ✅ | ✅ | Ebola outbreak |

**Conteúdo verificado no arquivo narrative BIP-001:**
- 78 linhas
- Conteúdo detalhado sobre Deepwater Horizon / Macondo
- Referências a fontes reais (`csb-01-macondo-v1`, `ncom-01-gulf`, `jit-01-report`)
- Linhas históricas ordenadas
- Zero termos ECP (conforme especificação)

**Conteúdo verificado no arquivo atomic facts BIP-001:**
- 77 linhas
- 39 fatos atômicos (linhas 1-39)
- Cada fato termina com `[refs...]`
- Zero termos ECP
- Conteúdo consistente com a narrativa

---

## 3. Resultado do Piloto (Atenção: Sintético, Não Real)

⚠️ **O arquivo `pilot_results.csv` atual contém dados SINTÉTICOS CONSTANTES, não derivados dos materiais de entrada.**

### Evidências de sintetização constante

| Coluna | Valor em todas as 63 linhas |
|--------|----------------------------|
| `s_struct` | 0.8523 |
| `s_sem` | 0.7619 |
| `schema` | "valid" |
| `nodes` | 12 |
| `edges` | 13 |
| `namespace` | "SYN" |

**Conclusão:** Os valores são constantes, indicando geração artificial e não processamento real dos materiais de entrada.

---

## 4. Limitações Técnicas Identificadas

Para executar o piloto GO-8B com dados reais, são necessários componentes que **NÃO EXISTEM** no códigobase atual:

### 4.1 GraphFromReconstruction Parser

**Necessário:** Parser que possa:
- Ler o arquivo `01-narrativa-original.md` (e arquivos similares dos outros BIPs)
- Ler o arquivo `02-atomic-facts.md`
- Extrair entidades, relações e estruturas do texto
- Criar grafo de reconstrução

**Status:** ❌ **NÃO IMPLEMENTADO**

Arquivos existentes com código que tenta processar gráficos (`p3_tests_gfr.py`, `p4_tests_wl.py`) validam apenas os artefatos operacionais existentes (C2_PERMUTATION.yaml, C3_TAXONOMY.yaml), não os materiais de entrada.

### 4.2 WL Kernel Implementation

**Necessário:** Implementação que:
- Processa os atomic facts extraídos
- Calcula embeddings semânticos
- Calcula métricas estruturais e semânticas
- Gera valores variados para s_struct e s_sem

**Status:** ❌ **NÃO IMPLEMENTADO**

O arquivo `p4_tests_wl.py` apenas executa testes sobre dados existentes, não processa novos fatos.

### 4.3 Lógica de Condições A/B/C

**Necessário:** Implementação que:
- Para **Condição A**: Usa apenas atomic facts (modo cego puro)
- Para **Condição B**: Usa atomic facts + C3_TAXONOMY.yaml (modo cego com taxonomia)
- Para **Condição C**: Usa apenas narrativa (modo não-cega)
- Para cada execução, aplica as 3 seeds registradas em SEEDS-PILOT-GO-8B.md

**Status:** ❌ **NÃO IMPLEMENTADO**

O pipeline atual não tem essa lógica.

### 4.4 Seeds Parameterization

**Necessário:** Implementação que:
- Lê as 63 seeds de SEEDS-PILOT-GO-8B.md
- Usa cada seed como entrada para o processamento
- Gera outputs diferentes para cada seed

**Status:** ❌ **NÃO IMPLEMENTADO**

O pipeline atual não usa as seeds.

---

## 5. Próximos Passos (Recomendados pela Governança)

### Opção A: Implementação Completa (Recomendada)

Criar novos componentes necessários:

1. **GraphFromReconstruction.py**
   - Parser que lê narrative.md e atomic_facts.md
   - Extrai entidades, relações e estrutura
   - Gera grafo reconstruído
   - Usa seeds como parâmetros de aleatoriedade

2. **WL_Implementation.py**
   - Processa atomic facts e calcula embeddings
   - Calcula S_struct e S_sem
   - Implementa lógica de condições A/B/C
   - Usa seeds como parâmetros de aleatoriedade

3. **Pilot_Engine.py**
   - Orquestra as 63 execuções
   - Lê SEEDS-PILOT-GO-8B.md
   - Para cada BIP e condição, executa 3 vezes com 3 seeds diferentes
   - Gera pilot_results.csv real
   - Valida schema, limites [0,1], NAMESPACE_MIX

4. **Execution_Log.md**
   - Registra cada execução detalhadamente
   - Inclui BIP, condição, seed, s_struct, s_sem, status

**Tempo estimado:** ~4-6 horas de desenvolvimento completo

### Opção B: Restringir Piloto a Execução de Testes Existentes

Se a governança decidir que **NÃO é necessário executar o piloto GO-8B** e que a validação das SUÍTES EXISTENTES (C2, C3, GFR, WL) já é suficiente:

1. Manter `p_run_consolidated.py` como está
2. Remover o arquivo `pilot_results.csv` (sintético)
3. Manter as decisões NC-01..NC-07 (validação do NT-05)
4. Não executar piloto GO-8B

**Justificativa:** As suítes de teste C2, C3, GFR, WL já validam os artefatos operacionais existentes.

---

## 6. Declaração da Governança

**Decision required:**

1. **Vale a pena implementar** os componentes necessários (Opção A)?
   - Pro: Piloto GO-8B real com dados derivados dos materiais de entrada
   - Contra: Tempo estimado 4-6 horas, necessidade de desenvolver novos componentes complexos

2. **É suficiente** validar apenas as suítes existentes (Opção B)?
   - Pro: Já validamos C2, C3, GFR, WL com sucesso
   - Contra: Não executamos o piloto GO-8B real, não temos evidência de processamento de narrativas e atomic facts

3. **Existe outra opção**?

---

## 7. Regras Inabaláveis Aplicadas

✅ **Núcleo congelado (00–08) intocável**
✅ **Nenhum dado experimental produzido** — stop imediato para evitar dados falsos
✅ **Zero atalhos** — dados sintéticos não aceitáveis para piloto
✅ **Registro claro da limitação técnica**

---

**Fim do relatório. STOP IMEDIATO aguardando decisão da governança.**