# Independent review and repository checks

PUBLIC / NON-CANONICAL, L1. Disposition: reviewed partial candidate,
primary STOP; no promotion readiness or public scientific gate asserted.

## Mathematical and implementation review

The finite-window proof (PROOF 1--8) was written by a separate agent from
the frozen preregistration and inherited definitions before scientific
execution. Its author rechecked empty dimensions, rank deficiency, the
integer quantifier, critical induction, above-window integer growth,
incidence limits and reversal after the audit. No gap was found.

The independently authored break.py was frozen without access to the
primary source/proof/output and completed one successful local execution.
Its author subsequently reviewed PROOF 1--8 and documented the two
primary defects in BREAKER-NOTES.md. This is independent implementation
with exposed targets, followed by exposed review; neither is a blind
discovery or another architecture.

A further separate agent statically reviewed the primary before its pin
and did not detect the two false hard-coded assertions. That review was
insufficient and is not presented as successful verification. After the
executed failure, the same reviewer manually checked PROOF 9--15 against
the independent certificates: K/K^-1, J, W^-1 and actual charges, Hermite
multiplication, Smith transformations, image congruences, shell witnesses
and the rational extension. No mathematical blocker was found. Its raw
admission clarification P F z=z was incorporated explicitly into PROOF 15.
Final scope review of RESULT, RUN and PROMO found no status or gate overclaim.
It caught an unnecessary erroneous graph-diameter sentence in the unpinned
proof text; that sentence was removed before delivery. RESULT now also
distinguishes the definitive primary STOP from the unresolved future gate.

Frozen PREREG.md, verify.py and break.py remain byte-identical to their
public pins. The primary is deliberately still failing; no assertion was
weakened, hidden or corrected in place. The successful breaker does not
erase this disposition. This package contains no successor execution.

## Public scope and security

One notes directory only. Source files use Python standard-library exact
arithmetic, no network or archival code. The primary reads only the six
declared public source files; the breaker reconstructs from definitions.
Scientific stdout and package hashes are small plain text. Machine paths
from the failing traceback are not imported. No Canon, release, registry,
gate owner, sealed probe, shared checker, allowlist or workflow changes.

Existing QDD-INSTRUMENT-APPARATUS, QDD-TERMINAL-EVENT-SEMANTICS and
PHOTON-MASSLESS-PHASE obligations are retained in full. The only next task
is a separately named/pinned successor audit, not a coupling or release.

## Repository validation

The unchanged repository checkers passed locally with Python 3.12:

```text
python -B tools/check_policy.py                         POLICY PASS
python -B -m unittest discover -s tools -p test_*.py     172 tests, OK (1 skipped)
python -B tools/check_canon.py                          CANON PASS v95 claims=484
python -B tools/check_ledger.py                         LEDGER PASS
python -B tools/check_gate_contract.py                  GATE CONTRACT PASS gates=25
```

The initial sandboxed unit-test invocation could not create temporary
fixture directories and failed with filesystem permission errors. Repeating
the unchanged repository checks with normal filesystem access produced the
passing result above. This was an infrastructure check retry, not a retry
of either scientific script. Negative test fixtures intentionally print
PROBES FAIL / REPRODUCTIONS FAIL before the unit suite's overall success.

The normal pull-request workflow remains the public repository acceptance
check. It validates repository integrity and does not scientifically replay
these notes. The primary failure and missing public computation gate remain
as recorded in RUN.md regardless of green repository checks.
