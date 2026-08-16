# FINDING-BIP-VAL-01 — Divergência: "47 termos" (congelado) vs. "52 termos" (operacional)

**Tipo:** Divergência metodológica/documental registrada (OBSERVED).
**Data do registro:** 2026-08-12
**Área afetada:** P2 — validação de neutralidade da taxonomia sintética C3 (BIP-VAL, NT-01).
**Artefato congelado:** `03-SYNTHETIC-TAXONOMY-C3.md` §4.1 (tabela NT-01) e §6 (T-C3-02).

---

## Descrição da divergência

O artefato congelado `03-SYNTHETIC-TAXONOMY-C3.md`:
- §4.1, tabela **NT-01 Léxico**: define o método como "Varredura por termos ECP-000..010 (lista fixa de **47 termos**)".
- §6, tabela **T-C3-02**: registra entrada "Taxonomia + lista **47 termos** ECP".
- §4.4, exemplo de `BIP-VAL_REPORT.yaml`: "0 ocorrências de **47 termos** ECP".

A compilação operacional do vocabulário ECP (usada na validação de zero-ECP dos materiais de entrada do P5 e na A2/NT-01) resulta em **52 termos** (lista em `pilot-input/validate_bip003.py` e `pilot-input/validate_bip007.py`, com `assert len == 52`). A diferença de 5 termos decorre da compilação ampliada decorrente do escopo efetivo do vocabulário ECP-000..010 utilizado no pipeline (ver DETALHE abaixo).

## Detalhe da contagem (52 termos compilados)

A lista operacional inclui, além do núcleo declarado (Problem, Goal, Claim, Knowledge, Assumption, Evidence, Decision, State, Artifact, L-0/L-1, P-1..P-12), as variantes léxicas e sinônimos compilados ao longo do P5 (ex.: `capacidade`, `objetivo`, `estado`, `evidencia`, `decisao`, `conhecimento`, `aprendizado`, `artefato`, `suposicao`, `problema`, `risco`, `contrato`, `entidade`, e equivalentes em inglês). A cifra "47" do congelado não foi atualizada após a compilação.

## Impacto

- **Nenhum bloqueio imediato:** NT-01 com 52 termos é uma varredura mais abrangente; 0 hits sob 52 termos implica 0 hits sob 47 termos (condição mais forte).
- **Requere esclarecimento em ciclo futuro:** o texto congelado deve ser harmonizado (47 → 52, ou referenciar a lista operacional como fonte da verdade) por decisão de governança.

## Estado

- **Estado: OBSERVED** — registrado, **não corrigido**.
- O artefato congelado **não foi alterado** (respeito ao Lock/Lock Protocol).
- Correção/metadados compatíveis tratados como pendência formal de governança (ciclo futuro).

## Conformidade

- Este registro não modifica o congelado; apenas documenta a divergência observada e o impacto nulo imediato.
- Verificável por: `grep -c "^\|\ `[a-z]" validate_bip00*.py` → contagem dos termos; comparação com §4.1/§4.4/§6 do congelado.