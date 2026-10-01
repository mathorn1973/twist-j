#!/usr/bin/env python3
"""Pinned public source bridge; runner policy stays in tools/check_reproduce.py."""
from hashlib import sha256
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[2]
NOTE = ROOT / "notes/C-FIELD-THREE-CELL-DELAYED-TRANSFER-N"
SOURCE_SHA256 = {
    "PREREG.md": "9b9f0c6ceab706474ac74ed0229df30fafced164ad128400770315a18796aa7d",
    "verify.py": "42ec10cd001028ec126045647eea89347ec12bbf3612c40e1aa204ab77913a59",
    "break.py": "fc435a7efffea8edd4bd8e11aa12e16c2d1489a39c74997ae0b204837b7445b1",
}


def main():
    for name, expected in SOURCE_SHA256.items():
        assert sha256((NOTE / name).read_bytes()).hexdigest() == expected, name
    for label, name in (("primary", "verify.py"), ("challenger", "break.py")):
        print("IMPLEMENTATION " + label)
        runpy.run_path(str(NOTE / name), run_name="__main__")
    print("DELAY PASS: NON-CANONICAL L1; middle at 1, arrival at 2, receiver work at 3")


if __name__ == "__main__":
    main()
