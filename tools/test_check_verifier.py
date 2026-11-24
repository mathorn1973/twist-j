#!/usr/bin/env python3
"""Focused tests for structured probe run records."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from contextlib import redirect_stdout
import hashlib
from io import StringIO
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from tools import check_verifier
from tools.check_verifier import ROOT, parse_run, read_run, recorded_leg_class


EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
VERIFIER_SHA256 = "1" * 64
STDOUT_SHA256 = "2" * 64


def abandoned_probe(root: Path, status: str) -> Path:
    probe = root / "probes" / "P-ABANDONED-FIXTURE"
    probe.mkdir(parents=True)
    (probe / "PREREG.md").write_text("# frozen pin\n", encoding="utf-8")
    (probe / "verify.py").write_text("# accepted verifier\n", encoding="utf-8")
    (probe / "RESULT.md").write_text(
        f"# Result\n\nStatus: {status}\n", encoding="utf-8"
    )
    return probe


class AbandonedProbeIntegrationTests(unittest.TestCase):
    """Exercise the real verifier gate, not only its shared predicate."""

    def test_valid_abandoned_shape_skips_reproduction_explicitly(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            probe = abandoned_probe(root, "`ABANDONED`. pin closed")
            output = StringIO()
            with patch.object(check_verifier, "ROOT", root), redirect_stdout(output):
                check_verifier.reproduce(probe)
            self.assertEqual(
                output.getvalue(),
                "VERIFY ABANDONED P-ABANDONED-FIXTURE "
                "no completed gate, nothing to reproduce\n",
            )

    def test_abandoned_word_later_on_status_line_cannot_skip(self) -> None:
        statuses = (
            "NOT ABANDONED",
            "FAILED; predecessor ABANDONED",
            "PASS / ABANDONED was considered",
            "PASS\nStatus: ABANDONED / second declaration",
        )
        for status in statuses:
            with self.subTest(status=status), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                probe = abandoned_probe(root, status)
                output = StringIO()
                with (
                    patch.object(check_verifier, "ROOT", root),
                    redirect_stdout(output),
                    self.assertRaises(SystemExit),
                ):
                    check_verifier.reproduce(probe)
                self.assertIn("lacks EXPECTED.txt", output.getvalue())

    def test_run_artefact_blocks_abandoned_skip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            probe = abandoned_probe(root, "ABANDONED / pin closed")
            (probe / "EXPECTED.txt").write_text("", encoding="utf-8")
            output = StringIO()
            with (
                patch.object(check_verifier, "ROOT", root),
                redirect_stdout(output),
                self.assertRaises(SystemExit),
            ):
                check_verifier.reproduce(probe)
            self.assertIn("lacks RUN.md", output.getvalue())


class ReplayTimeoutTests(unittest.TestCase):
    """Keep the exception tied to one exact probe and normal CLI execution."""

    probe = ROOT / "probes" / "P-H3-RELAY-CONTINUATION-1"
    pin = "050a9be48757348fd57021bcc68ab3b9f9fcaf3c"
    source_hash = "af031b96bc46851d19eb2ae907e02f77f68d063ccf204068690a10872532b018"
    expected_hash = "198ed32b967d202c0b729bc1c03e4de6e6ecbc3810b2709ec7880dfdd49cc1f3"

    def test_exact_probe_has_extended_timeout(self) -> None:
        self.assertEqual(
            check_verifier._replay_timeout(self.probe, self.pin, self.source_hash,
                                           self.expected_hash),
            900,
        )

    def test_name_pin_source_and_expected_must_all_match(self) -> None:
        cases = (
            ("name", self.probe.with_name("P-OTHER"), self.pin, self.source_hash,
             self.expected_hash),
            ("pin", self.probe, "0" * 40, self.source_hash, self.expected_hash),
            ("source", self.probe, self.pin, "0" * 64, self.expected_hash),
            ("expected", self.probe, self.pin, self.source_hash, "0" * 64),
        )
        for label, probe, pin, source_hash, expected_hash in cases:
            with self.subTest(label=label):
                self.assertEqual(
                    check_verifier._replay_timeout(probe, pin, source_hash, expected_hash),
                    600,
                )

    def test_cpp_and_header_drift_restore_default_timeout(self) -> None:
        read_bytes = Path.read_bytes
        for filename in ("continuation.cpp", "dynamics.hpp"):
            changed_path = self.probe / filename

            def read(path: Path) -> bytes:
                data = read_bytes(path)
                if path == changed_path:
                    return data + b"\n// modified input\n"
                return data

            with self.subTest(filename=filename), patch.object(Path, "read_bytes", read):
                self.assertEqual(
                    check_verifier._replay_timeout(self.probe, self.pin, self.source_hash,
                                                   self.expected_hash),
                    600,
                )

    def test_cli_uses_the_bound_timeout_and_fails_when_it_expires(self) -> None:
        expected = (self.probe / "EXPECTED.txt").read_bytes()
        verifier = self.probe / "verify.py"
        verifier_bytes = verifier.read_bytes()
        relative_verifier = verifier.relative_to(ROOT).as_posix()
        git_show = ["git", "show", f"{self.pin}:{relative_verifier}"]
        git_ancestor = ["git", "merge-base", "--is-ancestor", self.pin, "HEAD"]

        for expires in (False, True):
            with self.subTest(expires=expires):
                replay_timeouts = []

                def run(command, **kwargs):
                    if command == git_show:
                        return subprocess.CompletedProcess(command, 0, verifier_bytes, b"")
                    if command == git_ancestor:
                        return subprocess.CompletedProcess(command, 0)
                    self.assertEqual(command, [sys.executable, relative_verifier])
                    timeout = kwargs["timeout"]
                    replay_timeouts.append(timeout)
                    if expires:
                        raise subprocess.TimeoutExpired(command, timeout)
                    return subprocess.CompletedProcess(command, 0, expected, b"")

                output = StringIO()
                with (
                    patch.dict(os.environ, {"TWISTJ_EVIDENCE_DIR": ""}),
                    patch.object(sys, "argv", ["check_verifier.py"]),
                    patch.object(check_verifier, "changed_probes", return_value=[self.probe]),
                    patch.object(check_verifier, "ProcessPoolExecutor",
                                 side_effect=lambda max_workers, mp_context:
                                 ThreadPoolExecutor(max_workers=max_workers)),
                    patch.object(subprocess, "run", side_effect=run),
                    redirect_stdout(output),
                ):
                    if expires:
                        with self.assertRaises(SystemExit) as stopped:
                            check_verifier.main()
                        self.assertEqual(stopped.exception.code, 1)
                    else:
                        check_verifier.main()

                self.assertEqual(replay_timeouts, [900], output.getvalue())
                if expires:
                    self.assertIn("TimeoutExpired", output.getvalue())
                    self.assertNotIn(f"VERIFY PASS {self.probe.name}", output.getvalue())
                else:
                    self.assertIn(f"VERIFY PASS {self.probe.name}", output.getvalue())


def replace_last(text: str, old: str, new: str) -> str:
    before, separator, after = text.rpartition(old)
    if not separator:
        raise AssertionError(f"fixture lacks {old!r}")
    return before + new + after


def run_text(
    local_architecture: str = "aarch64",
    github_architecture: str = "x86_64",
    github_stdout_sha256: str = STDOUT_SHA256,
    *,
    prefixed: bool = False,
) -> str:
    local_prefix = "local_" if prefixed else ""
    github_prefix = "github_" if prefixed else ""
    return f"""# RUN fixture

## Immutable pin

pin_commit: {"a" * 40}
verifier_sha256: {VERIFIER_SHA256}

## Command

command: python3 probes/P-FIXTURE/verify.py

## Local formal leg

{local_prefix}platform: Ubuntu 24.04
{local_prefix}architecture: {local_architecture}
{local_prefix}python: Python 3.12.3
{local_prefix}exit_code: 0
{local_prefix}stdout_sha256: {STDOUT_SHA256}
{local_prefix}stdout_bytes: 5
{local_prefix}stdout_lines: 1
{local_prefix}stderr_sha256: {EMPTY_SHA256}
{local_prefix}stderr_bytes: 0

## Required GitHub leg

{github_prefix}status: PASS
{github_prefix}platform: Ubuntu 24.04
{github_prefix}architecture: {github_architecture}
{github_prefix}python: Python 3.12.13
{github_prefix}verifier_sha256: {VERIFIER_SHA256}
{github_prefix}stdout_sha256: {github_stdout_sha256}
{github_prefix}exit_code: 0
{github_prefix}stderr_bytes: 0
{github_prefix}verdict: VERIFY PASS
"""


class CheckVerifierTests(unittest.TestCase):
    def assert_parse_failure(self, text: str) -> None:
        with redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit):
                parse_run(text, "fixture")

    def assert_record_failure(self, record) -> None:
        with redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit):
                recorded_leg_class(
                    record, "P-FIXTURE", VERIFIER_SHA256, STDOUT_SHA256
                )

    def test_flat_view_keeps_local_leg_instead_of_last_duplicate(self) -> None:
        record = parse_run(run_text(), "fixture")
        self.assertEqual(record.fields["architecture"], "aarch64")
        self.assertEqual(
            record.sections["required github leg"]["architecture"], "x86_64"
        )

    def test_exact_architecture_pair_is_two_architecture(self) -> None:
        record = parse_run(run_text(), "fixture")
        self.assertEqual(
            recorded_leg_class(
                record, "P-FIXTURE", VERIFIER_SHA256, STDOUT_SHA256
            ),
            "TWO-ARCHITECTURE",
        )

    def test_same_architecture_is_reproduction_only(self) -> None:
        record = parse_run(run_text(local_architecture="x86_64"), "fixture")
        self.assertEqual(
            recorded_leg_class(
                record, "P-FIXTURE", VERIFIER_SHA256, STDOUT_SHA256
            ),
            "REPRODUCTION-ONLY",
        )

    def test_prefixed_leg_fields_are_supported(self) -> None:
        record = parse_run(run_text(prefixed=True), "fixture")
        self.assertEqual(
            recorded_leg_class(
                record, "P-FIXTURE", VERIFIER_SHA256, STDOUT_SHA256
            ),
            "TWO-ARCHITECTURE",
        )

    def test_github_stdout_must_match_expected(self) -> None:
        record = parse_run(
            run_text(github_stdout_sha256="3" * 64),
            "fixture",
        )
        self.assert_record_failure(record)

    def test_github_leg_may_be_aarch64_when_the_local_leg_differs(self) -> None:
        """The workflow runs both architectures, so either may be the recorded
        remote leg. What the gate needs is that the two legs differ."""
        record = parse_run(
            run_text(local_architecture="x86_64", github_architecture="aarch64"),
            "fixture",
        )
        self.assertEqual(
            recorded_leg_class(
                record, "P-FIXTURE", VERIFIER_SHA256, STDOUT_SHA256
            ),
            "TWO-ARCHITECTURE",
        )

    def test_matching_architectures_are_reproduction_only(self) -> None:
        """Agreement on one architecture is reproduction, not a gate, and is
        recorded as such rather than rejected."""
        for architecture in ("x86_64", "aarch64"):
            with self.subTest(architecture=architecture):
                record = parse_run(
                    run_text(
                        local_architecture=architecture,
                        github_architecture=architecture,
                    ),
                    "fixture",
                )
                self.assertEqual(
                    recorded_leg_class(
                        record, "P-FIXTURE", VERIFIER_SHA256, STDOUT_SHA256
                    ),
                    "REPRODUCTION-ONLY",
                )

    def test_unknown_github_architecture_is_rejected(self) -> None:
        record = parse_run(
            run_text(github_architecture="riscv64"),
            "fixture",
        )
        self.assert_record_failure(record)

    def test_github_verifier_must_match_pinned_verifier(self) -> None:
        text = replace_last(
            run_text(),
            f"verifier_sha256: {VERIFIER_SHA256}",
            f"verifier_sha256: {'3' * 64}",
        )
        record = parse_run(text, "fixture")
        self.assert_record_failure(record)

    def test_nonzero_github_exit_is_rejected(self) -> None:
        record = parse_run(
            replace_last(run_text(), "exit_code: 0", "exit_code: 7"),
            "fixture",
        )
        self.assert_record_failure(record)

    def test_nonempty_github_stderr_is_rejected(self) -> None:
        text = run_text().replace(
            "stderr_bytes: 0\nverdict: VERIFY PASS",
            "stderr_bytes: 4\nverdict: VERIFY PASS",
        )
        record = parse_run(text, "fixture")
        self.assert_record_failure(record)

    def test_conflicting_prefixed_and_plain_field_is_rejected(self) -> None:
        text = run_text().replace(
            "architecture: aarch64",
            "architecture: aarch64\nlocal_architecture: x86_64",
            1,
        )
        record = parse_run(text, "fixture")
        self.assert_record_failure(record)

    def test_flat_field_cannot_override_structured_local_leg(self) -> None:
        text = run_text().replace(
            f"verifier_sha256: {VERIFIER_SHA256}",
            f"verifier_sha256: {VERIFIER_SHA256}\narchitecture: x86_64",
            1,
        )
        record = parse_run(text, "fixture")
        self.assert_record_failure(record)

    def test_renamed_two_leg_headings_cannot_downgrade_to_legacy(self) -> None:
        text = (
            run_text(github_stdout_sha256="3" * 64)
            .replace("## Local formal leg", "## First run")
            .replace("## Required GitHub leg", "## Second run")
        )
        record = parse_run(text, "fixture")
        self.assert_record_failure(record)

    def test_duplicate_named_github_field_is_rejected(self) -> None:
        probe = ROOT / "probes" / "P-GYRON-DISCREPANCY-LOG-3"
        text = (probe / "RUN.md").read_text(encoding="utf-8")
        text += "\nx86_64_architecture: aarch64\n"
        record = parse_run(text, "fixture")
        self.assert_record_failure(record)

    def test_plain_and_prefixed_github_outcomes_must_agree(self) -> None:
        text = replace_last(run_text(), "exit_code: 0", "exit_code: 9")
        text = text.replace(
            "exit_code: 9\nstderr_bytes: 0",
            "exit_code: 9\ngithub_exit_code: 0\n"
            "stderr_bytes: 0\ngithub_stderr_bytes: 0",
        )
        record = parse_run(text, "fixture")
        self.assert_record_failure(record)

    def test_failed_github_status_cannot_hide_behind_zero_exit(self) -> None:
        text = run_text().replace("status: PASS", "status: FAIL")
        record = parse_run(text, "fixture")
        self.assert_record_failure(record)

    def test_structured_failed_optional_outcomes_are_rejected(self) -> None:
        for field in ("byte_identity", "replay"):
            with self.subTest(field=field):
                text = run_text().replace(
                    "verdict: VERIFY PASS",
                    f"verdict: VERIFY PASS\n{field}: FAIL",
                )
                record = parse_run(text, "fixture")
                self.assert_record_failure(record)

    def test_structured_plain_and_prefixed_outcomes_must_agree(self) -> None:
        text = run_text().replace(
            "verdict: VERIFY PASS",
            "verdict: VERIFY PASS\n"
            "byte_identity: PASS\n"
            "github_byte_identity: FAIL",
        )
        record = parse_run(text, "fixture")
        self.assert_record_failure(record)

    def test_critical_field_in_extra_section_is_rejected(self) -> None:
        record = parse_run(
            run_text() + "\n## Correction\n\narchitecture: x86_64\n",
            "fixture",
        )
        self.assert_record_failure(record)

    def test_duplicate_leg_heading_is_rejected(self) -> None:
        self.assert_parse_failure(
            run_text() + "\n## Local formal leg\n\nplatform: elsewhere\n"
        )

    def test_duplicate_singleton_command_is_rejected(self) -> None:
        self.assert_parse_failure(
            run_text() + "\ncommand: python3 probes/P-OTHER/verify.py\n"
        )

    def test_named_failed_replay_is_rejected(self) -> None:
        probe = ROOT / "probes" / "P-GYRON-DISCREPANCY-LOG-3"
        text = (probe / "RUN.md").read_text(encoding="utf-8")
        text = text.replace("x86_64_replay: PASS", "x86_64_replay: FAIL")
        record = parse_run(text, "fixture")
        self.assert_record_failure(record)

    def test_duplicate_named_optional_outcomes_are_rejected(self) -> None:
        probe = ROOT / "probes" / "P-GYRON-DISCREPANCY-LOG-3"
        original = (probe / "RUN.md").read_text(encoding="utf-8")
        for field in ("byte_identity", "replay"):
            with self.subTest(field=field):
                record = parse_run(
                    original + f"\nx86_64_{field}: FAIL\n",
                    "fixture",
                )
                self.assert_record_failure(record)

    def test_local_verifier_alias_must_match_pin(self) -> None:
        text = run_text().replace(
            "## Local formal leg\n",
            "## Local formal leg\n\nlocal_verifier_sha256: " + "3" * 64 + "\n",
        )
        record = parse_run(text, "fixture")
        self.assert_record_failure(record)

    def test_current_structured_records_are_classified_without_execution(self) -> None:
        expected = {
            "P-BOOST-COHERENCE-1": "TWO-ARCHITECTURE",
            "P-READ-REDUNDANCY-1": "TWO-ARCHITECTURE",
            "P-METRO-REDUCTION-ARROWS-4": "REPRODUCTION-ONLY",
            "P-ENTROPY-LAW-REDUCTION-1": "REPRODUCTION-ONLY",
            "P-ENTROPY-CURSOR-CLOSURE-1": "TWO-ARCHITECTURE",
            "P-KERNEL-Z6-SYNCHRONIZATION-1": "TWO-ARCHITECTURE",
            "P-TM-SYM2-REVERSAL-CLOSURE-1": "TWO-ARCHITECTURE",
            "P-TM-SYM2-SEMILINEAR-GAUGE-1": "TWO-ARCHITECTURE",
            "P-GYRON-DISCREPANCY-LOG-3": "TWO-ARCHITECTURE",
            "P-DE-TRACE-DENSITY-1": "LEGACY",
        }
        for name, classification in expected.items():
            with self.subTest(probe=name):
                probe = ROOT / "probes" / name
                record = read_run(probe / "RUN.md")
                verifier_hash = hashlib.sha256(
                    (probe / "verify.py").read_bytes()
                ).hexdigest()
                expected_hash = hashlib.sha256(
                    (probe / "EXPECTED.txt").read_bytes()
                ).hexdigest()
                self.assertEqual(
                    recorded_leg_class(
                        record,
                        name,
                        verifier_hash,
                        expected_hash,
                    ),
                    classification,
                )

    def test_all_current_records_parse_without_executing_verifiers(self) -> None:
        for run_path in sorted((ROOT / "probes").glob("*/RUN.md")):
            probe = run_path.parent
            with self.subTest(probe=probe.name):
                record = read_run(run_path)
                verifier_hash = hashlib.sha256(
                    (probe / "verify.py").read_bytes()
                ).hexdigest()
                expected_hash = hashlib.sha256(
                    (probe / "EXPECTED.txt").read_bytes()
                ).hexdigest()
                self.assertIn(
                    recorded_leg_class(
                        record,
                        probe.name,
                        verifier_hash,
                        expected_hash,
                    ),
                    {"LEGACY", "REPRODUCTION-ONLY", "TWO-ARCHITECTURE"},
                )


if __name__ == "__main__":
    unittest.main()
