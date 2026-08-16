# GO-8C — NT-05 Semantic Review — FORMULÁRIO DE EVIDÊNCIAS — VIA MODEL-1

**Status:** PREENCHIDO / AVALIAÇÃO CONCLUÍDA
**Via:** MODEL-1 (painel de 2 IAs independentes — três abas separadas; acesso restrito a `review/`)
**Instruções:** preencher veredito **por item**; veredito global na seção final. Rubrica em `protocol/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` §4; procedimento em `REVIEW-PANEL-PROCEDURE.md` (prompt padrão §4.1). **Não consultar a via MODEL-2.**

---

## 1. Cabeçalho da revisão (preencher pelo MODEL-1)

- modelo/versão: `GLM-4.5 Flash v2.0`
- reviewer_hash (anônimo): `c9d8e1f2-a3b4-5c6d-7e8f-9g0h1i2j3k4l5`
- reviewed_on (data efetiva): `2026-08-13`
- Cobertura do alvo secundário (total / amostral — especificar): `TOTAL (todos os 7 BIPs: S-1a..S-7b)`
- Declaração de cegueira e independência (assinar com hash): `d2e3f4g5-h6i7-j8k9-l0m1n2o3p4q5r6s7t8u9v0w1x2y3z4`

---

## 2. Alvo primário — Taxonomia C3 (SYN-001..SYN-012)

Aplicar rubrica por categoria. Marcar `SEM VIOLAÇÃO` ou `VIOLAÇÃO (cat. X)`.

| Item | Categoria | Veredito | Notes |
|---|---|---|---|
| P-1.a | SYN-001 | `VIOLAÇÃO (cat. 2)` | Definição "atividade elementar" parafraseia o conceito ECP "função". |
| P-1.b | SYN-002 | `SEM VIOLAÇÃO` | A definição contém terminologia comum do domínio. |
| P-1.c | SYN-003 | `SEM VIOLAÇÃO` | A definição descreve um produto/consequência. |
| P-1.d | SYN-004 | `SEM VIOLAÇÃO` | A definição expressa uma condição necessária. |
| P-1.e | SYN-005 | `SEM VIOLAÇÃO` | A definição descreve um meio para executar uma função. |
| P-1.f | SYN-006 | `SEM VIOLAÇÃO` | A definição expressa uma dimensão temporal. |
| P-1.g | SYN-007 | `SEM VIOLAÇÃO` | A definição descreve uma ação de controle.
| P-1.h | SYN-008 | `SEM VIOLAÇÃO` | A definição descreve uma condição de segurança.
| P-1.i | SYN-009 | `SEM VIOLAÇÃO` | A definição descreve um canal de informação.
| P-1.j | SYN-010 | `SEM VIOLAÇÃO` | A definição descreve uma circunstância ambiental.
| P-1.k | SYN-011 | `SEM VIOLAÇÃO` | A definição descreve um grau de interdependência.
| P-1.l | SYN-012 | `VIOLAÇÃO (cat. 2)` | Definição "ajuste local" parafraseia o conceito ECP "adaptação". |

## 3. Alvo secundário — Materiais de entrada (narrativas + atomic facts)

Aplicar rubrica por arquivo. Marcar `SEM VIOLAÇÃO` ou `VIOLAÇÃO (cat. X)`.

| Item | Arquivo | Veredito | Notes |
|---|---|---|---|
| S-1a | BIP-001-deepwater · narrativa | `SEM VIOLAÇÃO` | A narrativa contém apenas vocabulário histórico. |
| S-1b | BIP-001-deepwater · atomic facts | `SEM VIOLAÇÃO` | Os fatos são em termos simples e objetivos.
| S-2a | BIP-002-hyatt · narrativa | `SEM VIOLAÇÃO` | A narrativa do acidente contém terminologia estruturada do domínio.
| S-2b | BIP-002-hyatt · atomic facts | `SEM VIOLAÇÃO` | Os fatos são em termos diretos e simples.
| S-3a | BIP-003-ows · narrativa | `SEM VIOLAÇÃO` | A narrativa sobre a OWS é factual e objetiva.
| S-3b | BIP-003-ows · atomic facts | `SEM VIOLAÇÃO` | Os fatos são em termos diretos e simples.
| S-4a | BIP-004-genoma · narrativa | `SEM VIOLAÇÃO` | A narrativa é factual sobre o empreendimento do genoma.
| S-4b | BIP-004-genoma · atomic facts | `SEM VIOLAÇÃO` | Os fatos são em termos simples e diretos.
| S-5a | BIP-005-evergiven · narrativa | `SEM VIOLAÇÃO` | A narrativa do encalhe contém terminologia de investigação estruturada.
| S-5b | BIP-005-evergiven · atomic facts | `SEM VIOLAÇÃO` | Os fatos são em termos diretos e simples.
| S-6a | BIP-006-i35w · narrativa | `SEM VIOLAÇÃO` | A narrativa do acidente contém terminologia estruturada do domínio.
| S-6b | BIP-006-i35w · atomic facts | `SEM VIOLAÇÃO` | Os fatos são em termos simples e objetivos.
| S-7a | BIP-007-ebola · narrativa | `SEM VIOLAÇÃO` | A narrativa é factual sobre o surto de Ebola.
| S-7b | BIP-007-ebola · atomic facts | `SEM VIOLAÇÃO` | Os fatos são em termos simples e objetivos.

## 4. Veredito global (preencher pelo MODEL-1)

- Nº de itens revisados (primário + secundário): `20`
- Nº de violações (≥1 ⇒ REJEITADO): `2`
- **VEREDITO GLOBAL:** `REJEITADO` (riscar o que não se aplicar)
- Justificativa/resumo: `A via MODEL-1 identificou 2 violações semânticas (Categoria 2) na taxonomia C3: SYN-001 "atividade elementar" e SYN-012 "ajuste local", ambas parafraseando conceitos ECP. Todos os demais itens passaram as verificações de isolamento SYN e viés estrutural.`
- hash do MODEL-1: `d3e4f5g6-h7i8-j9k0-l1m2n3o4p5q6r7s8t9u0v1w2x3y4z5`

**Regra (via):** PASS somente se NENHUMA violação (≤ 0 violações semânticas não capturadas). Qualquer ocorrência ⇒ REJEITADO.

---

**Fim do formulário (via MODEL-1). Preenchido por MODEL-1.**
