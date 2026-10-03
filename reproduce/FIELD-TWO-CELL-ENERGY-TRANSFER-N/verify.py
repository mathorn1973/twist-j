#!/usr/bin/env python3
"""Pinned public source bridge; runner policy stays in tools/check_reproduce.py."""
from hashlib import sha256
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[2]
NOTE = ROOT / "notes/C-FIELD-TWO-CELL-ENERGY-TRANSFER-N"
SOURCE_SHA256 = {
    "PREREG.md": "b3ad38c5af85519c8cdc9e8dbbd1a5549c6d6c28046caf85b9f3e2be48c39fc4",
    "verify.py": "afbeac83be5fd7b51a57fac1172f3d0be9a4680ec2376756940a166eccb8ad77",
    "break.py": "563a194210deeca40dccf170a90cca1880cbeac88af8b1c60293ddb89e5735ab",
}


def main():
    for name, expected in SOURCE_SHA256.items():
        assert sha256((NOTE / name).read_bytes()).hexdigest() == expected, name
    for label, name in (("primary", "verify.py"), ("challenger", "break.py")):
        print("IMPLEMENTATION " + label)
        runpy.run_path(str(NOTE / name), run_name="__main__")
    print("TRANSFER PASS: NON-CANONICAL L1; source pays receiver; witnesses recur in 5")


if __name__ == "__main__":
    main()
