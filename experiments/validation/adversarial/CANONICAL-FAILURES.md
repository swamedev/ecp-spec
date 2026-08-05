# CANONICAL-FAILURES — Falhas Canônicas do Validation Program

| Campo | Valor |
|---|---|
| **Tipo** | Registro oficial de anti-padrões |
| **Status** | Ativo |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe |
| **Referências** | [OBS-SCHEMA v1.2](../corpus/OBS-SCHEMA.yaml), [CORPUS-EXPERIMENTAL-v1](../corpus/CORPUS-EXPERIMENTAL-v1.yaml), [ECP-AUDIT-001](../audit/ECP-AUDIT-001.md) |

## Propósito

Registrar **exemplos permanentes** de *"isto parece uma observação, mas não é"*.

Uma falha canônica não é removida do projeto: é preservada porque demonstra
**exatamente onde um ser humano tende a errar**. É ouro para treinamento de
novos avaliadores, calibração de auditorias e referência negativa nos
experimentos hostis (Fase C).

## Formato

Cada caso canônico segue o padrão:

```
CF-NNN — Nome
  Origem:  (OBS, artefato, documento)
  Aparência: o que parece ser
  Realidade: o que realmente é
  Regra violada: RA-OBS / critério
  Padrão humano de erro: por que um humano erra aqui
  Reescrita correta: como virar fato primário (se aplicável)
  Uso: onde serve de referência
```

---

## CF-001 — "Modelo estrutural validado" (OBS-0016)

- **Origem:** `OBS-0016` do [CORPUS-EXPERIMENTAL-v1](../corpus/CORPUS-EXPERIMENTAL-v1.yaml)
  (`exp001_model.json:model_validation`).
- **Aparência:** observação legítima — um evento registrado pelo runtime com
  evidência e trace ("Modelo estrutural validado: 32 cognitivas, 13
  operacionais").
- **Realidade:** uma **agregação + julgamento**. Contém classificação (nós
  "cognitivas" × "operacionais") e veredito ("validado"). É integralmente
  **derivável** do mesmo grafo que originou as demais observações.
- **Regra violada:** **RA-OBS-001** (fatos verificáveis sem interpretação,
  julgamento ou classificação).
- **Padrão humano de erro:** o texto *parece* factual porque descreve algo que
  "aconteceu" e tem evidência. O erro é confundir **registro do runtime** com
  **fato ontológico**: o runtime registrou um veredito; um veredito é
  interpretação, não fato primário.
- **Reescrita correta:**
  `event: "Model contém 32 nós no domínio cognitivo e 13 no operacional"` —
  separa a contagem (fato) do julgamento ("validado").
- **Uso:** caso de referência em auditorias (ECP-AUDIT-001 §11), treinamento de
  avaliadores, e como alvo no experimento hostil **H-004** (evidência falsa).

---

## Template para novos casos

```
CF-NNN — Nome
  Origem:
  Aparência:
  Realidade:
  Regra violada:
  Padrão humano de erro:
  Reescrita correta:
  Uso:
```

Novos casos são adicionados quando um experimento hostil (Fase C) ou uma
auditoria identifica uma falha de classificação recorrente.
