# GO-8C — DECISION D-01 — C2 / P1-C2-01 (Correção da Seed da Permutação C2)

**Data:** 2026-08-13
**Ciclo:** GO-8C
**Decisor:** Governança GO-8C
**Decisão:** aprovar a correção da seed conforme proposta D-01.
**Status:** DECIDED
**Escopo:** dívida D-01 (C2 — seed não reproduzível). Implementação autorizada SOMENTE dentro de `experiments/validation/GO-8C/`. Nenhum arquivo do GO-8B pode ser alterado.

---

## 1. Contexto

O artefato congelado do GO-8B (`02-C2-PERMUTATION.md`) registra a seed `11473621728585666159` (hex `0x9F3A7E2C1B8D4E6F`) como seed da permutação C2. Sob o algoritmo PCG64 + Fisher-Yates (§3.1), essa seed **não reproduz** a tabela de permutação congelada §5/§6. A proposta `D-01-C2-PROPOSAL.md` (2026-08-13) confirmou a causa raiz por verificação independente e submeteu a correção à governança.

## 2. Decisão

1. **Seed oficial corrigida para o GO-8C: `258915`** (hex `0x3f363`).
   - Reproduz EXATAMENTE a tabela congelada `[1, 5, 6, 3, 7, 0, 4, 8, 2]` sob PCG64 + Fisher-Yates.
   - Já era o `seed_operacional` do piloto (P1-C2-01, Opção A) — zero impacto nos 63 resultados validados do GO-8B.
2. **Tabela de permutação `[1, 5, 6, 3, 7, 0, 4, 8, 2]` permanece inalterada** (verdade operacional do piloto).
3. **Inversa verdadeira corrigida: `[5, 0, 8, 3, 6, 1, 2, 4, 7]`** (posição opaca → índice canônico).
   - A inversa declarada no §5 do congelado (`[5, 0, 8, 3, 7, 1, 6, 4, 2]`) está corrompida e NÃO deve ser usada.
4. **A seed antiga `11473621728585666159`** passa a ser registrada no contexto do GO-8C como **`HISTORICAL-NON-REPRODUCING`** (mantida como registro histórico, sem vínculo gerativo).

## 3. Referência ao GO-8B

- `P1-C2-01` foi resolvido no GO-8B como **Opção A** (`experiments/validation/GO-8B/decisions/P1-C2-01-DECISION.md`): tabela §5 autoritativa, `seed_operacional=258915`, seed registrada marcada `REGISTERED-NON-REPRODUCING`, com a correção formal do vínculo seed→permutação postergada como dívida.
- **O GO-8C corrige definitivamente a dívida**: formaliza `258915` como seed oficial e a inversa verdadeira, sem alterar a tabela/mapping já usados operacionalmente.
- O GO-8B permanece **CLOSED / LOCKED / FROZEN**. Nenhum arquivo do GO-8B é alterado por esta decisão.

## 4. Ações Autorizadas (implementação)

1. Criar `experiments/validation/GO-8C/02-C2-PERMUTATION-CORRECTED.md` (artefato corrigido do entregável 02).
2. Criar cópias operacionais corrigidas em `experiments/validation/GO-8C/scripts/`:
   - `C2_PERMUTATION.yaml` e `C2_PERMUTATION.json`
   - `p1_c2_test.py` (suíte de testes T-C2-01, T-C2-08, T-C2-09 e demais checks)
3. Executar a suíte de testes — **ALL PASS** obrigatório.
4. Registrar o resultado em `experiments/validation/GO-8C/decisions/D-01-C2-VALIDATION.md`.
5. Atualizar `TODO-GO-8C.md` (D-01 → DONE) e o `ACTION-REGISTER` do GO-8C.

**Não é autorizada** nesta etapa a geração de novo manifesto/Lock do GO-8C.

## 5. Referências

- `D-01-C2-PROPOSAL.md` (proposta técnica, 2026-08-13)
- `experiments/validation/GO-8B/02-C2-PERMUTATION.md` §3/§4/§5/§6 (congelado, referência histórica)
- `experiments/validation/GO-8B/decisions/P1-C2-01-DECISION.md` (Opção A, GO-8B)
- Hash do manifesto GO-8B (referência histórica): `c55799d895a4f73888713a8538c6b9a6c5df1d7cde71c88141e16b9e9b216636`

---

**Fim da decisão. D-01 DECIDED. Nenhum arquivo do GO-8B alterado. Nenhum Lock gerado.**
