# GO-8B — LOCK / IMMUTABILITY

## Locked state

GO-8B está LOCKED/FROZEN.

Manifest SHA-256:
`c55799d895a4f73888713a8538c6b9a6c5df1d7cde71c88141e16b9e9b216636`

## Freeze rule

Qualquer mudança em artefato congelado exige:
new version → governance decision → audit → rehash → new Lock.

## Hashing protocol

Canonical content:
- UTF-8 no BOM
- LF
- exactly one final newline
- whitespace otherwise preserved

Manifest:
- hashes dos conteúdos congelados;
- hash do manifesto não entra no próprio manifesto;
- hash do manifesto fica no Lock Record.

## Operational artifacts

Artefatos produzidos posteriormente não alteram o núcleo congelado. Eles devem possuir seu próprio controle de versão/freeze quando aplicável.

## STOP rule

Após primeiro hash:
qualquer divergência → STOP.
Nunca “corrigir e seguir” dentro da mesma operação de hashing.
