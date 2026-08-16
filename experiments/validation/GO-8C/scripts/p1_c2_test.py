import json
import os
import sys

CANONICAL_ORDER = ["Problem", "Goal", "Claim", "Knowledge", "Assumption", "Evidence", "Decision", "State", "Artifact"]

# ---- Configuração GO-8C (DECISION D-01, 2026-08-13) ----
SEED_OFICIAL = 258915
SEED_HEX = "0x3f363"
SEED_HISTORICA = 11473621728585666159
FROZEN_PERM_SS5 = [1, 5, 6, 3, 7, 0, 4, 8, 2]
TRUE_INVERSE_SS5 = [5, 0, 8, 3, 6, 1, 2, 4, 7]

FROZEN_OPAQUE_TO_CANONICAL = {
    "CAT-00": "Evidence",
    "CAT-01": "Problem",
    "CAT-02": "Artifact",
    "CAT-03": "Knowledge",
    "CAT-04": "Decision",
    "CAT-05": "Goal",
    "CAT-06": "Claim",
    "CAT-07": "Assumption",
    "CAT-08": "State",
}
FROZEN_CANONICAL_TO_OPAQUE = {v: k for k, v in FROZEN_OPAQUE_TO_CANONICAL.items()}
NAMESPACES = {"C1": "ECP", "C2": "CAT", "C3": "SYN", "C4": "NULL"}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
YAML_PATH = os.path.join(BASE_DIR, "C2_PERMUTATION.yaml")
JSON_PATH = os.path.join(BASE_DIR, "C2_PERMUTATION.json")


def pcg64_permutation(seed):
    import numpy as np
    rng = np.random.Generator(np.random.PCG64(seed))
    idx = np.arange(len(CANONICAL_ORDER))
    rng.shuffle(idx)
    return idx.tolist()


def true_inverse(perm):
    inv = [None] * len(perm)
    for c, p in enumerate(perm):
        inv[p] = c
    return inv


def load_yaml(path):
    import yaml
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def run_validation():
    results = {}

    # T-C2-01: determinismo da seed oficial 258915
    perm = pcg64_permutation(SEED_OFICIAL)
    results["T-C2-01"] = (perm == FROZEN_PERM_SS5,
                          f"PCG64({SEED_OFICIAL}) reproduces SS5 permutation {FROZEN_PERM_SS5}")

    # T-C2-02: sensibilidade a bit alterado na seed
    perm_alt = pcg64_permutation(SEED_OFICIAL ^ 1)
    results["T-C2-02"] = (perm_alt != FROZEN_PERM_SS5,
                          "single-bit seed change produces different permutation")

    # T-C2-03: bijetividade do mapping bidirecional
    o2c = FROZEN_OPAQUE_TO_CANONICAL
    c2o = FROZEN_CANONICAL_TO_OPAQUE
    bijective = all(c2o[o2c[x]] == x for x in o2c) and all(o2c[c2o[x]] == x for x in c2o)
    results["T-C2-03"] = (bijective, "bidirectional bijection SS6")

    # T-C2-04: completude (exatamente 9 categorias canonicas, sem duplicatas)
    vals = sorted(o2c.values())
    results["T-C2-04"] = (vals == sorted(CANONICAL_ORDER), "9 categories, no duplicates")

    # T-C2-05: estabilidade/reprodutibilidade PCG64 (duas instanciacoes independentes)
    perm2 = pcg64_permutation(SEED_OFICIAL)
    results["T-C2-05"] = (perm2 == FROZEN_PERM_SS5,
                          "PCG64(258915) stable across independent instantiations (portability of PCG64)")

    # T-C2-08: regressao - seed historica NAO reproduz a tabela (documental)
    perm_hist = pcg64_permutation(SEED_HISTORICA)
    not_reproducing = perm_hist != FROZEN_PERM_SS5
    results["T-C2-08"] = (not_reproducing,
                          f"PCG64({SEED_HISTORICA}) -> {perm_hist} NOT equal to SS5 {FROZEN_PERM_SS5} (HISTORICAL-NON-REPRODUCING)")

    # T-C2-09: oficialidade do YAML - seed_operacional=258915 e inversa correta
    y = load_yaml(YAML_PATH)
    seed_ok = (y.get("seed_operacional", {}).get("value") == SEED_OFICIAL)
    inv_yaml = y.get("inversa_verdadeira")
    inv_ok = (inv_yaml == TRUE_INVERSE_SS5)
    inv_true = true_inverse(FROZEN_PERM_SS5)
    inv_true_ok = (inv_true == TRUE_INVERSE_SS5)
    hist_ok = (y.get("seed_historica", {}).get("status") == "HISTORICAL-NON-REPRODUCING")
    results["T-C2-09"] = (seed_ok and inv_ok and inv_true_ok and hist_ok,
                          f"YAML seed_operacional={seed_ok}, inversa_verdadeira={inv_ok}, true inverse of perm={inv_true_ok}, seed_historica status={hist_ok}")

    return results


def main():
    results = run_validation()

    for k, (ok, desc) in results.items():
        print(f"{k}: {'PASS' if ok else 'FAIL'} ({desc})")

    n = len(results)
    npass = sum(1 for ok, _ in results.values() if ok)
    print(f"\nTOTAL: {n} PASS: {npass} FAIL: {n - npass}")
    all_pass = all(ok for ok, _ in results.values())
    print("ALL PASS:", all_pass)
    if not all_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
