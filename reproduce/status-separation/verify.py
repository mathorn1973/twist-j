#!/usr/bin/env python3
"""Current Public Canon theorem/dictionary separation audit.

Standard library only. This witness checks the ledger boundary introduced by
Genesis review G2B. It does not establish new physics or new mathematics; it
verifies that named exact rows remain at T and that their physical readings
are carried by explicit D, C, H, or O rows.
"""

import csv
import hashlib
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


def scope_sha256(index, claim_id):
    return hashlib.sha256(index[claim_id]["scope"].encode("utf-8")).hexdigest()


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
    expected_counts = {"T": 114, "D": 40, "C": 23, "F": 10,
                       "O": 24, "H": 4}
    checks.append((
        "COUNTS",
        "registry has 215 claims with the current status partition",
        len(rows) == 215 and counts == expected_counts,
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

    kernel = "KERNEL-Z6-SYNCHRONIZATION"
    kernel_path = "probes/P-KERNEL-Z6-SYNCHRONIZATION-1"
    kernel_digest = "7ac0cae9685575c8bd92f1c3f39603e0fc7a148fae5db80746fbcc1e5e4de1b9"
    kernel_dependencies = [
        row for row in dependencies if row["item_id"] == kernel
    ]
    c8 = "C8-BILINEAR-SHADOW"
    c8_path = "probes/P-C8-BILINEAR-SHADOW-2"
    c8_digest = "72728a88f45af777656a39d313b79c8189e2dfa2fa587e08fac5bf02aa6b234d"
    c8_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == c8
    }
    checks.append((
        "CARRY",
        "carry, synchronization, and C8 shadow theorems stay T and physically fenced",
        all(has_status(index, claim, "T") for claim in
            ("RAMIFIED-TM-LIFT", "CARRY-J-CHECKPOINT", "CARRY-PENTAD",
             "SQRT-PHI-DIGIT-LIFT", kernel, c8))
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
                                "gravity dynamics"))
        and scope_contains_all(index, c8,
                               ("<tau> = F_5^* union tau F_5^*",
                                "branch invariant",
                                "mixed-parity products are off-axis and branch-dependent",
                                "no branch selection",
                                "broader physical or gauge equivalence",
                                "lift to L2-L6"))
        and scope_contains_all(index, kernel,
                               ("at each fixed known n",
                                "q_n is a sheet label and not the checkpoint coordinate q",
                                "no unknown-time or unindexed checkpoint-fiber",
                                "physical-irreversibility",
                                "no L2-L6 claim is included"))
        and normative[kernel]["item_type"] == "THEOREM"
        and normative[kernel]["status"] == "T"
        and normative[kernel]["layer"] == "L1"
        and normative[kernel]["gate_ids"] == ""
        and len(kernel_dependencies) == 1
        and kernel_dependencies[0]["depends_on"] == "DEF-AUTONOMOUS-STATE"
        and kernel_dependencies[0]["relation"] == "REQUIRES"
        and evidence[kernel]["evidence_kind"] == "PUBLIC_PROBE"
        and evidence[kernel]["location"] == kernel_path
        and evidence[kernel]["sha256"] == kernel_digest
        and evidence[kernel]["hash_mode"] == "bundle-manifest-sha256-v1"
        and evidence[kernel]["architecture_requirement"] == "two-architecture"
        and kernel not in programs
        and normative[c8]["item_type"] == "THEOREM"
        and normative[c8]["status"] == "T"
        and normative[c8]["layer"] == "L1"
        and normative[c8]["gate_ids"] == ""
        and c8_dependencies == {
            ("PENTIT-ROOT-FACTS", "REQUIRES"),
            ("RAMIFIED-TM-LIFT", "REQUIRES"),
            ("SQRT-PHI-DIGIT-LIFT", "REQUIRES"),
        }
        and evidence[c8]["evidence_kind"] == "PUBLIC_PROBE"
        and evidence[c8]["location"] == c8_path
        and evidence[c8]["sha256"] == c8_digest
        and evidence[c8]["hash_mode"] == "bundle-manifest-sha256-v1"
        and evidence[c8]["architecture_requirement"] == "two-architecture"
        and c8 not in programs,
    ))

    drift = "DRIFT-IS-THE-READ"
    coin_selector = "COIN-SELECTION-CONDITIONAL"
    coin_premise = "COIN-MINIMAL-READ"
    coin_derivation = "MINIMAL-READ-DERIVATION"
    coin_gate = "GATE-L5-L1-MINIMAL-READ"
    boost_path = "probes/P-BOOST-COHERENCE-1"
    boost_digest = (
        "0e2c9daaee5a7c189615f1941894015be2b9e59a71a1183cfc6ed207c9c8d083"
    )
    boost_items = (drift, coin_selector, coin_premise, coin_derivation)
    expected_boost_dependencies = {
        drift: {
            ("BOOST-READING-SPLIT", "REQUIRES"),
            ("BOOST-COUNT-LADDER", "BOUNDED_BY"),
        },
        coin_selector: {
            ("BOOST-READING-SPLIT", "REQUIRES"),
            ("BOOST-COUNT-LADDER", "BOUNDED_BY"),
            (drift, "REQUIRES"),
        },
        coin_premise: {(coin_selector, "REQUIRES")},
        coin_derivation: {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            (coin_selector, "REQUIRES"),
            ("OBSERVER-WRITE-PORT", "REQUIRES"),
        },
    }
    actual_boost_dependencies = {
        item: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == item
        }
        for item in boost_items
    }
    checks.append((
        "BOOST",
        "exact drift and selector ranking stay T; MINIMAL-READ stays H with derivation O",
        has_status(index, drift, "T")
        and has_status(index, coin_selector, "T")
        and has_status(index, coin_premise, "H")
        and has_status(index, coin_derivation, "O")
        and normative.get(drift, {}).get("item_type") == "THEOREM"
        and normative.get(drift, {}).get("layer") == "L5"
        and normative.get(drift, {}).get("gate_ids") == ""
        and normative.get(coin_selector, {}).get("item_type") == "THEOREM"
        and normative.get(coin_selector, {}).get("layer") == "MULTI"
        and normative.get(coin_selector, {}).get("gate_ids") == ""
        and normative.get(coin_premise, {}).get("item_type") == "HYPOTHESIS"
        and normative.get(coin_premise, {}).get("layer") == "L1"
        and normative.get(coin_premise, {}).get("gate_ids") == ""
        and normative.get(coin_derivation, {}).get("item_type") == "OBLIGATION"
        and normative.get(coin_derivation, {}).get("layer") == "MULTI"
        and normative.get(coin_derivation, {}).get("gate_ids") == coin_gate
        and actual_boost_dependencies == expected_boost_dependencies
        and all(
            evidence.get(item, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(item, {}).get("location") == boost_path
            and evidence.get(item, {}).get("sha256") == boost_digest
            and evidence.get(item, {}).get("hash_mode")
                == "bundle-manifest-sha256-v1"
            and evidence.get(item, {}).get("architecture_requirement")
                == "two-architecture"
            for item in boost_items
        )
        and scope_contains_all(
            index, drift,
            ("division-free spectral skeleton",
             "minimum 16/5",
             "V_inf(1) = -beta_1 A_1",
             "for every N >= 1",
             "P1 and P2 are premises rather than conclusions",
             "no decoherence"),
        )
        and scope_contains_all(
            index, coin_selector,
            ("exactly {beta_1,beta_3}",
             "generic/rung multiplicities 2/1",
             "non-integral half-rung",
             "S1 minimum generic multiplicity",
             "S3 maximum coherent half-width",
             "theorem adopts no selector"),
        )
        and scope_contains_all(
            index, coin_premise,
            ("adopts beta_1 by MINIMAL-READ",
             "MAXIMAL-REACH",
             "not a general equivalence",
             "no claim that the decoder architecture forces MINIMAL-READ"),
        )
        and scope_contains_all(
            index, coin_derivation,
            ("complete registered decoder architecture",
             "without adopting MINIMAL-READ as a premise",
             "typed L5-read to L1-coin selection route"),
        )
        and all(
            phrase.lower() in index[coin_derivation]["falsifier"].lower()
            for phrase in (
                "complete admissible decoder class is proved nonempty",
                "fully compliant beta_1 and beta_3 realizations",
                "failure of no-feedback or any one favored route is STOP",
                "classifies the complete admissible class",
            )
        )
        and gates.get(coin_gate, {}).get("owner_item_id") == coin_derivation
        and gates.get(coin_gate, {}).get("from_layer") == "L5"
        and gates.get(coin_gate, {}).get("to_layer") == "L1"
        and gates.get(coin_gate, {}).get("gate_kind") == "OPEN_SELECTION"
        and all(
            phrase.lower() in gates[coin_gate]["decision_condition"].lower()
            for phrase in (
                "complete typed decoder carrier",
                "cover-to-output map",
                "accumulator/equality rule",
                "redundancy theorem",
                "uniquely force w = 1 and beta_1",
                "complete admissible class is proved nonempty",
                "fully compliant beta_1 and beta_3 realizations",
                "failure of one favored route is only STOP",
            )
        )
        and drift not in programs
        and coin_selector not in programs
        and programs.get(coin_premise, {}).get("program_id") == "DECODER_CORE"
        and programs.get(coin_premise, {}).get("queue_role") == "FOLLOWUP"
        and programs.get(coin_premise, {}).get("work_state") == "BLOCKED"
        and programs.get(coin_premise, {}).get("work_mode") == "FORMAL"
        and programs.get(coin_derivation, {}).get("program_id") == "DECODER_CORE"
        and programs.get(coin_derivation, {}).get("queue_role") == "ROOT"
        and programs.get(coin_derivation, {}).get("work_state") == "STOP"
        and programs.get(coin_derivation, {}).get("work_mode") == "FORMAL",
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

    gyron_density = "GYRON-DENSITY"
    gyron_discrepancy = "GYRON-DISCREPANCY-LOG"
    gyron_fixed_point = "TM-PAIR-SUBSTITUTION-FIXED-POINT"
    gyron_items = (gyron_density, gyron_discrepancy, gyron_fixed_point)
    gyron_path = "probes/P-GYRON-DISCREPANCY-LOG-3"
    gyron_digest = "b4e7eba23b815d0964a8516f25fe3cdc6db363e3646d658253ea5e9289e9382e"
    expected_gyron_dependencies = {
        gyron_density: {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            (gyron_discrepancy, "REQUIRES"),
            (gyron_fixed_point, "REQUIRES"),
        },
        gyron_discrepancy: {("DEF-ARCHITECTURE", "REQUIRES")},
        gyron_fixed_point: {("DEF-ARCHITECTURE", "REQUIRES")},
    }
    actual_gyron_dependencies = {
        item: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == item
        }
        for item in gyron_items
    }
    checks.append((
        "COSMOLOGY",
        "exact L1 Gyron theorems stay T; their physical reading stays D",
        all(has_status(index, claim, "T") for claim in
            ("TT-LINEAR-ZERO",) + gyron_items)
        and has_status(index, "COSMOLOGY-READING-DICTIONARY", "D")
        and scope_lacks(index, "TT-LINEAR-ZERO",
                        ("tensor", "isotropic", "r = 0", "cosmology"))
        and scope_lacks(index, gyron_density,
                        ("proton", "cosmology", "mass ladder", "basel"))
        and scope_contains_all(index, gyron_density,
                               ("both prefix normalizations",
                                "holds iff L is even",
                                "fixed I(v_*) and B(v_*) phase readouts",
                                "physical probability or measure"))
        and scope_contains_all(index, gyron_discrepancy,
                               ("complete 96-path",
                                "d(4L) = d(L) iff L is even",
                                "audit rather than proof",
                                "L2-L6 claim"))
        and scope_contains_all(index, gyron_fixed_point,
                               ("full maps are unequal",
                                "spectrum {1,-1/2,0}",
                                "only under their frozen equal average",
                                "not coarse-graining",
                                "decoder factor"))
        and all(
            normative[item]["item_type"] == "THEOREM"
            and normative[item]["status"] == "T"
            and normative[item]["layer"] == "L1"
            and normative[item]["gate_ids"] == ""
            for item in gyron_items
        )
        and all(
            evidence[item]["evidence_kind"] == "PUBLIC_PROBE"
            and evidence[item]["location"] == gyron_path
            and evidence[item]["sha256"] == gyron_digest
            and evidence[item]["hash_mode"]
                == "bundle-manifest-sha256-v1"
            and evidence[item]["architecture_requirement"]
                == "two-architecture"
            for item in gyron_items
        )
        and actual_gyron_dependencies == expected_gyron_dependencies,
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
             "mu_i = 1/6", "M_TM = (1/3)P1 + (2/15)P5",
             "is an outcome of the bridge and is not required of it",
             "comparison actions only", "enlarge no postcomposition gauge",
             "select no representative among the 48 selectors"),
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

    circle = "WALL-CIRCLE-LEMMA"
    circle_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == circle
    }
    circle_reverse_edges = [
        row for row in dependencies
        if row["item_id"] == wall and row["depends_on"] == circle
    ]
    circle_quant_edges = [
        row for row in dependencies
        if {row["item_id"], row["depends_on"]}
        == {circle, "QUANT-SUBSTRATE"}
    ]
    checks.append((
        "WALL-CIRCLE",
        "the uniform root-circle theorem stays exact and outside physics",
        has_status(index, circle, "T")
        and normative.get(circle, {}).get("item_type") == "THEOREM"
        and normative.get(circle, {}).get("status") == "T"
        and normative.get(circle, {}).get("layer") == "NOT_APPLICABLE"
        and normative.get(circle, {}).get("gate_ids") == ""
        and index.get(circle, {}).get("evidence") == "inline"
        and evidence.get(circle, {}).get("evidence_id")
        == "EV-WALL-CIRCLE-LEMMA"
        and evidence.get(circle, {}).get("evidence_kind") == "INLINE_CANON"
        and evidence.get(circle, {}).get("location") == "inline"
        and evidence.get(circle, {}).get("sha256")
        == scope_sha256(index, circle)
        and evidence.get(circle, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(circle, {}).get("architecture_requirement") == "none"
        and circle_dependencies == {
            ("J-PROJECTIONS", "REQUIRES"),
            ("PI-FROM-J", "REQUIRES"),
        }
        and not circle_reverse_edges
        and not circle_quant_edges
        and scope_contains_all(
            index, circle,
            ("psi = -Arg(-zeta_N^a)",
             "midpoint 2a = N proved directly from z = 0",
             "Li_1(0) = Li_2(0) = 0",
             "full nontrivial-root sum",
             "N = 5 specialization reproduces WALL-LI2-RUNG",
             "no statement about substrate coupling",
             "physical observables", "or uniqueness"),
        )
        and has_status(index, wall, "T")
        and has_status(index, "QUANT-SUBSTRATE", "O")
    ))

    metro = "METRO-FINITE-STATE-RATIONALITY"
    metro_calculus = "METRO-REDUCTION-CALCULUS"
    metro_arrows = "METRO-REDUCTION-ARROWS"
    metro_child = "METRO-ADMISSIBILITY-DIM"
    metro_residual = "METRO-ADMISSIBILITY"
    metro_gate = "GATE-L5-L6-METRO-NORMALIZATION"
    metro_dependencies = {
        item: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == item
        }
        for item in (metro, metro_arrows, metro_calculus, metro_child, metro_residual)
    }
    metro_residual_edges = [
        row for row in dependencies
        if {row["item_id"], row["depends_on"]} == {metro, metro_residual}
    ]
    checks.append((
        "METRO",
        "finite-state theorem stays T; reduction arrows stay C; typed calculus, dimensional child, and residual stay O",
        has_status(index, metro, "T")
        and normative.get(metro, {}).get("item_type") == "THEOREM"
        and normative.get(metro, {}).get("status") == "T"
        and normative.get(metro, {}).get("layer") == "L5"
        and normative.get(metro, {}).get("gate_ids") == ""
        and index.get(metro, {}).get("evidence") == "inline"
        and evidence.get(metro, {}).get("evidence_id")
        == "EV-METRO-FINITE-STATE-RATIONALITY"
        and evidence.get(metro, {}).get("evidence_kind") == "INLINE_CANON"
        and evidence.get(metro, {}).get("location") == "inline"
        and evidence.get(metro, {}).get("sha256")
        == scope_sha256(index, metro)
        and evidence.get(metro, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(metro, {}).get("architecture_requirement") == "none"
        and metro_dependencies[metro] == set()
        and not metro_residual_edges
        and scope_contains_all(
            index, metro,
            ("accessible q-DFAO", "rational output vector",
             "every row sum of B is q", "converge entrywise to L 1",
             "then L is rational", "q-primary spectral projector",
             "conditional rationality of an existing common limit only",
             "no convergence existence criterion", "L5-to-L6 lift"),
        )
        and "row-sum mismatch is outside the declared q-dfao input schema"
        in index[metro]["falsifier"].lower()
        and has_status(index, metro_arrows, "C")
        and normative.get(metro_arrows, {}).get("item_type") == "COMPUTATION"
        and normative.get(metro_arrows, {}).get("status") == "C"
        and normative.get(metro_arrows, {}).get("layer") == "L5"
        and normative.get(metro_arrows, {}).get("gate_ids") == ""
        and index.get(metro_arrows, {}).get("evidence")
        == "probes/P-METRO-REDUCTION-ARROWS-4"
        and evidence.get(metro_arrows, {}).get("evidence_id")
        == "EV-METRO-REDUCTION-ARROWS"
        and evidence.get(metro_arrows, {}).get("evidence_kind")
        == "PUBLIC_PROBE"
        and evidence.get(metro_arrows, {}).get("location")
        == "probes/P-METRO-REDUCTION-ARROWS-4"
        and evidence.get(metro_arrows, {}).get("sha256")
        == "7864cb2ea6a6939cc477efa89f005fd71943091b446866decfa5a4db9036e8c6"
        and evidence.get(metro_arrows, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(metro_arrows, {}).get("architecture_requirement")
        == "one-architecture"
        and metro_dependencies[metro_arrows] == {
            ("DEF-ARCHITECTURE", "REQUIRES"),
        }
        and scope_contains_all(
            index, metro_arrows,
            ("typed L5 U_RF tuple",
             "four admitted reductions have exact preconditions and transports",
             "state relabeling by a bijection",
             "closure of A0 under every single-digit map",
             "multi-action Nerode quotient",
             "congruence for every coordinate i >= 2",
             "coordinate 1 automatic",
             "coordinate permutation transporting coordinate names",
             "tau_R = identity",
             "exact pointwise transported L5-stream equality",
             "zero congruence counterexamples",
             "exactly 1024 two-state and 4251528 three-state protocols",
             "computation-only L5 scope",
             "no forbidden-transformation catalogue",
             "common q^k blocking",
             "completeness of approx_red",
             "or L6, cross-layer, physical, or SI claim"),
        )
        and all(
            phrase.lower() in index[metro_arrows]["falsifier"].lower()
            for phrase in (
                "pinned evidence bundle or exact stdout differs",
                "17 frozen gates fails",
                "admitted arrow changes a transported pointwise L5 stream",
                "either exhaustive family yields a congruence counterexample",
                "obligation B", "common q^k blocking",
                "approx_red completeness", "every L6",
            )
        )
        and metro_arrows not in programs
        and has_status(index, metro_calculus, "O")
        and normative.get(metro_calculus, {}).get("item_type") == "OBLIGATION"
        and normative.get(metro_calculus, {}).get("status") == "O"
        and normative.get(metro_calculus, {}).get("layer") == "L5"
        and normative.get(metro_calculus, {}).get("gate_ids") == ""
        and evidence.get(metro_calculus, {}).get("evidence_id")
        == "EV-METRO-REDUCTION-CALCULUS"
        and evidence.get(metro_calculus, {}).get("evidence_kind")
        == "INLINE_CANON"
        and evidence.get(metro_calculus, {}).get("location") == "inline"
        and evidence.get(metro_calculus, {}).get("sha256")
        == scope_sha256(index, metro_calculus)
        and evidence.get(metro_calculus, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(metro_calculus, {}).get("architecture_requirement")
        == "none"
        and metro_dependencies[metro_calculus] == {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            (metro, "REQUIRES"),
            (metro_arrows, "REQUIRES"),
        }
        and scope_contains_all(
            index, metro_calculus,
            ("remaining open L5 reduction-calculus obligations",
             "after METRO-REDUCTION-ARROWS [C]",
             "obligation B",
             "complete forbidden-transformation catalogue",
             "obligation D", "common q^k blocking",
             "scientific decision", "terminal value",
             "obligation E",
             "completeness of the finite-zig-zag equivalence approx_red",
             "obligations A and C are separated",
             "do not close B, D, or E",
             "no normalization or cross-layer gate is owned"),
        )
        and all(
            phrase.lower() in index[metro_calculus]["falsifier"].lower()
            for phrase in (
                "every forbidden entry has an exact witness",
                "common q^k blocking",
                "decision and terminal-value transport",
                "approx_red is complete",
                "STOP while any forbidden-witness",
                "closes only obligations A and C",
                "leaves this row O and STOP",
            )
        )
        and programs.get(metro_calculus, {}).get("program_id") == "DECODER_CORE"
        and programs.get(metro_calculus, {}).get("queue_role") == "ROOT"
        and programs.get(metro_calculus, {}).get("work_state") == "STOP"
        and programs.get(metro_calculus, {}).get("work_mode") == "FORMAL"
        and has_status(index, metro_child, "O")
        and normative.get(metro_child, {}).get("item_type") == "OBLIGATION"
        and normative.get(metro_child, {}).get("status") == "O"
        and normative.get(metro_child, {}).get("layer") == "MULTI"
        and normative.get(metro_child, {}).get("gate_ids") == metro_gate
        and evidence.get(metro_child, {}).get("evidence_id")
        == "EV-METRO-ADMISSIBILITY-DIM"
        and evidence.get(metro_child, {}).get("evidence_kind")
        == "INLINE_CANON"
        and evidence.get(metro_child, {}).get("location") == "inline"
        and evidence.get(metro_child, {}).get("sha256")
        == scope_sha256(index, metro_child)
        and evidence.get(metro_child, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(metro_child, {}).get("architecture_requirement")
        == "none"
        and metro_dependencies[metro_child] == {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            (metro_calculus, "REQUIRES"),
            (metro, "REQUIRES"),
        }
        and scope_contains_all(
            index, metro_child,
            ("finite N^a-indexed commuting digit-word systems",
             "complete raw L5 stream", "total tagged L6 normalization Y_r",
             "uniform translated-box convergence with an effective modulus",
             "independently defined joint certificate",
             "sound, complete, and decision-coherent"),
        )
        and gates.get(metro_gate, {}).get("owner_item_id") == metro_child
        and gates.get(metro_gate, {}).get("gate_kind") == "OPEN_LIFT"
        and gates.get(metro_gate, {}).get("from_layer") == "L5"
        and gates.get(metro_gate, {}).get("to_layer") == "L6"
        and all(
            phrase.lower() in gates[metro_gate]["decision_condition"].lower()
            for phrase in (
                "complete raw L5 stream", "total tagged L6 normalization",
                "effective modulus", "independent joint certificate",
                "invariant under every allowed reduction",
            )
        )
        and programs.get(metro_child, {}).get("program_id") == "DECODER_CORE"
        and programs.get(metro_child, {}).get("queue_role") == "FOLLOWUP"
        and programs.get(metro_child, {}).get("work_state") == "STOP"
        and programs.get(metro_child, {}).get("work_mode") == "FORMAL"
        and has_status(index, metro_residual, "O")
        and normative.get(metro_residual, {}).get("item_type") == "OBLIGATION"
        and normative.get(metro_residual, {}).get("status") == "O"
        and normative.get(metro_residual, {}).get("layer")
        == "NOT_APPLICABLE"
        and normative.get(metro_residual, {}).get("gate_ids") == ""
        and evidence.get(metro_residual, {}).get("evidence_id")
        == "EV-METRO-ADMISSIBILITY"
        and evidence.get(metro_residual, {}).get("evidence_kind")
        == "INLINE_CANON"
        and evidence.get(metro_residual, {}).get("location") == "inline"
        and evidence.get(metro_residual, {}).get("sha256")
        == scope_sha256(index, metro_residual)
        and evidence.get(metro_residual, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(metro_residual, {}).get("architecture_requirement")
        == "none"
        and metro_dependencies[metro_residual] == {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            (metro_calculus, "REQUIRES"),
        }
        and scope_contains_all(
            index, metro_residual,
            ("exhaustive residual cover R1 through R8",
             "R1=U_RF minus the commuting higher-rank "
             "METRO-ADMISSIBILITY-DIM child",
             "rank-one", "noncommuting", "non-finite-state",
             "unbounded-memory adaptive", "non-reducible stochastic",
             "irrational", "out-of-child cross-layer", "physical-unit",
             "mixed-class protocols"),
        )
        and all(
            phrase.lower() in index[metro_residual]["falsifier"].lower()
            for phrase in (
                "STOP until R1 through R8 each has a typed child",
                "closes only when all eight children close",
            )
        )
        and programs.get(metro_residual, {}).get("program_id")
        == "DECODER_CORE"
        and programs.get(metro_residual, {}).get("queue_role") == "FOLLOWUP"
        and programs.get(metro_residual, {}).get("work_state") == "STOP"
        and programs.get(metro_residual, {}).get("work_mode") == "FORMAL"
        and metro not in programs
    ))

    entropy = "ENTROPY-CYLINDER-NOGO-CURSOR"
    entropy_cut = "ENTROPY-CYLINDER-CUT"
    entropy_bridge = "ENTROPY-LAYER-BRIDGE"
    entropy_gate = "GATE-L2-L5-ENTROPY-BRIDGE"
    entropy_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == entropy
    }
    entropy_bridge_edges = {
        (row["depends_on"], row["relation"])
        for row in dependencies
        if row["item_id"] == entropy_bridge
        and row["depends_on"] in {entropy, entropy_cut}
    }
    entropy_cut_edges = [
        row for row in dependencies
        if {row["item_id"], row["depends_on"]} == {entropy, entropy_cut}
    ]
    checks.append((
        "ENTROPY",
        "cursor cylinder no-go stays T; narrow cut stays F and Route A bridge stays O",
        has_status(index, entropy, "T")
        and normative.get(entropy, {}).get("item_type") == "THEOREM"
        and normative.get(entropy, {}).get("status") == "T"
        and normative.get(entropy, {}).get("layer") == "L5"
        and normative.get(entropy, {}).get("gate_ids") == ""
        and index.get(entropy, {}).get("evidence")
        == "probes/P-ENTROPY-CURSOR-CLOSURE-1"
        and evidence.get(entropy, {}).get("evidence_id")
        == "EV-ENTROPY-CYLINDER-NOGO-CURSOR"
        and evidence.get(entropy, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(entropy, {}).get("location")
        == "probes/P-ENTROPY-CURSOR-CLOSURE-1"
        and evidence.get(entropy, {}).get("sha256")
        == "422ca1708e351b067f31134965f70d150194c4a6041be0351c9c131b3086f370"
        and evidence.get(entropy, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(entropy, {}).get("architecture_requirement")
        == "two-architecture"
        and entropy_dependencies == {("DEF-ARCHITECTURE", "REQUIRES")}
        and not entropy_cut_edges
        and scope_contains_all(
            index, entropy,
            ("exact L5 finite-cylindrical constraint graph on F_5^6",
             "two-sided Thue-Morse factor language",
             "every pure-word system at every cursor c = 0..L-1",
             "every window L = 4..32", "global solution count zero",
             "labelled graph projects exactly to the pure-word graph",
             "zero residue is fixed by multiplication by J",
             "same obstruction holds at every finite lambda-depth",
             "27 direct checks", "audits, not the source",
             "no non-cylindrical cut", "P_5 construction",
             "measurable selection", "L6", "physical claim"),
        )
        and entropy not in programs
        and has_status(index, entropy_cut, "F")
        and normative.get(entropy_cut, {}).get("item_type") == "FALSIFIED"
        and normative.get(entropy_cut, {}).get("status") == "F"
        and normative.get(entropy_cut, {}).get("layer") == "L5"
        and evidence.get(entropy_cut, {}).get("evidence_kind")
        == "PUBLIC_PROBE"
        and evidence.get(entropy_cut, {}).get("sha256")
        == "950f20397d23f395730e408a2400804c8a8dded2ac1c5e515e86a2f96ebd5f29"
        and evidence.get(entropy_cut, {}).get("architecture_requirement")
        == "two-architecture"
        and scope_contains_all(
            index, entropy_cut,
            ("cursor c = 0 for L = 4..16",
             "(L,c) = (5,1), (6,1), (6,2)",
             "no other cursor or window is included"),
        )
        and has_status(index, entropy_bridge, "O")
        and normative.get(entropy_bridge, {}).get("item_type") == "OBLIGATION"
        and normative.get(entropy_bridge, {}).get("status") == "O"
        and normative.get(entropy_bridge, {}).get("layer") == "MULTI"
        and normative.get(entropy_bridge, {}).get("gate_ids") == entropy_gate
        and evidence.get(entropy_bridge, {}).get("evidence_id")
        == "EV-ENTROPY-LAYER-BRIDGE"
        and evidence.get(entropy_bridge, {}).get("evidence_kind")
        == "PUBLIC_PROBE"
        and evidence.get(entropy_bridge, {}).get("location")
        == "probes/P-ENTROPY-BRIDGE-1"
        and evidence.get(entropy_bridge, {}).get("sha256")
        == "96cca583006f7090d094fd4a025a78e6ee4f98fb7627af7c880f829beafccb57"
        and evidence.get(entropy_bridge, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(entropy_bridge, {}).get("architecture_requirement")
        == "two-architecture"
        and scope_contains_all(
            index, entropy_bridge,
            ("measurable total maps P_5", "mu-almost-everywhere",
             "exact equivariance", "exact pushforward Law_W",
             "equal cardinalities do not construct an element of A_A"),
        )
        and all(
            phrase.lower() in index[entropy_bridge]["falsifier"].lower()
            for phrase in (
                "any registered (L,c) with 4 <= L <= 32",
                "at any finite lambda-depth",
                "would refute ENTROPY-CYLINDER-NOGO-CURSOR",
                "rather than close this row",
                "inside the older ENTROPY-CYLINDER-CUT scope",
                "correction of that F row",
            )
        )
        and entropy_bridge_edges == {
            (entropy_cut, "REQUIRES"),
            (entropy, "BOUNDED_BY"),
        }
        and gates.get(entropy_gate, {}).get("owner_item_id") == entropy_bridge
        and gates.get(entropy_gate, {}).get("gate_kind") == "OPEN_LIFT"
        and gates.get(entropy_gate, {}).get("from_layer") == "L2"
        and gates.get(entropy_gate, {}).get("to_layer") == "L5"
        and all(
            phrase.lower() in gates[entropy_gate]["decision_condition"].lower()
            for phrase in (
                "A_A is proved nonempty by one exact map",
                "mu-almost-everywhere equivariance",
                "pushforward Law_W", "A_A=empty",
                "failure of one proposal is STOP",
            )
        )
        and programs.get(entropy_bridge, {}).get("program_id") == "MEASURE"
        and programs.get(entropy_bridge, {}).get("queue_role") == "ROOT"
        and programs.get(entropy_bridge, {}).get("work_state") == "STOP"
        and programs.get(entropy_bridge, {}).get("work_mode") == "FORMAL"
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
