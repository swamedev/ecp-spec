# GO-8C — NT-05 Extended — FORMULÁRIO DE EVIDÊNCIAS — VIA MODEL-2

**Status:** CONCLUÍDO — PREENCHIDO PELO REVISOR 2
**Via:** MODEL-2 (painel de 2 IAs independentes — abas separadas; acesso restrito a `nt05-extended/`)
**Contexto:** NT-05 estendido aos 5 novos BIPs (008–012), decisão D-04.
**Instruções:** preencher veredito **por item**; veredito global na seção final. Rubrica em `protocol/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` §4. **Não consultar a via MODEL-1.**
**Acesso restrito:** ler somente arquivos dentro de `experiments/validation/GO-8C/review/nt05-extended/`. Não acessar outras pastas do projeto (não ler `study-input/`, `scripts/` além do `C3_TAXONOMY.yaml` aqui copiado, `decisions/`, histórico, etc.).

---

## 1. Cabeçalho da revisão (preencher pelo MODEL-2)

- modelo/versão: `Gemini 3.6 Flash (Revisor 2 Independente)`
- reviewer_hash (anônimo): `rev2-gemini36-dfa82b9e`
- reviewed_on (data efetiva): `2026-08-14`
- Cobertura do alvo secundário (total / amostral — especificar): `TOTAL (todos os 5 BIPs S-1..S-5, 10 arquivos)`
- Declaração de cegueira e independência (assinar com hash): `Declaro execução de revisão semântica independente em contexto isolado e cego. Não acessei histórico do projeto, decisões prévias, mapeamentos C2, hipóteses ECP nem arquivos fora de nt05-extended/. Hash: rev2-gemini36-dfa82b9e`

---

## 2. Alvo primário — Taxonomia C3 (SYN-001..SYN-012)

Aplicar rubrica por categoria (isolamento SYN / paráfrase ECP / viés estrutural). Marcar `SEM VIOLAÇÃO` ou `VIOLAÇÃO (cat. X)`.

| Item | Categoria | Veredito | Notes |
|---|---|---|---|
| P-1.a | SYN-001 | `SEM VIOLAÇÃO` | Definição neutra baseada em FRAM (Hollnagel 2012) e ISO-15288, sem contaminação ECP. |
| P-1.b | SYN-002 | `SEM VIOLAÇÃO` | Conceito neutro de entrada no modelo FRAM/STAMP, sem paráfrases ECP. |
| P-1.c | SYN-003 | `SEM VIOLAÇÃO` | Conceito de saída material/observável conforme FRAM, sem paráfrases ECP. |
| P-1.d | SYN-004 | `SEM VIOLAÇÃO` | Pré-condição alinhada a FRAM/ISO-15288, sem termos ou conceitos ECP. |
| P-1.e | SYN-005 | `SEM VIOLAÇÃO` | Recurso conforme FRAM/ISO-9001, isento de contaminação conceitual ECP. |
| P-1.f | SYN-006 | `SEM VIOLAÇÃO` | Dimensão temporal estritamente derivada de FRAM. |
| P-1.g | SYN-007 | `SEM VIOLAÇÃO` | Ação de regulação derivada de STAMP/FRAM, sem contaminação. |
| P-1.h | SYN-008 | `SEM VIOLAÇÃO` | Restrição de segurança derivada de STAMP Leveson 2011. |
| P-1.i | SYN-009 | `SEM VIOLAÇÃO` | Realimentacao conforme STAMP/FRAM, sem paráfrase de conceitos ECP. |
| P-1.j | SYN-010 | `SEM VIOLAÇÃO` | Condição externa neutra conforme STAMP/ISO-15288. |
| P-1.k | SYN-011 | `SEM VIOLAÇÃO` | Acoplamento derivado de FRAM e ISO-15288 interface. |
| P-1.l | SYN-012 | `SEM VIOLAÇÃO` | Adaptação em sistemas resilientes (FRAM/STAMP), sem paráfrases ECP. |

> A taxonomia C3 do GO-8C foi corrigida na D-03.7 (SYN-001 "Procedimento basico", SYN-012 "Resposta do comportamento"): verificar que as novas definições não reintroduzem paráfrase de "Funcao"/"Adaptacao".

## 3. Alvo secundário — Materiais de entrada (5 novos BIPs)

Aplicar rubrica por arquivo (Cat. 2 paráfrase de termo ECP / Cat. 3 viés estrutural). Marcar `SEM VIOLAÇÃO` ou `VIOLAÇÃO (cat. X)`.

| Item | Arquivo | Veredito | Notes |
|---|---|---|---|
| S-1a | BIP-008-apollo13 · narrativa | `SEM VIOLAÇÃO` | Narrativa histórica objetiva derivada dos relatórios NASA (mission report/review board), sem ECP. |
| S-1b | BIP-008-apollo13 · atomic facts | `SEM VIOLAÇÃO` | 68 fatos atômicos neutros e rastreáveis às fontes da NASA. |
| S-2a | BIP-009-chernobyl · narrativa | `SEM VIOLAÇÃO` | Narrativa técnica e histórica baseada em IAEA INSAG-1/INSAG-7, sem viés ou contaminação ECP. |
| S-2b | BIP-009-chernobyl · atomic facts | `SEM VIOLAÇÃO` | 72 fatos atômicos extraídos fielmente dos relatórios da IAEA. |
| S-3a | BIP-010-tacomanarrows · narrativa | `SEM VIOLAÇÃO` | Narrativa técnica de engenharia (Carmody Board / WSDOT), sem viés estrutural ou contaminação. |
| S-3b | BIP-010-tacomanarrows · atomic facts | `SEM VIOLAÇÃO` | 50 fatos atômicos estritamente factualizados sobre o colapso e investigação. |
| S-4a | BIP-011-dominos · narrativa | `SEM VIOLAÇÃO` | Narrativa de negócios derivada de relatórios SEC 10-K (2009/2010), sem termos ou viés ECP. |
| S-4b | BIP-011-dominos · atomic facts | `SEM VIOLAÇÃO` | 53 fatos atômicos de dados financeiros e operacionais neutros. |
| S-5a | BIP-012-eyjafjallajokull · narrativa | `SEM VIOLAÇÃO` | Narrativa da aviação civil (ICAO/IATA), sem contaminação ou viés ECP. |
| S-5b | BIP-012-eyjafjallajokull · atomic facts | `SEM VIOLAÇÃO` | 43 fatos atômicos objetivos sobre a erupção e impacto no tráfego aéreo. |

## 4. Veredito global (preencher pelo MODEL-2)

- Nº de itens revisados (primário + secundário): `22`
- Nº de violações (≥1 ⇒ REJEITADO): `0`
- **VEREDITO GLOBAL:** `PASS`
- Justificativa/resumo: `Revisão semântica completa realizada sobre 12 categorias C3 e 10 arquivos de materiais de entrada (5 BIPs). Nenhuma ocorrência de violação de isolamento SYN (Cat. 1), paráfrase de termo ECP (Cat. 2) ou viés estrutural (Cat. 3) foi identificada.`
- hash do MODEL-2: `rev2-gemini36-dfa82b9e`

**Regra (via):** PASS somente se NENHUMA violação (≤ 0 violações semânticas não capturadas). Qualquer ocorrência ⇒ REJEITADO (correção e revalidação).

---

**Fim do formulário (via MODEL-2). Aguardando preenchimento pelo revisor 2.**
