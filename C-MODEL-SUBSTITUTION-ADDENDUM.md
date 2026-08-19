# C-MODEL-SUBSTITUTION-ADDENDUM

## Adendo Controlado — Mecanismo de Consenso de Rótulos (MR-C7)

**Data:** 2026-08-18
**Status:** ADENDO CONTROLADO — **NÃO EXECUTA O GATE; AGUARDA CONFIRMAÇÃO DA GOVERNANÇA**
**Documento base:** `MR-C7-PROTOCOLO-PREREGISTRO.md`
**Hash do protocolo antes desta edição (verificado em 2026-08-18):** `cdc6aecacade51142a178713869ac67d228e1aeb3b1a21e1eee36d81efea5b69`
**Tipo de desvio registrado:** **DESVIO DE MÉTODO** (substituição do mecanismo de consenso), não de versão — por indisponibilidade total de APIs de LLM utilizáveis

---

## 1. Contexto

O protocolo `MR-C7-PROTOCOLO-PREREGISTRO.md` §4.3 congela a rotulação dos estados V0–V3 por
**consenso de IA** entre três modelos nomeados (`claude-3-opus-20240229`,
`gpt-4-2024-08-06`, `gemini-1.5-pro-20240801`), com regra ≥2/3. A governança determinou que,
antes da escolha do mecanismo de execução, fosse verificada a disponibilidade de APIs de LLM
externas no ambiente.

---

## 2. Verificação de acesso (2026-08-18)

| Item | Resultado |
|------|-----------|
| Conectividade a `api.anthropic.com/v1/models` | ALCANÇÁVEL (HTTP 401 — endpoint vivo, sem auth) |
| Conectividade a `api.openai.com/v1/models` | ALCANÇÁVEL (HTTP 401) |
| Conectividade a `generativelanguage.googleapis.com/v1beta/models` | ALCANÇÁVEL (HTTP 403) |
| Conectividade a `api.deepseek.com/v1/models` | ALCANÇÁVEL (HTTP 401) |
| Chaves de API no ambiente (variáveis de ambiente, 13 nomes padrão) | **NENHUMA** presente |
| Arquivos `.env` no workspace | Nenhum |
| Proxy de rede configurado | Nenhum |
| Única credencial existente | `auth.json` **interno do harness opencode** (`~/.local/share/opencode/`) — credencial do próprio harness para seu provedor de modelo; **não é** chave de API de uso geral, não é exportável para os scripts de execução do gate e não pode ser usada de forma segura/confiável |

**Conclusão:** o ambiente **não tem isolamento físico** (há conectividade de rede), mas **não há
nenhuma API de LLM externa utilizável programaticamente** (ausência total de credenciais).
Trata-se de **isolamento funcional** para fins de execução do gate.

---

## 3. Decisão (por determinação da governança)

Sem nenhuma API de LLM utilizável, o consenso dos três modelos nomeados é **inexecutável** e não
existe versão corrente de provedor algum que possa ser chamada (o que descaracteriza o "desvio de
versão"). Em conformidade com a determinação da governança (resposta de 2026-08-18), o mecanismo
de rótulos passa a ser:

> **Consenso algorítmico determinístico de três sinais independentes** (relevância temática,
> redundância lexical/entailment, novidade estrutural), com a correção factual ancorada ao
> gerador sintético — regra de consenso ≥2/3 preservada.

Este desvio é registrado como **desvio de método** (não de versão), documentado neste adendo,
**aprovado condicionalmente** pela governança, e **sujeito à camada extra de ressalva** no §5 do
protocolo (§6 deste adendo).

---

## 4. Sinais de rotulação algorítmica (substitutos dos 3 avaliadores)

Para cada candidato de cada caso, três sinais **independentes e determinísticos** produzem duas
decisões: **correção** (`verdadeiro`/`falso`) e **relevância** (`relevante`/`redundante`/
`irrelevante`). O rótulo do candidato é o **consenso ≥2/3** em ambas as dimensões (mesma regra do
§4.3).

| Sinal | Papel substituto | Sinal usado | Base de dados |
|-------|------------------|-------------|---------------|
| **S-A — Relevância temática** | (avaliador de "agrega ao núcleo do caso") | Sobreposição de tokens entre o candidato e o **núcleo temático do caso** (entidades centrais + fatos-base definidos pelo gerador) | Texto do candidato + metadados do gerador (entidades centrais) |
| **S-B — Redundância lexical/entailment** | (avaliador de "correto porém redundante") | Fração de tokens do candidato já cobertos pelo conjunto de fatos-base (sobreposição/subsumição) | Texto do candidato + texto dos fatos-base |
| **S-C — Novidade estrutural vs G0** | (avaliador de "adição estrutural") | Categorias intencionais do candidato (metadado do gerador) e se elas/relações já existem no grafo de verdade G0 do caso-base | Metadados do gerador (categoria intencional, relações desenhadas) + G0 |

**Âncora de correção:** o valor de verdade (verdadeiro/falso) é propriedade **objetiva do
gerador** (o gerador sabe o que é verdadeiro no caso). Todos os três sinais reportam a mesma
âncora factual do gerador; a discordância possível concentra-se na **dimensão de relevância**
(decisão semântica), que é onde o consenso ≥2/3 efetivamente opera.

**Atribuição de estado (inalterada, §4.3 do protocolo):**
- ΔV1 = `verdadeiro` **E** `relevante`
- ΔV2 = `verdadeiro` **E** `redundante`
- ΔV3 = `falso` **OU** `irrelevante`

**Todos os demais passos do protocolo permanecem inalterados** (geração, pares estruturais
casados, K=3 por sorteio determinístico, reconstrução, métrica, estatística, limiares, controles,
vetos).

---

## 5. Prova de não-compartilhamento (sinais de rotulação × métrica)

Determinação da governança: demonstrar que os sinais de rotulação algorítmica **não compartilham
modelo/pipeline** com `conf`/`ged_ref`/`div_metric`.

### 5.1 O que a métrica consome (inputs fechados)
| Componente | Processamento | Entrada | NÃO usa |
|------------|---------------|---------|---------|
| **conf** | F1 entre grafo de reconstrução e grafo de verdade do estado | grafos (nós = categorias, arestas = relações) | texto de candidatos; embeddings; WL kernel |
| **ged_ref** | similaridade estrutural WL-kernel (`s_struct` — hashing de estrutura, numpy puro) contra referência DATA-DRIVEN | dois grafos | texto de candidatos; embeddings; distribuição categórica |
| **div_metric** | Shannon / log(K) sobre a distribuição de categorias da reconstrução | contagem de categorias | texto de candidatos; embeddings; WL kernel |
| **DV** | média aritmética 1:1:1 | três componentes | — |

A métrica **nunca lê o texto dos fatos candidatos** e **não usa modelo de embedding** em nenhum
dos três componentes (o `ged_ref` usa apenas a variante estrutural do WL kernel, sem função de
embedding).

### 5.2 O que os sinais de rotulação consomem
| Sinal | Processamento | Entrada |
|-------|---------------|---------|
| S-A | sobreposição de conjuntos de tokens (strings) | texto do candidato + entidades centrais do gerador |
| S-B | sobreposição/subsumição de conjuntos de tokens (strings) | texto do candidato + texto dos fatos-base |
| S-C | consulta a metadados (categoria intencional, relações desenhadas) e a G0 | metadados do gerador + G0 |

Nenhum sinal usa **embedding**, **WL kernel**, **F1**, **entropia**, **grafo de reconstrução**
nem **referência DATA-DRIVEN**.

### 5.3 Invariantes de não-compartilhamento (a verificar e aplicar na execução)
1. **Sem modelo compartilhado:** nem a métrica nem os sinais usam modelo neural/embedding
   compartilhado. O único uso de embedding no gate é o classificador de categorias do pipeline de
   reconstrução (espelho do engine congelado, embedding por hash-fallback) — e ele é consumido
   **apenas** na geração das reconstruções (entrada da métrica), **nunca** pelos sinais de
   rotulação.
2. **Sem pipeline compartilhado:** a rotulação é concluída e gravada em registro estruturado
   **antes** de qualquer reconstrução e de qualquer cálculo de métrica (§6.4 do protocolo). A
   métrica não lê o registro de consenso além do valor de estado já fixado.
3. **Sem estrutura de dados compartilhada:** conjuntos de entrada disjuntos (tabelas 5.1 × 5.2).
4. **Separação de código:** módulos distintos (`labelers.py` × `metric.py` × `reconstruction.py`),
   sem importação cruzada entre `labelers` e `metric`; cada script hash-locked antes da execução;
   o relatório do gate inclui **checklist de inspeção de código** (grafo de importação + grep por
   símbolos compartilhados) como evidência.

### 5.4 Declaração
Com base nas invariantes 5.1–5.3, **os sinais de rotulação algorítmica não compartilham
modelo/pipeline com `conf`, `ged_ref` nem `div_metric`**. A independência é garantida por desenho
(entradas disjuntas), reforçada por separação de módulos e verificada por inspeção de código antes
da execução. Qualquer violação detectada na inspeção **aciona o Veto V-B** (integridade do
rótulo) — o gate não é executado até a violação ser corrigida e re-inspecionada.

---

## 6. Emenda ao §5 do protocolo (camada extra de ressalva)

A camada extra de ressalva exigida pela governança foi adicionada ao protocolo como nova subseção
**§5.1** — ver `MR-C7-PROTOCOLO-PREREGISTRO.md` (hash final registrado na §7). Ela declara:

- o ground truth deste gate é **consenso algorítmico determinístico**, **ainda mais fraco** que
  "consenso de IA" (nenhum modelo de IA participa);
- **qualquer PASS é PROVISÓRIO**, pendente de **reverificação com modelos de IA reais** (três
  provedores distintos, versões correntes) antes de qualquer decisão de governança sobre o GO-8E;
- um PASS algorítmico autoriza apenas a continuidade do processo de mensuração, **não** o uso
  confirmatório definitivo da métrica.

---

## 7. Registro de hashes

| Documento | SHA-256 |
|-----------|---------|
| `MR-C7-PROTOCOLO-PREREGISTRO.md` — antes deste adendo | `cdc6aecacade51142a178713869ac67d228e1aeb3b1a21e1eee36d81efea5b69` |
| `MR-C7-PROTOCOLO-PREREGISTRO.md` — após emenda §5.1 | calculado e reportado à governança no relatório; não registrado no próprio protocolo (convenção do repositório) |
| `C-MODEL-SUBSTITUTION-ADDENDUM.md` — este documento | registrado no protocolo, §16 |

---

## 8. Declaração

> Este adendo **não altera** nenhum limiar, critério de decisão, estatística, caso, controle,
> referência GED, agregação ou regra de veto do protocolo. Altera apenas o **mecanismo de
> rotulação** (de consenso de três modelos nomeados para consenso algorítmico determinístico) e a
> **leitura de validade** do resultado (PASS provisório).
>
> **Nenhuma execução do gate MR-C7 (Tarefa 4) ocorre até confirmação explícita da governança**
> sobre este adendo e sobre a emenda §5.1. Nenhum arquivo travado por hash foi alterado.

---

**Assinatura:** Governança ECP
**Data:** 2026-08-18
**Base:** Lock Manifest GO-8D-NC (`9247abcc8234c750ad1aa94ec3230e0cc93192783b9f0466e591f1b84fb2c058`)