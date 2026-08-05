#!/usr/bin/env python3
"""
Minerador P-0005A.2 — Extração de Observações do Corpus Experimental

Responsável por extrair **apenas fatos verificáveis** dos experimentos EXP-001..EXP-004
e escrevê-los no formato OBS-SCHEMA v1.0 congelado.

Regra: Apenas extrair fatos. NÃO agrupar, interpretar, criar padrões ou leis.
"""

from __future__ import annotations

import argparse
import json
import yaml
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional


class OBSMiner:
    """Extrai observações factuais dos arquivos de experimento."""

    def __init__(
        self,
        corpus_path: Path,
        runtime_data_path: Path,
    ):
        self.corpus_path = corpus_path
        self.runtime_data_path = runtime_data_path
        self.corpus_data = self._load_corpus()
        self.obs_counter = 0

    def _load_corpus(self) -> Dict:
        """Carrega o corpus existente."""
        if self.corpus_path.exists():
            with open(self.corpus_path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)
        else:
            return self._empty_corpus()

    def _empty_corpus(self) -> Dict:
        return {
            "version": "0.1.0",
            "status": "draft",
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "generated_from": {
                "experiments": [
                    "EXP-001"
                ]
            },
            "miner_version": "0.1.0",
            "observation_count": 0,
            "schema_version": "1.0",
            "observations": [],
        }

    def _next_obs_id(self) -> str:
        self.obs_counter += 1
        return f"OBS-{self.obs_counter:04d}"

    def _make_trace(self, source_file: str, element_id: str) -> str:
        """Cria trace rastreável."""
        return f"{source_file}:{element_id}"

    def _sha256_short(self, content: str) -> str:
        """Hash curto para trace."""
        return hashlib.sha256(content.encode()).hexdigest()[:16]

    def _build_obs(
        self,
        experiment: str,
        artifact_source: str,
        artifact_type: str,
        event: str,
        entities: List[str],
        evidence_content: str,
        trace_ref: str,
        confidence_source: str,
    ) -> Dict:
        """Constrói um OBS conforme schema v1.0."""
        self.obs_counter += 1
        return {
            "id": f"OBS-{self.obs_counter:04d}",
            "experiment": experiment,
            "artifact": {
                "source": artifact_source,
                "type": artifact_type,
                "reference_id": f"{experiment.lower()}_snapshot",
            },
            "event": event,
            "entidades": entities,
            "evidence": evidence_content,
            "trace": trace_ref,
            "confidence_source": confidence_source,
        }

    def mine_graph_json(self) -> List[Dict]:
        """Minera exp001_graph.json — grafo base do bootstrap."""
        observations = []
        file_path = self.runtime_data_path / "exp001_graph.json"
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        experiment = data.get("experimento", "EXP-001")
        artifact_source = "data/exp001_graph.json"
        artifact_type = "json"
        confidence = f"{experiment} visual inspection"

        for node in data.get("nodes", []):
            entity_id = node.get("id", "")
            entity_type = node.get("tipo", "")
            status = node.get("status", "")
            author = node.get("author", "runtime")
            created = node.get("created_at", "")

            # Evento factual: entidade criada com status
            event = f"{entity_type.capitalize()} {entity_id} criada com status {status}"
            entities = [entity_type.capitalize()]

            # Evidência: o nó completo serializado
            evidence = json.dumps(node, ensure_ascii=False, separators=(",", ":"))
            trace = self._make_trace("exp001_graph.json", entity_id)
            confidence_source = f"{experiment} {author} {created}"

            obs = self._build_obs(
                experiment=experiment,
                artifact_source="data/exp001_graph.json",
                artifact_type="json",
                event=event,
                entities=entities,
                evidence_content=evidence,
                trace_ref=trace,
                confidence_source=confidence_source,
            )
            observations.append(obs)

        # Edges também são fatos observáveis
        for edge in data.get("edges", []):
            source = edge.get("source", "")
            target = edge.get("target", "")
            label = edge.get("label", "")

            event = f"Relação {label} entre {source} e {target}"
            entities = [source, target]

            evidence = json.dumps(edge, ensure_ascii=False, separators=(",", ":"))
            trace = self._make_trace("exp001_graph.json", f"{source}-{label}-{target}")
            confidence_source = f"{experiment} edge extraction"

            obs = self._build_obs(
                experiment=experiment,
                artifact_source="data/exp001_graph.json",
                artifact_type="json",
                event=event,
                entities=entities,
                evidence_content=evidence,
                trace_ref=trace,
                confidence_source=confidence_source,
            )
            observations.append(obs)

        return observations

    def mine_identity_json(self) -> List[Dict]:
        """Minera exp001_identity.json — incremento 2."""
        observations = []
        file_path = self.runtime_data_path / "exp001_identity.json"
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        experiment = "EXP-001 / incremento 2"
        artifact_source = "data/exp001_identity.json"
        artifact_type = "json"
        confidence = "EXP-001 identity audit"

        # Fato: snapshot criado
        snap = data.get("snapshot", {})
        decision_id = snap.get("decision_id", "")
        message = snap.get("message", "")
        sha = snap.get("sha", "")
        parent_sha = snap.get("parent_sha", "")
        created_at = snap.get("created_at", "")

        event = f"Snapshot {decision_id} criado com mensagem '{message}'"
        entities = ["Decision", "Snapshot"]
        evidence = json.dumps(snap, ensure_ascii=False, separators=(",", ":"))
        trace = self._make_trace("exp001_identity.json", "snapshot")
        confidence_source = f"{experiment} snapshot {sha[:16]}"

        observations.append(self._build_obs(
            experiment=experiment,
            artifact_source="data/exp001_identity.json",
            artifact_type="json",
            event=event,
            entities=entities,
            evidence_content=evidence,
            trace_ref=trace,
            confidence_source=confidence_source,
        ))

        # Fato: decisão D-0002 com evidências
        decision_id = data.get("decision", "")
        alternatives = data.get("alternativas", 0)
        evidencias = data.get("evidencias", [])
        confianca = data.get("confianca", 0.0)
        audit = data.get("audit", {})

        event = f"Decision {decision_id} autorizada com {alternatives} alternativas e confiança {confianca}"
        entities = ["Decision", "Evidence"]
        evidence = json.dumps({
            "decision_id": decision_id,
            "alternatives": alternatives,
            "evidences": evidencias,
            "confidence": confianca,
            "audit_conforme": audit.get("conforme", False),
        }, ensure_ascii=False, separators=(",", ":"))
        trace = self._make_trace("exp001_identity.json", decision_id)
        confidence_source = f"{experiment} decision record"

        observations.append(self._build_obs(
            experiment=experiment,
            artifact_source="data/exp001_identity.json",
            artifact_type="json",
            event=event,
            entities=entities,
            evidence_content=evidence,
            trace_ref=trace,
            confidence_source=confidence_source,
        ))

        return observations

    def mine_execution_json(self) -> List[Dict]:
        """Minera exp001_execution.json — incremento 3."""
        observations = []
        file_path = self.runtime_data_path / "exp001_execution.json"
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        experiment = "EXP-001 / incremento 3"
        artifact_source = "data/exp001_execution.json"
        artifact_type = "json"
        confidence = "EXP-001 execution audit"

        # Fato: Execution Intent criado
        intent = data.get("intent", {})
        intent_id = intent.get("id", "")
        physical_id = intent.get("physical_id", "")
        author = intent.get("author", "")
        status = intent.get("status", "")
        created_at = intent.get("created_at", "")

        event = f"ExecutionIntent {intent_id} criado com status {status}"
        entities = ["ExecutionIntent"]
        evidence = json.dumps(intent, ensure_ascii=False, separators=(",", ":"))
        trace = self._make_trace("exp001_execution.json", intent_id)
        confidence_source = f"{experiment} intent record"

        observations.append(self._build_obs(
            experiment=experiment,
            artifact_source="data/exp001_execution.json",
            artifact_type="json",
            event=event,
            entities=entities,
            evidence_content=evidence,
            trace_ref=trace,
            confidence_source=confidence_source,
        ))

        # Fato: provider escolhido
        provider = data.get("provider_escolhido", "")
        negotiation = data.get("negotiation_reasons", [])

        event = f"Provider {provider} selecionado para intent"
        entities = ["Provider", "ExecutionIntent"]
        evidence = json.dumps({
            "provider": provider,
            "reasons": negotiation,
        }, ensure_ascii=False, separators=(",", ":"))
        trace = self._make_trace("exp001_execution.json", "provider_selection")
        confidence_source = "EXP-001 negotiation log"

        observations.append(self._build_obs(
            experiment=experiment,
            artifact_source="data/exp001_execution.json",
            artifact_type="json",
            event=event,
            entities=entities,
            evidence_content=evidence,
            trace_ref=trace,
            confidence_source=confidence_source,
        ))

        return observations

    def mine_model_json(self) -> List[Dict]:
        """Minera exp001_model.json — incremento 4."""
        observations = []
        file_path = self.runtime_data_path / "exp001_model.json"
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        experiment = "EXP-001 / incremento 4"
        artifact_source = "data/exp001_model.json"
        artifact_type = "json"
        confidence = "EXP-001 model audit"

        # Fato: Observation OBS-0001 criada
        obs_data = data.get("observation", {})
        obs_id = obs_data.get("id", "")
        physical_id = obs_data.get("physical_id", "")
        author = obs_data.get("author", "")
        status = obs_data.get("status", "")
        created_at = obs_data.get("created_at", "")

        event = f"Observation {obs_id} criada com status {status}"
        entities = ["Observation"]
        evidence = json.dumps(obs_data, ensure_ascii=False, separators=(",", ":"))
        trace = self._make_trace("exp001_model.json", obs_id)
        confidence_source = f"{experiment} observation record"

        observations.append(self._build_obs(
            experiment=experiment,
            artifact_source="data/exp001_model.json",
            artifact_type="json",
            event=event,
            entities=entities,
            evidence_content=evidence,
            trace_ref=trace,
            confidence_source=confidence_source,
        ))

        # Fato: Evidence E-00042 criada
        ev_data = data.get("evidence", {})
        ev_id = ev_data.get("id", "")
        physical_id = ev_data.get("physical_id", "")
        author = ev_data.get("author", "")
        status = ev_data.get("status", "")
        created_at = ev_data.get("created_at", "")

        event = f"Evidence {ev_id} criada com status {status}"
        entities = ["Evidence"]
        evidence = json.dumps(ev_data, ensure_ascii=False, separators=(",", ":"))
        trace = self._make_trace("exp001_model.json", ev_id)
        confidence_source = f"{experiment} evidence record"

        observations.append(self._build_obs(
            experiment=experiment,
            artifact_source="data/exp001_model.json",
            artifact_type="json",
            event=event,
            entities=entities,
            evidence_content=evidence,
            trace_ref=trace,
            confidence_source=confidence_source,
        ))

        # Fato: Decision D-0005 criada
        model = data.get("model", {})
        cognitive = model.get("cognitive", [])
        operational = model.get("operational", [])

        event = f"Modelo estrutural validado: {len(cognitive)} cognitivas, {len(operational)} operacionais"
        entities = ["Decision", "Model"]
        evidence = json.dumps({
            "cognitive_count": len(cognitive),
            "operational_count": len(operational),
            "cognitive": cognitive,
            "operational": operational,
        }, ensure_ascii=False, separators=(",", ":"))
        trace = self._make_trace("exp001_model.json", "model_validation")
        confidence_source = "EXP-001 model audit"

        observations.append(self._build_obs(
            experiment=experiment,
            artifact_source="data/exp001_model.json",
            artifact_type="json",
            event=event,
            entities=entities,
            evidence_content=evidence,
            trace_ref=trace,
            confidence_source=confidence_source,
        ))

        return observations

    def run(self) -> None:
        """Executa mineração completa."""
        print("=== P-0005A.2 Minerador de Observações ===")
        print(f"Lendo dados de: {self.runtime_data_path}")

        all_observations = []

        # Minera cada arquivo de experimento
        print("Mineração exp001_graph.json...")
        all_observations.extend(self.mine_graph_json())

        print("Mineração exp001_identity.json...")
        all_observations.extend(self.mine_identity_json())

        print("Mineração exp001_execution.json...")
        all_observations.extend(self.mine_execution_json())

        print("Mineração exp001_model.json...")
        all_observations.extend(self.mine_model_json())

        # Atualiza corpus
        self.corpus_data["observations"] = all_observations
        self.corpus_data["observation_count"] = len(all_observations)
        self.corpus_data["generated_at"] = datetime.utcnow().isoformat() + "Z"
        self.corpus_data["miner_version"] = "0.1.0"
        self.corpus_data["schema_version"] = "1.0"

        # Escreve corpus
        with open(self.corpus_path, "w", encoding="utf-8") as f:
            yaml.dump(self.corpus_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

        print(f"\nOK {len(all_observations)} OBS extraidas e escritas.")
        print(f"  Corpus salvo em: {self.corpus_path}")
        print(f"  Total OBS no corpus: {len(all_observations)}")


def main():
    parser = argparse.ArgumentParser(description="P-0005A.2 Minerador de Observações")
    parser.add_argument(
        "--corpus",
        default="D:/ecp-spec/experiments/validation/corpus/CORPUS-EXPERIMENTAL-v0.yaml",
        help="Caminho do corpus YAML"
    )
    parser.add_argument(
        "--data",
        default="D:/ecp-runtime/data",
        help="Diretório com arquivos JSON dos experimentos"
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Sobrescreve corpus existente"
    )
    args = parser.parse_args()

    miner = OBSMiner(
        corpus_path=Path(args.corpus),
        runtime_data_path=Path(args.data),
    )
    miner.run()


if __name__ == "__main__":
    main()