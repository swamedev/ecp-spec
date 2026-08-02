# ECP-INVARIANTS — Leis Imutáveis do Protocolo

| Campo | Valor |
|---|---|
| **Tipo** | Documento de Validação (`VALID`) |
| **Fase** | V0 — Validation |
| **Status** | Rascunho |
| **Versão** | 0.2.0 |
| **Data** | 2026-08-02 |
| **Autores** | ECP Contributors |
| **Objetivo** | Declarar o que **nunca** pode mudar no ECP |

> Estes são os invariantes do protocolo — análogos às "leis da física" do ECP. Qualquer RFC futura que os viole é, por definição, um **erro de arquitetura**, não uma divergência aceitável. A diferença entre invariante e princípio (ECP-000, P-1..P-12):
>
> - **Princípio** (`P`) — fundamento que orienta; deriva de ECP-000.
> - **Lei** (`L`) — regra operacional de comportamento (L-0, L-1).
> - **Invariante** (`INV`) — condição que **deve ser verdadeira em todo estado do protocolo**, verificável a qualquer momento.
>
> Enquanto os princípios podem ser refinados por deprecação, um invariante violado **não é editado** — é sinal de que o documento que o violou está errado.

---

## 1. Declaração dos invariantes

### `INV-1` — Toda decisão é rastreável a um problema

```
Forma:    ∀ decisão D, ∃ problema P: D → Goal → P (Lei L-1).
Origem:   L-1, P-12.
Verificação: Decision Record com `problem`/`goal` apontando para
            records existentes.
```

### `INV-2` — Nenhum estado muda sem uma decisão verificável

```
Forma:    ∀ transição T, ∃ Decision Record que a autorizou (Lei L-0).
Origem:   L-0.
Verificação: sequência de transições × Decision Records (auditável
            mecanicamente).
Nota (emenda da Fase V0 — ECP-PROOF, pendência L-0): em operações
    críticas de tempo a ação pode preceder o registro formal. Isso é
    **registro a posteriori**: a decisão continua existindo,
    identificável (quem/quê/quando) e reconstruível. O invariante
    verifica a **existência da decisão** — não o instante físico do
    registro. Registro tardio não é ausência de decisão (ver ECP-000
    §5, nota de escopo; ECP-009.3).
```

### `INV-3` — Evidência nunca é inferida por autoridade

```
Forma:    autoridade (cargo, nome, marca) não é evidência.
Origem:   P-5, hierarquia de evidência (ECP-008).
Verificação: Evidence Records sem campo "fonte verificável" são não
            conformes para afirmações críticas.
Nota (emenda da Fase V0 — ECP-PROOF, pendências P-5 e P-9): fonte
    *rastreável* (citação) é nível 3 — a evidência é a observação
    referenciada, não o prestígio de quem a emitiu. "Autoridade
    garante" sem fonte verificável é nível 5 (inadmissível). A
    verificação automática cobre **conformidade estrutural**; a
    **veracidade** é estabelecida por evidência e auditoria (ver
    ECP-008 §2.2, notas de escopo).
```

### `INV-4` — Objetivos existem para resolver problemas

```
Forma:    ∄ Goal sem Problem de origem.
Origem:   L-1, P-12.
Verificação: Goal Record sem `problem` válido é não conforme.
```

### `INV-5` — Hipóteses não são fatos

```
Forma:    Claims e Assumptions permanecem distinguíveis de
            Knowledge até serem convertidas por evidência.
Origem:   P-5; ECP-005, ECP-007.
Verificação: promoção de Claim/Assumption a Knowledge exige Evidence
            Record de força compatível.
```

### `INV-6` — Restrições limitam decisões

```
Forma:    toda decisão respeita as restrições declaradas; renegociar
            restrição é uma decisão registrada, não uma violação.
Origem:   P-6.
Verificação: Decision Record que ignora restrição declarada sem
            renegociação é não conforme.
```

### `INV-7` — Artefatos são consequência, não finalidade

```
Forma:    artefato sem decisão que o justifique é dívida (P-4);
            o produto durável do projeto é conhecimento (P-3).
Origem:   P-3, P-4.
Verificação: todo artefato rastreável a Decision → Goal → Problem.
```

---

## 2. Regras de manutenção

1. Um invariante **não muda por edição**. Mudança de invariante exige deprecação formal e nova ratificação da fundação inteira.
2. Toda RFC de qualquer camada deve declarar **quais invariantes toca** e **como não os viola**. RFC sem essa declaração é devolvida.
3. Um caso (ECP-CASES) ou contraexemplo (ECP-PROOF) que viola um invariante é prioridade máxima de correção: o invariante ou o documento que o contradiz.
4. A validação dos invariantes é condição de avanço da Camada 2 (ver ROADMAP, Fase V0).

## 3. Matriz de derivação

| Invariante | Deriva de | Protege contra |
|---|---|---|
| `INV-1` | L-1, P-12 | Projeto sem origem (solução imaginada) |
| `INV-2` | L-0 | Protocolo virar checklist/workflow |
| `INV-3` | P-5 | Argumento de autoridade como prova |
| `INV-4` | L-1, P-12 | Goal órfão (otimizar a coisa errada) |
| `INV-5` | P-5 | Suposição/claim disfarçada de fato |
| `INV-6` | P-6 | Ignorar restrições silenciosamente |
| `INV-7` | P-3, P-4 | Produção sem justificativa (dívida) |

---

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 0.2.0 | 2026-08-02 | Notas de escopo em INV-2 (registro a posteriori, pendência L-0) e INV-3 (autoridade × fonte; conformidade × veracidade, pendências P-5/P-9). |
| 0.1.0 | 2026-08-02 | Declaração dos 7 invariantes; regras de manutenção; matriz de derivação. |
