import sys
import subprocess
import os

BASE = r"D:\ecp-spec\scripts\go8b\operational"

def run(name):
    r = subprocess.run(["py", os.path.join(BASE, name)], capture_output=True, text=True)
    tail = (r.stdout.strip().splitlines() or [""])[-1]
    ok = r.returncode == 0
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {tail}")
    if not ok:
        print(r.stdout)
        print(r.stderr)
    return ok

suites = {
    "C2 (P1)": "p1_c2_permutation.py",
    "C3 (P2)": "p2_c3_taxonomy.py",
    "BIP-VAL (P2)": "p2_bip_val_report.py",
    "GFR (P3)": "p3_tests_gfr.py",
    "WL (P4)": "p4_tests_wl.py",
}

fails = []
for label, script in suites.items():
    if not run(script):
        fails.append(label)

print()
print("=" * 50)
print("CONSOLIDATED INFRASTRUCTURE VALIDATION")
if not fails:
    print("ALL SUITES PASS")
else:
    print("FAILED:", fails)
sys.exit(1 if fails else 0)