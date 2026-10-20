#!/usr/bin/env python3
"""Capture a pinned auxiliary verifier without overwriting an earlier run."""

from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import os
import platform
import subprocess
import sys


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("part", choices=("contact", "geometry", "independent"))
    parser.add_argument("--run-id", default="run01")
    args = parser.parse_args()
    if not args.run_id or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-" for c in args.run_id):
        parser.error("run-id must contain only letters, digits, underscores or hyphens")

    root = Path(__file__).resolve().parent
    prereg = json.loads((root / "FREEZE.json").read_text(encoding="utf-8"))
    sources = json.loads((root / "IMPLEMENTATIONS.json").read_text(encoding="utf-8"))
    for collection in (prereg["files"], sources["files"]):
        for relative, expected in collection.items():
            if digest(root / relative) != expected:
                raise RuntimeError("Pinned file changed: " + relative)

    source = root / args.part / "verify.py"
    destination = root / "runs" / args.part / args.run_id
    destination.mkdir(parents=True, exist_ok=False)
    stdout_path = destination / "stdout.txt"
    stderr_path = destination / "stderr.txt"
    started = datetime.now(timezone.utc).isoformat()
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONHASHSEED"] = "0"
    command = [sys.executable, str(source)]
    with stdout_path.open("xb") as output, stderr_path.open("xb") as errors:
        process = subprocess.run(command, cwd=root, env=environment, stdout=output, stderr=errors, check=False)
    ended = datetime.now(timezone.utc).isoformat()

    record = {
        "kind": "NON-CANONICAL local auxiliary first-run capture",
        "part": args.part,
        "run_id": args.run_id,
        "started_utc": started,
        "ended_utc": ended,
        "command": command,
        "working_directory": str(root),
        "python": sys.version,
        "machine": platform.machine(),
        "platform": platform.platform(),
        "exit_code": process.returncode,
        "source_sha256": digest(source),
        "prereg_sha256": digest(root / "PREREG.md"),
        "implementations_sha256": digest(root / "IMPLEMENTATIONS.json"),
        "stdout_sha256": digest(stdout_path),
        "stdout_bytes": stdout_path.stat().st_size,
        "stderr_sha256": digest(stderr_path),
        "stderr_bytes": stderr_path.stat().st_size,
    }
    with (destination / "run.json").open("x", encoding="utf-8") as output:
        output.write(json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n")

    summary = dict(record)
    summary["run_directory"] = str(destination)
    try:
        raw_report = stdout_path.read_text(encoding="utf-8")
        try:
            report = json.loads(raw_report)
        except ValueError:
            records = [json.loads(line) for line in raw_report.splitlines() if line.strip()]
            report = records[-1]
            summary["report_records"] = len(records)
        summary["report_status"] = report.get("status")
        summary["passed"] = report.get("passed", report.get("total_checks"))
        summary["failed"] = report.get("failed")
        summary["report_keys"] = sorted(report)
    except (ValueError, UnicodeError) as error:
        summary["report_parse_error"] = str(error)
    if record["stderr_bytes"]:
        summary["stderr_preview"] = stderr_path.read_text(encoding="utf-8", errors="replace")[:3000]
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return process.returncode


if __name__ == "__main__":
    sys.exit(main())
