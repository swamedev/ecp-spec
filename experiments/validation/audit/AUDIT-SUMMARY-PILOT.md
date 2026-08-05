# Auditoria Piloto do Corpus Experimental — Resumo

| Campo | Valor |
|---|---|
| **Etapa** | P-0005A.2b (Piloto) |
| **Protocolo** | [ECP-AUDIT-001](./ECP-AUDIT-001.md) v0.1 → v1.0 |
| **Relatório técnico** | [AUDIT-REPORT-PILOT.yaml](./AUDIT-REPORT-PILOT.yaml) |
| **Data** | 2026-08-03 |
| **Escopo** | EXP-001, 16 OBS do [CORPUS-EXPERIMENTAL-v1](../corpus/CORPUS-EXPERIMENTAL-v1.yaml) |

## O que esta auditoria responde — e o que não responde

Esta auditoria **não certifica o corpus**. Ela responde a pergunta de um nível
acima:

> **O protocolo de auditoria consegue decidir de forma consistente?**

Este é o princípio da **Meta-Validação**: antes de validar um artefato, valida-se
o instrumento de validação. Já validamos o schema (P-0005A.2a) e o minerador;
agora validamos o protocolo de auditoria.

## Resultados

### Reconstrução (RA-OBS-003)

- **16/16 OBS reconstruíveis** exclusivamente a partir dos artefatos de EXP-001.
- Nenhuma falha de reconstrução no relatório final.

### Classificação ontológica (concordância)

- Classificação independente aplicando os critérios objetivos do protocolo
  (necessidade relacional, independência de implementação, impacto causal):
  **16/16 concordantes** com o `kind` congelado do corpus (concordância = 1.0).

### Admissibilidade (RA-OBS)

- RA-OBS-001..007 conferidos; OBS-0016 confirmada como **caso canônico de
  não-observação** (derived, viola RA-OBS-001).

## O que o piloto revelou

1. **Fragilidade do instrumento, não do corpus.** O parsing inicial de chaves
   compostas (`G-0001-resolves-P-0001`) falhou por causa de IDs com hífen. A
   ferramenta foi corrigida — exatamente o tipo de achado que o piloto existe
   para expor.
2. **Critérios objetivos funcionam.** A aplicação mecânica dos critérios
   reproduziu 100% da classificação — sem consultar o `kind` gravado.
3. **Limitação honesta:** a concordância **inter-humana** (Cohen's kappa) ainda
   não foi medida — exige **dois avaliadores humanos independentes**, pendente
   para a auditoria oficial.

## Veredito do piloto

**PASS** — o protocolo mostrou-se **reproduzível e objetivo** dentro do escopo
avaliado.

## Próximos passos (ordem)

1. Protocolo congelado como **ECP-AUDIT-001 v1.0** (gate oficial).
2. Medir concordância inter-humana (kappa) com dois avaliadores independentes.
3. Aplicar o gate ao corpus — só então a auditoria oficial da P-0005A.2b
   certifica o corpus.
