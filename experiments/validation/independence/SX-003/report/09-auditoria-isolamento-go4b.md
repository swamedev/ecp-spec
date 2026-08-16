# SX-003 / Auditoria de Isolamento — GO-4B

| Campo | Valor |
|---|---|
| **Comando** | GO-4B — Auditar isolamento da reconstrução cega |
| **Autor** | Executor do pipeline congelado (GO-4B) |
| **Data** | 2026-08-09 |
| **Objeto** | Violação do isolamento: comparação com SX-001/SX-002 **dentro** da reconstrução cega (`03-reconstrucao-cega.md`) |
| **Fonte da regra** | `README.md` do SX-003 (Restrições §5: "não forçar o caso a reproduzir nem a contradizer o padrão dos SX-001/002") + instrução GO-2 ("não comparar com SX-001/002 antes da revisão pós-experimento") |
| **Natureza da blindagem** | A cegueira formal do pipeline protege contra a **Narrativa Original**. A comparação com SX-001/002 era vedada **temporariamente** (adiada para a revisão), não como blindagem de observador. |

---

## 0. Objetivo da auditoria

Determinar se o conhecimento de SX-001/SX-002 (casos de crise, EAR 0.775/0.82,
ausências características) **influenciou materialmente** a reconstrução cega do
Genoma — e, em caso positivo, em **quais elementos**. Resultado: classificação de
independência — **integral | comprometida | indeterminada**.

---

## 1. Pontos de exposição encontrados na reconstrução cega

| # | Local | Conteúdo | Classe de exposição |
|---|---|---|---|
| 1 | §0, linhas 18–22 ("Importância") | Cita que SX-001/002 eram casos de **crise/falha** e que este é classificado como **sucesso** | motivação do experimento (pré-registro) — **aceitável**, é o desenho |
| 2 | §2 (linhas 183–188) | "ao contrário dos casos de crise, onde a cadeia começava numa lacuna... aqui a cadeia começa definida desde o início" | **leitura interpretativa em contraste** com os casos de crise |
| 3 | §1.9 Problem (linhas 152–155) | "nos casos de crise o problema era pós-hoc. Aqui há o oposto" | interpretação comparativa |
| 4 | §3 (linhas 205–217) | **Tabela comparativa** de ausências SX-001 × SX-002 × SX-003 | **violação explícita** da instrução GO-2 (comparação antecipada) |
| 5 | §5 Resumo (linhas 246–250) | "Leitura-chave diferente dos casos de crise: ... contra-controle aos casos de crise" | interpretação comparativa |
| 6 | §5 Resumo (linhas 216–217) | citação de `SIG-002` (predição inversa) | conhecimento prévio dos signals dos casos anteriores |

> Os **Atomic Facts** (`02-atomic-facts.md`) não contêm referência comparativa aos
> SX-001/002. A contaminação potencial está **somente** na camada interpretativa da
> reconstrução, **não** na camada de fatos.

---

## 2. Classificação de influência por elemento

| Elemento da reconstrução | Suporte (AFs do Genoma) | Depende de SX-001/002 para se afirmar? | Grau |
|---|---|---|---|
| Goal / Problem ex-ante | AF-005/006, AF-047 (fatos do próprio Genoma) | **Não** — presença constatada direto dos AFs | 🟢 independente |
| Projeção prazo/custo | AF-011, AF-012 | **Não** | 🟢 |
| Knowledge / Lacuna / Assumption | AF-001/007/010/018/019/023/024 | **Não** | 🟢 |
| Decision / Execution / Evidence / Validation | AF-005/008/014/015/036…044/048/049 | **Não** | 🟢 |
| Risk formal **ausente** | AF-012, AF-032/034 | Interpretação apoia-se na governança ELSI; o contraste pode reforçar a leitura | 🟡 |
| Learning parcial | AF-010, AF-050 | **Não** | 🟢 |
| **Observação central** (linhas 183–188; 246–250) | — | Afirma **diferença em relação aos casos de crise** — exige conhecimento dos SX-001/002 | 🟠 |
| **Tabela comparativa §3** | — | É, ela mesma, o vazamento (referência direta a SX-001/002) | 🔴 |
| Uso de `SIG-002` (linhas 216–217) | — | Usa predição inversa de signal dos casos anteriores antes da Etapa 4 | 🟠 |
| EAR / contagem da Etapa 4 | — | Cálculo usa Narrativa × Reconstrução do **mesmo caso**; não depende dos outros | 🟢 |

---

## 3. Veredito de independência

### 3.1 Camada fática / observacional

**INTEGRAL.** As entidades emergiram com suporte direto de `AF-###` do próprio
Genoma. Mesmo removendo tudo o que menciona SX-001/002, Goal/Problem/projeção/
Knowledge/Decision/Execution/Evidence/Validation continuam sustentadas pelos fatos.

### 3.2 Camada interpretativa (contraste, tabela, SIG-002)

**COMPROMETIDA.** As observações interpretativas (§1 items 2, 3, 5, 6) e a tabela
comparativa prematura (§3) foram produzidas com conhecimento prévio dos SX-001/002.
Isso não invalida o dado, mas **não permite** tratar "a cadeia foi diferente das
crises" como reconstrução cega **imaculada**: a direção da comparação existia
antes da revisão (pré-registro) e a tabela violou o adiamento do GO-2.

### 3.3 Classificação global

| Classificação | Escopo | Decisão |
|---|---|---|
| **integral** | Emergência das entidades (Goal→Validation), suporte AF, contagens/EAR | ✅ íntegra para a **estrutura factual** da reconstrução |
| **comprometida** | Leitura comparativa / contraste ("diferente dos casos de crise", tabela §3, corolário SIG-002) | ⚠️ **comprometida como cadeia "cega"** — não pode sustentar sozinha uma lei/pattern |
| **indeterminada** | — | Nenhum elemento ficou cientificamente indeterminado |

### 3.4 Implicação operacional (registrar para GO-5)

- As **afirmações factuais** (presença ex-ante, projeção, governança do risco) permanecem
  admissíveis — têm suporte AF.
- A **interpretação comparativa** produzida pela reconstrução **não entra como evidência
  independente** de "primeiro caso de sucesso"; será re-avaliada na revisão pós-experimento
  (GO-5) sem poder suprimir o viés da leitura em contraste.
- O `new insight` da Etapa 4 (NI-002 — ausência de Risk *calculado* em vez de *cálculo*)
  conserva a categoria, mas sua base interpretativa deve ser registrada como **recomendação
  insegura** (viés da leitura em contraste).

---

## 4. Medidas GO-4B (não alteram dados)

1. Registrada nesta auditoria a violação de isolamento, com objeto e localização (§1).
2. Manter o trecho comparativo §3 no arquivo (registro do protocolo), marcado como
   "auditado em GO-4B".
3. Não tocar nos AFs nem nas classificações — nada foi encontrado que exija retificação.
4. Relatório separado garante rastreabilidade sem apagar o vazamento.

---

## 5. Verificação final (GO-4B)

- Recontagem Etapa 4: **26 itens (15 MATCH / 7 PARTIAL / 2 NOT / 2 NEW)** — inalterada (GO-4A).
- EAR: **0.77** — inalterado.
- Sinais: nenhuma promoção — inalterado.
- AF: 50 — inalterado.

---

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-09 | Auditoria GO-4B: 8 pontos de exposição mapeados (1 aceitável; §1). Camada factual: **integral**. Camada interpretativa comparativa: **comprometida**. Vazamento mantido como registro; decisão sobre transversal adiada para GO-5. Sem alteração de conteúdo nesta etapa. |
