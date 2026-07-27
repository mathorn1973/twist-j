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

    def test_aggregate_check_depends_on_architecture(self) -> None:
        block = (
            "  check:\n"
            "    if: github.ref_type != 'tag' && github.event_name != 'release'\n"
            "    needs: architecture\n"
            "    runs-on: ubuntu-latest"
        )
        self.assertIn(block, self.text)
        self.assertIn('echo "TWO-ARCHITECTURE CHECK PASS"', self.text)

    def test_publication_is_single_runner(self) -> None:
        block = (
            "  publication:\n"
            "    if: github.ref_type == 'tag' || github.event_name == 'release'\n"
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
        self.assertIn("python tools/check_incubation.py", architecture_block)

    def test_publication_does_not_run_changed_path_checks(self) -> None:
        publication_at = self.text.index("\n  publication:")
        publication_block = self.text[publication_at:]
        self.assertNotIn("check_verifier.py", publication_block)
        self.assertNotIn("check_reproduce.py", publication_block)
        self.assertIn("check_activation.py --full --post-activation", publication_block)

    def test_forbidden_trigger_absent(self) -> None:
        self.assertNotIn("pull_request_target:", self.text)


if __name__ == "__main__":
    unittest.main()
