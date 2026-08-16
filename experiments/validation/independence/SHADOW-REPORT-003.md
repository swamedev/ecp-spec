# SHADOW-REPORT-003 — Seleção do SX-003 (Projeto Genoma Humano)

| Campo | Valor |
|---|---|
| **Tipo** | Registro de seleção do Shadow Experiment 003 |
| **Status** | Selecionado (etapas 7-8 do SX-SELECTION; direção pré-registrada aplicada) |
| **Data** | 2026-08-09 |
| **Autor** | Protocolo SX-SELECTION (decisão automática; nenhuma preferência humana) + direção de escopo pré-registrada pela coordenação |
| **Governado por** | [SX-SELECTION](./SX-SELECTION.md), [SHADOW-EXPERIMENTS](./SHADOW-EXPERIMENTS.md), [SX-REAUDIT.yaml](./SX-REAUDIT.yaml), [00-pre-registro.md](./SX-003/00-pre-registro.md) |
| **Referências** | [P-0007](../P-0007-INDEPENDENCE.md), [P-0007.1](../P-0007.1-INDEPENDENCE-FRAMEWORK.md), [P-0007.2](../P-0007.2-CANDIDATE-REAUDIT.md) |

## Propósito do SX-003 (direção pré-registrada)

Atacar [DEBT-009](../METHODOLOGICAL-DEBT.md): os SX-001 e SX-002 observaram
apenas **casos de crise/falha**. O SX-003 observa um caso com **desfecho
pré-classificado como sucesso**, para testar se a estrutura/ausências dos casos
de crise também emergem em um sucesso (teste da predição inversa de SIG-002).
Definição operacional de "sucesso" (SUC-1..SUC-3) foi **fixada antes** de olhar
candidatos ([00-pre-registro.md](./SX-003/00-pre-registro.md)).

## Aplicação da direção ao universo SELECTABLE (etapas 4-7)

O universo é o conjunto **SELECTABLE** da reauditoria congelada
([SX-REAUDIT.yaml](./SX-REAUDIT.yaml)), restringido pela direção de escopo
(coordenação) **e** pelo protocolo congelado (matriz SC, EC, re-auditoria). A
direção é escopo, **não** critério novo.

| Candidato SELECTABLE | Domínio | Desfecho | SUC-1 | SUC-2 | SUC-3 | Pasa p/ SX-003? |
|---|---|---|---|---|---|---|
| Apollo 13 (1970) | Espacial | Recuperação de missão comprometida | Sim | **Não** (origem em incidente) | Sim | **Não** |
| Challenger (1986) | Espacial | Falha | — | — | — | Não (crise) |
| I-35W (2007) | Civil | Falha | — | — | — | Não (crise) |
| Deepwater Horizon (2010) | Industrial | Falha | — | — | — | Não (crise) |
| Chernobyl (1986) | Industrial | Falha | — | — | — | Não (crise) |
| Ebola (2014-2016) | Saúde | Crise de coordenação | — | — | — | Não (crise; já SX-002) |
| **Suez / Ever Given (2021)** | Logística | Incidente resolvido | Sim | **Não** (origem em incidente) | Sim | **Não** |
| **Operation Warp Speed (2020-2021)** | Saúde | Sucesso operacional (prazo curto) | Sim | Sim | Sim | **Sim** |
| **Genoma Humano (1990-2003)** | Pesquisa Científica | Sucesso científico (prazo longo) | Sim | Sim | Sim | **Sim** |

### Candidatos que passam a direção

- **Operation Warp Speed (OWS)** — sucesso operacional/medicinal em prazo curto;
  ≥3 origens causais (GAO, HHS/BARDA, empresas, imprensa).
- **Projeto Genoma Humano (HGP)** — sucesso científico de longo prazo; ≥3 origens
  causais (NHGRI/DOE, Nature/Science, Celera, imprensa).

## Aplicação das prioridades pré-registradas (etapa 7)

Para mais de um elegível no escopo, prioridade: **(a) domínio mais distante do
software → (b) preferência por postmortem → (c) maior multiplicidade de origens.**

1. **(a) Domínio mais distante do software:** ambos são fora-de-software. Porém,
   a **diversidade de domínios** (P-0008 Cross-Domain; diretriz da fila
   "cobrir domínio ainda não observado") é determinante: **OWS repete o domínio
   Saúde já observado no SX-002 (Ebola)**; **HGP introduz um domínio ainda não
   observado — Pesquisa Científica** (taxonomia canônica). O SX-003 deve
   maximizar a cobertura de domínios.
2. **(b) Postmortem público:** não aplicável por natureza a sucesso; não
   discrimina.
3. **(c) Maior multiplicidade de origens causais:** HGP tem ≥4 grupos de origem
   causal independente (programa público NHGRI/DOE, publicações revisadas
   Nature/Science, lado privado Celera, financiadores/coordenação Wellcome,
   imprensa) — multiplicidade **superior** à de OWS (GAO, agências, empresas,
   imprensa).

Portanto:

> **O protocolo seleciona o Projeto Genoma Humano (1990–2003), domínio
> Pesquisa Científica, como alvo do SX-003.**

Nenhuma votação, preferência ou gosto pessoal. A escolha decorre das regras
congeladas + escopo de direção pré-registrado.

## SX-003 — agora Selecionado

- **Alvo:** Projeto Genoma Humano (1990–2003), domínio **Pesquisa Científica**
  (primeiro caso de **sucesso** no programa; primeiro caso neste domínio).
- **Status:** **SELECIONADO — GO-1 concluído. Aguarda revisão da coordenação
  (GO-2) para execução do pipeline congelado.**
- **Fontes já em staging pré-gate:** [candidates/genoma-humano/sources](./candidates/genoma-humano/sources/)
  (NHGRI, DOE, Nature, Science, Celera) — promoverão para `SX-003/sources/` na
  execução.
- **Próxima etapa:** GO-2 — pipeline congelado: fontes → narrativa → Atomic
  Facts → Reconstrução Cega → Alignment → Signals → EAR → relatório → revisão.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-09 | Seleção do Projeto Genoma Humano como alvo do SX-003, pela aplicação da direção pré-registrada (sucesso) + prioridades congeladas do SX-SELECTION. |

---
> **Regra do teste:** uma boa teoria não cria os fenômenos que explica; ela os
> reconhece onde eles já existem.
