# D-05 — PROTOCOLO DO GATE SEMÂNTICO HÍBRIDO (Humano + IA)

**Data:** 2026-08-14
**Ciclo:** GO-8D — DIAGNOSTIC PHASE
**Tipo:** protocolo de produção (gate semântico do próximo ciclo GO-8D)
**Base:** `GO-8C/decisions/NT-05-SEMANTIC-REVIEW-PROTOCOL.md` (painel de IAs independentes, 2026-08-13) · `GO-8B/decisions/NT-05-AUTOMATED-INDEPENDENT-REVIEW.md` (auditoria automatizada, 2026-08-12) · `GO-8B/decisions/NC-01-HUMAN-REVIEW-SUBSTITUTION.md`
**Dependência:** deve estar concluído **antes** do novo Lock (D-07) — ver `D-03-DESIGN-REVIEW.md` §6

---

## 1. Objetivo

Fortalecer o gate semântico do GO-8D combinando, em camadas explícitas e auditáveis:

1. **Auditoria automatizada obrigatória** — checks determinísticos (herdados do GO-8B/GO-8C, sem
   alteração do engine congelado).
2. **Painel independente de IAs** — como já realizado no GO-8C (NT-05 substituto parcial), com
   arquiteturas/provedores distintos, contexto limpo e três abas.
3. **Amostra humana opcional** — revisão humana qualificada quando disponível, **sem** equivalência
   epistemológica entre as camadas.

O protocolo mantém a limitação registrada no GO-8C: *"Não há equivalência epistemológica entre a
revisão por painel de IAs e a revisão humana de três validadores independentes."*

---

## 2. Camadas do gate e obrigatoriedade

| Camada | Natureza | Obrigatória | Pré-requisito |
|---|---|---|---|
| **L1 — Auditoria automatizada** | Checks determinísticos (parseabilidade, léxico, estrutura, rastreabilidade, hashes) | **Sim** | ALL PASS para prosseguir |
| **L2 — Painel independente de IAs** | Revisão semântica mínima por ≥ 2 IAs de arquiteturas/provedores distintos, em abas separadas | **Sim** | L1 = PASS |
| **L3 — Amostra humana opcional** | Revisão humana qualificada de amostra, quando disponível | **Opcional** (ativação condicional) | L1 = PASS, L2 = PASS ou em avaliação |

**Princípio:** L1 é o guarda-corpo determinístico; L2 é o componente semântico mínimo; L3 é
reforço adicional. **Nenhuma camada é suprimida por outra.** A ausência de L3 (indisponibilidade
humana) é registrada como limitação, não como falha.

---

## 3. L1 — Auditoria automatizada (obrigatória)

Herdada dos ciclos anteriores, **sem alteração do engine congelado**:

| Check | Origem | Critério PASS |
|---|---|---|
| Parseabilidade dos materiais (`## Fatos`, ≥15 fatos, formato) | D-04 (GO-8D) — `validate_parseability.py` | ALL PASS por BIP |
| Checks lexicais (0 hits ECP na taxonomia/narrativa do namespace correto) | GO-8B P5 / GO-8C | 0 ocorrências |
| Estrutura da taxonomia (DAG, nós/arestas, labels do namespace) | GO-8B C3 / GO-8C | Schema PASS |
| Rastreabilidade dos atomic facts (`[ref]` válido) | GO-8B / GO-8C MAT-03 | 100% |
| Hashes das fontes e dos outputs | GO-8B / GO-8C | SHA-256 registrados |
| Taxonomia usada registrada (`taxonomy_sha256` + `taxonomy_version`) | D-03 P5 (GO-8D) | Presente por execução |

**Regra:** L1 = **ALL PASS** é pré-requisito absoluto. Qualquer FAIL → STOP e correção antes de
qualquer revisão semântica.

---

## 4. L2 — Painel independente de IAs (obrigatório)

Reproduz o protocolo do GO-8C (NT-05 SEMANTIC REVIEW) com as mesmas salvaguardas:

### 4.1 Composição

- **≥ 2 modelos de arquiteturas/provedores distintos** (ex. indicativos: GLM-4.5 Flash e
  Nemotron 3 Ultra). Modelo efetivo registrado na execução.
- Cada revisor opera em **aba separada**, com **contexto limpo** (sem acesso ao histórico do
  projeto) e acesso **restrito** ao pacote de revisão.
- O agente executor **não participa como revisor** — apenas prepara o pacote e consolida.

### 4.2 Escopo da revisão

- **Alvo primário:** taxonomia C3 corrigida (`SYN-001..012` e `CAT-XX` com definições neutras —
  as correções P2/P3 do D-03).
- **Alvo secundário:** narrativas reconstruídas e atomic facts (cobertura efetiva registrada).
- **Categorias de violação** (rubrica pré-registrada do GO-8C):
  1. Violação de isolamento do namespace (conteúdo ECP/CAT indevido);
  2. Paráfrase de termo ECP não capturada por check lexical;
  3. Viés estrutural na narrativa/atomic facts que comprometa a cegueira.

### 4.3 Regras de divergência e veredito

| Resultado | Condição | Ação |
|---|---|---|
| **PASS** | **Todas** as vias, **todos** os itens = `SEM VIOLAÇÃO` | Avança para L3 (ou Lock se L3 não ativa) |
| **VIOLAÇÃO (≥1)** | Qualquer via reporta ≥1 violação | **REJEITADO**: corrigir item + **revalidação completa** do gate (nova execução) |
| **DIVERGÊNCIA** | Vias discordam em qualquer item (incl. `SEM VIOLAÇÃO` × `VIOLAÇÃO`) | **STOP**: proibido votar/mediar; registra e escala à governança |

**Votação é proibida.** Divergência **sempre** = STOP.

### 4.4 Limites do painel (explícitos)

1. O painel **não substitui** a revisão humana (sem equivalência epistemológica).
2. O painel **não decide** desenho nem DV; verifica apenas a ausência de contaminação semântica
   não capturada por checks determinísticos.
3. O painel é executado **por produção de artefato** (taxonomia e materiais), não por execução.
4. O painel opera **às cegas**: sem mapping C2, sem hipóteses ECP, sem identidade das condições.
5. **Proibido** ao revisor acessar código executor, histórico de decisões ou qualquer arquivo
   fora do pacote de revisão.

---

## 5. L3 — Amostra humana opcional

### 5.1 Critérios de ativação

L3 é ativada **somente se** houver **≥ 1 revisor humano qualificado disponível** no momento da
produção do artefato. Não é acionada por default; a indisponibilidade **não** bloqueia o gate
(registrada como limitação).

**Indicadores de priorização (ativação seletiva) quando humanos disponíveis mas escassos:**

- Artefatos com qualquer violação histórica (ex.: BIP-009-Chernobyl) → alta prioridade;
- Taxonomia corrigida (novas definições `CAT_NEUTRAL_DEFS` / SYN corrigidas) → alta prioridade;
- Materiais com divergência L2 já resolvida ou limiar de risco — conforme §6.

### 5.2 Escopo da amostra

Quando ativada, a amostra humana cobre, **no mínimo**:

- As categorias da taxonomia C3 com definições alteradas pela correção P2/P3 (D-03);
- BIPs reincidentes em falhas de parseabilidade/validação nos ciclos anteriores;
- Uma amostra aleatória complementar de atomic facts/narrativas (registrada com seed, pré-coleta).

### 5.3 Papel do humano

- Validar a **plausibilidade semântica** das definições corrigidas e da ausência de contaminação,
  com acesso ao vocabulário ECP operacional e às hipóteses de comparação — **sem acesso ao
  resultado experimental** (cegueira preservada).
- Registrar veredito por item no mesmo formulário do painel, com identificação de revisor
  (anônima) e data.

### 5.4 Relação com o painel

- L3 **não** substitui L2 e **não** desfaz divergência (divergência L2 permanece STOP).
- Se L3 divergir de L2 em item com veredito unânime do painel, a divergência é **registrada e
  escalada à governança** (não é votação por maioria).
- Se L3 concordar com L2 unânime, o veredito é reforçado (auditoria de confirmação).

---

## 6. Regras de divergência — visão consolidada

| Camadas | Cenário | Ação |
|---|---|---|
| L1 | Qualquer FAIL | STOP — correção e reexecução de L1 |
| L2 | PASS unânime | Prosseguir (L3 opcional) |
| L2 | ≥1 VIOLAÇÃO | REJEITADO — correção + revalidação completa |
| L2 | DIVERGÊNCIA entre vias | STOP — sem votação; escala à governança |
| L2×L3 | L3 discorda de L2 unânime | Registra e escala à governança (não vota) |
| L2×L3 | L3 concorda com L2 unânime | Veredito reforçado (confirmação) |

**Regra invariável:** nenhuma votação por maioria; qualquer divergência entre vias independentes
é tratada como STOP ou escalada, nunca como consenso automático.

---

## 7. Forma de documentação

Cada execução do gate gera um **formulário de evidências** por camada:

```yaml
gate_run_id: "G-8D-<artefato>-<data>"
artefato: "<taxonomia-c3 | materia-bip-xxx | ...>"
taxonomy_sha256: "<hash da taxonomia usada>"
camadas:
  L1:
    status: PASS
    itens: {parseabilidade: PASS, lexical: PASS, estrutura: PASS, rastreabilidade: PASS, hashes: PASS, taxonomy_registro: PASS}
    tool_version: "validate_parseability.py v1"
  L2:
    status: PASS            # PASS | REJEITADO | STOP(DIVERGÊNCIA)
    revisores: [{modelo: "...", hash_anon: "...", vias: "independente"}]
    cobertura: {primario: "...", secundario: "..."}
    itens: [{item_id: "SYN-001", violations: [], verdict: "SEM VIOLAÇÃO"}]
  L3:
    ativada: false          # true/false
    status: NA              # NA | PASS | DIVERGÊNCIA_ESCALADA
    revisores_humanos: [{codigo_anon: "...", data: "..."}]
    amostra: {regra: "...", seed: "..."}
veredito_final: PASS
registro: "<link ACTION-REGISTER.md>"
```

**Regras de documentação:**

- Cada execução **independente** gera via própria; vias **não comunicam** entre si.
- Divergência/STOP/REJEITADO são registrados **obrigatoriamente** com `notes` e escalados.
- O resultado do gate é registrado no `ACTION-REGISTER.md` do GO-8D e referenciado no
  pré-registro do novo estudo (D-07) antes do Lock.

---

## 8. Fluxo operacional do gate no próximo ciclo

```
Produção do material/taxonomia
        │
        ▼
   L1 auditoria automatizada ──FAIL──► STOP + correção
        │ PASS
        ▼
   L2 painel de IAs ──VIOLAÇÃO/──► REJEITADO/STOP + correção + revalidação completa
        │ PASS (unânime)
        ▼
   L3 humano (se ativo) ──divergência──► escala à governança
        │ (concorda ou NA)
        ▼
   Veredito PASS → habilita pré-registro/Lock (D-07)
```

---

## 9. Confirmação de integridade

- **Nenhum arquivo do GO-8B/GO-8C alterado**; GO-8B e GO-8C permanecem CLOSED/LOCKED/FROZEN.
- Este protocolo é **pré-registrado como desenho** — não executado. A execução do gate ocorrerá
  **na produção do próximo ciclo**, após autorização por etapa.
- **Nenhum recálculo de N, novo pré-registro, Lock ou execução experimental realizado.**

---

**Fim do protocolo D-05. 2026-08-14. Status: PROPOSED (pré-registrado) — aguardando aceite da
governança; execução apenas na produção do próximo ciclo.
