from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "policy.yml"


class WorkflowArchitectureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = WORKFLOW.read_text(encoding="utf-8")

    def test_exact_architecture_runners(self) -> None:
        self.assertEqual(self.text.count("architecture: x86_64"), 1)
        self.assertEqual(self.text.count("runner: ubuntu-latest"), 1)
        self.assertEqual(self.text.count("architecture: aarch64"), 1)
        self.assertEqual(self.text.count("runner: ubuntu-24.04-arm"), 1)
        self.assertIn("runs-on: ${{ matrix.runner }}", self.text)

    def test_timeouts_match_policy(self) -> None:
        architecture_at = self.text.index("\n  architecture:")
        check_at = self.text.index("\n  check:")
        publication_at = self.text.index("\n  publication:")
        architecture_block = self.text[architecture_at:check_at]
        check_block = self.text[check_at:publication_at]
        publication_block = self.text[publication_at:]
        self.assertIn("timeout-minutes: 45", architecture_block)
        self.assertIn("timeout-minutes: 5", check_block)
        self.assertIn("timeout-minutes: 60", publication_block)
        self.assertEqual(self.text.count("timeout-minutes: 45"), 1)
        self.assertEqual(self.text.count("timeout-minutes: 60"), 1)
        self.assertEqual(self.text.count("timeout-minutes: 5"), 1)

    def test_aggregate_check_depends_on_architecture(self) -> None:
        block = (
            "  check:\n"
            "    if: always() && github.ref_type != 'tag' "
            "&& github.event_name != 'release' && github.event_name != 'workflow_dispatch'\n"
            "    needs: architecture\n"
            "    runs-on: ubuntu-latest"
        )
        self.assertIn(block, self.text)
        self.assertIn('echo "TWO-ARCHITECTURE CHECK PASS"', self.text)

    def test_aggregate_fails_rather_than_skips_on_architecture_failure(self) -> None:
        """A skipped required check can count as passing. The aggregate
        therefore runs always() and asserts the matrix result itself, so a
        failed architecture job fails the required context instead of
        vanishing from it."""
        self.assertIn("if: always() &&", self.text)
        self.assertIn("if: needs.architecture.result != 'success'", self.text)

    def test_publication_is_single_runner(self) -> None:
        block = (
            "  publication:\n"
            "    if: github.ref_type == 'tag' || github.event_name == 'release' || github.event_name == 'workflow_dispatch'\n"
            "    runs-on: ubuntu-latest"
        )
        self.assertIn(block, self.text)
        publication_at = self.text.index("\n  publication:")
        upload_token = "actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a"
        self.assertEqual(self.text.count(upload_token), 1)
        self.assertGreater(self.text.index(upload_token), publication_at)

    def test_both_architectures_run_reproduction_checks(self) -> None:
        architecture_at = self.text.index("\n  architecture:")
        aggregate_at = self.text.index("\n  check:")
        architecture_block = self.text[architecture_at:aggregate_at]
        self.assertIn('python tools/check_verifier.py --base "$BASE_SHA"', architecture_block)
        self.assertIn('python tools/check_reproduce.py --base "$BASE_SHA"', architecture_block)

    def test_publication_does_not_run_changed_path_checks(self) -> None:
        publication_at = self.text.index("\n  publication:")
        publication_block = self.text[publication_at:]
        self.assertNotIn("--base", publication_block)
        self.assertNotIn("BASE_SHA", publication_block)
        self.assertIn("check_activation.py --full --post-activation", publication_block)

    def test_manual_recovery_is_fixed_and_fail_closed(self) -> None:
        for required in (
            "  workflow_dispatch:\n\npermissions:",
            "if: github.ref_type != 'tag' && github.event_name != 'release' && github.event_name != 'workflow_dispatch'",
            "ref: ${{ github.event_name == 'workflow_dispatch' && 'a193e389fb1ddb0bdc89165b015c95a17eb1e425' || github.sha }}",
            "      - name: Pin manual recovery to immutable v106\n        if: github.event_name == 'workflow_dispatch'\n        run: |\n          test \"$(git rev-parse HEAD)\" = \"a193e389fb1ddb0bdc89165b015c95a17eb1e425\"\n          test \"$(git rev-parse refs/tags/canon-v106)\" = \"8f2d16a216524a04be3e1210821ab1e27535ed77\"\n          test \"$(git rev-parse 'refs/tags/canon-v106^{commit}')\" = \"a193e389fb1ddb0bdc89165b015c95a17eb1e425\"\n          echo \"RECOVERY CONTROLLER $GITHUB_SHA\"\n          echo \"RECOVERY SCIENTIFIC CHECKOUT a193e389fb1ddb0bdc89165b015c95a17eb1e425\"\n          echo \"RECOVERY TAG canon-v106 8f2d16a216524a04be3e1210821ab1e27535ed77\"",
            "      - name: Reproduce every frozen public probe for v106 recovery\n        if: github.event_name == 'workflow_dispatch'\n        env:\n          PYTHONDONTWRITEBYTECODE: \"1\"\n        run: python -u tools/check_verifier.py\n      - name: Reproduce every frozen minimal reproduction for v106 recovery\n        if: github.event_name == 'workflow_dispatch'\n        env:\n          PYTHONDONTWRITEBYTECODE: \"1\"\n        run: python -u tools/check_reproduce.py",
            "      - name: Validate v106 activation after complete recovery replay\n        if: github.event_name == 'workflow_dispatch'\n        env:\n          PYTHONDONTWRITEBYTECODE: \"1\"\n        run: python -u tools/check_activation.py --post-activation --expected-tag canon-v106",
            "      - name: Run activation readback on immutable publication events\n        if: github.event_name != 'workflow_dispatch'",
            "      - name: Preserve tag readback manifest\n        if: github.ref_type == 'tag' && github.event_name != 'workflow_dispatch'",
            "      - name: Verify published release assets\n        if: github.event_name == 'release' || github.event_name == 'workflow_dispatch'",
            "RELEASE_TAG: ${{ github.event_name == 'workflow_dispatch' && 'canon-v106' || github.event.release.tag_name }}",
            "python tools/check_release_manifest.py",
            "cmp canon/SHA256SUMS /tmp/twistj-release/SHA256SUMS",
        ):
            self.assertIn(required, self.text)
        self.assertNotIn("inputs:", self.text)
        self.assertNotIn("continue-on-error:", self.text)

    def test_complete_replays_precede_static_readback_and_assets(self) -> None:
        publication = self.text[self.text.index("\n  publication:"):]
        names = (
            "Reproduce every frozen public probe for v106 recovery",
            "Reproduce every frozen minimal reproduction for v106 recovery",
            "Validate v106 activation after complete recovery replay",
            "Verify published release assets",
            "Complete pinned v106 recovery",
        )
        positions = [publication.index(name) for name in names]
        self.assertEqual(positions, sorted(positions))
        for name in names:
            self.assertEqual(publication.count(name), 1)
        self.assertNotIn("--base", publication)
        self.assertNotIn("BASE_SHA", publication)

    def test_forbidden_trigger_absent(self) -> None:
        self.assertNotIn("pull_request_target:", self.text)


if __name__ == "__main__":
    unittest.main()
