#!/usr/bin/env python3
"""Dependency-free repository policy gate."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 5 * 1024 * 1024

ALLOWED_ROOT = {
    ".github", ".gitignore", "AGENTS.md", "LICENSE", "POLICY.md",
    "README.md", "STATUS.md", "canon", "data", "legacy", "notes",
    "probes", "reproduce", "tools",
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
        for required in ("PREREG.md", "verify.py"):
            if not (probe / required).is_file():
                fail(f"{probe.name} lacks {required}")

print("POLICY PASS")
