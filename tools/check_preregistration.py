#!/usr/bin/env python3
"""Validate non-formal post-Genesis preregistration drafts."""

from __future__ import annotations

import argparse
from pathlib import Path

from genesis_artifacts import GenesisArtifactError, validate_prereg


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        drafts = validate_prereg(args.root.resolve())
    except GenesisArtifactError as error:
        print(f"FAIL: {error}")
        raise SystemExit(1)
    print(f"PREREGISTRATION DRAFTS PASS drafts={drafts}")


if __name__ == "__main__":
    main()
