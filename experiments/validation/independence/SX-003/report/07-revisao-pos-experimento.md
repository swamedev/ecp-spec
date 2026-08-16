# SX-003 / Revisão pós-experimento — GO-3

| Campo | Valor |
|---|---|
| **Experimento** | EXP-SX003 (Projeto Genoma Humano, 1990–2003) |
| **Comando** | GO-3 — AUTORIZAR REVISÃO PÓS-EXPERIMENTO DO SX-003 |
| **Autor** | Executor do pipeline congelado (GO-3) |
| **Data** | 2026-08-09 |
| **Estado** | **PARAR — revisão da coordenação** |

> **Escopo do GO-3 (texto da autorização):** revisar **exclusivamente**
> integridade, independência, observações, dívidas metodológicas, admissibilidade
> dos Signals e limites do experimento. Não alterar artefatos científicos, não
> promover Signal → Pattern, não comparar EAR quantitativamente, não executar
> análise transversal e não fazer commit. Ao finalizar, **PARAR**.

> **Status do comando:** este documento **registra** a revisão. Nenhum artefato
> científico (`00-pre-registro` … `06-relatorio-ear`) foi modificado nesta etapa.
> Corrupções identificadas são listadas em §1 e **propostas de reparo** ficam para
> decisão da coordenação.

---

## 1. Revisão de integridade

### 1.1 Integridade estrutural (fluxo do pipeline)

O pipeline congelado foi executado em ordem e sem lacunas de artefato:

| Etapa | Artefato | Presente |
|---|---|---|
| 0 | `sources/00-fontes.md` | ✅ |
| 1 | `narrative/01-narrativa-original.md` | ✅ |
| 2 | `reconstruction/02-atomic-facts.md` (50 AFs) | ✅ |
| 3 | `reconstruction/03-reconstrucao-cega.md` | ✅ |
| 4 | `comparison/04-alignment-analysis.md` (26 itens) | ✅ |
| 5 | `signals/05-signals.yaml` | ✅ |
| 6 | `report/06-relatorio-ear.md` (EAR = 0.77) | ✅ |

Contagem verificada na Etapa 4 (auditável): **15 MATCH + 7 PARTIAL + 2
NOT_EXPLAINED + 2 NEW_INSIGHT = 26**; denominador EAR = 24 (15+7+2), numerador =
18.5 → `18.5/24 = 0.7708 → 0.77`. Cálculo conferido por recontagem dos itens.

### 1.2 Corrupções de texto detectadas (registro — reparo depende da coordenação)

Foram identificadas corrupções de digitação/edição em vários artefatos. **Não
foram alteradas nesta etapa** (GO-3 proíbe alterar artefatos científicos). Lista
completa:

| Arquivo | Local | Corrupção | Correção proposta |
|---|---|---|---|
| `narrative/01-narrativa-original.md` | §3, linha ~49 | "majorçamente" | "majoritariamente" |
| `narrative/01-narrativa-original.md` | §6, linha ~79 | "dedicassse" | "dedicasse" |
| `narrative/01-narrativa-original.md` | §7, linha ~84 | "o IHG em evento" | "o IHGSC em evento" |
| `sources/00-fontes.md` | Grupo 4 | "DOE/ORN-000" | "DOE/ORNL" |
| `sources/00-fontes.md` | nota | "Risco da terminolologia" | "Risco da terminologia" |
| `sources/00-fontes.md` | nota | "painéis do NHGIR" | "painéis do NHGRI" |
| `reconstruction/03-reconstrucao-cega.md` | §1.3, linha ~70 | "aún não existia" | "ainda não existia" |
| `reconstruction/03-reconstrucao-cega.md` | §1.8, linha ~137 | "validacao do resultado" | "validação do resultado" |
| `reconstruction/03-reconstrucao-cega.md` | §1.9, linha ~158 | "Sem suporte ver: (o 'aprendizado' explícito é af-037/038a)" | "Sem suporte direto para além da validação" |
| `reconstruction/03-reconstrucao-cega.md` | §5, linha ~248 | "DEB-009" | "DEBT-009" |
| `reconstruction/03-reconstrucao-cega.md` | §5, linha ~248 | "a reconstrução não resiste à conclusão" | "a reconstrução não força a conclusão" |
| `comparison/04-alignment-analysis.md` | NI-002 | "ausência de Risk calculus" | "ausência de Risk calculado" |

### 1.3 Inconsistência de referências AF-011 × AF-012 (troca prazo/custo)

Foi identificada uma **troca de referências** em dois artefatos:

- `AF-011` = prazo (~15 anos); `AF-012` = custo (~US$ 3 bi) — conforme
  [02-atomic-facts.md](../reconstruction/02-atomic-facts.md) §B (AF-011/AF-012).
- ❌ `reconstruction/03-reconstrucao-cega.md` §2 (linha ~165): "Goal (... AF-012 —
  prazo 15 anos; custo AF-011)" — **invertido**.
- ❌ `signals/05-signals.yaml` SIG-005 (linha ~72): "prazo 15 anos (AF-012), custo
  (AF-011)" — **invertido**.

A redação ("prazo 15 anos", "custo US$ 3 bi") está correta; apenas os números de
AF estão trocados nos dois arquivos. **Impacto no resultado: nenhum** — a
categoria é MATCH e o dado não muda. **Impacto na rastreabilidade: sim** (citação
factual incorreta). Proposta: corrigir as duas referências para `AF-011` (prazo)
e `AF-012` (custo).

### 1.4 Integridade do staging do candidato (inconsistência operacional)

`candidates/genoma-humano/sources/raw/inventory.json` declara "raw/ está vazio —
nenhum documento baixado ainda" e `total_arquivos: 0`. Porém o diretório `raw/`
contém **8 arquivos HTML** (`nhgri-01/02/03`, `doe-01`, `celera-01`,
`sci-01-pubmed`, `sci-02-pubmed`, `sci-01-nature`). O inventário está
**desatualizado** (gerado antes da promoção dos snapshots). Não afeta o
experimento (a fonte de verdade é `SX-003/sources/00-fontes.md`), mas é uma
pendência operacional de rastreabilidade para registrar.

### 1.5 Veredito de integridade

**ESTRUTURAL: APROVADO.** Pipeline completo, ordenado, com proveniência
preservada e contagens auditáveis.

**TEXTUAL: APROVADO COM RESSALVAS.** As corrupções da §1.2 são tipográficas e
não alteram o conteúdo científico; a troca AF-011/AF-012 (§1.3) afeta citação,
não resultado. **Reparo proposto** (depende da coordenação, pois o GO-3 proíbe
editar artefatos científicos).

---

## 2. Revisão de independência observacional

| Condição (P-0007.1) | Exigência | SX-003 |
|---|---|---|
| Projeto | não segue o ECP | ✅ HGP (1990–2003) nunca usou o ECP |
| Observador | não conhece o ECP | ❌ mesmo executor (ECP interno) |
| Executor | não conhece o ECP | ❌ mesmo executor |

- A condição **Projeto** é satisfeita de forma forte (caso histórico, exógeno,
  sem qualquer exposição ao ECP).
- As condições **Observador/Executor** não são satisfeitas — **reincidência**
  da limitação DEBT-001/DEBT-006 (mesmo executor na narrativa e na reconstrução).
  Mitigação aplicada: reconstrução cita apenas `AF-###` e marca inferências.
- **Multiplicidade causal (EI):** ≥4 origens independentes confirmadas na Etapa 0
  (NHGRI/DOE · Nature/Science · Celera · Wellcome/consórcio), consistente com
  `SX-REAUDIT.yaml` (lc_10_ei do candidato Genoma).
- **Blindagem da coleta:** `00-fontes.md` declara coleta anterior a qualquer uso
  do vocabulário ECP; verificação de acessibilidade por **grupo** de origens (não
  por URL individual) — reincidência da DEBT-010.

### Aderência ao pipeline congelado (GO-2)

- ❌ **Divergência registrada:** a §3 de `03-reconstrucao-cega.md` contém uma
  **tabela comparativa com SX-001/SX-002** (linhas ~204–216). A instrução do
  GO-2 determinava **não comparar com SX-001/SX-002 antes da revisão
  pós-experimento**. A tabela compara `Problem ex-ante / Risk formal / Project /
  Decisions` entre os três casos **dentro da reconstrução cega**.
  - **Leitura:** o conteúdo da comparação é coerente com a Etapa 4 e não altera
    o resultado; porém **a localização viola a instrução de isolamento**
    (comparação deveria ficar para a revisão, não na reconstrução cega).
  - **Ação proposta:** na pós-revisão, a coordenação decide se a tabela da §3
    permanece (registrada como observação pré-verificada, como rotulado no texto)
    ou se o trecho é movido/removido em reparo formal. **Não é decisão desta
    etapa.**

---

## 3. Observações do experimento (dados, não conclusões)

1. **Emergência afirmativa da cadeia no caso de sucesso:** Goal, Knowledge,
   Lacuna, Assumption, Decision, Execution, Evidence, Validation emergem dos 50
   Atomic Facts **sem ruptura e sem lag** — cadeia completa, com as decisões
   formais **antecedendo** os marcos de evidência.
2. **Presença ex-ante de Goal/Problem (dado central):** no Genoma, Goal e Problem
   são **declarados desde o início** (AF-005/006, AF-047), com projeção de prazo
   e custo (AF-011/012) — **contraste** com a ausência/pós-hoc dos casos de crise.
3. **Risk formal continua ausente mesmo no sucesso:** não emerge cálculo
   formal de risco (impacto×probabilidade) nos fatos; o risco social foi tratado
   por **governança** (programa ELSI, AF-034). Registro neutro de ausência.
4. **EAR(Genoma) = 0.77**, falso positivo zero (nada foi inventado pela
   reconstrução). **Observação de um caso — sem comparação quantitativa**
   (proibida no GO-3).

> Todas são **observações** (Discovery Log), não leis. A interpretação
> ("presença ex-ante distingue sucesso de crise") é **proibida nesta etapa** e
> fica para a coordenação.

---

## 4. Dívidas metodológicas (reincidências e novas)

### 4.1 Reincidências (mesmas dívidas de SX-001/002)

| Dívida | Status no SX-003 | Registro |
|---|---|---|
| DEBT-001/006 — mesmo executor na narrativa e na reconstrução | **Reincidiu** (§2) | `03-reconstrucao-cega.md` §0 |
| DEBT-002/007 — EAR com denominador definido post hoc | **Reincidiu** (24 itens na Etapa 4, sem regra pré-registrada) | `06-relatorio-ear.md` §1 |
| DEBT-010 — verificação de acessibilidade por grupo, não por URL | **Reincidiu** | `00-fontes.md` §Veredito |

### 4.2 Novas pendências específicas do SX-003

| Item | Descrição | Categoria |
|---|---|---|
| AF-011/AF-012 trocados em `03` e `05-signals` | Citação factual incorreta; sem impacto no resultado | Integridade de rastreabilidade |
| `inventory.json` do candidato desatualizado | Declara `raw/` vazio; há 8 arquivos | Operacional |
| Tabela comparativa SX-001/002 dentro da reconstrução cega | Violação do isolamento do GO-2; conteúdo coerente | Conformidade de protocolo |

> Nada aqui é **conclusão** nem **correção**; tudo é **registro para a v1.1**
> (regras da FASE E — pipeline congelado).

---

## 5. Admissibilidade dos Signals (RA-SIG-001 / RA-SIG-005)

| Signal | Ocorrências | independente | Admissível (RA-SIG-001 ≥2) | Promoção a Pattern (RA-SIG-005) |
|---|---|---|---|---|
| SIG-003 — cadeia emerge sem vocabulário ECP | 3 (Challenger, Ebola, **Genoma**) | true | ✅ | ❌ não nesta etapa |
| SIG-002 — ausência de infraestrutura cognitiva | 2 (Challenger, Ebola) | true | ✅ (não alterado) | ❌ |
| SIG-001 — decisão justificável requer conhecimento | 2 (Challenger, Ebola) | true | ✅ (não alterado) | ❌ |
| SIG-004 — lag alerta→coordenação | 1 (Ebola) | false | ❌ (candidato) | ❌ |
| **SIG-005** — presença ex-ante em sucesso | **1 (Genoma)** | true* | ❌ (1 ocorrência) | ❌ |

> **RA-SIG-005 (promoção a pattern):** não satisfeita — nenhum signal é promovido.
> **RA-SIG-001:** SIG-003 passa a satisfazê-la com folga (3 origens); SIG-005
> permanece **candidato** (1 ocorrência; *independente* mas *insuficiente* — não
> há 2º caso de sucesso).

**Decisão registrada para a coordenação:** a promoção de SIG-003 (e a evolução
de SIG-002 → corolário da predição inversa) **não é feita aqui**; requer revisão
formal da coordenação e a consolidação v1.1 (fora do escopo congelado).

---

## 6. Limites do experimento

1. **Single case de sucesso:** o "presença ex-ante" é dado de **1 caso**; exige
   reprodução (ex.: Operation Warp Speed, apontado no pré-registro) antes de
   qualquer inferência.
2. **Mesmo executor** em narrativa e reconstrução (DEBT-001/006 reincidente).
3. **EAR com denominador post hoc** (DEBT-002/007 reincidente).
4. **Trajetória longa (1990–2003)** comprimida em 50 Atomic Facts — escolha de
   granularidade do executor.
5. **Fontes públicas institucionais** (NHGRI/DOE são as próprias entidades do
   projeto) — mitigado por ≥4 origens causais e por publicações revisadas por
   pares; não elimina a endogeneidade parcial do registro institucional.
6. **Verificação de acessibilidade por grupo**, não por URL individual (DEBT-010).
7. **Blindagem imperfeita:** a reconstrução cega contém tabela comparativa com
   SX-001/002 (§2), enfraquecendo o isolamento ideal do pipeline.

---

## 7. Veredito e PARAR

> **Veredito da revisão (GO-3):**
> - **Integridade estrutural:** ✅ aprovada (pipeline completo, ordenado,
>   auditável).
> - **Independência:** ✅ caso exógeno forte; ❌ reincidência do mesmo-executor
>   (dívida conhecida, mitigada por AF-###).
> - **Observações:** registradas como dados — emergência afirmativa no sucesso,
>   presença ex-ante de Goal/Problem, Risk formal ausente.
> - **Dívidas metodológicas:** reincidências DEBT-001/006, DEBT-002/007,
>   DEBT-010 + pendências de rastreabilidade (§4).
> - **Admissibilidade dos Signals:** SIG-003 admissível (3 ocorrências); SIG-005
>   candidato (1 ocorrência); **nenhuma promoção**.
> - **Limites:** registrados (§6).

**PARAR — entregue à coordenação.**

Conforme o GO-3:
- ❌ Nenhum artefato científico alterado nesta revisão.
- ❌ Nenhum Signal → Pattern.
- ❌ Nenhuma comparação quantitativa de EAR.
- ❌ Nenhuma análise transversal.
- ❌ **Nenhum commit.**

> **Próximos passos (decisão da coordenação, fora desta etapa):**
> 1. Autorizar (ou não) o **reparo das corrupções** (§1.2) e da troca AF-011/AF-012 (§1.3).
> 2. Decidir sobre a tabela comparativa dentro da reconstrução cega (§2).
> 3. Autorizar **commit** do SX-003 (após aprovação da revisão).
> 4. Autorizar a **análise transversal** SX-001 × SX-002 × SX-003 e a decisão
>    sobre promoção de SIG-003 / SIG-005 (somente depois).
> 5. Registrar dívidas e observações (Discovery Log / METHODOLOGICAL-DEBT) — v1.1.

## 8. Encaminhamento dos GO-4A / GO-4B (2026-08-09)

> Decisões registradas da coordenação executadas após o GO-3. Nenhuma alteração de
> conteúdo científico — somente reparo controlado e auditoria.

### 8.1 GO-4A — Reparo controlado aplicado

- **Changelog auditável:** [`08-changelog-reparo-go4a.md`](./08-changelog-reparo-go4a.md).
- **Correções aplicadas:** 3 digitações na narrativa, 3 em fontes, 4 corrupções na
  reconstrução, 1 rótulo no alignment, e **troca AF-011/AF-012** corrigida nos 4
  pontos constatados (reconstrução §2, §1.4, §3; signals SIG-005) + 1 ponto
  adicional (reconstrução linha ~79) da mesma classe.
- **Verificação:** recontagem Etapa 4 = 26 (15/7/2/2) e EAR = 0.77 **inalterados**;
  AFs e sinais intocados; nenhum commit.

### 8.2 GO-4B — Auditoria de isolamento (tabela comparativa na reconstrução cega)

- **Relatório:** [`09-auditoria-isolamento-go4b.md`](./09-auditoria-isolamento-go4b.md).
- **Veredito:** camada **factual/observacional = INTEGRAL** (entidades têm suporte
  AF-### direto); camada **interpretativa comparativa = COMPROMETIDA** (contraste
  com SX-001/002, tabela §3, corolário SIG-002 produzidos com conhecimento prévio).
- **Decisão registrada:** o vazamento fica mantido como registro (não é apagado); a
  interpretação comparativa não entra como evidência independente de "primeiro caso
  de sucesso"; decisão sobre análise transversal adiada para GO-5.

---

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-09 | Revisão pós-experimento do SX-003 (GO-3). Integridade estrutural aprovada; corrupções textuais e troca AF-011/AF-012 registradas para reparo; dívidas DEBT-001/006, DEBT-002/007, DEBT-010 reincidentes; SIG-003 admissível (3 ocorrências), SIG-005 candidato; sem promoção; sem commit. **PARAR para revisão da coordenação.** |
| 1.1 | 2026-08-09 | Encaminhamento GO-4A/GO-4B: reparo controlado aplicado (08-changelog) e auditoria de isolamento (09-auditoria) registrados; contagens/EAR inalterados. |
