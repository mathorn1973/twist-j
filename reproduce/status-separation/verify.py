#!/usr/bin/env python3
"""Current Public Canon theorem/dictionary separation audit.

Standard library only. This witness checks the ledger boundary introduced by
Genesis review G2B. It does not establish new physics or new mathematics; it
verifies that named exact rows remain at T and that their physical readings
are carried by explicit D, C, or O rows.
"""

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "canon" / "REGISTRY.tsv"
NORMATIVE = ROOT / "canon" / "NORMATIVE.tsv"
DEPENDENCIES = ROOT / "canon" / "DEPENDENCIES.tsv"
EVIDENCE = ROOT / "canon" / "EVIDENCE.tsv"
GATES = ROOT / "canon" / "GATES.tsv"
FRONTIER_PROGRAMS = ROOT / "canon" / "FRONTIER_PROGRAMS.tsv"


def load_table(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_rows():
    rows = load_table(REGISTRY)
    normative_rows = load_table(NORMATIVE)
    dependencies = load_table(DEPENDENCIES)
    evidence_rows = load_table(EVIDENCE)
    gate_rows = load_table(GATES)
    program_rows = load_table(FRONTIER_PROGRAMS)
    return (
        rows,
        {row["claim_id"]: row for row in rows},
        {row["item_id"]: row for row in normative_rows},
        dependencies,
        {row["claim_id"]: row for row in evidence_rows},
        {row["gate_id"]: row for row in gate_rows},
        {row["claim_id"]: row for row in program_rows},
    )


def dependency_graph(rows):
    graph = {}
    for row in rows:
        graph.setdefault(row["item_id"], set()).add(row["depends_on"])
    return graph


def reaches(graph, start, target):
    seen = set()
    stack = list(graph.get(start, ()))
    while stack:
        item = stack.pop()
        if item == target:
            return True
        if item in seen:
            continue
        seen.add(item)
        stack.extend(graph.get(item, ()))
    return False


def has_cycle(graph):
    visiting = set()
    visited = set()

    def visit(item):
        if item in visiting:
            return True
        if item in visited:
            return False
        visiting.add(item)
        for dependency in graph.get(item, ()):
            if visit(dependency):
                return True
        visiting.remove(item)
        visited.add(item)
        return False

    return any(visit(item) for item in graph)


def has_status(index, claim_id, status):
    return claim_id in index and index[claim_id]["status"] == status


def scope_lacks(index, claim_id, words):
    scope = index[claim_id]["scope"].lower()
    return all(word.lower() not in scope for word in words)


def scope_contains_all(index, claim_id, phrases):
    scope = index[claim_id]["scope"].lower()
    return all(phrase.lower() in scope for phrase in phrases)


def run():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(newline="\n")

    (
        rows,
        index,
        normative,
        dependencies,
        evidence,
        gates,
        programs,
    ) = load_rows()
    checks = []

    counts = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    expected_counts = {"T": 104, "D": 40, "C": 22, "F": 10,
                       "O": 21, "H": 4}
    checks.append((
        "COUNTS",
        "registry has 201 claims with the current status partition",
        len(rows) == 201 and counts == expected_counts,
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

    checks.append((
        "SCHWINGER",
        "the exact target stays T while its physical realization stays O",
        has_status(index, "QUANT-SCHWINGER-TARGET", "T")
        and has_status(index, "QUANT-SUBSTRATE", "O")
        and all(has_status(index, claim, "T") for claim in
                ("J-MODULUS-CHORD", "BRIDGE-DEFECT"))
        and scope_contains_all(
            index, "QUANT-SCHWINGER-TARGET",
            ("J Jbar / script-Q = 1/(2 pi)", "arithmetic only",
             "no identification"),
        )
        and scope_contains_all(
            index, "QUANT-SUBSTRATE",
            ("physical-realization gate", "remains open"),
        ),
    ))

    c20 = "C20-TEICHMULLER-SPLIT"
    time_tower = "TIME-QUANTUM-TOWER"
    graph = dependency_graph(dependencies)
    c20_outgoing = [
        (row["depends_on"], row["relation"], row["basis"])
        for row in dependencies
        if row["item_id"] == c20
    ]
    checks.append((
        "C20",
        "the L1 C20 theorem stays separate from time and decoder readings",
        has_status(index, c20, "T")
        and normative.get(c20, {}).get("item_type") == "THEOREM"
        and normative.get(c20, {}).get("status") == "T"
        and normative.get(c20, {}).get("layer") == "L1"
        and normative.get(c20, {}).get("gate_ids") == ""
        and normative.get(c20, {}).get("statement_source")
        == "canon/CANON.md::1. The axiom and the two projections"
        and index.get(c20, {}).get("canon_section")
        == "1. The axiom and the two projections"
        and index.get(c20, {}).get("evidence")
        == "probes/P-C20-TEICHMULLER-SPLIT-2"
        and evidence.get(c20, {}).get("location")
        == "probes/P-C20-TEICHMULLER-SPLIT-2"
        and evidence.get(c20, {}).get("evidence_id")
        == "EV-C20-TEICHMULLER-SPLIT"
        and evidence.get(c20, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(c20, {}).get("sha256")
        == "bca1d2850ed40871bc8304defca46ee33f84f31f71a7197b30dfdbc2ded4db90"
        and evidence.get(c20, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(c20, {}).get("architecture_requirement")
        == "two-architecture"
        and scope_contains_all(
            index, c20,
            ("(5) = (lambda)^4 is an equality of ideals",
             "not an element equality", "finite local ring",
             "<J> = <t> x <u> isomorphic to C_4 x C_5",
             "for every m >= 1 the Sylow 2-subgroup of A_m^* is C_4",
             "no A_m contains an element of order 8",
             "no all-k order claim for M_J modulo 5^k",
             "L1 exact arithmetic only", "time", "decoder",
             "L2-L6 claim"),
        )
        and has_status(index, "J-STEP", "T")
        and c20_outgoing == [
            ("J-STEP", "REQUIRES",
             "the reduced matrix leg reconstructs M_R from the four public "
             "J-STEP columns and identifies it with multiplication by J")
        ]
        and has_status(index, time_tower, "C")
        and scope_contains_all(
            index, time_tower,
            ("computed exhaustively for k = 1 to 4",
             "no all-k theorem is claimed"),
        )
        and index.get(time_tower, {}).get("evidence")
        == "reproduce/foundations-places"
        and evidence.get(time_tower, {}).get("location")
        == "reproduce/foundations-places"
        and evidence.get(time_tower, {}).get("evidence_kind") == "REPRODUCTION"
        and not reaches(graph, c20, time_tower)
        and not reaches(graph, time_tower, c20),
    ))

    projective = "TM-SYM2-PROJECTIVE-FOURFOLD"
    semilinear = "TM-SYM2-SEMILINEAR-TWOFOLD"
    reversal = "TM-SYM2-REVERSAL-CLOSURE"
    frozen_owner = "TM-SYM2-MEASURE"
    physical_owner = "TM-SYM2-PHYSICAL-MEASURE"
    selector_gate = "GATE-L1-L5-TM-SYM2-SELECTOR-STREAM"
    born_gate = "GATE-L5-L6-TM-SYM2-BORN-MEASURE"
    tm_theorems = (projective, semilinear, reversal)
    expected_tm_dependencies = {
        projective: {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            ("RAMIFIED-TM-LIFT", "REQUIRES"),
            ("GOLDEN-SIX-LINE-SYM2-FRAME", "REQUIRES"),
        },
        semilinear: {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            (projective, "REQUIRES"),
        },
        reversal: {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            (semilinear, "REQUIRES"),
        },
        physical_owner: {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            ("GOLDEN-SIX-LINE-SYM2-FRAME", "REQUIRES"),
            ("GYRON-DENSITY", "REQUIRES"),
            ("MEASURE-BORN-VERB", "REQUIRES"),
            (projective, "BOUNDED_BY"),
            (semilinear, "BOUNDED_BY"),
            (reversal, "BOUNDED_BY"),
        },
    }
    actual_tm_dependencies = {
        item: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == item
        }
        for item in expected_tm_dependencies
    }
    theorem_to_owner = any(
        row["item_id"] in tm_theorems
        and row["depends_on"] in {frozen_owner, physical_owner}
        for row in dependencies
    )
    theorem_scopes = " ".join(index[item]["scope"].lower()
                              for item in tm_theorems)
    expected_evidence = {
        projective: (
            "probes/P-TM-SYM2-MEASURE-1",
            "f943c0fc8412fd6f39a0d21a6e51fffe4bda2d06ad8ec78e41816e44a35b113d",
        ),
        semilinear: (
            "probes/P-TM-SYM2-SEMILINEAR-GAUGE-1",
            "016bd059695ed9eb9ba21f7f36c9bd1ef90798fc130816ef6537c971080cfa1a",
        ),
        reversal: (
            "probes/P-TM-SYM2-REVERSAL-CLOSURE-1",
            "b329f3a65f821690e8ab1514b6ab2cc9c307ba05ebcccaf6c0d326bd36dc619e",
        ),
    }
    checks.append((
        "TM-SYM2",
        "closed action classifications stay T; fired selector and physical successor stay separated",
        all(has_status(index, item, "T") for item in tm_theorems)
        and normative.get(projective, {}).get("item_type") == "THEOREM"
        and normative.get(projective, {}).get("layer") == "MULTI"
        and normative.get(semilinear, {}).get("layer") == "L5"
        and normative.get(reversal, {}).get("layer") == "L5"
        and all(
            index.get(item, {}).get("evidence") == path
            and evidence.get(item, {}).get("location") == path
            and evidence.get(item, {}).get("sha256") == digest
            and evidence.get(item, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(item, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(item, {}).get("architecture_requirement")
            == "two-architecture"
            for item, (path, digest) in expected_evidence.items()
        )
        and scope_contains_all(
            index, projective,
            ("|Sel_class| = 48", "order 12 and acts freely",
             "four G-orbits of size 12", "NONCANONICAL",
             "nu_s(v_i) = 1/6", "M_s = (1/3)P1 + (2/15)P5",
             "no preferred selector", "or L6 measure"),
        )
        and scope_contains_all(
            index, semilinear,
            ("Gamma_sl = ker(chi_Q chi_F)", "order 24",
             "12 exponent-one members", "two selector orbits of size 24",
             "not adopted as gauge"),
        )
        and scope_contains_all(
            index, reversal,
            ("t_N = (0,1)", "t_R = (1,0)", "t_NR = (1,1)",
             "NONREALIZABLE", "REALIZABLE-E1", "one orbit of size 48",
             "precomposition closure only", "not a postcomposition"),
        )
        and has_status(index, frozen_owner, "F")
        and normative.get(frozen_owner, {}).get("item_type") == "FALSIFIED"
        and normative.get(frozen_owner, {}).get("gate_ids") == selector_gate
        and index.get(frozen_owner, {}).get("evidence")
        == "probes/P-TM-SYM2-MEASURE-1"
        and scope_contains_all(
            index, frozen_owner,
            ("frozen v16 S_TM compound route is falsified",
             "48 exact selectors", "four free projective-linear",
             "NONCANONICAL and N2 fires", "Born branch is not reached",
             "does not falsify", "every future TM-to-measure definition"),
        )
        and has_status(index, physical_owner, "O")
        and normative.get(physical_owner, {}).get("item_type") == "OBLIGATION"
        and normative.get(physical_owner, {}).get("layer") == "MULTI"
        and normative.get(physical_owner, {}).get("gate_ids") == born_gate
        and scope_contains_all(
            index, physical_owner,
            ("epsilon_read = chi_Q chi_F as typed L5 data",
             "rather than quotienting it", "coherence across all 48 selectors",
             "mu_i = 1/6", "1/6 = (1/2)(1/3)",
             "comparison actions only", "no enlarged postcomposition gauge"),
        )
        and gates.get(selector_gate, {}).get("owner_item_id") == frozen_owner
        and gates.get(selector_gate, {}).get("gate_kind") == "FIRED_NEGATIVE"
        and gates.get(selector_gate, {}).get("from_layer") == "L1"
        and gates.get(selector_gate, {}).get("to_layer") == "L5"
        and "four free projective-linear gauge orbits of size 12"
        in gates.get(selector_gate, {}).get("decision_condition", "")
        and gates.get(born_gate, {}).get("owner_item_id") == physical_owner
        and gates.get(born_gate, {}).get("gate_kind") == "OPEN_LIFT"
        and gates.get(born_gate, {}).get("from_layer") == "L5"
        and gates.get(born_gate, {}).get("to_layer") == "L6"
        and "reading orientation retained as typed data"
        in gates.get(born_gate, {}).get("decision_condition", "")
        and frozen_owner not in programs
        and programs.get(physical_owner, {}).get("program_id") == "MEASURE"
        and programs.get(physical_owner, {}).get("queue_role") == "ROOT"
        and programs.get(physical_owner, {}).get("work_state") == "STOP"
        and programs.get(physical_owner, {}).get("work_mode") == "FORMAL"
        and actual_tm_dependencies == expected_tm_dependencies
        and not theorem_to_owner
        and not has_cycle(graph)
        and "nullity" not in theorem_scopes
        and "q(zeta_5)" not in theorem_scopes
    ))

    wall = "WALL-LI2-RUNG"
    wall_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == wall
    }
    wall_quant_edges = [
        row for row in dependencies
        if {row["item_id"], row["depends_on"]} == {wall, "QUANT-SUBSTRATE"}
    ]
    checks.append((
        "WALL-LI2",
        "the exact Li_2 rung stays T while substrate coupling stays O",
        has_status(index, wall, "T")
        and normative.get(wall, {}).get("item_type") == "THEOREM"
        and normative.get(wall, {}).get("layer") == "NOT_APPLICABLE"
        and index.get(wall, {}).get("evidence") == "inline"
        and evidence.get(wall, {}).get("evidence_kind") == "INLINE_CANON"
        and evidence.get(wall, {}).get("location") == "inline"
        and evidence.get(wall, {}).get("sha256")
        == "520d79c7fb2fd2a3c1909877f1a7576ea61488be6652cf5c1a2a7541624b20cd"
        and evidence.get(wall, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(wall, {}).get("architecture_requirement") == "none"
        and wall_dependencies == {
            ("J-PROJECTIONS", "REQUIRES"),
            ("PI-FROM-J", "REQUIRES"),
        }
        and not wall_quant_edges
        and scope_contains_all(
            index, wall,
            ("principal dilogarithm", "pi^2/100", "9 pi^2/100",
             "Galois-orbit real-part sum", "no field-trace claim",
             "substrate coupling", "Schwinger coefficient"),
        )
        and has_status(index, "QUANT-SUBSTRATE", "O")
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
