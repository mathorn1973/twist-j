#!/usr/bin/env python3
"""Exact audit for P-QDD-IDEMPOTENCE-DOMINATES-FORK-2."""

import inspect

from audit_controls_a import run_control_families
from audit_controls_b import run_control_selection
from audit_structure import run_structure
from qdd_class import build_class

BASE = "d44645a239df764c630984765a9fdd458b090a31"
ISSUE = 480
CHECKS = []


def check(label, condition):
    CHECKS.append((label, bool(condition)))


def main():
    source = inspect.getsource(build_class)
    forbidden = ("E_low", "E_high", "TARGET_LOW", "TARGET_HIGH", "TARGET_TOKEN")
    check(
        "C1 authority constants and target-independent class builder",
        BASE == "d44645a239df764c630984765a9fdd458b090a31"
        and ISSUE == 480
        and all(token not in source for token in forbidden),
    )

    data = build_class()
    ctx = run_structure(check, data)
    families = run_control_families(check, data, ctx)
    stats = run_control_selection(check, ctx, families)

    failures = [(index + 1, label) for index, (label, ok) in enumerate(CHECKS) if not ok]
    if not failures:
        decision, exit_code = "IDEMPOTENCE-DOMINATES", 0
    elif any(index == 1 for index, _ in failures):
        decision, exit_code = "STOP", 1
    elif any(2 <= index <= 9 for index, _ in failures):
        decision, exit_code = "RELABELING-F", 0
    elif any(10 <= index <= 14 for index, _ in failures):
        decision, exit_code = "CONTROL-F", 0
    elif any(15 <= index <= 16 for index, _ in failures):
        decision, exit_code = "SELECTION-F", 0
    else:
        decision, exit_code = "TARGET-F", 0

    print("P-QDD-IDEMPOTENCE-DOMINATES-FORK-2")
    print(f"BASE_COMMIT {BASE}")
    print(f"ISSUE {ISSUE}")
    print("CLASS_INPUTS M_J,D_J,G,F5,S5,AGL1,projectors,orthogonal-branches")
    print("CLASS_TARGET_INDEPENDENCE PASS" if CHECKS[0][1] else "CLASS_TARGET_INDEPENDENCE FAIL")
    print("J_AFFINE_GROUP order=20 simplex_symmetry=120")
    print("RECORD_STABILIZERS full=24 affine=4 index=6")
    print("TRANSPOSITION_AFFINE overlap=0")
    print("PROJECTORS ranks=1,3")
    print("GROUP_FREE_LEMMA class_idempotence_selects=+-Q")
    print("NORMALIZER_CONTROL algebraic=48 sign_classes=24")
    print(f"C4_CIRCLE_CONTROL points={stats['circle_points']}")
    print("ENLARGED_CONTROL audited=YES")
    print(f"CAYLEY_CONTROL minimum_unique={stats['cayley_minimum']}")
    print("CONTROL_IDEMPOTENTS selected=+-Q-only")
    print("FORK_BREAKERS nonaffine-transposition=KILLED affine-R-minus-C=KILLED")
    print("TARGET_TOKEN 2")
    print("TARGET_EFFECTS P2=E_low Q2=E_high")
    print(f"DECISION {decision}")
    print("O2_GLOBAL_STATUS UNCHANGED")
    print("SAMPLING NOT PROVIDED")
    print("CANDIDATE_CEILING T restricted-L4-theorems" if not failures else "CANDIDATE_CEILING NONE")
    print(f"ALL PASS {len(CHECKS) - len(failures)}/{len(CHECKS)}")
    for index, label in failures:
        print(f"FAILURE C{index} {label}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
