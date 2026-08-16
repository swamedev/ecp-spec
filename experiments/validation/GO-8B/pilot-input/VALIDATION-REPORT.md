# GO-8B — P5 VALIDATION-REPORT: Produção de Materiais (piloto)

**Data:** 2026-08-12
**Autoridade:** DECISION P5-INPUT-MATERIALS; escopo de produção DECIDED (piloto BIP-004 + avanço BIP-001).
**Critérios (manifest §7):** verificação léxica (zero termos ECP), verificação de rastreabilidade (100% refs → sources), verificação de não-importação (diff contra SX-001/002/003).

---

## 1. Resumo

| BIP | Fontes brutas | Narrativa (C) | Atomic Facts (A/B) | Léxico zero-ECP | Rastreabilidade | Não-importação | Resultado |
|---|---|---|---|---|---|---|---|
| BIP-004 (Genoma) | 8 HTML (6 efetivas) | ✓ | ✓ (42 fatos) | PASS | PASS | PASS | **VALIDADO** |
| BIP-001 (Deepwater) | 3 PDF (3 origens primárias) | ✓ | ✓ (57 fatos) | PASS | PASS | PASS | **VALIDADO** |
| BIP-005 (Ever Given) | 2 fontes (PMA PDF; UK P&I HTML) | ✓ | ✓ (58 fatos) | PASS | PASS | PASS | **VALIDADO** |
| BIP-006 (I-35W) | 2 PDF (NTSB; GPM) | ✓ | ✓ (70 fatos) | PASS | PASS | PASS | **VALIDADO** |
| BIP-002 (Hyatt) | 2 fontes (NBS BSS 143 PDF; acórdão HTML) | ✓ | ✓ (124 fatos) | PASS | PASS | PASS | **VALIDADO** |
| BIP-003 (OWS) | 3 PDF (GAO-21-319; ficha HHS/DoD; CRS IN11560) | ✓ | ✓ (124 fatos) | PASS | PASS | PASS | **VALIDADO** |
| BIP-007 (Ebola) | 8 fontes (5 PDF extraídos; 3 HTML) | ✓ (1.340 palavras) | ✓ (90 fatos) | PASS | PASS | PASS | **VALIDADO** |

**Status de materiais de entrada: 7/7 BIPs com materiais produzidos (BIP-001..BIP-007).**

## 2. Léxico zero-ECP (vocabulário ECP-000..010, 52 termos)

- BIP-004 narrative/atomic-facts: **PASS** (0 ocorrências de termos ECP).
- BIP-001 narrative/atomic-facts: **PASS** (0 ocorrências; corrigidos durante produção: `capacidade`, `objetivo`, `estado`/`Estado` em cabeçalhos e corpo).
- BIP-005 narrative/atomic-facts: **PASS** (0 ocorrências).
- BIP-006 narrative/atomic-facts: **PASS** (0 ocorrências; corrigidos durante produção: `capacidade`, `state`).
- BIP-002 narrative/atomic-facts: **PASS** (0 ocorrências; corrigidos durante produção: `capacidade` → `resistência última`, `estado` → `território do Missouri`).
- BIP-003 narrative/atomic-facts: **PASS** (0 ocorrências; corrigidos durante produção: `capacidade` → `escala de manufatura`, `risco` → `incerteza`).
- BIP-007 narrative/atomic-facts: **PASS** (0 ocorrências; `validate_bip007.py`, 52 termos).
- Método: normalização acentuada + casamento por palavra (`\bterm\b`).

> Nota: substrings como "Estados"/"identidades" não contam como termo ECP (casamento por palavra, não por prefixo). Correções foram aplicadas mesmo assim para eliminar qualquer ambiguidade.

## 3. Rastreabilidade (100% refs → sources)

- BIP-004: todas as refs usadas (`nhgri-*`, `doe-*`, `sci-*`) presentes em `00-index.md`. PASS.
- BIP-001: todas as refs usadas (`ncom-01-gulf`, `csb-01-macondo-v1`, `jit-01-report`) presentes em `00-index.md`. PASS.
- BIP-005: todas as refs usadas (`pma-01-ever-given`, `ukpandi-01-ever-given`) presentes em `00-index.md`. PASS.
- BIP-006: todas as refs usadas (`ntsb-01-har0803`, `mngov-01-gpm`) presentes em `00-index.md`. PASS.
- BIP-002: todas as refs usadas (`nbs-01-bss143`, `vlex-02-duncan`) presentes em `00-index.md`. PASS.
- BIP-003: todas as refs usadas (`gao-01-21-319`, `dod-02-fact-sheet`, `crs-01-in11560`) presentes em `00-index.md`. PASS.
- BIP-007: todas as refs usadas (`who-01-sitrep-jun2016`, `who-02-overview-2014-2016`, `nejm-01-ebola-9months`, `msf-01-pushed-limit`, `msf-02-facts-figures`, `cdc-01-mmwr-sep2014`, `unmeer-01-mission`, `unmeer-02-sitrep`) presentes em `00-index.md`. PASS.
- Cada fato/bloco termina com `[refs...]`.

## 4. Não-importação (contra SX-001/002/003)

- Nenhuma narrativa/atomic-facts/reconstrução dos SX copiada para `pilot-input/`.
- BIP-004: fontes são páginas públicas primárias (genome.gov, doe, Nature/Science via PubMed).
- BIP-001: fontes são PDFs oficiais primários (GovInfo, CSB, BSEE).
- BIP-005: fontes são PDF oficial (SCA/PMA) e comunicado público do UK P&I Club (via Wayback).
- BIP-006: fontes são PDF oficiais (NTSB HAR-08/03; relatório GPM via lrl.mn.gov).
- BIP-002: fontes são PDF oficial do NBS (nvlpubs.nist.gov) e acórdão judicial 744 S.W.2d 524 (espelho público vLex Case Law, após tentativas HTTP 403/202 nos canais originais).
- BIP-003: fontes são PDF oficial do GAO (GAO-21-319), ficha oficial conjunta HHS/DoD e relatório breve do CRS (congress.gov). Nota de canal: gao.gov e hhs.gov devolveram HTTP 403 ao acesso automatizado e foram capturados via Wayback Machine / espelho público da secretaria (registrado em `01-origem-dos-documentos.md`).
- BIP-007: fontes são PDF(s)/HTML oficiais primários (who.int, paho.org mirror, msf.org.uk/msf.ie mirror, cdc.gov via Wayback, un.org). Extração de texto via PyMuPDF (documentada em `raw/00-extraction-errors.md`).
- PASS (por construção: revisão de conteúdo + ausência de arquivos de SX no diretório).

## 5. Qualidade das fontes

- BIP-004: `nhgri-03-timeline` (resposta HTTP 404) e `celera-01-2000` (somente aviso legal) registrados como capturas brutas sem uso de conteúdo — rastreamento íntegro, sem alegação de conteúdo.
- BIP-001: coleta inicial com 3 origens causais primárias independentes (SC-5): Comissão Nacional (govinfo), CSB (csb.gov), JIT BOEMRE/USCG (bsee.gov). Demais origens do plano (BP, Congresso, imprensa) permanecem pendentes e não bloqueiam o uso piloto.
- BIP-002: coleta inicial com 2 origens causais independentes (SC-5): NBS BSS 143 (investigação técnica federal) e Missouri Court of Appeals No. 52655 (revisão judicial). Nota de canal: Justia, Leagle e CourtListener não disponibilizaram acesso não autenticado; captura via vLex registrada em `01-origem-dos-documentos.md`.
- BIP-003: coleta inicial com 3 origens causais independentes (SC-5): GAO (órgão de controle do Congresso), HHS/DoD (Poder Executivo) e CRS (serviço de pesquisa do Congresso). `hhs-01-factory-to-frontlines.pdf` registrado na coleta, porém sem uso de conteúdo efetivo nos materiais.

## 6. Conclusão

- Os materiais dos **BIP-004, BIP-001, BIP-005, BIP-006, BIP-002, BIP-003 e BIP-007** atendem aos critérios de qualidade do manifest §6/§7.
- **Status de materiais de entrada: 7/7 (BIP-001..BIP-007) prontos para uso nas reconstruções A/B/C** (ainda não executadas — execução exige PRE-FLIGHT 2 e gates adicionais).
- Pendência permanece: **NT-05** do P2 (3 validadores humanos independentes) — não automatizável, PENDING.
- Sem demais pendências do piloto P5.

---
**Fim do relatório. Nenhum material interpretativo importado. Nenhuma execução experimental.**