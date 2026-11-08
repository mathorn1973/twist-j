#!/usr/bin/env python3
"""Capture-only reproduction of immutable S3 programs; standard library."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

SOURCE_COMMIT = "73f3cb4946b05f5d63aba1c279642f77c699caef"
NOTE = "notes/C-S3-HEIGHT-PHASE-INTERFACE-N"
PROGRAMS = (
    ("verify", "CONSTRUCTIVE-3/verify.py", "CONSTRUCTIVE-3/EXPECTED.txt", 120),
    ("audit", "CONSTRUCTIVE-3/audit.py", "CONSTRUCTIVE-3/AUDIT_EXPECTED.txt", 120),
    ("assembly", "CONSTRUCTIVE-3/assembly.py", "CONSTRUCTIVE-3/ASSEMBLY_EXPECTED.txt", 600),
    ("search", "search.py", "EXPECTED.txt", 120),
)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def git(source, *args):
    return subprocess.check_output(["git", "-C", str(source), *args])

def custody(source, manifest):
    if git(source, "rev-parse", "HEAD").decode().strip() != SOURCE_COMMIT:
        raise ValueError("source commit mismatch")
    if git(source, "status", "--porcelain"):
        raise ValueError("source checkout is not clean")
    for row in manifest["files"]:
        data = (source / row["path"]).read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if len(data) != row["bytes"] or sha(data) != row["sha256"] or blob != row["blob"]:
            raise ValueError("source manifest mismatch")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--architecture", required=True, choices=("x86_64", "aarch64"))
    args = parser.parse_args()
    source, output = args.source.resolve(), args.output.resolve()
    if output == source or source in output.parents:
        raise ValueError("output must be outside the source checkout")
    actual = {"amd64": "x86_64", "arm64": "aarch64"}.get(
        platform.machine().lower(), platform.machine().lower())
    if actual != args.architecture:
        raise ValueError("architecture mismatch")
    required_python = {"x86_64": (3, 12), "aarch64": (3, 13)}[actual]
    if sys.version_info[:2] != required_python:
        raise ValueError("Python minor version mismatch")
    if not __debug__:
        raise ValueError("assertions must be enabled")
    manifest = json.loads(Path(__file__).with_name("SOURCES.json").read_text(encoding="utf-8"))
    if manifest["source_commit"] != SOURCE_COMMIT or len(manifest["files"]) != 25:
        raise ValueError("manifest contract mismatch")
    custody(source, manifest)
    output.mkdir(parents=True, exist_ok=False)
    receipt = {
        "experiment": "S3-ARCHITECTURE-REPLAY-4",
        "source_commit": SOURCE_COMMIT,
        "architecture": actual,
        "system": platform.system(),
        "release": platform.release(),
        "python": platform.python_version(),
        "runner_sha256": sha(Path(__file__).read_bytes()),
        "manifest_sha256": sha(Path(__file__).with_name("SOURCES.json").read_bytes()),
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "programs": [],
        "result": "INCOMPLETE",
    }
    def save():
        (output / "receipt.json").write_bytes(
            (json.dumps(receipt, sort_keys=True, indent=2) + "\n").encode("utf-8"))
    save()
    env = dict(os.environ, PYTHONHASHSEED="0", PYTHONDONTWRITEBYTECODE="1",
               LC_ALL="C", LANG="C", TZ="UTC")
    exit_code = 1
    try:
        for name, rel, expected, timeout in PROGRAMS:
            command = [sys.executable, str(source / NOTE / rel)]
            if name == "audit":
                command.append(str(output / "verify.stdout"))
            started = datetime.now(timezone.utc).isoformat()
            began = time.monotonic()
            timed_out = False
            try:
                run = subprocess.run(command, cwd=source, env=env,
                                     capture_output=True, timeout=timeout)
                stdout, stderr, code = run.stdout, run.stderr, run.returncode
            except subprocess.TimeoutExpired as exc:
                stdout, stderr, code = exc.stdout or b"", exc.stderr or b"", None
                timed_out = True
            (output / (name + ".stdout")).write_bytes(stdout)
            (output / (name + ".stderr")).write_bytes(stderr)
            match = stdout == (source / NOTE / expected).read_bytes()
            record = {
                "program": str(Path(NOTE, rel)).replace("\\", "/"),
                "started_utc": started, "elapsed_seconds": time.monotonic() - began,
                "timeout_seconds": timeout, "timed_out": timed_out, "exit_code": code,
                "stdout_bytes": len(stdout), "stderr_bytes": len(stderr),
                "stdout_sha256": sha(stdout), "stderr_sha256": sha(stderr),
                "expected_match": match,
            }
            receipt["programs"].append(record)
            save()
            print(json.dumps({"program": name, "exit": code, "match": match}), flush=True)
            if timed_out or code != 0 or stderr or not match:
                receipt["result"] = "FAIL"
                save()
                break
        else:
            receipt["result"] = "PASS"
            exit_code = 0
    except Exception as exc:
        receipt["result"] = "ERROR"
        receipt["error_type"] = type(exc).__name__
    finally:
        try:
            custody(source, manifest)
            receipt["source_unchanged"] = True
        except Exception as exc:
            receipt["source_unchanged"] = False
            receipt["custody_error_type"] = type(exc).__name__
            if receipt["result"] == "PASS":
                receipt["result"] = "CUSTODY_FAILURE"
            exit_code = 1
        save()
    print("REPLAY " + receipt["result"], flush=True)
    return exit_code

if __name__ == "__main__":
    sys.exit(main())
