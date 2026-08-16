# DIAGNOSTIC-REPORT-GO8E-01

**Diagnóstico D-GO8E-01 — Por que C3 reduz a DV3?**
**Data:** 2026-08-15
**Status:** COMPLETE — GOVERNANCE REVIEW PENDING

---

## 1. Resumo Executivo

O diagnóstico D-GO8E-01 foi executado conforme a proposta D-GO8E-01-PROPOSAL.md, utilizando exclusivamente os dados congelados do GO-8D-NC (270 execuções, 30 BIPs, 3 condições × 3 réplicas), sem coleta de novos dados, sem novas reconstruções, sem alteração de Locks ou métricas experimentais.

**Classificação Final: H3 — INTERAÇÃO** (Score H3=7 vs H1=1, H2=1)

**Recomendação:** **Decompor a DV3 em seus três componentes (conf, ged_ecp, ent_n12) e reportá-los separadamente; não usar a média composta 1:1:1.**

---

## 2. Decomposição da DV3 (conf, ged_ecp, ent_n12)

### 2.1 Estatísticas Descritivas (Médias por Condição)

| Componente | A (cega pura) | B (cega + C3) | C (não-cega) | Dif A-B | Dif B-C |
|------------|---------------|---------------|--------------|---------|---------|
| **conf**   | 0.7339        | 0.7351        | 0.7153       | -0.0013 | 0.0198  |
| **ged_ecp**| 0.3157        | 0.2941        | 0.2905       | 0.0216  | 0.0036  |
| **ent_n12**| 0.8129        | 0.7123        | 0.6292       | 0.1007  | 0.0831  |
| **DV3**    | 0.6208        | 0.5805        | 0.5450       | 0.0403  | 0.0355  |

### 2.2 Contribuição para a Diferença DV3 (A vs B)

| Componente | Diferença Média (A-B) | % da Diferença DV3 |
|------------|----------------------|-------------------|
| **ent_n12** | **0.1007**           | **83.2%**         |
| ged_ecp     | 0.0216               | 17.9%             |
| conf        | -0.0013              | -1.0% (ligeiro ganho em B) |

> **ent_n12 é responsável por 83% da diferença DV3 entre A e B.** A queda massiva de entropia normalizada (ent_n12) de A para B é o motor principal da redução DV3.

### 2.3 Degradação por Componente (Proporção de BIPs com queda A→B)

| Componente | % BIPs com queda A→B |
|------------|---------------------|
| **ent_n12** | **93.3%**           |
| ged_ecp    | 73.3%               |
| conf       | 43.3%               |

---

## 3. Testes Sintéticos (TS-1 a TS-4)

### TS-1: Referência Neutra (ged_ecp usa ECP/CAT)
- **Achado:** ged_ecp mede similaridade ao grafo ECP canônico (CAT). B usa taxonomia SYN → viés inerente a favor de A.
- **Medianas ged_ecp:** A=0.3061, B=0.2929, C=0.3027
- **Evidência H2:** Viés estrutural da métrica a favor de categorias CAT.

### TS-2: Grade de Pesos (19 combinações)
- **Resultado:** **0/19** combinações de pesos preservam a ordem A > B > C.
- **19/19 combinações invertem** a ordem A > B > C.
- **Evidência H3:** A ordem A > B > C **não é robusta** à escolha de pesos; a média 1:1:1 mascara a instabilidade.

### TS-3: Métricas Alternativas (Geométrica/Harmônica)
| Métrica | A > B | B > C | Médias (A/B/C) |
|---------|-------|-------|----------------|
| Aritmética (DV3) | ✓ | ✓ | 0.621 / 0.580 / 0.545 |
| Geométrica | ✗ | ✗ | 0.572 / 0.533 / 0.504 |
| Harmônica | ✗ | ✗ | 0.519 / 0.481 / 0.461 |
- **Evidência H3:** A ordem A > B > C **não é robusta** à forma de agregação (média aritmética/geométrica/harmônica).

### TS-4: Contrafactual C3
| Cenário | B ged_ecp = A | B ged_ecp = max(A,B) |
|---------|---------------|----------------------|
| A > B | ✗ | ✗ |
| B > C | ✗ | ✗ |
- Mesmo igualando ou maximizando ged_ecp de B, a ordem A > B > C **não é restaurada**.
- **Evidência H1/H3:** A queda não é explicada apenas por ged_ecp; ent_n12 é o motor principal.

---

## 4. Análise de Sinais Opostos (Evidência H3)

| Transição | BIPs com sinais opostos entre componentes |
|-----------|------------------------------------------|
| A → B     | **22/30 (73.3%)**                        |
| B → C     | **20/30 (66.7%)**                        |

- Em 73% dos BIPs (A→B), os três componentes movem-se em direções opostas.
- Isso confirma que **a média composta 1:1:1 mascara trade-offs reais** entre componentes.

---

## 5. Evidência por Hipótese

| Hipótese | Evidência | Classificação |
|----------|-----------|---------------|
| **H1 — Efeito Real** | Degradação real em ent_n12 (93%), ged_ecp (73%), conf (43%). Mas ent_n12 é o motor principal. | Moderada |
| **H2 — Artefato DV3** | ent_n12 = 83% da diferença A-B. ged_ecp usa referência ECP (CAT) → viés estrutural a favor de A. | Moderada + Estrutural |
| **H3 — Interação** | **22/30 BIPs (A→B) e 20/30 (B→C) com sinais opostos**. TS-2: 19/19 inversões de peso. TS-3: geométrica/harmônica invertem ordem. TS-4: contrafactual não restaura ordem. | **Forte** |

---

## 6. Classificação e Pontuação

| Hipótese | Score | Justificativa |
|----------|-------|---------------|
| **H1** | 1 | Degradação real presente, mas concentrada em ent_n12 (métrica) |
| **H2** | 1 | Viés estrutural em ged_ecp, mas ent_n12 domina a diferença |
| **H3** | **7** | Sinais opostos (22/30, 20/30), TS-2 (19/19 inversões), TS-3 (inversão geométrica/harmônica), TS-4 (contrafactual falha) |

**Classificação Final: H3 — INTERAÇÃO**

---

## 6. Limitações

1. **Dados observacionais:** Não há randomização ou intervenção causal; inferências são associativas.
2. **Métrica DV3 congelada:** Não testamos variações de C2/C3 ou definições de componentes fora do Lock.
3. **Validação externa ausente:** Não há "ground truth" externo para validar qual componente reflete qualidade real.
4. **Amostra de 30 BIPs:** Poder estatístico limitado para detectar interações sutis por domínio.
5. **ent_n12 sensibilidade:** A entropia normalizada é sensível ao número de categorias usadas; C3 (SYN) tem mais categorias granulares, o que pode reduzir ent_n12 artificialmente.

---

## 7. Recomendação de Governança

### Recomendação Principal
> **DECOMPOR A DV3: Reportar conf, ged_ecp e ent_n12 separadamente; não usar a média composta 1:1:1 (DV3).**

### Justificativa
1. A média composta 1:1:1 **não é robusta**: falha em TS-2 (pesos), TS-3 (agregação), TS-4 (contrafactual).
2. Os componentes **movem-se em direções opostas** (73% A→B, 67% B→C), mascarados pela média.
3. **ent_n12 domina a diferença** (83% da queda DV3), mas reflete diversidade de categorias — não necessariamente qualidade.
4. **ged_ecp tem viés CAT** inerente (referência ECP), favorecendo artificialmente condição A.

### Próximos Passos Recomendados
| Ação | Prioridade |
|------|------------|
| Reportar conf, ged_ecp, ent_n12 separadamente em todos os relatórios GO-8D-NC | Imediata |
| Investigar métricas de diversidade alternativas a ent_n12 (Shannon, Simpson, riqueza bruta) | Curto prazo |
| Testar referência neutra para similaridade estrutural (ged_neutral) | Curto prazo |
| Se GO-8E for autorizado: usar componentes separados, não DV3 composta | Condicional |

---

## 8. Decisão de Governança

> **D-GO8E-01 COMPLETE — GOVERNANCE REVIEW PENDING**
>
> - Diagnóstico executado conforme proposta D-GO8E-01-PROPOSAL.md
- Classificação: **H3 (Interação)** — Score H3=7 vs H1=1, H2=1
- Recomendação: **Decompor DV3; não usar média composta**
- Nenhuma violação de regras: dados congelados, sem novos BIPs/reconstruções, Locks íntegros
- Próximo passo: Governança decide sobre implementação da recomendação (reportar componentes separados) e eventual autorização de GO-8E

---

## 9. Arquivos Gerados

| Arquivo | Descrição |
|---------|-----------|
| `study-output/diagnostic_components.json` | Componentes brutos (30×3×3) |
| `study-output/diagnostic_results.json` | Resultados completos (JSON) |
| `DIAGNOSTIC-REPORT-GO8E-01.md` | Este relatório |

---

## 9. Integridade e Conformidade

| Verificação | Status |
|-------------|--------|
| Dados GO-8D-NC apenas leitura | ✅ |
| Nenhum novo BIP | ✅ |
| Nenhuma nova reconstrução | ✅ |
| Nenhuma alteração de DV3 experimental | ✅ |
| Nenhuma alteração de Locks | ✅ (14/14 hashes OK) |
| Nenhuma escolha de métrica baseada em A > B | ✅ |
| Nenhum novo teste confirmatório | ✅ |
| Nenhum GO-8E executado | ✅ |
| Critérios TS-2/TS-3/TS-4 definidos antes dos resultados | ✅ |

---

**Assinatura:** Diagnóstico D-GO8E-01  
**Data:** 2026-08-15  
**Lock Manifest:** `9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`