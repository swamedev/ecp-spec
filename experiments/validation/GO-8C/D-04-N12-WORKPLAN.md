# GO-8C — D-04 WORKPLAN: Produção dos 5 Novos BIPs (008–012)

**Data:** 2026-08-14
**Ciclo:** GO-8C
**Autoridade:** DECISION D-04 (N=12) — itens 4 e 5 (produção dos 5 novos materiais autorizada após aprovação deste plano; NT-05 estendido).
**Status:** **PROPOSTA DE PLANO — aguardando aprovação da governança.**
**Regra global (herdada do P5/GO-8B):** fontes oficiais rastreadas; narrativa + atomic facts com **zero termos ECP**; validação lexical; nenhuma importação de narrativa/AF/reconstrução de SX-001/002/003; origem causal primária independente (SC-5).

---

## 1. Escopo

Produzir, sob `experiments/validation/GO-8C/study-input/`, os materiais dos 5 novos BIPs:

| BIP | Caso | Domínio | Natureza | Universo SX-REAUDIT |
|---|---|---|---|---|
| BIP-008-apollo13 | Apollo 13 (1970) | Aeroespacial | ENG | SELECTABLE |
| BIP-009-chernobyl | Chernobyl Unidade 4 (1986) | Industrial nuclear | ENG | SELECTABLE |
| BIP-010-tacomanarrows | Tacoma Narrows (1940) | Civil | ENG | ELIGIBLE |
| BIP-011-dominos | Domino's Turnaround (2009–10) | Pequenos Negócios | ORG | ELIGIBLE |
| BIP-012-eyjafjallajokull | Eyjafjallajökull (2010) | Logística/aviação | ORG | ELIGIBLE |

> Resultado esperado: 7 domínios distintos no estudo (≥4 exigido), 5 tipos de engenharia, ambas naturezas (P-0008).

## 2. Estrutura de diretórios a confirmar (idêntica ao P5/GO-8B)

```
experiments/validation/GO-8C/study-input/BIP-NNN-<caso>/
├── sources/
│   ├── 00-index.md                 # fronteira pré/pós gate (GO-8C)
│   ├── 01-origem-dos-documentos.md # proveniência EI (SC-5)
│   └── raw/                        # downloads + checksums SHA-256
├── narrative/
│   └── 01-narrativa-original.md    # condição C; zero ECP
├── atomic-facts/
│   └── 02-atomic-facts.md          # condições A/B; fatos mínimos, zero ECP
└── README.md
```

> **Confirmado:** corresponde exatamente ao padrão verificado nos 7 BIPs copiados (ex. BIP-002-hyatt: 7 arquivos, `sources/raw/` com PDFs/HTML + checksums no `00-index.md`). Nomes de pasta usam o slug de 2 letras do BIP (sem acento): `-apollo13`, `-chernobyl`, `-tacomanarrows`, `-dominos`, `-eyjafjallajokull`.

## 3. Fontes-alvo (oficiais/primárias) por BIP

| BIP | Fontes-alvo (origens causais primárias independentes) | Esforço de coleta |
|---|---|---|
| BIP-008 | NASA Apollo 13 Mission Report (SP-4009) / AIAA; relatório do Columbia Accident não se aplica — foco no SP-4009 + audio transcrição da missão + relatório presidencial (não aplicável; usar NASA Technical Reports Server) | baixa (acervo público NASA) |
| BIP-009 | INSAG-1 (IAEA, 1986) + INSAG-7 (1992) + relatório do Comitê Governamental Ussr (1991) | média-alta (acervo IAEA, 2 PDFs extensos) |
| BIP-010 | F. B. Farquharson's "Aerodynamic Stability of Suspension Bridges" (1949-52) + relatórios da University of Washington (1939-41) / contribuição de Kármán | média (relatórios técnicos históricos) |
| BIP-011 | Wall Street Journal / Business Insider / Forbes (caso Patrick Doyle); fontes corporativas (relatórios anuais Domino's 2008-2010); Harvard Business School case 514-011 | média-alta (múltiplas origens jornalísticas/corporativas) |
| BIP-012 | ICAO (Aircraft Accident Report?) — melhor: IATA Volcanic Ash Crisis communications + ICAO Circular 320-AN/184 (Volcanic Ash Contingency Plan); Eurocontrol; UK CAA | média-alta (múltiplos órgãos de aviação) |

> **Riscos de fonte (de D-04-N12-PROPOSAL R-1/R-2):** BIP-011 (Pequenos Negócios) pode ter menor disponibilidade de documentos oficiais primários → mitigação: usar relatórios anuais SEC (10-K da Domino's Pizza, Inc. 2009-2010) como origem primária regulatória; BIP-010/012 exigem re-verificação da elegibilidade no universo congelado antes da coleta.

## 4. Fases e cronograma proposto (7 dias úteis, ~5-8 h/dia)

| Fase | Atividades | Prazo | Entregável | Validação |
|---|---|---|---|---|
| **P0 — Aprovação** | Aprovação da governança deste plano | D0 | Plano aprovado | DECISION D-04.2 |
| **P1 — Coleta** | Buscar/baixar fontes oficiais por BIP (ordem: 008→009→010→011→012); salvar em `sources/raw/` com checksums | D1–D2 | `sources/raw/*` + `00-index.md` + `01-origem-dos-documentos.md` | 2+ origens causais primárias por BIP; checksums registrados |
| **P2 — Narrativa** | Redigir `01-narrativa-original.md` (condição C) por BIP — fatos históricos em ordem, zero ECP | D3–D4 | `narrative/01-narrativa-original.md` (5) | verificação léxica (zero ECP) |
| **P3 — Atomic Facts** | Extrair `02-atomic-facts.md` (condições A/B) por BIP — fatos mínimos atômicos, zero ECP, ≥15 AF | D5–D6 | `atomic-facts/02-atomic-facts.md` (5) | ≥15 AF/BIP; léxica + rastreabilidade 100% |
| **P4 — Validação** | Validação léxica + rastreabilidade + não-importação (diff SX) + README por BIP | D7 | `README.md` (5) + `VAL-008-012.md` | todas PASS |
| **P5 — Painel NT-05** | Estender painel D-03 (2 IAs independentes, 3 abas) aos 5 novos materiais — **etapa separada pós-aprovação** | D8+ | resultado do painel | unanimidade PASS (mesmos critérios/modelos) |

> **Paralelização:** P1 por BIP pode ser sequencial (1 BIP/dia de coleta) para manter rastreabilidade; narrativa/AF em 2 BIPs por dia. Total de produção: **5–8 dias úteis** (alinhado à proposta).

## 5. Critérios de qualidade (idênticos ao P5 §6)

- Vocabulário neutro (lista 52 termos ECP) — zero ocorrências.
- Atomic facts: fatos mínimos, sem interpretação, sem taxonomia.
- Narrativa: fatos históricos em ordem, sem categorias ECP.
- Rastreabilidade: cada AF/bloco narrativo referencia `source_refs` de `01-origem-dos-documentos.md`.
- Não-importação: diff contra SX-001/002/003 (nenhuma narrativa/AF/reconstrução reutilizada).
- Regra D-04 item 2: nenhum dado do GO-8B reutilizado como observação — vale também para materiais (novos são 100% independentes).

## 6. Gate de autorização pós-plano

1. **Governança aprova este plano** (DECISION D-04.2).
2. Executar P1–P4 (coleta→validação) — produção autorizada pela DECISION D-04 item 4.
3. Reportar validação; **governança aprova o painel NT-05** (P5) para os 5 novos.
4. Escrever **pré-registro N=12** (desenho, seeds, Go/No-Go, plano de análise) e aprovar.
5. Lock GO-8C + autorização explícita de execução (108 reconstruções) — **etapas separadas**.

> **NÃO é escopo deste plano:** execução experimental, análise estatística, geração de seeds, Lock, pré-registro, painel NT-05 (todos exigem autorização própria/etapa separada).

## 7. Riscos e mitigação (do D-04-N12-PROPOSAL, aplicados aos 5 novos)

| Risco | Impacto | Mitigação |
|---|---|---|
| R-1 falta de fontes primárias (010/012) | atraso coleta | re-verificar elegibilidade; fontes históricas da Univ. Washington/ICAO; registrar limitação |
| R-2 BIP-011 (Pequenos Negócios) sem doc. oficial primária | violação P5 | usar 10-K SEC Domino's 2009-2010 como origem primária regulatória |
| R-3 termos ECP acidentais | falha léxica | checklist 52 termos; revisão pré-validação |
| R-5 dependência pares (Deepwater/Chernobyl) | — | apenas registrar no pré-registro (decisão 06), não bloqueia produção |

---

**Fim do plano. Estrutura confirmada; aguardando aprovação da governança para executar P1–P4.
