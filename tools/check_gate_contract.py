#!/usr/bin/env python3
"""Validate the explicit semantic contract of every Public Canon gate.

This checker complements check_ledger.py. The ledger checker still requires a
matching gate for every dependency that actually crosses two concrete protocol
layers. This checker makes each GATES.tsv row load-bearing independently of
whether such a dependency edge happens to exist.
"""

from __future__ import annotations

import argparse
from collections import Counter
import csv
from pathlib import Path


NORMATIVE_FIELDS = (
    "item_id", "item_type", "claim_id", "status", "layer", "gate_ids",
    "statement_source",
)
GATE_FIELDS = (
    "gate_id", "owner_item_id", "from_layer", "to_layer", "gate_kind",
    "decision_condition",
)
PROTOCOL_LAYERS = {f"L{number}" for number in range(1, 7)}
GATE_KIND_OWNER = {
    "DEFINITION_PROJECTION": ("DEFINITION", ""),
    "OPEN_LIFT": ("OBLIGATION", "O"),
    "OPEN_SELECTION": ("OBLIGATION", "O"),
    "DICTIONARY_LIFT": ("DICTIONARY", "D"),
    "FIRED_NEGATIVE": ("FALSIFIED", "F"),
}


class GateContractError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise GateContractError(message)


def read_tsv(path: Path, fields: tuple[str, ...]) -> list[dict[str, str]]:
    if not path.is_file():
        fail(f"missing {path}")
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if tuple(reader.fieldnames or ()) != fields:
            fail(f"{path.name} header must be: " + "\t".join(fields))
        return list(reader)


def require(row: dict[str, str], field: str, context: str) -> str:
    value = row[field].strip()
    if not value:
        fail(f"{context} has empty {field}")
    return value


def validate_gate_contract(root: Path) -> Counter[str]:
    canon = root / "canon"
    normative_rows = read_tsv(canon / "NORMATIVE.tsv", NORMATIVE_FIELDS)
    gate_rows = read_tsv(canon / "GATES.tsv", GATE_FIELDS)

    items: dict[str, dict[str, str]] = {}
    for number, row in enumerate(normative_rows, 2):
        context = f"NORMATIVE.tsv line {number}"
        item = require(row, "item_id", context)
        if item in items:
            fail(f"NORMATIVE.tsv duplicates {item}")
        items[item] = row

    gates: dict[str, dict[str, str]] = {}
    kinds: Counter[str] = Counter()
    for number, row in enumerate(gate_rows, 2):
        context = f"GATES.tsv line {number}"
        gate = require(row, "gate_id", context)
        if gate in gates:
            fail(f"GATES.tsv duplicates {gate}")
        owner = require(row, "owner_item_id", context)
        if owner not in items:
            fail(f"{gate} names unknown owner item {owner}")
        source = require(row, "from_layer", context)
        target = require(row, "to_layer", context)
        if source not in PROTOCOL_LAYERS or target not in PROTOCOL_LAYERS:
            fail(f"{gate} endpoints must both be concrete protocol layers")
        if source == target:
            fail(f"{gate} does not cross a layer")

        gate_kind = require(row, "gate_kind", context)
        if gate_kind not in GATE_KIND_OWNER:
            fail(f"{gate} has invalid gate_kind {gate_kind}")
        expected_type, expected_status = GATE_KIND_OWNER[gate_kind]
        owner_row = items[owner]
        owner_type = owner_row["item_type"].strip()
        owner_status = owner_row["status"].strip()
        if owner_type != expected_type:
            fail(
                f"{gate} gate_kind {gate_kind} requires owner type "
                f"{expected_type}, found {owner_type or '<empty>'}"
            )
        if owner_status != expected_status:
            expected = expected_status or "<empty>"
            found = owner_status or "<empty>"
            fail(
                f"{gate} gate_kind {gate_kind} requires owner status "
                f"{expected}, found {found}"
            )

        owner_layer = owner_row["layer"].strip()
        if owner_layer in PROTOCOL_LAYERS and owner_layer != target:
            fail(
                f"{gate} to_layer {target} differs from concrete owner layer "
                f"{owner_layer}"
            )

        owner_gates = {
            part.strip() for part in owner_row["gate_ids"].split(";")
            if part.strip()
        }
        if gate not in owner_gates:
            fail(f"owner row {owner} does not name {gate}")

        gates[gate] = row
        kinds[gate_kind] += 1

    for item, row in items.items():
        for gate in filter(None, (part.strip() for part in row["gate_ids"].split(";"))):
            if gate not in gates:
                fail(f"{item} names unknown gate {gate}")
            if gates[gate]["owner_item_id"].strip() != item:
                fail(f"{item} names gate {gate} owned by another item")

    return kinds


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        kinds = validate_gate_contract(args.root.resolve())
    except GateContractError as error:
        print(f"FAIL: {error}")
        raise SystemExit(1)
    summary = ",".join(f"{kind}:{kinds[kind]}" for kind in sorted(kinds))
    print(f"GATE CONTRACT PASS gates={sum(kinds.values())} kinds={summary}")


if __name__ == "__main__":
    main()
