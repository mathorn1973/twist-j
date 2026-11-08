#!/usr/bin/env python3
"""Replay three previously exposed exact audits without repository writes.

NON-CANONICAL / L1. This is a publication audit, not a formal public probe,
blind review, or independent-author confirmation. The three component bodies
and stdout are retained from the declared source package. Temporary generated
JSON is checked by its prior digest, then discarded. The shell/classifier
cross-check repeats an already exposed audit using the included shell census.
"""

from collections import Counter
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent
# These are input fixtures from earlier exposed runs, not outputs invented
# after publication replay. SOURCES.md records their origin.
AUDITS = (
    (
        "classification",
        "d6e1dd491f596a1706a9e76c2f7c64b1ddc6a178a3a5e8b483bf76c5d33745f5",
        "74aee98fad8ba623ebf5aa59e7d767971e8f603e3397764773e30a46c8a93252",
        {"CLASSIFICATION_RESULTS.json":
         "6dbb162da62e911f8a774ea1af92b0b16c00ae2ac3167e115f4f326572b60440"},
    ),
    (
        "shell",
        "8115b641d021b2a12fc3203136c3b9e04a9d496528db32760b249b321458a70c",
        "66c938b723a7531204e37bc27cb1d24d6e56c45293dbe10dc383b6754287d035",
        {"results.json":
         "66c938b723a7531204e37bc27cb1d24d6e56c45293dbe10dc383b6754287d035",
         "shell_witness.json":
         "b0ee8b4c8582a2ea222d0f9b5941961d847db60391dd29ad9298483c63be582f"},
    ),
    (
        "phase",
        "d9796092866e3915a55e6522eabb2dd8ff0f96f31e95d5a70c19a87549ba1b2f",
        "5a48598f1e1d66faa19770ad98dd351f8584d87f748c8af7245e6c1dcdf75095",
        {"results.json":
         "175c1551cb74f308e8fb47a6a6f3be712e5e003649d0618734193fe20d109f3c"},
    ),
)

# kind, maximum depth, least period, rejection count, states, orbits.
# This is the prior CROSSCHECK_SHELL_CLASSIFICATION.json table.
EXPECTED_CROSSCHECK = (
    ("five_cycle", 0, 5, 5, 360, 72),
    ("one_rejection_fixed", 0, 1, 1, 8, 8),
    ("one_rejection_fixed", 2, 21, 16, 42, 2),
    ("two_rejection_fixed", 0, 1, 2, 2210, 2210),
    ("two_rejection_fixed", 1, 9, 8, 234, 26),
    ("two_rejection_fixed", 2, 41, 32, 41, 1),
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def crosscheck(classifier_path, shell_path):
    """Check every state, orbit type, rejection count and relative bound."""
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("rhythm_classifier", classifier_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    shell = json.loads(shell_path.read_text())
    states = [tuple(tuple(a) for a in state) for state in shell["states"]]
    assert len(states) == 2895 and len(shell["cycles"]) == 2319
    state_counts = Counter()
    orbit_counts = Counter()
    visited = set()
    for cycle in shell["cycles"]:
        key = None
        rejections = 0
        for index in cycle:
            assert index not in visited
            visited.add(index)
            state = states[index]
            prediction = module.classify(state)
            assert prediction["P"] == len(cycle)
            current = (prediction["kind"], prediction["depth"],
                       prediction["P"], prediction["R"])
            assert key is None or current == key
            key = current
            state_counts[current] += 1
            relative = 3 * module.energy(state) - module.Q(module.state_sum(state))
            assert relative == 64 and 3 * prediction["P"] <= 2 * relative - 5
            after, rejected = module.F(state)
            assert after == states[shell["F_index"][index]]
            rejections += rejected
        assert key[3] == rejections
        assert key[1] == max(module.depth(states[index]) for index in cycle)
        orbit_counts[key] += 1
    assert visited == set(range(len(states)))
    rows = tuple(key + (state_counts[key], orbit_counts[key])
                 for key in sorted(state_counts))
    assert rows == EXPECTED_CROSSCHECK


def main():
    if sys.flags.optimize:
        raise RuntimeError("Assertions must remain enabled; do not use -O.")
    environment = os.environ.copy()
    environment.update({
        "LC_ALL": "C", "LANG": "C", "TZ": "UTC",
        "PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0",
        "PYTHONOPTIMIZE": "0",
    })
    with tempfile.TemporaryDirectory(prefix="twist_rhythm_audit_") as temporary:
        temporary = Path(temporary)
        for name, source_hash, stdout_hash, products in AUDITS:
            source = ROOT / ("verify_" + name + ".py")
            expected = (ROOT / ("EXPECTED-" + name + ".txt")).read_bytes()
            assert digest(source.read_bytes()) == source_hash, (name, "source hash")
            assert digest(expected) == stdout_hash, (name, "expected stdout hash")
            working = temporary / name
            working.mkdir()
            copied = working / source.name
            shutil.copyfile(source, copied)
            run = subprocess.run(
                [sys.executable, "-B", str(copied)], cwd=working,
                env=environment, capture_output=True, timeout=600,
            )
            assert run.returncode == 0, (name, "exit code", run.returncode)
            assert run.stderr == b"", (name, "nonempty stderr")
            assert run.stdout == expected, (name, "stdout mismatch", digest(run.stdout))
            for filename, expected_hash in products.items():
                assert digest((working / filename).read_bytes()) == expected_hash, (
                    name, "generated data mismatch", filename)
            print("PASS", name, "exact stdout and generated-data digests")
        crosscheck(temporary / "classification" / "verify_classification.py",
                   temporary / "shell" / "shell_witness.json")
        print("PASS classifier versus all 2895 shell states and 2319 complete cycles")
    print("RESULT PASS: three exposed-source audits; NON-CANONICAL L1")


if __name__ == "__main__":
    main()
