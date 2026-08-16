# GO-8C — NT-05 SEMANTIC REVIEW — PROCEDIMENTO DO PAINEL (Três Abas Separadas)

**Data:** 2026-08-13
**Ciclo:** GO-8C
**Origem:** DECISION D-03 (Alternativa B, ATUALIZADA) — painel de 2 IAs independentes em três abas separadas, acesso restrito.
**Status:** READY TO RUN — a revisão **NÃO foi executada**. Este documento formaliza o procedimento de execução.

---

## 1. Visão geral do método

O painel usa **três abas separadas**:

| Aba | Papel | Participação na revisão |
|---|---|---|
| **Aba Executor** | Esta sessão de preparação/coordenação | **NÃO participa como revisor** — disponibiliza o pacote; após a execução, consolida os formulários |
| **Aba 1 — Revisor 1** | 1ª IA independente | Revisa via `REVIEW-FORM-MODEL-1.md` |
| **Aba 2 — Revisor 2** | 2ª IA independente | Revisa via `REVIEW-FORM-MODEL-2.md` |

- As abas de revisão **não comunicam entre si**.
- Cada revisor tem **contexto completamente limpo** (sem histórico do projeto).
- Cada revisor tem **acesso restrito** apenas a `experiments/validation/GO-8C/review/` (incluindo `review/materials/`) e aos itens a revisar.
- **Critério de aprovação:** AMBAS as IAs retornam PASS em todas as categorias, sem nenhuma violação.
- **Divergência entre revisores = STOP.** NÃO é aceitável votação por maioria.

## 2. Modelos recomendados

| Revisor | Modelo recomendado | Substituição permitida |
|---|---|---|
| **Revisor 1** | GLM-4.5 Flash | Outro modelo de arquitetura/provedor distinto, se indisponível |
| **Revisor 2** | Nemotron 3 Ultra | Outro modelo de arquitetura/provedor distinto, se indisponível |

> Regra: os 2 modelos devem ser de **arquiteturas/provedores diferentes**. O modelo efetivo é registrado no cabeçalho de cada formulário e no registro de validação.

## 3. Passo a passo

1. **Abrir as três abas** (janelas/instâncias separadas e independentes):
   - Aba Executor (esta sessão) — já aberta.
   - Aba 1: nova sessão limpa com o **Revisor 1**.
   - Aba 2: nova sessão limpa com o **Revisor 2**.
2. **Garantir contexto limpo:** em cada aba de revisão, confirmar que não há histórico/conversas anteriores do projeto (iniciar sessão nova).

> ### REGRA OBRIGATÓRIA — ABAS NOVAS E CÓPIAS ATUALIZADAS (cada rodada de revisão)
> - **Para CADA rodada de revisão é obrigatório abrir abas NOVAS com contexto 100% limpo** (sessões sem qualquer histórico/conversa anterior do projeto). Revisões feitas em abas com contexto antigo **invalidam** a rodada — elas podem ler versões desatualizadas dos arquivos e produzir resultados não confiáveis.
> - Os revisores devem ler **SOMENTE as cópias atualizadas em `review/materials/`** — nunca arquivos de outras pastas do projeto (ex.: `scripts/go8b/operational/`), cujas versões podem divergir do pacote revisado.
> - Se qualquer material em `review/materials/` for corrigido/atualizado entre rodadas, o executor deve **reconfirmar o conteúdo antes de relançar o painel** (ex.: conferir SYN-001/SYN-012 em `materials/C3_TAXONOMY.yaml`).

3. **Colar o prompt padrão** de cada revisor (seções 4.1 e 4.2) na respectiva aba.
4. **Cada revisor executa a revisão** conforme o prompt e o protocolo, lendo **somente** os arquivos dentro de `review/` (e `review/materials/`).
5. **Salvar o formulário:** cada revisor produz a via preenchida:
   - Revisor 1 → `REVIEW-FORM-MODEL-1.md` (preenchido)
   - Revisor 2 → `REVIEW-FORM-MODEL-2.md` (preenchido)
6. **Comparar os formulários:** o executor (que NÃO revisa) confere item a item:
   - Se **AMBOS** = `SEM VIOLAÇÃO` em **todos** os itens → **PASS**.
   - Se **qualquer** violação em **qualquer** via → **REJEITADO** (correção + revalidação).
   - Se **divergência** entre as vias em qualquer item → **STOP** (registrar e escalar à governança; proibido votação por maioria).
7. **Registrar o resultado:** preencher artefato de validação (`decisions/D-03-NT05-VALIDATION.md` atualizado ou novo) e, conforme resultado, atualizar `scripts/BIP-VAL_REPORT.yaml` (GO-8C) para `verdict: PASS` ou manter pendente/STOP.

## 4. Prompts padrão

### 4.1 Prompt do Revisor 1 (aba 1)

```
Você é o REVISOR 1 de um painel de revisão semântica do experimento GO-8C (NT-05).

RESTRIÇÃO DE ACESSO: leia APENAS arquivos dentro de:
  - experiments/validation/GO-8C/review/  (incluindo review/materials/)
Você NÃO deve acessar código executor/scripts, histórico de decisões, nem qualquer
outra pasta do projeto fora de review/. Use APENAS o conteúdo do pacote review/.

TAREFA:
1. Leia: review/README-REVIEW.md, review/protocol/NT-05-SEMANTIC-REVIEW-PROTOCOL.md,
   review/REVIEW-ITEMS.md e os materiais em review/materials/.
2. Revise CADA item da lista (alvo primário: 12 categorias SYN-001..SYN-012 da
   review/materials/C3_TAXONOMY.yaml; alvo secundário: materiais de entrada).
3. Aplique a rubrica pré-registrada (Categorias 1/2/3):
   - Categoria 1: violação de isolamento SYN (conteúdo ECP ou CAT indevido).
   - Categoria 2: paráfrase de termo ECP não capturada por check lexical.
   - Categoria 3: viés estrutural que comprometa a cegueira.
4. Preencha a SUA via do formulário (review/REVIEW-FORM-MODEL-1.md) com veredito por
   item (SEM VIOLAÇÃO | VIOLAÇÃO cat. X) e o veredito global.
5. Critério da via: PASS somente se NENHUMA violação (≤ 0). Qualquer ocorrência ⇒ REJEITADO.

NÃO consulte a via do Revisor 2. Trabalhe de forma 100% independente.
Registre: modelo/versão, hash anônimo, reviewed_on e cobertura efetiva.
```

### 4.2 Prompt do Revisor 2 (aba 2)

```
Você é o REVISOR 2 de um painel de revisão semântica do experimento GO-8C (NT-05).

RESTRIÇÃO DE ACESSO: leia APENAS arquivos dentro de:
  - experiments/validation/GO-8C/review/  (incluindo review/materials/)
Você NÃO deve acessar código executor/scripts, histórico de decisões, nem qualquer
outra pasta do projeto fora de review/. Use APENAS o conteúdo do pacote review/.

TAREFA:
1. Leia: review/README-REVIEW.md, review/protocol/NT-05-SEMANTIC-REVIEW-PROTOCOL.md,
   review/REVIEW-ITEMS.md e os materiais em review/materials/.
2. Revise CADA item da lista (alvo primário: 12 categorias SYN-001..SYN-012 da
   review/materials/C3_TAXONOMY.yaml; alvo secundário: materiais de entrada).
3. Aplique a rubrica pré-registrada (Categorias 1/2/3):
   - Categoria 1: violação de isolamento SYN (conteúdo ECP ou CAT indevido).
   - Categoria 2: paráfrase de termo ECP não capturada por check lexical.
   - Categoria 3: viés estrutural que comprometa a cegueira.
4. Preencha a SUA via do formulário (review/REVIEW-FORM-MODEL-2.md) com veredito por
   item (SEM VIOLAÇÃO | VIOLAÇÃO cat. X) e o veredito global.
5. Critério da via: PASS somente se NENHUMA violação (≤ 0). Qualquer ocorrência ⇒ REJEITADO.

NÃO consulte a via do Revisor 1. Trabalhe de forma 100% independente.
Registre: modelo/versão, hash anônimo, reviewed_on e cobertura efetiva.
```

## 5. Como salvar e comparar os formulários

- **Salvar:** cada via preenchida é um arquivo próprio (`REVIEW-FORM-MODEL-1.md` e `REVIEW-FORM-MODEL-2.md`), preservado em `review/` como evidência.
- **Comparar:** o executor compara **item a item** (P-1.a..l; S-1a..S-7b):
  - Ambos `SEM VIOLAÇÃO` em todos os itens ⇒ **PASS**.
  - Qualquer violação (em qualquer via) ⇒ **REJEITADO**.
  - Divergência em qualquer item ⇒ **STOP** (registrar; proibido votação por maioria).
- **Consolidar:** registrar o resultado consolidado em artefato de validação e, se PASS, atualizar `verdict` do `scripts/BIP-VAL_REPORT.yaml` (GO-8C) para `PASS`.

## 6. Regras de governança (inalteráveis)

- **Unanimidade obrigatória:** AMBAS as vias PASS.
- **Divergência = STOP:** sem votação por maioria; sem consolidação ad hoc.
- **Acesso restrito:** revisores leem somente `review/` (incluindo `review/materials/`).
- **Executor não revisa.**
- **GO-8B permanece intacto** — nenhum arquivo do GO-8B é lido-alterado pelos revisores; os materiais usados são cópias em `review/materials/`.

---

**Fim do procedimento. Pronto para abrir as duas abas de revisão e colar os prompts das seções 4.1 e 4.2.**
