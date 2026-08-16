# BIP-030-concordia - Fronteira e Indexamento

**Caso:** Costa Concordia (2012)
**Data de producao:** 2026-08-15
**Escopo de producao:** coleta e registro de fontes brutas primarias (BIP Acquisition Plan v1; gate 30/30)

---

## Materiais produzidos (narrativa e atomic facts)

- `narrative/01-narrativa-original.md` — narrativa (condicao C), zero ECP.
- `atomic-facts/02-atomic-facts.md` — atomic facts (condicoes A/B), zero ECP, 63 fatos.

## Fontes registradas

| id_fonte | descricao | url | data_acesso | arquivo (raw) | status |
|---|---|---|---|---|---|
| `mit-investigation` | MIT Marine Casualties Investigative Body - Costa Concordia report (2013) | https://maritimesafetyinnovationlab.org/wp-content/uploads/2020/11/MIT-Costa-Concordia-Grounding-Sinking-January-2012.pdf | 2026-08-15 | `mit-investigation.pdf` | acessivel |
| `protezione-civile` | Protezione Civile - Costa Concordia Shipwreck: Emergency Response Management (2012) | https://www.protezionecivile.gov.it/static/76e14a9fc11674a61ca53d088e7ab1d2/Pubblicazione_Concordia_ENG_web.pdf | 2026-08-15 | `protezione-civile.pdf` | acessivel |

## Checksums (SHA-256) das fontes brutas

| Arquivo | sha256 |
|---|---|
| `mit-investigation.pdf` | `c1279019bba76e1e168e9e5b3c31c53a0e94ceffc3e9fe190ece09472717e96f` |
| `protezione-civile.pdf` | `1101677762f53ccc9d4519ea763840b226e103b4e99a5328e66b6334817bc1a6` |

## Conformidade

- Apenas fontes brutas primarias registradas; nenhuma narrativa/atomic-facts/reconstrucao produzida nesta etapa.
- Rastreabilidade: cada atomic fact e cada bloco narrativo (etapa posterior) referenciarao os `id_fonte` acima.
- Cada fonte corresponde a arquivo em `sources/raw/` com SHA-256 registrado acima.
- Divergencia de hash entre registro e arquivo em disco -> rejeicao da fonte.
