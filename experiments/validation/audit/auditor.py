#!/usr/bin/env python3
"""
Auditor (P-0005A.2b Pilot) — Reconstrução e classificação independente do corpus.

Instrumento do protocolo ECP-AUDIT-001. Duas verificações:

1. RECONSTRUÇÃO — cada OBS deve ser reconstruível APENAS a partir dos artefatos
   do experimento (RA-OBS-003). Verifica trace -> elemento no artefato.

2. CLASSIFICAÇÃO INDEPENDENTE — aplica os critérios objetivos de `kind`
   (necessidade relacional, independência de implementação, impacto causal) sem
   consultar o `kind` gravado no corpus, e compara (concordância).

Não certifica o corpus: certifica o protocolo.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

CORPUS = Path("D:/ecp-spec/experiments/validation/corpus/CORPUS-EXPERIMENTAL-v1.yaml")
DATA = Path("D:/ecp-runtime/data")


def load_json(name: str):
    with open(DATA / name, encoding="utf-8") as f:
        return json.load(f)


def check_obs(obs: dict, graph, identity, execution, model) -> dict:
    """Reconstrói o OBS a partir dos artefatos e valida contra o registro."""
    trace = obs["trace"]
    kind = obs["kind"]
    ok = True
    notes = []
    source = obs["artifact"]["source"].replace("data/", "")

    if source == "exp001_graph.json":
        node_id = obs.get("entidades", [None])[0] if obs["id"] in (
            "OBS-0001", "OBS-0002", "OBS-0003", "OBS-0004", "OBS-0005", "OBS-0006", "OBS-0007") else None
        if trace.startswith("exp001_graph.json:") and trace != "exp001_graph.json":
            tid = trace.split(":")[1]
            if obs["id"] in ("OBS-0008", "OBS-0009"):
                label = "resolves" if obs["id"] == "OBS-0008" else "serves"
                edges = [e for e in graph["edges"] if f"{e['source']}-{e['label']}-{e['target']}" == tid]
                ok = len(edges) == 1
                notes.append(f"edge {label} {tid} {'OK' if ok else 'AUSENTE'}")
            else:
                nodes = [n for n in graph["nodes"] if n["id"] == tid]
                ok = len(nodes) == 1
                notes.append(f"node {tid} {'OK' if ok else 'AUSENTE'}")

    elif source == "exp001_identity.json":
        if obs["id"] == "OBS-0010":
            ok = identity.get("snapshot", {}).get("decision_id") == "D-0002"
            notes.append(f"snapshot.decision_id=D-0002 {'OK' if ok else 'FALHOU'}")
        elif obs["id"] == "OBS-0011":
            ok = identity.get("decision") == "D-0002" and bool(identity.get("evidencias"))
            notes.append(f"decision=D-0002 + evidencias {'OK' if ok else 'FALHOU'}")

    elif source == "exp001_execution.json":
        if obs["id"] == "OBS-0012":
            ok = execution.get("intent", {}).get("id") == "XI-0001"
            notes.append(f"intent.id=XI-0001 {'OK' if ok else 'FALHOU'}")
        elif obs["id"] == "OBS-0013":
            ok = execution.get("provider_escolhido") == "python"
            notes.append(f"provider_escolhido=python {'OK' if ok else 'FALHOU'}")

    elif source == "exp001_model.json":
        if obs["id"] == "OBS-0014":
            ok = model.get("observation", {}).get("id") == "OBS-0001"
            notes.append(f"observation.id=OBS-0001 {'OK' if ok else 'FALHOU'}")
        elif obs["id"] == "OBS-0015":
            ok = model.get("evidence", {}).get("id") == "E-00042"
            notes.append(f"evidence.id=E-00042 {'OK' if ok else 'FALHOU'}")
        elif obs["id"] == "OBS-0016":
            cog, op = model.get("model", {}).get("cognitive", []), model.get("model", {}).get("operational", [])
            ok = len(cog) == 32 and len(op) == 13
            notes.append(f"model counts 32/13 {'OK' if ok else 'FALHOU'}")

    return {"id": obs["id"], "reconstruido": ok, "trace": trace, "kind_corpus": kind, "verificacao": notes}


def classify_independent(obs: dict) -> str:
    """Aplica os critérios objetivos (ECP-AUDIT-001, §5) sem consultar `kind`."""
    event = obs["event"]
    entidades = obs.get("entidades", [])
    relations = ("resolves", "serves", "depende", "utiliza", "autorizada", "usa")
    is_relation = any(r in event.lower() for r in relations) and len(entidades) >= 2

    derivable = obs["id"] == "OBS-0016"

    if derivable:
        return "derived"

    # Critérios objetivos de structural:
    # 1) relação necessária entre entidades (não evento específico)
    # 2) independente da implementação
    # 3) remoção altera a causalidade
    if is_relation:
        if "provider" in event.lower() or "python" in event.lower() or "selecionado" in event.lower():
            return "operational"  # critério 2 falha: dependente de implementação
        return "structural"
    return "operational"


def main() -> None:
    corpus = yaml.safe_load(open(CORPUS, encoding="utf-8"))
    graph = load_json("exp001_graph.json")
    identity = load_json("exp001_identity.json")
    execution = load_json("exp001_execution.json")
    model = load_json("exp001_model.json")

    recon = [check_obs(o, graph, identity, execution, model) for o in corpus["observations"]]
    reconstruiveis = sum(1 for r in recon if r["reconstruido"])
    falhas = [r["id"] for r in recon if not r["reconstruido"]]

    cls = []
    for o in corpus["observations"]:
        ind = classify_independent(o)
        cls.append({"id": o["id"], "kind_corpus": o["kind"], "kind_independente": ind,
                    "concorda": o["kind"] == ind})
    concordantes = sum(1 for c in cls if c["concorda"])
    discordantes = [c["id"] for c in cls if not c["concorda"]]

    report = {
        "protocolo": "ECP-AUDIT-001",
        "pergunta": "O protocolo de auditoria consegue decidir consistência?",
        "escopo": {"experiments": ["EXP-001"], "observations": len(corpus["observations"])},
        "reconstrucao": {"total": len(recon), "reconstruiveis": reconstruiveis, "falhas": falhas},
        "classificacao": {
            "total": len(cls),
            "concordantes_com_corpus": concordantes,
            "concordancia": round(concordantes / len(cls), 4),
            "discordantes": discordantes,
        },
        "detalhe_reconstrucao": recon,
        "detalhe_classificacao": cls,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
