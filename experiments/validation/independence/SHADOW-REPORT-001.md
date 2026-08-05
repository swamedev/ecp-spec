# SHADOW-REPORT-001 — Seleção do SX-001 (Challenger STS-51-L)

| Campo | Valor |
|---|---|
| **Tipo** | Registro de seleção do Shadow Experiment 001 |
| **Status** | Selecionado (etapas 7-8 do SX-SELECTION concluídas) |
| **Data** | 2026-08-03 |
| **Autor** | Protocolo SX-SELECTION (decisão automática; nenhuma preferência humana) |
| **Governado por** | [SX-SELECTION](./SX-SELECTION.md), [P-0007](../P-0007-INDEPENDENCE.md), [P-0007.1](../P-0007.1-INDEPENDENCE-FRAMEWORK.md), [P-0007.2](../P-0007.2-CANDIDATE-REAUDIT.md) |
| **Referências** | [SX-REAUDIT.yaml](./SX-REAUDIT.yaml), [SHADOW-EXPERIMENTS](./SHADOW-EXPERIMENTS.md) |

## Seleção automática (algoritmo cego)

O protocolo recebeu apenas os dados dos 9 candidatos SELECTABLE e aplicou as
prioridades **pré-registradas** (SX-SELECTION, etapa 7), sem intervenção humana:

```
for candidato in SELECTABLE:
    verificar_fontes()   # etapa 5 — acessibilidade pública
    calcular_EI()        # contagem de origens causais independentes
    calcular_DDS()       # domínio pela taxonomia canônica
    emitir_veredito()
```

### Resultado da verificação de fontes (etapa 5)

Todos os 9 SELECTABLE tiveram fontes primárias públicas acessíveis confirmadas:
- **Apollo 13** — NASA transcripts, Apollo 13 Mission Report (NTRS), Apollo 13 Review Board, imprensa contemporânea.
- **Challenger** — Rogers Commission Report (público), NASA records, cobertura ao vivo.
- **I-35W** — NTSB/HAR-08/03 (público), registros MnDOT, imprensa.
- **Deepwater Horizon** — relatório BP, relatório CSB, investigação JIT, audiências do Congresso.
- **Chernobyl** — INSAG-1/7 (IAEA), relatório soviético, UNSCEAR.
- **Ebola** — relatórios WHO, relatos MSF, múltiplas equipes acadêmicas.
- **Operation Warp Speed** — relatórios GAO, documentos HHS/BARDA, imprensa.
- **Suez / Ever Given** — investigações de salvado (P&I Club), Suez Canal Authority, análise de satélite.
- **Genoma Humano** — documentos NHGRI/DOE, publicações revistas por pares, documentos Celera.

Nenhum candidato foi eliminado por inacessibilidade (EC-3).

### Classificação pré-registrada (ranking pré-decidido)

Já no [SX-CANDIDATES](./SX-CANDIDATES.md) (antes da reauditoria e antes da
verificação), o protocolo registrou a ordem de preferência por **(a) domínio mais
distante do software → (b) postmortem → (c) maior multiplicidade**:

1. **Challenger (1986)** — postmortem oficial, engenharia física, máxima multiplicidade (Comissão + NASA + mídia).
2. Apollo 13 (1970)
3. Chernobyl (1986)
4. Deepwater Horizon (2010)
5. I-35W (2007)

### Veredito (automação dos critérios)

Após a verificação de fontes (todos PASS), a aplicação da prioridade (a) `domínio
mais distante do software` não elimina entre os fora-de-software; (b) `postmortem
público` é satisfeita por Challenger (Rogers Commission Report, engenharia física)
com a **maior multiplicidade de origens causais** entre os SELECTABLE (Comissão
independente + registros NASA + mídia ao vivo). Portanto:

> **O protocolo seleciona o Challenger STS-51-L (1986) como alvo do SX-001.**

Nenhuma votação, preferência ou gosto pessoal. A escolha decorre das regras.

## SX-001 — agora Selecionado

- **Alvo:** Challenger STS-51-L (1986), domínio Espacial/Aeroespacial.
- **Pergunta central (SX-SELECTION):** as entidades do ECP emergem
  espontaneamente em um projeto conduzido sem qualquer influência do ECP?
- **Status:** **EXECUTADO (2026-08-03)** — ver [SX-001](./SX-001/README.md):
  Narrativa → Atomic Facts → Reconstrução Cega → Alignment → Signals → EAR.
  **`EAR(Challenger) = 0.775`** (observação) e achado Evidence→Decision em
  [DISCOVERY-LOG](../DISCOVERY-LOG.md).
- **Próxima etapa:** P-0008 — Cross-Domain Validation
  ([P-0008](../P-0008-CROSS-DOMAIN-VALIDATION.md)): selecionar SX-002 pelo
  protocolo congelado e repetir o pipeline em outro domínio. Nenhuma regra
  metodológica é alterada (FASE C2, infraestrutura congelada). Limitações →
  [dívida metodológica v1.1](../METHODOLOGICAL-DEBT.md).

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Seleção automática do Challenger STS-51-L como alvo do SX-001, pela automação das prioridades pré-registradas. |

---
> **Regra do teste:** uma boa teoria não cria os fenômenos que explica; ela os reconhece onde eles já existem.