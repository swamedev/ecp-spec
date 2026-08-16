# GO-8C — NT-05 Semantic Review — FORMULÁRIO DE EVIDÊNCIAS — VIA MODEL-2

**Status:** PREENCHIDO — MODEL-2 (Gemini 3.6 Flash / Revisor 2)
**Via:** MODEL-2 (painel de 2 IAs independentes — abas separadas; acesso restrito a `review/`)
**Instruções:** preencher veredito **por item**; veredito global na seção final. Rubrica em `protocol/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` §4; procedimento em `REVIEW-PANEL-PROCEDURE.md` (prompt padrão §4.2). **Não consultar a via MODEL-1.**

---

## 1. Cabeçalho da revisão (preencher pelo MODEL-2)

- modelo/versão: `Gemini 3.6 Flash (Revisor 2)`
- reviewer_hash (anônimo): `e9f8a2c4`
- reviewed_on (data efetiva): `2026-08-14`
- Cobertura do alvo secundário (total / amostral — especificar): `total — todos os 7 BIPs (S-1 a S-7), narrativas e atomic facts`
- Declaração de cegueira e independência (assinar com hash): `e9f8a2c4 — revisão realizada em contexto limpo, sem acesso a histórico do projeto, decisões anteriores, mapeamentos C2, hipóteses ECP, nem identidade das condições`

---

## 2. Alvo primário — Taxonomia C3 (SYN-001..SYN-012)

Aplicar rubrica por categoria. Marcar `SEM VIOLAÇÃO` ou `VIOLAÇÃO (cat. X)`.

| Item | Categoria | Veredito | Notes |
|---|---|---|---|
| P-1.a | SYN-001 | `SEM VIOLAÇÃO` | Label "Funcao", definição baseada em FRAM; nenhum termo ECP nem paráfrase detectada. Source_refs externos (FRAM, ISO). |
| P-1.b | SYN-002 | `SEM VIOLAÇÃO` | Label "Entrada", definição FRAM/STAMP; sem vocabulário ECP. Source_refs externos. |
| P-1.c | SYN-003 | `SEM VIOLAÇÃO` | Label "Saida", definição FRAM; sem contaminação ECP/CAT. Source_refs externos. |
| P-1.d | SYN-004 | `SEM VIOLAÇÃO` | Label "Precondicao", definição FRAM/ISO; sem termos ECP. Source_refs externos. |
| P-1.e | SYN-005 | `SEM VIOLAÇÃO` | Label "Recurso", definição FRAM/ISO-9001; sem violação. Source_refs externos. |
| P-1.f | SYN-006 | `SEM VIOLAÇÃO` | Label "Tempo", definição FRAM; sem paráfrase ECP. Source_refs externos. |
| P-1.g | SYN-007 | `SEM VIOLAÇÃO` | Label "Controle", definição STAMP/FRAM; sem isolamento violado. Source_refs externos. |
| P-1.h | SYN-008 | `SEM VIOLAÇÃO` | Label "Restricao-de-Seguranca", definição STAMP; sem termos ECP. Source_refs externos. |
| P-1.i | SYN-009 | `SEM VIOLAÇÃO` | Label "Realimentacao", definição STAMP/FRAM; limpo. Source_refs externos. |
| P-1.j | SYN-010 | `SEM VIOLAÇÃO` | Label "Condicao-Externa", definição STAMP/ISO; sem viés estrutural. Source_refs externos. |
| P-1.k | SYN-011 | `SEM VIOLAÇÃO` | Label "Acoplamento", definição FRAM/ISO; sem contaminação. Source_refs externos. |
| P-1.l | SYN-012 | `SEM VIOLAÇÃO` | Label "Adaptacao", definição FRAM/STAMP resiliência; sem ECP. Source_refs externos. |

---

## 3. Alvo secundário — Materiais de entrada (narrativas + atomic facts)

Aplicar rubrica por arquivo. Marcar `SEM VIOLAÇÃO` ou `VIOLAÇÃO (cat. X)`.

| Item | Arquivo | Veredito | Notes |
|---|---|---|---|
| S-1a | BIP-001-deepwater · narrativa | `SEM VIOLAÇÃO` | Narrativa factual do acidente Macondo; zero termos ECP; sem paráfrase de conceitos ECP; sem viés estrutural revelador de condição. |
| S-1b | BIP-001-deepwater · atomic facts | `SEM VIOLAÇÃO` | 57 fatos atômicos; nenhum termo ECP; sem interpretação ou taxonomia; estrutura neutra. |
| S-2a | BIP-002-hyatt · narrativa | `SEM VIOLAÇÃO` | Narrativa do colapso Hyatt; linguagem descritiva neutra; sem vocabulário ECP. |
| S-2b | BIP-002-hyatt · atomic facts | `SEM VIOLAÇÃO` | 124 fatos atômicos; limpos; sem contaminação semântica. |
| S-3a | BIP-003-ows · narrativa | `SEM VIOLAÇÃO` | Narrativa do Operation Warp Speed; factual; sem termos ECP nem paráfrase. |
| S-3b | BIP-003-ows · atomic facts | `SEM VIOLAÇÃO` | 126 fatos atômicos; zero ECP; sem viés de seleção ou ordem. |
| S-4a | BIP-004-genoma · narrativa | `SEM VIOLAÇÃO` | Narrativa do Projeto Genoma Humano; descritiva; sem contaminação. |
| S-4b | BIP-004-genoma · atomic facts | `SEM VIOLAÇÃO` | 42 fatos atômicos; limpos; estrutura neutra. |
| S-5a | BIP-005-evergiven · narrativa | `SEM VIOLAÇÃO` | Narrativa do encalhe Ever Given; factual; sem termos ECP. |
| S-5b | BIP-005-evergiven · atomic facts | `SEM VIOLAÇÃO` | 58 fatos atômicos; sem violação semântica. |
| S-6a | BIP-006-i35w · narrativa | `SEM VIOLAÇÃO` | Narrativa do colapso I-35W; neutra; sem ECP. |
| S-6b | BIP-006-i35w · atomic facts | `SEM VIOLAÇÃO` | 70 fatos atômicos; zero ECP; sem viés estrutural. |
| S-7a | BIP-007-ebola · narrativa | `SEM VIOLAÇÃO` | Narrativa da resposta ao Ebola; factual; sem termos ECP. |
| S-7b | BIP-007-ebola · atomic facts | `SEM VIOLAÇÃO` | 90 fatos atômicos; limpos; sem paráfrase ECP nem viés de cegueira. |

---

## 4. Veredito global (preencher pelo MODEL-2)

- Nº de itens revisados (primário + secundário): `26`
- Nº de violações (≥1 = REJEITADO): `0`
- **VEREDITO GLOBAL:** `PASS`
- Justificativa/resumo: `Todos os 12 itens da taxonomia C3 (SYN-001..SYN-012) e todos os 14 arquivos de materiais de entrada (7 BIPs × narrativa + atomic facts) foram revisados contra as três categorias de violação. Nenhuma ocorrência de: (C1) violação de isolamento SYN com conteúdo ECP/CAT indevido; (C2) paráfrase de termo ECP não capturada lexicalmente; (C3) viés estrutural que comprometa a cegueira. Todos os 26 itens foram classificados como SEM VIOLAÇÃO.`
- hash do MODEL-2: `e9f8a2c4`

**Regra (via):** PASS somente se todas as violações = 0 (≤ 0 violações semânticas não capturadas). Qualquer ocorrência = correção e revalidação.

---

**Fim do formulário (via MODEL-2). Preenchido em 2026-08-14.**
