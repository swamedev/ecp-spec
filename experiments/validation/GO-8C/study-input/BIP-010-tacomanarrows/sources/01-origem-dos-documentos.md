# BIP-010 — Tacoma Narrows: Origem dos Documentos (Proveniência)

**Data:** 2026-08-14
**Autoridade:** DECISION D-04.2 (GO-8C); padrão P5 (manifest §5).
**Regra aplicada:** nenhuma importação de narrativa/atomic-facts/reconstrução dos SX. Fontes são públicas e primárias.

---

## Registro de proveniência

| ref | Origem (quem) | O quê | Quando | Canal | Tipo EI (SC-5) |
|---|---|---|---|---|---|
| `caltech-01-carmody-board` | Board of Engineers nomeado pelo administrador do Federal Works Agency (John M. Carmody): Othmar H. Ammann, Theodore von Kármán, Glenn B. Woodruff | *The Failure of the Tacoma Narrows Bridge* — relatório ao Federal Works Agency | 28 de março de 1941 | CaltechAUTHORS (California Institute of Technology), registro q1ehq-5e206 (PDF escaneado do relatório original) | comissão de engenharia independente nomeada pelo poder executivo federal; relatório técnico de investigação |
| `wsdot-02-lessons-history` | Washington State Department of Transportation (WSDOT) | *Tacoma Narrows Bridge history — Lessons from the failure of a great machine* (página histórica oficial: danos, primeiras investigações, lições de projeto, "Why did Galloping Gertie collapse?") | publicação contínua (página institucional) | https://wsdot.wa.gov/tnbhistory/bridges-failure.htm (HTML íntegro) | órgão estadual de transportes; publicação institucional oficial do histórico e das lições do colapso |
| `wsdot-02-design-construction` | Washington State Department of Transportation (WSDOT), Office of Research & Library Services | *Documentation of the Design and Construction of the Tacoma Narrows Bridge* (relatório de pesquisa; cita e descreve o relatório Ammann-Kármán-Woodruff e os documentos históricos da ponte) | 2000 | WSDOT Research Reports, relatório 496.1 | órgão estadual de transportes; compilação documental histórica do projeto e construção (PDF escaneado, sem camada de texto — matéria-prima) |

## Independência das origens (SC-5)

Duas origens causais independentes entre si:
1. **Board of Engineers (1941)** — investigação técnica contemporânea ao colapso, produzida logo após o evento e reportada ao Federal Works Agency; fonte primária da determinação de causa.
2. **WSDOT (2000/página histórica)** — compilação documental histórica do Estado de Washington sobre o projeto, a construção e as lições do colapso; a página histórica (fonte de texto) é publicação institucional do próprio órgão.

Cada uma produziu conteúdo por conta própria; a segunda documenta o histórico e referencia o relatório da primeira como fonte externa, mas os fatos de projeto/construção provêm dos registros estaduais.

## Estado de coleta

- Coleta concluída: 2 origens primárias em `raw/` — `caltech-01-carmody-board.pdf` (287 p., texto extraível) e `wsdot-02-lessons-history.htm` (página oficial com texto integral) + `wsdot-02-design-construction.pdf` (34 p., **escaneado, sem camada de texto** — mantido como matéria-prima). Checksums em `00-index.md`.
- Validação P2: PDF íntegros (header `%PDF`, trailer `%%EOF`); conteúdo confirmado por extração de texto (Caltech: "THE FAILURE OF THE TACOMA NARROWS BRIDGE ... MARCH 28, 1941"; WSDOT página: "Lessons from the failure of a great machine"). O PDF do relatório WSDOT 496.1 não possui camada de texto extraível (0 caracteres em 34 páginas) — limitação registrada; substituído por `wsdot-02-lessons-history.htm` como fonte de texto do grupo WSDOT.

## Conformidade

- Nada importado de SX-001/002/003.
- Fontes brutas obtidas de canais públicos (CaltechAUTHORS; WSDOT); matéria-prima primária, não interpretativa.
