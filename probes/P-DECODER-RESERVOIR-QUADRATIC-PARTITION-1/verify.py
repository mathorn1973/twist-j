#!/usr/bin/env python3
"""Pinned exact audit of two explicitly bounded mathematical claims."""
import hashlib
from pathlib import Path

# Reviewed immutable source hashes, frozen before the first scientific run.
EXPECTED_DEPENDENCIES = {
    "partition.py": "9a990cf8f7096a3078b6cc3a2f05d801444511f12865381d1476af9533503c45",
    "audit_partition.py": "82b8f293d3eb9114d4d35d67adcdac09f5c580a63e0596dd7aad29f6d2055a44",
    "PROOF.md": "296cba62fe32484bdbdf04feda5a9c12f7ddd91af15e8dc0597b161dfe49eee9",
}

GATES = (
    "G01_TYPES_ZERO", "G02_INDEPENDENT_PROPAGATION", "G03_RESIDUAL_PARTITION_PSD",
    "G04_PREFIX_GROUPING", "G05_G_METRIC_TRACE", "G06_FIRST_PORT_ROW",
    "G07_POSTPROCESSING_OBSTRUCTION", "G08_THRESHOLD_BOUNDARY",
)
CLAIM_A_GATES = GATES[:5] + GATES[7:]
CLAIM_B_GATES = GATES


def integrity():
    if not __debug__:
        raise RuntimeError("STOP_INTEGRITY: assertions must be enabled")
    if set(EXPECTED_DEPENDENCIES) != {"partition.py", "audit_partition.py", "PROOF.md"}:
        raise RuntimeError("STOP_INTEGRITY: dependency inventory mismatch")
    for name, expected in EXPECTED_DEPENDENCIES.items():
        if len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected):
            raise RuntimeError("STOP_INTEGRITY: dependency hash not frozen: " + name)
        if hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() != expected:
            raise RuntimeError("STOP_INTEGRITY: dependency mismatch: " + name)


def main():
    integrity()
    import audit_partition
    checks = audit_partition.run_checks()
    if tuple(name for name, _ in checks) != GATES or any(type(value) is not bool for _, value in checks):
        raise RuntimeError("STOP_INTEGRITY: unexpected gate inventory or disposition")
    outcomes = dict(checks)
    claim_a = all(outcomes[name] for name in CLAIM_A_GATES)
    claim_b = all(outcomes[name] for name in CLAIM_B_GATES)
    print("PROBE P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1")
    print("MODE CHOICE-EXPLICIT PROOF-FIRST L1")
    for name, passed in checks:
        print("CHECK", name, "PASS" if passed else "FIRED")
    print("CLAIM DECODER-RESERVOIR-QUADRATIC-PARTITION", "CONFIRMED" if claim_a else "FIRED")
    print("CLAIM DECODER-RESERVOIR-QDD-POSTPROCESSING-OBSTRUCTION", "CONFIRMED" if claim_b else "FIRED")
    print("PHYSICAL_EFFECT_INSTRUMENT_OCCURRENCE UNRESOLVED")
    print("BORN_FREQUENCY UNTESTED STOP")
    print("PUBLIC_CLAIMS UNREGISTERED CANON_UNCHANGED")
    print("TERMINAL", "CONFIRMED" if claim_a and claim_b else "SCIENTIFIC-FIRED")


if __name__ == "__main__":
    main()
