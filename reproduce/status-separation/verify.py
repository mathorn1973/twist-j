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
HISTORY = ROOT / "canon" / "HISTORY.tsv"
GATES = ROOT / "canon" / "GATES.tsv"
FRONTIER_PROGRAMS = ROOT / "canon" / "FRONTIER_PROGRAMS.tsv"
CORE = ROOT / "canon" / "CORE.md"
REPRODUCE = ROOT / "reproduce"


def load_table(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_rows():
    rows = load_table(REGISTRY)
    normative_rows = load_table(NORMATIVE)
    dependencies = load_table(DEPENDENCIES)
    evidence_rows = load_table(EVIDENCE)
    history_rows = load_table(HISTORY)
    gate_rows = load_table(GATES)
    program_rows = load_table(FRONTIER_PROGRAMS)
    return (
        rows,
        {row["claim_id"]: row for row in rows},
        {row["item_id"]: row for row in normative_rows},
        dependencies,
        {row["claim_id"]: row for row in evidence_rows},
        history_rows,
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
    "SPLIT-PRIME-RAPIDITY-QUANTITATIVE-SEPARATION",
    "SPLIT-RAPIDITY-FEJER-GRAM-BOUND",
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
        history,
        gates,
        programs,
    ) = load_rows()
    core_text = CORE.read_text(encoding="utf-8")
    checks = []

    counts = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    two_architecture = sum(
        row["architecture_requirement"] == "two-architecture"
        for row in evidence.values()
    )
    expected_counts = {"T": 174, "D": 43, "C": 32, "F": 16,
                       "O": 24, "H": 3}
    checks.append((
        "COUNTS",
        "registry and companion-ledger counts match Public Canon v57",
        len(rows) == 292
        and counts == expected_counts
        and len(normative) == 337
        and len(dependencies) == 502
        and len(evidence) == 292
        and two_architecture == 210
        and len(history) == 811
        and len(gates) == 10
        and len(programs) == 27
        and len({row["program_id"] for row in programs.values()}) == 7
        and sum(path.is_dir() for path in REPRODUCE.iterdir()) == 23,
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
    orientation_source = "DEF-TM-SYM2-ORIENTATION-SOURCE"
    monomial_lift = "DEF-TM-SYM2-MONOMIAL-VERB-LIFT"
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
        orientation_source: {
            (projective, "REQUIRES"),
            (semilinear, "REQUIRES"),
            (reversal, "REQUIRES"),
        },
        monomial_lift: {
            ("J-UNIT", "REQUIRES"),
            ("J-GOLDEN-BRIDGE", "REQUIRES"),
        },
        physical_owner: {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            ("GOLDEN-SIX-LINE-SYM2-FRAME", "REQUIRES"),
            (projective, "REQUIRES"),
            (orientation_source, "REQUIRES"),
            (monomial_lift, "REQUIRES"),
            ("MEASURE-BORN-VERB", "REQUIRES"),
            ("ABELIAN-FACE-DICTIONARY", "REQUIRES"),
            (frozen_owner, "BOUNDED_BY"),
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
        "four exact classifications stay T; fired selector stays F; physical successor closes only at D",
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
        and has_status(index, physical_owner, "D")
        and normative.get(physical_owner, {}).get("item_type") == "DICTIONARY"
        and normative.get(physical_owner, {}).get("layer") == "MULTI"
        and normative.get(physical_owner, {}).get("gate_ids") == born_gate
        and normative.get(orientation_source, {}).get("item_type") == "DEFINITION"
        and normative.get(orientation_source, {}).get("layer") == "L5"
        and normative.get(monomial_lift, {}).get("item_type") == "DEFINITION"
        and normative.get(monomial_lift, {}).get("layer") == "L5"
        and index.get(physical_owner, {}).get("evidence") == "probes/P-TM-SYM2-BORN-HALVING-1"
        and evidence.get(physical_owner, {}).get("evidence_id") == "EV-TM-SYM2-PHYSICAL-MEASURE"
        and evidence.get(physical_owner, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(physical_owner, {}).get("location") == "probes/P-TM-SYM2-BORN-HALVING-1"
        and evidence.get(physical_owner, {}).get("sha256") == "acc598e670eb7e57f689a6ecc970438ce7211d1a097514a78847100e8871fa59"
        and evidence.get(physical_owner, {}).get("hash_mode") == "bundle-manifest-sha256-v1"
        and evidence.get(physical_owner, {}).get("architecture_requirement") == "two-architecture"
        and scope_contains_all(
            index, physical_owner,
            ("owner-approved typed L5-to-L6 physical dictionary bridge",
             "C_sel = Sel_class/G with four classes",
             "epsilon_read = chi_Q chi_F", "omega(a,b,c) = c-a",
             "separately frozen monomial verb-lift class",
             "same normalized two-sheet law for every t",
             "six equal line weights 1/6 only as an output",
             "no selector representative is chosen",
             "no postcomposition gauge is enlarged",
             "same-modulus nonmonomial lift has unequal coefficient Born weights",
             "no uniqueness among all amplitude lifts",
             "GYRON identification"),
        )
        and gates.get(selector_gate, {}).get("owner_item_id") == frozen_owner
        and gates.get(selector_gate, {}).get("gate_kind") == "FIRED_NEGATIVE"
        and gates.get(selector_gate, {}).get("from_layer") == "L1"
        and gates.get(selector_gate, {}).get("to_layer") == "L5"
        and "four free projective-linear gauge orbits of size 12"
        in gates.get(selector_gate, {}).get("decision_condition", "")
        and gates.get(born_gate, {}).get("owner_item_id") == physical_owner
        and gates.get(born_gate, {}).get("gate_kind") == "DICTIONARY_LIFT"
        and gates.get(born_gate, {}).get("from_layer") == "L5"
        and gates.get(born_gate, {}).get("to_layer") == "L6"
        and "complete orientation-retaining L5 source"
        in gates.get(born_gate, {}).get("decision_condition", "")
        and frozen_owner not in programs
        and spectral not in programs
        and physical_owner not in programs
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

    separation = "SPLIT-PRIME-RAPIDITY-QUANTITATIVE-SEPARATION"
    fejer = "SPLIT-RAPIDITY-FEJER-GRAM-BOUND"
    separation_path = "probes/P-SPLIT-RAPIDITY-QUANTITATIVE-SEPARATION-1"
    separation_digest = (
        "ea59451558e513f16ee471b3bf9ccddfa0bc6e1cabbed70d27809cedfeb25ecb"
    )
    separation_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == separation
    }
    fejer_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == fejer
    }
    checks.append((
        "SEPARATION",
        "quantitative separation and finite Fejer rows stay exact, distinct, and normalization-fenced",
        all(
            has_status(index, claim, "T")
            and normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("status") == "T"
            and normative.get(claim, {}).get("layer") == "L1"
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("canon_section")
            == "10. Relativity as counting"
            and index.get(claim, {}).get("evidence") == separation_path
            and evidence.get(claim, {}).get("evidence_id") == "EV-" + claim
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("location") == separation_path
            and evidence.get(claim, {}).get("sha256") == separation_digest
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            and all(row["owner_item_id"] != claim for row in gates.values())
            for claim in (separation, fejer)
        )
        and evidence[separation]["sha256"] == evidence[fejer]["sha256"]
        and separation_dependencies == {
            ("ARITHMETIC-RAPIDITY-DECOMPOSITION", "REQUIRES"),
            ("SPLIT-PRIME-RAPIDITY-CLASS", "REQUIRES"),
            ("SPLIT-PRIME-RAPIDITY-INDEPENDENCE", "REQUIRES"),
            ("REDUCED-SPLIT-GENERATOR-HEIGHT", "REQUIRES"),
        }
        and fejer_dependencies == {(separation, "REQUIRES")}
        and scope_contains_all(
            index, separation,
            ("finite nonzero integer vector c=(c_p)",
             "signed norm +p",
             "|D_c| in sqrt5 Z_{>0} for even n",
             "|D_c| in Z_{>0} for odd n",
             "d_L=0.0011737895036417",
             "d_2L=0.4800380355559618",
             "valid determinant may be negative",
             "selects no global orientation or parity sheet",
             "minimizing signed channel is unique up to simultaneous conjugation"),
        )
        and all(
            phrase.lower() in index[separation]["falsifier"].lower()
            for phrase in (
                "|D_c| in sqrt5 Z_{>0} for even n",
                "|D_c| in Z_{>0} for odd n",
                "negative D_c",
                "-182sqrt5",
            )
        )
        and scope_contains_all(
            index, fejer,
            ("finite set A of distinct oriented split prime-power addresses",
             "delta_A>=asinh(1/(2X))",
             "character chi_h(a)",
             "ordinary signed-channel rungs are |b|=22 and |b|=182",
             "doubled-phase falsifier is the effective vector (2,2)",
             "phi^-3 x^2",
             "trace 29",
             "numerator 841",
             "correct P(c)^2 budget",
             "no Hecke"),
        )
        and all(
            phrase.lower() in index[fejer]["falsifier"].lower()
            for phrase in (
                "two distinct declared finite addresses collide",
                "operator-norm bound",
                "singleton Gram matrix differs from [1]",
                "normalization STOP",
            )
        ),
    ))

    qdd_path = "reproduce/qdd-route-a"
    checks.append((
        "QDD-ROUTE-A",
        "the QDD Route A algebra is three L1 theorems on two-architecture evidence; the apparatus is a separate O; QUADRATIC-DECODER-DATA stays O with its ROOT/STOP program row; no gate and no L6 row exist",
        all(
            has_status(index, claim, "T")
            and normative.get(claim, {}).get("layer") == "L1"
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("evidence") == qdd_path
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            for claim in ("QDD-ALGEBRAIC-FACTORIZATION", "QDD-PROJECTOR-PAIR-TR4",
                          "QDD-QCARRIER-DIAGONAL-BOUNDARY")
        )
        and has_status(index, "QDD-INSTRUMENT-APPARATUS", "O")
        and programs.get("QDD-INSTRUMENT-APPARATUS", {}).get("program_id")
        == "DECODER_CORE"
        and programs.get("QDD-INSTRUMENT-APPARATUS", {}).get("queue_role")
        == "FOLLOWUP"
        and programs.get("QDD-INSTRUMENT-APPARATUS", {}).get("work_state")
        == "STOP"
        and has_status(index, "QUADRATIC-DECODER-DATA", "O")
        and programs.get("QUADRATIC-DECODER-DATA", {}).get("queue_role")
        == "ROOT"
        and programs.get("QUADRATIC-DECODER-DATA", {}).get("work_state")
        == "STOP"
        and "QDD-BORN-READOUT-MEASURE" not in index
        and "DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION" not in normative
        and "GATE-L1-L6-QDD-BORN-READOUT" not in gates
        and normative.get("DEF-QDD-PROJECTOR-LOW", {}).get("item_type")
        == "DEFINITION"
        and scope_lacks(index, "QDD-ALGEBRAIC-FACTORIZATION",
                        ("apparatus", "occurrence"))
        and scope_contains_all(index, "QDD-ALGEBRAIC-FACTORIZATION",
                               ("no completion-contract field is filled",))
        and scope_contains_all(index, "QDD-PROJECTOR-PAIR-TR4",
                               ("no uniqueness-from-j",))
        and scope_contains_all(index, "QDD-QCARRIER-DIAGONAL-BOUNDARY",
                               ("a_dagger = a_t = v v^t",
                                "no physical central phase"))
        and scope_contains_all(index, "QDD-INSTRUMENT-APPARATUS",
                               ("filling no field of the decoder completion contract",)),
    ))

    nonselection = "QDD-INSTRUMENT-NONSELECTION"
    nonselection_path = "probes/P-QDD-INSTRUMENT-NONSELECTION-1"
    nonselection_digest = (
        "d49930ce735413cb58601d85d697b6dc049e5571f50cdf16d837206db26727e2"
    )
    nonselection_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == nonselection
    }
    apparatus_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == "QDD-INSTRUMENT-APPARATUS"
    }
    checks.append((
        "QDD-NONSELECTION",
        "the L4 theorem fixes rational fibre, post-state and dilation nonselection while the apparatus remains O on exactly independent selection and realized-event sampling",
        has_status(index, nonselection, "T")
        and normative.get(nonselection, {}).get("item_type") == "THEOREM"
        and normative.get(nonselection, {}).get("status") == "T"
        and normative.get(nonselection, {}).get("layer") == "L4"
        and normative.get(nonselection, {}).get("gate_ids") == ""
        and index.get(nonselection, {}).get("evidence") == nonselection_path
        and evidence.get(nonselection, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(nonselection, {}).get("location") == nonselection_path
        and evidence.get(nonselection, {}).get("sha256") == nonselection_digest
        and evidence.get(nonselection, {}).get("architecture_requirement")
        == "two-architecture"
        and nonselection not in programs
        and all(row["owner_item_id"] != nonselection for row in gates.values())
        and nonselection_dependencies == set()
        and apparatus_dependencies == {
            ("DEF-QDD-PROJECTOR-LOW", "REQUIRES"),
            ("DEF-QDD-PROJECTOR-HIGH", "REQUIRES"),
            ("DEF-QDD-GRAM", "REQUIRES"),
        }
        and scope_contains_all(
            index, nonselection,
            ("one branchwise O(G,Q) x O(G,Q) orbit",
             "injects Q into physically distinct post-state instrument classes",
             "not an instrument-selection principle",
             "mathematical positive-square-root section",
             "no L5 realized-event stream",
             "no L6 measure",
             "SAMPLING NOT PROVIDED rather than SAMPLING IMPOSSIBLE"),
        )
        and scope_contains_all(
            index, "QDD-INSTRUMENT-APPARATUS",
            ("only two independent blockers remain",
             "O2 independent physical instrument selection",
             "O1 realized event generation / sampling",
             "target-controlled coupling is circular",
             "SAMPLING NOT PROVIDED",
             "SAMPLING IMPOSSIBLE is not claimed"),
        )
        and has_status(index, "QDD-INSTRUMENT-APPARATUS", "O")
        and has_status(index, "QUADRATIC-DECODER-DATA", "O"),
    ))

    suzuki = "SUZUKI-LOCAL-CAPACITY-NOGO"
    suzuki_path = "probes/P-SUZUKI-LOCAL-CAPACITY-NOGO-1"
    suzuki_digest = (
        "0891418a788e7e2d1d4795af8883020dbcd78c7ea2f9f9fefb41b055131deb65"
    )
    suzuki_window = "SUZUKI-PRIME-FREE-WINDOW"
    suzuki_count = "SUZUKI-EVENT-COUNT"
    suzuki_rows = (suzuki, suzuki_window, suzuki_count)
    suzuki_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] in suzuki_rows
    }
    checks.append((
        "SUZUKI-CAPACITY-NOGO",
        "the L1 no-go complex for the Suzuki completion capacity enters at T with two finite C computations, all pinned to the two-architecture public probe bundle and free of dependency, gate and frontier ownership",
        has_status(index, suzuki, "T")
        and has_status(index, suzuki_window, "C")
        and has_status(index, suzuki_count, "C")
        and normative.get(suzuki, {}).get("item_type") == "THEOREM"
        and normative.get(suzuki, {}).get("status") == "T"
        and normative.get(suzuki, {}).get("layer") == "L1"
        and normative.get(suzuki, {}).get("gate_ids") == ""
        and normative.get(suzuki_window, {}).get("item_type") == "COMPUTATION"
        and normative.get(suzuki_count, {}).get("item_type") == "COMPUTATION"
        and all(index.get(row, {}).get("evidence") == suzuki_path for row in suzuki_rows)
        and all(evidence.get(row, {}).get("evidence_kind") == "PUBLIC_PROBE" for row in suzuki_rows)
        and all(evidence.get(row, {}).get("location") == suzuki_path for row in suzuki_rows)
        and all(evidence.get(row, {}).get("sha256") == suzuki_digest for row in suzuki_rows)
        and all(
            evidence.get(row, {}).get("architecture_requirement") == "two-architecture"
            for row in suzuki_rows
        )
        and all(row not in programs for row in suzuki_rows)
        and all(row["owner_item_id"] not in suzuki_rows for row in gates.values())
        and suzuki_dependencies == set()
        and scope_contains_all(
            index, suzuki,
            ("orthogonal increments",
             "the nonnegative ramp class is empty",
             "at the first event q = 2",
             "separately indefinite",
             "the norm is exactly one",
             "nonlocal in t",
             "no J-coupling, no L2--L6 lift"),
        )
        and scope_contains_all(
            index, suzuki_window,
            ("[1/128, 45/64]", "zero undecided leaves"),
        )
        and scope_contains_all(
            index, suzuki_count,
            ("78734", "two independent counting paths"),
        ),
    ))

    tt_moment = "TT-VECTOR-MOMENT-UNDERDETERMINATION"
    tt_moment_path = "probes/P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1"
    tt_moment_digest = (
        "302e0403e5b1a0027555a39c33dddbe55e17b6ec76ee9292da8407630d5b10bf"
    )
    tt_moment_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == tt_moment
    }
    checks.append((
        "TT-MOMENT",
        "the exact L1 moment family proves fourth-order underdetermination while state normalization remains O and no numerical tensor ratio is produced",
        has_status(index, tt_moment, "T")
        and normative.get(tt_moment, {}).get("item_type") == "THEOREM"
        and normative.get(tt_moment, {}).get("layer") == "L1"
        and normative.get(tt_moment, {}).get("gate_ids") == ""
        and evidence.get(tt_moment, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(tt_moment, {}).get("location") == tt_moment_path
        and evidence.get(tt_moment, {}).get("sha256") == tt_moment_digest
        and evidence.get(tt_moment, {}).get("architecture_requirement")
        == "two-architecture"
        and tt_moment_dependencies == {
            ("TT-SQUARING-DECODER", "BOUNDED_BY"),
            ("POL-READ", "BOUNDED_BY"),
            ("TT-VECTOR-STATE-NORMALIZATION", "BOUNDED_BY"),
        }
        and scope_contains_all(
            index, tt_moment,
            ("every polynomial functional of total degree at most three",
             "minimal separating degree is exactly four",
             "no gaussian or wick closure exists at fixed modulus",
             "no normalization", "r_t(k)", "l2-l6 lift"),
        )
        and has_status(index, "TT-VECTOR-STATE-NORMALIZATION", "O")
        and scope_contains_all(
            index, "TT-VECTOR-STATE-NORMALIZATION",
            ("fourth-moment data", "explicit non-gaussian closure rule",
             "neither that choice nor a numerical r_t(k)"),
        )
        and evidence["TT-VECTOR-STATE-NORMALIZATION"]["sha256"]
        == scope_sha256(index, "TT-VECTOR-STATE-NORMALIZATION")
        and tt_moment not in programs
        and all(row["owner_item_id"] != tt_moment for row in gates.values()),
    ))

    qdd_u_channel = "QDD-U-INDUCED-CHANNEL"
    qdd_u_finite = "QDD-U-INDUCED-FINITE-NONSELECTION"
    qdd_u_path = "probes/P-QDD-INSTRUMENT-U-INDUCED-1"
    qdd_u_digest = (
        "17f5e001c9fce5360b021781fbb3910ed5045a5e9666ab7624a90e7880eae60f"
    )
    qdd_u_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in (qdd_u_channel, qdd_u_finite)
    }
    checks.append((
        "QDD-U",
        "the registered update supplies an exact L1 channel and a complete finite multi-layer nonselection computation while apparatus selection and sampling remain O and STOP",
        has_status(index, qdd_u_channel, "T")
        and has_status(index, qdd_u_finite, "C")
        and normative.get(qdd_u_channel, {}).get("item_type") == "THEOREM"
        and normative.get(qdd_u_channel, {}).get("layer") == "L1"
        and normative.get(qdd_u_finite, {}).get("item_type") == "COMPUTATION"
        and normative.get(qdd_u_finite, {}).get("layer") == "MULTI"
        and all(
            evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("location") == qdd_u_path
            and evidence.get(claim, {}).get("sha256") == qdd_u_digest
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            for claim in (qdd_u_channel, qdd_u_finite)
        )
        and qdd_u_dependencies[qdd_u_channel] == {
            ("DEF-AUTONOMOUS-STATE", "REQUIRES"),
            ("DEF-QDD-BALANCED-PISTON", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        }
        and qdd_u_dependencies[qdd_u_finite] == {
            (qdd_u_channel, "REQUIRES"),
            ("DEF-QDD-BRANCH-WEIGHT-PAIRING", "REQUIRES"),
            ("DEF-QDD-MATTER-RECORD", "REQUIRES"),
            ("QDD-INSTRUMENT-NONSELECTION", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        }
        and scope_contains_all(
            index, qdd_u_channel,
            ("five generator fibers are exactly", "delay one",
             "exact bidirectional algebraic channel structure only",
             "no physical measurement"),
        )
        and scope_contains_all(
            index, qdd_u_finite,
            ("180 two-cell maps", "900 record-delay pairs",
             "info is true for exactly 150", "functional=0",
             "post-undefined-or-zero=900", "evaluated/member/outside=0/0/0",
             "multi-layer scope", "no limit", "sampling impossibility"),
        )
        and scope_contains_all(
            index, "QDD-INSTRUMENT-APPARATUS",
            ("qdd-u-induced-channel", "frozen 900 record-delay pairs",
             "does not exclude another admissible apparatus class"),
        )
        and evidence["QDD-INSTRUMENT-APPARATUS"]["sha256"]
        == scope_sha256(index, "QDD-INSTRUMENT-APPARATUS")
        and has_status(index, "QDD-INSTRUMENT-APPARATUS", "O")
        and programs.get("QDD-INSTRUMENT-APPARATUS", {}).get("work_state")
        == "STOP",
    ))

    field_cut = "FIELD-ZERO-NONZERO-MULTIPLICATIVE-CUT"
    field_cut_path = "probes/P-FIELD-ZERO-NONZERO-CUT-1"
    field_cut_digest = (
        "baf65d43b2016d629f1442dea3e20191631e5b0f2729e8020eb6d36e9fe3384c"
    )
    checks.append((
        "FIELD-CUT",
        "the unique total multiplicative field bit is exactly the two oriented zero/nonzero cuts and remains independent of QDD and fifth-prime selection",
        has_status(index, field_cut, "T")
        and normative.get(field_cut, {}).get("item_type") == "THEOREM"
        and normative.get(field_cut, {}).get("layer") == "L1"
        and evidence.get(field_cut, {}).get("location") == field_cut_path
        and evidence.get(field_cut, {}).get("sha256") == field_cut_digest
        and evidence.get(field_cut, {}).get("architecture_requirement")
        == "two-architecture"
        and all(row["item_id"] != field_cut for row in dependencies)
        and scope_contains_all(
            index, field_cut,
            ("for every field f", "a={0} with b=or",
             "a=f^x with b=and", "b is unique",
             "qr/xnor and nqr/xor", "no five-specific selection",
             "no qdd equation", "dependency edge"),
        )
        and field_cut not in programs
        and all(row["owner_item_id"] != field_cut for row in gates.values()),
    ))

    tensor_path = "probes/P-QPAIR-SYM2-TENSOR-DEFECT-1"
    tensor_digest = (
        "ae345af394adf1693b5515d038743dc3f3697fa0c55340972eb979682538fed5"
    )
    tensor_rows = (
        "QPAIR-PRODUCT-COMPOSITION",
        "QPAIR-CROSS-SECTOR-NONDESCENT",
        "QPAIR-SYM2-TENSOR-DEFECT",
    )
    checks.append((
        "QPAIR-TENSOR",
        "matched quadratic sectors compose on product vectors, cross sectors fail factor-gauge descent, and the symmetric target has the exact determinant 9+1 defect",
        all(
            has_status(index, claim, "T")
            and normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("layer") == "L1"
            and evidence.get(claim, {}).get("location") == tensor_path
            and evidence.get(claim, {}).get("sha256") == tensor_digest
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and all(row["item_id"] != claim for row in dependencies)
            and claim not in programs
            for claim in tensor_rows
        )
        and scope_contains_all(
            index, tensor_rows[0],
            ("natural, associative, symmetric and unital",
             "exact for product vectors", "no surjectivity"),
        )
        and scope_contains_all(
            index, tensor_rows[1],
            ("c(lambda)/lambda", "lambda/c(lambda)",
             "zeta_5^3 and zeta_5^2", "no fifth-prime physical"),
        )
        and scope_contains_all(
            index, tensor_rows[2],
            ("10=9+1", "product squares span exactly",
             "((ad-bc)/2)kappa", "not a bell state",
             "not a claim that a full hermitian-plus-symmetric defect"),
        )
        and all(row["owner_item_id"] not in tensor_rows for row in gates.values()),
    ))

    qpair_path = "probes/P-QPAIR-C4-2I-MINIMALITY-1"
    qpair_digest = (
        "6f1d5a5859a193cb68eb53f6ed58f5da21b25f3c0084c3875eede690317ea592"
    )
    qpair_t = (
        "QPAIR-HERM-INTEGER-NONDESCENT",
        "QPAIR-TRANSPOSE-FIBER-REDUNDANCY",
        "QPAIR-TYPED-MIXED-C4-CLOSURE",
        "QPAIR-SYM2-2I-IRREDUCIBLE",
        "QPAIR-MINIMAL-2I-CLOSURE-OF-HERM-UNDER-MIXED-C4",
    )
    qpair_f = (
        "QPAIR-2I-ONLY-PAIR-FORCING",
        "QPAIR-MIXED-C4-NORMALIZES-2I",
    )
    qpair_definitions = {
        "DEF-QPAIR-SPIN-CARRIER",
        "DEF-QPAIR-HERM-SLOT",
        "DEF-QPAIR-SYM-SLOT",
        "DEF-QPAIR-MIXED-C4",
        "DEF-QPAIR-ADMISSIBLE-LINEAR-CLASS",
    }
    qpair_dependency_map = {
        item: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == item
        }
        for item in qpair_definitions | set(qpair_t) | set(qpair_f)
    }
    checks.append((
        "QPAIR-C4-2I",
        "the independent integral carrier has exact mixed closure and relative 2I minimality while set redundancy, 2I-only pair forcing, and normalization firewalls remain explicit",
        all(has_status(index, claim, "T") for claim in qpair_t)
        and all(has_status(index, claim, "F") for claim in qpair_f)
        and all(
            normative.get(item, {}).get("item_type") == "DEFINITION"
            and normative.get(item, {}).get("layer") == "L1"
            for item in qpair_definitions
        )
        and all(
            evidence.get(claim, {}).get("location") == qpair_path
            and evidence.get(claim, {}).get("sha256") == qpair_digest
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and normative.get(claim, {}).get("layer") == "L1"
            for claim in qpair_t + qpair_f
        )
        and qpair_dependency_map["QPAIR-SYM2-2I-IRREDUCIBLE"] == {
            ("COLOR-CORE-2I", "REQUIRES"),
            ("COLOR-GOLDEN-TABLE", "REQUIRES"),
            ("COLOR-INTEGRAL-LIFT", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
        }
        and qpair_dependency_map[
            "QPAIR-MINIMAL-2I-CLOSURE-OF-HERM-UNDER-MIXED-C4"
        ] == {
            ("QPAIR-SYM2-2I-IRREDUCIBLE", "REQUIRES"),
            ("DEF-QPAIR-SPIN-CARRIER", "REQUIRES"),
            ("DEF-QPAIR-HERM-SLOT", "REQUIRES"),
            ("DEF-QPAIR-SYM-SLOT", "REQUIRES"),
            ("DEF-QPAIR-MIXED-C4", "REQUIRES"),
            ("DEF-QPAIR-ADMISSIBLE-LINEAR-CLASS", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
        }
        and all(
            qpair_dependency_map[claim] == set()
            for claim in qpair_t[:3] + qpair_f
        )
        and qpair_dependency_map["DEF-QPAIR-SPIN-CARRIER"] == set()
        and qpair_dependency_map["DEF-QPAIR-HERM-SLOT"]
        == {("DEF-QPAIR-SPIN-CARRIER", "REQUIRES")}
        and qpair_dependency_map["DEF-QPAIR-SYM-SLOT"]
        == {("DEF-QPAIR-SPIN-CARRIER", "REQUIRES")}
        and qpair_dependency_map["DEF-QPAIR-MIXED-C4"]
        == {("DEF-QPAIR-SPIN-CARRIER", "REQUIRES")}
        and qpair_dependency_map["DEF-QPAIR-ADMISSIBLE-LINEAR-CLASS"] == {
            ("DEF-QPAIR-HERM-SLOT", "REQUIRES"),
            ("DEF-QPAIR-SYM-SLOT", "REQUIRES"),
            ("DEF-QPAIR-MIXED-C4", "REQUIRES"),
            ("COLOR-INTEGRAL-LIFT", "REQUIRES"),
        }
        and scope_contains_all(
            index, qpair_t[0],
            ("independent carrier", "no total set map",
             "field fiber is k^1 v", "fixed nonzero content layer",
             "full lattice can have wider fibers"),
        )
        and scope_contains_all(
            index, qpair_t[1],
            ("s(v)=s(w) iff w=+-v", "set-theoretic redundancy only",
             "no informational defense of two slots"),
        )
        and scope_contains_all(
            index, qpair_t[4],
            ("frozen class a_rel", "absolute determinant 64",
             "relative minimality", "not minimality of slot count"),
        )
        and scope_contains_all(
            index, qpair_f[0],
            ("universal proposition", "single symmetric slot"),
        )
        and "disproving the universal pair-forcing proposition"
        in index[qpair_f[0]]["falsifier"].lower()
        and scope_contains_all(
            index, qpair_f[1],
            ("not complex-linear or k-linear",),
        )
        and "disproving normalization"
        in index[qpair_f[1]]["falsifier"].lower()
        and all(claim not in programs for claim in qpair_t + qpair_f),
    ))


    qpair_area_rows = (
        "QPAIR-DET-AREA-SLOT-COMPARISON",
        "QPAIR-DET-AREA-PLACE-PAIR",
    )
    qpair_area_path = "probes/P-QPAIR-RELATIONAL-AREA-1"
    qpair_area_digest = (
        "5c02838a8d0bfe822fd30d703b6b0dad71cc459cbede3b9347ed8dfccd25a47f"
    )
    qpair_area_definitions = {
        "DEF-QPAIR-TYPED-PARTIAL-TRACE",
        "DEF-QPAIR-DET-AREA",
    }
    checks.append((
        "QPAIR-AREA",
        "typed determinant slots and the two cyclotomic places stay exact L1 algebra with no physical lift",
        all(
            has_status(index, claim, "T")
            and normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("layer") == "L1"
            and evidence.get(claim, {}).get("location") == qpair_area_path
            and evidence.get(claim, {}).get("sha256") == qpair_area_digest
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            and all(row["item_id"] != claim for row in dependencies)
            for claim in qpair_area_rows
        )
        and all(
            normative.get(item, {}).get("item_type") == "DEFINITION"
            and normative.get(item, {}).get("layer") == "L1"
            for item in qpair_area_definitions
        )
        and scope_contains_all(
            index, qpair_area_rows[0],
            ("4n(d/2)=det rho_v", "beta_b+4a=1",
             "no necessity", "physical-qubit"),
        )
        and scope_contains_all(
            index, qpair_area_rows[1],
            ("every nonzero x in o_k^4", "f_5^x/{+-1}",
             "[0,1/4]", "conservative common scope o_k^4",
             "fresh lock for any field-wide promotion", "no qubit"),
        )
        and all(row["owner_item_id"] not in qpair_area_rows
                for row in gates.values()),
    ))

    piston_rows = (
        "PISTON-2X2-RESHAPE-WEDGE",
        "QDD-TR4-OCCURRENCE-WEIGHT-WEDGE-BLIND",
        "PISTON-WEDGE-LIFT-CENSUS",
    )
    piston_path = "probes/P-PISTON-RELATIONAL-WEDGE-1"
    piston_digest = (
        "680d4ea3a134d3523f67260b64d21720f4ed5777b36c055b9d23ae3f4c00d2b8"
    )
    piston_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in piston_rows
    }
    checks.append((
        "PISTON-WEDGE",
        "the rational piston reshape, occurrence-weight boundary, and lift census stay exact and decoder-fenced",
        all(
            has_status(index, claim, "T")
            and normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("layer") == "L1"
            and evidence.get(claim, {}).get("location") == piston_path
            and evidence.get(claim, {}).get("sha256") == piston_digest
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            for claim in piston_rows
        )
        and all(
            normative.get(item, {}).get("item_type") == "DEFINITION"
            and normative.get(item, {}).get("layer") == "L1"
            for item in ("DEF-PISTON-2X2-RESHAPE", "DEF-PISTON-WEDGE")
        )
        and piston_dependencies[piston_rows[0]] == {
            ("KERNEL-WEDGE-AFFINITY", "REQUIRES"),
            ("DEF-QDD-BALANCED-PISTON", "REQUIRES"),
            ("DEF-QDD-QPAIR", "REQUIRES"),
            ("DEF-QDD-TRANSPOSE", "REQUIRES"),
            ("QPAIR-SYM2-TENSOR-DEFECT", "REQUIRES"),
        }
        and piston_dependencies[piston_rows[1]] == {
            ("QDD-PROJECTOR-PAIR-TR4", "REQUIRES"),
            ("QDD-ALGEBRAIC-FACTORIZATION", "REQUIRES"),
            (piston_rows[0], "REQUIRES"),
        }
        and piston_dependencies[piston_rows[2]]
        == {(piston_rows[0], "REQUIRES")}
        and scope_contains_all(
            index, piston_rows[0],
            ("exactly 8 of 24", "d_z/2", "exactly 145",
             "no carrier bridge"),
        )
        and scope_contains_all(
            index, piston_rows[1],
            ("same (m,w_low,w_high)", "full registered quadratic record is not wedge-blind",
             "no claim about what a decoder should read"),
        )
        and scope_contains_all(
            index, piston_rows[2],
            ("145", "129+16", "exactly 48", "no concurrence"),
        )
        and all(row["owner_item_id"] not in piston_rows
                for row in gates.values()),
    ))

    pure_rows = (
        "PURE-QUBIT-RELATIONAL-AREA",
        "PURE-QUBIT-LOCAL-RELATION-PYTHAGORAS",
        "PURE-QUBIT-RELATIONAL-CHSH",
        "PURE-QUBIT-RELATIONAL-READING",
    )
    pure_path = "probes/P-PURE-QUBIT-RELATIONAL-GEOMETRY-2"
    pure_digest = (
        "bcfc2d7c1552fb4b42e64f4bca7a3025415893152129aea67a45585f6d15320e"
    )
    pure_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in pure_rows
    }
    checks.append((
        "PURE-QUBIT",
        "conditional pure-two-qubit area, Pythagoras, CHSH, and reading stay on the external standard-QM scope",
        all(has_status(index, claim, "T") for claim in pure_rows[:3])
        and has_status(index, pure_rows[3], "D")
        and all(
            normative.get(claim, {}).get("layer") == "L1"
            and evidence.get(claim, {}).get("location") == pure_path
            and evidence.get(claim, {}).get("sha256") == pure_digest
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            and all(row["owner_item_id"] != claim for row in gates.values())
            for claim in pure_rows
        )
        and all(normative.get(claim, {}).get("item_type") == "THEOREM"
                for claim in pure_rows[:3])
        and normative.get(pure_rows[3], {}).get("item_type") == "DICTIONARY"
        and pure_dependencies[pure_rows[0]]
        == {("QPAIR-SYM2-TENSOR-DEFECT", "REQUIRES")}
        and pure_dependencies[pure_rows[1]]
        == {(pure_rows[0], "REQUIRES")}
        and pure_dependencies[pure_rows[2]] == {
            (pure_rows[0], "REQUIRES"),
            ("BELL-CAUSAL-ACCOUNTING", "BOUNDED_BY"),
        }
        and pure_dependencies[pure_rows[3]]
        == {(pure_rows[0], "REQUIRES")}
        and scope_contains_all(
            index, pure_rows[0],
            ("externally supplying", "||kappa||^2=4",
             "(1/2)||u wedge v||_tensor^2", "including a possible zero",
             "determinant phase", "external standard-qm"),
        )
        and scope_contains_all(
            index, pure_rows[1],
            ("|b_vec|^2+c^2=1", "not a mixed-state conservation law",
             "werner p=1/2"),
        )
        and scope_contains_all(
            index, pure_rows[2],
            ("maximum absolute expectation", "optimized model value",
             "no-signalling test", "causal account"),
        )
        and scope_contains_all(
            index, pure_rows[3],
            ("only after externally supplying", "not a third particle",
             "no map from the integral qpair carrier", "l6 measure"),
        ),
    ))

    bell = "BELL-CAUSAL-ACCOUNTING"
    bell_incoming = {
        (row["item_id"], row["relation"])
        for row in dependencies if row["depends_on"] == bell
    }
    bell_outgoing = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == bell
    }
    checks.append((
        "BELL-CAUSAL",
        "the Bell row remains an inline O/STOP accounting barrier with no experiment or causal conclusion",
        has_status(index, bell, "O")
        and normative.get(bell, {}).get("item_type") == "OBLIGATION"
        and normative.get(bell, {}).get("status") == "O"
        and normative.get(bell, {}).get("layer") == "MULTI"
        and normative.get(bell, {}).get("gate_ids") == ""
        and index.get(bell, {}).get("canon_section") == "18. The frontier"
        and index.get(bell, {}).get("evidence") == "inline"
        and evidence.get(bell, {}).get("evidence_kind") == "INLINE_CANON"
        and evidence.get(bell, {}).get("location") == "inline"
        and evidence.get(bell, {}).get("sha256") == scope_sha256(index, bell)
        and evidence.get(bell, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(bell, {}).get("architecture_requirement") == "none"
        and programs.get(bell, {}).get("program_id") == "QUANTUM_EM"
        and programs.get(bell, {}).get("queue_role") == "ROOT"
        and programs.get(bell, {}).get("work_state") == "STOP"
        and programs.get(bell, {}).get("work_mode") == "FORMAL"
        and bell_outgoing == set()
        and bell_incoming == {
            ("BELL-MAGIC-BOUNDARY", "BOUNDED_BY"),
            ("PURE-QUBIT-RELATIONAL-CHSH", "BOUNDED_BY"),
            ("DQRC-INTEGER-CENSUS-ARITHMETIC", "BOUNDED_BY"),
            ("DQRC-HORODECKI-REENCODING", "BOUNDED_BY"),
            ("DQRC-H-COEFFICIENT-NONSELECTION", "BOUNDED_BY"),
            ("DQRC-ORIGIN-NONSELECTION", "BOUNDED_BY"),
            ("DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY", "BOUNDED_BY"),
        }
        and all(row["owner_item_id"] != bell for row in gates.values())
        and scope_contains_all(
            index, bell,
            ("source state or variable lambda", "setting-selection mechanism",
             "normalized kernel p(a,b|x,y,lambda)", "bell-local factorization",
             "measurement independence", "no-signalling marginal equalities",
             "controllable-superluminal-signalling test",
             "l1-to-l4, l4-to-l5, and l5-to-l6",
             "complete dimensional audit", "failure of factorization alone",
             "no latent-variable", "selected in advance"),
        )
        and "partial accounts and failed individual candidates remain stop"
        in index[bell]["falsifier"].lower(),
    ))

    dqrc_rows = (
        "DQRC-INTEGER-CENSUS-ARITHMETIC",
        "DQRC-HORODECKI-REENCODING",
        "DQRC-H-COEFFICIENT-NONSELECTION",
        "DQRC-ORIGIN-NONSELECTION",
        "DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY",
    )
    dqrc_definition = "DEF-DQRC-INTEGER-CENSUS"
    dqrc_path = "probes/P-DQRC-ARITHMETIC-RECONSTRUCTION-1"
    dqrc_digest = (
        "25af7d719a244e4d877cf364736f9f9d0c4d0d45ff07a3611f7ff39b1679ee4b"
    )
    dqrc_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in dqrc_rows
    }
    checks.append((
        "DQRC",
        "the deterministic integer census and four boundary theorems stay exact L1 results while coefficient, origin, apparatus, event, measure, Bell, and physical readings remain unselected",
        {claim for claim in index if claim.startswith("DQRC-")}
        == set(dqrc_rows)
        and all(has_status(index, claim, "T") for claim in dqrc_rows)
        and dqrc_definition not in index
        and normative.get(dqrc_definition, {}).get("item_type") == "DEFINITION"
        and normative.get(dqrc_definition, {}).get("claim_id") == ""
        and normative.get(dqrc_definition, {}).get("status") == ""
        and normative.get(dqrc_definition, {}).get("layer") == "L1"
        and all(
            normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("status") == "T"
            and normative.get(claim, {}).get("layer") == "L1"
            and normative.get(claim, {}).get("gate_ids") == ""
            and evidence.get(claim, {}).get("location") == dqrc_path
            and evidence.get(claim, {}).get("sha256") == dqrc_digest
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            and all(row["owner_item_id"] != claim for row in gates.values())
            for claim in dqrc_rows
        )
        and dqrc_dependencies[dqrc_rows[0]] == {
            (dqrc_definition, "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            ("BELL-CAUSAL-ACCOUNTING", "BOUNDED_BY"),
        }
        and dqrc_dependencies[dqrc_rows[1]] == {
            (dqrc_rows[0], "REQUIRES"),
            ("PURE-QUBIT-RELATIONAL-CHSH", "REQUIRES"),
            ("BELL-CAUSAL-ACCOUNTING", "BOUNDED_BY"),
        }
        and dqrc_dependencies[dqrc_rows[2]] == {
            (dqrc_rows[0], "REQUIRES"),
            (dqrc_rows[1], "REQUIRES"),
            ("BELL-CAUSAL-ACCOUNTING", "BOUNDED_BY"),
        }
        and dqrc_dependencies[dqrc_rows[3]] == {
            (dqrc_rows[0], "REQUIRES"),
            ("BELL-CAUSAL-ACCOUNTING", "BOUNDED_BY"),
        }
        and dqrc_dependencies[dqrc_rows[4]] == {
            (dqrc_rows[0], "REQUIRES"),
            ("DEGREES-BY-PRIME", "REQUIRES"),
            ("BELL-CAUSAL-ACCOUNTING", "BOUNDED_BY"),
        }
        and scope_contains_all(
            index, dqrc_rows[0],
            ("exact integral l1 carrier", "margin exactly 2k",
             "inserted t involution", "parity solely from sigma_xy",
             "no realized setting", "no-signalling"),
        )
        and scope_contains_all(
            index, dqrc_rows[1],
            ("externally supplying", "exactly reencodes",
             "local singular-value rotations", "not an intrinsic derivation"),
        )
        and scope_contains_all(
            index, dqrc_rows[2],
            ("every integer beta>=0", "if and only if beta=4",
             "do not select 4", "no claim excludes a richer"),
        )
        and scope_contains_all(
            index, dqrc_rows[3],
            ("s_1^[0]=0", "s_1^[1]=4", "not origin invariant",
             "not an intrinsic physical prediction"),
        )
        and scope_contains_all(
            index, dqrc_rows[4],
            ("proper subfield of q(zeta_40)", "integer substitution",
             "not an integer limiting frequency", "no physical place"),
        )
        and has_status(index, "BELL-CAUSAL-ACCOUNTING", "O")
        and has_status(index, "QDD-INSTRUMENT-APPARATUS", "O")
        and has_status(index, "QUADRATIC-DECODER-DATA", "O")
        and has_status(index, "BELL-MAGIC-BOUNDARY", "T")
        and has_status(index, "PURE-QUBIT-RELATIONAL-CHSH", "T")
        and has_status(index, "TWO-PLACE-PHYSICS", "D")
        and has_status(index, "SILVER-RING-FACTS", "C")
        and has_status(index, "SILVER-SIBLING", "D")
        and "P-DQRC-FINITE-DEFICIT-1" not in normative
        and "P-DQRC-FINITE-DEFICIT-1" not in programs
        and all(row["owner_item_id"] != "P-DQRC-FINITE-DEFICIT-1"
                for row in gates.values()),
    ))

    de_w_edges = {
        (row["item_id"], row["depends_on"], row["relation"])
        for row in dependencies
        if "DE-W-CONSTANT" in (row["item_id"], row["depends_on"])
    }
    checks.append((
        "DE-W-CONSTANT",
        "the armed dark-energy reading enters at H on the completed public probe with exactly its three declared edges, while the register dictionary and the conformal-weight obligation keep their statuses and no gate, layer lift, or selection premise is created",
        has_status(index, "DE-W-CONSTANT", "H")
        and index["DE-W-CONSTANT"]["evidence"] == "probes/P-DE-W-ARMING-1"
        and index["DE-W-CONSTANT"]["canon_section"] == "18. The frontier"
        and evidence["DE-W-CONSTANT"]["evidence_kind"] == "PUBLIC_PROBE"
        and evidence["DE-W-CONSTANT"]["architecture_requirement"]
        == "two-architecture"
        and normative["DE-W-CONSTANT"]["layer"] == "NOT_APPLICABLE"
        and normative["DE-W-CONSTANT"]["gate_ids"] == ""
        and tuple(programs["DE-W-CONSTANT"][field] for field in
                  ("program_id", "queue_role", "work_state", "work_mode"))
        == ("COSMOLOGY", "FOLLOWUP", "BLOCKED", "EMPIRICAL")
        and de_w_edges == {
            ("COSMOLOGY-REGISTER", "DE-W-CONSTANT", "BOUNDED_BY"),
            ("DE-CONFORMAL-WEIGHT", "DE-W-CONSTANT", "BOUNDED_BY"),
            ("DE-W-CONSTANT", "DEF-ARCHITECTURE", "REQUIRES"),
        }
        and scope_contains_all(
            index, "DE-W-CONSTANT",
            ("-14/15", "constant in a", "no derivation from j",
             "no dictionary source", "no selection premise"),
        )
        and has_status(index, "COSMOLOGY-REGISTER", "D")
        and has_status(index, "DE-CONFORMAL-WEIGHT", "O")
        and has_status(index, "NS-TILT", "H")
        and all(row["owner_item_id"] != "DE-W-CONSTANT"
                for row in gates.values()),
    ))

    wall_new = (
        "J-LI-PENTAGON-DILATION-DEFICIENCY",
        "PENTAGON-ONLY-DILATIONS",
        "J-LI-CYCLIC-CARRIER-DIMENSION",
    )
    wall_edges = {
        (row["item_id"], row["depends_on"], row["relation"])
        for row in dependencies
        if any(claim in (row["item_id"], row["depends_on"])
               for claim in wall_new)
    }
    checks.append((
        "J-LI-WALL-CLOSURES",
        "the pentagon-tower dilation route is dead by the exact constant deficiency with the fired route recorded at F, and every finite-dimensional cyclic carrier is excluded, while the three registered carrier no-gos and the live cocycle-vector hypothesis keep their statuses and no gate or program row is created",
        has_status(index, "J-LI-PENTAGON-DILATION-DEFICIENCY", "T")
        and has_status(index, "PENTAGON-ONLY-DILATIONS", "F")
        and has_status(index, "J-LI-CYCLIC-CARRIER-DIMENSION", "T")
        and all(index[claim]["canon_section"] == "16. p = 5 and the wall"
                and evidence[claim]["evidence_kind"] == "PUBLIC_PROBE"
                and evidence[claim]["architecture_requirement"]
                == "two-architecture"
                and normative[claim]["layer"] == "NOT_APPLICABLE"
                and normative[claim]["gate_ids"] == ""
                for claim in wall_new)
        and index["J-LI-PENTAGON-DILATION-DEFICIENCY"]["evidence"]
        == "probes/P-PENTAGON-ONLY-DILATIONS-1"
        and index["PENTAGON-ONLY-DILATIONS"]["evidence"]
        == "probes/P-PENTAGON-ONLY-DILATIONS-1"
        and index["J-LI-CYCLIC-CARRIER-DIMENSION"]["evidence"]
        == "probes/P-J-LI-CARRIER-NOGO-1"
        and scope_contains_all(
            index, "J-LI-PENTAGON-DILATION-DEFICIENCY",
            ("(1/12)(1 - 1/q^2)", "constant in the tower height",
             "(1/q) g_1"),
        )
        and scope_contains_all(
            index, "PENTAGON-ONLY-DILATIONS",
            ("falsified", "unreachable"),
        )
        and scope_contains_all(
            index, "J-LI-CYCLIC-CARRIER-DIMENSION",
            ("finite-dimensional cyclic", "infinite spectral support",
             "no atom at 1"),
        )
        and wall_edges == {
            ("PENTAGON-ONLY-DILATIONS",
             "J-LI-PENTAGON-DILATION-DEFICIENCY", "REQUIRES"),
        }
        and has_status(index, "J-LI-TORAL-HAAR-NOGO", "T")
        and has_status(index, "J-LI-LAMBDA-HAAR-HS-NOGO", "T")
        and has_status(index, "J-LI-LAMBDA-SHIFT-NOGO", "T")
        and has_status(index, "LAMBDA-COCYCLE-ANGLES", "H")
        and all(row["owner_item_id"] not in wall_new
                for row in gates.values())
        and all(claim not in programs for claim in wall_new),
    ))

    anchor_new = (
        "KERNEL-SUBSET-LANDSCAPE",
        "J-TORAL-ENTROPY",
        "TM-ENTROPY-ZERO",
        "BINARY-READ-RELATIVE-ENTROPY",
    )
    anchor_edges = {
        (row["item_id"], row["depends_on"], row["relation"])
        for row in dependencies
        if any(claim in (row["item_id"], row["depends_on"])
               for claim in anchor_new)
    }
    checks.append((
        "ENTROPY-KERNEL-ANCHORS",
        "the subset landscape decides the exact 32-entry table with connectivity iff dim U_S = 6, and the rate 2 log phi enters with the toral anchor, the zero-entropy driver, and the binary residue bracket, while the layer-bridge obligation keeps its exact scope and no gate or program row is created",
        has_status(index, "KERNEL-SUBSET-LANDSCAPE", "T")
        and has_status(index, "J-TORAL-ENTROPY", "T")
        and has_status(index, "TM-ENTROPY-ZERO", "T")
        and has_status(index, "BINARY-READ-RELATIVE-ENTROPY", "T")
        and all(evidence[claim]["evidence_kind"] == "PUBLIC_PROBE"
                and evidence[claim]["architecture_requirement"]
                == "two-architecture"
                and normative[claim]["gate_ids"] == ""
                for claim in anchor_new)
        and index["KERNEL-SUBSET-LANDSCAPE"]["evidence"]
        == "probes/P-KERNEL-SUBSET-LANDSCAPE-1"
        and all(index[claim]["evidence"]
                == "probes/P-ENTROPY-RESIDUE-MATH-1"
                for claim in ("J-TORAL-ENTROPY", "TM-ENTROPY-ZERO",
                              "BINARY-READ-RELATIVE-ENTROPY"))
        and index["KERNEL-SUBSET-LANDSCAPE"]["canon_section"]
        == "3. The kernel and the census"
        and index["TM-ENTROPY-ZERO"]["canon_section"]
        == "3. The kernel and the census"
        and index["J-TORAL-ENTROPY"]["canon_section"]
        == "2. Time, space, and the decoder"
        and index["BINARY-READ-RELATIVE-ENTROPY"]["canon_section"]
        == "2. Time, space, and the decoder"
        and normative["KERNEL-SUBSET-LANDSCAPE"]["layer"] == "L1"
        and normative["J-TORAL-ENTROPY"]["layer"] == "L2"
        and normative["TM-ENTROPY-ZERO"]["layer"] == "L5"
        and normative["BINARY-READ-RELATIVE-ENTROPY"]["layer"]
        == "NOT_APPLICABLE"
        and scope_contains_all(
            index, "KERNEL-SUBSET-LANDSCAPE",
            ("dim U_S = 6", "acde", "abcde"),
        )
        and scope_contains_all(
            index, "J-TORAL-ENTROPY",
            ("2 log phi", "#fix(t^n)", "1860496"),
        )
        and scope_contains_all(
            index, "TM-ENTROPY-ZERO",
            ("linear factor complexity", "entropy rate 0"),
        )
        and scope_contains_all(
            index, "BINARY-READ-RELATIVE-ENTROPY",
            ("log(phi^2/2)", "2 log phi = log 2 + log(phi^2/2)"),
        )
        and anchor_edges == {
            ("KERNEL-SUBSET-LANDSCAPE", "KERNEL-CONNECT-ALL-K",
             "REQUIRES"),
            ("KERNEL-SUBSET-LANDSCAPE", "KERNEL-WEDGE-AFFINITY",
             "REQUIRES"),
            ("J-TORAL-ENTROPY", "J-STEP", "REQUIRES"),
            ("J-TORAL-PERIODIC-POINTS", "J-TORAL-ENTROPY", "REQUIRES"),
        }
        and has_status(index, "KERNEL-CONNECT-ALL-K", "T")
        and has_status(index, "ENTROPY-LAYER-BRIDGE", "O")
        and scope_contains_all(
            index, "ENTROPY-LAYER-BRIDGE",
            ("equal cardinalities do not construct",),
        )
        and all(row["owner_item_id"] not in anchor_new
                for row in gates.values())
        and all(claim not in programs for claim in anchor_new),
    ))

    arith_new = ("J-MAHLER-MEASURE", "REGULATOR-TWO-LOG-PHI",
                 "CYCLOTOMIC-CLASS-NUMBER-ONE", "J-TORAL-PERIODIC-POINTS")
    arith_edges = {
        (row["item_id"], row["depends_on"], row["relation"])
        for row in dependencies
        if any(claim in (row["item_id"], row["depends_on"])
               for claim in arith_new)
    }
    checks.append((
        "TWOLOGPHI-ARITHMETIC-ANCHOR",
        "2 log phi gains its arithmetic anchor as a Mahler measure and a regulator, with class number one proved rather than imported and the periodic-point structure entering at C, while the entropy bridge keeps its exact scope and every new row carries the fence as a ledger edge",
        has_status(index, "J-MAHLER-MEASURE", "T")
        and has_status(index, "REGULATOR-TWO-LOG-PHI", "T")
        and has_status(index, "CYCLOTOMIC-CLASS-NUMBER-ONE", "T")
        and has_status(index, "J-TORAL-PERIODIC-POINTS", "C")
        and all(index[claim]["evidence"] == "probes/P-TWOLOGPHI-INVARIANTS-1"
                and evidence[claim]["evidence_kind"] == "PUBLIC_PROBE"
                and evidence[claim]["architecture_requirement"]
                == "two-architecture"
                and normative[claim]["gate_ids"] == ""
                for claim in arith_new)
        and index["J-MAHLER-MEASURE"]["canon_section"]
        == "1. The axiom and the two projections"
        and index["REGULATOR-TWO-LOG-PHI"]["canon_section"]
        == "4. The two places"
        and index["CYCLOTOMIC-CLASS-NUMBER-ONE"]["canon_section"]
        == "4. The two places"
        and index["J-TORAL-PERIODIC-POINTS"]["canon_section"]
        == "2. Time, space, and the decoder"
        and normative["J-MAHLER-MEASURE"]["layer"] == "L1"
        and normative["REGULATOR-TWO-LOG-PHI"]["layer"] == "L1"
        and normative["CYCLOTOMIC-CLASS-NUMBER-ONE"]["layer"] == "L1"
        and normative["J-TORAL-PERIODIC-POINTS"]["layer"] == "L2"
        and scope_contains_all(index, "J-MAHLER-MEASURE",
                               ("mahler measure", "log m(j) = 2 log phi",
                                "irreducible over q"))
        and scope_contains_all(index, "REGULATOR-TWO-LOG-PHI",
                               ("reg(q(zeta_5)) = 2 log phi",
                                "fundamental unit", "labeled imports"))
        and scope_contains_all(index, "CYCLOTOMIC-CLASS-NUMBER-ONE",
                               ("1125 < 16 pi^4", "5 < 16",
                                "proved not imported"))
        and scope_contains_all(index, "J-TORAL-PERIODIC-POINTS",
                               ("l_n^2", "(l_n - 2)^2", "finite-range"))
        and arith_edges == {
            ("J-MAHLER-MEASURE", "J-STEP", "REQUIRES"),
            ("J-MAHLER-MEASURE", "ENTROPY-LAYER-BRIDGE", "BOUNDED_BY"),
            ("REGULATOR-TWO-LOG-PHI", "J-PROJECTIONS", "REQUIRES"),
            ("REGULATOR-TWO-LOG-PHI", "ENTROPY-LAYER-BRIDGE", "BOUNDED_BY"),
            ("CYCLOTOMIC-CLASS-NUMBER-ONE",
             "QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS", "REQUIRES"),
            ("J-TORAL-PERIODIC-POINTS", "J-TORAL-ENTROPY", "REQUIRES"),
            ("J-TORAL-PERIODIC-POINTS", "ENTROPY-LAYER-BRIDGE", "BOUNDED_BY"),
        }
        and has_status(index, "J-TORAL-ENTROPY", "T")
        and has_status(index, "J-UNIT", "T")
        and has_status(index, "ENTROPY-LAYER-BRIDGE", "O")
        and scope_contains_all(index, "ENTROPY-LAYER-BRIDGE",
                               ("equal cardinalities do not construct",))
        and all(row["owner_item_id"] not in arith_new
                for row in gates.values())
        and all(claim not in programs for claim in arith_new),
    ))

    metro_edges = {
        (row["item_id"], row["depends_on"], row["relation"])
        for row in dependencies
        if "METRO-FORBIDDEN-WITNESSES" in (row["item_id"], row["depends_on"])
    }
    checks.append((
        "METRO-FORBIDDEN-WITNESSES",
        "obligation B is discharged for the five entries section 15 names, at C on the completed public probe with exactly its two declared edges, while the parent keeps status O and STOP with only its obligation B clause changed and the arrows row does not move",
        has_status(index, "METRO-FORBIDDEN-WITNESSES", "C")
        and index["METRO-FORBIDDEN-WITNESSES"]["evidence"]
        == "probes/P-METRO-FORBIDDEN-WITNESSES-1"
        and index["METRO-FORBIDDEN-WITNESSES"]["canon_section"]
        == "15. Couplings, instruments, and metrology"
        and evidence["METRO-FORBIDDEN-WITNESSES"]["evidence_kind"]
        == "PUBLIC_PROBE"
        and evidence["METRO-FORBIDDEN-WITNESSES"]["architecture_requirement"]
        == "two-architecture"
        and normative["METRO-FORBIDDEN-WITNESSES"]["layer"] == "L5"
        and normative["METRO-FORBIDDEN-WITNESSES"]["gate_ids"] == ""
        and metro_edges == {
            ("METRO-FORBIDDEN-WITNESSES", "METRO-REDUCTION-ARROWS",
             "REQUIRES"),
            ("METRO-FORBIDDEN-WITNESSES", "METRO-REDUCTION-CALCULUS",
             "BOUNDED_BY"),
        }
        and scope_contains_all(
            index, "METRO-FORBIDDEN-WITNESSES",
            ("functional obstruction", "16140", "21987",
             "distinctions of the stream"),
        )
        and has_status(index, "METRO-REDUCTION-CALCULUS", "O")
        and has_status(index, "METRO-REDUCTION-ARROWS", "C")
        and scope_contains_all(
            index, "METRO-REDUCTION-CALCULUS",
            ("discharged for the five entries section 15 names",
             "obligation d", "obligation e"),
        )
        and "METRO-FORBIDDEN-WITNESSES" not in programs
        and all(row["owner_item_id"] != "METRO-FORBIDDEN-WITNESSES"
                for row in gates.values()),
    ))

    fw_requires = {}
    for row in dependencies:
        fw_requires.setdefault(row["item_id"], set()).add(row["depends_on"])
    fw_seen, fw_stack = set(), ["DEF-QDD-DIRECT-WRITE"]
    while fw_stack:
        fw_cur = fw_stack.pop()
        for fw_nxt in fw_requires.get(fw_cur, ()):
            if fw_nxt not in fw_seen:
                fw_seen.add(fw_nxt)
                fw_stack.append(fw_nxt)
    fw_qdd = {x for x in fw_seen if x.startswith("DEF-QDD-") or x.startswith("QDD-")}
    checks.append((
        "QDD-DIRECT-FIREWALL",
        "the definitional closure of DEF-QDD-DIRECT-WRITE in the dependency ledger is exactly the domain, the balanced piston, the amplitude, the coefficient data, the trace pairing, the LOW LINE and the record schema, and contains no factor-side object (Gram, dagger, transpose, Q_QDD, the carrier equality, the projectors, the Born pairing, the factor map)",
        fw_qdd == {"DEF-QDD-DOMAIN-K0", "DEF-QDD-BALANCED-PISTON",
                   "DEF-QDD-AMPLITUDE-B0", "DEF-QDD-COEFFICIENT-Q",
                   "DEF-QDD-TRACE-PAIRING", "DEF-QDD-LOW-LINE",
                   "DEF-QDD-MATTER-RECORD"}
        and not fw_seen & {"DEF-QDD-GRAM", "DEF-QDD-DAGGER", "DEF-QDD-TRANSPOSE",
                           "DEF-QDD-QPAIR", "DEF-QDD-QCARRIER-EQUALITY",
                           "DEF-QDD-PROJECTOR-LOW", "DEF-QDD-PROJECTOR-HIGH",
                           "DEF-QDD-BRANCH-WEIGHT-PAIRING", "DEF-QDD-FACTOR-MAP"},
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
