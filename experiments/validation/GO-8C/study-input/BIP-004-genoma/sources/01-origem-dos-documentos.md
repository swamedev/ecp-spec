# BIP-004 — Genoma Humano: Origem dos Documentos (Proveniência)

**Data:** 2026-08-12
**Autoridade:** DECISION P5-INPUT-MATERIALS; manifest §5 (fontes brutas podem ser cópia/rastreadas; artefatos interpretativos não).
**Regra aplicada:** nenhuma importação de narrativa/atomic-facts/reconstrução dos SX. Fontes são públicas e primárias.

---

## Registro de proveniência

| ref | Origem (quem) | O quê | Quando | Canal | Tipo EI (SC-5) |
|---|---|---|---|---|---|
| `nhgri-01-hgp` | National Human Genome Research Institute (EUA) | visão geral do HGP | página atualizada em 2025-03-19 | website `genome.gov/human-genome-project` | instituição de pesquisa pública |
| `nhgri-02-factsheet` | NHGRI (EUA) | fact sheet oficial do HGP | atualizado em 2024-06-13 | website `genome.gov` -> Fact Sheets | instituição de pesquisa pública |
| `nhgri-03-timeline` | NHGRI (EUA) | timeline do HGP | captura do arquivo `.html` (resposta HTTP 404) | website `genome.gov` | instituição de pesquisa pública (**sem conteúdo extraído**) |
| `doe-01-archive` | U.S. Department of Energy (EUA) | arquivo do HGP; coordenação DOE/NIH | página vigente | website `genomicscience.energy.gov` | agência governamental (EUA) |
| `sci-01-ihgsc-2001` | International Human Genome Sequencing Consortium / Nature | resumo do artigo Lander et al. | 2001-02-15 | PubMed (PMID 11237011) | instrumento científico revisado por pares |
| `sci-01-nature-2001-full` | Nature / NIH (NCBI) | texto completo do artigo IHGSC | 2001 | Nature 409(6822):860-921 | instrumento científico revisado por pares |
| `sci-02-venter-2001` | Celera Genomics / Science | resumo do artigo Venter et al. | 2001-02-16 | PubMed (PMID 11181995) | instrumento científico revisado por pares |
| `celera-01-2000` | Celera Genomics | página web arquivada | captura 2000 | arquivo web | empresa privada (**somente aviso legal**) |

## Independência das origens (SC-5)

Origens causais independentes entre si:
1. **Agência governamental (DOE)** — coordenação e financiamento.
2. **Instituto de pesquisa público (NHGRI/NIH)** — liderança científica e financiamento.
3. **Instrumentos científicos (Nature/Science via PubMed)** — publicação revisada por pares da sequência draft e da sequência shotgun.
4. **Empresa privada (Celera)** — abordagem de sequenciamento distinta (whole-genome shotgun).

Os dois documentos sem conteúdo extraído (`nhgri-03-timeline`, `celera-01-2000`) permanecem rastreados para integridade, sem uso como fonte de conteúdo.

## Checksums

Registrados em `00-index.md` (tabela SHA-256) e confirmados contra os arquivos em `sources/raw/`.

## Conformidade

- Nada importado de SX-001/002/003.
- Fontes brutas copiadas do staging `independence/candidates/genoma-humano/raw` (matéria-prima primária, não interpretativa).
