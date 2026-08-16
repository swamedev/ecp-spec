# -*- coding: utf-8 -*-
"""
GO-8D-NC — graph_from_reconstruction (self-contained).

Graph builder from a reconstruction input: schema validation, namespace checks,
collapse by synthetic category, edge construction. P3 (D-03 §3.2) granularity
standardization is handled at the metric layer (common ECP reference for DV3).

No runtime dependency on GO-8B/GO-8C/GO-8D. Self-contained.
"""
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
                    "syn_category": {"type": "string"},
                    "confidence": {"type": "number", "minimum": 0.0, "maximum": 1.0},
                    "source_af_ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},
                },
            },
        },
        "relations": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["relation_id", "source", "target", "relation_type", "confidence"],
                "properties": {
                    "relation_id": {"type": "string"},
                    "source": {"type": "string"},
                    "target": {"type": "string"},
                    "relation_type": {"type": "string"},
                    "confidence": {"type": "number", "minimum": 0.0, "maximum": 1.0},
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
        self.taxonomy_registry = taxonomy_registry or {}

    def parse(self, input_data):
        try:
            validate(instance=input_data, schema=SCHEMA)
        except ValidationError:
            raise ValueError("SCHEMA_INVALID")

        if input_data.get("taxonomy_version") not in self.taxonomy_registry:
            raise ValueError("VERSION_MISMATCH")

        ns = input_data["taxonomy_namespace"]
        if ns not in ("ECP", "CAT", "SYN", "NULL"):
            raise ValueError("SCHEMA_INVALID")
        if ns == "NULL":
            raise ValueError("NAMESPACE_MIX")

        entities = input_data["entities"]
        rels = input_data.get("relations", [])

        for e in entities:
            if namespace_of(e["syn_category"]) != ns:
                raise ValueError("NAMESPACE_MIX")

        node_map = {}
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

        ent_to_cat = {e["entity_id"]: e["syn_category"] for e in entities}
        edge_map = {}
        for r in rels:
            s_cat = ent_to_cat.get(r["source"])
            t_cat = ent_to_cat.get(r["target"])
            if s_cat is None or t_cat is None:
                continue
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

        nodes = []
        for cat, nd in node_map.items():
            nodes.append({
                "node_id": nd["node_id"],
                "syn_category": cat,
                "confidence": round(nd["_conf_sum"] / nd["_conf_n"], 6),
                "source_entities": nd["source_entities"],
                "merged": len(nd["source_entities"]) > 1,
            })

        edges = []
        for (s, t, rt), ed in edge_map.items():
            edges.append({
                "edge_id": ed["edge_id"],
                "source": ed["source"],
                "target": ed["target"],
                "relation_type": rt,
                "confidence": round(ed["_conf_sum"] / ed["_conf_n"], 6),
                "source_relations": ed["source_relations"],
            })

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
            "_namespace": ns,
        }


if __name__ == "__main__":
    sample = {
        "case_id": "SX-999",
        "reconstruction_version": "2026-08-15T00:00:00Z",
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
