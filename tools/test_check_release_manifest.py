#!/usr/bin/env python3
"""Tests for release-manifest file and commit pinning."""

from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.check_activation import manifest
from tools.check_release_manifest import validate_manifest


class ReleaseManifestTests(unittest.TestCase):
    def test_manifest_pins_complete_file_inventory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "canon").mkdir()
            (root / "data").mkdir()
            (root / "reproduce").mkdir()
            (root / "STATUS.md").write_text("STATE: ACTIVE\n", encoding="utf-8")
            (root / "canon" / "CANON.md").write_text("canon\n", encoding="utf-8")
            content = "1" * 40
            activation = "2" * 40
            data = manifest(root, content, activation, False)
            path = root / "manifest.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            validate_manifest(root, path, content, activation)
            (root / "canon" / "CANON.md").write_text("changed\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "inventory"):
                validate_manifest(root, path, content, activation)


if __name__ == "__main__":
    unittest.main()
