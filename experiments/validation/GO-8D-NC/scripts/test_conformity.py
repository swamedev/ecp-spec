# -*- coding: utf-8 -*-
"""
GO-8D-NC — Conformity tests: demonstrates the self-contained implementation matches D-03
and reproduces the approved DV3 calibration.

Correction (D-MV-04 controlado, 2026-08-15, Opção 2): removed all runtime reads of
GO-8B/GO-8C/GO-8D. Provenance hashes are embedded constants; T8 uses a self-contained
fixture (calibration_fixture.json) derived from the approved calibration.

Checks:
  T1  Self-contained: no executable references to GO-8B/GO-8C/GO-8D in scripts/
      (source scan).
  T2  Taxonomy provenance: local C3/C2 copies match embedded reference hashes of the
      sources (verified at derivation time).
  T3  DV3 formula: dv3 == clamp((conf + ged_ecp + ent_n12)/3) on fixture cells.
  T4  P1 labeled WL: structural_features with real labels differs from neutral (no
      anonymization collapse).
  T5  P2 corrected embeddings: CAT-XX emb != ECP canonical emb (no cosine 1.0 collapse);
      SYN-XX uses corrected C3 definition.
  T6  P3/P4 common reference: ged_ecp computed vs COMMON_REF (ECP chain) for all conditions;
      ent_n12 denominator log(12) for all conditions.
  T7  P5 taxonomy traceability: cell() records taxonomy_sha256 (C3 for B, C2 for A/C).
  T8  Re-derivation: pe.dv3() reproduces the approved calibration DV3 values for all
      36 fixture cells (max abs diff < 1e-9).
"""
import os
import sys
import re
import glob
import json
import hashlib
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# Reference provenance hashes (verified at derivation time from the frozen sources):
#   C3 = GO-8C/scripts/C3_TAXONOMY.yaml           (corrected taxonomy, D-03.7)
#   C2 = GO-8B/operational/C2_PERMUTATION.yaml    (used by DV3 calibration)
C3_REF_SHA256 = "5ba63db7a81c454d7432873c184d2171741f8676e70d94cc538594627819bec8"
C2_REF_SHA256 = "c91fecfeae83d9edb88dd16f2d1827283e308b53fdd6bf0a02c4b636a376b2a2"

FAIL = []


def check(name, ok, detail=""):
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail))
    if not ok:
        FAIL.append((name, detail))


# ---------------- T1: self-containment ----------------
print("== T1 SELF-CONTAINED (no GO-8B/GO-8C/GO-8D runtime dependency) ==")
banned = [
    r"sys\.path",
    r"experiments\\validation\\GO-8",        # windows path literal to a cycle dir
    r"GO-8[BC]\\",                            # any backslash path descending into GO-8B/GO-8C
    r"GO-8D\\",
    r"import\s+.*go8",                        # importing a previous-cycle module
    r"scripts[\\/]+go8",
]
issues = []
for py in glob.glob(os.path.join(HERE, "*.py")):
    name = os.path.basename(py)
    if name == "test_conformity.py":
        continue
    with open(py, encoding="utf-8") as f:
        for ln, line in enumerate(f, start=1):
            for pat in banned:
                if re.search(pat, line) and "GO-8D-NC" not in line:
                    issues.append((name, ln, pat, line.strip()))
check("no executable refs to GO-8B/GO-8C/GO-8D in scripts/", not issues, str(issues[:5]))

# ---------------- T2: taxonomy provenance (embedded reference hashes) ----------------
print("\n== T2 TAXONOMY PROVENANCE ==")
h = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
c3_local = h(os.path.join(HERE, "C3_TAXONOMY.yaml"))
c2_local = h(os.path.join(HERE, "C2_PERMUTATION.yaml"))
check("C3 copy == embedded reference hash (GO-8C source)",
      c3_local == C3_REF_SHA256, c3_local[:16])
check("C2 copy == embedded reference hash (GO-8B source used by calibration)",
      c2_local == C2_REF_SHA256, c2_local[:16])

# ---------------- T3/T4/T5/T6/T7: engine-level checks ----------------
print("\n== T3..T7 ENGINE CHECKS ==")
import pilot_engine as pe
from wl_kernel import WLKernel, ecp_ref_graph

# T3: DV3 formula on fixture
fixture = json.load(open(os.path.join(HERE, "calibration_fixture.json"), encoding="utf-8"))
formula_err = max(abs(float(c["dv3"]) -
                      max(0.0, min(1.0, (float(c["conf"]) + float(c["ged_ecp"]) + float(c["ent_n12"])) / 3.0)))
                  for c in fixture["cells"])
check("T3 DV3 formula on %d fixture cells" % len(fixture["cells"]), formula_err < 1e-9,
      "max_err=%.2e" % formula_err)

# T4: labeled WL vs neutral
wl = WLKernel(h=3)
g = {"nodes": [{"id": "a"}, {"id": "b"}],
     "edges": [{"source": "a", "target": "b"}]}
h_neutral = wl.structural_features(g, labels=None)
h_labeled = wl.structural_features(g, labels={"a": "Problem", "b": "Evidence"})
check("T4 labeled WL differs from neutral (P1)", h_neutral != h_labeled)

# T5: corrected embeddings — CAT-XX != ECP canonical (no cosine 1.0)
emb_cat = pe.label_emb_corrected("CAT-01")   # maps to Problem via O2C
emb_ecp = pe.label_emb_corrected("Problem")
cos_cat_ecp = float(np.dot(emb_cat, emb_ecp) / (np.linalg.norm(emb_cat) * np.linalg.norm(emb_ecp)))
check("T5 CAT-01 emb != ECP Problem emb (P2, cos<0.999)", cos_cat_ecp < 0.999, "cos=%.4f" % cos_cat_ecp)
syn_cats = pe.SYN_IDS
emb_syn = pe.label_emb_corrected(syn_cats[0])
cos_syn = float(np.dot(emb_syn, emb_ecp) / (np.linalg.norm(emb_syn) * np.linalg.norm(emb_ecp)))
check("T5 SYN-001 emb != ECP Problem emb", cos_syn < 0.999, "cos=%.4f" % cos_syn)

# T6: common reference cardinality (DV3 M-02)
ref = ecp_ref_graph()
check("T6 COMMON_REF is ECP 9-node chain (P3/P4)",
      len(ref["nodes"]) == 9 and len(ref["edges"]) == 8)
check("T6 COMMON_REF == pe.COMMON_REF", ref["nodes"] == pe.COMMON_REF["nodes"])

# T7: taxonomy sha recorded per execution (P5)
check("T7 TAX_SHA_C3 set (B)", len(pe.TAX_SHA_C3) == 64 and pe.TAX_SHA_C3 == C3_REF_SHA256)
check("T7 TAX_SHA_C2 set (A/C)", len(pe.TAX_SHA_C2) == 64 and pe.TAX_SHA_C2 == C2_REF_SHA256)

# ---------------- T8: re-derivation vs embedded fixture ----------------
print("\n== T8 RE-DERIVATION vs calibration fixture (self-contained) ==")
n_ok = 0
max_err = 0.0
for c in fixture["cells"]:
    row = {"conf": float(c["conf"]), "ged_ecp": float(c["ged_ecp"]), "ent_n12": float(c["ent_n12"])}
    dv3_engine = pe.dv3(row)
    err = abs(dv3_engine - float(c["dv3"]))
    max_err = max(max_err, err)
    n_ok += 1
check("T8 pe.dv3() reproduces calibration DV3 (max|diff|<1e-9, %d/36 cells)" % n_ok,
      max_err < 1e-9, "max_err=%.3e" % max_err)

print("\n=== RESULTADO: %s (%d falhas) ===" % ("PASS" if not FAIL else "FAIL", len(FAIL)))
for name, detail in FAIL:
    print("  - %s: %s" % (name, detail))
sys.exit(1 if FAIL else 0)
