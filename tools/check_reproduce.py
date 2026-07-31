#!/usr/bin/env python3
"""Run every minimal reproduction changed by a pull request."""

from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
REPRODUCE = ROOT / "reproduce"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def touches_canon(paths: "list[str]") -> bool:
    """True when a changed path lies under canon/.

    A Canon change can invalidate a verifier that reads canon/ at run time even
    though that verifier's own directory is untouched, so the changed-path
    selection below widens to every directory when this returns True.
    """
    return any(Path(raw).parts[:1] == ("canon",) for raw in paths if raw)


def changed_reproductions(base: str | None) -> list[Path]:
    if not REPRODUCE.exists():
        return []
    if not base:
        return sorted(path for path in REPRODUCE.iterdir() if path.is_dir())
    if not re.fullmatch(r"[0-9a-fA-F]{40}", base):
        fail("base SHA must contain 40 hexadecimal characters")
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...HEAD"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        fail(f"cannot read changed paths: {result.stderr.strip()}")
    changed = result.stdout.splitlines()
    if touches_canon(changed):
        print("REPRODUCE FULL SWEEP canon change")
        return sorted(path for path in REPRODUCE.iterdir() if path.is_dir())
    names = set()
    for raw in changed:
        parts = Path(raw).parts
        if len(parts) >= 3 and parts[0] == "reproduce":
            names.add(parts[1])
    return [REPRODUCE / name for name in sorted(names) if (REPRODUCE / name).exists()]


def reproduce(path: Path) -> None:
    for name in ("verify.py", "EXPECTED.txt", "README.md"):
        if not (path / name).is_file():
            fail(f"{path.name} lacks {name}")

    expected = (path / "EXPECTED.txt").read_bytes()
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
    relative = (path / "verify.py").relative_to(ROOT).as_posix()
    result = subprocess.run(
        [sys.executable, relative],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        timeout=120,
    )
    if result.returncode:
        fail(f"{path.name} exits {result.returncode}")
    if result.stderr:
        fail(f"{path.name} writes {len(result.stderr)} stderr bytes")
    if result.stdout != expected:
        fail(
            f"{path.name} stdout mismatch: expected {sha256(expected)}, "
            f"received {sha256(result.stdout)}"
        )
    print(
        f"REPRODUCE PASS {path.name} "
        f"{sha256((path / 'verify.py').read_bytes())} {sha256(expected)}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base")
    args = parser.parse_args()
    paths = changed_reproductions(args.base)
    if not paths:
        print("REPRODUCE NOT APPLICABLE")
        return
    for path in paths:
        reproduce(path)


if __name__ == "__main__":
    main()
