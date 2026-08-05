# P-0009 — Competitive Theory Validation Program

| Campo | Valor |
|---|---|
| **Tipo** | Programa científico (pesquisa) — **NÃO é** AD, RFC, LAW, schema, entidade nem critério |
| **Status** | Aberto (charter) — **execução adiada** pela ordem de coordenação |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe (coordenação 2026-08-03) |
| **Governado por** | [RESEARCH-CHARTER](./RESEARCH-CHARTER.md), [P-0008](./P-0008-CROSS-DOMAIN-VALIDATION.md), [P-0006](./P-0006-LAW-DISCOVERY.md), [DISCOVERY-LOG](./DISCOVERY-LOG.md) |

## Missão

> **Nunca avaliar o ECP sozinho. Sempre contra rivais.**

A pergunta científica de um programa de pesquisa não é **"o ECP explica?"** —
é **"o ECP explica melhor que qualquer teoria concorrente?"**. Este programa
formaliza essa comparação: medir o **poder explicativo relativo** do ECP versus
teorias rivais de falha/análise de sistemas, nos mesmos casos, e construir
evidência comparativa — não apenas evidência interna.

## Por que existe

O SX-001 mediu apenas:

> "Quanto o ECP conseguiu reconstruir." (`EAR(Challenger) = 0.775`)

Não mediu:

> "Quanto outras teorias reconstruiriam o mesmo caso."

Se o Challenger também for bem explicado por STAMP, Swiss Cheese, FRAM, RCA,
OODA ou Systems Thinking, o EAR do ECP perde quase todo o poder de evidência.
Hoje **não sabemos**. Esse desconhecimento é o problema científico que este
programa ataca.

Isso transforma o nível de evidência exigido:

| Antes (P-0008) | Depois (P-0009) |
|---|---|
| "O ECP explica?" | "O ECP explica **mais**?" |
| Evidência de que a estrutura aparece | Evidência de que a estrutura explica **melhor que alternativas** |
| EAR(ECP) isolado | Matriz comparativa de EAR/rivais |

## Teorias concorrentes (concorrentes de referência)

Para cada caso SX-00X, quando a execução do P-0009 começar, o ECP será avaliado
**contra ao menos as seguintes** (familiares em falha/análise de sistemas):

- **STAMP** (Systems-Theoretic Accident Model and Processes — Leveson)
- **Swiss Cheese** (Reason — modelo de camadas de defesa)
- **Normal Accident Theory** (Perrow)
- **FRAM** (Functional Resonance Analysis Method)
- **Root Cause Analysis** (tradicional, árvores de causa)
- **OODA** (Observe–Orient–Decide–Act — Boyd)
- **Systems Thinking** (leitura sistêmica geral)

A lista é de **referência inicial**, não exaustiva, e pode ser ampliada por caso
(dependência do domínio). A seleção dos rivais por caso é registrada no próprio
caso — semântica de "model comparison".

## Matriz comparativa (forma de resultado)

Para cada caso, em vez de apenas `EAR(ECP)`:

```
Caso: SX-00X (domínio, natureza)

Teoria           EAR/Rácio    Observações
ECP              0.81         cadeia P→G→K→E→D emergiu; topologia X
STAMP            0.76         ...
FRAM             0.74         ...
RCA              0.62         ...
OODA             0.48         ...
```

Regras de leitura da matriz:

- **Empate** (`EAR(rival) ≈ EAR(ECP)`) não é derrota, mas **remove poder de
  evidência** do ECP — o caso não discrimina teorias.
- **Vitória** exige que o ECP explique **mais** que os rivais, idealmente com
  topologia que os rivais não capturam (ex.: a cadeia cognitiva completa).
- A matriz deve ser publicada **antes** de qualquer interpretação favorável
  (anti-hindsight — mesmo espírito do LAW-CRITERIA pré-congelado).

## Taxonomia provisória de leis (conceito de pesquisa — NÃO é artefato)

> **Nota da coordenação:** criada **apenas como conceito de pesquisa**, para
> orientar a leitura dos dados. Não é schema, não é critério, não é regra. Deve
> **emergir dos experimentos**, não ser assumida.

Lente provisória de classificação das futuras generalizações:

| Tipo | Define | Exemplo conceitual |
|---|---|---|
| **Estrutural** | o que deve existir | alguma forma de Problem, Goal, Decision |
| **Dinâmica** | como as entidades interagem no tempo | a ordem/emergência da cadeia |
| **Epistêmica** | condições para uma decisão ser justificável | Knowledge/Evidence antes de decidir |
| **Institucional** | múltiplos agentes, organizações, governança | decisões coletivas, hierarquia, contrato |

**Uso:** quando os dados dos SX acumularem, classificar cada generalização
candidata nesta lente e perguntar se a distribuição confirma a classe — se uma
classe ficar vazia ou saturada, a taxonomia é ajustada pelos dados, não por
preferência.

## Leis × Restrições (hipótese filosófica — NÃO muda nada agora)

> **Hipótese observacional da coordenação:** talvez o ECP não esteja descobrindo
> **leis** da engenharia, mas **restrições invariantes**.

| Formulação | Afirma |
|---|---|
| **Lei** | "A implica B" |
| **Restrição** | "Qualquer engenharia que viole isto deixa de ser justificável" |

A formulação como **restrição** aproxima o ECP do modo como áreas maduras tratam
invariantes e propriedades fundamentais.

**Regra de trabalho:** **nada muda agora.** Apenas observar, durante os próximos
SX, se os dados apontam mais para "leis" ou para "restrições" — e registrar isso
como observação no [DISCOVERY-LOG](./DISCOVERY-LOG.md) (DL-007). Não criar
artefato, não renomear LAW, não alterar LAW-CRITERIA.

## Ordem de trabalho (coordenação do Arquiteto-Chefe)

> **Não criar nenhum novo AD, RFC ou entidade. A fundação já está suficientemente
> rica.**

```
1. Executar SX-002, SX-003 e SX-004 em domínios radicalmente diferentes,
   seguindo exatamente o protocolo congelado (P-0008 / SX-SELECTION).
2. Construir o Atlas da Engenharia comparando topologias, EAR, EER e Signals
   entre casos — SEM promover novas leis (P-0008).
3. SOMENTE APÓS um conjunto consistente de casos: iniciar a execução deste
   programa (P-0009), medindo o poder explicativo relativo do ECP contra os
   rivais nos mesmos casos.
4. Só então reconsiderar a promoção de LAW-H para níveis superiores, com base
   em evidência COMPARATIVA — não apenas evidência interna.
```

**O charter está aberto agora; a execução começa na etapa 3.** Até lá, o P-0009
funciona apenas como compromisso registrado: quando a matriz comparativa existir,
a promoção de leis passa a exigir evidência comparativa.

## Regra de gate

> **Nenhuma LAW-H avança para níveis superiores com base apenas em evidência
> interna.** A promoção a partir deste ponto exige que a leitura ECP **explique
> melhor que as hipóteses concorrentes** nos casos em que for avaliada (RC-3,
> RC-5, RESEARCH-CHARTER).

Isso protege o programa do risco de se tornar "elegante e autorreferente": um
sistema que explica tudo com suas próprias categorias.

## Relação com os demais programas

| Programa | Relação |
|---|---|
| P-0008 (Cross-Domain) | Produz o Atlas e a distribuição; P-0009 acrescenta o eixo **comparativo** (explicar melhor que rivais). |
| P-0006 (Law Discovery) | P-0009 fornece o critério comparativo para as promoções que P-0006 decide. |
| DISCOVERY-LOG | Cada comparação com rivais vira observação (DL-###) com explicações/hipóteses concorrentes obrigatórias. |
| RESEARCH-CHARTER | RC-3 (Competing Explanations) e RC-5 (Asymmetry) são os princípios que este programa operacionaliza. |

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Abertura do Competitive Theory Validation Program (coordenação pós-SX-001). Missão: nunca avaliar o ECP sozinho, sempre contra rivais. Matriz comparativa EAR(ECP) × EAR(rivais). Taxonomia provisória de leis (estrutural/dinâmica/epistêmica/institucional) como conceito de pesquisa. Hipótese leis × restrições (observacional). Ordem de trabalho: execução adiada até conjunto consistente de casos (SX-002..004); gate de promoção com base em evidência comparativa. Nenhum AD/RFC/entidade criado. |
