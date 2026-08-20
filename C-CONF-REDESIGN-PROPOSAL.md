# C-CONF-REDESIGN-PROPOSAL.md

**Hash do documento (após escrita, será registrado no commit):** a ser preenchido

---

## 1. Contexto e Motivação

A métrica `conf` original (v1/v2/v3) mede F1 entre a reconstrução de um estado e **seu próprio grafo de verdade** (§7.4). Isso cria um problema estrutural no par V0×V1:

- `conf(V0) = F1(reconstrução(V0), G0)` → V0 reconstrói G0 perfeitamente → `conf ≈ 1.0`
- `conf(V1) = F1(reconstrução(V1), G1)` → V1 reconstrói G1 (G0 + 3 fatos verdadeiros) perfeitamente → `conf ≈ 1.0`
- O termo de `conf` **não discrimina V0 de V1** porque cada estado é medido contra seu próprio teto, que cresce junto com o conteúdo.

Resultado observado na v3: `conf(V0)=1.0000`, `conf(V1)=1.0000`, gap de `conf` no par V0×V1 = 0.0000. A discriminação residual veio apenas de `ged_ref` e `div_metric` (pesos 0.2 cada), insuficiente para passar o piso de 0.05.

---

## 2. Hipótese de Redesenho — `conf_v2`

**Definição:** Comparar **todos os estados contra um grafo de verdade fixo e máximo** — o grafo de verdade de V1 (`G1 = G0 + ΔV1_true`), que representa o teto de conteúdo verdadeiro conhecido no caso.

```
conf_v2(estado) = F1(reconstrução(estado), G1)    onde G1 = truth_graphs[case_id]["V1"]
```

**Intuição do comportamento esperado:**

| Estado | Conteúdo vs G1 | `conf_v2` esperado |
|--------|----------------|--------------------|
| V1     | Tem todo G1 (reconstrução ≈ G1) | Recall alto, Precisão alta → **alto** |
| V0     | Tem G0 (subconjunto de G1), falta ΔV1 | Recall **menor** (faltam 3 fatos), Precisão alta → **médio** |
| V2     | Tem G0 + redundância (não fatos novos de ΔV1) | Recall menor (não tem ΔV1 verdadeiros), Precisão pode cair (redundância não está em G1) → **médio/baixo** |
| V3     | Tem G0 + ruído (fatos falsos não estão em G1) | Recall menor, **Precisão penalizada** (ruído extra) → **baixo** |

Crucial: `conf_v2` captura **quantidade de valor recuperado** (recall contra teto fixo) **e** penaliza conteúdo espúrio (precisão contra teto fixo). `conf` original só capturava fidelidade ao próprio teto.

---

## 3. Implementação Realizada (Diagnóstico)

**Arquivo:** `measurement-redesign/phase4-v3/scripts/metric.py` (adicionado `conf_v2_m` e computado junto ao `conf` original, **sem alterar DV_P/DV_Q** do pré-registro v3).

Executado sobre os **mesmos 24 casos da v3** (hash-locked, sem regeneração) para diagnóstico comparativo.

---

## 4. Resultado da Checagem de Sanidade (Empírica nos 24 casos v3)

### 4.1 Valores observados (média ± range)

| Estado | conf_v2 (média) | conf_v2 (min–max) |
|--------|-----------------|-------------------|
| V0     | 0.8971          | 0.8814 – 0.9352   |
| V1     | 1.0000          | 1.0000 – 1.0000   |
| V2     | 0.8508          | 0.8286 – 0.8875   |
| V3     | **0.9887**      | **0.9328 – 1.0000** |

### 4.2 Análise dos gaps críticos

| Par | Gap conf_v2 (mediana) | Piso 0.05? |
|-----|----------------------|------------|
| V1 − V0 | **+0.103** | ✅ PASS |
| V1 − V2 | **+0.149** | ✅ PASS |
| V0 − V3 | **−0.092** (V3 > V0) | ❌ FAIL |
| V2 − V3 | **−0.138** (V3 > V2) | ❌ FAIL |

**O `conf_v2` NÃO resolve a discriminação V0×V3 nem V2×V3** — V3 pontua **acima** de V0 e V2 na maioria dos casos (em 10/24 casos, `conf_v2(V3) = 1.0000` idêntico a V1).

---

## 5. Diagnóstico da Causa Raiz (Não Prevista na Hipótese)

A hipótese assumia que G1 = `truth_graphs[case_id]["V1"]` seria consistentemente **G0 + 3 novas categorias (MRCAT-10,11,12)**. Na prática:

1. **O classificador hash-fallback tem imperfeições conhecidas** (49 issues de classificação na geração dos casos, distribuição similar v2/v3).
2. Os fatos V1 *intencionados* para NEW_CATS (MRCAT-10,11,12) **frequentemente classificam em BASE_CATS** (MRCAT-01..09) pelo engine congelado.
3. Quando o engine reconstrói os fatos V1 para construir G1 (`reconstruction.py` linha 329-330), **G1 não ganha as 3 novas categorias** — fica com as mesmas 9 categorias de G0.
4. **Consequência:** quando G1 = G0 (sem categorias novas), **V0 e V3 cobrem G1 perfeitamente** → `conf_v2 = 1.0` para ambos (zero discriminação).
5. Mesmo quando G1 tem as novas categorias, **os fatos V3 são corrupções de fatos-base** → classificam em BASE_CATS → V3 não introduz categorias fora de G1 → **precisão não é penalizada** → V3 ≈ V0 contra G1.

### 5.1 Verificação das 4.1–4.3 da Proposta Original

| Item | Previsão | Realidade |
|------|----------|-----------|
| 4.1 `conf_v2(V0)` não infla | Recall < 1 expõe ausência ΔV1 | **Parcial**: quando G1 tem ΔV1, sim; quando G1 não tem (classificador falha), V0=1.0 |
| 4.2 Sem circularidade | G1 vem do gerador, não da reconstrução | **Mantém-se**: G1 = `reconstruct_facts(V1_facts_do_gerador)` — fluxo unidirecional OK |
| 4.3 `conf_v2(V3)` penalizado por precisão | Ruído V3 cria categorias fora de G1 | **FALHA**: ruído V3 é corrupção de base → mesmas BASE_CATS → precisão = 1.0 |

---

## 6. Conclusão da Fase 1

**A hipótese `conf_v2` NÃO FUNCIONA** com o gerador + engine congelado atuais.

- O componente **separa V1 de V0/V2** (gap > 0.10), o que é progresso sobre o `conf` original.
- Mas **não separa V0 de V3 nem V2 de V3** — V3 "parece verdadeiro" contra G1 porque seu ruído não escapa das categorias-base.
- Isso é uma limitação **estrutural do par gerador/classificador**, não de ponderação: o engine não distingue semanticamente "fato-base corrompido" de "fato-base limpo" no espaço de categorias MRCAT.

**Não há caminho viável para v4 com este desenho de `conf_v2`.** Qualquer métrica baseada apenas nas categorias MRCAT colapsadas pelo engine hash-fallback terá essa limitação: V3 é indistinguível de V0 no nível de categorias.

---

## 7. Próximo Passo Recomendado (Freio Explícito)

**Não prosseguir para Fase 2 (v4 pre-registro).** Em vez disso, criar **`M-REDESIGN-01-FECHAMENTO-FORMAL.md`** documentando:

1. Cadeia completa: v1 (viés circular) → v2 (gerador consertado, diluição agregação) → v3 (reponderação não resolve zero estrutural de `conf` V0×V1) → v4 tentado via `conf_v2` (falha por limitação gerador/classificador).
2. Conclusão honesta: com os componentes disponíveis (conf, ged_ref, div_metric) e o engine/classificador congelados, **DV-REDESIGN não atinge validade discriminante de valor no eixo "nada vs. valor real adicionado"**.
3. GO-8E permanece não autorizado por decisão fundamentada, não por esgotamento de tentativas.
4. Lição: a discriminação de "valor adicionado" requer capacidades semânticas além do namespace MRCAT-01..12 + hash-fallback — fora de escopo deste programa.

---

## 8. Arquivos Modificados Neste Diagnóstico

- `measurement-redesign/phase4-v3/scripts/metric.py` — adicionado `conf_v2_m` e output diagnóstico (campo `"conf_v2"` em `dv_values.json`). **DV_P/DV_Q inalterados.**
- `C-CONF-REDESIGN-PROPOSAL.md` — este documento (atualizado com resultados).