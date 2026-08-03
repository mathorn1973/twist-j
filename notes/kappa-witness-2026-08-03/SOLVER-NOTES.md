# Solver notes for the Kappa witness candidate

**STATUS: NON-CANONICAL EXPLORATORY SUMMARY. NO FORMAL EXECUTION RECORD.**

This file preserves only the facts needed to understand how the candidate
JSON was found.  It is not a solver transcript, an optimality certificate, or
public evidence.  Raw `*.log` files are excluded by repository policy.

## Successful searched-anchor report

The rejected delivery commit `501489c47654b2110c426fc5bcd64f8cf93f8d38`
contained a sanitized transcript reporting this exploratory invocation:

```text
repair_witness.py 6 3 6 6 8 3000
front end: PuLP, version not recorded
solver: HiGHS 1.15.1, reported git hash 04024d7
solver license reported by the program: MIT
variable faces: 309808
edge constraints: 235668
reported status: Optimal
reported primal and dual objective: 7993
```

The transcript also referred to unbundled third-party notices, so its
verbatim output is not retained.  The scientific certificate does not depend
on the claimed optimum or on any solver status: the committed JSON is checked
directly and exactly by the two standard-library verifiers.

## Superseded fixed-anchor obstruction

A second rejected transcript reported the rings-6 shell infeasible for an
older fixed-formula bridge placement.  It then showed a Python assertion
failure but incorrectly ended with `exit 0`; the removed wrapper had captured
the status after another shell expansion.  A rings-8 failure for that same
superseded placement was reported as overwritten and has no artifact.
Accordingly, neither historical solver report is used as evidence.

`legacy_bridges_demo.py` retains only the exact, solver-independent local
diagnostic for that placement.  The current searched-anchor construction is
separate.

## Dependency and safety boundary

`repair_witness.py` and `cluster_repair.py` may use PuLP with HiGHS or CBC.
Only HiGHS 1.15.1 was identified in the rejected successful transcript; PuLP
and CBC versions were not recorded.  No dependency is downloaded, vendored,
or executed by the read-only certificate replay.  Builder output is accepted
only from a solver status exactly equal to `Optimal`, and the builders refuse
to overwrite an existing witness file.
