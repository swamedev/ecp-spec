# D-MV-04 — NEW-CYCLE EXECUTION PACKAGE (Resolução das Divergências da Fase 1)

**Data:** 2026-08-15
**Ciclo:** Novo ciclo confirmatório (GO-8D-NC) — preparação do Lock (Fase 1)
**Status:** **APROVADO pela governança** (2026-08-15)
**Base:** `08-PRE-REGISTRATION-NEW-CYCLE.md` (v1.0 FINAL) · `D-03-PIPELINE-REDESIGN.md` ·
Fase 1 do Lock (relatório de divergências, 2026-08-15)
**Artefatos:** `GO-8D-NC/scripts/*` (implementação autocontida) · `GO-8D-NC/decisions/SEED-MASTER-DECISION.md`

---

## 1. Contexto

A Fase 1 do Lock do novo ciclo identificou divergências bloqueantes: (a) pipeline reprojetado
do novo ciclo não existia como scripts; (b) taxonomia C3 corrigida fora do escopo (GO-8C);
(c) ausência de `requirements.txt`; (d) `seed_master` não definido; (e) scripts DV3 com
`sys.path`/leituras diretas de GO-8B/GO-8C; (f) artefatos de diagnóstico fora do escopo;
(g) `__pycache__` presente.

## 2. Regra geral

**Nenhuma dependência executável de GO-8B, GO-8C ou do GO-8D anterior será aceita.**
Referências históricas podem existir apenas como proveniência/verificação, **nunca como
runtime dependency**.

## 3. Decisões formalizadas

| # | Decisão |
|---|---|
| 1 | **Pipeline do novo ciclo** implementado agora, a partir do desenho aprovado no D-03, como scripts **autocontidos** em `GO-8D-NC/scripts/`. |
| 2 | **Taxonomia C3** copiada de `GO-8C/scripts/C3_TAXONOMY.yaml` → `GO-8D-NC/scripts/C3_TAXONOMY.yaml`, **sem modificação**, com registro de proveniência e SHA-256 da origem. |
| 3 | **requirements.txt** criado para o novo ciclo, com dependências fixadas. |
| 4 | **seed_master do novo ciclo = `20260816`** (próxima data sequencial; distinto de todos os anteriores). Registrado em `GO-8D-NC/decisions/SEED-MASTER-DECISION.md` **antes** de qualquer geração de seeds. |
| 5 | **Scripts DV3** revisados para remover qualquer `sys.path` ou leitura direta de arquivos de GO-8B/GO-8C; todo o necessário reside no novo ciclo. |
| 6 | **analysis/ de diagnóstico** do GO-8D anterior **fica fora do Lock**. |
| 7 | **__pycache__** removido antes da nova Fase 1. |

## 4. Escopo do Lock (desta etapa)

**Incluir (scripts do novo ciclo):** `wl_kernel.py` · `graph_from_reconstruction.py` ·
`pilot_engine.py` · `validate_data.py` · `analyze.py` · `generate_seeds.py` ·
`requirements.txt` · `C3_TAXONOMY.yaml` · `C2_PERMUTATION.yaml` (cópia) ·
`test_conformity.py` · decisões D-MV-04/SEED-MASTER · pré-registro v1.0.

**NÃO incluir (ainda):** materiais de entrada dos 30 BIPs (produzidos e validados depois) ·
dados experimentais · artefatos de GO-8B/GO-8C/GO-8D (exceção: cópias de taxonomia com
proveniência).

## 5. Conformidade verificada (relatório)

- **Proveniência C3:** SHA-256 da cópia = `5ba63db7a81c454d7432873c184d2171741f8676e70d94cc538594627819bec8`
  (idêntico a `GO-8C/scripts/C3_TAXONOMY.yaml`, taxonomia corrigida D-03.7, 12 nós/13 arestas).
- **Proveniência C2:** SHA-256 da cópia = `c91fecfeae83d9edb88dd16f2d1827283e308b53fdd6bf0a02c4b636a376b2a2`
  (idêntico a `GO-8B/operational/C2_PERMUTATION.yaml`, usado pela calibração DV3 no GO-8D).
- **Testes de conformidade:** `GO-8D-NC/scripts/test_conformity.py` (T1 autocontenção, T2
  proveniência, T3 fórmula DV3, T4 WL rotulado, T5 embeddings corrigidos, T6 referência comum,
  T7 rastreabilidade de taxonomia, T8 re-derivação reproduz DV3 da calibração).
- **Sem dependência executável:** nenhum script lê GO-8B/GO-8C/GO-8D em runtime; taxonomias são
  cópias locais; embeddings derivados do modelo congelado (sentence-transformers).

## 6. Restrições desta etapa

- **Não** executar Lock, **não** gerar seeds finais (script fornecido, execução aguarda
  autorização), **não** rodar experimento.
- Nenhum arquivo congelado de GO-8B/GO-8C/Lock GO-8D alterado.

---

**Fim do relatório D-MV-04. 2026-08-15. Aprovado pela governança.**
