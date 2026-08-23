#!/usr/bin/env python3
"""Temporary non-canonical v61 preparation: print exact public-probe bundle hashes."""

from pathlib import Path
import unittest

from check_ledger import bundle_sha256


class V61BundleHashPreparationTest(unittest.TestCase):
    def test_print_frozen_probe_bundle_hashes(self) -> None:
        root = Path(__file__).resolve().parents[1]
        probes = (
            "probes/P-J-BINARY-NORM-INDEX-1",
            "probes/P-RECORD-QUOTIENT-CALCULUS-1",
            "probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-2",
        )
        for relative in probes:
            path = root / relative
            self.assertTrue(path.is_dir())
            digest = bundle_sha256(path, root)
            print(f"V61_BUNDLE {relative} {digest}")
            self.assertEqual(len(digest), 64)


if __name__ == "__main__":
    unittest.main()
