#!/usr/bin/env python3
"""Frozen analysis wrapper: records the analyzer's own process outcome.

Runs analyze.py on an untouched run_snake.py output directory as a subprocess,
preserves its stdout as analysis.json and its stderr as analysis.stderr inside
that directory, records exit code, byte counts and SHA-256 values in
analysis_execution.json, and writes SHA256SUMS_FINAL over every file in the
directory. It changes no threshold and reads no scientific value.
"""
from pathlib import Path
import argparse
import hashlib
import json
import platform
import subprocess
import sys
import time


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path, help="run_snake.py output directory")
    args = parser.parse_args()
    out = args.output.resolve(strict=True)
    analyzer = Path(__file__).resolve().with_name("analyze.py")
    for name in ("analysis.json", "analysis.stderr", "analysis_execution.json", "SHA256SUMS_FINAL"):
        if (out / name).exists():
            print(f"refusing to overwrite existing {name}", file=sys.stderr)
            return 3
    started = time.monotonic()
    with (out / "analysis.json").open("wb") as stdout, (out / "analysis.stderr").open("wb") as stderr:
        completed = subprocess.run([sys.executable, str(analyzer), str(out)],
                                   stdout=stdout, stderr=stderr, check=False)
    record = {
        "analyzer": analyzer.name, "analyzer_sha256": sha256(analyzer),
        "python": platform.python_version(), "exit_code": completed.returncode,
        "seconds": round(time.monotonic() - started, 3),
        "stdout_bytes": (out / "analysis.json").stat().st_size,
        "stderr_bytes": (out / "analysis.stderr").stat().st_size,
        "stdout_sha256": sha256(out / "analysis.json"),
        "stderr_sha256": sha256(out / "analysis.stderr"),
    }
    (out / "analysis_execution.json").write_text(json.dumps(record, indent=2) + "\n")
    files = sorted(p for p in out.iterdir() if p.is_file() and p.name != "SHA256SUMS_FINAL")
    (out / "SHA256SUMS_FINAL").write_text("".join(
        sha256(p) + "  " + p.name + "\n" for p in files))
    print(json.dumps(record, sort_keys=True))
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
