# GO-8C — DECISION D-04 — Aprovação do Pré-registro N=12

**Data:** 2026-08-14
**Ciclo:** GO-8C
**Decisor:** Governança GO-8C
**Decisão:** **APROVAR** o pré-registro do estudo confirmatório GO-8C (N=12).
**Referência ao arquivo aprovado:** `experiments/validation/GO-8C/08-PRE-REGISTRATION-N12.md`
**Status:** **DECIDED**

---

## 1. Objeto da aprovação

- O documento `08-PRE-REGISTRATION-N12.md` (criado em 2026-08-14, D-04.8) foi revisado e **aprovado** pela governança.
- O pré-registro fixa o desenho do estudo confirmatório GO-8C (N=12): N=12 BIPs, 3 condições (A/B/C), 3 seeds por célula, 12×3×3 = 108 execuções, S_struct primária + S_sem exploratória, Friedman (df=2, α=0.05) → Wilcoxon bilateral + Holm-Bonferroni, Kendall W / r_rb / Cliff δ, bootstrap B=10.000, TOST não vigente, Go/No-Go ≥ 10 de 12.

## 2. Adaptações em relação ao GO-8B — confirmadas corretas

| Adaptação | Origem | Confirmada |
|---|---|---|
| **N=12** | D-04 (N=12) | ✅ |
| **Go/No-Go ≥ 10 de 12** | D-04 (decisão 3) | ✅ |
| **Seed C2 corrigida: `258915`** (hex `0x3f363`; antiga → `HISTORICAL-NON-REPRODUCING`) | D-01 | ✅ |
| **Namespace operacional: A→CAT / B→SYN / C→CAT** | D-02 | ✅ |

## 3. Escopo da aprovação

- Aprova o **desenho e o plano de análise** pré-registrados.
- **NÃO autoriza** (nesta decisão):
  - Geração de seeds (valores permanecem `PENDING LOCK PROTOCOL`).
  - Lock do GO-8C (manifesto + hashes) — etapa separada, requer nova autorização.
  - Execução experimental (108 reconstruções) — requer Lock + nova autorização.
  - Análise estatística.

## 4. Próximo passo (não autorizado nesta decisão)

- **Preparar e executar o Lock GO-8C** (manifesto + hashes) **mediante nova autorização explícita** da governança, em etapa separada.
- Após o Lock: autorização explícita de execução experimental e análise.

## 5. Limites

- Nenhum arquivo do GO-8B alterado.
- Nenhuma seed gerada; nenhum hash final preenchido.
- GO-8B permanece CLOSED / LOCKED / FROZEN.

---

**Fim da decisão D-04 (aprovação do pré-registro N=12). DECIDED — aguardando autorização para a etapa de Lock GO-8C.**
