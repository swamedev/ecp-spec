# GO-8D-NC — BIP ACQUISITION PLAN v1 (BIPs 013–030)

**Versão:** v1.0
**Data:** 2026-08-15
**Status:** **Elaboração autorizada pela governança** (aguarda análise e autorização de coleta)
**Estado do programa:** GO-8D-NC LOCKED / FROZEN (14 artefatos) · Lock íntegro
**Gate atual:** BIP ACQUISITION PLAN → (autorização) → COLETA
**Base:** `08-PRE-REGISTRATION-NEW-CYCLE.md` (v1.0 FINAL, §7.2) · `D-MV-03` (desenho) · `D-03` (pipeline)

---

## 1. Objetivo

Adquirir, validar e acondicionar os **18 novos BIPs (013–030)** segundo o formato canônico de
`study-input`, de modo que os 30 BIPs do ciclo (12 existentes + 18 novos) passem no gate
**30/30 BIPs válidos** antes de qualquer execução (pré-registro §6.4).

**Requisito inegociável:** **30/30 BIPs válidos** — parseabilidade canônica (gate D-04) +
rastreabilidade fato→fonte + validação ECP/lexicon + aceitação/rejeição independente. Sem
nenhum BIP válido a menos, **nenhuma execução do piloto**.

---

## 2. Identidade inequívoca de cada BIP

Cada BIP (013–030) é identificado por:
- `bip_id` canônico: `BIP-NNN-nome` (ex.: `BIP-013-bhopal`), conforme §7.2 do pré-registro.
- **Caso** (nome inequívoco + data/ocorrência).
- **Domínio** (classificação do pré-registro).
- **Fontes primárias/oficiais propostas** (relatórios de comissões/agências/reguladores).
- **Narrativa única em pt-BR** derivada exclusivamente das fontes adquiridas (sem fontes externas
  não listadas).

> A identidade do BIP é **congelada no momento da validação** (hash do diretório `study-input`).
> Alteração de identidade após a validação → rejeição do BIP.

---

## 3. Os 18 BIPs e fontes primárias/oficiais propostas

> Fonte candidata (não coletada). URLs/PDFs a confirmar na coleta. Se uma fonte proposta não
> estiver acessível, a comissão de aquisição pode substituí-la **por equivalente oficial**,
> documentando o motivo (ver §8.2).

| # | BIP (id) | Caso | Domínio | Fontes primárias/oficiais propostas |
|---|---|---|---|---|
| 13 | BIP-013-bhopal | Desastre de Bhopal (1984) | Indústria química | ICMR (Relatório Técnico BGDRC) · Relatório Varadarajan (NTIS PB89115380) · Grupo de Ministros (Gov. Índia) |
| 14 | BIP-014-tmi | Three Mile Island (1979) | Nuclear | NRC · Comissão Kemeny · GAO |
| 15 | BIP-015-challenger | Challenger STS-51-L (1986) | Aeroespacial | Comissão Rogers (NASA History) · GAO |
| 16 | BIP-016-columbia | Columbia STS-107 (2003) | Aeroespacial | CAIB Report (NASA) |
| 17 | BIP-017-katrina | Furacão Katrina (2005) | Gestão de emergências | USACE Performance Evaluation · White House Federal Response · FEMA |
| 18 | BIP-018-flint | Crise da água de Flint (2014–16) | Água/saúde pública | Michigan Civil Rights Commission · EPA · DOJ |
| 19 | BIP-019-fukushima | Fukushima Daiichi (2011) | Nuclear | IAEA · NAIIC · TEPCO |
| 20 | BIP-020-grenfell | Incêndio Grenfell Tower (2017) | Segurança de edifícios | Grenfell Tower Inquiry (Reino Unido) |
| 21 | BIP-021-vajont | Desastre de Vajont (1963) | Engenharia civil/barragens | Inquérito parlamentar italiano · ISPRA |
| 22 | BIP-022-max8 | Boeing 737 MAX (2018–19) | Aviação | NTSB · FAA · House T&I Committee |
| 23 | BIP-023-mariana | Rompimento de Mariana (2015) | Mineração/ambiente | Fundação Renova · Estado de MG · agências |
| 24 | BIP-024-dieselgate | VW Dieselgate (2015) | Automotivo/ambiente | EPA (NOV) · DOJ (acordo) |
| 25 | BIP-025-wellsfargo | Contas falsas Wells Fargo (2016) | Setor financeiro | CFPB · OCC · relatório do Senado |
| 26 | BIP-026-theranos | Theranos (2015–18) | Biotecnologia/saúde | SEC · CMS · DOJ |
| 27 | BIP-027-opioids | Crise dos opioides/Purdue (2007–19) | Farmacêutica | DOJ · CDC · tribunais |
| 28 | BIP-028-enron | Escândalo Enron (2001) | Corporativo/finanças | SEC · Congresso dos EUA |
| 29 | BIP-029-takata | Airbags Takata (2008–17) | Segurança automotiva | NHTSA · DOJ |
| 30 | BIP-030-concordia | Costa Concordia (2012) | Transporte marítimo | Inquérito italiano · autoridades portuárias |

**Domínios novos cobertos (não representados nos 12 atuais):** química, emergências,
água/saneamento, mineração, financeiro/corporativo, biotecnologia, farmacêutica, segurança
automotiva, incêndio em edifícios, barragens. Reforço: nuclear, aeroespacial, aviação, marítimo.

---

## 4. Critérios de inclusão/exclusão

### 4.1 Inclusão (todos obrigatórios)
- Caso real, histórico, **não utilizado em GO-8B/GO-8C/GO-8D** (proibição de reuso de caso — ver §7).
- Pelo menos **uma fonte primária oficial** (relatório de comissão/agência/regulador) acessível e
  íntegra (download verificável; PDF/HTML oficial).
- Domínio com cobertura mínima de **narrativa** e **atomic facts** extraíveis.
- Possibilidade de produzir narrativa única em pt-BR **sem termos ECP** (condições cegas).
- Identidade inequívoca (caso, datas, entidades) verificável em ≥ 2 fontes independentes.

### 4.2 Exclusão (qualquer uma → rejeição)
- Caso com fontes apenas jornalísticas/midiáticas (sem relatório oficial de base).
- Fonte oficial indisponível/ilegível no download (quebra de integridade).
- Sobreposição de caso com BIPs 001–012 ou com qualquer material dos ciclos anteriores
  (contaminação — ver §7).
- Impossibilidade de rastrear **cada fato → fonte** (sem referência).
- Narrativa que dependa de interpretação taxonômica ou de conhecimento externo às fontes.

---

## 5. Estrutura de narrativa e atomic facts (formato canônico)

Cada BIP adota a estrutura do `study-input` (padrão GO-8C/BIP-001):

```
BIP-NNN-nome/
├── README.md                        (identidade, fontes, estado de validação)
├── narrative/
│   └── 01-narrativa-original.md     (narrativa única pt-BR, condições C)
├── atomic-facts/
│   └── 02-atomic-facts.md           (fatos atômicos mínimos, condições A/B)
└── sources/
    ├── 00-index.md                  (índice de fontes)
    ├── 01-origem-dos-documentos.md  (proveniência e procedência)
    └── raw/                         (cópias íntegras das fontes, hasheadas)
```

### 5.1 `02-atomic-facts.md`
- Cabeçalho com condições (A/B), uso (cegas; zero termos ECP; sem interpretação/taxonomia),
  fontes efetivas e regra de rastreabilidade.
- **Fatos mínimos atômicos**: um fato = uma afirmação verificável (sujeito-predicado-objeto ou
  evento), em pt-BR, sem adjetivação avaliativa, sem inferência.
- **Cada fato termina com `[refs...]`** (identificadores das fontes efetivas, ex.: `[ncom-01-gulf]`).
- Número de fatos coerente com a complexidade do caso (sem limite rígido; alvo ~40–80 por BIP).

### 5.2 `01-narrativa-original.md`
- Narrativa em pt-BR, única, sequencial (linha do tempo), cobrindo: contexto, evento(s)
  crítico(s), causas/condições, resposta/contramedidas e desfecho.
- Baseada **exclusivamente** nas fontes adquiridas; sem termos ECP; sem interpretação.

---

## 6. Requisitos de rastreabilidade (cada fato → fonte)

1. **Fato → fonte:** todo fato em `02-atomic-facts.md` referencia ≥ 1 identificador de fonte
   efetiva (do `00-index.md`/`01-origem-dos-documentos.md`).
2. **Fonte → arquivo:** todo identificador de fonte corresponde a um arquivo em `sources/raw/`
   com hash SHA-256 registrado no `README.md`/`00-index.md`.
3. **Narrativa → fontes:** cada seção da narrativa indica as fontes de base (mesmos
   identificadores).
4. **Sem órfãos:** nenhum fato sem referência; nenhuma referência a fonte inexistente;
   nenhum arquivo `raw/` não referenciado (exceto erros corrigidos antes da validação).
5. Verificação automatizada (script de rastreabilidade) + verificação humana independente (§9).

---

## 7. Regras contra contaminação por ciclos anteriores

1. **Proibição absoluta:** nenhum BIP novo pode coincidir (caso, narrativa, atomic facts, fontes)
   com qualquer material de GO-8B/GO-8C/GO-8D anterior.
2. **Ausência de termos ECP** nas condições cegas (A/B): verificação via léxico (o pipeline
   classifica por namespace; a validação ECP/lexicon assegura zero contaminação).
3. **Nenhuma leitura de artefatos congelados** em runtime (pipeline autocontido — Lock §íntegro).
4. **Fontes novas:** todo arquivo `raw/` é **novo download** (ou cópia de documento oficial
   público), nunca reaproveitado de `study-input` anterior.
5. **Hash de integridade:** cada fonte `raw/` tem SHA-256 registrado; divergência → rejeição.
6. A equipe de aquisição **não consulta** os artefatos dos ciclos anteriores durante a produção
   dos novos BIPs (isolamento documentado).

---

## 8. Procedimento de validação independente do pacote

### 8.1 Validação ECP/lexicon
- **Condições A/B:** zero ocorrências de termos do namespace ECP (problema, evidência, contexto,
  pressão, camada/relativo, oportunidade, preparação, incerteza, reação — conforme C2/C3
  congeladas) na narrativa e atomic facts.
- **Condição C:** narrativa completa (pode conter termos ECP — é o material não-cego; mesmo
  assim, a atomic facts permanece cega).
- Verificação por (i) script léxico contra o vocabulário congelado e (ii) leitura humana
  independente.

### 8.2 Critérios de aceitação/rejeição independente
Aceitação de um BIP (todos):
- Estrutura canônica completa (§5) e parseável (gate D-04).
- Rastreabilidade 100% (§6).
- Zero contaminação ECP nas condições A/B (§7/§8.1).
- Fontes íntegras com hash verificado.
- **Aprovação por 2 revisores independentes** (pares), com registro escrito.

Rejeição de um BIP (qualquer um):
- Falha em qualquer critério acima.
- Discrepância irreconciliável entre revisores (escalada à governança).
- Substituição de fonte sem equivalência oficial documentada → rejeição.

### 8.3 Gate final
- **30/30 BIPs válidos** (12 existentes revalidados + 18 novos validados).
- Relatório de validação com hashes de todos os diretórios `study-input`.
- **Somente então:** autorização da governança para seeds + execução do piloto.

---

## 9. Relatório e entregáveis da aquisição

- `GO-8D-NC/study-input/BIP-013..030/` (formato canônico, §5).
- `GO-8D-NC/ACQUISITION-REPORT.md`: por BIP — fontes efetivas, hashes, rastreabilidade,
  validação ECP/lexicon, revisores e parecer (aceito/rejeitado).
- Script de validação de rastreabilidade (automatizado) + log de execução.

---

## 10. Restrições desta etapa

- **Nenhuma coleta definitiva de fontes**, produção de narrativas/atomic facts, geração de seeds,
  execução do piloto, análise estatística ou alteração de artefatos congelados.
- **Nenhum commit.**
- Qualquer divergência do Lock → STOP e reporte.

---

**Fim do BIP Acquisition Plan v1. 2026-08-15. Elaborado por autorização da governança;
aguarda análise e autorização de coleta.
