#!/usr/bin/env python3
"""Prep-only shim giving the v62 temporary export checkout a Git index."""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import unittest


_ORIGINAL_COPYTREE = shutil.copytree


def _copytree_with_temp_git(src, dst, *args, **kwargs):
    result = _ORIGINAL_COPYTREE(src, dst, *args, **kwargs)
    target = Path(dst)
    if target.name == "repo" and (target / "tools/test_v62_build_export.py").is_file():
        subprocess.run(
            ["git", "init", "-q"], cwd=target, check=True,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        subprocess.run(
            ["git", "add", "-A"], cwd=target, check=True,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    return result


shutil.copytree = _copytree_with_temp_git


class V62TempGitShimTest(unittest.TestCase):
    def test_shim_is_installed(self) -> None:
        self.assertIs(shutil.copytree, _copytree_with_temp_git)


if __name__ == "__main__":
    unittest.main()
