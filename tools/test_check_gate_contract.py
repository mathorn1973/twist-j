#!/usr/bin/env python3
"""Unit tests for the explicit GATES.tsv semantic contract."""

from __future__ import annotations

import csv
from pathlib import Path
import tempfile
import unittest

from tools.check_gate_contract import (
    GATE_FIELDS,
    NORMATIVE_FIELDS,
    GateContractError,
    validate_gate_contract,
)


def write_tsv(path: Path, fields: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


class GateFixture:
    def __init__(self, root: Path) -> None:
        self.canon = root / "canon"
        self.canon.mkdir()
        self.normative = [
            {"item_id": "DEF-PROJ", "item_type": "DEFINITION", "claim_id": "", "status": "", "layer": "L5", "gate_ids": "GATE-DEF", "statement_source": "fixture"},
            {"item_id": "OPEN-LIFT", "item_type": "OBLIGATION", "claim_id": "OPEN-LIFT", "status": "O", "layer": "L2", "gate_ids": "GATE-LIFT", "statement_source": "fixture"},
            {"item_id": "OPEN-SELECT", "item_type": "OBLIGATION", "claim_id": "OPEN-SELECT", "status": "O", "layer": "MULTI", "gate_ids": "GATE-SELECT", "statement_source": "fixture"},
            {"item_id": "DICT-LIFT", "item_type": "DICTIONARY", "claim_id": "DICT-LIFT", "status": "D", "layer": "NOT_APPLICABLE", "gate_ids": "GATE-DICT", "statement_source": "fixture"},
            {"item_id": "FIRED", "item_type": "FALSIFIED", "claim_id": "FIRED", "status": "F", "layer": "MULTI", "gate_ids": "GATE-FIRED", "statement_source": "fixture"},
        ]
        self.gates = [
            {"gate_id": "GATE-DEF", "owner_item_id": "DEF-PROJ", "from_layer": "L1", "to_layer": "L5", "gate_kind": "DEFINITION_PROJECTION", "decision_condition": "fixture definition projection decision condition"},
            {"gate_id": "GATE-LIFT", "owner_item_id": "OPEN-LIFT", "from_layer": "L1", "to_layer": "L2", "gate_kind": "OPEN_LIFT", "decision_condition": "fixture open lift decision condition"},
            {"gate_id": "GATE-SELECT", "owner_item_id": "OPEN-SELECT", "from_layer": "L5", "to_layer": "L1", "gate_kind": "OPEN_SELECTION", "decision_condition": "fixture open selection decision condition"},
            {"gate_id": "GATE-DICT", "owner_item_id": "DICT-LIFT", "from_layer": "L5", "to_layer": "L6", "gate_kind": "DICTIONARY_LIFT", "decision_condition": "fixture dictionary lift decision condition"},
            {"gate_id": "GATE-FIRED", "owner_item_id": "FIRED", "from_layer": "L1", "to_layer": "L5", "gate_kind": "FIRED_NEGATIVE", "decision_condition": "fixture fired negative decision condition"},
        ]

    def write(self) -> None:
        write_tsv(self.canon / "NORMATIVE.tsv", NORMATIVE_FIELDS, self.normative)
        write_tsv(self.canon / "GATES.tsv", GATE_FIELDS, self.gates)


class GateContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.fixture = GateFixture(self.root)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_valid_gate_contract(self) -> None:
        self.fixture.write()
        kinds = validate_gate_contract(self.root)
        self.assertEqual(sum(kinds.values()), 5)
        self.assertEqual(kinds["OPEN_LIFT"], 1)

    def test_gate_kind_is_closed(self) -> None:
        self.fixture.gates[1]["gate_kind"] = "DECORATIVE"
        self.fixture.write()
        with self.assertRaisesRegex(GateContractError, "invalid gate_kind DECORATIVE"):
            validate_gate_contract(self.root)

    def test_gate_kind_requires_owner_type(self) -> None:
        self.fixture.normative[1]["item_type"] = "THEOREM"
        self.fixture.write()
        with self.assertRaisesRegex(GateContractError, "requires owner type OBLIGATION"):
            validate_gate_contract(self.root)

    def test_gate_kind_requires_owner_status(self) -> None:
        self.fixture.normative[3]["status"] = "T"
        self.fixture.write()
        with self.assertRaisesRegex(GateContractError, "requires owner status D"):
            validate_gate_contract(self.root)

    def test_concrete_owner_layer_matches_gate_target(self) -> None:
        self.fixture.normative[1]["layer"] = "L3"
        self.fixture.write()
        with self.assertRaisesRegex(GateContractError, "differs from concrete owner layer L3"):
            validate_gate_contract(self.root)

    def test_multi_owner_does_not_invent_a_concrete_layer(self) -> None:
        self.fixture.write()
        kinds = validate_gate_contract(self.root)
        self.assertEqual(kinds["OPEN_SELECTION"], 1)

    def test_owner_must_name_its_gate(self) -> None:
        self.fixture.normative[1]["gate_ids"] = ""
        self.fixture.write()
        with self.assertRaisesRegex(GateContractError, "owner row OPEN-LIFT does not name GATE-LIFT"):
            validate_gate_contract(self.root)


if __name__ == "__main__":
    unittest.main()
