# BIP-022 — Boeing 737 MAX: Narrativa (Condição C)

**Condição:** C — não-cega
**Uso:** Entrada da reconstrução não-cega; **zero termos ECP**; linhas em ordem histórica.
**Fontes efetivas:** `house-ti-737max`, `ntsb-asr1901`.
**Rastreabilidade:** o primeiro `ref` após cada parágrafo indica a fonte do fato.

---

## 1. O 737 MAX e a introdução do MCAS

Para enfrentar a concorrência do Airbus A320neo, a Boeing decidiu, em 2011, não criar uma aeronave nova do zero e, em vez disso, modificar o 737 NG existente para torná-lo mais econômico, dando origem ao 737 MAX. `[house-ti-737max]`

O 737 MAX 8 é um derivado do 737-800 da família NG e incorporou o motor CFM LEAP-1B, com ventoinha de diâmetro maior e nacela reprojetada; os testes e a análise da Boeing indicaram que essas mudanças produziam um momento de nariz para cima em AOA elevado e números Mach intermediários, e a empresa implementou mudanças aerodinâmicas e a função de aumento de estabilidade MCAS, como extensão do sistema de trim de velocidade. `[ntsb-asr1901]`

O relatório do Comitê da Câmara dos EUA registra que o MCAS foi criado para tratar de dificuldades de estabilidade em certas condições de voo provocadas pelos motores maiores e por sua posição relativa no 737 MAX. `[house-ti-737max]`

## 2. Como o MCAS operava

Na versão original, o MCAS operava em voo manual, sem piloto automático, com os flaps totalmente recolhidos, quando o valor de AOA medido por um dos dois sensores ultrapassava um limite baseado no número Mach; ao ativar, o MCAS comandava o estabilizador horizontal a mover o nariz da aeronave para baixo e, quando o AOA voltava abaixo do limite, movia o estabilizador de volta à posição original. `[ntsb-asr1901]`

Em qualquer momento, os pilotos podiam interromper ou inverter o movimento usando os interruptores de trim do estabilizador; se a condição de AOA elevado persistisse, o MCAS comandava novo movimento de nariz para baixo 5 segundos após o uso dos interruptores. `[ntsb-asr1901]`

O MCAS se apoiava nos dados de um único sensor AOA por vez, alternando entre o esquerdo e o direito a cada voo; se o sensor em uso falhasse e indicasse AOA elevado de forma errônea, o MCAS ativava repetidamente e mantinha o nariz para baixo enquanto o piloto não soubesse como desativá-lo. Na versão inicial, o MCAS tinha autoridade máxima de 0,6 grau no estabilizador e ativava apenas em condições de voo pouco usuais. `[house-ti-737max]`

## 3. Lion Air — o voo anterior (28 de outubro de 2018)

Na véspera da queda do voo 610, um mecânico em Denpasar, na Indonésia, substituiu o sensor AOA esquerdo da aeronave por um sensor reformado, previamente usado em um 737-900ER da Malindo Air e reconstruído pela Xtra Aerospace. `[house-ti-737max]`

No voo de Denpasar para Jacarta, o MCAS ativou a partir de leitura errônea do novo sensor e comandou o estabilizador a empurrar o nariz para baixo, enquanto os pilotos lutavam para estabilizar a aeronave; um terceiro piloto no assento da cabine reconheceu o que ocorria e instruiu os dois pilotos a acionar os interruptores STAB TRIM CUTOUT, que cortavam a alimentação elétrica do comando que o MCAS ativava erroneamente, permitindo recuperar o controle e pousar em segurança. Ao aterrissar, o capitão registrou no diário de manutenção alguns avisos e alertas do voo, mas não relatou o uso dos interruptores de corte do estabilizador. `[house-ti-737max]`

Segundo o NTSB, o registrador de dados de voo (DFDR) desse voo anterior registrou a mesma diferença de cerca de 20° entre os sensores AOA esquerdo e direito durante toda a gravação, com o agitador do manche esquerdo ativo e valores de velocidade e altitude divergentes; após o recolhimento dos flaps, houve uma entrada automática de nariz para baixo, e a tripulação a conteve com trim elétrico de nariz para cima, até notar que a aeronave estava se compensando automaticamente para baixo; o capitão levou os interruptores STAB TRIM CUTOUT para CUTOUT, depois os restaurou para NORMAL, com a condição reaparecendo, e então os levou novamente para CUTOUT; a tripulação executou três listas de verificação não normais e continuou o voo com trim manual até o pouso. `[ntsb-asr1901]`

## 4. Lion Air — voo 610 (29 de outubro de 2018)

Em 29 de outubro de 2018, o voo 610 da Lion Air, um Boeing 737 MAX 8 (PK-LQP), caiu no Mar de Java logo após decolar do aeroporto Soekarno-Hatta, em Jacarta; todos os 189 passageiros e tripulantes morreram, e a aeronave foi destruída. `[ntsb-asr1901]`

O DFDR registrou diferença entre os sensores AOA esquerdo e direito durante todo o voo, com o esquerdo cerca de 20° acima do direito; durante a rotação, o agitador do manche esquerdo ativou, e a velocidade e a altitude do lado esquerdo divergiam dos valores do lado direito; após o recolhimento total dos flaps, ocorreu uma entrada automática de nariz para baixo de 10 segundos, seguida de trim elétrico de nariz para cima pela tripulação, e nas cerca de 6 minutos seguintes ocorreram mais de 20 entradas automáticas de nariz para baixo, cada uma contida com trim elétrico, até que as últimas entradas não foram totalmente contidas. `[ntsb-asr1901]`

O relatório do Comitê da Câmara descreve que, no voo 610, o sensor AOA forneceu informações imprecisas ao computador de comando de voo, ativando o MCAS mais de 20 vezes enquanto os pilotos lutavam para manter o controle; como a tripulação anterior não registrou o uso dos interruptores de corte, a nova tripulação não dispunha dessa informação; em meio a uma profusão de avisos e alertas, o estabilizador forçou a aeronave a uma atitude de nariz para baixo da qual os pilotos não conseguiram se recuperar. `[house-ti-737max]`

## 5. Ethiopian Airlines — voo 302 (10 de março de 2019)

Em 10 de março de 2019, o voo 302 da Ethiopian Airlines, um Boeing 737 MAX 8 (ET-AVJ), caiu perto de Ejere, na Etiópia, logo após decolar do aeroporto de Addis Ababa; todos os 157 passageiros e tripulantes morreram, e a aeronave foi destruída; o DFDR indicou que, logo após a decolagem, o sensor AOA esquerdo subiu rapidamente para 74,5°, 59,2° acima do direito, o agitador do manche do capitão ativou, os valores de velocidade e altitude do lado esquerdo divergiram dos do direito, e houve um alerta Master Caution. `[ntsb-asr1901]`

Como no voo 610, após o recolhimento dos flaps e em voo manual, ocorreu uma entrada automática de nariz para baixo de 9 segundos; o capitão, que pilotava, aplicou trim elétrico de nariz para cima; seguiram-se novas entradas automáticas, e a tripulação discutiu os interruptores STAB TRIM CUTOUT, cujos registros indicam que foram levados para CUTOUT; como a aeronave permaneceu fora de compensação com nariz para baixo, a tripulação precisou aplicar força contínua de nariz para cima; cerca de 32 segundos antes do impacto ocorreram breves comandos elétricos de nariz para cima e, 5 segundos depois, outra entrada automática de nariz para baixo, e a aeronave começou a descer o nariz. `[ntsb-asr1901]`

O relatório do Comitê da Câmara registra que, nos cerca de seis minutos de voo, o MCAS ativou quatro vezes por causa das leituras falsas de AOA, e que a aeronave não apresentava dificuldades técnicas conhecidas antes daquele voo. `[house-ti-737max]`

## 6. O MCAS e os sensores de AOA

Cada 737 MAX tem dois sensores AOA, um de cada lado da dianteira; o MCAS, porém, foi concebido para usar dados de apenas um sensor por vez, o que tornava o sistema de comando de voo vulnerável a uma falha única de um sensor AOA. O relatório final da investigação indonésia sobre o voo 610 registra que esse projeto apoiado em um único sensor tornou o sistema suscetível a uma falha única, iniciada por uma alta tendência de leitura do sensor. `[house-ti-737max]`

Em 17 de dezembro de 2015, um engenheiro da Boeing que também era Representante Autorizado perguntou, em mensagem interna, se o MCAS era vulnerável a falhas de um único sensor AOA; o relato mostrou-se posteriormente preciso, pois dados errôneos de AOA ativaram o MCAS nos dois voos acidentados. `[house-ti-737max]`

O MCAS do avião-tanque KC-46, da Força Aérea dos EUA, usa dados de dois sensores AOA; nele, o MCAS movia o estabilizador apenas uma vez por ativação, com autoridade limitada para empurrar o nariz para baixo, e os pilotos podiam desativá-lo puxando o manche. `[house-ti-737max]`

## 7. O redesenho do MCAS em março de 2016

Em março de 2016, após pilotos de ensaio constatarem que o 737 MAX não se comportava bem perto do estol em baixas velocidades, a Boeing redesenhou o MCAS para ativar em velocidades menores e aumentou a autoridade máxima do estabilizador de 0,6 grau para 2,5 graus. `[house-ti-737max]`

A aprovação do redesenho foi dada pelo gerente-geral do programa, Keith Leverkuhn, e pelo engenheiro-chefe do programa, Michael Teal, para atender a requisitos de características de estol necessários à certificação pela FAA; depois do redesenho, a Boeing não reavaliou o sistema nem executou novas análises de falha única e múltipla do MCAS. `[house-ti-737max]`

As ativações repetidas do estabilizador nos voos 610 e 302 colocaram as duas aeronaves em mergulhos dos quais não houve recuperação, o que violou requisitos internos de projeto do MCAS da própria Boeing; em junho de 2016, após um voo de ensaio em que o MCAS contrariou as tentativas do piloto de compensar a aeronave, um Representante Autorizado levantou preocupações sobre leituras errôneas de AOA, e as preocupações foram desconsideradas pelos colegas, um dos quais respondeu que não considerava o evento um tema de segurança. `[house-ti-737max]`

## 8. A não divulgação do MCAS

Em junho de 2013, funcionários da Boeing formularam um plano para descrever o MCAS como uma adição ao sistema de trim de velocidade existente, com a finalidade de evitar maior impacto de certificação e de treinamento de pilotos; em março de 2016, poucas horas após a aprovação do redesenho, a Boeing pediu e a FAA aprovou a remoção de referências ao MCAS do Flight Crew Operations Manual (FCOM) e dos materiais de treinamento. `[house-ti-737max]`

Como resultado, os pilotos do 737 MAX ficaram sem saber da existência do MCAS e de seu possível efeito no manuseio da aeronave sem comando do piloto; o relatório final indonésio sobre o voo 610 apontou que, sem saber da existência da função, a tripulação poderia reconhecer uma ativação do MCAS como entrada do sistema de trim de velocidade, embora o MCAS se comporte de modo diferente, movendo o estabilizador mais rapidamente. `[house-ti-737max]`

A Boeing também não compartilhou com a FAA, com seus clientes nem com os pilotos os dados de ensaio que mostravam que um piloto de ensaio da própria empresa levou mais de 10 segundos para responder a uma ativação não comandada do MCAS em simulador, condição que esse piloto considerou catastrófica; a primeira referência a essa resposta de 10 segundos encontrada pelo Comitê data de 1º de novembro de 2012, e a orientação federal presume que os pilotos respondem a um estabilizador em fuga em quatro segundos. `[house-ti-737max]`

## 9. Certificação, delegação e supervisão da FAA

A FAA certificou o 737 MAX como seguro para voar em março de 2017; a aeronave foi certificada sob certificação de tipo alterado, não sendo obrigada a atender vários requisitos mais novos. `[house-ti-737max]`

Os procedimentos da FAA para certificação de tipo exigem que o fabricante demonstre a conformidade do projeto com os regulamentos aplicáveis; para aeronaves de categoria de transporte, a demonstração deve atender aos requisitos do Título 14 do CFR, Parte 25, incluindo o 14 CFR 25.671 e o 14 CFR 25.672, relativos a sistemas de comando e a sistemas de aumento de estabilidade. `[ntsb-asr1901]`

Sob o programa ODA, a FAA delega a fabricantes a execução de atividades de certificação, e os Representantes Autorizados são funcionários da Boeing autorizados a atuar em nome da agência; o escritório BASOO da FAA, em Seattle, delegou à Boeing as ações de certificação relativas ao MCAS, e, quando a Boeing redesenhou o MCAS em 2016, não atualizou os planos de certificação nem informou o BASOO, cujos funcionários só souberam do redesenho após a queda do voo 610; os pilotos de ensaio do ACO de Seattle souberam do redesenho, pois afetava os ensaios, mas não compartilharam a informação com outros escritórios, e o AEG, responsável pelos requisitos de treinamento, permaneceu sem saber até depois do acidente. `[house-ti-737max]`

A FAA não classificou o MCAS como sistema crítico de segurança, o que teria atraído maior escrutínio durante a certificação; em maio de 2019, o então administrador interino da FAA, Dan Elwell, reconheceu esse ponto; o inspetor-geral do DOT registrou que a Boeing apresentou o software como modificação do sistema de trim de velocidade que ativaria apenas em condições limitadas, e que o MCAS não foi uma área de ênfase nos esforços de certificação. `[house-ti-737max]`

## 10. Alertas e indicações na cabine

O alerta AOA Disagree tinha a finalidade de avisar a tripulação quando as leituras dos dois sensores AOA divergissem, e foi concebido como item padrão em todas as aeronaves 737 MAX; em julho de 2015, uma atualização de software da fornecedora Collins vinculou a exibição do alerta AOA Disagree à exibição opcional do Indicador AOA, e o alerta passou a funcionar apenas em aeronaves com o indicador opcional, ficando inoperante em mais de 80% da frota entregue. `[house-ti-737max]`

A Boeing tomou ciência em agosto de 2017 de que o alerta só funcionava com o indicador opcional e adiou a correção, sem informar a FAA nem seus clientes; a aeronave do voo 610 não tinha o Indicador AOA opcional, de modo que o alerta AOA Disagree não funcionava, a tripulação não sabia disso, e, se o alerta funcionasse, teria indicado a diferença significativa entre os dois sensores. `[house-ti-737max]`

Nos três voos, as leituras errôneas do sensor AOA ativaram o agitador do manche e os alertas IAS DISAGREE e ALT DISAGREE, e a tripulação do voo 302 recebeu ainda um alerta Master Caution; os múltiplos alertas e indicações aumentaram a carga de trabalho das tripulações, e a combinação de alertas não levou os pilotos dos voos acidentados a executar imediatamente o procedimento de estabilizador em fuga durante a primeira entrada automática de nariz para baixo. `[ntsb-asr1901]`

## 11. Constatações e recomendações do NTSB

O NTSB, na condição de autoridade de investigação do país de projeto e fabricação da aeronave, examinou o processo de certificação de projeto usado para aprovar o projeto original do MCAS no 737 MAX; após o acidente do voo 610, a Boeing desenvolveu uma atualização de software do MCAS para acrescentar camadas de proteção. `[ntsb-asr1901]`

Em sua análise da avaliação de segurança da Boeing para o comando de trim do estabilizador, o NTSB verificou que os testes em simulador induziram a entrada do estabilizador, mas não simularam os efeitos adicionais na cabine, como os alertas IAS DISAGREE e ALT DISAGREE e o agitador do manche, decorrentes da mesma falha de origem; o NTSB concluiu que as premissas usadas pela Boeing na avaliação funcional de perigos do MCAS não levaram em conta adequadamente o efeito de múltiplos alertas e indicações na resposta dos pilotos, e que, nos três voos, as respostas dos pilotos diferiram das premissas de resposta em que a Boeing baseou suas classificações de perigo, que a FAA aprovou e usou. `[ntsb-asr1901]`

O NTSB recomendou que a FAA exigisse da Boeing que as avaliações de segurança do 737 MAX considerassem o efeito de todos os alertas e indicações possíveis na cabine sobre o reconhecimento e a resposta dos pilotos, e que incorporasse melhorias de projeto, procedimentos e requisitos de treinamento (A-19-10); o NTSB também recomendou estender a exigência a todas as demais aeronaves de categoria de transporte certificadas nos EUA (A-19-11), notificar outros reguladores internacionais (A-19-12), desenvolver ferramentas e métodos para avaliar premissas sobre o reconhecimento e a resposta dos pilotos (A-19-13), revisar os regulamentos e orientações da FAA para incorporar o uso dessas ferramentas (A-19-14) e desenvolver padrões de projeto para ferramentas de diagnóstico que melhorem a priorização e a clareza das indicações de falha apresentadas aos pilotos (A-19-15 e A-19-16). `[ntsb-asr1901]`

## 12. Cultura de gestão, pressão de produção e desfecho

O Comitê identificou pressão financeira intensa sobre o programa 737 MAX para competir com o A320neo da Airbus, com esforços para cortar custos, manter o cronograma e evitar requisitos de treinamento em simulador; um cronômetro regressivo instalado em 2012 lembrava os funcionários de manter o cronograma do programa; em junho de 2018, o supervisor Ed Pierson alertou, por mensagem, sobre preocupações de segurança e pressão de produção na fábrica de Renton, e, em julho, Pierson relatou que o gerente-geral respondeu que as Forças Armadas não são uma organização voltada ao lucro. `[house-ti-737max]`

A produção continuou a aumentar, e o voo 610 caiu três meses depois; a aeronave do voo 610 foi a 172ª aeronave MAX produzida, e a do voo 302 foi a 239ª. `[house-ti-737max]`

Após a queda do voo 302, em 11 de março de 2019, a FAA emitiu notificação de aeronavegabilidade continuada permitindo que o 737 MAX continuasse voando; em 13 de março de 2019, após dados adicionais, a FAA determinou a suspensão da frota 737 MAX, seguindo ações já tomadas por China, União Europeia e Canadá, entre outros; na época do acidente do voo 302, a frota do 737 MAX era de 387 aeronaves com 59 companhias aéreas em todo o mundo. `[house-ti-737max]`

O relatório final do Comitê conclui que tanto a Boeing quanto a FAA compartilham a responsabilidade pelo desenvolvimento e pela certificação de uma aeronave insegura, e que os dois acidentes mataram 346 pessoas em menos de cinco meses. `[house-ti-737max]`