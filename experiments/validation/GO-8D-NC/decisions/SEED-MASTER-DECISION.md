# GO-8D-NC — SEED MASTER DECISION

**Data:** 2026-08-15
**Decisor:** Governança do novo ciclo confirmatório
**Base:** D-MV-04-NEW-CYCLE-EXECUTION-PACKAGE.md (decisão 4) · 08-PRE-REGISTRATION-NEW-CYCLE.md (§2)

## Decisão

- **seed_master = `20260816`** (uint64).
- Distinto de todos os anteriores: GO-8C = 20260814; GO-8D = 20260815.
- **Método:** PCG64 via `np.random.SeedSequence(20260816, spawn_key=(bip_idx, cond_idx))`,
  3 uint64 por célula (seed1/seed2/seed3); total 30×3×3 = **270 seeds únicas**.
- `seed_statistics` (análise) derivado por spawn isolado (não o master), documentado no
  script `analyze.py`.

## Regra

A geração **efetiva** das seeds (`generate_seeds.py` → `seeds_nc.py`) só ocorre **após
autorização formal da governança** (não nesta etapa de Lock Fase 1). O valor já está congelado
neste documento.

---

**Fim. Aprovado pela governança em 2026-08-15.**
