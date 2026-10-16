#!/usr/bin/env python3
"""Formal verifier wrapper for P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-2."""

from __future__ import annotations

import importlib.util
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location("independent_break", here / "break.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load break.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.main()


if __name__ == "__main__":
    main()
