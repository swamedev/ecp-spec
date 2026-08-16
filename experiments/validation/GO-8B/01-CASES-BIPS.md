# GO-8B Deliverable 1 — Lista Preliminar de 7 Casos/BIPs

**Status:** Preparação Documental (PARAR)  
**Data:** 2026-08-10  
**Governado por:** P-0007.1 / SX-SELECTION (congelado em 2026-08-03)  
**Referências:** SX-SELECTION.md, SX-CANDIDATES.md, SX-REAUDIT.yaml, P-0008 (diversidade cross-domain)

---

## 1. Critérios de Inclusão (derivados de SX-SELECTION, regra pré-registrada)

| Critério | Exigência | Fonte |
|---|---|---|
| **SC-1 Independência** | Projeto nunca utilizou ECP; equipe nunca ouviu falar | SX-SELECTION §SC-1 |
| **SC-2 Evidência Pública** | Documentação suficiente e acessível (relatórios, atas, postmortems) | SX-SELECTION §SC-2 |
| **SC-3 Sequência Temporal** | Ordem dos acontecimentos reconstruível (datas, marcos, causalidade) | SX-SELECTION §SC-3 |
| **SC-4 Decisões Identificáveis** | Decisões identificáveis no registro | SX-SELECTION §SC-4 |
| **SC-5 Múltiplas Fontes (≥2 origens causais)** | Fontes de múltiplas origens causais (não apenas múltiplas fontes derivadas) | SX-SELECTION §SC-5 + P-0007.1 EI (RA-EI-001) |
| **SC-6 Reprodutibilidade** | Outro avaliador com mesmas fontes chega praticamente às mesmas conclusões | SX-SELECTION §SC-6 |

**Regra de elegibilidade (inalterada desde congelamento):**
- SC-1, SC-3, SC-4 = **Sim** (obrigatórios)
- **Nenhum** critério = **Não**
- ≥ **4** dos 6 critérios = **Sim**
- Qualquer exclusão EC-1..EC-7 → **inelegível**

---

## 2. Critérios de Exclusão (EC-1..EC-7, congelados)

| Código | Critério | Motivo |
|---|---|---|
| **EC-1** | Núcleo de software (SX-001) | Risco de contaminação (ECP nasceu em software) |
| **EC-2** | Memória única | Documentação depende de único participante sem registro |
| **EC-3** | Fonte inacessível | Paywall total sem alternativa |
| **EC-4** | Narrativa única | Uma narrativa incontestada fragiliza SC-5/SC-6 |
| **EC-5** | Sem consequência | Toy/demonstração sem decisões de consequência real |
| **EC-6** | Envolvimento ECP | Qualquer participação dos autores do ECP |
| **EC-7** | Exposição prévia | Equipe já exposta ao ECP |

---

## 3. Justificativa de Diversidade (Matriz P-0008)

A diversidade é avaliada em **três eixos** (P-0008 §"Matriz de diversidade"):  
1. **Domínio** (setor)  
2. **Tipo de engenharia** (física, biomédica, civil, científica, industrial)  
3. **Natureza** (falha/colapso vs. sucesso)

O SX-001 (Challenger) já cobriu: **Aeroespacial × Física × Falha**.  
O conjunto deve maximizar distância em relação a este ponto.

---

## 4. 7 Casos/BIPs Selecionados (dos 9 SELECTABLE do SX-REAUDIT)

| # | Caso | Domínio (Taxonomia P-0007.1) | Tipo Engenharia | Natureza | Origens Causais Independentes (EI) | Status Reaudit | Justificativa Diversidade |
|---|---|---|---|---|---|---|---|
| **1** | **Deepwater Horizon (2010)** | Industrial/Energia/Offshore | Industrial | Falha | ≥3 (JIT, CSB, BP, Congresso) | SELECTABLE | Domínio industrial distinto; múltiplas investigações independentes; falha catastrófica |
| **2** | **Hyatt Regency Walkway (1981)** | Construção Civil | Civil | Colapso | PARCIAL (NBS dominante; litígio 2ª origem) | ELIGIBLE | Domínio civil distinto; tipo engenharia civil; colapso estrutural; decisão de mudança de projeto documentada |
| **3** | **Operation Warp Speed (2020–2021)** | Medicina/Saúde | Biomédica | Sucesso | ≥3 (GAO, HHS/BARDA, empresas, imprensa) | SELECTABLE | Domínio saúde distinto; tipo biomédica; **sucesso** (não falha); decisões risco/financiamento |
| **4** | **Genoma Humano (1990–2003)** | Pesquisa Científica | Científica | Sucesso | ≥3 (NHGRI/DOE, Nature/Science, Celera, imprensa) | SELECTABLE | Domínio pesquisa distinto; tipo científica; **sucesso**; decisão público vs. privado |
| **5** | **Ever Given / Suez (2021)** | Logística/Transporte | Industrial | Falha/Recuperação | ≥3 (SCA, P&I Club/salvado, satélite) | SELECTABLE | Domínio logística distinto; tipo industrial; falha operacional com recuperação |
| **6** | **I-35W Mississippi Bridge (2007)** | Construção Civil | Civil | Falha | ≥3 (NTSB, MnDOT, imprensa) | SELECTABLE | Segundo caso civil (reforça robustez no domínio); relatório NTSB oficial; decisões manutenção/inspeção |
| **7** | **Resposta Ebola África Ocidental (2014–2016)** | Medicina/Saúde | Biomédica | Crise/Falha Parcial | ≥3 (WHO, MSF, equipes acadêmicas) | SELECTABLE | Segundo caso saúde (diversidade dentro domínio); resposta a crise; decisões sob incerteza extrema |

---

## 5. Cobertura de Diversidade (Matriz Agregada)

| Eixo | SX-001 (Challenger) | Conjunto GO-8B (7 casos) | Cobertura Total |
|---|---|---|---|
| **Domínios distintos** | 1 (Aeroespacial) | +6 (Industrial, Civil, Saúde, Pesquisa, Logística) | **7 domínios** |
| **Tipos engenharia** | 1 (Física) | +4 (Industrial, Civil, Biomédica, Científica) | **5 tipos** |
| **Natureza** | Falha | 4 Falhas + 3 Sucessos | **Ambas naturezas** |
| **Origens causais independentes (mínimo por caso)** | 3 | 2–3 (≥2 por EI) | **Satisfaz RA-EI-001** |

**Observação:** Hyatt Regency (ELIGIBLE) mantido por trazer **domínio civil + colapso + decisão de mudança de projeto** — combinação única não replicada pelos outros casos. A pendência EI (origem NBS dominante) é registrada como limitação conhecida (DEBT-005 paralelo); não invalida elegibilidade pois SC-5 = PARCIAL (não "Não") e ≥4 critérios = Sim.

---

## 6. BIPs (Blind Inference Protocols) Associados

Cada caso terá um **BIP separado** para validação de reconstrução cega:

| BIP-ID | Caso | Objetivo | Status |
|---|---|---|---|
| BIP-001 | Deepwater Horizon | Reconstrução cega → comparação narrativa oficial | Pendente |
| BIP-002 | Hyatt Regency | Reconstrução cega → comparação narrativa oficial | Pendente |
| BIP-003 | Operation Warp Speed | Reconstrução cega → comparação narrativa oficial | Pendente |
| BIP-004 | Genoma Humano | Reconstrução cega → comparação narrativa oficial | Pendente |
| BIP-005 | Ever Given/Suez | Reconstrução cega → comparação narrativa oficial | Pendente |
| BIP-006 | I-35W Bridge | Reconstrução cega → comparação narrativa oficial | Pendente |
| BIP-007 | Resposta Ebola | Reconstrução cega → comparação narrativa oficial | Pendente |
| **BIP-VAL** | **Validação Taxonomia Sintética C3** | Verificação de neutralidade da taxonomia sintética (entregável 3) | **Separado, obrigatório** |

### 6.1 Seeds Pré-especificadas (R5 M-3)

- **3 seeds por (BIP × condição)** — desenho estabelecido em GO-8A; número fixo, **não** ajustado por resultados.
- `cell_value = median(seed_1, seed_2, seed_3)`; `seed = observação repetida dentro de BIP × condição`.
- Seeds **não** são unidades experimentais independentes (ver Entregável 6 §1.3.1).
- **Banda de casos:** mínimo metodológico (5 válidos p/ análise), recomendado piloto (7), necessário p/ potência inferencial (12) — separados no Entregável 6 §5.4; qualquer alteração = DECISION REQUIRED.

---

## 7. Próximos Passos (Não Executados Aqui)

1. Verificação de acessibilidade de fontes (etapa 5 SX-SELECTION) para cada caso
2. Seleção automática pelo protocolo congelado (etapas 7–8 SX-SELECTION)
3. Execução pipeline: Narrativa → Atomic Facts → Reconstrução Cega → Alignment → EAR
4. Registro em SHADOW-REPORT-### e atualização DISCOVERY-LOG

---

**Fim do Entregável 1.** Nenhum experimento executado. Nenhum dado coletado. Apenas preparação documental.
