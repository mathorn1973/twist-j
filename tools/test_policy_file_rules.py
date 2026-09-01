#!/usr/bin/env python3

from pathlib import Path
import tempfile
import unittest

from tools.policy_file_rules import (
    PUBLIC_PROBE_TRANSCRIPTS,
    is_forbidden_repository_file,
    public_transcript_integrity_problem,
)


class PolicyFileRulesTests(unittest.TestCase):
    def test_exact_twenty_public_transcripts_are_allowed(self) -> None:
        self.assertEqual(len(PUBLIC_PROBE_TRANSCRIPTS), 20)
        for path in PUBLIC_PROBE_TRANSCRIPTS:
            with self.subTest(path=path):
                self.assertFalse(is_forbidden_repository_file(path))
                self.assertFalse(is_forbidden_repository_file(Path(path)))

    def test_log_exception_is_exact_path_only(self) -> None:
        rejected = (
            "debug.log",
            "probes/P-OTHER/L6_cold_r1.log",
            "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/extra.log",
            "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L6_cold_r1.LOG",
            "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L6_cold_r1.log.bak",
            "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/primal_L6_cold_r2.log",
            "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/dual_L6_cold_r3.jsonl",
        )
        for path in rejected:
            with self.subTest(path=path):
                self.assertTrue(is_forbidden_repository_file(path))

    def test_other_security_suffixes_remain_forbidden(self) -> None:
        for path in ("secret.pem", ".env", ".env.local", "model.pt", "cache.pyc"):
            with self.subTest(path=path):
                self.assertTrue(is_forbidden_repository_file(path))
        self.assertFalse(is_forbidden_repository_file("probes/P-X/RESULT.md"))

    def test_gitignore_exceptions_equal_the_allowlist(self) -> None:
        root = Path(__file__).resolve().parents[1]
        exceptions = {
            line[1:]
            for line in (root / ".gitignore").read_text(encoding="utf-8").splitlines()
            if line.startswith("!probes/")
        }
        self.assertEqual(exceptions, PUBLIC_PROBE_TRANSCRIPTS)

    def test_public_transcript_requires_printable_lf_text(self) -> None:
        relative = sorted(PUBLIC_PROBE_TRANSCRIPTS)[0]
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "transcript.log"
            for data, expected in (
                (b"RUN value=1\n", None),
                (b"", "final LF"),
                (b"RUN value=1", "final LF"),
                (b"RUN value=1\r\n", "final LF"),
                (b"RUN value=\x00\n", "printable ASCII"),
            ):
                with self.subTest(data=data):
                    path.write_bytes(data)
                    problem = public_transcript_integrity_problem(path, relative)
                    if expected is None:
                        self.assertIsNone(problem)
                    else:
                        self.assertIn(expected, problem or "")

    def test_public_transcript_rejects_symlink(self) -> None:
        relative = sorted(PUBLIC_PROBE_TRANSCRIPTS)[0]
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "target.txt"
            link = Path(temporary) / "transcript.log"
            target.write_bytes(b"RUN value=1\n")
            try:
                link.symlink_to(target)
            except OSError as error:
                self.skipTest(f"symlinks unavailable: {error}")
            self.assertIn(
                "non-symlink",
                public_transcript_integrity_problem(link, relative) or "",
            )


if __name__ == "__main__":
    unittest.main()
