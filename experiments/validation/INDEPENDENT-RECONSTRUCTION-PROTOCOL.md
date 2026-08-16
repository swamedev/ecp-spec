# Independent Reconstruction Protocol (IRP) — Desenho metodológico (GO-6)

| Campo | Valor |
|---|---|
| **Comando** | GO-6 — AUTORIZAR DESENHO DO MECANISMO DE INDEPENDÊNCIA DEBT-001/006 |
| **Tipo** | Proposta técnica/metodológica (desenho; **não normativo** até revisão da coordenação) |
| **Status** | **PROPOSTA — aguarda revisão da coordenação** |
| **Data** | 2026-08-09 |
| **Autor** | Executor do desenho (GO-6) |
| **Dívidas atacadas** | [DEBT-001](../METHODOLOGICAL-DEBT.md), [DEBT-006](../METHODOLOGICAL-DEBT.md) |
| **Governado por** | [P-0007.1](./P-0007.1-INDEPENDENCE-FRAMEWORK.md) (RA-OI-003 — reconstrução cega), [SHADOW-EXPERIMENTS](./independence/SHADOW-EXPERIMENTS.md) (regra 7), [METHODOLOGICAL-DEBT](./METHODOLOGICAL-DEBT.md) |
| **Referências** | [SX-003/report/09-auditoria-isolamento-go4b](./independence/SX-003/report/09-auditoria-isolamento-go4b.md), [SX-003/report/10-decisao-coordenacao-go5a](./independence/SX-003/report/10-decisao-coordenacao-go5a.md) |

---

## 0. Objetivo do GO-6

Especificar um **mecanismo verificável** para separar a produção da narrativa da
**reconstrução cega**, resolvendo a cadeia DEBT-001 → DEBT-006 → SX-003 → GO-4B
**para uso futuro**, sem resolver retrospectivamente a contaminação do SX-003.

**Escopo do desenho:** isolamento, manifesto de entrada, congelamento, hashes e
audit trail.

### Restrições do GO-6 (respeitadas)

| Restrição | Estado neste desenho |
|---|---|
| Não alterar SX-003 | ✅ nenhum arquivo de SX-003 tocado |
| Não alterar P-0010 | ✅ não tocado |
| Não alterar SX-SELECTION | ✅ não tocado |
| Não alterar protocolo congelado | ✅ não tocado |
| Não executar novo experimento | ✅ apenas desenho |
| Não criar Pattern ou LAW-H | ✅ nenhuma promoção |
| Não resolver retrospectivamente a contaminação do SX-003 | ✅ o vazamento permanece registro (GO-5A) |

---

## 1. O problema: "não consulte" não é cegueira

A blindagem do pipeline atual (SHADOW-EXPERIMENTS, regra 7) é uma **instrução**:
"quem reconstrói não lê a narrativa oficial antes". A GO-4B mostrou o limite
desse modelo: o mesmo executor já carregava o conhecimento dos SX-001/002 e a
**instrução** de não comparar foi violada dentro da reconstrução — com a
diferença registrável de que a violação **permaneceu como dado** (resultado
metodológico do próprio experimento).

A lição consolida uma exigência de desenho:

> Uma propriedade epistemológica (cegueira) só é útil ao programa quando pode ser
> **verificada sobre o sistema**, não apenas **declarada no protocolo**.

---

## 2. O que significa "independente" — três níveis

| Nível | Modelo | Força | Verificável? |
|---|---|---|---|
| **I** | Instrução humana: "não consulte" | 🔴 baixa | Não — depende de adesão não observável |
| **II** | Separação de arquivos + controle de acesso | 🟡 média | Parcialmente — força o caminho, não prova a origem da informação |
| **III** | Ambiente isolado + manifesto + hash + audit trail | 🟢 forte | Sim — cada condição de cegamento vira uma checagem executável |

> **Recomendação para o ECP: Nível III.** Não por exigir infraestrutura grande —
> por transformar propriedades epistemológicas em **propriedades verificáveis do
> sistema** (Claim → Evidence → **Audit** → Decision).

---

## 3. Mecanismo proposto — arquitetura

```
NARRATIVE PRODUCER
       │
       ▼
  Narrative Package          (fontes + narrativa + AFs — a verdade de referência)
       │
       │ 🔒 selo (hash + timestamp no momento da separação)
       │
       ├───────────────┐
       │               │
       ▼               ▼
   Evidence        Blind Input
   Archive         Package (BIP)      ← único insumo autorizado da reconstrução
       │               │
       ▼               ▼
              INDEPENDENT RECONSTRUCTOR
       (principal distinto; NÃO recebe o Narrative Package)
                       │
                       ▼
               Reconstruction          (texto da reconstrução cega)
                       │
                       ▼
                Freeze / Hash          (imutável a partir daqui)
                       │
                       ▼
             Isolation Audit          (condições de cegamento checadas)
                       │
                       ▼
              Narrative Reveal        (só agora a narrativa é revelada)
                       │
                       ▼
              Alignment Analysis      (comparação reaberta)
```

### 3.1 Papéis — principals distintos

A separação não é um cargo retórico; é um **principal** (processo/sessão/agente
com contexto próprio e escopo de acesso definido):

| Papel | Acesso | Fora de acesso |
|---|---|---|
| **Narrative Producer** | fontes, narrativa, AFs | — |
| **Independent Reconstructor** | **somente BIP** | Narrative Package, demais SX-###, relatórios EAR/Signals anteriores |
| **Isolation Auditor** | manifestos + trilhas + hashes | conteúdo interpretativo em avaliação |

Se o executor físico for o mesmo (limitação DEBT-001/006), a separação é feita
por **isolamento de contexto**: sessão reconstrução com estado inicial **nulo
em relação** a SX-001/002/003 e ao vocabulário interpretativo — e isso é
**rastreado**, não assumido.

### 3.2 Pacotes e interfaces

- **Narrative Package (NP):** fontes verificadas + narrativa original (zero
  vocabulário ECP) + Atomic Facts. É a verdade de referência — **selada** no
  momento da separação (hash + timestamp).
- **Evidence Archive:** cópia imutável do NP com proveniência (árvore origem →
  fontes derivadas, RA-EI-004), para auditoria posterior.
- **Blind Input Package (BIP):** o **único** insumo permitido da reconstrução —
  pacote **factual autorizado**, extraído do NP, com:

  - somente Atomic Facts autorizados (e sua proveniência por fato);
  - instruções neutras de reconstrução ("registre inferências como inferências",
    "ausência é dado");
  - **proibido no BIP:** prosa interpretativa da narrativa, referências cruzadas
    a SX-001/002/003, vocabulário ECP interpretativo, conclusões comparativas.

Regra fundamental:

> O Independent Reconstructor **não recebe a narrativa** — recebe somente o
> pacote factual autorizado (BIP). A revelação da narrativa ocorre somente depois
> do **congelamento** da reconstrução.

### 3.3 Manifiesto de entrada (BIP Manifest)

O BIP é acompanhado de um manifesto verificável:

| Campo | Conteúdo |
|---|---|
| `bip_version` | versão do pacote |
| `af_ids` | lista exaustiva de AF incluídos |
| `sources` | origens causais + hashes dos documentos |
| `digests` | hash de cada AF e do BIP inteiro (SHA-256) |
| `exclusions` | o que foi **deixado de fora** do NP (itens interpretativos) |
| `constraints` | restrições impostas à reconstrução (neutralidade, inferências explícitas) |
| `seal` | assinatura+timestamp do selador (Narrative Producer / coordenação) |

O manifesto permite ao **auditor** reprovar um BIP que contenha qualquer item
fora da lista — antes mesmo da reconstrução.

### 3.4 Congelamento (Freeze) + hashes

- No fim da reconstrução, o artefato é **congelado**: hash SHA-256 + timestamp,
  sem edição subsequente.
- O congelamento produz o registro `FRZ-###` (hash pré-reveal), que é a âncora
  temporal: **tudo depois disso não pode alterar o que foi reconstruído cegamente**.
- Qualquer mudança pós-freeze é **nova versão**, marcada e auditável — nunca um
  retoque silencioso.

### 3.5 Audit trail

Trilha mínima obrigatória (toda com timestamp e identidade do principal):

1. criação do NP e seu selo;
2. derivação do BIP (quais AFs, quais exclusões) e seu meanifesto;
3. abertura de sessão do Reconstructor **sem** acesso ao NP (escopo efetivo
   logado);
4. inputs efetivamente lidos pela sessão (lista de arquivos acessados);
5. congelamento da reconstrução (`FRZ-###`);
6. auditoria de isolamento; 
7. revelação da narrativa (ponto em que a comparação fica legítima).

### 3.6 Isolation Audit + Narrative Reveal

A **Isolation Audit** verifica, em ordem:

1. **Integridade do BIP:** conteúdo real == conteúdo do manifesto (digests batem)? Nada extra?
2. **Escopo efetivo:** a trilha mostra a sessão do Reconstructor lendo **apenas** caminhos do BIP? Zero acesso ao NP?
3. **Ausência de contaminação cruzada:** busca por referências a SX-001/002/003 e a frases-âncora da narrativa no texto **congelado**?
4. **Ordem temporal:** `timestamp(FRZ) < timestamp(Narrative Reveal)` e trinta de acesso ao NP **antes** do FRZ igual a vazio?

Somente com as quatro condições **verdes** o experimento é classificado como
cegueira **verificada**. Sem isso, a classificação registrada é
**comprometida** — e o vazamento, quando existe, **permanece como registro**
(lição do GO-4B), nunca apagado.

---

## 4. A evolução conceitual (o que muda no vocabulário)

```
antes:  "A reconstrução é cega."
depois: "A reconstrução satisfaz condições verificáveis de cegamento."
```

A cegueira deixa de ser um **atributo** declarado e passa a ser um **invariante
auditável**. Isso eleva o padrão da cadeia:

```
Claim → Evidence → Audit → Decision
   (cada claim da reconstrução rastreia um AF do BIP; o audit valida o cegamento;
    a decisão (admissível/comprometido) é registrada antes do reveal)
```

---

## 5. Checklist de verificação (executável)

`IRP-CHECKLIST` — proposta de lista mínima de checagens automáticas:

| # | Checagem | Origem do invariante |
|---|---|---|
| C-01 | BIP contém apenas AF autorizados (digests do manifesto) | §3.3 |
| C-02 | BIP sem prosa interpretativa / sem referência cruzada a SX-### | §3.2 |
| C-03 | Sessão do Reconstructor sem acesso ao NP (trilha) | §3.5-2/3 |
| C-04 | Reconstrução congelada antes de qualquer revelação (`FRZ` < reveal) | §3.4/§3.6 |
| C-05 | Texto congelado sem termos-âncora da narrativa (busca automatizada) | §3.6 |
| C-06 | Nenhum edit pós-freeze sem nova versão registrada | §3.4 |
| C-07 | Veredito de cegamento registrado **antes** da revelação | §3.6 |

Falha em qualquer C-## → veredito registrado como **comprometido**, sem retoques.

---

## 6. Por que Nível III para o ECP

- O objetivo do ECP é transformar **propriedades epistemológicas** em
  **propriedades verificáveis do sistema** — exatamente o que Nível III faz.
- O custo é baixo (hashes, manifestos, trilhas em texto); o benefício é
  central: **reprodutibilidade e auditabilidade do instrumento de produção de
  evidência**.
- Depois de três casos (DEBT-009), o programa não precisa correr para um quarto
  caso — precisa garantir que o **instrumento** que produz evidência é ele mesmo
  reprodutível e auditável.

---

## 7. Relação com DEBT-001/006 e a lição do SX-003

| Fonte | Lição | Tradução em requisito do IRP |
|---|---|---|
| DEBT-001 / DEBT-006 | mesmo executor em narrativa e reconstrução | principals distintos ou isolamento de contexto rastreado (§3.1) |
| GO-4B (SX-003) | instrução "não compare" violada dentro da reconstrução | C-02/C-05 tornam a proibição **checável**, não apenas declarada |
| GO-5A | vazamento permanece como registro; não apagar | §3.6: falha → "comprometido", registro preservado |
| P-0007.1 (RA-OI-003) | reconstrução cega exige não ler a narrativa antes | C-03/C-04 — exigência elevada a invariante auditável |

> Este desenho é **candidato a resolução** de DEBT-001/006 na consolidação v1.1
> (registro de proposta; **não** altera o METHODOLOGICAL-DEBT hoje).

---

## 8. O que este desenho NÃO faz

- ❌ Não altera o SX-003 nem resolve retrospectivamente sua contaminação.
- ❌ Não altera P-0010, SX-SELECTION, SHADOW-EXPERIMENTS nem qualquer protocolo congelado.
- ❌ Não executa experimento novo.
- ❌ Não promove Signal a Pattern, nem Pattern a LAW-H.
- ❌ Não decide ainda como o SX-003 entrará no transversal (decisão reservada à
  coordenação após resolução do isolamento — GO-5).

---

## 9. Perguntas abertas para a coordenação

1. O IRP deve valer para **todos** os SX futuros ou ser executado como
   **experimento-piloto de método** (ex.: reexecução isolada da camada de
   reconstrução do SX-003) antes de virar padrão?
2. O Reconstructor deve ser **outra entidade** (ex.: segundo modelo/agente) ou é
   suficiente **isolamento de contexto** rastreado dentro da mesma entidade?
3. Os Atomic Facts (camada DEBT-003) passam a ser **parte oficial do BIP** ou o
   BIP deriva direto das fontes?
4. Quem exerce o papel de **Isolation Auditor** sem criar novo gate burocrático?
5. Em que documento o IRP será formalizado na v1.1 (evolução de
   SHADOW-EXPERIMENTS, novo P-0007.x, ou seção do METHODOLOGICAL-DEBT)?

---

## 10. PARAR

Após este registro de desenho, **PARAR para revisão da coordenação**.

- ✅ Nenhum protocolo congelado alterado.
- ✅ Nenhum artefato científico do SX-003 tocado (contaminação permanece registro — GO-5A).
- ✅ Nenhuma promoção, nenhum experimento novo, nenhum commit.

> **Próximo encaminhamento possível (decisão da coordenação):** aprovar/ajustar
> este desenho → validar o IRP → então decidir o tratamento da camada
> contaminada do SX-003 → só depois GO-5 (transversal).

---

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-09 | Desenho GO-6: Independent Reconstruction Protocol. Níveis I/II/III (recomendação Nível III). Arquitetura Narrative Producer → NP selado → Evidence Archive + BIP → Reconstructor → Freeze/Hash → Isolation Audit → Reveal. Manifiesto de entrada, hashes e audit trail. Checklist C-01..C-07. Relação com DEBT-001/006, GO-4B e GO-5A. **PROPOSTA — PARAR para revisão da coordenação.** |