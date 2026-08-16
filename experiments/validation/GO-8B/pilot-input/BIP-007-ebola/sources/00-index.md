# BIP-007 — Resposta Ebola África Ocidental: Fronteira e Indexamento

**Caso:** Resposta internacional à epidemia de doença pelo vírus Ebola na África Ocidental (2014–2016)
**Data de produção:** 2026-08-12
**Escopo de produção (DECIDED):** produção de materiais (ordem manifest §3 — BIP-007); **coleta de fontes CONCLUÍDA em 2026-08-12**; **materiais PRODUZIDOS (narrativa + atomic facts) em 2026-08-12** (7/7 materiais de entrada do piloto prontos)

---

## Fronteira pré/pós gate

| Fase | Escopo permitido |
|---|---|
| **Pré-gate (produção P5)** | Coleta, rastreamento e registro de fontes brutas primárias; produção de narrativa (condição C) e atomic facts (condições A/B), ambos com **zero termos ECP**, com rastreabilidade às fontes. |
| **Pós-gate (execução experimental)** | Apenas reconstrução anonimizada (labels neutros, arestas in/out, sem ECP) e análise conforme 04/06. **Não altera estes materiais.** |

## Fontes coletadas (coleta-alta; múltiplas origens causais, SC-5)

| ref | Fonte proposta | Tipo | Origem causal (grupo) | Justificativa (aderência ao caso) | Status | Arquivo raw | SHA-256 | Texto extraído SHA-256 |
|---|---|---|---|---|---|---|---|---|
| `who-01-sitrep-jun2016` | WHO, *Ebola Situation Report — 10 June 2016* (final; 28 616 casos; 11 310 óbitos; fim do PHEIC em 29/03/2016) | relatório de situação (PDF) | OMS (agência especializada da ONU) | Números finais oficiais e linha do tempo do fim da epidemia; declaração de fim em Guiné (01/06) e Libéria (09/06) | **Coletado** (via Wayback, ver E-01) | `WHO-SitRep-2016-06-10.pdf` | `a356b2319997a837ea2d706af16770f222fcb29685d6bcba87361d931925b5c1` | `25f38089fe562bd129b31a6f15d3cfce2df1ce012115d8714427b248c2170860` |
| `who-02-overview-2014-2016` | WHO, *Ebola outbreak 2014-2016 — West Africa* (página oficial de situação) | página oficial (HTML) | OMS | Visão oficial do surto: início em Guiné (dez/2013), PHEIC (ago/2014), disseminação a 10 países, total >28 600 infectados e 11 325 óbitos | **Coletado** (direto) | `WHO-Overview-2014-2016.html` | `933e7ce1824810d83cb71b1f9bf0afdbe14437d221e19a09dff5325db4125f66` | *(HTML: leitura direta, sem extração)* |
| `nejm-01-ebola-9months` | WHO Ebola Response Team, *Ebola Virus Disease in West Africa — The First 9 Months of the Epidemic and Forward Projections* (NEJM 2014; 371:1481-1495) | artigo seminal revisado por pares | WHO Ebola Response Team / periódico científico (NEJM) | Análise epidemiológica dos primeiros 9 meses; projeções; dados clínicos e de letalidade | **Coletado** (direto, mirror oficial PAHO) | `NEJM-Ebola-First-9-Months-2014.pdf` | `1bf8632789e386870d335fc507db1d3de7a5f3ea4252f18097e1f2dc4c666906` | `2238b4527854b2eeb0a38a3b11b87c893e9dbfe968a91434197f92fc7341fbf6` |
| `msf-01-pushed-limit` | MSF, *Pushed to the limit and beyond: A year into the largest ever Ebola outbreak* (23/03/2015) | relatório operacional humanitário (PDF) | Médecins Sans Frontières (organização humanitária de campo) | Visão operacional do terreno: alertas precoces, déficit da resposta global, >1 300 internacionais e ~4 000 locais mobilizados, ~5 000 pacientes confirmados sob cuidado | **Coletado** (PDF oficial MSF UK; landing page descartada, ver E-03) | `MSF-Pushed-to-Limit-2015.pdf` | `a2f5c5cc93e6e2aa19c29d18088de94e56458a071e37de97ec9ea62013a57cd8` | `09f0bb462d215d94b01c828e631ac2834ef5d42ea5f6aa92bf56f835638b66a4` |
| `msf-02-facts-figures` | MSF, *Ebola 2014-2015 Facts & Figures / An Unprecedented Year* (23/03/2016) | relatório financeiro-operacional (PDF) | MSF | Dimensão da operação: 10 310 pacientes admitidos, 5 201 confirmados (~1/3 dos casos WHO), ~104 M€ gastos entre mar/2014 e dez/2015 | **Coletado** (PDF oficial, mirror msf.ie; ver E-02) | `MSF-Ebola-2014-2015-Facts-Figures.pdf` | `5a8f96bcca03541863294348757ba92a8b8e18ab6728f5838663b60a94a5e4e2` | `9ef4a639f2aa2dfb39a1dd8662aa49306f89cf24bc5f490aac76c300d9431191` |
| `cdc-01-mmwr-sep2014` | CDC, *Ebola Virus Disease Outbreak — West Africa, September 2014* (MMWR 63, early release 30/09/2014) | relatório epidemiológico oficial (HTML) | CDC / ministérios da saúde (autoridade federal de saúde dos EUA) | Situação epidemiológica em set/2014 (6 574 casos em 5 países); funerais como vetor de transmissão; esforço de resposta | **Coletado** (via Wayback, ver E-04) | `CDC-MMWR-Ebola-Sep-2014.html` | `a32e03b3d9611018168c8739331f62d6a1193bc7d2353a57dab183a45fd91a8c` | *(HTML: leitura direta, sem extração)* |
| `unmeer-01-mission` | ONU, *UN Mission for Ebola Emergency Response (UNMEER)* — página oficial da missão | página oficial (HTML) | Nações Unidas (missão de emergência em saúde) | Criação (19/09/2014, res. AG 69/1 e CS 2177), objetivos, princípios operacionais e encerramento (31/07/2015) com transição ao WHO | **Coletado** (direto) | `UNMEER-Mission.html` | `9723391f518dc5583f8bd94d26526feec2788bf4d6941512f5a2b70d3091f49f` | *(HTML: leitura direta, sem extração)* |
| `unmeer-02-sitrep` | UNMEER, *External Situation Report* (05/03/2015 — substitui 27/03/2015, ver E-05) | relatório de situação (PDF) | UNMEER | Operação no terreno da missão da ONU: coordenação regional, apoio aos países, logística | **Coletado** (direto, domínio oficial) | `UNMEER-External-SitRep-2015-03-05.pdf` | `ade566ceff87ade571952ba91b12124afacca4d28cb291c956371ac17375928d` | `496650d55d5f8971abcaa5a105b969129284f8f49d6b5d3676cbcc18789c1ffc` |

> **Ocorrências de acesso (E-01..E-05):** detalhes completos e tentativas em `sources/raw/00-fetch-errors.md`.

> **Origem causal adicional (facultativa, ciclo posterior):** relatórios nacionais dos ministérios da saúde de Guiné, Libéria e Serra Leoa; artigos do *The Lancet Global Health* sobre a resposta; relatório de avaliação independente do WHO (2015) sobre o manejo da crise.

> **Critério de coleta-alta atendido:** 8/8 fontes coletadas cobrindo ≥ 4 origens causais independentes (OMS; periódico científico com autoria OMS/acadêmica; MSF; CDC; ONU) — atende SC-5 e a matriz de diversidade do caso (saúde/biomédica, crise/falha parcial).

## Pendências

- **Extração de conteúdo** dos PDFs: **CONCLUÍDA em 2026-08-12** (5/5 PDFs → `.txt` via PyMuPDF/fitz; ocorrências em `raw/00-extraction-errors.md`; SHA-256 registrados na tabela acima). Nenhum erro não recuperado.
- **NT-05** do P2 segue pendente de validação humana (independe do BIP-007).

## Conformidade

- Apenas fontes brutas primárias públicas; nenhuma narrativa/atomic-facts/reconstrução de SX-001/002/003 importada.
- Rastreabilidade futura: cada atomic fact e cada bloco narrativo referenciarão os `refs` acima.

## Materiais produzidos (BIP-007, DATA SET COMPLETO)

| Artefato | Condição | Caminho | Estatística |
|---|---|---|---|
| Narrativa (não-cega) | C | [`../narrative/narrative_pt.md`](../narrative/narrative_pt.md) | 1.340 palavras; zero termos ECP |
| Atomic facts (cegas) | A/B | [`../atomic-facts/atomic_facts.md`](../atomic-facts/atomic_facts.md) | 90 fatos; zero termos ECP |
| Roteiro de validação | P5 §7 | [`../../validate_bip007.py`](../../validate_bip007.py) | 52 termos ECP; léxico + rastreabilidade |

> **Validação:** 0 hits ECP; 100% refs → esta tabela. Registro global em `pilot-input/VALIDATION-REPORT.md` (7/7 materiais de entrada).