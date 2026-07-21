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
    FRONTIER_PROGRAM_FIELDS,
    GATE_FIELDS,
    HISTORY_FIELDS,
    LedgerError,
    NORMATIVE_FIELDS,
    REGISTRY_FIELDS,
    bundle_sha256,
    validate_frontier_programs,
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
        (self.canon / "CANON.md").write_text(
            "# TWIST-J Public Canon v1\nFixture. T-CLAIM [T]. O-CLAIM [O].\n",
            encoding="utf-8",
        )
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
        self.evidence = [
            {
                "claim_id": row["claim_id"],
                "evidence_id": f"EV-{row['claim_id']}",
                "evidence_kind": "INLINE_CANON",
                "location": "inline",
                "sha256": hashlib.sha256(row["scope"].encode()).hexdigest(),
                "hash_mode": "registry-scope-sha256-v1",
                "architecture_requirement": "none",
            }
            for row in self.registry
        ]
        self.history = []
        for claim, status, scope in (("T-CLAIM", "T", scope_t), ("O-CLAIM", "O", scope_o)):
            self.history.append({
                "event_id": f"GENESIS-{claim}", "event_sequence": "1", "event_date": "2026-07-13", "release": "canon-v1-genesis", "claim_id": claim,
                "event_type": "DECLARE", "previous_status": "-", "new_status": status,
                "scope_sha256": hashlib.sha256(scope.encode()).hexdigest(), "evidence_id": f"EV-{claim}",
                "evidence_location": "inline",
                "evidence_sha256": hashlib.sha256(scope.encode()).hexdigest(),
                "rationale": "fixture declaration",
            })
        self.gates = [{
            "gate_id": "GATE-FIXTURE", "owner_item_id": "O-CLAIM", "from_layer": "L1", "to_layer": "L2",
            "gate_kind": "OPEN_LIFT", "decision_condition": "closes positively by a fixture and negatively by its exact counterexample",
        }]
        self.core_selection = [
            {"rank": "1", "claim_id": "T-CLAIM"},
        ]
        self.frontier_programs = [{
            "claim_id": "O-CLAIM",
            "program_id": "DECODER_CORE",
            "queue_role": "ROOT",
            "work_state": "READY",
            "work_mode": "FORMAL",
        }]

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
        write_tsv(
            self.canon / "FRONTIER_PROGRAMS.tsv",
            FRONTIER_PROGRAM_FIELDS,
            self.frontier_programs,
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
        self.assertEqual(snapshot.frontier_programs, 1)

    def test_frontier_programs_must_cover_every_live_claim(self) -> None:
        registry = {"O-CLAIM": {"status": "O"}}
        with self.assertRaisesRegex(LedgerError, "lacks live claims: O-CLAIM"):
            validate_frontier_programs([], registry)

    def test_frontier_programs_reject_unknown_closed_and_duplicate_claims(self) -> None:
        base = {
            "claim_id": "O-CLAIM", "program_id": "DECODER_CORE",
            "queue_role": "ROOT", "work_state": "READY", "work_mode": "FORMAL",
        }
        registry = {"O-CLAIM": {"status": "O"}, "T-CLAIM": {"status": "T"}}
        with self.assertRaisesRegex(LedgerError, "unknown claim UNKNOWN"):
            validate_frontier_programs([dict(base, claim_id="UNKNOWN")], registry)
        with self.assertRaisesRegex(LedgerError, "non-live claim T-CLAIM"):
            validate_frontier_programs([dict(base, claim_id="T-CLAIM")], registry)
        with self.assertRaisesRegex(LedgerError, "duplicates O-CLAIM"):
            validate_frontier_programs([base, dict(base)], registry)

    def test_frontier_programs_require_closed_enums(self) -> None:
        base = {
            "claim_id": "O-CLAIM", "program_id": "DECODER_CORE",
            "queue_role": "ROOT", "work_state": "READY", "work_mode": "FORMAL",
        }
        registry = {"O-CLAIM": {"status": "O"}}
        cases = (
            ("program_id", "UNKNOWN_PROGRAM"),
            ("queue_role", "LEAF"),
            ("work_state", "RUNNING"),
            ("work_mode", "NUMERICAL"),
        )
        for field, value in cases:
            with self.subTest(field=field):
                with self.assertRaisesRegex(LedgerError, f"invalid {field}"):
                    validate_frontier_programs([dict(base, **{field: value})], registry)

    def test_frontier_program_rows_are_claim_sorted(self) -> None:
        registry = {
            "A-OPEN": {"status": "O"},
            "B-HYP": {"status": "H"},
        }
        rows = [
            {"claim_id": claim, "program_id": "MEASURE", "queue_role": "ROOT",
             "work_state": "READY", "work_mode": "FORMAL"}
            for claim in ("B-HYP", "A-OPEN")
        ]
        with self.assertRaisesRegex(LedgerError, "sorted by claim_id"):
            validate_frontier_programs(rows, registry)

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

    def test_unrelated_canon_edit_does_not_change_inline_evidence(self) -> None:
        self.fixture.write()
        canon = self.fixture.canon / "CANON.md"
        canon.write_text(
            canon.read_text(encoding="utf-8") + "Unrelated release prose.\n",
            encoding="utf-8",
        )
        self.assertEqual(validate(self.root).claims, 2)

    def test_scope_change_requires_evidence_and_history_update(self) -> None:
        self.fixture.registry[0]["scope"] = "revised exact fixture theorem"
        self.fixture.write()
        with self.assertRaisesRegex(LedgerError, "invalid inline evidence hash"):
            validate(self.root)

        digest = hashlib.sha256(
            self.fixture.registry[0]["scope"].encode()
        ).hexdigest()
        self.fixture.evidence[0]["sha256"] = digest
        self.fixture.write()
        with self.assertRaisesRegex(LedgerError, "latest scope differs"):
            validate(self.root)

        latest = dict(self.fixture.history[0])
        latest.update({
            "event_id": "SCOPE-T-CLAIM-2",
            "event_sequence": "2",
            "event_type": "SCOPE_CHANGE",
            "previous_status": "T",
            "new_status": "T",
            "scope_sha256": digest,
            "evidence_sha256": digest,
            "rationale": "fixture scope correction",
        })
        self.fixture.history.append(latest)
        self.fixture.write()
        self.assertEqual(validate(self.root).claims, 2)

    def test_public_probe_is_a_five_file_evidence_bundle(self) -> None:
        location = "probes/P-FIXTURE-1"
        probe = self.root / location
        probe.mkdir(parents=True)
        for name in ("PREREG.md", "verify.py", "EXPECTED.txt", "RUN.md", "RESULT.md"):
            (probe / name).write_text(f"{name}\n", encoding="utf-8")
        digest = bundle_sha256(probe, self.root)
        self.fixture.registry[1]["evidence"] = location
        self.fixture.evidence[1] = {
            "claim_id": "O-CLAIM",
            "evidence_id": "EV-O-CLAIM",
            "evidence_kind": "PUBLIC_PROBE",
            "location": location,
            "sha256": digest,
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture_requirement": "two-architecture",
        }
        self.fixture.history[1]["evidence_location"] = location
        self.fixture.history[1]["evidence_sha256"] = digest
        self.fixture.write()
        self.assertEqual(validate(self.root).claims, 2)

    def test_bundle_hash_uses_case_sensitive_posix_path_order(self) -> None:
        bundle = self.root / "bundle"
        bundle.mkdir()
        upper = bundle / "B.txt"
        lower = bundle / "a.txt"
        upper.write_bytes(b"upper\n")
        lower.write_bytes(b"lower\n")
        manifest = "".join(
            f"{hashlib.sha256(path.read_bytes()).hexdigest()}  "
            f"{path.relative_to(self.root).as_posix()}\n"
            for path in (upper, lower)
        ).encode("utf-8")
        self.assertEqual(
            bundle_sha256(bundle, self.root), hashlib.sha256(manifest).hexdigest()
        )

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
        self.fixture.frontier_programs = []
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
        old_hash = hashlib.sha256((self.fixture.canon / "CANON.md").read_bytes()).hexdigest()
        self.fixture.history[0]["evidence_sha256"] = old_hash
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
