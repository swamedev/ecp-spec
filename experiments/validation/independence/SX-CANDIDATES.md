# SX-CANDIDATES — Candidatos e Matriz de Elegibilidade

| Campo | Valor |
|---|---|
| **Tipo** | Aplicação do protocolo de seleção |
| **Status** | Preliminar (aguarda verificação de fontes — procedimento, etapa 4) |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe |
| **Governado por** | [SX-SELECTION](./SX-SELECTION.md) (congelado em 2026-08-03, antes desta lista) |
| **Referências** | [P-0007](../P-0007-INDEPENDENCE.md), [SHADOW-EXPERIMENTS](./SHADOW-EXPERIMENTS.md) |

## Nota de integridade

Esta lista foi produzida **somente após** o congelamento do protocolo
SX-SELECTION. Nenhum projeto foi escolhido antecipadamente; **o protocolo
decide** os elegíveis. As classificações SC-1..SC-6 são **preliminares**,
baseadas na documentação pública conhecida — a **verificação de fontes**
(acessibilidade real) é obrigatória antes da seleção final.

> **Re-auditoria obrigatória (P-0007.1 — Independence Framework):** o conjunto
> elegível será **re-auditado** antes da seleção final do SX-001 sob os três
> eixos congelados: (1) **EI** — SC-5 passa a contar **origens causais**, não
> fontes (ex.: NASA+Wikipédia+livro = uma origem no Apollo 13); (2) **DI** —
> domínios contados pela **taxonomia canônica** (Apollo 13/Challenger/Columbia/
> MOC = 1 domínio); (3) **OI** — contexto exógeno confirmado. Alguns "elegíveis"
> desta tabela podem **deixar de ser elegíveis** após a re-auditoria.

## Regra de elegibilidade (pré-registrada, inalterada)

Elegível ⇔ **SC-1, SC-3, SC-4 = Sim**; **nenhum** critério = Não; **≥ 4** = Sim.
Qualquer exclusão **EC-1..EC-7** → inelegível.

## Categoria A — Engenharia Física

| Projeto | Domínio | SC-1 | SC-2 | SC-3 | SC-4 | SC-5 | SC-6 | Elegível | Observação |
|---|---|---|---|---|---|---|---|---|---|
| Apollo 13 (1970) | Aeroespacial | Sim | Sim | Sim | Sim | Sim | Sim | **Sim** | Postmortem NASA + transcrições + múltiplas fontes; decisões sob incerteza documentadas. |
| Challenger STS-51-L (1986) | Aeroespacial | Sim | Sim | Sim | Sim | Sim | Sim | **Sim** | Rogers Commission Report; decisão de lançamento e pressões documentadas. |
| Tacoma Narrows (1940) | Civil (ponte) | Sim | Sim | Sim | Sim | Parcial | Sim | **Sim** | Filmes+relatórios técnicos; documentação rica porém narrativa mais concentrada. |
| I-35W Mississippi (2007) | Civil (ponte) | Sim | Sim | Sim | Sim | Sim | Sim | **Sim** | Relatório final NTSB + MnDOT + cobertura. |
| Deepwater Horizon (2010) | Industrial (offshore) | Sim | Sim | Sim | Sim | Sim | Sim | **Sim** | JIT + CSB + relatório BP; decisões de projeto do poço documentadas. |
| Hyatt Regency (1981) | Civil (estrutura) | Sim | Sim | Sim | Sim | Parcial | Sim | **Sim** | NBS report; decisão de mudança de projeto; fontes secundárias menos numerosas. |
| Chernobyl Unidade 4 (1986) | Industrial (nuclear) | Sim | Sim | Sim | Sim | Sim | Sim | **Sim** | INSAG-1/7 + relatório soviético; teste e decisões de operação. |
| Mars Climate Orbiter (1999) | Aeroespacial | Sim | Sim | Sim | Sim | Parcial | Sim | **Não** | **EC-1**: erro central é interface de software (unidades) — risco de contaminação no SX-001. |

## Categoria B — Saúde

| Projeto | Domínio | SC-1 | SC-2 | SC-3 | SC-4 | SC-5 | SC-6 | Elegível | Observação |
|---|---|---|---|---|---|---|---|---|---|
| Resposta ao Ebola, África Ocidental (2014–2016) | Saúde pública | Sim | Sim | Sim | Sim | Sim | Sim | **Sim** | WHO/MSF + análises acadêmicas; decisões de resposta documentadas. |
| Operation Warp Speed (2020–2021) | Saúde/vacinas | Sim | Sim | Sim | Sim | Sim | Sim | **Sim** | GAO + agências + mídia; decisões de risco/financiamento documentadas. |
| Hospital de Campanha Ibirapuera (SP, 2020) | Gestão hospitalar | Sim | Parcial | Parcial | Parcial | Parcial | Parcial | **Não** | Profundidade de fontes insuficiente; SC-3/SC-4 ≠ Sim. |
| Adoção de EHR hospitalar (ex.: Geisinger/Kaiser) | Gestão clínica | Sim | Parcial | Parcial | Parcial | Parcial | Parcial | **Não** | Estudos de caso com paywall parcial; sequência/decisões pouco rastreáveis. |

## Categoria C — Pequenos Negócios

| Projeto | Domínio | SC-1 | SC-2 | SC-3 | SC-4 | SC-5 | SC-6 | Elegível | Observação |
|---|---|---|---|---|---|---|---|---|---|
| Turnaround da Domino's (2009–2010) | Restaurante/cadeia | Sim | Sim | Sim | Sim | Parcial | Parcial | **Sim** | 4 Sim, sem Não; porém narrativa em parte corporativa (vigiar EC-4). |
| Postmortem público de abertura de restaurante | Restaurante | Sim | Parcial | Parcial | Parcial | Não | Parcial | **Não** | **EC-2/EC-4**: fonte única (blog); SC-5 = Não. |

## Categoria D — Logística

| Projeto | Domínio | SC-1 | SC-2 | SC-3 | SC-4 | SC-5 | SC-6 | Elegível | Observação |
|---|---|---|---|---|---|---|---|---|---|
| Bloqueio do Canal de Suez — Ever Given (2021) | Transporte | Sim | Sim | Sim | Sim | Sim | Sim | **Sim** | ECA/SCA + mídia + relatórios de salvado; decisões operacionais documentadas. |
| Fechamento aéreo — Eyjafjallajökull (2010) | Transporte | Sim | Sim | Sim | Sim | Sim | Sim | **Sim** | EU/EASA/ICAO + análises acadêmicas. |
| RFID na Walmart (2003–2005) | Cadeia de suprimentos | Sim | Sim | Sim | Sim | Parcial | Parcial | **Sim** | 4 Sim, sem Não; fontes múltiplas porém setor centrado. |
| Zara/Inditex — cadeia | Cadeia de suprimentos | Sim | Parcial | Parcial | Parcial | Parcial | Parcial | **Não** | Não é incidente com sequência definida; SC-3/SC-4 ≠ Sim. |

## Categoria E — Pesquisa Científica

| Projeto | Domínio | SC-1 | SC-2 | SC-3 | SC-4 | SC-5 | SC-6 | Elegível | Observação |
|---|---|---|---|---|---|---|---|---|---|
| Projeto Genoma Humano (1990–2003) | Big science | Sim | Sim | Sim | Sim | Sim | Sim | **Sim** | Relatórios públicos + decisões (público vs. Celera) documentadas. |
| Detecção de ondas gravitacionais (LIGO, 2015) | Física experimental | Sim | Sim | Parcial | Parcial | Sim | Parcial | **Não** | Trajetória longa; decisões pontuais pouco rastreáveis como decisões. |

## Resultado da aplicação do protocolo

**Elegíveis (14):** Apollo 13, Challenger, Tacoma Narrows, I-35W, Deepwater
Horizon, Hyatt Regency, Chernobyl, Ebola, Operation Warp Speed, Domino's, Suez
(Ever Given), Eyjafjallajökull, RFID Walmart, Genoma Humano.

**Inelegíveis (6):** Mars Climate Orbiter (EC-1 — software central), Ibirapuera
(SC-3/SC-4 Parcial), EHR hospitalar (SC-3/SC-4 Parcial), postmortem de
restaurante (EC-2/EC-4 — fonte única), Zara (SC-3/SC-4 Parcial), LIGO (SC-3/SC-4
Parcial).

## Ranking pré-registrado (para quando houver mais de um elegível)

Prioridade: (a) domínio mais distante do software → (b) postmortem público →
(c) maior multiplicidade de fontes.

1. **Challenger (1986)** — postmortem oficial, engenharia física, máxima
   multiplicidade (Comissão + NASA + mídia).
2. **Apollo 13 (1970)** — postmortem, decisões sob incerteza, fontes múltiplas.
3. **Chernobyl (1986)** — postmortem, engenharia industrial, múltiplas fontes.
4. **Deepwater Horizon (2010)** — postmortem, industrial offshore, múltiplas fontes.
5. **I-35W (2007)** — postmortem NTSB, civil.

## Próximo passo obrigatório (procedimento, etapa 4)

Verificar **acessibilidade real** das fontes públicas dos 14 elegíveis (links,
relatórios baixáveis, atas), antes de qualquer seleção final. Só depois a escolha
do SX-001 é registrada em `SHADOW-REPORT-001`.

> **Atualização (2026-08-03):** etapa 5 (verificação de fontes) **concluída** —
> todos os 9 SELECTABLE tiveram fontes primárias públicas acessíveis confirmadas.
> **SX-001 selecionado automaticamente pelo protocolo: Challenger STS-51-L**
> ([SHADOW-REPORT-001](./SHADOW-REPORT-001.md)).

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Primeira aplicação do SX-SELECTION (congelado antes desta lista). 20 candidatos, 14 elegíveis, 6 inelegíveis. Nenhuma escolha antecipada. |
| 1.1 | 2026-08-03 | Nota de **re-auditoria obrigatória** sob o P-0007.1 (EI por origens, DI por taxonomia canônica, OI exógena) antes da seleção final. Elegibilidade provisória. |
