# GO-8C — D-04 — Divergência do Painel NT-05 Estendido — ANÁLISE E DECISÃO

**Data:** 2026-08-14
**Ciclo:** GO-8C
**Autor:** executor (análise) + governança (decisão)
**Contexto:** painel estendido NT-05 (D-04.6) retornou divergência:
- **Revisor 1 (GLM):** REJEITADO — 2 violações na taxonomia C3.
- **Revisor 2 (Gemini):** PASS — 0 violações.
- **Regra aplicada:** divergência = **STOP**; investigação antes de decidir.

---

## 1. Lista de termos ECP (fonte congelada)

A lista operacional de 52 termos ECP está registrada em dois artefatos:
- `GO-8B/pilot-input/validate_bip007.py:13-23` (validador congelado GO-8B).
- `GO-8C/scripts/C3_TAXONOMY.yaml:170-221` (`ecp_term_list`, compilação operacional).

```
afirmacao, aprendizado, artefato, artifact, assumption, cadeia de dependencias,
capability, capacidade, claim, conhecimento, contrato, decisao, decisao e causa,
decision, entidade, estado, evidence, evidencia, fase pos-artefato,
fluxo e consequencia, goal, grafo de conhecimento, knowledge, l-0, l-1, l0, l1,
learning, lei um, lei zero, objetivo, p-1..p-12, problem, problema, rastreabil,
risco, risk, state, suposicao, validacao, validation
```

## 2. Labels atuais da taxonomia C3 (GO-8C `C3_TAXONOMY.yaml`)

| ID | label |
|---|---|
| SYN-001 | `Funcao` |
| SYN-012 | `Adaptacao` |

## 3. "Funcao"/"Adaptacao" constam na lista ECP?

**NÃO.** Verificação programática sobre a lista de 52 termos:

| Probe | Na lista ECP? |
|---|---|
| `funcao` | Não |
| `function` | Não |
| `adaptacao` | Não |
| `adaptation` | Não |
| `ajuste` | Não |
| `atividade` | Não |

## 4. Definições atuais após a correção D-03.7

A correção D-03.7 alterou **apenas as definições**, não os labels:

| ID | Antes (D-03.7) | Depois (D-03.7) | Label (inalterado) |
|---|---|---|---|
| SYN-001 | `Atividade elementar que transforma entradas...` | `Procedimento basico que transforma entradas...` | `Funcao` |
| SYN-012 | `Ajuste local do comportamento...` | `Resposta do comportamento das funcoes...` | `Adaptacao` |

## 5. Análise: a violação apontada pelo Revisor 1 procede?

### Conclusão: **FALSO POSITIVO (Cenário B).**

### Argumentos técnicos

1. **Isolamento léxico ECP é satisfeito (NT-01).**
   O teste automatizado NT-01 varre labels, definitions e source_refs contra os **52 termos ECP** via casamento por palavra (`\bterm\b`, normalização acentuada). Resultado registrado no próprio `C3_TAXONOMY.yaml`: `NT-01: 0 matches of 52 ECP terms; hits=[]`. Como `funcao`/`function` e `adaptacao`/`adaptation` **não estão** na lista, os labels **não violam** o isolamento léxico ECP.

2. **Origem externa é permitida por construção (regra N-3).**
   O `03-SYNTHETIC-TAXONOMY-C3.md` (GO-8B) exige que a taxonomia derive de **literatura externa de engenharia** — ex.: **ISO 15288, SysML, STAMP, FRAM** — explicitamente **não do ECP**. Os labels `Funcao` e `Adaptacao` são **vocabulário FRAM/STAMP** (source_refs: `FRAM-Hollnagel-2012`, `STAMP-Leveson-2011`, `FRAM-Hollnagel-2012-resilience`). Trata-se de terminologia de **fonte externa permitida**, não de termo ECP.

3. **A D-03.7 já resolveu a paráfrase de conceito ECP.**
   A D-03.7 identificou **paráfrase de conceito ECP nas definições** ("Atividade elementar" ~ Função; "Ajuste local" ~ Adaptação) e corrigiu **somente as definições**. Os labels foram mantidos e passaram na revisão semântica **D-03.8** (painel GLM + Gemini, ambos PASS nas 12 categorias P-1, incluindo SYN-001 e SYN-012). O Revisor 1 do painel estendido re-litiga um ponto já resolvido pela D-03.7.

4. **Inconsistência interna do Revisor 1.**
   Se os labels de origem FRAM/STAMP fossem violação, o Revisor 1 deveria ter flagrado **todas** as categorias com a mesma natureza: `Entrada`, `Saida`, `Precondicao`, `Recurso`, `Tempo`, `Controle`, `Realimentacao`, `Acoplamento`, `Condicao-Externa`, `Restricao-de-Seguranca` (todas com source_refs FRAM/STAMP/ISO). Flagrar apenas SYN-001 e SYN-012, sem critério sistemático, indica interpretação não reproduzível, não uma falha real de isolamento.

5. **Precedente congelado.**
   O GO-8B aprovou a C3 com esses labels; o GO-8C herdou a estrutura intacta (D-03.7 confirmou nós 12/12 e arestas 13/13 idênticos ao GO-8B, alterando apenas 2 definições). Não há registro congelado apontando os labels como termos ECP.

## 6. Recomendação à governança

- **Conclusão técnica:** o Revisor 1 cometeu **erro de interpretação** — confundiu terminologia de **fonte externa (FRAM/STAMP), permitida pela regra N-3**, com termos do vocabulário **ECP**. Os labels `Funcao` e `Adaptacao` **não violam** o isolamento.
- **Opções (decisão da governança):**
  - **Opção B1 — Aceitar a divergência com justificativa:** registrar este documento, considerar o Revisor 1 como falso positivo e o painel como PASS (alinhado ao Revisor 2 e ao NT-01 determinístico). Requer decisão de governança de que um voto errôneo não invalida o consenso técnico.
  - **Opção B2 — Reexecutar o painel com nota de contexto:** acrescentar ao prompt dos revisores a regra N-3 (labels FRAM/STAMP são fontes externas permitidas; isolamento ECP é definido pela lista de 52 termos) e reexecutar o painel estendido. Sem alteração de taxonomia ou materiais.

## 7. Escopo desta análise

- Nenhuma alteração em `C3_TAXONOMY.yaml` (Cenário A **não** aplicável — não há violação real).
- Nenhuma alteração nos materiais do GO-8C.
- Nenhum arquivo do GO-8B alterado.
- Registro de análise criado apenas para suportar a decisão da governança.

## 8. DECISÃO DA GOVERNANÇA (Opção B1 — aceitar divergência com justificativa)

- **Decisor:** Governança GO-8C
- **Data da decisão:** 2026-08-14
- **Decisão:** aceitar a divergência com justificativa formal; consolidar o **NT-05 estendido como PASS**.
- **Classificação:** a divergência apontada pelo Revisor 1 (GLM) é **falso positivo**.
- **Justificativa formal:**
  - Os labels `Funcao` e `Adaptacao` **não constam** na lista ECP (52 termos, congelada em `validate_bip007.py` e `C3_TAXONOMY.yaml`).
  - São **vocabulário FRAM/STAMP**, fontes externas permitidas pela regra **N-3** (`03-SYNTHETIC-TAXONOMY-C3.md`).
  - O teste determinístico **NT-01** confirma **zero hits** dos 52 termos ECP (labels/definitions/source_refs).
  - A **D-03.7** corrigiu as definições (paráfrases removidas) e a **D-03.8** já havia aprovado os labels no painel base (GLM + Gemini, PASS).
- **Posição sobre o processo:** esta decisão **não enfraquece** o processo — a divergência foi resolvida por **análise da governança**, como previsto na regra (divergência = STOP + investigação antes de decidir).
- **Ressalva de auditoria:** a divergência fica **registrada para auditoria futura** (este documento + formulários MODEL-1/MODEL-2 do painel estendido, sem alteração).
- **Consequência operacional:** `BIP-VAL_REPORT.yaml` (GO-8C) atualizado para `NT-05 extended: PASS_AI_PANEL (divergence justified)`; `verdict: PASS`. `TODO-GO-8C.md` e `decisions/ACTION-REGISTER.md` atualizados.

---

**Fim da análise técnica e decisão da divergência NT-05 estendida (Cenário B — falso positivo; DECIDED B1 — PASS com justificativa).**
