# D-06 — Definição Formal da Margem Δ para TOST (Equivalência)

**Data:** 2026-08-14
**Ciclo:** GO-8D — DIAGNOSTIC PHASE
**Tipo:** análise formal + proposta de margem de equivalência (não constitui decisão de governança)
**Base normativa:** R3-03 + R5-GOV-03 (`GO-8B/06-STATISTICAL-PROTOCOL.md` §8; `00-GO-8B-R5-GOVERNANCE-DECISION-RECORD.md`)
**Dependência:** pré-requisito do recálculo de N (D-07) — ver `D-03-DESIGN-REVIEW.md` §6
**Artefatos:** `GO-8D/analysis/d06_delta_anchors.py` (cálculo das âncoras) · este relatório

---

## 1. Contexto normativo (R3-03 + R5-GOV-03)

Regras herdadas do GO-8B (§8 / R5-GOV-03), vigentes e **in alteradas**:

1. **TOST é secondary/optional** — equivalência **não** é hipótese primária do estudo.
2. **Nenhuma margem Δ é pré-aprovada.** Em particular, **Δ = 0.10 explicitamente NÃO aprovada**
   e não pode aparecer como decisão vigente.
3. **Nenhum TOST pode ser executado sem margem Δ especificada e justificada antes da coleta.**
4. Não-significância **não** implica equivalência (regra `p > 0.20 ⇒ equivalência` eliminada).

Consequência para o GO-8D: a margem Δ deve ser **proposta, justificada e aprovada pela
governança** antes do recálculo de N (D-07), porque o tamanho de efeito usado na potência precisa
ser coerente com o critério de equivalência que o estudo poderá aplicar.

---

## 2. Unidades e escala da DV_confirm

`DV_confirm = (conf + ged_ref + ent) / 3`, com `conf ∈ [0,1]`, `ged_ref ∈ [0,1]` (GED normalizada
vs taxonomia da condição) e `ent ∈ [0,1]` (entropia normalizada). Logo **DV_confirm ∈ [0,1]**.

Essa escala é **deliberadamente interpretável**: 1.0 = fidelidade perfeita + zero edição de grafo
vs taxonomia da condição + distribuição degenerada (entropia 0). A margem Δ é definida **nesta
escala de pontos da DV**, não em unidades relativas.

### Estatísticas observadas (simulação D-03, 12 BIPs × 3 condições, células do N=12)

| Condição | Mediana DV_confirm | Média | SD intra-condição | IQR |
|---|---|---|---|---|
| A (cadeia T_PERM, 9 slots) | 0.7134 | 0.7084 | 0.0173 | 0.0282 |
| B (DAG C3 corrigido, 12 nós) | 0.6220 | 0.6234 | 0.0175 | 0.0287 |
| C (cadeia T_PERM, 9 slots) | 0.6843 | 0.6756 | 0.0318 | 0.0925 |

| Par | Δ de medianas (A−B) | |média da diferença pareada| | SD da diferença pareada |
|---|---|---|---|---|
| A vs B | **+0.0793** | 0.0850 | 0.0235 |
| B vs C | **−0.0689** | 0.0522 | 0.0401 |
| A vs C | **+0.0345** | 0.0328 | 0.0297 |

Desvio-padrão global (pooled, 36 células): **SD = 0.0420**.

Interpretação dos dados para fixação de Δ:

- As diferenças de mediana entre condições (hipóteses primárias A vs B e B vs C) são
  **0.069–0.079**, bem maiores que o ruído intra-condição (SD ≈ 0.017–0.032).
- A diferença **A vs C** (0.035), embora não seja hipótese primária, ilustra a magnitude mínima
  de efeito que o instrumento ainda resolve.
- A escala tem resolução observada fina: as âncoras baseadas em SD resultam em valores muito
  pequenos (ver §3), porque o composto é estável por célula.

---

## 3. Âncoras candidatas e avaliação

| Âncora | Valor | Avaliação |
|---|---|---|
| 0.2 · SD global (Cohen "pequeno") | 0.008 | **Rejeitada** — abaixo da resolução prática do composto; equivalente a declarar equivalência apenas para diferenças < 1% da escala; tornaria TOST sem poder com N realista |
| 0.25 · SD global | 0.011 | **Rejeitada** — mesma objeção, muito estrita |
| 0.33 · SD global | 0.014 | Rejeitada — ainda abaixo da diferença A vs C observada (0.035); margem menor que a menor separação que o instrumento resolve |
| 0.5 · SD global | 0.021 | **Aceitável como piso** — ≈ metade da diferença B vs C (0.069); margem estrita mas realizável |
| 0.05 · escala (5%) | **0.050** | **Recomendada** — 1.19 × SD global; ≈ 0.63 × diferença A vs B (0.079); ≈ 0.72 × diferença B vs C (0.069); 1.4 × diferença A vs C (0.035); inteiramente interpretável (5% da escala da DV) |
| 0.075 · escala (7.5%) | 0.075 | Aceitável, porém perto demais da diferença observada B vs C (0.069) — correria risco de TOST "declarar equivalência" justamente no par de hipótese primária com efeito real |
| 0.10 · escala (10%) | 0.100 | **Explicitamente NÃO aprovada** (R5-GOV-03); maior que ambas as diferenças de hipótese primária (0.079 e 0.069) — declararia equivalência mesmo com efeito presente |

### Justificativa da recomendação (Δ = 0.05)

1. **Conservadora em relação aos efeitos de interesse:** as hipóteses primárias (A vs B, B vs C)
   têm diferenças observadas de **0.069–0.079**, todas **acima** de 0.05. Sob H₁ com efeito
   real dessa magnitude, o TOST rejeitará a hipótese de equivalência (correto) — Δ=0.05 não
   "absolve" efeitos que o estudo procura.
2. **Estrita o bastante para ser significativa:** Δ=0.05 é ≈ 2.1 × SD da diferença pareada
   A vs B (0.0235) e ≈ 1.2 × SD da diferença pareada B vs C (0.0401) — bem maior que o ruído,
   garantindo poder razoável para concluir equivalência quando o efeito real é ≤ Δ.
3. **Interpretável na escala da DV:** 5% da escala composta [0,1] é uma declaração comunicável e
   auditável ("diferenças de até 5 pontos na DV_confirm são tratadas como negligenciáveis").
4. **Consistente com o histórico:** evita o valor rejeitado (0.10) e evita âncoras derivadas
   apenas de SD (que produzem margens minúsculas e sem interpretação substantiva).

### Comparação pareada para TOST

A unidade de teste é **por par de condições** (A vs B, B vs C — mesmas comparações do GO-8C),
sobre a **diferença pareada** DV_confirm(BIPᵢ, cond₁) − DV_confirm(BIPᵢ, cond₂), com o mesmo
pareamento por BIP. O TOST é aplicado **após** o Friedman global e apenas nos pares que entram
nas hipóteses secundárias de equivalência, com correção de multiplicidade (Holm) consistente com
o plano inferencial do estudo.

---

## 4. Integração com o recálculo de N (D-07)

A margem entra na potência de duas maneiras:

1. **Potência de superioridade (primária):** detectar diferença de medianas entre A e B (e B vs C)
   sob o efeito observado na simulação (mediana A=0.7134 vs B=0.6220, Δ≈0.091 na escala).
   *Não* depende de Δ.
2. **Potência de equivalência (secundária, TOST):** concluir equivalência quando a diferença real
   é ≤ Δ. Com Δ=0.05, o N necessário para potência de TOST (α=0.05 bilateral, β=0.80, teste
   pareado na escala [0,1], SD da diferença ≈ 0.024–0.040) deve ser **calculado na D-07** e
   informado no pré-registro.

**Regra:** o N final do próximo estudo é o máximo entre (i) N da potência de superioridade e
(ii) N da potência de equivalência sob Δ aprovado. D-06 fornece a margem; D-07 dimensiona N.

---

## 5. Proposta formal (para decisão da governança)

**Proposta:** adotar **Δ = 0.05** (5% da escala da DV_confirm) como margem de equivalência do
TOST no próximo estudo, com as seguintes especificações:

- Escala da margem: **pontos da DV_confirm** (escala [0,1]), não relativa;
- Teste: TOST de duas caldas sobre a **diferença pareada** por BIP, α=0.05, pareamento
  preservado, correção Holm nos pares;
- Decisão: equivalência **concluída** se o IC 95% (bootstrap percentil, B=10.000) da diferença
  estiver **contido em (−Δ, +Δ)**;
- Sem equivalência se o IC exceder Δ em qualquer das caudas.

**Não autorizado nesta etapa:** executar TOST, recálculo de N, pré-registro, Lock ou qualquer
execução experimental. A presente proposta **aguarda decisão formal da governança.**

---

## 6. Confirmação de integridade

- **Nenhum arquivo do GO-8B/GO-8C alterado** (verificado por `git status`); GO-8B e GO-8C
  permanecem CLOSED/LOCKED/FROZEN.
- Arquivo deste ciclo (novo, no GO-8D): `analysis/d06_delta_anchors.py` + este relatório.
- **Nenhum pré-registro, recálculo de N, Lock ou execução experimental foi realizado.**

---

**Fim do relatório D-06. 2026-08-14. Status: PROPOSED (Δ=0.05) — aguardando decisão da governança.
