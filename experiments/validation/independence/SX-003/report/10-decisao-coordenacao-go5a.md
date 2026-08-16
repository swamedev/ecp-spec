# SX-003 / Decisão de coordenação — GO-5A

| Campo | Valor |
|---|---|
| **Comando** | GO-5A — DECISÃO DE ADMISSIBILIDADE DO SX-003 (tratamento da contaminação de isolamento) |
| **Autor** | Coordenação do programa (veredito registrado) |
| **Data** | 2026-08-09 |
| **Antecedentes** | GO-3 ([07-revisao-pos-experimento](./07-revisao-pos-experimento.md)), GO-4A ([08-changelog-reparo-go4a](./08-changelog-reparo-go4a.md)), GO-4B ([09-auditoria-isolamento-go4b](./09-auditoria-isolamento-go4b.md)) |
| **Governado por** | Leis L-0/L-1; P-0007.1 (Independence Framework); regras da FASE E (pipeline congelado) |
| **Decisão** | **AUTORIZADA** — GO-5A registrado; emissão transversal adiada |

---

## 1. Natureza da decisão

O GO-5A decide a **admissibilidade do SX-003** e o tratamento da contaminação de
isolamento detectada na GO-4B, **antes** de qualquer análise transversal. É uma
decisão sobre o tratamento do experimento — **não** sobre o valor científico dos
fatos coletados.

> **Regra central preservada:** não transformar uma evidência metodologicamente
> comprometida em evidência de confirmação. E o inverso: não transformar um
> problema de isolamento numa decisão sobre o resultado científico.

---

## 2. Veredito

| Item | Estado |
|---|---|
| Status do SX-003 | **PARADO** |
| Promoção | **NÃO PROMOVER** |
| Descarte | **NÃO DESCARTAR** |
| Transversal SX-001 × SX-002 × SX-003 | **BLOQUEADO** |

> **SX-003: PARADO — NÃO PROMOVER — NÃO DESCARTAR.**

---

## 3. Separação das duas perguntas

### Pergunta A — validade factual do SX-003

A auditoria GO-4B (§3.1) classificou a camada factual como **integral**. Os
artefatos factuais permanecem aproveitáveis: fatos, reconstrução factual,
contagens (15 MATCH / 7 PARTIAL / 2 NOT / 2 NEW = 26) e **EAR = 0.77**.

### Pergunta B — validade da inferência independente

**Comprometida** na camada interpretativa comparativa. A reconstrução cega expôs
o executor a SX-001/SX-002 (tabela comparativa §3, leitura em contraste §2/SIG-002).
Essa parte **não pode** ser usada como evidência de independência interpretativa.

> O vazamento **permanece registrado exatamente como está** — ele próprio é um
> resultado metodológico. Não se "corrige" apagando evidência.

---

## 4. Admissibilidade (as duas questões respondidas)

**Q1 — O SX-003 é utilizável agora para a análise transversal?**

| Alternativa | Descrição | Escolha |
|---|---|---|
| A | Sim | — |
| **B** | **Não por enquanto** | ✔ preferível |

**Q2 — O que fazer com o caso/artefatos enquanto isso?**

| Alternativa | Descrição | Escolha |
|---|---|---|
| A | Reexecutar/descartar imediatamente | — |
| **B** | **Preservar como experimento válido com ressalvas e dívida registrada** | ✔ preferível |

A escolha B/B mantém o caso disponível como observação factual, sem promover a
camada cuja independência não está demonstrada.

---

## 5. Dois resultados, mantidos separados

O SX-003 produziu **dois resultados distintos** — e eles devem permanecer separados:

- **Resultado substantivo:** o caso de sucesso apresentou estrutura cognitiva
  observável (cadeia Goal→Validation emerge; SIG-003 reaparece; presença ex-ante
  de Goal/Problem).
- **Resultado metodológico:** o desenho experimental permitiu exposição
  interpretativa; portanto a independência **dessa camada** não está demonstrada.

Nenhum dos dois pode converter o outro. O substantivo não se torna confirmação;
o metodológico não invalida os fatos.

---

## 6. Implicação para DEBT-001/006

O SX-003 evidenciou algo que os dois primeiros experimentos não revelaram com
tanta clareza:

> **O isolamento do avaliador precisa ser tratado como propriedade experimental
> explícita — não como intenção do protocolo.**

Isso conversa diretamente com DEBT-001/DEBT-006 (mesmo executor em narrativa e
reconstrução) e deve ser registrado na consolidação v1.1
(Discovery Log / [METHODOLOGICAL-DEBT](../../METHODOLOGICAL-DEBT.md)).

---

## 7. Sequência decidida

```
GO-4A ✅
GO-4B ✅
   ↓
GO-5A — decisão formal          ← registrada aqui
   ↓
PARADO / NÃO PROMOVER / NÃO DESCARTAR
   ↓
resolver situação do isolamento (camada interpretativa contaminada)
   ↓
GO-5 — análise transversal
   ↓
somente depois:
   Signals → candidatura a Pattern
   Pattern → eventual LAW-H
```

---

## 8. Não autorizado (até a resolução do isolamento)

| Ação | Autorizado? |
|---|---|
| Análise transversal SX-001 × SX-002 × SX-003 | ❌ Não |
| Promoção de Signal (SIG-003 / SIG-005) | ❌ Não |
| Criação de Pattern | ❌ Não |
| Alteração de protocolo | ❌ Não |
| Novo experimento | ❌ Não |

Misturar o SX-003 aos outros dois casos **agora** poderia produzir exatamente o
tipo de contaminação metodológica que o ECP está tentando detectar (GO-4B: camada
factual íntegra, camada interpretativa comparativa comprometida).

---

## 9. Próxima decisão da coordenação (após o GO-5A)

Resolver o **tratamento da camada contaminada** — duas alternativas ficam
abertas:

- **A — Aceitar com limite:** SX-003 como evidência factual + evidência de
  emergência estrutural, **excluindo** qualquer inferência comparativa
  contaminada.
- **B — Reexecutar somente a reconstrução cega/interpretação** em condições
  realmente isoladas, mesmo caso, **sem alterar o pipeline congelado**. —
  **Recomendada** se o objetivo do ECP for construir uma evidência
  metodologicamente forte.

---

## 10. PARAR

Após este registro, **PARAR novamente para revisão da coordenação**.

- ❌ Nenhum artefato científico alterado (estágio de decisão, não de coleta).
- ❌ Nenhuma análise transversal.
- ❌ Nenhum Signal → Pattern.
- ❌ Nenhuma alteração de protocolo.
- ❌ **Nenhum commit.**

---

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-09 | GO-5A autorizado pela coordenação. SX-003: **PARADO — NÃO PROMOVER — NÃO DESCARTAR**. Transversal **BLOQUEADO**. Camada factual preservada (EAR 0.77); camada interpretativa comparativa comprometida; vazamento mantido como registro. As duas perguntas separadas (Q1/Q2 → B/B). Próxima decisão: tratamento da camada contaminada (recomendação: reexecução isolada, alt. B). Sem commit. |