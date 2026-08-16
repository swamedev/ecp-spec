import json
import re
from jsonschema import validate, ValidationError

SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "ReconstructionInput",
    "type": "object",
    "required": ["case_id", "reconstruction_version", "entities", "relations", "taxonomy_version", "taxonomy_namespace"],
    "properties": {
        "case_id": {"type": "string", "pattern": "^SX-\\d{3}$"},
        "reconstruction_version": {"type": "string", "format": "date-time"},
        "taxonomy_version": {"type": "string"},
        "taxonomy_namespace": {"type": "string", "enum": ["ECP", "CAT", "SYN", "NULL"]},
        "entities": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": ["entity_id", "syn_category", "confidence", "source_af_ids"],
                "properties": {
                    "entity_id": {"type": "string", "pattern": "^ENT-\\d{4}$"},
                    "syn_category": {
                        "type": "string",
                        "pattern": "^(CAT-\\d{2}|SYN-\\d+|Problem|Goal|Claim|Knowledge|Assumption|Evidence|Decision|State|Artifact)$",
                    },
                    "confidence": {"type": "number", "minimum": 0.0, "maximum": 1.0},
                    "source_af_ids": {"type": "array", "items": {"type": "string", "pattern": "^AF-\\d{3}$"}, "minItems": 1},
                    "attributes": {"type": "object", "additionalProperties": {"type": "string"}},
                },
            },
        },
        "relations": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["relation_id", "source", "target", "relation_type", "confidence"],
                "properties": {
                    "relation_id": {"type": "string", "pattern": "^REL-\\d{4}$"},
                    "source": {"type": "string", "pattern": "^ENT-\\d{4}$"},
                    "target": {"type": "string", "pattern": "^ENT-\\d{4}$"},
                    "relation_type": {"type": "string"},
                    "confidence": {"type": "number", "minimum": 0.0, "maximum": 1.0},
                    "evidence_af_ids": {"type": "array", "items": {"type": "string", "pattern": "^AF-\\d{3}$"}},
                },
            },
        },
    },
}

ECP_LABELS = {"Problem", "Goal", "Claim", "Knowledge", "Assumption", "Evidence", "Decision", "State", "Artifact"}


def namespace_of(syn_category):
    if syn_category in ECP_LABELS:
        return "ECP"
    if re.match(r"^CAT-\d{2}$", syn_category):
        return "CAT"
    if re.match(r"^SYN-\d+$", syn_category):
        return "SYN"
    return None


class GraphFromReconstruction:
    def __init__(self, taxonomy_registry=None):
        # taxonomy_registry: dict taxonomy_version -> available (for VERSION_MISMATCH)
        self.taxonomy_registry = taxonomy_registry or {}

    def parse(self, input_data):
        # 1. Schema validation
        try:
            validate(instance=input_data, schema=SCHEMA)
        except ValidationError:
            raise ValueError("SCHEMA_INVALID")

        # Version check
        if input_data.get("taxonomy_version") not in self.taxonomy_registry:
            raise ValueError("VERSION_MISMATCH")

        # Namespace validation (R5 M-1)
        ns = input_data["taxonomy_namespace"]
        if ns not in ("ECP", "CAT", "SYN", "NULL"):
            raise ValueError("SCHEMA_INVALID")
        if ns == "NULL":
            raise ValueError("NAMESPACE_MIX")  # C4/T_NULL not processed by this parser

        declared = ns
        entities = input_data["entities"]
        rels = input_data.get("relations", [])

        # All syn_category must belong to declared namespace
        for e in entities:
            en_ns = namespace_of(e["syn_category"])
            if en_ns is None or en_ns != declared:
                raise ValueError("NAMESPACE_MIX")

        # 2. Grouping by synthetic category
        node_map = {}  # syn_category -> {node_id, syn_category, confidence (sum), n, source_entities}
        for e in entities:
            cat = e["syn_category"]
            if cat not in node_map:
                node_map[cat] = {
                    "node_id": f"N-{len(node_map) + 1:04d}",
                    "syn_category": cat,
                    "_conf_sum": 0.0,
                    "_conf_n": 0,
                    "source_entities": [],
                }
            node_map[cat]["_conf_sum"] += e["confidence"]
            node_map[cat]["_conf_n"] += 1
            node_map[cat]["source_entities"].append(e["entity_id"])

        # 3. Edge construction
        ent_to_cat = {e["entity_id"]: e["syn_category"] for e in entities}
        edge_map = {}  # (src_cat, tgt_cat, rel_type) -> {..., _conf_sum, _conf_n, source_relations}
        for r in rels:
            s_cat = ent_to_cat.get(r["source"])
            t_cat = ent_to_cat.get(r["target"])
            if s_cat is None or t_cat is None:
                continue  # T-GFR-08: edge with missing source ignored
            key = (s_cat, t_cat, r["relation_type"])
            if key not in edge_map:
                edge_map[key] = {
                    "edge_id": f"E-{len(edge_map) + 1:04d}",
                    "source": node_map[s_cat]["node_id"],
                    "target": node_map[t_cat]["node_id"],
                    "relation_type": r["relation_type"],
                    "_conf_sum": 0.0,
                    "_conf_n": 0,
                    "source_relations": [],
                }
            edge_map[key]["_conf_sum"] += r["confidence"]
            edge_map[key]["_conf_n"] += 1
            edge_map[key]["source_relations"].append(r["relation_id"])

        # 4. Normalize confidence
        nodes = []
        for cat, nd in node_map.items():
            nodes.append(
                {
                    "node_id": nd["node_id"],
                    "syn_category": cat,
                    "confidence": round(nd["_conf_sum"] / nd["_conf_n"], 6),
                    "source_entities": nd["source_entities"],
                    "merged": len(nd["source_entities"]) > 1,
                }
            )

        edges = []
        for (s, t, rt), ed in edge_map.items():
            edges.append(
                {
                    "edge_id": ed["edge_id"],
                    "source": ed["source"],
                    "target": ed["target"],
                    "relation_type": rt,
                    "confidence": round(ed["_conf_sum"] / ed["_conf_n"], 6),
                    "source_relations": ed["source_relations"],
                }
            )

        # 5. Metadata
        metadata = {
            "num_nodes": len(nodes),
            "num_edges": len(edges),
            "syn_categories_used": [n["syn_category"] for n in nodes],
            "unmapped_entities": [],
        }

        return {
            "case_id": input_data["case_id"],
            "graph_version": input_data["reconstruction_version"],
            "nodes": nodes,
            "edges": edges,
            "metadata": metadata,
            "_namespace": declared,
        }


if __name__ == "__main__":
    sample = {
        "case_id": "SX-999",
        "reconstruction_version": "2026-08-12T00:00:00Z",
        "taxonomy_version": "C3_TAXONOMY-v1",
        "taxonomy_namespace": "SYN",
        "entities": [
            {"entity_id": "ENT-0001", "syn_category": "SYN-001", "confidence": 0.8, "source_af_ids": ["AF-001"]},
            {"entity_id": "ENT-0002", "syn_category": "SYN-002", "confidence": 0.6, "source_af_ids": ["AF-001"]},
        ],
        "relations": [
            {"relation_id": "REL-0001", "source": "ENT-0001", "target": "ENT-0002", "relation_type": "feeds", "confidence": 0.7},
        ],
    }
    p = GraphFromReconstruction(taxonomy_registry={"C3_TAXONOMY-v1": True})
    print(json.dumps(p.parse(sample), indent=2))