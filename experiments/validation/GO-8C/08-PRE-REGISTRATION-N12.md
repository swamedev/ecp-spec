# GO-8C — Pré-registro do estudo confirmatório (N=12)

**Status:** PRÉ-REGISTRO — PENDING GOVERNANCE APPROVAL · HASH STATUS: **PENDING LOCK PROTOCOL**
**Data:** 2026-08-14
**Versão:** 1.0
**Ciclo:** GO-8C
**Governado por:** D-04 (N=12) · DECISION D-04-N12 · desenho metodológico replicado dos artefatos congelados GO-8B (06/07/08), com **N=12** e as adaptações aprovadas pela governança GO-8C.

> Este documento **pré-registra** o desenho e o plano de análise do estudo confirmatório GO-8C (N=12), replicando o desenho metodológico congelado do GO-8B (entregáveis 06, 07, 08). **Não introduz nenhum parâmetro novo fora do aprovado; não contém hashes finais; não constitui execução experimental; não gera seeds nem aplica o Lock Protocol.**

---

## 1. Declaração de Não-Execução

- **Nenhum experimento foi executado** para elaborar este pré-registro.
- **Nenhum dado experimental foi criado ou coletado.**
- **Nenhuma seed foi gerada** (valores de seed permanecem `PENDING LOCK PROTOCOL`; somente o método de geração é pré-especificado).
- **Nenhum hash final foi gerado.** Todos os hashes permanecem `PENDING LOCK PROTOCOL`.
- **Lock Protocol não aplicado.**
- As simulações metodológicas do GO-8B (potência — seed `20260811`; cobertura do bootstrap — seed `20260812`) **não** entram como observações deste estudo.

---

## 2. Contexto e Objetivo (referência: GO-8B 06 §1.3.2)

Comparar a similaridade estrutural `S_struct` do grafo reconhecido (espaço sintético da condição) com o grafo canônico ECP, entre as **3 condições de reconstrução**, sobre os **12 BIPs válidos**, para avaliar a utilidade da taxonomia sintética C3 no estudo confirmatório GO-8C (N=12), com potência pré-registrada ≈ 0.895 (≥ 0.80) sob o cenário S1_PRIMARY.

---

## 3. Desenho Experimental (Pré-registrado — Fixado)

| Parâmetro | Especificação | Fonte |
|---|---|---|
| **Unidade experimental** | **BIP/Caso** | GO-8B 06 §1.3 |
| **N (tamanho de amostra)** | **12 BIPs** (001–012); análise prossegue com ≥ 10 válidos (D-04 decisão 3; salvo se este pré-registro for mais restritivo) | D-04; GO-8B 07 §8 adaptado |
| **Seeds por célula** | **3 seeds por (BIP × condição)** | GO-8B 06 §1.3.1 (R5 M-3) |
| **Agregação** | `cell_value = median(seed_1, seed_2, seed_3)` | GO-8B 06 §1.3.1 |
| **Condições** | **3** — (A) Cega pura (só Atomic Facts) · (B) Cega + Taxonomia C3 · (C) Não-cega (narrativa completa) | GO-8B 06 §1.2 |
| **Medida repetida** | seed = observação repetida dentro de BIP × condição; **não é unidade independente** | GO-8B 06 §1.3.1 |
| **N nunca é multiplicado** por avaliadores ou seeds | `N = nº de BIPs válidos` | GO-8B 06 §1.3 |
| **Total de execuções** | **12 × 3 × 3 = 108 reconstruções** (12 BIPs × 3 condições × 3 seeds) | D-04; cálculo de execuções |

**BIPs (12):**
- **001–007 (reuso de materiais, reexecutados no GO-8C):** BIP-001 Deepwater Horizon · BIP-002 Hyatt Regency · BIP-003 Operation Warp Speed · BIP-004 Genoma Humano · BIP-005 Ever Given/Suez · BIP-006 I-35W Bridge · BIP-007 Resposta Ebola.
- **008–012 (novos, produzidos no GO-8C):** BIP-008 Apollo 13 · BIP-009 Chernobyl Unidade 4 · BIP-010 Tacoma Narrows · BIP-011 Domino's Turnaround · BIP-012 Eyjafjallajökull.

**Taxonomias e namespaces (GO-8C, D-01/D-02):** C1=T_ECP (`ECP`) · C2=T_PERM (`CAT`) · C3=T_SYNTH (`SYN`) · C4=T_NULL (`NULL`). Namespace operacional: **A → CAT, B → SYN, C → CAT** (D-02, sem equivalências NULL≡CAT nem CAT≡SYN/ECP). O campo `taxonomy_namespace` é **obrigatório** e exclusivo por reconstrução; mistura de namespaces → `NAMESPACE_MIX` (rejeição). Nenhum mapping entre namespaces.

---

## 4. Variáveis (idênticas ao GO-8B)

| Variável | Papel | Definição | Fonte |
|---|---|---|---|
| **S_struct** | **Primária / confirmatória** | Similaridade topológica WL Subtree Kernel (anonimização `"neutral"`), ∈ [0,1] | GO-8B 05 §3 |
| **S_sem** | **Exploratória** | Alinhamento semântico contínuo (Hungarian); **não confirmatória** | GO-8B 05 §4 |
| **K = α·S_struct + (1−α)·S_sem** | Exploratória | α = 0.6 pré-especificado | GO-8B 05 §6 |

---

## 5. Hipóteses (Pré-registradas — GO-8B 06 §2)

### 5.1 Omnibus (primária)
> **H₀:** A distribuição de S_struct é idêntica nas 3 condições (A, B, C) sobre os BIPs válidos.
> **H₁:** Pelo menos uma condição difere.

### 5.2 Pós-hoc (condicionadas à rejeição de H₀)
| Comparação | Hipótese |
|---|---|
| B vs A | S_struct(B) > S_struct(A) — taxonomia C3 adiciona estrutura |
| C vs A | S_struct(C) > S_struct(A) — narrativa completa (upper bound) |
| C vs B | S_struct(C) ≥ S_struct(B) |

### 5.3 Exploratórias (não confirmatórias)
Interação Caso × Condição; efeito avaliador; S_sem diagnóstico.

---

## 6. Plano de Análise Estatística (Pré-registrado — Fixado)

| Elemento | Especificação | Fonte |
|---|---|---|
| **Teste global (primário)** | **Friedman** (df = 2) | GO-8B 06 §3 |
| **α** | **0.05** | GO-8B 06 §3.3 |
| **Pós-hoc** | **Wilcoxon signed-rank pareado, bilateral** | GO-8B 06 §4 |
| **Correção** | **Holm-Bonferroni** (3 comparações) | GO-8B 06 §4.1 |
| **Tamanho de efeito** | Kendall's W (omnibus); r_rb e Cliff's δ (pós-hoc) | GO-8B 06 §3.4, §4.2 |
| **ICs 95%** | Bootstrap percentil B=10.000 (pareado); **IC exato da mediana reportado ao lado** do IC percentil (mitigação STAT-08) | GO-8B 06 §4.3, §4.3.1 |
| **Nenhuma decisão unilateral** após resultados | proibido | GO-8B 06 R3-04 |
| **TOST / equivalência** | **NÃO vigente** (sem Δ aprovada; TOST não executado) | GO-8B 06 §8; R5-GOV-03 |

**Ordem de execução** (GO-8B 06 §7): data check → agregação (mediana das 3 seeds) → descritiva → Friedman → pós-hoc (se H₀ rejeitada) → exploratório → sensibilidade → relatório.

**Sensibilidade (GO-8B 06 §7, R5-GOV-04):** STAT-04 (não winsorizar; reportar com/sem outliers; reexecutar sem outliers IQR×1.5) · STAT-06 (exploratório sem controle formal de família) · STAT-08 (B=10.000; reportar IC exato da mediana ao lado; N=12 mediana ≈0.93–0.94 e diferença pareada ≈0.97 — ver tabela GO-8B 06 §4.3.1) · STAT-09 (excluir 1 caso por par dependente; sem modelo misto).

---

## 7. Potência (Pré-registrada — Go/No-Go N=12)

- **Potência N=12: ≈ 0.895** (IC 95% 0.886–0.903) sob o cenário S1_PRIMARY pré-especificado (μ=(0.50, 0.60, 0.66); σ_b=0.12, σ_e=0.08, σ_s=0.06; 3 seeds/célula; mediana; Friedman; α=0.05; B=5.000; seed `20260811`) — **GO-8B 06 §5.2.**
- N=12 é o **menor N da grade pré-especificada com potência ≥ 0.80** (0.895) — GO-8B 06 §5.3.
- Esta potência é **justificativa de desenho** do estudo confirmatório N=12 (não justificativa retroativa de N=7 do piloto).

---

## 8. Critérios de Exclusão e Go/No-Go

- **Exclusões automáticas:** aplicam-se os critérios do GO-8B 07 (FP-01..08 piloto, FC-01..07 caso, FE-01..05 avaliador, FR-01..06 reconstrução), com as seguintes adaptações de limiar para N=12:
  - **Go/No-Go para análise (D-04 decisão 3):** **≥ 10 de 12 casos válidos**; matriz N×3 completa; nenhum `FAIL-PILOT`.
  - Nenhuma exclusão manual; exclusões 100% determinísticas (regras 07).
- **Insuficiência:** < 10 casos válidos → "STUDY INCONCLUSIVE — insufficient data"; **não** executar análise estatística.
- **Prevalência do pré-registro:** se este pré-registro definir Go/No-Go diferente de "≥ 10 de 12", este pré-registro prevalece (D-04 decisão 3). **Valor fixado: ≥ 10 de 12.**

---

## 9. Critérios de Interpretação (Decision Rules — GO-8B 06 §10)

| Cenário | Interpretação |
|---|---|
| Friedman p<0.05 **E** B>A (Holm) | Evidência a favor da utilidade de C3 |
| Friedman p<0.05 **E** C>A **MAS** B≈A | C3 não justificada; rever design |
| Friedman p≥0.05 | Nenhuma evidência; **NÃO** é equivalência; reportar (N=12 ≈ 0.895 — potência adequada) |
| Friedman p<0.05 **MAS** A>B | C3 prejudica; falha crítica |
| TOST | **não executado** (sem Δ aprovada) |

---

## 10. Configurações de Reprodutibilidade (Método — sem hashes/valores finais)

```yaml
seed_method: PCG64(seed_master)
seed_master:
  value: PENDING LOCK PROTOCOL      # a definir/aprovar pela governança antes do Lock
  type: uint64
derivation: |
  Para cada (bip, condicao), 3 seeds geradas deterministicamente a partir de
  seed_master via PCG64, em stream isolado por (bip, condicao).
  Nenhuma seed é reutilizada entre streams; nenhuma seed é derivada de resultados.
  Total: 12 x 3 x 3 = 108 seeds (3 por célula).
seed_statistics:
  value: PENDING LOCK PROTOCOL      # stream isolado da análise estatística (mirror GO-8B 06 §9.1)
  type: uint64
seed_c2:
  value: 258915 (hex 0x3f363)       # seed oficial da permutação C2 (D-01, corrigida)
  type: uint64
seed_generation:
  value: 12088763053434307680, type: uint64   # geração C3, se estocástico (GO-8B 03 §3.3)
seed_power_simulation:  { value: 20260811, type: uint64 }   # metodológica GO-8B (06 §9.2)
seed_coverage_bootstrap: { value: 20260812, type: uint64 }  # metodológica GO-8B (06 §4.3.1)
```

**Isolamento de streams:** cada seed tem uso exclusivo; nenhuma reutilização entre streams. **Geração de seeds NÃO executada** — aguardando aprovação da governança + Lock GO-8C.

**Software:** Python 3.11+; `scipy.stats` (friedmanchisquare, wilcoxon), `numpy`, `pandas`, `scikit-posthocs` (Holm); scripts no pipeline do GO-8C.

---

## 11. Compromissos Pré-Registrados (O que está comprometido / proibido)

**Comprometido:** Friedman primário (df=2, α=0.05); Wilcoxon bilateral + Holm-Bonferroni; unidade BIP/Caso; N=12; 3 seeds/célula; mediana; sensibilidade STAT-04/06/08/09; potência N=12 ≈ 0.895; Go/No-Go ≥ 10 de 12; Kendall W, r_rb, Cliff δ; bootstrap B=10.000; IC exato da mediana ao lado do percentil.

**Proibido neste estudo:** TOST (sem Δ aprovada); winsorização; transformação de S_struct; modelo misto; tuning de parâmetros pós-resultados; decisões unilaterais; correção de N por resultados; tratar simulações metodológicas como observações; preencher hashes fora do Lock Protocol; **gerar seeds antes da autorização; aplicar Lock antes da autorização**.

---

## 12. Gate de Autorização

- **Execução da geração de seeds:** **SOMENTE após** aprovação formal deste pré-registro pela governança.
- **Lock GO-8C (manifesto + hashes):** **SOMENTE após** aprovação do pré-registro e decisão explícita da governança, em etapa separada autorizada.
- **Execução experimental (108 reconstruções) e análise estatística:** **SOMENTE após** o Lock GO-8C e decisão explícita de execução.
- Qualquer desvio deve seguir o protocolo de achados (registrar, PARAR, não corrigir automaticamente).

---

## 13. Consistência com o GO-8B (verificação — artefatos 06/07/08)

Verificação documental contra os artefatos congelados do GO-8B (originais não alterados):

| Requisito GO-8B | Adaptação GO-8C (N=12) | Consistente? |
|---|---|---|
| Unidade experimental = BIP/Caso; N = BIPs válidos; seeds como repetição intra-unidade, mediana por célula (06 §1.3) | Mantido integralmente | ✅ |
| 3 seeds por (BIP × condição); agregação por mediana (06 §1.3.1) | Mantido; total 108 execuções | ✅ |
| Condições A/B/C e taxonomias C1–C4 (06 §1.2; 02 §1) | Mantido; namespace operacional A→CAT, B→SYN, C→CAT (D-02) | ✅ |
| S_struct primária; S_sem exploratória; K α=0.6 (05 §3/§4/§6) | Mantido | ✅ |
| Friedman primário df=2 α=0.05; Wilcoxon bilateral; Holm; W/r_rb/Cliff δ; bootstrap B=10.000; IC exato da mediana ao lado (06 §3–§4.3.1) | Mantido | ✅ |
| TOST não vigente; sem Δ aprovada (06 §8; R5-GOV-03) | Mantido | ✅ |
| Potência N=12 ≈ 0.895 ≥ 0.80 (06 §5.2/§5.4; 08 §9) | N=12 é o desenho oficial | ✅ |
| Go/No-Go análise (07 §8): ≥ 5 de 7, ≥ 4 domínios | Adaptado por D-04: **≥ 10 de 12** (com prevalência do pré-registro) | ✅ (decisão de governança D-04) |
| Exclusões automáticas FP/FC/FE/FR (07 §§2–5) | Mantido; nenhuma exclusão manual | ✅ |
| Pré-registro não gera seeds/hashes/Lock (08 §1) | Mantido — tudo `PENDING LOCK PROTOCOL` | ✅ |
| Seed C2 (02 §4): piloto usava `11473621728585666159` | **Corrigido em GO-8C (D-01):** seed oficial `258915` (0x3f363) reproduz a permutação congelada; antiga = `HISTORICAL-NON-REPRODUCING` | ✅ (D-01 validada 7/7) |

**Conclusão de consistência:** o pré-registro N=12 replica o desenho congelado do GO-8B (06/07/08) com as **únicas adaptações aprovadas pela governança GO-8C**: N=12, Go/No-Go ≥ 10 de 12 (D-04 decisão 3), seed C2 corrigida (D-01) e namespace operacional (D-02). Nenhum parâmetro metodológico adicional foi introduzido.

---

## 14. Status e Próximos Passos

- **HASH STATUS:** todos os artefatos e o próprio pré-registro permanecem **PENDING LOCK PROTOCOL**.
- **Próxima parada obrigatória:** **aprovação formal deste pré-registro pela governança GO-8C**.
- Após aprovação: **etapa separada de Lock GO-8C** (manifesto + hashes) em etapa autorizada.
- Após o Lock: **autorização explícita de execução** (108 reconstruções), depois validação (07 adaptado ao N=12), análise (06 exato), relatório e encerramento.

---

**Fim do pré-registro N=12. Nenhum experimento executado. Nenhuma seed gerada. Nenhum dado experimental coletado. Nenhum hash final gerado. Lock Protocol não aplicado.**
