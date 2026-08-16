# GO-8B — STATE SNAPSHOT

## Current state

| Item | Estado |
|---|---|
| R1 | concluído |
| R2 | STOP → decisões necessárias |
| R3–R5 | revisões e decisões aplicadas |
| R6 | PASS/CLEAN |
| R7 | PASS/CLEAN |
| R8 | READY condicionado |
| R9 | PASS/CLEAN |
| Pré-registro 08 | criado e auditado |
| Hashes | gerados |
| Lock | LOCKED/FROZEN |
| Experimento | não executado |
| Dados reais | nenhum |
| Commit | nenhum |
| Pilot authorization | concedida |
| Pre-flight | FAIL por artefatos ausentes |
| P1 | STOP por P1-C2-01 |

## Current blocker

A seed registrada em `02-C2-PERMUTATION.md` não reproduz a permutação congelada. O JSON §6 é internamente consistente; a seed `258915` reproduz a tabela, mas não é a seed registrada.

## Immediate gate

`GOVERNANCE DECISION → P1-C2-01`

## Forbidden shortcuts

- não escolher seed/tabela sem decisão;
- não editar 02;
- não produzir C2 com interpretação não autorizada;
- não iniciar P2–P5 como se P1 estivesse resolvido se houver dependência;
- não executar experimento.
