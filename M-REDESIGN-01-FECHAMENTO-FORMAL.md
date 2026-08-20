# M-REDESIGN-01-FECHAMENTO-FORMAL.md

**Hash SHA-256:** `879772de1d34548aa795c6bb55068d78781edc32e63bd5bb2e24e11b076275e1`

---

## Encerramento Formal do Programa de Redesenho de Métrica (DV-REDESIGN)

**Data:** 2026-08-19  
**Decisão:** Encerramento formal da linha de investigação "DV-REDESIGN" — GO-8E permanece NÃO AUTORIZADO.

---

## 1. Linha do Tempo e Achados por Etapa

| Etapa | Commit | Documento Principal | Hash SHA-256 | Resultado | Causa Raiz Identificada |
|-------|--------|---------------------|--------------|-----------|------------------------|
| GO-8D (N=12) | `38eda1a` | `FINAL-PROJECT-REPORT-GO-8D.md` | `4d40f5c5dee0146ff3e28bf63447503196515554643381a0be20e9a956c91e3e` | **Negativo genuíno** — Hipótese C3 rejeitada (taxonomia C3 piorou reconstrução, poder ≈0.999) | — |
| GO-8D-NC (N=30) | `e2971ba` | `STATISTICAL-REPORT-GO-8D-NC.md` | `3e967d5c95ba2113a846448b7f48e8550f50f0cea5506c2a4690791570e80c79` | **Aparentemente positivo** (p=2.61e-8), **invalidado** | Viés circular em `ged_ecp` (taxonomia própria do ECP usada como referência contra si mesma) |
| Measurement Redesign Fase A/B/C | — | `MEASUREMENT-REDESIGN-PHASE1-REPORT.md`, `MEASUREMENT-REDESIGN-PHASE2-REPORT.md` | — | Métrica `DV-REDESIGN` construída sem viés circular; validada em C1-C6 (robustez, interpretabilidade 97.7% com Claude/GPT/Gemini) | — |
| MR-C7 v1 | `e2971ba` | `MR-C7-PROTOCOLO-PREREGISTRO.md` | `380fc1281f685c9baaefa46c6ef69aaff2d88dc844ad37ae250a50ae90acefe3` | **FAIL** | Colisão espúria de token em `make_v2_paraphrase` (viés de gerador) |
| MR-C7 v2 (gerador corrigido) | `bcfc945` | `MR-C7-PROTOCOLO-PREREGISTRO-V2.md` | `5a926b77c8baaf722a8eea1eccba43320ce00b676306f3d0042f4b7c1bb2627f` | **FAIL** | Diluição de agregação (peso 1:1:1 dilui sinal real de `conf` com `ged_ref`/`div_metric` ≈0 ou invertidos) |
| MR-C7 v3 (peso 0.6/0.2/0.2, casos novos) | `9c7b38d` | `MR-C7-PROTOCOLO-PREREGISTRO-V3.md` | `26986e473d3ee7245810945af619ab945db545fed35d90185defe998e7ed440b` | **FAIL** | `conf` estruturalmente incapaz de discriminar V0×V1 (F1 contra verdade por-estado não captura *quantidade* de conteúdo, só fidelidade) |
| `conf_v2` (F1 contra G1 fixo) | `a994132` | `C-CONF-REDESIGN-PROPOSAL.md` | `b561d6964ab14f72fead0c0b4d616381d78e842bb3176e428ba48aa34ddb9fdc` | **FAIL** | Classificador hash-fallback confunde negação com conteúdo novo (V3 classifica em NEW_CATS por sobreposição lexical: "prazo", "risco", "qualidade") |

### Evidência Quantitativa do `conf_v2` (24 casos v3, seed 20260819)

| Gap (mediana) | Valor | Piso 0.05 |
|---------------|-------|-----------|
| V1 − V0 | **+0.108** | ✅ PASS |
| V1 − V2 | **+0.150** | ✅ PASS |
| V0 − V3 | **−0.101** (V3 > V0) | ❌ FAIL |
| V2 − V3 | **−0.145** (V3 > V2) | ❌ FAIL |

- V3 atinge `conf_v2 = 1.0000` em 10/24 casos
- No nível de pool: 16/24 casos com ≥1 candidato V3 classificando em NEW_CATS (MRCAT-10/11/12)
- Exemplos textuais auditados: "nao conclui dentro do **prazo** com cronograma e vencimento" → MRCAT-10; "nao enfrenta **risco** de contingencia com **ameaca**" → MRCAT-11; "nao confere **qualidade** com avaliacao de aceitacao e **aptidao**" → MRCAT-12
- G1 **contém** MRCAT-10,11,12 em todos os 24 casos (verificado em `reconstruction_graphs.json`)

---

## 2. Conclusão Transversal (Aprendizado Estrutural)

**Duas causas raízes distintas — v1→v2 (regra `relates` no gerador) e `conf_v2` (classificador por cosseno) — são instâncias do mesmo problema estrutural:**

> **O embedding hash-fallback do engine não carrega semântica — só coincidência lexical.**

- Na v1→v2: a regra `relates` (overlap ≥ 2 tokens) gerava self-loops espúrios que "pareciam" estrutura verdadeira
- No `conf_v2`: o classificador por cosseno sobre embedding hash-fallback não distingue "conteúdo novo verdadeiro" de "negação de conteúdo base que compartilha tokens-chave"

**Isso não é um bug isolado corrigível ponto a ponto.** É uma limitação de desenho do motor de reconstrução (GO-8D-NC/scripts) usado em todo o programa GO-8/MR-C7. Qualquer métrica baseada apenas nas categorias MRCAT-01..12 colapsadas por este engine terá essa limitação: ruído semântico (negação, redundância, ruído lexical) é indistinguível de sinal semântico no espaço de categorias.

---

## 3. Conclusão Científica Honesta

`DV-REDESIGN`, com os componentes e abordagens tentados (pesos variados: 1:1:1 → 0.6/0.2/0.2; redefinição de `conf` contra verdade fixa), **não atinge validade discriminante de valor semântico** no par mais fundamental do gate: **nada adicionado (V0) vs. valor real adicionado (V1)**.

- Cada hipótese de correção foi testada empiricamente com pré-registro, hash-lock, casos novos, e descartada com evidência — não por suposição.
- O processo de governança funcionou: detectou viés circular (GO-8D-NC), viés de gerador (v1), diluição de agregação (v2), zero estrutural de componente (v3), limitação de representação (conf_v2).
- **Resultado negativo bem fundamentado ≠ fracasso do processo.** É o oposto: processo rigoroso que evitou falso positivo.

---

## 4. Consequências Formais

1. **GO-8E permanece NÃO AUTORIZADO** — agora por decisão fundamentada (esgotamento razoável de hipóteses de correção testáveis no escopo atual), não por prudência genérica.

2. **Achados negativos genuínos anteriores NÃO SÃO INVALIDADOS:**
   - GO-8D (N=12, poder ≈0.999, hipótese C3 rejeitada) permanece válido e independente de `DV-REDESIGN`.
   - Medidas de robustez C1-C6 do Measurement Redesign (sem viés circular) permanecem válidas.

3. **Pré-requisito para retomada futura (se houver):**
   > Não é mais peso ou definição de `conf` — é **substituir o embedding hash-fallback por uma representação com semântica real** (fora do escopo desta rodada de governança).

---

## 5. Hashes e Referências Completas (Cadeia de Custódia)

| Documento | Hash SHA-256 |
|-----------|--------------|
| `MR-C7-PROTOCOLO-PREREGISTRO.md` (v1) | `380fc1281f685c9baaefa46c6ef69aaff2d88dc844ad37ae250a50ae90acefe3` |
| `MR-C7-REPORT.md` (v1) | `b239e0a9436beb0c3841c688f4635de7b2cd5f157734124f752efd571a658888` |
| `C-GENERATOR-FIX-V2-PARAPHRASE.md` | `d4a5b1b361137b42a7037ec885e8a217da99fd8bf8ef41cf767b9333ae8efa7b` |
| `MR-C7-PROTOCOLO-PREREGISTRO-V2.md` | `5a926b77c8baaf722a8eea1eccba43320ce00b676306f3d0042f4b7c1bb2627f` |
| `measurement-redesign/phase4-v2/outputs/MR-C7-REPORT-V2.md` | `a9b323b839863b2a09e27d09e3d7e58dbd5d1e1c1c49fb9c976e752b79d4690a` |
| `MR-C7-PROTOCOLO-PREREGISTRO-V3.md` | `26986e473d3ee7245810945af619ab945db545fed35d90185defe998e7ed440b` |
| `measurement-redesign/phase4-v3/outputs/MR-C7-REPORT-V3.md` | `728b0303339fc7c2796b2e16f6abac4f0e7b7f0f9dde3dfe61b4aba867008dea` |
| `C-CONF-REDESIGN-PROPOSAL.md` | `b561d6964ab14f72fead0c0b4d616381d78e842bb3176e428ba48aa34ddb9fdc` |
| `C-MODEL-SUBSTITUTION-ADDENDUM.md` | `4ce9fa87f0cd4fa6c0b33ffe2cc4ee5d27e3d998c142fce1c5ac60a9f13b4dc5` |
| `FINAL-PROJECT-REPORT-GO-8D.md` | `4d40f5c5dee0146ff3e28bf63447503196515554643381a0be20e9a956c91e3e` |
| `STATISTICAL-REPORT-GO-8D-NC.md` | `3e967d5c95ba2113a846448b7f48e8550f50f0cea5506c2a4690791570e80c79` |
| `FLIGHT-F2-EXECUTION-REPORT-GO-8D-NC.md` | `b346b4fbee03308e891cb2607578b219db4fa13c716807c8038e4a31ddcd669c` |

### Commits da Cadeia (Git)
- `38eda1a` — GO-8D encerrado (C3 rejeitada)
- `e2971ba` — MR-C7 v1 executado (FAIL, colisão espúria)
- `f63b385` — Fix gerador v2 (`make_v2_paraphrase`)
- `bcfc945` — MR-C7 v2 executado (FAIL, diluição agregação)
- `c4a7604` — Pré-registro v3
- `9c7b38d` — MR-C7 v3 executado (FAIL, zero estrutural conf)
- `a994132` — `conf_v2` diagnóstico + proposta (FAIL, limitação classificador)

---

## 6. Verificação de Não-Alteração de Arquivos Históricos

Confirmado: **nenhum arquivo hash-locked de v1/v2/v3 foi alterado** neste encerramento. Os únicos arquivos novos/adicionados são:
- `C-CONF-REDESIGN-PROPOSAL.md` (diagnóstico, hash `b561d696...`)
- `measurement-redesign/phase4-v3/scripts/metric.py` (campo diagnóstico `conf_v2` adicionado, DV_P/DV_Q inalterados)
- `measurement-redesign/phase4-v3/outputs/dv_values.json` (regerado com `conf_v2`)
- `M-REDESIGN-01-FECHAMENTO-FORMAL.md` (este documento)

Todos os artefatos de v1, v2, v3 (`cases.yaml`, `states.yaml`, `reconstruction_graphs.json`, relatórios MD/JSON, hash-locks) permanecem intactos nos commits `e2971ba`, `bcfc945`, `9c7b38d`.

---

## 7. Assinatura

**Execução de encerramento formal:** Medição Redesign — DV-REDESIGN  
**Governança:** Decisão baseada em evidência empírica completa, sem hipótese residual testável no escopo atual  
**Próximo passo (se aplicável):** Substituição do motor de embedding — fora de escopo