#!/usr/bin/env python3
"""Testes operacionais de prepare_candidate.py (ferramenta não-ECP).

Testa os códigos de saída previsíveis da ferramenta descartável:
    0 = candidato válido;
    1 = avisos de organização (ex.: raw/ vazio);
    2 = falha estrutural (arquivos obrigatórios ausentes) ou uso incorreto.

Não é requisito científico — é guarda de regressão para uma ferramenta
operacional que outros possam modificar no futuro.

Uso:
    python tools/test_prepare_candidate.py
"""
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import prepare_candidate


def build_candidate(tmp: str, *, files: bool = True, raw_file: bool = True) -> Path:
    base = Path(tmp) / "candidate"
    sources = base / "sources"
    sources.mkdir(parents=True)
    raw = sources / "raw"
    raw.mkdir()
    if files:
        (sources / "00-index.md").write_text("# index", encoding="utf-8")
        (sources / "01-origem-dos-documentos.md").write_text("# origens", encoding="utf-8")
    if raw_file:
        (raw / "doc.pdf").write_bytes(b"fake-pdf-content")
    return base


def run(dir_path: Path) -> int:
    with redirect_stdout(io.StringIO()):
        return prepare_candidate.main([str(dir_path)])


class TestExitCodes(unittest.TestCase):
    def test_candidato_valido_exit_0(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(run(build_candidate(tmp)), 0)

    def test_raw_vazio_exit_1(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(run(build_candidate(tmp, raw_file=False)), 1)

    def test_estrutura_invalida_exit_2(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(run(build_candidate(tmp, files=False)), 2)

    def test_diretorio_inexistente_exit_2(self):
        self.assertEqual(run(Path("nao-existe-dir")), 2)

    def test_sem_argumento_exit_2(self):
        with redirect_stdout(io.StringIO()):
            code = prepare_candidate.main([])
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
