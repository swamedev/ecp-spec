# D-MV-01 — APROVAÇÃO FORMAL DA DV CONFIRMATÓRIA

**Data:** 2026-08-14
**Status:** **APPROVED**
**Gate:** D-MV-01 — DV confirmatória (análise decisória, sem execução experimental)
**Referência:** `D-MV-01-DV-CONFIRMATORY.md`

---

## 1. Decisão Formal da Governança

A governança **aprova** a DV3 como **candidata confirmatória** para futuros ciclos, com as
limitações registradas.

## 2. Especificação Congelada da DV

| Parâmetro | Valor |
|---|---|
| **DV** | `DV = (conf + ged_ecp + ent_n12) / 3` |
| **Pesos** | **1:1:1** |
| **conf** | fidelidade por fato (média da confiança das entidades) |
| **ged_ecp** | similaridade GED (w_edge=0.5) vs **referência ECP comum** (grafo canônico de 9 nós) |
| **ent_n12** | entropia normalizada com **denominador comum log(12)** (entropia bruta H / log 12) |
| **Escala** | clamp em [0, 1] |
| **Unidade de análise** | mediana das seeds por célula (BIP × condição) |

## 3. Limitações Registradas (explicitadas e aceitas)

1. **ged_ecp em faixa estreita** (0.219–0.395) devido ao mapeamento CAT/SYN→ECP por `text_emb`
   (cos ≈ 0.12–0.28). **Aceitável para comparação de condições**; **não** usar como medida absoluta
   de qualidade isolada.
2. **ent_n12 concentra ~73% do sinal de condição** — sem artefato de denominador (denominador
   comum), porém o desbalanceamento de contribuição permanece.
3. **Sobreposição parcial entre condições** na distribuição de DV3 — a magnitude do efeito B<A é
   menor que na DV0 (Δ −0.0793 → −0.0374); a decisão qualitativa (C3 sem utilidade) se mantém.

## 4. Próximos Passos Autorizados

1. **D-MV-02 — Recálculo de potência** com a DV3 congelada (Monte Carlo calibrado com dados GO-8D).
2. Preparação do pré-registro do novo ciclo **somente após** a definição do N.
3. **Nenhum experimento novo** será executado nesta etapa.

---

**Fim do registro. D-MV-01 APPROVED (2026-08-14). Lock GO-8D intocado.