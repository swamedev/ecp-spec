# GAP-VALIDADE-DISCRIMINANTE-MR-C7

## Registro Formal do Gap de Validade Discriminante de Valor

**Data:** 2026-08-18
**Status:** GAP REGISTRADO — critério MR-C7 proposto, **não executado**
**Nomenclatura:** conforme `C-NOMENCLATURE-CORRECTION.md` (critérios com prefixo `MR-`)

---

## 1. O que MR-C1–MR-C6 comprovam

Os critérios que a métrica `DV-REDESIGN = (conf + ged_ref + div_metric) / 3` já passou (Fase B/C
do gate de mensuração, `MEASUREMENT-GATE-CONSOLIDATION.md`) comprovam **neutralidade e robustez**:

| Critério | O que comprova | Resultado congelado |
|----------|----------------|---------------------|
| **MR-C1** — Validade convergente | Correlaciona com ground truth sintético | ρ = 0.905 (≥ 0.7) **PASS** |
| **MR-C2** — Ausência de viés estrutural | Não favorece CAT vs SYN | bias_score = 0.432 (< 0.5) **PASS** |
| **MR-C3** — Robustez a pesos | Ordem não colapsa sob variação de pesos | 93.6% (≥ 80%) **PASS** |
| **MR-C4** — Robustez a agregação | Ordem estável entre agregadores | CV = 0.135 (≤ 0.15) **PASS** |
| **MR-C5** — Sensibilidade | **Detecta degradação injetada** (ruído/omissão/permutação) | 1.0 **PASS** |
| **MR-C6** — Interpretabilidade | Avaliadores independentes concordam sobre o que veem | 97.7% (≥ 80%) **PASS** |

Em resumo: **a métrica é neutra, estável e sensível a degradação.** Nenhum veto acionado;
seleção cega da referência GED concluída (DATA-DRIVEN).

---

## 2. O que MR-C1–MR-C6 NÃO comprovam

**Nenhum dos critérios acima demonstra que a métrica consegue detectar valor semântico real
quando ele existe.**

A propriedade em questão chama-se **validade discriminante de valor**: a capacidade de atribuir
score mais alto a reconstruções que receberam informação adicional **correta e relevante**
(em relação ao baseline) e score mais baixo a reconstruções que receberam informação
**incorreta/ruidosa**. Essa propriedade é distinta de todas as anteriores:

- **MR-C1 (validade convergente)** correlaciona com *ground truth sintético* cuja construção é
  independente da questão "a métrica premia valor semântico adicionado?".
- **MR-C2/MR-C3/MR-C4 (neutralidade/robustez)** garantem que a métrica *não* favorece
  inadvertidamente uma condição, um peso ou um agregador — não garantem que ela *reconhece*
  melhoria semântica.
- **MR-C5 (sensibilidade)** testa apenas o eixo **degradação** (ruído ↑ → score ↓). Não testa o
  eixo **melhoria** (valor ↑ → score ↑).
- **MR-C6 (interpretabilidade)** mede concordância entre avaliadores sobre o que a reconstrução
  exibe — não mede se a métrica quantifica valor de forma válida.

**Uma métrica pode passar MR-C1–MR-C6 e ainda ser cega a melhoria genuína** (valor ↑ → score
não muda, ou muda na direção errada), exatamente por ser robusta demais às variações que o valor
semântico produz. São dois eixos ortogonais:

| Eixo | Pergunta | Critério |
|------|----------|----------|
| **Sensibilidade a degradação** | "A métrica piora quando a informação piora?" | MR-C5 (**PASS**, já testado) |
| **Validade discriminante de valor** | "A métrica melhora quando a informação correta e relevante aumenta o conteúdo, e permanece insensível a redundância?" | **MR-C7 (proposto, não testado)** |

---

## 3. Distinção operacional: MR-C5 × MR-C7

| | **MR-C5 (já PASS)** | **MR-C7 (gap)** |
|---|---|---|
| Tipo de perturbação | Degradação (ruído, omissão, permutação) | Informação adicional: correta+relevante (V1), redundante (V2), incorreta/ruidosa (V3) |
| Direção esperada | Score diminui | Ordem V1 > V2 ≈ V0 > V3 (V0 = baseline) |
| O que provaria | A métrica não é cega a dano | A métrica não é cega a valor; não premia redundância nem densidade estrutural |
| Consequência de ausência | N/A (testado e PASS) | GO-8E não pode abrir: o desfecho do experimento seria não interpretável |

---

## 4. Por que o gap bloqueia a abertura do GO-8E

O GO-8E testaria, de forma confirmatória, a hipótese de utilidade de uma intervenção de
informação adicional (a taxonomia C3). Para esse desfecho ser interpretável, a métrica precisa
**poder subir quando o valor subir** — não apenas descer quando o valor cair.

O precedente do GO-8D é direto: a limitação nº 1 do `FINAL-PROJECT-REPORT-GO-8D.md`
(limitações §4.1, hash `4d40f5c5...`) registra que *"DV_confirm não captura utilidade da C3:
a redução observada em B pode refletir limitação da métrica composta ... a C3 adiciona
informação que a DV_confirm trata como ruído, não como melhoria semântica."* Ou seja, já houve
um ciclo (GO-8D) em que **a ausência de validade discriminante de valor tornou um resultado
negativo não interpretável como refutação da hipótese**. O GO-8D foi fechado honestamente como
negativo genuíno (Cliff δ = 1.000, 12/12), mas a dúvida sobre o instrumento permaneceu.

Sem MR-C7, um resultado positivo no GO-8E poderia ser artefato de densidade estrutural/lexical,
e um resultado negativo poderia ser cegueira da métrica — nenhum dos dois seria interpretável.
Por isso:

> **A abertura do GO-8E fica bloqueada até que MR-C7 seja pré-registrado e executado**
> (ou a governança decida formalmente tratar o instrumento como não apto para inferência
> confirmatória).

---

## 5. Caminho de resolução proposto

1. **Pré-registro congelado** do gate MR-C7 com desenho de casos sintéticos/contrafactuais
   (4 estados de informação adicional V0–V3) — ver `MR-C7-PROTOCOLO-PREREGISTRO.md`.
2. **Execução** estritamente conforme o pré-registro, sem ajuste retroativo.
3. **Regra de decisão:**
   - **MR-C7 PASS** → documentar que `DV-REDESIGN` fica autorizada para uso confirmatório;
     preparar material para a decisão de governança sobre o **desenho** do GO-8E (o experimento
     continua exigindo autorização separada).
   - **MR-C7 FAIL** → documentar como resultado válido; recomendar redesenho do componente de
     diversidade/estrutura (`div_metric`/`ged_ref`) antes de nova tentativa; **não** tentar
     "salvar" a métrica atual.

---

## 6. Limitações registradas

- Este documento **não** executa MR-C7; apenas registra formalmente o gap e o critério proposto.
- MR-C7, quando executado, usará **ground truth por consenso de IA** (Claude, GPT, Gemini),
  com limitação registrada no mesmo padrão de honestidade de P-0010 (reprodutibilidade) e de
  M-REDESIGN-01 (avaliação por IA ≠ ground truth científico). Detalhes no pré-registro.
- Nenhum cálculo de potência, pré-registro do GO-8E, coleta de BIPs ou autorização de GO-8E é
  realizado por este documento.

---

**Assinatura:** Governança ECP
**Data:** 2026-08-18
**Base:** Lock Manifest GO-8D-NC (`9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`)