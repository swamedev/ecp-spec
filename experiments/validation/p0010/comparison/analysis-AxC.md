# P-0010 — Fase 2: Comparação A × C

> Comparador: análise semântica humana estruturada (não automática).
> Referência de leitura: `input/evaluator-A.md` (46 AFs) × `input/evaluator-C.md` (73 AFs).
> Taxonomia: match / granularidade fina (decompôs) / granularidade grossa (agrupou) /
> exclusivo / divergência factual.

## 1. Mapeamento A → C (46 linhas)

| A | C | Classe | Observação |
|---|---|---|---|
| AF-001 | C-AF-014 | match | Igual (1977, teste → falha nas vedações). |
| AF-002 | C-AF-015 | match | Igual (1985, erosão em quase todos os voos). |
| AF-003 | C-AF-016 + C-AF-017 | granularidade fina | C decompôs temperatura e inspeção em 2. |
| AF-004 | C-AF-018 | match | Igual. |
| AF-005 | C-AF-019 | match | Igual (C nomeia Boisjoly). |
| AF-006 | C-AF-020 | match | Igual. |
| AF-007 | C-AF-001 + C-AF-002 + C-AF-003 | granularidade fina | C decompõe decolagem, 25º e 10º em 3. |
| AF-008 | C-AF-004 + C-AF-005 + C-AF-006 | granularidade fina | C decompõe os 3 objetivos em 3. |
| AF-009 | C-AF-007 | match | Sete tripulantes com cargos. |
| AF-010 | C-AF-008 | granularidade grossa | C agrupa desintegração em 73 s + óbito em 1. |
| AF-011 | C-AF-008 | granularidade grossa | C agrupa óbito + desintegração; C também repete o óbito em C-AF-061 (ver §3). |
| AF-012 | C-AF-021 | match | Igual. |
| AF-013 | C-AF-022 | match | Igual. |
| AF-014 | C-AF-023 | match | Igual. |
| AF-015 | C-AF-053 + C-AF-054 + C-AF-051 | granularidade fina | C decompõe; **revisar** causa do adiamento de 1 h (idem A×B). |
| AF-016 | C-AF-024 + C-AF-025 + C-AF-026 | granularidade fina | C decompõe a previsão em 3 temperaturas — **difere de B**, que consolidou em 1 (Fase 3). |
| AF-017 | C-AF-027 | match | B identifique organizador e sedes. |
| AF-018 | C-AF-029 | match | Igual (sem dados < 53 °F). |
| AF-019 | C-AF-031 | match | Igual (Lund e Kilminster). |
| AF-020 | C-AF-032 + C-AF-033 | granularidade fina | C decompõe "não aceitava" e "pergunta sobre abril" — **difere de B**, que consolida. |
| AF-021 | C-AF-034 | match | Igual. |
| AF-022 | C-AF-036 + C-AF-037 + C-AF-038 | granularidade fina | C decompõe mudança, dados inconclusivos e recomendação em 3. |
| AF-023 | C-AF-039 | match | Igual. |
| AF-024 | C-AF-040 + C-AF-041 | granularidade fina | C decompõe exigência por escrito e fax em 2. |
| AF-025 | C-AF-042 | match | Igual. |
| AF-026 | C-AF-044 | match | Igual. |
| AF-027 | C-AF-045 + C-AF-046 | granularidade fina | C decompõe não-comunicadas e não-critério em 2. |
| AF-028 | C-AF-047 + C-AF-048 | granularidade fina | C decompõe gelo na torre e Rockwell em 2. |
| AF-029 | C-AF-049 | match | C inclui a consulta de Aldrich + a opinião. |
| AF-030 | C-AF-050 | match | Igual. |
| AF-031 | C-AF-053 | match | C agrupa decolagem + temperatura; A isolou. |
| AF-032 | C-AF-055 | match | Igual (T+0,7 s e O-ring primário). |
| AF-033 | C-AF-056 | match | Igual. |
| AF-034 | C-AF-057 | match | Igual (record + 3.000 m). |
| AF-035 | C-AF-058 | match | Igual (T+58 s). |
| AF-036 | C-AF-060 | match | C adiciona tempo de queda. |
| AF-037 | C-AF-063 | match | Igual (causa = O-ring fora traseira). |
| AF-038 | C-AF-062 | match | C agrupou criação + entrega do relatório (ver obs de data). |
| AF-039 | C-AF-064 | match | Igual. |
| AF-040 | C-AF-066 | match | C inclui as ignorâncias dentro do mesmo AF (conteúdo a mais, ver §3). |
| AF-041 | C-AF-067 | match | Igual. |
| AF-042 | C-AF-068 | match | Parte correspondente (estrutura de gestão). |
| AF-043 | C-AF-068 | match | Parte correspondente (gravidade). |
| AF-044 | C-AF-069 | match | Igual (reverter para acomodar cliente). |
| AF-045 | C-AF-070 | match | Igual. |
| AF-046 | C-AF-071 + C-AF-072 | granularidade fina | C decompõe suspensão e retomada em 2. |

## 2. Exclusivo A

Nenhum fato de A ficou sem correspondente em C (A ⊆ C em cobertura semântica).

## 3. Exclusivo C (presentes na narrativa; A não extraiu)

| C | Observação |
|---|---|
| C-AF-009…013 | Composição do veículo e das vedações (nave, tanque, 2 SRBs, fabricante, segmentos, juntas, dois O-rings, função). Presentes na narrativa. |
| C-AF-030 | 53 °F é a menor temperatura de um lançamento já realizado. |
| C-AF-035 | Intervalo para reunião privada da Thiokol. |
| C-AF-043 | Mulloy e Aldrich prosseguiram. |
| C-AF-052 | Inspeção às T−20 indicou gelo derretendo. |
| C-AF-059 | Altitude/posição da desintegração (46.000 pés, 14 km, Atlântico). |
| C-AF-061 | Óbito dos sete em T+73 s — redundância interna com C-AF-008. |
| C-AF-062 | Criação da comissão **sem data própria**; C aplicou 6/6 (data do relatório). Confluência cronológica a registrar como consistência interna, não conflito factual. |
| C-AF-065 | Conclusão de que o processo de lançamento foi falho. |
| C-AF-066 | As três ignorâncias dos responsáveis (embutidas no AF de falhas de comunicação). |
| C-AF-068 | Nível mais alto da revisão em silêncio (embutido). |
| C-AF-073 | Criação do Office of Safety, Reliability and Quality Assurance. |

Exclusivos C estritos: 13 (C-AF-009,010,011,012,013,030,035,043,052,059,061,065,073);
parciais/embutidos: C-AF-049, 051, 062, 066, 068, 071/072 (retomada). Apenas 1 redundância interna (C-AF-061) — mesmo padrão de B.

## 4. Tabela de trabalho (contagens)

| Tipo | A×B | A×C |
|---|---|---|
| Match (1:1 semântico) | 34 | 33 |
| Granularidade fina (decompôs) | 10 | 11 |
| Granularidade grossa (agrupou) | 2 | 2 |
| Divergência factual | 0 | 0 |
| Exclusivo (lado de referência) | 0 | 0 |
| Exclusivo (lado comparado) | 16 | ~15 |
| A revisar | 1 | 1 |

## 5. Leitura provisória (Fase 2)

1. **A ⊆ C** confirmado. Dois avaliadores independentes mantêm toda a cobertura de A.
2. **Zero divergência factual** em A×C — o padrão de A×B se repete.
3. C também tem a **mesma redundância interna** (C-AF-008 e C-AF-061 duplicam o óbito),
   exatamente como B — forte indício de consistência do padrão de extração, a registrar à parte (não no AFR).
4. C tende a **decompor um pouco mais** que B em 2 pontos (previsão de temperatura
   em 3 AFs; pergunta do Mulloy em 2 AFs), enquanto B consolida esses mesmos pontos
   como A. Isso adiciona granulação fina, mas sem alterar o conteúdo factual.

Além disso: C-AF-062 aplica a data do relatório à criação da comissão — mesmo tipo de
problema que descartou a rodada 1 do B, porém **não é contaminação**: os dois fatos são
suportados pela narrativa, apenas a data compartilhada é discutível. Classifico como
achado de consistência interna, fora do AFR.

> Nota de método: classificação rastreável e revisável pelo comparador humano.