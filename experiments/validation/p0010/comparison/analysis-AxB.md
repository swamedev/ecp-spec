# P-0010 — Fase 1: Comparação A × B

> Comparador: análise semântica humana estruturada (não automática).
> Referência de leitura: `input/evaluator-A.md` (46 AFs) × `input/evaluator-B.md` (75 AFs, rodada 2).
> Taxonomia: match / granularidade fina (B decompôs) / granularidade grossa (B agrupou) /
> exclusivo / divergência factual.

## 1. Mapeamento A → B (46 linhas)

| A | B | Classe | Observação |
|---|---|---|---|
| AF-001 | B-AF-011 | match | Semântica equivalente (A: "possibilidade de falha"; B: "falha potencialmente catastrófica"). |
| AF-002 | B-AF-012 | match | Igual. |
| AF-003 | B-AF-013 + B-AF-014 | granularidade fina | A agrupou temperatura + inspeção; B decompôs em 2. |
| AF-004 | B-AF-015 | match | Igual. |
| AF-005 | B-AF-016 | match | B nomeia o autor (Boisjoly). |
| AF-006 | B-AF-017 | match | B data "julho de 1985" (narrativa fornece o mês); A data "1985". |
| AF-007 | B-AF-001 + B-AF-002 + B-AF-003 | granularidade fina | A agrupou decolagem + 25º + 10º; B decompôs em 3. |
| AF-008 | B-AF-004 + B-AF-005 + B-AF-006 | granularidade fina | A agrupou os 3 objetivos; B decompôs em 3. |
| AF-009 | B-AF-007 | match | Ambos: 7 tripulantes com nomes; B inclui os cargos. |
| AF-010 | B-AF-008 | granularidade grossa | B agrupou desintegração em 73 s + óbito em 1 AF. |
| AF-011 | B-AF-008 | granularidade grossa | B agrupou óbito + desintegração; B também repete o óbito em B-AF-055 (ver §3). |
| AF-012 | B-AF-018 | match | Igual. |
| AF-013 | B-AF-019 | match | Igual. |
| AF-014 | B-AF-020 | match | Igual. |
| AF-015 | B-AF-047 + B-AF-048 + B-AF-045 | granularidade fina | B decompôs lançamento, motivo técnico e adiamento do gelo. **revisar**: causa do adiamento de 1 h (A: detecção de incêndio; B: gelo) — ambas constam da narrativa; não é conflito factual. |
| AF-016 | B-AF-021 | match | Ambos consolidam as 3 temperaturas em 1 AF. |
| AF-017 | B-AF-022 | match | B nomeia o organizador (Houston) e as sedes. |
| AF-018 | B-AF-024 | match | Igual. |
| AF-019 | B-AF-025 | match | Igual. |
| AF-020 | B-AF-026 | match | B mantém não-aceitação + pergunta sobre abril agrupadas, como A. |
| AF-021 | B-AF-027 | match | Igual. |
| AF-022 | B-AF-029 + B-AF-030 + B-AF-031 | granularidade fina | A agrupou mudança de posição + dados inconclusivos + recomendação de lançar; B decompôs em 3. |
| AF-023 | B-AF-032 | match | Igual. |
| AF-024 | B-AF-033 + B-AF-034 | granularidade fina | B decompôs exigência por escrito e assinatura/fax em 2. |
| AF-025 | B-AF-035 | match | Igual. |
| AF-026 | B-AF-037 | match | Igual (B data "madrugada de 28", coerente). |
| AF-027 | B-AF-038 + B-AF-039 | granularidade fina | B decompôs "registradas e não comunicadas" e "não era critério formal". |
| AF-028 | B-AF-040 + B-AF-041 | granularidade fina | B decompôs "gelo na torre" e "Rockwell insegura". |
| AF-029 | B-AF-043 | match | Igual na opinião dos engenheiros (B-AF-042 = consulta, é exclusivo B parcial). |
| AF-030 | B-AF-044 | match | Igual. |
| AF-031 | B-AF-047 | match | B agrupou decolagem + temperatura; A isolou a temperatura. |
| AF-032 | B-AF-049 | match | B detalha T+0,7 s e o O-ring primário. |
| AF-033 | B-AF-050 | match | Igual. |
| AF-034 | B-AF-051 | match | B detalha recorde + 3.000 m. |
| AF-035 | B-AF-052 | match | Igual (T+58 s). |
| AF-036 | B-AF-054 | match | B adiciona tempo de queda (2,5 min). |
| AF-037 | B-AF-058 | match | Ambos: causa = O-ring da junta traseira do SRB direito. |
| AF-038 | B-AF-056 | match | Ambos: criação da comissão, sem data (correto). |
| AF-039 | B-AF-059 | match | Igual (projeto defeituoso, fatores sensíveis). |
| AF-040 | B-AF-061 | match | Igual (informação incompleta/enganosa). |
| AF-041 | B-AF-065 | match | Igual (dados × julgamentos). |
| AF-042 | B-AF-066 | match | Igual (estrutura de gestão contornou gerentes-chave). |
| AF-043 | B-AF-067 | match | Igual (gravidade não transmitida nos níveis superiores). |
| AF-044 | B-AF-069 + B-AF-070 | granularidade fina | B decompôs "mudou posição contrariando engenheiros" e "acomodar cliente". |
| AF-045 | B-AF-071 | match | Igual. |
| AF-046 | B-AF-072 + B-AF-073 + B-AF-074 | granularidade fina | A agrupou suspensão + retomada + O-rings reprojetados; B decompôs em 3. |

## 2. Exclusivo A

Nenhum fato de A ficou sem correspondente em B (A ⊆ B em cobertura semântica).

## 3. Exclusivo B (presentes na narrativa, A não extraiu)

| B | Observação |
|---|---|
| B-AF-009 | Composição do veículo (nave + tanque + 2 SRBs, fabricante). |
| B-AF-010 | Montagem em segmentos, juntas de campo, dois O-rings. |
| B-AF-023 | Preocupação com elasticidade da borracha no frio. |
| B-AF-028 | Intervalo para reunião privada da Thiokol. |
| B-AF-036 | Mulloy e Aldrich prosseguiram. |
| B-AF-042 | Aldrich consultou engenheiros do Kennedy/JSC (parcial: A só registra a opinião, AF-029). |
| B-AF-045 | Adiamento de 1 h para o gelo derreter (parcial: A funde no AF-015). |
| B-AF-046 | Inspeção às T−20 indicou gelo derretendo. |
| B-AF-053 | Altitude/posição da desintegração (46.000 pés, 14 km, Atlântico). |
| B-AF-055 | Óbito dos sete em T+73 s — **redundância interna de B** com B-AF-008. |
| B-AF-057 | Entrega do relatório em 6/6/1986. |
| B-AF-060 | Conclusão de que o processo de lançamento foi falho. |
| B-AF-062/063/064 | Três ignorâncias dos responsáveis (história dos O-rings, recomendação escrita, oposição dos engenheiros). |
| B-AF-068 | Nível mais alto da revisão em silêncio. |
| B-AF-075 | Criação do Office of Safety, Reliability and Quality Assurance. |

Total: 16 exclusivos B, dos quais 1 redundância interna (B-AF-055) e 2 parciais (B-AF-042, B-AF-045).

## 4. Tabela de trabalho (contagens)

| Tipo | Contagem |
|---|---|
| Match (1:1 semântico) | 34 |
| Granularidade fina (B decompôs) | 10 |
| Granularidade grossa (B agrupou) | 2 |
| Divergência factual | 0 |
| Exclusivo A | 0 |
| Exclusivo B | 16 |
| A revisar | 1 (A-AF-015) |

## 5. Leitura provisória (hipótese, a confirmar nas fases 2 e 3)

- A cobertura de A está **contida** na de B (exclusivo A = 0). A variabilidade é de
  **decomposição**: B decompõe acontecimentos que A consolida (10 de 46 linhas de A).
- 34/46 linhas de A (≈74%) têm correspondência 1:1 em B.
- Zero divergência factual entre A e B até aqui.
- A fonte dominante de diferença é o grau de decomposição, coerente com a hipótese
  de que ~90% da variabilidade será de granularidade.

> Nota de método: a classificação acima é rastreável AF a AF e revisável pelo
> comparador humano antes do cálculo do AFR.
