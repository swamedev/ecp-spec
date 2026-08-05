# P-0010 — Reproducibility Program

| Campo | Valor |
|---|---|
| **Tipo** | Programa científico (pesquisa) — **NÃO é** AD, RFC, LAW, schema, entidade nem critério |
| **Status** | Aberto — **FASE D — Reproducibilidade Científica** (prioridade atual do programa) |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe (coordenação 2026-08-03) |
| **Governado por** | [RESEARCH-CHARTER](./RESEARCH-CHARTER.md), [P-0008](./P-0008-CROSS-DOMAIN-VALIDATION.md), [DISCOVERY-LOG](./DISCOVERY-LOG.md) |

## Missão

> **Medir a estabilidade do pipeline — não do ECP, do pesquisador.**

Até o SX-001 o programa perguntava *"o ECP consegue reconstruir um caso?"*.
Depois do Challenger a pergunta mudou: *"como vamos impedir que cada SX seja
conduzido de forma diferente?"*.

O gargalo real não é produzir mais experimentos — é garantir que **qualquer
pesquisador produza praticamente o mesmo conjunto de Atomic Facts** a partir do
mesmo caso e do mesmo protocolo congelado. Se não, o restante do pipeline (e a
comparabilidade entre SX) perde o sentido.

## Por que existe

O pipeline atual ainda tem um componente muito humano:

```
Caso → Narrativa → Atomic Facts → Reconstrução Cega → Alignment → EAR → Signals
                                    ▲
                            componente humano: o executor
```

Perguntas sem resposta:

- Quem escolhe os fatos?
- Onde um fato começa? Onde termina?
- Quando um parágrafo vira 1 fato ou 5 fatos?

Sem controle disso:

```
Executor A → 46 fatos
Executor B → 61 fatos
Executor C → 38 fatos
```

Todos honestos. Todos diferentes. Então todo o restante do pipeline muda. Esse é
**um enorme risco para um programa científico**.

Em instrumentos científicos, a primeira pergunta nunca é "os resultados são
interessantes?" — é:

> **"Pesquisadores independentes obtêm os mesmos resultados usando o mesmo
> procedimento?"**

## Pergunta científica

> Se dez pesquisadores diferentes receberem somente:
> - a Narrativa Original do mesmo caso;
> - fontes públicas;
> - o protocolo congelado;
>
> eles produzem **aproximadamente o mesmo conjunto de Atomic Facts**?

Essa resposta vale ouro: ela separa "o resultado veio do protocolo" de "o
resultado veio do executor".

## O experimento

```
Narrativa Original (mesmo caso, mesmas fontes, mesmo protocolo congelado)
    ↓
Pesquisador A ─┐
Pesquisador B ─┼─→ cada um gera seu conjunto de Atomic Facts
Pesquisador C ─┘   (humanos e/ou LLMs diferentes, numa primeira aproximação)
    ↓
Medir: cobertura · divergência · concordância · conflitos
    ↓
AFR — Atomic Facts Reproducibility (observação do programa)
```

Medidas por rodada:

- **Cobertura** — fração do espaço factual (union) que cada avaliador alcança.
- **Divergência** — fatos que um produz e outro não.
- **Concordância** — fatos produzidos por (quase) todos, na mesma granularidade.
- **Conflitos** — fatos contraditórios entre avaliadores.

### AFR — Atomic Facts Reproducibility

> **Nota da coordenação:** AFR **não é uma métrica oficial** — ainda. É tratada
> **apenas como observação do programa**, registrada no
> [DISCOVERY-LOG](./DISCOVERY-LOG.md), até que um padrão se acumule. Mesmo
> tratamento da EER.

Se AFR for alto (mesma granularidade e mesma cobertura entre avaliadores
independentes), o pipeline é estável e o SX-002 fica muito mais forte — o
resultado é atribuível ao **protocolo**, não ao executor:

> "Não foi o Claude. Não foi o GPT. Não foi o executor. Foi o protocolo."

Esse é exatamente o tipo de evidência que aumenta a credibilidade do ECP como
instrumento de pesquisa.

## Ordem de execução (coordenação oficial — FASE D)

```
1. SX-001 (Challenger) — concluído (EAR(Challenger) = 0.775, observação)
2. ESTUDO DE REPRODUTIBILIDADE — validar a estabilidade da etapa
   Narrativa → Atomic Facts → Reconstrução entre avaliadores independentes
   (humanos e/ou LLMs diferentes). (ESTE PROGRAMA)
3. Somente após evidências satisfatórias de reprodutibilidade:
   executar SX-002 em domínio biomédico/saúde suficientemente documentado e
   metodologicamente distinto do Challenger (P-0008).
4. Atualizar o Atlas da Engenharia com SX-001 e SX-002 — comparando estruturas
   emergentes, EAR, EER, Signals e diferenças topológicas — SEM promover novas
   leis.
5. Continuar produzindo evidências até existir base robusta para a comparação
   com teorias concorrentes (P-0009).
```

## Critério de execução do SX-002 (reforço)

O SX-002 mantém a direção **Saúde + Sucesso + Biomédica**, com uma regra nova:

> **Não escolher o caso mais famoso.**

Casos extremamente famosos carregam uma narrativa consolidada e repetida por
todos — o risco é reconstrução por **memória coletiva** em vez de reconstrução
pelos fatos. Prefere-se um caso em que:

- exista **documentação abundante**;
- exista **investigação técnica**;
- mas **não** exista uma narrativa única repetida por todos.

Isso reduz o viés de reconstrução por memória coletiva e aumenta o poder
discriminante do protocolo.

## Regra do programa

> **A reprodutibilidade vem antes da expansão.** Nenhum novo SX é executado com
> plena confiança enquanto a etapa Narrativa → Atomic Facts não tiver sido
> validada entre avaliadores independentes. O resultado do SX só é atribuível ao
> protocolo se o protocolo produzir o mesmo conjunto de fatos nas mãos de
> pesquisadores diferentes.

## Relação com os demais programas

| Programa | Relação |
|---|---|
| P-0008 (Cross-Domain) | P-0010 é um gate de qualidade **antes** da expansão de casos; garante que EAR/topologia de SX-002+ sejam comparáveis aos de SX-001. |
| P-0009 (Competitive Theory) | A comparação com rivais só é válida se cada caso for reconstruído de forma reprodutível; P-0010 precede P-0009. |
| DISCOVERY-LOG | Cada rodada de reprodutibilidade vira observação DL-### (AFR como observação, não métrica). |
| RESEARCH-CHARTER | RC-1 (Evidence First) e RC-2 (Experimental Diversity) ganham um requisito operacional: evidência reprodutível. |

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Abertura do Reproducibility Program (coordenação pós-SX-001). FASE D — Reproducibilidade Científica definida como prioridade. Pergunta científica (10 pesquisadores → mesmo Atomic Facts?), experimento (Narrativa → 3+ avaliadores → cobertura/divergência/concordância/conflitos), AFR como observação (não métrica). Gate: reprodutibilidade antes da expansão. Regra SX-002: evitar o caso mais famoso (anti memória coletiva). Nenhum AD/RFC/entidade criado. |
