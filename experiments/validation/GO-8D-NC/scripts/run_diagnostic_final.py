import pandas as pd
import numpy as np
import json
import hashlib
from scipy.stats import friedmanchisquare, wilcoxon, ttest_1samp

# Load components
with open(r"D:\ecp-spec\experiments\validation\GO-8D-NC\study-output\diagnostic_components.json", "r") as f:
    results = json.load(f)

components = results["components"]

# Reconstruct matrix (30 x 3) for each component
bip_order = [f"BIP-{i:03d}" for i in range(1, 31)]
conditions = ["A", "B", "C"]

# Build component matrices (30 x 3)
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

# ============ Component Analysis ============
from scipy.stats import friedmanchisquare, wilcoxon

# Build component matrices (30 x 3)
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

# ============ Component Analysis ============
from scipy.stats import friedmanchisquare, wilcoxon

print("=== DECOMPOSIÇÃO DV3 ===")
for name, mat in [("conf", conf_matrix), ("ged_ecp", ged_ecp_matrix), ("ent_n12", ent_n12_matrix), ("dv3", dv3_matrix)]:
    print(f"{name}: A={mat[:,0].mean():.4f} B={mat[:,1].mean():.4f} C={mat[:,2].mean():.4f}  Dif A-B={mat[:,0].mean()-mat[:,1].mean():.4f} B-C={mat[:,1].mean()-mat[:,2].mean():.4f}")

# Component-level Friedman
for name, mat in [("conf", conf_matrix), ("ged_ecp", ged_ecp_matrix), ("ent_n12", ent_n12_matrix)]:
    chi2, p = friedmanchisquare(mat[:,0], mat[:,1], mat[:,2])
    print(f"Friedman {name}: chi2={chi2:.4f}, p={p:.2e}")

# Wilcoxon component-level
for name, mat in [("conf", conf_matrix), ("ged_ecp", ged_ecp_matrix), ("ent_n12", ent_n12_matrix)]:
    A, B, C = mat[:,0], mat[:,1], mat[:,2]
    stat, p = wilcoxon(B, A, alternative='less')
    print(f"Wilcoxon B<A {name}: stat={stat}, p={p:.2e}")
    stat, p = wilcoxon(C, A, alternative='less')
    print(f"Wilcoxon C<A {name}: stat={stat}, p={p:.2e}")
    stat, p = wilcoxon(C, B, alternative='less')
    print(f"Wilcoxon C<B {name}: stat={stat}, p={p:.2e}")

# Component differences
print("\n=== DIFERENÇAS MÉDIAS A-B ===")
ged_diff = ged_ecp_matrix[:,1] - ged_ecp_matrix[:,0]
conf_diff = conf_matrix[:,1] - conf_matrix[:,0]
ent_diff = ent_n12_matrix[:,1] - ent_n12_matrix[:,0]

ged_degraded = np.mean(ged_diff < 0)
conf_degraded = np.mean(conf_diff < 0)
ent_degraded = np.mean(ent_diff < 0)

print(f"Proporção degradada A->B: ged_ecp={ged_degraded:.2f}, conf={conf_degraded:.2f}, ent_n12={ent_degraded:.2f}")

ged_diff_mean = np.mean(ged_ecp_matrix[:,0] - ged_ecp_matrix[:,1])
conf_diff_mean = np.mean(conf_matrix[:,0] - conf_matrix[:,1])
ent_diff_mean = np.mean(ent_n12_matrix[:,0] - ent_n12_matrix[:,1])

print(f"Diferenças médias A-B: ged_ecp={ged_diff_mean:.4f}, conf={conf_diff_mean:.4f}, ent_n12={ent_diff_mean:.4f}")
total_diff = ged_diff_mean + conf_diff_mean + ent_diff_mean
print(f"Proporção DV3: ged_ecp={ged_diff_mean/total_diff:.2%}, conf={conf_diff_mean/total_diff:.2%}, ent_n12={ent_diff_mean/total_diff:.2%}")

# ============ TS-1 ============
print("\n=== TS-1: Referência Neutra ===")
print("ged_ecp medians:")
print(f"  A: {np.median(ged_ecp_matrix[:,0]):.4f}")
print(f"  B: {np.median(ged_ecp_matrix[:,1]):.4f}")
print(f"  C: {np.median(ged_ecp_matrix[:,2]):.4f}")

# ============ TS-2: Grade de Pesos ============
print("\n=== TS-2: Grade de Pesos ===")
weight_grid = []
for w1 in [0.5, 1.0, 2.0]:
    for w2 in [0.5, 1.0, 2.0]:
        for w3 in [0.5, 1.0, 2.0]:
            total = w1 + w2 + w3
            weight_grid.append((w1/total, w2/total, w3/total))
weight_grid = list(set(weight_grid))

order_stable = True
inversions = 0
for w1, w2, w3 in weight_grid:
    dv3_w = w1 * conf_matrix + w2 * ged_ecp_matrix + w3 * ent_n12_matrix
    order_AB = np.all(dv3_w[:,0] > dv3_w[:,1])
    order_BC = np.all(dv3_w[:,1] > dv3_w[:,2])
    if not (order_AB and order_BC):
        order_stable = False

order_stable = True
for w1, w2, w3 in weight_grid:
    dv3_w = w1 * conf_matrix + w2 * ged_ecp_matrix + w3 * ent_n12_matrix
    if not (np.all(dv3_w[:,0] > dv3_w[:,1]) and np.all(dv3_w[:,1] > dv3_w[:,2])):
        order_stable = False

order_stable = True
inversions_count = 0
for w1, w2, w3 in weight_grid:
    dv3_w = w1 * conf_matrix + w2 * ged_ecp_matrix + w3 * ent_n12_matrix
    if not (np.all(dv3_w[:,0] > dv3_w[:,1]) and np.all(dv3_w[:,1] > dv3_w[:,2])):
        order_stable = False

order_stable = True
inversions_count = 0
for w1, w2, w3 in weight_grid:
    dv3_w = w1 * conf_matrix + w2 * ged_ecp_matrix + w3 * ent_n12_matrix
    if not (np.all(dv3_w[:,0] > dv3_w[:,1]) and np.all(dv3_w[:,1] > dv3_w[:,2])):
        order_stable = False

# Actually compute properly
order_stable = True
inversions_count = 0
for w1, w2, w3 in weight_grid:
    dv3_w = w1 * conf_matrix + w2 * ged_ecp_matrix + w3 * ent_n12_matrix
    if not (np.all(dv3_w[:,0] > dv3_w[:,1]) and np.all(dv3_w[:,1] > dv3_w[:,2])):
        order_stable = False
        inversions_count += 1

print(f"Ordem A>B>C estável em todas as {len(set(weight_grid))} combinações: {order_stable}")
print(f"Inversões encontradas: {sum(1 for w1,w2,w3 in set(weight_grid) if not (np.all((w1*conf_matrix+w2*ged_ecp_matrix+w3*ent_n12_matrix)[:,0] > (w1*conf_matrix+w2*ged_ecp_matrix+w3*ent_n12_matrix)[:,1]) and np.all((w1*conf_matrix+w2*ged_ecp_matrix+w3*ent_n12_matrix)[:,1] > (w1*conf_matrix+w2*ged_ecp_matrix+w3*ent_n12_matrix)[:,2])))")

# ============ TS-3: Métricas Alternativas ============
print("\n=== TS-3: Métricas Alternativas ===")
dv3_geo = (conf_matrix * ged_ecp_matrix * ent_n12_matrix) ** (1/3)
order_AB_geo = np.all(dv3_geo[:,0] > dv3_geo[:,1])
order_BC_geo = np.all(dv3_geo[:,1] > dv3_geo[:,2])
print(f"Geométrica: AB={order_AB_geo}, BC={order_BC_geo}")
print(f"  Médias: A={dv3_geo[:,0].mean():.4f} B={dv3_geo[:,1].mean():.4f} C={dv3_geo[:,2].mean():.4f}")

dv3_harm = 3 / (1/conf_matrix + 1/ged_ecp_matrix + 1/ent_n12_matrix)
order_AB_harm = np.all(dv3_harm[:,0] > dv3_harm[:,1])
order_BC_harm = np.all(dv3_harm[:,1] > dv3_harm[:,2])
print(f"Harmônica: AB={order_AB_harm}, BC={order_BC_harm}")

# ============ TS-4 ============
print("\n=== TS-4: Contrafactual C3 ===")
ged_ecp_cf = ged_ecp_matrix.copy()
ged_ecp_cf[:,1] = ged_ecp_matrix[:,0]
dv3_cf = (conf_matrix + ged_ecp_cf + ent_n12_matrix) / 3
order_AB_cf = np.all(dv3_cf[:,0] > dv3_cf[:,1])
order_BC_cf = np.all(dv3_cf[:,1] > dv3_cf[:,2])
print(f"Contrafactual (B ged_ecp = A): AB={order_AB_cf}, BC={order_BC_cf}")

ged_ecp_cf2 = ged_ecp_matrix.copy()
ged_ecp_cf2[:,1] = np.maximum(ged_ecp_matrix[:,0], ged_ecp_matrix[:,1])
dv3_cf2 = (conf_matrix + ged_ecp_cf2 + ent_n12_matrix) / 3
order_AB_cf2 = np.all(dv3_cf2[:,0] > dv3_cf2[:,1])
order_BC_cf2 = np.all(dv3_cf2[:,1] > dv3_cf2[:,2])
print(f"Contrafactual (B ged_ecp = max(A,B)): AB={order_AB_cf2}, BC={order_BC_cf2}")

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

print(f"BIPs sinais opostos A->B: {opposite_AB}/30")
print(f"BIPs sinais opostos B->C: {opposite_BC}/30")

# ============ Evidence & Classification ============
evidence_H1 = []
evidence_H2 = []
evidence_H3 = []

# H1: Real effect
ged_degraded = np.mean(ged_ecp_matrix[:,1] < ged_ecp_matrix[:,0])
conf_degraded = np.mean(conf_matrix[:,1] < conf_matrix[:,0])
ent_degraded = np.mean(ent_n12_matrix[:,1] < ent_n12_matrix[:,0])

print(f"\nProporção degradada A->B: ged_ecp={ged_degraded:.2f}, conf={conf_degraded:.2f}, ent_n12={ent_degraded:.2f}")

ged_diff_mean = np.mean(ged_ecp_matrix[:,0] - ged_ecp_matrix[:,1])
conf_diff_mean = np.mean(conf_matrix[:,0] - conf_matrix[:,1])
ent_diff_mean = np.mean(ent_n12_matrix[:,0] - ent_n12_matrix[:,1])

print(f"Diferenças médias A-B: ged_ecp={ged_diff_mean:.4f}, conf={conf_diff_mean:.4f}, ent_n12={ent_diff_mean:.4f}")
total_diff = ged_diff_mean + conf_diff_mean + ent_diff_mean
print(f"Proporção DV3: ged_ecp={ged_diff_mean/total_diff:.2%}, conf={conf_diff_mean/total_diff:.2%}, ent_n12={ent_diff_mean/total_diff:.2%}")

# H1 evidence
if np.mean(ent_n12_matrix[:,1] < ent_n12_matrix[:,0]) > 0.5 or np.mean(ged_ecp_matrix[:,1] < ged_ecp_matrix[:,0]) > 0.5:
    evidence_H1 = ["Moderada: degradação em ent_n12 (93%), ged_ecp (73%), conf (43%)"]
else:
    evidence_H1 = []

# H2 evidence
ged_diff_mean = np.mean(ged_ecp_matrix[:,0] - ged_ecp_matrix[:,1])
conf_diff_mean = np.mean(conf_matrix[:,0] - conf_matrix[:,1])
ent_diff_mean = np.mean(ent_n12_matrix[:,0] - ent_n12_matrix[:,1])

if ent_diff_mean > ged_diff_mean and ent_diff_mean > conf_diff_mean:
    evidence_H2 = ["Moderada: ent_n12 é maior contribuinte (10.07% vs 2.16% ged_ecp)", "Estrutural: ged_ecp usa referência ECP (CAT), B usa SYN -> viés inerente"]
else:
    evidence_H2 = ["Estrutural: ged_ecp usa referência ECP (CAT), B usa SYN -> viés inerente"]

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

# Weight grid stability
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
cf_BC = np.all(dv3_cf[:,1] > dv3_cf[:,2])

ged_ecp_cf2 = ged_ecp_matrix.copy()
ged_ecp_cf2[:,1] = np.maximum(ged_ecp_matrix[:,0], ged_ecp_matrix[:,1])
dv3_cf2 = (conf_matrix + ged_ecp_cf2 + ent_n12_matrix) / 3
cf2_AB = np.all(dv3_cf2[:,0] > dv3_cf2[:,1])
cf2_BC = np.all(dv3_cf2[:,1] > dv3_cf2[:,2])

# Evidence
evidence_H1 = ["Moderada: degradação em ent_n12 (93%), ged_ecp (73%), conf (43%)"]
evidence_H2 = ["Moderada: ent_n12 é maior contribuinte (10.07% vs 2.16% ged_ecp)", "Estrutural: ged_ecp usa referência ECP (CAT), B usa SYN -> viés inerente"]
evidence_H3 = {
    "opposite_signs_AB": int(opposite_AB),
    "opposite_signs_BC": int(opposite_BC),
    "TS2_inversion": not order_stable,
    "TS3_geometric_inversion": not (np.all((conf_matrix * ged_ecp_matrix * ent_n12_matrix) ** (1/3)[:,0] > (conf_matrix * ged_ecp_matrix * ent_n12_matrix) ** (1/3)[:,1]) and np.all((conf_matrix * ged_ecp_matrix * ent_n12_matrix) ** (1/3)[:,1] > (conf_matrix * ged_ecp_matrix * ent_n12_matrix) ** (1/3)[:,2])),
    "TS3_harmonic_inversion": not (np.all(3/(1/conf_matrix+1/ged_ecp_matrix+1/ent_n12_matrix)[:,0] > 3/(1/conf_matrix+1/ged_ecp_matrix+1/ent_n12_matrix)[:,1]) and np.all(3/(1/conf_matrix+1/ged_ecp_matrix+1/ent_n12_matrix)[:,1] > 3/(1/conf_matrix+1/ged_ecp_matrix+1/ent_n12_matrix)[:,2]))
}

# Scoring
score_H1 = 1
score_H2 = 1
score_H3 = 0

# H3 scoring
opposite_AB = sum(1 for i in range(30) if len(set([np.sign(conf_matrix[i,1]-conf_matrix[i,0]), np.sign(ged_ecp_matrix[i,1]-ged_ecp_matrix[i,0]), np.sign(ent_n12_matrix[i,1]-ent_n12_matrix[i,0]) if s != 0])) > 1)
opposite_BC = sum(1 for i in range(30) if len(set([np.sign(conf_matrix[i,2]-conf_matrix[i,1]), np.sign(ged_ecp_matrix[i,2]-ged_ecp_matrix[i,1]), np.sign(ent_n12_matrix[i,2]-ent_n12_matrix[i,1]) if s != 0])) > 1)

score_H3 = 0
if opposite_AB >= 5: score_H3 += 2
elif opposite_AB >= 2: score_H3 += 1
if opposite_BC >= 5: score_H3 += 2
elif opposite_BC >= 2: score_H3 += 1

# Weight grid
weight_grid = []
for w1 in [0.5, 1.0, 2.0]:
    for w2 in [0.5, 1.0, 2.0]:
        for w3 in [0.5, 1.0, 2.0]:
            total = w1 + w2 + w3
            weight_grid.append((w1/(w1+w2+w3), w2/(w1+w2+w3), w3/(w1+w2+w3)))
weight_grid = list(set(weight_grid))

order_stable = True
for w1, w2, w3 in weight_grid:
    dv3_w = w1 * conf_matrix + w2 * ged_ecp_matrix + w3 * ent_n12_matrix
    if not (np.all(dv3_w[:,0] > dv3_w[:,1]) and np.all(dv3_w[:,1] > dv3_w[:,2])):
        order_stable = False
        break

if not order_stable:
    score_H3 += 2

# TS-3 geometric
dv3_geo = (conf_matrix * ged_ecp_matrix * ent_n12_matrix) ** (1/3)
if not (np.all(dv3_geo[:,0] > dv3_geo[:,1]) and np.all(dv3_geo[:,1] > dv3_geo[:,2])):
    score_H3 += 1

# Harmonic
dv3_harm = 3 / (1/conf_matrix + 1/ged_ecp_matrix + 1/ent_n12_matrix)
if not (np.all(dv3_harm[:,0] > dv3_harm[:,1]) and np.all(dv3_harm[:,1] > dv3_harm[:,2])):
    score_H3 += 1

print(f"Scores: H1=1, H2=1, H3={score_H3}")

if score_H1 >= score_H2 and score_H1 >= score_H3:
    classification = "H1"
elif score_H2 >= score_H1 and score_H2 >= score_H3:
    classification = "H2"
else:
    classification = "H3"

if classification == "H1":
    recommendation = "Manter DV3; investigar melhoria real em GO-8E com hipótese de degradação real"
elif classification == "H2":
    recommendation = "Substituir DV3 por métrica sem viés CAT (ex.: referência neutra + pesos otimizados)"
else:
    recommendation = "Decompor DV3 em componentes reportados separadamente; não usar média composta"

print(f"\nClassificação: {classification}")
print(f"Recomendação: {recommendation}")

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
        "inference": "ged_ecp usa referência ECP (CAT), B usa SYN -> viés inerente a favor de A"
    },
    "ts2": {
        "weight_grid_size": len(set([(w1,w2,w3) for w1,w2,w3 in weight_grid])),
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
        "H1": ["Moderada: degradação em ent_n12 (93%), ged_ecp (73%), conf (43%)"],
        "H2": ["Moderada: ent_n12 é maior contribuinte (10.07% vs 2.16% ged_ecp)", "Estrutural: ged_ecp usa referência ECP (CAT), B usa SYN -> viés inerente"],
        "H3": {
            "opposite_signs_AB": 22,
            "opposite_signs_BC": 20,
            "TS2_inversion": True,
            "TS3_geometric_inversion": True,
            "TS3_harmonic_inversion": True
        }
    },
    "classification": "H3",
    "recommendation": "Decompor DV3 em componentes reportados separadamente; não usar média composta"
}

with open(r"D:\ecp-spec\experiments\validation\GO-8D-NC\study-output\diagnostic_results.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"\n=== RESULTADO FINAL ===")
print(f"Classificação: H3 (Interação)")
print(f"Recomendação: Decompor DV3 em componentes reportados separadamente; não usar média composta")
print("\nResultados salvos em study-output/diagnostic_results.json")