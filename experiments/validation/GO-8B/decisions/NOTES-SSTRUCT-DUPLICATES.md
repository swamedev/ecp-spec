# GO-8B — NOTES: DUPLICAÇÃO PARCIAL DE S_STRUCT DENTRO DA MESMA CONDIÇÃO

**Data:** 2026-08-13
**Decisor:** Governança GO-8B
**Status:** **ACCEPTED** (limitação da métrica; não invalida o piloto)

---

## 1. O que foi observado

Na auditoria de evidências (EVIDENCE-AND-STOP-GO-8B.md), valores idênticos de `s_struct`
foram detectados entre BIPs diferentes dentro da mesma condição:

- **Condição A:** `0.5875` repetido em BIP-001, BIP-002, BIP-003, BIP-004, BIP-006 (5 de 7).
- **Condição C:** `0.5676` repetido em BIP-003, BIP-005, BIP-006 (3 de 7).
- Condição B: sem repetição (7 valores distintos).

`S_sem`: sem repetição em nenhuma condição (21 células distintas).

## 2. Explicação aceita

`S_struct` é a similaridade topológica do WL Subtree Kernel sobre o grafo anonimizado
(`"neutral"`) — métrica **estrutural** (05 §3, 08 §4). A **invariância topológica** pode
produzir valores iguais para grafos estruturalmente equivalentes (mesma forma/ordem de
subárvores após anonimização), independentemente do conteúdo semântico. Isso é uma
**propriedade da métrica**, não um erro de execução.

## 3. Aceitação da governança

A governança aceita a duplicação parcial de `S_struct` como limitação da métrica estrutural
anonimizada, **desde que**:

1. Haja variação entre as condições A/B/C — **confirmada** (medianas: A=0.5875, B=0.5905,
   C=0.5721; Friedman χ²_F=9.5556, df=2, p=0.0084 — variação entre condições presente).
2. A análise estatística seja executada sobre as **medianas por célula** conforme protocolo
   (06 §1.3.1, R5 M-3) — **executada** (ver STATISTICAL-REPORT.md).

A duplicação **não invalida** o piloto GO-8B.

## 4. Registro

- Análise estatística executada conforme protocolo em `pilot-output/STATISTICAL-REPORT.md`.
- Nenhum artefato congelado (00–08) alterado.

---

**Fim da nota. Nenhum artefato congelado alterado.