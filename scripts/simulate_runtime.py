#!/usr/bin/env python3
"""Simulador de execução do Runtime ECP (ECP-300).

Executa cenários (`runtime_scenario`) sobre o grafo e verifica os
invariantes do motor em cada passo:

- RNF-3 / ECP-300.3 — evento externo entra na fila, nunca transiciona;
- ECP-300.4        — reavaliação é decisão registrada (ou não-reação
                      justificada);
- ECP-300.2        — falha sem tratamento bloqueia, nunca resolve sozinha;
- ECP-300 §3       — invalidação sem dependentes é sinal de grafo mal ligado;
- ECP-100.1 / L-0  — transição exige autoridade e Decision Record.

Uso:
    python scripts/simulate_runtime.py
    python scripts/simulate_runtime.py schemas/examples/runtime/scenarios

Cenários positivos (schemas/examples/runtime/) devem produzir 0 violações.
Cenários negativos (schemas/negative/runtime/) devem produzir >= 1 violação.
Exit code 0 se ambos os critérios forem atendidos.
"""
import json
import sys
from pathlib import Path

from validate_contracts import build_registry, load_schema, validate_against

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
POSITIVE_ROOT = SCHEMAS / "examples" / "runtime"
NEGATIVE_ROOT = SCHEMAS / "negative" / "runtime"
SCENARIO_SCHEMA = "runtime_scenario.schema.json"
EVENT_SCHEMA = "runtime_event.schema.json"
REAVAL_SCHEMA = "runtime_reaval.schema.json"
SESSION_SCHEMA = "runtime_session.schema.json"


def load_all(root: Path) -> list[tuple[Path, dict]]:
    if not root.exists():
        return []
    docs = []
    for path in sorted(root.rglob("*.json")):
        try:
            docs.append((path, json.loads(path.read_text(encoding="utf-8"))))
        except json.JSONDecodeError as exc:
            docs.append((path, {"__json_error__": str(exc)}))
    return docs


def schema_errors(doc: dict, path: Path, registry) -> list[str]:
    if "__json_error__" in doc:
        return [f"{path}: JSON inválido ({doc['__json_error__']})"]
    kind = doc.get("kind")
    schema_name = {
        "runtime_event": EVENT_SCHEMA,
        "runtime_reaval": REAVAL_SCHEMA,
        "runtime_session": SESSION_SCHEMA,
        "runtime_scenario": SCENARIO_SCHEMA,
    }.get(kind)
    if schema_name is None:
        return [f"{path}: 'kind' de runtime desconhecido: {kind!r}"]
    schema = load_schema(SCHEMAS / schema_name)
    if schema is None:
        return [f"{path}: schema ausente para o kind '{kind}'"]
    return validate_against(doc, schema, registry, path)


def build_events(docs) -> dict[str, dict]:
    events = {}
    for path, doc in docs:
        if doc.get("kind") == "runtime_event":
            events[doc.get("event_id")] = doc
    return events


def simulate(doc: dict, path: Path, events: dict[str, dict]) -> list[str]:
    """Verifica os invariantes do motor sobre a sequência de passos."""
    errors: list[str] = []
    state = None
    open_events = 0
    suspects_pending: set[str] = set()
    blocked = False

    for idx, step in enumerate(doc.get("steps", [])):
        tag = f"passo {idx + 1}"
        st = step.get("step")

        if st == "event":
            event_id = step.get("event")
            ev = events.get(event_id)
            if ev is None:
                errors.append(f"{path}: {tag}: evento {event_id!r} não encontrado")
                continue
            suspects_pending.update(ev.get("affects", []))
            open_events += 1
            # RNF-3: o evento por si só não muda o estado observável.

        elif st == "invalidate":
            affects = step.get("affects", [])
            if not affects:
                errors.append(
                    f"{path}: {tag}: invalidação sem dependentes no grafo (ECP-300 §3)"
                )
            suspects_pending.update(affects)

        elif st == "reaval":
            result = step.get("result")
            if result == "reavaliado" and not step.get("decision"):
                errors.append(f"{path}: {tag}: reavaliação 'reavaliado' sem decisão (ECP-300.4)")
            if result == "sem_reacao" and not step.get("justification"):
                errors.append(
                    f"{path}: {tag}: não-reação sem justificativa registrada (ECP-100.2)"
                )
            for suspect in step.get("suspects", []):
                suspects_pending.discard(suspect)
            if open_events > 0:
                open_events -= 1

        elif st == "transition":
            if open_events > 0:
                errors.append(
                    f"{path}: {tag}: transição com evento externo não reavaliado (RNF-3 / ECP-300.3)"
                )
            if blocked:
                errors.append(
                    f"{path}: {tag}: transição após falha sem tratamento (ECP-300.2)"
                )
            if state is not None and step.get("from") != state:
                errors.append(
                    f"{path}: {tag}: transição a partir de {step.get('from')!r}, mas o "
                    f"estado corrente é {state!r}"
                )
            authority = step.get("authority", {})
            if not authority.get("actor"):
                errors.append(f"{path}: {tag}: transição sem autoridade (ECP-100.1 / RNF-2)")
            if not step.get("decision"):
                errors.append(f"{path}: {tag}: transição sem Decision Record (Lei L-0)")
            state = step.get("to")

        elif st == "failure":
            declared = step.get("declared")
            handled = step.get("handled")
            if declared is None and handled:
                errors.append(
                    f"{path}: {tag}: falha sem FAILURE declarado resolvida pelo motor (ECP-300.2)"
                )
            if declared is not None and not handled:
                blocked = True
            if declared is None and not handled:
                blocked = True

        else:
            errors.append(f"{path}: {tag}: tipo de passo desconhecido: {st!r}")

    if suspects_pending:
        errors.append(
            f"{path}: decisões suspeitas sem reavaliação (ECP-300.4): {sorted(suspects_pending)}"
        )
    if open_events > 0:
        errors.append(
            f"{path}: evento(s) externo(s) sem reavaliação registrada (RNF-3): {open_events}"
        )
    return errors


def run_root(root: Path, events: dict[str, dict], expect_violations: bool) -> tuple[int, int]:
    docs = load_all(root)
    registry = build_registry()
    ok = 0
    failed = 0
    for path, doc in docs:
        kind = doc.get("kind")
        errors = schema_errors(doc, path, registry)
        if kind == "runtime_scenario":
            errors.extend(simulate(doc, path, events))
        if expect_violations:
            if errors:
                ok += 1
                for err in errors:
                    print(f"[VIOL] {err}")
            else:
                failed += 1
                print(f"[FALHA] {path}: documento negativo não produziu violação")
        else:
            if not errors:
                ok += 1
                print(f"[OK]   {path}")
            else:
                failed += 1
                for err in errors:
                    print(f"[ERRO] {err}")
    label = "negativos" if expect_violations else "positivos"
    print(f"{ok} documentos {label} conforme; {failed} falhas.")
    return ok, failed


def main() -> int:
    positive_docs = load_all(POSITIVE_ROOT)
    negative_docs = load_all(NEGATIVE_ROOT)
    events = build_events(positive_docs + negative_docs)
    positive_ok, positive_failed = run_root(POSITIVE_ROOT, events, expect_violations=False)
    negative_ok, negative_failed = run_root(NEGATIVE_ROOT, events, expect_violations=True)
    if positive_failed:
        print(f"{positive_failed} documento(s) positivo(s) violaram o runtime.")
        return 1
    if negative_failed:
        print(f"{negative_failed} falsificação(ões) negativa(s) não foram detectadas.")
        return 1
    print(
        f"Runtime simulado conforme: {positive_ok} documentos positivos; "
        f"{negative_ok} falsificações detectadas."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
