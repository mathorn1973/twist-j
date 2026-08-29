#!/usr/bin/env python3
"""Deterministic, non-formal conformance check for the v70 successor manifest."""

from __future__ import annotations

import csv
import hashlib
import io
import json
from collections import Counter
from pathlib import Path
import subprocess
import sys


PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
MANIFEST_PATH = PACKAGE / "MANIFEST.json"


class CheckError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_bytes(*args: str) -> bytes:
    completed = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise CheckError(f"git {' '.join(args)} failed: {detail}")
    return completed.stdout


def git_blob(commit: str, path: str) -> bytes:
    return git_bytes("show", f"{commit}:{path}")


def rows(blob: bytes) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(blob.decode("utf-8")), delimiter="\t"))


def by_id(items: list[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
    return {item[key]: item for item in items}


def status_fields(blob: bytes) -> dict[str, str]:
    result: dict[str, str] = {}
    for raw in blob.decode("utf-8").splitlines():
        if ":" in raw:
            key, value = raw.split(":", 1)
            if key and key == key.upper():
                result[key] = value.strip()
    return result


def git_tree_paths(commit: str, path: str) -> list[str]:
    output = git_bytes("ls-tree", "-r", "--name-only", "-z", commit, "--", path)
    return sorted(item for item in output.decode("utf-8").split("\0") if item)


def git_bundle_sha256(commit: str, path: str) -> str:
    lines: list[str] = []
    for relative in git_tree_paths(commit, path):
        relative_parts = Path(relative).relative_to(path).parts
        if (
            "__pycache__" in relative_parts
            or Path(relative).suffix == ".pyc"
            or "RUNS" in relative_parts
        ):
            continue
        lines.append(f"{sha256(git_blob(commit, relative))}  {relative}\n")
    return sha256("".join(lines).encode("utf-8"))


def assert_acyclic(edges: list[tuple[str, str]]) -> None:
    graph: dict[str, set[str]] = {}
    nodes: set[str] = set()
    for parent, child in edges:
        graph.setdefault(parent, set()).add(child)
        nodes.update((parent, child))
    state: dict[str, int] = {}

    def visit(node: str) -> None:
        mark = state.get(node, 0)
        if mark == 1:
            raise CheckError(f"prospective dependency cycle reaches {node}")
        if mark == 2:
            return
        state[node] = 1
        for child in sorted(graph.get(node, ())):
            visit(child)
        state[node] = 2

    for node in sorted(nodes):
        visit(node)


def main() -> None:
    manifest_text = MANIFEST_PATH.read_text(encoding="utf-8")

    def reject_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in pairs:
            if key in result:
                raise CheckError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    manifest = json.loads(manifest_text, object_pairs_hook=reject_duplicates)
    base = manifest["authority"]["public_main_base"]
    expected_top = {
        "manifest_format",
        "artifact",
        "authority",
        "immutable_predecessors",
        "owner_choice",
        "lifecycle",
        "successor_contract",
        "apparatus_transfer",
        "ledger_transaction",
        "target_count_contract",
        "release_transaction",
        "invalid_conditions",
    }
    require(set(manifest) == expected_top, "manifest top-level schema drift")
    require(
        {item.name for item in PACKAGE.iterdir() if item.is_file()}
        == {"MANIFEST.json", "README.md", "verify.py", "EXPECTED.txt"},
        "package must contain exactly four files",
    )
    require(
        manifest["manifest_format"]
        == "TWISTJ_QDD_ALGEBRAIC_DMATTER_SUCCESSOR_1",
        "wrong manifest format",
    )
    require(
        manifest_text == json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        "MANIFEST.json is not canonical two-space JSON with one final newline",
    )
    artifact = manifest["artifact"]
    require(
        artifact
        == {
            "status": "NON-CANONICAL_SUCCESSOR_MANIFEST",
            "authority": "NOT_CANON",
            "formal_run": "NONE",
            "scientific_result": "NONE",
            "scientific_credit": "NONE",
            "transaction": "NOTES_ONLY_MANIFEST",
            "normative_change": "NONE",
            "decoder_completion_candidate_submitted": False,
            "full_completion_contract_conformance_claimed": False,
            "whole_decoder_completion": False,
            "authorized_next_transaction": "SEPARATE_PUBLIC_CANON_V70_RELEASE",
        },
        "artifact boundary drift",
    )
    print("PASS 01 PACKAGE    exact four-file notes-only, non-formal manifest package")

    authority = manifest["authority"]
    require(base == "6e3d54576d9348eadac7fedfcc87adbe6c3e3811", "base pin drift")
    status = status_fields(git_blob(base, "STATUS.md"))
    require(status["STATE"] == "ACTIVE", "base is not ACTIVE")
    require(status["CANON"] == authority["public_canon"], "Canon label mismatch")
    require(status["TAG"] == authority["public_canon_tag"], "tag declaration mismatch")
    require(status["CONTENT_COMMIT"] == authority["content_commit"], "content pin mismatch")
    require(status["CANON_SHA256"] == authority["canon_sha256"], "status Canon hash mismatch")
    require(int(status["CANON_BYTES"]) == authority["canon_bytes"], "status Canon size mismatch")
    canon_blob = git_blob(base, "canon/CANON.md")
    require(sha256(canon_blob) == authority["canon_sha256"], "base Canon hash mismatch")
    require(len(canon_blob) == authority["canon_bytes"], "base Canon size mismatch")
    tag_commit = git_bytes("rev-parse", f"{authority['public_canon_tag']}^{{commit}}")
    require(tag_commit.decode().strip() == authority["activation_commit"], "tag target mismatch")
    for older, newer in (
        (authority["content_commit"], authority["activation_commit"]),
        (authority["activation_commit"], base),
    ):
        completed = subprocess.run(
            ["git", "merge-base", "--is-ancestor", older, newer],
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        require(completed.returncode == 0, f"authority ancestry fails: {older} -> {newer}")
    require(authority["required_check_conclusion"] == "success", "required check not pinned green")
    require(authority["required_check_run_id"] == 33244056058, "required check run drift")
    require(authority["owner_choice_pr"] == 648, "owner-choice PR drift")
    completed = subprocess.run(
        ["git", "merge-base", "--is-ancestor", base, "HEAD"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(completed.returncode == 0, "frozen public base is not an ancestor of HEAD")
    print("PASS 02 AUTHORITY  v69 content, activation, tag, Canon bytes and main base agree")

    owner_blob = git_blob(base, authority["owner_note_path"])
    require(sha256(owner_blob) == authority["owner_note_sha256"], "owner note hash mismatch")
    require(len(owner_blob) == authority["owner_note_bytes"], "owner note size mismatch")
    predecessors = manifest["immutable_predecessors"]
    require(len(predecessors) == 5, "predecessor inventory must have five entries")
    for item in predecessors[:3]:
        blob = git_blob(base, item["path"])
        require(sha256(blob) == item["sha256"], f"predecessor hash mismatch: {item['path']}")
        require(len(blob) == item["bytes"], f"predecessor size mismatch: {item['path']}")
        require(item["disposition"] == "PRESERVE_BYTE_EXACT", "old manifest is not byte-frozen")
    for item in predecessors[3:]:
        require(item["hash_mode"] == "bundle-manifest-sha256-v1", "bundle hash mode drift")
        require(git_bundle_sha256(base, item["path"]) == item["sha256"], f"bundle hash mismatch: {item['path']}")
        require(item["disposition"] == "PRESERVE_EVIDENCE_AND_SCOPE", "evidence disposition drift")
    print("PASS 03 PREDECESS old manifests are byte-frozen; theorem bundles stay pinned")

    choice = manifest["owner_choice"]
    require(choice["selected_route"] == "ALGEBRAIC-DMATTER", "selected route drift")
    require(choice["choice_kind"] == "OWNER_ADOPTED_ARCHITECTURE", "choice kind drift")
    require(
        not any(
            choice[key]
            for key in (
                "mathematically_forced",
                "unique",
                "canonical",
                "factorization_selects_route",
                "projector_relative_uniqueness_selects_route",
                "counterroute_public_claim",
                "p_dmatter_total_1_resumed",
                "candidate_identifier_promoted",
            )
        ),
        "owner choice is being redescribed as a theorem or public counterclaim",
    )
    require(
        choice["counterroute_state"] == "UNADOPTED_NOT_FALSIFIED_NOT_SHOWN_COMPLETE",
        "counterroute disposition drift",
    )
    print("PASS 04 CHOICE     ALGEBRAIC-DMATTER is an owner choice, not forced or unique")

    registry = rows(git_blob(base, "canon/REGISTRY.tsv"))
    normative = rows(git_blob(base, "canon/NORMATIVE.tsv"))
    evidence = rows(git_blob(base, "canon/EVIDENCE.tsv"))
    programs = rows(git_blob(base, "canon/FRONTIER_PROGRAMS.tsv"))
    dependencies = rows(git_blob(base, "canon/DEPENDENCIES.tsv"))
    history = rows(git_blob(base, "canon/HISTORY.tsv"))
    gates = rows(git_blob(base, "canon/GATES.tsv"))
    core_selection = rows(git_blob(base, "canon/CORE_SELECTION.tsv"))
    reg = by_id(registry, "claim_id")
    norm = by_id(normative, "item_id")
    ev = by_id(evidence, "claim_id")
    prog = by_id(programs, "claim_id")
    old_id = "QUADRATIC-DECODER-DATA"
    require(reg[old_id]["status"] == "O", "predecessor is not O")
    require(norm[old_id]["item_type"] == "OBLIGATION", "predecessor type drift")
    require(norm[old_id]["status"] == "O" and norm[old_id]["layer"] == "MULTI", "predecessor normative drift")
    require(ev[old_id]["sha256"] == "8b2b79b5060bbea943429afda25f24affcda2bd9a55961965cf63a962b3cee8d", "predecessor evidence drift")
    require(sha256(reg[old_id]["scope"].encode()) == ev[old_id]["sha256"], "predecessor scope hash drift")
    require(
        (prog[old_id]["program_id"], prog[old_id]["queue_role"], prog[old_id]["work_state"], prog[old_id]["work_mode"])
        == ("DECODER_CORE", "ROOT", "STOP", "FORMAL"),
        "predecessor frontier state drift",
    )
    require(reg["QDD-INSTRUMENT-APPARATUS"]["status"] == "O", "apparatus is not O")
    require(prog["QDD-INSTRUMENT-APPARATUS"]["work_state"] == "STOP", "apparatus is not STOP")
    for absent in ("ALGEBRAIC-DMATTER", "PHYSICAL-DMATTER", "QDD-PROJECTOR-APPARATUS"):
        require(absent not in reg and absent not in norm and absent not in ev and absent not in prog, f"unexpected base row: {absent}")
    print("PASS 05 BASE       v69 has composite O/STOP, apparatus O/STOP and no successor row")

    lifecycle = manifest["lifecycle"]
    predecessor = lifecycle["predecessor"]
    require(predecessor["claim_id"] == old_id, "retirement claim drift")
    require(predecessor["action"] == "RETIRE_AS_SPLIT", "retirement action drift")
    require(predecessor["event_type"] == "RETIRE" and predecessor["event_sequence"] == 14, "retirement event drift")
    require(predecessor["new_status"] == "RETIRED", "retirement status drift")
    require(not predecessor["falsifier_fired"] and not predecessor["positive_closure"], "retirement misstates a result")
    require(predecessor["scientific_result"] == "NONE", "retirement claims scientific credit")
    require(predecessor["scope_sha256_to_preserve_in_history"] == ev[old_id]["sha256"], "retirement loses old scope hash")
    successor = lifecycle["successor"]
    require(
        (successor["claim_id"], successor["item_type"], successor["status"], successor["status_ceiling"], successor["layer"])
        == ("ALGEBRAIC-DMATTER", "DICTIONARY", "D", "D", "L1"),
        "successor identity/type/status/layer drift",
    )
    require(successor["gate_ids"] == [] and successor["bridge_manifest"] == [], "successor acquired a gate or bridge")
    require(
        (
            successor["evidence_id"],
            successor["evidence_kind"],
            successor["evidence_location"],
            successor["evidence_sha256"],
            successor["evidence_hash_mode"],
            successor["architecture_requirement"],
        )
        == (
            "EV-ALGEBRAIC-DMATTER",
            "INLINE_CANON",
            "inline",
            "DERIVE_FROM_FINAL_REGISTRY_SCOPE",
            "registry-scope-sha256-v1",
            "none",
        ),
        "successor evidence-row contract drift",
    )
    require(not successor["frontier_program"] and not successor["scientific_promotion"], "dictionary became a frontier promotion")
    physical = lifecycle["physical_owner"]
    require(
        (physical["claim_id"], physical["status"], physical["work_state"], physical["debt_state"])
        == ("QDD-INSTRUMENT-APPARATUS", "O", "STOP", "TRANSFERRED_NOT_SATISFIED"),
        "physical debt disposition drift",
    )
    require(set(lifecycle["forbidden_new_claim_ids"]) == {"PHYSICAL-DMATTER", "QDD-PROJECTOR-APPARATUS"}, "forbidden claim wall drift")
    print("PASS 06 LIFECYCLE  old O retires as split; new D declares; physical debt stays O/STOP")

    contract = manifest["successor_contract"]
    require(
        set(contract)
        == {
            "binding_scope", "binding", "domain_id", "leg_id", "codomain_id",
            "write_map_id", "stage_id", "totality_domain_id", "record_field_manifest",
            "quadratic_manifest", "forbidden_quadratic_manifest_keys",
            "excluded_meanings", "anti_inheritance",
        },
        "successor-contract key schema drift",
    )
    require(contract["binding_scope"] == "K_QDD_AND_D_QUADRATIC_ONLY", "binding scope drift")
    require(
        contract["binding"]
        == "D_matter|_(K_QDD,D_quadratic) := D_QDD_direct : K_QDD -> MatterData_QDD",
        "exact binding drift",
    )
    require(
        (
            contract["domain_id"], contract["leg_id"], contract["codomain_id"],
            contract["write_map_id"], contract["stage_id"], contract["totality_domain_id"],
        )
        == (
            "DEF-QDD-DOMAIN-K0", "D_quadratic", "DEF-QDD-MATTER-RECORD",
            "DEF-QDD-DIRECT-WRITE", "D_matter", "DEF-QDD-DOMAIN-K0",
        ),
        "binding endpoint drift",
    )
    expected_fields = [
        {"field_id": "support_state", "field_type_id": "DEF-QDD-MATTER-RECORD", "field_type_clause": "support_state in {ZERO_SUPPORT, SUPPORTED}", "role": "READOUT", "semantics": "ALGEBRAIC_ONLY", "layer": "L1"},
        {"field_id": "total_weight", "field_type_id": "DEF-QDD-MATTER-RECORD", "field_type_clause": "total_weight in Q_(>=0)", "role": "READOUT", "semantics": "ALGEBRAIC_ONLY", "layer": "L1"},
        {"field_id": "branch_weights", "field_type_id": "DEF-QDD-MATTER-RECORD", "field_type_clause": "ordered (LOW,HIGH) pair in Q_(>=0)^2, no swap", "role": "READOUT", "semantics": "ALGEBRAIC_ONLY", "layer": "L1"},
        {"field_id": "density_state", "field_type_id": "DEF-QDD-MATTER-RECORD", "field_type_clause": "ZERO_DENOMINATOR or DENSITY carrying a 4x4 rational matrix", "role": "READOUT", "semantics": "ALGEBRAIC_ONLY", "layer": "L1"},
        {"field_id": "normalized_weight_state", "field_type_id": "DEF-QDD-MATTER-RECORD", "field_type_clause": "ZERO_DENOMINATOR or NORMALIZED carrying a rational pair", "role": "READOUT", "semantics": "ALGEBRAIC_ONLY", "layer": "L1"},
    ]
    require(contract["record_field_manifest"] == expected_fields, "five-field manifest drift")
    require(
        all(norm[item["field_type_id"]]["item_type"] == "DEFINITION" for item in expected_fields),
        "field type source is not a public definition",
    )
    quadratic = contract["quadratic_manifest"]
    require(
        quadratic
        == {
            "coefficient_ring_id": "DEF-QDD-COEFFICIENT-Q",
            "effective_carrier_id": "DEF-QDD-BALANCED-PISTON",
            "orbit_to_amplitude_bridge_id": "DEF-QDD-AMPLITUDE-B0",
            "gram_id": "DEF-QDD-GRAM",
            "dagger_id": "DEF-QDD-DAGGER",
            "transpose_id": "DEF-QDD-TRANSPOSE",
            "qcarrier_id": "DEF-QDD-QCARRIER-EQUALITY",
            "q_equality_id": "DEF-QDD-QCARRIER-EQUALITY",
            "q_map_id": "DEF-QDD-QPAIR",
            "projector_ids": ["DEF-QDD-PROJECTOR-LOW", "DEF-QDD-PROJECTOR-HIGH"],
            "branch_weight_pairing_id": "DEF-QDD-BRANCH-WEIGHT-PAIRING",
            "factorization_map_id": "DEF-QDD-FACTOR-MAP",
            "slot_boundary_id": "QDD-QCARRIER-DIAGONAL-BOUNDARY",
            "factorization_theorem_id": "QDD-ALGEBRAIC-FACTORIZATION",
        },
        "quadratic manifest drift",
    )
    require(not (set(contract["forbidden_quadratic_manifest_keys"]) & set(quadratic)), "physical legacy slot leaked into algebraic schema")
    require(set(contract["forbidden_quadratic_manifest_keys"]) == {"effect_ids", "born_pairing_id"}, "legacy slot wall drift")
    require(
        set(contract["excluded_meanings"])
        == {
            "PHYSICAL_EFFECT", "APPARATUS", "APPARATUS_COMPLETENESS",
            "REALIZED_EVENT", "OCCURRENCE_LAW", "FREQUENCY", "SAMPLING",
            "RANDOMNESS", "INDEPENDENCE", "POST_STATE_INSTRUMENT",
            "POST_STATE_INSTRUMENT_UNIQUENESS", "L6_MEASURE",
        },
        "algebraic meaning wall drift",
    )
    require(
        set(contract["anti_inheritance"])
        == {
            "K_QDD_EQUALS_K", "DOM_D_MATTER_EQUALS_K",
            "TOTALITY_OUTSIDE_K_QDD_D_QUADRATIC", "WHOLE_DECODER_COMPLETION",
            "OTHER_DECODER_LEG_CLOSURE", "CROSS_LEG_OR_STATE_RECONSTRUCTION",
            "PROJECTORS_DERIVED_FROM_J",
            "BRANCH_WEIGHT_PAIRING_DERIVED_FROM_J",
            "PHYSICAL_EFFECT_SELECTION_OR_APPARATUS_COMPLETENESS",
            "POST_STATE_INSTRUMENT_UNIQUENESS",
            "OCCURRENCE_FREQUENCY_SAMPLING_RANDOMNESS_OR_INDEPENDENCE",
            "L6_MEASURE",
            "PHYSICAL_ROUTE_CANONICITY_OR_UNIQUENESS",
            "CM_OR_PRIMARY_CARRIER_CONSEQUENCE",
            "PSI_CONSEQUENCE", "SEAM_CONSEQUENCE", "WRITEBACK_CONSEQUENCE",
        },
        "anti-inheritance firewall drift",
    )
    print("PASS 07 CONTRACT   exact scoped direct writer, five L1 fields and algebraic schema")

    transfer = manifest["apparatus_transfer"]
    require(
        (transfer["owner_claim_id"], transfer["source_claim_id"], transfer["state"])
        == ("QDD-INSTRUMENT-APPARATUS", old_id, "TRANSFERRED_NOT_SATISFIED"),
        "apparatus transfer drift",
    )
    require(not transfer["algebraic_results_close_apparatus"], "algebraic result closes apparatus")
    apparatus = transfer["apparatus_manifest"]
    expected_apparatus_keys = {
        "projector_target_ids", "effect_ids", "instrument_ids", "apparatus_carrier_id", "ready_state_id",
        "physical_context_key_id", "selected_ready_phase_id", "coupling_id", "pointer_id",
        "reduction_id", "target_comparison_relation_id", "target_comparison_domain_id",
        "complete_apparatus_family_class_id", "apparatus_family_equality_id",
        "phase_equality_id", "target_independence_certificate_id",
        "class_completeness_certificate_id", "realization_certificate_ids",
        "realized_outcome_ids", "realized_event_semantics_id", "occurrence_law_id",
        "post_state_instrument_ids", "persistence_update_reset_law_id",
        "zero_support_semantics_id", "l1_to_l5_gate_id", "l6_measure_boundary",
    }
    require(set(apparatus) == expected_apparatus_keys, "apparatus schema drift")
    for key, value in apparatus.items():
        if key == "projector_target_ids":
            require(value == ["DEF-QDD-PROJECTOR-LOW", "DEF-QDD-PROJECTOR-HIGH"], "apparatus target order drift")
            continue
        if key == "l6_measure_boundary":
            require(value == "REQUIRES_SEPARATE_GATE", "L6 boundary drift")
            continue
        if isinstance(value, list):
            require(value == ["UNRESOLVED"], f"apparatus list prematurely resolves {key}")
        else:
            require(value == "UNRESOLVED", f"apparatus field prematurely resolves {key}")
    print("PASS 08 TYPE-WALL  all physical effect, event, law and post-state slots stay unresolved")

    transaction = manifest["ledger_transaction"]
    require(transaction["remove_active_rows_for"] == [old_id], "active-row removal set drift")
    old_dependencies = [row["depends_on"] for row in dependencies if row["item_id"] == old_id]
    require(len(old_dependencies) == 19 and len(set(old_dependencies)) == 19, "base predecessor dependency count drift")
    require(set(old_dependencies) == set(transaction["remove_predecessor_dependencies"]), "predecessor dependency removal drift")
    successor_requires = transaction["successor_requires"]
    require(
        successor_requires
        == [
            "DEF-ARCHITECTURE",
            "DEF-DECODER-MATTER",
            "DEF-DECODER-COMPLETION-CONTRACT",
            "COUPLINGS-DETERMINE",
            "QDD-ALGEBRAIC-FACTORIZATION",
            "DEF-QDD-COEFFICIENT-Q",
            "DEF-QDD-BALANCED-PISTON",
            "DEF-QDD-DOMAIN-K0",
            "DEF-QDD-AMPLITUDE-B0",
            "DEF-QDD-GRAM",
            "DEF-QDD-DAGGER",
            "DEF-QDD-TRANSPOSE",
            "DEF-QDD-QCARRIER-EQUALITY",
            "DEF-QDD-QPAIR",
            "DEF-QDD-PROJECTOR-LOW",
            "DEF-QDD-PROJECTOR-HIGH",
            "DEF-QDD-BRANCH-WEIGHT-PAIRING",
            "DEF-QDD-MATTER-RECORD",
            "DEF-QDD-DIRECT-WRITE",
        ],
        "exact successor dependency set drift",
    )
    require(len(set(successor_requires)) == 19, "successor dependency duplicate")
    require(transaction["forbidden_successor_dependencies"] == ["MEASURE-BORN-VERB"], "forbidden dependency wall drift")
    require("MEASURE-BORN-VERB" not in successor_requires, "physical Born lineage leaked into successor")
    require("DEF-DECODER-COMPLETION-CONTRACT" in successor_requires, "completion contract dependency missing")
    require("QDD-ALGEBRAIC-FACTORIZATION" in successor_requires, "factorization dependency missing")
    additional = transaction["additional_requires"]
    require(
        additional
        == [
            {"parent": "READING-SPLIT", "dependency": "ALGEBRAIC-DMATTER", "relation": "REQUIRES"},
            {"parent": "QDD-INSTRUMENT-APPARATUS", "dependency": "DEF-DECODER-COMPLETION-CONTRACT", "relation": "REQUIRES"},
        ],
        "additional dependency set drift",
    )
    prospective_edges = [
        (row["item_id"], row["depends_on"])
        for row in dependencies
        if row["item_id"] != old_id
    ]
    prospective_edges.extend(("ALGEBRAIC-DMATTER", child) for child in successor_requires)
    prospective_edges.extend((row["parent"], row["dependency"]) for row in additional)
    require(len(prospective_edges) == len(dependencies) - 19 + 19 + 2, "dependency delta is not +2")
    require(len(prospective_edges) == len(set(prospective_edges)), "prospective dependency duplicate")
    assert_acyclic(prospective_edges)
    graph: dict[str, set[str]] = {}
    for parent, child in prospective_edges:
        graph.setdefault(parent, set()).add(child)
    direct_closure: set[str] = set()
    pending = ["DEF-QDD-DIRECT-WRITE"]
    while pending:
        node = pending.pop()
        if node in direct_closure:
            continue
        direct_closure.add(node)
        pending.extend(graph.get(node, ()))
    factor_side = {
        "DEF-QDD-QPAIR", "DEF-QDD-GRAM", "DEF-QDD-DAGGER", "DEF-QDD-TRANSPOSE",
        "DEF-QDD-PROJECTOR-LOW", "DEF-QDD-PROJECTOR-HIGH",
        "DEF-QDD-BRANCH-WEIGHT-PAIRING", "DEF-QDD-FACTOR-MAP",
        "QDD-ALGEBRAIC-FACTORIZATION",
    }
    require(not (direct_closure & factor_side), "direct-write factor-side firewall broke")
    print("PASS 09 DAG        replace 19 edges, add two ownership edges; net +2 and acyclic")

    events = transaction["history_events"]
    expected_events = [
        ("QUADRATIC-DECODER-DATA", "RETIRE", 14, "O", "RETIRED"),
        ("ALGEBRAIC-DMATTER", "DECLARE", 1, "-", "D"),
        ("READING-SPLIT", "SCOPE_CHANGE", 14, "D", "D"),
        ("QDD-ALGEBRAIC-FACTORIZATION", "SCOPE_CHANGE", 2, "T", "T"),
        ("QPAIR-HERM-INTEGER-NONDESCENT", "SCOPE_CHANGE", 2, "T", "T"),
        ("QDD-INSTRUMENT-APPARATUS", "SCOPE_CHANGE", 6, "O", "O"),
    ]
    actual_events = [
        (item["claim_id"], item["event_type"], item["event_sequence"], item["previous_status"], item["new_status"])
        for item in events
    ]
    require(actual_events == expected_events, "six-event lifecycle drift")
    max_sequence: dict[str, int] = {}
    for row in history:
        max_sequence[row["claim_id"]] = max(max_sequence.get(row["claim_id"], 0), int(row["event_sequence"]))
    for claim_id, _event, sequence, previous, _new in expected_events:
        expected_sequence = 1 if previous == "-" else max_sequence[claim_id] + 1
        require(sequence == expected_sequence, f"event sequence drift for {claim_id}")
    print("PASS 10 HISTORY    exactly one retirement, one declaration and four scope events")

    target = manifest["target_count_contract"]
    status_count = Counter(row["status"] for row in registry)
    simulated_status = status_count.copy()
    simulated_status["O"] -= 1
    simulated_status["D"] += 1
    simulated_programs = [row for row in programs if row["claim_id"] != old_id]
    simulated_program_ids = {row["program_id"] for row in simulated_programs}
    reproduction_dirs = {
        Path(path).parts[1]
        for path in git_tree_paths(base, "reproduce")
        if len(Path(path).parts) >= 3
    }
    calculated = {
        "claims": len(registry),
        "status_T-LOCK": simulated_status["T-LOCK"],
        "status_T": simulated_status["T"],
        "status_D": simulated_status["D"],
        "status_C": simulated_status["C"],
        "status_H": simulated_status["H"],
        "status_O": simulated_status["O"],
        "status_F": simulated_status["F"],
        "live_H_O": simulated_status["H"] + simulated_status["O"],
        "normative_items": len(normative),
        "dependencies": len(prospective_edges),
        "evidence_rows": len(evidence),
        "history_rows": len(history) + len(events),
        "gates": len(gates),
        "frontier_program_rows": len(simulated_programs),
        "frontier_program_ids": len(simulated_program_ids),
        "core_selection_rows": len(core_selection),
        "evidence_none": sum(row["architecture_requirement"] == "none" for row in evidence),
        "evidence_one-architecture": sum(row["architecture_requirement"] == "one-architecture" for row in evidence),
        "evidence_recorded-audit": sum(row["architecture_requirement"] == "recorded-audit" for row in evidence),
        "two_architecture_evidence": sum(row["architecture_requirement"] == "two-architecture" for row in evidence),
        "reproductions": len(reproduction_dirs),
        "core_selection_change": 0,
    }
    require(target == calculated, f"target count contract drift: {calculated}")
    print("PASS 11 COUNTS     342 claims; D=44, O=27, live=29; deps=632; history=871")

    release = manifest["release_transaction"]
    require(
        set(release)
        == {
            "manifest_pr_must_merge_first", "release_branch", "release_base",
            "commit_count_above_base", "content_commit", "release_form_commit",
            "frozen_input_path", "frozen_input_disposition", "merge_method",
            "required_pr_checks", "public_merge_readback",
            "public_main_required_check", "tag_after_public_readback", "tag",
            "tag_kind", "tag_target", "tag_message_requires_content_commit",
            "tag_readback_required_before_draft", "publication_manifest_source",
            "draft_release_required", "draft_asset_count", "draft_asset_names",
            "draft_assets_download_and_validate_before_publish",
            "post_publish_release_event_readback",
        },
        "release-contract key schema drift",
    )
    require(release["manifest_pr_must_merge_first"], "release may start before manifest merge")
    require(release["release_branch"] == "release/canon-v70", "release branch drift")
    require(release["commit_count_above_base"] == 2, "release is not exactly two commits")
    require(release["content_commit"]["ordinal"] == 1 and release["content_commit"]["name"] == "C1", "C1 contract drift")
    require(
        set(release["content_commit"]["forbidden_paths"])
        == {
            "STATUS.md", "README.md", "CITATION.cff",
            "notes/canon/QDD-ALGEBRAIC-DMATTER-SUCCESSOR-V70/**",
        },
        "C1 frozen-path wall drift",
    )
    require(release["release_form_commit"]["ordinal"] == 2 and release["release_form_commit"]["name"] == "C2", "C2 contract drift")
    require(release["release_form_commit"]["exact_paths"] == ["STATUS.md", "README.md", "CITATION.cff"], "C2 exact-path contract drift")
    require(
        release["frozen_input_path"] == "notes/canon/QDD-ALGEBRAIC-DMATTER-SUCCESSOR-V70/"
        and release["frozen_input_disposition"] == "CONSUME_BYTE_EXACT_DO_NOT_REWRITE",
        "successor manifest is not frozen as a release input",
    )
    require(release["merge_method"] == "MERGE_COMMIT_ONLY", "release merge-method drift")
    require(
        release["required_pr_checks"] == ["architecture-x86_64", "architecture-aarch64", "check"],
        "required release checks drift",
    )
    require(release["public_merge_readback"] == "BYTE_IDENTICAL_TO_C2_TREE", "merge readback drift")
    require(release["public_main_required_check"] == "SUCCESS_BEFORE_TAG", "public-main check drift")
    require(release["tag_after_public_readback"], "tag may precede public readback")
    require(
        release["tag"] == "canon-v70"
        and release["tag_kind"] == "ANNOTATED"
        and release["tag_target"] == "PUBLIC_RELEASE_PR_MERGE_COMMIT",
        "release tag contract drift",
    )
    require(release["tag_message_requires_content_commit"], "tag message may omit content commit")
    require(release["tag_readback_required_before_draft"], "draft may precede tag readback")
    require(release["publication_manifest_source"] == "SUCCESSFUL_TAG_JOB_ONLY", "publication manifest source drift")
    require(release["draft_release_required"], "release need not be assembled as draft")
    require(release["draft_asset_count"] == 2, "draft asset count drift")
    require(release["draft_asset_names"] == ["activation-manifest.json", "SHA256SUMS"], "draft asset names drift")
    require(release["draft_assets_download_and_validate_before_publish"], "draft assets need not be validated")
    require(release["post_publish_release_event_readback"] == "REQUIRED_SUCCESS", "release-event readback drift")
    print("PASS 12 RELEASE    manifest first; v70 is separate C1+C2, merge tag and official assets")

    invalid = set(manifest["invalid_conditions"])
    required_invalid = {
        "PARTIAL_ADOPTION", "PHYSICAL_INPUT_LEAK", "TYPE_ALIAS", "CHOICE_AS_THEOREM",
        "ALTERNATIVE_ERASURE", "DEBT_ERASURE", "STATUS_LEAK",
        "PREDECESSOR_FALSIFICATION_OR_POSITIVE_CLOSURE", "NEW_CROSS_LAYER_GATE",
        "NON_ATOMIC_CONTENT_FOLD", "OLD_MANIFEST_MUTATION", "RELEASE_BRANCH_THIRD_COMMIT",
    }
    require(invalid == required_invalid, "invalid-condition firewall drift")
    require(transaction["gate_change"] == "NONE", "unexpected gate change")
    require(transaction["core_selection_change"] == "NONE", "unexpected core-selection change")
    require(
        transaction["reproduction_change"] == "STATUS_SEPARATION_CONFORMANCE_ONLY",
        "status-separation conformance update is not frozen",
    )
    require(
        transaction["reproduction_paths"]
        == [
            "reproduce/status-separation/verify.py",
            "reproduce/status-separation/EXPECTED.txt",
            "reproduce/status-separation/README.md",
        ],
        "status-separation path set drift",
    )
    require(transaction["scientific_evidence_change"] == "NONE", "scientific evidence change leaked")
    require("CAND-" not in manifest_text, "proposal-local CAND identifier leaked")
    require("TYPE-QDD-" not in manifest_text, "proposal-local TYPE-QDD identifier leaked")

    unresolved_paths: list[str] = []

    def find_unresolved(value: object, path: str) -> None:
        if value == "UNRESOLVED":
            unresolved_paths.append(path)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                find_unresolved(item, f"{path}[{index}]")
        elif isinstance(value, dict):
            for key, item in value.items():
                find_unresolved(item, f"{path}.{key}" if path else key)

    find_unresolved(manifest, "")
    require(unresolved_paths, "apparatus must retain unresolved physical debt")
    require(
        all(path.startswith("apparatus_transfer.apparatus_manifest.") for path in unresolved_paths),
        "UNRESOLVED leaked outside apparatus_manifest",
    )
    print("PASS 13 FIREWALL   no theorem, alternative erasure, debt erasure, gate or scope leak")

    print()
    print("RESULT 13/13 successor-manifest checks hold; NON-FORMAL; PUBLIC CANON V69 UNCHANGED")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    try:
        main()
    except (CheckError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL {exc}")
        raise SystemExit(1)
