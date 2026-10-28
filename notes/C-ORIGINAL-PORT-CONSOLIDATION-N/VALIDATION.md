# Consolidation validation and publication boundary

**NON-CANONICAL. L1. Source custody and authoring checks.**
Author: A. M. Thorn. Apache-2.0.

## Scope

The change imports three exact analytical packages and adds this
consolidation directory. The imported files and manifests are unchanged.
The only new mathematical text is ENERGY_EXTENSION.md and
MEASURED_CONTINUATION.md, each with eight separate review obligations.
No original20/21-point list is rewritten and no24-point successor is
used without its source.

The public base is `892a0b11089d34e241e1eb76d2c03247022d18e6`.
STATUS, POLICY, AGENTS, CORE and FRONTIER were read. All five normative
hashes, Canon byte count, content/tag ancestry and existing public
authority checks were verified. The immutable release and successful
main/check/publication records are identified in SOURCES.md.

## Checks in this authoring session

The following existing checks actually completed on Linux x86_64 with
Python3.12.14, with zero exits:

| Command or comparison | Observed result |
| --- | --- |
| `python3 tools/check_policy.py` | POLICY PASS |
| `python3 tools/check_canon.py` | CANON PASS v105 claims=577 |
| `python3 tools/check_ledger.py` | LEDGER PASS claims=577 items=641 dependencies=1160 evidence=577 history=1124 gates=26 programs=7 |
| `python3 tools/check_gate_contract.py` | GATE CONTRACT PASS gates=26 |
| `python3 -m unittest discover -s tools -p 'test_*.py'` | 210 tests, OK |
| `git diff --cached --check` | No whitespace errors |
| Original source bytes and three original manifests | All25 imported files remain byte-identical; all22 content entries verify |

No scientific executable, formal gate, numerical simulation or physical
experiment has been run for the new analytical notes. The210 existing
repository tests are infrastructure validation only, including their
expected negative fixtures. New PR architecture jobs are not claimed
merely because local checks or inherited main checks passed.

The energy-extension note received a coordinating proof read. The
measured-continuation proof received a separate same-session adversarial
read against the original controller and thermal-channel definitions.
That read checked the whole-input history factorization, physical
projectors, normalization and both contrast bounds. The final text uses
the ideal setting masses for its additional conditional bound and
explicitly names the reduced endpoint state. These are authoring checks,
not independent scientific acceptance.

## Public scope

The source reservation is issue1776. Opening a PR, passing infrastructure
CI or importing the exact source notes does not promote a claim. Any
public PR and its actual checks must be identified by their returned
GitHub records, not inferred from this document.

Existing Canon, registry, frontier, gates, probes, reproductions,
workflows and predecessor notes outside these imports are not changed.
The old source statements about no publication retain their historical
meaning; this directory records the new intake separately.
