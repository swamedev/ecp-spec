# GO-8C — NT-05 Extended — LISTA DE ITENS A REVISAR (5 novos BIPs)

**Data:** 2026-08-14
**Ciclo:** GO-8C
**Base:** `protocol/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` (escopo: alvo primário = 12 categorias C3; alvo secundário = materiais de entrada)
**Contexto:** NT-05 estendido (D-04) aos materiais dos 5 novos BIPs (008–012); aplica a mesma rubrica e o mesmo painel de 2 IAs independentes da D-03.
**Convenção de caminhos:** relativos a **`experiments/validation/GO-8C/review/nt05-extended/`** (raiz do pacote de revisão). **TODOS os itens estão disponíveis localmente em `materials/`** — o revisor **NÃO precisa nem deve** acessar outras pastas do projeto.

---

## 1. Alvo primário — Taxonomia C3

| # | Tipo | Caminho (relativo a `nt05-extended/`) | Itens |
|---|---|---|---|
| P-1 | C3_TAXONOMY | `materials/C3_TAXONOMY.yaml` | 12 categorias: `SYN-001` .. `SYN-012` |

> **Nota:** a taxonomia C3 do GO-8C foi corrigida na D-03.7 (definições de **SYN-001** e **SYN-012** substituídas por redação neutra, removendo paráfrases de "Funcao"/"Adaptacao"). Aplicar a rubrica (Cat. 1 isolamento SYN / Cat. 2 paráfrase ECP / Cat. 3 viés estrutural) a **cada categoria** `SYN-001..SYN-012` (labels, definições, source_refs). 12 itens de formulário (P-1.a .. P-1.l).

## 2. Alvo secundário — Materiais de entrada (5 novos BIPs)

Narrativas reconstruídas e atomic facts dos BIPs 008–012.

| # | BIP | Narrativa (relativo a `nt05-extended/`) | Atomic facts (relativo a `nt05-extended/`) |
|---|---|---|---|
| S-1 | BIP-008-apollo13 | `materials/BIP-008-apollo13/narrative/01-narrativa-original.md` | `materials/BIP-008-apollo13/atomic-facts/02-atomic-facts.md` |
| S-2 | BIP-009-chernobyl | `materials/BIP-009-chernobyl/narrative/01-narrativa-original.md` | `materials/BIP-009-chernobyl/atomic-facts/02-atomic-facts.md` |
| S-3 | BIP-010-tacomanarrows | `materials/BIP-010-tacomanarrows/narrative/01-narrativa-original.md` | `materials/BIP-010-tacomanarrows/atomic-facts/02-atomic-facts.md` |
| S-4 | BIP-011-dominos | `materials/BIP-011-dominos/narrative/01-narrativa-original.md` | `materials/BIP-011-dominos/atomic-facts/02-atomic-facts.md` |
| S-5 | BIP-012-eyjafjallajokull | `materials/BIP-012-eyjafjallajokull/narrative/01-narrativa-original.md` | `materials/BIP-012-eyjafjallajokull/atomic-facts/02-atomic-facts.md` |

> **Sobre a cobertura do alvo secundário:** o protocolo permite amostra OU total, conforme viabilidade. O revisor deve registrar no cabeçalho do formulário a **cobertura efetiva** (todos os S-1..S-5 ou subconjunto amostral). Recomendação: revisar **todos** os materiais listados (custo baixo; cobertura máxima).

## 3. Resumo de itens do formulário

- **Alvo primário:** 12 itens (P-1.a .. P-1.l) — um por categoria C3.
- **Alvo secundário:** 10 itens (S-1a..S-5a narrativa, S-1b..S-5b atomic facts) — um por arquivo de material (cobertura total) ou subconjunto (cobertura amostral registrada).
- **Total: 22 itens.**

---

**Fim da lista. Itens disponíveis em `materials/`. Prontos para preenchimento dos formulários (`REVIEW-FORM-MODEL-1.md` / `REVIEW-FORM-MODEL-2.md`).**
