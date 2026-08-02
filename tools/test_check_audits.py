#!/usr/bin/env python3
"""Positive and adversarial tests for supplemental public Lean audits."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from tools.check_audits import (
    AUDIT_FIELDS,
    AXIOM_FIELDS,
    AuditError,
    COVERAGE_FIELDS,
    DEPENDENCY_FIELDS,
    EVENT_FIELDS,
    records_sha256,
    source_sha256,
    validate,
    validate_events,
)


def write_tsv(path: Path, fields: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


class AuditFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.scope = "closed theorem fixture"
        self.revision = "1" * 40
        self.dependency_source = "https://github.com/leanprover-community/mathlib4.git"
        self._git("init", "--quiet", "--initial-branch=main")
        self._git("config", "user.name", "A. M. Thorn")
        self._git("config", "user.email", "thorn@twistj.com")
        self._git("config", "core.autocrlf", "false")
        self._write_canon()
        self._git("add", ".")
        self._git("commit", "--quiet", "-m", "fixture Canon content")
        self.content_commit = self._head()
        self._write_status(self.content_commit)
        self._git("add", "STATUS.md")
        self._git("commit", "--quiet", "-m", "fixture Canon activation")
        self._git("tag", "canon-v31")
        audits = self.root / "audits"
        audits.mkdir()
        (audits / "README.md").write_text("# Audits\n", encoding="utf-8")
        write_tsv(audits / "INDEX.tsv", AUDIT_FIELDS, [])
        write_tsv(audits / "EVENTS.tsv", EVENT_FIELDS, [])
        self._git("add", ".")
        self._git("commit", "--quiet", "-m", "add audit policy")
        self.base_commit = self._head()

    def _git(self, *arguments: str) -> str:
        completed = subprocess.run(
            ["git", *arguments], cwd=self.root, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
        )
        return completed.stdout.strip()

    def _head(self) -> str:
        return self._git("rev-parse", "HEAD")

    def _write_status(self, content_commit: str) -> None:
        (self.root / "STATUS.md").write_text(
            "STATE: ACTIVE\nCANON: Public Canon v31\n"
            "AUTHORITY: mathorn1973/twist-j main\nCUTOVER: 2026-08-02\n"
            f"TAG: canon-v31\nCONTENT_COMMIT: {content_commit}\n"
            f"CANON_SHA256: {'a' * 64}\nCANON_BYTES: 1\n",
            encoding="utf-8",
        )

    def _write_canon(self) -> None:
        canon = self.root / "canon"
        registry = [
            {
                "claim_id": "T-CLAIM", "status": "T", "scope": self.scope,
                "canon_section": "Fixture", "evidence": "inline", "falsifier": "",
            },
            {
                "claim_id": "C-CLAIM", "status": "C", "scope": "computed fixture",
                "canon_section": "Fixture", "evidence": "inline", "falsifier": "",
            },
        ]
        write_tsv(
            canon / "REGISTRY.tsv",
            ("claim_id", "status", "scope", "canon_section", "evidence", "falsifier"),
            registry,
        )
        write_tsv(
            canon / "EVIDENCE.tsv", ("claim_id", "location"),
            [{"claim_id": row["claim_id"], "location": "inline"} for row in registry],
        )
        write_tsv(
            canon / "HISTORY.tsv", ("claim_id", "evidence_location"),
            [{"claim_id": row["claim_id"], "evidence_location": "inline"} for row in registry],
        )
        self._write_status("0" * 40)

    def _write_index(self, rows: list[dict[str, str]]) -> None:
        write_tsv(self.root / "audits" / "INDEX.tsv", AUDIT_FIELDS, rows)

    def _write_events(self, rows: list[dict[str, str]]) -> None:
        write_tsv(self.root / "audits" / "EVENTS.tsv", EVENT_FIELDS, rows)

    def add_audit(
        self,
        *,
        audit_id: str = "A-LEAN-FIXTURE",
        claim: str = "T-CLAIM",
        coverage: str = "PARTIAL",
        exclusion: str | None = None,
        proof: str | None = None,
        lakefile: str | None = None,
        command: str = "lake env lean Audit.lean",
        unrelated_path: bool = False,
        accepted_axioms: str = "NONE",
        include_transitive: bool = False,
    ) -> tuple[Path, dict[str, str], str]:
        package = self.root / "audits" / "lean" / audit_id
        package.mkdir(parents=True)
        (package / "README.md").write_text(
            "# Fixture\n\nStatus: SUPPLEMENTAL PUBLIC AUDIT\n\n"
            "## Scope\nFixture.\n\n## Trust boundary\nKernel.\n\n"
            f"## Accepted axioms\n{accepted_axioms}\n\n"
            "## Dependency provenance\nSee DEPENDENCIES.tsv.\n\n"
            "## Upstream closure\n"
            "https://github.com/leanprover-community/mathlib4/blob/"
            f"{self.revision}/lake-manifest.json\n",
            encoding="utf-8",
        )
        if exclusion is None:
            exclusion = "remaining prose bridge" if coverage == "PARTIAL" else "NONE"
        write_tsv(
            package / "COVERAGE.tsv", COVERAGE_FIELDS,
            [{
                "claim_id": claim, "theorem_name": "auditedClaim",
                "covered_statement": "True in the fixture model",
                "unformalized_scope": exclusion,
            }],
        )
        dependency_rows = [{
            "name": "mathlib", "source": self.dependency_source,
            "revision": self.revision, "license": "Apache-2.0",
        }]
        manifest_packages = [{
            "name": "mathlib",
            "type": "git",
            "url": self.dependency_source,
            "rev": self.revision,
            "inputRev": self.revision,
            "subDir": None,
            "scope": "leanprover-community",
            "manifestFile": "lake-manifest.json",
            "inherited": False,
            "configFile": "lakefile.toml",
        }]
        upstream_packages: list[dict[str, object]] = []
        if include_transitive:
            transitive_source = "https://github.com/leanprover-community/batteries"
            transitive_revision = "2" * 40
            dependency_rows.insert(0, {
                "name": "batteries", "source": transitive_source,
                "revision": transitive_revision, "license": "Apache-2.0",
            })
            manifest_packages.append({
                "name": "batteries",
                "type": "git",
                "url": transitive_source,
                "rev": transitive_revision,
                "inputRev": "main",
                "subDir": None,
                "scope": "leanprover-community",
                "manifestFile": "lake-manifest.json",
                "inherited": True,
                "configFile": "lakefile.toml",
            })
            upstream_packages.append({**manifest_packages[-1], "inherited": False})
        write_tsv(package / "DEPENDENCIES.tsv", DEPENDENCY_FIELDS, dependency_rows)
        (package / "lean-toolchain").write_text("leanprover/lean4:v4.30.0\n", encoding="utf-8")
        if lakefile is None:
            lakefile = (
                'name = "FixtureAudit"\nversion = "0.1.0"\n'
                'defaultTargets = ["LeanAudit"]\n\n'
                '[[require]]\nname = "mathlib"\n'
                f'git = "{self.dependency_source}"\nrev = "{self.revision}"\n\n'
                '[[lean_lib]]\nname = "LeanAudit"\n'
            )
        (package / "lakefile.toml").write_text(lakefile, encoding="utf-8")
        (package / "lake-manifest.json").write_text(
            json.dumps({
                "version": "1.2.0",
                "packagesDir": ".lake/packages",
                "packages": manifest_packages,
                "name": "FixtureAudit",
                "lakeDir": ".lake",
                "fixedToolchain": False,
            }) + "\n",
            encoding="utf-8",
        )
        (package / "MATHLIB-MANIFEST.json").write_text(
            json.dumps({
                "version": "1.2.0",
                "packagesDir": ".lake/packages",
                "packages": upstream_packages,
                "name": "mathlib",
                "lakeDir": ".lake",
                "fixedToolchain": False,
            }) + "\n",
            encoding="utf-8",
        )
        if proof is None:
            proof = (
                "set_option autoImplicit false\n"
                "theorem auditedClaim : True := by trivial\n"
                "#print axioms auditedClaim\n"
            )
        (package / "Audit.lean").write_text(proof, encoding="utf-8")
        self._git("add", ".")
        self._git("commit", "--quiet", "-m", f"pin source for {audit_id}")
        source_commit = self._head()
        source_digest = source_sha256(package, self.root)

        expected = b"auditedClaim depends on axioms: []\n"
        (package / "EXPECTED.txt").write_bytes(expected)
        write_tsv(
            package / "AXIOMS.tsv", AXIOM_FIELDS,
            [{"theorem_name": "auditedClaim", "axioms": "NONE"}],
        )
        (package / "RUN.md").write_text(
            f"source_commit: {source_commit}\n"
            f"source_sha256: {source_digest}\n"
            f"working_directory: audits/lean/{audit_id}\n"
            f"command: {command}\n"
            "exit_code: 0\n"
            f"stdout_sha256: {hashlib.sha256(expected).hexdigest()}\n"
            f"stdout_bytes: {len(expected)}\n"
            "stderr_bytes: 0\n"
            "platform: Ubuntu 24.04\n"
            "architecture: x86_64\n"
            "lean_version: 4.30.0\n"
            "lake_version: 5.0.0\n"
            "clean_before: true\n"
            "clean_after: true\n"
            "fresh_clone: true\n"
            "lake_state_before_fetch: absent\n"
            "dependency_checkouts_verified: true\n"
            "network: disabled\n"
            "secrets: none\n",
            encoding="utf-8",
        )
        (package / "RESULT.md").write_text(
            f"audit_id: {audit_id}\nresult: RECORDED_PASS\nclaim_effect: NONE\n",
            encoding="utf-8",
        )
        scope = self.scope if claim == "T-CLAIM" else "computed fixture"
        row = {
            "audit_id": audit_id,
            "audit_kind": "LEAN4",
            "profile": "LEAN4-RECORDED-V1",
            "claim_id": claim,
            "coverage": coverage,
            "status_effect": "NONE",
            "canon_tag": "canon-v31",
            "content_commit": self.content_commit,
            "claim_scope_sha256": hashlib.sha256(scope.encode()).hexdigest(),
            "location": f"audits/lean/{audit_id}",
            "source_commit": source_commit,
            "source_sha256": source_digest,
            "records_sha256": records_sha256(package, self.root),
            "hash_mode": "lean-audit-source-sha256-v1",
        }
        self._write_index([row])
        if unrelated_path:
            (self.root / "unrelated.txt").write_text("not allowed\n", encoding="utf-8")
        self._git("add", ".")
        self._git("commit", "--quiet", "-m", f"record {audit_id}")
        return package, row, self._head()

    def add_event(
        self,
        audit_id: str,
        *,
        event_id: str = "AE-FIXTURE-WITHDRAWN",
        event_type: str = "WITHDRAWN",
        replacement: str = "-",
        unrelated_path: bool = False,
    ) -> str:
        self._write_events([{
            "event_id": event_id,
            "event_sequence": "1",
            "audit_id": audit_id,
            "event_type": event_type,
            "event_date": "2026-08-02",
            "reason": "Independent review found a semantic translation defect.",
            "replacement_audit_id": replacement,
        }])
        if unrelated_path:
            (self.root / "unrelated.txt").write_text("not allowed\n", encoding="utf-8")
        self._git("add", ".")
        self._git("commit", "--quiet", "-m", f"qualify {audit_id}")
        return self._head()


class AuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.fixture = AuditFixture(self.root)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_empty_index_is_valid(self) -> None:
        self.assertEqual(validate(self.root, self.fixture.base_commit), 0)

    def test_release_pinned_partial_audit_is_valid(self) -> None:
        self.fixture.add_audit()
        self.assertEqual(validate(self.root, self.fixture.base_commit), 1)

    def test_manifest_profile_accepts_pinned_inherited_dependencies(self) -> None:
        self.fixture.add_audit(include_transitive=True)
        self.assertEqual(validate(self.root, self.fixture.base_commit), 1)

    def test_source_commit_must_exist(self) -> None:
        _, row, _ = self.fixture.add_audit()
        row["source_commit"] = "f" * 40
        self.fixture._write_index([row])
        with self.assertRaisesRegex(AuditError, "does not exist"):
            validate(self.root, self.fixture.base_commit)

    def test_source_pin_must_descend_from_pinned_canon_tag(self) -> None:
        _, row, _ = self.fixture.add_audit()
        row["source_commit"] = self.fixture.content_commit
        self.fixture._write_index([row])
        with self.assertRaisesRegex(AuditError, "Canon tag at source pin"):
            validate(self.root, self.fixture.base_commit)

    def test_source_tree_is_bound_to_pre_run_commit(self) -> None:
        package, _, _ = self.fixture.add_audit()
        with (package / "Audit.lean").open("a", encoding="utf-8") as handle:
            handle.write("Changed translation basis.\n")
        with self.assertRaisesRegex(AuditError, "current source differs"):
            validate(self.root, self.fixture.base_commit)

    def test_canon_tag_and_historical_theorem_are_verified(self) -> None:
        self.fixture.add_audit(claim="C-CLAIM")
        with self.assertRaisesRegex(AuditError, "does not map a theorem claim"):
            validate(self.root, self.fixture.base_commit)

    def test_scope_hash_is_bound_to_pinned_canon(self) -> None:
        _, row, _ = self.fixture.add_audit()
        row["claim_scope_sha256"] = "0" * 64
        self.fixture._write_index([row])
        with self.assertRaisesRegex(AuditError, "scope hash differs"):
            validate(self.root, self.fixture.base_commit)

    def test_private_axiom_is_rejected(self) -> None:
        proof = (
            "set_option autoImplicit false\n"
            "private axiom cheat : False\n"
            "theorem auditedClaim : True := by trivial\n"
            "#print axioms auditedClaim\n"
        )
        self.fixture.add_audit(proof=proof)
        with self.assertRaisesRegex(AuditError, "package-local axiom"):
            validate(self.root, self.fixture.base_commit)

    def test_auto_implicit_false_must_be_global(self) -> None:
        proof = (
            "set_option autoImplicit false in\n"
            "theorem helper : True := by trivial\n"
            "theorem auditedClaim : True := by trivial\n"
            "#print axioms auditedClaim\n"
        )
        self.fixture.add_audit(proof=proof)
        with self.assertRaisesRegex(AuditError, "global standalone command"):
            validate(self.root, self.fixture.base_commit)

    def test_auto_implicit_false_must_precede_declarations(self) -> None:
        proof = (
            "theorem helper : True := by trivial\n"
            "set_option autoImplicit false\n"
            "theorem auditedClaim : True := by trivial\n"
            "#print axioms auditedClaim\n"
        )
        self.fixture.add_audit(proof=proof)
        with self.assertRaisesRegex(AuditError, "before declarations"):
            validate(self.root, self.fixture.base_commit)

    def test_comments_cannot_hide_auto_implicit_reenable(self) -> None:
        proof = (
            "set_option autoImplicit false\n"
            "set_option/- hidden separator -/autoImplicit true\n"
            "theorem auditedClaim : True := by trivial\n"
            "#print axioms auditedClaim\n"
        )
        self.fixture.add_audit(proof=proof)
        with self.assertRaisesRegex(AuditError, "must not re-enable autoImplicit"):
            validate(self.root, self.fixture.base_commit)

    def test_syntax_quotation_cannot_spoof_axiom_output(self) -> None:
        proof = (
            "set_option autoImplicit false\n"
            "def fake := `(term| True)\n"
            "theorem auditedClaim : True := by trivial\n"
            "#print axioms auditedClaim\n"
        )
        self.fixture.add_audit(proof=proof)
        with self.assertRaisesRegex(AuditError, "syntax quotation"):
            validate(self.root, self.fixture.base_commit)

    def test_execution_command_is_rejected(self) -> None:
        proof = (
            "set_option autoImplicit false\n"
            "#eval (1 + 1)\n"
            "theorem auditedClaim : True := by trivial\n"
            "#print axioms auditedClaim\n"
        )
        self.fixture.add_audit(proof=proof)
        with self.assertRaisesRegex(AuditError, "output or execution command"):
            validate(self.root, self.fixture.base_commit)

    def test_custom_notation_is_rejected(self) -> None:
        proof = (
            "set_option autoImplicit false\n"
            "notation \"truth\" => True\n"
            "theorem auditedClaim : True := by trivial\n"
            "#print axioms auditedClaim\n"
        )
        self.fixture.add_audit(proof=proof)
        with self.assertRaisesRegex(AuditError, "metaprogramming"):
            validate(self.root, self.fixture.base_commit)

    def test_arbitrary_hash_command_is_rejected(self) -> None:
        proof = (
            "set_option autoImplicit false\n"
            "#unknown\n"
            "theorem auditedClaim : True := by trivial\n"
            "#print axioms auditedClaim\n"
        )
        self.fixture.add_audit(proof=proof)
        with self.assertRaisesRegex(AuditError, "top-level exact #print axioms"):
            validate(self.root, self.fixture.base_commit)

    def test_same_line_hash_command_is_rejected(self) -> None:
        proof = (
            "set_option autoImplicit false\n"
            "def helper : Nat := 1 #unknown\n"
            "theorem auditedClaim : True := by trivial\n"
            "#print axioms auditedClaim\n"
        )
        self.fixture.add_audit(proof=proof)
        with self.assertRaisesRegex(AuditError, "top-level exact #print axioms"):
            validate(self.root, self.fixture.base_commit)

    def test_path_dependency_is_rejected_by_strict_toml_profile(self) -> None:
        lakefile = (
            'name = "FixtureAudit"\nversion = "0.1.0"\n'
            'defaultTargets = ["LeanAudit"]\n\n'
            '[[require]]\nname = "evil"\npath = "../evil"\n\n'
            '[[lean_lib]]\nname = "LeanAudit"\n'
        )
        self.fixture.add_audit(lakefile=lakefile)
        with self.assertRaisesRegex(AuditError, "unsupported dependency declaration"):
            validate(self.root, self.fixture.base_commit)

    def test_non_public_dependency_host_is_rejected(self) -> None:
        self.fixture.dependency_source = "https://localhost/mathlib/mathlib4.git"
        self.fixture.add_audit()
        with self.assertRaisesRegex(AuditError, "public full-SHA git pin"):
            validate(self.root, self.fixture.base_commit)

    def test_entrypoint_command_is_exact(self) -> None:
        self.fixture.add_audit(command="lake build")
        with self.assertRaisesRegex(AuditError, "command must be"):
            validate(self.root, self.fixture.base_commit)

    def test_exact_coverage_cannot_hide_an_exclusion(self) -> None:
        self.fixture.add_audit(coverage="EXACT", exclusion="untranslated bridge")
        with self.assertRaisesRegex(AuditError, "EXACT coverage"):
            validate(self.root, self.fixture.base_commit)

    def test_result_record_rejects_overclaim_prose(self) -> None:
        package, row, _ = self.fixture.add_audit()
        with (package / "RESULT.md").open("a", encoding="utf-8") as handle:
            handle.write("This establishes T-LOCK.\n")
        row["records_sha256"] = records_sha256(package, self.root)
        self.fixture._write_index([row])
        with self.assertRaisesRegex(AuditError, "not a structured field"):
            validate(self.root, self.fixture.base_commit)

    def test_records_digest_detects_run_mutation(self) -> None:
        package, _, _ = self.fixture.add_audit()
        with (package / "RUN.md").open("a", encoding="utf-8") as handle:
            handle.write("\n")
        with self.assertRaisesRegex(AuditError, "records hash differs"):
            validate(self.root, self.fixture.base_commit)

    def test_existing_audit_row_is_immutable(self) -> None:
        package, row, audit_commit = self.fixture.add_audit()
        run = package / "RUN.md"
        run.write_text(
            run.read_text(encoding="utf-8").replace(
                "platform: Ubuntu 24.04", "platform: Ubuntu 24.04.1"
            ),
            encoding="utf-8",
        )
        row["records_sha256"] = records_sha256(package, self.root)
        self.fixture._write_index([row])
        self.fixture._git("add", ".")
        self.fixture._git("commit", "--quiet", "-m", "attempt rewrite")
        with self.assertRaisesRegex(AuditError, "sealed audit rows are immutable"):
            validate(self.root, audit_commit)

    def test_audit_pull_request_cannot_change_unrelated_paths(self) -> None:
        self.fixture.add_audit(unrelated_path=True)
        with self.assertRaisesRegex(AuditError, "unrelated paths"):
            validate(self.root, self.fixture.base_commit)

    def test_audit_lane_has_exactly_two_commits(self) -> None:
        self.fixture.add_audit()
        self.fixture._git("commit", "--allow-empty", "--quiet", "-m", "third audit commit")
        with self.assertRaisesRegex(AuditError, "exactly one source commit and one record commit"):
            validate(self.root, self.fixture.base_commit)

    def test_audit_commits_cannot_be_merge_commits(self) -> None:
        _, _, audit_commit = self.fixture.add_audit()
        source_commit = self.fixture._git("rev-parse", f"{audit_commit}^")
        self.fixture._git("branch", "side", source_commit)
        self.fixture._git("checkout", "--quiet", "side")
        self.fixture._git("commit", "--allow-empty", "--quiet", "-m", "hidden side history")
        self.fixture._git("checkout", "--quiet", "main")
        self.fixture._git("merge", "--no-ff", "--quiet", "-m", "merge hidden history", "side")
        with self.assertRaisesRegex(AuditError, "must not be merge commits"):
            validate(self.root, self.fixture.base_commit)

    def test_primary_evidence_cannot_point_into_audits(self) -> None:
        evidence = self.root / "canon" / "EVIDENCE.tsv"
        variants = (
            {"evidence_id": "EV-FIXTURE", "location": "audits/lean/A-LEAN-FIXTURE"},
            {"evidence_id": "EV-FIXTURE", "location": ".\\AUDITS\\lean\\A-LEAN-FIXTURE"},
            {
                "evidence_id": "EV-FIXTURE",
                "location": "https://github.com/mathorn1973/twist-j/tree/main/audits/lean/A-LEAN-FIXTURE",
            },
            {"evidence_id": "A-LEAN-FIXTURE", "location": "external"},
            {"evidence_id": "EV-A-LEAN-FIXTURE", "location": "external"},
        )
        for record in variants:
            with self.subTest(record=record):
                write_tsv(
                    evidence, ("claim_id", "evidence_id", "location"),
                    [{"claim_id": "T-CLAIM", **record}],
                )
                with self.assertRaisesRegex(
                    AuditError, "supplemental audit as primary evidence",
                ):
                    validate(self.root, self.fixture.base_commit)

    def test_readme_axioms_must_match_structured_record(self) -> None:
        self.fixture.add_audit(accepted_axioms="Classical.choice")
        with self.assertRaisesRegex(AuditError, "accepted axioms differ"):
            validate(self.root, self.fixture.base_commit)

    def test_manifest_input_revision_must_match_resolved_revision(self) -> None:
        package, _, _ = self.fixture.add_audit()
        manifest_path = package / "lake-manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["packages"][0]["inputRev"] = "2" * 40
        manifest_path.write_text(json.dumps(manifest) + "\n", encoding="utf-8")
        with self.assertRaisesRegex(AuditError, "mutable inputRev"):
            validate(self.root, self.fixture.base_commit)

    def test_manifest_revision_must_be_a_json_string(self) -> None:
        package, _, _ = self.fixture.add_audit()
        manifest_path = package / "lake-manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["packages"][0]["rev"] = int("1" * 40)
        manifest_path.write_text(json.dumps(manifest) + "\n", encoding="utf-8")
        with self.assertRaisesRegex(AuditError, "invalid field types"):
            validate(self.root, self.fixture.base_commit)

    def test_manifest_rejects_duplicate_json_keys(self) -> None:
        package, _, _ = self.fixture.add_audit()
        manifest_path = package / "lake-manifest.json"
        text = manifest_path.read_text(encoding="utf-8").replace(
            '"version": "1.2.0",',
            '"version": "1.2.0", "version": "1.2.0",',
        )
        manifest_path.write_text(text, encoding="utf-8")
        with self.assertRaisesRegex(AuditError, "duplicates JSON key version"):
            validate(self.root, self.fixture.base_commit)

    def test_inherited_closure_must_match_mathlib_snapshot(self) -> None:
        package, _, _ = self.fixture.add_audit(include_transitive=True)
        snapshot_path = package / "MATHLIB-MANIFEST.json"
        snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
        snapshot["packages"][0]["rev"] = "3" * 40
        snapshot_path.write_text(json.dumps(snapshot) + "\n", encoding="utf-8")
        with self.assertRaisesRegex(AuditError, "differs from its Mathlib snapshot"):
            validate(self.root, self.fixture.base_commit)

    def test_tsv_rows_cannot_hide_extra_columns(self) -> None:
        self.fixture.add_audit()
        index = self.root / "audits" / "INDEX.tsv"
        lines = index.read_text(encoding="utf-8").splitlines()
        lines[1] += "\thidden"
        index.write_text("\n".join(lines) + "\n", encoding="utf-8")
        with self.assertRaisesRegex(AuditError, "wrong number of columns"):
            validate(self.root, self.fixture.base_commit)

    def test_unrelated_main_advance_does_not_invalidate_source_pin(self) -> None:
        self.fixture.add_audit()
        self.fixture._git("branch", "base-advance", self.fixture.base_commit)
        self.fixture._git("checkout", "--quiet", "base-advance")
        (self.root / "main-advance.txt").write_text("unrelated public change\n", encoding="utf-8")
        self.fixture._git("add", "main-advance.txt")
        self.fixture._git("commit", "--quiet", "-m", "advance public main")
        advanced_base = self.fixture._head()
        self.fixture._git("checkout", "--quiet", "main")
        self.fixture._git("merge", "--no-ff", "--quiet", "-m", "test merge", "base-advance")
        self.assertEqual(validate(self.root, advanced_base), 1)

    def test_withdrawal_is_append_only_and_status_neutral(self) -> None:
        _, _, audit_commit = self.fixture.add_audit()
        self.fixture.add_event("A-LEAN-FIXTURE")
        self.assertEqual(validate(self.root, audit_commit), 1)

    def test_event_cannot_name_unknown_replacement(self) -> None:
        _, _, audit_commit = self.fixture.add_audit()
        self.fixture.add_event(
            "A-LEAN-FIXTURE",
            event_id="AE-FIXTURE-SUPERSEDED",
            event_type="SUPERSEDED",
            replacement="A-LEAN-NOT-PRESENT",
        )
        with self.assertRaisesRegex(AuditError, "needs another existing audit"):
            validate(self.root, audit_commit)

    def test_event_sequence_is_consecutive(self) -> None:
        _, _, audit_commit = self.fixture.add_audit()
        self.fixture.add_event("A-LEAN-FIXTURE")
        events = self.root / "audits" / "EVENTS.tsv"
        text = events.read_text(encoding="utf-8").replace(
            "AE-FIXTURE-WITHDRAWN\t1\t", "AE-FIXTURE-WITHDRAWN\t2\t",
        )
        events.write_text(text, encoding="utf-8")
        with self.assertRaisesRegex(AuditError, "event_sequence"):
            validate(self.root, audit_commit)

    def test_event_date_cannot_lock_the_ledger_in_the_future(self) -> None:
        _, _, audit_commit = self.fixture.add_audit()
        self.fixture.add_event("A-LEAN-FIXTURE")
        events = self.root / "audits" / "EVENTS.tsv"
        text = events.read_text(encoding="utf-8").replace("2026-08-02", "9999-12-31")
        events.write_text(text, encoding="utf-8")
        with self.assertRaisesRegex(AuditError, "in the future"):
            validate(self.root, audit_commit)

    def test_event_pull_request_changes_only_events_ledger(self) -> None:
        _, _, audit_commit = self.fixture.add_audit()
        self.fixture.add_event("A-LEAN-FIXTURE", unrelated_path=True)
        with self.assertRaisesRegex(AuditError, "append exactly one event"):
            validate(self.root, audit_commit)

    def test_event_pull_request_has_exactly_one_non_merge_commit(self) -> None:
        _, _, audit_commit = self.fixture.add_audit()
        self.fixture.add_event("A-LEAN-FIXTURE")
        self.fixture._git("commit", "--allow-empty", "--quiet", "-m", "extra event commit")
        with self.assertRaisesRegex(AuditError, "one non-merge commit"):
            validate(self.root, audit_commit)

    def test_supersession_must_map_the_same_claim(self) -> None:
        audits = {
            "A-LEAN-ONE": {
                "claim_id": "T-ONE", "claim_scope_sha256": "1" * 64,
                "coverage": "PARTIAL",
            },
            "A-LEAN-TWO": {
                "claim_id": "T-TWO", "claim_scope_sha256": "1" * 64,
                "coverage": "PARTIAL",
            },
        }
        events = [{
            "event_id": "AE-ONE-SUPERSEDED",
            "event_sequence": "1",
            "audit_id": "A-LEAN-ONE",
            "event_type": "SUPERSEDED",
            "event_date": "2026-08-02",
            "reason": "A newer translation covers the corrected statement.",
            "replacement_audit_id": "A-LEAN-TWO",
        }]
        with self.assertRaisesRegex(AuditError, "maps another claim"):
            validate_events(events, audits)

    def test_supersession_must_map_the_same_pinned_scope(self) -> None:
        audits = {
            "A-LEAN-ONE": {
                "claim_id": "T-ONE", "claim_scope_sha256": "1" * 64,
                "coverage": "PARTIAL",
            },
            "A-LEAN-TWO": {
                "claim_id": "T-ONE", "claim_scope_sha256": "2" * 64,
                "coverage": "EXACT",
            },
        }
        events = [{
            "event_id": "AE-ONE-SUPERSEDED",
            "event_sequence": "1",
            "audit_id": "A-LEAN-ONE",
            "event_type": "SUPERSEDED",
            "event_date": "2026-08-02",
            "reason": "A newer translation covers the corrected statement.",
            "replacement_audit_id": "A-LEAN-TWO",
        }]
        with self.assertRaisesRegex(AuditError, "another claim scope"):
            validate_events(events, audits)

    def test_supersession_cannot_weaken_coverage(self) -> None:
        audits = {
            "A-LEAN-ONE": {
                "claim_id": "T-ONE", "claim_scope_sha256": "1" * 64,
                "coverage": "EXACT",
            },
            "A-LEAN-TWO": {
                "claim_id": "T-ONE", "claim_scope_sha256": "1" * 64,
                "coverage": "PARTIAL",
            },
        }
        events = [{
            "event_id": "AE-ONE-SUPERSEDED",
            "event_sequence": "1",
            "audit_id": "A-LEAN-ONE",
            "event_type": "SUPERSEDED",
            "event_date": "2026-08-02",
            "reason": "A newer translation claims to replace the exact audit.",
            "replacement_audit_id": "A-LEAN-TWO",
        }]
        with self.assertRaisesRegex(AuditError, "weakens coverage"):
            validate_events(events, audits)

    def test_superseded_replacement_can_later_be_withdrawn(self) -> None:
        audits = {
            "A-LEAN-ONE": {
                "claim_id": "T-ONE", "claim_scope_sha256": "1" * 64,
                "coverage": "PARTIAL",
            },
            "A-LEAN-TWO": {
                "claim_id": "T-ONE", "claim_scope_sha256": "1" * 64,
                "coverage": "PARTIAL",
            },
        }
        events = [
            {
                "event_id": "AE-ONE-SUPERSEDED",
                "event_sequence": "1",
                "audit_id": "A-LEAN-ONE",
                "event_type": "SUPERSEDED",
                "event_date": "2026-08-01",
                "reason": "A newer translation covers the corrected statement.",
                "replacement_audit_id": "A-LEAN-TWO",
            },
            {
                "event_id": "AE-TWO-WITHDRAWN",
                "event_sequence": "2",
                "audit_id": "A-LEAN-TWO",
                "event_type": "WITHDRAWN",
                "event_date": "2026-08-02",
                "reason": "Independent review found a later semantic defect.",
                "replacement_audit_id": "-",
            },
        ]
        self.assertIsNone(validate_events(events, audits))

    def test_supersession_cycle_is_rejected(self) -> None:
        audits = {
            "A-LEAN-ONE": {
                "claim_id": "T-ONE", "claim_scope_sha256": "1" * 64,
                "coverage": "PARTIAL",
            },
            "A-LEAN-TWO": {
                "claim_id": "T-ONE", "claim_scope_sha256": "1" * 64,
                "coverage": "PARTIAL",
            },
        }
        events = [
            {
                "event_id": "AE-ONE-SUPERSEDED",
                "event_sequence": "1",
                "audit_id": "A-LEAN-ONE",
                "event_type": "SUPERSEDED",
                "event_date": "2026-08-01",
                "reason": "A newer translation covers the corrected statement.",
                "replacement_audit_id": "A-LEAN-TWO",
            },
            {
                "event_id": "AE-TWO-SUPERSEDED",
                "event_sequence": "2",
                "audit_id": "A-LEAN-TWO",
                "event_type": "SUPERSEDED",
                "event_date": "2026-08-02",
                "reason": "The replacement incorrectly points back to the first audit.",
                "replacement_audit_id": "A-LEAN-ONE",
            },
        ]
        with self.assertRaisesRegex(AuditError, "already qualified|cycle"):
            validate_events(events, audits)

    def test_historical_audit_does_not_hang_on_later_scope_change(self) -> None:
        self.fixture.add_audit()
        registry = self.root / "canon" / "REGISTRY.tsv"
        with registry.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle, delimiter="\t"))
        rows[0]["scope"] = "later revised scope"
        write_tsv(
            registry,
            ("claim_id", "status", "scope", "canon_section", "evidence", "falsifier"),
            rows,
        )
        self.assertEqual(validate(self.root, None), 1)


if __name__ == "__main__":
    unittest.main()
