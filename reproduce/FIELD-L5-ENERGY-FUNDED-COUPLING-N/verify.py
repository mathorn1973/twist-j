#!/usr/bin/env python3
"""Pinned public source bridge; runner policy stays in tools/check_reproduce.py."""
from hashlib import sha256
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[2]
NOTE = ROOT / "notes/C-FIELD-L5-ENERGY-FUNDED-COUPLING-N"
SOURCE_SHA256 = {
    "PREREG.md": "0cc0e1cffe396d6dbef867549c6bf7634ea1e9c453f8ccec9eb6aab72a2ed753",
    "verify.py": "b0b3312f7c7f9b7cc3a3ad89ac6d7800a32099cb8b1e5098205c90fff17c7d84",
    "break.py": "d581ab780dc74b053ac51220df87c6adb6ed67af2429b4480dae892b76e5e89f",
}


def main():
    for name, expected in SOURCE_SHA256.items():
        assert sha256((NOTE / name).read_bytes()).hexdigest() == expected, name
    for label, name in (("primary", "verify.py"), ("challenger", "break.py")):
        print("IMPLEMENTATION " + label)
        runpy.run_path(str(NOTE / name), run_name="__main__")
    print("COUPLING PASS: NON-CANONICAL L1; one selected finite-cell law; period 10")


if __name__ == "__main__":
    main()
