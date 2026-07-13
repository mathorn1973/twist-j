#!/usr/bin/env python3
"""Validate external-source and engineering-disposition manifests."""

from __future__ import annotations

import argparse
from pathlib import Path

from genesis_artifacts import GenesisArtifactError, validate_sources


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        sources, engineering = validate_sources(args.root.resolve())
    except GenesisArtifactError as error:
        print(f"FAIL: {error}")
        raise SystemExit(1)
    print(f"EXTERNAL SOURCES PASS sources={sources} dispositions={engineering}")


if __name__ == "__main__":
    main()
