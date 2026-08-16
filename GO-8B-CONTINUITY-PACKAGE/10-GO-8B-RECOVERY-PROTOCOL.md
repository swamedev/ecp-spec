# GO-8B — RECOVERY PROTOCOL

## If a new chat/AI receives this package

1. Read `00-GO-8B-CONTINUITY-MASTER.md`.
2. Read `01-GO-8B-STATE.md`.
3. Read `05-GO-8B-CURRENT-BLOCKER.md`.
4. Read `02-GO-8B-GOVERNANCE.md`.
5. Read `07-GO-8B-ACTION-QUEUE.md`.
6. Do not execute anything.
7. Report reconstructed state.
8. Ask whether governance has decided P1-C2-01.

## Recovery prompt

"Leia o pacote GO-8B-CONTINUITY. Não execute alterações. Reconstrua o estado, identifique o gate, o blocker e as decisões pendentes. Confirme que os artefatos 00–08 e scripts estão LOCKED/FROZEN. O estado atual é STOP por P1-C2-01. Aguarde decisão de governança."

## If files differ from this package

Do not reconcile silently.
Classify:
- source artifact;
- continuity package;
- filesystem;
- Lock manifest.

Then STOP and report.

## If an artifact is missing

Do not recreate from memory.
Use the authoritative repository/Lock data if available.
If reconstruction is necessary, treat it as a new governance action.

## If a frozen artifact is edited

STOP.
Record:
- file;
- timestamp;
- before/after if available;
- whether hash changed.
Do not repair in-place.
