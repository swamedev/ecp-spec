# BIP-009 — Chernobyl Unidade 4: Origem dos Documentos (Proveniência)

**Data:** 2026-08-14
**Autoridade:** DECISION D-04.2 (GO-8C); padrão P5 (manifest §5).
**Regra aplicada:** nenhuma importação de narrativa/atomic-facts/reconstrução dos SX. Fontes são públicas e primárias.

---

## Registro de proveniência

| ref | Origem (quem) | O quê | Quando | Canal | Tipo EI (SC-5) |
|---|---|---|---|---|---|
| `iaea-02-insag1` | International Atomic Energy Agency (IAEA) — International Nuclear Safety Advisory Group (INSAG) | *Summary Report on the Post-Accident Review Meeting on the Chernobyl Accident* (Safety Series No. 75-INSAG-1) | 1986 (reunião de revisão pós-acidente; relatório publicado em 1986) | IAEA INIS (International Nuclear Information System), registro INIS 8e700-gms57 | organismo internacional de energia nuclear; grupo consultivo internacional de segurança |
| `iaea-01-insag7` | IAEA — INSAG | *The Chernobyl Accident: Updating of INSAG-1* (Safety Series No. 75-INSAG-7) | 1992 (publicação; STI/PUB/913, ISBN 92-0-104692-8) | IAEA Publications (www-pub.iaea.org), `Pub913e_web.pdf` | organismo internacional de energia nuclear; atualização do INSAG-1 com novos dados soviéticos |

## Independência das origens (SC-5)

Duas origens causais independentes entre si:
1. **INSAG-1 (1986)** — conclusões da reunião de revisão pós-acidente, com forte ênfase nas ações da equipe de operação; reflete o entendimento imediato pós-evento.
2. **INSAG-7 (1992)** — atualização baseada em estudos soviéticos posteriores (relatórios do Comitê Estatal da URSS e do grupo de trabalho de especialistas soviéticos, traduzidos pelo IAEA), deslocando ênfase das ações da equipe para características de projeto do reator RBMK e do sistema de controle e proteção.

Cada uma produziu conteúdo por conta própria e em momentos distintos; a segunda documenta a revisão da primeira com informação nova. Nenhuma deriva de artefatos interpretativos dos SX.

## Estado de coleta

- Coleta inicial concluída: 2 origens primárias baixadas para `raw/`, checksums registrados em `00-index.md`.
- **Nota de integridade P2:** os nomes de arquivo foram ajustados após validação de conteúdo — `iaea-02-insag1.pdf` contém o texto "75-INSAG-1 / Summary Report on the Post-Accident Review Meeting" (123 p.) e `iaea-01-insag7.pdf` contém "75-INSAG-7 / Updating of INSAG-1" (148 p.). A confirmação foi feita por extração de texto.

## Conformidade

- Nada importado de SX-001/002/003.
- Fontes brutas obtidas de canais públicos (IAEA INIS; IAEA Publications); matéria-prima primária, não interpretativa.
