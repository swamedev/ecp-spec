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