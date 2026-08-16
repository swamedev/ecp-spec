# GO-8D — PRÉ-REGISTRO DO NOVO CICLO CONFIRMATÓRIO (DV3, N=30)

**Título:** Estudo confirmatório da DV3 com N=30 BIPs — superioridade B<A e equivalência A−C (Δ=0.05)
**Versão:** v1.0 (FINAL)
**Data:** 2026-08-15
**Status:** **APROVADO pela governança** (2026-08-15) — fechado; pendente apenas o Lock do novo ciclo
**Base de desenho:** D-MV-03-GOVERNANCE-DESIGN-DECISION.md (APPROVED) · D-MV-01 (DV3) · D-MV-02 (N=30)
**Estado do programa:** GO-8D CLOSED · GO-8B/GO-8C FROZEN · nenhum novo Lock

---

## 1. Objetivo e Hierarquia das Hipóteses

**Pergunta primária (superioridade B<A):** a condição cega + taxonomia C3 (B) tem DV3 menor que a
cega pura (A)? (Resultado observado no GO-8D; hipótese de utilidade da C3 já rejeitada — este ciclo
consolida com N maior e métrica calibrada.) Testes: **Friedman** (omnibus) + **Wilcoxon B−A**.

**Pergunta secundária (equivalência TOST A−C):** a condição não-cega (C) é equivalente à condição
cega pura (A) na DV3, dentro da margem Δ=0.05? Teste: **TOST A−C com Δ=0.05**.

**Hipótese complementar:** comparação **B vs C** (Wilcoxon B−C), informativa (interpretação do
efeito da C3 no contexto não-cego).

## 2. Desenho Experimental

| Parâmetro | Especificação |
|---|---|
| **Desenho** | Medidas repetidas em pares: 30 BIPs × 3 condições (A, B, C) × 3 seeds |
| **Total de execuções** | 30 × 3 × 3 = **270** |
| **Unidade de análise** | BIP (célula = **mediana das 3 seeds**) |
| **N** | **30 BIPs** — **justificado pela hipótese primária** (superioridade B<A): com o efeito observado no GO-8D (δ_BA ≈ −0.0374 em DV3), N=30 garante poder ≥ 0.80 para Wilcoxon B−A **com folga**, e ainda cobre o teste mais exigente do plano (TOST A−C, que exige N=30 para poder 0.804; D-MV-02) — ver §4 |
| **Condições** | A = cega pura (atomic facts, namespace CAT) · B = cega + taxonomia C3 corrigida (SYN) · C = não-cega (narrativa completa, namespace CAT) |
| **Seeds** | 3 seeds determinísticas por célula; `seed_master` a definir no pré-registro final (distinto de 20260815) |
| **Pipeline** | reprojetado GO-8D (D-03) — determinístico por (BIP, condição); engine `pilot_engine.py` + `wl_kernel.py` |

## 3. Métrica Primária

**DV3 = (conf + ged_ecp + ent_n12) / 3** (pesos 1:1:1; clamp [0,1])

| Componente | Definição | Referência/Normalização |
|---|---|---|
| **conf** | fidelidade por fato = média da confiança das entidades | inalterado |
| **ged_ecp** | similaridade GED (w_edge=0.5) do grafo reconstruído vs **grafo de referência ECP comum** (G_ECP, 9 nós canônicos) | **referência única para A/B/C** |
| **ent_n12** | entropia normalizada `H / log(12)` da distribuição de categorias sintéticas na reconstrução | **denominador comum 12** (não mais 9/12) |

**Métricas secundárias:** componentes individuais `conf`, `ged_ecp`, `ent_n12`; `H` bruta; `k_obs`
(categorias distintas observadas); `nodes`/`edges`.

## 4. Plano de Análise Estatística (pré-registrado)

**Ordenação por hierarquia das hipóteses (Decisão da governança, 2026-08-15): primária →
secundária → complementar.**

| Passo | Teste | Detalhe |
|---|---|---|
| 1 | **Data check + validação** | 270 linhas; células completas (3 seeds); DV3 ∈ [0,1]; namespace por condição; taxonomy_sha256 por execução; gate D-04 (parseabilidade) nos 30 BIPs; aplicação do Go/No-Go (§5) |
| 2 | **Agregação** | célula = mediana das 3 seeds; matriz 30×3 |
| 3 | **HIPÓTESE PRIMÁRIA — omnibus** | **Friedman** (df=2, α=0.05) + Kendall's W + IC bootstrap — teste gate da hierarquia |
| 4 | **HIPÓTESE PRIMÁRIA — post-hoc B−A** | **Wilcoxon signed-rank pareado bilateral** **B−A** + Holm-Bonferroni (com A−C e B−C); r_rb, Cliff δ + IC bootstrap |
| 5 | **HIPÓTESE SECUNDÁRIA — TOST A−C** | **A−C, Δ=0.05** — two one-sided tests pareados (t pareado, α=0.05) + bootstrap percentil pareado B=10.000 (IC da diferença ⊂ (−0.05, +0.05)) |
| 6 | **HIPÓTESE COMPLEMENTAR — B vs C** | **Wilcoxon B−C** (pós-Holm, informativo); reportar TOST A−B e B−C como informativos |
| 7 | **ICs** | bootstrap percentil pareado (B=10.000, seed_statistics isolada); IC exato da mediana ao lado |
| 8 | **Sensibilidade** | sem outliers (IQR×1.5); drop de 1 caso por vez; sem modelo misto (STAT-09); sem winsorização (STAT-04) |

**Decisão inferencial (por hierarquia):**
- **Primária — Superioridade B<A:** Friedman significativo (α=0.05) **e** Wilcoxon B−A pós-Holm
  significativo com direção B<A → **confirmar o efeito negativo da C3 na DV3**. Se Friedman n.s. →
  sem confirmação da primária (reportar exploratório para as demais).
- **Secundária — Equivalência A−C:** interpretada **somente** com a primária concluída; se IC 95%
  da diferença pareada A−C ⊂ (−0.05, +0.05) **e** ambos os testes one-sided rejeitam em α=0.05 →
  declarar **equivalência dentro de Δ=0.05**.
- **Complementar — B vs C:** informativa, não decide o estudo.
- **Nenhuma métrica selecionada por p-valor; nenhuma decisão unilateral (R3-04).**

## 5. Critérios de Sucesso e de Parada (Go/No-Go)

### 5.1 Go/No-Go metodológico (pré-especificado; Decisão da governança, 2026-08-15)

- Matriz N×3 completa; 270/270 execuções sem FAIL; gates D-04 (parseabilidade) + validação de dados PASS.
- **Não compensar faltas com mais seeds nem imputar células ausentes.**
- **Critério por faixa de BIPs válidos (N_válidos):**

| N_válidos | Decisão | Análise |
|---|---|---|
| **≥ 27/30** | **GO — análise confirmatória** conforme este pré-registro (hierarquia §1/§4) | Inferencial completa |
| **10–26/30** | **NO-GO confirmatório** — o pré-registro NÃO é seguido de forma confirmatória | **Apenas relatório exploratório/descritivo** (ICs, efeitos, sem testes confirmatórios de decisão) |
| **< 10/30** | **STOP** | **Sem análise inferencial planejada**; reporte operacional + proposta de nova rodada à governança |

### 5.2 Regras de parada antecipada
- Nenhuma análise intermediária; **sem** parada antecipada por análise sequencial (desenho fixo).
- Parada operacional apenas por falha de infraestrutura/validação (reportada, não inferencial).

### 5.3 Interpretação pré-especificada (somente quando GO, N_válidos ≥ 27/30)
| Cenário (primária) | Cenário (secundária) | Conclusão |
|---|---|---|
| B<A significativo pós-Holm | TOST A−C equivalente (IC ⊂ Δ) | **C3 sem utilidade confirmada**; A≈C em DV3 |
| B<A significativo pós-Holm | TOST A−C não equivalente | C3 sem utilidade confirmada; A e C diferem > Δ na DV3 (reportar direção/magnitude) |
| B<A não significativo | qualquer | efeito negativo da C3 **não replicado** com N=30 (reavaliar hipótese; secundária/complementar reportadas como informativas) |
| Friedman n.s. | qualquer | **sem confirmação da hipótese primária**; reportar exploratório para as demais |

## 6. Regras de Execução e Validação

1. **Determinismo:** pipeline reexecutado exatamente como GO-8D (D-03); célula independente da seed
   (seeds registradas para rastreabilidade); re-derivação deve reproduzir os valores (validação cruzada).
2. **taxonomy_sha256 por execução:** B (condição B) = hash da C3 corrigida; A/C = hash da C2
   operacional; conferência na validação.
3. **Namespaces:** A/C → CAT (C2_PERMUTATION.yaml); B → SYN (C3_TAXONOMY.yaml corrigida).
4. **Gate D-04 (parseabilidade):** todos os 30 BIPs devem passar (atomic facts parseáveis no
   formato canônico).
5. **Nenhum arquivo congelado (GO-8B/GO-8C/Lock GO-8D) pode ser alterado.**
6. **Falha de qualquer execução** → STOP e reporte (não imputar, não re-amostrar seeds).

## 7. BIPs

### 7.1 Os 12 BIPs existentes (reuso com re-execução no novo pipeline)

| # | BIP | Caso | Domínio |
|---|---|---|---|
| 1 | BIP-001 | Deepwater Horizon (2010) | Petróleo/energia |
| 2 | BIP-002 | Hyatt Regency (1981) | Engenharia civil |
| 3 | BIP-003 | Operation Warp Speed (2020–21) | Saúde pública |
| 4 | BIP-004 | Genoma Humano (1990–2003) | Genética/ciência |
| 5 | BIP-005 | Ever Given / Suez (2021) | Transporte marítimo |
| 6 | BIP-006 | I-35W Bridge (2007) | Engenharia civil |
| 7 | BIP-007 | Resposta Ebola (2014–16) | Saúde pública |
| 8 | BIP-008 | Apollo 13 (1970) | Aeroespacial |
| 9 | BIP-009 | Chernobyl (1986) | Nuclear |
| 10 | BIP-010 | Tacoma Narrows (1940) | Engenharia civil |
| 11 | BIP-011 | Domino's Turnaround (2009–10) | Pequenos negócios |
| 12 | BIP-012 | Eyjafjallajökull (2010) | Aviação/logística |

> Reexecução no pipeline DV3 (conf + ged_ecp + ent_n12). Os valores do GO-8D (DV_confirm) **não**
> são observações deste ciclo — o ciclo novo usa **DV3** (métrica recalibrada), portanto todo o
> conjunto é reexecutado.

### 7.2 Os 18 novos BIPs propostos (diversidade + fontes oficiais acessíveis)

**Critérios de seleção:** (a) não usados em GO-8B/GO-8C/GO-8D; (b) cobertura de domínios variados,
incluindo domínios **não representados** nos 12 atuais (indústria química, gestão de emergências,
água/saneamento, mineração, finanças/corporativo, biotecnologia, segurança automotiva, incêndio
edifícios, segurança alimentar); (c) existência de **fontes oficiais acessíveis** (relatórios
governamentais/agências, comissões de inquérito) passíveis de download.

| # | Novo BIP | Caso | Domínio | Fontes oficiais |
|---|---|---|---|---|
| 13 | BIP-013-bhopal | Desastre de Bhopal (1984) | Indústria química | ICMR (Relatório Técnico BGDRC, PDF) · Relatório Varadarajan (NTIS PB89115380) · Grupo de Ministros (Gov. Índia) |
| 14 | BIP-014-tmi | Three Mile Island (1979) | Nuclear | NRC · Comissão Kemeny · GAO |
| 15 | BIP-015-challenger | Challenger STS-51-L (1986) | Aeroespacial | Comissão Rogers (NASA History) · GAO |
| 16 | BIP-016-columbia | Columbia STS-107 (2003) | Aeroespacial | CAIB Report (NASA) |
| 17 | BIP-017-katrina | Furacão Katrina (2005) | Gestão de emergências | USACE Performance Evaluation · White House Federal Response · FEMA |
| 18 | BIP-018-flint | Crise da água de Flint (2014–16) | Água/saúde pública | Michigan Civil Rights Commission · EPA · DOJ |
| 19 | BIP-019-fukushima | Fukushima Daiichi (2011) | Nuclear | IAEA · NAIIC · TEPCO |
| 20 | BIP-020-grenfell | Incêndio Grenfell Tower (2017) | Segurança de edifícios | Grenfell Tower Inquiry (Reino Unido) |
| 21 | BIP-021-vajont | Desastre de Vajont (1963) | Engenharia civil/barragens | Inquérito parlamentar italiano · ISPRA |
| 22 | BIP-022-max8 | Boeing 737 MAX (2018–19) | Aviação | NTSB · FAA · House T&I Committee |
| 23 | BIP-023-mariana | Rompimento de Mariana (2015) | Mineração/ambiente | Fundação Renova · Estado de MG · agências |
| 24 | BIP-024-dieselgate | VW Dieselgate (2015) | Automotivo/ambiente | EPA (NOV) · DOJ (acordo) |
| 25 | BIP-025-wellsfargo | Contas falsas Wells Fargo (2016) | Setor financeiro | CFPB · OCC · relatório do Senado |
| 26 | BIP-026-theranos | Theranos (2015–18) | Biotecnologia/saúde | SEC · CMS · DOJ |
| 27 | BIP-027-opioids | Crise dos opioides/Purdue (2007–19) | Farmacêutica | DOJ · CDC · tribunais |
| 28 | BIP-028-enron | Escândalo Enron (2001) | Corporativo/finanças | SEC · Congresso dos EUA |
| 29 | BIP-029-takata | Airbags Takata (2008–17) | Segurança automotiva | NHTSA · DOJ |
| 30 | BIP-030-concordia | Costa Concordia (2012) | Transporte marítimo | Inquérito italiano · autoridades portuárias |

**Justificativa de diversidade:** os 18 novos cobrem 10 domínios novos (química, emergências,
água/saneamento, mineração, financeiro/corporativo, biotecnologia, farmacêutica, segurança
automotiva, incêndio em edifícios, barragens) e reforçam domínios existentes (nuclear com TMI +
Fukushima; aeroespacial com Challenger + Columbia; aviação com 737 MAX; marítimo com Concordia),
assegurando variabilidade de estrutura de grafos e de complexidade de atomic facts.

> **Aviso:** a disponibilidade exata de URLs e a acessibilidade dos PDFs serão confirmadas na fase
> de aquisição (planejada), **após aprovação da lista pela governança**. Nenhuma coleta agora.

## 8. Regras de Governança e Conformidade

1. Este pré-registro é **v1.0 FINAL APROVADO** pela governança (2026-08-15); **não** constitui
   autorização de execução.
2. A execução exige: **Lock do novo ciclo** → aprovação do seed_master → autorização de execução.
3. Nenhum arquivo congelado (GO-8B/GO-8C/Lock GO-8D) pode ser alterado.
4. Métricas não serão selecionadas por p-valor; pesos 1:1:1 fixos (D-MV-01).
5. Limitações registradas de ged_ecp (faixa estreita; não usar como medida absoluta isolada).
6. N=30 justificado pela hipótese **primária** (superioridade B<A) e suficiente para a secundária
   (TOST A−C, o teste mais exigente; D-MV-02).

## 9. Entregáveis Esperados

- `study-output/pilot_results_newcycle.csv` (270 linhas)
- `study-output/data_validation_newcycle.json`
- `study-output/STATISTICAL-REPORT-NEWCYCLE.md`
- `FINAL-PROJECT-REPORT-NEWCYCLE.md` + pacote de encerramento

---

**Fim do pré-registro (v1.0 FINAL APROVADO). 2026-08-15. Decisões da governança incorporadas:
Go/No-Go por faixa (≥27/30 GO · 10–26/30 NO-GO exploratório · <10/30 STOP); hierarquia
primária B<A (Friedman + Wilcoxon B−A) → secundária TOST A−C Δ=0.05 → complementar B−C;
N=30 justificado pela hipótese primária. Sem coleta, sem Lock, sem execução. Lock GO-8D intocado.
