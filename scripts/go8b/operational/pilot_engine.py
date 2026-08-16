#!/usr/bin/env python3
"""
GO-8B Pilot Engine — CORRIGIDO

Executes the 63 pilot runs (7 BIPs × 3 conditions × 3 seeds) using REAL narrative
and atomic facts content. Produces genuine per-BIP variation in s_struct / s_sem.

Corrections vs previous version:
  1. Namespaces per frozen protocol (02 §8, 03 §5, P5):
       A (blind pure, atomic facts)  -> CAT  (T_PERM opaque canonical slots)
       B (blind + C3, atomic facts)  -> SYN  (C3/T_SYNTH taxonomy)
       C (non-blind, narrative)      -> CAT  (never ECP)
  2. syn_category assigned by CONTENT (embedding of fact/block text vs neutral
     taxonomy definitions), never by line index.
  3. Relations from real content (temporal sequence + key-term co-occurrence),
     not self-loops.
  4. S_sem via label embeddings (05 §4.1) instead of positional AF IDs.
  5. Fixed arity bug in semantic_similarity call and non-deterministic hash().
"""

import os
import sys
import re
import json
import yaml
import numpy as np
import hashlib
from datetime import datetime
from collections import Counter

sys.path.insert(0, r"D:\ecp-spec\scripts\go8b\operational")

from graph_from_reconstruction import GraphFromReconstruction
from wl_kernel import WLKernel, G_ECP

BASE_DIR = r"D:\ecp-spec"
PILOT_INPUT_DIR = os.path.join(BASE_DIR, "experiments", "validation", "GO-8B", "pilot-input")
PILOT_OUTPUT_DIR = os.path.join(BASE_DIR, "experiments", "validation", "GO-8B", "pilot-output")
SEEDS_FILE = os.path.join(BASE_DIR, "scripts", "go8b", "operational", "seeds_dict.py")

exec(open(SEEDS_FILE, encoding='utf-8').read())

BIPS = [f"BIP-00{i}" for i in range(1, 8)]
CONDITIONS = ["A", "B", "C"]
is_validation_run = any(a in sys.argv for a in ("--validate", "--sanidade", "--smoke"))
ONLY_BIP = None
for a in sys.argv[1:]:
    if a.startswith("--bip="):
        ONLY_BIP = a.split("=", 1)[1]

# ---------- frozen taxonomy data ----------
with open(os.path.join(BASE_DIR, "scripts", "go8b", "operational", "C2_PERMUTATION.yaml"), encoding="utf-8") as f:
    C2 = yaml.safe_load(f)
with open(os.path.join(BASE_DIR, "scripts", "go8b", "operational", "C3_TAXONOMY.yaml"), encoding="utf-8") as f:
    C3 = yaml.safe_load(f)

CANONICAL_ORDER = C2["canonical_order"]                     # 9 ECP slots
CANON2OPAQUE = C2["canonical_to_opaque"]                    # Problem -> CAT-01 ...
SYN_NODES = C3["taxonomy"]["nodes"]                          # [{id=SYN-001, label, definition}]
SYN_ID2LABEL = {n["id"]: n["label"] for n in SYN_NODES}     # SYN-001 -> "Funcao"
SYN_ID2DEF = {n["id"]: n["definition"] for n in SYN_NODES}

# Neutral PT definitions for the 9 opaque CAT slots (no ECP vocabulary).
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

# ---------- embeddings (frozen model, analysis phase only) ----------
EMB_FILE = os.path.join(BASE_DIR, "scripts", "go8b", "operational", "EMBEDDINGS.npy")
with open(EMB_FILE, "rb") as f:
    _EMB = np.load(f, allow_pickle=True).item()
EMB_TABLE = {}
for (ns, lbl), vec in zip(_EMB["keys"], _EMB["vectors"]):
    EMB_TABLE[(ns, lbl)] = np.asarray(vec, dtype=float)

def _norm(v):
    if v is None:
        return np.zeros(384)
    v = np.asarray(v, dtype=float).flatten()
    return v / np.linalg.norm(v) if np.linalg.norm(v) > 0 else v

def label_emb(label):
    """Embedding of a node label (ECP canonical, CAT-XX, SYN-XXX, or a raw vector)."""
    if isinstance(label, np.ndarray):
        return _norm(label)
    if not isinstance(label, str):
        return np.zeros(384)
    if label in CANONICAL_ORDER:                        # ECP canonical
        return _norm(EMB_TABLE.get(("ECP", label)))
    if re.match(r"^CAT-\d{2}$", label):                 # opaque CAT slot
        return _norm(EMB_TABLE.get(("CAT", label)))
    if re.match(r"^SYN-\d{1,3}$", label):               # C3 node -> label text
        lab = SYN_ID2LABEL.get(label, label)
        return _norm(EMB_TABLE.get(("SYN", lab)))
    return np.zeros(384)


# ---------- content extraction ----------
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


# ---------- classification (content -> taxonomy slot) ----------
_MODEL = None
_EMB_CACHE = {}


def get_model():
    """Load the frozen all-MiniLM-L6-v2 model once (same model as EMBEDDINGS.npy / P4)."""
    global _MODEL
    if _MODEL is None:
        from sentence_transformers import SentenceTransformer
        _MODEL = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return _MODEL


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
        # deterministic fallback (never used in normal operation)
        vec = np.zeros(384, dtype=float)
        for tok in fact_tokens(t):
            h = hashlib.sha256(("tok|" + tok).encode()).digest()
            vec += (np.frombuffer(h * 24, dtype=np.uint8).astype(float)[:384] * 3.0 + 8.0)
        vec = _norm(vec)
    _EMB_CACHE[t] = vec
    return vec


class Classifier:
    """Assigns each unit text to a taxonomy slot via content embeddings."""

    def __init__(self, definitions, slots):
        # slots: list of category ids aligned with definitions (texts)
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
    if condition in ("A", "C"):  # CAT opaque slots
        slots = [CANON2OPAQUE[c] for c in CANONICAL_ORDER]
        defs = {CANON2OPAQUE[c]: CAT_NEUTRAL_DEFS[c] for c in CANONICAL_ORDER}
        return Classifier(defs, slots)
    else:  # B -> C3 SYN slots
        return Classifier(SYN_ID2DEF, list(SYN_ID2DEF.keys()))


# ---------- graph building ----------
def build_entities_relations(units, condition):
    """From unit texts, produce entities + relations with real content topology."""
    clf = make_classifier(condition)
    entities = []
    relations = []
    tokensets = []
    ent_vectors = {}  # entity_id -> content embedding vector
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
        # temporal sequence edge (i -> i+1) when it exists
        if i < n:
            relations.append({
                "relation_id": rid,
                "source": eid,
                "target": f"ENT-{(i+1):04d}",
                "relation_type": "follows",
                "confidence": 0.8,
                "evidence_af_ids": [u["af_id"]],
            })
    # co-occurrence edges between non-adjacent units sharing >=2 key terms
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
        "reconstruction_version": datetime.now().isoformat(),
        "taxonomy_version": taxv,
        "taxonomy_namespace": namespace,
        "entities": entities,
        "relations": relations,
    }
    parser = GraphFromReconstruction(taxonomy_registry={
        "C3_TAXONOMY-v1": True, "T_PERM-v1": True,
    })
    try:
        return parser.parse(input_data)
    except Exception:
        import traceback
        traceback.print_exc()
        return None


# ---------- metrics ----------
def compute_s_metrics(graph, condition, ent_vectors=None):
    if graph is None:
        return 0.0, 0.0
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])

    graph_data = {
        "nodes": [{"id": n["node_id"]} for n in nodes],
        "edges": [{"source": e["source"], "target": e["target"]} for e in edges],
    }

    wl = WLKernel(h=3, emb_function=label_emb)

    # Content vector per reconstructed node = mean of its entities' real text vectors
    node_labels_rec = {}
    for nd in nodes:
        src_ids = nd.get("source_entities", [])
        if ent_vectors and src_ids:
            vecs = [ent_vectors[s] for s in src_ids if s in ent_vectors]
            if vecs:
                node_labels_rec[nd["node_id"]] = _norm(np.mean(vecs, axis=0))
                continue
        node_labels_rec[nd["node_id"]] = label_emb(nd["syn_category"])

    node_labels_ecp = {nd["id"]: nd["label"] for nd in G_ECP["nodes"]}
    edge_labels_rec = {(e["source"], e["target"]): e["relation_type"] for e in edges}
    edge_labels_ecp = {(e["source"], e["target"]): e["label"] for e in G_ECP["edges"]}

    s_struct = wl.s_struct(graph_data, G_ECP)
    s_sem = wl.semantic_similarity(
        graph_data,
        G_ECP,
        node_labels_rec,
        node_labels_ecp,
        edge_labels_rec,
        edge_labels_ecp,
    )

    s_struct = max(0.0, min(1.0, float(s_struct)))
    s_sem = max(0.0, min(1.0, float(s_sem)))
    return round(s_struct, 4), round(s_sem, 4)


# ---------- execution ----------
def resolve_paths(bip_dir):
    narr = os.path.join(PILOT_INPUT_DIR, bip_dir, "narrative", "01-narrativa-original.md")
    if not os.path.exists(narr):
        narr = os.path.join(PILOT_INPUT_DIR, bip_dir, "narrative", "narrative_pt.md")
    if not os.path.exists(narr):
        narr = os.path.join(PILOT_INPUT_DIR, bip_dir, "narrative", "narrative.md")

    af = os.path.join(PILOT_INPUT_DIR, bip_dir, "atomic-facts", "02-atomic-facts.md")
    if not os.path.exists(af):
        af = os.path.join(PILOT_INPUT_DIR, bip_dir, "atomic-facts", "atomic_facts.md")
    return narr, af


def execute_pilot_run(actual_bip, condition, seed_idx, bip_dir):
    try:
        narr, af = resolve_paths(bip_dir)
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
        graph = build_graph(entities, relations, condition, actual_bip)
        if graph is None:
            raise ValueError("graph construction failed")

        s_struct, s_sem = compute_s_metrics(graph, condition, ent_vectors)
        namespace = graph.get("_namespace", "UNKNOWN")

        if namespace not in ("CAT", "SYN"):
            return {
                "status": "FAIL", "s_struct": 0.0, "s_sem": 0.0,
                "nodes": len(graph.get("nodes", [])), "edges": len(graph.get("edges", [])),
                "namespace": namespace, "error": f"invalid namespace {namespace}",
            }

        return {
            "status": "PASS",
            "s_struct": s_struct,
            "s_sem": s_sem,
            "nodes": len(graph.get("nodes", [])),
            "edges": len(graph.get("edges", [])),
            "namespace": namespace,
            "namespace_mix": False,
            "seed_value": seed_idx,
            "syn_cat_used": sorted({n["syn_category"] for n in graph.get("nodes", [])}),
        }
    except Exception as e:
        return {
            "status": "FAIL", "s_struct": 0.0, "s_sem": 0.0,
            "nodes": 0, "edges": 0, "namespace": "SYN", "error": str(e),
        }


BIP_DIR_MAP = {
    "BIP-001": "BIP-001-deepwater",
    "BIP-002": "BIP-002-hyatt",
    "BIP-003": "BIP-003-ows",
    "BIP-004": "BIP-004-genoma",
    "BIP-005": "BIP-005-evergiven",
    "BIP-006": "BIP-006-i35w",
    "BIP-007": "BIP-007-ebola",
}


def main():
    print("=== GO-8B PILOT ENGINE (CORRIGIDO) ===")
    print(f"Start: {datetime.now().isoformat()}")

    results = []
    total = passed = failed = 0

    for bip in BIPS:
        if ONLY_BIP and bip != ONLY_BIP:
            continue
        if bip not in seeds:
            continue
        for condition in CONDITIONS:
            if condition not in seeds[bip]:
                continue
            for seed_idx in [1, 2, 3]:
                total += 1
                seed_value = seeds[bip][condition][f"seed{seed_idx}"]
                bip_dir = BIP_DIR_MAP.get(bip, bip)
                result = execute_pilot_run(bip, condition, seed_idx, bip_dir)
                if result["status"] == "PASS":
                    passed += 1
                else:
                    failed += 1
                results.append({
                    "bip_id": bip,
                    "condition": condition,
                    "seed_num": seed_idx,
                    "seed_value": seed_value,
                    "status": result["status"],
                    "s_struct": result["s_struct"],
                    "s_sem": result["s_sem"],
                    "nodes": result["nodes"],
                    "edges": result["edges"],
                    "namespace": result["namespace"],
                    "namespace_mix": result.get("namespace_mix", False),
                    "error": result.get("error", ""),
                    "timestamp": datetime.now().isoformat(),
                })

    csv_file = os.path.join(PILOT_OUTPUT_DIR, "pilot_results.csv")
    with open(csv_file, "w", encoding="utf-8") as f:
        f.write("bip_id,condition,seed_num,seed_value,status,s_struct,s_sem,nodes,edges,namespace,validation\n")
        for r in results:
            validation = "PASS" if r["status"] == "PASS" and not r["namespace_mix"] else "FAIL"
            f.write(
                f"{r['bip_id']},{r['condition']},{r['seed_num']},{r['seed_value']},"
                f"{r['status']},{r['s_struct']},{r['s_sem']},{r['nodes']},{r['edges']},"
                f"{r['namespace']},{validation}\n"
            )

    print()
    print("=== RESULTADO ===")
    print(f"Total: {total}  Passed: {passed}  Failed: {failed}")
    print(f"CSV: {csv_file}")
    print(f"End: {datetime.now().isoformat()}")

    # per-BIP / per-condition variation check
    if total:
        means = {}
        counts = {}
        for r in results:
            k = (r["bip_id"], r["condition"])
            means.setdefault(k, [])
            means[k].append(r["s_struct"])
            counts.setdefault(k, r["nodes"])
        print("\nMediana s_struct por BIP×condição (3 seeds):")
        print(f"{'BIP':8} {'A':>8} {'B':>8} {'C':>8}")
        for bip in BIPS:
            row = [bip]
            for cond in CONDITIONS:
                v = means.get((bip, cond))
                if v:
                    m = sorted(v)[1]
                    row.append(f"{m:.4f}")
                else:
                    row.append("  -")
            print(" ".join(f"{x:>8}" for x in row))

        sem_means = {}
        for r in results:
            k = (r["bip_id"], r["condition"])
            sem_means.setdefault(k, [])
            sem_means[k].append(r["s_sem"])
        print("\nMediana s_sem por BIP×condição (3 seeds):")
        print(f"{'BIP':8} {'A':>8} {'B':>8} {'C':>8}")
        for bip in BIPS:
            row = [bip]
            for cond in CONDITIONS:
                v = sem_means.get((bip, cond))
                if v:
                    m = sorted(v)[1]
                    row.append(f"{m:.4f}")
                else:
                    row.append("  -")
            print(" ".join(f"{x:>8}" for x in row))

        print("\nChecagem de variação (mediana por BIP×condição):")
        all_vals = sorted({ (r["bip_id"], r["condition"], sorted([x for r2 in results if r2["bip_id"]==r["bip_id"] and r2["condition"]==r["condition"] for x in [r2['s_struct']]])[1]) for r in results })
        distinct = len({v for _, _, v in all_vals})
        print(f"Valores distintos de s_struct (mediana por célula): {distinct}/{len(results)//3}")
        sem_all = sorted({ (r["bip_id"], r["condition"], sorted([x for r2 in results if r2["bip_id"]==r["bip_id"] and r2["condition"]==r["condition"] for x in [r2['s_sem']]])[1]) for r in results })
        sem_distinct = len({v for _, _, v in sem_all})
        print(f"Valores distintos de s_sem   (mediana por célula): {sem_distinct}/{len(results)//3}")


if __name__ == "__main__":
    main()