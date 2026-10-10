#!/usr/bin/env python3
"""Frozen-input, byte-exact comparison of two separate integer audits."""

import base64
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
PROBE = "P-U-OCCUPIED-SUM-COVARIANT-CONTACT-1"
TIMEOUT = 240
# Replaced once during static preparation, before the immutable public pin.
INPUT_SHA256 = {
    "PREREG.md": "cffe55f1f8a89b37bf65b0796ac2aaa18380096c0f7a7e7dc20650878df0144c",
    "PROOF.md": "1172f643c544ecb40fd7880b1b26e98cf036a0b52d9e8747d7ca3c441ac0966a",
    "REVIEW.md": "3dae33b1118d11ab5e98121f006a4371ecb065a2fbad80a295a1d178c69d4ece",
    "independent.py": "6ad152ea9b871580e5b76034245585623162d0bb182bf089eb7a37577da4b228",
    "primary.py": "439cd7c2a8a774204a07d8af3271d8ffb106398e5751559671b60211ae95195e"
}
CHILD_RECORDS = []
KEYS = {
    "class_maps", "class_point_checks", "target_maps", "class_sha256",
    "target_sha256", "linear_coefficients", "full_carrier_source_pairs",
    "full_contact_inverse_checks", "full_generator_commutation_checks",
    "full_m_change_checks", "off_support_unit_counterexample",
    "global_injectivity_counterexample", "prepared_trajectories",
    "prepared_state_boundaries", "prepared_step_inverse_checks",
    "first_record_boundaries", "second_record_boundaries",
    "initial_record_boundaries", "prepared_source_boundaries",
    "trigger_times", "tail_horizon",
}


def fail(message):
    # Preserve every started child, including a successful earlier child.
    # Base64 keeps arbitrary failed stdout/stderr byte-exact and unambiguous.
    failure = {"failure": message, "children": CHILD_RECORDS}
    sys.stderr.write(json.dumps(failure, sort_keys=True) + "\n")
    raise SystemExit(1)


def retain(name, code, stdout, stderr):
    CHILD_RECORDS.append({
        "name": name, "exit_code": code,
        "stdout_base64": base64.b64encode(stdout).decode("ascii"),
        "stderr_base64": base64.b64encode(stderr).decode("ascii"),
    })


def run(name):
    environment = dict(os.environ)
    environment.update(PYTHONHASHSEED="0", PYTHONDONTWRITEBYTECODE="1",
                       LC_ALL="C", TZ="UTC")
    try:
        result = subprocess.run(
            [sys.executable, "-B", str(HERE / name)], cwd=HERE.parents[1],
            env=environment, capture_output=True, timeout=TIMEOUT, check=False,
        )
    except subprocess.TimeoutExpired as error:
        retain(name, "TIMEOUT", error.stdout or b"", error.stderr or b"")
        fail(name + ": fixed child timeout")
    retain(name, result.returncode, result.stdout, result.stderr)
    if result.returncode or result.stderr:
        fail(name + ": nonzero exit or nonempty stderr; no later child executed")
    try:
        parsed = json.loads(result.stdout)
    except (ValueError, UnicodeError):
        fail(name + ": invalid JSON output")
    if not isinstance(parsed, dict) or set(parsed) != KEYS:
        fail(name + ": wrong report schema")
    canonical = (json.dumps(parsed, sort_keys=True, separators=(",", ":"))
                 + "\n").encode("ascii")
    if result.stdout != canonical:
        fail(name + ": noncanonical stdout bytes")
    return result.stdout, parsed


def main():
    if set(INPUT_SHA256) != {"PREREG.md", "PROOF.md", "REVIEW.md",
                             "primary.py", "independent.py"}:
        fail("input manifest is not frozen")
    for name, expected in sorted(INPUT_SHA256.items()):
        if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != expected:
            fail("pinned input mismatch: " + name)
    first, report = run("primary.py")
    second, _ = run("independent.py")
    if first != second:
        fail("independent complete reports disagree")
    result = {"probe": PROBE, "status": "PASS", "audit": report}
    sys.stdout.buffer.write((json.dumps(result, sort_keys=True,
                                       separators=(",", ":")) + "\n").encode("ascii"))


if __name__ == "__main__":
    main()
