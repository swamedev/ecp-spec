# BIP-011 — Domino's Turnaround: Origem dos Documentos (Proveniência)

**Data:** 2026-08-14
**Autoridade:** DECISION D-04.2 (GO-8C); padrão P5 (manifest §5).
**Regra aplicada:** nenhuma importação de narrativa/atomic-facts/reconstrução dos SX. Fontes são públicas e primárias.

---

## Registro de proveniência

| ref | Origem (quem) | O quê | Quando | Canal | Tipo EI (SC-5) |
|---|---|---|---|---|---|
| `sec-01-10k-2009` | Domino's Pizza, Inc. (registrante; arquivamento obrigatório perante a U.S. Securities and Exchange Commission) | Form 10-K do ano fiscal encerrado em 3 de janeiro de 2010 (documento principal d10k.htm; arquivado em 2 de março de 2010) | exercício fiscal 2009 | SEC EDGAR, acession 0001193125-10-045334 | órgão regulador federal (SEC); arquivamento oficial da empresa com relatórios de administração, demonstrações financeiras auditadas e fatores de risco |
| `sec-02-10k-2010` | Domino's Pizza, Inc. | Form 10-K do ano fiscal encerrado em 2 de janeiro de 2011 (documento principal d10k.htm; arquivado em 1 de março de 2011) | exercício fiscal 2010 | SEC EDGAR, acession 0001193125-11-050979 | órgão regulador federal (SEC); arquivamento oficial com resultados do turnaround |

## Independência das origens (SC-5)

Duas origens causais independentes entre si (arquivamentos regulatórios em exercícios distintos):
1. **10-K 2009 (arquivado 2010)** — documento produzido no final do exercício de 2009; descreve a posição antes/durante a virada (inclui a reformulação de produto de 2009, o plano de sucessão com David Brandon e J. Patrick Doyle, e os resultados de 2009).
2. **10-K 2010 (arquivado 2011)** — documento do exercício seguinte; descreve os resultados de 2010 (crescimento de vendas das mesmas lojas, receita) e o desenrolar do turnaround.

Cada arquivamento foi preparado em data própria, com fatos auditados por firma de contabilidade registrada (PricewaterhouseCoopers LLP), e é uma fonte primária independente no tempo.

## Estado de coleta

- Coleta inicial concluída: 2 origens primárias baixadas para `raw/`, checksums registrados em `00-index.md`.
- Validação P2: arquivos HTML com marcadores de conteúdo confirmados ("DOMINO", "Brandon", "Doyle", "fiscal", "Pizza"); obtidos do SEC EDGAR oficial com User-Agent declarado.

## Conformidade

- Nada importado de SX-001/002/003.
- Fontes brutas obtidas de canal público oficial (SEC EDGAR); matéria-prima primária, não interpretativa.
