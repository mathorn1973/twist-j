#!/usr/bin/env python3
"""Run one immutable synthesis candidate and write a neutral run record."""

from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import platform
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
NAME = re.compile(r"[a-z0-9][a-z0-9-]*")
SHA = re.compile(r"[0-9a-f]{40}")
ALLOWED_ARCHITECTURES = {"aarch64", "x86_64"}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def run_git(*args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        capture_output=True,
    )
    if check and result.returncode:
        fail(result.stderr.decode("utf-8", "replace").strip() or "git failed")
    return result


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalized_architecture() -> str:
    raw = platform.machine().lower()
    aliases = {
        "amd64": "x86_64",
        "arm64": "aarch64",
    }
    value = aliases.get(raw, raw)
    if value not in ALLOWED_ARCHITECTURES:
        fail(f"unsupported architecture: {raw}")
    return value


def neutral_platform() -> str:
    fields: dict[str, str] = {}
    path = Path("/etc/os-release")
    if path.is_file():
        for raw in path.read_text(encoding="utf-8").splitlines():
            if "=" not in raw:
                continue
            key, value = raw.split("=", 1)
            fields[key] = value.strip().strip('"')
    system = fields.get("ID", platform.system()).lower()
    version = fields.get("VERSION_ID", platform.release())
    names = {
        "ubuntu": "Ubuntu",
        "debian": "Debian",
    }
    name = names.get(system, fields.get("NAME", platform.system()))
    value = f"{name} {version}".strip()
    if not value or re.search(r"jas|twister", value, re.IGNORECASE):
        fail("platform name is not neutral")
    return value


def candidate_bytes(candidate: str, relative: str) -> bytes:
    result = run_git("show", f"{candidate}:{relative}")
    return result.stdout


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("reproduction")
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--timeout", type=int, default=600)
    args = parser.parse_args()

    name = args.reproduction
    candidate = args.candidate
    if not NAME.fullmatch(name):
        fail("invalid reproduction name")
    if not SHA.fullmatch(candidate):
        fail("candidate must be a full lowercase commit SHA")
    if args.timeout <= 0 or args.timeout > 3600:
        fail("timeout must be between 1 and 3600 seconds")

    run_git("cat-file", "-e", f"{candidate}^{{commit}}")
    head = run_git("rev-parse", "HEAD").stdout.decode().strip()
    if run_git("merge-base", "--is-ancestor", candidate, head, check=False).returncode:
        fail("candidate is not an ancestor of HEAD")

    status = run_git("status", "--porcelain").stdout.decode()
    if status:
        fail("working tree must be clean before the staged run")

    base = Path("reproduce") / name
    verifier = base / "verify.py"
    expected_path = base / "EXPECTED.txt"
    readme = base / "README.md"
    for path in (verifier, expected_path, readme):
        if not (ROOT / path).is_file():
            fail(f"missing {path.as_posix()}")

    allowed_prefix = f"{base.as_posix()}/RUNS/"
    changed = run_git("diff", "--name-only", f"{candidate}..HEAD").stdout.decode().splitlines()
    illegal = [path for path in changed if not path.startswith(allowed_prefix)]
    if illegal:
        fail("post-candidate commits changed non-record paths: " + ", ".join(illegal))

    verifier_bytes = (ROOT / verifier).read_bytes()
    expected = (ROOT / expected_path).read_bytes()
    if candidate_bytes(candidate, verifier.as_posix()) != verifier_bytes:
        fail("verifier differs from the immutable candidate")
    if candidate_bytes(candidate, expected_path.as_posix()) != expected:
        fail("EXPECTED.txt differs from the immutable candidate")

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
    command = f"python3 {verifier.as_posix()}"
    result = subprocess.run(
        [sys.executable, verifier.as_posix()],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        timeout=args.timeout,
    )
    if result.returncode:
        fail(f"verifier exits {result.returncode}")
    if result.stderr:
        fail(f"verifier writes {len(result.stderr)} stderr bytes")
    if result.stdout != expected:
        fail(
            "stdout differs from EXPECTED.txt: "
            f"expected {sha256(expected)}, received {sha256(result.stdout)}"
        )

    architecture = normalized_architecture()
    record = base / "RUNS" / f"{architecture}.md"
    if (ROOT / record).exists():
        fail(f"record already exists: {record.as_posix()}")
    (ROOT / record).parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Synthesis staging run (non-canonical)",
        "",
        f"candidate_commit: {candidate}",
        f"run_base_commit: {head}",
        f"reproduction: {name}",
        f"verifier_sha256: {sha256(verifier_bytes)}",
        f"expected_sha256: {sha256(expected)}",
        f"command: {command}",
        f"platform: {neutral_platform()}",
        f"architecture: {architecture}",
        f"python: {platform.python_version()}",
        f"exit_code: {result.returncode}",
        f"stdout_sha256: {sha256(result.stdout)}",
        f"stdout_bytes: {len(result.stdout)}",
        f"stdout_lines: {len(result.stdout.splitlines())}",
        f"stderr_sha256: {sha256(result.stderr)}",
        f"stderr_bytes: {len(result.stderr)}",
        "result: PASS",
        "",
    ]
    (ROOT / record).write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"STAGING RUN PASS {name} {architecture}")
    print(f"candidate {candidate}")
    print(f"verifier {sha256(verifier_bytes)}")
    print(f"stdout {sha256(result.stdout)} {len(result.stdout)} bytes")
    print(f"record {record.as_posix()}")


if __name__ == "__main__":
    main()
