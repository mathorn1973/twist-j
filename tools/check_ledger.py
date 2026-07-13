#!/usr/bin/env python3
"""Validate Public Canon companion ledgers without third-party packages."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date
import hashlib
from pathlib import Path
import re


REGISTRY_FIELDS = (
    "claim_id", "status", "scope", "canon_section", "evidence", "falsifier"
)
NORMATIVE_FIELDS = (
    "item_id", "item_type", "claim_id", "status", "layer", "gate_ids",
    "statement_source",
)
DEPENDENCY_FIELDS = ("item_id", "depends_on", "relation", "basis")
EVIDENCE_FIELDS = (
    "claim_id", "evidence_id", "evidence_kind", "location", "sha256",
    "hash_mode", "architecture_requirement",
)
HISTORY_FIELDS = (
    "event_id", "event_date", "release", "claim_id", "event_type",
    "previous_status", "new_status", "scope_sha256", "evidence_id", "rationale",
)
GATE_FIELDS = (
    "gate_id", "claim_id", "from_layer", "to_layer", "gate_kind",
    "decision_condition",
)
CORE_SELECTION_FIELDS = ("rank", "claim_id")

STATUSES = {"T-LOCK", "T", "D", "C", "H", "O", "F"}
ITEM_TYPES = {
    "AXIOM", "DEFINITION", "THEOREM", "DICTIONARY", "COMPUTATION",
    "HYPOTHESIS", "OBLIGATION", "FALSIFIED", "EMPIRICAL_ANCHOR",
}
STATUS_TYPES = {
    "T-LOCK": "THEOREM", "T": "THEOREM", "D": "DICTIONARY",
    "C": "COMPUTATION", "H": "HYPOTHESIS", "O": "OBLIGATION",
    "F": "FALSIFIED",
}
LAYERS = {
    "FOUNDATION", "L1", "L2", "L3", "L4", "L5", "L6", "MULTI",
    "NOT_APPLICABLE",
}
RELATIONS = {"REQUIRES", "BOUNDED_BY"}
EVIDENCE_KINDS = {"INLINE_CANON", "REPRODUCTION", "EXTERNAL_SOURCE"}
HASH_MODES = {"file-sha256", "bundle-manifest-sha256-v1", "external-manifest"}
ARCHITECTURE_REQUIREMENTS = {
    "none", "one-architecture", "two-architecture",
    "two-architecture-pending", "recorded-audit",
}
EVENT_TYPES = {"DECLARE", "STATUS_CHANGE", "SCOPE_CHANGE", "EVIDENCE_CHANGE", "RETIRE"}
ID = re.compile(r"^[A-Z][A-Z0-9-]*$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


class LedgerError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise LedgerError(message)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def bundle_sha256(path: Path, root: Path) -> str:
    if path.is_file():
        return sha256_bytes(path.read_bytes())
    lines: list[str] = []
    for item in sorted(candidate for candidate in path.rglob("*") if candidate.is_file()):
        if "__pycache__" in item.parts or item.suffix == ".pyc":
            continue
        relative = item.relative_to(root).as_posix()
        lines.append(f"{sha256_bytes(item.read_bytes())}  {relative}\n")
    return sha256_bytes("".join(lines).encode("utf-8"))


def read_tsv(path: Path, fields: tuple[str, ...]) -> list[dict[str, str]]:
    if not path.is_file():
        fail(f"missing {path}")
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if tuple(reader.fieldnames or ()) != fields:
            fail(f"{path.name} header must be: " + "\t".join(fields))
        return list(reader)


def require_text(row: dict[str, str], field: str, context: str) -> str:
    value = row[field].strip()
    if not value:
        fail(f"{context} has empty {field}")
    return value


def records_for(location: Path) -> set[str]:
    runs = location / "RUNS"
    if not runs.is_dir():
        return set()
    return {path.stem for path in runs.glob("*.md") if path.is_file()}


@dataclass(frozen=True)
class Snapshot:
    claims: int
    items: int
    dependencies: int
    evidence: int
    history_events: int
    gates: int


def validate(root: Path) -> Snapshot:
    canon = root / "canon"
    registry_rows = read_tsv(canon / "REGISTRY.tsv", REGISTRY_FIELDS)
    normative_rows = read_tsv(canon / "NORMATIVE.tsv", NORMATIVE_FIELDS)
    dependency_rows = read_tsv(canon / "DEPENDENCIES.tsv", DEPENDENCY_FIELDS)
    evidence_rows = read_tsv(canon / "EVIDENCE.tsv", EVIDENCE_FIELDS)
    history_rows = read_tsv(canon / "HISTORY.tsv", HISTORY_FIELDS)
    gate_rows = read_tsv(canon / "GATES.tsv", GATE_FIELDS)
    core_selection_rows = read_tsv(
        canon / "CORE_SELECTION.tsv", CORE_SELECTION_FIELDS
    )

    registry: dict[str, dict[str, str]] = {}
    for number, row in enumerate(registry_rows, 2):
        claim = require_text(row, "claim_id", f"REGISTRY.tsv line {number}")
        if claim in registry:
            fail(f"REGISTRY.tsv duplicates {claim}")
        if row["status"].strip() not in STATUSES:
            fail(f"REGISTRY.tsv {claim} has invalid status")
        registry[claim] = row

    items: dict[str, dict[str, str]] = {}
    claim_items: dict[str, dict[str, str]] = {}
    for number, row in enumerate(normative_rows, 2):
        context = f"NORMATIVE.tsv line {number}"
        item = require_text(row, "item_id", context)
        if not ID.fullmatch(item):
            fail(f"{context} has invalid item_id")
        if item in items:
            fail(f"NORMATIVE.tsv duplicates {item}")
        item_type = require_text(row, "item_type", context)
        if item_type not in ITEM_TYPES:
            fail(f"{item} has invalid item_type {item_type}")
        layer = require_text(row, "layer", context)
        if layer not in LAYERS:
            fail(f"{item} has invalid layer {layer}")
        statement_source = require_text(row, "statement_source", context)
        relative_source, separator, anchor = statement_source.partition("::")
        source_path = root / relative_source
        if not separator or not source_path.is_file() or not anchor:
            fail(f"{item} has invalid statement_source")
        if anchor not in source_path.read_text(encoding="utf-8"):
            fail(f"{item} statement_source anchor is absent")
        claim = row["claim_id"].strip()
        status = row["status"].strip()
        if claim:
            if claim not in registry:
                fail(f"NORMATIVE.tsv names unregistered claim {claim}")
            if claim in claim_items:
                fail(f"NORMATIVE.tsv duplicates claim row {claim}")
            if item != claim:
                fail(f"claim row {claim} must use the claim id as item_id")
            expected_status = registry[claim]["status"].strip()
            if status != expected_status:
                fail(f"{claim} status differs from REGISTRY.tsv")
            if item_type != STATUS_TYPES[status]:
                fail(f"{claim} item_type differs from status class")
            claim_items[claim] = row
        elif status:
            fail(f"non-claim item {item} must not carry public status")
        items[item] = row
    missing_items = sorted(set(registry) - set(claim_items))
    if missing_items:
        fail("NORMATIVE.tsv lacks claims: " + ", ".join(missing_items))

    core_claims: set[str] = set()
    core_ranks: list[int] = []
    for number, row in enumerate(core_selection_rows, 2):
        context = f"CORE_SELECTION.tsv line {number}"
        claim = require_text(row, "claim_id", context)
        if claim not in registry:
            fail(f"{context} names unknown claim {claim}")
        if claim in core_claims:
            fail(f"CORE_SELECTION.tsv duplicates {claim}")
        if registry[claim]["status"].strip() not in {"T", "T-LOCK", "D", "C"}:
            fail(f"CORE_SELECTION.tsv contains non-closed orientation claim {claim}")
        try:
            rank = int(require_text(row, "rank", context))
        except ValueError:
            fail(f"{context} has invalid rank")
        core_claims.add(claim)
        core_ranks.append(rank)
    if sorted(core_ranks) != list(range(1, len(core_ranks) + 1)):
        fail("CORE_SELECTION.tsv ranks must be contiguous from 1")

    gates: dict[str, dict[str, str]] = {}
    for number, row in enumerate(gate_rows, 2):
        context = f"GATES.tsv line {number}"
        gate = require_text(row, "gate_id", context)
        if not ID.fullmatch(gate):
            fail(f"{context} has invalid gate_id")
        if gate in gates:
            fail(f"GATES.tsv duplicates {gate}")
        claim = require_text(row, "claim_id", context)
        if claim not in registry:
            fail(f"{gate} names unknown claim {claim}")
        source = require_text(row, "from_layer", context)
        target = require_text(row, "to_layer", context)
        if source not in LAYERS or target not in LAYERS:
            fail(f"{gate} has invalid layer")
        if source == target:
            fail(f"{gate} does not cross a layer")
        require_text(row, "gate_kind", context)
        if len(require_text(row, "decision_condition", context)) < 20:
            fail(f"{gate} decision condition is too short")
        gates[gate] = row
    for item, row in items.items():
        for gate in filter(None, (part.strip() for part in row["gate_ids"].split(";"))):
            if gate not in gates:
                fail(f"{item} names unknown gate {gate}")
            if row["claim_id"].strip() != gates[gate]["claim_id"].strip():
                fail(f"{item} names gate {gate} owned by another claim")
    for gate, row in gates.items():
        owner = claim_items[row["claim_id"]]
        if gate not in owner["gate_ids"].split(";"):
            fail(f"claim row {row['claim_id']} does not name {gate}")

    dependency_keys: set[tuple[str, str, str]] = set()
    adjacency: dict[str, set[str]] = {item: set() for item in items}
    for number, row in enumerate(dependency_rows, 2):
        context = f"DEPENDENCIES.tsv line {number}"
        item = require_text(row, "item_id", context)
        target = require_text(row, "depends_on", context)
        relation = require_text(row, "relation", context)
        require_text(row, "basis", context)
        if item not in items or target not in items:
            fail(f"{context} names unknown item")
        if item == target:
            fail(f"{context} is a self dependency")
        if relation not in RELATIONS:
            fail(f"{context} has invalid relation {relation}")
        key = (item, target, relation)
        if key in dependency_keys:
            fail(f"DEPENDENCIES.tsv duplicates {item} -> {target} ({relation})")
        dependency_keys.add(key)
        adjacency[item].add(target)
        if relation == "REQUIRES":
            source_status = items[item]["status"].strip()
            target_status = items[target]["status"].strip()
            target_type = items[target]["item_type"].strip()
            if source_status in {"T", "T-LOCK"}:
                if target_status not in {"T", "T-LOCK"} and target_type not in {"AXIOM", "DEFINITION"}:
                    fail(f"theorem {item} requires lower-status item {target}")
            if source_status == "D" and target_status in {"H", "O", "F"}:
                fail(f"dictionary {item} requires open or falsified item {target}")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(item: str) -> None:
        if item in visiting:
            fail(f"dependency graph contains a cycle at {item}")
        if item in visited:
            return
        visiting.add(item)
        for target in sorted(adjacency[item]):
            visit(target)
        visiting.remove(item)
        visited.add(item)

    for item in sorted(items):
        visit(item)

    evidence: dict[str, dict[str, str]] = {}
    evidence_by_claim: dict[str, dict[str, str]] = {}
    canon_hash = sha256_bytes((canon / "CANON.md").read_bytes())
    for number, row in enumerate(evidence_rows, 2):
        context = f"EVIDENCE.tsv line {number}"
        claim = require_text(row, "claim_id", context)
        evidence_id = require_text(row, "evidence_id", context)
        if claim not in registry:
            fail(f"{context} names unknown claim {claim}")
        if claim in evidence_by_claim:
            fail(f"EVIDENCE.tsv duplicates claim {claim}")
        if evidence_id in evidence:
            fail(f"EVIDENCE.tsv duplicates evidence_id {evidence_id}")
        kind = require_text(row, "evidence_kind", context)
        location = require_text(row, "location", context)
        digest = require_text(row, "sha256", context)
        mode = require_text(row, "hash_mode", context)
        architecture = require_text(row, "architecture_requirement", context)
        if kind not in EVIDENCE_KINDS or mode not in HASH_MODES:
            fail(f"{evidence_id} has invalid evidence kind or hash mode")
        if architecture not in ARCHITECTURE_REQUIREMENTS:
            fail(f"{evidence_id} has invalid architecture requirement")
        if location != registry[claim]["evidence"].strip():
            fail(f"{claim} evidence location differs from REGISTRY.tsv")
        if kind == "INLINE_CANON":
            if location != "inline" or mode != "file-sha256" or digest != canon_hash:
                fail(f"{evidence_id} has invalid inline evidence hash")
        elif kind == "REPRODUCTION":
            relative = Path(location)
            if relative.is_absolute() or ".." in relative.parts:
                fail(f"{evidence_id} has unsafe location")
            artifact = root / relative
            if not artifact.is_dir() or mode != "bundle-manifest-sha256-v1":
                fail(f"{evidence_id} reproduction is missing")
            if not SHA256.fullmatch(digest) or digest != bundle_sha256(artifact, root):
                fail(f"{evidence_id} reproduction hash differs")
            architectures = records_for(artifact)
            if architecture == "two-architecture" and not {"aarch64", "x86_64"}.issubset(architectures):
                fail(f"{evidence_id} lacks the two-architecture records")
            if architecture == "two-architecture-pending":
                for required in ("verify.py", "EXPECTED.txt", "README.md"):
                    if not (artifact / required).is_file():
                        fail(f"{evidence_id} lacks {required}")
            if architecture == "one-architecture":
                for required in ("verify.py", "EXPECTED.txt", "README.md"):
                    if not (artifact / required).is_file():
                        fail(f"{evidence_id} lacks {required}")
        else:
            if mode != "external-manifest" or digest != "PENDING-SOURCE-MANIFEST":
                fail(f"{evidence_id} external source is not delegated to the source manifest")
        evidence[evidence_id] = row
        evidence_by_claim[claim] = row
    missing_evidence = sorted(set(registry) - set(evidence_by_claim))
    if missing_evidence:
        fail("EVIDENCE.tsv lacks claims: " + ", ".join(missing_evidence))

    events: set[str] = set()
    histories: dict[str, list[dict[str, str]]] = {claim: [] for claim in registry}
    for number, row in enumerate(history_rows, 2):
        context = f"HISTORY.tsv line {number}"
        event = require_text(row, "event_id", context)
        claim = require_text(row, "claim_id", context)
        if event in events:
            fail(f"HISTORY.tsv duplicates {event}")
        events.add(event)
        if claim not in registry:
            fail(f"{event} names unknown claim {claim}")
        try:
            date.fromisoformat(require_text(row, "event_date", context))
        except ValueError:
            fail(f"{event} has invalid event_date")
        if require_text(row, "event_type", context) not in EVENT_TYPES:
            fail(f"{event} has invalid event_type")
        new_status = require_text(row, "new_status", context)
        if new_status not in STATUSES:
            fail(f"{event} has invalid new_status")
        if not SHA256.fullmatch(require_text(row, "scope_sha256", context)):
            fail(f"{event} has invalid scope hash")
        if require_text(row, "evidence_id", context) not in evidence:
            fail(f"{event} names unknown evidence")
        require_text(row, "release", context)
        require_text(row, "rationale", context)
        histories[claim].append(row)
    for claim, rows in histories.items():
        if not rows:
            fail(f"HISTORY.tsv lacks {claim}")
        rows.sort(key=lambda row: (row["event_date"], row["event_id"]))
        previous = "-"
        for row in rows:
            if row["previous_status"].strip() != previous:
                fail(f"{row['event_id']} breaks the status transition chain")
            previous = row["new_status"].strip()
        if previous != registry[claim]["status"].strip():
            fail(f"HISTORY.tsv latest status differs for {claim}")
        expected_scope = sha256_bytes(registry[claim]["scope"].encode("utf-8"))
        if rows[-1]["scope_sha256"].strip() != expected_scope:
            fail(f"HISTORY.tsv latest scope differs for {claim}")
        if rows[-1]["evidence_id"].strip() != evidence_by_claim[claim]["evidence_id"].strip():
            fail(f"HISTORY.tsv latest evidence differs for {claim}")

    return Snapshot(
        claims=len(registry),
        items=len(items),
        dependencies=len(dependency_rows),
        evidence=len(evidence_rows),
        history_events=len(history_rows),
        gates=len(gates),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        snapshot = validate(args.root.resolve())
    except LedgerError as error:
        print(f"FAIL: {error}")
        raise SystemExit(1)
    print(
        "LEDGER PASS "
        f"claims={snapshot.claims} items={snapshot.items} "
        f"dependencies={snapshot.dependencies} evidence={snapshot.evidence} "
        f"history={snapshot.history_events} gates={snapshot.gates}"
    )


if __name__ == "__main__":
    main()
