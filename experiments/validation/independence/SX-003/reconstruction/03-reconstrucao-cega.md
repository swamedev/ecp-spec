# SX-003 / reconstruction — Etapa 3: Reconstrução Cega

| Campo | Valor |
|---|---|
| **Experimento** | EXP-SX003 |
| **Etapa** | 3 — Reconstrução Cega |
| **Entrada** | **Somente** [02-atomic-facts.md](./02-atomic-facts.md) + Kernel ECP-000..ECP-009 |
| **Proibido** | Consultar a [narrativa original](../narrative/01-narrativa-original.md) durante a reconstrução |
| **Data** | 2026-08-09 |

> **Protocolo de reconstrução:** (1) ler os Atomic Facts; (2) para cada fato,
> perguntar *"que papel esse fato desempenha na estrutura do evento?"*; (3)
> reconhecer uma entidade **somente quando** existir suporte factual direto
> (`AF-###`); (4) marcar como **inferida** qualquer categoria que exija
> interpretação sem suporte direto; (5) registrar **ausências** (entidades que o
> Kernel prediz e que não aparecem).

> **Importância deste experimento (não é uma lente imposta):** os SX-001 e SX-002
> observaram **casos de crise/falha**. Este caso (Genoma Humano) é classificado
> nas fontes como **sucesso** — conforme o [00-pre-registro.md](../00-pre-registro.md).
> A pergunta é exatamente a mesma: **as entidades do Kernel emergem dos fatos?**
> A resposta, seja qual for (emergem, não emergem, surgem diferenças), é o dado.

---

## 0. Declaração de cegueira

Esta reconstrução foi produzida **antes** de reler a Narrativa Original. As
entidades abaixo foram reconhecidas a partir dos **50 Atomic Facts** e do Kernel.
Onde o rótulo ECP não era claramente suportado pelos fatos, foi marcado como
**inferido** — e **não conta** como emergência espontânea.

> **Limitação de execução (registrada):** reconstrução e narrativa foram
> produzidas pelo mesmo executor, sob o pipeline congelado. A separação ideal
> (Pessoa A reconstrói, Pessoa B compara) permanece não aplicada nesta sessão.
> Para mitigar, a reconstrução cita **apenas** `AF-###`, nunca a narrativa. A
> limitação é registrada em [METHODOLOGICAL-DEBT.md](../../METHODOLOGICAL-DEBT.md).

## 1. Reconhecimento de entidades

### 1.1 Goal (Objetivo) — EMERGENTE

| Suporte | Fato |
|---|---|
| AF-005 / AF-006 | Comitê da NAS delineia objetivos — sequenciar o genoma humano e organismos selecionados. |
| AF-047 | O objetivo principal era gerar a primeira sequência do genoma humano. |
| AF-011 | Plano de concluir em ~15 anos (meta temporal). |

O **objetivo** emerge diretamente: produzir a primeira sequência do genoma
humano, com escopo (organismos), prazo (15 anos) e custo-projeção declarados.
Não exigiu interpretação.

### 1.2 Knowledge (Conhecimento) — EMERGENTE

| Suporte | Fato |
|---|---|
| AF-005 | Comitê NAS (1988) — base de conhecimento sobre o que era preciso sequenciar. |
| AF-010 | Organismos-alvo selecionados — conhecimento do estado da arte. |
| AF-018 / AF-019 | Quem financiava — ambiente institucional conhecido. |

Knowledge emerge: sabia-se **o que** sequenciar (AF-005, AF-010), **quem**
financiava (AF-018/019) e qual método existia (AF-018). Também há **lacuna de
conhecimento** inicial: a sequência humana **não existia** (AF-001 — objetivo
era *gerar* a primeira) — mas isso é implícito (o objetivo é produzir algo
ainda não existente).

### 1.3 Knowledge — Lacuna (o "não saber") — EMERGENTE (implícita na meta)

A lacuna central é **consequência da meta**: "gerar a primeira sequência"
(AF-047) pressupõe que ela **ainda não existia**. O Kernel ECP-006 prevê
classificar o que se sabe e o que não se sabe; aqui a lacuna é o próprio objeto
do projeto — o desconhecido era o genoma humano. Isto é suportado por AF-001 e
AF-047; marcado como **implícito**, mas estrutural.

### 1.4 Assumption (Suposição) — EMERGENTE

| Suporte | Fato |
|---|---|
| AF-011 | Tempo (prazo de ~15 anos) era adequado, com a experiência da época. |
| AF-023 | A Celera afirmava que conseguiria ser mais rápida e barata — uma suposição/afirmação da era. |

Suposição emergente forte: **A-1** — *"a sequência do genoma humano podia ser
concluída com a tecnologia e o financiamento previstos"* (AF-011, AF-012).
Bem como **A-2**, partilhada pelo lado privado: *"o whole-genome shotgun seria
suficiente e mais barato/rápido"* (AF-023/024). Essas são suposições **declaradas
por agentes** (plano, anúncio privado) — mais explícitas que nos casos de
crise.

### 1.5 Evidence (Evidência) — EMERGENTE

| Suporte | Fato |
|---|---|
| AF-036 | Anúncio do draft (jun/2000) — evidência de resultado intermediário. |
| AF-037 | Cobertura de 90% — evidência de quantidade/completeza. |
| AF-038 | 150.000 gaps — evidência de limitação. |
| AF-039 / AF-040 | Publicação Nature e Science (2001) — evidência formalizada e revisada |
| AF-041..044 | Anúncio de conclusão (abr/2003): 92%, <400 gaps, mais preciso — evidência final |
| AF-049 / AF-050 | Registros sobre superação de metas e ganhos econômicos — evidência de efeito |

Evidence emerge em estágios: **draft** → **publicação revisada** → **conclusão**
→ **efeito**. Não precisou interpretar.

### 1.6 Decision (Decisão) — EMERGENTE (cadeia de decisões)

| Suporte | Fato |
|---|---|
| AF-005 | DECISÃO: comitê NAS define os objetivos (1988). |
| AF-007 / AF-008 | DECISÃO: NIH cria/renomeia office (1988/1990/1997). |
| AF-018 / AF-019 | DECISÃO de financiamento público (EUA) + Wellcome. |
| AF-027 / AF-028 | DECISÃO: Bermuda Principles — compartilhar dados rapidamente (1996). |
| AF-032 / AF-034 | DECISÃO: criar programa ELSI (1990) — ética. |
| AF-039 / AF-040 | DECISÃO: publicar em revisadas (natureza dos marcos). |
| AF-041 | DECISÃO: anunciar conclusão (abr/2003). |

A cadeia de decisões emerge: **definir metas → instituir o projeto → nomear e
financiar → escolher compartilhar dados → escolher tratar ética → publicar →
concluir**. As decisões são **identificáveis nos fatos** — são artefatos
explicitos do registro público.

### 1.7 Execution (Execução) — EMERGENTE

| Suporte | Fato |
|---|---|
| AF-014 | 20 centros / AF-015 / 6 países — organização da execução. |
| AF-021 / AF-024 | Interação com a Celera (execução concorrente). |
| AF-036 → AF-041 | Sequência de execução: draft (2000) → publicação (2001) → conclusão (2003). |

Execução emerge como **processo**: a ordem cronológica dos fatos (AF-036
2000; AF-039/040 2001; AF-041 2003) estrutura uma execução em fases.

### 1.8 Validation (Validação) — EMERGENTE

| Suporte | Fato |
|---|---|
| AF-039 / AF-040 | Revisão de pares (Nature, Science) — validação por especialista. |
| AF-042 / AF-043 / AF-044 | Métricas de completeza (92%, gaps<400, mais preciso) — validação contra metas. |
| AF-048 / AF-049 | Fontes registram superação dos objetivos — validação do resultado. |

Validation é forte: as fontes registram que o HGP **superou metas** (AF-048),
fez além do possível em 1988 (AF-049). É uma validação **explícita e
quantificada**.

### 1.9 Demais entidades (Jogo, aprendizado, risco, problema-formal)

- **Risk (Risco):** ECP prevê impacto × probabilidade. Aqui há **matéria-prima**:
  US$ 3 bi (AF-012), incerteza técnica (AF-023 sobre viabilidade da Celera),
  riscos efeitos sociais (AF-033: seguros/emprego). Mas **nenhum fato** mostra
  uma **declaração formal de cálculo de risco** para a decisão de começar. O
  medo etico (AF-032/033) foi tratado com o programa ELSI — uma **resposta
  estruturada** ao risco social, mas não um artefato "risco=impact×prob".
  → **Risk formal não emerge; há resposta a risco (governança ética)**.
- **Problem definido (formal):** nos casos de crise o problema era pós-hoc.
Aqui há o **oposto**: o problema ("não temos a sequência") foi **definido
ex-ante** com metas (AF-005/006). O Problem **emerge de forma estruturada
desde o início** — ao contrário dos casos de crise.
- **Learning:** parcial. As fontes registram a validação do resultado
  (AF-048/049) e a continuidade da biomedicina (AF-031, AF-050). Sem suporte
  direto para além da validação (o "aprendizado" explícito é AF-037/038, nas
  lições do draft: cobertura 90% e gaps).

## 2. A cadeia reconstruída

```
Problem explícito ex-ante (AF-005/006 — "não temos a sequência")
   ↓
Goal (AF-047 — gerar a primeira sequência; AF-011 — prazo 15 anos; custo AF-012)
   ↓
Knowledge (AF-010/018/019 — o que/ quem sabe)  +  Lacuna conhecida (AF-001/047)
   ↓
Assumption (A-1 AF-011/012 — factível no prazo; A-2 AF-023/024 — viabilidade da abordagem)
   ↓
Decision (AF-005, AF-008, AF-027, AF-034, AF-039, AF-041 — começar, financiar, compartilhar, publicar, concluir)
   ↓
Execution (AF-014/015, AF-017; marcos AF-036 2000 → AF-039/040 2001 → AF-041 2003)
   ↓
Evidence de resultado (AF-036/037/038 — draft 90%; AF-042/043/044 — conclusão 92%, <400, mais preciso)
   ↓
Validation (AF-039/040 — peer review; AF-042..044 — métricas; AF-048/049 — superação de metas)
   ↓
Learning/O efeito (AF-050 — avanços econômicos; AF-010 — avanço biomédico)
```

**Observação central:** ao contrário dos casos de crise, onde a cadeia começava
**numa lacuna de conhecimento e respondia tarde**, aqui a cadeia começa **definida
desde o início** (Goal e Problem artefato ex-ante), as decisões formais
**antecedem** os marcos de evidência (decisão 1990/1996 → evidência 2000/2003),
e a validação é **quantificada e bem sucedida**. A ordem é: definir → decidir →
executar → medir → validar → aprender.

## 3. Ausências (negative evidence)

| Entidade | Status nos fatos | Leitura |
|---|---|---|
| **Risk formal calculado (impacto×probabilidade)** | Não aparece | Há matéria-prima (AF-012 custo; AF-032/033 riscos sociais), mas nenhum fato mostra um cálculo de risco explícito que tenha *antecedido* a decisão de iniciar. |
| **Origem causal única** | — | (não se aplica; múltiplas origens confirmadas — ver 00-fontes) |
| **Hypothesis/hesitação dramática** | Não aparece como crise | Não há uma "crise" de viabilidade registrada como decisão agonizante; as decisões são registradas como executadas. Há tensão com a Celera (AF-026) mas não aparece como crise de viabilidade. |
| **Cálculo de risco financeiro documentado em decisão** | Não aparece | AF-012 (custo projetado) existe; um argumento de risco/retorno documentado não aparece entre os fatos de decisão. |

> Estas ausências são **dados**: mesmo num caso de sucesso, o Kernel prevê que
> uma empreitada grande teria Risk formalizado e um processo de decisão que
> levasse em conta risco. Nos fatos, o risco social (ético) foi tratado por
> governança (ELSI, AF-034) — o artefato "Risk" do Kernel **não emerge**, mas não
> como uma falha: foi uma resposta institucional estruturada.

Comparação de ausências **com os casos de crise (SX-001/SX-002)**:

| Caso | Problem ex-ante | Risk formal | Project/scale | Decisions |
|---|---|---|---|---|
| SX-001 (crise) | Ausente | Ausente | Ausente | Decision sem evidência |
| SX-002 (crise) | Ausente | Ausente | Ausente | Decision tardia |
| **SX-003 (sucesso)** | **PRESENTE (AF-005/006)** | Ausente (risco tratado por governança) | **PRESENTE (AF-011 prazo)** | Decision antecede os marcos |

> **Observação pré-verificada (a confirmar na Etapa 4):** aqui a **presença** é
> o dado divergente dos casos de crise: nos dois casos anteriores, Problem e
> projeção eram **ausentes**; no Genoma **são presentes** (definidos ex-ante). A
> predição inversa (SIG-002) previa que, em casos de sucesso, essas
> entidades **estariam presentes** — é o que os fatos mostram. (Ver Etapa 4.)

## 4. O que a reconstrução NÃO conseguiu (limites)

- **Não reconstruiu a biologia interna** do processamento (mecanismo técnico
  completo de sequenciamento shotgun vs clone-by-clone) — exigiria ciência que
  os AFs não contêm.
- **Não reconstruiu o processo decisório interno** (como exatamente as decisões
  foram tomadas no comitê/consórcio) — os AFs mostram as decisões como artefatos,
  não o porquê interno.
- **Não reconstruiu a tensão pública×privada em profundidade** (quanto impacto
  a Celera teve) — os fatos a registram (AF-026) sem quantificá-la.

## 5. Resumo da Etapa 3

| Entidade | Emergência | Suporte |
|---|---|---|
| Goal | **Emergente** | AF-005/006, AF-047, AF-011 |
| Problem ex-ante | **Emergente** (declarado) | AF-005/006 |
| Lacuna de conhecimento | Emergente (implícita) | AF-001, AF-047 |
| Knowledge | **Emergente** | AF-007/010/018/019 |
| Assumption (A-1/A-2) | Emergente (declarada) | AF-011/012, AF-023/024 |
| Decision (cadeia) | **Emergente** | AF-005, AF-008, AF-027/028, AF-034, AF-039/040, AF-041 |
| Execution | **Emergente** | AF-014/015, AF-036…AF-041 |
| Evidence | **Emergente** | AF-036/037, AF-039..044 |
| Validation | **Emergente** | AF-039/040, AF-042..044, AF-048/049 |
| Risk formal | Não emerge (governança em vez de cálculo) | AF-012, AF-032/034 |
| Learning | Parcial | AF-010, AF-050 |

**Leitura-chave diferente dos casos de crise:** a cadeia completa do Kernel
emerge **sem rupturas de decisão** e, sobretudo, **Goal/projeção estão presentes
ex-ante**. Isto é um **contra-controle aos casos de crise** — exatamente o que
o SX-003 foi escolhido para testar (DEBT-009), mas **a reconstrução não força
a conclusão**: apenas registra a presença como dado, sem forçar a visada.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-09 | Reconstrução cega a partir dos 50 Atomic Facts + Kernel. Emergência plena da cadeia Goal→…→Validation com Goal/Problem presentes ex-ante; Risk formal ausente (governança ética no lugar). Verificação de "presença" como dado (DE-002). |