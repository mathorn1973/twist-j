#!/usr/bin/env python3
"""One-command replay of preregistration-only, target-free checks."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
CLASSIFIER_STDOUT_SHA256 = (
    "e448f842db9cc6fe2a62e4ea0269da801cfcfb351ba7e27b1a4b898f47b3da82"
)
SKELETON_STDOUT_SHA256 = (
    "54d878ce4445b5860b2b6eab17ea121a49ca1a45230b18f4fbd8dc9e6ab2f496"
)
PACKAGE_FILES = (
    "PREREG.md",
    "README.md",
    "SOURCE_PINS.json",
    "construction_skeleton.py",
    "diagram_classifier.py",
    "run_prereg_checks.py",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run(script: str, *arguments: str) -> bytes:
    completed = subprocess.run(
        [sys.executable, str(ROOT / script), *arguments],
        check=True,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=ROOT,
    )
    if completed.stderr:
        raise AssertionError(f"unexpected stderr from {script}: {completed.stderr!r}")
    return completed.stdout


def main() -> None:
    classifier_first = run("diagram_classifier.py")
    classifier_second = run("diagram_classifier.py")
    if classifier_first != classifier_second:
        raise AssertionError("classifier stdout is not deterministic")
    if sha256(classifier_first) != CLASSIFIER_STDOUT_SHA256:
        raise AssertionError("classifier stdout does not match prereg pin")

    classifier_json_bytes = run("diagram_classifier.py", "--json")
    classifier_json = json.loads(classifier_json_bytes)
    if classifier_json["party_action_image_order"] != 6:
        raise AssertionError("wrong party-action image")
    if classifier_json["party_action_kernel_order"] != 4:
        raise AssertionError("wrong party-action kernel")
    if any(action["class_action"][0] != 0 for action in classifier_json["party_actions"]):
        raise AssertionError("D0 is not fixed by every party")

    skeleton = run("construction_skeleton.py", "--self-test")
    if sha256(skeleton) != SKELETON_STDOUT_SHA256:
        raise AssertionError("skeleton stdout does not match prereg pin")
    if b"TARGET_INVARIANT=NOT_COMPUTED\n" not in skeleton:
        raise AssertionError("target-computation firewall line is missing")

    source_pins = json.loads((ROOT / "SOURCE_PINS.json").read_text("utf-8"))
    if source_pins["policy"]["target_invariants_evaluated_while_making_manifest"]:
        raise AssertionError("source-pin policy contradicts prereg status")

    print("ARTISAN_F8_PREREG_REPLAY_V1")
    print("RUNTIME=PYTHON3_STANDARD_LIBRARY_ONLY")
    print(f"CLASSIFIER_STDOUT_SHA256={sha256(classifier_first)}")
    print(f"CLASSIFIER_JSON_SHA256={sha256(classifier_json_bytes)}")
    print(f"SKELETON_STDOUT_SHA256={sha256(skeleton)}")
    for filename in PACKAGE_FILES:
        path = ROOT / filename
        print(f"FILE_SHA256 {filename} {sha256(path.read_bytes())}")
    print("SOURCE_IO=NONE")
    print("TARGET_INVARIANT=NOT_COMPUTED")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
