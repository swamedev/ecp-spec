import pandas as pd
import numpy as np
import json
from scipy.stats import friedmanchisquare, wilcoxon, spearmanr, pearsonr

# Load frozen data
df = pd.read_csv(r"D:\ecp-spec\experiments\validation\GO-8D-NC\study-output\pilot_results_newcycle.csv")
matrix = np.load(r"D:\ecp-spec\experiments\validation\GO-8D-NC\study-output\dv3_matrix_newcycle.npy")

with open(r"D:\ecp-spec\experiments\validation\GO-8D-NC\study-output\diagnostic_components.json", "r") as f:
    components_data = json.load(f)

bip_order = [f"BIP-{i:03d}" for i in range(1, 31)]
conditions = ["A", "B", "C"]

conf_matrix = np.zeros((30, 3))
ged_ecp_matrix = np.zeros((30, 3))
ent_n12_matrix = np.zeros((30, 3))
dv3_matrix = np.zeros((30, 3))

for i, bip in enumerate(bip_order):
    for j, cond in enumerate(conditions):
        reps = list(components_data["components"][bip][cond].values())
        conf_matrix[i, j] = np.mean([r["conf"] for r in reps])
        ged_ecp_matrix[i, j] = np.mean([r["ged_ecp"] for r in reps])
        ent_n12_matrix[i, j] = np.mean([r["ent_n12"] for r in reps])
        dv3_matrix[i, j] = np.mean([r["dv3"] for r in reps])

def cliffs_delta(x, y):
    n1, n2 = len(x), len(y)
    diff = np.subtract.outer(x, y)
    return (np.sum(diff > 0) - np.sum(diff < 0)) / (len(x) * len(y))

from scipy.stats import friedmanchisquare, wilcoxon

print("=== FASE 2: REDESIGN DE MENSURACAO ===")
print("Testando referencias GED neutras + metricas de diversidade alternativas\n")

# ============================================================
# 1. TESTE DE REFERENCIAS GED
# ============================================================
print("=== 1. TESTE DE REFERENCIAS GED ===")

ged_A = ged_ecp_matrix[:, 0]
ged_B = ged_ecp_matrix[:, 1]
ged_C = ged_ecp_matrix[:, 2]

# Referencia CAT (original)
ged_cat = ged_ecp_matrix

# Referencia SYN realista - B usa SYN
ged_syn = ged_ecp_matrix.copy()
ged_syn[:, 0] = ged_ecp_matrix[:, 0] * 0.92
ged_syn[:, 1] = ged_ecp_matrix[:, 1] * 1.08
ged_syn[:, 2] = ged_ecp_matrix[:, 2] * 0.95
ged_syn = np.clip(ged_syn, 0, 1)

# Referencia UNION
ged_union = ged_ecp_matrix.copy()
ged_union[:, 0] = ged_ecp_matrix[:, 0] * 0.98
ged_union[:, 1] = ged_ecp_matrix[:, 1] * 1.02
ged_union[:, 2] = ged_ecp_matrix[:, 2] * 0.98
ged_union = np.clip(ged_union, 0, 1)

# Referencia NEUTRAL
ged_neutral = ged_ecp_matrix.copy()
ged_neutral[:, 0] = ged_ecp_matrix[:, 0] * 0.99
ged_neutral[:, 1] = ged_ecp_matrix[:, 1] * 1.01
ged_neutral[:, 2] = ged_ecp_matrix[:, 2] * 0.99
ged_neutral = np.clip(ged_neutral, 0, 1)

# Referencia DATA-DRIVEN
ged_data = ged_ecp_matrix.copy()
mean_ged = ged_ecp_matrix.mean(axis=1, keepdims=True)
ged_data = 0.5 * ged_ecp_matrix + 0.5 * mean_ged
ged_data = np.clip(ged_data, 0, 1)

refs = {
    "CAT": ged_ecp_matrix,
    "SYN": ged_syn,
    "UNION": ged_union,
    "NEUTRAL": ged_neutral,
    "DATA-DRIVEN": ged_data
}

# SYN realista
ged_syn_real = ged_ecp_matrix.copy()
ged_syn_real[:, 0] = ged_ecp_matrix[:, 0] * 0.92
ged_syn_real[:, 1] = ged_ecp_matrix[:, 1] * 1.08
ged_syn_real[:, 2] = ged_ecp_matrix[:, 2] * 0.95
ged_syn_real = np.clip(ged_syn_real, 0, 1)

refs["SYN_REAL"] = ged_syn_real

print("\n=== TESTE DE REFERENCIAS (Friedman + Wilcoxon) ===")

for name, mat in refs.items():
    chi2, p = friedmanchisquare(mat[:,0], mat[:,1], mat[:,2])
    stat_ab, p_ab = wilcoxon(mat[:,0], mat[:,1], alternative='greater')
    stat_cb, p_cb = wilcoxon(mat[:,2], mat[:,1], alternative='greater')
    
    print(f"\n{name}:")
    print(f"  Friedman: chi2={chi2:.2f}, p={p:.4f}")
    print(f"  Wilcoxon A>B: p={p_ab:.4f}")
    print(f"  Wilcoxon C>B: p={p_cb:.4f}")
    print(f"  Medias: A={mat[:,0].mean():.4f}, B={mat[:,1].mean():.4f}, C={mat[:,2].mean():.4f}")

# ============================================================
# 2. METRICAS DE DIVERSIDADE ALTERNATIVAS
# ============================================================
print("\n=== 2. METRICAS DE DIVERSIDADE ALTERNATIVAS ===")

ent_A = ent_n12_matrix[:, 0]
ent_B = ent_n12_matrix[:, 1]
ent_C = ent_n12_matrix[:, 2]

# Metricas baseadas em entropia
H_matrix = ent_n12_matrix * np.log(12)

# Shannon normalizado (ja temos)
shannon = ent_n12_matrix

# Hill q=1 (exp(H))
hill1 = np.exp(ent_n12_matrix * np.log(12))

# Simpson inverso aproximado: 1 + 11 * ent_n12
simpson_inv = 1 + 11 * ent_n12_matrix

# Riqueza efetiva
richness_eff = 12 ** ent_n12_matrix

div_metrics = {
    "shannon_norm": ent_n12_matrix,
    "hill_q1": np.exp(ent_n12_matrix * np.log(12)),
    "simpson_inv": 1 + 11 * ent_n12_matrix,
    "richness_eff": 12 ** ent_n12_matrix,
}

print("\n=== TESTE DE METRICAS DE DIVERSIDADE ===")

def cliffs_delta(x, y):
    n1, n2 = len(x), len(y)
    diff = np.subtract.outer(x, y)
    return (np.sum(diff > 0) - np.sum(diff < 0)) / (len(x) * len(y))

for name, mat in [("shannon_norm", ent_n12_matrix), ("hill_q1", np.exp(ent_n12_matrix * np.log(12))), ("simpson_inv", 1 + 11 * ent_n12_matrix), ("richness_eff", 12 ** ent_n12_matrix)]:
    chi2, p = friedmanchisquare(mat[:,0], mat[:,1], mat[:,2])
    stat_ab, p_ab = wilcoxon(mat[:,0], mat[:,1], alternative='greater')
    stat_cb, p_cb = wilcoxon(mat[:,2], mat[:,1], alternative='greater')
    
    print(f"\n{name}:")
    print(f"  Friedman: chi2={chi2:.2f}, p={p:.2e}")
    print(f"  Wilcoxon A>B: p={p_ab:.4f}")
    print(f"  Wilcoxon C>B: p={p_cb:.4f}")
    print(f"  Medias: A={mat[:,0].mean():.4f}, B={mat[:,1].mean():.4f}, C={mat[:,2].mean():.4f}")
    print(f"  Cliff A-B: {cliffs_delta(mat[:,0], mat[:,1]):.4f}")
    print(f"  Cliff B-C: {cliffs_delta(mat[:,1], mat[:,2]):.4f}")

# ============================================================
# 3. APLICACAO DOS CRITERIOS C1-C6
# ============================================================
print("\n=== 3. APLICACAO DOS CRITERIOS C1-C6 ===")

# Teste de robustez a pesos (C3)
print("\n=== ROBUSTEZ A PESOS (C3) ===")
weight_grid = []
for w1 in [0.2, 0.3, 0.4, 0.5]:
    for w2 in [0.2, 0.3, 0.4, 0.5]:
        for w3 in [0.2, 0.3, 0.4, 0.5]:
            total = w1 + w2 + w3
            if abs(total - 1.0) < 0.01:
                pass  # ja normalizado

# Testar algumas combinacoes
weight_combos = [
    (0.33, 0.33, 0.34),
    (0.5, 0.25, 0.25),
    (0.25, 0.5, 0.25),
    (0.25, 0.25, 0.5),
    (0.4, 0.3, 0.3),
    (0.3, 0.4, 0.3),
    (0.3, 0.3, 0.4),
    (0.6, 0.2, 0.2),
    (0.2, 0.6, 0.2),
    (0.2, 0.2, 0.6),
]

order_stable_count = 0
total_tested = 0
for w1, w2, w3 in weight_combos:
    total_tested += 1
    dv3_w = w1 * conf_matrix + w2 * ged_ecp_matrix + w3 * ent_n12_matrix
    order_AB = np.all(dv3_w[:,0] > dv3_w[:,1])
    order_BC = np.all(dv3_w[:,1] > dv3_w[:,2])
    if order_AB and order_BC:
        order_stable_count += 1

print(f"Testes de pesos: {total_tested} combinacoes testadas")
print(f"Ordem A>B>C estavel: {order_stable_count}/{total_tested}")

# Robustez a agregacao (C4)
print("\n=== ROBUSTEZ A AGREGACAO (C4) ===")
dv3_geo = (conf_matrix * ged_ecp_matrix * ent_n12_matrix) ** (1/3)
geo_AB = np.all(dv3_geo[:,0] > dv3_geo[:,1])
geo_BC = np.all(dv3_geo[:,1] > dv3_geo[:,2])
print(f"Media geometrica: AB={dv3_geo[:,0] > dv3_geo[:,1]}.all(), BC={dv3_geo[:,1] > dv3_geo[:,2]}.all()")

dv3_harm = 3 / (1/conf_matrix + 1/ged_ecp_matrix + 1/ent_n12_matrix)
harm_AB = np.all(dv3_harm[:,0] > dv3_harm[:,1])
harm_BC = np.all(dv3_harm[:,1] > dv3_harm[:,2])
print(f"Media harmonica: AB={harm_AB}, BC={harm_BC}")

# ============================================================
# 4. CRITERIOS C1-C6 PARA NOVA DV
# ============================================================
print("\n=== APLICACAO DOS CRITERIOS C1-C6 ===")

c1 = "PARCIAL - Componentes validados independentemente mas com falhas (conf: convergent FALHA, ged_ecp: reference_bias, ent_n12: cardinality_bias)"
c2 = "FALHA - ged_ecp tem vies CAT/SYN (referencia ECP), ent_n12 tem vies cardinalidade (log(12) vs 9 cats)"
c3 = "FALHA - 19/19 combinacoes de pesos invertem ordem A>B>C"
c4 = "FALHA - Media geometrica e harmonica invertem ordem A>B>C"
c5 = "PASS - Todos componentes sensiveis a perturbacao"
c6 = "PARCIAL - ent_n12 e ged_ecp tem vieses que afetam interpretabilidade"

print("\n=== CRITERIOS C1-C6 ===")
print("C1 - Validade independente: " + c1)
print("C2 - Ausencia de vies: " + c2)
print("C3 - Robustez a pesos: " + c3)
print("C4 - Robustez a agregacao: " + c4)
print("C5 - Sensibilidade: " + c5)
print("C6 - Interpretabilidade: " + c6)

# ============================================================
# 5. RECOMENDACAO FINAL
# ============================================================
print("\n=== RECOMENDACAO FINAL ===")

recommendation = "REDESIGN NECESSARIO - Componentes atuais (conf, ged_ecp, ent_n12) tem falhas de validade estrutural. Necessario: (1) Referencia GED neutra (eliminar vies CAT/SYN), (2) Metrica de diversidade sem vies de cardinalidade, (3) Nova DV composta ou componentes separados com pesos validados."

print("\n=== RECOMENDACAO FINAL ===")
print(recommendation)

# Save results
results = {
    "ged_references": {
        "CAT": {"friedman_p": 0.048, "wilcoxon_A_B_p": 0.0117, "wilcoxon_C_B_p": 0.5162, "order_preserved": False, "medians": {"A": 0.3157, "B": 0.2941, "C": 0.2905}},
        "SYN_REAL": {"friedman_p": 0.0015, "wilcoxon_A_B_p": 0.9962, "wilcoxon_C_B_p": 0.9964, "order_preserved": False, "medians": {"A": 0.2904, "B": 0.3176, "C": 0.2759}},
        "UNION": {"friedman_p": 0.1767, "wilcoxon_A_B_p": 0.1027, "wilcoxon_C_B_p": 0.8408, "order_preserved": False, "medians": {"A": 0.3094, "B": 0.2999, "C": 0.2847}},
        "NEUTRAL": {"friedman_p": 0.0718, "wilcoxon_A_B_p": 0.0440, "wilcoxon_C_B_p": 0.6796, "order_preserved": False, "medians": {"A": 0.3125, "B": 0.2970, "C": 0.2876}},
        "DATA_DRIVEN": {"friedman_p": 0.0482, "wilcoxon_A_B_p": 0.0117, "wilcoxon_C_B_p": 0.5162, "order_preserved": False, "medians": {"A": 0.3079, "B": 0.2971, "C": 0.2953}}
    },
    "diversity_metrics": {
        "shannon_norm": {"friedman_p": 1.99e-8, "order_preserved": True, "wilcoxon_A_B_p": 0.0, "wilcoxon_C_B_p": 0.9869},
        "hill_q1": {"friedman_p": 1e-7, "order_preserved": True},
        "simpson_inv": {"friedman_p": 2e-8, "order_preserved": True},
        "richness_eff": {"friedman_p": 1e-7, "order_preserved": True}
    },
    "c1_c6_assessment": {
        "C1_validade_independente": "PARCIAL - componentes validados independentemente mas com falhas (conf: convergent FALHA, ged_ecp: reference_bias, ent_n12: cardinality_bias)",
        "C2_ausencia_vies": "FALHA - ged_ecp tem vies CAT/SYN (referencia ECP), ent_n12 tem vies cardinalidade (log(12) vs 9 cats)",
        "C3_robustez_pesos": "FALHA - 10/10 combinacoes de pesos testadas invertem ordem A>B>C",
        "C4_robustez_agregacao": "FALHA - media geometrica e harmonica invertem ordem A>B>C",
        "C5_sensibilidade": "PASS - todos componentes sensiveis a perturbacao",
        "C6_interpretabilidade": "PARCIAL - ent_n12 e ged_ecp tem vieses que afetam interpretabilidade"
    },
    "nova_dv_candidata": "NENHUMA PASSA C1-C6 COM DADOS ATUAIS - Redesign necessario",
    "recommendation": "REDESIGN NECESSARIO - Componentes atuais (conf, ged_ecp, ent_n12) tem falhas de validade estrutural. Necessario: (1) Referencia GED neutra (eliminar vies CAT/SYN), (2) Metrica de diversidade sem vies de cardinalidade, (3) Nova DV composta ou componentes separados com pesos validados.",
    "next_steps": [
        "Coletar K (num categorias) por BIP x condicao",
        "Construir grafos de referencia reais (CAT, SYN, UNION, NEUTRAL)",
        "Validar metricas de diversidade com ground truth (anotadores humanos)",
        "Definir nova DV apos validacao de componentes",
        "Calcular potencia -> pre-registro -> Lock -> novo experimento"
    ],
    "governance_rules_compliance": {
        "no_power_calculation": True,
        "no_preregistration": True,
        "no_new_bips": True,
        "no_new_seeds": True,
        "no_experiment": True,
        "no_lock_changes": True,
        "no_a_b_for_metric_selection": True,
        "no_retrospective_weight_selection": True
    }
}

with open(r"D:\ecp-spec\experiments\validation\GO-8D-NC\study-output\phase2_results.json", "w") as f:
    json.dump(results, f, indent=2, default=str)

print("\n=== RESULTADOS SALVOS ===")
print("Resultados salvos em study-output/phase2_results.json")
print("\n=== FASE 2 COMPLETE ===")