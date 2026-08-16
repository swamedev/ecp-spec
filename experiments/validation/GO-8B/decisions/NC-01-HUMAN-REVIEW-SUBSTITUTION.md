# DECISÃO DE GOVERNANÇA — NC-01 (HUMAN-REVIEW SUBSTITUTION)

**Data:** 2026-08-12
**Decisor:** Governança GO-8B
**Status:** DECIDED
**Artefatos afetados:** nenhum artefato do núcleo congelado (00–08) é alterado; esta decisão é registrada em artefato separado (este arquivo).

---

## 1. Contexto

O requisito original de revisão humana independente (NT-05, conforme `03-SYNTHETIC-TAXONOMY-C3.md` §4.1/§4.4) exige três validadores humanos independentes (R1, R2, R3) para emitir o verdict final do BIP-VAL. Em 2026-08-12, constatou-se a indisponibilidade de três validadores humanos qualificados para conduzir a revisão no prazo do piloto.

O BIP-VAL_REPORT.yaml (gerado em 2026-08-12) reporta:
- NT-01..04: PASS
- NT-05: PENDING (requer 3 validadores humanos independentes)
- Verdict: PENDING

---

## 2. Decisão

**A governança autoriza a substituição temporária do gate NT-05 (revisão humana) por um protocolo de auditoria automatizada independente**, doravante denominado `NT-05-AUTOMATED-INDEPENDENT-REVIEW`.

**Esta substituição NÃO atribui equivalência entre revisão automatizada e revisão humana.** Trata-se de um mecanismo operacional limitado e auditável, criado para permitir a verificação objetiva dos artefatos operacionais sem interromper o fluxo do piloto.

**O escopo da substituição limita-se ao NT-05.** Nenhum outro gate humano é afetado por esta decisão.

---

## 3. Justificativa

- O requisito original de revisão humana (NT-05) não pode ser satisfeito na fase atual por indisponibilidade de três validadores humanos qualificados.
- O piloto GO-8B requer progressão além do bloqueio NT-05, mantendo integridade metodológica.
- Um protocolo de auditoria automatizada com dupla execução independente, critérios PASS/FAIL objetivos e evidências verificáveis preserva a honestidade metodológica sem fingir equivalência epistemológica com revisão humana.

---

## 4. Implementação operacional

1. **Criar protocolo** `NT-05-AUTOMATED-INDEPENDENT-REVIEW.md` com checklist objetivo, critérios PASS/FAIL e regra de independência (dupla execução, divergência = STOP).
2. **Executar PRIMEIRA auditoria** conforme o protocolo (C2, C3, GFR, WL, Materiais, Reprodutibilidade).
3. **Registrar** em `decisions/ACTION-REGISTER.md`: NC-01 = DECIDED; NC-02 = IN PROGRESS (primeira execução).
3. **NÃO executar segunda auditoria** até revisão dos resultados da primeira.

---

## 5. Referências

- `03-SYNTHETIC-TAXONOMY-C3.md` §4.1/§4.4 (NT-05 original)
- `scripts/go8b/operational/BIP-VAL_REPORT.yaml` (NT-01..04 PASS, NT-05 PENDING)
- `scripts/go8b/operational/INFRA-VALIDATION-REPORT.md` (item 3: auditoria externa C2/C3)
- `experiments/validation/GO-8B/decisions/NT-05-AUTOMATED-INDEPENDENT-REVIEW.md` (protocolo)
- `decisions/ACTION-REGISTER.md` (NC-01, NC-02)
- Hash do manifesto vigente: `c55799d895a4f73888713a8538c6b9a6c5df1d7cde71c88141e16b9e9b216636`

---

**Fim da decisão. Nenhum artefato congelado alterado. Nenhum dado experimental produzido.**