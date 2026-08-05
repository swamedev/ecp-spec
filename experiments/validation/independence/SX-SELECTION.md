# SX-SELECTION — Protocolo de Seleção de Shadow Experiments

| Campo | Valor |
|---|---|
| **Tipo** | Protocolo de seleção (não-RFC, não-AD) |
| **Status** | Congelado |
| **Data** | 2026-08-03 |
| **Autor** | Arquiteto-Chefe |
| **Governado por** | [P-0007 — Independence Program](../P-0007-INDEPENDENCE.md) |
| **Referências** | [SHADOW-EXPERIMENTS](./SHADOW-EXPERIMENTS.md), [LAW-CRITERIA](../laws/LAW-CRITERIA.md) (LC-9) |

## Por que este protocolo está congelado

Critérios de elegibilidade definidos **antes** de qualquer lista de candidatos —
nunca depois. O protocolo decide; a seleção não. (Mesma disciplina do
[LAW-CRITERIA](../laws/LAW-CRITERIA.md): critérios antes dos resultados.)

## O que este documento NÃO é

- Não é uma RFC.
- Não é uma AD.
- **Não seleciona projeto.** Apenas define **como** selecionar.

## Critérios de elegibilidade (SC-1..SC-6)

### SC-1 — Independência

O projeto **nunca utilizou o ECP** (e, preferencialmente, nunca ouviu falar
dele). Operacional: verificação documental de que nenhum artefato, método ou
termo ECP aparece na origem do projeto.

### SC-2 — Evidência Pública

Existe **documentação suficiente** e acessível. Exemplos: postmortem, atas,
entrevistas, artigos, documentação pública.

### SC-3 — Sequência Temporal

É possível **reconstruir a ordem dos acontecimentos** (datas, marcos,
causalidade entre eventos).

### SC-4 — Decisões Identificáveis

Existem **decisões identificáveis** no registro, mesmo que não estejam
documentadas formalmente como "decisões".

### SC-5 — Múltiplas Fontes

**Nunca confiar em apenas uma fonte** — fontes independentes corroboram o relato.

> **Interpretação consolidada (P-0007.1, Eixo 2 — Evidence Independence, LC-10):**
> "múltiplas fontes" passa a significar **fontes de múltiplas origens causais**.
> Fontes derivadas de um mesmo evento documental (ex.: NASA, Wikipédia e um livro
> sobre o Apollo 13) contam como **uma única origem** — não como três fontes
> independentes. Verificar a **árvore de proveniência** (RA-EI-004).

### SC-6 — Reprodutibilidade

Outro avaliador, com as **mesmas fontes públicas**, chega **praticamente às
mesmas conclusões**.

## Matriz de elegibilidade

Aplicada em [SX-CANDIDATES.md](./SX-CANDIDATES.md). Colunas:

```
Projeto | Domínio (Cat) | SC-1 | SC-2 | SC-3 | SC-4 | SC-5 | SC-6 | Elegível | Observação
```

Escala por critério: **Sim | Parcial | Não**.

## Regra de elegibilidade (pré-registrada)

Um candidato é **elegível** se, e somente se, **todas** as condições valerem:

1. **SC-1, SC-3 e SC-4 = Sim** (obrigatórios);
2. **Nenhum** critério = **Não**;
3. Ao menos **4** dos seis critérios = **Sim**.

> Esta regra é **congelada antes** da aplicação. A lista de candidatos não pode
> alterá-la.

## Critérios mínimos de documentação

Para ser elegível, o projeto deve permitir reconstruir, a partir de fontes
públicas:

- o **objetivo/contexto**;
- os **problemas** enfrentados;
- as **decisões** tomadas (com alternativas, quando visíveis);
- as **hipóteses/suposições**;
- os **erros e resultados** (fim conhecido).

Um **postmortem público** costuma conter exatamente esses elementos — daí a
preferência metodológica.

## Critérios de independência (reforço ao SC-1 / LC-9)

Além de o projeto não seguir o ECP:

| Condição | Exigência |
|---|---|
| Observador | quem coleta não conhece o ECP (ou coleta em linguagem neutra) |
| Executor | a equipe do projeto nunca aplicou nem ouviu falar do ECP |
| Projeto | nenhum artefato, termo ou decisão derivou do ECP |
| Autoria | autores do ECP **não** participaram do projeto |

## Critérios de reprodutibilidade (reforço ao SC-6)

- Fontes públicas **estáveis** (relatórios oficiais, atas, arquivos acessíveis);
- **Reconstrução cega**: quem reconstrói não lê a narrativa oficial antes
  ([SHADOW-EXPERIMENTS v1.1](./SHADOW-EXPERIMENTS.md));
- **Registro auditável** dos passos de reconstrução, para um segundo avaliador.

## Critérios de exclusão (EC)

Qualquer critério de exclusão → **inelegível** (sobrepõe-se à matriz):

- **EC-1 — Núcleo de software** (SX-001): projeto cujo artefato central é
  engenharia de software. Motivo: o ECP nasceu em software; risco de
  contaminação. Projetos "software-adjacentes" entram só se o núcleo for
  físico/operacional.
- **EC-2 — Memória única:** documentação depende de um único participante, sem
  registro.
- **EC-3 — Fonte inacessível:** sem documentação pública acessível (paywall
  total sem alternativa).
- **EC-4 — Narrativa única:** uma única narrativa incontestada (fragiliza
  SC-5/SC-6).
- **EC-5 — Sem consequência:** projeto sem decisões de consequência real
  (toy/demonstração).
- **EC-6 — Envolvimento ECP:** qualquer participação dos autores do ECP.
- **EC-7 — Exposição prévia:** equipe já exposta ao ECP.

## Preferência metodológica

1. **Postmortem público** (contém objetivo, problemas, decisões, hipóteses,
   erros, resultados).
2. **Fora de software** — domínios o mais distantes possível da origem do ECP.
3. **Múltiplas fontes independentes** (relatórios oficiais + cobertura +
   documentos internos divulgados).

## Categorias-alvo (SX-001)

| Categoria | Exemplos |
|---|---|
| **A — Engenharia Física** | construção, ponte, fábrica |
| **B — Saúde** | implantação hospitalar, mudança de protocolo, gestão clínica |
| **C — Pequenos Negócios** | abertura de restaurante, expansão de loja, reorganização operacional |
| **D — Logística** | distribuição, cadeia de suprimentos, transporte |
| **E — Pesquisa Científica** | projetos acadêmicos, experimentos laboratoriais |

## Procedimento de seleção

1. **Congelar** este protocolo (feito em 2026-08-03).
2. Levantar **10–20 candidatos** em domínios distintos (preferencialmente fora
   de software).
3. Aplicar a **matriz** com a regra pré-registrada (seção acima).
4. **Re-auditar** os elegíveis sob o framework congelado ([P-0007.2](../P-0007.2-CANDIDATE-REAUDIT.md)
   → [SX-REAUDIT.yaml](./SX-REAUDIT.yaml)): EI por origens causais, DI por
   taxonomia, OI exógena.
5. **Verificar fontes** (confirmar acessibilidade pública) — etapa **obrigatória**
   antes da escolha final.
6. Aplicar os **critérios de exclusão** (EC-1..EC-7).
7. Se mais de um elegível, prioridade pré-registrada:
   a. domínio mais **distante** do software;
   b. preferência por **postmortem público**;
   c. maior **multiplicidade** de origens.
8. Selecionar e registrar em `SHADOW-REPORT-###`.

**Estágios de seleção (P-0007.2):**

```
Elegível → Auditado → Selecionável → Selecionado
```

| Estágio | Significado |
|---|---|
| **Elegível** | "em princípio atende" (matriz SC-1..SC-6). |
| **Auditado** | passou o re-audit sob o framework congelado (SX-REAUDIT). |
| **Selecionável** | auditado e sem pendências metodológicas. |
| **Selecionado** | escolhido pelo **protocolo** — nunca pelo autor. |

> **Nenhuma seleção antecipada.** A lista é ampla; **o protocolo decide** quais
> candidatos são elegíveis.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-03 | Versão inicial (**Congelado antes da lista de candidatos**). SC-1..SC-6; matriz; regra de elegibilidade pré-registrada; mínimos de documentação; independência; reprodutibilidade; exclusões EC-1..EC-7; procedimento; preferência por postmortem; categorias A-E. |
| 1.1 | 2026-08-03 | **Consolidação (P-0007.1):** SC-5 reinterpretada pela **Evidence Independence** — múltiplas fontes = fontes de múltiplas **origens causais** (RA-EI). Domínio passa a ser contado pela taxonomia canônica do Independence Framework (RA-DI). |
| 1.2 | 2026-08-03 | **Estágios de seleção (P-0007.2):** Elegível → Auditado → Selecionável → Selecionado; etapa 4 de re-auditoria adicionada ao procedimento. |
