from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

import check_incubation as check


class IncubationCheckTests(unittest.TestCase):
    def write(self, root: Path, relative: str, text: str) -> None:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def candidate(self, root: Path, name: str, target: str = "NONE") -> None:
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
        self.write(root, f"{base}/PREREG.md", "prereg_revision: 1\n")
        self.write(root, f"{base}/verify.py", "print('PASS')\n")
        self.write(
            root,
            f"{base}/break.py",
            f"BREAKER_SESSION = 'breaker-{name}'\nprint('PASS')\n",
        )
        self.write(root, f"{base}/RESULT.md", "result: candidate-C\n")
        probe = target.removeprefix("probe/") if target != "NONE" else "NONE"
        claim = target.removeprefix("probe/P-") if target != "NONE" else "NONE"
        self.write(
            root,
            f"{base}/PROMO.md",
            f"""incubation_id: {name}
target_issue: NONE
target_branch: {target}
target_probe_id: {probe}
target_claim_id: {claim}
""",
        )

    def test_not_applicable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            errors, count = check.findings(Path(tmp))
            self.assertEqual(errors, [])
            self.assertEqual(count, 0)

    def test_valid_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.candidate(root, "C-ALPHA-1", "probe/P-ALPHA-1")
            errors, count = check.findings(root)
            self.assertEqual(errors, [])
            self.assertEqual(count, 1)

    def test_duplicate_promotion_target(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.candidate(root, "C-ALPHA-1", "probe/P-FOO-1")
            self.candidate(root, "C-BETA-1", "probe/P-FOO-1")
            errors, _ = check.findings(root)
            self.assertTrue(any("PROMO-NAME-COLLISION" in error for error in errors))

    def test_ambiguous_promotion_target(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.candidate(root, "C-ALPHA-1")
            promo = root / "notes/incubation/C-ALPHA-1/PROMO.md"
            promo.write_text(
                promo.read_text(encoding="utf-8").replace(
                    "target_claim_id: NONE", "target_claim_id: FOO or BAR"
                ),
                encoding="utf-8",
            )
            errors, _ = check.findings(root)
            self.assertTrue(any("PROMO-TARGET-AMBIGUOUS" in error for error in errors))

    def test_duplicate_manifest_field(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.candidate(root, "C-ALPHA-1")
            promo = root / "notes/incubation/C-ALPHA-1/PROMO.md"
            with promo.open("a", encoding="utf-8") as handle:
                handle.write("target_claim_id: SECOND\n")
            errors, _ = check.findings(root)
            self.assertTrue(any("appears 2 times" in error for error in errors))

    def test_visible_verifier_reference(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.candidate(root, "C-ALPHA-1")
            breaker = root / "notes/incubation/C-ALPHA-1/break.py"
            breaker.write_text(
                "BREAKER_SESSION = 'b'\nTARGET = 'verify.py'\n",
                encoding="utf-8",
            )
            errors, _ = check.findings(root)
            self.assertTrue(
                any("PREMATURE-VERIFIER-DISCLOSURE" in error for error in errors)
            )

    def test_invalid_revision(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.candidate(root, "C-ALPHA-1")
            prereg = root / "notes/incubation/C-ALPHA-1/PREREG.md"
            prereg.write_text("prereg_revision: 3\n", encoding="utf-8")
            errors, _ = check.findings(root)
            self.assertTrue(any("must be 1 or 2" in error for error in errors))

    def test_public_run_machine_nickname(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "probes/P-X/RUN.md", "platform: JAS 2\n")
            errors, _ = check.findings(root)
            self.assertTrue(any("machine nickname" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
