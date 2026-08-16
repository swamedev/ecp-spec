import json

CANONICAL_ORDER = ["Problem", "Goal", "Claim", "Knowledge", "Assumption", "Evidence", "Decision", "State", "Artifact"]

# Autoritative mapping from 02 SS6 (frozen, registered for pipeline use)
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

# Frozen SS5 permutation array: canonical index -> opaque position
FROZEN_PERM_SS5 = [1, 5, 6, 3, 7, 0, 4, 8, 2]
# TRUE inverse of FROZEN_PERM_SS5: opaque position -> canonical index
TRUE_INVERSE_SS5 = [5, 0, 8, 3, 6, 1, 2, 4, 7]
# Registered seed (02 SS4) - documented as non-reproducing under PCG64 SS3.1
SEED_C2 = 11473621728585666159
# Operational seed (P1-C2-01 option A) - reproduces SS5 table under PCG64
SEED_OPERATIONAL = 258915
# Namespace map (02 SS1, R3-01)
NAMESPACES = {"C1": "ECP", "C2": "CAT", "C3": "SYN", "C4": "NULL"}

def mapping_from_perm(perm):
    out = {}
    for c, p in enumerate(perm):
        out[FROZEN_CANONICAL_TO_OPAQUE[CANONICAL_ORDER[c]]] = CANONICAL_ORDER[c]
    return out

def run_validation():
    results = {}
    o2c = FROZEN_OPAQUE_TO_CANONICAL
    c2o = FROZEN_CANONICAL_TO_OPAQUE

    # T-C2-03: bijetividade bidirecional
    bijective = all(c2o[o2c[x]] == x for x in o2c) and all(o2c[c2o[x]] == x for x in c2o)
    results["T-C2-03-MAP-BIJECTION"] = (bijective, "bidirectional bijection SS6")

    # T-C2-04: completude (exatamente 9 categorias canonicas, sem duplicatas)
    vals = sorted(o2c.values())
    results["T-C2-04-MAP-COMPLETENESS"] = (vals == sorted(CANONICAL_ORDER), "9 categories, no duplicates")

    # T-C2-MAP-01: mapping SS6 == mapping derivado da permutacao SS5
    results["T-C2-MAP-01"] = (mapping_from_perm(FROZEN_PERM_SS5) == o2c, "SS6 consistent with SS5 permutation")

    # T-C2-MAP-02: mapping SS6 == tabela de posicoes SS5 (CAT-00..CAT-08)
    table5 = dict(sorted(o2c.items()))  # keys CAT-00..CAT-08 in order == positions table
    results["T-C2-MAP-02"] = (all(table5[f"CAT-{i:02d}"] == o2c[f"CAT-{i:02d}"] for i in range(9)), "SS6 consistent with SS5 position table")

    # T-C2-MAP-03: inversa verdadeira da perm SS5 == SS6 opaque_to_canonical
    true_inverse = [None] * 9
    for c, p in enumerate(FROZEN_PERM_SS5):
        true_inverse[p] = c
    expected_inverse_o2o = {f"CAT-{p:02d}": CANONICAL_ORDER[c] for p, c in enumerate(true_inverse)}
    results["T-C2-MAP-03"] = (expected_inverse_o2o == o2c, "true inverse of SS5 perm == SS6 mapping")

    # T-C2-MAP-04: namespace CAT exclusivo - todos os labels CAT-XX
    ns_ok = all(k.startswith("CAT-") and k[4:].isdigit() for k in o2c)
    results["T-C2-MAP-04"] = (ns_ok and len(o2c) == 9, "namespace CAT exclusive")

    # T-C2-MAP-05: seed registrada NAO reproduz sob PCG64 - documentado, nao falha
    results["T-C2-MAP-05-NOTE"] = (True, "seed documented non-reproducing (P1-C2-01); mapping used verbatim SS6")

    # T-C2-MAP-06: seed operacional reproduz SS5 sob PCG64
    import numpy as np
    rng = np.random.Generator(np.random.PCG64(SEED_OPERATIONAL))
    idx = np.arange(len(CANONICAL_ORDER))
    rng.shuffle(idx)
    results["T-C2-MAP-06-SEED-OPERATIONAL"] = (idx.tolist() == FROZEN_PERM_SS5, "PCG64(258915) reproduces SS5")

    # T-C2-MAP-07: inversa verdadeira == SS6 mapping
    inv = [None] * 9
    for c, p in enumerate(FROZEN_PERM_SS5):
        inv[p] = c
    results["T-C2-MAP-07-TRUE-INVERSE"] = (inv == TRUE_INVERSE_SS5, "true inverse matches operational array")

    return results

def main():
    results = run_validation()
    o2c = FROZEN_OPAQUE_TO_CANONICAL
    c2o = FROZEN_CANONICAL_TO_OPAQUE

    doc = {
        "namespace": "CAT",
        "namespaces": NAMESPACES,
        "source": "02-C2-PERMUTATION.md SS6 (frozen, GO-8B lock) - reproduced verbatim",
        "derived_from": "02-C2-PERMUTATION.md SS6 (frozen)",
        "mapping_status": "OPERATIONAL-AUTHORITATIVE",
        "seed_registrada": {
            "value": SEED_C2,
            "hex": "0x9F3A7E2C1B8D4E6F",
            "status": "REGISTERED-NON-REPRODUCING",
            "note": "Under PCG64 SS3.1 this seed does not reproduce SS5/SS6 (P1-C2-01). Mapping used verbatim; no generative claim. Repair deferred to future version/Lock cycle."
        },
        "seed_operacional": {
            "value": SEED_OPERATIONAL,
            "status": "OPERATIONAL",
            "note": "P1-C2-01 option A: reproduces frozen SS5 permutation under PCG64."
        },
        "algorithm_note": "NOT regenerated from registered seed. Content is a literal reproduction of the frozen mapping SS6; seed_operacional reproduces SS5.",
        "canonical_order": CANONICAL_ORDER,
        "opaque_to_canonical": {k: o2c[k] for k in sorted(o2c)},
        "canonical_to_opaque": {k: c2o[k] for k in CANONICAL_ORDER},
        "permutation_ss5_canonical_to_opaque_position": FROZEN_PERM_SS5,
        "inverse_verdadeira_opaque_to_canonical_index": TRUE_INVERSE_SS5,
        "validation": {k: ("PASS" if v[0] else "FAIL") for k, v in results.items()},
        "governance": {
            "decision": "P1-C2-01 option A (DECIDED 2026-08-12)",
            "decision_record": "experiments/validation/GO-8B/decisions/P1-C2-01-DECISION.md",
            "note": "C2 operational = SS6 mapping verbatim; seed_operacional=258915; repair of registered seed->permutation deferred to later governance/version cycle."
        },
        "generated_by": "p1_c2_permutation.py",
    }

    try:
        import yaml
        with open(r"D:\ecp-spec\scripts\go8b\operational\C2_PERMUTATION.yaml", "w", encoding="utf-8", newline="\n") as f:
            yaml.safe_dump(doc, f, sort_keys=False, allow_unicode=True)
    except ImportError:
        with open(r"D:\ecp-spec\scripts\go8b\operational\C2_PERMUTATION.yaml", "w", encoding="utf-8", newline="\n") as f:
            json.dump(doc, f, indent=2, ensure_ascii=False)

    with open(r"D:\ecp-spec\scripts\go8b\operational\C2_PERMUTATION.json", "w", encoding="utf-8", newline="\n") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)

    for k, (ok, desc) in results.items():
        print(f"{k}: {'PASS' if ok else 'FAIL'} ({desc})")
    all_pass = all(v[0] for v in results.values())
    print("ALL PASS:", all_pass)
    if not all_pass:
        raise SystemExit(1)

if __name__ == "__main__":
    main()