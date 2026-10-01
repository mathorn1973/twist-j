# Finite-chain first delivery: public candidate

PUBLIC / NON-CANONICAL / candidate-T by conditional proof / L1.
Authority remains Public Canon v95. Reservation: [#1311](https://github.com/mathorn1973/twist-j/issues/1311).

For the exact preparation and four-layer law of #1310, this candidate proves
first boundary delivery at N-1 and first receiver reaction at N for every
finite N>=2 and every integer w with H(w)=1. The full state has32N-1
coordinates and initial energy41. Every individual cut fixes the prepared
downstream component for all time. The target returns to R in step N+1;
the result is first work, not a persistent record.

Read the [proof](PROOF.md) for the universal mathematical argument and the
[public replay protocol](PREREG.md) for exposure, custody, dependencies and
the unchanged bounded audit. [REVIEW.md](REVIEW.md) records static review.
Post-pin execution is documented separately in RUN.md once a run exists.
No new execution is implied merely by this README or by the source pin.

## Historical local package and known results

The six files SCOPE.md, PROOF.md, audit.py, audit_challenger.py, RESULT.md and
SHA256SUMS are preserved byte for byte from the local analytical package.
Its [RESULT.md](RESULT.md) records the Windows exploratory audit performed
**before any public pin**:20 seeds,6280 connected boundaries,151 cut cases
and2079 occupied-contact cases. The user supplied the candidate induction
before that work. Its conclusions and output digest were already exposed.

Statements in those original files that no issue, commit, public gate or
publication exists describe the time of the original local audit. They are
not the current publication status. Their original manifest remains the
local receipt; PUBLIC_SHA256SUMS binds this prospective public package.
No local execution is retroactively described as publicly preregistered.
New runs test reproducibility of known results, not independent discovery.

## Dependency and replay

This is a stacked candidate on the open draft
[#1310](https://github.com/mathorn1973/twist-j/pull/1310), exact commit
`dd354e3e01ad7f7bb535f33e012c5ef1b46a87d2`. Its unmerged candidate inputs
remain noncanonical. The new bridge verifies the exact source hashes and
invokes the unchanged generic-N audit, which runs both representations and
compares them to the full-state formula. It uses only Python's standard
library and the pinned public predecessor files present in this checkout.

From a clean pinned checkout, run the unchanged repository runner:

```text
python3 tools/check_reproduce.py --base dd354e3e01ad7f7bb535f33e012c5ef1b46a87d2
```

The new [reproduction entry](../../reproduce/field-finite-chain-first-delivery-n/README.md)
is selected by the existing CI workflow on both x86_64 and aarch64. Its
scientific stdout retains the original wording, including LOCAL AUDIT PASS;
the distinct REPRODUCE PASS receipt supplies the new public replay evidence.
Only actual completed runs and their logs can establish that evidence.

Connected execution stops at N; return at N+1 is proved analytically.
There are no added lengths, preparations, memory registers, laws, period
searches or physical identifications. This handoff authorizes a reviewed
draft only: no merge, Canon fold, promotion, tag or release.
