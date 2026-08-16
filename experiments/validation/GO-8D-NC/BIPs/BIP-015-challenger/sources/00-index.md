# BIP-015-challenger - Fronteira e Indexamento

**Caso:** Challenger (1986)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, 147 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `rogers-vol1` | Rogers Commission Report Vol 1 (NASA NTRS) | https://ntrs.nasa.gov/api/citations/19860015255/downloads/19860015255.pdf | 2026-08-15 | `rogers-vol1.pdf` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `rogers-vol1.pdf` | `6e820b6cf96a6f03f98cc539454ed7686e87f8be9a94bdfdb7ad69f995d5ef00` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.
