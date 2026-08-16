# BIP-008 — Apollo 13: Origem dos Documentos (Proveniência)

**Data:** 2026-08-14
**Autoridade:** DECISION D-04.2 (GO-8C); padrão P5 (manifest §5).
**Regra aplicada:** nenhuma importação de narrativa/atomic-facts/reconstrução dos SX. Fontes são públicas e primárias.

---

## Registro de proveniência

| ref | Origem (quem) | O quê | Quando | Canal | Tipo EI (SC-5) |
|---|---|---|---|---|---|
| `nasa-01-a13-mission-report` | NASA Manned Spacecraft Center (MSC), Mission Evaluation Team (MET) | *Apollo 13 Mission Report* (MSC-02654) | setembro de 1970 | NASA Technical Reports Server (NTRS), identificador 19710003598 | agência federal de espaço/aeronáutica; relatório oficial de missão da equipe de avaliação |
| `nasa-02-a13-review-board` | NASA Apollo 13 Review Board (presidida por Edgar M. Cortright) | *Report of Apollo 13 Review Board* | 15 de junho de 1970 (publicação) | NASA Technical Reports Server (NTRS), identificador 19700078913 | painel de investigação nomeado pela agência; reporta ao Administrador da NASA |

## Independência das origens (SC-5)

Duas origens causais independentes entre si, ambas do poder público federal dos EUA:
1. **MSC/MET** — relatório de missão produzido pela equipe de avaliação do centro de voos tripulados, com dados da missão e do veículo.
2. **Apollo 13 Review Board** — investigação independente da causa do acidente, com testes e análises próprias, nomeada após o evento e reportada ao Administrador.

Cada uma produziu conteúdo por conta própria; o relatório da Review Board é a fonte da determinação de causa, enquanto o relatório de missão documenta os parâmetros e fatos da missão.

## Estado de coleta

- Coleta inicial concluída: 2 origens primárias baixadas para `raw/`, checksums registrados em `00-index.md`.
- Validação P2: PDFs íntegros (header `%PDF`, trailer `%%EOF`); conteúdo confirmado por extração de texto (Review Board: "APOLLO 13 REVIEW BOARD"; Mission Report: 158 p.).

## Conformidade

- Nada importado de SX-001/002/003.
- Fontes brutas obtidas de canal público (NTRS); matéria-prima primária, não interpretativa.
