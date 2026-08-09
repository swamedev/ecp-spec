# METHODOLOGICAL-DEBT — Dívida Metodológica (v1.1)

| Campo | Valor |
|---|---|
| **Tipo** | Registro de limitações (não-RFC, não-AD, não-lei) |
| **Status** | Ativo — aberto pela FASE C1 (coordenação 2026-08-03) |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe |
| **Governado por** | [ROADMAP — Fase C1 → C2](../ROADMAP.md), [P-0007](./P-0007-INDEPENDENCE.md) |

## Proposito

Na Fase C2 (Evidence Production), a infraestrutura metodológica está
**congelada**. Qualquer limitação descoberta **durante o SX-001** é registrada
aqui, para a **v1.1** — **nunca** corrigida no meio do experimento.

> Este é exatamente o procedimento da ciência experimental: o experimento corre
> sob um protocolo fixo; as lições são adiadas para a próxima revisão.

## Regras

- Registra-se **limitação**, não correção.
- Cada item só é corrigido **depois** do fim do SX-001 (v1.1).
- Durante o SX-001, itens aqui **não** alteram a execução.

## Itens

### DEBT-001 — Mesmo executor na narrativa e na reconstrução (SX-001)

- **Fonte:** [SX-001/reconstruction](../independence/SX-001/reconstruction/03-reconstrucao-cega.md), §0.
- **Limitação:** a blindagem ideal do pipeline — Pessoa A reconstrói, Pessoa B
  compara — não pôde ser aplicada; narrativa e reconstrução foram produzidas
  pelo mesmo executor.
- **Mitigação usada no experimento:** reconstrução cita **apenas** Atomic Facts
  (`AF-###`), nunca a narrativa; entidades inferidas são marcadas como tais.
- **V1.1:** exigir avaliador independente para a Reconstrução Cega (ou ao menos
  para o Alignment Analysis) quando o executor da coleta for o mesmo.

### DEBT-002 — EAR com denominador definido post hoc (SX-001)

- **Fonte:** [SX-001/report](../independence/SX-001/report/06-relatorio-ear.md), §5.2.
- **Limitação:** a lista de 20 itens comparáveis (Narrativa × Reconstrução) foi
  construída na Etapa 4, sem regra pré-registrada de contagem. Risco de viés de
  seleção do denominador.
- **V1.1:** pré-registrar a unidade de contagem do EAR (ex.: por entidade do
  Kernel, por elemento de narrativa) antes do SX-002.

### DEBT-003 — Camada Atomic Facts não prevista no pipeline formal (SX-001)

- **Fonte:** coordenação 2026-08-03; [SX-001/README](../independence/SX-001/README.md).
- **Limitação:** a camada intermediária `Narrativa → Atomic Facts → Reconstrução`
  foi aplicada **dentro** do experimento, mas o pipeline formal
  ([SHADOW-EXPERIMENTS](../independence/SHADOW-EXPERIMENTS.md)) não a previa.
- **Veredito preliminar do experimento:** a camada aumentou a força (reduz a
  carga de interpretação implícita entre narrativa e reconstrução).
- **V1.1:** formalizar a etapa Atomic Facts no pipeline de shadow experiments,
  se a avaliação confirmar o valor.

### DEBT-004 — SX-001 é um caso único (generalização limitada)

- **Fonte:** [SX-001/report](../independence/SX-001/report/06-relatorio-ear.md), §5.4.
- **Limitação:** um único experimento não estabelece padrão; a emergência
  espontânea precisa de replicação (SX-002, SX-003, …) para virar Pattern.
- **V1.1:** nada a corrigir — apenas registrar que a promoção de SIG-003 (e a
  consolidação de SIG-001) depende de novas ocorrências independentes.

### DEBT-005 — Confiança do SIG-001 estimada, não derivada (SX-001)

- **Fonte:** [SX-001/signals](../independence/SX-001/signals/05-signals.yaml).
- **Limitação:** a elevação de confiança 0.6 → 0.75 do SIG-001 com a primeira
  ocorrência externa é **estimada**, não calculada por fórmula registrada
  (RA-SIG-001 ainda não satisfeita: faltam ≥2 ocorrências independentes).
- **V1.1:** definir a regra de derivação de confiança por ocorrência antes de
  consolidar os Signals.

### DEBT-006 — Mesmo executor na narrativa e na reconstrução (reincidência SX-002)

- **Fonte:** [SX-002/03-reconstrucao-cega](../independence/SX-002/reconstruction/03-reconstrucao-cega.md), §0.
- **Limitação:** o mesmo padrão do DEBT-001 **reincidiu** no SX-002: narrativa e
  reconstrução foram produzidas pelo mesmo executor; a blindagem ideal (Pessoa A
  reconstrói, Pessoa B compara) não foi aplicada.
- **Mitigação usada no experimento:** reconstrução cita **apenas** Atomic Facts
  (`AF-###`), nunca a narrativa; entidades inferidas são marcadas como tais.
- **V1.1:** o item DEBT-001 já exigia avaliador independente; permanece sem
  correção aplicada. Reforça a obrigatoriedade para o SX-003+.

### DEBT-007 — EAR com denominador definido post hoc (reincidência SX-002)

- **Fonte:** [SX-002/alignment](../independence/SX-002/comparison/04-alignment-analysis.md);
  [SX-002/report](../independence/SX-002/report/06-relatorio-ear.md), §1.
- **Limitação:** a lista de 25 itens comparáveis (Narrativa × Reconstrução) foi
  construída na Etapa 4 do SX-002, sem regra pré-registrada de contagem — o item
  DEBT-002 permaneceu aberto e a reincidência ocorreu.
- **Consequência metodológica (registrada, não comparada):** como cada
  experimento define seu próprio denominador (20 no SX-001; 25 no SX-002), o EAR
  **não** é uma métrica calibrada e os valores **não** devem ser comparados
  quantitativamente entre experimentos enquanto essa unidade não for padronizada.
- **V1.1:** pré-registrar a unidade de contagem do EAR antes de cada experimento.

### DEBT-008 — Dependência de memória documental pública (SX-002)

- **Fonte:** [SX-002/sources](../independence/SX-002/sources/00-fontes.md);
  [SX-002/narrative](../independence/SX-002/narrative/01-narrativa-original.md).
- **Limitação:** datas, totais e sequência da resposta ao Ebola baseiam-se em
  corpus documental público (WHO Situation Reports, MSF, painéis de
  investigação); a verificação de acessibilidade (Etapa 0) confirma
  disponibilidade, **não** substitui a citação individual por fato. Há registro
  de leitura com base na memória do executor ao montar os fatos.
- **Mitigação usada:** proveniência preservada na Etapa 0; narrativa reduzida ao
  que as fontes registram; números ligados a valores documentados.
- **Observação metodológica (não é correção):** a numeração dos Atomic Facts e
  do cronograma segue as fontes citadas; não houve verificação de acesso a
  **cada** URL individual, apenas aos grupos principais.
- **V1.1:** exigir citação por fato com URL + data de acesso para cada Atomic
  Fact, e verificação individual de acessibilidade (não só por grupo).

### DEBT-009 — Amostra seletiva para casos de crise/falha (SX-001 e SX-002)

- **Fonte:** [SX-001/report](../independence/SX-001/report/06-relatorio-ear.md) §5.4;
  [SX-002/signals](../independence/SX-002/signals/05-signals.yaml).
- **Limitação:** os dois experimentos realizados usam casos de perda/crise
  (Challenger — falha física; Ebola — crise de resposta). A predição do Kernel
  sobre presença das entidades em projetos **bem-sucedidos** ainda **não foi
  testada** (é hipótese pendente, não resultado).
- **Consequência:** SIG-002 ("ausência observável") foi observado apenas na
  presença de ausência; a inferência inversa permanece **hipótese**, não
  conclusão.
- **V1.1:** incluir obrigatoriamente um caso de sucesso (domínio de operação
  estável) no rol de shadow experiments antes de consolidar SIG-002.

### DEBT-010 — Verificação de acessibilidade por grupo, não por URL individual (SX-002)

- **Fonte:** [SX-002/sources](../independence/SX-002/sources/00-fontes.md), §veredito.
- **Limitação:** a verificação de acessibilidade foi feita por **grupo de
  origens** (WHO, MSF, painéis, documentos nacionais), não para **cada URL**
  individual registrado na Etapa 0.
- **Consequência:** a disponibilidade de links específicos (ex.: um Situation
  Report de mês específico) pode variar sem impacto grande no traço, mas a
  reprodução por terceiros pode tropeçar em link ausente.
- **V1.1:** no passo de proveniência, checar cada URL e registrar estado de
  acesso por link (OK / archive / fora de ar), com data da verificação.

> **Nota final — classificação (registrada, não conclusão):** os itens
> DEBT-006..DEBT-010 são **dívidas metodológicas** (limitações registradas para a
> v1.1). Não são resultados, não são conclusões e não alteram o experimento. O
> EAR(Ebola)=0,82 preservado como resultado do experimento (EXP-SX002);
> nenhuma destas dívidas o promove a métrica oficial nem a compara
> quantitativamente com o EAR do SX-001 (0,775).

| Dívida | Categoria |
|---|---|
| DEBT-006 | Dívida metodológica |
| DEBT-007 | Dívida metodológica (resultado EAR(Ebola)=0,82 preservado) |
| DEBT-008 | Dívida metodológica |
| DEBT-009 | Dívida metodológica + hipótese pendente (não é conclusão) |
| DEBT-010 | Dívida metodológica |
| DEBT-001..DEBT-010 | Todas limitações; nenhum SIG promovido a Pattern nem a LAW-H; EAR não é métrica oficial |