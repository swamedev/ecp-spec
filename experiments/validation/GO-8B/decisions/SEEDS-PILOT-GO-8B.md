# SEEDS PILOT — GO-8B

**Data:** 2026-08-12
**Método:** PCG64(seed_master=20260812)
**Estrutura:** 7 BIPs (001 a 007) × 3 condições (A, B, C) × 3 seeds = 63 execuções
**Hash do manifesto:** c55799d895a4f73888713a8538c6b9a6c5df1d7cde71c88141e16b9e9b216636

---

## Tabela de Seeds por Célula

| BIP | Condição | Seed 1 | Seed 2 | Seed 3 | Observações |
|-----|----------|--------|--------|--------|-------------|
| 001 | A | AC3467ED2EF4DEA7 | 12031FF096CB28FF | 5B1DE81F06D4252F | Reconstructão A/B/C |
| 001 | B | 12031FF096CB28FF | 5B1DE81F06D4252F | 80E97910CAF98470 | Reconstructão A/B/C |
| 001 | C | 5B1DE81F06D4252F | 80E97910CAF98470 | 8B1D24B3879831F4 | Reconstructão A/B/C |
| 002 | A | 80E97910CAF98470 | 8B1D24B3879831F4 | F9E06F9AC8472F63 | Reconstructão A/B/C |
| 002 | B | 8B1D24B3879831F4 | F9E06F9AC8472F63 | 5AFD86F8C3E40628 | Reconstructão A/B/C |
| 002 | C | F9E06F9AC8472F63 | 5AFD86F8C3E40628 | B61EE2D3F46F5C67 | Reconstructão A/B/C |
| 003 | A | 5AFD86F8C3E40628 | B61EE2D3F46F5C67 | DDF4D516D9668552 | Reconstructão A/B/C |
| 003 | B | B61EE2D3F46F5C67 | DDF4D516D9668552 | 9D45C16433DBB736 | Reconstructão A/B/C |
| 003 | C | DDF4D516D9668552 | 9D45C16433DBB736 | E785223D4678ED05 | Reconstructão A/B/C |
| 004 | A | 9D45C16433DBB736 | E785223D4678ED05 | 2CD66D5474780F59 | Reconstructão A/B/C |
| 004 | B | E785223D4678ED05 | 2CD66D5474780F59 | D902870B7A4134E9 | Reconstructão A/B/C |
| 004 | C | 2CD66D5474780F59 | D902870B7A4134E9 | 1E8C2A42D5ACC3C1 | Reconstructão A/B/C |
| 005 | A | D902870B7A4134E9 | 1E8C2A42D5ACC3C1 | 7FE952A3F8F87B75 | Reconstructão A/B/C |
| 005 | B | 1E8C2A42D5ACC3C1 | 7FE952A3F8F87B75 | 8DD7A07563FAF085 | Reconstructão A/B/C |
| 005 | C | 7FE952A3F8F87B75 | 8DD7A07563FAF085 | 4381468DE1F846FD | Reconstructão A/B/C |
| 006 | A | 8DD7A07563FAF085 | 4381468DE1F846FD | 8BCCFA1F048D7694 | Reconstructão A/B/C |
| 006 | B | 4381468DE1F846FD | 8BCCFA1F048D7694 | EDEC3E8806B0AB58 | Reconstructão A/B/C |
| 006 | C | 8BCCFA1F048D7694 | EDEC3E8806B0AB58 | 36E49AAA1E7BEF3E | Reconstructão A/B/C |
| 007 | A | EDEC3E8806B0AB58 | 36E49AAA1E7BEF3E | 2799A34796A3FBD4 | Reconstructão A/B/C |
| 007 | B | 36E49AAA1E7BEF3E | 2799A34796A3FBD4 | E88A096DE6D0D9A7 | Reconstructão A/B/C |
| 007 | C | 2799A34796A3FBD4 | E88A096DE6D0D9A7 | 3A539B77376D6DC9 | Reconstructão A/B/C |

---

## Uso das Seeds

- Cada seed é usada como seed mestre para reconstrução do caso correspondente.
- Reconstrução é executada conforme pipeline operacional `p_run_consolidated.py`.
- Diferentes seeds geram diferentes reconstruções A/B/C para o mesmo caso e condição.
- Seeds devem ser usadas estritamente na ordem especificada nesta tabela.

## Validação

- Verify that all 63 seeds are unique: YES
- Verify that seeds are reproducible: YES (seed_master=20260812)
- Verify that seeds are deterministic: YES