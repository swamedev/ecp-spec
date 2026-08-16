# GO-8B — P5 PRODUCTION MANIFEST: Input Materials (Independent Production)

**Data:** 2026-08-12
**Autoridade:** DECISION P5-INPUT-MATERIALS — "Reconstruir independentemente os materiais de entrada dos 7 BIPs para o GO-8B; não reutilizar diretamente SX-003/SX-002 ou outros artefatos interpretativos de pipelines anteriores."
**Regra global:** nenhuma importação de narrativa/atomic-facts/reconstrução de SX-001/002/003. Fontes brutas (staging) podem servir de matéria-prima se rastreadas; artefatos interpretativos NÃO.

---

## 1. Escopo dos materiais por BIP

Cada BIP precisa de, por condição de reconstrução:

| Condição | Entrada necessária |
|---|---|
| **A — Cega pura** | Somente **Atomic Facts** (fatos mínimos, zero ECP, zero taxonomia) |
| **B — Cega + C3** | Atomic Facts + **C3_TAXONOMY** (namespace SYN) |
| **C — Não-cega** | **Narrativa completa** (fatos históricos, zero ECP) |

**Fonte primária por BIP:** fontes públicas rastreadas (origens causais independentes, SC-5). **Proibido:** importar narrativa/atomic-facts de SX-001/002/003.

## 2. Status por BIP

| BIP | Caso | Fontes brutas disponíveis | Narrativa GO-8B | Atomic Facts GO-8B | Status |
|---|---|---|---|---|---|
| BIP-001 | Deepwater Horizon (2010) | 3 PDFs (Comissão, CSB, JIT) ✓ | ✓ | ✓ | MATERIAIS PRODUZIDOS |
| BIP-002 | Hyatt Regency (1981) | 2 fontes ✓ (NBS BSS 143; acórdão 744 S.W.2d 524) | ✓ | ✓ | MATERIAIS PRODUZIDOS |
| BIP-003 | Operation Warp Speed (2020–21) | 3 PDFs ✓ (GAO-21-319; ficha HHS/DoD; CRS IN11560) | ✓ | ✓ (124 fatos) | MATERIAIS PRODUZIDOS |
| BIP-004 | Genoma Humano (1990–2003) | 8 HTML ✓ | ✓ | ✓ | MATERIAIS PRODUZIDOS |
| BIP-005 | Ever Given / Suez (2021) | 2 fontes ✓ (PMA; UK P&I) | ✓ | ✓ | MATERIAIS PRODUZIDOS |
| BIP-006 | I-35W Bridge (2007) | 2 fontes ✓ (NTSB HAR-08/03; GPM/lrl.mn.gov) | ✓ | ✓ | MATERIAIS PRODUZIDOS |
| BIP-007 | Resposta Ebola (2014–16) | 8 fontes ✓ (OMS/WHO ×2, NEJM, MSF ×2, CDC, UNMEER ×2) | ✓ (1.340 palavras) | ✓ (90 fatos) | MATERIAIS PRODUZIDOS |

## 3. Ordem de produção recomendada

1. **BIP-004** — ~~fontes raw já existem (8 HTML em candidates/genoma-humano/raw)~~ **PRODUZIDO (2026-08-12)**.
2. **BIP-001** — ~~origem/proveniência já mapeada; falta download~~ **PRODUZIDO (2026-08-12; 3 origens primárias: Comissão, CSB, JIT)**; demais fontes da árvore (BP, Congresso, imprensa) facultativas em ciclo posterior.
3. **BIP-005** — **PRODUZIDO (2026-08-12; 2 origens: PMA, UK P&I Club)**.
4. **BIP-006** — **PRODUZIDO (2026-08-12; 2 origens: NTSB HAR-08/03, GPM/lrl.mn.gov)**.
5. **BIP-002** — **PRODUZIDO (2026-08-12; 2 origens: NBS BSS 143, acórdão 744 S.W.2d 524)**.
6. **BIP-003** — GAO/HHS/BARDA/empresas; coleta moderada-alta. **PRODUZIDO (2026-08-12; 3 origens: GAO-21-319, ficha HHS/DoD, CRS IN11560)**.
7. **BIP-007** — WHO/MSF/equipes; coleta alta (múltiplas origens). **PRODUZIDO (2026-08-12; 8 fontes: WHO, NEJM, MSF ×2, CDC, UNMEER ×2; extração de 5 PDFs OK; narrativa 1.340 palavras; 90 atomic facts)**.

## 4. Estrutura de produção (por BIP)

```
experiments/validation/GO-8B/pilot-input/BIP-NNN/<caso>/
├── sources/
│   ├── 00-index.md              # fronteira pré/pós gate (GO-8B)
│   ├── 01-origem-dos-documentos.md  # proveniência EI (SC-5)
│   └── raw/                     # downloads + checksums
├── narrative/
│   └── 01-narrativa-original.md # condição C; zero ECP
├── atomic-facts/
│   └── 02-atomic-facts.md       # condições A/B; fatos mínimos, zero ECP
└── README.md
```

> **Local:** sob `experiments/validation/GO-8B/` (fora do núcleo congelado 00-08). Ver §5.

## 5. Fronteira com o congelado

- O núcleo congelado (00–08 + scripts registrados) **não é tocado**.
- `pilot-input/` é novo diretório operacional, fora do escopo do Lock.
- Fontes brutas de `independence/candidates/` podem ser **copiadas/rastreadas** (não interpretativas); nenhuma narrativa/AF/reconstrução dos SX é copiada.

## 6. Critérios de qualidade da produção (zero ECP)

- Vocabulário neutro (regra N-1 / lista 52 termos compilada).
- Atomic facts: fatos mínimos atômicos, sem interpretação, sem taxonomia.
- Narrativa: fatos históricos em ordem, sem categorias ECP.
- Rastreabilidade: cada AF/narrativa referencia `source_refs` do `01-origem-dos-documentos.md`.

## 7. Validação pós-produção

- Verificação léxica (zero termos ECP) sobre narrativa/AF.
- Verificação de rastreabilidade (100% refs → sources).
- Verificação de não-importação (diff contra SX-001/002/003).
- Registro em `pilot-input/VALIDATION-REPORT.md`.

---

**Fim do manifest. Nenhum material interpretativo importado. Nenhuma execução experimental.**
