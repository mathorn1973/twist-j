#!/usr/bin/env python3
"""Frozen two-method audit; deterministic stdout and no external inputs."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SHARED = (
    "h0_word_states", "affine_candidates", "affine_preparations",
    "unital_preparations", "unital_inputs", "sum_inputs",
    "context_inputs", "context_collision", "first_tick_context_witness",
    "dependency_cases", "dependency_survivors", "templates", "unital_codes",
)


def audit(streams):
    if not __debug__:
        raise RuntimeError("Assertions must be enabled")
    required = {
        "PREREG.md", "PROOF.md", "VARIABLE-TRACE.md", "AFFINE-THREE-PORT.md",
        "REVIEW.md", "primary.py", "independent.py", "verify.py",
    }
    seen = set()
    for line in (HERE/"INPUTS.sha256").read_text(encoding="ascii").splitlines():
        digest, filename = line.split("  ", 1)
        if filename not in required or filename in seen:
            raise RuntimeError("Unexpected or duplicate frozen input: "+filename)
        actual = hashlib.sha256((HERE/filename).read_bytes()).hexdigest()
        if digest != actual:
            raise RuntimeError("Frozen input hash mismatch: "+filename)
        seen.add(filename)
    if seen != required:
        raise RuntimeError("Incomplete frozen input manifest")
    reports = []
    for filename in ("primary.py", "independent.py"):
        try:
            run = subprocess.run(
                [sys.executable, "-I", str(HERE/filename)],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                check=False, timeout=270,
            )
        except subprocess.TimeoutExpired as error:
            streams.append({
                "file": filename, "exit_code": None, "timeout": True,
                "stdout_hex": (error.stdout or b"").hex(),
                "stderr_hex": (error.stderr or b"").hex(),
            })
            raise RuntimeError(filename+" timed out") from error
        streams.append({
            "file": filename, "exit_code": run.returncode, "timeout": False,
            "stdout_hex": run.stdout.hex(), "stderr_hex": run.stderr.hex(),
        })
        if run.returncode or run.stderr:
            raise RuntimeError(filename+" failed its exit/stderr gate")
        if not run.stdout.endswith(b"\n") or b"\r" in run.stdout:
            raise RuntimeError(filename+" did not produce LF-terminated stdout")
        report = json.loads(run.stdout.decode("ascii"))
        if report.get("status") != "PASS":
            raise RuntimeError(filename+" did not pass")
        reports.append(report)
    for key in SHARED:
        if reports[0][key] != reports[1][key]:
            raise RuntimeError("Independent result mismatch at "+key)
    return {
        "probe": "P-U-NATIVE-FIXED-READ-1",
        "status": "PASS", "schema": 1,
        "direct": reports[0], "matrix": reports[1],
    }


def main():
    streams = []
    try:
        out = audit(streams)
    except Exception as error:
        # Preserve every completed/partial child stream if any gate fails.
        failure = {"error": type(error).__name__+": "+str(error), "streams": streams}
        sys.stderr.buffer.write(
            (json.dumps(failure, sort_keys=True, separators=(",", ":"))
             + "\n").encode("ascii")
        )
        return 1
    sys.stdout.buffer.write((json.dumps(out, sort_keys=True, separators=(",", ":"))
                             + "\n").encode("ascii"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
