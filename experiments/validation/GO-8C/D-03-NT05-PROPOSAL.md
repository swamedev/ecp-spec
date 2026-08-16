# GO-8C — D-03 PROPOSTA — NT-05 (Substituição da Revisão Humana por Auditoria Automatizada)

**Data:** 2026-08-13
**Ciclo:** GO-8C
**Modo:** DOCUMENTARY / DECISION ANALYSIS ONLY — nenhuma alteração em GO-8B ou GO-8C; nenhum experimento; nenhuma decisão consumida; NT-05 **não** marcado como resolvido; D-04 **não** iniciado.
**Escopo:** dívida D-03 — formalizar e auditar a substituição do requisito humano NT-05 por auditoria automatizada, preservando rastreabilidade e critérios de validade.

---

## 1. FATO

### 1.1 Requisito original de NT-05 (artefatos congelados)

O requisito NT-05 está definido no entregável congelado **`experiments/validation/GO-8B/03-SYNTHETIC-TAXONOMY-C3.md`**:

- **§4.1 (BIP-VAL):** o Blind Inference Protocol valida a neutralidade/independência de `C3_TAXONOMY.yaml` em relação ao ECP (pergunta N-1..N-5). Executores: Validador (V) + 2 revisores independentes (R1, R2). Cegueira: os validadores **não** conhecem mapping C2, resultados SX-001 nem hipóteses ECP.
- **§4.2 (NT-05 — Julgamento Humano):** *"3 validadores independentes classificam cada categoria C3: 'derivado de ECP?' (Sim/Não/Incerto)".* Critério Pass: **≤ 1 "Sim" por categoria** (maioria "Não").
- **§4.3 (Aprovação BIP-VAL):** APROVADO se e somente se **todos** NT-01..NT-04 = Pass **E** NT-05 = Pass. REJEITADO → taxonomia descartada; novo ciclo de geração cega.
- **§4.4 (Registro):** exemplo com `reviewers: [<hash_r1>, <hash_r2>]` e `NT-05: {status: PASS, details: "R1: 0 Sim; R2: 1 Sim; R3: 0 Sim"}`.

**Base metodológica:** NT-05 é o componente do BIP-VAL que verifica a **independência conceitual** (N-1..N-5) de forma semântica, complementando os testes objetivos (NT-01 léxico, NT-02 estrutural, NT-03 origem de fonte, NT-04 independência de geração).

### 1.2 O que foi feito no GO-8B (substituição temporária)

1. **Decisão NC-01** (`decisions/NC-01-HUMAN-REVIEW-SUBSTITUTION.md`, 2026-08-12): constatada a **indisponibilidade de três validadores humanos qualificados** no prazo do piloto; a governança autorizou a **substituição temporária** do gate NT-05 pelo protocolo `NT-05-AUTOMATED-INDEPENDENT-REVIEW`, com ressalva explícita: **sem equivalência epistemológica** entre auditoria automatizada e revisão humana. Escopo limitado ao NT-05.
2. **Protocolo** (`decisions/NT-05-AUTOMATED-INDEPENDENT-REVIEW.md`): auditoria em 6 áreas — C2 (Permutação/Mapping), C3 (Taxonomia/BIP-VAL), GFR (GraphFromReconstruction), WL (Kernel/Embeddings), Materiais (7 BIPs), Reprodutibilidade — com 27 subitens, critérios PASS/FAIL objetivos, **dupla execução independente** e **divergência = STOP**.
3. **Execuções:** NC-02 (primeira execução) e NC-03 (segunda execução independente, sem acesso a relatórios anteriores) — **ambas PASS, nenhuma divergência**.
4. **Registro:** NC-04 (`decisions/NT-05-AUTOMATED-INDEPENDENT-REVIEW-RESULT.md`) — gate NT-05 substituído considerado **VALIDATED para os fins do piloto**, **sem equivalência** à revisão humana original.
5. **Estado documental do artefato:** `BIP-VAL_REPORT.yaml` **permanece com `NT-05: PENDING` e `verdict: PENDING`** (o artefato não foi alterado; a aceitação do gate se deu por decisão de governança em artefato separado).

---

## 2. EVIDÊNCIA

### 2.1 O que NT-05 exigia originalmente

- **Natureza:** julgamento humano independente (3 validadores) sobre cada uma das 12 categorias de `C3_TAXONOMY.yaml` (e demais itens do BIP-VAL), respondendo **"esta categoria é derivada do ECP?"** (Sim/Não/Incerto).
- **Critério de aprovação:** ≤ 1 "Sim" por categoria.
- **Papel no BIP-VAL:** bloco obrigatório (junto com NT-01..04) para APROVAR a taxonomia C3 antes do primeiro caso.

### 2.2 Verificações necessariamente humanas

- **Núcleo de NT-05:** a classificação semântica "categoria derivada do ECP?" — envolve compreensão conceitual, sinônimos, paráfrases e conhecimento de domínio. Não é redutível a uma varredura lexical.
- **NT-04 (parcial):** a declaração assinada de cegueira do gerador tem componente de atestação humana (embora seu *registro* seja automatizável).

### 2.3 Verificações formalizáveis em testes automatizados determinísticos

| Verificação | Mecanismo determinístico existente |
|---|---|
| NT-01 Léxico (zero termos ECP) | `validate_bip00*.py` (52 termos, normalização acentuada, `\bterm\b`) |
| NT-02 Estrutural (não isomórfico ao ECP) | `p2_c3_taxonomy.py` (DAG, nós≠9, arestas>nós) |
| NT-03 Origem de fonte (100% source_refs externos) | `p2_c3_taxonomy.py` + validação de rastreabilidade |
| NT-04 Registro de geração (log de cegueira) | `p2_c3_taxonomy.py` (procedimento determinístico documentado) |
| Schema/DAG da taxonomia | `p2_c3_taxonomy.py` (T-C3-01) |
| Isolamento SYN (zero CAT/ECP no YAML) | Protocolo NT-05-AUTOMATED C3-01/C3-02 |
| GFR (21 testes) | `p3_tests_gfr.py` |
| WL (12 testes) | `p4_tests_wl.py` |
| Materiais (7 BIPs; hashes; rastreabilidade; léxico) | Protocolo MAT-01..05 + `validate_bip00*.py` |
| Reprodutibilidade (5 suítes; hashes) | `p_run_consolidated.py`; hashes SHA-256 |

### 2.4 Verificações que continuam exigindo julgamento semântico

- **O julgamento central de NT-05:** "categoria C3 é conceitualmente derivada do ECP?" — mesmo com léxico ampliado e varredura por palavra, a detecção de **contaminação conceitual via sinônimo/paráfrase** não é coberta de forma garantida por teste determinístico.
- **Interpretação de achados de fronteira** (ex.: categoria neutra que coincide lexicalmente com vocabulário genérico de engenharia).

### 2.5 Cobertura do mecanismo automatizado já utilizado no piloto

O protocolo NT-05-AUTOMATED cobre as **componentes objetivas/estruturais** das 6 áreas (27 itens): permutação C2, isolamento lexical/estrutural C3, schema GFR, anonimização WL, integridade de materiais e reprodutibilidade. **NÃO executa** o julgamento semântico do NT-05 original — ele verifica um **proxy objetivo** (ausência de ocorrências textuais ECP/CAT e de isomorfismo estrutural), e registra explicitamente `NT-05 = PENDING (substituído por este protocolo)`.

### 2.6 Falsos negativos / falsos positivos conhecidos

- **Falso negativo (FN):** categoria **conceitualmente derivada do ECP mas expressa com sinonímia/paráfrase** fora das 52 entradas do léxico → escapa ao NT-01 e ao proxy C3-01/02. Este é exatamente o risco que o NT-05 humano foi desenhado para mitigar.
- **FN documentado (FINDING-BIP-VAL-01):** o congelado cita "47 termos" e a compilação operacional usa 52. A varredura com 52 é condição mais forte (0 hits em 52 ⇒ 0 hits em 47), mas a lista operacional **não é registro formal** de nenhum artefato congelado — há divergência documental não harmonizada.
- **Falso positivo (FP):** categorias neutras que usam vocabulário genérico de engenharia coincidente com ECP (ex.: `estado`, `risco`, `entidade`, `validacao`) podem disparar hits lexicais → falha espúria. Mitigado por casamento por palavra + normalização acentuada, mas a sobreposição léxica ECP×engenharia é estrutural (ECP deriva do discurso de engenharia).

### 2.7 A substituição altera critérios de inclusão/exclusão ou Go/No-Go?

- **Não altera critérios de caso.** Os critérios de inclusão/exclusão de casos e o Go/No-Go para análise (07 §8: ≥5 casos válidos, ≥4 domínios, matriz N×3 completa, nenhum FAIL-PILOT) e os critérios FR-01..06 **permanecem idênticos** — NT-05 é um gate de **aprovação da taxonomia C3** (artefato), não um critério por caso.
- **Altera como o gate do artefato C3 foi liberado:** o BIP-VAL original exigia NT-05 humano; o GO-8B liberou o gate via decisão de governança (NC-01/NC-04) sem alterar o artefato. **Atenção a rastreabilidade:** `BIP-VAL_REPORT.yaml` ainda exibe `NT-05: PENDING / verdict: PENDING`; um terceiro que leia apenas o artefato não percebe que a governança aceitou a substituição.

### 2.8 A substituição afeta independência/cegueira?

- **Cegueira da reconstrução: NÃO afetada.** NT-05 dizia respeito à validação da taxonomia, não à cegueira dos avaliadores da reconstrução.
- **Independência da validação: enfraquecida (aproximada).** A dupla execução independente (executor + auditor sem acesso a relatórios anteriores) aproxima a independência, mas **não equivale** a 3 validadores humanos independentes com julgamento semântico próprio.
- **Risco de viés:** a auditoria automatizada verifica somente o que foi programado para verificar (proxy objetivo). A decisão de "o que checar" continua nas mãos de quem programa/define o protocolo.

### 2.9 A auditoria automatizada pode ser reproduzida por terceiro?

- **Sim, para as partes determinísticas:** todas as suítes (C2/C3/GFR/WL/Materiais/Reprodutibilidade) e os hashes SHA-256 são reproduzíveis — a segunda execução independente (NC-03) já demonstrou a reprodutibilidade.
- **Não, para o julgamento semântico:** a decisão "categoria derivada do ECP?" não é reproduzível por um teste determinístico; só pode ser delegada a humanos ou aproximada por proxy (com risco residual).

---

## 3. IMPACTO

### 3.1 Substituição integral (auditoria automatizada como gate definitivo)

| Dimensão | Impacto |
|---|---|
| Validade científica | Reduz a garantia de independência conceitual do C3 (risco FN por sinonímia). Adequado apenas se houver demonstração de cobertura do proxy. |
| Rastreabilidade/auditabilidade | Alta — determinístico, reproduzível, hashes e logs; mas exige harmonizar a divergência `BIP-VAL_REPORT.yaml` (PENDING) vs decisão de aceite. |
| Risco de viés | Média — viés de programação do proxy (o que se decide checar). Sem guarda semântica. |
| Recursos | Mínimos — sem gargalo humano; escalável ao N=12. |

### 3.2 Substituição parcial (automatizar o determinístico; manter gate semântico mínimo humano)

| Dimensão | Impacto |
|---|---|
| Validade científica | Mais alta — preserva o julgamento semântico (núcleo de NT-05) em um gate mínimo, mantendo o restante automatizado e determinístico. |
| Rastreabilidade/auditabilidade | Alta — testes objetivos reproduzíveis + rubric semântico pré-registrado. |
| Risco de viés | Menor — humano independente cobre o que o proxy não cobre (sinonímia/paráfrase). |
| Recursos | Moderados — requer ≥1 revisor qualificado (menos que os 3 originais), com rubric objetivo para mitigar subjetividade. |

### 3.3 Não substituir (manter NT-05 humano integral)

| Dimensão | Impacto |
|---|---|
| Validade científica | Máxima — fiel ao congelado (3 validadores independentes). |
| Rastreabilidade/auditabilidade | Documental, mas dependente de disponibilidade humana e da qualidade dos registros dos validadores. |
| Risco de viés | Mínimo (se a independência dos 3 for efetiva). |
| Recursos | Crítico — a indisponibilidade já demonstrada no GO-8B (NC-01) tende a se repetir; bloqueia o fluxo até a revisão ser feita. |

**Efeito transversal comum:** nenhuma das três opções altera métricas (S_struct/S_sem), análise estatística, critérios de caso ou decisão Go/No-Go do experimento — o impacto concentra-se na **aprovação do artefato taxonomia C3** e na **integridade epistemológica** do pipeline.

---

## 4. ALTERNATIVAS

### Alternativa A — Substituição integral por auditoria automatizada

- **Critérios objetivos de aprovação:**
  - Cobertura do proxy demonstrada (ex.: léxico aumentado com sinônimos + proxy semântico por embeddings com concordância ≥ limiar pré-registrado em conjunto de calibração rotulado).
  - Dupla execução independente PASS, divergência = STOP (mantém regra do protocolo).
  - Todas as suítes determinísticas ALL PASS; hashes registrados.
  - Divulgação explícita de risco residual (sem equivalência com revisão humana).
- **Vantagens:** custo mínimo; sem gargalo humano; totalmente reproduzível; escalável a N=12.
- **Desvantagens:** perde o julgamento semântico; risco de FN por sinonímia/paráfrase; requer prova de cobertura para ser defensável.
- **Impacto em testes/métricas/Go-No-Go:** testes: adicionar prova de cobertura (proxy semântico) à suíte; métricas: inalteradas; Go/No-Go: inalterado (gate do artefato liberado por auditoria, como já no GO-8B).

### Alternativa B — Substituição parcial (determinístico automatizado + gate semântico mínimo humano)

- **Critérios objetivos de aprovação:**
  - Suítes determinísticas ALL PASS (NT-01..04 + proxy estrutural/lexical + C2/GFR/WL/Materiais/Reprodutibilidade).
  - Gate semântico mínimo: ≥1 revisor humano qualificado e independente classifica cada categoria C3 como "derivada de ECP?" (Sim/Não/Incerto) com rubric pré-registrado; PASS se ≤1 "Sim"/categoria (espelha o critério original).
  - Divergência entre a avaliação semântica e o proxy automatizado = revisão obrigatória (não STOP automático, mas investigação registrada).
- **Vantagens:** preserva o componente epistemológico central do NT-05; mantém o pipeline desbloqueado; reduz o gargalo de 3 para 1 revisor; equilíbrio entre rigor e viabilidade.
- **Desvantagens:** ainda depende de ≥1 humano; exige gestão de qualificação e de viés do revisor; rubric precisa ser robusto.
- **Impacto em testes/métricas/Go-No-Go:** testes: adicionar suíte determinística + rubric semântico; métricas: inalteradas; Go/No-Go: inalterado.

### Alternativa C — Manter NT-05 humano integral (3 validadores independentes)

- **Critérios objetivos de aprovação:**
  - 3 validadores humanos qualificados e independentes disponíveis e confirmados.
  - Classificação individual por categoria (Sim/Não/Incerto); PASS se ≤1 "Sim"/categoria; registros assinados/anônimos rastreáveis.
- **Vantagens:** máxima integridade epistemológica; fiel ao desenho congelado (03 §4.2/§4.3).
- **Desvantagens:** gargalo humano demonstrado no GO-8B (NC-01); custo e prazo; repetição de revisão por ciclo (oneroso para N=12).
- **Impacto em testes/métricas/Go-No-Go:** testes: sem mudança (suíte determinística permanece como apoio); métricas: inalteradas; Go/No-Go: gate do artefato **bloqueado até** a revisão humana — risco de paralisação.

---

## 5. RECOMENDAÇÃO

**Recomendação do agente: Alternativa B — substituição parcial.**

**Fundamentação:**

1. **Integridade metodológica do GO-8C:** o objetivo do ciclo é quitar dívidas **preservando a integridade metodológica** (abertura do GO-8C: dívida D-03 = "formalizar e auditar a substituição ... preservando rastreabilidade e critérios de validade"). Substituir integralmente NT-05 por um proxy lexical/estrutural (Alternativa A) abandonaria o único componente que detecta contaminação conceitual por sinonímia — um risco aceitável para um estudo confirmatório N=12.
2. **O custo humano é pequeno e gerível:** o gargalo original eram **3** validadores qualificados indisponíveis; um **gate semântico mínimo de ≥1 revisor independente com rubric pré-registrado** espelha o critério original (≤1 "Sim"/categoria) com custo substancialmente menor. Se, e somente se, a governança comprovar que nem 1 revisor qualificado estará disponível no N=12, a Alternativa A torna-se o fallback — **com divulgação explícita de risco residual e reforço do proxy** (léxico sinonimizado + proxy semântico por embeddings), **nunca com equivalência declarada**.
3. **Rastreabilidade e auditabilidade:** a Alternativa B combina o melhor dos dois mundos — a parte determinística é reproduzível por terceiro (como já demonstrado), e o julgamento semântico fica registrado com rubric explícito. Inclui a **harmonização obrigatória** da divergência documental do GO-8B (`BIP-VAL_REPORT.yaml` exibindo `NT-05: PENDING`/`verdict: PENDING` enquanto a governança aceitou a substituição) — em GO-8C o artefato e a decisão devem ser **coerentes e rastreáveis**.
4. **Não impacta o experimento:** nenhuma das alternativas altera métricas, critérios de caso ou Go/No-Go; a decisão concentra-se no gate do artefato C3. Isso permite resolver D-03 sem afetar a linha confirmatória N=12.

**Observação:** esta proposta **não** marca NT-05 como resolvido. Ela apenas mapeia evidências e opções; a resolução depende da decisão formal da governança (próximo passo).

---

## 6. DECISION REQUIRED

**DECISION REQUIRED** — a governança deve decidir a forma de formalização do gate NT-05 no GO-8C:

| ID | Alternativa | Descrição |
|---|---|---|
| **A** | Substituição integral | Auditoria automatizada como gate definitivo, mediante demonstração de cobertura do proxy e divulgação de risco residual. |
| **B** | Substituição parcial | Automatizar o determinístico + manter gate semântico mínimo humano (≥1 revisor, rubric pré-registrado, critério ≤1 "Sim"/categoria). |
| **C** | Manter NT-05 integral | 3 validadores humanos independentes obrigatórios (fiel ao congelado), com risco de gargalo/bloqueio. |

**Itens que acompanham a decisão (independentemente da alternativa):**
- Harmonizar a rastreabilidade entre artefato operacional (`BIP-VAL_REPORT.yaml`) e decisão de governança no GO-8C.
- Definir rubric objetivo para o componente semântico (se B) ou prova de cobertura (se A).
- Registrar explicitamente a **não equivalência** auditoria automatizada × revisão humana.
- Nenhuma mudança em métricas, critérios de caso ou Go/No-Go.

---

**Fim da proposta. Nenhum arquivo do GO-8B ou GO-8C alterado. Nenhum experimento executado. Nenhuma decisão consumida. NT-05 não resolvido. D-04 não iniciado.**
