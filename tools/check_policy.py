#!/usr/bin/env python3
"""Dependency-free repository policy gate."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 5 * 1024 * 1024

ALLOWED_ROOT = {
    ".gitattributes", ".github", ".gitignore", "AGENTS.md", "CITATION.cff",
    "LICENSE", "POLICY.md", "README.md", "STATUS.md", "canon", "data",
    "legacy",
    "notes", "probes", "reproduce", "tools",
}
FORBIDDEN_SUFFIXES = {
    ".bak", ".bin", ".dll", ".dylib", ".env", ".exe", ".jam", ".key",
    ".log", ".pem", ".pt", ".pth", ".pyc", ".so", ".token",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def tracked_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            yield path


for path in sorted(ROOT.iterdir()):
    if path.name != ".git" and path.name not in ALLOWED_ROOT:
        fail(f"unapproved root entry: {path.name}")

for path in tracked_files():
    relative = path.relative_to(ROOT)
    if path.stat().st_size > MAX_BYTES:
        fail(f"file exceeds 5 MiB: {relative}")
    if path.suffix.lower() in FORBIDDEN_SUFFIXES or path.name.startswith(".env"):
        fail(f"forbidden file: {relative}")

status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
for field in ("STATE:", "CANON:", "AUTHORITY:", "CUTOVER:"):
    if field not in status:
        fail(f"STATUS.md lacks {field}")

probes = ROOT / "probes"
if probes.exists():
    for probe in sorted(path for path in probes.iterdir() if path.is_dir()):
        if not probe.name.startswith("P-"):
            fail(f"probe directory must start P-: {probe.name}")
        for required in (
            "PREREG.md", "verify.py", "EXPECTED.txt", "RUN.md", "RESULT.md"
        ):
            if not (probe / required).is_file():
                fail(f"{probe.name} lacks {required}")

workflows = ROOT / ".github" / "workflows"
workflow_files = {path.name for path in workflows.iterdir() if path.is_file()}
if workflow_files != {"policy.yml"}:
    fail("policy.yml must be the only workflow")
workflow = (workflows / "policy.yml").read_text(encoding="utf-8")
for invariant in (
    "permissions:\n  contents: read",
    "timeout-minutes: 15",
    "actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5",
    "persist-credentials: false",
    "actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065",
):
    if invariant not in workflow:
        fail(f"workflow lacks security invariant: {invariant}")
if "pull_request_target:" in workflow:
    fail("pull_request_target is forbidden")

print("POLICY PASS")
