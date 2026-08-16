# GO-8C — STUDY-INPUT MANIFEST (Materiais do Estudo N=12)

**Data da cópia:** 2026-08-14
**Ciclo:** GO-8C
**Decisão:** DECISION D-04 (N=12) — item 2 (re-execução dos 7 BIPs)
**Proveniência:** cópias operacionais derivadas de `experiments/validation/GO-8B/pilot-input/` (FROZEN), copiadas no GO-8C. **Originais GO-8B intocados.**

---

## 1. BIPs copiados (001–007 — reuso de materiais)

| BIP | Caso | Arquivos | Verificação SHA-256 (vs. GO-8B) |
|---|---|---|---|
| BIP-001-deepwater | Deepwater Horizon (2010) | 8 | MATCH (idêntico) |
| BIP-002-hyatt | Hyatt Regency (1981) | 7 | MATCH (idêntico) |
| BIP-003-ows | Operation Warp Speed (2020–21) | 9 | MATCH (idêntico) |
| BIP-004-genoma | Genoma Humano (1990–2003) | 13 | MATCH (idêntico) |
| BIP-005-evergiven | Ever Given / Suez (2021) | 7 | MATCH (idêntico) |
| BIP-006-i35w | I-35W Bridge (2007) | 7 | MATCH (idêntico) |
| BIP-007-ebola | Resposta Ebola (2014–16) | 20 | MATCH (idêntico) |

> **Regra:** `derived_from: GO-8B pilot-input (frozen), copied in GO-8C (D-04)`. Nenhum arquivo do GO-8B foi alterado; nenhum dado do GO-8B será reutilizado como observação (os 7 BIPs serão **reexecutados** no pipeline do GO-8C).

## 2. BIPs a produzir (008–012 — novos)

| BIP | Caso | Domínio | Status |
|---|---|---|---|
| BIP-008-apollo13 | Apollo 13 (1970) | Aeroespacial | **A PRODUZIR** (após aprovação do plano de trabalho) |
| BIP-009-chernobyl | Chernobyl Unidade 4 (1986) | Industrial nuclear | **A PRODUZIR** |
| BIP-010-tacomanarrows | Tacoma Narrows (1940) | Civil | **A PRODUZIR** |
| BIP-011-dominos | Domino's Turnaround (2009–10) | Pequenos Negócios | **A PRODUZIR** |
| BIP-012-eyjafjallajokull | Eyjafjallajökull (2010) | Logística/aviação | **A PRODUZIR** |

> Padrão P5 (GO-8B): `sources/00-index.md` + `sources/01-origem-dos-documentos.md` + `sources/raw/` + `narrative/01-narrativa-original.md` + `atomic-facts/02-atomic-facts.md` + `README.md`. Zero termos ECP; rastreabilidade 100%; ≥15 atomic facts; sem importação de SX-001/002/003.

## 3. Estrutura

```
study-input/
├── BIP-001-deepwater/  …  BIP-007-ebola/   (copiados, 2026-08-14)
└── BIP-008-apollo13/  …  BIP-012-eyjafjallajokull/  (a produzir)
```

## 4. NOTA

- BIP-003-warpspeed (diretório residual vazio do GO-8B) **não foi copiado** — fora do escopo (BIP-003 = Operation Warp Speed, pasta `BIP-003-ows`).
- A produção dos 5 novos BIPs será executada **somente após a governança aprovar o plano de trabalho** (cronograma e estrutura).
- GO-8B permanece CLOSED / LOCKED / FROZEN.

---

**Fim do manifesto. 7 BIPs copiados e verificados; 5 a produzir após autorização.
