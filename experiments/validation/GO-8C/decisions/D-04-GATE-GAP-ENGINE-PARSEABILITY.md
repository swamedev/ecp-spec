# GO-8C — D-04 — Gate Gap: Parseabilidade pelo Engine (FINDING)

**Data:** 2026-08-14
**Ciclo:** GO-8C
**Tipo:** Finding registrado para auditoria (não é decisão de desenho; não altera o experimento).
**Contexto:** falha de 6 células na execução do estudo N=12 (BIP-009 condições A/B) causada por formato markdown não parseável pelo engine congelado — revelou uma lacuna de validação no gate de produção P4 (D-04.5).

---

## 1. O que aconteceu

- `study-input/BIP-009-chernobyl/atomic-facts/02-atomic-facts.md` foi produzido na fase **P3 (D-04.4)** em **formato tabela markdown** (`| # | Atomic fact | Fonte |`).
- O parser congelado do engine (`scripts/go8b/operational/pilot_engine.py:126-153`, `parse_atomic_facts`) exige:
  1. cabeçalho `## Fatos`;
  2. cada fato em linha `N. <texto> [ref]` terminando em `]` ou `]``.
- As linhas da tabela terminam em `|` → **0 fatos parseados** → `ValueError("no units parsed")` → `status=FAIL` nas condições A/B (que leem atomic facts). A condição C (narrativa) não foi afetada.

## 2. Por que o gate não detectou

O validador de produção **P4 (D-04.5)** — `validate_bip.py` (temp) — verificava apenas:
- **LEXICON:** zero ocorrências dos 52 termos ECP;
- **TRACE:** rastreabilidade das `[ref]` vs. `00-index.md`.

**NÃO verificava a parseabilidade do markdown pelo engine congelado.** Como BIP-009 passou no léxico e na rastreabilidade (e no NT-05 semântico, que é agnóstico de formato), o arquivo atravessou todos os gates sem ser detectado até a execução.

O formato de atomic facts **não é especificado** nos artefatos de produção (proposta `D-04-N12-PROPOSAL.md` e plano `D-04-N12-WORKPLAN.md` apenas exigem "lista de proposições atômicas, `[ref]` por fato" e "≥15 AF"). O padrão `## Fatos` + lista numerada foi seguido por convenção (cópia do template dos 7 BIPs existentes), não por exigência formal do gate.

## 3. Natureza do erro

**ISOLADO** (não sistemático): 1 de 12 arquivos de atomic facts; 1 de 5 novos BIPs; apenas as condições A/B. Os outros 4 novos BIPs (008, 010, 011, 012) e os 7 copiados usam o formato padrão.

## 4. Recomendação para ciclos futuros

- **Adicionar check de parseabilidade pelo engine** ao validador de produção: para cada `02-atomic-facts.md`, executar `parse_atomic_facts()` do engine congelado e exigir `len(facts) >= 15` e igualdade de ordem/texto com a fonte estruturada.
- **Especificar o formato markdown-máquina** de `02-atomic-facts.md` nos artefatos de produção (proposta/plano de trabalho), tornando o padrão `## Fatos` + `N. <texto> [ref]` uma exigência formal, não uma convenção.
- Registrar como **lição aprendida** no encerramento do GO-8C; sem custo metodológico para o estudo atual.

## 5. Status

- Registrado em `decisions/ACTION-REGISTER.md` (D-04.11) e `TODO-GO-8C.md`.
- **Nenhum arquivo do GO-8B alterado; nenhum outro artefato do Lock GO-8C alterado.**
