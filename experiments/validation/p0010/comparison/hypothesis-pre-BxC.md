# P-0010 — Hipótese pré-B×C (expectativa de trabalho)

> Registrada **antes** da execução da Fase 3. Não é conclusão; é a expectativa
> de trabalho com base em A×B e A×C. Se B×C confirmar, a evidência se fortalece;
> se não, ajustamos a leitura.

## Estado congelado

- ✅ Fase 1 — `analysis-AxB.md` (congelada)
- ✅ Fase 2 — `analysis-AxC.md` (congelada)
- ❄️ Entradas imutáveis: `input/evaluator-{A,B,C}.md`
- 🔒 Sem reabertura de classificação das fases 1 e 2 durante a Fase 3

## Padrão observado (A×B e A×C)

1. Cobertura: a referência A (46 AFs) está **contida** nos avaliadores B e C
   (exclusivo A = 0 em ambas).
2. Divergência factual: **0 conflitos** em A×B e em A×C.
3. Variabilidade dominante: **grau de decomposição** (granularidade fina),
   nunca alteração de causalidade ou cronologia.
4. Consistência interna (achado à parte, fora do AFR): B e C ambos produzem
   uma **redundância interna** do óbito (B-AF-008/B-AF-055; C-AF-008/C-AF-061).

## Hipótese pré-B×C

B×C deve reproduzir o mesmo padrão:

- **H1 — cobertura**: B e C devem se cobrir quase integralmente; a diferença de
  contagem (75 × 73) deve vir de granulação, não de fatos ausentes.
- **H2 — divergência factual**: esperado ~0 conflitos factuais entre B e C
  (ambos extraem da mesma narrativa, sem conhecimento externo).
- **H3 — granularidade**: as diferenças devem se concentrar em 2 a 4 pontos em
  que C decompõe além de B (ex.: previsão de temperatura em 3 AFs; pergunta do
  Mulloy em 2 AFs) e em casos em que um consolida o que o outro separa.
- **H4 — exclusivos**: fatos exclusivos de um lado devem ser poucos e rastreáveis
  à narrativa, sem inferência.
- **H5 — consistência interna**: eventuais redundâncias internas devem ser
  registradas à parte, não misturadas ao AFR.

## Critério de decisão

- Se H1–H4 confirmarem → fechar P-0010 com evidência robusta de que a
  variabilidade do protocolo é predominantemente de granulação, com AFR alto.
- Se B×C revelar conflito factual real → revisar a leitura das fases 1 e 2.

> Método: mesma taxonomia (match / granularidade fina / granularidade grossa /
> exclusivo / divergência factual) e mesma disciplina de rastreabilidade AF a AF.
