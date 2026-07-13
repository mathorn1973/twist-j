#!/usr/bin/env python3
"""Tests for the parallel aarch64 Genesis artifact interface."""

from __future__ import annotations

import csv
from pathlib import Path
import tempfile
import unittest

from tools.genesis_artifacts import (
    ENGINEERING_FIELDS,
    ENGINEERING_ITEMS,
    EXTERNAL_SOURCE_FIELDS,
    FRONTIER_SPLIT_FIELDS,
    GenesisArtifactError,
    PREREG_FIELDS,
    PREREG_FILES,
    RECONSTRUCTION_FIELDS,
    RECON_ITEMS,
    SPLIT_COUNTS,
    validate_prereg,
    validate_recon,
    validate_sources,
)


REGISTRY_FIELDS = (
    "claim_id", "status", "scope", "canon_section", "evidence", "falsifier"
)


def write_tsv(path: Path, fields: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


class GenesisFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        claims = sorted(RECON_ITEMS | set(SPLIT_COUNTS))
        (root / "canon").mkdir(parents=True)
        (root / "canon" / "CANON.md").write_text("# Fixture\n", encoding="utf-8")
        write_tsv(
            root / "canon" / "REGISTRY.tsv",
            REGISTRY_FIELDS,
            [
                {"claim_id": claim, "status": "O", "scope": "fixture scope", "canon_section": "Fixture", "evidence": "inline", "falsifier": "fixture decision condition is exact and public"}
                for claim in claims
            ],
        )
        self.recon = [
            {
                "item_id": item,
                "current_claim_id": item,
                "action": "KEEP_PRECISE_H" if item == "KERNEL-CONNECT-ALL-K" else "KEEP_PRECISE_O",
                "public_statement": f"Public executable statement for {item}",
                "evidence_required": "A named public equation and exact decision witness",
                "post_genesis_probe": f"P-{item}",
                "blocker": "No formal probe may run before Public Canon v1 activation",
            }
            for item in sorted(RECON_ITEMS)
        ]
        self.splits: list[dict[str, str]] = []
        for parent, count in SPLIT_COUNTS.items():
            for index in range(1, count + 1):
                self.splits.append({
                    "parent_id": parent,
                    "child_id": f"{parent}-CHILD-{index}",
                    "child_status": "O",
                    "layer": "NOT_APPLICABLE",
                    "decision_condition": "closes positively by the named exact gate and negatively by an exact counterexample",
                    "dependencies": "-",
                })
        self.sources = [{
            "source_id": "SRC-FIXTURE",
            "observable": "fixture observable",
            "source_title": "Fixture public record",
            "edition": "2026",
            "DOI_or_record": "record:fixture",
            "value": "1",
            "uncertainty": "0",
            "units": "dimensionless",
            "scheme": "fixture",
            "access_date": "2026-07-13",
            "local_hash": "NOT-LOCAL",
            "license": "public record metadata only",
        }]
        self.engineering = [
            {
                "item_id": item,
                "canon_locator": "Fixture",
                "observable": "fixture observable",
                "value": "fixture value",
                "source_id": "SRC-FIXTURE",
                "action": "KEEP_MEASURED",
                "evidence_path": "-",
                "rationale": "Fixture retains a measured comparison with an explicit source",
            }
            for item in sorted(ENGINEERING_ITEMS)
        ]

    def write_recon(self) -> None:
        directory = self.root / "notes" / "genesis" / "recon"
        write_tsv(directory / "RECONSTRUCTION.tsv", RECONSTRUCTION_FIELDS, self.recon)
        write_tsv(directory / "FRONTIER_SPLITS.tsv", FRONTIER_SPLIT_FIELDS, self.splits)

    def write_sources(self) -> None:
        write_tsv(self.root / "data" / "EXTERNAL_SOURCES.tsv", EXTERNAL_SOURCE_FIELDS, self.sources)
        write_tsv(self.root / "data" / "ENGINEERING_DISPOSITION.tsv", ENGINEERING_FIELDS, self.engineering)

    def write_prereg(self) -> None:
        directory = self.root / "notes" / "prereg" / "post-genesis"
        directory.mkdir(parents=True)
        fields = "\n".join(f"**{field}:** fixed fixture value" for field in PREREG_FIELDS)
        for name in PREREG_FILES:
            (directory / name).write_text(
                f"# NON-CANONICAL PREREGISTRATION DRAFT\n\n{fields}\n",
                encoding="utf-8",
            )


class GenesisArtifactTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.fixture = GenesisFixture(self.root)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_complete_package_passes(self) -> None:
        self.fixture.write_recon()
        self.fixture.write_sources()
        self.fixture.write_prereg()
        self.assertEqual(validate_recon(self.root), (9, 19))
        self.assertEqual(validate_sources(self.root), (1, 9))
        self.assertEqual(validate_prereg(self.root), 6)

    def test_missing_reconstruction_decision_fails(self) -> None:
        self.fixture.recon.pop()
        self.fixture.write_recon()
        with self.assertRaisesRegex(GenesisArtifactError, "RECONSTRUCTION.tsv lacks"):
            validate_recon(self.root)

    def test_genesis_split_cannot_promote(self) -> None:
        self.fixture.splits[0]["child_status"] = "T"
        self.fixture.write_recon()
        with self.assertRaisesRegex(GenesisArtifactError, "must remain H or O"):
            validate_recon(self.root)

    def test_retired_reconstruction_item_must_leave_registry(self) -> None:
        self.fixture.recon[0]["action"] = "RETIRE"
        self.fixture.recon[0]["current_claim_id"] = "-"
        self.fixture.write_recon()
        with self.assertRaisesRegex(GenesisArtifactError, "must leave no current claim"):
            validate_recon(self.root)

    def test_retained_measurement_needs_source(self) -> None:
        self.fixture.engineering[0]["source_id"] = "SRC-MISSING"
        self.fixture.write_sources()
        with self.assertRaisesRegex(GenesisArtifactError, "retained without valid source_id"):
            validate_sources(self.root)

    def test_preregistration_cannot_contain_result(self) -> None:
        self.fixture.write_prereg()
        target = self.root / "notes" / "prereg" / "post-genesis" / "01-curvature.md"
        target.write_text(target.read_text(encoding="utf-8") + "\n**Result:** forbidden\n", encoding="utf-8")
        with self.assertRaisesRegex(GenesisArtifactError, "contains a result"):
            validate_prereg(self.root)


if __name__ == "__main__":
    unittest.main()
