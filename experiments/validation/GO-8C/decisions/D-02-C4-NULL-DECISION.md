# GO-8C — DECISION D-02 — C4 / NULL (Namespace Operacional das Condições A/C)

**Data:** 2026-08-13
**Ciclo:** GO-8C
**Decisor:** Governança GO-8C
**Decisão:** **Opção 2** — formalizar o uso de **CAT** (C2) como namespace operacional das condições A e C, mantendo **SYN** (C3) na condição B.
**Status:** DECIDED
**Escopo:** dívida D-02 (C4/NULL). Implementação autorizada SOMENTE dentro de `experiments/validation/GO-8C/`. Nenhum arquivo do GO-8B pode ser alterado.

---

## 1. Contexto

- O parser congelado `graph_from_reconstruction.py` (linhas 84-85) rejeita o namespace `NULL` (C4/T_NULL) com erro `NAMESPACE_MIX`.
- A especificação congelada `04-GRAPH-FROM-RECONSTRUCTION.md` §1.1 declara que C4/T_NULL "não produz grafo no espaço sintético e **não é processado** por este parser".
- A proposta `D-02-C4-NULL-PROPOSAL.md` (2026-08-13) diagnosticou que a incompatibilidade é um **gap de desenho** (intenção de A/C sem taxonomia × fronteira de processabilidade do pipeline), **não um bug** do parser.
- O piloto GO-8B já usou operacionalmente **A=CAT, B=SYN, C=CAT** (decisão `NAMESPACE-OPERATIONAL-DECISION.md`, 2026-08-13), preservando 63 execuções.

## 2. Decisão (Opção 2)

1. **As condições A e C usam o namespace `CAT` (C2) como operacional** no GO-8C; a condição B usa `SYN` (C3).
2. **O parser `graph_from_reconstruction.py` permanece inalterado.**
3. **NULL continua significando "não processável" no parser** (fiel à especificação congelada 04 §1.1).
4. **Não é criada equivalência `NULL` ≡ `CAT`.**
5. **Não é criada equivalência `CAT` ≡ `SYN`/`ECP`.** CAT é uma **representação operacional** para A/C — rótulos opacos e permutados que preservam a cegueira — e não uma equivalência semântica entre namespaces.
6. **A decisão vale para o GO-8C e para o estudo confirmatório derivado dele (N=12).**
7. **Opção 3 registrada como roadmap/pesquisa futura**, sem prazo e **sem execução agora**: sonda de viabilidade para processamento real de NULL (codificação livre) exigiria novo ciclo decisório e nova validação.
8. **Qualquer mudança futura para processamento real de NULL** exige **novo ciclo decisório e nova validação**, fora do escopo desta decisão.

## 3. Justificativa

- **Cegueira preservada:** `CAT-XX` são rótulos opacos (02 §3) — o avaliador não conhece a correspondência com ECP. A manipulação cega das condições A/C permanece íntegra.
- **Continuidade:** mantém comparabilidade com as 63 execuções validadas do GO-8B e permite que o estudo N=12 seja derivado sem ruptura de desenho.
- **Respeito à especificação:** a fronteira de 04 §1.1 (NULL não processado) é mantida; a decisão é de **desenho/documentação**, não de alteração de parser.
- **Custo mínimo e zero risco de infraestrutura.**

## 4. Limites e Ressalvas

- D-02 **não desbloqueia automaticamente** D-03 e D-04: cada dívida permanece uma **decisão independente**.
- O **N=12 (D-04)** só deve ser efetivamente fixado depois que o desenho operacional final estiver estabilizado.
- Ordem proposta: D-02 → testes T-D-02-01..03 → validação → DONE; depois D-03 (análise independente); por fim D-04 (desenho confirmatório N=12 → potência → decisão → novo pré-registro/Lock).

## 5. Implementação Autorizada

1. Criar testes `scripts/test_d02_namespace.py`:
   - **T-D-02-01:** o parser rejeita `NULL` com `NAMESPACE_MIX` (conforme especificação).
   - **T-D-02-02:** o parser aceita `CAT` e produz grafo válido com rótulos `CAT-XX`.
   - **T-D-02-03:** os namespaces operacionais das condições A, B, C no GO-8C são `CAT`, `SYN`, `CAT`.
2. Executar a suíte — **ALL PASS** obrigatório.
3. Registrar o resultado em `decisions/D-02-C4-NULL-VALIDATION.md`.
4. Atualizar `TODO-GO-8C.md` (D-02 → DONE; Opção 3 como roadmap) e `decisions/ACTION-REGISTER.md`.

**Não é autorizada** nesta etapa: alteração do parser, processamento real de NULL, geração de novo manifesto/Lock, alteração de qualquer arquivo do GO-8B.

## 6. Referências

- `D-02-C4-NULL-PROPOSAL.md` (proposta técnica, 2026-08-13)
- `experiments/validation/GO-8B/04-GRAPH-FROM-RECONSTRUCTION.md` §1.1 (congelado, referência histórica)
- `scripts/go8b/operational/graph_from_reconstruction.py:84-85` (referência histórica)
- `experiments/validation/GO-8B/decisions/NAMESPACE-OPERATIONAL-DECISION.md`
- `experiments/validation/GO-8B/02-C2-PERMUTATION.md` §3/§8
- Hash do manifesto GO-8B (referência histórica): `c55799d895a4f73888713a8538c6b9a6c5df1d7cde71c88141e16b9e9b216636`

---

**Fim da decisão. D-02 DECIDED (Opção 2). Nenhum arquivo do GO-8B alterado. Nenhum Lock gerado.**
