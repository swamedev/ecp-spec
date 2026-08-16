# GO-8C — Pacote de Revisão — NT-05 Semantic Review (Painel de IAs Independentes)

**Data de preparação:** 2026-08-13
**Ciclo:** GO-8C
**Origem:** DECISION D-03 (Alternativa B, ATUALIZADA) — substituição **parcial** do requisito humano NT-05.
**Status:** READY FOR REVIEW — a revisão **NÃO foi executada**. Este pacote disponibiliza o material ao **painel de 2 IAs independentes em três abas separadas**.

---

## 1. O que é esta revisão

É a **revisão semântica mínima** do NT-05 (GO-8C D-03, Alternativa B). A governança substituiu parcialmente o requisito humano original de NT-05 (3 validadores) por: componentes determinísticos automatizados (NT-01..04 + suítes operacionais — já PASS) **+ um gate semântico mínimo por painel de 2 IAs independentes** (arquiteturas/provedores diferentes, abas separadas), com rubrica pré-registrada.

**Limitação divulgada:** *"NT-05 substituído por painel de IAs independentes por indisponibilidade humana. Não há equivalência epistemológica com revisão humana."*

Esta revisão cobre **exatamente o que a auditoria automatizada NÃO cobre**: a detecção de **contaminação conceitual por paráfrase/sinonímia** na taxonomia C3 e nos materiais de entrada.

## 2. Painel — requisitos e instruções

### 2.1 Requisitos do painel (três abas separadas)

- **Método de três abas:** aba Executor (coordenação — **não participa como revisor**) + **aba 1** (Revisor 1) + **aba 2** (Revisor 2). Procedimento completo em `REVIEW-PANEL-PROCEDURE.md`.
- **2 IAs independentes, de arquiteturas/provedores diferentes** (ex. indicativos: GLM-4.5 Flash e Nemotron 3 Ultra). Modelos efetivos registrados na execução.
- **Acesso restrito:** cada revisor lê **somente** arquivos dentro de `review/` (incluindo `review/materials/`) e os itens a revisar. **Sem acesso** ao código executor, ao histórico de decisões ou a outras pastas do projeto.
- **Contextos completamente limpos:** cada IA opera **sem acesso ao histórico do projeto** (sem sessões anteriores, decisões ou conversas prévias). Recebe **somente** este pacote (`review/`) e a sua via do formulário.
- **Sem comunicação entre vias:** cada IA preenche a **sua** via do formulário (`REVIEW-FORM-MODEL-1.md` / `REVIEW-FORM-MODEL-2.md`) de forma independente.

### 2.2 Passos para cada IA (ver prompt padrão em `REVIEW-PANEL-PROCEDURE.md` §4)

1. **Leia primeiro** o protocolo `protocol/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` (cópia somente leitura) e a lista de itens `REVIEW-ITEMS.md`.
2. Revise cada item da lista conforme a **rubrica pré-registrada** (Categorias 1/2/3) — ver §4.
3. **Use os materiais de `review/materials/`** (cópias locais da taxonomia C3 e dos materiais de entrada) — **não acesse outras pastas**.
4. Preencha a **sua via** do formulário (`REVIEW-FORM-MODEL-1.md` se MODEL-1; `REVIEW-FORM-MODEL-2.md` se MODEL-2), com veredito **por item** e, ao final, o veredito global.
5. **Cegueira:** NÃO conhecer o mapping C2 (permutação), resultados SX-001, hipóteses ECP específicas, nem a identidade das condições.
6. **Independência:** a execução é separada; não consultar a outra via nem qualquer material fora do pacote.
7. **Critério (por via):** ≤ 0 (nenhuma) violação semântica não capturada. Qualquer ocorrência na via → REJEITADO.
8. **Registro:** identificar **modelo/versão** e **hash anônimo**; preencher `reviewed_on`; `notes` obrigatório em caso de violação.
9. **Devolução:** entregar a via preenchida como artefato do GO-8C (ver seção 6), sem alterar nenhum outro arquivo.

## 3. Critério global de aprovação (unanimidade)

- **AMBAS as vias** devem retornar **PASS em todas as categorias/item**, sem nenhuma violação.
- **Divergência entre modelos = STOP.** NÃO é aceitável votação por maioria. Qualquer divergência (ex.: `SEM VIOLAÇÃO` × `VIOLAÇÃO` em um item) → STOP: resultado registrado e escalado à governança.
- **Qualquer violação em qualquer via** → REJEITADO: correção e **revalidação completa**.

## 4. Rubrica (resumo — ver protocolo para detalhes)

| Cat. | Nome | Significado |
|---|---|---|
| **1** | Violação de isolamento SYN | Conteúdo ECP ou CAT indevido em labels/definições/source_refs/narrativas (não capturado por check lexical). |
| **2** | Paráfrase de termo ECP | Termo/conceito ECP reexpresso com sinonímia/paráfrase, escapando à varredura léxica. |
| **3** | Viés estrutural na narrativa/atomic facts | Padrão estrutural ou de seleção que comprometa a **cegueira**. |

## 5. Conteúdo do pacote

```
review/
├── README-REVIEW.md                       <- este arquivo
├── REVIEW-PANEL-PROCEDURE.md              <- procedimento operacional das três abas (passo a passo, prompts)
├── protocol/
│   └── NT-05-SEMANTIC-REVIEW-PROTOCOL.md  <- cópia somente leitura do protocolo
├── REVIEW-ITEMS.md                        <- lista dos itens a revisar (caminhos relativos a review/)
├── REVIEW-FORM.md                         <- template mestre (não preencher diretamente)
├── REVIEW-FORM-MODEL-1.md                 <- via MODEL-1 (formulário de evidências)
├── REVIEW-FORM-MODEL-2.md                 <- via MODEL-2 (formulário de evidências)
└── materials/                             <- cópias de leitura dos itens a revisar
    ├── C3_TAXONOMY.yaml                   <- taxonomia C3 (SYN-001..SYN-012)
    └── BIP-00X-*/narrative|atomic-facts/  <- materiais de entrada dos BIPs
```

## 6. Nota sobre escopo de escrita

- Este pacote fica em `experiments/validation/GO-8C/review/`.
- **GO-8B permanece CLOSED / LOCKED / FROZEN** — os itens em `review/materials/` são **cópias de leitura**; os originais em `experiments/validation/GO-8B/...` e `scripts/go8b/operational/...` **NÃO são alterados**.
- O `BIP-VAL_REPORT.yaml` do GO-8C **NÃO será atualizado** nesta etapa; isso ocorrerá apenas após a entrega e análise das vias do formulário.

---

**Fim do README. Pacote pronto para o painel de 2 IAs independentes (três abas). Nenhuma revisão executada nesta preparação.**
