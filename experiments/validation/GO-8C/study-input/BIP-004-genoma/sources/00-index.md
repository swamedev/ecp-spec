# BIP-004 — Genoma Humano: Fronteira e Indexamento

**Caso:** Projeto Genoma Humano (1990–2003)
**Data de produção:** 2026-08-12
**Escopo de produção (DECIDED):** piloto BIP-004 (produção de materiais para A/B/C)

---

## Fronteira pré/pós gate

| Fase | Escopo permitido |
|---|---|
| **Pré-gate (produção P5)** | Coleta, rastreamento e registro de fontes brutas primárias; produção de narrativa (condição C) e atomic facts (condições A/B), ambos com **zero termos ECP**, com rastreabilidade às fontes. |
| **Pós-gate (execução experimental)** | Apenas reconstrução anonimizada (labels neutros, arestas in/out, sem ECP) e análise conforme 04/06. **Não altera estes materiais.** |

## Fontes registradas

| ref | Arquivo (raw) | Tipo | Conteúdo |
|---|---|---|---|
| `nhgri-01-hgp` | `nhgri-01-human-genome-project.html` | página institucional (Genome.gov) | visão geral do HGP; lançamento out/1990, conclusão abr/2003 |
| `nhgri-02-factsheet` | `nhgri-02-hgp-fact-sheet.html` | fact sheet (Genome.gov) | contexto, metas, método Sanger, custo, Bermuda Principles, ELSI, draft 2000 vs 2003 |
| `nhgri-03-timeline` | `nhgri-03-hgp-timeline.html` | arquivo capturado (resposta 404) | **conteúdo não extraível**; registrado como captura bruta, sem uso como fonte de conteúdo |
| `doe-01-archive` | `doe-01-hgp-information-archive.html` | página institucional (DOE) | coordenação DOE/NIH 13 anos; parceiros (Wellcome Trust, Japão, França, Alemanha, China) |
| `sci-01-ihgsc-2001` | `sci-01-pubmed-ihgsc-2001.html` | instrumento científico (PubMed, IHGSC) | Lander et al., Nature 2001; id 409(6822):860-921; draft público |
| `sci-01-nature-2001-full` | `sci-01-nature-2001-ihgsc.html` | texto completo (Nature/NIH) | artigo IHGSC; detalhe da sequência draft |
| `sci-02-venter-2001` | `sci-02-pubmed-venter-2001.html` | instrumento científico (PubMed, Celera) | Venter et al., Science 2001; shotgun de genoma completo; cinco doadores |
| `celera-01-2000` | `celera-01-webarchive-2000.html` | captura web (arquivo) | **somente aviso legal capturado**; sem conteúdo factual; sem uso como fonte de conteúdo |

> Nota de qualidade: `nhgri-03-timeline` (resposta 404) e `celera-01-2000` (apenas nota legal) estão registrados para integridade do rastreamento, **mas nenhuma narrativa/atomic fact deriva deles**. Fonte efetiva de conteúdo: 6 documentos (nhgri-01, nhgri-02, doe-01, sci-01-ihgsc-2001, sci-01-nature-2001-full, sci-02-venter-2001).

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `nhgri-01-human-genome-project.html` | `3fa0e62e892489f75f6459fc84b528231915442a61af1b32b1a75bbf55283365` |
| `nhgri-02-hgp-fact-sheet.html` | `6686848fa84934fd285c68dd68abb6facac2e195f81de7ae07a4edc1c2798790` |
| `nhgri-03-hgp-timeline.html` | `a646bb932013181a1f2dd236d2fbda8de1b12bab9790df9687a6b49899496c2d` |
| `doe-01-hgp-information-archive.html` | `42e07062e7dfbeb90cd8c29e1009b9cb982c1e04563f549b33b176b3e5f5e439` |
| `sci-01-pubmed-ihgsc-2001.html` | `574cc7299326e8a4c32bbb4581394aa8bae4385708d3624aa38df51d12f0f8a6` |
| `sci-01-nature-2001-ihgsc.html` | `751f91526da4eed83cad9e1fdd442a38b4077bd6d49be8d33f2e826767bedc92` |
| `sci-02-pubmed-venter-2001.html` | `091fa94aa9bf00e0ff60105c378a6e24dfc57ea777d2764589069a90774c7975` |
| `celera-01-webarchive-2000.html` | `8cbd7e19cb1422c31c7209c3811dd36fe2a2e17d3ff00deae70517f06fce2de9` |

## Conformidade

- Apenas fontes brutas primárias; nenhuma narrativa/atomic-facts/reconstrução de SX-001/002/003 importada.
- Rastreabilidade: cada atomic fact e cada bloco narrativo referenciam os `refs` acima.
