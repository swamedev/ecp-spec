# BIP-010 — Tacoma Narrows: Fronteira e Indexamento

**Caso:** Colapso da Ponte Tacoma Narrows, Estado de Washington (1940)
**Data de produção:** 2026-08-14
**Escopo de produção (DECIDED D-04.2):** produção de materiais (fases P1–P4)

---

## Fronteira pré/pós gate

| Fase | Escopo permitido |
|---|---|
| **Pré-gate (produção P1–P4)** | Coleta, rastreamento e registro de fontes brutas primárias; produção de narrativa (condição C) e atomic facts (condições A/B), ambos com **zero termos ECP**, com rastreabilidade às fontes. |
| **Pós-gate (execução experimental)** | Apenas reconstrução anonimizada (labels neutros, arestas in/out, sem ECP) e análise conforme 04/06. **Não altera estes materiais.** |

## Fontes registradas

| ref | Arquivo (raw) | Tipo | Origem causal (grupo) |
|---|---|---|---|
| `caltech-01-carmody-board` | `caltech-01-carmody-board.pdf` | relatório oficial de investigação (Board of Engineers — O. H. Ammann, T. von Kármán, G. B. Woodruff, "The Failure of the Tacoma Narrows Bridge", relatório ao Federal Works Agency / administrador John M. Carmody, 28 de março de 1941; 287 p.) | Board of Engineers nomeado pelo Federal Works Agency (governo federal dos EUA); repositório CaltechAUTHORS |
| `wsdot-02-lessons-history` | `wsdot-02-lessons-history.htm` | página histórica oficial do Estado de Washington (WSDOT, "Tacoma Narrows Bridge history — Lessons from failure"; texto integral com lições, fatos do colapso e do projeto) | WSDOT (órgão estadual de transportes) |

> **Nota de coleta:** o PDF `wsdot-02-design-construction.pdf` (relatório 496.1, 2000) foi baixado e validado (checksum registrado abaixo), mas é **escaneado sem camada de texto extraível** (0 caracteres em 34 páginas, sem OCR disponível). Para garantir rastreabilidade de texto, a fonte efetiva de texto do WSDOT passou a ser a página oficial `wsdot-02-lessons-history.htm`; o PDF escaneado permanece registrado como matéria-prima documental.

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `caltech-01-carmody-board.pdf` | `227dd931284567a6173884740012ea2a4b73464f14c90de44e1ca9f74cb06344` |
| `wsdot-02-design-construction.pdf` | `cd47e9e3fe1c29a1910ccb6a747185b0efb83932874e2c47912270e21efb839c` |
| `wsdot-02-lessons-history.htm` | `37e4c7421186fd5926fd7d295b85ee321956fbc1de3751c5fe5242a86f9ea95f` |

## Conformidade

- Apenas fontes brutas primárias; nenhuma narrativa/atomic-facts/reconstrução de SX-001/002/003 importada.
- Rastreabilidade: cada atomic fact e cada bloco narrativo referenciam os `refs` acima.
