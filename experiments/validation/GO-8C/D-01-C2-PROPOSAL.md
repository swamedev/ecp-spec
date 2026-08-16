# GO-8C — D-01 PROPOSTA TÉCNICA — C2 / P1-C2-01 (Seed da Permutação)

**Data:** 2026-08-13
**Ciclo:** GO-8C
**Status:** **PROPOSTA** — PENDING GOVERNANCE DECISION (nenhuma implementação executada)
**Escopo:** dívida D-01 (C2 — seed não reproduzível). Somente leitura do GO-8B; nenhum arquivo do GO-8B alterado.

---

## 1. Causa Raiz Confirmada (verificação independente 2026-08-13)

Reprodução independente sob `numpy.random.Generator(PCG64(seed))` + Fisher-Yates (§3.1):

| Fonte | Permutação (índices canônicos → posições opacas) | Reproduz §5? |
|---|---|---|
| **§5 congelado** (verdade operacional) | `[1, 5, 6, 3, 7, 0, 4, 8, 2]` | — |
| `PCG64(11473621728585666159)` (seed registrada §4) | `[1, 5, 0, 4, 3, 8, 6, 2, 7]` | **NÃO** |
| `PCG64(258915)` (seed operacional P1-C2-01) | `[1, 5, 6, 3, 7, 0, 4, 8, 2]` | **SIM** |

**Inversa §5 declarada (corrompida):** `[5, 0, 8, 3, 7, 1, 6, 4, 2]`
**Inversa verdadeira (§5 → §6, já calculada e registrada no YAML operacional):** `[5, 0, 8, 3, 6, 1, 2, 4, 7]`

Conclusões:
- A **seed registrada** `11473621728585666159` NÃO gera a tabela congelada §5/§6 — o artefato congelado tem vínculo seed→permutação errado.
- A **tabela/JSON §6 é internamente consistente** com a permutação §5 e foi a verdade operacional usada no piloto (`C2_PERMUTATION.yaml`, mapping verbatim, `OPERATIONAL-AUTHORITATIVE`).
- A **inversa declarada** do §5 está corrompida; a inversa verdadeira é `[5, 0, 8, 3, 6, 1, 2, 4, 7]` (já validada: `T-C2-MAP-03/07`, `T-C2-MAP-07-TRUE-INVERSE` = PASS).

**Causa raiz:** seed congelada incorreta para o algoritmo PCG64 Fisher-Yates. A correção requer formalizar, no GO-8C, a **seed operacional correta** (`258915`) e a **inversa verdadeira**, mantendo a tabela de permutação já usada no piloto.

---

## 2. Proposta de Correção (para o GO-8C — a implementar somente após decisão da governança)

### 2.1 Nova seed oficial

- **Nova seed oficial C2 = `258915`** (uint64).
- **Justificativa:**
  1. Reproduz EXATAMENTE a tabela §5/§6 congelada sob o algoritmo documentado (§3.1) — única seed validada.
  2. Já é o `seed_operacional` operacionalmente ativo do piloto (P1-C2-01, opção A).
  3. Mantém **idêntica** a permutação usada no piloto — zero impacto nos 63 resultados já validados.
  4. A seed antiga `11473621728585666159` fica registrada como **histórica/não-reprodutora** (sem uso no GO-8C).
- `0x3f363` é o equivalente hexadecimal de `258915`.

### 2.2 Tabela de permutação

- **PERMANECE A MESMA:** `[1, 5, 6, 3, 7, 0, 4, 8, 2]`.
- Mapping bidirecional §6 permanece idêntico (CAT-00..CAT-08 ↔ canônicos), pois foi a verdade operacional do piloto.

### 2.3 Inversa correta

- **Inversa verdadeira (posição opaca → índice canônico):** `[5, 0, 8, 3, 6, 1, 2, 4, 7]`.
- A inversa declarada no §5 (`[5, 0, 8, 3, 7, 1, 6, 4, 2]`) deve ser **corrigida** no documento corrigido do GO-8C.

### 2.4 JSON §6 (documento corrigido)

No `02-C2-PERMUTATION-CORRECTED.md` do GO-8C, o bloco JSON §6 deve ser ajustado:
- `"seed": "0x9F3A7E2C1B8D4E6F"` → `"seed": "0x3f363"` (ou campo `seed_operacional` com `value: 258915`).
- Mapping `opaque_to_canonical` / `canonical_to_opaque`: **inalterados**.
- Adicionar nota de proveniência: corrigido em GO-8C a partir da decisão P1-C2-01 (GO-8B) + verificação independente.

### 2.5 Artefato operacional `C2_PERMUTATION.yaml` (cópia GO-8C)

Novo artefato em `experiments/validation/GO-8C/scripts/` (não tocar no YAML do GO-8B):
- `seed_operacional.value = 258915` (já presente).
- `seed_registrada` → marcada **`HISTORICAL-NON-REPRODUCING`** (nova semântica: mantida como registro histórico, sem vínculo gerativo).
- `inverse_verdadeira_opaque_to_canonical_index = [5, 0, 8, 3, 6, 1, 2, 4, 7]`.
- `mapping_status = OPERATIONAL-AUTHORITATIVE` (inalterado).
- `governance.decision` → referência a nova decisão GO-8C (D-01) e a P1-C2-01 como histórico.

### 2.6 Testes de C2 (P1) após a correção

Ajustes propostos no script de validação do GO-8C (`p1_c2_permutation.py` — versão GO-8C):
- `SEED_C2` deixa de ser a seed registrada; passa a ser `258915` (oficial).
- **T-C2-01 (determinismo):** `PCG64(258915)` → deve reproduzir `[1, 5, 6, 3, 7, 0, 4, 8, 2]` → **PASS** esperado (hoje o teste genérico não valida contra a seed por causa da não-reprodução).
- **T-C2-02 (sensibilidade):** qualquer bit alterado na seed → permutação diferente (inalterado).
- **T-C2-03/04 (bijetividade/completude):** inalterados, PASS.
- **T-C2-MAP-03/07 (inversa verdadeira):** PASS contra `[5, 0, 8, 3, 6, 1, 2, 4, 7]`.
- **Novo T-C2-08 (regressão):** `PCG64(11473621728585666159)` NÃO produz a tabela §5 — registra que a seed antiga é não-reprodutora (documental, esperado NOT-REPRODUCING, não falha o suite).
- **Novo T-C2-09 (oficialidade):** o artefato YAML declara `seed_operacional.value == 258915` e `inverse_verdadeira == [5,0,8,3,6,1,2,4,7]`.

---

## 3. Impacto em Testes e Artefatos Operacionais

| Artefato | Impacto |
|---|---|
| Tabela §5 permutação | **Nenhum** (mantida idêntica) |
| Mapping bidirecional §6 | **Nenhum** (mantido) |
| Inversa declarada §5 | **Corrigida** para `[5, 0, 8, 3, 6, 1, 2, 4, 7]` (somente no doc corrigido GO-8C) |
| Seed registrada §4 | Substituída por `258915` no GO-8C; antiga → `HISTORICAL-NON-REPRODUCING` |
| `C2_PERMUTATION.yaml/.json` (GO-8B) | **Não tocados**; cópia GO-8C criada com novos campos |
| Piloto GO-8B (63 execuções) | **Nenhum** — permutação operacional idêntica (o piloto usou o mapping verbatim) |
| Resultados estatísticos GO-8B | **Inalterados** (não dependem da seed) |
| FP-04 (mapping C2) | Corrigido no GO-8C: seed oficial reproduz a permutação |

---

## 4. Estrutura de Arquivos Recomendada para o GO-8C

```
experiments/validation/GO-8C/
├── GO-8C-OPENING-DECISION.md          (criado)
├── TODO-GO-8C.md                      (criado)
├── 02-C2-PERMUTATION-CORRECTED.md     ← documento corrigido (nova versão do entregável 02)
├── D-01-C2-PROPOSAL.md                ← este relatório
├── decisions/                         ← novas decisões do GO-8C (futuro)
├── pilot-input/                       (vazio — aguardando autorização)
├── pilot-output/                      (vazio — aguardando autorização)
└── scripts/
    ├── C2_PERMUTATION.yaml            ← cópia GO-8C corrigida
    ├── C2_PERMUTATION.json            ← cópia GO-8C corrigida
    └── p1_c2_permutation.py           ← versão GO-8C dos testes
```

- **Novo manifesto e Lock no GO-8C:** **SIM, será necessário no futuro**, após implementação e validação do ciclo GO-8C (Lock de novo manifesto com a seed/inversa corrigidas). **Não executar nesta etapa.**
- Nenhum arquivo do GO-8B é alterado; nenhum hash/Lock do GO-8B recalculado.

---

## 5. Próximos Passos Sugeridos (após aprovação da governança)

1. Governança aprova esta proposta (registrar decisão em `decisions/` do GO-8C).
2. Criar `02-C2-PERMUTATION-CORRECTED.md` a partir do congelado, com seed `258915`, inversa verdadeira e JSON §6 corrigido (nota de proveniência GO-8C).
3. Criar cópias operacionais corrigidas em `GO-8C/scripts/` (`C2_PERMUTATION.yaml/.json`, `p1_c2_permutation.py`).
4. Executar suíte de validação T-C2 (determinismo, sensibilidade, bijetividade, completude, inversa, regressão) — **ALL PASS**.
5. Registrar resultado e, se aplicável, gerar novo manifesto/Lock do GO-8C (em etapa separada autorizada).
6. Atualizar `TODO-GO-8C.md`: D-01 → validação concluída (somente após decisão formal e evidência).

---

**Fim da proposta. Nenhuma correção executada. Nenhum arquivo do GO-8B alterado. Nenhum hash/Lock gerado.**
