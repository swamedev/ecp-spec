# DECISION — P1-C2-01 (GO-8B) — Resolução Formal da Seed da Permutação C2

**Data:** 2026-08-12
**Decisor:** Governança GO-8B
**Decisão:** **Opção A**
**Status:** DECIDED
**Artefatos afetados:** nenhum artefato do núcleo congelado (00–08) é alterado; esta decisão é registrada em artefato separado (este arquivo).

---

## 1. Contexto (achado P1-C2-01)

A seed registrada no artefato congelado `02-C2-PERMUTATION.md` §4

```
SEED_C2 = 0x9F3A7E2C1B8D4E6F  # 11473621728585666159 decimal
```

**não reproduz** a tabela de permutação congelada no §5 do mesmo artefato, quando aplicada ao algoritmo PCG64 Fisher-Yates especificado no §3.

**Verificação por reprodução independente (2026-08-12):**

| Fonte | Permutação (índices canônicos → posições opacas) |
|---|---|
| §5 congelado (esperado) | `[1, 5, 6, 3, 7, 0, 4, 8, 2]` |
| `PCG64(11473621728585666159)` | `[1, 5, 0, 4, 3, 8, 6, 2, 7]` — **não reproduz** |
| `PCG64(258915)` | `[1, 5, 6, 3, 7, 0, 4, 8, 2]` — **reproduz** |

O JSON do §6 (*opaque_to_canonical* / *canonical_to_opaque*) é **internamente consistente** com a tabela de permutações §5 (ver `p1_c2_permutation.py`, testes T-C2-MAP-01/02/03) e diverge apenas na "inversa declarada" do §5 (que está corrompida e não representa a inversa verdadeira da permutação).

---

## 2. Decisão (Opção A)

1. **A tabela de permutação congelada no §5 do artefato `02-C2-PERMUTATION.md` é a verdade operacional autoritativa.**
2. **O JSON §6** (internamente consistente) é a fonte para o artefato operacional `C2_PERMUTATION.yaml`.
3. **A seed `258915` (PCG64)** é reconhecida como o valor que reproduz a tabela congelada e passa a ser registrada operacionalmente como `seed_operacional` para fins de reprodutibilidade.
4. **A seed original (`11473621728585666159`)** permanece marcada como `REGISTERED-NON-REPRODUCING`; a correção do vínculo seed→permutação fica postergada como **dívida de reparação** para um futuro ciclo de versão/Lock.
5. **Nenhum artefato do núcleo congelado é alterado.**

---

## 3. Implementação operacional

- **`experiments/validation/GO-8B/decisions/P1-C2-01-DECISION.md`** — este registro formal.
- **`scripts/go8b/operational/C2_PERMUTATION.yaml`** — regenerado com:
  - permutação (índices canônicos → opacos): `[1, 5, 6, 3, 7, 0, 4, 8, 2]`
  - **inversa verdadeira** (posição opaca → índice canônico): `[5, 0, 8, 3, 6, 1, 2, 4, 7]`
  - namespaces C1 (`ECP`) / C2 (`CAT`) / C3 (`SYN`) / C4 (`NULL`)
  - `seed_operacional: 258915`
  - `seed_registrada: 11473621728585666159` com nota `REGISTERED-NON-REPRODUCING`
  - proveniência `derived_from: 02-C2-PERMUTATION.md §6 (frozen)`

---

## 4. Implicações

- **FP-04 desbloqueado** parcialmente: o mecanismo de cegueira C2 passa a ter seed operacional reprodutível, sem alterar o congelado. A dívida formal (vínculo seed registrada ↔ permutação) permanece registrada.
- O mapeamento visual "inversa declarada" do §5 (corrompido) não deve ser usado; o artefato operacional registra a inversa verdadeira.

---

## 5. Referências

- Hash do manifesto vigente: `c55799d895a4f73888713a8538c6b9a6c5df1d7cde71c88141e16b9e9b216636`
- `02-C2-PERMUTATION.md` §3 (algoritmo), §4 (seed), §5 (tabela), §6 (JSON)
- `GO-8B-LOCK-MANIFEST.yaml` (C2_PERMUTATION.yaml fora do escopo congelado: `excluded_artifacts_pending_generation`)
- `scripts/go8b/operational/p1_c2_permutation.py` (validação T-C2-MAP-01..05)

---

**Fim da decisão. Nenhum artefato congelado alterado. Nenhum dado experimental produzido.**