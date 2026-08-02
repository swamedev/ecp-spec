#!/usr/bin/env python3
"""Linter mínimo de contratos ECP.

Valida documentos de contrato (JSON) contra a gramática formal em
schemas/ (contract.base.schema.json + contracts/<tipo>.schema.json).

Uso:
    python scripts/validate_contracts.py            # varre schemas/examples/
    python scripts/validate_contracts.py <path>...  # arquivos ou diretórios

Saída: relatório por arquivo. Exit code 0 se tudo conforme, 1 caso contrário.
"""
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry
from referencing.jsonschema import DRAFT202012

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
CONTRACTS_DIR = SCHEMAS / "contracts"
BASE = SCHEMAS / "contract.base.schema.json"
DEFAULT_EXAMPLES = SCHEMAS / "examples"

BASE_URI = "https://ecp.dev/schemas/contract.base.schema.json"
CONTRACT_TYPES = ("discovery", "research", "planning", "execution", "validation")
KIND_FILES = {
    "entity_capability": "capability.schema.json",
    "contract_capability": "contract_capability.schema.json",
    "negotiation": "negotiation.schema.json",
    "runtime_event": "runtime_event.schema.json",
    "runtime_reaval": "runtime_reaval.schema.json",
    "runtime_session": "runtime_session.schema.json",
    "runtime_scenario": "runtime_scenario.schema.json",
}
CONTRACT_MAPPINGS_DIR = SCHEMAS / "examples" / "capabilities" / "contracts"


def build_registry() -> Registry:
    """Registra o schema base para resolver os $ref dos schemas por tipo."""
    base = json.loads(BASE.read_text(encoding="utf-8"))
    return Registry().with_resource(BASE_URI, DRAFT202012.create_resource(base))


def load_schema(relative: Path):
    if not relative.exists():
        return None
    return json.loads(relative.read_text(encoding="utf-8"))


def load_type_schema(ctype: str):
    return load_schema(CONTRACTS_DIR / f"{ctype}.schema.json")


def validate_against(instance: dict, schema: dict, registry: Registry, path: Path) -> list[str]:
    errors: list[str] = []
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{path}: schema inválido ({exc})")
        return errors
    validator = Draft202012Validator(schema, registry=registry)
    for err in validator.iter_errors(instance):
        loc = ".".join(str(p) for p in err.path) or "/"
        errors.append(f"{path}: {err.message} (em {loc})")
    return errors


def load_contract_mapping(ctype: str):
    """Carrega o mapeamento contrato→capacidades (para checagem de can_sign)."""
    m = load_schema(CONTRACT_MAPPINGS_DIR / f"{ctype}.json")
    return m.get("required", {}) if m else {}


def validate_document(path: Path, doc: dict, registry: Registry) -> list[str]:
    errors: list[str] = []

    kind = doc.get("kind")
    if kind is None:
        ctype = doc.get("contract")
        if ctype not in CONTRACT_TYPES:
            return [f"{path}: documento sem 'kind'/'contract' reconhecível"]
        if path.stem != ctype:
            errors.append(f"{path}: nome do arquivo '{path.stem}' difere de contract '{ctype}'")
        schema = load_type_schema(ctype)
        if schema is None:
            errors.append(f"{path}: schema ausente para o tipo '{ctype}'")
            return errors
        errors.extend(validate_against(doc, schema, registry, path))
        errors.extend(contract_semantic_checks(path, doc))
        return errors

    schema_file = KIND_FILES.get(kind)
    if schema_file is None:
        return [f"{path}: 'kind' desconhecido: {kind!r}"]
    schema = load_schema(SCHEMAS / schema_file)
    if schema is None:
        return [f"{path}: schema ausente para o kind '{kind}'"]
    errors.extend(validate_against(doc, schema, registry, path))
    errors.extend(kind_semantic_checks(path, doc))
    return errors


def contract_semantic_checks(path: Path, doc: dict) -> list[str]:
    """Checagens que o JSON Schema não captura (requisitos ECP-001 §7.2)."""
    errors: list[str] = []
    outputs = set(doc.get("outputs", {}).keys())

    for ev in doc.get("evidence", []):
        if ev not in outputs:
            errors.append(f"{path}: evidence '{ev}' não declarada em outputs")

    pre = doc.get("preconditions", [])
    for cond in pre:
        if not isinstance(cond, str) or not cond.strip():
            errors.append(f"{path}: precondição vazia ou inválida: {cond!r}")

    exit_ = doc.get("exit")
    if isinstance(exit_, dict) and exit_.get("probabilistic"):
        if not exit_.get("method"):
            errors.append(f"{path}: EXIT probabilístico sem método pré-registrado (ECP-100.3)")
        if not exit_.get("threshold"):
            errors.append(f"{path}: EXIT probabilístico sem limiar declarado (ECP-100.3)")

    authority = doc.get("authority")
    if authority and not authority.get("actor"):
        errors.append(f"{path}: authority sem actor (ECP-100.1 / RNF-2)")
    co = authority.get("co_authors") if authority else []
    if co and not authority.get("consensus"):
        errors.append(f"{path}: co-autoria sem método de consenso declarado (ECP-100.1)")

    return errors


def kind_semantic_checks(path: Path, doc: dict) -> list[str]:
    """Checagens semânticas de capacidade/negociação (ECP-200)."""
    errors: list[str] = []
    kind = doc["kind"]

    if kind == "entity_capability":
        atomic = doc.get("atomic", {})
        if not atomic.get("write"):
            errors.append(f"{path}: entidade sem capacidade mínima de registro (ECP-200.3)")
        for ctype in doc.get("can_sign", []):
            required = load_contract_mapping(ctype)
            if not required:
                continue
            missing = [cap for cap, needed in required.items() if needed and not atomic.get(cap)]
            if missing:
                errors.append(
                    f"{path}: can_sign inclui '{ctype}' mas falta capacidade {missing} (ECP-200.1)"
                )

    elif kind == "contract_capability":
        for cap in ("read", "write", "execute", "verify", "research", "remember"):
            if cap not in doc.get("required", {}) and cap not in doc.get("optional", {}):
                errors.append(f"{path}: capacidade '{cap}' não declarada em required/optional")

    elif kind == "negotiation":
        candidates = doc.get("candidates", [])
        chosen_entity = doc.get("chosen")
        chosen_obj = next((c for c in candidates if c.get("entity") == chosen_entity), None)
        has_full = any(c.get("match") for c in candidates)
        if chosen_obj is None:
            if not doc.get("fallback"):
                errors.append(
                    f"{path}: 'chosen' {chosen_entity!r} não referencia candidato e sem fallback (ECP-200.2)"
                )
        elif not chosen_obj.get("match"):
            if not doc.get("fallback"):
                errors.append(
                    f"{path}: escolhido candidato parcial/não conforme sem fallback registrado (ECP-200.2)"
                )
        elif not has_full:
            errors.append(f"{path}: 'chosen' marcado match mas nenhum candidato com match (inconsistente)")

    elif kind == "runtime_scenario":
        open_events = 0
        for step in doc.get("steps", []):
            st = step.get("step")
            if st == "event":
                open_events += 1
            elif st == "reaval":
                if open_events > 0:
                    open_events -= 1
            elif st == "transition":
                if open_events > 0:
                    errors.append(
                        f"{path}: transição com evento externo não reavaliado (RNF-3 / ECP-300.3)"
                    )
            elif st == "invalidate":
                if not step.get("affects"):
                    errors.append(f"{path}: invalidação sem dependentes no grafo (ECP-300 §3)")
            elif st == "failure":
                if step.get("declared") is None and step.get("handled"):
                    errors.append(
                        f"{path}: falha sem FAILURE declarado resolvida pelo motor (ECP-300.2)"
                    )

    return errors


def collect_files(args: list[str]) -> list[Path]:
    if not args:
        return sorted(DEFAULT_EXAMPLES.rglob("*.json"))
    files: list[Path] = []
    for arg in args:
        p = Path(arg)
        if p.is_dir():
            files.extend(sorted(p.rglob("*.json")))
        elif p.is_file():
            files.append(p)
    return files


def main() -> int:
    registry = build_registry()
    files = collect_files(sys.argv[1:])
    if not files:
        print(f"nenhum contrato JSON encontrado em {DEFAULT_EXAMPLES}")
        return 1

    total_errors = 0
    checked = 0
    for path in files:
        checked += 1
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            total_errors += 1
            print(f"[ERRO] {path}: JSON inválido ({exc})")
            continue
        errors = validate_document(path, doc, registry)
        if errors:
            total_errors += len(errors)
            for err in errors:
                print(f"[ERRO] {err}")
        else:
            print(f"[OK]   {path}")

    print(f"\n{checked} contratos verificados; {total_errors} erros.")
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
