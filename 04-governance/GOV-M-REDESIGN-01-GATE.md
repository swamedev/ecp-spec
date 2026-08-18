# GOVERNANCE — REGRAS CONGELADAS PARA M-REDESIGN-01-SPEC-A.md

## Registro Formal das Regras Congeladas

**Documento:** GOV-M-REDESIGN-01-GATE
**Data:** 2026-08-17
**Associado a:** M-REDESIGN-01-SPEC-A.md

---

## REGRAS CONGELADAS

### 1. Gate de Mensuração B
A Fase B é um gate de mensuração. Seus resultados **não** constituem evidência sobre a hipótese substantiva do GO-8D-NC.

### 2. Seleção Cega da Referência GED
A seleção da referência GED **não pode** depender de A>B>C nem de qualquer resultado A/B/C.

### 3. Validação Métrica Sem Potência
A validação da métrica **não pode** depender de potência nem de resultado de novo experimento.

### 4. Bloqueio de Influência dos Avaliadores IA
Os avaliadores Claude/GPT/Gemini **não podem** influenciar:
- a seleção da referência GED;
- os critérios C1–C5.

### 5. Avaliação por IA como Interpretabilidade Apenas
Avaliação por IA **não é** ground truth científico. Serve apenas para o componente de interpretabilidade/concordância previamente definido.

### 6. Regra Fail/Gate Closed
Nenhuma referência GED PASS → **GATE CLOSED**. É proibido escolher uma referência "menos ruim" se todas falharem.

### 7. Congelamento de Especificação
Após o congelamento, qualquer alteração em:
- critérios;
- limiares;
- referências;
- pesos;
- seed;
- agregadores;
- regras de decisão;
  **deverá** ser tratada como **MUDANÇA DE ESPECIFICAÇÃO**, não como ajuste operacional.

---

## Decisão de Autorização

**Fase B:** ❌ **NÃO AUTORIZADA**
**Fase C:** ❌ **NÃO AUTORIZADA**
**GO-8E:** ❌ **NÃO AUTORIZADO**

---

**Assinatura:** Governança ECP
**Data:** 2026-08-17