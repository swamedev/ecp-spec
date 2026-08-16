# GO-8C — NT-05 Semantic Review — FORMULÁRIO DE EVIDÊNCIAS

**Status:** VAZIO / AGUARDANDO REVISOR — preencher sem alterar estrutura.
**Instruções:** preencher veredito **por item**; veredito global na seção final. Rubrica em `protocol/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` §3.

---

## 1. Cabeçalho da revisão (preencher pelo revisor)

- reviewer (hash anônimo): `____________`
- reviewed_on (data efetiva): `____________`
- Cobertura do alvo secundário (total / amostral — especificar): `____________`
- Declaração de cegueira e independência (assinar com hash): `____________`

---

## 2. Alvo primário — Taxonomia C3 (SYN-001..SYN-012)

Aplicar rubrica por categoria. Marcar `SEM VIOLAÇÃO` ou `VIOLAÇÃO (cat. X)`.

| Item | Categoria | Veredito | Notes |
|---|---|---|---|
| P-1.a | SYN-001 | `____` | |
| P-1.b | SYN-002 | `____` | |
| P-1.c | SYN-003 | `____` | |
| P-1.d | SYN-004 | `____` | |
| P-1.e | SYN-005 | `____` | |
| P-1.f | SYN-006 | `____` | |
| P-1.g | SYN-007 | `____` | |
| P-1.h | SYN-008 | `____` | |
| P-1.i | SYN-009 | `____` | |
| P-1.j | SYN-010 | `____` | |
| P-1.k | SYN-011 | `____` | |
| P-1.l | SYN-012 | `____` | |

## 3. Alvo secundário — Materiais de entrada (narrativas + atomic facts)

Aplicar rubrica por arquivo. Marcar `SEM VIOLAÇÃO` ou `VIOLAÇÃO (cat. X)`.

| Item | Arquivo | Veredito | Notes |
|---|---|---|---|
| S-1a | BIP-001-deepwater · narrativa | `____` | |
| S-1b | BIP-001-deepwater · atomic facts | `____` | |
| S-2a | BIP-002-hyatt · narrativa | `____` | |
| S-2b | BIP-002-hyatt · atomic facts | `____` | |
| S-3a | BIP-003-ows · narrativa | `____` | |
| S-3b | BIP-003-ows · atomic facts | `____` | |
| S-4a | BIP-004-genoma · narrativa | `____` | |
| S-4b | BIP-004-genoma · atomic facts | `____` | |
| S-5a | BIP-005-evergiven · narrativa | `____` | |
| S-5b | BIP-005-evergiven · atomic facts | `____` | |
| S-6a | BIP-006-i35w · narrativa | `____` | |
| S-6b | BIP-006-i35w · atomic facts | `____` | |
| S-7a | BIP-007-ebola · narrativa | `____` | |
| S-7b | BIP-007-ebola · atomic facts | `____` | |

*(BIP-003-warpspeed: sem narrativa/atomic facts — fora do escopo.)*

---

## 4. Veredito global (preencher pelo revisor)

- Nº de itens revisados (primário + secundário): `____`
- Nº de violações (≥1 ⇒ REJEITADO): `____`
- **VEREDITO GLOBAL:** `PASS` / `REJEITADO` (riscar o que não se aplicar)
- Justificativa/resumo: `__________________________________________________________________`
- hash do revisor: `____________`

**Regra:** PASS somente se todas as violações = 0 (≤ 0 violações semânticas não capturadas). Qualquer ocorrência ⇒ correção e revalidação.

---

**Fim do formulário. Vazio até entrega pelo revisor independente.**
