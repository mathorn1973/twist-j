"""Pinned-source custody and typed Gate 0 audit, not an occurrence simulation."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys


MANIFEST_SHA256 = "30aa7f1f8b27fc0cee45e27df394df31749ef6d39d07730857eb9ea84cbf2c1c"
SCHEMA = "C-OCCURRENCE-CYCLE-COUNT-N/gate0/v1"
CONTRACT = {
    "native_full_state": "N0_times_F5_power6",
    "native_counter_update": "n_to_n_plus_1",
    "native_full_state_finite_cycles": False,
    "native_history_preserving_finite_factor_supplied": False,
    "device_state_type": "category2_complex_vector_or_density",
    "device_actual_state_transition_and_event_map_supplied": False,
    "device_independent_preparation_classes_supplied": False,
    "device_recurrent_fresh_trial_protocol_supplied": False,
    "complete_finite_preparation_descriptor_supplied": False,
    "cycle_counting_enabled": False,
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    require(len(sys.argv) == 2, "usage: verify_contract.py REPOSITORY_ROOT")
    repo = Path(sys.argv[1]).resolve(strict=True)
    require(repo.is_dir(), "repository root is not a directory")
    manifest_bytes = Path(__file__).with_name("SOURCES.json").read_bytes()
    require(hashlib.sha256(manifest_bytes).hexdigest() == MANIFEST_SHA256,
            "frozen source manifest digest differs")
    manifest = json.loads(manifest_bytes)
    require(manifest["schema"] == SCHEMA, "manifest schema differs")
    require(manifest["repository"] == "https://github.com/mathorn1973/twist-j",
            "source repository identity differs")
    require(manifest["hypothesis"] == "occurrence_is_count", "hypothesis differs")
    require(manifest["source_semantics"] ==
            "manually_audited_paper_contract_not_machine_inferred",
            "semantic review disclosure differs")
    require(manifest["gate0"] == CONTRACT, "typed paper contract differs")
    sources = manifest["sources"]
    require([row["id"] for row in sources] ==
            ["canon", "cycle_result", "device_interface", "device_result"],
            "immutable source set differs")

    # These are custody checks. Source meaning is argued in PREREG section 3.
    # git-show receives fixed manifest values as argv, never a shell command.
    for row in sources:
        completed = subprocess.run(
            ["git", "-C", str(repo), "show", row["commit"] + ":" + row["path"]],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
        )
        require(completed.returncode == 0, "source object unavailable: " + row["id"])
        require(completed.stderr == b"", "git stderr for source: " + row["id"])
        require(len(completed.stdout) == row["bytes"], "source length differs: " + row["id"])
        require(hashlib.sha256(completed.stdout).hexdigest() == row["sha256"],
                "source digest differs: " + row["id"])

    # There is deliberately no state enumeration, cycle finder, target-weight
    # evaluator, RNG, partial trial, or comparison to an occurrence law here.
    report = [
        "C-OCCURRENCE-CYCLE-COUNT-N",
        "artifact_custody=PASS sources=4/4 manifest=PINNED",
        "semantic_paper_review=NOT_AUTOMATED",
        "gate0=STOP reason=ACTUAL_FINITE_EVENT_CONTRACT_NOT_SUPPLIED",
        "hypothesis=H_NOT_TESTED",
        "occurrence_runs=0 cycles_counted=0 histories_counted=0",
        "cycle_trace_comparisons=0",
        "epsilon_occurrence=UNDEFINED",
        "new_machine=NONE canon_change=NONE",
    ]
    sys.stdout.buffer.write(("\n".join(report) + "\n").encode("ascii"))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("AUDIT_ERROR: " + str(error), file=sys.stderr)
        raise SystemExit(2)
