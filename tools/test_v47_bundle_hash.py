from pathlib import Path
import unittest

from check_ledger import bundle_sha256

ROOT = Path(__file__).resolve().parents[1]
PROBE = ROOT / "probes" / "P-TM-SYM2-BORN-HALVING-1"


class V47BundleHashPrep(unittest.TestCase):
    def test_print_bundle_hash(self):
        digest = bundle_sha256(PROBE, ROOT)
        print(f"V47_TM_SYM2_PROBE_BUNDLE_SHA256={digest}")
        self.assertRegex(digest, r"^[0-9a-f]{64}$")


if __name__ == "__main__":
    unittest.main()
