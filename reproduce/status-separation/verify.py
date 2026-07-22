#!/usr/bin/env python3
"""Current Public Canon theorem/dictionary separation audit.

Standard library only. This witness checks the registry boundary introduced
by Genesis review G2B. It does not establish new physics or new mathematics;
it verifies that named exact rows remain at T and that their physical readings
are carried by explicit D rows.
"""

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "canon" / "REGISTRY.tsv"


def load_rows():
    with REGISTRY.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    return rows, {row["claim_id"]: row for row in rows}


def has_status(index, claim_id, status):
    return claim_id in index and index[claim_id]["status"] == status


def scope_lacks(index, claim_id, words):
    scope = index[claim_id]["scope"].lower()
    return all(word.lower() not in scope for word in words)


def scope_contains_all(index, claim_id, phrases):
    scope = index[claim_id]["scope"].lower()
    return all(phrase.lower() in scope for phrase in phrases)


def run():
    rows, index = load_rows()
    checks = []

    counts = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    expected_counts = {"T": 98, "D": 40, "C": 22, "F": 9,
                       "O": 20, "H": 5}
    checks.append((
        "COUNTS",
        "registry has 194 claims with the current status partition",
        len(rows) == 194 and counts == expected_counts,
    ))

    checks.append((
        "AXIOM",
        "J and plenum algebra stay T; projection and plenum physics are D",
        all(has_status(index, claim, "T") for claim in
            ("J-PROJECTIONS", "PLENUM-POINT", "J-MODULUS-CHORD",
             "J-RAMIFIED-CHORD"))
        and has_status(index, "AXIOM-PROJECTION-DICTIONARY", "D")
        and scope_lacks(index, "J-PROJECTIONS",
                        ("gravity", "electromagnetism", "force"))
        and scope_lacks(index, "PLENUM-POINT",
                        ("gravity", "space channel", "writes", "reads")),
    ))

    checks.append((
        "PLACES",
        "field and Galois facts stay T; place and CPT physics are D",
        all(has_status(index, claim, "T") for claim in
            ("DEGREES-BY-PRIME", "Z2-PLACES-SPLIT",
             "METAL-TRACE-CASCADE"))
        and has_status(index, "TWO-PLACE-PHYSICS", "D")
        and scope_lacks(index, "DEGREES-BY-PRIME",
                        ("magic", "qubit", "gravity", "born"))
        and scope_lacks(index, "Z2-PLACES-SPLIT", ("cpt", "force", "spin")),
    ))

    checks.append((
        "CARRY",
        "carry lifts and checkpoint no-go stay T; physical readings stay fenced",
        all(has_status(index, claim, "T") for claim in
            ("RAMIFIED-TM-LIFT", "CARRY-J-CHECKPOINT", "CARRY-PENTAD",
             "SQRT-PHI-DIGIT-LIFT"))
        and scope_contains_all(index, "CARRY-PENTAD",
                               ("selects no prime", "physical reading"))
        and scope_contains_all(index, "RAMIFIED-TM-LIFT",
                               ("no checkpoint factorization",
                                "physical carry/phase reading"))
        and scope_contains_all(index, "CARRY-J-CHECKPOINT",
                               ("full forward carrier", "no restricted carrier",
                                "physical reading"))
        and scope_contains_all(index, "SQRT-PHI-DIGIT-LIFT",
                               ("not constant", "no sign-branch selection",
                                "gravity dynamics")),
    ))

    checks.append((
        "FORCE",
        "the finite Weyl commutator stays T; force as curvature is D",
        has_status(index, "FORCE-WEYL-HOLONOMY", "T")
        and has_status(index, "FORCE-AS-CURVATURE", "D")
        and scope_lacks(index, "FORCE-WEYL-HOLONOMY",
                        ("force", "curvature", "gravity", "electromagnetism")),
    ))

    checks.append((
        "MAXWELL",
        "four exact chain rows stay T; the classical Maxwell reading is D",
        all(has_status(index, claim, "T") for claim in
            ("MAXWELL-BIANCHI", "MAXWELL-GAUSS-CHAIN",
             "MAXWELL-AMPERE-CHAIN", "MAXWELL-OBSTRUCTION-P"))
        and has_status(index, "MAXWELL-CLOSED", "D"),
    ))

    checks.append((
        "BORN",
        "finite Born algebra stays T; measurement and cell readings are D",
        all(has_status(index, claim, "T") for claim in
            ("BORN-FACE-WEIGHTS", "BORN-HALF-ANGLE",
             "BORN-RESIDUAL-SPLIT", "SPIN-BISECTOR",
             "BORN-ORDER-STAIRCASE", "SUBSTRATE-KNIT"))
        and all(has_status(index, claim, "D") for claim in
                ("MEASURE-BORN-VERB", "KERNEL-CELL-DICTIONARY"))
        and scope_lacks(index, "SUBSTRATE-KNIT",
                        ("born", "measurement", "abelian face")),
    ))

    color_theorems = (
        "COLOR-RETURN-D5", "COLOR-TORSOR-HOLONOMY",
        "COLOR-KIN-NORMALIZER", "COLOR-CORE-2I", "COLOR-GOLDEN-TABLE",
        "COLOR-MCKAY-E8", "COLOR-MOMENT-FINGERPRINT",
        "COLOR-SPECTRAL-INVARIANTS", "COLOR-DICKSON-RAMIFICATION",
        "COLOR-KLEIN-REDUCTION", "COLOR-INTEGRAL-LIFT",
        "COLOR-MEASURE-TRANSPORT",
    )
    checks.append((
        "COLOR",
        "finite group and invariant rungs stay T; the color reading is D",
        all(has_status(index, claim, "T") for claim in color_theorems)
        and has_status(index, "COLOR-LADDER-DICTIONARY", "D"),
    ))

    checks.append((
        "COSMOLOGY",
        "phase and density identities stay T; their cosmology reading is D",
        all(has_status(index, claim, "T") for claim in
            ("TT-LINEAR-ZERO", "GYRON-DENSITY"))
        and has_status(index, "COSMOLOGY-READING-DICTIONARY", "D")
        and scope_lacks(index, "TT-LINEAR-ZERO",
                        ("tensor", "isotropic", "r = 0", "cosmology"))
        and scope_lacks(index, "GYRON-DENSITY",
                        ("proton", "cosmology", "mass ladder", "basel")),
    ))

    print("TWIST-J theorem/dictionary separation audit")
    print("exact algebra and finite computations remain distinct from physical readings")
    print()
    passed = 0
    for number, (tag, description, ok) in enumerate(checks, 1):
        state = "PASS" if ok else "FAIL"
        print(f"{state} {number:02d} {tag:<10} {description}")
        passed += int(ok)
    print()
    print(f"RESULT {passed}/{len(checks)} "
          f"{'ALL PASS' if passed == len(checks) else 'FAIL'}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    sys.exit(run())
