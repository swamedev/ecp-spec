# SX-003 / sources — Fontes do caso: Projeto Genoma Humano (1990–2003)

| Campo | Valor |
|---|---|
| **Experimento** | EXP-SX003 |
| **Etapa** | 0 — Verificação de fontes (SX-SELECTION, etapa 5) |
| **Data** | 2026-08-09 |
| **Status** | Acessibilidade pública confirmada para os grupos principais |

> **Regra EI (RA-EI-003):** fontes derivadas de um mesmo evento documental contam
> como **uma única origem causal**. A multiplicidade aqui é a da **origem**
> (programa público NHGRI/DOE × publicações revisadas × lado privado Celera ×
> financiadores internacionais × imprensa), não a do número de páginas.

> **Blindagem da coleta:** as fontes foram colhidas **antes** de qualquer uso do
> vocabulário do ECP. Nenhum termo do Kernel serviu de critério de seleção ou
> redação das fontes — são documentos públicos primários do caso.

## Grupo 1 — Programa público (governo dos EUA: NHGRI/NIH + DOE)

- **NHGRI — Human Genome Project Fact Sheet** — síntese oficial do NHGRI
  (genome.gov) sobre iniciantes, metas, custo, cronologia, resultados e
  implicações éticas (ELSI).
  - [Human Genome Project Fact Sheet](https://www.genome.gov/about-genomics/educational-resources/fact-sheets/human-genome-project)
  - snapshot local: [raw/nhgri-02-hgp-fact-sheet.html](../candidates/genoma-humano/sources/raw/nhgri-02-hgp-fact-sheet.html) (2026) —
    **fonte primária** de datas (1988 NAS, 1990 início, jun/2000 draft, abr/2003
    completo), custo (~US$ 3 bi), metas, Bermuda Principles, ELSI.
- **DOE — Human Genome Project Information Archive** (doe-humangenomeproject.ornl.gov)
  — histórico oficial do programa coordenado DOE/NIH, parceiros internacionais,
  metas e timeline do HGP.
  - snapshot: [raw/doe-01-hgp-information-archive.html](../candidates/genoma-humano/sources/raw/doe-01-hgp-information-archive.html)
  - páginas: [Overview](https://doe-humangenomeproject.ornl.gov/about-the-hgp/),
    [Research Goals](https://doe-humangenomeproject.ornl.gov/u-s-human-genome-project-research-goals/),
    [Timeline](https://doe-humangenomeproject.ornl.gov/human-genome-project-timeline/),
    [Budget](https://doe-humangenomeproject.ornl.gov/human-genome-project-budget/),
    [Private Sector](https://doe-humangenomeproject.ornl.gov/the-human-genome-project-the-private-sector/)
- **NHGRI — Human Genome Project page** ([raw/nhgri-01-human-genome-project.html]) —
  visão geral do NHGRI (reservada como checagem de conteúdo vs Fact Sheet).

## Grupo 2 — Publicações científicas revisadas por pares

- **International Human Genome Sequencing Consortium (IHGSC) — "Initial
  sequencing and analysis of the human genome", *Nature* 409, 860–921
  (15/02/2001)** — artigo-marco da **sequência-draft** financiada por
  financiamento público.
  - [PubMed — IHGSC 2001](https://pubmed.ncbi.nlm.nih.gov/11237011/) ·
    [raw/sci-01-pubmed-ihgsc-2001.html] · DOI 10.1038/35057062
- **Venter et al. (Celera) — "The sequence of the human genome", *Science*
  291, 1304–1351 (16/02/2001)** — artigo-marco da **sequência Celera**
  (whole-genome shotgun).
  - [PubMed — Venter 2001](https://pubmed.ncbi.nlm.nih.gov/11181995/) ·
    [raw/sci-02-pubmed-venter-2001.html] · DOI 10.1126/science.1058040

> Rasgos quantitativos citados (Nature: draft rascunho 90%, <400 gaps em 2003;
> Science: 2,91 Gb, 26.588 transcritos proteicos) provêm destes dois marcos
> revisados por pares — origens causais independentes entre si e do NHGRI/DOE.

## Grupo 3 — Lado privado — Celera Genomics (fonte independente)

- **Celera Genomics — site histórico (web.archive.org, snapshot 03/12/2000)** —
  registro oficial do esforço privado concurrent com o público.
  - [raw/celera-01-webarchive-2000.html] — snapshot do portal corporativo Celera
    (2000), evidência da existência pública do lado privado no período.

## Grupo 4 — Financiadores/coordenação internacional (complemento)

- **Wellcome Trust (Reino Unido)** — financiador importante do HGP na primeira
  fase (parceiro do DOE/NIH), conforme registro do DOE/ORNL.
- **Consórcio IHGSC — 20 centros em 6 países** (EUA, Reino Unido, França,
  Alemanha, Japão, China), conforme Fact Sheet NHGRI.
- Os arquivos `raw/nhgri-03-hgp-timeline.html` e outros registros dele chegam a
  snapshot override (404 para o timeline 1980-90); **verificação de
  acessibilidade: ver nota §"Estado")**.

## Grupo 5 — Enciclopédias/referência cruzada (qualquer checagem de datas)

- **Wikipedia — Human Genome Project** (referência cruzada somente; não contém
  como origem EI).

> **Risco da terminologia:** grupos 1–4 são origens causais **distintas
> (público + revisão por pares + privado + financiadores)**. Publicações
> derivadas de um mesmo corpo documental (ex.: vários painéis do NHGRI)
> contam como **um** — nunca como origens independentes.

## Veredito da verificação (etapa 5 do protocolo)

Grupos 1, 2, 3 e 4 são **públicos e acessíveis** (confirmado na reauditoria
2026-08-01 e reforçado nesta etapa via snapshots locais). O candidato **não é
eliminado por inacessibilidade (EC-3)**. SELECTABLE — confirmado por
[SX-REAUDIT.yaml](../../SX-REAUDIT.yaml).

## Nota operacional (não-método)

Os arquivos brutos foram promovidos do staging pré-gate
`candidates/genoma-humano/sources/raw/` para este experimento, **sem
transformação**: são os mesmos documentos capturados, preservando proveniência.
A presente coleção de fontes é o **material de entrada** da
[01-narrativa-original.md](../narrative/01-narrativa-original.md).

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-09 | Fontes do SX-003 (Genoma Humano 1990–2003) verificadas e consolidadas a partir do staging pré-gate. Quatro origens causais independentes declaradas. |