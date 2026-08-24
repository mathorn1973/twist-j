#!/usr/bin/env python3
"""Integration tests for same-layer OPEN_DECISION in check_ledger.py."""

from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from tools.check_ledger import LedgerError, validate
from tools.check_gate_contract import GateContractError
from tools.test_check_ledger import LedgerFixture


class LedgerOpenDecisionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.fixture = LedgerFixture(self.root)
        # Keep the fixture dependency graph same-layer so the decision gate is
        # tested independently of the cross-layer dependency rule.
        self.fixture.normative[0]["layer"] = "L2"
        self.fixture.normative[1]["layer"] = "L2"
        self.fixture.normative[2]["layer"] = "L2"
        self.fixture.gates[0].update({
            "from_layer": "L2",
            "to_layer": "L2",
            "gate_kind": "OPEN_DECISION",
        })

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_same_layer_open_decision_is_accepted(self) -> None:
        self.fixture.write()
        snapshot = validate(self.root)
        self.assertEqual(snapshot.gates, 1)

    def test_same_layer_nondecision_is_rejected(self) -> None:
        self.fixture.gates[0]["gate_kind"] = "OPEN_LIFT"
        self.fixture.write()
        with self.assertRaisesRegex(GateContractError, "same-layer endpoints require OPEN_DECISION"):
            validate(self.root)

    def test_open_decision_cannot_hide_cross_layer_dependency(self) -> None:
        self.fixture.normative[1]["layer"] = "L1"
        self.fixture.write()
        with self.assertRaisesRegex(LedgerError, "cross-layer dependency"):
            validate(self.root)


if __name__ == "__main__":
    unittest.main()
