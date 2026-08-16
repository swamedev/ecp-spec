# BIP-012 — Eyjafjallajökull: Origem dos Documentos (Proveniência)

**Data:** 2026-08-14
**Autoridade:** DECISION D-04.2 (GO-8C); padrão P5 (manifest §5).
**Regra aplicada:** nenhuma importação de narrativa/atomic-facts/reconstrução dos SX. Fontes são públicas e primárias.

---

## Registro de proveniência

| ref | Origem (quem) | O quê | Quando | Canal | Tipo EI (SC-5) |
|---|---|---|---|---|---|
| `icao-01-journal-2010` | International Civil Aviation Organization (ICAO) | ICAO Journal, Vol. 65, No. 4 (2010) — edição dedicada à crise das cinzas vulcânicas: "Safety as a Guiding Priority"; documenta a resposta da ICAO (EUR/NAT VATF, IVATF), os limites da política de evitação estrita e a revisão dos planos de contingência | 2010 (Vol. 65, No. 4) | site oficial da ICAO (icao.int, arquivo 6504_en.pdf) | organismo internacional de aviação civil; publicação oficial da organização |
| `iata-02-ash-plume` | International Air Transport Association (IATA), departamento de economia | *The Impact of Eyjafjallajokull's Volcanic Ash Plume* (IATA Economic Briefing) | maio de 2010 | repositório oficial da IATA (iata.org) | associação internacional de companhias aéreas; nota econômica com dados de cancelamentos e impacto de capacidade |

## Independência das origens (SC-5)

Duas origens causais independentes entre si:
1. **ICAO** — órgão intergovernamental de aviação civil; documenta a resposta regulatória/institucional e a revisão dos planos de contingência.
2. **IATA** — associação setorial das companhias aéreas; documenta o impacto operacional/econômico (cancelamentos, capacidade mundial).

Cada uma produziu conteúdo por conta própria, de perspectivas distintas (regulador internacional × indústria aérea); ambas são fontes primárias contemporâneas ao evento (2010).

## Estado de coleta

- Coleta inicial concluída: 2 origens primárias baixadas para `raw/`, checksums registrados em `00-index.md`.
- Validação P2: PDFs íntegros (header `%PDF`, trailer `%%EOF`); conteúdo confirmado por extração de texto (ICAO Journal Vol. 65 No. 4; IATA Economic Briefing, 4 p.).
- **Nota de coleta:** o ICAO Doc 9974 (Flight Safety and Volcanic Ash, 2012) e o EUR Doc 019/NAT Doc 006 Part II (Volcanic Ash Contingency Plan, dezembro de 2010) não estavam acessíveis nos URLs legados (HTTP 404) durante a coleta — registrado como limitação; as duas fontes válidas acima atendem ao requisito de ≥2 origens causais primárias independentes.

## Conformidade

- Nada importado de SX-001/002/003.
- Fontes brutas obtidas de canais públicos (icao.int; iata.org); matéria-prima primária, não interpretativa.
