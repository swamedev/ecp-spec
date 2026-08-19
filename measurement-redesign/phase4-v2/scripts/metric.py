# -*- coding: utf-8 -*-
"""
MR-C7 phase4 — metric.py (componentes DV-REDESIGN; protocolo §7, M-REDESIGN-01-SPEC-A).

Lê outputs/reconstruction_graphs.json e computa, por caso × estado:
  conf      = F1(nós, arestas) entre o grafo da reconstrução e o grafo de verdade do
              estado (§7.2/§7.4) — média(F1 nós, F1 arestas), média de 3 seeds (§7.1).
  ged_ref   = s_struct (WL-kernel do engine congelado, hashing de estrutura, numpy
              puro, SEM rótulos de categoria) contra a referência DATA-DRIVEN (§7.3),
              construída pelo método da Fase B (consenso MST ponderado por confiança)
              sobre as reconstruções V0 dos 24 casos-base.
  div_metric= H / log(K), K = nº de categorias distintas nas entidades (§7.2); K<=1 -> 0.
  DV_REDESIGN = (conf + ged_ref + div_metric) / 3   (pesos 1:1:1, aritmética).

NÃO importa labelers.py nem reconstruction.py (standalone). NÃO lê texto de
candidatos. Usa apenas grafos e contagens (inputs fechados — addendum §5.1).
"""
import os
import json
import math
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUTS = os.path.join(HERE, "..", "outputs")

FROZEN_SCRIPTS = os.path.join(HERE, "..", "..", "..", "experiments", "validation",
                              "GO-8D-NC", "scripts")
sys.path.insert(0, FROZEN_SCRIPTS)
from wl_kernel import WLKernel  # noqa: E402   (arquivo congelado, somente leitura)

WL_H = 3


def view(graph):
    return {
        "nodes": [{"id": n["node_id"]} for n in graph["nodes"]],
        "edges": [{"source": e["source"], "target": e["target"]} for e in graph["edges"]],
    }


def f1_nodes_m(rec, truth):
    a = set(n["syn_category"] for n in rec["nodes"])
    b = set(n["syn_category"] for n in truth["nodes"])
    if not a or not b:
        return 0.0
    inter = len(a & b)
    p = inter / len(a)
    r = inter / len(b)
    return 2 * p * r / (p + r) if (p + r) else 0.0


def f1_edges_m(rec, truth):
    a = set((e["source"], e["target"], e["relation_type"]) for e in rec["edges"])
    b = set((e["source"], e["target"], e["relation_type"]) for e in truth["edges"])
    if not a or not b:
        return 0.0
    inter = len(a & b)
    p = inter / len(a)
    r = inter / len(b)
    return 2 * p * r / (p + r) if (p + r) else 0.0


def conf_m(rec, truth):
    return (f1_nodes_m(rec, truth) + f1_edges_m(rec, truth)) / 2.0


def div_m(cat_counts):
    k = len(cat_counts)
    if k <= 1:
        return 0.0
    total = sum(cat_counts.values())
    H = 0.0
    for c in cat_counts.values():
        p = c / total
        H -= p * math.log(p)
    return H / math.log(k)


def build_data_driven_reference(v0_graphs):
    """Consenso MST ponderado por confiança sobre as reconstruções V0 (§7.3, Fase B)."""
    node_set = set()
    weights = {}
    for g in v0_graphs:
        for n in g["nodes"]:
            node_set.add(n["syn_category"])
        for e in g["edges"]:
            key = tuple(sorted([e["source"], e["target"]]))
            weights[key] = weights.get(key, 0.0) + e["confidence"]

    # Maximum Spanning Tree (Kruskal) sobre as arestas presentes com peso > 0.
    parent = {n: n for n in node_set}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    mst_edges = []
    for (u, v), w in sorted(weights.items(), key=lambda kv: -kv[1]):
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
            mst_edges.append((u, v))

    ref = {
        "nodes": [{"node_id": n, "syn_category": n, "confidence": 1.0} for n in sorted(node_set)],
        "edges": [{"source": u, "target": v, "relation_type": "consensus",
                   "confidence": 1.0} for (u, v) in mst_edges],
    }
    return ref, {"num_nodes": len(node_set), "num_mst_edges": len(mst_edges),
                 "num_edge_instances": len(weights)}


def main():
    with open(os.path.join(OUTPUTS, "reconstruction_graphs.json"), encoding="utf-8") as f:
        data = json.load(f)

    results = data["results"]
    truth_graphs = data["truth_graphs"]
    case_ids = sorted(results.keys())

    v0_graphs = [results[c]["V0"]["graph"] for c in case_ids]
    dd_ref, dd_meta = build_data_driven_reference(v0_graphs)
    wl = WLKernel(h=WL_H)
    dd_view = view(dd_ref)

    out = {}
    for case_id in case_ids:
        r = {}
        for state in ("V0", "V1", "V2", "V3"):
            rec = results[case_id][state]["graph"]
            # §7.4 v2: V1 usa G1 (estendida com ΔV1); V2 usa a verdade estendida
            # (G0 + self-loop do pai, §7.4 v2); V0 e V3 usam G0.
            truth_key = "V1" if state == "V1" else ("V2" if state == "V2" else "G0")
            truth = truth_graphs[case_id][truth_key]
            cat_counts = results[case_id][state]["cat_counts"]

            c = conf_m(rec, truth)
            g = wl.s_struct(view(rec), dd_view)
            d = div_m(cat_counts)
            r[state] = {
                "conf": round(c, 6),
                "ged_ref": round(g, 6),
                "div_metric": round(d, 6),
                "dv": round((c + g + d) / 3.0, 6),
                "k_obs": len(cat_counts),
                "nodes": len(rec["nodes"]),
                "edges": len(rec["edges"]),
            }
        out[case_id] = r

    with open(os.path.join(OUTPUTS, "dv_values.json"), "w", encoding="utf-8") as f:
        json.dump({
            "wl_h": WL_H,
            "dd_reference": {"metadata": dd_meta, "graph": dd_view},
            "values": out,
        }, f, indent=2, ensure_ascii=False)

    print("Referência DATA-DRIVEN: %d nós, %d arestas MST (de %d instâncias de aresta)"
          % (dd_meta["num_nodes"], dd_meta["num_mst_edges"], dd_meta["num_edge_instances"]))
    print("DV por estado (média sobre casos):")
    states = ("V0", "V1", "V2", "V3")
    for st in states:
        vals = [out[c][st]["dv"] for c in case_ids]
        print("  %s: mean=%.6f min=%.6f max=%.6f" % (st, sum(vals) / len(vals), min(vals), max(vals)))
    print("saved:", os.path.join(OUTPUTS, "dv_values.json"))


if __name__ == "__main__":
    main()
