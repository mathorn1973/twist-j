"""Temporary Ubuntu preflight for the exact Public Canon v27 release object."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CONTENT_COMMIT = "116b62edf505914d96fcd65318d97f3675c53f85"
RELEASE_COMMIT = "afc6f1fba20a959f5b26216d08d6598646899d6f"


class V27ActivationPreflightTests(unittest.TestCase):
    @unittest.skipUnless(sys.platform.startswith("linux"), "Linux publication preflight")
    def test_exact_release_object_passes_full_activation(self) -> None:
        with tempfile.TemporaryDirectory(prefix="twistj-v27-") as temporary:
            checkout = Path(temporary) / "release"
            added = subprocess.run(
                ["git", "worktree", "add", "--detach", str(checkout), RELEASE_COMMIT],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )
            self.assertEqual(added.returncode, 0, added.stdout + added.stderr)
            try:
                result = subprocess.run(
                    [
                        sys.executable,
                        "tools/check_activation.py",
                        "--full",
                        "--content-commit",
                        CONTENT_COMMIT,
                    ],
                    cwd=checkout,
                    capture_output=True,
                    text=True,
                    timeout=600,
                )
                output = result.stdout + result.stderr
                self.assertEqual(result.returncode, 0, output)
                self.assertIn("ACTIVATION PASS mode=active full=True", output)
            finally:
                subprocess.run(
                    ["git", "worktree", "remove", "--force", str(checkout)],
                    cwd=ROOT,
                    capture_output=True,
                    text=True,
                    check=False,
                )
