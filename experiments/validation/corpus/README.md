# Corpus Experimental — Foundation

## Objetivo

Estabelece a **infraestrutura inicial** para o **Validation Program** do ECP.

Permite, futuramente, a descoberta sistemática de **padrões recorrentes**, **hipóteses (LAW-H)** e, por fim, **leis universais (ECP-LAWS)** através de **observações concretas e verificáveis** extraídas dos experimentos já realizados.

## Papel no Validation Program

```
Experimento
  ↓
Observação
  ↓
Corpus
  ↓
Padrão
  ↓
Hipótese (LAW-H)
  ↓
Lei (ECP-LAW)
```

- **Experimento** → gera dados brutos (artefatos)
- **Observação** → registra **exclusivamente fatos verificáveis**, sem interpretações
- **Corpus** → coleção estruturada e reproduzível de observações, **sem hipóteses ainda**
- **Padrão** → Agrupa observações equivalentes (ainda em fase de mineração)
- **Hipótese (LAW-H)** → “Se X, então Y” em forma formal, **em aberto**
- **Lei (ECP-LAW)** → lei validada, pronta para incorporação ao núcleo do ECP

## Arquitetura do Validation Program

```
validation/
├── P-0006-LAW-DISCOVERY.md  # Programa de descoberta de leis (Regra 1, genealogia, diversidade)
├── corpus/          # Fundamentos para descoberta de padrões (OBS + schema)
│   ├── OBS-SCHEMA.yaml    # Definição formal de uma Observation
│   ├── CORPUS-EXPERIMENTAL-v0.yaml  # Metadados da fundação (Sem observações)
│   ├── CORPUS-EXPERIMENTAL-v1.yaml  # Corpus congelado (P-0005A.2a)
│   └── README.md          # Este documento
│
├── audit/           # Instrumento de validação do corpus (P-0005A.2b)
│   ├── ECP-AUDIT-001.md   # Protocolo de auditoria (v1.0, gate oficial)
│   ├── auditor.py         # Reconstrução + classificação independente
│   ├── AUDIT-REPORT-PILOT.yaml  # Relatório do piloto EXP-001
│   └── AUDIT-SUMMARY-PILOT.md   # Resumo do piloto EXP-001
│
├── adversarial/     # Fase C — tentativa deliberada de quebrar o ECP
│   ├── README.md          # Fase C (congelamento, endogeneidade, RI, eras, funil)
│   ├── HOSTILE-EXPERIMENTS.md  # Ataques H-001..H-006
│   └── CANONICAL-FAILURES.md   # Falhas canônicas (CF-001: OBS-0016)
│
├── signals/         # Inferência Científica — camada OBS → SIGNAL → PATTERN
│   ├── README.md          # Frente Inferência Científica (promoção Signal→Pattern)
│   └── SIGNAL-SCHEMA.yaml # Definição formal de um Signal
│
├── patterns/         # Lista de padrões detectados (P-0005A.3)
├── laws/             # Leis e candidatos (P-0005A.4+); LAW-METRICS (LSI/PI); LAW-BACKLOG (perguntas científicas)
└── reports/          # Relatórios gerados, guias de referência
```

## Meta-Validação (H-009 — cadeia epistemológica)

```
Conhecimento
      ▲
      │
Artefato
      ▲
      │
Instrumento
      ▲
      │
Ferramenta
      ▲
      │
Especificação
```

Cada camada **dá validade** à camada acima — não apenas executa. O fluxo de
execução desce; o **fluxo de validação sobe**. Antes de validar um artefato,
valida-se o instrumento que o valida. Ordem já percorrida: schema (P-0005A.2a) →
minerador → protocolo de auditoria (piloto) → corpus (auditoria oficial) →
conhecimento.

## Processos principais do Validation Program

1. **Experimento** → Gera artefatos (json, código-fonte, logs, etc.)
2. **Mineração** → Extrai **observações** concretas de artefatos de experimentos (P-0005A.2)
3. **Revisão Ontológica** → Classifica cada observação como fato operacional ou estrutural (P-0005A.2a)
4. **Auditoria** → Verificação externa de qualidade do corpus (P-0005A.2b)
5. **Inferência Científica** → Formaliza **SIGNALS** (evidência recorrente) → **PATTERNS** (Inferência Científica)
6. **Catalogação** → Agrega padrões (P-0005A.3)
7. **Formulação de hipóteses** → Formula **hipóteses (LAW-H)** (P-0005A.4)
8. **Validação** → Testa hipóteses, separa candidatos e **leis validadas** (P-0005A.5+)
9. **Documentação** → Publica **ECP-LAWS** e **ECP-012** para uso geral (P-0005)

## Regras de admissibilidade (RA-OBS)

1. **RA-OBS-001** — Uma **Observation** deve descrever apenas **fatos verificáveis** ocorridos durante um experimento, sem interpretações, hipóteses, inferências, julgamentos, recomendações ou classificação.

2. **RA-OBS-002** — Todo OBS deve possuir pelo menos **uma evidência rastreadável** (`evidence` + `trace`).

3. **RA-OBS-003** — Todo OBS deve poder ser **reconstruído** por outro avaliador utilizando **APENAS os artefatos originais do experimento**.

4. **RA-OBS-006** — Todo corpus **congelado** deve classificar cada OBS com `kind` (`operational` | `structural` | `derived`). Observações `derived` não são admissíveis no corpus primário.

5. **RA-OBS-007** — Todo corpus **congelado** deve declarar a métrica `observation_profile` (proporção operational/structural/derived) para observação de tendências entre experimentos.

## Dois níveis de observação (P-0005A.2a — etapa permanente)

A revisão ontológica — agora **fase obrigatória** do Validation Program — mostrou que as observações se distribuem em **dois níveis**:

- **Observation Operacional** — fatos/eventos da execução: instanciação de entidade, seleção, snapshot, persistência. Singulares, datados, amarrados a instâncias.
- **Observation Estrutural** — relações entre entidades que compõem a ontologia: dependência, resolução, serviço, uso de evidência. São os candidatos mais próximos de futuras leis (LAW-H).

Observações **derivadas** (agregações/interpretações) violam RA-OBS-001 e não pertencem ao corpus primário.

**Classificação por critérios objetivos** (não pela opinião do autor): um OBS é `structural` somente se satisfaz **todos** — (1) descreve relação **necessária** entre entidades; (2) permanece válida **independentemente da implementação**; (3) sua remoção **altera a compreensão da causalidade** do experimento.

**Caso canônico de não-observação:** `OBS-0016` ("Modelo estrutural validado") permanece como exemplo permanente de violação de RA-OBS-001 — *isto parece uma observação, mas não é.*

Ver [P-0005A.2a — Revisão Ontológica do Corpus](../reports/REVISAO-ONTOLOGICA-P0005A-2a.md).

## Fluxo do Pipeline

```
Experimentos (EXP-001...EXP-006) → Artefatos (JSON, .py, logs, ...)
                                     ↓
                                 Minerador (P-0005A.2) → Corpus Experimental
                                     ↓
                                 Revisão Ontológica (P-0005A.2a) → Corpus v1 (congelado)
                                     ↓
                                 Auditoria (P-0005A.2b) — ECP-AUDIT-001 (gate oficial)
                                     ↓
                                 Signals (Inferência Científica)
                                     ↓
                                 Padrões (P-0005A.3)
                                     ↓
                                 Hipóteses (LAW-H) (P-0005A.4)
                                     ↓
                                 Lei Candidata (LAW-C)
                                     ↓
                                 Lei Validada (LAW-V)
                                     ↓
                                 Lei Fundamental (LAW-F)
                                     ↓
                                 ECP-LAWS (Documentação central das leis)
                                     ↓
                                 ECP-012 (Protocolo de descoberta de leis)
                                     ↓
                                 Ontologia (Entidades) (P-0005)
```

## Organização de componentes

### corpus/
Contém os **arquivos fundacionais** para o pipeline de descoberta de leis.

**OBS-SCHEMA.yaml** — Definição formal de uma Observation (v1.1 inclui `kind`).

**CORPUS-EXPERIMENTAL-v0.yaml** — **Metadados do corpus** inicial (sem observações preenchidas ainda).

**CORPUS-EXPERIMENTAL-v1.yaml** — **Corpus congelado** (P-0005A.2a) com as 16 OBS classificadas por `kind` e essencialidade.

### observations/
*Reservado para versão futura*: catalogação completa de observações (quando minerador estiver implementado).

### patterns/ / laws/ / reports/
*Future components*:
- **patterns/**: catalogação de padrões detectados.
- **laws/**: hipóteses de leis e candidaturas a leis validadas.
- **reports/**: guias de referência e documentação de resultados (contém [P-0005A.2a](../reports/REVISAO-ONTOLOGICA-P0005A-2a.md)).

## Notas de implementação

- **Sem LLM**: Todo o processo deve ser independente de modelos de IA/LLM — conduzido por regras, auditável e automatizado.
- **Reproducível**: Cada observação deve conter referência direta a um trecho exato do artefato original.
- **Progressivo**: Todo o pipeline avança **grau a grau**, sem saltos: experimento → observação → padrão → hipótese → lei.
- **Separação de preocupações**:
  - **Runtime** → Gera dados (artefatos)
  - **Validation Program** → Processa dados → Conhecimento (observações, padrões, leis)

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.3 | 2026-08-03 | Frente **Inferência Científica**: camada `OBS → SIGNAL → PATTERN → LAW-H` (camada Signals); critérios objetivos de promoção Signal→Pattern; **LSI** e **Predictive Index** ([LAW-METRICS](../laws/LAW-METRICS.md)); funil científico da Fase C. |
| 1.2 | 2026-08-03 | Auditoria P-0005A.2b: protocolo **ECP-AUDIT-001 v1.0** (gate oficial) + piloto EXP-001 (16/16 reconstrução, concordância 1.0); conceito de **Meta-Validação (H-009)**; RA-OBS-007 e `observation_profile`. |
| 1.1 | 2026-08-03 | Etapa **P-0005A.2a — Revisão Ontológica do Corpus** antes da auditoria; descoberta dos dois níveis de observação (operacional × estrutural); campo `kind` e RA-OBS-006; Corpus v1 congelado; auditoria renomeada para P-0005A.2b. |
| 1.0 | 2026-08-02 | Versão inicial (Aprovado). Estabelece a fundação do pipeline de descoberta de leis para o ECP — arquivo README principal para o diretório `validation/corpus`. |

### Mapa de Revisão

**P-0005A.2a — Revisão Ontológica do Corpus** (implementado em 2026-08-03)

1. **Classificação por OBS** (16 OBS, uma a uma)
   - fato × interpretação
   - operacional × estrutural
   - redundante / derivável / essencial
2. **Descoberta**: existem dois níveis de observação (operacional × estrutural).
3. **Novo campo `kind`** (`operational` | `structural` | `derived`) e **RA-OBS-006**.
4. **Corpus v1 congelado** → [`CORPUS-EXPERIMENTAL-v1.yaml`](./CORPUS-EXPERIMENTAL-v1.yaml).

**P-0005A.2b — Auditoria do Corpus Experimental** (protocolo congelado; auditoria oficial pendente de avaliadores humanos)

1. **Protocolo** — [ECP-AUDIT-001](../audit/ECP-AUDIT-001.md) **v1.0 (gate oficial)**; instrumento [`auditor.py`](../audit/auditor.py).
2. **Piloto EXP-001 executado** — reconstrução 16/16; classificação independente 16/16 (concordância 1.0); ver [AUDIT-REPORT-PILOT](../audit/AUDIT-REPORT-PILOT.yaml) e [AUDIT-SUMMARY-PILOT](../audit/AUDIT-SUMMARY-PILOT.md).
3. **Meta-objetivo do piloto** — certificar o **protocolo**, não o corpus (Meta-Validação).
4. **Equivalência tipificada**
   - Equivalência estrutural
   - Equivalência causal
   - Equivalência temporal
5. **Concordância entre avaliadores** (novo objetivo, decisão do Arquiteto-Chefe)
   - Dois avaliadores independentes classificam as mesmas OBS (operational/structural/derived)
   - Concordância alta → classificação fortalecida; baixa → refinar critérios antes de P-0005A.3
   - Cohen's kappa na auditoria oficial (humano × humano) — pendente
6. **Método da auditoria**
   - Reconstruções A e B independentes
   - Pass/PASS_COM_RESSALVAS/Fail
   - Requisito de mínimo dois auditores
   - Duas auditorias obrigatórias por ciclo
7. **Obrigatório para next**
   - **RA-OBS-005** — essencialidade
   - **RA-OBS-004** — `confidence_source`
   - **Equivalência tipificada**

### Referências cruzadas relevantes

- **Pipeline da auditoria:** > **Regras de admissibilidade** → *RA-OBS-004* → *RA-OBS-005* → *Equivalência tipificada* → *Cobertura* → *Pass/Fail*

- **Ordem cronológica:** > **Fundação do Corpus** → **Revisão Ontológica (2a)** → **Auditoria (2b)** → **Métricas** → **Padrões** → **Hipóteses** → **Leis**

- **Dependência hierárquica:** > **Mineração** → **Corpus** → **Revisão Ontológica (2a)** → **Auditoria (2b)** → **Padrões** → **Hipóteses** → **Leis**

- **Alteração funcional:** O pipeline muda de *extrair e agregar* → *classificar ontologicamente* → *auditar e consumir* → *interpretar e formalizar*

- **Mecanismo de validação:** O pipeline depende de **reconstrução interna** (método estrito para garantir consistência)

- **Disciplina:** Cada etapa só avança **depois** de rigorosa verificação externa; **sem saltos**; **sem atalhos**

- **Abstração:** A arquitetura evolui de **observações concretas** → **padrões** → **hipóteses** → **leis** — um aumento gradual de abstração

- **Negociação:** Cada etapa deve **preservar informações essenciais** da anterior (RA-OBS-005)

- **Auditoria:** A **primeira** grande etapa de verificação externa é *Auditoria (P-0005A.2b)* — estabelecendo disciplinas de verificação de qualidade, precedida pela *Revisão Ontológica (P-0005A.2a)*

- **Evolução:** Mude de **repo** → **commits** → **branches** → **merged** → **master**

- **Processo:** Transforma um programa linear em um pipeline iterativo baseado em validações

- **Aspecto:** A **primeira** abordagem do pipeline que trata todas as etapas **como processos baseados em evidências**
