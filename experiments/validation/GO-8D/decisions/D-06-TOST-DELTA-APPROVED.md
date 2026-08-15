# D-06 — APROVAÇÃO FORMAL DA MARGEM Δ PARA TOST

**Data:** 2026-08-14
**Ciclo:** GO-8D — DIAGNOSTIC PHASE
**Tipo:** registro formal de decisão de governança (aprovado)
**Base:** `decisions/D-06-TOST-DELTA.md` (proposta, 2026-08-14)
**Dependência:** libera o recálculo de N (D-07) — ver `D-03-DESIGN-REVIEW.md` §6

---

## 1. Decisão

A governança **aprova formalmente** a margem de equivalência do TOST:

> **Δ = 0.05** (5% da escala da DV_confirm, escala [0,1]).

**Especificação vigente (a partir desta data):**

- **Escala da margem:** pontos da DV_confirm `(conf + ged_ref + ent)/3 ∈ [0,1]`, não relativa.
- **Teste:** TOST de duas caudas sobre a **diferença pareada** por BIP, α=0.05, pareamento
  preservado, correção Holm nos pares avaliados.
- **Decisão de equivalência:** IC 95% (bootstrap percentil, B=10.000) da diferença **contido em
  (−Δ, +Δ)**.
- **Sem equivalência:** IC exceder Δ em qualquer das caudas.
- Aplicável aos pares de hipóteses secundárias (equivalência) do próximo estudo GO-8D.

## 2. Justificativa (consolidada da proposta D-06)

1. **5% da escala:** Δ=0.05 equivale a 1.19 × SD global observado (SD=0.0420) e é uma declaração
   interpretável e auditável na escala [0,1] da DV_confirm.
2. **Acima dos efeitos primários? — Não; abaixo.** Os efeitos observados das hipóteses primárias
   (A vs B = 0.0793, B vs C = 0.0689) são **maiores** que Δ=0.05: sob H₁ com efeito real dessa
   magnitude, o TOST rejeitará a equivalência (comportamento correto). Δ não "absolve" o efeito
   que o estudo procura.
3. **Δ = 0.10 rejeitada:** explicitamente NÃO aprovada (R5-GOV-03) e maior que as diferenças
   primárias observadas — declararia equivalência mesmo com efeito presente.
4. **Âncoras por SD inviáveis:** 0.2·SD a 0.5·SD global (0.008–0.021) ficam abaixo da resolução
   prática do composto e da menor separação observada (A vs C = 0.035); tornariam o TOST sem
   poder com N realista.

## 3. Escopo e efeitos

- **Escopo:** apenas GO-8D. Sem retroação sobre GO-8B ou GO-8C.
- **GO-8B/GO-8C permanecem CLOSED/LOCKED/FROZEN** — a decisão não altera artefatos congelados,
  nem o histórico de TOST "não executado" registrado nesses ciclos.
- O TOST passa a ser **vigente apenas no contexto do novo estudo GO-8D**, condicionado ao novo
  pré-registro (D-07) e ao Lock do GO-8D. Nenhuma execução ocorreu e nenhuma ocorrerá antes da
  autorização por etapa.

## 4. Efeito sobre o fluxo de trabalho

- **D-06 concluído (APPROVED).** Desbloqueia o pré-requisito do recálculo de N.
- **D-07 (próximo):** recálculo de N = máx(N potência de superioridade, N potência de
  equivalência sob Δ=0.05) + novo pré-registro (DV_confirm + Δ + plano inferencial) + novo Lock
  do GO-8D — **somente após autorização formal por etapa**.

## 5. Confirmação de integridade

- **Nenhum arquivo do GO-8B/GO-8C alterado**; GO-8B e GO-8C permanecem CLOSED/LOCKED/FROZEN.
- **Nenhum recálculo de N, pré-registro, Lock ou execução experimental realizado.**
- Artefatos do ciclo D-06: `D-06-TOST-DELTA.md` (proposta) · `D-06-TOST-DELTA-APPROVED.md`
  (este registro) · `analysis/d06_delta_anchors.py`.

---

**Fim do registro de decisão. 2026-08-14. Status: APPROVED (Δ = 0.05).
