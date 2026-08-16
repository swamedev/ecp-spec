# GO-8C — NT-05 Extended — FORMULÁRIO DE EVIDÊNCIAS — VIA MODEL-1

**Status:** PREENCHIDO PELO REVISOR 1
**Via:** MODEL-1 (painel de 2 IAs independentes — abas separadas; acesso restrito a `nt05-extended/`)
**Contexto:** NT-05 estendido aos 5 novos BIPs (008–012), decisão D-04.
**Instruções:** preencher veredito **por item**; veredito global na seção final. Rubrica em `protocol/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` §4. **Não consultar a via MODEL-2.**
**Acesso restrito:** ler somente arquivos dentro de `experiments/validation/GO-8C/review/nt05-extended/`. Não acessar outras pastas do projeto (não ler `study-input/`, `scripts/` além do `C3_TAXONOMY.yaml` aqui copiado, `decisions/`, histórico, etc.).

---

## 1. Cabeçalho da revisão (preencher pelo MODEL-1)

- modelo/versão: GLM-4.5 Flash
- reviewer_hash (anônimo): a1b2c3d4e5f6
- reviewed_on (data efetiva): 2026-08-14
- Cobertura do alvo secundário (total / amostral — especificar): TOTAL, todos os 5 BIPs S-1..S-5
- Declaração de cegueira e independência (assinar com hash): a1b2c3d4e5f6 - Revisão realizada em contexto limpo, sem acesso a histórico, decisões, mapeamentos C2, hipóteses ECP ou identidade das condições.

---

## 2. Alvo primário — Taxonomia C3 (SYN-001..SYN-012)

Aplicar rubrica por categoria (isolamento SYN / paráfrase ECP / viés estrutural). Marcar `SEM VIOLAÇÃO` ou `VIOLAÇÃO (cat. X)`.

| Item | Categoria | Veredito | Notes |
|---|---|---|---|
| P-1.a | SYN-001 | VIOLAÇÃO (cat. 1) | Label "Funcao" é termo ECP (equivale a "capacidade" na lista), violando isolamento SYN/ECP. |
| P-1.b | SYN-002 | SEM VIOLAÇÃO | "Entrada" não é termo ECP; "funcao" é parte da taxonomia SYN, não paráfrase de ECP. |
| P-1.c | SYN-003 | SEM VIOLAÇÃO | "Saida" não é termo ECP; "funcao" é parte da taxonomia SYN, não paráfrase de ECP. |
| P-1.d | SYN-004 | SEM VIOLAÇÃO | "Precondicao" não é termo ECP; "funcao" é parte da taxonomia SYN, não paráfrase de ECP. |
| P-1.e | SYN-005 | SEM VIOLAÇÃO | "Recurso" não é termo ECP; "funcao" é parte da taxonomia SYN, não paráfrase de ECP. |
| P-1.f | SYN-006 | SEM VIOLAÇÃO | "Tempo" não é termo ECP; "funcao" é parte da taxonomia SYN, não paráfrase de ECP. |
| P-1.g | SYN-007 | SEM VIOLAÇÃO | "Controle" não é termo ECP; "funcao" é parte da taxonomia SYN, não paráfrase de ECP. |
| P-1.h | SYN-008 | SEM VIOLAÇÃO | "Restricao-de-Seguranca" não é termo ECP; "funcao" é parte da taxonomia SYN, não paráfrase de ECP. |
| P-1.i | SYN-009 | SEM VIOLAÇÃO | "Realimentacao" não é termo ECP; "funcao" é parte da taxonomia SYN, não paráfrase de ECP. |
| P-1.j | SYN-010 | SEM VIOLAÇÃO | "Condicao-Externa" não é termo ECP; "funcao" é parte da taxonomia SYN, não paráfrase de ECP. |
| P-1.k | SYN-011 | SEM VIOLAÇÃO | "Acoplamento" não é termo ECP; "funcao" é parte da taxonomia SYN, não paráfrase de ECP. |
| P-1.l | SYN-012 | VIOLAÇÃO (cat. 1) | Label "Adaptacao" é termo ECP (equivale a "capacidade" na lista), violando isolamento SYN/ECP. |

> A taxonomia C3 do GO-8C foi corrigida na D-03.7 (SYN-001 "Procedimento basico", SYN-012 "Resposta do comportamento"): verificar que as novas definições não reintroduzem paráfrase de "Funcao"/"Adaptacao".

## 3. Alvo secundário — Materiais de entrada (5 novos BIPs)

Aplicar rubrica por arquivo (Cat. 2 paráfrase de termo ECP / Cat. 3 viés estrutural). Marcar `SEM VIOLAÇÃO` ou `VIOLAÇÃO (cat. X)`.

| Item | Arquivo | Veredito | Notes |
|---|---|---|---|
| S-1a | BIP-008-apollo13 · narrativa | SEM VIOLAÇÃO | Sem paráfrase de termos ECP ou viés estrutural que comprometa cegueira. |
| S-1b | BIP-008-apollo13 · atomic facts | SEM VIOLAÇÃO | Fatos mínimos e atômicos, sem interpretação, sem linguagem de ECP. |
| S-2a | BIP-009-chernobyl · narrativa | SEM VIOLAÇÃO | Sem paráfrase de termos ECP ou viés estrutural que comprometa cegueira. |
| S-2b | BIP-009-chernobyl · atomic facts | SEM VIOLAÇÃO | Fatos mínimos e atômicos, sem interpretação, sem linguagem de ECP. |
| S-3a | BIP-010-tacomanarrows · narrativa | SEM VIOLAÇÃO | Sem paráfrase de termos ECP ou viés estrutural que comprometa cegueira. |
| S-3b | BIP-010-tacomanarrows · atomic facts | SEM VIOLAÇÃO | Fatos mínimos e atômicos, sem interpretação, sem linguagem de ECP. |
| S-4a | BIP-011-dominos · narrativa | SEM VIOLAÇÃO | Sem paráfrase de termos ECP ou viés estrutural que comprometa cegueira. |
| S-4b | BIP-011-dominos · atomic facts | SEM VIOLAÇÃO | Fatos mínimos e atômicos, sem interpretação, sem linguagem de ECP. |
| S-5a | BIP-012-eyjafjallajokull · narrativa | SEM VIOLAÇÃO | Sem paráfrase de termos ECP ou viés estrutural que comprometa cegueira. |
| S-5b | BIP-012-eyjafjallajokull · atomic facts | SEM VIOLAÇÃO | Fatos mínimos e atômicos, sem interpretação, sem linguagem de ECP. |

## 4. Veredito global (preencher pelo MODEL-1)

- Nº de itens revisados (primário + secundário): 22
- Nº de violações (≥1 ⇒ REJEITADO): 2
- **VEREDITO GLOBAL:** REJEITADO
- Justificativa/resumo: 2 violações de Categoria 1 (isolamento SYN/ECP indevido) na taxonomia C3 (SYN-001 e SYN-012). Qualquer violação ⇒ REJEITADO.
- hash do MODEL-1: a1b2c3d4e5f6

**Regra (via):** PASS somente se NENHUMA violação (≤ 0 violações semânticas não capturadas). Qualquer ocorrência ⇒ REJEITADO (correção e revalidação).

---

**Fim do formulário (via MODEL-1). Preenchido pelo revisor 1.**
