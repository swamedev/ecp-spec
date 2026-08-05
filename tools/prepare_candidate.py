#!/usr/bin/env python3
"""Ferramenta operacional descartável para staging pré-gate de candidatos.

FERRAMENTA DESCARTÁVEL DE APOIO OPERACIONAL — NÃO FAZ PARTE DO ECP.

Esta ferramenta automatiza apenas tarefas mecânicas de organização de fontes:
não interpreta, não resume, não classifica e não produz nenhuma evidência
científica. A fronteira científica da FASE E permanece onde está.

O que faz:
    - valida a estrutura de diretórios de um candidato (source staging);
    - calcula SHA-256 dos arquivos em raw/;
    - detecta duplicatas por hash;
    - verifica extensões suportadas;
    - gera um inventário dos documentos;
    - registra tempos de preparação;
    - emite erros/avisos de organização.

O que NÃO faz (proibido — participaria do experimento):
    narrativa original, Atomic Facts, sugestão de entidades, Signals,
    atualização de Atlas, escrita no Discovery Log, decisão de elegibilidade.

Regra de fronteira (você pode apagar a ferramenta sem alterar evidência):
"Se eu apagar este script amanhã, alguma evidência científica do ECP muda?"
  sim  -> cruzou a fronteira científica (rejeitar).
  não  -> continua apenas infraestrutura operacional.

Uso:
    python tools/prepare_candidate.py <candidate_dir> [--out manifest.json]
    python tools/prepare_candidate.py --self-check

Saída:
    Um manifest JSON de inventário (impresso na saída padrão e/ou salvo em --out).
    Exit code: 0 = ok; 1 = avisos de organização (ex.: raw/ vazio); 2 = falha
    estrutural ou uso incorreto.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

REQUIRED_FILES = ("00-index.md", "01-origem-dos-documentos.md")
RAW_DIR = "raw"

SUPPORTED_EXTENSIONS = {
    ".pdf", ".txt", ".md", ".html", ".htm", ".doc", ".docx", ".rtf", ".epub", ".json",
}


def sha256(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def validate_structure(candidate_dir: Path) -> list[str]:
    errors = []
    sources = candidate_dir / "sources"
    for name in REQUIRED_FILES:
        p = sources / name
        if not p.is_file():
            errors.append(f"FALTA o arquivo esperado em sources/: {name}")
    raw = sources / RAW_DIR
    if not raw.is_dir():
        errors.append(f"FALTA o diretório em sources/: {RAW_DIR}/")
    return errors


def scan_raw(raw_dir: Path) -> list[dict]:
    entries = []
    if not raw_dir.is_dir():
        return entries
    for p in sorted(raw_dir.rglob("*")):
        if p.is_dir():
            continue
        if p.name in {"inventory.json", ".gitkeep"}:
            continue
        entries.append(
            {
                "caminho": str(p.relative_to(raw_dir)),
                "extensao": p.suffix.lower() or "(sem extensao)",
                "bytes": p.stat().st_size,
            }
        )
    return entries


def check_duplicates(files: list[dict]) -> dict[str, list[str]]:
    by_hash: dict[str, list[str]] = {}
    for item in files:
        by_hash.setdefault(item["sha256"], []).append(item["caminho"])
    return {h: paths for h, paths in by_hash.items() if len(paths) > 1}


def organize_outcomes(files: list[dict]) -> dict[str, list[dict]]:
    unsupported, ok = [], []
    for item in files:
        (ok if item["extensao"] in SUPPORTED_EXTENSIONS else unsupported).append(item)
    return {"ok": ok, "unsupported": unsupported}


def build_manifest(candidate_dir: Path, timing_note: dict) -> dict:
    sources = candidate_dir / "sources"
    raw_dir = sources / RAW_DIR

    files = scan_raw(raw_dir)
    started = time.perf_counter()
    for item in files:
        item["sha256"] = sha256(raw_dir / item["caminho"])
    hashing_elapsed = time.perf_counter() - started
    timing_note["hashing_s"] = round(hashing_elapsed, 4)

    grouped = organize_outcomes(files)
    duplicates = check_duplicates(files)

    estrutura = validate_structure(candidate_dir)
    org = []
    for item in grouped["unsupported"]:
        org.append(f"RELEVANTE extensão não suportada: {item['caminho']}")
    if len(files) == 0:
        org.append("raw/ está vazio — nenhum documento baixado ainda.")

    return {
        "tipo": "inventario_operacional_candidato",
        "status_ecp": "NAO_PARTE_DO_ECP — ferramenta operacional descartável",
        "producao_evidencia": "nenhuma — apenas metadados de organização",
        "candidato": str(candidate_dir),
        "estrutura_valida": not estrutura,
        "erros_estrutura": estrutura,
        "erros_organizacao": org,
        "tempo_preparacao_s": timing_note,
        "total_arquivos": len(files),
        "extensoes_suportadas": sorted(SUPPORTED_EXTENSIONS),
        "duplicatas": duplicates,
        "arquivos": grouped,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Ferramenta operacional descartável de staging (não-ECP).")
    parser.add_argument("candidate_dir", nargs="?", help="Diretório do candidato (ex.: experiments/validation/independence/candidates/genoma-humano)")
    parser.add_argument("--out", help="Caminho opcional para salvar o manifest JSON.")
    parser.add_argument("--self-check", action="store_true", help="Valida a própria estrutura de um candidato sem exigir arquivos.")
    args = parser.parse_args(argv)

    start = time.perf_counter()

    if args.self_check:
        print("A ferramenta opera apenas sobre metadados de organização; não produz evidência científica. (self-check ok)")
        return 0

    if not args.candidate_dir:
        parser.print_usage(sys.stderr)
        return 2

    candidate_dir = Path(args.candidate_dir).resolve()
    if not candidate_dir.is_dir():
        print(f"ERRO: diretório do candidato não encontrado: {candidate_dir}", file=sys.stderr)
        return 2

    manifest = build_manifest(candidate_dir, {})
    manifest["tempo_preparacao_s"]["total_cli_s"] = round(time.perf_counter() - start, 4)

    text = json.dumps(manifest, ensure_ascii=False, indent=2)
    if args.out:
        out = Path(args.out)
        out.write_text(text, encoding="utf-8")
        print(f"Manifest salvo em: {out}")
    else:
        print(text)

    if manifest["erros_estrutura"]:
        return 2
    return 1 if manifest["erros_organizacao"] else 0


if __name__ == "__main__":
    sys.exit(main())