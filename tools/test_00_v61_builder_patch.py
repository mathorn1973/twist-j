#!/usr/bin/env python3
"""Temporary preparation-only wording patch for the v61 export builder."""

import test_v61_build_export as v61

v61.V61_CANON_BLOCK = v61.V61_CANON_BLOCK.replace(
    "inside the theorem rather than hidden.",
    "inside the theorem rather than omitted.",
)
