Warning: truncated output (original token count: 69514)
Total output lines: 5976

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
CORE_SELECTION = ROOT / "canon" / "CORE_SELECTION.tsv"
FRONTIER = ROOT / "canon" / "FRONTIER.md"
CANON = ROOT / "canon" / "CANON.md"
REPRODUCE = ROOT / "reproduce"
SUCCESSOR_MANIFEST_DIR = (
    ROOT / "notes" / "canon" / "QDD-ALGEBRAIC-DMATTER-SUCCESSOR-V70"
)


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


def registry_row_sha256(index, claim_id):
    row = index[claim_id]
    fields = (
        "claim_id", "status", "scope", "canon_section", "evidence", "falsifier",
    )
    payload = "\t".join(row[field] for field in fields)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def table_row_sha256(row):
    payload = "\t".join(row.values())
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


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
    canon_text = CANON.read_text(encoding="utf-8")
    core_text = CORE.read_text(encoding="utf-8")
    frontier_text = FRONTIER.read_text(encoding="utf-8")
    core_selection_rows = load_table(CORE_SELECTION)
    checks = []

    qdd_predecessor = "QUADRATIC-DECODER-DATA"
    qdd_successor = "ALGEBRAIC-DMATTER"
    qdd_apparatus = "QDD-INSTRUMENT-APPARATUS"
    qdd_current_split = (
        qdd_predecessor not in index
        and qdd_predecessor not in normative
        and qdd_predecessor not in evidence
        and qdd_predecessor not in programs
        and all(
            row["item_id"] != qdd_predecessor
            and row["depends_on"] != qdd_predecessor
            for row in dependencies
        )
        and has_status(index, qdd_successor, "D")
        and normative.get(qdd_successor, {}).get("item_type") == "DICTIONARY"
        and normative.get(qdd_successor, {}).get("status") == "D"
        and normative.get(qdd_successor, {}).get("layer") == "L1"
        and normative.get(qdd_successor, {}).get("gate_ids") == ""
        and evidence.get(qdd_successor, {}).get("evidence_kind") == "INLINE_CANON"
        and evidence.get(qdd_successor, {}).get("location") == "inline"
        and evidence.get(qdd_successor, {}).get("sha256")
        == scope_sha256(index, qdd_successor)
        and evidence.get(qdd_successor, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(qdd_successor, {}).get("architecture_requirement") == "none"
        and qdd_successor not in programs
        and all(row["owner_item_id"] != qdd_successor for row in gates.values())
        and has_status(index, qdd_apparatus, "O")
        and normative.get(qdd_apparatus, {}).get("item_type") == "OBLIGATION"
        and normative.get(qdd_apparatus, {}).get("status") == "O"
        and normative.get(qdd_apparatus, {}).get("layer") == "MULTI"
        and normative.get(qdd_apparatus, {}).get("gate_ids") == ""
        and programs.get(qdd_apparatus) == {
            "claim_id": qdd_apparatus,
            "program_id": "DECODER_CORE",
            "queue_role": "FOLLOWUP",
            "work_state": "STOP",
            "work_mode": "FORMAL",
        }
    )

    counts = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    two_architecture = sum(
        row["architecture_requirement"] == "two-architecture"
        for row in evidence.values()
    )
    expected_counts = {"T": 225, "D": 45, "C": 34, "F": 17,
                       "O": 29, "H": 2}
    checks.append((
        "COUNTS",
        "registry and companion-ledger counts match Public Canon v74",
        len(rows) == 352
        and counts == expected_counts
        and len(normative) == 398
        and len(dependencies) == 648
        and len(evidence) == 352
        and two_architecture == 265
        and len(history) == 882
        and len(gates) == 14
        and len(programs) == 31
        and len({row["program_id"] for row in programs.values()}) == 8
        and len(core_selection_rows) == 30
        and sum(path.is_dir() for path in REPRODUCE.iterdir()) == 24,
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
        and qdd_current_split
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
        and "## Two field characterisations involving five" in core_text
        and "{(K_5,5),(K_8,2)}" in core_text
        and "unique absolute-discriminant" in core_text
        and "separate frozen classes, not a physical-selection chain or evidence"
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
        "marked semilinear pair stays T at L4; the algebraic decoder dictionary stays D while physical apparatus and measure stay O/STOP",
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
        and qdd_current_split
        and has_status(index, "COLOR-MEASURE-SELECTION", "O")
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
        == "bundle-ma…39514 tokens truncated…        "95e6cf05f176c25f7f563fd6710a6fa739efa4f41952411d617dc14fe3c3fd0c"
            ),
            "bundle": (
                "a8b728effa5c936929e06a9da61447d8ae133dda4ba9b3030b0b84065ea2dc31"
            ),
            "dependencies": {"CM-ALTERNATING-PENCIL"},
            "scope_markers": (
                "Per_Z(Omega)={Omega(C):C in Lambda^2 L}",
                "every GL_4(Z) pullback preserves Per_Z",
                "one J-pullback does not scale it by phi^-2",
                "can return a unit-period bivector",
                "no nonzero decomposable rational fixed bivector",
                "integer image subgroup rather than a geometric period integral",
                "no torus, manifold, homology, cohomology, action, h, hbar, 2 pi",
                "L2-L6 lift is selected",
            ),
        },
    }
    v69_claims = tuple(v69_contract)
    v69_actual_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in v69_claims
    }
    v69_history_rows = [
        row for row in history if row["release"].startswith("canon-v69")
    ]
    v69_events = {row["claim_id"]: row for row in v69_history_rows}
    v69_excluded_claims = {
        "J-QUADRATIC-CARRY-NORM-SEAM",
        "THORN-PLENUM-QUADRANT-CHARACTERIZATION",
        "THORN-TRIANGLE-PENTAGON-RIGIDITY",
    }
    v69_excluded_evidence_locations = {
        "probes/P-J-QUADRATIC-CARRY-NORM-SEAM-1",
        "probes/P-J-QUADRATIC-CARRY-NORM-SEAM-2",
        "probes/P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-1",
        "probes/P-THORN-PLENUM-QUADRANT-CHARACTERIZATION-1",
        "probes/P-THORN-PLENUM-QUADRANT-CHARACTERIZATION-2",
        "probes/P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1",
    }
    checks.append((
        "V69-CM",
        "five focused L1 CM lattice and ramification theorems keep exact "
        "scopes, evidence, dependencies and nonselection firewalls with no "
        "gate, Frontier, CORE or action bridge",
        all(has_status(index, claim, "T") for claim in v69_claims)
        and all(
            index[claim]["canon_section"] == v69_contract[claim]["section"]
            and index[claim]["evidence"] == v69_contract[claim]["path"]
            and scope_sha256(index, claim) == v69_contract[claim]["scope_sha"]
            and registry_row_sha256(index, claim)
            == v69_contract[claim]["row_sha"]
            and scope_contains_all(
                index, claim, v69_contract[claim]["scope_markers"]
            )
            for claim in v69_claims
        )
        and all(
            normative[claim]["item_type"] == "THEOREM"
            and normative[claim]["claim_id"] == claim
            and normative[claim]["status"] == "T"
            and normative[claim]["layer"] == "L1"
            and normative[claim]["gate_ids"] == ""
            and normative[claim]["statement_source"]
            == f"canon/CANON.md::{claim} [T]"
            for claim in v69_claims
        )
        and all(
            evidence[claim]["evidence_id"] == "EV-" + claim
            and evidence[claim]["evidence_kind"] == "PUBLIC_PROBE"
            and evidence[claim]["location"] == v69_contract[claim]["path"]
            and evidence[claim]["sha256"] == v69_contract[claim]["bundle"]
            and evidence[claim]["hash_mode"] == "bundle-manifest-sha256-v1"
            and evidence[claim]["architecture_requirement"]
            == "two-architecture"
            for claim in v69_claims
        )
        and all(
            v69_actual_dependencies[claim] == {
                (dependency, "REQUIRES")
                for dependency in v69_contract[claim]["dependencies"]
            }
            for claim in v69_claims
        )
        and all(
            normative[dependency]["status"] == "T"
            and normative[dependency]["layer"] in {"L1", "NOT_APPLICABLE"}
            for claim in v69_claims
            for dependency in v69_contract[claim]["dependencies"]
        )
        and len(v69_history_rows) == 5
        and set(v69_events) == set(v69_claims)
        and all(
            v69_events[claim]["event_id"] == f"CANON69-DECLARE-{claim}"
            and v69_events[claim]["event_sequence"] == "1"
            and v69_events[claim]["event_date"] == "2026-08-29"
            and v69_events[claim]["release"] == "canon-v69-candidate"
            and v69_events[claim]["event_type"] == "DECLARE"
            and v69_events[claim]["previous_status"] == "-"
            and v69_events[claim]["new_status"] == "T"
            and v69_events[claim]["scope_sha256"]
            == v69_contract[claim]["scope_sha"]
            and v69_events[claim]["evidence_id"] == "EV-" + claim
            and v69_events[claim]["evidence_location"]
            == v69_contract[claim]["path"]
            and v69_events[claim]["evidence_sha256"]
            == v69_contract[claim]["bundle"]
            for claim in v69_claims
        )
        and all(row["owner_item_id"] not in v69_claims for row in gates.values())
        and all(claim not in programs for claim in v69_claims)
        and all(f"- {claim} [" not in core_text for claim in v69_claims)
        and all(
            row["claim_id"] not in v69_claims for row in core_selection_rows
        )
        and all(
            claim not in index
            and claim not in normative
            and claim not in evidence
            and claim not in programs
            for claim in v69_excluded_claims
        )
        and all(
            row["location"] not in v69_excluded_evidence_locations
            for row in evidence.values()
        )
        and hashlib.sha256(CORE_SELECTION.read_bytes()).hexdigest() == (
            "eee121dd437d06fc2b0fda5377ea6c2e6e01b220e5f1bfb9aa09727885d03d4e"
        ),
    ))

    v70_contract = {
        "ALGEBRAIC-DMATTER": {
            "event_id": "CANON70-DECLARE-ALGEBRAIC-DMATTER",
            "sequence": "1",
            "event_type": "DECLARE",
            "previous": "-",
            "new": "D",
            "scope_sha": "b542d0f6d40c8ade93589334670156c2b5788ef5414a3a3efddc777ea7635d75",
            "row_sha": "41d4f53def45ba05ecd5d532ff2a145a0d16259a6df75a86d68a2e25950d71d4",
            "evidence_id": "EV-ALGEBRAIC-DMATTER",
            "evidence_location": "inline",
            "evidence_sha": "b542d0f6d40c8ade93589334670156c2b5788ef5414a3a3efddc777ea7635d75",
        },
        "READING-SPLIT": {
            "event_id": "CANON70-SCOPE-READING-SPLIT",
            "sequence": "14",
            "event_type": "SCOPE_CHANGE",
            "previous": "D",
            "new": "D",
            "scope_sha": "b503f0f6a30965623a09e826795bce4ce626b171340b2fecfa86fd0cf2818922",
            "row_sha": "e762db5b7554d1b57f9d7666338a672aec6d957235dbcfc7b6f2081c0d5b8151",
            "evidence_id": "EV-READING-SPLIT",
            "evidence_location": "inline",
            "evidence_sha": "b503f0f6a30965623a09e826795bce4ce626b171340b2fecfa86fd0cf2818922",
        },
        "QDD-ALGEBRAIC-FACTORIZATION": {
            "event_id": "CANON70-SCOPE-QDD-ALGEBRAIC-FACTORIZATION",
            "sequence": "2",
            "event_type": "SCOPE_CHANGE",
            "previous": "T",
            "new": "T",
            "scope_sha": "873c418ffee3ad66eaf9d7e279929aaa4172785a12c2081c4d2734e041ea939f",
            "row_sha": "8655df8ba78aca0c007ee5808605161247546d172935a43ead51f6f45fbe1999",
            "evidence_id": "EV-QDD-ALGEBRAIC-FACTORIZATION",
            "evidence_location": "reproduce/qdd-route-a",
            "evidence_sha": "897f18e27e822a96ece61048cb17d4a5488b267d014f2bb10787f1a56edc8c6a",
        },
        "QPAIR-HERM-INTEGER-NONDESCENT": {
            "event_id": "CANON70-SCOPE-QPAIR-HERM-INTEGER-NONDESCENT",
            "sequence": "2",
            "event_type": "SCOPE_CHANGE",
            "previous": "T",
            "new": "T",
            "scope_sha": "54c0338ff722ffe8e69a7435477adf43c704c15bbbf82967c50184f89dc4c697",
            "row_sha": "84ee9b37aaac46311ff4458ea3ea117258c8c4e418813c420284dc23b20706b3",
            "evidence_id": "EV-QPAIR-HERM-INTEGER-NONDESCENT",
            "evidence_location": "probes/P-QPAIR-C4-2I-MINIMALITY-1",
            "evidence_sha": "6f1d5a5859a193cb68eb53f6ed58f5da21b25f3c0084c3875eede690317ea592",
        },
        "QDD-INSTRUMENT-APPARATUS": {
            "event_id": "CANON70-SCOPE-QDD-INSTRUMENT-APPARATUS",
            "sequence": "6",
            "event_type": "SCOPE_CHANGE",
            "previous": "O",
            "new": "O",
            "scope_sha": "2aa1688ede2fa319cd0fad5467195f1df8a1ab5308f6cf725c0030abf48cb6f5",
            "row_sha": "06288f428275ed4dd79e399c3ea0b8f298e838ba32d4ab5d427c1cbed3133d21",
            "evidence_id": "EV-QDD-INSTRUMENT-APPARATUS",
            "evidence_location": "inline",
            "evidence_sha": "2aa1688ede2fa319cd0fad5467195f1df8a1ab5308f6cf725c0030abf48cb6f5",
        },
    }
    v70_retirement = {
        "event_id": "CANON70-RETIRE-QUADRATIC-DECODER-DATA",
        "sequence": "14",
        "event_type": "RETIRE",
        "previous": "O",
        "new": "RETIRED",
        "scope_sha": "8b2b79b5060bbea943429afda25f24affcda2bd9a55961965cf63a962b3cee8d",
        "evidence_id": "EV-QUADRATIC-DECODER-DATA",
        "evidence_location": "inline",
        "evidence_sha": "8b2b79b5060bbea943429afda25f24affcda2bd9a55961965cf63a962b3cee8d",
    }
    v70_history_rows = [
        row for row in history if row["release"] == "canon-v70-candidate"
    ]
    v70_events = {row["claim_id"]: row for row in v70_history_rows}
    v70_successor_dependencies = {
        "DEF-ARCHITECTURE", "DEF-DECODER-MATTER",
        "DEF-DECODER-COMPLETION-CONTRACT", "COUPLINGS-DETERMINE",
        "QDD-ALGEBRAIC-FACTORIZATION", "DEF-QDD-COEFFICIENT-Q",
        "DEF-QDD-BALANCED-PISTON", "DEF-QDD-DOMAIN-K0",
        "DEF-QDD-AMPLITUDE-B0", "DEF-QDD-GRAM", "DEF-QDD-DAGGER",
        "DEF-QDD-TRANSPOSE", "DEF-QDD-QCARRIER-EQUALITY",
        "DEF-QDD-QPAIR", "DEF-QDD-PROJECTOR-LOW",
        "DEF-QDD-PROJECTOR-HIGH", "DEF-QDD-BRANCH-WEIGHT-PAIRING",
        "DEF-QDD-MATTER-RECORD", "DEF-QDD-DIRECT-WRITE",
    }
    v70_reading_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == "READING-SPLIT"
    }
    v70_apparatus_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == qdd_apparatus
    }
    v70_successor_consumers = {
        (row["item_id"], row["relation"])
        for row in dependencies if row["depends_on"] == qdd_successor
    }
    v70_live_frontier = {
        row["claim_id"] for row in rows if row["status"] in {"H", "O"}
    }
    v70_apparatus_manifest_lines = (
        "apparatus_manifest.projector_target_ids =",
        "apparatus_manifest.effect_ids = (UNRESOLVED)",
        "apparatus_manifest.instrument_ids = (UNRESOLVED)",
        "apparatus_manifest.apparatus_carrier_id = UNRESOLVED",
        "apparatus_manifest.ready_state_id = UNRESOLVED",
        "apparatus_manifest.physical_context_key_id = UNRESOLVED",
        "apparatus_manifest.selected_ready_phase_id = UNRESOLVED",
        "apparatus_manifest.coupling_id = UNRESOLVED",
        "apparatus_manifest.pointer_id = UNRESOLVED",
        "apparatus_manifest.reduction_id = UNRESOLVED",
        "apparatus_manifest.target_comparison_relation_id = UNRESOLVED",
        "apparatus_manifest.target_comparison_domain_id = UNRESOLVED",
        "apparatus_manifest.complete_apparatus_family_class_id = UNRESOLVED",
        "apparatus_manifest.apparatus_family_equality_id = UNRESOLVED",
        "apparatus_manifest.phase_equality_id = UNRESOLVED",
        "apparatus_manifest.target_independence_certificate_id = UNRESOLVED",
        "apparatus_manifest.class_completeness_certificate_id = UNRESOLVED",
        "apparatus_manifest.realization_certificate_ids = (UNRESOLVED)",
        "apparatus_manifest.realized_outcome_ids = (UNRESOLVED)",
        "apparatus_manifest.realized_event_semantics_id = UNRESOLVED",
        "apparatus_manifest.occurrence_law_id = UNRESOLVED",
        "apparatus_manifest.post_state_instrument_ids = (UNRESOLVED)",
        "apparatus_manifest.persistence_update_reset_law_id = UNRESOLVED",
        "apparatus_manifest.zero_support_semantics_id = UNRESOLVED",
        "apparatus_manifest.l1_to_l5_gate_id = UNRESOLVED",
        "apparatus_manifest.l6_measure_boundary = REQUIRES_SEPARATE_GATE",
    )
    v70_algebraic_manifest_lines = (
        "stage_id = D_matter",
        "leg_id = D_quadratic",
        "domain_id = DEF-QDD-DOMAIN-K0",
        "codomain_id = DEF-QDD-MATTER-RECORD",
        "write_map_id = DEF-QDD-DIRECT-WRITE",
        "totality_domain_id = DEF-QDD-DOMAIN-K0",
        "(support_state, total_weight, branch_weights,",
        "density_state, normalized_weight_state)",
        "quadratic_manifest.coefficient_ring_id = DEF-QDD-COEFFICIENT-Q",
        "quadratic_manifest.effective_carrier_id = DEF-QDD-BALANCED-PISTON",
        "quadratic_manifest.orbit_to_amplitude_bridge_id = DEF-QDD-AMPLITUDE-B0",
        "quadratic_manifest.gram_id = DEF-QDD-GRAM",
        "quadratic_manifest.dagger_id = DEF-QDD-DAGGER",
        "quadratic_manifest.transpose_id = DEF-QDD-TRANSPOSE",
        "quadratic_manifest.qcarrier_id = DEF-QDD-QCARRIER-EQUALITY",
        "quadratic_manifest.q_equality_id = DEF-QDD-QCARRIER-EQUALITY",
        "quadratic_manifest.q_map_id = DEF-QDD-QPAIR",
        "quadratic_manifest.projector_ids =",
        "(DEF-QDD-PROJECTOR-LOW, DEF-QDD-PROJECTOR-HIGH)",
        "quadratic_manifest.branch_weight_pairing_id =",
        "DEF-QDD-BRANCH-WEIGHT-PAIRING",
        "quadratic_manifest.factorization_map_id = DEF-QDD-FACTOR-MAP",
        "quadratic_manifest.slot_boundary_id = QDD-QCARRIER-DIAGONAL-BOUNDARY",
        "quadratic_manifest.factorization_theorem_id =",
        "QDD-ALGEBRAIC-FACTORIZATION",
    )
    v70_frozen_manifest = {
        "EXPECTED.txt": (1145, "931b8de96b408a7a427103949e2d0a53111081df0a4d7072ad3b6788264f3880"),
        "MANIFEST.json": (16083, "561cfd403c126981342393c473846acbb7d54c2194cecff43ae1b3dc835636c7"),
        "README.md": (7162, "948df790610f4fde4e64013192ceda52dc0990bdfe1a16c650631700337154fa"),
        "verify.py": (34325, "32510c01386db17589104190424ddb76f47a05b4a7f429a613e2b83dd78af58e"),
    }
    v70_actual_manifest = {
        path.name: (
            path.stat().st_size,
            hashlib.sha256(path.read_bytes()).hexdigest(),
        )
        for path in SUCCESSOR_MANIFEST_DIR.iterdir() if path.is_file()
    }
    checks.append((
        "V70-QDD-SPLIT",
        "the composite quadratic O retires as a split; ALGEBRAIC-DMATTER is "
        "an owner-selected D/L1 dictionary with exact algebraic wiring and no "
        "gate, while all transferred physical debt stays on "
        "QDD-INSTRUMENT-APPARATUS at O/STOP",
        qdd_current_split
        and len(v70_history_rows) == 6
        and set(v70_events) == set(v70_contract) | {qdd_predecessor}
        and all(
            v70_events[claim]["event_id"] == contract["event_id"]
            and v70_events[claim]["event_sequence"] == contract["sequence"]
            and v70_events[claim]["event_date"] == "2026-08-29"
            and v70_events[claim]["event_type"] == contract["event_type"]
            and v70_events[claim]["previous_status"] == contract["previous"]
            and v70_events[claim]["new_status"] == contract["new"]
            and v70_events[claim]["scope_sha256"] == contract["scope_sha"]
            and v70_events[claim]["evidence_id"] == contract["evidence_id"]
            and v70_events[claim]["evidence_location"]
            == contract["evidence_location"]
            and v70_events[claim]["evidence_sha256"] == contract["evidence_sha"]
            and scope_sha256(index, claim) == contract["scope_sha"]
            and registry_row_sha256(index, claim) == contract["row_sha"]
            and evidence[claim]["evidence_id"] == contract["evidence_id"]
            and evidence[claim]["location"] == contract["evidence_location"]
            and evidence[claim]["sha256"] == contract["evidence_sha"]
            for claim, contract in v70_contract.items()
        )
        and all(
            v70_events[qdd_predecessor][field] == expected
            for field, expected in {
                "event_id": v70_retirement["event_id"],
                "event_sequence": v70_retirement["sequence"],
                "event_type": v70_retirement["event_type"],
                "previous_status": v70_retirement["previous"],
                "new_status": v70_retirement["new"],
                "scope_sha256": v70_retirement["scope_sha"],
                "evidence_id": v70_retirement["evidence_id"],
                "evidence_location": v70_retirement["evidence_location"],
                "evidence_sha256": v70_retirement["evidence_sha"],
            }.items()
        )
        and v70_events[qdd_predecessor]["event_date"] == "2026-08-29"
        and all(
            phrase in v70_events[qdd_predecessor]["rationale"].lower()
            for phrase in ("no falsifier fired",
                           "no positive closure or scientific result is recorded",
                           "rather than satisfied")
        )
        and v70_successor_edges == v70_successor_dependencies
        and v70_reading_dependencies == {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            ("CODEC-TR4", "REQUIRES"),
            (qdd_successor, "REQUIRES"),
        }
        and v70_apparatus_dependencies == {
            ("DEF-QDD-PROJECTOR-LOW", "REQUIRES"),
            ("DEF-QDD-PROJECTOR-HIGH", "REQUIRES"),
            ("DEF-QDD-GRAM", "REQUIRES"),
            ("DEF-DECODER-COMPLETION-CONTRACT", "REQUIRES"),
        }
        and v70_successor_consumers == {("READING-SPLIT", "REQUIRES")}
        and "MEASURE-BORN-VERB" not in v70_successor_edges
        and scope_contains_all(
            index, qdd_successor,
            ("owner-adopted L1 algebraic dictionary binds only",
             "D_matter|_(K_QDD,D_quadratic) := D_QDD_direct",
             "exactly five fields", "ordered algebraic projector pair",
             "algebraic branch-weight pairing", "total only on K_QDD",
             "owner architecture choice",
             "not a mathematically forced, unique or canonical route",
             "PHYSICAL-DMATTER remains unadopted, not falsified and not shown complete"),
        )
        and index[qdd_successor]["falsifier"] == ""
        and scope_contains_all(
            index, "READING-SPLIT",
            ("ALGEBRAIC-DMATTER only on (K_QDD,D_quadratic)",
             "L1 algebraic data", "not a physical effect, apparatus",
             "no totality beyond K_QDD", "other-leg closure"),
        )
        and scope_contains_all(
            index, "QPAIR-HERM-INTEGER-NONDESCENT",
            ("no bridge to DEF-QDD-QPAIR", "algebraic branch-weight pairing",
             "decoder write map", "or ALGEBRAIC-DMATTER",
             "no physical U(1), apparatus"),
        )
        and scope_contains_all(
            index, qdd_apparatus,
            ("sole owner of the physical debt split from QUADRATIC-DECODER-DATA",
             "transferred but not satisfied", "projector_target_ids",
             "are algebraic targets and are not aliases for physical effects",
             "effect_ids, instrument_ids, apparatus_carrier_id",
             "target-independence and class-completeness certificates",
             "persistence/update/reset law", "all remain UNRESOLVED",
             "any L6 measure requiring a separate gate",
             "do not close or partially satisfy this row",
             "PHYSICAL-DMATTER remains unadopted, not falsified and not shown complete",
             "SAMPLING NOT PROVIDED rather than impossible"),
        )
        and all(line in canon_text for line in v70_algebraic_manifest_lines)
        and all(line in canon_text for line in v70_apparatus_manifest_lines)
        and "an `ALGEBRAIC_ONLY` L1 `READOUT`" in canon_text
        and "there is no sixth field" in canon_text
        and "no `effect_ids` or `born_pairing_id`" in canon_text
        and "no algebraic identifier is an alias for a physical" in canon_text
        and "The debt is TRANSFERRED_NOT_SATISFIED." in canon_text
        and "PHYSICAL-DMATTER" not in index
        and "PHYSICAL-DMATTER" not in normative
        and "PHYSICAL-DMATTER" not in evidence
        and "PHYSICAL-DMATTER" not in programs
        and "QDD-PROJECTOR-APPARATUS" not in index
        and v70_live_frontier == set(programs)
        and f"- {qdd_predecessor} [" not in frontier_text
        and f"- {qdd_successor} [" not in frontier_text
        and f"- {qdd_apparatus} [O]:" in frontier_text
        and all(row["claim_id"] != qdd_successor for row in core_selection_rows)
        and f"- {qdd_successor} [" not in core_text
        and v70_actual_manifest == v70_frozen_manifest,
    ))

    v72_contract = {
        "FCC-WEIGHTED-SHELL-SYMBOL": {
            "status": "T",
            "item_type": "THEOREM",
            "layer": "L2",
            "gate_ids": "",
            "row_sha": "3d381847735954398dec73af73d3b85d6b113fc5a9847e67837c2fbc4b542f9f",
            "scope_sha": "c444163e61c5df5727b4d6925e49515d00db2ee3e607f58267489b544358ae53",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-FCC-WEIGHTED-SHELL-SYMBOL-1",
            "evidence_sha": "23522dc6c0fc91b8e7b6953be5922726e8de1d09f15bc3e43e5f63e1a162bd3f",
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "unique positive integral solution of minimum total weight 24",
                "the exact sixth-order term is anisotropic",
                "no global remainder",
                "physical-photon conclusion",
            ),
        },
        "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP": {
            "status": "T",
            "item_type": "THEOREM",
            "layer": "L4",
            "gate_ids": "",
            "row_sha": "262439e776ad0da4a6d2e1c542b591c543d462b690b0eabd596a5a2334094dc3",
            "scope_sha": "a8cf70ace567afe5090d0927d30c6dbf5c3defc1aafae3ebca75a267d1199177",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-PHOTON-WILSON-VILLAIN-BRIDGE-1",
            "evidence_sha": "ea6cb44943cc5d98ffd4257d5ab84dfeefa4f06f929532369af186f2dd828bb7",
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "unordered bi-support",
                "direct finite-coupling nonmembership",
                "no parameter limit",
                "no parameter limit, projective closure",
                "massless",
                "physical-photon conclusion",
            ),
        },
        "PHOTON-CONE-CONVERGENCE": {
            "status": "O",
            "item_type": "OBLIGATION",
            "layer": "MULTI",
            "gate_ids": (
                "GATE-L2-L5-PHOTON-TEMPORAL-CHARACTERISTIC;"
                "GATE-L4-L5-PHOTON-CONE-IDENTIFICATION"
            ),
            "row_sha": "ddbb22ed4ec217af13846e7213e0d8c853e119ab815f7727aca1f307d1fa5a4c",
            "scope_sha": "be3311e71496820cf13256dcee526143e196517255cb1542bea9d35301412ee6",
            "evidence_kind": "INLINE_CANON",
            "location": "inline",
            "evidence_sha": "be3311e71496820cf13256dcee526143e196517255cb1542bea9d35301412ee6",
            "hash_mode": "registry-scope-sha256-v1",
            "architecture": "none",
            "scope_markers": (
                "convergence here means agreement of the two typed routes",
                "not a continuum limit",
                "no Lorentz invariance",
                "physical-photon conclusion",
            ),
        },
        "PHOTON-MASSLESS-PHASE": {
            "status": "O",
            "item_type": "OBLIGATION",
            "layer": "MULTI",
            "gate_ids": "GATE-L4-L6-PHOTON-MASSLESS-PHASE",
            "row_sha": "387d2f49e94f2b27a9a74f910d65f6feb34a8c2e0bc91f0b60c8364874309a4e",
            "scope_sha": "0a65f92a89de6cfc15080d3dfca601f7cf371b8de5b8c783dd0f23e83ef52add",
            "evidence_kind": "INLINE_CANON",
            "location": "inline",
            "evidence_sha": "0a65f92a89de6cfc15080d3dfca601f7cf371b8de5b8c783dd0f23e83ef52add",
            "hash_mode": "registry-scope-sha256-v1",
            "architecture": "none",
            "scope_markers": (
                "complete theorem-preserving comparison with explicit constants",
                "finite-volume configuration space and action",
                "no roughening slogan",
                "uncited Froehlich-Spencer import",
                "physical-photon conclusion",
            ),
        },
    }
    v72_current_contract = {
        claim: contract for claim, contract in v72_contract.items()
        if claim != "PHOTON-CONE-CONVERGENCE"
    }
    v72_dependencies = {
        "FCC-WEIGHTED-SHELL-SYMBOL": set(),
        "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP": {
            ("PHOTON-WINDOW-COORDINATES", "REQUIRES"),
        },
        "PHOTON-MASSLESS-PHASE": {
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            ("PHOTON-WINDOW-COORDINATES", "REQUIRES"),
            (
                "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP",
                "BOUNDED_BY",
            ),
        },
    }
    v72_dependency_hashes = {
        ("PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP", "PHOTON-WINDOW-COORDINATES", "REQUIRES"): "ba3ec189da893464ac7fb1b579abd73fad28760bbf0d80e85363d3f939d2a189",
        ("PHOTON-MASSLESS-PHASE", "DEF-ACTION-LAYERS", "REQUIRES"): "5a205f0cb5e04826724742c39e59c521126cd0b3527b5e44519915a2ecc116f7",
        ("PHOTON-MASSLESS-PHASE", "PHOTON-WINDOW-COORDINATES", "REQUIRES"): "ba559c1dd1a9b6e4879e61df82fc067be6c6045aa753ba5d341a1524ea9df66d",
        ("PHOTON-MASSLESS-PHASE", "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP", "BOUNDED_BY"): "898d9103e3f4a17b53b8888f33eeaaba959bb313d39989c0692e51110dea958d",
    }
    v72_gate_contract = {
        "GATE-L4-L5-PHOTON-CONE-IDENTIFICATION": {
            "owner": "PHOTON-CONE-CONVERGENCE",
            "source": "L4",
            "target": "L5",
            "markers": ("exact equality of null sets", "otherwise STOP"),
            "row_sha": "324b9bf5abdbb44539a0f4e4dec1d0a239a8885cfba4c38fd4c65010be21ea63",
        },
        "GATE-L4-L6-PHOTON-MASSLESS-PHASE": {
            "owner": "PHOTON-MASSLESS-PHASE",
            "source": "L4",
            "target": "L6",
            "markers": (
                "thermodynamic limit",
                "named L6 massless observable",
                "otherwise STOP",
            ),
            "row_sha": "68a9c49f82e039e09e5cdd99ffb7d0e5dce62d842d5eefaeb77ae7cb2cbbdb35",
        },
    }
    v72_history_hashes = {
        "FCC-WEIGHTED-SHELL-SYMBOL": "fee15622899178ea188a5879e5e33fb85bf4ebb8924a69371194ce0d8756d3c5",
        "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP": "dbf27e54507911a3ad6ed37a3ab9601d9f8b6f92747ba3a2f64634108e962522",
        "PHOTON-CONE-CONVERGENCE": "3e2d6aca42d3d5aad7072260e72ff280f2de61897e1b26fe62edce8ce5cca0f9",
        "PHOTON-MASSLESS-PHASE": "7e92caff74858a8d54c69de86eeb0bdf73f8bca4cdd41e9662fe2b6a8c1a03ac",
    }
    v72_claims = tuple(v72_contract)
    v72_history_rows = [
        row for row in history if row["release"] == "canon-v72-candidate"
    ]
    v72_events = {row["claim_id"]: row for row in v72_history_rows}
    v72_actual_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in v72_current_contract
    }
    v72_actual_dependency_hashes = {
        (row["item_id"], row["depends_on"], row["relation"]): table_row_sha256(row)
        for row in dependencies if row["item_id"] in v72_current_contract
    }
    v72_expected_consumers = {
        "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP": {
            ("PHOTON-MASSLESS-PHASE", "BOUNDED_BY"),
        },
        "PHOTON-MASSLESS-PHASE": set(),
    }
    v72_actual_consumers = {
        claim: {
            (row["item_id"], row["relation"])
            for row in dependencies if row["depends_on"] == claim
        }
        for claim in v72_expected_consumers
    }
    v72_photon_gate_ids = set(v72_gate_contract)
    v72_owned_gate_ids = {
        gate_id for gate_id, row in gates.items()
        if row["owner_item_id"] in v72_claims
    }
    v72_canon_start = canon_text.find("### FCC-WEIGHTED-SHELL-SYMBOL [T]")
    v72_canon_end = (
        canon_text.find("### Photon successor roots", v72_canon_start)
        if v72_canon_start >= 0 else -1
    )
    v72_canon_block = (
        canon_text[v72_canon_start:v72_canon_end]
        if v72_canon_start >= 0 and v72_canon_end >= 0 else ""
    )
    checks.append((
        "V72-PHOTON",
        "the v72 boundary theorems and declarations remain pinned while the "
        "Herm2-cone and massless routes stay O/STOP",
        all(
            has_status(index, claim, contract["status"])
            and scope_sha256(index, claim) == contract["scope_sha"]
            and registry_row_sha256(index, claim) == contract["row_sha"]
            and index[claim]["canon_section"] == "9. The photon and the electron"
            and scope_contains_all(index, claim, contract["scope_markers"])
            and normative[claim]["item_type"] == contract["item_type"]
            and normative[claim]["claim_id"] == claim
            and normative[claim]["status"] == contract["status"]
            and normative[claim]["layer"] == contract["layer"]
            and normative[claim]["gate_ids"] == contract["gate_ids"]
            and normative[claim]["statement_source"] == "canon/CANON.md::9. The photon and the electron"
            and evidence[claim]["evidence_id"] == "EV-" + claim
            and evidence[claim]["evidence_kind"] == contract["evidence_kind"]
            and evidence[claim]["location"] == contract["location"]
            and evidence[claim]["sha256"] == contract["evidence_sha"]
            and evidence[claim]["hash_mode"] == contract["hash_mode"]
            and evidence[claim]["architecture_requirement"]
            == contract["architecture"]
            for claim, contract in v72_current_contract.items()
        )
        and v72_actual_dependencies == v72_dependencies
        and v72_actual_dependency_hashes == v72_dependency_hashes
        and v72_actual_consumers == v72_expected_consumers
        and len(v72_history_rows) == 4
        and set(v72_events) == set(v72_claims)
        and all(
            v72_events[claim]["event_id"] == f"CANON72-DECLARE-{claim}"
            and v72_events[claim]["event_sequence"] == "1"
            and v72_events[claim]["event_date"] == "2026-08-30"
            and v72_events[claim]["event_type"] == "DECLARE"
            and v72_events[claim]["previous_status"] == "-"
            and v72_events[claim]["new_status"] == contract["status"]
            and v72_events[claim]["scope_sha256"] == contract["scope_sha"]
            and v72_events[claim]["evidence_id"] == "EV-" + claim
            and v72_events[claim]["evidence_location"] == contract["location"]
            and v72_events[claim]["evidence_sha256"]
            == contract["evidence_sha"]
            and table_row_sha256(v72_events[claim]) == v72_history_hashes[claim]
            for claim, contract in v72_contract.items()
        )
        and v72_owned_gate_ids == v72_photon_gate_ids
        and all(
            gate_id in gates
            and gates[gate_id]["owner_item_id"] == contract["owner"]
            and gates[gate_id]["from_layer"] == contract["source"]
            and gates[gate_id]["to_layer"] == contract["target"]
            and gates[gate_id]["gate_kind"] == "OPEN_LIFT"
            and table_row_sha256(gates[gate_id]) == contract["row_sha"]
            and all(
                marker.lower() in gates[gate_id]["decision_condition"].lower()
                for marker in contract["markers"]
            )
            for gate_id, contract in v72_gate_contract.items()
        )
        and programs.get("PHOTON-CONE-CONVERGENCE") == {
            "claim_id": "PHOTON-CONE-CONVERGENCE",
            "program_id": "PHOTON_CONTINUUM",
            "queue_role": "ROOT",
            "work_state": "STOP",
            "work_mode": "FORMAL",
        }
        and programs.get("PHOTON-MASSLESS-PHASE") == {
            "claim_id": "PHOTON-MASSLESS-PHASE",
            "program_id": "PHOTON_CONTINUUM",
            "queue_role": "ROOT",
            "work_state": "STOP",
            "work_mode": "FORMAL",
        }
        and "FCC-WEIGHTED-SHELL-SYMBOL" not in programs
        and "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP" not in programs
        and f"- PHOTON-CONE-CONVERGENCE [O]:" in frontier_text
        and f"- PHOTON-MASSLESS-PHASE [O]:" in frontier_text
        and f"- FCC-WEIGHTED-SHELL-SYMBOL [" not in frontier_text
        and (
            f"- PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP ["
            not in frontier_text
        )
        and all(row["claim_id"] not in v72_claims for row in core_selection_rows)
        and all(f"- {claim} [" not in core_text for claim in v72_claims)
        and len(v72_canon_block.encode("utf-8")) == 2740
        and hashlib.sha256(v72_canon_block.encode("utf-8")).hexdigest()
        == "dcb94cbfd9283e371a1c9904f5f8d84541bcc2dc48081a547dfa7bf43ccd3fd0"
        and all(
            phrase in canon_text
            for phrase in (
                "This is one displayed L2 scalar symbol. It does not select the FCC carrier,",
                "This is direct finite-coupling nonmembership only.",
                "It proves no Gibbs state, thermodynamic",
                "The preceding theorems do not repair or reopen `PHOTON-KAPPA-LEMMA [F]`",
                "Wilson/Villain nonmembership theorem is boundary information only; it is not",
                "Both successor roots are `ROOT / STOP / FORMAL`.",
                "Neither adopts a roughening",
                "an uncited Froehlich-Spencer import, Lorentz invariance, a continuum",
                "physical readout or a physical photon.",
            )
        )
        and has_status(index, "PHOTON-KAPPA-LEMMA", "F")
        and has_status(index, "PHOTON-WINDOW-PROOF", "F")
        and "PHOTON-KAPPA-LEMMA" not in programs
        and "PHOTON-WINDOW-PROOF" not in programs
        and all(
            all("ROUGHEN" not in claim_id for claim_id in collection)
            for collection in (index, normative, evidence, programs)
        )
        and all(
            "ROUGHEN" not in row["item_id"]
            and "ROUGHEN" not in row["depends_on"]
            for row in dependencies
        ),
    ))

    v73_contract = {
        "C8-MARKING-RIGIDITY": {
            "status": "T",
            "item_type": "THEOREM",
            "layer": "L1",
            "section": "3. The kernel and the census",
            "row_sha": "d341c1696adf64fba058f0b0e931aad1050ec724f51fda391ee2515157308b82",
            "scope_sha": "1de8ab00e9113b12983eb54caae4340d491aad6b614d086376670db6979a8627",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-C8-MARKING-RIGIDITY-2",
            "evidence_sha": "85310f5ac782aed62c976c8ad35be241d8076e48d2b9c6fc91a0e5cce0b7b378",
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "the marking J_lambda=2 is an input and is not derived",
                "no unique C8 generator orientation is selected",
                "relative no-go",
            ),
        },
        "C8-PAULI-QUOTIENT-TRANSPORT": {
            "status": "T",
            "item_type": "THEOREM",
            "layer": "L1",
            "section": "3. The kernel and the census",
            "row_sha": "26358db400f51ca40d3321c867e793a073b66cc230fee9a75008348705a175fb",
            "scope_sha": "2b7897be4bdad094e8a90c82dc9f99b04de2b7408d1b63003057f66e68d11a57",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-C8-PAULI-QUOTIENT-TRANSPORT-1",
            "evidence_sha": "d86f710667b0afe241d8f115325c1c2fd074e27bbd20714891ce9184b221c016",
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "complete transport for one named multiplicative record",
                "not a Born-norm or field embedding",
                "no branch selector, new coordinate, lost component or new physical gauge",
            ),
        },
        "FCC-WEIGHTED-SHELL-REMAINDER": {
            "status": "T",
            "item_type": "THEOREM",
            "layer": "L2",
            "section": "9. The photon and the electron",
            "row_sha": "f22893357599a98ca6b2fc927620cc23559dad731c46957b5a396f6a1be8c749",
            "scope_sha": "648be021804c48838c3156e155d861475ec36371fa4848e7939b1265277009a2",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-FCC-WEIGHTED-SHELL-REMAINDER-1",
            "evidence_sha": "64dd69e762b3bd8be2ebf1f1a4e693e8c70f934beb8151f22e02c10114ecafba",
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "no sharpness claim for the displayed constants",
                "not an architecture-to-physical-continuum lift",
                "are not two photons or two polarizations",
            ),
        },
        "PHOTON-Z5-STAR-QUADRATURE": {
            "status": "C",
            "item_type": "COMPUTATION",
            "layer": "L4",
            "section": "9. The photon and the electron",
            "row_sha": "37a277e979fbb4d1c1424e44e5b71a8c21967796cedc79ed8b987dcdd207d698",
            "scope_sha": "0f3a6cd2a3916d47bc26c65327e9d8dd46ccc0d5c47178ff62ddcd86dd0749f1",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-PHOTON-Z5-STAR-QUADRATURE-1",
            "evidence_sha": "942901869d5296f6d6bdf41423b0fb0d438ac582bf3d582c73fb9a21999aa6a9",
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "theta_star=(82+50 sqrt(5))/361",
                "exactly these five refute the frozen predicate HALF",
                "adopt no L6 probability law",
            ),
        },
    }
    v73_dependencies = {
        "C8-MARKING-RIGIDITY": {
            ("I-BILOCATED", "BOUNDED_BY"),
        },
        "C8-PAULI-QUOTIENT-TRANSPORT": {
            ("C8-BILINEAR-SHADOW", "REQUIRES"),
            ("I-BILOCATED", "BOUNDED_BY"),
        },
        "FCC-WEIGHTED-SHELL-REMAINDER": {
            ("FCC-WEIGHTED-SHELL-SYMBOL", "REQUIRES"),
        },
        "PHOTON-Z5-STAR-QUADRATURE": set(),
    }
    v73_dependency_hashes = {
        ("C8-MARKING-RIGIDITY", "I-BILOCATED", "BOUNDED_BY"): "282225ab1380251e5ee7efa8be5d1fa05ceee0b5ea0d8230225308e26a938a64",
        ("C8-PAULI-QUOTIENT-TRANSPORT", "C8-BILINEAR-SHADOW", "REQUIRES"): "242b8fc98b282b93e216500f5d4d63d0a0f842b738276e44299d7f5b178592c4",
        ("C8-PAULI-QUOTIENT-TRANSPORT", "I-BILOCATED", "BOUNDED_BY"): "7b9462114648b25db6c69a25730eb948e7c721cf26f251fd2cc0016bba5d7bf2",
        ("FCC-WEIGHTED-SHELL-REMAINDER", "FCC-WEIGHTED-SHELL-SYMBOL", "REQUIRES"): "fa3e42047adb81fd43ecc8e2ec843d5b3f4f0ca3ab96836a0a16dbd12d4d3dd9",
    }
    v73_history_hashes = {
        "C8-MARKING-RIGIDITY": "a6613333db41ea9fd1f57b4c312fc6a796397c433fc8258caae08f0ad3967006",
        "C8-PAULI-QUOTIENT-TRANSPORT": "2847f6d1aaa748fa2be11a9b0c5982f38b8aec9f783f16cbd5148460c13ebb51",
        "FCC-WEIGHTED-SHELL-REMAINDER": "9632a74512c5f6590ce37f729ff646f10bb3d75a3158f607abc372e8621a166b",
        "PHOTON-Z5-STAR-QUADRATURE": "a7c3360606a580a25ab36ca5a47ecb36cf1b847f37cf75fdf3bd3d38d64de05c",
    }
    v73_claims = tuple(v73_contract)
    v73_history_rows = [
        row for row in history if row["release"] == "canon-v73-candidate"
    ]
    v73_events = {row["claim_id"]: row for row in v73_history_rows}
    v73_actual_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in v73_claims
    }
    v73_actual_dependency_hashes = {
        (row["item_id"], row["depends_on"], row["relation"]): table_row_sha256(row)
        for row in dependencies if row["item_id"] in v73_claims
    }
    checks.append((
        "V73-FOLD",
        "three proof-first rows and one complete finite classification enter at "
        "their earned status, the C8 marking stays a dictionary input, the "
        "refuted HALF predicate is preserved, and no gate, program or frontier "
        "row moves",
        all(
            has_status(index, claim, contract["status"])
            and scope_sha256(index, claim) == contract["scope_sha"]
            and registry_row_sha256(index, claim) == contract["row_sha"]
            and index[claim]["canon_section"] == contract["section"]
            and scope_contains_all(index, claim, contract["scope_markers"])
            and normative[claim]["item_type"] == contract["item_type"]
            and normative[claim]["claim_id"] == claim
            and normative[claim]["status"] == contract["status"]
            and normative[claim]["layer"] == contract["layer"]
            and normative[claim]["gate_ids"] == ""
            and normative[claim]["statement_source"]
            == "canon/CANON.md::" + contract["section"]
            and evidence[claim]["evidence_id"] == "EV-" + claim
            and evidence[claim]["evidence_kind"] == contract["evidence_kind"]
            and evidence[claim]["location"] == contract["location"]
            and evidence[claim]["sha256"] == contract["evidence_sha"]
            and evidence[claim]["hash_mode"] == contract["hash_mode"]
            and evidence[claim]["architecture_requirement"]
            == contract["architecture"]
            and "### " + claim + " [" + contract["status"] + "]" in canon_text
            for claim, contract in v73_contract.items()
        )
        and v73_actual_dependencies == v73_dependencies
        and v73_actual_dependency_hashes == v73_dependency_hashes
        and len(v73_history_rows) == 4
        and set(v73_events) == set(v73_claims)
        and all(
            v73_events[claim]["event_id"] == "CANON73-DECLARE-" + claim
            and v73_events[claim]["event_sequence"] == "1"
            and v73_events[claim]["event_date"] == "2026-08-31"
            and v73_events[claim]["event_type"] == "DECLARE"
            and v73_events[claim]["previous_status"] == "-"
            and v73_events[claim]["new_status"] == contract["status"]
            and v73_events[claim]["scope_sha256"] == contract["scope_sha"]
            and v73_events[claim]["evidence_id"] == "EV-" + claim
            and v73_events[claim]["evidence_location"] == contract["location"]
            and v73_events[claim]["evidence_sha256"] == contract["evidence_sha"]
            and table_row_sha256(v73_events[claim]) == v73_history_hashes[claim]
            for claim, contract in v73_contract.items()
        )
        and not any(
            row["owner_item_id"] in v73_claims for row in gates.values()
        )
        and all(claim not in programs for claim in v73_claims)
        and all("- " + claim + " [" not in frontier_text for claim in v73_claims)
        and has_status(index, "I-BILOCATED", "D")
        and has_status(index, "C8-BILINEAR-SHADOW", "T")
        and has_status(index, "FCC-WEIGHTED-SHELL-SYMBOL", "T")
        and has_status(index, "PHOTON-CONE-CONVERGENCE", "O")
        and has_status(index, "PHOTON-MASSLESS-PHASE", "O")
        and has_status(index, "PHOTON-KAPPA-LEMMA", "F")
        and has_status(index, "PHOTON-WINDOW-PROOF", "F")
    ))

    v74_bundle = (
        "5216488c404111736d9e6d4d60b81ff52ae36791f693c21bf7d99dc6b4e035f3"
    )
    v74_contract = {
        "PHOTON-SPATIAL-TEMPORAL-TRANSFER": {
            "status": "D",
            "item_type": "DICTIONARY",
            "layer": "MULTI",
            "gate_ids": "GATE-L2-L5-PHOTON-TEMPORAL-CHARACTERISTIC",
            "row_sha": "77976e84dde6735e836e1e8bdcbfba42a3a028d2dbdc37539319427aed482474",
            "scope_sha": "e916ffddedaffad5ed980436438481e4fbfd5254e5011276432551db2e9b0a6e",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1",
            "evidence_sha": v74_bundle,
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "owner-adopted L2-to-L5 dictionary",
                "(a,b)=(-2,1)",
                "claims no completeness or uniqueness outside the displayed class",
                "SI speed",
                "physical photon",
            ),
        },
        "PHOTON-TEMPORAL-CHARACTERISTIC": {
            "status": "T",
            "item_type": "THEOREM",
            "layer": "L5",
            "gate_ids": "",
            "row_sha": "33eb50d4ea884fef565ff376f8750425a967579beeb6c371ba3cd968595f1424",
            "scope_sha": "626c8fd13d05da7180f9ddcf05e57b52a840074bb1d68998f2ce265656207c3c",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1",
            "evidence_sha": v74_bundle,
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "total exact characteristic",
                "reciprocal conjugate unit-modulus multipliers",
                "uniformly on bounded lifted sets",
                "unit phases rather than contraction/expansion amplitudes",
                "Herm2 carrier",
                "physical photon",
            ),
        },
        "PHOTON-CONE-CONVERGENCE": {
            "status": "O",
            "item_type": "OBLIGATION",
            "layer": "MULTI",
            "gate_ids": "GATE-L4-L5-PHOTON-CONE-IDENTIFICATION",
            "row_sha": "448d04f1dfdec5090b0ef962a14e32aa97cb72ca8be735b75ab225a2c265854c",
            "scope_sha": "f67b713037517aac2a0f2ca119b7f7176e0c49f6ad4414031353cd67c9577853",
            "evidence_kind": "INLINE_CANON",
            "location": "inline",
            "evidence_sha": "f67b713037517aac2a0f2ca119b7f7176e0c49f6ad4414031353cd67c9577853",
            "hash_mode": "registry-scope-sha256-v1",
            "architecture": "none",
            "scope_markers": (
                "remaining open MULTI decision after the L2-to-L5 route is fixed",
                "separately public L4 Herm2 quadratic carrier",
                "not characteristic-function convergence",
                "no Lorentz invariance",
                "physical-photon conclusion",
            ),
        },
    }
    v74_dependencies = {
        "PHOTON-SPATIAL-TEMPORAL-TRANSFER": {
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            ("FCC-WEIGHTED-SHELL-SYMBOL", "REQUIRES"),
            ("FCC-WEIGHTED-SHELL-REMAINDER", "REQUIRES"),
        },
        "PHOTON-TEMPORAL-CHARACTERISTIC": {
            ("PHOTON-SPATIAL-TEMPORAL-TRANSFER", "BOUNDED_BY"),
        },
        "PHOTON-CONE-CONVERGENCE": {
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            ("CENTRAL-LIFT-PHASE", "BOUNDED_BY"),
            ("PHOTON-SPATIAL-TEMPORAL-TRANSFER", "REQUIRES"),
            ("PHOTON-TEMPORAL-CHARACTERISTIC", "REQUIRES"),
        },
    }
    v74_dependency_hashes = {
        ("PHOTON-SPATIAL-TEMPORAL-TRANSFER", "DEF-ACTION-LAYERS", "REQUIRES"):
            "53493f4ac821a8a456fc075f17fe5fe2b50f6d0d400c9d45db8e83acb4f90b03",
        ("PHOTON-SPATIAL-TEMPORAL-TRANSFER", "FCC-WEIGHTED-SHELL-SYMBOL", "REQUIRES"):
            "81660bd76e84a9ecda54055acfc894564529fcf69d971188b0d71e6eb0d28c1c",
        ("PHOTON-SPATIAL-TEMPORAL-TRANSFER", "FCC-WEIGHTED-SHELL-REMAINDER", "REQUIRES"):
            "0ba4d0fe90d4d1d6f5c00c5c1b493d80c97e0fc58366a881d68a49e0d05e7453",
        ("PHOTON-TEMPORAL-CHARACTERISTIC", "PHOTON-SPATIAL-TEMPORAL-TRANSFER", "BOUNDED_BY"):
            "748aab7ab1efbc50cf12fe28c21917d183b7a10d483bf554bfab0202510263a7",
        ("PHOTON-CONE-CONVERGENCE", "DEF-ACTION-LAYERS", "REQUIRES"):
            "4bd6904d69bdb26a28fdaa500e0a8183cce88f603174400904bf57e398b35849",
        ("PHOTON-CONE-CONVERGENCE", "CENTRAL-LIFT-PHASE", "BOUNDED_BY"):
            "0f5cf0861f55dbe6ba17ca92dbebad344ece685bdd1fba2eb8e44710a3fd573e",
        ("PHOTON-CONE-CONVERGENCE", "PHOTON-SPATIAL-TEMPORAL-TRANSFER", "REQUIRES"):
            "84fc6f9c21f0ca9ba369693a6e8dce02ba13c91f8087ed8bdfef1dae4dc26d88",
        ("PHOTON-CONE-CONVERGENCE", "PHOTON-TEMPORAL-CHARACTERISTIC", "REQUIRES"):
            "0e570e01ecf4de0a817614223895e6980f8b739b630c31c55eeaccdaa97ce3c2",
    }
    v74_expected_consumers = {
        "FCC-WEIGHTED-SHELL-SYMBOL": {
            ("FCC-WEIGHTED-SHELL-REMAINDER", "REQUIRES"),
            ("PHOTON-SPATIAL-TEMPORAL-TRANSFER", "REQUIRES"),
        },
        "FCC-WEIGHTED-SHELL-REMAINDER": {
            ("PHOTON-SPATIAL-TEMPORAL-TRANSFER", "REQUIRES"),
        },
        "PHOTON-SPATIAL-TEMPORAL-TRANSFER": {
            ("PHOTON-TEMPORAL-CHARACTERISTIC", "BOUNDED_BY"),
            ("PHOTON-CONE-CONVERGENCE", "REQUIRES"),
        },
        "PHOTON-TEMPORAL-CHARACTERISTIC": {
            ("PHOTON-CONE-CONVERGENCE", "REQUIRES"),
        },
        "PHOTON-CONE-CONVERGENCE": set(),
    }
    v74_actual_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in v74_contract
    }
    v74_actual_dependency_hashes = {
        (row["item_id"], row["depends_on"], row["relation"]):
            table_row_sha256(row)
        for row in dependencies if row["item_id"] in v74_contract
    }
    v74_actual_consumers = {
        claim: {
            (row["item_id"], row["relation"])
            for row in dependencies if row["depends_on"] == claim
        }
        for claim in v74_expected_consumers
    }
    v74_history_rows = [
        row for row in history if row["release"] == "canon-v74-candidate"
    ]
    v74_history_by_event = {
        row["event_id"]: row for row in v74_history_rows
    }
    v74_history_contract = {
        "CANON74-DECLARE-PHOTON-SPATIAL-TEMPORAL-TRANSFER": {
            "claim": "PHOTON-SPATIAL-TEMPORAL-TRANSFER",
            "sequence": "1", "type": "DECLARE", "previous": "-", "new": "D",
            "scope": "e916ffddedaffad5ed980436438481e4fbfd5254e5011276432551db2e9b0a6e",
            "evidence": "EV-PHOTON-SPATIAL-TEMPORAL-TRANSFER",
            "location": "probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1",
            "evidence_sha": v74_bundle,
            "row_sha": "30c6733f64f5115f7a9bc07435c79424d5ca92d875b953eb46b0a85e7027d826",
        },
        "CANON74-DECLARE-PHOTON-TEMPORAL-CHARACTERISTIC": {
            "claim": "PHOTON-TEMPORAL-CHARACTERISTIC",
            "sequence": "1", "type": "DECLARE", "previous": "-", "new": "T",
            "scope": "626c8fd13d05da7180f9ddcf05e57b52a840074bb1d68998f2ce265656207c3c",
            "evidence": "EV-PHOTON-TEMPORAL-CHARACTERISTIC",
            "location": "probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1",
            "evidence_sha": v74_bundle,
            "row_sha": "e999bf6e3a6fb8a33858e06711c15b9cf1523e7cebfd814f935a3f6a0b4f5df0",
        },
        "CANON74-SCOPE-PHOTON-CONE-CONVERGENCE": {
            "claim": "PHOTON-CONE-CONVERGENCE",
            "sequence": "2", "type": "SCOPE_CHANGE", "previous": "O", "new": "O",
            "scope": "f67b713037517aac2a0f2ca119b7f7176e0c49f6ad4414031353cd67c9577853",
            "evidence": "EV-PHOTON-CONE-CONVERGENCE",
            "location": "inline",
            "evidence_sha": "f67b713037517aac2a0f2ca119b7f7176e0c49f6ad4414031353cd67c9577853",
            "row_sha": "1156887c7abfb280fd615d32f972e00a5fb2ffd54cda4086786fdcab5294ff16",
        },
    }
    v74_gate_contract = {
        "GATE-L2-L5-PHOTON-TEMPORAL-CHARACTERISTIC": {
            "owner": "PHOTON-SPATIAL-TEMPORAL-TRANSFER",
            "source": "L2", "target": "L5", "kind": "DICTIONARY_LIFT",
            "markers": ("closed at status D", "supported by", "no Herm2 carrier"),
            "row_sha": "14e3328125b6b1dd653b697178ecd1320c1923434d787b21b381a9613937c74d",
        },
        "GATE-L4-L5-PHOTON-CONE-IDENTIFICATION": {
            "owner": "PHOTON-CONE-CONVERGENCE",
            "source": "L4", "target": "L5", "kind": "OPEN_LIFT",
            "markers": ("exact equality of null sets", "otherwise STOP"),
            "row_sha": "324b9bf5abdbb44539a0f4e4dec1d0a239a8885cfba4c38fd4c65010be21ea63",
        },
    }
    v74_dt_start = canon_text.find(
        "### PHOTON-SPATIAL-TEMPORAL-TRANSFER [D]"
    )
    v74_dt_end = canon_text.find(
        "### PHOTON-Z5-STAR-QUADRATURE [C]", v74_dt_start
    )
    v74_dt_block = (
        canon_text[v74_dt_start:v74_dt_end]
        if v74_dt_start >= 0 and v74_dt_end >= 0 else ""
    )
    v74_successor_start = canon_text.find("### Photon successor roots")
    v74_successor_end = canon_text.find(
        "The electron:", v74_successor_start
    )
    v74_successor_block = (
        canon_text[v74_successor_start:v74_successor_end]
        if v74_successor_start >= 0 and v74_successor_end >= 0 else ""
    )
    checks.append((
        "V74-PHOTON",
        "selected D3 transfer enters at D/MULTI and its exact characteristic "
        "at T/L5, closing only the L2-to-L5 dictionary lift while the Herm2 "
        "cone route stays O/STOP",
        all(
            has_status(index, claim, contract["status"])
            and scope_sha256(index, claim) == contract["scope_sha"]
            and registry_row_sha256(index, claim) == contract["row_sha"]
            and index[claim]["canon_section"] == "9. The photon and the electron"
            and scope_contains_all(index, claim, contract["scope_markers"])
            and normative[claim]["item_type"] == contract["item_type"]
            and normative[claim]["claim_id"] == claim
            and normative[claim]["status"] == contract["status"]
            and normative[claim]["layer"] == contract["layer"]
            and normative[claim]["gate_ids"] == contract["gate_ids"]
            and normative[claim]["statement_source"]
            == "canon/CANON.md::9. The photon and the electron"
            and evidence[claim]["evidence_id"] == "EV-" + claim
            and evidence[claim]["evidence_kind"] == contract["evidence_kind"]
            and evidence[claim]["location"] == contract["location"]
            and evidence[claim]["sha256"] == contract["evidence_sha"]
            and evidence[claim]["hash_mode"] == contract["hash_mode"]
            and evidence[claim]["architecture_requirement"]
            == contract["architecture"]
            for claim, contract in v74_contract.items()
        )
        and v74_actual_dependencies == v74_dependencies
        and v74_actual_dependency_hashes == v74_dependency_hashes
        and v74_actual_consumers == v74_expected_consumers
        and len(v74_history_rows) == 3
        and set(v74_history_by_event) == set(v74_history_contract)
        and all(
            v74_history_by_event[event_id]["claim_id"] == contract["claim"]
            and v74_history_by_event[event_id]["event_sequence"]
            == contract["sequence"]
            and v74_history_by_event[event_id]["event_date"] == "2026-09-01"
            and v74_history_by_event[event_id]["event_type"] == contract["type"]
            and v74_history_by_event[event_id]["previous_status"]
            == contract["previous"]
            and v74_history_by_event[event_id]["new_status"] == contract["new"]
            and v74_history_by_event[event_id]["scope_sha256"] == contract["scope"]
            and v74_history_by_event[event_id]["evidence_id"]
            == contract["evidence"]
            and v74_history_by_event[event_id]["evidence_location"]
            == contract["location"]
            and v74_history_by_event[event_id]["evidence_sha256"]
            == contract["evidence_sha"]
            and table_row_sha256(v74_history_by_event[event_id])
            == contract["row_sha"]
            for event_id, contract in v74_history_contract.items()
        )
        and all(
            gate_id in gates
            and gates[gate_id]["owner_item_id"] == contract["owner"]
            and gates[gate_id]["from_layer"] == contract["source"]
            and gates[gate_id]["to_layer"] == contract["target"]
            and gates[gate_id]["gate_kind"] == contract["kind"]
            and table_row_sha256(gates[gate_id]) == contract["row_sha"]
            and all(
                marker.lower() in gates[gate_id]["decision_condition"].lower()
                for marker in contract["markers"]
            )
            for gate_id, contract in v74_gate_contract.items()
        )
        and sum(row["gate_kind"] == "OPEN_LIFT" for row in gates.values()) == 7
        and sum(
            row["gate_kind"] == "DICTIONARY_LIFT" for row in gates.values()
        ) == 3
        and programs.get("PHOTON-CONE-CONVERGENCE") == {
            "claim_id": "PHOTON-CONE-CONVERGENCE",
            "program_id": "PHOTON_CONTINUUM",
            "queue_role": "ROOT",
            "work_state": "STOP",
            "work_mode": "FORMAL",
        }
        and all(
            claim not in programs
            for claim in (
                "PHOTON-SPATIAL-TEMPORAL-TRANSFER",
                "PHOTON-TEMPORAL-CHARACTERISTIC",
            )
        )
        and "- PHOTON-CONE-CONVERGENCE [O]:" in frontier_text
        and all(
            "- " + claim + " [" not in frontier_text
            and "- " + claim + " [" not in core_text
            and all(row["claim_id"] != claim for row in core_selection_rows)
            for claim in (
                "PHOTON-SPATIAL-TEMPORAL-TRANSFER",
                "PHOTON-TEMPORAL-CHARACTERISTIC",
            )
        )
        and has_status(index, "PHOTON-MASSLESS-PHASE", "O")
        and len(v74_dt_block.encode("utf-8")) == 4216
        and hashlib.sha256(v74_dt_block.encode("utf-8")).hexdigest()
        == "04de7998932b896c0a62a9c9d7e1a29e31a2e5ce3c37f23d2b3e56e64428ad2d"
        and len(v74_successor_block.encode("utf-8")) == 2198
        and hashlib.sha256(v74_successor_block.encode("utf-8")).hexdigest()
        == "112b95be0baeff5bbee514c9ee2ca0a0f396634881766bdb6f8ffd20e37415ca"
        and all(
            phrase in canon_text
            for phrase in (
                "The L2-to-L5 temporal-characteristic gate is\ntherefore closed positively as a dictionary lift.",
                "The L4-to-L5 identification gate therefore remains `OPEN_LIFT`.",
                "unit-modulus phases; they are not a\ncontraction/expansion pair",
                "No Herm2 carrier, positive cone,\nBorn rule",
                "interpretation is neither assumed nor refuted.",
            )
        )
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
