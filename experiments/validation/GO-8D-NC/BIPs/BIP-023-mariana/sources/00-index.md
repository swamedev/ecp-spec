# BIP-023-mariana - Fronteira e Indexamento

**Caso:** Barragem de Fundao / Samarco - Mariana (2015)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, 150 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `ibama-laudo` | Ibama - Laudo Tecnico Preliminar (Nov/2015) - copy oficial | https://ambientedomeio.com/wp-content/uploads/2016/01/laudo-preliminar-do-ibama-sobre-mariana.pdf | 2026-08-15 | `ibama-laudo.pdf` | acessivel |
| `ibama-portal` | Ibama - Rompimento da Barragem de Fundao (pagina oficial) | https://www.gov.br/ibama/pt-br/assuntos/notas/2020/rompimento-da-barragem-de-fundao-documentos-relacionados-ao-desastre-da-samarco-em-mariana-mg | 2026-08-15 | `ibama-portal.html` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `ibama-laudo.pdf` | `2782999d43c8389a5568263a6804b9f62ec9b67b76936ed69df045bec197fc57` |
| `ibama-portal.html` | `9c394e659cd9563767878bdf6a4033f60fff3a6f759eac4981903e0402bafefd` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.
