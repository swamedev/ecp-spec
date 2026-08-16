# GO-8C — NT-05 SEMANTIC REVIEW PROTOCOL (Revisão Semântica Mínima — Painel de IAs Independentes)

**Data:** 2026-08-13
**Ciclo:** GO-8C
**Origem:** DECISION D-03 (Alternativa B, ATUALIZADA) — substituição **parcial** do requisito humano NT-05.
**Status:** REGISTERED (pré-registrado; aguardando execução pelo painel de 2 IAs independentes).
**Referência congelada:** `GO-8B/03-SYNTHETIC-TAXONOMY-C3.md` §4.1/§4.2/§4.3/§4.4 (histórico).

---

## 1. Objetivo

Detectar **contaminação conceitual por paráfrase** na taxonomia C3 e nos materiais de entrada que **não é capturada** pelos checks lexicais/estruturais determinísticos (NT-01..NT-04 e suítes operacionais). É o componente semântico do BIP-VAL que a auditoria automatizada não cobre.

## 2. Escopo da Revisão

- **Alvo primário:** as 12 categorias de `C3_TAXONOMY.yaml` (`SYN-001` .. `SYN-012`), namespace `SYN`.
- **Alvo secundário:** amostra dos materiais de entrada (narrativas reconstruídas / atomic facts) — ou todos os materiais, conforme viabilidade. A cobertura efetiva deve ser registrada no formulário de evidências (§5).
- **Fonte de comparação:** vocabulário ECP operacional (52 termos, conforme `C3_TAXONOMY.yaml → ecp_term_list`) e as hipóteses/mappings ECP (não expostos ao revisor na condição de cegueira; ver §6).

## 3. Participantes — Painel de 2 IAs Independentes (Três Abas Separadas)

### 3.1 Método de três abas

O painel opera em **três abas totalmente separadas e independentes**:

| Aba | Papel | Participação na revisão |
|---|---|---|
| **Executor** | Esta sessão de preparação/coordenação | **NÃO participa como revisor** — apenas disponibiliza o pacote e, após a execução, consolida os formulários |
| **Revisor 1** | 1ª IA independente (via `REVIEW-FORM-MODEL-1.md`) | Executa a revisão de forma independente |
| **Revisor 2** | 2ª IA independente (via `REVIEW-FORM-MODEL-2.md`) | Executa a revisão de forma independente |

As abas **não comunicam entre si** durante a revisão. Cada revisor recebe **somente** o seu prompt padrão, o pacote `review/` e a sua via do formulário.

### 3.2 Modelos

- **Modelos diferentes:** 2 IAs de **arquiteturas/provedores diferentes** — ex. indicativos: **Revisor 1 = GLM-4.5 Flash**, **Revisor 2 = Nemotron 3 Ultra**. Se um dos modelos não estiver disponível, **outro modelo de arquitetura/provedor distinto pode substituí-lo**; o modelo efetivo é registrado na execução.
- **Contextos completamente limpos:** cada IA opera **sem acesso ao histórico do projeto** — sem contexto de sessão de desenvolvimento, sem decisões anteriores, sem conversas prévias, sem qualquer informação além do próprio pacote de revisão (`review/`).
- **Preenchimento independente:** cada IA preenche **o mesmo formulário** `REVIEW-FORM.md` em via própria (`REVIEW-FORM-MODEL-1.md` / `REVIEW-FORM-MODEL-2.md`).
- **Justificativa do painel:** reduzir risco de viés correlacionado — arquiteturas/provedores distintos têm fronteiras de generalização semântica diferentes.

### 3.3 Restrição de acesso

Cada revisor (aba de revisão) **só pode ler**:

- Arquivos dentro de `experiments/validation/GO-8C/review/` (incluindo `review/materials/`), e
- Os **itens a revisar** (materiais de entrada e `C3_TAXONOMY.yaml`), disponibilizados como cópias de leitura em `review/materials/`.

**É proibido** ao revisor acessar:

- O código executor / scripts (qualquer `*.py`, `p*_*.py` do projeto),
- O histórico de decisões (arquivos `decisions/`, `ACTION-REGISTER.md`, propostas, validações) fora do pacote,
- Qualquer outra pasta do projeto fora de `experiments/validation/GO-8C/review/`.

Os prompts padrão (§ `REVIEW-PANEL-PROCEDURE.md`) reforçam essa restrição.

## 4. Rubrica Pré-registrada

Cada IA classifica cada item revisado em **até 3 categorias de violação** (pode marcar múltiplas; 0 se nenhuma):

| Categoria | Descrição | Exemplo indicativo |
|---|---|---|
| **Categoria 1 — Violação de isolamento SYN** | Conteúdo ECP ou CAT **indevido** presente em labels, definições, source_refs ou narrativas (não capturado por check lexical). | Definição que incorpora termo/conceito ECP por extenso, mesmo sem a palavra exata da lista de 52. |
| **Categoria 2 — Paráfrase de termo ECP** | Um termo/conceito ECP reexpresso com sinonímia ou paráfrase, de modo que a varredura léxica não o detecta. | Conceito ECP descrito com outra construção sintática sem o termo canônico. |
| **Categoria 3 — Viés estrutural na narrativa/atomic facts** | Padrão estrutural ou de seleção que comprometa a **cegueira** (ex.: narrativa que direciona o avaliador para a identidade da condição/ECP). | Nomes/ordem/omissões sistemáticas que revelem a condição de origem. |

## 5. Critério de Aprovação (Unanimidade)

- **Aprovação:** **≤ 0** (nenhuma) ocorrência nas categorias acima **em AMBAS as vias** — ou seja, **nenhuma violação semântica não capturada** pelos testes automatizados, **por nenhuma das 2 IAs**.
- **Unanimidade obrigatória:** o gate é `PASS` somente se **AMBOS** os modelos retornarem `PASS` em **todas** as categorias/item.
- **Divergência entre modelos = STOP:** se os 2 modelos divergirem em qualquer item/categoria (inclusive `SEM VIOLAÇÃO` × `VIOLAÇÃO`), o resultado é **STOP** — **NÃO é aceitável votação por maioria** nem consolidação ad hoc. A divergência é registrada e encaminhada à governança.
- **Votação é proibida:** nenhum mecanismo de maioria/consenso automático; divergência SEMPRE = STOP.
- **Qualquer ocorrência** (≥ 1) em qualquer via → **REJEITADO**: correção do item e **revalidação** completa (nova execução do protocolo), antes de qualquer uso do artefato.
- O resultado é **binário por item e global**: cada item revisado recebe veredito `SEM VIOLAÇÃO` / `VIOLAÇÃO (cat. X)`; o veredito global é `PASS` somente se **todas as vias e todos os itens** = `SEM VIOLAÇÃO`.

## 6. Formulário de Evidências (pré-registrado)

Cada item revisado gera registro objetivo com veredito por item (em cada via):

```yaml
- item_id: SYN-001            # ou material-id / atomic-fact-id
  item_type: C3_CATEGORY      # C3_CATEGORY | INPUT_MATERIAL | ATOMIC_FACT
  reviewer_model: "<modelo/versão>"
  reviewer_hash: "<hash_anon>"
  reviewed_on: "YYYY-MM-DD"
  violations: []              # [] = sem violação | ["C1"] | ["C2"] | ["C3"] | combinações
  notes: "Racional sucinto da avaliação; trecho relevante se houver"
  verdict: "SEM VIOLAÇÃO"     # SEM VIOLAÇÃO | VIOLAÇÃO
```

**Regras de registro:**
- Cada via identifica o **modelo/versão** e um **hash anônimo** da execução (sem identidade nominal).
- `reviewed_on` preenchido na data efetiva da revisão.
- `notes` obrigatório quando houver violação; opcional quando `SEM VIOLAÇÃO`.
- Cobertura efetiva (quais itens/alvo secundário) registrada no cabeçalho de cada via.
- As vias são **independentes e não comunicam entre si**.

## 7. Condições de Cegueira e Independência

- Cada IA **não conhece**: mapping C2 (permutação), resultados SX-001, hipóteses ECP específicas, nem a identidade das condições (espelha o escopo de cegueira do BIP-VAL).
- **Contexto limpo:** nenhum acesso ao histórico do projeto (sessões anteriores, decisões, conversas). Cada IA recebe apenas o pacote `review/` + formulário próprio.
- **Acesso restrito:** cada revisor lê somente `experiments/validation/GO-8C/review/` (incluindo `review/materials/`) e os itens a revisar; **sem acesso** ao código executor nem ao histórico de decisões.
- **Independência por arquitetura/provedor e por aba:** os 2 modelos são diferentes, cada um em aba separada, sem comunicação entre vias.
- O **agente executor não participa como revisor**; atua apenas na preparação do pacote e, posteriormente, na consolidação.
- A execução da revisão é **posterior** à implementação desta etapa (Decisão D-03) e ocorrerá como etapa subsequente, com registro em artefato de validação próprio.

## 8. Relação com os Testes Automatizados

- Os testes determinísticos (NT-01..NT-04 e suítes operacionais) permanecem **inalterados** e são pré-requisito (`ALL PASS`) para o artefato.
- Este protocolo **complementa** o gate objetivo com o julgamento semântico mínimo; **não** substitui nenhum teste existente.
- **Procedimento operacional:** ver `review/REVIEW-PANEL-PROCEDURE.md` (abertura das três abas, prompts padrão, salvamento e comparação dos formulários).
- **Limitação explícita:** *"NT-05 substituído por painel de IAs independentes por indisponibilidade humana. Não há equivalência epistemológica com revisão humana."*

## 9. Status do BIP-VAL do GO-8C

- Até a execução da revisão do painel: `NT-05: SUBSTITUTED_PARTIAL (2 independent AI reviewers)` e `verdict: PASS_PENDING_AI_PANEL`.
- Após execução e aprovação unânime: nova validação registrada; `verdict` atualizado para `PASS`.
- Em caso de **STOP** (divergência): `verdict` permanece pendente; divergência registrada e escalada à governança.

---

**Fim do protocolo. Pré-registrado em 2026-08-13 (atualizado para painel de 2 IAs independentes em três abas separadas com acesso restrito). Nenhum arquivo do GO-8B alterado.**
