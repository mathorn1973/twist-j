#!/usr/bin/env python3
"""Minimal verifier runner for P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2.

Author: A. M. Thorn <thorn@twistj.com>
License: Apache-2.0
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(newline="\n")
    probe_dir = Path(__file__).resolve().parent
    break_path = probe_dir / "break.py"
    spec = importlib.util.spec_from_file_location("break_audit", break_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {break_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["break_audit"] = module
    spec.loader.exec_module(module)
    return int(module.main())


if __name__ == "__main__":
    sys.exit(main())
