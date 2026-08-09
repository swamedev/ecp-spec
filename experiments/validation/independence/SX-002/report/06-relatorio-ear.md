# SX-002 / report — Etapa 6: EAR e Conclusão

| Campo | Valor |
|---|---|
| **Experimento** | EXP-SX002 |
| **Etapa** | 6 — Relatório final |
| **Método** | EAR — Engineering Alignment Rate |
| **Data** | 2026-08-04 |

> Este é o relatório **do experimento** — todo o conteúdo pertence ao EXP-SX002,
> não ao framework.

---

## 1. EAR — Engineering Alignment Rate (observação experimental)

**Fórmula:** `EAR(experimento) = itens corretamente reconstruídos / itens avaliados`

> **Nota de escopo (coordenação 2026-08-03):** o EAR é **observação experimental**,
> nunca conclusão. A calibração pertence ao
> [P-0008 — Cross-Domain Validation](../../../P-0008-CROSS-DOMAIN-VALIDATION.md).
> Escreve-se sempre com escopo explícito: **`EAR(Ebola)`**.

Onde:
- **Itens avaliados** = elementos comparáveis entre Narrativa × Reconstrução
  (tabela da [Etapa 4](../comparison/04-alignment-analysis.md)).
- **Corretamente reconstruídos** = `MATCH` + `PARTIAL_MATCH` (parcial conta 1/2).

| Categoria | Contagem | Peso |
|---|---|---|
| MATCH | 19 | ×1 |
| PARTIAL_MATCH | 3 | ×0.5 |
| NOT_EXPLAINED | 3 | ×0 |
| NEW_INSIGHT | 2 | (bônus, ver §3) |
| **Total avaliado** | **25** | — |

### Cálculo (núcleo)

```
corretamente_reconstruidos = 19 + 3×0.5 = 20.5
itens_avaliados             = 19 + 3 + 3 = 25

EAR(Ebola) = 20.5 / 25 = 0.82  (82%)
```

> Os 2 NEW_INSIGHT são **bônus** (não alteram o denominador). Se contados como
> "explicado além", o desempenho seria 22.5/25 = 90%.

> **Status epistemológico:** `EAR(Ebola) = 0.82` é **um dado em um caso**.

## 2. Leitura do EAR(Ebola)

- **82%** do caso Ebola WA (2014–2016) foi **reconstruído corretamente** a
  partir apenas dos fatos + Kernel, sem o vocabulário ECP na coleta e sem
  consultar a narrativa histórica.
- **12% não explicado** (3/25): o contexto de origem (local, sintomas), os
  rituais funerários como entidade e os fatores estruturais (sistemas frágeis,
  medo/desconfiança). Nenhum desses é causal para a estrutura da resposta.
- **Zero invenção** (falso positivo zero): tudo o que a reconstrução afirmou
  tinha suporte factual.

> **Cautela metodológica (obrigatória):** `EAR(Ebola)` é uma **observação**, não
> uma conclusão nem métrica calibrada. Mesmo executor, um único caso, denominador
> definido na Etapa 4 (não pré-registrado). A comparação cross-domínio é o
> [P-0008 — Cross-Domain Validation](../../../P-0008-CROSS-DOMAIN-VALIDATION.md).

## 3. Veredito do experimento

### 3.1 Emergência espontânea — RESPOSTA AFIRMATIVA

As entidades centrais do ECP **emergiram** dos fatos do caso Ebola, um evento
que nunca usou o protocolo:

| Entidade | Emergência |
|---|---|
| Lacuna inicial (agente não identificado) | Emergente |
| Goal (coordenação + estados finais) | Emergente |
| Knowledge (transmissão, agente) | Emergente |
| Evidence (detecção e resultado) | Emergente |
| Decision (cadeia de 6) | Emergente |
| Cadeia até Validation/Learning | Emergente |
| Assumption (A-1) | Inferida (não conta como emergência plena) |
| Problem formal / Risk calculado | Não emergiram (ausências) |

**Resposta à pergunta do SX-002:** quanto da resposta à epidemia de Ebola WA o
ECP explica sem conhecer a explicação oficial? → **`EAR(Ebola)` = 82%**,
incluindo o achado central (a defasagem entre o alerta e a coordenação formal).

### 3.2 O achado central (NEW_INSIGHT)

A reconstrução cega localizou **a defasagem (lag) alerta → coordenação**: as
evidências e os alertas existiam (notificação AF-005, identificação AF-006,
alertas da MSF AF-016) **antes** da decisão formal, mas a coordenação
(PHEIC AF-020, UNMEER AF-021) veio **tarde demais** — o pico (AF-030) foi
atingido e o declínio (AF-034/035) **só ocorreu após a expansão** da resposta.

> **Isto converge com o veredito independente dos painéis** (AF-044 — "resposta
> internacional tardia"), **produzido pela reconstrução sem consultar nenhum
> relatório final.**

### 3.3 Divergência com o SX-001 — registrada como dado

- **Challenger** (SX-001): decisão (lançar) **sem** evidência suficiente → falha
  no elo `Evidence → Decision`.
- **Ebola** (SX-002): decisão **com** evidência disponível, porém **tardia** →
  falha temporal (lag).

A cadeia do Kernel (Goal→Knowledge→…→Decision→…) **emergiu em ambos**, mas a
**forma da falha difere**. Isto é um resultado positivo do ponto de vista da
teoria: a estrutura prevê o esqueleto; o contexto define o modo de falha. **Não**
foi procurar uma divergência — foi o que os dados mostraram.

### 3.4 Ausência como explicação

Assim como no SX-001, o ECP explicou o que **faltava**: Problema definido
formalmente antes da resposta, cálculo de risco explícito, projeção de
escala/capacidade e metas mensuráveis pré-declaradas — todos **ausentes** nos
fatos. A ausência é coerente com a lentidão registrada (AF-018).

## 4. Consequência para a rede de Inferência Científica

| Signal | Efeito do SX-002 |
|---|---|
| **SIG-001** (decisão justificável requer conhecimento) | 2ª ocorrência causalmente independente (Ebola). **RA-SIG-001 satisfeita.** Afirmação refinada: conhecimento também deve ser usado a tempo. |
| **SIG-002** (ausência observável) | **RA-SIG-001 satisfeita** (2 ocorrências: Challenger, Ebola). Ressalva amostral (ambos casos de crise). |
| **SIG-003** (emergência da cadeia sem vocabulário ECP) | **RA-SIG-001 satisfeita** (2 ocorrências, domínios distintos). |
| **SIG-004** (defasagem alerta→coordenação) | Candidato novo (1 ocorrência). Não admissível ainda. |

Nenhuma promoção a `pattern` (RA-SIG-005). Consolidação v1.1 — fora do escopo.

## 5. Limitações registradas (para o método, não corrigidas agora)

1. **Mesmo executor na narrativa e na reconstrução** — a blindagem ideal não é
   aplicada. Mitigado pelo uso exclusivo de `AF-###` na reconstrução.
2. **EAR com denominador definido post hoc** — lista de 25 itens construída na
   Etapa 4; risco de viés de seleção.
3. **Atomic Facts como camada intermediária** — mantida do SX-001; se confirmar
   valor, formalizar na v1.1.
4. **Dois casos** — melhora, mas ainda insuficiente para calibração.
5. **Fontes históricas públicas** — a dependência da memória documental pública
   (WHO/MSF/painéis) limita a independência formal em relação ao pesquisador;
   atenuado pela verificação de acessibilidade e proveniência (Etapa 0).

> Limitações registradas em
> [METHODOLOGICAL-DEBT.md](../../../METHODOLOGICAL-DEBT.md) — **sem alterar** a
> especificação durante o experimento.

## 6. Conclusão final

> **Observação do experimento:** o ECP reconstruiu **82%** da resposta à epidemia
> de Ebola na África Ocidental a partir apenas dos fatos e do Kernel — incluindo
> a defasagem alerta→coordenação, a cadeia emergente e as ausências — sem usar o
> vocabulário ECP na coleta e sem inventar nada.

Diferente do SX-001 (falha por falta de evidência), o SX-002 (falha por decisão
tardia com evidência presente) **reproduz a mesma estrutura** e revela um segundo
mecanismo de falha. Juntos, os dois casos de origens independentes fornecem a
**primeira satisfação de RA-SIG-001** para 3 signals da rede de Inferência
Científica.

> **Ressalva de coordenação:** os dois casos **não** calibram métrica nem
> estabelecem universalidade. A pergunta decisiva permanece cross-domain
> ([P-0008 — Cross-Domain Validation](../../../P-0008-CROSS-DOMAIN-VALIDATION.md)),
> e o próximo passo é incluir domínios não ligados a respostas a crise
> (product engineering, sucesso, operação de longo prazo). **Nenhuma lei é
> escrita agora** ([DISCOVERY-LOG](../../../DISCOVERY-LOG.md)).

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-04 | Relatório final do EXP-SX002. **EAR = 0.82**. Veredito afirmativo de emergência espontânea. Achado: lag alerta→coordenação (NI-002). Ra-SIG-001 satisfeito para 3 signals (2ª ocorrência independente). Limitações 1–5 registradas. |