# SX-003 / report — Etapa 6: EAR e Conclusão

| Campo | Valor |
|---|---|
| **Experimento** | EXP-SX003 |
| **Etapa** | 6 — Relatório final |
| **Método** | EAR — Engineering Alignment Rate |
| **Data** | 2026-08-09 |

> Este é o relatório **do experimento** — todo o conteúdo pertence ao EXP-SX003,
> não ao framework.

---

## 1. EAR — Engineering Alignment Rate (observação experimental)

**Fórmula:** `EAR(experimento) = itens corretamente reconstruídos / itens avaliados`

> **Nota de escopo (coordenação 2026-08-03):** o EAR é **observação experimental**,
> nunca conclusão. A calibração pertence ao
> [P-0008 — Cross-Domain Validation](../../../P-0008-CROSS-DOMAIN-VALIDATION.md).
> Escreve-se sempre com escopo explícito: **`EAR(Genoma)`**.

Onde:
- **Itens avaliados** = elementos comparáveis entre Narrativa × Reconstrução
  (tabela da [Etapa 4](../comparison/04-alignment-analysis.md)).
- **Corretamente reconstruídos** = `MATCH` + `PARTIAL_MATCH` (parcial conta 1/2).

| Categoria | Contagem | Peso |
|---|---|---|
| MATCH | 15 | ×1 |
| PARTIAL_MATCH | 7 | ×0.5 |
| NOT_EXPLAINED | 2 | ×0 |
| NEW_INSIGHT | 2 | (bônus, ver §3) |
| **Total avaliado** | **24** | — |

### Cálculo (núcleo)

```
corretamente_reconstruidos = 15 + 7×0.5 = 18.5
itens_avaliados             = 15 + 7 + 2 = 24

EAR(Genoma) = 18.5 / 24 = 0.77  (77%)
```

> Os 2 NEW_INSIGHT são **bônus** (não alteram o denominador). Se contados como
> "explicado além", o desempenho seria 20.5/24 = 85%.

> **Status epistemológico:** `EAR(Genoma) = 0.77` é **um dado em um caso**.

> **Cautela metodológica (DEBT-007 — reincidência):** o denominador (24 itens) foi
> definido **na Etapa 4**, não pré-registrado. Isso é uma limitação metodológica
> conhecida, registrada em [METHODOLOGICAL-DEBT.md](../../../METHODOLOGICAL-DEBT.md);
> não se compara este EAR diretamente com SX-001/SX-002 fora da revisão
> pós-experimento (a comparação **é da coordenação**, não desta etapa).

## 2. Leitura do EAR(Genoma)

- **77%** do caso Genoma Humano (1990–2003) foi **reconstruído corretamente**
  a partir apenas dos fatos + Kernel, sem o vocabulário ECP na coleta e sem
  consultar a narrativa histórica.
- **~8% não explicado** (2/24): atualização de planos estratégicos e o evento
  T2T (fora do período). Nada que seja causal para a estrutura do projeto.
- **Zero invenção** (falso positivo zero): tudo o que a reconstrução afirmou
  tinha suporte factual.

## 3. Veredito do experimento

### 3.1 Emergência espontânea — RESPOSTA AFIRMATIVA (caso de sucesso)

As entidades centrais do ECP **emergiram** dos fatos do Projeto Genoma Humano,
um esforço (classificado pelas fontes como bem-sucedido) que nunca usou o
protocolo:

| Entidade | Emergência |
|---|---|
| Goal | Emergente (AF-005/006, AF-047, AF-011) |
| Problem ex-ante | Emergente (declarado — AF-005/006) |
| Knowledge + Lacuna | Emergente (AF-007/010/018; lacuna implícita AF-001/047) |
| Assumption (A-1/A-2) | Emergente (declarada — AF-011/012, AF-023/024) |
| Decision (cadeia) | Emergente |
| Execution | Emergente |
| Evidence | Emergente (draft → publicação → conclusão) |
| Validation | Emergente (peer review + métricas) |
| Risk formal | Não emerge (governança ética no lugar) |

**Resposta à pergunta do SX-003:** quanto do Projeto Genoma Humano o ECP explica
sem conhecer a explicação oficial? → **`EAR(Genoma)` = 77%**, incluindo o dado
adverso: **Goal/Problem presentes ex-ante** — ao contrário dos casos de crise.

### 3.2 O dado central (NEW_INSIGHT)

A reconstrução cega registrou que um grande empreendimento **de sucesso**:

1. **Tem Goal e Problem definidos desde o início** (AF-005/006, AF-047) e uma
   **projeção de prazo/custo** (AF-011/012) — **presentes**, ao contrário dos
   casos de crise (SX-001, SX-002), onde eram ausentes/pós-hoc.
2. **Não formaliza Risk** (impacto×probabilidade): o risco social foi tratado
   por **governança** (ELSI — AF-034), não por cálculo de risco.

> **Isto é um dado neutro de estrutura — não uma busca deliberada de divergência
> nem de convergência.** A reconstrução cega não consultou os casos anteriores
> (blindagem), e ainda assim evidenciou (a) presença ex-ante e (b) ausência
> persistente de Risk. A **interpretação** (o que isso significa para a teoria —
> predição inversa de SIG-002, DEBT-009) pertence à **revisão pós-experimento**,
> após o PARAR.

### 3.3 Sem força de conclusão

Este relatório **não** afirma que "presença ex-ante diferencia sucesso de
crise" como lei: é **um dado em um caso** (SX-003). A relação com os outros dois
casos é prerrogativa da coordenação na revisão pós-experimento, após o PARAR.
Nenhuma lei, Pattern ou RFC é criada nesta etapa.

## 4. Consequência para a rede de Inferência Científica (registro, não decisão)

| Signal | Efeito/registro do SX-003 (a confirmar na revisão) |
|---|---|
| **SIG-003** (cadeia emerge sem vocabulário ECP) | **3ª ocorrência causalmente independente** (Challenger, Ebola, **Genoma**). RA-SIG-001 satisfeita. Sem promoção. |
| **SIG-002** (ausência observável em crises) | Corolário: em sucesso as entidades **presentes** — apoiado pelo SX-003. Sem mudança de status nesta etapa. |
| **SIG-001** (decisão justificável requer conhecimento) | Não adiciona ocorrência aqui (caso sem falha de decisão). |
| **SIG-004** (lag alerta→coordenação) | Não adiciona ocorrência (o sucesso não tem lag). |
| **SIG-005** (presença ex-ante em sucesso) | Candidato novo (1 ocorrência). **Não admissível** (RA-SIG-001: ≥2). |

> Nenhuma promoção a `pattern` (RA-SIG-005). Tudo nesta seção é **registro**,
> não decisão — a decisão é pós-experimento.

## 5. Limitações registradas (para o método, não corrigidas agora)

1. **Mesmo executor na narrativa e na reconstrução** — blindagem ideal não
   aplicada. Mitigado pelo uso exclusivo de `AF-###` na reconstrução.
2. **EAR com denominador definido post hoc** — risco de viés; DEBT-007
   reincidente.
3. **Trajetória longa (1990–2003)** — a compressão em 50 facts é uma escolha;
   poderia haver mais/de outra forma.
4. **Fontes públicas institucionais** — NHGRI/DOE são as mesmas entidades do
   projeto; mitigada pela + ELI (multiplicidade de origens) e publicações
   revisadas. Limitação da independência formal total do observador.
5. **Single case de sucesso** — o "presença ex-ante" é dado de 1 caso; requer
   reprodução (OWS) antes de qualquer inferência.

> Limitações registradas em
> [METHODOLOGICAL-DEBT.md](../../../METHODOLOGICAL-DEBT.md) — **sem alterar** a
> especificação durante o experimento.

## 6. Conclusão final (decisão fica para a revisão)

> **Observação do experimento:** o ECP reconstruiu **77%** do Projeto Genoma
> Humano a partir apenas dos fatos e do Kernel — incluindo a cadeia emergente
> completa e, como dado novo, a **presença ex-ante de Goal/Problem** (contraste
> com os casos de crise) — sem usar o vocabulário ECP na coleta e sem inventar
> nada.

O SX-003, **primeiro caso de sucesso** do programa, alcançou o propósito do
pré-registro: oferecer um controle positivo para DEBT-009 (a amostra de crises).
Entretanto, **a interpretação — "presença ex-ante distingue sucesso" — NÃO é
feita agora**. Como ordenado no GO-2: **aqui o pipeline PARAR e a coordenação faz
a revisão pós-experimento antes de qualquer commit, concessão de Signals ou
análise transversal.**

> **Ressalva de coordenação:** EAR(Genoma)=0.77 e o dado de presença ex-ante são
> **observações**, não conclusões. Não se compara com SX-001/SX-002 fora da
> revisão pós-experimento. Nenhuma lei é escrita agora
> ([DISCOVERY-LOG](../../../DISCOVERY-LOG.md)).

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-09 | Relatório final do EXP-SX003. **EAR = 0.77**. Emergência afirmativa da cadeia no caso de sucesso. Dado central: Goal/Problem ex-ante presentes; Risk formal ausente (governança). **PARAR** autorizado — sem commit, sem interpretação transversal. |