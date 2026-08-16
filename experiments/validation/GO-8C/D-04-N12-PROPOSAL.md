# GO-8C — D-04 PROPOSTA — N=12 (Estudo Confirmatório)

**Data:** 2026-08-14
**Ciclo:** GO-8C
**Modo:** DOCUMENTARY / DECISION ANALYSIS ONLY — nenhuma alteração em GO-8B ou GO-8C; nenhum experimento; nenhuma coleta de dados; nenhuma seed; nenhum Lock; **D-04 NÃO iniciado** (planejamento apenas).
**Escopo:** dívida D-04 — planejar o estudo confirmatório com **N=12** para atingir a potência pré-especificada (≥ 0.80) sob o cenário S1_PRIMARY, sem reabrir o GO-8B.
**Documentos de referência (somente leitura):** GO-8B 01-CASES-BIPS.md · 06-STATISTICAL-PROTOCOL.md · 07-FAILURE-CRITERIA.md · 08-PRE-REGISTRATION.md · FINAL-PROJECT-REPORT.md · pilot-output/STATISTICAL-REPORT.md · pilot-output/pilot_results.csv · pilot-input/P5-PRODUCTION-MANIFEST.md · SX-REAUDIT.yaml · SX-CANDIDATES.md · P-0008-CROSS-DOMAIN-VALIDATION.md.

---

## 1. FATO (Contexto do GO-8B)

### 1.1 Potência pré-especificada

- **Piloto GO-8B (N=7): potência ≈ 0.63** (IC 95% 0.617–0.644) sob o cenário **S1_PRIMARY** pré-especificado (μ=(0.50, 0.60, 0.66); σ_b=0.12, σ_e=0.08, σ_s=0.06; 3 seeds/célula; mediana; Friedman; α=0.05; B=5.000; seed `20260811`). — `06 §5.2/§5.3`, `08 §9`.
- **N=12: potência ≈ 0.895** (IC 95% 0.886–0.903) — menor N da grade com potência ≥ 0.80 sob S1_PRIMARY. — `06 §5.2`.
- **Banda oficial (R5-GOV-02, `06 §5.4`):** mínimo metodológico 5 válidos / recomendado piloto 7 / **necessário para potência 12**. Qualquer alteração = DECISION REQUIRED.
- **Conclusão do GO-8B (FINAL-PROJECT-REPORT §3.2):** "Recomenda-se um estudo confirmatório com N=12 para atingir a potência pré-especificada (≥ 0.80) sob o cenário S1_PRIMARY."

### 1.2 Desenho fixado a preservar

| Parâmetro | Especificação (GO-8B) | Fonte |
|---|---|---|
| Unidade experimental | BIP/Caso (N = nº de BIPs válidos; nunca multiplicado) | 06 §1.3 |
| Condições | 3 — (A) cega pura · (B) cega + C3 · (C) não-cega | 06 §1.2 |
| Seeds por célula | **3 seeds por (BIP × condição)**; `cell = median(seed1, seed2, seed3)` | R5 M-3; 06 §1.3.1 |
| Teste global primário | **Friedman** (df=2, α=0.05) | R5 M-2 |
| Pós-hoc | Wilcoxon signed-rank pareado bilateral + Holm-Bonferroni | 06 §4 |
| Tamanho de efeito | Kendall's W; r_rb; Cliff's δ | 06 §3.4/§4.2 |
| IC 95% | Bootstrap percentil B=10.000 pareado + IC exato da mediana (mitigação STAT-08) | 06 §4.3 |
| Namespaces | A/C = CAT (operacional), B = SYN (D-02 GO-8C) | D-02 |
| TOST | **não executado** (nenhuma Δ aprovada) | R3-03/R5-GOV-03 |

### 1.3 O piloto em números

- **63 execuções** (7 BIPs × 3 condições × 3 seeds), todas PASS (`pilot_results.csv`).
- Resultado: Friedman p=0.0084, W=0.68; pós-Holm apenas **B>C** significativo; **B vs A p=1.00**.
- Sensibilidades (sem outliers; drop 1 por par dependente) — todas mantêm p<0.05.
- Materiais de entrada: `pilot-input/` com **7 BIPs** (~78 MB, incluindo fontes brutas PDF/HTML).
- **D-03 (NT-05) VALIDADO** no GO-8C por painel de 2 IAs (unanimidade PASS); `BIP-VAL_REPORT.yaml` → `verdict: PASS`.

---

## 2. EVIDÊNCIA (Universo de Candidatos Disponíveis)

### 2.1 Pool de candidatos (SX-REAUDIT.yaml, congelado em 2026-08-03)

**9 SELECTABLE:** Apollo 13, Challenger STS-51-L, I-35W, Deepwater Horizon, Chernobyl Unidade 4, Ebola, Operation Warp Speed, Suez/Ever Given, Genoma Humano.
**4 ELIGIBLE:** Tacoma Narrows, Hyatt Regency, Domino's Turnaround, Eyjafjallajökull.
**1 REJECTED:** RFID Walmart (EI falha — origens entrelaçadas).
**Verificação de fontes:** COMPLETA (etapa 5, 2026-08-03) — todos os 9 SELECTABLE com fontes públicas acessíveis; nenhum eliminado por EC-3.

### 2.2 BIPs já utilizados no piloto (7)

| BIP | Caso | Domínio | Status reaudit |
|---|---|---|---|
| BIP-001 | Deepwater Horizon | Industrial/Energia | SELECTABLE |
| BIP-002 | Hyatt Regency | Construção Civil | ELIGIBLE (mantido por diversidade) |
| BIP-003 | Operation Warp Speed | Medicina/Saúde | SELECTABLE |
| BIP-004 | Genoma Humano | Pesquisa Científica | SELECTABLE |
| BIP-005 | Ever Given/Suez | Logística | SELECTABLE |
| BIP-006 | I-35W Bridge | Construção Civil | SELECTABLE |
| BIP-007 | Resposta Ebola | Medicina/Saúde | SELECTABLE |

### 2.3 Candidatos restantes (para os 5 novos)

| Candidato | Domínio | Status reaudit | Observação |
|---|---|---|---|
| **Apollo 13 (1970)** | Aeroespacial | SELECTABLE | Postmortem; decisões sob incerteza; origens múltiplas (NASA, transcrições, imprensa) |
| **Chernobyl Unidade 4 (1986)** | Industrial/Energia nuclear | SELECTABLE | Demonstra EI (≥2 origens causais reais); postmortem |
| **Tacoma Narrows (1940)** | Construção Civil | ELIGIBLE | Registro visual excepcional; pendência de profundidade de decisões |
| **Domino's Turnaround (2009-10)** | Pequenos Negócios | ELIGIBLE | Novo domínio (pequenos negócios); risco EC-4 (narrativa corporativa) — monitorar |
| **Eyjafjallajökull (2010)** | Logística/aviação | ELIGIBLE | Novo subdomínio (aviação); pendência de multiplicidade de origens |

> **Nota Challenger:** o Challenger foi alvo do **SX-001** (já trabalhado pela equipe). Reutilizá-lo como BIP do GO-8C reintroduziria conteúdo de pipeline anterior (violação da regra P5 "sem importação de SX-001/002/003"). **Recomenda-se excluir** e usar Apollo 13 como representante aeroespacial.

---

## 3. ANÁLISE (Necessidades do Estudo N=12)

### 3.1 Quantidade de BIPs adicionais

- **5 novos** (12 − 7 existentes). O universo disponível tem exatamente **5 candidatos** após excluir Challenger (SX-001) e RFID (REJECTED): Apollo 13, Chernobyl, Tacoma Narrows, Domino's, Eyjafjallajökull.
- **Cobertura de domínios resultante (12 BIPs):** Aeroespacial (1) · Industrial (2: Deepwater, Chernobyl) · Civil (3: Hyatt, I-35W, Tacoma) · Saúde (2: OWS, Ebola) · Pesquisa (1: Genoma) · Logística (2: Suez, Eyjafjallajökull) · Pequenos Negócios (1: Domino's) → **7 domínios distintos** (≥4 exigido), **5 tipos de engenharia**, ambas naturezas (falha/colapso + sucesso/crise) — respeita a matriz P-0008 e a diversidade máxima.

### 3.2 Critérios de seleção dos 5 novos

1. **Independência (SC-1..SC-6):** candidatos já reauditados; sem re-exposição (evitar Challenger).
2. **Diversidade (P-0008):** maximizar distância em domínio × tipo de engenharia × natureza; cobrir domínios ainda não representados (Aeroespacial, Pequenos Negócios) e ampliar subdomínios (nuclear, aviação).
3. **Disponibilidade de fontes (SC-2/EC-3):** preferir SELECTABLE (fontes já verificadas) e tratar ELIGIBLE com pendência registrada (como o GO-8B fez com Hyatt).
4. **Prioridades pré-registradas (SX-SELECTION etapa 7):** domínio mais distante do software → postmortem público → maior multiplicidade de origens.

### 3.3 Reuso dos 7 BIPs existentes (sem violar o congelamento)

- **GO-8B permanece CLOSED / LOCKED / FROZEN.** Nenhum arquivo do GO-8B é alterado.
- Padrão já estabelecido no GO-8C (D-01/D-02/D-03): **criar cópias operacionais dentro do GO-8C** (ex.: `C2_PERMUTATION.yaml`, `C3_TAXONOMY.yaml`).
- Para os materiais dos 7 BIPs: **copiar** (não mover) narrativa + atomic facts + fontes de `GO-8B/pilot-input/` para o diretório operacional do GO-8C (`GO-8C/study-input/BIP-001..007/`), com registro de proveniência `derived_from: GO-8B pilot-input (frozen), copied in GO-8C`.
- **Questionamento a decidir pela governança:** os resultados do piloto (S_struct dos 7 BIPs) devem ser (a) **reaproveitados** como observações do estudo N=12 (mantendo a mesma seed_master `20260812` e as mesmas 63 execuções) ou (b) **re-executados integralmente** com nova seed_master cobrindo os 12 BIPs. Ver §6 (Recomendação).

### 3.4 Materiais de entrada para os novos BIPs

- Para cada novo BIP, produzir (seguindo o P5-PRODUCTION-MANIFEST):
  - `sources/00-index.md` + `sources/01-origem-dos-documentos.md` (proveniência EI/SC-5) + `sources/raw/` (downloads + checksums).
  - `narrative/01-narrativa-original.md` (condição C; zero ECP).
  - `atomic-facts/02-atomic-facts.md` (condições A/B; fatos mínimos; zero ECP; ≥15 AFs — FC-06).
  - `README.md`.
- **Regra zero-ECP:** vocabulário neutro (52 termos ECP compilados); rastreabilidade 100%; sem importação de SX-001/002/003.
- Estimativa de esforço por BIP (base: P5, produção dos 7 BIPs em 1 dia/2026-08-12): coleta de fontes (2–8 origens) + narrativa + AFs ≈ **0.5–1.5 dia por BIP**, dependendo da complexidade. Os 5 novos: **≈ 5–8 dias de trabalho**.

### 3.5 Condições, seeds e métricas (igual ao piloto)

- **Estrutura: 12 BIPs × 3 condições × 3 seeds = 108 execuções** (vs. 63 no piloto).
- **Seeds:** nova **seed_master GO-8C** (não reutilizar streams do GO-8B — isolamento de streams, 06 §9.2), gerando 108 seeds únicas via PCG64, uma por célula, registradas em manifesto de seeds do GO-8C.
- **Métricas:** S_struct (confirmatória, WL Kernel anonimizado) + S_sem (exploratória); agregação por mediana.
- **Namespaces:** A/C = CAT, B = SYN (D-02, GO-8C), via C2_PERMUTATION.yaml corrigido (D-01).

### 3.6 Impacto em tempo, armazenamento e análise

| Recurso | Piloto (N=7) | Confirmatório (N=12) | Delta |
|---|---|---|---|
| Execuções | 63 | **108** | +45 (×1.71) |
| Células (BIP×condição) | 21 | 36 | +15 |
| Linhas CSV de resultado | 63 | 108 | +45 |
| Materiais de entrada | ~78 MB (7 BIPs) | ~115–130 MB (12 BIPs) | +5 BIPs (Apollo, Chernobyl, Tacoma, Domino's, Eyjafjallajökull) |
| Tempo de produção de materiais | ~1 dia (7 BIPs) | ~5–8 dias (5 novos) | +5–8 dias |
| Tempo de execução do pipeline | unidades de horas (63 exec) | ~1.7× | +70% |
| Análise estatística | Friedman/Wilcoxon/Holm/IC | **mesmos scripts** (N=12) | custo computacional marginal |
| Bootstrap (B=10.000) | cobertura sub-nominal mediana N=7 | N=12: mediana ≈0.94, dif. pareada ≈0.97 (STAT-08) | cobertura adequada |

---

## 4. PROPOSTA DE DESENHO DO ESTUDO N=12

### 4.1 Lista dos 12 BIPs

| # | BIP | Caso | Domínio | Status | Origem |
|---|---|---|---|---|---|
| 1 | BIP-001 | Deepwater Horizon (2010) | Industrial | Reuso | GO-8B (cópia GO-8C) |
| 2 | BIP-002 | Hyatt Regency (1981) | Civil | Reuso | GO-8B (cópia GO-8C) |
| 3 | BIP-003 | Operation Warp Speed (2020–21) | Saúde | Reuso | GO-8B (cópia GO-8C) |
| 4 | BIP-004 | Genoma Humano (1990–2003) | Pesquisa Científica | Reuso | GO-8B (cópia GO-8C) |
| 5 | BIP-005 | Ever Given/Suez (2021) | Logística | Reuso | GO-8B (cópia GO-8C) |
| 6 | BIP-006 | I-35W Bridge (2007) | Civil | Reuso | GO-8B (cópia GO-8C) |
| 7 | BIP-007 | Resposta Ebola (2014–16) | Saúde | Reuso | GO-8B (cópia GO-8C) |
| 8 | **BIP-008** | **Apollo 13 (1970)** | **Aeroespacial** | **Novo** | SELECTABLE |
| 9 | **BIP-009** | **Chernobyl Unidade 4 (1986)** | **Industrial nuclear** | **Novo** | SELECTABLE |
| 10 | **BIP-010** | **Tacoma Narrows (1940)** | **Civil** | **Novo** | ELIGIBLE (pendência registrada) |
| 11 | **BIP-011** | **Domino's Turnaround (2009–10)** | **Pequenos Negócios** | **Novo** | ELIGIBLE (pendência EC-4 — monitorar) |
| 12 | **BIP-012** | **Eyjafjallajökull (2010)** | **Logística/aviação** | **Novo** | ELIGIBLE (pendência EI — monitorar) |

> **Justificativa dos 5 novos:** Apollo 13 (SELECTABLE, novo domínio aeroespacial, forte EI); Chernobyl (SELECTABLE, novo subdomínio nuclear, demonstra EI); Tacoma Narrows (novo tipo civil com registro visual, pendência de profundidade registrada — mesma tratativa dada a Hyatt no piloto); Domino's (cobre domínio Pequenos Negócios exigido pela matriz P-0008, risco EC-4 registrado); Eyjafjallajökull (amplia logística/aviação, pendência EI registrada). Todos dentro do universo congelado; nenhum re-exposição.

### 4.2 Estrutura de diretórios proposta (GO-8C)

```
experiments/validation/GO-8C/
├── D-04-N12-PROPOSAL.md              ← este documento
├── decisions/
│   └── D-04-N12-DECISION.md          ← (futuro, após decisão da governança)
│   └── D-04-N12-VALIDATION.md        ← (futuro, após validação)
├── scripts/                          ← cópias operacionais (D-01..D-03) + suíte N=12
│   ├── C2_PERMUTATION.yaml/.json     (D-01 corrigido)
│   ├── C3_TAXONOMY.yaml              (D-03 corrigido)
│   ├── BIP-VAL_REPORT.yaml           (D-03: verdict PASS)
│   └── (novos) test_d04_n12.py · go8c_seed_manifest.yaml
├── study-input/                      ← materiais operacionais do estudo N=12
│   ├── BIP-001-deepwater/ … BIP-007-ebola/   ← cópias GO-8C (proveniência GO-8B)
│   └── BIP-008-apollo13/ … BIP-012-eyjafjallajokull/  ← novos (produção P5)
├── study-output/                     ← execuções do estudo (futuro, autorizado)
│   ├── run-*/ (108 execuções, seed manifest)
│   └── stats_input_sstruct.csv
└── TODO-GO-8C.md                     ← D-04 → (em andamento / DONE após validação)
```

### 4.3 Processo de produção e validação dos novos materiais

1. **Coleta de fontes** por BIP (etapa 5 SX-SELECTION já verificou acessibilidade dos 9 SELECTABLE; re-verificar ELIGIBLE no momento da coleta).
2. **Narrativa + Atomic Facts** (regras P5: zero ECP, rastreabilidade 100%, ≥15 AFs).
3. **Validação pós-produção** (`VALIDATION-REPORT.md` do GO-8C): léxica (0 termos ECP), rastreabilidade (100% refs), não-importação (diff vs SX-001/002/003).
4. **Gate de qualidade de materiais** por BIP antes de entrar no estudo (critérios FC-01..FC-07).

### 4.4 Critérios de congelamento e Lock do GO-8C

- **Congelar o desenho** do estudo N=12 em documento próprio (análogo ao `08-PRE-REGISTRATION.md` do GO-8B), **antes** de qualquer execução.
- **Lock do GO-8C:** novo manifesto + Lock (hash dos artefatos operacionais e do pré-registro N=12) em **etapa separada autorizada**, com base nos artefatos congelados e scripts registrados. **Não executar nesta etapa.**
- GO-8B permanece FROZEN; nenhum hash do GO-8B recalculado.

### 4.5 Gate de autorização para execução

1. **Governança aprova esta proposta** (D-04-N12-PROPOSAL) → registrar DECISION.
2. **Produzir os 5 novos BIPs** (materiais) e **validar** (zero ECP, rastreabilidade, não-importação) → DECISION de aprovação dos materiais.
3. **Copiar os 7 BIPs existentes** para `study-input/` (proveniência registrada).
4. **Escrever o pré-registro N=12** (desenho, seeds, critérios Go/No-Go, plano de análise — replicando 06/07/08 do GO-8B) → DECISION de aprovação do pré-registro.
5. **Lock do GO-8C** (manifesto + hashes).
6. **Autorização explícita de execução** (108 execuções) → coletar dados → validação (07 adaptado) → análise (06 exato) → relatório → encerramento.

> Nenhuma etapa é autorizada por inferência (GO-8C-OPENING-DECISION §6).

---

## 5. RISCOS E DEPENDÊNCIAS

| # | Risco/Dependência | Gravidade | Mitigação |
|---|---|---|---|
| R-1 | **Disponibilidade de fontes dos 5 novos** (Apollo 13, Chernobyl, Tacoma, Domino's, Eyjafjallajökull) | Média | 3 dos 5 são SELECTABLE com fontes verificadas; ELIGIBLE (Tacoma, Domino's, Eyjafjallajökull) têm pendência — re-verificar no momento da coleta; se 1 falhar, buscar substituto no universo congelado (não fora dele) |
| R-2 | **Domino's (EC-4)** — narrativa corporativa dominante; risco de fonte única/parcial | Média | Pendência registrada; exigir ≥2 origens causais independentes (documentário, HBS case study, imprensa); se não confirmar, trocar por outro candidato ELIGIBLE |
| R-3 | **Impacto do NT-05 (painel de IAs) no N=12** | Baixa | D-03 já VALIDOU a taxonomia C3 (verdict PASS); painel é reutilizável para o estudo; novos materiais exigem **validação léxica + semântica** (estender painel aos 5 novos BIPs) — registrar como etapa no desenho |
| R-4 | **Protocolo estatístico precisa mudar para N=12?** | **Não** | Confirmado: `06` já contempla N=12 (potência §5, cobertura bootstrap §4.3.1 N=12); Friedman/Wilcoxon/Holm/α=0.05 **inalterados**; apenas o Go/No-Go do `07 §8` (≥5 casos) deve ser re-especificado para N=12 (ex.: ≥10–11 válidos para preservar potência) — **DECISION REQUIRED** no pré-registro |
| R-5 | **Dependência entre casos (STAT-09)** | Baixa | Ampliar sensibilidade de "1 caso por par dependente" para os novos pares (ex.: Deepwater/Chernobyl — Industrial); sem modelo misto |
| R-6 | **Reuso vs re-execução dos 7 BIPs** | Alta (decisão) | DECISION REQUIRED: (a) reaproveitar as 63 execuções do piloto (seed `20260812`) ou (b) re-executar os 12 com nova seed. Recomendação: **reaproveitar** para evitar custo duplicado e manter continuidade, **desde que** os dados do piloto sejam auditados e registrados como parte do estudo; alternativamente re-executar apenas se a governança exigir seed uniforme |
| R-7 | **Custo (tempo/armazenamento)** | Baixa | +5–8 dias de produção; +70% execuções; ~115–130 MB de materiais; custo computacional de análise marginal |
| R-8 | **Vazamento de conteúdo do GO-8B para o GO-8C** | Baixa | Cópias operacionais com `derived_from`; GO-8B intocado; diff de integridade ao copiar |

---

## 6. RECOMENDAÇÃO SOBRE VIABILIDADE

- **VIÁVEL.** O estudo N=12 é realizável **integralmente dentro do GO-8C**, sem reabrir o GO-8B:
  - Universo de candidatos suficiente (5 disponíveis: Apollo 13, Chernobyl, Tacoma Narrows, Domino's, Eyjafjallajökull), todos do re-audit congelado.
  - Protocolo estatístico **não muda** (06 já cobre N=12); apenas re-especificar o Go/No-Go do 07 para N=12 no pré-registro.
  - Infraestrutura do GO-8C (D-01..D-03) reutilizável: C2 corrigido, C3 validado (NT-05 PASS), namespaces operacionais definidos.
  - Custo estimado: **5–8 dias de produção de materiais** + cópia/reuso dos 7 BIPs + 108 execuções + análise.
- **Decisões de governança requeridas nesta etapa (para registrar na DECISION D-04):**
  1. Aprovar a **lista dos 12 BIPs** (7 reuso + 5 novos) e o desenho geral.
  2. Definir **reuso (a) vs re-execução (b)** dos 7 BIPs.
  3. Definir **Go/No-Go para N=12** (mínimo de casos válidos; proposta: ≥10 de 12).
  4. Autorizar a **produção dos 5 novos BIPs** como próxima etapa (ainda sem execução experimental).
  5. Confirmar que o **NT-05 do estudo N=12** será o painel de 2 IAs (D-03), estendido aos novos materiais.

---

## 7. NÃO-AUTORIZADO NESTA ETAPA

- Nenhuma criação de arquivos em `GO-8C/` além deste documento de proposta (se aprovado, os artefatos D-04 serão criados em etapa autorizada).
- Nenhuma alteração em GO-8B; nenhum Lock; nenhuma seed; nenhuma execução; nenhuma coleta de dados.
- D-04 permanece `PENDING GOVERNANCE REVIEW` até decisão formal da governança.

---

**Fim da proposta D-04. Aguardando decisão da governança.**
