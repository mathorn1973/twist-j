#!/usr/bin/env python3
"""Validate Genesis reconstruction decisions and frontier splits."""

from __future__ import annotations

import argparse
from pathlib import Path

from genesis_artifacts import GenesisArtifactError, validate_recon


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        recon, splits = validate_recon(args.root.resolve())
    except GenesisArtifactError as error:
        print(f"FAIL: {error}")
        raise SystemExit(1)
    print(f"GENESIS RECON PASS decisions={recon} child_gates={splits}")


if __name__ == "__main__":
    main()
