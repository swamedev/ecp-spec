# ECP-AUDIT-001 — Protocolo de Auditoria do Corpus Experimental (P-0005A.2b)

| Campo | Valor |
|---|---|
| **Tipo** | Instrumento de Validação (protocolo) |
| **Status** | Congelado — v1.0 (gate oficial) |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe |
| **Governado por** | [ECP-012](../../ECP/ECP-012.md), [AD-007](../../04-governance/AD-007.md) |
| **Referências** | P-0005A, [OBS-SCHEMA v1.2](../corpus/OBS-SCHEMA.yaml), [CORPUS-EXPERIMENTAL-v1](../corpus/CORPUS-EXPERIMENTAL-v1.yaml), [AUDIT-REPORT-PILOT](./AUDIT-REPORT-PILOT.yaml), [AUDIT-SUMMARY-PILOT](./AUDIT-SUMMARY-PILOT.md) |
| **Instrumento associado** | [auditor.py](./auditor.py) |

## 1. Objetivo

Definir o método rigoroso para auditar o **Corpus Experimental** do Validation
Program, tornando a decisão "o corpus é válido?" **reproduzível** por
avaliadores independentes.

**Meta-objetivo (piloto):** antes de usar este protocolo como *gate oficial*,
demonstrar que ele próprio é capaz de decidir de forma **consistente e
objetiva**. O instrumento de validação precisa ser validado antes do artefato.

## 2. Escopo

- **Corpus:** qualquer `CORPUS-EXPERIMENTAL-vN.yaml` congelado.
- **Artefatos:** os JSON/artefatos brutos do experimento (fonte de evidência).
- **Observações:** todas as OBS do corpus no escopo da auditoria.
- **Fora de escopo:** padrões (P-0005A.3), hipóteses (P-0005A.4) e leis.

## 3. Meta-Validação (conceito metodológico — cadeia epistemológica)

> **H-009:** o Validation Program é uma **cadeia epistemológica**:

```
Conhecimento
      ▲
      │
Artefato
      ▲
      │
Instrumento (de Validação)
      ▲
      │
Ferramenta
      ▲
      │
Especificação
```

Cada camada **dá validade** à camada acima — não apenas executa. O fluxo de
execução desce; o **fluxo de validação sobe**. Antes de validar um artefato,
valida-se o instrumento que o valida. A cadeia percorrida até aqui:

1. **Especificação** — OBS-SCHEMA (validada na P-0005A.2a).
2. **Ferramenta** — minerador (produziu o corpus).
3. **Instrumento de Validação** — este protocolo (validado no piloto EXP-001).
4. **Artefato** — o corpus (auditado pelo protocolo congelado).
5. **Conhecimento** — padrões e leis derivadas.

**Limitação endógena (registrada):** a cadeia ainda é **interna** — o protocolo
gera experimentos, usa ferramentas e critérios definidos pelo próprio protocolo.
Isso é inevitável no início, mas é o risco central que a **Fase C (Adversarial
Validation)** existe para enfrentar: a validade precisa eventualmente vir de
fora ([adversarial/](../adversarial/README.md)).

## 4. Estrutura da auditoria

Cada ciclo de auditoria exige **reconstruções independentes** por **dois
avaliadores** (A e B), cegos entre si:

- **Reconstrução A — automática:** execução do `auditor.py` contra os artefatos
  do experimento. Determinística e auditável.
- **Reconstrução B — manual independente:** um avaliador humano reconstrói cada
  OBS a partir **apenas** dos artefatos (RA-OBS-003), sem consultar o corpus.

Cada avaliador registra, por OBS: reconstruível (sim/não), `kind` classificado,
e ressalvas. Os registros são comparados no relatório.

**Mínimo de auditores:** dois por ciclo, obrigatório (decisão do Arquiteto-Chefe).

## 5. Critérios de verificação

### 5.1 Admissibilidade (RA-OBS)

- **RA-OBS-001** — fato verificável, sem interpretação/julgamento/classificação.
- **RA-OBS-002** — evidência rastreadável (`evidence` + `trace`).
- **RA-OBS-003** — reconstruível apenas com os artefatos do experimento.
- **RA-OBS-004** — `confidence_source` presente.
- **RA-OBS-005** — informação essencial preservada.
- **RA-OBS-006** — `kind` presente no corpus congelado.
- **RA-OBS-007** — `observation_profile` presente.

### 5.2 Classificação ontológica (`kind`) — critérios objetivos

Uma OBS é **`structural`** somente se satisfaz **todos**:

1. **Necessidade relacional** — descreve relação **necessária** entre entidades,
   não um evento específico.
2. **Independência de implementação** — permanece válida independentemente da
   linguagem/framework/ferramenta.
3. **Impacto causal** — sua remoção **altera a compreensão da causalidade** do
   experimento.

Senão: **`operational`** (evento concreto, datado, amarrado a instâncias).

Uma OBS é **`derived`** quando é **derivável** de outras observações do mesmo
experimento (agregação/interpretação) — viola RA-OBS-001 e **não é admissível**
no corpus primário.

## 6. Equivalência tipificada

Para comparar reconstruções A e B entre si e contra o corpus:

- **Equivalência estrutural** — mesmo conjunto de entidades e relações.
- **Equivalência causal** — mesmo motivo para cada transição de estado.
- **Equivalência temporal** — mesma ordem causal (timestamps não necessários).

Duas OBS são equivalentes se são equivalentes em **todos** os três eixos.

## 7. Concordância entre avaliadores

Métrica da confiabilidade da classificação ontológica:

- **Concordância de classificação** — proporção de OBS em que avaliadores A e B
  atribuem o mesmo `kind` (operational/structural/derived).
- **Cohen's kappa** — corrige a concordância pelo acaso (recomendado para o gate).

**Limiares sugeridos** (parâmetro do piloto, a confirmar com dados):

| Métrica | Aceitável | Excelente |
|---|---|---|
| Concordância kind | ≥ 0.80 | ≥ 0.95 |
| Cohen's kappa | ≥ 0.60 | ≥ 0.80 |

Concordância **abaixo** do aceitável ⇒ os critérios da §5.2 devem ser refinados
antes de avançar para P-0005A.3.

## 8. Métricas do relatório

Todo relatório de auditoria deve conter:

- `reconstrucao`: total, reconstruíveis, falhas.
- `classificacao`: total, concordantes, concordância, discordantes.
- `equivalencia`: contagem por eixo (estrutural/causal/temporal).
- `observation_profile`: conferência da métrica do corpus.
- `avaliadores`: identificação e status (A, B, humano pendente).

## 9. Veredito

| Veredito | Condição |
|---|---|
| **PASS** | 100% das OBS reconstruíveis; RA-OBS-001..007 conformes; concordância ≥ limiar aceitável. |
| **PASS_COM_RESSALVAS** | ≥ 1 ressalva não crítica (ex.: OBS derivada presente, mas identificada). |
| **FAIL** | ≥ 1 OBS não reconstruível, RA-OBS violada, ou concordância abaixo do limiar. |

## 10. Critérios de saída (gate oficial)

O protocolo se torna *gate oficial* (v1.0) somente após:

1. Documento de protocolo congelado (este arquivo).
2. Piloto executado em EXP-001 com relatório registrado.
3. Ambiguidades identificadas no piloto **resolvidas** no protocolo.
4. Dois avaliadores humanos independentes treinados nos critérios.

## 11. Resultado do piloto (EXP-001)

Ver [AUDIT-SUMMARY-PILOT](./AUDIT-SUMMARY-PILOT.md). Resumo:

- Reconstrução automática: **16/16** (100%).
- Classificação independente vs corpus congelado: **16/16** (concordância 1.0).
- Achado do piloto: fragilidade do instrumento de reconstrução em chaves
  compostas (`G-0001-resolves-P-0001`) — corrigida no `auditor.py` antes do
  relatório final.
- Limitação registrada: avaliador humano independente **pendente** — a
  concordância inter-humana (kappa) será medida na auditoria oficial.

**O piloto certifica o protocolo, não o corpus.**

## 12. Ajustes aplicados após o piloto

1. `auditor.py`: reconstrução de arestas por **chave composta exata**
   (`source-label-target`), não por parsing frágil de IDs com hífen.
2. Protocolo: explicitado que **OBS-0016 (caso canônico de não-observação)**
   entra no piloto como verificação da capacidade do instrumento de detectar
   violação de RA-OBS-001.
3. Protocolo: limiares de concordância declarados como parâmetro **ajustável**
   até a medição com avaliadores humanos.

## 13. Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Congelado após piloto EXP-001 (16/16 reconstrução, concordância 1.0). Ajustes §12 incorporados. Torna-se **gate oficial** da P-0005A.2b. |
| 0.1 | 2026-08-03 | Rascunho inicial (Fase 1) — especificação do protocolo antes da execução do piloto. |
