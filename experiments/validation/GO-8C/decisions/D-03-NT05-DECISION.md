# GO-8C — DECISION D-03 — NT-05 (Substituição Parcial: Painel de IAs Independentes)

**Data:** 2026-08-13
**Ciclo:** GO-8C
**Decisor:** Governança GO-8C
**Decisão:** **Alternativa B** — substituição **parcial** do requisito humano NT-05: componentes determinísticos automatizados + **gate semântico mínimo por painel de 2 IAs independentes (abas separadas) com acesso restrito**, com rubrica pré-registrada.

**ATUALIZAÇÃO (2026-08-13):** em substituição ao item 2 da decisão original ("1 revisor independente humano"), a governança, reconhecendo a **indisponibilidade de revisor humano**, determina o gate semântico por **painel de 2 IAs independentes em três abas separadas** (ver §2.1 e §7). O restante da decisão permanece válido.

**Status:** DECIDED (ATUALIZADO)
**Escopo:** exclusivamente o requisito NT-05 (aprovação do artefato taxonomia C3). Não altera outros gates, métricas, critérios de caso ou Go/No-Go. Implementação autorizada SOMENTE dentro de `experiments/validation/GO-8C/`. Nenhum arquivo do GO-8B pode ser alterado.

---

## 1. Contexto

- O requisito congelado NT-05 (`GO-8B/03-SYNTHETIC-TAXONOMY-C3.md` §4.2) exigia **3 validadores humanos independentes** classificando cada categoria C3 como "derivada de ECP?" (Sim/Não/Incerto); critério de aprovação: ≤ 1 "Sim" por categoria.
- O GO-8B substituiu temporariamente NT-05 por auditoria automatizada (NC-01, 2026-08-12), com ressalva explícita de **não equivalência epistemológica**; resultado registrado em NC-04 (gate VALIDATED para os fins do piloto).
- A proposta `D-03-NT05-PROPOSAL.md` (2026-08-13) diagnosticou que o **julgamento semântico** (núcleo de NT-05 — contaminação conceitual por sinônimo/paráfrase) **não é coberto** por proxy lexical/estrutural determinístico; e que havia divergência documental (`BIP-VAL_REPORT.yaml` exibindo `NT-05: PENDING` / `verdict: PENDING` enquanto a governança aceitara a substituição).
- Governança GO-8C **aprovou a Alternativa B** (originalmente com 1 revisor humano).
- **ATUALIZAÇÃO (2026-08-13):** a governança reconhece que **não há revisor humano disponível** e formaliza o gate semântico como **painel de 2 IAs independentes em três abas separadas**, aceitando a limitação com **divulgação explícita**.

## 2. Decisão (Alternativa B — atualizada)

1. **Componentes determinísticos (NT-01..04 e suítes operacionais)** permanecem **automatizados** e são o gate objetivo da taxonomia C3.
2. **Um gate semântico mínimo é mantido: painel de 2 IAs independentes em abas separadas**, com acesso restrito, com rubrica pré-registrada (ver `decisions/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` e `review/REVIEW-PANEL-PROCEDURE.md`). O **agente executor não participa como revisor**.
3. **Critério de aprovação:** **AMBAS** as IAs devem retornar **PASS** em todas as categorias, sem nenhuma violação. Qualquer ocorrência → correção e revalidação.
4. **Regra de divergência:** divergência entre os 2 modelos = **STOP**; **NÃO** é aceitável votação por maioria.
5. **Harmonização do artefato BIP-VAL do GO-8C:** refletir o novo protocolo — `NT-05: SUBSTITUTED_PARTIAL (2 independent AI reviewers)` e `verdict: PASS_PENDING_AI_PANEL` (até a revisão do painel ser executada).
6. **Nenhuma alteração no GO-8B.** As suítes, o parser, o C3_TAXONOMY e os parâmetros do GO-8B permanecem intocados.
7. **Não é criada equivalência** entre auditoria automatizada e revisão humana; a substituição é **parcial** e limitada ao NT-05. **A limitação é registrada explicitamente.**

### 2.1 Requisitos do painel de IAs (três abas separadas)

- **Três abas separadas:** aba do executor (esta sessão — não participa como revisor) + **aba 1** (Revisor 1) + **aba 2** (Revisor 2). As abas de revisão operam de forma **totalmente independente e sem comunicação entre si**.
- **Modelos diferentes** (arquiteturas/provedores diferentes) — ex.: GLM-4.5 Flash e Nemotron 3 Ultra (exemplos indicativos; a governança registra os modelos efetivos na execução).
- **Acesso restrito:** cada revisor lê **somente** arquivos dentro de `experiments/validation/GO-8C/review/` (incluindo `review/materials/`) e os itens a revisar (materiais e taxonomia). **Sem acesso** ao código executor, ao histórico de decisões ou a qualquer outra pasta do projeto.
- **Contextos completamente limpos:** cada IA opera **sem acesso ao histórico do projeto** (sem contexto da sessão de desenvolvimento, sem decisões anteriores, sem conversas prévias).
- **Mesmo formulário** `REVIEW-FORM.md` (preenchimento independente por via — `REVIEW-FORM-MODEL-1.md` e `REVIEW-FORM-MODEL-2.md`).
- **Critério de aprovação:** AMBAS retornam PASS em todas as categorias, sem nenhuma violação.
- **Divergência entre modelos = STOP** (não é aceitável votação por maioria).

## 3. Justificativa

- **Preserva o núcleo epistemológico de NT-05:** a detecção de contaminação conceitual por sinonímia/paráfrase é irredutivelmente semântica; um painel de 2 IAs independentes, com rubrica pré-registrada, fornece julgamento independente com rastreabilidade.
- **Independência por arquitetura/provedor:** 2 modelos de arquiteturas/provedores diferentes, com contextos limpos, reduzem o risco de viés correlacionado (diferentes fronteiras de generalização semântica).
- **Divergência = STOP:** evita falsa consolidação; qualquer divergência força revisão/análise antes de qualquer aprovação.
- **Viabilidade:** sem gargalo humano; escalável ao estudo confirmatório N=12.
- **Limitação divulgada:** reconhecimento explícito de que **não há equivalência epistemológica** com a revisão humana original (3 validadores).

## 4. Limites e Ressalvas

- D-03 resolve **apenas** NT-05; não altera outros gates do BIP-VAL nem critérios de caso (FR-01..06) ou Go/No-Go (07 §8).
- O **verdict final** do BIP-VAL do GO-8C permanece **`PASS_PENDING_AI_PANEL`** até a execução da revisão do painel; a revalidação será registrada em artefato de validação próprio.
- A divergência documental do GO-8B (artefato `PENDING` × decisão de aceite) **não é modificada no GO-8B**; apenas o artefato **do GO-8C** é harmonizado.
- D-03 **não desbloqueia automaticamente** D-04: o N=12 (D-04) continua dependente de decisão independente.
- **Limitação registrada:** *"NT-05 substituído por painel de IAs independentes por indisponibilidade humana. Não há equivalência epistemológica com revisão humana."*

## 5. Implementação Autorizada

1. Criar/atualizar `decisions/D-03-NT05-DECISION.md` (este arquivo).
2. Criar/atualizar `decisions/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` (protocolo da revisão semântica mínima por painel de IAs em três abas).
3. Criar `review/REVIEW-PANEL-PROCEDURE.md` (passo a passo das três abas, modelos, prompts padrão, comparação de formulários) e a subpasta `review/materials/` (cópias de leitura dos materiais de entrada e da `C3_TAXONOMY.yaml`; originais NÃO alterados).
3. Criar a cópia harmonizada `scripts/BIP-VAL_REPORT.yaml` do GO-8C:
   - `NT-05: SUBSTITUTED_PARTIAL (2 independent AI reviewers)`
   - `verdict: PASS_PENDING_AI_PANEL`
   - NT-01..04 mantidos como PASS; FINDING-BIP-VAL-01 preservado.
4. Criar `scripts/test_d03_nt05.py` (e atualizar, se necessário, para refletir o painel de 2 IAs):
   - **T-D-03-01:** confirmar que NT-01..04 continuam PASS.
   - **T-D-03-02:** confirmar que o protocolo exige painel de 2 IAs independentes (unanimidade; divergência = STOP).
   - **T-D-03-03:** confirmar que `scripts/BIP-VAL_REPORT.yaml` reflete a substituição parcial.
5. Executar a suíte — **ALL PASS** obrigatório.
6. Registrar o resultado em `decisions/D-03-NT05-VALIDATION.md`.
7. Atualizar `TODO-GO-8C.md` (D-03 → DONE) e `decisions/ACTION-REGISTER.md`.

**Não é autorizada** nesta etapa: execução da revisão do painel (ocorrerá como etapa subsequente, com modelos/contextos limpos), alteração do parser, geração de novo manifesto/Lock, alteração de qualquer arquivo do GO-8B, início de D-04.

## 6. Referências

- `D-03-NT05-PROPOSAL.md` (proposta técnica, 2026-08-13 — Alternativa B recomendada e aprovada)
- `decisions/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` (protocolo desta decisão)
- `review/REVIEW-PANEL-PROCEDURE.md` (procedimento operacional das três abas)
- `review/materials/` (cópias de leitura dos itens a revisar)
- `experiments/validation/GO-8B/03-SYNTHETIC-TAXONOMY-C3.md` §4.1/§4.2/§4.3/§4.4 (congelado, referência histórica)
- `experiments/validation/GO-8B/decisions/NC-01-HUMAN-REVIEW-SUBSTITUTION.md` e `NC-04-NT-05-AUTOMATED-INDEPENDENT-REVIEW-RESULT.md` (referência histórica)
- `experiments/validation/GO-8B/decisions/FINDING-BIP-VAL-01.md` (referência histórica)
- `scripts/go8b/operational/BIP-VAL_REPORT.yaml` (referência histórica — não alterado)

---

## 7. Registro de Limitação (divulgação explícita)

> **"NT-05 substituído por painel de IAs independentes por indisponibilidade humana. Não há equivalência epistemológica com revisão humana."**
> - Modelo original: 3 validadores humanos independentes (03 §4.2).
> - Gate atual: 2 IAs independentes (abas separadas, arquiteturas/provedores diferentes, contextos limpos, acesso restrito a `review/`), unanimidade obrigatória, divergência = STOP. Agente executor não participa como revisor.
> - A decisão é de desenho/documentação do GO-8C; não modifica o congelado do GO-8B.

---

**Fim da decisão. D-03 DECIDED (Alternativa B — painel de 2 IAs independentes, ATUALIZADO). Nenhum arquivo do GO-8B alterado. Nenhum Lock gerado.**
