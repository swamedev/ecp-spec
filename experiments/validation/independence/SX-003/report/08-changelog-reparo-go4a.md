# SX-003 / Changelog de reparo — GO-4A

| Campo | Valor |
|---|---|
| **Comando** | GO-4A — AUTORIZAR REPARO CONTROLADO |
| **Autor** | Executor do pipeline congelado (GO-4A) |
| **Data** | 2026-08-09 |
| **Regra** | Corrigir **somente** as corrupções listadas no GO-3 §1.2/§1.3. Nenhuma alteração por interpretação. Protocolo congelado intocado. |

> **Critério de verificação (GO-4A):** após cada correção, confirmar que o
> conteúdo **fático/classificatório/conclusivo** permanece inalterado — apenas a
> grafia/citação foi corrigida. Verificação de recontagem ao final (§4).

---

## 1. Correções aplicadas (diff auditável)

### 1.1 `narrative/01-narrativa-original.md`

| Linha | Antes | Depois | Tipo |
|---|---|---|---|
| ~49 (§3) | "majorçamente público" | "majoritariamente público" | digitação |
| ~79 (§6) | "dedicassse" | "dedicasse" | digitação |
| ~84 (§7) | "o IHG em evento" | "o IHGSC em evento" | sigla/abreviação |

### 1.2 `sources/00-fontes.md`

| Linha | Antes | Depois | Tipo |
|---|---|---|---|
| Grupo 4 | "DOE/ORN-000" | "DOE/ORNL" | sigla (ORNL) |
| nota | "Risco da terminolologia" | "Risco da terminologia" | digitação |
| nota | "painéis do NHGIR" | "painéis do NHGRI" | sigla (NHGRI) |

### 1.3 `reconstruction/03-reconstrucao-cega.md`

| Linha | Antes | Depois | Tipo |
|---|---|---|---|
| §1.3 (~70) | "aún não existia" | "ainda não existia" | digitação |
| §1.8 (~137) | "validacao do resultado" | "validação do resultado" | digitação/acento |
| §1.9 (~158) | "Sem suporte ver: (o 'aprendizado' explícito é af-037/038a)" | "Sem suporte direto para além da validação" | fragmento corrompido |
| §5 (~248) | "DEB-009" | "DEBT-009" | sigla da dívida |
| §5 (~248) | "a reconstrução não resiste à conclusão" | "a reconstrução não força a conclusão" | corrupção de frase |

### 1.4 Troca de referências AF-011 × AF-012 (GO-3 §1.3)

Referência canônica: `AF-011` = prazo (~15 anos); `AF-012` = custo (~US$ 3 bi).

| Arquivo | Local | Antes | Depois |
|---|---|---|---|
| `03-reconstrucao-cega.md` | §2, linha ~166 | "Goal (... AF-012 — prazo 15 anos; custo AF-011)" | "Goal (... AF-011 — prazo 15 anos; custo AF-012)" |
| `signals/05-signals.yaml` | SIG-005 (linha ~72) | "prazo 15 anos (AF-012), custo (AF-011)" | "prazo 15 anos (AF-011), custo (AF-012)" |

### 1.5 `comparison/04-alignment-analysis.md`

| Item | Antes | Depois | Tipo |
|---|---|---|---|
| NI-002 | "ausência de Risk calculus" | "ausência de Risk calculado" | rótulo técnico |

---

## 2. Correções adicionais identificadas durante o reparo (mesma classe GO-3 §1.3)

Durante a verificação do §1.4, foram localizados **mais 2 pontos** da mesma troca
AF-011/AF-012, corrigidos sob o mesmo critério (correção de citação, sem alterar
dado):

| Arquivo | Local | Antes | Depois |
|---|---|---|---|
| `03-reconstrucao-cega.md` | §1.4 Assumption (linha ~79) | "AF-012 \| Tempo (15 anos) era adequado" | "AF-011 \| Tempo (prazo de ~15 anos) era adequado" |
| `03-reconstrucao-cega.md` | §3 comparativa (linha ~211) | "PRESENTE (AF-012 prazo)" | "PRESENTE (AF-011 prazo)" |

> A redação do dado ("prazo 15 anos", "custo US$ 3 bi") estava correta em todos;
> somente o número de AF citado foi invertido. **Impacto no resultado: nenhum**
> (mesma observação de GO-3 §1.3).

---

## 3. Correções executadas em sessão anterior (registradas em GO-3 §1.2)

Foram também aplicadas em execução anterior do pipeline as correções tipográficas
de `narrative` (majorçamente, dedicassse, IHG→IHGSC) e `sources` (ORN-000,
terminolologia, NHGIR) — registradas aqui para completude do diff GO-4A. Ver §1.1
e §1.2 acima.

---

## 4. Verificação pós-reparo (nenhum conteúdo alterado)

| Checagem | Antes (GO-3) | Depois (GO-4A) | Status |
|---|---|---|---|
| Contagem de itens Etapa 4 | 26 (15+7+2+2) | 26 (15+7+2+2) | ✅ inalterado |
| EAR | 0.7708 → 0.77 | 0.7708 → 0.77 | ✅ inalterado |
| Atomic Facts | 50 (AF-001…AF-050) | 50 | ✅ inalterado |
| Sinais promovidos | 0 | 0 | ✅ inalterado |
| Categoria do NI-002 | NEW_INSIGHT | NEW_INSIGHT | ✅ inalterado |

> Confirma-se: **nenhuma mudança fática, classificatória ou conclusiva.** As
> correções são exclusivamente de grafia, sigla e referência de AF.

---

## 5. Garantias (GO-4A)

- ❌ Nenhum artefato do **protocolo congelado** (README, P-0010, SHADOW-EXPERIMENTS,
  SIGNAL-SCHEMA, SX-REAUDIT) foi alterado.
- ❌ Nenhuma **interpretação** foi introduzida.
- ❌ Nenhum **Signal → Pattern**.
- ❌ Nenhuma **comparação quantitativa de EAR**.
- ❌ Nenhuma **análise transversal**.
- ❌ **Nenhum commit** (repositório permanece sem mudanças rastreadas no SX-003).

---

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-08-09 | Reparo controlado GO-4A: 3 digitações narrativa, 3 fontes, 4 corrupções reconstrução, 1 rótulo alignment, 2 trocas AF-011/AF-012 (GO-3) + 2 adicionais da mesma classe. Verificação §4: contagens e EAR inalterados. |
