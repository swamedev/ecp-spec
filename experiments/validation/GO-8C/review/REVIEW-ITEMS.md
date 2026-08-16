# GO-8C — NT-05 Semantic Review — LISTA DE ITENS A REVISAR

**Data:** 2026-08-13
**Ciclo:** GO-8C
**Base:** `decisions/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` (escopo: alvo primário = 12 categorias C3; alvo secundário = materiais de entrada)
**Convenção de caminhos:** relativos a **`experiments/validation/GO-8C/review/`** (raiz do pacote de revisão). **TODOS os itens estão disponíveis localmente em `review/materials/`** — o revisor **NÃO precisa nem deve** acessar outras pastas do projeto.

---

## 1. Alvo primário — Taxonomia C3

| # | Tipo | Caminho (relativo a `review/`) | Itens |
|---|---|---|---|
| P-1 | C3_TAXONOMY | `materials/C3_TAXONOMY.yaml` | 12 categorias: `SYN-001` .. `SYN-012` |

> Aplicar a rubrica (Cat. 1 isolamento SYN / Cat. 2 paráfrase ECP / Cat. 3 viés estrutural) a **cada categoria** `SYN-001..SYN-012` (labels, definições, source_refs). 12 itens de formulário (P-1.a .. P-1.l).

## 2. Alvo secundário — Materiais de entrada

Narrativas reconstruídas e atomic facts dos 7 BIPs (BIP-003-warpspeed sem narrativa/atomic facts — diretório residual vazio, fora do escopo).

| # | BIP | Narrativa (relativo a `review/`) | Atomic facts (relativo a `review/`) |
|---|---|---|---|
| S-1 | BIP-001-deepwater | `materials/BIP-001-deepwater/narrative/01-narrativa-original.md` | `materials/BIP-001-deepwater/atomic-facts/02-atomic-facts.md` |
| S-2 | BIP-002-hyatt | `materials/BIP-002-hyatt/narrative/01-narrativa-original.md` | `materials/BIP-002-hyatt/atomic-facts/02-atomic-facts.md` |
| S-3 | BIP-003-ows | `materials/BIP-003-ows/narrative/01-narrativa-original.md` | `materials/BIP-003-ows/atomic-facts/02-atomic-facts.md` |
| — | BIP-003-warpspeed | *(fora do escopo — diretório residual vazio)* | — |
| S-4 | BIP-004-genoma | `materials/BIP-004-genoma/narrative/01-narrativa-original.md` | `materials/BIP-004-genoma/atomic-facts/02-atomic-facts.md` |
| S-5 | BIP-005-evergiven | `materials/BIP-005-evergiven/narrative/01-narrativa-original.md` | `materials/BIP-005-evergiven/atomic-facts/02-atomic-facts.md` |
| S-6 | BIP-006-i35w | `materials/BIP-006-i35w/narrative/01-narrativa-original.md` | `materials/BIP-006-i35w/atomic-facts/02-atomic-facts.md` |
| S-7 | BIP-007-ebola | `materials/BIP-007-ebola/narrative/narrative_pt.md` | `materials/BIP-007-ebola/atomic-facts/atomic_facts.md` |

> **Sobre a cobertura do alvo secundário:** o protocolo permite amostra OU total, conforme viabilidade. O revisor deve registrar no cabeçalho do formulário a **cobertura efetiva** (todos os S-1..S-7 ou subconjunto amostral). Recomendação: revisar **todos** os materiais listados (custo baixo; cobertura máxima).

## 3. Resumo de itens do formulário

- **Alvo primário:** 12 itens (P-1.a .. P-1.l) — um por categoria C3.
- **Alvo secundário:** 14 itens (S-1a..S-7a narrativa, S-1b..S-7b atomic facts) — um por arquivo de material (cobertura total) ou subconjunto (cobertura amostral registrada).

## 4. Identidade BIP-003 (definição inequívoca)

- O BIP-003 canônico do GO-8B é **Operation Warp Speed (OWS)**, pasta `BIP-003-ows` (item S-3) — conforme `P5-PRODUCTION-MANIFEST.md` §2 e `BIP-003-ows/README.md`.
- A pasta `BIP-003-warpspeed` **NÃO é um segundo caso**: é um **diretório residual vazio** (apenas `sources/raw/` sem arquivos; sem README/narrativa/atomic facts), **fora do escopo**.
- **O BIP-003 a ser revisado é exclusivamente o OWS (`BIP-003-ows`).**

---

**Fim da lista. Itens disponíveis em `review/materials/`. Prontos para preenchimento dos formulários (`REVIEW-FORM-MODEL-1.md` / `REVIEW-FORM-MODEL-2.md`).**
