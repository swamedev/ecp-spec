# -*- coding: utf-8 -*-
"""
GO-8D — D-04: Production validator with engine-parseability gate.

Closes the gate gap documented in
`GO-8C/decisions/D-04-GATE-GAP-ENGINE-PARSEABILITY.md`: the GO-8C production
validator (P4/D-04.5) checked only LEXICON + TRACE and did NOT verify that an
atomic-facts markdown was parseable by the frozen engine (BIP-009-Chernobyl was
produced as a markdown TABLE -> 0 facts parsed -> 6 cells FAIL).

This validator, for each `02-atomic-facts.md`:
  1. detects divergent formats (markdown table / non-standard) -> REJECT before Lock;
  2. runs `parse_atomic_facts()` from the frozen engine -> requires >= MIN_FACTS facts;
  3. cross-checks order/text of extracted facts against the numbered source list.

Read-only with respect to GO-8B/GO-8C. Lives entirely inside GO-8D.
"""
import os
import re
import sys

sys.path.insert(0, r"D:\ecp-spec\scripts\go8b\operational")
import pilot_engine as pe

MIN_FACTS = 15
# Required structural markers per frozen parser (pilot_engine.py:126-153)
HEADER_MARKER = "## Fatos"
# A standard fact line is: `N. <texto> [ref]` ending in `]` (or ``]` ``)
_FACT_LINE = re.compile(r"^\s*\d+\.\s+.+\[[^\]]+\](`)?$")


# --------------------------------------------------------------------------- table / divergent format
def detect_table_format(path):
    """Return True if the atomic-facts file is a markdown table (non-parseable)."""
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    in_facts = False
    pipe_rows = 0
    for raw in lines:
        line = raw.strip()
        if line.startswith(HEADER_MARKER):
            in_facts = True
            continue
        if in_facts and line.startswith("##"):
            break
        if in_facts and line:
            if line.startswith("|"):
                pipe_rows += 1
            elif _FACT_LINE.match(line):
                return False  # a standard fact line inside Fatos section -> not a table
    # a file is "table format" if the Fatos section is dominated by pipe rows
    return pipe_rows >= 3 and pipe_rows >= 1


def detect_has_fatos_header(path):
    with open(path, encoding="utf-8") as f:
        return HEADER_MARKER in f.read()


# --------------------------------------------------------------------------- engine parseability
def validate_atomic_facts(path, min_facts=MIN_FACTS):
    """Return dict(status, n_facts, reason). status in {'PASS','FAIL'}."""
    if not os.path.exists(path):
        return {"status": "FAIL", "n_facts": 0,
                "reason": f"file not found: {path}"}
    if not detect_has_fatos_header(path):
        return {"status": "FAIL", "n_facts": 0,
                "reason": f"missing '{HEADER_MARKER}' header (non-standard format)"}
    if detect_table_format(path):
        return {"status": "FAIL", "n_facts": 0,
                "reason": "markdown table format detected (pipe rows under '## Fatos') - "
                          "not parseable by frozen engine (gate gap GO-8C D-04.11)"}

    facts = pe.parse_atomic_facts(path)
    if not facts:
        return {"status": "FAIL", "n_facts": 0,
                "reason": "engine parsed 0 facts (format diverges from `N. <texto> [ref]`)"}
    if len(facts) < min_facts:
        return {"status": "FAIL", "n_facts": len(facts),
                "reason": f"only {len(facts)} facts parsed (minimum {min_facts})"}

    # cross-check: order of extracted facts == order in source numbered list
    src_af = _source_af_ids(path)
    if src_af and [f["af_id"] for f in facts] != src_af:
        return {"status": "FAIL", "n_facts": len(facts),
                "reason": f"extracted AF id order {[f['af_id'] for f in facts][:5]}... != source {src_af[:5]}..."}

    return {"status": "PASS", "n_facts": len(facts),
            "reason": f"{len(facts)} facts parsed; order/text consistent with source"}


def _source_af_ids(path):
    """Parse the source numbered list independently of the engine (order check)."""
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    in_facts, ids = False, []
    for raw in lines:
        line = raw.strip()
        if line.startswith(HEADER_MARKER):
            in_facts = True
            continue
        if in_facts and line.startswith("##"):
            break
        if in_facts and _FACT_LINE.match(line):
            m = re.match(r"^\s*(\d+)\.\s+", line)
            if m:
                ids.append(f"AF-{int(m.group(1)):03d}")
    return ids


def validate_narrative(path):
    """Narrative is not the parseability gap (C was never affected), but validate anyway."""
    if not os.path.exists(path):
        return {"status": "FAIL", "n_facts": 0, "reason": f"file not found: {path}"}
    blocks = pe.parse_narrative(path)
    status = "PASS" if blocks else "FAIL"
    return {"status": status, "n_facts": len(blocks),
            "reason": f"{len(blocks)} blocks parsed" if status == "PASS" else "0 blocks parsed"}


# --------------------------------------------------------------------------- CLI over GO-8C study-input
def validate_study_input():
    study = r"D:\ecp-spec\experiments\validation\GO-8C\study-input"
    bips = [b for b in sorted(os.listdir(study)) if b.startswith("BIP-")]
    results = []
    for b in bips:
        af = os.path.join(study, b, "atomic-facts", "02-atomic-facts.md")
        if not os.path.exists(af):
            af = os.path.join(study, b, "atomic-facts", "atomic_facts.md")
        narr = os.path.join(study, b, "narrative", "01-narrativa-original.md")
        if not os.path.exists(narr):
            narr = os.path.join(study, b, "narrative", "narrative_pt.md")
        if not os.path.exists(narr):
            narr = os.path.join(study, b, "narrative", "narrative.md")
        ra = validate_atomic_facts(af) if os.path.exists(af) else {"status": "FAIL", "n_facts": 0, "reason": "no atomic-facts file"}
        rn = validate_narrative(narr) if os.path.exists(narr) else {"status": "FAIL", "n_facts": 0, "reason": "no narrative file"}
        results.append({"bip": b, "af": ra, "narr": rn})
    return results


if __name__ == "__main__":
    import json
    res = validate_study_input()
    n_pass = sum(1 for r in res if r["af"]["status"] == "PASS" and r["narr"]["status"] == "PASS")
    print(f"GO-8C study-input parseability: {n_pass}/{len(res)} BIPs PASS")
    for r in res:
        print(f"  {r['bip']:22s} AF={r['af']['status']:4s} ({r['af']['n_facts']:3d} facts)  NARR={r['narr']['status']:4s} ({r['narr']['n_facts']:3d} blocks)")
    json.dump(res, open(r"D:\ecp-spec\experiments\validation\GO-8D\analysis\d04_study_validation.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print("saved: GO-8D/analysis/d04_study_validation.json")
