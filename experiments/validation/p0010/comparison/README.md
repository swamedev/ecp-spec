# P-0010 — Preparação da comparação A × B × C

Esta pasta contém a **infraestrutura de preparação** da comparação entre os
conjuntos de Atomic Facts dos Avaliadores A, B e C. Ela é deliberadamente
"burra": organiza o trabalho humano, mas **não** faz nenhum julgamento.

## Papel desta infraestrutura

- Reduzir o trabalho repetitivo (copiar AFs para as tabelas).
- Preservar 100% do julgamento científico para o **comparador humano**.
- Registrar que nenhuma correspondência foi calculada (auditoria).

## Regra de ouro

> A comparação é feita por um **comparador determinístico** (humano, com o apoio
> deste script apenas para montar as tabelas). **Nenhuma IA** alinha os fatos.
> A única variabilidade medida continua sendo a dos Avaliadores A, B e C.

## O que o script faz (e não faz)

### Faz
- Lê `input/evaluator-A.md`, `input/evaluator-B.md`, `input/evaluator-C.md`.
- Extrai de cada AF: **número** | **data** | **texto** | **fonte** (se presente).
- Gera as tabelas vazias em `comparison/`.
- Gera `output/report.txt` com apenas as contagens.

### NÃO faz
- ❌ comparar textos
- ❌ calcular similaridade
- ❌ usar embeddings
- ❌ usar regex "inteligente" / heurística de correspondência
- ❌ inferir correlações
- ❌ sugerir matches
- ❌ ordenar automaticamente
- ❌ preencher células vazias

## Arquivos

### `comparison/A-vs-B.csv`
Lado esquerdo preenchido com os AFs de A (referência); colunas `B`, `Texto B`,
`Tipo`, `Observação` **vazias** para preenchimento humano.

### `comparison/B-vs-C.csv`
Lado esquerdo preenchido com os AFs de B; colunas `C`, `Texto C` vazias.

### `comparison/A-vs-C.csv`
Lado esquerdo preenchido com os AFs de A; colunas `C`, `Texto C` vazias.

### `comparison/consensus-matrix.csv`
Referência = AFs de A; colunas `B`, `C`, `Status`, `Observação` vazias.

## Como preencher

Para cada linha, o comparador humano indica o que corresponde no outro
avaliador e classifica:

**Tipo (tabelas de comparação):**
- `1:1` — correspondência direta, mesma granularidade.
- `1:N` — um AF de referência implode vários do outro.
- `N:1` — vários AFs de um lado implodem um do outro.
- `Ausente` — sem correspondente no outro avaliador.
- `Conflito` — os dois lados se contradizem.

**Status (matriz de consenso):**
- `consenso`
- `granularidade`
- `divergência factual`
- `ausente`
- `revisar`

## Uso

```
python tools/build_comparison_tables.py
```

**Fail-fast:** se algum avaliador obrigatório estiver ausente, o script **não**
gera as tabelas nem o relatório, imprime um `ERROR` listando os arquivos
faltantes e termina com **exit code 1**. Assim ninguém inicia a comparação com
uma matriz incompleta por engano.

```
ERROR: missing evaluator(s):
  - evaluator-C.md
Comparison tables are incomplete.
No scientific comparison can begin until all required inputs exist.
```

Tudo é determinístico: dado o mesmo conjunto de arquivos de entrada, o script
produz exatamente as mesmas tabelas e o mesmo relatório (ou o mesmo erro).

## Estado atual

- ✅ `input/evaluator-A.md` → 46 AFs
- ✅ `input/evaluator-B.md` → 75 AFs (rodada 2, regenerada do zero; rodada 1
  descartada por contaminação metodológica — ver `P0010-B-EVALUATION/discarded/`)
- ✅ `input/evaluator-C.md` → 73 AFs (produzido por avaliador independente;
  workspace `P0010-C-EVALUATION/`)
- ✅ Tabelas geradas por `build_comparison_tables.py` (A-vs-B, A-vs-C, B-vs-C,
  consensus-matrix). **Nenhuma correspondência calculada** — aguardam
  preenchimento humano.

## Próximo passo (comparação científica)

Para cada linha das tabelas, o comparador humano indica a correspondência no
outro avaliador e classifica conforme a taxonomia do experimento:

- `erro documental`
- `erro de protocolo`
- `divergência de granularidade`
- `divergência factual`

Depois: cálculo do AFR (Aceptable Fact Reproducibility) e produção da matriz
de consenso.