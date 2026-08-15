# GO-8D — OPENING DECISION

**Data:** 2026-08-14
**Ciclo:** GO-8D
**Status:** **OPENED / DIAGNOSTIC PHASE — NO EXPERIMENT AUTHORIZED**
**Decisor da abertura:** Governança GO-8D (autorização formal de abertura, em continuidade ao diagnóstico D-01)

---

## 1. Relação com GO-8B e GO-8C

- **GO-8D** é um ciclo **novo e independente**, aberto para tratar as dívidas herdadas do GO-8C,
  com prioridade para **validade da métrica** e **validade da taxonomia**.
- **GO-8B** permanece: **CLOSED / LOCKED / FROZEN** (registro histórico imutável).
- **GO-8C** permanece: **CLOSED** (estudo confirmatório N=12 concluído, 2026-08-14, D-04.13).
- É **PROIBIDO** alterar, corrigir, sobrescrever, re-hashar ou substituir qualquer arquivo
  congelado do GO-8B ou qualquer artefato do GO-8C (Lock GO-8C LOCKED, 151 artefatos).
- Qualquer correção identificada por este ciclo somente poderá ser implementada como **novo
  artefato/versionamento dentro do GO-8D**, mediante autorização explícita por etapa.

## 2. Contexto da Abertura (continuidade do D-01)

- O diagnóstico **D-01 (auditoria de S_struct)** foi concluído na fase de diagnóstico pré-abertura:
  `experiments/validation/GO-8C/decisions/D-01-SSTRUCT-AUDIT.md`.
- **Achados centrais do D-01:**
  1. `S_struct` mede essencialmente contagem de nós + degenerescência WL do grafo colapsado,
     **não** fidelidade ao ECP (produto interno com o ECP ≈ n²; `S_base(9)=0.587512…` explica o
     platô 0.5875 na condição A).
  2. A anonimização uniforme (`wl_kernel.py:30`) elimina o sinal de categoria/label.
  3. A topologia é amplamente determinada pelo parser (`follows` temporal + co-ocorrência crua).
  4. Seeds são vestigiais para a DV (108 linhas = 36 valores únicos).
  5. A condição B do N=12 **não é reproduzível** com o engine congelado atual (taxonomia corrigida
     D-03.7 vs congelada; BIP-007-B inconsistente na própria execução N=12).
- A abertura formal do GO-8D **incorpora** esses achados como base para D-02 e D-03.

## 3. Objetivo do GO-8D

1. Tratar as dívidas herdadas do GO-8C (7 dívidas, organizadas em 3 blocos — ver TODO).
2. Concluir e aprovar as fases de **diagnóstico (D-01..D-07)** antes de qualquer decisão de
   experimento.
3. Restaurar a **validade métrica e taxonômica** do pipeline antes de qualquer novo estudo
   confirmatório.

## 4. Escopo Inicial — Dívidas D-01..D-07

### Bloco 1 — Validade da medida
| ID | Dívida | Estado |
|----|--------|--------|
| **D-01** | S_struct — viés estrutural (auditoria concluída) | **DIAGNOSED** |
| **D-02** | Métricas alternativas | PENDING |
| **D-03** | Refinamento da taxonomia C3 | PENDING |

### Bloco 2 — Validade do desenho
| ID | Dívida | Estado |
|----|--------|--------|
| **D-04** | Gate de parseabilidade (check no validador de produção) | PENDING |
| **D-05** | Gate semântico híbrido (humano + IA) | PENDING |
| **D-06** | Definição formal de Δ para TOST | PENDING |

### Bloco 3 — Poder estatístico
| ID | Dívida | Estado |
|----|--------|--------|
| **D-07** | Recalcular N após estabilizar a métrica | PENDING |

**Importante:** nenhuma dívida está automaticamente resolvida pela abertura. Cada uma passa por:
`OBSERVAÇÃO → ANÁLISE → OPÇÕES → DECISÃO DE GOVERNANÇA → IMPLEMENTAÇÃO AUTORIZADA → VALIDAÇÃO`.

## 5. Regra de Imutabilidade

- Nenhum arquivo do GO-8B pode ser alterado por este ciclo.
- Nenhum artefato do GO-8C pode ser alterado por este ciclo (Lock GO-8C íntegro).
- Não recalcular hashes do GO-8B/GO-8C; não criar Lock para GO-8B/GO-8C.

## 6. Regra de Autorização Individual das Etapas

- Cada etapa do GO-8D exige **autorização formal e explícita** da governança.
- Nenhuma etapa é autorizada por inferência, recomendação ou memória de conversa.
- Somente decisões formalmente registradas podem alterar o estado de uma dívida.

## 7. Ausência de Autorização para Execução Neste Momento

Esta etapa de abertura **NÃO autoriza**:

- executar D-02 (métricas alternativas), D-03 (refinamento C3) ou qualquer outra dívida;
- coletar dados; executar experimento novo; executar reconstruções A/B/C;
- executar análise estatística experimental; gerar hashes; criar Lock;
- alterar qualquer arquivo do GO-8B ou do GO-8C;
- alterar parâmetros do pipeline; interpretar nenhuma dívida como automaticamente decidida;
- transformar recomendações do D-01 em decisões.

## 8. Protocolo de Achados

Se forem encontrados arquivos inesperados, inconsistências, divergências entre registros,
artefatos ausentes, alterações inesperadas ou conflitos entre versões:

1. Registrar: `FATO OBSERVADO → IMPACTO → EVIDÊNCIA → OPÇÕES → RECOMENDAÇÃO → DECISION REQUIRED`.
2. **PARAR.**
3. **NÃO corrigir automaticamente.**

## 9. Estado Final Obrigatório (desta etapa)

- **GO-8D = OPENED / DIAGNOSTIC PHASE / PENDING GOVERNANCE REVIEW**
- **GO-8B = CLOSED / LOCKED / FROZEN**
- **GO-8C = CLOSED / LOCKED (Lock GO-8C LOCKED, validado PASS)**

---

**Fim da decisão de abertura. Nenhum arquivo do GO-8B/GO-8C foi alterado. Nenhuma execução de dívida autorizada nesta etapa.
