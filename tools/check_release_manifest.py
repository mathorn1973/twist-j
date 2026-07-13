#!/usr/bin/env python3
"""Validate a published Public Canon activation manifest against a checkout."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

try:
    from check_activation import git, manifest, read_status
except ModuleNotFoundError:
    from tools.check_activation import git, manifest, read_status


SHA40 = re.compile(r"^[0-9a-f]{40}$")


def validate_manifest(
    root: Path,
    path: Path,
    content_commit: str,
    activation_commit: str,
) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    exact = {
        "schema": "twistj-activation-manifest-v1",
        "mode": "active",
        "state": "ACTIVE",
        "content_commit": content_commit,
        "activation_commit": activation_commit,
    }
    for field, value in exact.items():
        if data.get(field) != value:
            raise ValueError(f"release manifest {field} mismatch")
    for field in ("platform", "architecture", "python"):
        if not isinstance(data.get(field), str) or not data[field]:
            raise ValueError(f"release manifest lacks {field}")
    expected = manifest(root, content_commit, activation_commit, False)["files"]
    if data.get("files") != expected:
        raise ValueError("release manifest file inventory differs from checkout")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    fields = read_status(root)
    content_commit = fields.get("CONTENT_COMMIT", "")
    if not SHA40.fullmatch(content_commit):
        raise SystemExit("FAIL: STATUS.md lacks a valid CONTENT_COMMIT")
    tagged = git(root, "rev-parse", "canon-v1^{}")
    if tagged.returncode:
        raise SystemExit("FAIL: canon-v1 tag is unavailable")
    activation_commit = tagged.stdout.decode().strip()
    try:
        validate_manifest(root, args.manifest.resolve(), content_commit, activation_commit)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(f"FAIL: {error}")
    print(
        "RELEASE MANIFEST PASS "
        f"content={content_commit} activation={activation_commit}"
    )


if __name__ == "__main__":
    main()
