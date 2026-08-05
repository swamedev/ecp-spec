# SX-001 / report — Etapa 6: EAR e Conclusão

| Campo | Valor |
|---|---|
| **Experimento** | EXP-SX001 |
| **Etapa** | 6 — Relatório final |
| **Método** | EAR — Engineering Alignment Rate |
| **Data** | 2026-08-03 |

> Este é o relatório **do experimento** — todo o conteúdo pertence ao EXP-SX001,
> não ao framework.

---

## 1. EAR — Engineering Alignment Rate (observação experimental)

**Fórmula:** `EAR(experimento) = itens corretamente reconstruídos / itens avaliados`

> **Nota de linguagem (coordenação 2026-08-03):** o EAR é uma **observação
> experimental**, não uma conclusão. Um único caso não calibra uma métrica —
> ainda não sabemos se 0.775 é excelente, comum, baixo, nem se varia por domínio.
> Por isso o EAR é escrito sempre com escopo explícito: **`EAR(Challenger)`**.
> A distribuição (e a calibração) é objetivo do [P-0008 — Cross-Domain Validation](../../../P-0008-CROSS-DOMAIN-VALIDATION.md).

Onde:
- **Itens avaliados** = elementos comparáveis entre Narrativa × Reconstrução
  (tabela da [Etapa 4](../comparison/04-alignment-analysis.md)).
- **Corretamente reconstruídos** = `MATCH` + `PARTIAL_MATCH` (parcial conta 1/2).

| Categoria | Contagem | Peso |
|---|---|---|
| MATCH | 14 | ×1 |
| PARTIAL_MATCH | 3 | ×0.5 |
| NOT_EXPLAINED | 3 | ×0 |
| NEW_INSIGHT | 2 | (bonus, ver §3) |
| **Total avaliado** | **20** | — |

### Cálculo (núcleo)

```
corretamente_reconstruidos = 14 + 3×0.5 = 15.5
itens_avaliados             = 14 + 3 + 3 = 20

EAR(Challenger) = 15.5 / 20 = 0.775  (77.5%)
```

> Os 2 NEW_INSIGHT são **bônus** (não alteram o denominador): explicam algo que
> a narrativa não dizia — não são itens a reproduzir, são excedentes de
> compreensão. Se contados como "explicado além", o desempenho é 17.5/20 = 87.5%.

> **Status epistemológico:** `EAR(Challenger) = 0.775` é **um dado em um caso**.
> Não é conclusão sobre o EAR, sobre o domínio Aeroespacial, nem sobre o ECP.

## 2. Leitura do EAR(Challenger)

- **77.5%** do caso Challenger foi **reconstruído corretamente** a partir apenas
  dos fatos + Kernel, sem uso do vocabulário ECP na coleta e sem consultar o
  relatório oficial.
- **15% não explicado** (3/20): a causa técnica exata (qual junta/O-ring), a
  motivação dos decisores e o processo interno da teleconferência.
- **Nenhuma invenção** (falso positivo zero): tudo o que a reconstrução
  afirmou tinha suporte factual.

> **Cautela metodológica (obrigatória):** `EAR(Challenger)` é uma **observação**,
> não uma conclusão nem uma métrica calibrada. Foi calculada com um único
> avaliador e um único caso. O denominador (20 itens) foi definido na Etapa 4
> pela comparação — não por uma regra pré-registrada de contagem. **Não sabemos
> se 0.775 é excelente, comum ou baixo** — isso exige distribuição
> (P-0008 — Cross-Domain Validation).

## 3. Veredito do experimento

### 3.1 Emergência espontânea — RESPOSTA AFIRMATIVA

As entidades centrais do ECP **emergiram** dos fatos do Challenger, um projeto
que nunca usou o protocolo:

| Entidade | Emergência |
|---|---|
| Goal | Emergente |
| Knowledge + lacuna | Emergente |
| Assumption | Emergente |
| Evidence | Emergente |
| Decision (cadeia de 6) | Emergente |
| Cadeia até Learning | Emergente |
| Problem / Risk | Não emergiram (ausências) |

**A resposta à pergunta do SX-001:** quanto do Challenger o ECP explica sem
conhecer a explicação oficial? → **`EAR(Challenger)` = 77.5%**, incluindo a
estrutura causal central e — o achado mais forte — o ponto exato da falha
(decisão sem evidência).

> **Importante:** este valor é uma observação de um caso. A pergunta "essa
> estrutura é universal?" pertence ao [P-0008 — Cross-Domain Validation](../../../P-0008-CROSS-DOMAIN-VALIDATION.md),
> e só pode ser respondida com vários domínios.

### 3.2 O achado central (NEW_INSIGHT)

A reconstrução cega localizou, sozinha, a **falha no elo `Evidence → Decision`**:
as decisões de lançamento foram autorizadas com base em suposições (A-1/A-2/A-3)
e **sem evidência suficiente** para o risco — exatamente a transição que a Lei
Zero (`L-0`) e o ECP-008 tornam obrigatória. A Rogers Commission chegou à mesma
conclusão por outro vocabulário ("informação incompleta e enganosa", "conflito
entre dados de engenharia e julgamento gerencial").

> **Isto é a convergência que o experimento buscava:** a estrutura que o ECP
> prediz foi **descoberta** no caso (não imposta), e coincidiu com o veredito da
> investigação histórica independente.

### 3.3 Ausência como explicação

O ECP explicou também o que **faltava**: Problem não declarado, Risk não
calculado, validação pré-decisão ausente, registro incompleto. Em um caso de
falha, o ECP não apenas vê as decisões erradas — vê a **infraestrutura cognitiva
ausente** que teria tornado a decisão segura.

## 4. Consequências para a rede de Inferência Científica

| Signal | Efeito do SX-001 |
|---|---|
| **SIG-001** (decisão justificável depende de conhecimento) | Ganhou a **1ª ocorrência causalmente independente** (Challenger). Confiança preliminar 0.6 → 0.75. Ainda não satisfaz RA-SIG-001 (faltam ≥2 independentes). |
| **SIG-002** (ausência observável) | Novo candidato (1 ocorrência). |
| **SIG-003** (emergência da cadeia sem vocabulário ECP) | Novo candidato (1 ocorrência). Sinal conceitualmente mais forte. |

Nenhuma promoção a `pattern` (RA-SIG-005). Consolidação adiada para a calibração
v1.1.

## 5. Limitações registradas (para o método, não corrigidas agora)

1. **Mesmo executor na narrativa e na reconstrução** — a blindagem ideal (Pessoa
   A reconstrói, Pessoa B compara) não foi aplicada. Mitigado pelo uso exclusivo
   de `AF-###` na reconstrução, mas a limitação permanece.
2. **EAR com denominador definido post hoc** — a lista de 20 itens foi construída
   na Etapa 4; não havia regra pré-registrada de contagem. Risco de viés de
   seleção.
3. **Atomic Facts como camada intermediária** — a introdução da camada
   `Narrativa → Atomic Facts → Reconstrução` foi uma melhoria aplicada **dentro**
   do experimento; o pipeline formal (SHADOW-EXPERIMENTS) não a previa. Se
   confirmar valor, deve ser formalizada na v1.1.
4. **Um único caso** — o SX-001 é um experimento; a generalização exige
   replicação (SX-002, SX-003, …).

> As limitações 1–4 são registradas em
> [METHODOLOGICAL-DEBT.md](../../../METHODOLOGICAL-DEBT.md) — **sem alterar** a
> especificação durante o experimento.

## 6. Conclusão final

> **Observação do experimento:** o ECP reconstruiu 77.5% do desastre do
> Challenger a partir apenas dos fatos e do Kernel — incluindo o elo exato da
> falha — sem depender do vocabulário ECP para coletar os dados, e sem inventar
> nada.

Esta é a primeira evidência externa e independente de que o Kernel descreve uma
**estrutura recorrente da engenharia** (a cadeia Goal → Knowledge → Lacuna →
Assumption → Evidence → Decision → …), e não apenas uma taxonomia criada pelo
próprio projeto. A teoria reconheceu os fenômenos onde eles já existiam — antes
de a explicação oficial ser consultada.

> **Ressalva de coordenação (2026-08-03):** o SX-001 é um **caso**. Ele não
> calibra a métrica nem estabelece universalidade. A pergunta decisiva passa a
> ser **cross-domain**: a mesma estrutura emerge espontaneamente em domínios
> radicalmente diferentes (Apollo 13, Deepwater Horizon, Hyatt Regency, Genoma
> Humano, Operation Warp Speed, …)? Isto é o escopo do
> [P-0008 — Cross-Domain Validation](../../../P-0008-CROSS-DOMAIN-VALIDATION.md).
> Nenhuma lei é escrita agora ([DISCOVERY-LOG](../../../DISCOVERY-LOG.md)).

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Relatório final do EXP-SX001. EAR = 0.775. Veredito afirmativo de emergência espontânea. NI-001 (elo Evidence→Decision) como achado central. 4 limitações registradas. |
| 1.1 | 2026-08-03 | EAR renomeado para **`EAR(Challenger)`** — observação experimental, não conclusão (coordenação 2026-08-03). Estatuto epistemológico explicitado; calibração adiada ao P-0008 (Cross-Domain Validation). |
