#!/usr/bin/env python3
"""Pinned public source bridge; runner policy stays in tools/check_reproduce.py."""
from hashlib import sha256
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[2]
NOTE = ROOT / "notes/C-FIELD-CYCLOTOMIC-WINDOW-AUDIT-N"
SOURCE_SHA256 = {
    "PREREG.md": "c1d6585c03c703948d7ebafd98af4fddff8d456a2947d95b8e5c252d0c4b893c",
    "verify.py": "18917c54c4a21b7b2010757e3657ba761e532ac2fb3d3b9cb48aed833d2aa782",
    "break.py": "cfa213376ac715ca8d634ae950a5cd3e30bc7fe15ce70d5703f424b4ca95a85c",
}


def main():
    for name, expected in SOURCE_SHA256.items():
        assert sha256((NOTE / name).read_bytes()).hexdigest() == expected, name
    for label, name in (("primary", "verify.py"), ("challenger", "break.py")):
        print("IMPLEMENTATION " + label)
        runpy.run_path(str(NOTE / name), run_name="__main__")
    print("AUDIT PASS: exposed targets; NON-CANONICAL L1; proof required for universal claims")


if __name__ == "__main__":
    main()
