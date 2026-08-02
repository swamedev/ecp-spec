# ECP-CASES — Laboratório de Aplicação

| Campo | Valor |
|---|---|
| **Tipo** | Documento de Validação (`VALID`) |
| **Fase** | V0 — Validation |
| **Status** | Rascunho |
| **Versão** | 0.3.0 |
| **Data** | 2026-08-02 |
| **Autores** | ECP Contributors |
| **Objetivo** | Testar se o ECP funciona em projetos de naturezas diferentes |

> Este documento é o **laboratório** do protocolo. Cada caso responde a uma pergunta: *o ECP continua funcionando aqui?* Um caso que falha é uma **descoberta**, não um fracasso — ele alimenta ECP-PROOF e as RFCs futuras. Nenhum caso é "exemplo bonito"; todos devem registrar onde o protocolo foi **forçado**, **omisso** ou **excessivo**.

---

## 1. Template de aplicação

Cada caso segue esta estrutura:

```
CASO <n> — <nome>
TIPO:       <domínio do projeto>
PROBLEMA:   <P — condição verificável que motiva o projeto>
OBJETIVO:   <G — estado desejado que responde a P>
CLAIMS:     <C — afirmações críticas que sustentam as decisões>
CONHECIMENTO: <K — o que se sabe; lacunas>
SUPOSIÇÕES: <A — hipóteses registradas>
EVIDÊNCIA:  <E — observações que sustentam os claims>
DECISÕES:   <D — decisões de transição mais marcantes>
ARTEFATOS:  <A — produtos materiais>
VALIDAÇÃO:  <como o resultado foi verificado>
APRENDIZADO:<o que a validação corrigiu>
VEREDITO:   <PASSA | NÃO PASSA | PARCIAL>
PONTO DE FALHA/STRESS:
    <onde o ECP foi forçado, omisso ou excessivo>
```

---

## 2. Casos

### CASO 1 — ERP (Sistema de Gestão Empresarial)
```
PROBLEMA:   Fechamento do caixa leva 4 horas; reconciliação é manual.
OBJETIVO:   Reduzir fechamento do caixa para < 15 min em 90% dos dias.
CLAIMS:     C-1 "Integração financeira elimina reentrada manual de dados."
            C-2 "O banco de dados suporta 500 usuários concorrentes."
CONHECIMENTO: Regras fiscais; processos do cliente; esquema legado.
SUPOSIÇÕES: A-1 "A legislação fiscal não muda durante o projeto."
            A-2 "O fornecedor mantém a API do banco por 3 anos."
EVIDÊNCIA:  Benchmark de concorrência; amostra de fechamentos reais.
DECISÕES:   Migrar para SaaS vs. on-premise → SaaS (evidência de TCO).
ARTEFATOS:  ERP configurado; scripts de migração; documentação.
VALIDAÇÃO:  30 dias de fechamentos reais cronometrados.
APRENDIZADO:A-1 falhou (nota fiscal eletrônica mudou) → decisões de
            layout fiscal reavaliadas.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    A-1 invalidada no meio do projeto exigiu reavaliação de 11
    decisões — o mecanismo de invalidação do ECP funcionou, mas o custo
    foi alto. Suposições regulatórias deveriam ter `validation_date`
    mais curta.
```

### CASO 2 — PDV (Ponto de Venda)
```
PROBLEMA:   Filas no checkout no horário de pico (tempo de atendimento
            médio 6 min; meta 2 min).
OBJETIVO:   Atendimento médio < 2 min no pico em 8 semanas.
CLAIMS:     C-1 "Leitor de código de barras reduz tempo de digitação."
            C-2 "Offline-first mantém vendas com rede instável."
CONHECIMENTO: Padrões de varejo; hardware de leitura disponível.
SUPOSIÇÕES: A-1 "Operadores aceitam o novo fluxo em 2 semanas."
            A-2 "A rede da loja permanece instável."
EVIDÊNCIA:  Teste A/B do fluxo; piloto em 1 loja.
DECISÕES:   Hardware dedicado vs. celular → celular (custo × evidência).
ARTEFATOS:  PDV mobile; treinamento; métricas de fila.
VALIDAÇÃO:  Medição contínua do tempo de checkout em 4 lojas.
APRENDIZADO: A-1 subestimada; treinamento ampliado.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    A cadência de decisões de campo (ajustes diários) é alta para o
    custo de um Decision Record por decisão. Requer política de
    agregação (pendência do ECP-PROOF, P-4).
```

### CASO 3 — Game Indie
```
PROBLEMA:   Protótipo não gerou retenção além da primeira sessão.
OBJETIVO:   Retenção D1 >= 30% no lançamento do jogo.
CLAIMS:     C-1 "Loop de jogo em 10 minutos sustenta a retenção."
            C-2 "Pixel art reduz custo de produção sem perder apelo."
CONHECIMENTO: Gêneros concorrentes; mecânicas testadas na comunidade.
SUPOSIÇÕES: A-1 "O estilo visual atrai o público-alvo."
            A-2 "O ciclo de produção de 6 meses é viável."
EVIDÊNCIA:  Playtests com telemetria; pesquisa com público.
DECISÕES:   Focar em uma mecânica vs. três → uma (evidência de playtest).
ARTEFATOS:  Build jogável; trailer; página de venda.
VALIDAÇÃO:  Beta fechado com métricas de retenção.
APRENDIZADO: C-1 confirmada parcialmente; curva de dificuldade ajustada.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    A área criativa resiste a "claim com evidência" para decisões
    estéticas. O caso mostrou que evidência de playtest resolve — mas
    exige nota no P-1 sobre protótipos como evidência.
```

### CASO 4 — SaaS B2B
```
PROBLEMA:   Churn de 6%/mês em clientes enterprise.
OBJETIVO:   Reduzir churn para < 2%/mês em 2 trimestres.
CLAIMS:     C-1 "Onboarding estruturado reduz churn de 30 dias."
            C-2 "Suporte no idioma do cliente eleva NPS."
CONHECIMENTO: Jornadas de clientes ativos × cancelados.
SUPOSIÇÕES: A-1 "Churn é causado por onboarding, não por preço."
EVIDÊNCIA:  Entrevistas de churn; funil de ativação.
DECISÕES:   Investir em onboarding vs. redução de preço → onboarding.
ARTEFATOS:  Fluxo de onboarding; e-mails reativados.
VALIDAÇÃO:  A/B com 40% da base por 60 dias.
APRENDIZADO: A-1 parcialmente confirmada; preço ainda afeta segmento SMB.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    Nenhum stress significativo; o caso é o mais "doméstico" do ECP.
```

### CASO 5 — API Pública (Plataforma)
```
PROBLEMA:   Integradores abandonam a API por documentação e SLA ruins.
OBJETIVO:   TTFH (time-to-first-hello) < 5 min e uptime 99.9%.
CLAIMS:     C-1 "A API idempotente evita duplicações de pagamento."
            C-2 "Rate limiting protege o backend sob pico."
CONHECIMENTO: Contratos de API concorrentes; padrões de mercado.
SUPOSIÇÕES: A-1 "O volume projetado de 10k req/s se confirma."
EVIDÊNCIA:  Load test; testes de contrato automatizados.
DECISÕES:   REST vs. gRPC → REST (ecossistema de integradores).
ARTEFATOS:  Spec OpenAPI; sandbox; SDKs.
VALIDAÇÃO:  Programas de teste de integradores reais.
APRENDIZADO: A-1 superestimada; capacidade ampliada com folga.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    Nenhum — processo de contrato do ECP é análogo ao design de APIs.
```

### CASO 6 — Aplicativo (App Mobile)
```
PROBLEMA:   Baixa adoção (DAU) após o lançamento v1.
OBJETIVO:   DAU de 50k em 6 meses com retenção D7 >= 25%.
CLAIMS:     C-1 "Notificações push segmentadas elevam D7."
            C-2 "Tempo de carregamento < 2s reduz abandono."
CONHECIMENTO: Dados de uso; benchmarks de performance.
SUPOSIÇÕES: A-1 "O usuário-alvo aceita permissões de notificação."
EVIDÊNCIA:  Análise de funil; testes de performance em devices reais.
DECISÕES:   Nativos vs. híbrido → híbrido (velocidade × evidência).
ARTEFATOS:  Build v2; painel de métricas.
VALIDAÇÃO:  Lançamento gradual (canário) por 4 semanas.
APRENDIZADO: A-1 confirmada com 68% de aceite; copy otimizado.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    Nenhum — caso típico de métricas; decisões frequentes exigem
    agregação (como PDV).
```

### CASO 7 — Agente de IA (Automação de Suporte)
```
PROBLEMA:   Suporte humano não escala; SLA de resposta > 4h.
OBJETIVO:   Resolver 60% dos tickets sem humano, SLA < 10 min.
CLAIMS:     C-1 "O modelo responde corretamente em 85% dos tickets."
            C-2 "Escalabilidade de custo por ticket é viável."
CONHECIMENTO: Base de FAQs; históricos de tickets resolvidos.
SUPOSIÇÕES: A-1 "Os tickets atuais são similares aos históricos."
EVIDÊNCIA:  Avaliação em conjunto de validação com 2k tickets.
DECISÕES:   LLM proprietário vs. fine-tune aberto → decisão por custo
            e evidência de acurácia.
ARTEFATOS:  Agente; instrumentação de confiança; fallback humano.
VALIDAÇÃO:  Shadow mode por 30 dias comparado ao humano.
APRENDIZADO: A-1 falhou em nicho de tickets (legislação) → domínio
            específico delegado ao humano.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    O agente produz *respostas*, não *decisões* — a triagem de
    conhecimento do ECP (ECP-006) é o ponto natural de acoplamento.
    A confiança calculada do ECP-008 é diretamente aplicável à
    calibração do modelo.
```

### CASO 8 — Curso (Educação Digital)
```
PROBLEMA:   Alta evasão em curso online (70% não concluem).
OBJETIVO:   Conclusão >= 40% com satisfação NPS >= 50.
CLAIMS:     C-1 "Pílulas de vídeo curtas reduzem abandono."
            C-2 "Projetos práticos aumentam engajamento."
CONHECIMENTO: Análise de onde os alunos desistem.
SUPOSIÇÕES: A-1 "O público trabalha e estuda à noite."
EVIDÊNCIA:  Piloto com turma controlada; analytics de engajamento.
DECISÕES:   Ao vivo vs. gravado → gravado + tutorias (evidência).
ARTEFATOS:  Trilha do curso; materiais; avaliações.
VALIDAÇÃO:  Duas turmas completas com comparação de evasão.
APRENDIZADO: A-1 confirmada; horários de tutorias ajustados.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    Nenhum stress; a cadeia P→G→C→E→D se aplica com naturalidade a
    design instrucional.
```

### CASO 9 — Sistema Embarcado (Dispositivo Médico)
```
PROBLEMA:   Falhas de firmware causam recalls e risco ao paciente.
OBJETIVO:   Zero defeitos críticos em produção; certificação IEC 62304.
CLAIMS:     C-1 "O firmware é seguro sob falha de energia."
            C-2 "A RTOS atende ao tempo real (< 10ms de jitter)."
CONHECIMENTO: Normas de certificação; análise de risco do dispositivo.
SUPOSIÇÕES: A-1 "O hardware de produção é idêntico ao do protótipo."
EVIDÊNCIA:  Testes HIL (hardware-in-the-loop); análise estática; FMEA.
DECISÕES:   RTOS comercial vs. bare-metal → RTOS certificável.
ARTEFATOS:  Firmware; matriz de rastreabilidade de requisitos; dossiê.
VALIDAÇÃO:  Auditoria externa de certificação.
APRENDIZADO: A-1 falhou (variante de processador) → retrabalho em 3 módulos.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    É o caso mais próximo do "ideal" do ECP: a indústria já exige
    rastreabilidade total (equivalente à Lei L-1). O ECP é praticamente
    um IEC 62304 genérico. A ausência de artefatos físicos não é um
    problema — o firmware é o artefato.
```

### CASO 10 — Pesquisa Científica
```
PROBLEMA:   Resultados não reproduzíveis; hipóteses não registradas.
OBJETIVO:   Publicação com pipeline reprodutível e dados abertos.
CLAIMS:     C-1 "O efeito observado não é devido a confundidores."
            C-2 "O resultado replica com outra amostra."
CONHECIMENTO: Literatura; método; dados preliminares.
SUPOSIÇÕES: A-1 "A hipótese nula será rejeitada na amostra final."
EVIDÊNCIA:  Pré-registro; análise pré-especificada; replicação.
DECISÕES:   Publicar vs. adiar até mais poder estatístico → publicar
            com análise de sensibilidade.
ARTEFATOS:  Pré-registro; código da análise; dados abertos; paper.
VALIDAÇÃO:  Revisão por pares; replicação independente.
APRENDIZADO: A-1 parcial; efeito menor que o estimado — calibração
            melhorada.
VEREDITO:   PARCIAL
PONTO DE FALHA/STRESS:
    Duas tensões: (1) a exploração pré-problema (pendência do L-1)
    é o *motor* da ciência; (2) o "claim de verdade" em ciência não é
    decidível por evidência finita — a força de evidência do ECP-008
    precisa acomodar o conceito de *inferência estatística*. A
    serendipidade (pendência do P-2) ocorre aqui com frequência.
```

### CASO 11 — Livro (Produção Editorial)
```
PROBLEMA:   Livro planejado em 12 meses, em atraso crônico.
OBJETIVO:   Entrega do manuscrito em 9 meses com qualidade editorial.
CLAIMS:     C-1 "Ritmo de 500 palavras/dia atinge a meta."
            C-2 "O público-alvo valoriza o estilo proposto."
CONHECIMENTO: Voz do autor; estrutura narrativa; público.
SUPOSIÇÕES: A-1 "O capítulo inicial prende a leitura."
EVIDÊNCIA:  Leitores-beta; capítulos pilotos; leitura crítica.
DECISÕES:   Estrutura fixa vs. orgânica → híbrido (evidência de betas).
ARTEFATOS:  Manuscrito; revisões; capa; sumário final.
VALIDAÇÃO:  Leitura crítica por pares; teste com leitores.
APRENDIZADO: A-1 confirmada; prólogo reescrito.
VEREDITO:   PARCIAL
PONTO DE FALHA/STRESS:
    A criação literária responde a *gosto*, não a "verdade" — a
    evidência (beta) é parcialmente subjetiva. O ECP funciona na
    *produção* (prazos, escopo, decisões editoriais), mas não decide
    *qualidade estética*. Verditio honesto: o ECP governa o processo,
    não a arte.
```

### CASO 12 — Hospital (Projeto de Melhoria de Fluxo)
```
PROBLEMA:   Tempo de espera no pronto-socorro > 4h para casos urgentes.
OBJETIVO:   Tempo até o primeiro atendimento < 30 min em 90% dos casos.
CLAIMS:     C-1 "Triagem por prioridade real aloca médicos melhor."
            C-2 "Leito de observação libera salas de atendimento."
CONHECIMENTO: Fluxo real por turno; capacidades de leitos.
SUPOSIÇÕES: A-1 "O corpo clínico adere ao protocolo de triagem."
EVIDÊNCIA:  Medições de fluxo; simulação de filas; pilotos por ala.
DECISÕES:   Redesenhar triagem vs. contratar médicos → triagem.
ARTEFATOS:  Protocolo de triagem; sistema de priorização.
VALIDAÇÃO:  Medição contínua por 60 dias.
APRENDIZADO: A-1 parcial; necessidade de campeões clínicos.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    Decisões de *campo* e hierarquia clínica adicionam uma camada de
    governança que o ECP não modela ainda (quem pode decidir o quê).
    O caso recomenda a RFC de Governance antecipada.
```

### CASO 13 — Construção Civil (Obra)
```
PROBLEMA:   Atraso de 4 meses em obra por incompatibilidade de projetos.
OBJETIVO:   Entregar obra com tolerância de 2 semanas sobre o cronograma.
CLAIMS:     C-1 "BIM detecta incompatibilidades antes da execução."
            C-2 "A programação da obra é factível com a equipe atual."
CONHECIMENTO: Projetos de disciplinas; cronograma; fornecedores.
SUPOSIÇÕES: A-1 "O solo do terreno é estável conforme sondagem."
            A-2 "Fornecedor de estrutura entrega no prazo."
EVIDÊNCIA:  Compatibilização BIM; relatórios de sondagem; histórico.
DECISÕES:   Compatibilizar BIM vs. executar direto → BIM.
ARTEFATOS:  Modelo BIM; cronograma; registros de decisão (diário).
VALIDAÇÃO:  Marcos físicos de obra com inspeção.
APRENDIZADO: A-2 falhou (chuvas + fornecedor) → plano B acionado.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    Decisões orais de campo são frequentes (pendência P-4); o diário de
    obra funciona como agregador de decisões. A causalidade física
    (clima) escapa ao controle, mas entra como risco declarado.
```

### CASO 14 — Treinamento Militar
```
PROBLEMA:   Prontidão operacional baixa por falta de treino realista.
OBJETIVO:   Elevar índice de proficiência do pelotão para >= 85%.
CLAIMS:     C-1 "Simulação de combate melhora tomada de decisão tática."
            C-2 "O custo por ciclo de treino cai com simuladores."
CONHECIMENTO: Doutrina; limitações de equipamento; métricas atuais.
SUPOSIÇÕES: A-1 "O simulador transfere aprendizado para o campo real."
EVIDÊNCIA:  Exercícios controlados comparando simulação × campo.
DECISÕES:   Simuladores vs. exercícios reais → híbrido.
ARTEFATOS:  Currículo; simuladores configurados; avaliações.
VALIDAÇÃO:  Avaliação cega de proficiência pós-treino.
APRENDIZADO: A-1 confirmada para tática, não para condicionamento físico.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    O paradigma de comando (ordem) convive mal com "decisão verificável"
    em níveis táticos rápidos. A distinção decisão × processamento
    (pendência L-0) é essencial aqui.
```

### CASO 15 — Startup (MVP)
```
PROBLEMA:   Incerteza de demanda: não se sabe se o mercado quer o produto.
OBJETIVO:   Validar demanda com 100 clientes pagantes em 90 dias.
CLAIMS:     C-1 "CLV do segmento-alvo justifica o CAC."
            C-2 "A proposta de valor resolve dor real e não só desejada."
CONHECIMENTO: Entrevistas com potenciais clientes; mercado.
SUPOSIÇÕES: A-1 "O segmento inicial é o correto."
EVIDÊNCIA:  Landing page com conversão; pré-vendas; entrevistas.
DECISÕES:   Pivotar vs. perseverar → perseverar (evidência de conversão).
ARTEFATOS:  MVP; funil de vendas; métricas.
VALIDAÇÃO:  Pagamentos reais e retenção inicial.
APRENDIZADO: A-1 parcial; segmento refinado.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    A velocidade do lean startup (testar por semana) contrasta com o
    custo de formalização. O ECP funciona, mas a versão *encerrada* do
    protocolo precisa de peso leve para MVP (ex.: Decision Record
    reduzido). Recomenda-se uma "edição lean" na Camada 2.
```

### CASO 16 — Filme (Produção Audiovisual)
```
PROBLEMA:   Orçamento estourado em produção anterior.
OBJETIVO:   Entregar filme dentro do orçamento e do prazo de pós.
CLAIMS:     C-1 "O roteiro cabe no orçamento de locação."
            C-2 "A pós-produção completa em 6 meses com a equipe atual."
CONHECIMENTO: Planos de filmagem; custos de locação; disponibilidade.
SUPOSIÇÕES: A-1 "O clima não interrompe as gravações externas."
            A-2 "O ator principal está disponível nas datas."
EVIDÊNCIA:  Cotações; plano de filmagem; histórico de produções.
DECISÕES:   Locação real vs. estúdio → locação (evidência de custo ×
            fidelidade).
ARTEFATOS:  Roteiro final; cronograma; corte; mixagem.
VALIDAÇÃO:  Teste com público; revisão de custo final.
APRENDIZADO: A-1 falhou parcial (2 dias de chuva) → replanejamento.
VEREDITO:   PARCIAL
PONTO DE FALHA/STRESS:
    Igual ao Livro: a *decisão artística* (direção de arte, atuação)
    não é reduzível a claim com evidência — há um componente de gosto
    irredutível. O ECP governa a *produção* (logística, custo, prazo)
    e documenta as decisões criativas, sem julgar a estética. A
    pergunta "o ECP decide a qualidade do filme?" deve ser respondida
    NÃO — e isso precisa estar escrito na fundação (escopo).
```

### CASO 17 — Sistema de Faturamento Hospitalar (a partir do CASO 12)
```
PROBLEMA:   Perda de receita por glosas de faturamento (12%).
OBJETIVO:   Reduzir glosas para < 3% em 2 trimestres.
CLAIMS:     C-1 "Conferência automatizada reduz erros de cobrança."
            C-2 "Tabela de procedimentos atualizada evita negativas."
CONHECIMENTO: Regras de operadoras; causas de glosas.
SUPOSIÇÕES: A-1 "As operadoras mantêm as regras atuais."
EVIDÊNCIA:  Amostra de glosas classificadas por causa.
DECISÕES:   Automação de conferência vs. re-treinamento humano →
            automação + supervisão.
ARTEFATOS:  Regras de conferência; dashboard de glosas.
VALIDAÇÃO:  Comparação mensal de glosas pré/pós.
APRENDIZADO: A-1 falhou em 1 operadora → regra específica criada.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    Nenhum novo; reutiliza as pendências do CASO 12 (governança de
    decisão por hierarquia).
```

### CASO 18 — Projeto Open Source
```
PROBLEMA:   Manutenção concentrada em 1 mantenedor; risco de abandono.
OBJETIVO:   Distribuir manutenção em 3+ mantenedores ativos em 6 meses.
CLAIMS:     C-1 "Governança clara atrai contribuidores de longo prazo."
            C-2 "Tempo de resposta a PRs correlaciona com retenção."
CONHECIMENTO: Padrões de comunidades similares.
SUPOSIÇÕES: A-1 "Contribuidores surgirão com documentação de onboarding."
EVIDÊNCIA:  Métricas de contribuição; entrevistas com contribuidores.
DECISÕES:   BDFL vs. comitê → comitê com consenso 2/3.
ARTEFATOS:  Código; guias de contribuição; estrutura de governança.
VALIDAÇÃO:  Trimestre com 3 mantenedores ativos.
APRENDIZADO: A-1 confirmada parcialmente; onboarding simplificado.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    Decisões de comunidade são consensuais e lentas — o Decision
    Record individual não captura consenso facilmente. Requer nota
    sobre *decisões coletivas* (múltiplas entidades, uma decisão).
```

### CASO 19 — Marca / Produto Físico (Bens de Consumo)
```
PROBLEMA:   Lançamento anterior fracassou por proposta de valor difusa.
OBJETIVO:   Lançar produto com posicionamento validado e preço testado.
CLAIMS:     C-1 "O posicionamento diferencia de 2 concorrentes diretos."
            C-2 "O preço máximo aceito >= preço-alvo."
CONHECIMENTO: Painel de consumidores; análise de concorrência.
SUPOSIÇÕES: A-1 "O canal de distribuição chega ao público."
EVIDÊNCIA:  Teste de conceito; análise conjunta de preço.
DECISÕES:   Distribuição online vs. varejo → híbrido (evidência de
            alcance).
ARTEFATOS:  Protótipo; plano de lançamento; campanha.
VALIDAÇÃO:  Piloto em canal único com vendas reais.
APRENDIZADO: A-1 confirmada; expansão de canal.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    Nenhum novo; validação de mercado se encaixa no modelo de
    evidência.
```

### CASO 20 — Consultoria / Projeto por Contrato
```
PROBLEMA:   Escopo indefinido gera retrabalho e margem negativa.
OBJETIVO:   Entregar escopo fechado com margem >= 25%.
CLAIMS:     C-1 "O escopo levantado cobre os requisitos reais do cliente."
            C-2 "A estimativa tem precisão de +/- 15%."
CONHECIMENTO: Contratos anteriores; domínio do cliente.
SUPOSIÇÕES: A-1 "O cliente aprova o escopo sem mudanças."
EVIDÊNCIA:  Workshops de levantamento; benchmarks de estimativa.
DECISÕES:   Fixo vs. time & materials → híbrido (evidência de risco).
ARTEFATOS:  Contrato; cronograma; relatórios de progresso.
VALIDAÇÃO:  Aceite formal em marcos.
APRENDIZADO: A-1 falhou (3 mudanças de escopo) → processo de change
            request formalizado.
VEREDITO:   PASSA
PONTO DE FALHA/STRESS:
    O *contrato comercial* (escopo, preço) coexiste com o contrato ECP.
    A interface entre os dois precisa ser desenhada — mudanças de
    escopo viram novos goals ou revisão de problem.
```

---

## 3. Síntese dos casos

| # | Caso | Verditio | Stress principal identificado |
|---|---|---|---|
| 1 | ERP | PASSA | Suposições regulatórias com `validation_date` curta |
| 2 | PDV | PASSA | Agregação de decisões de campo |
| 3 | Game Indie | PASSA | Estética × evidência (P-1 protótipo) |
| 4 | SaaS B2B | PASSA | — |
| 5 | API | PASSA | — |
| 6 | App | PASSA | Agregação de decisões frequentes |
| 7 | Agente de IA | PASSA | Acoplamento com triagem de conhecimento |
| 8 | Curso | PASSA | — |
| 9 | Embarcado/médico | PASSA | ECP ≈ IEC 62304 genérico |
| 10 | Pesquisa científica | **PARCIAL** | Exploração pré-problema; inferência estatística; serendipidade |
| 11 | Livro | **PARCIAL** | Qualidade estética fora do escopo do ECP |
| 12 | Hospital | PASSA | Camada de governança de hierarquia |
| 13 | Construção civil | PASSA | Decisões orais; causalidade física |
| 14 | Treinamento militar | PASSA | Comando × decisão verificável em tempo real |
| 15 | Startup (MVP) | PASSA | Necessidade de edição "lean" do protocolo |
| 16 | Filme | **PARCIAL** | Escopo: ECP não decide estética |
| 17 | Faturamento hospitalar | PASSA | — |
| 18 | Open Source | PASSA | Decisões coletivas (consenso) |
| 19 | Produto físico | PASSA | — |
| 20 | Consultoria | PASSA | Interface contrato comercial × contrato ECP |

**17 PASSA, 3 PARCIAL, 0 NÃO PASSA (Rodada 1).**

## 4. Descobertas que alimentam a fundação

1. **Edição lean necessária** (CASO 15, 2, 6): decisões de baixa cadência exigem Decision Record completo; alta cadência exige versão agregada. → Regra de agregação (pendência P-4).
2. **Exploração pré-problema** (CASO 10): a ciência começa antes do problema formal. → Pendência L-1.
3. **Inferência estatística como evidência** (CASO 10): a hierarquia do ECP-008 precisa de nível para evidência probabilística pré-registrada.
4. **Decisões coletivas** (CASO 18): consenso ≠ decisão individual; precisa de modelo de co-autoria de decisão.
5. **Governança de hierarquia** (CASO 12, 14): quem pode decidir o quê não está modelado — antecipar a RFC de Governance.
6. **Escopo da estética** (CASO 11, 16): o ECP governa o processo de decisão, não a qualidade artística; escrever explicitamente na fundação.
7. **Interface com contrato comercial** (CASO 20): mudança de escopo = revisão de problem/goal; desenhar a interface.

---

## 5. Rodada 2 — Fechamento das descobertas contra as emendas

Cada descoberta foi re-testada contra as emendas aplicadas na fundação (ECP-000, ECP-003, ECP-008, ECP-009, ECP-INVARIANTS, ECP-GLOSSARY). Descoberta sem emenda correspondente permanece aberta como recomendação para a Camada 2.

| # | Descoberta | Emenda que a fecha | Situação |
|---|---|---|---|
| 1 | Edição lean (CASO 2, 6, 15) | ECP-009.3 — agregação de decisões de baixo impacto | RESOLVIDA |
| 2 | Exploração pré-problema (CASO 10) | ECP-000 §5.1 + GLOSSARY `EXPLORAÇÃO` | RESOLVIDA |
| 3 | Inferência estatística como evidência (CASO 10) | — (não é pendência do PROOF) | ABERTA — RFC futura de ECP-008 (Camada 2) |
| 4 | Decisões coletivas (CASO 18) | — | ABERTA — RFC futura de Governance |
| 5 | Governança de hierarquia (CASO 12, 14) | — | ABERTA — RFC futura de Governance |
| 6 | Escopo da estética (CASO 11, 16) | ECP-000 §6.1 `P-12` — escopo dos problemas não funcionais | RESOLVIDA |
| 7 | Interface com contrato comercial (CASO 20) | — | ABERTA — RFC futura de ECP-001/ECP-004 |

**Revalidação dos vereditos:**

- **CASO 10 (Pesquisa)** — a tensão de exploração pré-problema foi resolvida; permanece `PARCIAL` porque a inferência estatística como evidência (descoberta 3) segue aberta.
- **CASO 11 (Livro)** — o stress era o escopo da estética; resolvido pela nota `P-12`. **PARCIAL → PASSA.**
- **CASO 16 (Filme)** — idem. **PARCIAL → PASSA.**
- **17 casos PASSA da Rodada 1** — re-testados contra as emendas; nenhuma emenda altera os critérios que os tornaram conformes. **Zero regressões.**

**Novo placar: 19 PASSA, 1 PARCIAL (Pesquisa), 0 NÃO PASSA.**

---

## 6. Rodada 3 — Validação do par ECP-010 + ECP-100

Requisito da Camada 2 (ROADMAP): o par `ECP-010` (ciclo conceitual) + `ECP-100` (máquina formal) é validado contra pelo menos 3 casos antes de seguir para o Capability Engine.

| Caso | Discovery | Research | Planning | Execution | Validation | Learning | Verdicto na máquina |
|---|---|---|---|---|---|---|---|
| **CASO 1 — ERP** | entendimento do fechamento do caixa; goal `< 15 min` | benchmark + amostra de fechamentos reais | decisão SaaS vs. on-premise; plano | ERP configurado; scripts de migração | 30 dias de fechamentos cronometrados | A-1 invalidada → decisões de layout fiscal reavaliadas (ECP-008; agregação ECP-009.3) | PASSA |
| **CASO 3 — Game Indie** | retenção D1; goal `>= 30%` | playtests com telemetria (protótipo como evidência, nota P-1) | decisão "1 mecânica vs. 3" → 1 | build jogável; trailer | beta fechado com métricas | C-1 parcial → curva de dificuldade ajustada | PASSA |
| **CASO 12 — Hospital** | tempo de espera; goal `< 30 min em 90%` | medições de fluxo; simulação de filas; pilotos | decisão "triagem vs. contratar" → triagem (com campo `autoridade` — RNF-2) | protocolo de triagem; sistema de priorização | medição contínua por 60 dias | A-1 parcial → campeões clínicos (hierarquia registrada, validação no ECP-400) | PASSA |

**Conclusão da Rodada 3:** os 3 casos atravessam o ciclo em todos os seis estados e cumprem as regras da máquina formal — autoridade registrada (ECP-100.1), gatilhos externos como reavaliação (ECP-100.2) e decisão sob incerteza (ECP-100.3, aplicável ao CASO 10 em rodada futura). **Zero regressões** em relação à Rodada 2. Invariantes preservados: `INV-1` (Planning exige Decision Record com goal/problem), `INV-2` (toda transição tem decisão), `INV-7` (Execution exige `artifacts_traceable`).

---

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 0.3.0 | 2026-08-02 | Rodada 3: validação do par ECP-010 + ECP-100 contra CASOS 1 (ERP), 3 (Game), 12 (Hospital); 3/3 PASSA na máquina formal; zero regressões; invariantes preservados. |
| 0.2.0 | 2026-08-02 | Rodada 2: fechamento das descobertas contra as emendas; Livro e Filme PARCIAL → PASSA; placar corrigido (17 PASSA na R1) e final (19 PASSA, 1 PARCIAL); zero regressões. |
| 0.1.0 | 2026-08-02 | Rodada 1: 20 casos de domínios diversos; 17 PASSA, 3 PARCIAL, 0 NÃO PASSA; 7 descobertas alimentando a fundação. |
