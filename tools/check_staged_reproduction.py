#!/usr/bin/env python3
"""Validate synthesis run records against an immutable candidate commit."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
NAME = re.compile(r"[a-z0-9][a-z0-9-]*")
SHA = re.compile(r"[0-9a-f]{40}")
ALLOWED_ARCHITECTURES = {"aarch64", "x86_64"}
REQUIRED_FIELDS = {
    "candidate_commit",
    "run_base_commit",
    "reproduction",
    "verifier_sha256",
    "expected_sha256",
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
    "result",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def run_git(*args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    if check and result.returncode:
        fail(result.stderr.decode("utf-8", "replace").strip() or "git failed")
    return result


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_record(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    pattern = re.compile(r"^([a-z][a-z0-9_]*):\s*(.*?)\s*$")
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            fields[match.group(1)] = match.group(2)
    missing = sorted(REQUIRED_FIELDS - fields.keys())
    if missing:
        fail(f"{path.relative_to(ROOT)} lacks fields: {', '.join(missing)}")
    return fields


def nonnegative(value: str, field: str, record: Path) -> int:
    try:
        number = int(value)
    except ValueError:
        fail(f"{record.relative_to(ROOT)} has invalid {field}")
    if number < 0:
        fail(f"{record.relative_to(ROOT)} has negative {field}")
    return number


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("reproduction")
    parser.add_argument("--candidate", required=True)
    parser.add_argument(
        "--require-architectures",
        nargs="*",
        default=[],
    )
    args = parser.parse_args()

    name = args.reproduction
    candidate = args.candidate
    required_architectures = set(args.require_architectures)
    if not NAME.fullmatch(name):
        fail("invalid reproduction name")
    if not SHA.fullmatch(candidate):
        fail("candidate must be a full lowercase commit SHA")
    if not required_architectures <= ALLOWED_ARCHITECTURES:
        fail("unsupported required architecture")

    run_git("cat-file", "-e", f"{candidate}^{{commit}}")
    head = run_git("rev-parse", "HEAD").stdout.decode().strip()
    if run_git("merge-base", "--is-ancestor", candidate, head, check=False).returncode:
        fail("candidate is not an ancestor of HEAD")

    base = Path("reproduce") / name
    verifier = base / "verify.py"
    expected_path = base / "EXPECTED.txt"
    records_dir = ROOT / base / "RUNS"
    for path in (verifier, expected_path):
        if not (ROOT / path).is_file():
            fail(f"missing {path.as_posix()}")

    verifier_bytes = (ROOT / verifier).read_bytes()
    expected = (ROOT / expected_path).read_bytes()
    candidate_verifier = run_git(
        "show", f"{candidate}:{verifier.as_posix()}"
    ).stdout
    candidate_expected = run_git(
        "show", f"{candidate}:{expected_path.as_posix()}"
    ).stdout
    if verifier_bytes != candidate_verifier:
        fail("current verifier differs from the candidate")
    if expected != candidate_expected:
        fail("current EXPECTED.txt differs from the candidate")

    allowed_prefix = f"{base.as_posix()}/RUNS/"
    changed = run_git("diff", "--name-only", f"{candidate}..HEAD").stdout.decode().splitlines()
    illegal = [path for path in changed if not path.startswith(allowed_prefix)]
    if illegal:
        fail("post-candidate commits changed non-record paths: " + ", ".join(illegal))

    records = sorted(records_dir.glob("*.md")) if records_dir.is_dir() else []
    architectures: set[str] = set()
    for record in records:
        fields = parse_record(record)
        architecture = fields["architecture"]
        if architecture not in ALLOWED_ARCHITECTURES:
            fail(f"{record.relative_to(ROOT)} has unsupported architecture")
        if record.stem != architecture:
            fail(f"{record.relative_to(ROOT)} filename must match architecture")
        if architecture in architectures:
            fail(f"duplicate architecture record: {architecture}")
        architectures.add(architecture)

        if fields["candidate_commit"] != candidate:
            fail(f"{record.relative_to(ROOT)} candidate mismatch")
        run_base = fields["run_base_commit"]
        if not SHA.fullmatch(run_base):
            fail(f"{record.relative_to(ROOT)} has invalid run_base_commit")
        if run_git(
            "merge-base", "--is-ancestor", candidate, run_base, check=False
        ).returncode:
            fail(f"{record.relative_to(ROOT)} run base predates candidate")
        if run_git(
            "merge-base", "--is-ancestor", run_base, head, check=False
        ).returncode:
            fail(f"{record.relative_to(ROOT)} run base is not in current history")
        if fields["reproduction"] != name:
            fail(f"{record.relative_to(ROOT)} reproduction mismatch")
        if fields["verifier_sha256"] != sha256(verifier_bytes):
            fail(f"{record.relative_to(ROOT)} verifier hash mismatch")
        if fields["expected_sha256"] != sha256(expected):
            fail(f"{record.relative_to(ROOT)} expected hash mismatch")
        if fields["command"] != f"python3 {verifier.as_posix()}":
            fail(f"{record.relative_to(ROOT)} command mismatch")
        if re.search(r"jas|twister", fields["platform"], re.IGNORECASE):
            fail(f"{record.relative_to(ROOT)} platform is not neutral")
        if not fields["platform"] or not fields["python"]:
            fail(f"{record.relative_to(ROOT)} has empty platform metadata")
        if fields["exit_code"] != "0" or fields["result"] != "PASS":
            fail(f"{record.relative_to(ROOT)} does not record a passing run")
        if fields["stdout_sha256"] != sha256(expected):
            fail(f"{record.relative_to(ROOT)} stdout hash mismatch")
        if nonnegative(fields["stdout_bytes"], "stdout_bytes", record) != len(expected):
            fail(f"{record.relative_to(ROOT)} stdout byte count mismatch")
        if nonnegative(
            fields["stdout_lines"], "stdout_lines", record
        ) != len(expected.splitlines()):
            fail(f"{record.relative_to(ROOT)} stdout line count mismatch")
        if fields["stderr_sha256"] != EMPTY_SHA256:
            fail(f"{record.relative_to(ROOT)} stderr hash is not empty")
        if fields["stderr_bytes"] != "0":
            fail(f"{record.relative_to(ROOT)} stderr is not empty")

    missing = sorted(required_architectures - architectures)
    if missing:
        fail("missing staged architectures: " + ", ".join(missing))
    if not records:
        print(f"STAGING RECORDS NOT APPLICABLE {name}")
        return
    print(
        f"STAGING RECORDS PASS {name} candidate={candidate} "
        f"architectures={','.join(sorted(architectures))}"
    )


if __name__ == "__main__":
    main()
