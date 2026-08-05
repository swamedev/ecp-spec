# PARKING-LOT — Itens Arquivados para Futuras Fases

| Campo | Valor |
|-------|-------|
| **Tipo** | Registro em espera (não-AD, não-RFC, não-lei) |
| **Status** | Aberto — registrado durante a FASE E (estabilidade) |
| **Data** | 2026-08-04 |
| **Autor** | Coordenação (baseado em visão do Arquiteto-Chefe) |
| **Governado por** | [ROADMAP — FASE E](../ROADMAP.md), [P-0008](./P-0008-CROSS-DOMAIN-VALIDATION.md) |

## Propósito

Durante a FASE E (estabilidade metodológica), ideias valiosas são registradas **em espera**, para implementação apenas quando os dados e a maturidade do programa justificarem. As entradas possuem **critérios objetivos de ativação** — as mesmas regras que governam qualquer RFC, AD ou lei — para que possam ser promovidas automaticamente assim que estiverem justificadas por evidências.

## Regras

- **Registra-se visão, não implementação.**
- **Os critérios de ativação tornam-se o manifesto de evolução.**
- Durante a FASE E, **nenhum item da parking lot pode ser executado, editado ou promovido** ( Princípio da Suficiência Metodológica).
- Um item permanece em espera até que as evidências revisadas pelos pares atendam **ambas** às condições de ativação.

## Itens

### PL-001 — Fluxo futuro do Atlas (fluxo alternativo de casos)

- **Fonte:** visão do Arquiteto-Chefe, DL-022, coordenação 2026-08-04.
- **Visão:** depois de dezenas de casos, o fluxo será:
  ```
  Casos
    ↓
  Atlas
    ↓
  Hipóteses concorrentes
    ↓
  Seleção automática de novos casos
    ↓
  Novos experimentos
  ```
- **Visão vs. atual:** seleção do pesquisador → filtragem baseada em evidência.
- **Ativação:** (EC-1) existência de ≥30 casos reconstruídos (soma CX-001..CX-030).
- **Ativação:** (EC-2) existência de ≥3 hipóteses concorrentes (síndrome N-hipóteses, N≥3) *registradas* no [P-0009](./P-0009-COMPETITIVE-THEORY-VALIDATION.md) — evidência de competição além do ECP.
- **Ativação:** (EC-3) modelo de seleção automática (seleção baseada em hipóteses) implementado e testado (pilotado apenas após a execução do P-0009, ≥15 casos) — não uma regra.
- **Ativação:** (EC-4) ativação formal como **RFC** (não-AD) após dados revisados pelos pares.

### PL-002 — Três futuros gargalos (infraestrutura vs. método)

#### PL-002.1 — Gargalo de execução

- **Fonte:** coordenação 2026-08-04, DL-022.
- **Visão:** custo de produção de um SX completo.
- **Visão atual:** gargalo principal (P-0010). 
- **Ativação:** (EC-1) AFR < 0.70 por duas rodadas independentes do P-0010 (pilotado como observação no [DISCOVERY-LOG](./DISCOVERY-LOG.md), não como métrica formal).
- **Ativação:** (EC-2) gateway **ANTES** do SX-002 (observação) → piloto de “reproducibilidade e executabilidade” (inclui sugestão de automação para a etapa Narrativa → Atomic Facts).
- **Ativação:** (EC-3) registro como **RFC** após dados revisados pelos pares.

#### PL-002.2 — Gargalo de curadoria

- **Fonte:** coordenação 2026-08-04, DL-022.
- **Visão:** quando houver 30 SXs, milhares de Atomic Facts, centenas de Signals — como garantir consistência?
- **Visão atual:** registro como **dívida metodológica v1.1** (DEBT-003) — camada intermediária entre Narrativa e Reconstrução.
- **Ativação:** (EC-1) existência de ≥30 casos (CX-001..CX-030, acúmulo).
- **Ativação:** (EC-2) número de Atomic Facts > 5.000 (observação agregada no [DISCOVERY-LOG](./DISCOVERY-LOG.md)).
- **Ativação:** (EC-3) número de Signals ≥ 100 (como ocorrência registrada, não como resultado de promoção).  
- **Ativação:** (EC-4) pilune de ferramentas de curadoria (semação de padrões, revisão algorítmica) implementado e pilotado (apenas após o piloto de execução).
- **Ativação:** (EC-5) registro como **RFC**.

#### PL-002.3 — Gargalo estatístico

- **Fonte:** coordenação 2026-08-04, DL-022.
- **Visão:** avaliações posteriores a muitos casos: raro/comum? específico de domínio? efeito de seleção? artefato de amostra?
- **Visão atual:** comparação quantitativa inalterada (P-0008 mede diversidade, P-0009 mede melhor que rivais).
- **Ativação:** (EC-1) distribuição observacional de ≥50 casos reconstruídos (CX-001..CX-050, acúmulo de EER no [DISCOVERY-LOG](./DISCOVERY-LOG.md)).
- **Ativação:** (EC-2) estudo estatístico exploratório (estatística descritiva + teste de hipóteses em EER/Numerosidade do grafo) conduzido como **observação do programa** (sem métrica oficial, sem RFC).
- **Ativação:** (EC-3) padrões estatísticos reprodutíveis validados (ex.: consultas DB fixas, dossiê revisado pelos pares) — em espera até a execução do P-0010.
- **Ativação:** (EC-4) registro como **RFC**.

### PL-003 — Atlas como Observatório da Engenharia (do repositório ao instrumento)

- **Fonte:** visão do Arquiteto-Chefe, coordenação 2026-08-04.
- **Visão atual:** Atlas = Data Warehouse (comparação caso a caso).
- **Visão futura:** Atlas = Observatório da Engenharia — monitoramento contínuo de um fenômeno.
- **Ativação:** (EC-1) Atlas consistente por ≥5 domínios (CX-001..CX-005, observação agregada em [DISCOVERY-LOG](./DISCOVERY-LOG.md]).
- **Ativação:** (EC-2) pipeline expandido (observação contínua, não apenas comparação) operando por ≥2 anos de tempo real (pilotado apenas após execução de longo prazo).
- **Ativação:** (EC-3) métricas de monitoramento contínuo validadas (ex.: distribuição emergente, diagnóstico de estabilidade, ativação automática de sinal) — pilotadas como observações de programa, não como RFCs.
- **Ativação:** (EC-4) registro como **RFC** após revisão por pares.

### PL-004 — Seleção baseada em hipóteses (maximizar potencial de falsificação)

- **Fonte:** visão do Arquiteto-Chefe, coordenação 2026-08-04.
- **Visão:** escolher novos casos pelo potencial de contradizer hipóteses sobreviventes (em vez de apenas diversidade).
- **Visão atual:** máxima diversidade (matriz de três eixos), anti-viés de seleção (RC-2).
- **Ativação:** (EC-1) pelo menos 5 hipóteses concorrentes (incluindo rivais) sendo ativamente testadas como avaliação revisada pelos pares (correlação com P-0009).
- **Ativação:** (EC-2) distribuição observacional consistente (CX-001..CX-020) mostrando que uma única hipótese explica muitos domínios (chamada para potencial de falsificação).
- **Ativação:** (EC-3) candidato a algoritmo de seleção (fatores de pontuação baseados em hipóteses) implementado e validado (pilotado apenas após o candidato de curadoria).
- **Ativação:** (EC-4) registro como **RFC**.

## Regra de Promovação

- **Obrigatório:** nenhum item pode ser editado, promovido ou executado até que TODAS as condições de ativação sejam satisfeitas.
- **Sequência:** execução → curadoria → estatística → observatório → hipóteses (na ordem de ativação, se paralelo, sujeito à coordenação).
- **Documentação:** cada ativação cria uma entrada no [DISCOVERY-LOG](./DISCOVERY-LOG.md), vinculada ao registro de parking lot.
- **Governança:** apenas o **Arquiteto-Chefe** pode assinar a transição de um PL-XXX para RFC/AD, após revisão por pares.

## Histórico de revisão

| Versão | Data | Mudança |
|--------|------|------|
| 1.0 | 2026-08-04 | Abertura do Parking Lot — registro da visão como itens em espera durante a FASE E (estabilidade). Três gargalos futuros (execução, curadoria, estatístico), fluxo futuro do Atlas (do repositório ao instrumento) e seleção baseada em hipóteses registradas com critérios objetivos de ativação (EC-1..EC-4). |