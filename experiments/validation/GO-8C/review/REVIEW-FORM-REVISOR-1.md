# GO-8C — NT-05 Semantic Review — FORMULÁRIO DE EVIDÊNCIAS — VIA REVISOR-1

**Status:** PREENCHIDO / AVALIAÇÃO CONCLUÍDA
**Via:** REVISOR-1 (painel de 2 IAs independentes — acesso restrito a `review/`)
**Instruções:** preencher veredito **por item**; veredito global na seção final. Rubrica em `protocol/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` §4; procedimento em `REVIEW-PANEL-PROCEDURE.md` (prompt padrão §4.1). **Não consultar a via MODEL-2.**

---

## 1. Cabeçalho da revisão (preencher pelo REVISOR-1)

- modelo/versão: `GLM-4.5 Flash v2.0`
- reviewer_hash (anônimo): `e1f2g3h4-i5j6-k7l8-m9n0o1p2q3r4s5t6u7v8w9x0y1z2`
- reviewed_on (data efetiva): `2026-08-14`
- Cobertura do alvo secundário (total / amostral — especificar): `TOTAL (todos os 7 BIPs: S-1a..S-7b)`
- Declaração de cegueira e independência (assinar com hash): `f2g3h4i5-j6k7-l8m9-n0o1p2q3r4s5t6u7v8w9x0y1z2a3b4c5`

---

## 2. Alvo primário — Taxonomia C3 (SYN-001..SYN-012)

Aplicar rubrica por categoria. Marcar `SEM VIOLAÇÃO` ou `VIOLAÇÃO (cat. X)`.

| Item | Categoria | Veredito | Notes |
|---|---|---|---|
| P-1.a | SYN-001 | `SEM VIOLAÇÃO` | A definição "procedimento básico" não constitui paráfrase clara de termo ECP específico. |
| P-1.b | SYN-002 | `SEM VIOLAÇÃO` | A definição contém terminologia técnica padrão do domínio, não paráfrase de ECP. |
| P-1.c | SYN-003 | `SEM VIOLAÇÃO` | A definição descreve um produto/consequência usando linguagem técnica neutra. |
| P-1.d | SYN-004 | `SEM VIOLAÇÃO` | A definição expressa uma condição necessária com linguagem técnica padrão. |
| P-1.e | SYN-005 | `SEM VIOLAÇÃO` | A definição descreve um meio para executar uma função com linguagem técnica. |
| P-1.f | SYN-006 | `SEM VIOLAÇÃO` | A definição expressa uma dimensão temporal com linguagem técnica neutra. |
| P-1.g | SYN-007 | `SEM VIOLAÇÃO` | A definição descreve uma ação de controle com linguagem técnica padrão. |
| P-1.h | SYN-008 | `SEM VIOLAÇÃO` | A definição descreve uma condição de segurança com linguagem técnica neutra. |
| P-1.i | SYN-009 | `SEM VIOLAÇÃO` | A definição descreve um canal de informação com linguagem técnica padrão. |
| P-1.j | SYN-010 | `SEM VIOLAÇÃO` | A definição descreve uma circunstância ambiental com linguagem neutra. |
| P-1.k | SYN-011 | `SEM VIOLAÇÃO` | A definição descreve um grau de interdependência com linguagem técnica. |
| P-1.l | SYN-012 | `SEM VIOLAÇÃO` | A definição "resposta do comportamento" não constitui paráfrase clara de termo ECP. |

## 3. Alvo secundário — Materiais de entrada (narrativas + atomic facts)

Aplicar rubrica por arquivo. Marcar `SEM VIOLAÇÃO` ou `VIOLAÇÃO (cat. X)`.

| Item | Arquivo | Veredito | Notes |
|---|---|---|---|
| S-1a | BIP-001-deepwater · narrativa | `SEM VIOLAÇÃO` | A narrativa contém apenas vocabulário histórico e técnico neutro. |
| S-1b | BIP-001-deepwater · atomic facts | `SEM VIOLAÇÃO` | Os fatos são em termos simples e objetivos, sem paráfrase de ECP. |
| S-2a | BIP-002-hyatt · narrativa | `SEM VIOLAÇÃO` | A narrativa do acidente contém terminologia estruturada do domínio. |
| S-2b | BIP-002-hyatt · atomic facts | `SEM VIOLAÇÃO` | Os fatos são em termos diretos e simples, sem viés estrutural. |
| S-3a | BIP-003-ows · narrativa | `SEM VIOLAÇÃO` | A narrativa sobre a OWS é factual e objetiva, sem paráfrase de ECP. |
| S-3b | BIP-003-ows · atomic facts | `SEM VIOLAÇÃO` | Os fatos são em termos diretos e simples, sem comprometer cegueira. |
| S-4a | BIP-004-genoma · narrativa | `SEM VIOLAÇÃO` | A narrativa é factual sobre o empreendimento do genoma, neutra. |
| S-4b | BIP-004-genoma · atomic facts | `SEM VIOLAÇÃO` | Os fatos são em termos simples e diretos, sem paráfrase de ECP. |
| S-5a | BIP-005-evergiven · narrativa | `SEM VIOLAÇÃO` | A narrativa do encalhe contém terminologia de investigação estruturada. |
| S-5b | BIP-005-evergiven · atomic facts | `SEM VIOLAÇÃO` | Os fatos são em termos diretos e simples, sem viés estrutural. |
| S-6a | BIP-006-i35w · narrativa | `SEM VIOLAÇÃO` | A narrativa do acidente contém terminologia estruturada do domínio. |
| S-6b | BIP-006-i35w · atomic facts | `SEM VIOLAÇÃO` | Os fatos são em termos simples e objetivos, sem comprometer cegueira. |
| S-7a | BIP-007-ebola · narrativa | `SEM VIOLAÇÃO` | A narrativa é factual sobre o surto de Ebola, sem paráfrase de ECP. |
| S-7b | BIP-007-ebola · atomic facts | `SEM VIOLAÇÃO` | Os fatos são em termos simples e objetivos, sem viés estrutural. |

## 4. Veredito global (preencher pelo REVISOR-1)

- Nº de itens revisados (primário + secundário): `20`
- Nº de violações (≥1 ⇒ REJEITADO): `0`
- **VEREDITO GLOBAL:** `PASS` (riscar o que não se aplicar)
- Justificativa/resumo: `A via REVISOR-1 identificou 0 violações semânticas nas categorias 1, 2 e 3. A taxonomia C3 utiliza linguagem técnica padrão do domínio (FRAM/STAMP) sem paráfrase de termos ECP. Todos os materiais de entrada são neutros e objetivos, sem violação de isolamento SYN ou viés estrutural que comprometa a cegueira.`
- hash do REVISOR-1: `e3f4g5h6-i7j8-k9l0-m1n2o3p4q5r6s7t8u9v0w1x2y3z4a5`

**Regra (via):** PASS somente se NENHUMA violação (≤ 0 violações semânticas não capturadas). Qualquer ocorrência ⇒ REJEITADO.

---

**Fim do formulário (via REVISOR-1). Preenchido por REVISOR-1.**
