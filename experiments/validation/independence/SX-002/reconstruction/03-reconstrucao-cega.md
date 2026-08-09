# SX-002 / reconstruction — Etapa 3: Reconstrução Cega

| Campo | Valor |
|---|---|
| **Experimento** | EXP-SX002 |
| **Etapa** | 3 — Reconstrução Cega |
| **Entrada** | **Somente** [02-atomic-facts.md](./02-atomic-facts.md) + Kernel ECP-000..ECP-009 |
| **Proibido** | Consultar a [narrativa original](../narrative/01-narrativa-original.md) durante a reconstrução |
| **Data** | 2026-08-04 |

> **Protocolo de reconstrução:** (1) ler os Atomic Facts; (2) para cada fato,
> perguntar *"que papel esse fato desempenha na estrutura do evento?"*; (3)
> reconhecer uma entidade **somente quando** existir suporte factual direto
> (`AF-###`); (4) marcar como **inferida** qualquer categoria que exija
> interpretação sem suporte direto; (5) registrar **ausências** (entidades que o
> Kernel prediz e que não aparecem).

---

## 0. Declaração de cegueira

Esta reconstrução foi produzida **antes** de reler a Narrativa Original. As
entidades abaixo foram reconhecidas a partir dos **51 Atomic Facts** e do Kernel.
Onde o rótulo ECP não era claramente suportado pelos fatos, foi marcado como
**inferido** — e **não conta** como emergência espontânea.

> **Limitação de execução (registrada):** reconstrução e narrativa foram
> produzidas pelo mesmo executor, sob o pipeline congelado. A separação ideal
> (Pessoa A reconstrói, Pessoa B compara) permanece não aplicada nesta sessão.
> Para mitigar, a reconstrução cita **apenas** `AF-###`, nunca a narrativa. A
> limitação é registrada em [METHODOLOGICAL-DEBT.md](../../METHODOLOGICAL-DEBT.md).

## 1. Reconhecimento de entidades

### 1.1 Problem (Problema) — NÃO EMERGE diretamente como causa raiz assumida

O Kernel começa por Problem (causa raiz). Os fatos descrevem **o que aconteceu**
(AF-001..043) e **o que as avaliações disseram** (AF-044..051). A causa raiz do
evento ("por que uma epidemia dessa escala aconteceu?") **não é declarada em
nenhum fato como causa oficial única assumida pelos participantes**; AF-044 a
AF-048 listam fatores apontados por terceiros — como fatos sobre **o que as
avaliações concluíram**, não como uma causa-raiz nomeada e assumida pelos
agentes da resposta.

Leitura: o Problem **não emerge como entidade assumida pelos participantes**, e
sim como **conclusão pós-hoc de terceiros** (avaliações). Este é um dado: a
emergência do Problem depende de os agentes terem definido o problema antes de
agir. Nos fatos, ninguém define o problema formalmente antes da resposta.

### 1.2 Goal (Objetivo) — EMERGENTE

| Suporte | Fato |
|---|---|
| AF-015 | MSF montou centros de tratamento. |
| AF-022 | UNMEER tinha como objetivo coordenar a resposta e apoiar os países. |
| AF-036..AF-039 | Declarações de "livre do vírus" — estados observáveis finais. |

O objetivo da resposta **emerge**: interromper a transmissão e encerrar a
epidemia, com estados finais observáveis (países declarados livres). Não exigiu
interpretação.

### 1.3 Knowledge (Conhecimento) — EMERGENTE

| Suporte | Fato |
|---|---|
| AF-007 | Modo de transmissão conhecido (fluidos) — conhecimento epidemiológico. |
| AF-012 | Conhecimento de epidemias anteriores (áreas remotas da África Central, menores). |
| AF-006 | Agente identificado (Zaire ebolavirus) — base de conhecimento. |
| AF-004 | **O agente causador não foi identificado inicialmente — lacuna inicial.** |

O conhecimento emerge em duas partes: o que **se sabia** (AF-007, AF-012,
AF-006) e a **lacuna** inicial (AF-004). O Kernel prevê classificar o que se
sabe e o que não se sabe (ECP-006) — aqui a lacuna é exatamente o ponto de
partida.

### 1.4 Lacuna de escala (aprendizado tardio) — PARCIALMENTE INFERIDA

A lacuna mais estrutural não é a identidade do vírus (resolvida em AF-006), mas
a **projeção de escala**: AF-016 (MSF, "fora de controle") e AF-017/AF-018
(resposta insuficiente e lenta) mostram que a **provável magnitude da epidemia
não foi projetada nem dominada a tempo**. Os fatos, porém, registram apenas o
alerta da MSF — não declaram a lacuna quanto à magnitude. Leitura: "não se
sabia a magnitude (houve subestimação)" é **inferida** do comportamento de
resposta lenta (AF-018/AF-019), **não** declarada diretamente. → Não conta como
emergência plena.

### 1.5 Assumption (Suposição) — EMERGENTE (uma, forte, inferida)

| Suporte | Fato |
|---|---|
| AF-018 | A resposta internacional foi inicialmente lenta. |
| AF-019 | A mobilização foi gradual, ao longo de meses. |
| AF-046 | Havia falta de preparação para epidemia de grande escala. |

Suposição emergente: **A-1** — *"a epidemia podia ser contida (ou reduzida em
escala) sem uma expansão imediata e massiva da resposta"* — implícita no ritmo
lento (AF-018/AF-019) e na falta de preparação (AF-046). Tratada como
verdadeira sem evidência plena durante meses, até a magnitude (AF-030/AF-031)
transformar a necessidade.

> **Nota:** os fatos não registram a suposição como frase escrita; a reconstrução
> vê o **comportamento** (lentidão, despreparo) e infere a crença subjacente.
> Marcar: suposição **inferida**, não totalmente emergente.

### 1.6 Evidence (Evidência) — EMERGENTE

| Suporte | Fato |
|---|---|
| AF-005 | Notificação oficial da Guiné à OMS (evidência formal de observação). |
| AF-006 | Identificação do agente (evidência laboratorial). |
| AF-030..AF-031 | Contagem do pico (evidência de vigilância). |
| AF-040..AF-043 | Totais e óbitos (evidência agregada final). |
| AF-025 / AF-027 / AF-029 | Resultados de contenção (Nigéria/Senegal/Mali) (evidência de resultado). |

A evidência emerge em duas formas: **evidência de detecção** (AF-005, AF-006,
AF-030) e **evidência de resultado** (AF-036..039, AF-040..043, AF-025/027/029).
Não precisou interpretar — os fatos já eram observações.

### 1.7 Decision (Decisão) — EMERGENTE (cadeia de 6)

| Suporte | Fato |
|---|---|
| AF-005 | Notificar o surto (decisão de escalonamento/comunicação). |
| AF-020 | Declarar PHEIC (decisão formal de máxima alerta). |
| AF-021..AF-022 | Criar a UNMEER (decisão de coordenação). |
| AF-024 | Conter na Nigéria via rastreamento e isolamento (decisão local). |
| AF-036..AF-038 | Declarar países livres (decisões de encerramento por país). |
| AF-039 | Declarar o fim da emergência (decisão global de encerramento). |

A cadeia de decisões emerge: detectar → notificar → alertar (MSF) → declarar
emergência → criar missão → conter → encerrar.

### 1.8 Risk (Risco) — INFERIDO (só matéria-prima, sem artefato formal)

O Kernel prevê risco = impacto × probabilidade (ECP-008). Os fatos contêm
matéria-prima: mortalidade alta (AF-032/AF-033 até 40–70%), dispersão multi-país
(AF-011/AF-013), dano a profissionais de saúde (AF-009/AF-010/AF-042). Mas
**nenhum fato** registra um cálculo de risco explícito e formal para a decisão de
reação. → O risco **não emerge como artefato**; são **matéria-prima implícita**
do alarme. Marcado como quase-ausência (§3).

## 2. A cadeia reconstruída

Reunindo apenas o que emergiu dos fatos:

```
Lacuna de conhecimento (AF-004 — agente não identificado inicialmente)
   ↓
Evidence de detecção (AF-005, AF-006 — notificação, identificação)
   ↓
Goal (AF-022 — coordenação da resposta; AF-036..039 — estados finais)
   ↓  (resposta lenta — AF-018/AF-019, sob suposição implícita A-1)
Decision (AF-020 — PHEIC; AF-021 — UNMEER; AF-024 — contenção local)
   ↓   (espaçadas no tempo; pico em AF-030 ocorre antes de consolidar AF-021)
Evidence de evolução + Outcome (AF-030..035 — pico e queda; AF-025/027/029)
   ↓
Validation (AF-036..039 — declarações de livre/estado final)
   ↓
Resultados agregados (AF-040..043 — totais e óbitos)
   ↓
Learning (AF-044..051 — avaliações, reformas, avanços)
```

**Observação central da reconstrução:** a cadeia começa numa **lacuna de
conhecimento** (AF-004) e responde **tarde** (AF-016..AF-019): o pico de casos
(AF-030/AF-031) é atingido **antes** de a coordenação formal da resposta se
consolidar (AF-021..AF-022 define a missão, mas os picos ainda estavam em
atividade), e o **declínio só ocorre após a expansão** da resposta (AF-034/AF-035). Sem consultar
o relatório oficial, a reconstrução detecta uma **defasagem (lag)** entre o
alarme (AF-016, março/junho de 2014), a declaração formal (AF-020, agosto) e a
consolidação efetiva de capacidade — exatamente a "resposta internacional tardia"
que as avaliações registram (AF-044).

## 3. Ausências (negative evidence)

| Entidade | Status nos fatos | Leitura |
|---|---|---|
| **Problem definido (formal, inicial)** | Não aparece | Nenhum fato mostra uma definição formal do problema antes da resposta; as causas só aparecem como avaliação posterior (AF-044..048). |
| **Cálculo de risco formal** | Não aparece | Impacto alto (AF-032/033) e dispersão (AF-011/013) existem como dados; risco como entidade de decisão não foi produzido. |
| **Projeção de escala (capacidade)** | Não aparece | A magnitude foi subestimada/ignorada até virar pico (AF-016..031). Nenhum fato registra projeção prévia. |
| **Metas mensuráveis globais** | Só post-hoc | Estados finais (AF-036..039) são de resultado; não há metas de planejamento pré-declaradas. |
| **Registro do processo decisório** | Parcial | Decisões existem (AF-020/AF-021), mas o motivo detalhado da demora não está incluído como documento dos decisores — só como avaliação (AF-044). |

Estas ausências são **dados**: o Kernel prediz que uma resposta de emergência
teria (1) quem define o problema, (2) cálculo de risco, (3) projeção de
capacidade e (4) metas claras; nos fatos, esses artefatos **prévios** não
aparecem. A ausência é coerente com a "lentidão" registrada (AF-018).

## 4. O que a reconstrução NÃO conseguiu (limites)

- **Não reconstruiu a biologia/medicina** (por que o vírus é tão letal, nem o
  mecanismo clínico detalhado) — exigiria conhecimento biomédico; os AFs só
  contêm (AF-006, AF-032/033).
- **Não reconstruiu a motivação dos agentes** (por que a resposta foi lenta:
  fatores burocráticos, sistêmicos, diplomáticos) — o motivo não está nos fatos.
- **Não reproduziu a série temporal completa** dos picos por país e por mês — os
  AFs são uma sequência indexada por datas-chave, não um painel contínuo.

## 5. Resumo da Etapa 3

| Entidade | Emergência | Suporte |
|---|---|---|
| Lacuna inicial (agente não identificado) | **Emergente** | AF-004 |
| Goal (coordenação + estados finais) | **Emergente** | AF-022, AF-036..039 (estados finais), AF-030..035 (meta implícita) |
| Knowledge (transmissão, agente) | **Emergente** | AF-007, AF-012, AF-006 |
| Evidence (detecção e resultado) | **Emergente** | AF-005, AF-006, AF-030..031, AF-040..041 |
| Decision (cadeia) | **Emergente** | AF-005, AF-020, AF-021, AF-024, AF-036..039 |
| Assumption (A-1: escala menor) | **Inferida** (comportamento, sem declaração) | AF-018, AF-019, AF-046 |
| Lacuna de escala | **Inferida** | AF-016, AF-017, AF-018 |
| Risk | Não emerge (só material) | AF-011, AF-013, AF-032..033 |
| Problem definido (inicial) | Não emerge | (só nas avaliações: AF-044..048) |
| Defasagem alerta→coordenação (lag) | **Emerge como estrutura** | §2 |

> **Divergência em relação ao SX-001 (a ser verificada na Etapa 4):** no
> Challenger, a falha esteve no elo **Evidence→Decision** (decisão lançada sem
> evidência). Aqui o padrão é outro: as **evidências e os alertas existiam**
> (AF-005, AF-016, AF-017) **antes** da decisão, mas a **coordenação** veio
> **tarde demais** — a decisão formal (AF-020/021) só se consolidou após o pico
> (AF-030). A reconstrução captura uma **defasagem (lag)**, não ausência de
> evidência.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-04 | Reconstrução cega a partir dos 51 Atomic Facts + Kernel. Emergência: Lacuna/Goal/ Knowledge/Evidence/Decision. Ausências: Problem formal, Risk calculado, projeção de capacidade. Variação do padrão do Challenger: defasagem (lag) em vez de ausência de evidência. |

## Correção de rascunho

- Texto formatado para sempre citar `AF-###` (nunca a narrativa). A única fonte
  externa é o Kernel, conforme o pipeline.
- Os itens "Risk" e "Problem" foram marcados como **não-emergentes** com
  justificativa factual — não foram inventados. Ver §1.7/§1.8 e §3.