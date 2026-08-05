# Inferência Científica — Camada de Sinais (SIGNAL)

| Campo | Valor |
|---|---|
| **Tipo** | Frente metodológica (Fase C) |
| **Status** | Aberta — aguarda dados hostis (H-001) e EXP-002+ |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe |
| **Referências** | [ECP-012](../../ECP/ECP-012.md), [adversarial](../adversarial/README.md), [LAW-METRICS](../laws/LAW-METRICS.md), [SIGNAL-SCHEMA](./SIGNAL-SCHEMA.yaml) |

## O problema que esta frente resolve

O pipeline clássico saltava de `OBS → PATTERN`. Mas há uma pergunta que ficava
sem resposta:

> **Quem disse que uma observação representa um padrão?**

Na ciência existe uma diferença enorme entre **observei algo** e **isto é
recorrente**. Sem essa distinção formal, corre-se o risco de fabricar **falsas
leis** a partir de coincidências.

## A camada que faltava

```
OBS        →  um fato. Sozinho não significa nada.
SIGNAL     →  a mesma afirmação observada em experimentos independentes. Ainda não é padrão.
PATTERN    →  diversos sinais independentes convergem.
LAW-H      →  o padrão sobrevive aos experimentos hostis.
```

## O que é um Signal

Um **SIGNAL (SIG)** formaliza uma **evidência recorrente**: a mesma afirmação
observada em experimentos **independentes** — e mensurável:

```yaml
S-001:
  afirmacao: Decision aparece após Evidence
  ocorrencias: [EXP-001, EXP-003, EXP-008, EXP-021]
  confianca: 0.82
  dominios: [Software, ERP, App, IA]
  contraexemplos: 1
  status: signal
```

Ainda **não** é um padrão: é a matéria-prima medida para a promoção.
Ver [SIGNAL-SCHEMA](./SIGNAL-SCHEMA.yaml).

## Critérios objetivos de promoção Signal → Pattern

Um Signal **promove a Pattern** somente se satisfaz **todos**:

| Critério | Limiar | Justificativa |
|---|---|---|
| **Independência** | ≥ 3 ocorrências em origens/autores **independentes** | anti-endogeneidade |
| **Cobertura de domínio** | ≥ 2 domínios diferentes | generalidade |
| **Confiança** | ≥ 0.70 | força da recorrência |
| **Contraexemplos** | ≤ 1 **explicado** | nenhum contraexemplo sem explicação |
| **Rastreabilidade** | todas as ocorrências reconstruíveis (corpus auditado) | RA-OBS-003 |

A promoção **Pattern → LAW-H** exige adicionalmente que o padrão **sobreviva
aos experimentos hostis** (Fase C) e ao **Programa de Diversidade Experimental**
([P-0006](../P-0006-LAW-DISCOVERY.md)) — sobrevivência em domínios
radicalmente diferentes, nunca apenas em múltiplos projetos do mesmo domínio.

## O funil científico da Fase C

```
Fase C
  ↓
H-001 Hostile Experiments
  ↓
Corpus atualizado
  ↓
Signals            ← camada formalizada aqui
  ↓
Patterns
  ↓
LAW-H
  ↓
Hostile novamente
  ↓
LAW-C
  ↓
External Validation
  ↓
LAW
  ↓
LAW Strength (LSI)
  ↓
Industrial Validation
  ↓
LAW-F
```

Cada estágio reduz o conjunto candidato: um **funil**, não uma lista.

## Do normativo ao científico

- **Normativo:** o ECP define como as coisas devem ser.
- **Científico:** a lei **prevê** o futuro (Predictive Index) e tem **força
  mensurável** (Law Strength Index) — ver [LAW-METRICS](../laws/LAW-METRICS.md).

A maior inovação do ECP pode ser exatamente este **método para descobrir leis
de engenharia** — aplicável a qualquer domínio (software, eletrônica, civil,
embarcados, IA).

## Regras desta frente

- **Congelamento mantido:** nenhuma RFC, AD, entidade, lei ou schema novo além
  dos artefatos desta frente.
- **Nada de Signal fabricado:** sem ≥ 2 ocorrências independentes, não há
  Signal. Com apenas EXP-001, ainda não há Signals reais — apenas o candidato
  **S-001** ilustrativo aguardando dados.
- **Contraexemplos nunca ocultos:** todo Signal registra explicitamente seus
  contraexemplos.
