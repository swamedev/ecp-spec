import os
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_PATH = os.path.join(BASE_DIR, "BIP-VAL_REPORT.yaml")
PROTOCOL_PATH = os.path.join(BASE_DIR, "..", "decisions", "NT-05-SEMANTIC-REVIEW-PROTOCOL.md")

EXPECTED_NT05 = "PASS_AI_PANEL (divergence justified)"
EXPECTED_VERDICT = "PASS"
AUTOMATED_NTS = ["NT-01", "NT-02", "NT-03", "NT-04"]


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    results = {}

    report = load_yaml(REPORT_PATH)

    # T-D-03-01: NT-01..04 continuam PASS no BIP-VAL do GO-8C
    tests = report.get("tests", {})
    auto_ok = all(tests.get(nt, {}).get("status") == "PASS" for nt in AUTOMATED_NTS)
    results["T-D-03-01"] = (
        auto_ok,
        f"NT-01..04 status = {[tests.get(nt, {}).get('status') for nt in AUTOMATED_NTS]} (expected all PASS)",
    )

    # T-D-03-02: painel de 2 IAs independentes (tres abas separadas, acesso restrito)
    with open(PROTOCOL_PATH, encoding="utf-8") as f:
        protocol = f.read()
    proto_panel = ("2 IAs independentes" in protocol or "2 AI" in protocol
                   or "painel" in protocol.lower())
    proto_indep = ("independente" in protocol.lower() or "independ" in protocol.lower())
    results["T-D-03-02"] = (
        proto_panel and proto_indep,
        "protocolo exige painel de 2 IAs independentes (rubrica pre-registrada)",
    )

    # T-D-03-03: BIP-VAL_REPORT.yaml reflete a conclusao do painel (PASS)
    # Estado consolidado D-04.7: NT-05 extended PASS com divergencia justificada
    # (aceite da governanca - opcao B1; ver decisions/D-04-NT05-DIVERGENCE-ANALYSIS.md).
    nt05 = tests.get("NT-05", {})
    nt05_ok = nt05.get("status") == EXPECTED_NT05
    verdict_ok = report.get("verdict") == EXPECTED_VERDICT
    reviewers_ok = len(report.get("reviewers", [])) >= 2
    results["T-D-03-03"] = (
        nt05_ok and verdict_ok and reviewers_ok,
        f"NT-05 status = {nt05.get('status')}, verdict = {report.get('verdict')}, "
        f"reviewers = {report.get('reviewers')}",
    )

    for k, (ok, desc) in results.items():
        print(f"{k}: {'PASS' if ok else 'FAIL'} ({desc})")

    n = len(results)
    npass = sum(1 for ok, _ in results.values() if ok)
    print(f"\nTOTAL: {n} PASS: {npass} FAIL: {n - npass}")
    all_pass = all(ok for ok, _ in results.values())
    print("ALL PASS:", all_pass)
    if not all_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
