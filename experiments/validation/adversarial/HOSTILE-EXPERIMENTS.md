# HOSTILE-EXPERIMENTS — Experimentos Hostis (Fase C)

| Campo | Valor |
|---|---|
| **Tipo** | Especificações de ataques ao protocolo |
| **Status** | Ativo |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe |
| **Referências** | [README da Fase C](./README.md), [ECP-AUDIT-001](../audit/ECP-AUDIT-001.md), [CANONICAL-FAILURES](./CANONICAL-FAILURES.md) |

## Objetivo

Projetos **construídos para quebrar** o ECP. Cada experimento hostil escolhe um
vetor de ataque e mede o **Resistance Index (RI)**.

```
RI = critérios do protocolo que permaneceram válidos / critérios testados no ataque
```

RI **mínimo** e RI **acumulado** são as métricas oficiais da Fase C.

## Regras comuns

- O projeto adversarial é preparado **fora do controle do protocolo**, quando
  possível (outro autor, outro domínio, outro ambiente).
- O protocolo completo roda contra ele: **mineração → revisão ontológica →
  auditoria** (ECP-AUDIT-001).
- Cada ataque produz um `HOSTILE-REPORT-###.yaml` com o RI medido.
- Falhas humanas encontradas entram no [CANONICAL-FAILURES](./CANONICAL-FAILURES.md).
- Vereditos possíveis por critério: **resistiu** (RI=1) ou **quebrou** (RI=0).

---

## H-001 — Projeto mínimo (sobrecarga)

- **Vetor de ataque:** peso/dimensionalidade. O ECP é pesado demais para o
  trivial?
- **Cenário:** projeto extremamente pequeno — **uma única página HTML**.
- **Pergunta hostil:** o protocolo permanece aplicável sem custo
  desproporcional, ou o overhead mata a utilidade?
- **Critérios testados:** aplicabilidade total do pipeline; relação
  esforço/valor; RA-OBS aplicáveis a poucos artefatos.

## H-002 — Projeto artístico (objetivo indefinido)

- **Vetor de ataque:** intencionalidade. Sem objetivo totalmente definido, o
  ciclo cognitivo ainda vale?
- **Cenário:** projeto artístico/exploratório, intenção aberta e iterativa.
- **Pergunta hostil:** Goal/Problem existem sem objetivo fechado? O protocolo
  força uma rigidez que o processo artístico não tem?
- **Critérios testados:** modelo Problem/Goal/Intent; decisão sob incerteza;
  equivalência temporal sem milestones claros.

## H-003 — Informação contraditória

- **Vetor de ataque:** inconsistência interna.
- **Cenário:** projeto cujos artefatos se contradizem (dois problemas, dois
  objetivos, evidências opostas).
- **Pergunta hostil:** o protocolo detecta a contradição ou a propaga? A
  invalidação atinge as decisões dependentes?
- **Critérios testados:** propagação de invalidação; RA-OBS-005 (essencialidade);
  integridade do corpus sob conflito.

## H-004 — Metade das evidências falsa

- **Vetor de ataque:** falsificação de evidência.
- **Cenário:** 50% das evidências foram fabricadas/adulteradas.
- **Pergunta hostil:** a auditoria detecta? O corpus filtra o falso positivo
  (como OBS-0016 — ver [CF-001](./CANONICAL-FAILURES.md#cf-001--modelo-estrutural-validado-obs-0016))?
- **Critérios testados:** RA-OBS-001/002/003; capacidade do instrumento de
  auditoria de expor o não-observável.

## H-005 — Projeto em tempo real

- **Vetor de ataque:** temporalidade/velocidade.
- **Cenário:** decisões em tempo real, janelas de decisão curtas, estado que
  muda enquanto se observa.
- **Pergunta hostil:** o protocolo acompanha? A latência da auditoria é
  compatível com o ritmo do sistema?
- **Critérios testados:** equivalência temporal; snapshot/estado; overhead
  temporal do pipeline.

## H-006 — Cinco LLMs discordando

- **Vetor de ataque:** conflito epistêmico entre múltiplos agentes.
- **Cenário:** cinco LLMs (ou agentes) propõem soluções contraditórias para o
  mesmo problema.
- **Pergunta hostil:** o ECP resolve o dissenso via decisão justificada, ou o
  conflito é indecidível?
- **Critérios testados:** decisão sob incerteza (ECP-010); uso de evidência;
  governança do dissenso; RA-OBS de fontes múltiplas.

---

## Execução

1. Selecionar um H-NNN.
2. Preparar o cenário adversarial (autor/ambiente fora do controle, quando
   possível).
3. Rodar mineração → revisão ontológica → auditoria contra ele.
4. Medir RI por critério; escrever `HOSTILE-REPORT-###.yaml`.
5. Registrar falhas humanas como CF-NNN.
6. Decidir: ajustar protocolo / refinar critérios / registrar lei refutada.
