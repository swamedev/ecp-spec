import json
import os
import sys

sys.path.insert(0, r"D:\ecp-spec\scripts\go8b\operational")
from graph_from_reconstruction import GraphFromReconstruction

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
YAML_PATH = os.path.join(BASE_DIR, "C2_PERMUTATION.yaml")

REG = {"T_ECP-v1": True, "T_PERM-v1": True, "T_SYNTH-v1": True}

EXPECTED_OPERATIONAL = {"A": "CAT", "B": "SYN", "C": "CAT"}


def base(namespace="CAT", taxonomy="T_PERM-v1"):
    return {
        "case_id": "SX-999",
        "reconstruction_version": "2026-08-13T00:00:00Z",
        "taxonomy_version": taxonomy,
        "taxonomy_namespace": namespace,
        "entities": [
            {"entity_id": "ENT-0001", "syn_category": "CAT-00", "confidence": 0.8, "source_af_ids": ["AF-001"]},
            {"entity_id": "ENT-0002", "syn_category": "CAT-01", "confidence": 0.6, "source_af_ids": ["AF-001"]},
        ],
        "relations": [
            {"relation_id": "REL-0001", "source": "ENT-0001", "target": "ENT-0002", "relation_type": "feeds", "confidence": 0.7},
        ],
    }


def load_yaml(path):
    import yaml
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    results = {}

    parser = GraphFromReconstruction(taxonomy_registry=REG)

    # T-D-02-01: parser rejeita NULL com NAMESPACE_MIX (conforme especificacao 04 SS1.1)
    d = base(namespace="NULL", taxonomy="T_SYNTH-v1")
    try:
        parser.parse(d)
        results["T-D-02-01"] = (False, "NULL accepted - parser should reject with NAMESPACE_MIX")
    except ValueError as e:
        results["T-D-02-01"] = (str(e) == "NAMESPACE_MIX",
                                f"NULL rejected with {str(e)} (expected NAMESPACE_MIX)")

    # T-D-02-02: parser aceita CAT e produz grafo valido com rotulos CAT-XX
    d = base(namespace="CAT", taxonomy="T_PERM-v1")
    out = parser.parse(d)
    cats_ok = all(n["syn_category"].startswith("CAT") for n in out["nodes"])
    results["T-D-02-02"] = (out["metadata"]["num_nodes"] == 2 and cats_ok,
                            f"CAT graph built: {out['metadata']['num_nodes']} nodes, all CAT-XX labels")

    # T-D-02-03: namespaces operacionais A/B/C = CAT/SYN/CAT no artefato operacional GO-8C
    y = load_yaml(YAML_PATH)
    op = y.get("namespace_operacional", {})
    match = all(op.get(k) == v for k, v in EXPECTED_OPERATIONAL.items())
    results["T-D-02-03"] = (match,
                            f"namespace_operacional = {op} (expected {EXPECTED_OPERATIONAL})")

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
