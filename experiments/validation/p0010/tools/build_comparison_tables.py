#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_comparison_tables.py
Ferramenta deterministica de apoio a comparacao A x B x C (P-0010).

PAPEL: apenas ORGANIZAR o trabalho humano. NAO analisa.
  - Le os tres arquivos de Atomic Facts (avaliadores A, B, C).
  - Extrai de cada AF: numero | data | texto | fonte (quando presente).
  - Gera as tabelas vazias de comparacao e a matriz de consenso.
  - Gera um relatorio objetivo (apenas contagens; nenhuma correspondencia).

NAO FAZ (por escolha):
  - nao compara textos, nao calcula similaridade, nao usa embeddings;
  - nao usa heuristica de correspondencia, nao infere matches, nao sugere linas;
  - nao ordena nem infera o conteudo de celula vazia.
  As unicas regras sao as do FORMATO (separador " - " + prefixo "AF-nnn" ao iniciar
  de linha). Nada de logica semantica.

USO:
  python build_comparison_tables.py
  Entrada: input/evaluator-{A,B,C}.md
  Saida:   comparison/A-vs-B.csv, B-vs-C.csv, A-vs-C.csv, consensus-matrix.csv
           output/report.txt
"""

import csv
import re
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
P0010_DIR = TOOLS_DIR.parent
INPUT_DIR = P0010_DIR / "input"
COMPARISON_DIR = P0010_DIR / "comparison"
OUTPUT_DIR = P0010_DIR / "output"

INPUT_FILES = {
    "A": INPUT_DIR / "evaluator-A.md",
    "B": INPUT_DIR / "evaluator-B.md",
    "C": INPUT_DIR / "evaluator-C.md",
}


def extract_facts(data):
    """Extrai Atomic Facts de um arquivo de forma mecanica.

    Uma " fact" começa numa linha cujo token AF-nnn aparece no inicio (<=8 chars)
    - padrao dos arquivos: "- **AF-001** -- descricao" ou "AF-001 -- descricao".
    Linhas subsequentes ate a proxima ocorrencia passam a fazer parte do mesmo
    fato (para acomodar quebra de linha do markdown). Cabecalhos (#) encerram.
    """
    facts = []

    def flush(block):
        if not block:
            return
        raw = re.sub(r"\s+", " ", " ".join(block)).strip()
        tok = re.search(r"\bAF-\d{3}\b", raw)
        if not tok:
            return
        fields = [p.strip() for p in re.split(r"\s*—\s*", raw)]
        parts = [p for p in fields if p]
        date = ""
        text = ""
        if len(parts) >= 3:
            date = parts[1]
            text = " — ".join(parts[2:])
        elif len(parts) == 2:
            text = parts[1]
        source = ""
        m = re.search(r"\[\s*([^\[\]]+?)\s*\]\s*$", text)
        if m:
            source = m.group(1).strip()
            text = text[: m.start()].strip()
        facts.append({"id": tok.group(0), "date": date, "text": text, "source": source})

    buf = []
    for line in data.splitlines():
        s = line.strip()
        if re.match(r"^#", s):  # cabecalho encerra o fato corrente
            flush(buf)
            buf = []
            continue
        tok = re.search(r"\bAF-\d{3}\b", s)
        is_fact = tok is not None and tok.start() <= 8
        if is_fact:
            flush(buf)
            buf = []
            buf.append(s)
        elif buf:
            buf.append(s)
    flush(buf)
    return facts


def load(key):
    path = INPUT_FILES[key]
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as fh:
        return extract_facts(fh.read())


def cell(fact):
    body = " — ".join(p for p in (fact["date"], fact["text"]) if p)
    if fact["source"]:
        body = "%s [%s]" % (body, fact["source"])
    return body


def write_rows(path, header, left_key, empty_count):
    with open(path, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        for f in facts.get(left_key) or []:
            w.writerow([f["id"], cell(f)] + [""] * empty_count)


facts = {"A": load("A"), "B": load("B"), "C": load("C")}


def run():
    missing = [INPUT_FILES[k].name for k in ("A", "B", "C") if not INPUT_FILES[k].exists()]
    if missing:
        print("ERROR: missing evaluator(s):")
        for name in missing:
            print("  - %s" % name)
        print("Comparison tables are incomplete.")
        print("No scientific comparison can begin until all required inputs exist.")
        return 1

    counts = {}
    for k in ("A", "B", "C"):
        counts[k] = "%d Atomic Facts" % len(facts[k])

    write_rows(
        COMPARISON_DIR / "A-vs-B.csv",
        ["A", "Texto A", "B", "Texto B", "Tipo", "Observação"],
        "A", 4,
    )
    write_rows(
        COMPARISON_DIR / "B-vs-C.csv",
        ["B", "Texto B", "C", "Texto C", "Tipo", "Observação"],
        "B", 4,
    )
    write_rows(
        COMPARISON_DIR / "A-vs-C.csv",
        ["A", "Texto A", "C", "Texto C", "Tipo", "Observação"],
        "A", 4,
    )
    write_rows(
        COMPARISON_DIR / "consensus-matrix.csv",
        ["Referência", "B", "C", "Status", "Observação"],
        "A", 3,
    )

    report = [
        "Relatorio de preparacao — P-0010 comparacao A x B x C",
        "Gerado por: build_comparison_tables.py (ferramenta deterministica, sem IA)",
        "",
        "Evaluator A: %s" % counts["A"],
        "Evaluator B: %s" % counts["B"],
        "Evaluator C: %s" % counts["C"],
        "",
        "Nenhuma correspondencia foi calculada.",
        "As tabelas aguardam preenchimento humano.",
    ]
    with open(OUTPUT_DIR / "report.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(report) + "\n")
    print("\n".join(report))


if __name__ == "__main__":
    sys.exit(run())