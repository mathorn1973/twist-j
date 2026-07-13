#!/usr/bin/env python3
"""Negative and positive unit tests for check_ledger.py."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path
import tempfile
import unittest

from tools.check_ledger import (
    CORE_SELECTION_FIELDS,
    DEPENDENCY_FIELDS,
    EVIDENCE_FIELDS,
    GATE_FIELDS,
    HISTORY_FIELDS,
    LedgerError,
    NORMATIVE_FIELDS,
    REGISTRY_FIELDS,
    validate,
)


def write_tsv(path: Path, fields: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


class LedgerFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.canon = root / "canon"
        self.canon.mkdir()
        (self.canon / "CANON.md").write_text("# Fixture\nT-CLAIM [T]. O-CLAIM [O].\n", encoding="utf-8")
        scope_t = "exact fixture theorem"
        scope_o = "open fixture gate"
        self.registry = [
            {"claim_id": "T-CLAIM", "status": "T", "scope": scope_t, "canon_section": "Fixture", "evidence": "inline", "falsifier": ""},
            {"claim_id": "O-CLAIM", "status": "O", "scope": scope_o, "canon_section": "Fixture", "evidence": "inline", "falsifier": "closes positively by a fixture and negatively by its exact counterexample"},
        ]
        self.normative = [
            {"item_id": "DEF-FIXTURE", "item_type": "DEFINITION", "claim_id": "", "status": "", "layer": "L1", "gate_ids": "", "statement_source": "canon/CANON.md::Fixture"},
            {"item_id": "T-CLAIM", "item_type": "THEOREM", "claim_id": "T-CLAIM", "status": "T", "layer": "L1", "gate_ids": "", "statement_source": "canon/CANON.md::Fixture"},
            {"item_id": "O-CLAIM", "item_type": "OBLIGATION", "claim_id": "O-CLAIM", "status": "O", "layer": "NOT_APPLICABLE", "gate_ids": "GATE-FIXTURE", "statement_source": "canon/CANON.md::Fixture"},
        ]
        self.dependencies = [
            {"item_id": "T-CLAIM", "depends_on": "DEF-FIXTURE", "relation": "REQUIRES", "basis": "fixture theorem uses fixture definition"},
            {"item_id": "O-CLAIM", "depends_on": "T-CLAIM", "relation": "REQUIRES", "basis": "fixture obligation starts from fixture theorem"},
        ]
        canon_hash = hashlib.sha256((self.canon / "CANON.md").read_bytes()).hexdigest()
        self.evidence = [
            {"claim_id": claim, "evidence_id": f"EV-{claim}", "evidence_kind": "INLINE_CANON", "location": "inline", "sha256": canon_hash, "hash_mode": "file-sha256", "architecture_requirement": "none"}
            for claim in ("T-CLAIM", "O-CLAIM")
        ]
        self.history = []
        for claim, status, scope in (("T-CLAIM", "T", scope_t), ("O-CLAIM", "O", scope_o)):
            self.history.append({
                "event_id": f"GENESIS-{claim}", "event_sequence": "1", "event_date": "2026-07-13", "release": "canon-v1-genesis", "claim_id": claim,
                "event_type": "DECLARE", "previous_status": "-", "new_status": status,
                "scope_sha256": hashlib.sha256(scope.encode()).hexdigest(), "evidence_id": f"EV-{claim}",
                "evidence_location": "inline", "evidence_sha256": canon_hash,
                "rationale": "fixture declaration",
            })
        self.gates = [{
            "gate_id": "GATE-FIXTURE", "owner_item_id": "O-CLAIM", "from_layer": "L1", "to_layer": "L2",
            "gate_kind": "OPEN_LIFT", "decision_condition": "closes positively by a fixture and negatively by its exact counterexample",
        }]
        self.core_selection = [
            {"rank": "1", "claim_id": "T-CLAIM"},
        ]

    def write(self) -> None:
        write_tsv(self.canon / "REGISTRY.tsv", REGISTRY_FIELDS, self.registry)
        write_tsv(self.canon / "NORMATIVE.tsv", NORMATIVE_FIELDS, self.normative)
        write_tsv(self.canon / "DEPENDENCIES.tsv", DEPENDENCY_FIELDS, self.dependencies)
        write_tsv(self.canon / "EVIDENCE.tsv", EVIDENCE_FIELDS, self.evidence)
        write_tsv(self.canon / "HISTORY.tsv", HISTORY_FIELDS, self.history)
        write_tsv(self.canon / "GATES.tsv", GATE_FIELDS, self.gates)
        write_tsv(
            self.canon / "CORE_SELECTION.tsv",
            CORE_SELECTION_FIELDS,
            self.core_selection,
        )


class LedgerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.fixture = LedgerFixture(self.root)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_valid_snapshot(self) -> None:
        self.fixture.write()
        snapshot = validate(self.root)
        self.assertEqual(snapshot.claims, 2)

    def test_theorem_cannot_require_obligation(self) -> None:
        self.fixture.dependencies.append({"item_id": "T-CLAIM", "depends_on": "O-CLAIM", "relation": "REQUIRES", "basis": "invalid lower status dependency"})
        self.fixture.write()
        with self.assertRaisesRegex(LedgerError, "theorem T-CLAIM requires lower-status"):
            validate(self.root)

    def test_cycle_is_rejected(self) -> None:
        self.fixture.dependencies.append({"item_id": "DEF-FIXTURE", "depends_on": "T-CLAIM", "relation": "REQUIRES", "basis": "invalid reverse edge"})
        self.fixture.write()
        with self.assertRaisesRegex(LedgerError, "contains a cycle"):
            validate(self.root)

    def test_evidence_hash_is_pinned(self) -> None:
        self.fixture.evidence[0]["sha256"] = "0" * 64
        self.fixture.write()
        with self.assertRaisesRegex(LedgerError, "invalid inline evidence hash"):
            validate(self.root)

    def test_every_claim_needs_history(self) -> None:
        self.fixture.history.pop()
        self.fixture.write()
        with self.assertRaisesRegex(LedgerError, "HISTORY.tsv lacks claims: O-CLAIM"):
            validate(self.root)

    def test_retired_claim_can_leave_current_registry(self) -> None:
        retired = self.fixture.history.pop()
        self.fixture.registry.pop()
        self.fixture.normative.pop()
        self.fixture.dependencies.pop()
        self.fixture.evidence.pop()
        self.fixture.gates = []
        self.fixture.core_selection = [{"rank": "1", "claim_id": "T-CLAIM"}]
        retired.update({
            "event_sequence": "2", "event_type": "RETIRE",
            "previous_status": "O", "new_status": "RETIRED",
            "rationale": "fixture retirement",
        })
        declaration = dict(retired)
        declaration.update({
            "event_id": "GENESIS-O-CLAIM", "event_sequence": "1",
            "event_type": "DECLARE", "previous_status": "-", "new_status": "O",
            "rationale": "fixture declaration",
        })
        retired["event_id"] = "RETIRE-O-CLAIM"
        self.fixture.history.extend((declaration, retired))
        self.fixture.write()
        self.assertEqual(validate(self.root).claims, 1)

    def test_evidence_change_preserves_historical_hash(self) -> None:
        current = self.fixture.evidence[0]
        old_hash = current["sha256"]
        current["evidence_id"] = "EV-T-CLAIM-V2"
        latest = dict(self.fixture.history[0])
        latest.update({
            "event_id": "EVIDENCE-T-CLAIM-2", "event_sequence": "2",
            "event_type": "EVIDENCE_CHANGE", "previous_status": "T",
            "new_status": "T", "evidence_id": "EV-T-CLAIM-V2",
            "evidence_sha256": current["sha256"],
            "rationale": "fixture evidence replacement",
        })
        self.fixture.history.append(latest)
        self.fixture.write()
        validate(self.root)
        self.assertEqual(self.fixture.history[0]["evidence_sha256"], old_hash)

    def test_core_selection_is_unique(self) -> None:
        self.fixture.core_selection.append({"rank": "2", "claim_id": "T-CLAIM"})
        self.fixture.write()
        with self.assertRaisesRegex(LedgerError, "CORE_SELECTION.tsv duplicates T-CLAIM"):
            validate(self.root)

    def test_cross_layer_dependency_needs_matching_gate(self) -> None:
        self.fixture.normative[2]["layer"] = "L2"
        self.fixture.normative[2]["gate_ids"] = ""
        self.fixture.gates = []
        self.fixture.write()
        with self.assertRaisesRegex(LedgerError, "cross-layer dependency"):
            validate(self.root)


if __name__ == "__main__":
    unittest.main()
