from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import tempfile
import unittest

import check_incubation as check


class IncubationCheckTests(unittest.TestCase):
    def git(self, root: Path, *args: str) -> str:
        process = subprocess.run(
            ["git", "-C", str(root), *args],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )
        return process.stdout.strip()

    def init_repo(self, root: Path) -> None:
        self.git(root, "init", "-b", "main")
        self.git(root, "config", "user.name", "A. M. Thorn")
        self.git(root, "config", "user.email", "thorn@twistj.com")

    def write(self, root: Path, relative: str, text: str) -> None:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def commit(self, root: Path, message: str) -> str:
        self.git(root, "add", "--all")
        self.git(root, "commit", "-m", message)
        return self.git(root, "rev-parse", "HEAD")

    def claim(self, root: Path, name: str = "C-ALPHA-1") -> str:
        base = f"notes/incubation/{name}"
        self.write(
            root,
            f"{base}/CLAIM.md",
            f"""incubation_id: {name}
object_key: REGISTRY:TEST
claim_key: {name}-CLAIM
claim_issue: 1
owner_session: owner-{name}
builder_session: builder-{name}
status: NO-AUTHORITY
scope: exact test scope
excluded_scope: none
dependencies: none
action_layer: L1
""",
        )
        self.write(root, f"{base}/PREREG-r1.md", "prereg_revision: 1\n")
        self.commit(root, "freeze prereg r1")
        return base

    def breaker_text(self, session: str, revision: int, digest: str, body: str = "") -> str:
        return (
            f'BREAKER_SESSION = "{session}"\n'
            f"PREREG_REVISION = {revision}\n"
            f'PREREG_SHA256 = "{digest}"\n'
            + body
        )

    def add_blind_breaker(
        self,
        root: Path,
        base: str,
        prereg_commit: str,
        session: str = "sess-b",
        body: str = "print('PASS')\n",
    ) -> tuple[str, str]:
        self.git(root, "switch", "-c", "breaker-r1", prereg_commit)
        prereg = root / base / "PREREG-r1.md"
        digest = hashlib.sha256(prereg.read_bytes()).hexdigest()
        self.write(
            root,
            f"{base}/break/r1/break.py",
            self.breaker_text(session, 1, digest, body),
        )
        breaker_commit = self.commit(root, "freeze breaker r1")
        return breaker_commit, digest

    def integrate_builder_and_breaker(
        self,
        root: Path,
        base: str,
        prereg_commit: str,
        breaker_commit: str,
    ) -> None:
        self.git(root, "switch", "-c", "builder-r1", prereg_commit)
        self.write(root, f"{base}/verify-r1.py", "print('PASS')\n")
        self.commit(root, "freeze verifier r1")
        self.git(root, "merge", "--no-ff", breaker_commit, "-m", "integrate blind routes")

    def add_result_and_promo(self, root: Path, base: str) -> None:
        name = Path(base).name
        self.write(root, f"{base}/RESULT.md", "result: candidate-C\n")
        self.write(
            root,
            f"{base}/PROMO.md",
            f"""incubation_id: {name}
target_issue: NONE
target_branch: probe/P-ALPHA-1
target_probe_id: P-ALPHA-1
target_claim_id: ALPHA-1
""",
        )
        self.commit(root, "record result and promo")

    def valid_integrated_candidate(self, root: Path) -> str:
        self.init_repo(root)
        base = self.claim(root)
        prereg_commit = self.git(root, "rev-parse", "HEAD")
        breaker_commit, _ = self.add_blind_breaker(root, base, prereg_commit)
        self.integrate_builder_and_breaker(root, base, prereg_commit, breaker_commit)
        self.add_result_and_promo(root, base)
        return base

    def run_record(self, command: str = "$HOME/.local/bin/python3 probes/P-X/verify.py") -> str:
        h = "a" * 64
        return f"""run_format: 2
candidate_commit: {'b' * 40}
prereg_sha256: {h}
verifier_sha256: {h}
expected_sha256: {h}
stdout_sha256: {h}
expected_bytes: 4
stdout_bytes: 4
stderr_bytes: 0
exit_code: 0
command: {command}
platform: Ubuntu 24.04
architecture: aarch64
python: 3.12.3
"""

    def test_not_applicable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            errors, count = check.findings(Path(tmp))
            self.assertEqual(errors, [])
            self.assertEqual(count, 0)

    def test_valid_blind_dag_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.valid_integrated_candidate(root)
            errors, count = check.findings(root)
            self.assertEqual(errors, [])
            self.assertEqual(count, 1)

    def test_breaker_with_verifier_ancestor_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.init_repo(root)
            base = self.claim(root)
            prereg = root / base / "PREREG-r1.md"
            digest = hashlib.sha256(prereg.read_bytes()).hexdigest()
            self.write(root, f"{base}/verify-r1.py", "print('PASS')\n")
            self.commit(root, "add verifier first")
            self.write(
                root,
                f"{base}/break/r1/break.py",
                self.breaker_text("sess-b", 1, digest, "print('PASS')\n"),
            )
            self.commit(root, "add contaminated breaker")
            errors, _ = check.findings(root)
            self.assertTrue(any("BREAKER-VERIFIER-ANCESTRY" in error for error in errors))

    def test_dynamic_verifier_name_is_safe_only_on_blind_branch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.init_repo(root)
            base = self.claim(root)
            prereg_commit = self.git(root, "rev-parse", "HEAD")
            body = (
                "import pathlib\n"
                'name = "ver" + "ify-r1" + "." + "py"\n'
                "target = pathlib.Path(__file__).parents[2] / name\n"
            )
            breaker_commit, _ = self.add_blind_breaker(root, base, prereg_commit, body=body)
            self.integrate_builder_and_breaker(root, base, prereg_commit, breaker_commit)
            errors, _ = check.findings(root)
            self.assertEqual(errors, [])

    def test_arbitrary_stop_does_not_authorize_promo(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.init_repo(root)
            base = self.claim(root)
            name = Path(base).name
            self.write(
                root,
                f"{base}/RESULT.md",
                "result: STOP\nstop_reason: owner-went-on-holiday\n",
            )
            self.write(
                root,
                f"{base}/PROMO.md",
                f"""incubation_id: {name}
target_issue: NONE
target_branch: NONE
target_probe_id: NONE
target_claim_id: NONE
""",
            )
            self.commit(root, "invalid unrelated stop")
            errors, _ = check.findings(root)
            self.assertTrue(any("exact underspecified STOP" in error for error in errors))

    def test_exact_underspecified_stop_authorizes_handoff(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.init_repo(root)
            base = self.claim(root)
            prereg = root / base / "PREREG-r1.md"
            digest = hashlib.sha256(prereg.read_bytes()).hexdigest()
            self.write(
                root,
                f"{base}/BREAK-r1.md",
                f"""breaker_session: sess-b
prereg_revision: 1
prereg_sha256: {digest}
stop_reason: BLIND-BREAKER-UNDERSPECIFIED
missing_types: output equality
""",
            )
            self.commit(root, "freeze underspecified report")
            name = Path(base).name
            self.write(
                root,
                f"{base}/RESULT.md",
                "result: STOP\nstop_reason: BLIND-BREAKER-UNDERSPECIFIED\n",
            )
            self.write(
                root,
                f"{base}/PROMO.md",
                f"""incubation_id: {name}
target_issue: NONE
target_branch: NONE
target_probe_id: NONE
target_claim_id: NONE
""",
            )
            self.commit(root, "record exact stop")
            errors, _ = check.findings(root)
            self.assertEqual(errors, [])

    def test_revision_two_reuses_session_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.init_repo(root)
            base = self.claim(root)
            prereg1 = root / base / "PREREG-r1.md"
            digest1 = hashlib.sha256(prereg1.read_bytes()).hexdigest()
            self.write(
                root,
                f"{base}/BREAK-r1.md",
                f"""breaker_session: sess-b
prereg_revision: 1
prereg_sha256: {digest1}
stop_reason: BLIND-BREAKER-UNDERSPECIFIED
missing_types: equality
""",
            )
            self.commit(root, "freeze report r1")
            self.write(root, f"{base}/PREREG-r2.md", "prereg_revision: 2\n")
            self.commit(root, "freeze prereg r2")
            prereg2 = root / base / "PREREG-r2.md"
            digest2 = hashlib.sha256(prereg2.read_bytes()).hexdigest()
            self.write(
                root,
                f"{base}/break/r2/break.py",
                self.breaker_text("sess-b", 2, digest2, "print('PASS')\n"),
            )
            self.commit(root, "freeze breaker r2")
            errors, _ = check.findings(root)
            self.assertTrue(any("different breaker_session" in error for error in errors))

    def test_indented_duplicate_manifest_field_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.valid_integrated_candidate(root)
            promo = root / "notes/incubation/C-ALPHA-1/PROMO.md"
            promo.write_text(
                promo.read_text(encoding="utf-8")
                + " target_branch: probe/P-DECOY-9\n",
                encoding="utf-8",
            )
            self.commit(root, "add hidden field")
            errors, _ = check.findings(root)
            self.assertTrue(any("indented manifest field" in error for error in errors))

    def test_duplicate_promotion_target_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.init_repo(root)
            for name in ("C-ALPHA-1", "C-BETA-1"):
                base = f"notes/incubation/{name}"
                self.write(
                    root,
                    f"{base}/CLAIM.md",
                    f"""incubation_id: {name}
object_key: REGISTRY:TEST
claim_key: {name}-CLAIM
claim_issue: 1
owner_session: owner-{name}
builder_session: builder-{name}
status: NO-AUTHORITY
scope: exact test scope
excluded_scope: none
dependencies: none
action_layer: L1
""",
                )
                self.write(root, f"{base}/PREREG-r1.md", "prereg_revision: 1\n")
                self.write(root, f"{base}/RESULT.md", "result: STOP\nstop_reason: BLIND-BREAKER-UNDERSPECIFIED\n")
                digest = hashlib.sha256((root / base / "PREREG-r1.md").read_bytes()).hexdigest()
                self.write(root, f"{base}/BREAK-r1.md", f"""breaker_session: {name}-b
prereg_revision: 1
prereg_sha256: {digest}
stop_reason: BLIND-BREAKER-UNDERSPECIFIED
missing_types: equality
""")
                self.write(root, f"{base}/PROMO.md", f"""incubation_id: {name}
target_issue: NONE
target_branch: probe/P-SAME-1
target_probe_id: P-SAME-1
target_claim_id: SAME-1
""")
            self.commit(root, "add colliding candidates")
            errors, _ = check.findings(root)
            self.assertTrue(any("PROMO-NAME-COLLISION" in error for error in errors))

    def test_historical_legacy_run_record_is_ignored_by_base_diff(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.init_repo(root)
            self.write(root, "probes/P-OLD/RUN.md", "historical prose format\n")
            base = self.commit(root, "add historical run")
            self.write(root, "README.md", "change\n")
            self.commit(root, "unrelated change")
            errors, _ = check.findings(root, base_sha=base)
            self.assertEqual(errors, [])

    def test_changed_legacy_run_record_must_upgrade_to_format_two(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.init_repo(root)
            self.write(root, "probes/P-OLD/RUN.md", "historical prose format\n")
            base = self.commit(root, "add historical run")
            self.write(root, "probes/P-OLD/RUN.md", "changed historical prose\n")
            self.commit(root, "change run")
            errors, _ = check.findings(root, base_sha=base)
            self.assertTrue(any("field lines only" in error for error in errors))
            self.assertTrue(any("run_format" in error for error in errors))

    def test_home_local_command_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = "probes/P-X/RUN.md"
            self.write(root, path, self.run_record())
            errors, _ = check.findings(root, changed_files={path})
            self.assertEqual(errors, [])

    def test_run_record_prose_line_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = "probes/P-X/RUN.md"
            self.write(root, path, self.run_record() + "unstructured note\n")
            errors, _ = check.findings(root, changed_files={path})
            self.assertTrue(any("field lines only" in error for error in errors))

    def test_unknown_run_field_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = "probes/P-X/RUN.md"
            self.write(root, path, self.run_record() + "note: extra\n")
            errors, _ = check.findings(root, changed_files={path})
            self.assertTrue(any("unknown run-record field note" in error for error in errors))

    def test_invalid_run_architecture_and_platform_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = "probes/P-X/RUN.md"
            text = self.run_record().replace("architecture: aarch64", "architecture: armv8")
            text = text.replace("platform: Ubuntu 24.04", "platform: private-linux")
            self.write(root, path, text)
            errors, _ = check.findings(root, changed_files={path})
            self.assertTrue(any("architecture must be" in error for error in errors))
            self.assertTrue(any("platform is not allowed" in error for error in errors))

    def test_private_mdns_hostname_fails_but_local_path_does_not(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = "probes/P-X/RUN.md"
            self.write(root, path, self.run_record("python3 verify.py --host node.local"))
            errors, _ = check.findings(root, changed_files={path})
            self.assertTrue(any("private infrastructure" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
