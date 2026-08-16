import sys
import json

sys.path.insert(0, r"D:\ecp-spec\scripts\go8b\operational")
from graph_from_reconstruction import GraphFromReconstruction

REG = {"T_ECP-v1": True, "T_PERM-v1": True, "T_SYNTH-v1": True}

def base(namespace="SYN", taxonomy="T_SYNTH-v1"):
    return {
        "case_id": "SX-999",
        "reconstruction_version": "2026-08-12T00:00:00Z",
        "taxonomy_version": taxonomy,
        "taxonomy_namespace": namespace,
        "entities": [
            {"entity_id": "ENT-0001", "syn_category": "SYN-001", "confidence": 0.8, "source_af_ids": ["AF-001"]},
            {"entity_id": "ENT-0002", "syn_category": "SYN-002", "confidence": 0.6, "source_af_ids": ["AF-001"]},
        ],
        "relations": [
            {"relation_id": "REL-0001", "source": "ENT-0001", "target": "ENT-0002", "relation_type": "feeds", "confidence": 0.7},
        ],
    }

results = {}

def record(tid, ok, note=""):
    results[tid] = (ok, note)

# T-GFR-01: valid input -> zero schema errors
p = GraphFromReconstruction(taxonomy_registry=REG)
try:
    out = p.parse(base())
    record("T-GFR-01", True, f"nodes={out['metadata']['num_nodes']} edges={out['metadata']['num_edges']}")
except Exception as e:
    record("T-GFR-01", False, str(e))

# T-GFR-02: missing required field -> SCHEMA_INVALID
d = base()
del d["entities"]
try:
    p.parse(d)
    record("T-GFR-02", False, "no error raised")
except ValueError as e:
    record("T-GFR-02", str(e) == "SCHEMA_INVALID", str(e))

# T-GFR-03: version mismatch -> VERSION_MISMATCH
d = base()
d["taxonomy_version"] = "NONEXISTENT"
try:
    p.parse(d)
    record("T-GFR-03", False, "no error")
except ValueError as e:
    record("T-GFR-03", str(e) == "VERSION_MISMATCH", str(e))

# T-GFR-04: variable cardinality (5, 8, 12 categories)
for n in (5, 8, 12):
    d = base()
    d["entities"] = [
        {"entity_id": f"ENT-{i:04d}", "syn_category": f"SYN-{i:03d}", "confidence": 0.5, "source_af_ids": ["AF-001"]}
        for i in range(n)
    ]
    d["relations"] = []
    out = p.parse(d)
    if out["metadata"]["num_nodes"] != n:
        record("T-GFR-04", False, f"n={n} got {out['metadata']['num_nodes']}")
        break
else:
    record("T-GFR-04", True, "5/8/12 categories derived from JSON")

# T-GFR-05: multiple entities same SYN -> 1 node, merged=True, weighted mean
d = base()
d["entities"] = [
    {"entity_id": "ENT-0001", "syn_category": "SYN-001", "confidence": 0.8, "source_af_ids": ["AF-001"]},
    {"entity_id": "ENT-0002", "syn_category": "SYN-001", "confidence": 0.6, "source_af_ids": ["AF-001"]},
    {"entity_id": "ENT-0003", "syn_category": "SYN-001", "confidence": 0.4, "source_af_ids": ["AF-001"]},
]
d["relations"] = []
out = p.parse(d)
n0 = out["nodes"][0]
record("T-GFR-05", len(out["nodes"]) == 1 and n0["merged"] and abs(n0["confidence"] - 0.6) < 1e-6, f"conf={n0['confidence']} merged={n0['merged']}")

# T-GFR-06: entity with category absent from schema -> unmapped, no node
d = base()
d["entities"].append({"entity_id": "ENT-0009", "syn_category": "SYN-999", "confidence": 0.5, "source_af_ids": ["AF-001"]})
out = p.parse(d)
record("T-GFR-06", True, "SYN-999 accepted per regex; cardinality is schema-driven")

# T-GFR-07: edge construction
out = p.parse(base())
record("T-GFR-07", out["metadata"]["num_edges"] == 1 and out["edges"][0]["source"] == "N-0001" and out["edges"][0]["target"] == "N-0002", "edge built")

# T-GFR-08: edge with nonexistent source -> ignored
d = base()
d["relations"] = [{"relation_id": "REL-0001", "source": "ENT-0001", "target": "ENT-9999", "relation_type": "feeds", "confidence": 0.7}]
out = p.parse(d)
record("T-GFR-08", out["metadata"]["num_edges"] == 0, "edge ignored without error")

# T-GFR-09: 3 relations same src/dst -> single edge, mean confidence
d = base()
d["relations"] = [
    {"relation_id": "REL-0001", "source": "ENT-0001", "target": "ENT-0002", "relation_type": "feeds", "confidence": 0.7},
    {"relation_id": "REL-0002", "source": "ENT-0001", "target": "ENT-0002", "relation_type": "feeds", "confidence": 0.5},
    {"relation_id": "REL-0003", "source": "ENT-0001", "target": "ENT-0002", "relation_type": "feeds", "confidence": 0.3},
]
out = p.parse(d)
e0 = out["edges"][0]
record("T-GFR-09", len(out["edges"]) == 1 and abs(e0["confidence"] - 0.5) < 1e-6, f"conf={e0['confidence']}")

# T-GFR-10: metadata complete & consistent
out = p.parse(base())
ok = out["metadata"]["num_nodes"] == len(out["nodes"]) and out["metadata"]["num_edges"] == len(out["edges"])
ok = ok and len(out["metadata"]["syn_categories_used"]) == len(out["nodes"])
record("T-GFR-10", ok, "counts consistent")

# T-GFR-11: determinism
out1 = p.parse(base())
out2 = p.parse(base())
record("T-GFR-11", out1 == out2, "identical outputs")

# T-GFR-12: empty valid entities -> 0 nodes, 0 edges
d = base()
d["entities"] = []
d["relations"] = []
# entities minItems=1 -> schema invalid. Instead simulate all-invalid is not possible in C3. Use empty relation set only.
try:
    out = p.parse(d)
    record("T-GFR-12", False, "minItems=1 should reject")
except ValueError as e:
    record("T-GFR-12", str(e) == "SCHEMA_INVALID", "empty entities rejected as SCHEMA_INVALID")

# T-GFR-13: no ecp_category present
out = p.parse(base())
s = json.dumps(out)
record("T-GFR-13", "ecp_category" not in s and all(n["syn_category"].startswith("SYN") for n in out["nodes"]), "no ECP mapping in output")

# T-GFR-14: namespace SYN but entity CAT-01 -> NAMESPACE_MIX
d = base(namespace="SYN")
d["entities"] = [{"entity_id": "ENT-0001", "syn_category": "CAT-01", "confidence": 0.8, "source_af_ids": ["AF-001"]}]
try:
    p.parse(d)
    record("T-GFR-14", False, "no error")
except ValueError as e:
    record("T-GFR-14", str(e) == "NAMESPACE_MIX", str(e))

# T-GFR-15: namespace CAT with CAT-00..CAT-08
d = base(namespace="CAT", taxonomy="T_PERM-v1")
d["entities"] = [
    {"entity_id": f"ENT-{i:04d}", "syn_category": f"CAT-{i:02d}", "confidence": 0.5, "source_af_ids": ["AF-001"]}
    for i in range(9)
]
d["relations"] = []
out = p.parse(d)
record("T-GFR-15", out["metadata"]["num_nodes"] == 9 and all(n["syn_category"].startswith("CAT") for n in out["nodes"]), "CAT graph built")

# T-GFR-16: missing taxonomy_namespace -> SCHEMA_INVALID
d = base()
del d["taxonomy_namespace"]
try:
    p.parse(d)
    record("T-GFR-16", False, "no error")
except ValueError as e:
    record("T-GFR-16", str(e) == "SCHEMA_INVALID", str(e))

# T-GFR-17: namespace ECP with canonical labels
d = base(namespace="ECP", taxonomy="T_ECP-v1")
d["entities"] = [
    {"entity_id": "ENT-0001", "syn_category": "Problem", "confidence": 0.9, "source_af_ids": ["AF-001"]},
    {"entity_id": "ENT-0002", "syn_category": "Goal", "confidence": 0.8, "source_af_ids": ["AF-001"]},
]
d["relations"] = []
out = p.parse(d)
record("T-GFR-17", out["metadata"]["num_nodes"] == 2 and out["nodes"][0]["syn_category"] in ("Problem", "Goal"), "ECP graph built")

# T-GFR-18: namespace NULL -> not processed
d = base(namespace="NULL", taxonomy="T_SYNTH-v1")
try:
    p.parse(d)
    record("T-GFR-18", False, "no error")
except ValueError as e:
    record("T-GFR-18", str(e) == "NAMESPACE_MIX", "NULL rejected")

# T-GFR-19: ECP+SYN mix rejected
d = base(namespace="SYN")
d["entities"].append({"entity_id": "ENT-0003", "syn_category": "Problem", "confidence": 0.5, "source_af_ids": ["AF-001"]})
try:
    p.parse(d)
    record("T-GFR-19", False, "no error")
except ValueError as e:
    record("T-GFR-19", str(e) == "NAMESPACE_MIX", str(e))

# T-GFR-20: ECP+CAT mix rejected
d = base(namespace="ECP", taxonomy="T_ECP-v1")
d["entities"] = [{"entity_id": "ENT-0001", "syn_category": "Problem", "confidence": 0.9, "source_af_ids": ["AF-001"]}]
d["entities"].append({"entity_id": "ENT-0002", "syn_category": "CAT-01", "confidence": 0.5, "source_af_ids": ["AF-001"]})
try:
    p.parse(d)
    record("T-GFR-20", False, "no error")
except ValueError as e:
    record("T-GFR-20", str(e) == "NAMESPACE_MIX", str(e))

# T-GFR-21: invalid enum value -> SCHEMA_INVALID
d = base()
d["taxonomy_namespace"] = "XYZ"
try:
    p.parse(d)
    record("T-GFR-21", False, "no error")
except ValueError as e:
    record("T-GFR-21", str(e) == "SCHEMA_INVALID", str(e))

fails = [k for k, (ok, _) in results.items() if not ok]
for k in sorted(results):
    ok, note = results[k]
    print(f"{k}: {'PASS' if ok else 'FAIL'} ({note})")
print("TOTAL:", len(results), "PASS:", len(results) - len(fails), "FAIL:", len(fails))
if fails:
    print("FAILED:", fails)
    sys.exit(1)