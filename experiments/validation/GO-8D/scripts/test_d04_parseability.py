# -*- coding: utf-8 -*-
"""
GO-8D — D-04: test suite for the engine-parseability gate.

Cases:
  T-D-04-01  markdown TABLE atomic-facts  -> validator FAIL (rejects divergent format)
  T-D-04-02  standard `## Fatos` + `N. <texto> [ref]` -> validator PASS
  T-D-04-03  missing `## Fatos` header -> FAIL
  T-D-04-04  < MIN_FACTS facts -> FAIL
  T-D-04-05  production regression: all 12 GO-8C study-input BIPs PASS parseability
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_parseability import validate_atomic_facts

PASS = 0
FAIL = 0
RESULTS = []


def check(name, got, expect):
    global PASS, FAIL
    ok = got == expect
    if ok:
        PASS += 1
    else:
        FAIL += 1
    RESULTS.append((name, "PASS" if ok else "FAIL", got))
    print(f"  {'PASS' if ok else 'FAIL'}  {name}  -> got={got} expected={expect}")


# ---- fixture builders --------------------------------------------------------
def write_table(tmp, content):
    p = os.path.join(tmp, "table.md")
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    return p


def write_standard(tmp, n_facts):
    p = os.path.join(tmp, "standard.md")
    lines = ["# Fixture\n", "\n", "## Fatos\n", "\n"]
    for i in range(1, n_facts + 1):
        lines.append(f"{i}. Fato atômico de teste número {i} com referência. `[src-{i}]`\n")
    with open(p, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return p


def write_noheader(tmp):
    p = os.path.join(tmp, "noheader.md")
    with open(p, "w", encoding="utf-8") as f:
        f.write("# Sem cabecalho\n\n1. Fato sem secao Fatos. `[src]`\n")
    return p


with tempfile.TemporaryDirectory() as tmp:
    print("T-D-04 suite")

    # T-D-04-01: markdown table (the BIP-009 failure mode) must FAIL
    table = write_table(tmp, (
        "# BIP-009 tabela\n\n## Fatos\n\n"
        "| # | Fato atomico | Fonte |\n"
        "|---|---|---|\n"
        "| 1 | Primeiro fato tabela. | src-1 |\n"
        "| 2 | Segundo fato tabela. | src-2 |\n"
        "| 3 | Terceiro fato tabela. | src-3 |\n"
    ))
    check("T-D-04-01 table format rejected", validate_atomic_facts(table)["status"], "FAIL")

    # T-D-04-02: standard format must PASS
    std = write_standard(tmp, 20)
    check("T-D-04-02 standard format accepted", validate_atomic_facts(std)["status"], "PASS")

    # T-D-04-03: missing header must FAIL
    check("T-D-04-03 missing '## Fatos' header rejected",
          validate_atomic_facts(write_noheader(tmp))["status"], "FAIL")

    # T-D-04-04: too few facts must FAIL
    small = write_standard(tmp, 5)
    check("T-D-04-04 <15 facts rejected", validate_atomic_facts(small)["status"], "FAIL")

# ---- production regression over GO-8C study-input (read-only) ----------------
print("\nT-D-04-05 production regression (GO-8C study-input, 12 BIPs)")
from validate_parseability import validate_study_input
res = validate_study_input()
all_pass = all(r["af"]["status"] == "PASS" and r["narr"]["status"] == "PASS" for r in res)
check("T-D-04-05 all 12 BIPs parseable", all_pass, True)
for r in res:
    if not (r["af"]["status"] == "PASS" and r["narr"]["status"] == "PASS"):
        print(f"    NOT PASS: {r['bip']} AF={r['af']} NARR={r['narr']}")

print(f"\nTOTAL: {PASS} PASS / {FAIL} FAIL")

import json
json.dump(RESULTS, open(r"D:\ecp-spec\experiments\validation\GO-8D\analysis\d04_test_results.json", "w", encoding="utf-8"),
          indent=2, ensure_ascii=False)
print("saved: GO-8D/analysis/d04_test_results.json")
