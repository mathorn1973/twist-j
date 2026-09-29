#!/usr/bin/env python3
"""One pinned notes-only audit and descriptive reanalysis; never sample."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FROZEN = (
    "PREREG.md", "PROOF.md", "INPUTS.json", "ANALYTICAL_REVIEW.md",
    "AUDIT_SPEC.md", "audit.py", "LOCALIZATION_SPEC.md", "localize.py",
    "run_once.py",
)


def digest(raw):
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pin", required=True)
    args = parser.parse_args()
    if len(args.pin) != 40 or any(c not in "0123456789abcdef" for c in args.pin):
        raise SystemExit("a complete lowercase source pin is required")
    output = HERE / "ENGINEERING"
    if output.exists():
        raise SystemExit("declared output already exists: this execution is consumed")
    if git("status", "--porcelain"):
        raise SystemExit("a clean worktree is required before execution")
    subprocess.run(["git", "merge-base", "--is-ancestor", args.pin, "HEAD"],
                   cwd=ROOT, check=True)
    frozen = {}
    for name in FROZEN:
        relative = (HERE / name).relative_to(ROOT).as_posix()
        raw = (HERE / name).read_bytes()
        if raw != git("show", args.pin + ":" + relative):
            raise SystemExit("frozen source differs from pin: " + name)
        frozen[name] = digest(raw)
    output.mkdir()
    environment = os.environ.copy()
    environment.update(PYTHONHASHSEED="0", PYTHONDONTWRITEBYTECODE="1",
                       LC_ALL="C.UTF-8", TZ="UTC")
    relative = HERE.relative_to(ROOT).as_posix()
    tasks = (
        ("audit", [sys.executable, relative + "/audit.py"], 45),
        ("localization", [sys.executable, relative + "/localize.py", "--repo", ".",
                          "--inputs", relative + "/INPUTS.json", "--output",
                          relative + "/ENGINEERING/localization"], 120),
    )
    records = []
    started = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    for label, command, timeout in tasks:
        before = time.monotonic()
        try:
            done = subprocess.run(command, cwd=ROOT, env=environment,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  timeout=timeout, check=False)
            code, stdout, stderr, timed_out = done.returncode, done.stdout, done.stderr, False
        except subprocess.TimeoutExpired as exc:
            code, stdout, stderr, timed_out = None, exc.stdout or b"", exc.stderr or b"", True
        (output / (label + "_stdout.txt")).write_bytes(stdout)
        (output / (label + "_stderr.txt")).write_bytes(stderr)
        records.append({
            "task": label, "command": ["python3", *command[1:]],
            "timeout_seconds": timeout, "elapsed_seconds": time.monotonic() - before,
            "exit_code": code, "timed_out": timed_out,
            "stdout": digest(stdout), "stderr": digest(stderr),
            "success": code == 0 and not stderr and not timed_out,
        })
        print(label + ": " + ("PASS" if records[-1]["success"] else "FAIL"), flush=True)
    data = {
        "status": "COMPLETE" if all(x["success"] for x in records) else "FAILED_CONSUMED",
        "pin_commit": args.pin, "head_commit": git("rev-parse", "HEAD").decode().strip(),
        "started_utc": started,
        "finished_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "environment": {"platform": platform.system(), "architecture": platform.machine(),
                        "python": platform.python_version(),
                        "deterministic": {k: environment[k] for k in
                                          ("PYTHONHASHSEED", "PYTHONDONTWRITEBYTECODE", "LC_ALL", "TZ")}},
        "frozen": frozen, "tasks": records,
        "scientific_scope": "candidate-C finite exact audit only; localization ZERO scientific evidential weight",
    }
    (output / "execution.json").write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    lines = []
    for path in sorted(output.rglob("*")):
        if path.is_file():
            lines.append(hashlib.sha256(path.read_bytes()).hexdigest() + "  " + path.relative_to(HERE).as_posix())
    (HERE / "SHA256SUMS_RESULTS").write_text("\n".join(lines) + "\n")
    return 0 if data["status"] == "COMPLETE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
