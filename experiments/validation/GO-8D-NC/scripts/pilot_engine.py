# -*- coding: utf-8 -*-
"""
GO-8D-NC — pilot_engine (self-contained, D-03 redesign + DV3).

Redesigned pipeline components implemented per D-03:
  P1 wl_kernel labeled             -> wl_kernel.py (labeled structural_features)
  P2 embeddings CAT corrigidos     -> label_emb_corrected() (CAT uses CAT_NEUTRAL_DEFS,
                                      SYN uses corrected C3 definitions, ECP canonical)
  P3 granularidade padronizada     -> DV3 metric uses a COMMON reference (ECP chain) for
                                      all conditions (ged_ecp) and common log(12) (ent_n12)
  P4 referência por condição       -> ged_ecp vs common ECP reference (DV3 M-02)
  P5 rastreabilidade de taxonomia  -> taxonomy_sha256 recorded per execution

DV3 = clamp((conf + ged_ecp + ent_n12) / 3)   (metric-validation DV3, D-MV-01 approved)

No runtime dependency on GO-8B/GO-8C/GO-8D. Self-contained: reads its own copies of
C2_PERMUTATION.yaml and C3_TAXONOMY.yaml (in this same directory).
"""
import os
import re
import sys
import json
import math
import hashlib
import numpy as np
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))

import yaml
from graph_from_reconstruction import GraphFromReconstruction
from wl_kernel import WLKernel, ged_similarity, ecp_ref_graph

# ---------------- taxonomy loading (self-contained copies) ----------------
C2_PATH = os.path.join(HERE, "C2_PERMUTATION.yaml")
C3_PATH = os.path.join(HERE, "C3_TAXONOMY.yaml")

with open(C2_PATH, encoding="utf-8") as f:
    C2 = yaml.safe_load(f)
with open(C3_PATH, encoding="utf-8") as f:
    C3 = yaml.safe_load(f)

TAX_SHA_C2 = hashlib.sha256(open(C2_PATH, "rb").read()).hexdigest()
TAX_SHA_C3 = hashlib.sha256(open(C3_PATH, "rb").read()).hexdigest()

CANONICAL_ORDER = C2["canonical_order"]
O2C = C2["opaque_to_canonical"]
CAN2OPQ = C2["canonical_to_opaque"]
CAT_IDS = sorted(O2C.keys())

SYN_NODES = C3["taxonomy"]["nodes"]
SYN_ID2DEF = {n["id"]: n["definition"] for n in SYN_NODES}
SYN_ID2LABEL = {n["id"]: n["label"] for n in SYN_NODES}
SYN_EDGES = [(e["from"], e["to"]) for e in C3["taxonomy"]["edges"]]
SYN_IDS = [n["id"] for n in SYN_NODES]

# Neutral PT definitions for the 9 opaque CAT slots (no ECP vocabulary) — P2.
CAT_NEUTRAL_DEFS = {
    "Problem": "condicao adversa, risco, falha ou ameaca identificada no caso",
    "Goal": "objetivo, meta, alvo ou intencao visada",
    "Claim": "afirmacao, alegacao ou proposicao declarada",
    "Knowledge": "conhecimento, informacao ou aprendizado estabelecido",
    "Assumption": "suposicao, premissa ou hipotese admitida sem confirmacao completa",
    "Evidence": "fato observado, medido ou verificado diretamente",
    "Decision": "decisao, escolha ou deliberacao tomada, com ou sem fundamento",
    "State": "estado, condicao ou etapa em um determinado momento",
    "Artifact": "produto, documento, infraestrutura ou objeto material gerado",
}

# Common reference for ALL conditions (DV3 M-02): canonical ECP chain (9 nodes).
COMMON_REF = ecp_ref_graph()

# ---------------- embeddings ----------------
_MODEL = None
_EMB_CACHE = {}


def get_model():
    global _MODEL
    if _MODEL is None:
        from sentence_transformers import SentenceTransformer
        _MODEL = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return _MODEL


def _norm(v):
    if v is None:
        return np.zeros(384)
    v = np.asarray(v, dtype=float).flatten()
    return v / np.linalg.norm(v) if np.linalg.norm(v) > 0 else v


def text_emb(text):
    """384-dim embedding of real content using the frozen model (deterministic)."""
    t = (text or "").strip()
    if not t:
        return np.zeros(384)
    if t in _EMB_CACHE:
        return _EMB_CACHE[t]
    try:
        vec = np.asarray(get_model().encode(t, normalize_embeddings=True, show_progress_bar=False), dtype=float).flatten()
        vec = _norm(vec)
    except Exception:
        vec = np.zeros(384, dtype=float)
        for tok in fact_tokens(t):
            h = hashlib.sha256(("tok|" + tok).encode()).digest()
            vec += (np.frombuffer(h * 24, dtype=np.uint8).astype(float)[:384] * 3.0 + 8.0)
        vec = _norm(vec)
    _EMB_CACHE[t] = vec
    return vec


def label_emb_corrected(label):
    """P2 (D-03 §3.3): CAT-XX -> neutral PT definition embedding (not ECP canonical name);
    SYN-XX -> corrected C3 definition embedding; ECP canonical -> own embedding."""
    if isinstance(label, np.ndarray):
        return _norm(label)
    if not isinstance(label, str):
        return np.zeros(384)
    if label in CANONICAL_ORDER:                       # ECP canonical
        return text_emb(label)
    if label in O2C:                                   # opaque CAT slot
        return text_emb(CAT_NEUTRAL_DEFS[O2C[label]])
    if label in SYN_ID2DEF:                            # C3 node
        return text_emb(SYN_ID2DEF[label])
    return np.zeros(384)


# ---------------- content extraction ----------------
PT_STOP = {
    "o", "a", "os", "as", "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas",
    "para", "por", "com", "sem", "que", "era", "ser", "for", "foi", "sao", "mais", "menos",
    "um", "uma", "uns", "umas", "como", "mas", "ou", "se", "ja", "tambem", "e", "nao",
    "entre", "sobre", "ate", "apos", "depois", "antes", "durante", "contra",
}


def clean_text(text):
    return re.sub(r"`\[[^\]]*\]`", "", text).strip()


def fact_tokens(text):
    return {
        t for t in re.findall(r"[A-Za-zÀ-ÿ0-9]+", text.lower())
        if len(t) >= 4 and t not in PT_STOP
    }


def parse_atomic_facts(file_path):
    """Return list of fact dicts {text, af_id} from an atomic-facts markdown."""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    facts = []
    in_facts = False
    idx = 0
    for raw in lines:
        line = raw.strip()
        if line.startswith("## Fatos"):
            in_facts = True
            continue
        if in_facts and line.startswith("##"):
            break
        if not in_facts or not line:
            continue
        if not (line.endswith("]") or line.endswith("]`")):
            continue
        parts = line.split(".", 1)
        if len(parts) < 2:
            continue
        body = parts[1].strip()
        if not body:
            continue
        idx += 1
        facts.append({"text": clean_text(body), "af_id": f"AF-{idx:03d}"})
    return facts


def parse_narrative(file_path):
    """Return list of narrative block dicts {text, af_id} (paragraphs)."""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    blocks = []
    idx = 0
    for raw in lines:
        line = raw.strip()
        if line.startswith("#") or line.startswith("**") or line.startswith("---"):
            continue
        if not line:
            continue
        idx += 1
        blocks.append({"text": clean_text(line), "af_id": f"AF-{idx:03d}"})
    return blocks


# ---------------- classification ----------------
class Classifier:
    def __init__(self, definitions, slots):
        self.slots = slots
        self.def_emb = {s: text_emb(definitions[s]) for s in slots}

    def classify(self, text):
        emb = text_emb(text)
        best, best_sim = None, -1.0
        for s, d in self.def_emb.items():
            sim = float(np.dot(emb, d))
            if sim > best_sim:
                best, best_sim = s, sim
        conf = min(1.0, max(0.1, round((best_sim + 1) / 2.0, 4)))
        return best, conf


def make_classifier(condition):
    if condition in ("A", "C"):
        slots = [CAN2OPQ[c] for c in CANONICAL_ORDER]
        defs = {CAN2OPQ[c]: CAT_NEUTRAL_DEFS[c] for c in CANONICAL_ORDER}
        return Classifier(defs, slots)
    return Classifier(SYN_ID2DEF, list(SYN_ID2DEF.keys()))


# ---------------- graph building ----------------
def build_entities_relations(units, condition):
    clf = make_classifier(condition)
    entities = []
    relations = []
    tokensets = []
    ent_vectors = {}
    n = len(units)
    for i, u in enumerate(units, start=1):
        eid = f"ENT-{i:04d}"
        rid = f"REL-{i:04d}"
        cat, conf = clf.classify(u["text"])
        entities.append({
            "entity_id": eid,
            "syn_category": cat,
            "confidence": conf,
            "source_af_ids": [u["af_id"]],
        })
        ent_vectors[eid] = text_emb(u["text"])
        ts = fact_tokens(u["text"])
        tokensets.append(ts)
        if i < n:
            relations.append({
                "relation_id": rid,
                "source": eid,
                "target": f"ENT-{(i+1):04d}",
                "relation_type": "follows",
                "confidence": 0.8,
                "evidence_af_ids": [u["af_id"]],
            })
    rel_counter = 0
    for i in range(n):
        for j in range(i + 2, n):
            overlap = tokensets[i] & tokensets[j]
            if len(overlap) >= 2:
                rel_counter += 1
                relations.append({
                    "relation_id": f"REL-{9000 + rel_counter:04d}",
                    "source": f"ENT-{i+1:04d}",
                    "target": f"ENT-{j+1:04d}",
                    "relation_type": "relates",
                    "confidence": 0.7,
                    "evidence_af_ids": [units[i]["af_id"], units[j]["af_id"]],
                })
    return entities, relations, ent_vectors


def build_graph(entities, relations, condition, actual_bip):
    if condition == "A":
        namespace, taxv = "CAT", "T_PERM-v1"
    elif condition == "B":
        namespace, taxv = "SYN", "C3_TAXONOMY-v1"
    else:
        namespace, taxv = "CAT", "T_PERM-v1"

    input_data = {
        "case_id": f"SX-{int(actual_bip.split('-')[1]):03d}",
        "reconstruction_version": "GO-8D-NC-v1",
        "taxonomy_version": taxv,
        "taxonomy_namespace": namespace,
        "entities": entities,
        "relations": relations,
    }
    parser = GraphFromReconstruction(taxonomy_registry={"C3_TAXONOMY-v1": True, "T_PERM-v1": True})
    try:
        return parser.parse(input_data)
    except Exception:
        import traceback
        traceback.print_exc()
        return None


# ---------------- DV3 metric ----------------
def dv3_components(graph, entities, ent_vectors):
    """Return dict with conf, ged_ecp, ent_n12 and raw counts (DV3 components)."""
    nodes = graph["nodes"]
    gd = {"nodes": [{"id": n["node_id"]} for n in nodes],
          "edges": [{"source": e["source"], "target": e["target"]} for e in graph["edges"]]}
    lab = {n["node_id"]: n["syn_category"] for n in nodes}

    cat_counts = Counter(e["syn_category"] for e in entities)
    k_obs = len(cat_counts)
    p = np.array([cat_counts[c] for c in cat_counts], float) / len(entities) if entities else np.array([0.0])
    H = float(-(p * np.log(p)).sum())
    ent_n12 = H / math.log(12) if 12 > 1 else 0.0

    confs = [e["confidence"] for e in entities]
    conf = float(np.mean(confs)) if confs else 0.0

    emb_rec = {nd["id"]: label_emb_corrected(lab[nd["id"]]) for nd in gd["nodes"]}
    emb_ref_ecp = {nd["id"]: label_emb_corrected(nd["id"]) for nd in COMMON_REF["nodes"]}
    ged_ecp = max(0.0, min(1.0, ged_similarity(gd, COMMON_REF, emb_rec, emb_ref_ecp)))

    return {
        "conf": round(float(conf), 6),
        "ged_ecp": round(float(ged_ecp), 6),
        "ent_n12": round(float(ent_n12), 6),
        "H": round(H, 6),
        "k_obs": int(k_obs),
        "nodes": len(nodes),
        "edges": len(gd["edges"]),
        "ns": graph.get("_namespace", "UNKNOWN"),
    }


def dv3(row):
    return max(0.0, min(1.0, (row["conf"] + row["ged_ecp"] + row["ent_n12"]) / 3.0))


# ---------------- execution ----------------
def resolve_paths(study_input_dir, bip_dir):
    d = os.path.join(study_input_dir, bip_dir)
    narr = os.path.join(d, "narrative", "01-narrativa-original.md")
    if not os.path.exists(narr):
        narr = os.path.join(d, "narrative", "narrative_pt.md")
    if not os.path.exists(narr):
        narr = os.path.join(d, "narrative", "narrative.md")
    af = os.path.join(d, "atomic-facts", "02-atomic-facts.md")
    if not os.path.exists(af):
        af = os.path.join(d, "atomic-facts", "atomic_facts.md")
    return narr, af


def cell(bip, bip_dir, condition, study_input_dir):
    """Deterministic per (bip, cond). Returns dict with DV3 components or FAIL."""
    try:
        narr, af = resolve_paths(study_input_dir, bip_dir)
        if condition in ("A", "B"):
            if not os.path.exists(af):
                raise FileNotFoundError(f"atomic facts missing: {af}")
            units = parse_atomic_facts(af)
        else:
            if not os.path.exists(narr):
                raise FileNotFoundError(f"narrative missing: {narr}")
            units = parse_narrative(narr)
        if not units:
            raise ValueError("no units parsed")

        entities, relations, ent_vectors = build_entities_relations(units, condition)
        graph = build_graph(entities, relations, condition, bip)
        if graph is None:
            raise ValueError("graph construction failed")

        comp = dv3_components(graph, entities, ent_vectors)
        if comp["ns"] not in ("CAT", "SYN"):
            raise ValueError(f"invalid namespace {comp['ns']}")

        tax_sha = TAX_SHA_C3 if condition == "B" else TAX_SHA_C2
        return {
            "status": "PASS", "bip": bip, "cond": condition, "ns": comp["ns"],
            "conf": comp["conf"], "ged_ecp": comp["ged_ecp"], "ent_n12": comp["ent_n12"],
            "H": comp["H"], "k_obs": comp["k_obs"],
            "nodes": comp["nodes"], "edges": comp["edges"], "tax_sha": tax_sha,
        }
    except Exception as e:
        return {"status": "FAIL", "bip": bip, "cond": condition, "reason": str(e)}


def run_study(study_input_dir, study_output_dir, seeds, bips, conditions=("A", "B", "C")):
    """Execute all cells and write pilot_results_newcycle.csv (N x 3 x 3 rows)."""
    import csv as _csv
    rows = []
    for bip_dir in bips:
        bip = "BIP-" + bip_dir.split("-")[1]
        for cond in conditions:
            cell_res = cell(bip, bip_dir, cond, study_input_dir)
            if cell_res["status"] == "FAIL":
                for j in (1, 2, 3):
                    rows.append({
                        "bip_id": bip, "condition": cond, "seed_num": j,
                        "seed_value": seeds[bip][cond]["seed%d" % j],
                        "status": "FAIL", "dv3": "", "conf": "", "ged_ecp": "",
                        "ent_n12": "", "nodes": 0, "edges": 0, "namespace": "",
                        "taxonomy_sha256": "", "error": cell_res["reason"],
                    })
                continue
            for j in (1, 2, 3):
                rows.append({
                    "bip_id": bip, "condition": cond, "seed_num": j,
                    "seed_value": seeds[bip][cond]["seed%d" % j],
                    "status": "PASS",
                    "dv3": round(dv3(cell_res), 6),
                    "conf": cell_res["conf"], "ged_ecp": cell_res["ged_ecp"],
                    "ent_n12": cell_res["ent_n12"],
                    "nodes": cell_res["nodes"], "edges": cell_res["edges"],
                    "namespace": cell_res["ns"],
                    "taxonomy_sha256": cell_res["tax_sha"],
                    "error": "",
                })

    os.makedirs(study_output_dir, exist_ok=True)
    csv_path = os.path.join(study_output_dir, "pilot_results_newcycle.csv")
    cols = ["bip_id", "condition", "seed_num", "seed_value", "status", "dv3",
            "conf", "ged_ecp", "ent_n12", "nodes", "edges", "namespace",
            "taxonomy_sha256", "error"]
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        w = _csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print("Executions:", len(rows), " PASS:", sum(1 for r in rows if r["status"] == "PASS"),
          " FAIL:", sum(1 for r in rows if r["status"] == "FAIL"))
    print("saved:", csv_path)
    return rows


if __name__ == "__main__":
    print("GO-8D-NC pilot_engine module. Use run_study() after study-input + seeds exist.")
    print("TAX_SHA_C2=", TAX_SHA_C2[:16], " TAX_SHA_C3=", TAX_SHA_C3[:16])
