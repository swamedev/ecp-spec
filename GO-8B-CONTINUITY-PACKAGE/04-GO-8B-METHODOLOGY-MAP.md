# GO-8B — METHODOLOGY MAP

## Experimental unit

BIP/Caso.

N = número de BIPs válidos.
Seeds são repetições intra-unidade, não unidades independentes.

## Conditions

A = cega pura
B = cega + C3
C = não-cega

## Seeds

3 seeds por (BIP × condição).
Cell value = mediana das 3 seeds.

## Primary metric

S_struct.

Structural graph anonymization:
- node labels = neutral;
- edge labels = in/out;
- sem nomes/mappings/leis/penalidades ECP.

## Secondary metric

S_sem:
- contínua;
- embeddings somente neste eixo;
- sem hard constraint;
- exploratória.

## Kernel combination

K com α=0.6.

## C2/C3

Namespaces:
- C1 → ECP
- C2 → CAT
- C3 → SYN
- C4 → NULL

Sem equivalência/mapping automático:
CAT↔SYN, SYN↔ECP, ECP↔CAT.

## Statistics

Primary:
Friedman, df=2, α=0.05.

Post-hoc:
Wilcoxon signed-rank bilateral + Holm-Bonferroni.

Effects:
Kendall W, rank-biserial r, Cliff δ.

Bootstrap:
B=10.000, com IC exato da mediana ao lado do percentil quando aplicável.

TOST:
não vigente; Δ não aprovada.

## Power

R5:
S1_PRIMARY = (0.50, 0.60, 0.66)
N=7 ≈ 0.63
N=12 ≈ 0.90
N=10 ≈ 0.80

O piloto segue N=7 conforme decisão R5-GOV-01.
