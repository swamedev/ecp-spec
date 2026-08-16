# BIP-022 — Boeing 737 MAX: Atomic Facts (Condições A/B)

**Condições:** A — cega pura (somente este arquivo); B — cega + C3 (este arquivo + `C3_TAXONOMY.yaml`).
**Uso:** Entrada das reconstruções cegas; **zero termos ECP**; **fatos mínimos atômicos**, sem interpretação, sem taxonomia.
**Fontes efetivas:** `house-ti-737max`, `ntsb-asr1901`.
**Rastreabilidade:** cada fato termina com referência entre colchetes.

---

## Fatos

1. Em 2011, para competir com o Airbus A320neo, a Boeing escolheu modificar o 737 NG em vez de criar uma nova aeronave, dando origem ao 737 MAX. `[house-ti-737max]`
2. O 737 MAX 8 é um derivado do 737-800 da família NG. `[ntsb-asr1901]`
3. O 737 MAX 8 incorporou o motor CFM LEAP-1B. `[ntsb-asr1901]`
4. O motor LEAP-1B tem ventoinha de diâmetro maior e nacela reprojetada. `[ntsb-asr1901]`
5. Os testes e a análise da Boeing indicaram que as mudanças do motor produziam um momento de nariz para cima em AOA elevado e números Mach intermediários. `[ntsb-asr1901]`
6. A Boeing implementou mudanças aerodinâmicas para tratar o momento de nariz para cima. `[ntsb-asr1901]`
7. O MCAS foi uma função de aumento de estabilidade estendida do sistema de trim de velocidade do 737 MAX. `[ntsb-asr1901]`
8. O MCAS foi criado para tratar de dificuldades de estabilidade em certas condições de voo provocadas pelos motores maiores. `[house-ti-737max]`
9. Na versão original, o MCAS operava apenas em voo manual, sem piloto automático. `[ntsb-asr1901]`
10. Na versão original, o MCAS operava apenas com os flaps totalmente recolhidos. `[ntsb-asr1901]`
11. O MCAS ativava quando o valor de AOA ultrapassava um limite baseado no número Mach. `[ntsb-asr1901]`
12. O MCAS usava o valor de AOA medido por um dos dois sensores. `[ntsb-asr1901]`
13. Ao ativar, o MCAS comandava o estabilizador horizontal a mover o nariz da aeronave para baixo. `[ntsb-asr1901]`
14. Quando o AOA voltava abaixo do limite, o MCAS movia o estabilizador de volta à posição original. `[ntsb-asr1901]`
15. Os pilotos podiam interromper o movimento do estabilizador usando os interruptores de trim do estabilizador. `[ntsb-asr1901]`
16. Se a condição de AOA elevado persistisse, o MCAS comandava novo movimento de nariz para baixo 5 segundos após o uso dos interruptores. `[ntsb-asr1901]`
17. Na versão inicial, o MCAS tinha autoridade máxima de 0,6 grau no estabilizador. `[house-ti-737max]`
18. Na versão inicial, o MCAS ativava apenas em condições de voo pouco usuais. `[house-ti-737max]`
19. Se o sensor em uso falhasse e indicasse AOA elevado de forma errônea, o MCAS ativava repetidamente. `[house-ti-737max]`
20. Os comandos repetidos do MCAS mantinham o nariz para baixo enquanto o piloto não soubesse como desativar o sistema. `[house-ti-737max]`
21. Os interruptores STAB TRIM CUTOUT cortavam a alimentação elétrica do comando que o MCAS ativava erroneamente. `[house-ti-737max]`
22. Cada 737 MAX tem dois sensores AOA, um de cada lado da dianteira. `[house-ti-737max]`
23. O MCAS foi concebido para usar dados de apenas um sensor AOA por vez. `[house-ti-737max]`
24. O MCAS alternava entre o sensor AOA esquerdo e o direito a cada voo. `[house-ti-737max]`
25. O projeto do MCAS tornava o sistema de comando de voo vulnerável a uma falha única de um sensor AOA. `[house-ti-737max]`
26. O relatório final da investigação indonésia registrou que o projeto apoiado em um único sensor tornava o sistema suscetível a uma falha única. `[house-ti-737max]`
27. A falha única era iniciada por uma alta tendência de leitura do sensor AOA. `[house-ti-737max]`
28. Em 17 de dezembro de 2015, um engenheiro da Boeing perguntou se o MCAS era vulnerável a falhas de um único sensor AOA. `[house-ti-737max]`
29. O relato desse engenheiro mostrou-se posteriormente preciso. `[house-ti-737max]`
30. Dados errôneos de AOA ativaram o MCAS nos dois voos acidentados. `[house-ti-737max]`
31. O MCAS do avião-tanque KC-46 usa dados de dois sensores AOA. `[house-ti-737max]`
32. No KC-46, o MCAS movia o estabilizador apenas uma vez por ativação. `[house-ti-737max]`
33. No KC-46, o MCAS tinha autoridade limitada para empurrar o nariz para baixo. `[house-ti-737max]`
34. No KC-46, os pilotos podiam desativar o MCAS puxando o manche. `[house-ti-737max]`
35. Em 28 de outubro de 2018, um mecânico em Denpasar substituiu o sensor AOA esquerdo da aeronave do voo 610. `[house-ti-737max]`
36. O novo sensor era um sensor reformado previamente usado em um 737-900ER da Malindo Air. `[house-ti-737max]`
37. O sensor reformado foi reconstruído pela Xtra Aerospace. `[house-ti-737max]`
38. No voo de Denpasar para Jacarta, o MCAS ativou a partir de leitura errônea do novo sensor. `[house-ti-737max]`
39. No voo de Denpasar, os pilotos lutavam para estabilizar a aeronave. `[house-ti-737max]`
40. Um terceiro piloto no assento da cabine reconheceu o que ocorria. `[house-ti-737max]`
41. O terceiro piloto instruiu os dois pilotos a acionar os interruptores STAB TRIM CUTOUT. `[house-ti-737max]`
42. A tripulação recuperou o controle e pousou em segurança em Jacarta. `[house-ti-737max]`
43. Ao aterrissar, o capitão registrou no diário de manutenção avisos e alertas do voo. `[house-ti-737max]`
44. O capitão não relatou o uso dos interruptores de corte do estabilizador. `[house-ti-737max]`
45. O DFDR do voo anterior registrou diferença de cerca de 20° entre os sensores AOA esquerdo e direito durante toda a gravação. `[ntsb-asr1901]`
46. No voo anterior, o agitador do manche esquerdo esteve ativo. `[ntsb-asr1901]`
47. No voo anterior, os valores de velocidade e altitude divergiam entre os lados esquerdo e direito. `[ntsb-asr1901]`
48. Após o recolhimento dos flaps, houve uma entrada automática de nariz para baixo no voo anterior. `[ntsb-asr1901]`
49. A tripulação do voo anterior conteve a entrada com trim elétrico de nariz para cima. `[ntsb-asr1901]`
50. O capitão do voo anterior levou os interruptores STAB TRIM CUTOUT para CUTOUT. `[ntsb-asr1901]`
51. O capitão restaurou os interruptores para NORMAL, e a condição reapareceu. `[ntsb-asr1901]`
52. O capitão levou novamente os interruptores para CUTOUT. `[ntsb-asr1901]`
53. A tripulação do voo anterior executou três listas de verificação não normais. `[ntsb-asr1901]`
54. A tripulação do voo anterior continuou o voo com trim manual até o pouso. `[ntsb-asr1901]`
55. Em 29 de outubro de 2018, o voo 610 da Lion Air caiu no Mar de Java. `[ntsb-asr1901]`
56. O voo 610 decolou do aeroporto Soekarno-Hatta, em Jacarta. `[ntsb-asr1901]`
57. A aeronave do voo 610 era um Boeing 737 MAX 8 com matrícula PK-LQP. `[ntsb-asr1901]`
58. O voo 610 caiu logo após a decolagem. `[ntsb-asr1901]`
59. Todos os 189 passageiros e tripulantes do voo 610 morreram. `[ntsb-asr1901]`
60. A aeronave do voo 610 foi destruída. `[ntsb-asr1901]`
61. O DFDR do voo 610 registrou diferença entre os sensores AOA esquerdo e direito durante todo o voo. `[ntsb-asr1901]`
62. No voo 610, o sensor AOA esquerdo ficou cerca de 20° acima do direito. `[ntsb-asr1901]`
63. Durante a rotação do voo 610, o agitador do manche esquerdo ativou. `[ntsb-asr1901]`
64. No voo 610, a velocidade e a altitude do lado esquerdo divergiam dos valores do lado direito. `[ntsb-asr1901]`
65. Após o recolhimento total dos flaps, ocorreu uma entrada automática de nariz para baixo de 10 segundos. `[ntsb-asr1901]`
66. A tripulação do voo 610 respondeu com trim elétrico de nariz para cima. `[ntsb-asr1901]`
67. Nas cerca de 6 minutos seguintes ocorreram mais de 20 entradas automáticas de nariz para baixo. `[ntsb-asr1901]`
68. Cada entrada automática foi contida com trim elétrico até o fim. `[ntsb-asr1901]`
69. As últimas entradas automáticas do voo 610 não foram totalmente contidas. `[ntsb-asr1901]`
70. O sensor AOA forneceu informações imprecisas ao computador de comando de voo do voo 610. `[house-ti-737max]`
71. O MCAS ativou mais de 20 vezes no voo 610. `[house-ti-737max]`
72. A nova tripulação do voo 610 não dispunha da informação sobre o uso dos interruptores de corte. `[house-ti-737max]`
73. A cabine do voo 610 apresentou uma profusão de avisos e alertas. `[house-ti-737max]`
74. O estabilizador forçou a aeronave do voo 610 a uma atitude de nariz para baixo. `[house-ti-737max]`
75. Os pilotos do voo 610 não conseguiram se recuperar do mergulho. `[house-ti-737max]`
76. Em 10 de março de 2019, o voo 302 da Ethiopian Airlines caiu perto de Ejere, na Etiópia. `[ntsb-asr1901]`
77. O voo 302 decolou do aeroporto de Addis Ababa. `[ntsb-asr1901]`
78. A aeronave do voo 302 era um Boeing 737 MAX 8 com matrícula ET-AVJ. `[ntsb-asr1901]`
79. Todos os 157 passageiros e tripulantes do voo 302 morreram. `[ntsb-asr1901]`
80. A aeronave do voo 302 foi destruída. `[ntsb-asr1901]`
81. Logo após a decolagem, o sensor AOA esquerdo do voo 302 subiu rapidamente para 74,5°. `[ntsb-asr1901]`
82. O sensor AOA esquerdo do voo 302 ficou 59,2° acima do direito. `[ntsb-asr1901]`
83. O agitador do manche do capitão do voo 302 ativou. `[ntsb-asr1901]`
84. No voo 302, os valores de velocidade e altitude do lado esquerdo divergiram dos do direito. `[ntsb-asr1901]`
85. No voo 302 houve um alerta Master Caution. `[ntsb-asr1901]`
86. Após o recolhimento dos flaps, ocorreu uma entrada automática de nariz para baixo de 9 segundos no voo 302. `[ntsb-asr1901]`
87. O capitão do voo 302, que pilotava, aplicou trim elétrico de nariz para cima. `[ntsb-asr1901]`
88. Seguiram-se novas entradas automáticas de nariz para baixo no voo 302. `[ntsb-asr1901]`
89. A tripulação do voo 302 discutiu os interruptores STAB TRIM CUTOUT. `[ntsb-asr1901]`
90. Os registros indicam que os interruptores do voo 302 foram levados para CUTOUT. `[ntsb-asr1901]`
91. A aeronave do voo 302 permaneceu fora de compensação com nariz para baixo. `[ntsb-asr1901]`
92. A tripulação do voo 302 precisou aplicar força contínua de nariz para cima. `[ntsb-asr1901]`
93. Cerca de 32 segundos antes do impacto ocorreram breves comandos elétricos de nariz para cima. `[ntsb-asr1901]`
94. Cinco segundos depois, ocorreu outra entrada automática de nariz para baixo. `[ntsb-asr1901]`
95. A aeronave do voo 302 começou a descer o nariz. `[ntsb-asr1901]`
96. O MCAS ativou quatro vezes no voo 302. `[house-ti-737max]`
97. As ativações do MCAS no voo 302 ocorreram por causa de leituras falsas de AOA. `[house-ti-737max]`
98. A aeronave do voo 302 não apresentava dificuldades técnicas conhecidas antes daquele voo. `[house-ti-737max]`
99. Em março de 2016, pilotos de ensaio constataram que o 737 MAX não se comportava bem perto do estol em baixas velocidades. `[house-ti-737max]`
100. A Boeing redesenhou o MCAS em março de 2016. `[house-ti-737max]`
101. O redesenho fez o MCAS ativar em velocidades menores. `[house-ti-737max]`
102. O redesenho aumentou a autoridade máxima do estabilizador de 0,6 grau para 2,5 graus. `[house-ti-737max]`
103. A aprovação do redesenho foi dada pelo gerente-geral do programa, Keith Leverkuhn. `[house-ti-737max]`
104. A aprovação do redesenho foi dada pelo engenheiro-chefe do programa, Michael Teal. `[house-ti-737max]`
105. O redesenho atendeu a requisitos de características de estol necessários à certificação pela FAA. `[house-ti-737max]`
106. Depois do redesenho, a Boeing não reavaliou o sistema. `[house-ti-737max]`
107. Depois do redesenho, a Boeing não executou novas análises de falha única e múltipla do MCAS. `[house-ti-737max]`
108. As ativações repetidas do estabilizador nos voos 610 e 302 violaram requisitos internos de projeto do MCAS da própria Boeing. `[house-ti-737max]`
109. As ativações repetidas colocaram as duas aeronaves em mergulhos dos quais não houve recuperação. `[house-ti-737max]`
110. Em junho de 2016, um voo de ensaio apresentou MCAS contrariando as tentativas do piloto de compensar a aeronave. `[house-ti-737max]`
111. Após esse voo de ensaio, um Representante Autorizado levantou preocupações sobre leituras errôneas de AOA. `[house-ti-737max]`
112. As preocupações desse Representante Autorizado foram desconsideradas pelos colegas. `[house-ti-737max]`
113. Um dos colegas respondeu que não considerava o evento um tema de segurança. `[house-ti-737max]`
114. Em junho de 2013, funcionários da Boeing formularam um plano para descrever o MCAS como uma adição ao sistema de trim de velocidade existente. `[house-ti-737max]`
115. A finalidade do plano era evitar maior impacto de certificação. `[house-ti-737max]`
116. A finalidade do plano era evitar maior impacto de treinamento de pilotos. `[house-ti-737max]`
117. Em março de 2016, a Boeing pediu a remoção de referências ao MCAS do FCOM. `[house-ti-737max]`
118. Em março de 2016, a Boeing pediu a remoção de referências ao MCAS dos materiais de treinamento. `[house-ti-737max]`
119. A remoção das referências ocorreu poucas horas após a aprovação do redesenho. `[house-ti-737max]`
120. A FAA aprovou a remoção das referências ao MCAS. `[house-ti-737max]`
121. Os pilotos do 737 MAX ficaram sem saber da existência do MCAS. `[house-ti-737max]`
122. Os pilotos do 737 MAX ficaram sem saber do possível efeito do MCAS no manuseio da aeronave. `[house-ti-737max]`
123. O relatório final indonésio apontou que, sem saber da existência da função, a tripulação poderia reconhecer uma ativação do MCAS como entrada do sistema de trim de velocidade. `[house-ti-737max]`
124. O MCAS se comporta de modo diferente do sistema de trim de velocidade. `[house-ti-737max]`
125. O MCAS move o estabilizador mais rapidamente do que o sistema de trim de velocidade. `[house-ti-737max]`
126. A Boeing não compartilhou com a FAA os dados de ensaio sobre a resposta de 10 segundos. `[house-ti-737max]`
127. A Boeing não compartilhou com seus clientes os dados de ensaio sobre a resposta de 10 segundos. `[house-ti-737max]`
128. A Boeing não compartilhou com os pilotos os dados de ensaio sobre a resposta de 10 segundos. `[house-ti-737max]`
129. Um piloto de ensaio da Boeing levou mais de 10 segundos para responder a uma ativação não comandada do MCAS em simulador. `[house-ti-737max]`
130. O piloto de ensaio considerou a condição catastrófica. `[house-ti-737max]`
131. A primeira referência à resposta de 10 segundos encontrada pelo Comitê data de 1º de novembro de 2012. `[house-ti-737max]`
132. A orientação federal presume que os pilotos respondem a um estabilizador em fuga em quatro segundos. `[house-ti-737max]`
133. A FAA certificou o 737 MAX como seguro para voar em março de 2017. `[house-ti-737max]`
134. O 737 MAX foi certificado sob certificação de tipo alterado. `[house-ti-737max]`
135. O 737 MAX não foi obrigado a atender vários requisitos mais novos. `[house-ti-737max]`
136. Os procedimentos da FAA para certificação de tipo exigem que o fabricante demonstre a conformidade do projeto com os regulamentos aplicáveis. `[ntsb-asr1901]`
137. Para aeronaves de categoria de transporte, a demonstração deve atender aos requisitos do Título 14 do CFR, Parte 25. `[ntsb-asr1901]`
138. A Parte 25 inclui o 14 CFR 25.671, relativo a sistemas de comando. `[ntsb-asr1901]`
139. A Parte 25 inclui o 14 CFR 25.672, relativo a sistemas de aumento de estabilidade. `[ntsb-asr1901]`
140. Sob o programa ODA, a FAA delega a fabricantes a execução de atividades de certificação. `[house-ti-737max]`
141. Os Representantes Autorizados são funcionários da Boeing autorizados a atuar em nome da agência. `[house-ti-737max]`
142. O escritório BASOO da FAA, em Seattle, delegou à Boeing as ações de certificação relativas ao MCAS. `[house-ti-737max]`
143. Quando a Boeing redesenhou o MCAS em 2016, não atualizou os planos de certificação. `[house-ti-737max]`
144. A Boeing não informou o BASOO sobre o redesenho. `[house-ti-737max]`
145. Os funcionários do BASOO só souberam do redesenho após a queda do voo 610. `[house-ti-737max]`
146. Os pilotos de ensaio do ACO de Seattle souberam do redesenho. `[house-ti-737max]`
147. Os pilotos de ensaio do ACO souberam do redesenho porque afetava os ensaios. `[house-ti-737max]`
148. Os pilotos de ensaio do ACO não compartilharam a informação com outros escritórios. `[house-ti-737max]`
149. O AEG, responsável pelos requisitos de treinamento, permaneceu sem saber até depois do acidente. `[house-ti-737max]`
150. A FAA não classificou o MCAS como sistema crítico de segurança. `[house-ti-737max]`
151. A classificação de sistema crítico de segurança teria atraído maior escrutínio durante a certificação. `[house-ti-737max]`
152. Em maio de 2019, o administrador interino da FAA, Dan Elwell, reconheceu que o MCAS não foi classificado como sistema crítico de segurança. `[house-ti-737max]`
153. O inspetor-geral do DOT registrou que a Boeing apresentou o software como modificação do sistema de trim de velocidade. `[house-ti-737max]`
154. A Boeing apresentou o software como função que ativaria apenas em condições limitadas. `[house-ti-737max]`
155. O MCAS não foi uma área de ênfase nos esforços de certificação. `[house-ti-737max]`
156. O alerta AOA Disagree tinha a finalidade de avisar a tripulação quando as leituras dos dois sensores AOA divergissem. `[house-ti-737max]`
157. O alerta AOA Disagree foi concebido como item padrão em todas as aeronaves 737 MAX. `[house-ti-737max]`
158. Em julho de 2015, uma atualização de software da fornecedora Collins vinculou a exibição do alerta AOA Disagree à exibição opcional do Indicador AOA. `[house-ti-737max]`
159. Depois da atualização, o alerta AOA Disagree passou a funcionar apenas em aeronaves com o Indicador AOA opcional. `[house-ti-737max]`
160. O alerta AOA Disagree ficou inoperante em mais de 80% da frota entregue. `[house-ti-737max]`
161. A Boeing tomou ciência em agosto de 2017 de que o alerta só funcionava com o indicador opcional. `[house-ti-737max]`
162. A Boeing adiou a correção do alerta. `[house-ti-737max]`
163. A Boeing não informou a FAA sobre o mau funcionamento do alerta. `[house-ti-737max]`
164. A Boeing não informou seus clientes sobre o mau funcionamento do alerta. `[house-ti-737max]`
165. A aeronave do voo 610 não tinha o Indicador AOA opcional. `[house-ti-737max]`
166. O alerta AOA Disagree não funcionava na aeronave do voo 610. `[house-ti-737max]`
167. A tripulação do voo 610 não sabia que o alerta não funcionava. `[house-ti-737max]`
168. Se o alerta funcionasse, teria indicado a diferença significativa entre os dois sensores no voo 610. `[house-ti-737max]`
169. Nos três voos, as leituras errôneas do sensor AOA ativaram o agitador do manche. `[ntsb-asr1901]`
170. Nos três voos, as leituras errôneas ativaram os alertas IAS DISAGREE e ALT DISAGREE. `[ntsb-asr1901]`
171. Os múltiplos alertas e indicações aumentaram a carga de trabalho das tripulações. `[ntsb-asr1901]`
172. A combinação de alertas não levou os pilotos dos voos acidentados a executar imediatamente o procedimento de estabilizador em fuga durante a primeira entrada automática. `[ntsb-asr1901]`
173. O NTSB atuou como autoridade de investigação do país de projeto e fabricação da aeronave. `[ntsb-asr1901]`
174. O NTSB examinou o processo de certificação de projeto usado para aprovar o projeto original do MCAS. `[ntsb-asr1901]`
175. Após o acidente do voo 610, a Boeing desenvolveu uma atualização de software do MCAS. `[ntsb-asr1901]`
176. A atualização de software acrescentou camadas de proteção ao MCAS. `[ntsb-asr1901]`
177. Nos testes em simulador da avaliação de segurança, a entrada do estabilizador foi induzida. `[ntsb-asr1901]`
178. Os testes não simularam os efeitos adicionais na cabine decorrentes da mesma falha de origem. `[ntsb-asr1901]`
179. Os efeitos não simulados incluíram os alertas IAS DISAGREE e ALT DISAGREE. `[ntsb-asr1901]`
180. Os efeitos não simulados incluíram o agitador do manche. `[ntsb-asr1901]`
181. O NTSB concluiu que as premissas da Boeing na avaliação funcional de perigos do MCAS não levaram em conta adequadamente o efeito de múltiplos alertas. `[ntsb-asr1901]`
182. Nos três voos, as respostas dos pilotos diferiram das premissas de resposta usadas pela Boeing. `[ntsb-asr1901]`
183. A FAA aprovou e usou as classificações de perigo baseadas nessas premissas. `[ntsb-asr1901]`
184. O NTSB recomendou que a FAA exigisse da Boeing que as avaliações de segurança do 737 MAX considerassem o efeito de todos os alertas possíveis na resposta dos pilotos (A-19-10). `[ntsb-asr1901]`
185. A recomendação A-19-10 incluía incorporar melhorias de projeto, procedimentos e requisitos de treinamento. `[ntsb-asr1901]`
186. O NTSB recomendou estender a exigência a todas as demais aeronaves de categoria de transporte certificadas nos EUA (A-19-11). `[ntsb-asr1901]`
187. O NTSB recomendou notificar outros reguladores internacionais (A-19-12). `[ntsb-asr1901]`
188. O NTSB recomendou desenvolver ferramentas e métodos para avaliar premissas sobre o reconhecimento e a resposta dos pilotos (A-19-13). `[ntsb-asr1901]`
189. O NTSB recomendou revisar os regulamentos e orientações da FAA para incorporar o uso dessas ferramentas (A-19-14). `[ntsb-asr1901]`
190. O NTSB recomendou desenvolver padrões de projeto para ferramentas de diagnóstico (A-19-15). `[ntsb-asr1901]`
191. O NTSB recomendou desenvolver padrões de projeto que melhorem a priorização e a clareza das indicações de falha (A-19-16). `[ntsb-asr1901]`
192. O Comitê identificou pressão financeira intensa sobre o programa 737 MAX para competir com o A320neo. `[house-ti-737max]`
193. Os esforços buscavam cortar custos. `[house-ti-737max]`
194. Os esforços buscavam manter o cronograma do programa. `[house-ti-737max]`
195. Os esforços buscavam evitar requisitos de treinamento em simulador. `[house-ti-737max]`
196. Um cronômetro regressivo instalado em 2012 lembrava os funcionários de manter o cronograma do programa. `[house-ti-737max]`
197. Em junho de 2018, o supervisor Ed Pierson alertou sobre preocupações de segurança na fábrica de Renton. `[house-ti-737max]`
198. Em junho de 2018, o supervisor Ed Pierson alertou sobre pressão de produção na fábrica de Renton. `[house-ti-737max]`
199. Em julho de 2018, Pierson relatou que o gerente-geral respondeu que as Forças Armadas não são uma organização voltada ao lucro. `[house-ti-737max]`
200. A produção continuou a aumentar após os alertas. `[house-ti-737max]`
201. O voo 610 caiu três meses depois dos alertas de Pierson. `[house-ti-737max]`
202. A aeronave do voo 610 foi a 172ª aeronave MAX produzida. `[house-ti-737max]`
203. A aeronave do voo 302 foi a 239ª aeronave MAX produzida. `[house-ti-737max]`
204. Após a queda do voo 302, em 11 de março de 2019, a FAA emitiu notificação de aeronavegabilidade continuada permitindo que o 737 MAX continuasse voando. `[house-ti-737max]`
205. Em 13 de março de 2019, após dados adicionais, a FAA determinou a suspensão da frota 737 MAX. `[house-ti-737max]`
206. China, União Europeia e Canadá suspenderam a frota antes da FAA. `[house-ti-737max]`
207. Na época do acidente do voo 302, a frota do 737 MAX era de 387 aeronaves. `[house-ti-737max]`
208. Na época do acidente do voo 302, a frota do 737 MAX atendia 59 companhias aéreas. `[house-ti-737max]`
209. O relatório final do Comitê conclui que a Boeing e a FAA compartilham a responsabilidade pelo desenvolvimento de uma aeronave insegura. `[house-ti-737max]`
210. O relatório final do Comitê conclui que a Boeing e a FAA compartilham a responsabilidade pela certificação de uma aeronave insegura. `[house-ti-737max]`
211. Os dois acidentes mataram 346 pessoas em menos de cinco meses. `[house-ti-737max]`