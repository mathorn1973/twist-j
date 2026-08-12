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
CORE = ROOT / "canon" / "CORE.md"


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


INDEPENDENCE_ROWS = (
    "SPLIT-PRIME-RAPIDITY-INDEPENDENCE",
    "REDUCED-SPLIT-GENERATOR-HEIGHT",
)


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
    core_text = CORE.read_text(encoding="utf-8")
    checks = []

    counts = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    expected_counts = {"T": 133, "D": 41, "C": 27, "F": 13,
                       "O": 23, "H": 2}
    checks.append((
        "COUNTS",
        "registry has 239 claims with the current status partition",
        len(rows) == 239 and counts == expected_counts,
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
    retired_observer = "OBSERVER-WRITE-PORT"
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
        "exact drift and selector ranking stay T; retired observer no longer blocks derivation O",
        has_status(index, drift, "T")
        and has_status(index, coin_selector, "T")
        and has_status(index, coin_premise, "D")
        and has_status(index, coin_derivation, "O")
        and normative.get(drift, {}).get("item_type") == "THEOREM"
        and normative.get(drift, {}).get("layer") == "L5"
        and normative.get(drift, {}).get("gate_ids") == ""
        and normative.get(coin_selector, {}).get("item_type") == "THEOREM"
        and normative.get(coin_selector, {}).get("layer") == "MULTI"
        and normative.get(coin_selector, {}).get("gate_ids") == ""
        and normative.get(coin_premise, {}).get("item_type") == "DICTIONARY"
        and normative.get(coin_premise, {}).get("status") == "D"
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
        and coin_premise not in programs
        and programs.get(coin_derivation, {}).get("program_id") == "DECODER_CORE"
        and programs.get(coin_derivation, {}).get("queue_role") == "ROOT"
        and programs.get(coin_derivation, {}).get("work_state") == "STOP"
        and programs.get(coin_derivation, {}).get("work_mode") == "FORMAL"
        and retired_observer not in index
        and retired_observer not in normative
        and retired_observer not in evidence
        and retired_observer not in programs
        and all(
            retired_observer not in (row["item_id"], row["depends_on"])
            for row in dependencies
        )
        and all(
            row["owner_item_id"] != retired_observer
            for row in gates.values()
        ),
    ))

    checks.append((
        "FORCE",
        "the finite Weyl commutator stays T; force as curvature is D",
        has_status(index, "FORCE-WEYL-HOLONOMY", "T")
        and has_status(index, "FORCE-AS-CURVATURE", "D")
        and scope_lacks(index, "FORCE-WEYL-HOLONOMY",
                        ("force", "curvature", "gravity", "electromagnetism")),
    ))

    scheme = "SCHEME-DICTIONARY"
    scheme_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == scheme
    }
    checks.append((
        "SCHEME",
        "scheme dictionary stays O and is explicitly STOP before definition",
        has_status(index, scheme, "O")
        and normative.get(scheme, {}).get("item_type") == "OBLIGATION"
        and normative.get(scheme, {}).get("status") == "O"
        and normative.get(scheme, {}).get("layer") == "NOT_APPLICABLE"
        and normative.get(scheme, {}).get("gate_ids") == ""
        and evidence.get(scheme, {}).get("evidence_kind") == "INLINE_CANON"
        and evidence.get(scheme, {}).get("location") == "inline"
        and evidence.get(scheme, {}).get("sha256")
        == scope_sha256(index, scheme)
        and evidence.get(scheme, {}).get("architecture_requirement") == "none"
        and scheme_dependencies == {("DEF-ARCHITECTURE", "REQUIRES")}
        and all(
            phrase.lower() in index[scheme]["falsifier"].lower()
            for phrase in (
                "STOP until the exact source-seed domain",
                "named measurement scheme",
                "scale and threshold conventions",
                "total map with equality and window semantics",
                "source manifests",
                "complete acyclic dependency graph",
                "failure of one candidate is STOP",
                "exact dictionary at that frozen scope requiring no new free dimensionless parameter",
                "every admissible dictionary requires a new free dimensionless parameter",
            )
        )
        and programs.get(scheme, {}) == {
            "claim_id": scheme,
            "program_id": "DECODER_CORE",
            "queue_role": "ROOT",
            "work_state": "STOP",
            "work_mode": "FORMAL",
        }
        and all(row["owner_item_id"] != scheme for row in gates.values())
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

    central = "CENTRAL-LIFT-PHASE"
    central_path = "probes/P-CENTRAL-LIFT-PHASE-1"
    central_digest = (
        "ff0ffb98cbc3197d18a86a22dd3cabe853b5f50a80e099ede48b1ae6a7a258e0"
    )
    central_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == central
    }
    checks.append((
        "CENTRAL",
        "central Herm/Sym phase stays T at L4; cone, decoder, and physics stay outside",
        has_status(index, central, "T")
        and normative.get(central, {}).get("item_type") == "THEOREM"
        and normative.get(central, {}).get("status") == "T"
        and normative.get(central, {}).get("layer") == "L4"
        and normative.get(central, {}).get("gate_ids") == ""
        and index.get(central, {}).get("canon_section") == "4. The two places"
        and index.get(central, {}).get("evidence") == central_path
        and evidence.get(central, {}).get("evidence_id")
        == "EV-CENTRAL-LIFT-PHASE"
        and evidence.get(central, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(central, {}).get("location") == central_path
        and evidence.get(central, {}).get("sha256") == central_digest
        and evidence.get(central, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(central, {}).get("architecture_requirement")
        == "two-architecture"
        and central_dependencies == {
            ("J-PROJECTIONS", "REQUIRES"),
            ("J-TENTH-ROOT", "REQUIRES"),
            ("J-GOLDEN-BRIDGE", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
        }
        and scope_contains_all(
            index, central,
            ("fifth projective Herm power is a pure boost",
             "H_(cA) = H_A", "central Sym factor zeta_5^2",
             "image of O_K^x", "exactly mu_5",
             "mu_10 \\ mu_5", "L4 quadratic-support",
             "no Herm2 positive/Born/causal cone", "decoder Q or QCarrier",
             "MatterData", "L5 stream", "L6 measure", "cross-layer lift"),
        )
        and all(
            phrase.lower() in index[central]["falsifier"].lower()
            for phrase in (
                "unit-phase image differs from mu_5",
                "1-J lies in mu_5",
                "excluded physical, decoder, cone, carrier, or cross-layer",
                "integrity STOP, not a scientific falsifier",
            )
        )
        and has_status(index, "QUADRATIC-DECODER-DATA", "O")
        and programs.get("QUADRATIC-DECODER-DATA", {}).get("work_state")
        == "STOP"
        and central not in programs,
    ))

    quartic = "QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS"
    quartic_path = (
        "probes/P-QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS-1"
    )
    quartic_digest = (
        "05f6a5c1e29b5e962c357f323ec2104d39f771230ea5cb6953a6b25126bbe5ee"
    )
    quartic_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == quartic
    }
    checks.append((
        "QUARTIC",
        "quartic total ramification stays T at L1; no field selection or physical lift",
        has_status(index, quartic, "T")
        and normative.get(quartic, {}).get("item_type") == "THEOREM"
        and normative.get(quartic, {}).get("status") == "T"
        and normative.get(quartic, {}).get("layer") == "L1"
        and normative.get(quartic, {}).get("gate_ids") == ""
        and index.get(quartic, {}).get("canon_section") == "4. The two places"
        and index.get(quartic, {}).get("evidence") == quartic_path
        and evidence.get(quartic, {}).get("evidence_id")
        == "EV-QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS"
        and evidence.get(quartic, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(quartic, {}).get("location") == quartic_path
        and evidence.get(quartic, {}).get("sha256") == quartic_digest
        and evidence.get(quartic, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(quartic, {}).get("architecture_requirement")
        == "two-architecture"
        and quartic_dependencies == {
            ("C20-TEICHMULLER-SPLIT", "REQUIRES"),
            ("RAMIFIED-TM-LIFT", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
        }
        and scope_contains_all(
            index, quartic,
            ("phi(n)=4 exactly for n in {5,8,10,12}",
             "Q(zeta_10)=Q(zeta_5)",
             "total-ramification locus is exactly {(K_5,5),(K_8,2)}",
             "(e,f,g)=(2,2,1)", "F_5^x=C_4", "F_2^x=C_1",
             "F_4^x=C_3", "F_9^x=C_8", "J mod p_(5,5)=2",
             "L1 exact arithmetic only", "no selection of degree four",
             "TWO-PLACE-PHYSICS promotion", "lift to L2-L6"),
        )
        and all(
            phrase.lower() in index[quartic]["falsifier"].lower()
            for phrase in (
                "solution set of phi(n)=4 differs",
                "total-ramification locus differs",
                "J-reduction mismatch requires correction",
                "integrity STOP, not a scientific falsifier",
            )
        )
        and has_status(index, "TWO-PLACE-PHYSICS", "D")
        and quartic not in programs,
    ))

    abelian_cm = "ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM"
    abelian_cm_path = (
        "probes/P-ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM-1"
    )
    abelian_cm_digest = (
        "31a4d20d4cd73778a7c058435ccc9e8bb1b7fcdc5a5475a5181c1e3aa739e2e0"
    )
    abelian_cm_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == abelian_cm
    }
    checks.append((
        "ABELIAN-CM",
        "unique even-bit minimum stays T at L1; its class is not a physical selector",
        has_status(index, abelian_cm, "T")
        and normative.get(abelian_cm, {}).get("item_type") == "THEOREM"
        and normative.get(abelian_cm, {}).get("status") == "T"
        and normative.get(abelian_cm, {}).get("layer") == "L1"
        and normative.get(abelian_cm, {}).get("gate_ids") == ""
        and index.get(abelian_cm, {}).get("canon_section")
        == "4. The two places"
        and index.get(abelian_cm, {}).get("evidence") == abelian_cm_path
        and evidence.get(abelian_cm, {}).get("evidence_id")
        == "EV-ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM"
        and evidence.get(abelian_cm, {}).get("evidence_kind")
        == "PUBLIC_PROBE"
        and evidence.get(abelian_cm, {}).get("location") == abelian_cm_path
        and evidence.get(abelian_cm, {}).get("sha256") == abelian_cm_digest
        and evidence.get(abelian_cm, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(abelian_cm, {}).get("architecture_requirement")
        == "two-architecture"
        and abelian_cm_dependencies == {
            ("DEF-ACTION-LAYERS", "REQUIRES"),
        }
        and scope_contains_all(
            index, abelian_cm,
            ("Q(zeta_5) belongs to A",
             "|Hom(G_K,C_2)|=2 including the trivial character",
             "absDisc(K)>=125",
             "unique absolute-discriminant minimizer",
             "primitive character epsilon associated to the pointwise square psi^2",
             "pure 2-primary control (16,8) giving floor 2048",
             "no total-ramification premise",
             "no claim that A or discriminant minimization is selected",
             "TWO-PLACE-PHYSICS promotion", "lift to L2-L6"),
        )
        and all(
            phrase.lower() in index[abelian_cm]["falsifier"].lower()
            for phrase in (
                "field K in A has absDisc(K)<125",
                "not Q-isomorphic to Q(zeta_5) has absDisc(K)=125",
                "Q(zeta_5) fails an admissibility condition",
                "field conductor-discriminant identity",
                "integrity STOP, not a scientific falsifier",
            )
        )
        and "## Why five, twice" in core_text
        and "{(K_5,5),(K_8,2)}" in core_text
        and "unique absolute-discriminant" in core_text
        and "separate frozen classes, not a physical-selection chain"
        in core_text
        and has_status(index, "TWO-PLACE-PHYSICS", "D")
        and abelian_cm not in programs,
    ))

    cm_pencil = "CM-ALTERNATING-PENCIL"
    cm_pencil_path = "probes/P-CM-ALTERNATING-PENCIL-1"
    cm_pencil_digest = (
        "74e15b610ef60afab903b241ff550febd08ce6ca8a685f0b1be698e1528163ed"
    )
    cm_pencil_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == cm_pencil
    }
    checks.append((
        "CM-PENCIL",
        "alternating trace pencil stays T at L1; repaired similitude boundary stays exact",
        has_status(index, cm_pencil, "T")
        and normative.get(cm_pencil, {}).get("item_type") == "THEOREM"
        and normative.get(cm_pencil, {}).get("status") == "T"
        and normative.get(cm_pencil, {}).get("layer") == "L1"
        and normative.get(cm_pencil, {}).get("gate_ids") == ""
        and index.get(cm_pencil, {}).get("canon_section")
        == "4. The two places"
        and index.get(cm_pencil, {}).get("evidence") == cm_pencil_path
        and evidence.get(cm_pencil, {}).get("evidence_id")
        == "EV-CM-ALTERNATING-PENCIL"
        and evidence.get(cm_pencil, {}).get("evidence_kind")
        == "PUBLIC_PROBE"
        and evidence.get(cm_pencil, {}).get("location") == cm_pencil_path
        and evidence.get(cm_pencil, {}).get("sha256") == cm_pencil_digest
        and evidence.get(cm_pencil, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(cm_pencil, {}).get("architecture_requirement")
        == "two-architecture"
        and cm_pencil_dependencies == {
            ("J-GOLDEN-BRIDGE", "REQUIRES"),
            ("J-STEP", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
        }
        and scope_contains_all(
            index, cm_pencil,
            ("L = lambda_1 Z[phi]",
             "Omega_lam(x,y) = Tr(lam x conjugate(y))/5",
             "unimodular exactly when (lam) = (lambda_1)",
             "Pf(Omega_(a,b)) = a^2-a b-b^2",
             "Pell unit orbit",
             "action kernel is exactly {+zeta_5^k,-zeta_5^k : 0<=k<5}",
             "A_J=[[1,-1],[-1,2]]",
             "A_J is the inverse of its square",
             "unit multiplication has a scalar multiplier only at +1",
             "conjugation acts with multiplier -1",
             "L1 exact algebra only",
             "lift to L2-L6"),
        )
        and all(
            phrase.lower() in index[cm_pencil]["falsifier"].lower()
            for phrase in (
                "unimodular locus differs",
                "relative-norm kernel other than the ten roots of unity",
                "integral determinant-one scalar similitude has multiplier outside {+1,-1}",
                "unit other than a root of unity fixes Omega_1",
                "conjugation does not act by -1",
                "changed evidence bundle or architecture transcript",
                "integrity STOP",
            )
        )
        and cm_pencil not in programs,
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

    cm_pair = "COLOR-CM-2I-SEMILINEAR-PAIR"
    cm_path = "probes/P-CM-2I-QCARRIER-1"
    cm_digest = "2d480767d992215fe0c7328c8fb794484cd7c99c22d6b56f65b340c8b9d09bee"
    cm_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == cm_pair
    }
    checks.append((
        "CM-2I",
        "marked semilinear pair stays T at L4; decoder and measure stay O/STOP",
        has_status(index, cm_pair, "T")
        and normative.get(cm_pair, {}).get("item_type") == "THEOREM"
        and normative.get(cm_pair, {}).get("status") == "T"
        and normative.get(cm_pair, {}).get("layer") == "L4"
        and normative.get(cm_pair, {}).get("gate_ids") == ""
        and index.get(cm_pair, {}).get("canon_section") == "12. The color door"
        and index.get(cm_pair, {}).get("evidence") == cm_path
        and evidence.get(cm_pair, {}).get("evidence_id")
        == "EV-COLOR-CM-2I-SEMILINEAR-PAIR"
        and evidence.get(cm_pair, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(cm_pair, {}).get("location") == cm_path
        and evidence.get(cm_pair, {}).get("sha256") == cm_digest
        and evidence.get(cm_pair, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(cm_pair, {}).get("architecture_requirement")
        == "two-architecture"
        and cm_dependencies == {
            ("COLOR-INTEGRAL-LIFT", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
        }
        and scope_contains_all(
            index, cm_pair,
            ("marked twist-isomorphism stabilizer is exactly {1,sigma}",
             "Galois-stable K-isomorphism class through explicit intertwiners",
             "Hom_G(rho^tau,rho) = 0",
             "Hom_G(rho^sigma,rho) = K C0",
             "End_G(rho^tau) = K I2",
             "Hom_G(rho^sigma,rho^tau) = 0",
             "exhaustive antidiagonal form",
             "cocycle class [-1]", "order four is impossible",
             "eight is the smallest attainable finite order",
             "invariant sigma-Hermitian forms",
             "exactly the F-line F H0",
             "phi^2 forced by determinants and positivity",
             "no claim is made that the full space of invariant forms",
             "no Q-form or coherent C4 descent datum",
             "no uniqueness or selection of a marked lift",
             "decoder Q or QCarrier", "decoder Gram",
             "orbit-to-amplitude map", "MatterData",
             "physical U(1)", "L5-L6 measure lift"),
        )
        and all(
            phrase.lower() in index[cm_pair]["falsifier"].lower()
            for phrase in (
                "pair character is not Q-valued",
                "an explicit Galois pair intertwiner fails",
                "H0 is not totally positive definite",
                "balanced multiplier is not forced to phi^2",
            )
        )
        and has_status(index, "SPIN-LIFT-FORCED", "F")
        and has_status(index, "QUADRATIC-DECODER-DATA", "O")
        and has_status(index, "COLOR-MEASURE-SELECTION", "O")
        and programs.get("QUADRATIC-DECODER-DATA", {}).get("program_id")
        == "DECODER_CORE"
        and programs.get("QUADRATIC-DECODER-DATA", {}).get("queue_role")
        == "ROOT"
        and programs.get("QUADRATIC-DECODER-DATA", {}).get("work_state")
        == "STOP"
        and programs.get("QUADRATIC-DECODER-DATA", {}).get("work_mode")
        == "FORMAL"
        and programs.get("COLOR-MEASURE-SELECTION", {}).get("program_id")
        == "NONABELIAN_QCD"
        and programs.get("COLOR-MEASURE-SELECTION", {}).get("queue_role")
        == "ROOT"
        and programs.get("COLOR-MEASURE-SELECTION", {}).get("work_state")
        == "STOP"
        and programs.get("COLOR-MEASURE-SELECTION", {}).get("work_mode")
        == "FORMAL"
        and cm_pair not in programs,
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
    spectral = "TM-SYM2-SPECTRAL-COHERENCE"
    frozen_owner = "TM-SYM2-MEASURE"
    physical_owner = "TM-SYM2-PHYSICAL-MEASURE"
    selector_gate = "GATE-L1-L5-TM-SYM2-SELECTOR-STREAM"
    born_gate = "GATE-L5-L6-TM-SYM2-BORN-MEASURE"
    tm_theorems = (projective, semilinear, reversal, spectral)
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
        spectral: {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            (projective, "REQUIRES"),
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
            (spectral, "BOUNDED_BY"),
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
        spectral: (
            "probes/P-TM-SYM2-SPECTRAL-COHERENCE-1",
            "22662135d6e5e6a7cd6729690a98f6c2998bcedd24f8cd696feb5cc16d81e60c",
        ),
    }
    checks.append((
        "TM-SYM2",
        "four closed exact classifications stay T; fired selector and physical successor stay separated",
        all(has_status(index, item, "T") for item in tm_theorems)
        and normative.get(projective, {}).get("item_type") == "THEOREM"
        and normative.get(projective, {}).get("layer") == "MULTI"
        and normative.get(semilinear, {}).get("layer") == "L5"
        and normative.get(reversal, {}).get("layer") == "L5"
        and normative.get(spectral, {}).get("item_type") == "THEOREM"
        and normative.get(spectral, {}).get("layer") == "L5"
        and normative.get(spectral, {}).get("gate_ids") == ""
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
        and scope_contains_all(
            index, spectral,
            ("frozen v16 S_TM carrier", "48-selector class", "L5"),
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
        and spectral not in programs
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

    photon_child = "PHOTON-KAPPA-LEMMA"
    photon_parent = "PHOTON-WINDOW-PROOF"
    photon_path = "probes/P-PHOTON-KAPPA-LEMMA-1"
    photon_digest = (
        "b0f14e92c008fdd5fcdbc6f0960aac0e1b5b55bb85b1e05dd3945fa67b31f0d6"
    )
    photon_child_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == photon_child
    }
    photon_parent_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == photon_parent
    }
    roughening = "PHOTON-ROUGHENING-CERTIFICATE"
    checks.append((
        "PHOTON",
        "Kappa universal proposition and compound route are F; roughening stays unregistered",
        has_status(index, photon_child, "F")
        and normative.get(photon_child, {}).get("item_type") == "FALSIFIED"
        and normative.get(photon_child, {}).get("status") == "F"
        and normative.get(photon_child, {}).get("layer") == "L4"
        and normative.get(photon_child, {}).get("gate_ids") == ""
        and evidence.get(photon_child, {}).get("evidence_id")
        == "EV-PHOTON-KAPPA-LEMMA"
        and evidence.get(photon_child, {}).get("evidence_kind")
        == "PUBLIC_PROBE"
        and evidence.get(photon_child, {}).get("location") == photon_path
        and evidence.get(photon_child, {}).get("sha256") == photon_digest
        and evidence.get(photon_child, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(photon_child, {}).get("architecture_requirement")
        == "two-architecture"
        and photon_child_dependencies == {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            ("MONOPOLE-FIFTHS", "REQUIRES"),
        }
        and scope_contains_all(
            index, photon_child,
            ("positive proposition", "is false on the frozen L4 carrier",
             "no connectedness restriction", "partial n=5j",
             "F_occ(j_*)<=7993", "neither equality nor optimality",
             "no roughening", "no roughening, Froehlich-Spencer, Coulomb"),
        )
        and all(
            phrase.lower() in index[photon_child]["falsifier"].lower()
            for phrase in (
                "fired", "public two-architecture exact certificate",
                "2^7993<=7^3240", "no value of F_occ(j_*) is computed",
            )
        )
        and photon_child not in programs
        and has_status(index, photon_parent, "F")
        and normative.get(photon_parent, {}).get("item_type") == "FALSIFIED"
        and normative.get(photon_parent, {}).get("status") == "F"
        and evidence.get(photon_parent, {}).get("evidence_kind")
        == "PUBLIC_PROBE"
        and evidence.get(photon_parent, {}).get("location") == photon_path
        and evidence.get(photon_parent, {}).get("sha256") == photon_digest
        and evidence.get(photon_parent, {}).get("architecture_requirement")
        == "two-architecture"
        and photon_parent_dependencies == {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            (photon_child, "REQUIRES"),
        }
        and scope_contains_all(
            index, photon_parent,
            ("requires both (i)", "and (ii)",
             "electric-face roughening certificate"),
        )
        and photon_parent not in programs
        and roughening not in index
        and roughening not in normative
        and roughening not in programs
        and has_status(index, "KAPPA-SHAPES", "C")
        and has_status(index, "MONOPOLE-COST", "C")
    ))

    collapse = "LAMBDA-COCYCLE-BRANCH-COLLAPSE"
    grid = "LAMBDA-COCYCLE-GRID-EQUIVALENCE"
    angles = "LAMBDA-COCYCLE-ANGLES"
    collapse_path = "probes/P-LAMBDA-COCYCLE-ANGLES-1"
    grid_path = "probes/P-LAMBDA-COCYCLE-ANGLES-2"
    collapse_digest = (
        "6fa30375944a0c5ad2ed84705191552442dc1024b4248046a1382f5a0caf7710"
    )
    grid_digest = (
        "d721d7dea495f447f136a30fc310d99fee27b5fa3af7515c62fb662d120486f2"
    )
    lambda_dependencies = {
        (row["item_id"], row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] in {collapse, grid}
    }
    checks.append((
        "LAMBDA-COC",
        "both wall reductions stay T at L6; the cocycle hypothesis stays H and unfired",
        all(
            has_status(index, claim, "T")
            and normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("status") == "T"
            and normative.get(claim, {}).get("layer") == "L6"
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("canon_section")
            == "16. p = 5 and the wall"
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            for claim in (collapse, grid)
        )
        and index.get(collapse, {}).get("evidence") == collapse_path
        and evidence.get(collapse, {}).get("location") == collapse_path
        and evidence.get(collapse, {}).get("sha256") == collapse_digest
        and index.get(grid, {}).get("evidence") == grid_path
        and evidence.get(grid, {}).get("location") == grid_path
        and evidence.get(grid, {}).get("sha256") == grid_digest
        and lambda_dependencies == {
            (collapse, angles, "BOUNDED_BY"),
            (grid, collapse, "REQUIRES"),
        }
        and scope_contains_all(
            index, collapse,
            ("1 - 1/rho = e^(i alpha_gamma)",
             "0 <= M - t_n <= 2 M is necessary at every n",
             "no general finite-profile nonfalsifiability or realization theorem",
             "a finite ordinate window"),
        )
        and scope_contains_all(
            index, grid,
            ("y = 0 is the unique orbit of length 1",
             "exact positive level k",
             "ord_(lambda^(4m))(J) = 4 . 5^m for every m >= 1",
             "n_0 = 4 occurs at level 1",
             "dist(4 . 5^A x,Z) -> 0",
             "pure point spectrum with eigenvalue angle set exactly",
             "if and only if RH holds"),
        )
        and has_status(index, angles, "H")
        and normative.get(angles, {}).get("item_type") == "HYPOTHESIS"
        and normative.get(angles, {}).get("layer") == "L6"
        and programs.get(angles, {}) == {
            "claim_id": angles, "program_id": "ENRICHMENT",
            "queue_role": "ROOT", "work_state": "BLOCKED",
            "work_mode": "ENRICHMENT",
        }
        and evidence.get(angles, {}).get("sha256")
        == "811c41d0d1b1ec00fa1d114385c7915bd648dfea8c0e773ca41c292768156bdc"
        and scope_contains_all(
            index, angles,
            ("if and only if RH holds",
             "rho = 1/(1 - xi) with xi != 1",
             "n_A = 4 . 5^A",
             "no general finite-profile nonfalsifiability or realization theorem"),
        )
        and all(
            phrase.lower() in index[angles]["falsifier"].lower()
            for phrase in (
                "fires if rh is disproved",
                "for a critical-line zero that is exactly the exclusion",
                "exact finite violation",
                "finite satisfaction does not decide the row",
            )
        )
    ))

    seam = "J-HARMONIC-SEAM"
    seam_path = "probes/P-J-HARMONIC-SEAM-1"
    seam_digest = (
        "9054c62b919f5edb1b67ae9100d5ab733fd78a6b094662424a24a43a8bfe21cd"
    )
    seam_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == seam
    }
    checks.append((
        "J-SEAM",
        "harmonic seam stays T at L1; dictionary, places, decoder, and physics stay outside",
        has_status(index, seam, "T")
        and normative.get(seam, {}).get("item_type") == "THEOREM"
        and normative.get(seam, {}).get("status") == "T"
        and normative.get(seam, {}).get("layer") == "L1"
        and normative.get(seam, {}).get("gate_ids") == ""
        and index.get(seam, {}).get("canon_section")
        == "1. The axiom and the two projections"
        and index.get(seam, {}).get("evidence") == seam_path
        and evidence.get(seam, {}).get("evidence_id") == "EV-J-HARMONIC-SEAM"
        and evidence.get(seam, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(seam, {}).get("location") == seam_path
        and evidence.get(seam, {}).get("sha256") == seam_digest
        and evidence.get(seam, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(seam, {}).get("architecture_requirement")
        == "two-architecture"
        and seam_dependencies == {
            ("J-GOLDEN-BRIDGE", "REQUIRES"),
            ("J-TENTH-ROOT", "REQUIRES"),
        }
        and scope_contains_all(
            index, seam,
            ("u_n=-psi^n=-F_(n+1)-F_n zeta_5^2-F_n zeta_5^3",
             "H(x) is real iff x in {1,-1}",
             "Re H(x)=0 iff x in {-zeta_5,-zeta_5^-1}",
             "O_K^x=mu_10 x <phi>",
             "Log J=-H(1)-2H(-zeta_5)",
             "no promotion of AXIOM-PROJECTION-DICTIONARY or TWO-PLACE-PHYSICS",
             "no decoder, measure, observer, force, spacetime, SI bridge",
             "lift to L2-L6"),
        )
        and all(
            phrase.lower() in index[seam]["falsifier"].lower()
            for phrase in (
                "universal integral numerator identity",
                "complete mu_10 axis classification",
                "unit-group product",
                "principal-branch reconstruction of Log J",
                "integrity STOP",
            )
        )
        and has_status(index, "AXIOM-PROJECTION-DICTIONARY", "D")
        and has_status(index, "TWO-PLACE-PHYSICS", "D")
        and has_status(index, "BOOST-COUNT-LADDER", "D")
        and has_status(index, "LOG-AXES-INDEPENDENCE", "T")
        and has_status(index, "QUADRATIC-DECODER-DATA", "O")
        and seam not in programs,
    ))

    mobius = "MOBIUS-TM-PRIME2-BRIDGE"
    mobius_path = "probes/P-MOBIUS-TM-PRIME2-1"
    mobius_digest = (
        "94c8338bb78d2836c4bb707ce3dc13ed00b38f423645e17c78d6d3bc07cd501a"
    )
    mobius_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == mobius
    }
    checks.append((
        "MOBIUS-TM",
        "prime-2 bridge stays exact L1 arithmetic with no fermionizer or physical lift",
        has_status(index, mobius, "T")
        and normative.get(mobius, {}).get("item_type") == "THEOREM"
        and normative.get(mobius, {}).get("status") == "T"
        and normative.get(mobius, {}).get("layer") == "L1"
        and normative.get(mobius, {}).get("gate_ids") == ""
        and index.get(mobius, {}).get("canon_section")
        == "9. The photon and the electron"
        and index.get(mobius, {}).get("evidence") == mobius_path
        and evidence.get(mobius, {}).get("evidence_id")
        == "EV-MOBIUS-TM-PRIME2-BRIDGE"
        and evidence.get(mobius, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(mobius, {}).get("location") == mobius_path
        and evidence.get(mobius, {}).get("sha256") == mobius_digest
        and evidence.get(mobius, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(mobius, {}).get("architecture_requirement")
        == "two-architecture"
        and mobius_dependencies == set()
        and all(row["depends_on"] != mobius for row in dependencies)
        and scope_contains_all(
            index, mobius,
            ("D_p f=f on all positive integers iff",
             "c_TM(2n)=0 for every n>=1",
             "unique odd-supported arithmetic function",
             "with I the identity operator",
             "c_TM(n)=product_(p|n)(D_p-I)tau_TM(1)",
             "c_TM(15)=-2",
             "product_(j>=0)(1-x^(2^j))-1",
             "zeta_odd(s)C_TM(s)=T_TM,odd(s)",
             "tau=sqrt(J)",
             "mu(2x)=-mu(x) restricted to odd x",
             "no multiplicativity or Euler-product claim",
             "not equal to FERMIONIZER's Phi_f(s)=1-2^(1-s) at the same argument",
             "although it equals Phi_f(s+1)",
             "unused shift creating no dependency or physical identification",
             "no RH, zeta-zero, Nyman-Beurling, Baez-Duarte",
             "pointwise or averaged/Cesaro Moebius-Thue-Morse orthogonality",
             "Sarnak-type correlation",
             "asymptotic cancellation",
             "physical-vacuum",
             "L2-L6 conclusion"),
        )
        and all(
            phrase.lower() in index[mobius]["falsifier"].lower()
            for phrase in (
                "prime-dilation equivalence",
                "even-support annihilation",
                "odd-supported uniqueness or reconstruction",
                "odd-squarefree Boolean formula",
                "Lambert identity in |x|<1",
                "Dirichlet identities",
                "integrity STOP",
            )
        )
        and has_status(index, "FERMIONIZER", "T")
        and has_status(index, "TM-BREATH-TOWER", "T")
        and mobius not in programs
        and all(row["owner_item_id"] != mobius for row in gates.values()),
    ))

    carry_mul = "TM-MULTIPLICATION-CARRY-DEFECT"
    carry_mul_path = "probes/P-TM-MULTIPLICATION-CARRY-DEFECT-1"
    carry_mul_digest = (
        "348e359dd2c2566c7c142ac9f7217bec3dd4ab3e725584e89a477420354e50bf"
    )
    carry_mul_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == carry_mul
    }
    checks.append((
        "TM-MUL-CARRY",
        "multiplication carry defect stays standalone L1 arithmetic with no physical lift",
        has_status(index, carry_mul, "T")
        and normative.get(carry_mul, {}).get("item_type") == "THEOREM"
        and normative.get(carry_mul, {}).get("status") == "T"
        and normative.get(carry_mul, {}).get("layer") == "L1"
        and normative.get(carry_mul, {}).get("gate_ids") == ""
        and index.get(carry_mul, {}).get("canon_section")
        == "9. The photon and the electron"
        and index.get(carry_mul, {}).get("evidence") == carry_mul_path
        and evidence.get(carry_mul, {}).get("evidence_id")
        == "EV-TM-MULTIPLICATION-CARRY-DEFECT"
        and evidence.get(carry_mul, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(carry_mul, {}).get("location") == carry_mul_path
        and evidence.get(carry_mul, {}).get("sha256") == carry_mul_digest
        and evidence.get(carry_mul, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(carry_mul, {}).get("architecture_requirement")
        == "two-architecture"
        and carry_mul_dependencies == set()
        and all(row["depends_on"] != carry_mul for row in dependencies)
        and scope_contains_all(
            index, carry_mul,
            ("kappa_(2,mul)(a,b)=s_2(a)s_2(b)-s_2(ab)>=0",
             "normalization-order-independent count of unit moves",
             "R=(P AND Q) XOR K",
             "tau_TM(ab)tau_TM(a)tau_TM(b)=(-1)^((P OR Q) XOR K)",
             "takes the values -2,-4,0,-2,0,-2,0,2",
             "vanishes iff K=0 and (P OR Q)=1",
             "kappa_(2,mul)(3,11)=4 and c_TM(33)=0",
             "c_TM(p^2)=0 iff kappa_(2,mul)(p,p) is even",
             "Delta_mul(empty)=0",
             "c_TM(n)=sum_(S subseteq {1,...,m})",
             "finite-vector-space e_2 carry layer of CARRY-PENTAD",
             "chronological nu_2(n+1) carry cocycle of RAMIFIED-TM-LIFT",
             "semiprime table not asserting realization",
             "c_TM=0 not implying zero carries or trivial multiplication",
             "no multiplicativity claim for c_TM",
             "no dependence on MOBIUS-TM-PRIME2-BRIDGE as a theorem premise",
             "decoder, measure, Born, observer",
             "physical-vacuum, matter, light, entanglement, curvature",
             "L2-L6 conclusion"),
        )
        and all(
            phrase.lower() in index[carry_mul]["falsifier"].lower()
            for phrase in (
                "raw-column recurrence",
                "carry-mass identity",
                "unit-normalization-order independence",
                "lexicographic semiprime table entry",
                "prime-square identity",
                "odd-squarefree carry-parity-cube formula",
                "integrity STOP",
            )
        )
        and carry_mul not in programs
        and all(
            row["owner_item_id"] != carry_mul for row in gates.values()
        ),
    ))

    hankel_path = "probes/P-TM-HANKEL-K3-TRANSFER-1"
    hankel_digest = (
        "364f459aee2910edc27e3fa7c85e692f0a8f93cf7c17e7bc0771daa334b53592"
    )
    hankel_rows = {
        "TM-HANKEL-DIVISOR-BRIDGE": ("T", "THEOREM"),
        "TM-HANKEL-SQUAREFUL-RANK-NOGO": ("T", "THEOREM"),
        "TM-HANKEL-EXTREMAL-WITT-SKELETON": ("T", "THEOREM"),
        "TM-HANKEL-K2-TRANSFER": ("T", "THEOREM"),
        "TM-HANKEL-K3-UNIVERSAL-TRANSFER": ("F", "FALSIFIED"),
        "TM-HANKEL-K3-TWO-SCALAR-CLASSIFICATION": ("C", "COMPUTATION"),
        "TM-HANKEL-K3-QUADRATIC-INVARIANT-SUFFICIENCY": ("C", "COMPUTATION"),
    }
    checks.append((
        "TM-HANKEL",
        "Hankel divisor block splits T, F, and C exactly; no physical lift",
        all(
            has_status(index, claim, status)
            and normative.get(claim, {}).get("item_type") == item_type
            and normative.get(claim, {}).get("status") == status
            and normative.get(claim, {}).get("layer") == "L1"
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("canon_section")
            == "9. The photon and the electron"
            and index.get(claim, {}).get("evidence") == hankel_path
            and evidence.get(claim, {}).get("evidence_id") == "EV-" + claim
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("location") == hankel_path
            and evidence.get(claim, {}).get("sha256") == hankel_digest
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and all(row["item_id"] != claim for row in dependencies)
            and all(row["depends_on"] != claim for row in dependencies)
            and claim not in programs
            and all(
                row["owner_item_id"] != claim for row in gates.values()
            )
            for claim, (status, item_type) in hankel_rows.items()
        )
        and scope_contains_all(
            index, "TM-HANKEL-K2-TRANSFER",
            ("h(s)=-9+s(3D+3E+F)-s^2(A+D)^2/(3+sA)-s^2(B+E)^2/(3+sB)"
             "<=-9+7s<=-2<0",
             "NEG 2 ZERO 0 POS 2",
             "universal at k=2"),
        )
        and scope_contains_all(
            index, "TM-HANKEL-K3-UNIVERSAL-TRANSFER",
            ("147965=5.101.293",
             "NEG 5 ZERO 0 POS 3",
             "determinant -3840",
             "157 extremal triples with n<=200000",
             "unique nonbalanced case"),
        )
        and index["TM-HANKEL-K3-UNIVERSAL-TRANSFER"]["falsifier"]
        .startswith("fired:")
        and scope_contains_all(
            index, "TM-HANKEL-K3-TWO-SCALAR-CLASSIFICATION",
            ("32398/110/260",
             "518368/1760/4160",
             "522462 tables",
             "FAIL iff det G_6<0 and det K<=0",
             "computation grade"),
        )
        and scope_contains_all(
            index, "TM-HANKEL-K3-QUADRATIC-INVARIANT-SUFFICIENCY",
            ("3584 buckets of which exactly 58 are mixed",
             "88352 buckets with zero mixed",
             "factors through the quadratic invariant map",
             "(2^19+3.2^12+2.2^7)/6=89472",
             "merging 1120 orbit distinctions",
             "no claim is made that the deciding function is itself a "
             "polynomial of degree two"),
        ),
    ))

    rapidity_path = "probes/P-ARITH-RAPIDITY-1"
    rapidity_digest = (
        "e053d4950e368c7815f6df723b4dde316c6bb5a17d4f8d62f8fcee8eeb105fda"
    )
    rapidity_rows = {
        "ARITHMETIC-RAPIDITY-DECOMPOSITION": ("T", "THEOREM"),
        "SPLIT-PRIME-RAPIDITY-CLASS": ("T", "THEOREM"),
        "SPLIT-PRIME-RAPIDITY-CONSTRUCTION-AGREEMENT": ("C", "COMPUTATION"),
    }
    checks.append((
        "RAPIDITY",
        "arithmetic rapidity rows split T and C exactly; no physical lift",
        all(
            has_status(index, claim, status)
            and normative.get(claim, {}).get("item_type") == item_type
            and normative.get(claim, {}).get("status") == status
            and normative.get(claim, {}).get("layer") == "L1"
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("canon_section")
            == "10. Relativity as counting"
            and index.get(claim, {}).get("evidence") == rapidity_path
            and evidence.get(claim, {}).get("evidence_id") == "EV-" + claim
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("location") == rapidity_path
            and evidence.get(claim, {}).get("sha256") == rapidity_digest
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and all(row["item_id"] != claim for row in dependencies)
            and all(
                row["item_id"] in INDEPENDENCE_ROWS
                for row in dependencies
                if row["depends_on"] == claim
            )
            and claim not in programs
            and all(
                row["owner_item_id"] != claim for row in gates.values()
            )
            for claim, (status, item_type) in rapidity_rows.items()
        )
        and scope_contains_all(
            index, "ARITHMETIC-RAPIDITY-DECOMPOSITION",
            ("t^2-s^2=N(x)",
             "null locus is empty",
             "dense, not discrete",
             "Lucas always the time reading",
             "with no conflict"),
        )
        and scope_contains_all(
            index, "SPLIT-PRIME-RAPIDITY-CLASS",
            ("R(p)={r,-r}",
             "|Tr(w)|=L_(2m)",
             "class zero exactly",
             "not merely 0 modulo the lattice"),
        )
        and scope_contains_all(
            index, "SPLIT-PRIME-RAPIDITY-CONSTRUCTION-AGREEMENT",
            ("all 146 of them",
             "R1(p)=R2(p) in every case",
             "70 pairs agreeing oriented and 76 only after conjugation",
             "computation grade"),
        ),
    ))

    independence_path = "probes/P-SPLIT-PRIME-INDEPENDENCE-1"
    independence_digest = (
        "8c293da2f9b3af5d96e20fea472be19676d18328350bb2c0800ed68de2e7ffbf"
    )
    independence_rows = {
        "SPLIT-PRIME-RAPIDITY-INDEPENDENCE": ("T", "THEOREM"),
        "REDUCED-SPLIT-GENERATOR-HEIGHT": ("T", "THEOREM"),
    }
    checks.append((
        "INDEPENDENCE",
        "split-prime independence rows stay exact L1 arithmetic with no "
        "analytic or ordering lift",
        all(
            has_status(index, claim, status)
            and normative.get(claim, {}).get("item_type") == item_type
            and normative.get(claim, {}).get("status") == status
            and normative.get(claim, {}).get("layer") == "L1"
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("canon_section")
            == "10. Relativity as counting"
            and index.get(claim, {}).get("evidence") == independence_path
            and evidence.get(claim, {}).get("evidence_id") == "EV-" + claim
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("location") == independence_path
            and evidence.get(claim, {}).get("sha256") == independence_digest
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            and all(
                row["owner_item_id"] != claim for row in gates.values()
            )
            for claim, (status, item_type) in independence_rows.items()
        )
        and scope_contains_all(
            index, "SPLIT-PRIME-RAPIDITY-INDEPENDENCE",
            ("forces every m_i=0",
             "unique factorisation of fractional ideals",
             "the statement is orientation-free",
             "NOT about the distribution of primes as p grows"),
        )
        and scope_contains_all(
            index, "REDUCED-SPLIT-GENERATOR-HEIGHT",
            ("open fundamental half-period",
             "both real embeddings exceed one",
             "h(pi) = (1/2) log p",
             "the height is unbounded at fixed class"),
        ),
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
