#!/usr/bin/env python3
"""Reproduce every probe changed by a pull request."""

from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PROBES = ROOT / "probes"
EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
REQUIRED = {
    "pin_commit",
    "verifier_sha256",
    "command",
    "platform",
    "architecture",
    "python",
    "exit_code",
    "stdout_sha256",
    "stdout_bytes",
    "stdout_lines",
    "stderr_sha256",
    "stderr_bytes",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def changed_probes(base: str | None) -> list[Path]:
    if not PROBES.exists():
        return []
    if not base:
        return sorted(path for path in PROBES.iterdir() if path.is_dir())
    if not re.fullmatch(r"[0-9a-fA-F]{40}", base):
        fail("base SHA must contain 40 hexadecimal characters")
    command = ["git", "diff", "--name-only", f"{base}...HEAD"]
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    if result.returncode:
        fail(f"cannot read changed paths: {result.stderr.strip()}")
    names = set()
    for raw in result.stdout.splitlines():
        parts = Path(raw).parts
        if len(parts) >= 3 and parts[0] == "probes":
            names.add(parts[1])
    return [PROBES / name for name in sorted(names)]


def read_run(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    pattern = re.compile(r"^([a-z][a-z0-9_]*):\s*(.*?)\s*$")
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            fields[match.group(1)] = match.group(2)
    missing = sorted(REQUIRED - fields.keys())
    if missing:
        fail(f"{path.relative_to(ROOT)} lacks fields: {', '.join(missing)}")
    return fields


def as_nonnegative_int(value: str, field: str, probe: str) -> int:
    try:
        number = int(value)
    except ValueError:
        fail(f"{probe} has invalid {field}")
    if number < 0:
        fail(f"{probe} has negative {field}")
    return number


def reproduce(probe: Path) -> None:
    name = probe.name
    verifier = probe / "verify.py"
    expected_path = probe / "EXPECTED.txt"
    run_path = probe / "RUN.md"
    for path in (verifier, expected_path, run_path):
        if not path.is_file():
            fail(f"{name} lacks {path.name}")

    fields = read_run(run_path)
    relative_verifier = verifier.relative_to(ROOT).as_posix()
    expected_command = f"python3 {relative_verifier}"
    if fields["command"] != expected_command:
        fail(f"{name} command must be: {expected_command}")
    if not re.fullmatch(r"[0-9a-f]{40}", fields["pin_commit"]):
        fail(f"{name} pin_commit must be a full lowercase SHA")
    for field in ("platform", "architecture", "python"):
        if not fields[field]:
            fail(f"{name} has empty {field}")

    verifier_bytes = verifier.read_bytes()
    verifier_hash = sha256(verifier_bytes)
    if fields["verifier_sha256"] != verifier_hash:
        fail(f"{name} verifier SHA-256 differs from RUN.md")
    pinned = subprocess.run(
        ["git", "show", f"{fields['pin_commit']}:{relative_verifier}"],
        cwd=ROOT,
        capture_output=True,
    )
    if pinned.returncode or sha256(pinned.stdout) != verifier_hash:
        fail(f"{name} verifier does not match its pin_commit")
    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", fields["pin_commit"], "HEAD"],
        cwd=ROOT,
    )
    if ancestor.returncode:
        fail(f"{name} pin_commit is not an ancestor of HEAD")

    expected = expected_path.read_bytes()
    if fields["stdout_sha256"] != sha256(expected):
        fail(f"{name} EXPECTED.txt SHA-256 differs from RUN.md")
    if as_nonnegative_int(fields["stdout_bytes"], "stdout_bytes", name) != len(expected):
        fail(f"{name} EXPECTED.txt byte count differs from RUN.md")
    if as_nonnegative_int(fields["stdout_lines"], "stdout_lines", name) != len(expected.splitlines()):
        fail(f"{name} EXPECTED.txt line count differs from RUN.md")
    if fields["exit_code"] != "0":
        fail(f"{name} local exit_code is not zero")
    if fields["stderr_sha256"] != EMPTY_SHA256 or fields["stderr_bytes"] != "0":
        fail(f"{name} local stderr is not empty")

    environment = os.environ.copy()
    environment.update(
        {
            "LC_ALL": "C",
            "LANG": "C",
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONHASHSEED": "0",
            "TZ": "UTC",
        }
    )
    result = subprocess.run(
        [sys.executable, relative_verifier],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        timeout=600,
    )
    if result.returncode != 0:
        fail(f"{name} GitHub run exits {result.returncode}")
    if result.stderr:
        fail(f"{name} GitHub run writes {len(result.stderr)} stderr bytes")
    if result.stdout != expected:
        fail(
            f"{name} stdout mismatch: expected {sha256(expected)}, "
            f"received {sha256(result.stdout)}"
        )
    print(f"VERIFY PASS {name} {verifier_hash} {sha256(result.stdout)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base")
    args = parser.parse_args()
    probes = changed_probes(args.base)
    if not probes:
        print("VERIFY NOT APPLICABLE")
        return
    for probe in probes:
        reproduce(probe)


if __name__ == "__main__":
    main()
