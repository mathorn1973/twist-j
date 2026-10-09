#!/usr/bin/env python3
"""Custody wrapper: verify frozen inputs and preserve a first audit execution.

This wrapper performs no mathematical evaluation of its own. It deliberately
refuses to overwrite any first output or run record. Use the ordinary commands
in PREREG.md for later reproductions in separate output files.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time


def utc():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def digest(path):
    data = path.read_bytes()
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("verify.py", "break_check.py"):
        raise SystemExit("usage: python3 -I run_once.py verify.py|break_check.py")
    root = Path(__file__).resolve().parent
    name = sys.argv[1]
    pin = json.loads((root / "FREEZE.json").read_text())
    for entry in pin["files"]:
        observed = digest(root / entry["file"])
        if any(observed[key] != entry[key] for key in ("bytes", "sha256")):
            raise SystemExit("frozen input differs: " + entry["file"])
    stem = name.removesuffix(".py")
    stdout_path = root / (stem + ".first.stdout")
    stderr_path = root / (stem + ".first.stderr")
    record_path = root / (stem + ".run.json")
    if any(path.exists() for path in (stdout_path, stderr_path, record_path)):
        raise SystemExit("first-run custody files already exist; refusing overwrite")
    env = os.environ.copy()
    env.update(LC_ALL="C", LANG="C", TZ="UTC", PYTHONHASHSEED="0",
               PYTHONDONTWRITEBYTECODE="1")
    started = utc()
    before = time.monotonic()
    timed_out = False
    with stdout_path.open("xb") as out, stderr_path.open("xb") as err:
        try:
            result = subprocess.run([sys.executable, "-I", name], cwd=root,
                                    env=env, stdout=out, stderr=err,
                                    timeout=pin["budget_seconds_per_program"],
                                    check=False)
            exit_code = result.returncode
        except subprocess.TimeoutExpired:
            timed_out = True
            exit_code = 124
    duration = time.monotonic() - before
    record = {
        "status": "INCOMPLETE_TIMEOUT" if timed_out else
                  "PASS" if exit_code == 0 and stderr_path.stat().st_size == 0 else "FAIL",
        "program": name,
        "program_custody": digest(root / name),
        "freeze_custody": digest(root / "FREEZE.json"),
        "command": "LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 "
                   "PYTHONDONTWRITEBYTECODE=1 python3 -I " + name,
        "started_utc": started,
        "finished_utc": utc(),
        "elapsed_seconds": round(duration, 6),
        "exit_code": exit_code,
        "timeout_seconds": pin["budget_seconds_per_program"],
        "architecture": platform.machine(),
        "platform": platform.freedesktop_os_release().get("PRETTY_NAME"),
        "python": platform.python_version(),
        "stdout_file": stdout_path.name,
        "stdout": digest(stdout_path),
        "stderr_file": stderr_path.name,
        "stderr": digest(stderr_path),
        "public_gate": False,
        "repeat_run": False,
    }
    for entry in pin["files"]:
        observed = digest(root / entry["file"])
        if any(observed[key] != entry[key] for key in ("bytes", "sha256")):
            record["status"] = "FROZEN_INPUT_CHANGED_DURING_EXECUTION"
    record_path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps(record, sort_keys=True), flush=True)
    return 0 if record["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
