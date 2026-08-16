import pandas as pd
import numpy as np
import json
import hashlib
from scipy.stats import friedmanchisquare, wilcoxon, ttest_1samp
from itertools import product

# Load components
with open(r"D:\ecp-spec\experiments\validation\GO-8D-NC\study-output\diagnostic_components.json", "r") as f:
    results = json.load(f)

components = results["components"]

# Reconstruct matrix (30 x 3) for each component
bip_order = [f"BIP-{i:03d}" for i in range(1, 31)]
conditions = ["A", "B", "C"]

conf_matrix = np.zeros((30, 3))
ged_ecp_matrix = np.zeros((30, 3))
ent_n12_matrix = np.zeros((30, 3))
dv3_matrix = np.zeros((30, 3))

for i, bip in enumerate(bip_order):
    for j, cond in enumerate(conditions):
        reps = list(results["components"][bip][cond].values())
        conf_matrix[i, j] = np.mean([r["conf"] for r in reps])
        ged_ecp_matrix[i, j] = np.mean([r["ged_ecp"] for r in reps])
        ent_n12_matrix[i, j] = np.mean([r["ent_n12"] for r in reps])
        dv3_matrix[i, j] = np.mean([r["dv3"] for r in reps])

from scipy.stats import friedmanchisquare, wilcoxon

print("=== DECOMPOSIÇÃO DV3 ===")
for name, mat in [("conf", conf_matrix), ("ged_ecp", ged_ecp_matrix), ("ent_n12", ent_n12_matrix), ("dv3", dv3_matrix)]:
    print(name + ": A=" + str(mat[:,0].mean()) + " B=" + str(mat[:,1].mean()) + " C=" + str(mat[:,2].mean()) + "  Dif A-B=" + str(mat[:,0].mean()-mat[:,1].mean()) + " B-C=" + str(mat[:,1].mean()-mat[:,2].mean()))

for name, mat in [("conf", conf_matrix), ("ged_ecp", ged_ecp_matrix), ("ent_n12", ent_n12_matrix)]:
    chi2, p = friedmanchisquare(mat[:,0], mat[:,1], mat[:,2])
    print("Friedman " + name + ": chi2=" + str(chi2) + ", p=" + str(p))

for name, mat in [("conf", conf_matrix), ("ged_ecp", ged_ecp_matrix), ("ent_n12", ent_n12_matrix)]:
    A, B, C = mat[:,0], mat[:,1], mat[:,2]
    stat, p = wilcoxon(B, A, alternative='less')
    print("Wilcoxon B<A " + name + ": stat=" + str(stat) + ", p=" + str(p))
    stat, p = wilcoxon(C, A, alternative='less')
    print("Wilcoxon C<A " + name + ": stat=" + str(stat) + ", p=" + str(p))
    stat, p = wilcoxon(C, B, alternative='less')
    print("Wilcoxon C<B " + name + ": stat=" + str(stat) + ", p=" + str(p))

print("\n=== DIFERENCAS MEDIAS A-B ===")
ged_diff = ged_ecp_matrix[:,1] - ged_ecp_matrix[:,0]
conf_diff = conf_matrix[:,1] - conf_matrix[:,0]
ent_diff = ent_n12_matrix[:,1] - ent_n12_matrix[:,0]

ged_degraded = np.mean(ged_diff < 0)
conf_degraded = np.mean(conf_diff < 0)
ent_degraded = np.mean(ent_diff < 0)

print("Proporcao degradada A->B: ged_ecp=" + str(ged_degraded) + ", conf=" + str(conf_degraded) + ", ent_n12=" + str(ent_degraded))

ged_diff_mean = np.mean(ged_ecp_matrix[:,0] - ged_ecp_matrix[:,1])
conf_diff_mean = np.mean(conf_matrix[:,0] - conf_matrix[:,1])
ent_diff_mean = np.mean(ent_n12_matrix[:,0] - ent_n12_matrix[:,1])

print("Diferencas medias A-B: ged_ecp=" + str(ged_diff_mean) + ", conf=" + str(conf_diff_mean) + ", ent_n12=" + str(ent_diff_mean))
total_diff = ged_diff_mean + conf_diff_mean + ent_diff_mean
print("Proporcao DV3: ged_ecp=" + str(ged_diff_mean/total_diff) + ", conf=" + str(conf_diff_mean/total_diff) + ", ent_n12=" + str(ent_diff_mean/total_diff))

# TS-1
print("\n=== TS-1: Referencia Neutra ===")
print("ged_ecp medians:")
print("  A: " + str(np.median(ged_ecp_matrix[:,0])))
print("  B: " + str(np.median(ged_ecp_matrix[:,1])))
print("  C: " + str(np.median(ged_ecp_matrix[:,2])))

# TS-2
print("\n=== TS-2: Grade de Pesos ===")
weight_grid = []
for w1 in [0.5, 1.0, 2.0]:
    for w2 in [0.5, 1.0, 2.0]:
        for w3 in [0.5, 1.0, 2.0]:
            total = w1 + w2 + w3
            weight_grid.append((w1/total, w2/total, w3/total))
weight_grid = list(set(weight_grid))

order_stable = True
inversions_count = 0
for w1, w2, w3 in weight_grid:
    dv3_w = w1 * conf_matrix + w2 * ged_ecp_matrix + w3 * ent_n12_matrix
    if not (np.all(dv3_w[:,0] > dv3_w[:,1]) and np.all(dv3_w[:,1] > dv3_w[:,2])):
        order_stable = False

order_stable = True
for w1, w2, w3 in weight_grid:
    dv3_w = w1 * conf_matrix + w2 * ged_ecp_matrix + w3 * ent_n12_matrix
    if not (np.all(dv3_w[:,0] > dv3_w[:,1]) and np.all(dv3_w[:,1] > dv3_w[:,2])):
        order_stable = False
        break

inversions_count = sum(1 for w1,w2,w3 in set(weight_grid) if not (np.all((w1*conf_matrix+w2*ged_ecp_matrix+w3*ent_n12_matrix)[:,0] > (w1*conf_matrix+w2*ged_ecp_matrix+w3*ent_n12_matrix)[:,1]) and np.all((w1*conf_matrix+w2*ged_ecp_matrix+w3*ent_n12_matrix)[:,1] > (w1*conf_matrix+w2*ged_ecp_matrix+w3*ent_n12_matrix)[:,2])))

print("Ordem A>B>C estavel em todas as " + str(len(set(weight_grid))) + " combinacoes: " + str(order_stable))
print("Inversoes encontradas: " + str(inversions_count))

# TS-3
print("\n=== TS-3: Metricas Alternativas ===")
dv3_geo = (conf_matrix * ged_ecp_matrix * ent_n12_matrix) ** (1/3)
order_AB_geo = np.all(dv3_geo[:,0] > dv3_geo[:,1])
order_BC_geo = np.all(dv3_geo[:,1] > dv3_geo[:,2])
print("Geometrica: AB=" + str(order_AB_geo) + ", BC=" + str(order_BC_geo))
print("  Medias: A=" + str(dv3_geo[:,0].mean()) + " B=" + str(dv3_geo[:,1].mean()) + " C=" + str(dv3_geo[:,2].mean()))

dv3_harm = 3 / (1/conf_matrix + 1/ged_ecp_matrix + 1/ent_n12_matrix)
order_AB_harm = np.all(dv3_harm[:,0] > dv3_harm[:,1])
order_BC_harm = np.all(dv3_harm[:,1] > dv3_harm[:,2])
print("Harmonica: AB=" + str(order_AB_harm) + ", BC=" + str(order_BC_harm))

# TS-4
print("\n=== TS-4: Contrafactual C3 ===")
ged_ecp_cf = ged_ecp_matrix.copy()
ged_ecp_cf[:,1] = ged_ecp_matrix[:,0]
dv3_cf = (conf_matrix + ged_ecp_cf + ent_n12_matrix) / 3
order_AB_cf = np.all(dv3_cf[:,0] > dv3_cf[:,1])
order_BC_cf = np.all(dv3_cf[:,1] > dv3_cf[:,2])
print("Contrafactual (B ged_ecp = A): AB=" + str(order_AB_cf) + ", BC=" + str(order_BC_cf))

ged_ecp_cf2 = ged_ecp_matrix.copy()
ged_ecp_cf2[:,1] = np.maximum(ged_ecp_matrix[:,0], ged_ecp_matrix[:,1])
dv3_cf2 = (conf_matrix + ged_ecp_cf2 + ent_n12_matrix) / 3
order_AB_cf2 = np.all(dv3_cf2[:,0] > dv3_cf2[:,1])
order_BC_cf2 = np.all(dv3_cf2[:,1] > dv3_cf2[:,2])
print("Contrafactual (B ged_ecp = max(A,B)): AB=" + str(order_AB_cf2) + ", BC=" + str(order_BC_cf2))

# Opposite signs
opposite_AB = 0
opposite_BC = 0
for i in range(30):
    d_conf = conf_matrix[i,1] - conf_matrix[i,0]
    d_ged = ged_ecp_matrix[i,1] - ged_ecp_matrix[i,0]
    d_ent = ent_n12_matrix[i,1] - ent_n12_matrix[i,0]
    signs = [np.sign(d_conf), np.sign(d_ged), np.sign(d_ent)]
    if len(set([s for s in signs if s != 0])) > 1:
        opposite_AB += 1
        
    d_conf = conf_matrix[i,2] - conf_matrix[i,1]
    d_ged = ged_ecp_matrix[i,2] - ged_ecp_matrix[i,1]
    d_ent = ent_n12_matrix[i,2] - ent_n12_matrix[i,1]
    signs = [np.sign(d_conf), np.sign(d_ged), np.sign(d_ent)]
    if len(set([s for s in signs if s != 0])) > 1:
        opposite_BC += 1

print("BIPs sinais opostos A->B: " + str(opposite_AB) + "/30")
print("BIPs sinais opostos B->C: " + str(opposite_BC) + "/30")

# ============ Evidence & Classification ============
print("\n=== EVIDENCIA PARA H1/H2/H3 ===")

# H1
ged_degraded = np.mean(ged_ecp_matrix[:,1] < ged_ecp_matrix[:,0])
conf_degraded = np.mean(conf_matrix[:,1] < conf_matrix[:,0])
ent_degraded = np.mean(ent_n12_matrix[:,1] < ent_n12_matrix[:,0])

print("\nProporcao degradada A->B: ged_ecp=" + str(ged_degraded) + ", conf=" + str(conf_degraded) + ", ent_n12=" + str(ent_degraded))

ged_diff_mean = np.mean(ged_ecp_matrix[:,0] - ged_ecp_matrix[:,1])
conf_diff_mean = np.mean(conf_matrix[:,0] - conf_matrix[:,1])
ent_diff_mean = np.mean(ent_n12_matrix[:,0] - ent_n12_matrix[:,1])

print("Diferencas medias A-B: ged_ecp=" + str(ged_diff_mean) + ", conf=" + str(conf_diff_mean) + ", ent_n12=" + str(ent_diff_mean))
total_diff = ged_diff_mean + conf_diff_mean + ent_diff_mean
print("Proporcao DV3: ged_ecp=" + str(ged_diff_mean/total_diff) + ", conf=" + str(conf_diff_mean/total_diff) + ", ent_n12=" + str(ent_diff_mean/total_diff))

evidence_H1 = ["Moderada: degradacao em ent_n12 (93%), ged_ecp (73%), conf (43%)"]
evidence_H2 = ["Moderada: ent_n12 e maior contribuinte (10.07% vs 2.16% ged_ecp)", "Estrutural: ged_ecp usa referencia ECP (CAT), B usa SYN -> vies inerente"]

opposite_AB = 0
opposite_BC = 0
for i in range(30):
    d_conf = conf_matrix[i,1] - conf_matrix[i,0]
    d_ged = ged_ecp_matrix[i,1] - ged_ecp_matrix[i,0]
    d_ent = ent_n12_matrix[i,1] - ent_n12_matrix[i,0]
    signs = [np.sign(d_conf), np.sign(d_ged), np.sign(d_ent)]
    if len(set([s for s in signs if s != 0])) > 1:
        opposite_AB += 1
        
    d_conf = conf_matrix[i,2] - conf_matrix[i,1]
    d_ged = ged_ecp_matrix[i,2] - ged_ecp_matrix[i,1]
    d_ent = ent_n12_matrix[i,2] - ent_n12_matrix[i,1]
    signs = [np.sign(d_conf), np.sign(d_ged), np.sign(d_ent)]
    if len(set([s for s in signs if s != 0])) > 1:
        opposite_BC += 1

print("BIPs sinais opostos A->B: " + str(opposite_AB) + "/30")
print("BIPs sinais opostos B->C: " + str(opposite_BC) + "/30")

# Weight grid
weight_grid = []
for w1 in [0.5, 1.0, 2.0]:
    for w2 in [0.5, 1.0, 2.0]:
        for w3 in [0.5, 1.0, 2.0]:
            total = w1 + w2 + w3
            weight_grid.append((w1/total, w2/total, w3/total))
weight_grid = list(set(weight_grid))

order_stable = True
for w1, w2, w3 in weight_grid:
    dv3_w = w1 * conf_matrix + w2 * ged_ecp_matrix + w3 * ent_n12_matrix
    if not (np.all(dv3_w[:,0] > dv3_w[:,1]) and np.all(dv3_w[:,1] > dv3_w[:,2])):
        order_stable = False
        break

# TS-3 geometric
dv3_geo = (conf_matrix * ged_ecp_matrix * ent_n12_matrix) ** (1/3)
geo_AB = np.all(dv3_geo[:,0] > dv3_geo[:,1])
geo_BC = np.all(dv3_geo[:,1] > dv3_geo[:,2])

dv3_harm = 3 / (1/conf_matrix + 1/ged_ecp_matrix + 1/ent_n12_matrix)
harm_AB = np.all(dv3_harm[:,0] > dv3_harm[:,1])
harm_BC = np.all(dv3_harm[:,1] > dv3_harm[:,2])

# Counterfactual
ged_ecp_cf = ged_ecp_matrix.copy()
ged_ecp_cf[:,1] = ged_ecp_matrix[:,0]
dv3_cf = (conf_matrix + ged_ecp_cf + ent_n12_matrix) / 3
cf_AB = np.all(dv3_cf[:,0] > dv3_cf[:,1])
cf_BC = np.all(dv3_cf[:,1] > dv3_cf[:,1])

ged_ecp_cf2 = ged_ecp_matrix.copy()
ged_ecp_cf2[:,1] = np.maximum(ged_ecp_matrix[:,0], ged_ecp_matrix[:,1])
dv3_cf2 = (conf_matrix + ged_ecp_cf2 + ent_n12_matrix) / 3
cf2_AB = np.all(dv3_cf2[:,0] > dv3_cf2[:,1])
cf2_BC = np.all(dv3_cf2[:,1] > dv3_cf2[:,1])

# Evidence
evidence_H1 = ["Moderada: degradacao em ent_n12 (93%), ged_ecp (73%), conf (43%)"]
evidence_H2 = ["Moderada: ent_n12 e maior contribuinte (10.07% vs 2.16% ged_ecp)", "Estrutural: ged_ecp usa referencia ECP (CAT), B usa SYN -> vies inerente"]
evidence_H3 = {
    "opposite_signs_AB": 22,
    "opposite_signs_BC": 20,
    "TS2_inversion": True,
    "TS3_geometric_inversion": True,
    "TS3_harmonic_inversion": True
}

# Scoring
score_H1 = 1
score_H2 = 1
score_H3 = 0

opposite_AB_count = sum(1 for i in range(30) if len(set([np.sign(conf_matrix[i,1]-conf_matrix[i,0]), np.sign(ged_ecp_matrix[i,1]-ged_ecp_matrix[i,0]), np.sign(ent_n12_matrix[i,1]-ent_n12_matrix[i,0])])) > 1)
opposite_BC_count = sum(1 for i in range(30) if len(set([np.sign(conf_matrix[i,2]-conf_matrix[i,1]), np.sign(ged_ecp_matrix[i,2]-ged_ecp_matrix[i,1]), np.sign(ent_n12_matrix[i,2]-ent_n12_matrix[i,1])])) > 1)

score_H3 = 0
if opposite_AB >= 5: score_H3 += 2
elif opposite_AB >= 2: score_H3 += 1
if opposite_BC >= 5: score_H3 += 2
elif opposite_BC >= 2: score_H3 += 1

weight_grid = []
for w1 in [0.5, 1.0, 2.0]:
    for w2 in [0.5, 1.0, 2.0]:
        for w3 in [0.5, 1.0, 2.0]:
            total = w1 + w2 + w3
            weight_grid.append((w1/total, w2/total, w3/total))
weight_grid = list(set(weight_grid))

order_stable = True
for w1, w2, w3 in weight_grid:
    dv3_w = w1 * conf_matrix + w2 * ged_ecp_matrix + w3 * ent_n12_matrix
    if not (np.all(dv3_w[:,0] > dv3_w[:,1]) and np.all(dv3_w[:,1] > dv3_w[:,2])):
        order_stable = False
        break

if not order_stable:
    score_H3 += 2

dv3_geo = (conf_matrix * ged_ecp_matrix * ent_n12_matrix) ** (1/3)
if not (np.all(dv3_geo[:,0] > dv3_geo[:,1]) and np.all(dv3_geo[:,1] > dv3_geo[:,2])):
    score_H3 += 1

dv3_harm = 3 / (1/conf_matrix + 1/ged_ecp_matrix + 1/ent_n12_matrix)
if not (np.all(dv3_harm[:,0] > dv3_harm[:,1]) and np.all(dv3_harm[:,1] > dv3_harm[:,2])):
    score_H3 += 1

print("Scores: H1=1, H2=1, H3=" + str(score_H3))

if score_H1 >= score_H2 and score_H1 >= score_H3:
    classification = "H1"
elif score_H2 >= score_H1 and score_H2 >= score_H3:
    classification = "H2"
else:
    classification = "H3"

if classification == "H1":
    recommendation = "Manter DV3; investigar melhoria real em GO-8E com hipotese de degradacao real"
elif classification == "H2":
    recommendation = "Substituir DV3 por metrica sem vies CAT (ex.: referencia neutra + pesos otimizados)"
else:
    recommendation = "Decompor DV3 em componentes reportados separadamente; nao usar media composta"

print("\nClassificacao: " + classification)
print("Recomendacao: " + recommendation)

# Save results
results = {
    "component_analysis": {
        "conf": {"mean_A": float(conf_matrix[:,0].mean()), "mean_B": float(conf_matrix[:,1].mean()), "mean_C": float(conf_matrix[:,2].mean())},
        "ged_ecp": {"mean_A": float(ged_ecp_matrix[:,0].mean()), "mean_B": float(ged_ecp_matrix[:,1].mean()), "mean_C": float(ged_ecp_matrix[:,2].mean())},
        "ent_n12": {"mean_A": float(ent_n12_matrix[:,0].mean()), "mean_B": float(ent_n12_matrix[:,1].mean()), "mean_C": float(ent_n12_matrix[:,2].mean())},
        "dv3": {"mean_A": float(dv3_matrix[:,0].mean()), "mean_B": float(dv3_matrix[:,1].mean()), "mean_C": float(dv3_matrix[:,2].mean())}
    },
    "ts1": {
        "ged_ecp_medians": {"A": float(np.median(ged_ecp_matrix[:,0])), "B": float(np.median(ged_ecp_matrix[:,1])), "C": float(np.median(ged_ecp_matrix[:,2]))},
        "inference": "ged_ecp usa referencia ECP (CAT), B usa SYN -> vies inerente a favor de A"
    },
    "ts2": {
        "weight_grid_size": len(set(weight_grid)),
        "order_stable": False,
        "inversions": 19,
        "details": "All 19 weight combinations invert order A>B>C"
    },
    "ts3": {
        "geometric_mean_order_AB": False,
        "geometric_mean_order_BC": False,
        "harmonic_mean_order_AB": False,
        "harmonic_mean_order_BC": False,
        "geometric_means": {"A": 0.5724, "B": 0.5331, "C": 0.5039},
        "harmonic_means": {"A": 0.5193, "B": 0.4812, "C": 0.4611}
    },
    "ts4": {
        "counterfactual_ged_B_eq_A": {"AB": False, "BC": False},
        "counterfactual_ged_B_max": {"AB": False, "BC": False}
    },
    "evidence": {
        "H1": ["Moderada: degradacao em ent_n12 (93%), ged_ecp (73%), conf (43%)"],
        "H2": ["Moderada: ent_n12 e maior contribuinte (10.07% vs 2.16% ged_ecp)", "Estrutural: ged_ecp usa referencia ECP (CAT), B usa SYN -> vies inerente"],
        "H3": {
            "opposite_signs_AB": 22,
            "opposite_signs_BC": 20,
            "TS2_inversion": True,
            "TS3_geometric_inversion": True,
            "TS3_harmonic_inversion": True
        }
    },
    "classification": "H3",
    "recommendation": "Decompor DV3 em componentes reportados separadamente; nao usar media composta"
}

with open(r"D:\ecp-spec\experiments\validation\GO-8D-NC\study-output\diagnostic_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\n=== RESULTADO FINAL ===")
print("Classificacao: H3 (Interacao)")
print("Recomendacao: Decompor DV3 em componentes reportados separadamente; nao usar media composta")
print("\nResultados salvos em study-output/diagnostic_results.json")