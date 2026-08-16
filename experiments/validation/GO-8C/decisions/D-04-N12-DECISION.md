# GO-8C — DECISION D-04 — N=12 (Estudo Confirmatório)

**Data:** 2026-08-14
**Ciclo:** GO-8C
**Decisor:** Governança GO-8C
**Decisão:** aprovar o desenho do estudo confirmatório **N=12**, conforme a proposta `D-04-N12-PROPOSAL.md`, com as 5 decisões formalizadas abaixo.
**Status:** DECIDED (implementação autorizada por etapas; execução experimental NÃO autorizada nesta decisão)
**Escopo:** dívida D-04 (N=12). Implementação autorizada SOMENTE dentro de `experiments/validation/GO-8C/`. Nenhum arquivo do GO-8B pode ser alterado; nenhum dado do GO-8B será reutilizado diretamente como observação do estudo.

---

## 1. Contexto

- O piloto GO-8B (N=7) tem potência ≈ 0.63 sob o cenário S1_PRIMARY; o pré-registro fixou **N=12** para potência ≈ 0.895 (≥ 0.80) — `06 §5.2/§5.4`, `08 §9`.
- A proposta `D-04-N12-PROPOSAL.md` (2026-08-14) recomendou a lista dos 12 BIPs, estrutura de diretórios, gate de autorização, riscos e dependências, e concluiu pela **viabilidade** do estudo integralmente no GO-8C.
- D-01 (C2 corrigido), D-02 (namespaces operacionais) e D-03 (NT-05 validado por painel de 2 IAs) já estão DONE — infraestrutura de desenho disponível.

## 2. Decisões Formalizadas

1. **Lista dos 12 BIPs aprovada:**
   - **001–007 (reuso de materiais):** Deepwater, Hyatt, Operation Warp Speed, Genoma, Ever Given/Suez, I-35W, Resposta Ebola.
   - **008–012 (novos):** Apollo 13, Chernobyl Unidade 4, Tacoma Narrows, Domino's Turnaround, Eyjafjallajökull.
2. **Re-execução dos 7 BIPs:** os materiais dos 7 BIPs existentes serão **copiados para o GO-8C** (proveniência registrada, originais GO-8B intocados), mas serão **reexecutados no novo pipeline do GO-8C**. **Nenhum dado do GO-8B será reutilizado diretamente como observação** (as 63 execuções do piloto NÃO entram no estudo N=12).
3. **Critério de sucesso (Go/No-Go):** aprovar **≥ 10 de 12 casos válidos** como Go, **desde que o pré-registro N=12 não estabeleça outro valor**; em caso de conflito, **prevalece o pré-registro**.
4. **Produção dos 5 novos materiais autorizada:** seguir o mesmo padrão dos anteriores (fontes oficiais, narrativa + atomic facts, **zero termos ECP**, validação lexical). A produção será executada **após aprovação do plano de trabalho** (cronograma e estrutura).
5. **NT-05 estendido:** o painel de revisão semântica da D-03 (2 IAs independentes, três abas, acesso restrito) será **estendido aos 5 novos materiais**, com os mesmos critérios e modelos.

## 3. Justificativa

- **Potência:** N=12 é o menor N da grade pré-especificada com potência ≥ 0.80 (0.895) sob S1_PRIMARY.
- **Independência:** re-execução integral no GO-8C preserva o estudo confirmatório de qualquer dependência dos resultados do piloto; os 7 BIPs mantêm a comparabilidade de desenho (mesmas condições/seeds/métricas), sem importar observações.
- **Diversidade:** os 5 novos cobrem domínios ausentes (Aeroespacial, Pequenos Negócios) e ampliam subdomínios (nuclear, aviação), respeitando a matriz P-0008 e o universo congelado SX-REAUDIT.
- **Continuidade de governança:** NT-05 segue o mecanismo já validado na D-03 (painel de IAs), estendido aos novos materiais; nenhum re-audit de taxonomia necessário.

## 4. Limites e Ressalvas

- Esta decisão **autoriza** a preparação do ambiente (diretórios, cópia dos 7 BIPs, plano de trabalho dos 5 novos) e a **produção dos 5 novos materiais** (após aprovação do plano).
- **NÃO autoriza:** execução experimental (108 reconstruções), análise estatística, geração de seeds, Lock do GO-8C ou qualquer alteração no GO-8B.
- O **pré-registro N=12** (desenho, seeds, Go/No-Go, plano de análise — replicando 06/07/08 do GO-8B) deverá ser escrito e **aprovado antes de qualquer execução**; se definir Go/No-Go diferente de "≥10 de 12", **o pré-registro prevalece**.
- Qualquer desvio de materiais/desenho deve seguir o protocolo de achados (GO-8C-OPENING-DECISION §8): registrar, PARAR, não corrigir automaticamente.
- GO-8B permanece CLOSED / LOCKED / FROZEN.

---

**Fim da decisão D-04. DECIDED — aguardando plano de trabalho dos 5 novos materiais para a próxima etapa autorizada.**
