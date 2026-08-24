#!/usr/bin/env python3
"""Prep-only overlay validating v62 Canon identity without contaminating content fold."""

from __future__ import annotations

import hashlib
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


_ORIGINAL_RUN = subprocess.run


def _replace_status_field(text: str, field: str, value: str) -> str:
    pattern = rf"(?m)^({re.escape(field)}:\s*).*$"
    replaced, count = re.subn(pattern, rf"\g<1>{value}", text)
    if count != 1:
        raise AssertionError(f"STATUS field {field} replacement count={count}")
    return replaced


def _run_with_v62_overlay(args, *pargs, **kwargs):
    cwd_value = kwargs.get("cwd")
    command = list(args) if isinstance(args, (list, tuple)) else None
    if (
        command
        and len(command) >= 2
        and str(command[1]) == "tools/check_canon.py"
        and cwd_value is not None
    ):
        cwd = Path(cwd_value)
        canon_path = cwd / "canon/CANON.md"
        status_path = cwd / "STATUS.md"
        if canon_path.is_file() and status_path.is_file():
            title = canon_path.read_text(encoding="utf-8").splitlines()[0]
            status_text = status_path.read_text(encoding="utf-8")
            if title == "# TWIST-J Public Canon v62" and "CANON:          Public Canon v61" in status_text:
                with tempfile.TemporaryDirectory() as td:
                    overlay = Path(td) / "overlay"
                    shutil.copytree(
                        cwd,
                        overlay,
                        ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
                    )
                    canon_bytes = (overlay / "canon/CANON.md").read_bytes()
                    canon_hash = hashlib.sha256(canon_bytes).hexdigest()
                    status = (overlay / "STATUS.md").read_text(encoding="utf-8")
                    status = _replace_status_field(status, "CANON", "Public Canon v62")
                    status = _replace_status_field(status, "TAG", "canon-v62")
                    status = _replace_status_field(status, "CANON_SHA256", canon_hash)
                    status = _replace_status_field(status, "CANON_BYTES", str(len(canon_bytes)))
                    (overlay / "STATUS.md").write_text(status, encoding="utf-8", newline="\n")
                    citation_path = overlay / "CITATION.cff"
                    citation = citation_path.read_text(encoding="utf-8")
                    citation, count = re.subn(
                        r'(?m)^version:\s*"61"\s*$', 'version: "62"', citation
                    )
                    if count != 1:
                        raise AssertionError(f"CITATION version replacement count={count}")
                    citation_path.write_text(citation, encoding="utf-8", newline="\n")
                    print("V62 PREP CHECK_CANON overlay=release-form metadata only")
                    overlay_kwargs = dict(kwargs)
                    overlay_kwargs["cwd"] = overlay
                    return _ORIGINAL_RUN(args, *pargs, **overlay_kwargs)
    return _ORIGINAL_RUN(args, *pargs, **kwargs)


subprocess.run = _run_with_v62_overlay


class V62CheckCanonOverlayTest(unittest.TestCase):
    def test_overlay_hook_is_installed(self) -> None:
        self.assertIs(subprocess.run, _run_with_v62_overlay)


if __name__ == "__main__":
    unittest.main()
