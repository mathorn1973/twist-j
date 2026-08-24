#!/usr/bin/env python3
"""Which files a probe directory must and must not carry.

Split out of check_policy.py so the rule can be tested directly.  The rule
distinguishes two shapes of closed probe:

* a probe that executed its formal gate carries the pin, the accepted
  verifier and the full run record;
* an abandoned pin never executed, so it carries the pin and the verifier and
  is closed by a RESULT.md that records the abandonment.  It must carry no run
  artefacts, so that a probe which did run cannot be relabelled abandoned to
  keep a fired falsifier out of the public record.
"""

from __future__ import annotations

import re


PIN_FILES = ("PREREG.md", "verify.py", "RESULT.md")
RUN_FILES = ("EXPECTED.txt", "RUN.md")

ABANDON_PATTERN = re.compile(r"^Status:.*\bABANDONED\b", re.MULTILINE)


def declares_abandoned(result_text: str | None) -> bool:
    """True when RESULT.md text closes an abandoned pin."""
    if not result_text:
        return False
    return bool(ABANDON_PATTERN.search(result_text))


def problems(present: set[str], result_text: str | None) -> list[str]:
    """Return the reasons a probe directory is not a valid closed record."""
    if declares_abandoned(result_text):
        found = [f"lacks {name}" for name in PIN_FILES if name not in present]
        found += [
            f"is recorded ABANDONED but carries {name}; a probe that ran is "
            "closed by its result, not by abandonment"
            for name in RUN_FILES
            if name in present
        ]
        return found
    return [
        f"lacks {name}" for name in PIN_FILES + RUN_FILES if name not in present
    ]
