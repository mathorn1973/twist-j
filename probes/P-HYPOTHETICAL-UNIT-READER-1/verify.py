#!/usr/bin/env python3
"""Frozen exact audit; verify custody, run two algorithms, compare bytes."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

MANIFEST_SHA256 = "bfe0d650bd273864985159cd63a6623f7fa40df11c8b1525d79c1ab1ee813b34"
INPUT_NAMES = {
    "README.md", "MODEL.md", "PREREG.md", "REVIEW.md",
    "model.py", "primary.py", "independent.py",
}


def check_inputs(directory):
    manifest = (directory / "INPUTS.sha256").read_bytes()
    if hashlib.sha256(manifest).hexdigest() != MANIFEST_SHA256:
        raise RuntimeError("frozen manifest SHA-256 mismatch")
    found = set()
    for line in manifest.decode("ascii").splitlines():
        expected, name = line.split("  ", 1)
        if name not in INPUT_NAMES or name in found:
            raise RuntimeError("unexpected or repeated frozen input")
        found.add(name)
        data = (directory / name).read_bytes()
        if hashlib.sha256(data).hexdigest() != expected:
            raise RuntimeError("frozen input SHA-256 mismatch: " + name)
    if found != INPUT_NAMES:
        raise RuntimeError("incomplete frozen input manifest")


def failure(message, attempts):
    """Retain every attempted child's exact bytes, including partial timeout."""
    receipt = {"error": message, "attempts": attempts}
    sys.stderr.write(json.dumps(receipt, sort_keys=True, indent=2) + "\n")
    raise SystemExit(1)


def attempt_record(program, returncode, timed_out, stdout, stderr):
    return {"program": program, "returncode": returncode,
            "timeout": timed_out, "stdout_hex": (stdout or b"").hex(),
            "stderr_hex": (stderr or b"").hex()}


def main():
    directory = Path(__file__).resolve().parent
    attempts = []
    try:
        check_inputs(directory)
    except (OSError, RuntimeError, ValueError, UnicodeError) as exc:
        failure(str(exc), attempts)
    environment = os.environ.copy()
    environment.update({"LC_ALL": "C.UTF-8", "TZ": "UTC",
                        "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1"})
    outputs = []
    for program in ("primary.py", "independent.py"):
        try:
            result = subprocess.run(
                [sys.executable, "-I", "-B", str(directory / program)],
                cwd=directory, env=environment, capture_output=True,
                timeout=55, check=False,
            )
        except subprocess.TimeoutExpired as exc:
            attempts.append(attempt_record(
                program, None, True, exc.stdout, exc.stderr))
            failure(program + " exceeded 55 seconds", attempts)
        except OSError as exc:
            attempts.append(attempt_record(program, None, False, b"", b""))
            failure(program + " launch error: " + str(exc), attempts)
        attempts.append(attempt_record(
            program, result.returncode, False, result.stdout, result.stderr))
        if result.returncode or result.stderr:
            failure(program + " failed the exact execution gate", attempts)
        outputs.append(result.stdout)
    try:
        check_inputs(directory)
    except (OSError, RuntimeError, ValueError, UnicodeError) as exc:
        failure(str(exc), attempts)
    if outputs[0] != outputs[1]:
        failure("independent scientific stdout differs", attempts)
    if not outputs[0]:
        failure("empty scientific stdout", attempts)
    sys.stdout.buffer.write(outputs[0])


if __name__ == "__main__":
    main()
