#!/usr/bin/env python3
"""Temporary preparation-only wording patch for the v61 export builder."""

import test_v61_build_export as v61

v61.V61_CANON_BLOCK = v61.V61_CANON_BLOCK.replace(
    "inside the theorem rather than hidden.",
    "inside the theorem rather than omitted.",
)
v61.V61_CANON_BLOCK = v61.V61_CANON_BLOCK.replace(
    "For `H=g+g^-1`, the sector eigenvalues",
    "For `H_k=g_k+g_k^-1`, the sector eigenvalues",
)
v61.V61_CANON_BLOCK = v61.V61_CANON_BLOCK.replace(
    "det[zI-(H+tA)]",
    "det[zI-(H_k+tA)]",
)
