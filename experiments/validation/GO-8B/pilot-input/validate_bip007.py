# BIP-007 — Ebola: verificação pós-produção (P5, manifest §7)
# Método: normalização acentuada + casamento por palavra (\bterm\b) — 52 termos ECP.
# Verifica: (1) léxico zero-ECP; (2) rastreabilidade 100% refs -> sources/00-index.md.

import re
import sys
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parent
BIP = BASE / "BIP-007-ebola"

ECP_TERMS = [
    "afirmacao", "aprendizado", "artefato", "artifact", "assumption",
    "cadeia de dependencias", "capability", "capacidade", "claim",
    "conhecimento", "contrato", "decisao", "decisao e causa", "decision",
    "entidade", "estado", "evidence", "evidencia", "fase pos-artefato",
    "fluxo e consequencia", "goal", "grafo de conhecimento", "knowledge",
    "l-0", "l-1", "l0", "l1", "learning", "lei um", "lei zero", "objetivo",
    "p-1", "p-10", "p-11", "p-12", "p-2", "p-3", "p-4", "p-5", "p-6",
    "p-7", "p-8", "p-9", "problem", "problema", "rastreabil", "risco",
    "risk", "state", "suposicao", "validacao", "validation",
]

assert len(ECP_TERMS) == 52, f"expected 52 termos ECP, got {len(ECP_TERMS)}"


def norm(s: str) -> str:
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode().lower()


def check_lexicon(path: Path) -> list:
    text = norm(path.read_text(encoding="utf-8"))
    hits = []
    for term in ECP_TERMS:
        t = norm(term)
        pat = r"\b" + re.escape(t) + r"\b"
        for m in re.finditer(pat, text):
            hits.append(term)
    return hits


def check_traceability(path: Path, refs: set) -> list:
    text = path.read_text(encoding="utf-8")
    used = set(re.findall(r"\[([^\]]+)\]", text))
    missing = []
    for u in used:
        for ref in u.split(","):
            ref = ref.strip()
            if ref not in refs:
                missing.append(ref)
    return missing


def main() -> int:
    idx = (BIP / "sources" / "00-index.md").read_text(encoding="utf-8")
    refs = set(re.findall(r"^\| `([^`]+)` ", idx, flags=re.M))
    files = [
        BIP / "narrative" / "narrative_pt.md",
        BIP / "atomic-facts" / "atomic_facts.md",
    ]
    ok = True
    for f in files:
        if not f.exists():
            print(f"[MISSING] {f} (arquivo ainda não criado)")
            ok = False
            continue
        hits = check_lexicon(f)
        if hits:
            ok = False
            print(f"[LEXICON FAIL] {f.name}: {hits}")
        else:
            print(f"[LEXICON PASS] {f.name}: 0 ECP terms")
        missing = check_traceability(f, refs)
        if missing:
            ok = False
            print(f"[TRACE FAIL] {f.name}: missing refs {missing}")
        else:
            print(f"[TRACE PASS] {f.name}: all refs in 00-index")
    print(f"\nRESULT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())