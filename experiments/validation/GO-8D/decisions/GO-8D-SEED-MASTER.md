# GO-8D — SEED MASTER (Decisão Formal da Governança)

**Data:** 2026-08-14
**Ciclo:** GO-8D — EXECUTION PHASE
**Tipo:** decisão de governança (etapa autorizada de geração de seeds)
**Base:** pré-registro v1.0 §10 (seed_master PENDING LOCK PROTOCOL) · D-07 §5 ("novo seed_master GO-8D")
**Status:** **APROVADO** (2026-08-14)

---

## 1. Decisão

A governança aprova o `seed_master` do estudo confirmatório GO-8D:

```yaml
seed_master:
  value: 20260815
  type: uint64
  hex: 0x1F5143F
```

- **Justificativa:** convenção de data sequencial; **distinto do GO-8C (20260814)**; determinístico e
  auditável; nenhuma sobreposição com streams metodológicos (D-02/D-03/D-07 usaram `20260814`).
- **Streams metodológicos:** `seed_power_simulation = 20260814` (D-07) **não** é reutilizado;
  `seed_statistics` usa stream isolado derivado do seed_master (ver §2).

## 2. Método de derivação das 108 seeds (execução GO-8D)

Para cada célula `(bip, condicao)`:

1. Stream isolado via `numpy.random.SeedSequence(seed_master=20260815, spawn_key=(bip_idx, cond_idx))`,
   `cond_idx` em 0/1/2 (A/B/C), `bip_idx` em 0..11 (BIP-001..012) — **sem reutilização entre células**;
2. `rng = numpy.random.Generator(PCG64(ss))`;
3. `seed_j = int.from_bytes(rng.bytes(8), "little")` para `j = 1, 2, 3` (3 seeds por célula).

Total: **12 BIPs × 3 condições × 3 seeds = 108 seeds** determinísticas. Nenhuma seed deriva de
resultados; nenhuma reutilização entre streams.

## 3. Stream da análise estatística

`seed_statistics` = stream isolado: `SeedSequence(20260815, spawn_key=("statistics",))` → usado para
o bootstrap pareado (B=10.000) e demais cálculos estocásticos do plano inferencial. Documentado no
`STATISTICAL-REPORT-G8D.md`.

## 4. Rastreabilidade

- Registro por execução: `taxonomy_sha256` (corrigida = `5ba63db7a81c454d…`) e `taxonomy_version`.
- Manifesto de seeds salvo em `study-output/seeds_g8d.py` (estrutura `seeds[bip][cond] = {seed1,seed2,seed3}`).
- Este registro entra no `ACTION-REGISTER.md` (GO-8D) como decisão autorizada.

---

**Fim do registro do seed_master. GO-8D EXECUTION PHASE — 2026-08-14. Seed_master APROVADO = 20260815.**