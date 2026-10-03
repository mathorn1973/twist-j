#!/usr/bin/env python3
"""Public frozen wrapper: exact primary and separately authored control audit."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
INDEPENDENT = "independent_native.py"


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("Optimized Python execution is outside the contract")
    manifest = (HERE / "INPUTS.sha256").read_bytes()
    seen = set()
    for line in manifest.decode("utf-8").splitlines():
        expected, name = line.split("  ", 1)
        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts or name in seen:
            raise RuntimeError("Invalid or duplicate frozen input path")
        seen.add(name)
        actual = hashlib.sha256((HERE / relative).read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError(f"Frozen input mismatch: {name}")
    if not {"primary.py", INDEPENDENT, "PREREG.md"} <= seen:
        raise RuntimeError("Missing required frozen inputs")
    environment = os.environ.copy()
    environment.update(PYTHONDONTWRITEBYTECODE="1", PYTHONHASHSEED="0", PYTHONIOENCODING="utf-8", LC_ALL="C", LANG="C", TZ="UTC")
    reports = {}
    for role, name in (("primary", "primary.py"), ("independent", INDEPENDENT)):
        process = subprocess.run([sys.executable, "-B", str(HERE / name)], cwd=HERE, env=environment, capture_output=True, timeout=270)
        if process.returncode or process.stderr:
            sys.stdout.buffer.write(process.stdout)
            sys.stderr.buffer.write(process.stderr)
            raise RuntimeError(f"{role} failed with exit {process.returncode}")
        if b"\r" in process.stdout or not process.stdout.endswith(b"\n"):
            raise RuntimeError(f"{role} output must use explicit UTF-8/LF bytes")
        reports[role] = json.loads(process.stdout.decode("utf-8"))
    primary, independent = reports["primary"], reports["independent"]
    if independent.get("status") != "PASS":
        raise RuntimeError("Independent audit did not pass")
    if INDEPENDENT == "independent_decoder.py":
        if primary.get("status") != "PASS":
            raise RuntimeError("Primary decoder audit did not pass")
        if independent["api_sha256"] != hashlib.sha256((HERE / "decoder.py").read_bytes()).hexdigest():
            raise RuntimeError("Independent audit used a different decoder")
    else:
        if primary["full_native_seeds"] != independent["full_heads"]:
            raise RuntimeError("Full native carrier counts disagree")
        if primary["full_parameter_tuples_including_time"] != independent["full_parameter_tuples"]:
            raise RuntimeError("Preparation class counts disagree")
        if primary["input_time_checks"] != independent["input_rows"]:
            raise RuntimeError("Receiver input coverage disagrees")
        for t in (1, 2, 3):
            if primary["receiver_configurations"] != independent["receiver_configurations"][str(t)]:
                raise RuntimeError("Receiver configuration counts disagree")
            for s in range(5):
                if primary["receiver_survivors_by_s_and_time"][t-1][s] != independent["survivors_by_time_and_source_sum"][str(t)][str(s)]:
                    raise RuntimeError("Independent receiver decisions disagree")
    # The independent decoder calls the public API as a black box; the native
    # control derives full trajectories independently. Per-program predicates
    # and their exact domains are fixed by PREREG.md and REVIEW-PREREG.md.
    result = {"status": "PASS", "frozen_inputs_sha256": hashlib.sha256(manifest).hexdigest(), "reports": reports}
    sys.stdout.buffer.write((json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
