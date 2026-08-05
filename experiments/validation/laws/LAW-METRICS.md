# LAW-METRICS — Força da Lei e Poder Preditivo

| Campo | Valor |
|---|---|
| **Tipo** | Definição de métricas (Inferência Científica) |
| **Status** | Draft — parâmetros v0.1 a calibrar com dados |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe |
| **Referências** | [ECP-012](../../ECP/ECP-012.md), [adversarial](../adversarial/README.md), [signals](../signals/README.md) |

## Por que medir a força de uma lei?

Nem toda lei é igual. Na ciência, algumas leis sobrevivem séculos; outras são
destruídas em meses. Tratar todas as leis como equivalentes esconde a diferença
entre uma hipótese frágil e uma lei fundamental.

Este documento define dois índices:

- **Law Strength Index (LSI)** — quão forte é a lei.
- **Predictive Index (PI)** — quão bem a lei prevê o futuro.

## Law Strength Index (LSI)

### Campos

| Campo | Exemplo |
|---|---|
| Domínios testados | 8 |
| Experimentos | 43 |
| Contraexemplos | 2 |
| Hostile Tests | 9 |
| External Validation | 3 |
| Industrial Validation | 1 |
| **LSI** | **0.93** |

### Fórmula (v0.1 — a calibrar)

```
LSI = 0.35·S + 0.20·D + 0.25·V + 0.20·P
```

- **S — Sobrevivência** = `1 − contraexemplos / experimentos`
- **D — Cobertura de domínios** = `min(domínios / 8, 1)`
- **V — Profundidade de validação** =
  `0.3·min(hostile/10, 1) + 0.4·min(external/3, 1) + 0.3·min(industrial/1, 1)`
- **P — Preditividade** = Predictive Index (abaixo)

### Exemplo numérico

Com os campos da tabela (e P ilustrativo = 0.85):

```
S = 1 − 2/43 ≈ 0.953
D = min(8/8, 1) = 1.0
V = 0.3·0.9 + 0.4·1.0 + 0.3·1.0 = 0.97
P = 0.85

LSI = 0.35·0.953 + 0.20·1.0 + 0.25·0.97 + 0.20·0.85
    ≈ 0.334 + 0.200 + 0.243 + 0.170
    ≈ 0.95
```

> O valor ilustrativo (≈0.95) é próximo do LSI 0.93 do exemplo. **Os pesos são
> parâmetros v0.1** — devem ser calibrados conforme os primeiros dados reais
> chegarem.

### Faixas por estado (proposta)

| Estado | Faixa LSI | Significado |
|---|---|---|
| LAW-H | 0.20 – 0.45 | hipótese, sem validação externa |
| LAW-C | 0.45 – 0.70 | sobreviveu a experimentos independentes |
| LAW-V | 0.70 – 0.85 | validada em múltiplos domínios |
| LAW-F | > 0.85 | fundacional |

## Predictive Index (PI)

Uma lei científica boa **não explica apenas o passado; prevê o futuro**.

### Definição

```
PI = previsões confirmadas / previsões totais (amostra fora da origem da lei)
```

### Medição (preregistro obrigatório)

- A previsão é registrada **antes** do desfecho (preregistro) — nunca
  reconstruída depois. Sem isso, a "previsão" é retrofiting.
- Cada experimento novo (EXP-N) e cada experimento hostil pode servir como
  teste preditivo.

### Exemplo

Se **LAW-003** diz *"toda decisão justificável depende de conhecimento"*, ela
deve prever:

> qualquer projeto **sem** conhecimento suficiente **vai falhar**.

Se essa previsão se confirma em novos projetos (e nos hostis), a lei fica muito
mais forte — seu **PI** sobe.

## Relação com o pipeline

```
LAW-H → (hostil) → LAW-C → External Validation → LAW → LAW Strength (LSI) → Industrial Validation → LAW-F
```

O LSI consolida **evidência retrospectiva + robustez + validação externa**; o PI
adiciona a dimensão **prospectiva**. Juntos, eles medem a força de uma lei de
forma comparável — o que transforma o ECP de especificação em investigação
científica da engenharia.

## Notas de governança (P-0006)

- **Naming:** até a validação industrial a lei é uma **Candidate Universal
  Law**; somente depois, **Universal Engineering Law** — ver
  [P-0006](../P-0006-LAW-DISCOVERY.md).
- **Genealogia:** toda lei registra os Signals de origem (OBS → SIGNAL →
  PATTERN → LAW-H), conforme [LAW-BACKLOG](./LAW-BACKLOG.md).
- **Negative Evidence:** ausência de evidência conta como dado (registrada por
  lei e por backlog item), junto de contraexemplos.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 0.1 | 2026-08-03 | Versão inicial (Draft). Definição do Law Strength Index (LSI) e do Predictive Index (PI). |
