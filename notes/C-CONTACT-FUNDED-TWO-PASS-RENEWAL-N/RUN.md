# First execution at the public source pin

**NON-CANONICAL / L1. Result-exposed finite replay, candidate-C.**

All four source files were publicly committed and read back byte-identical
before the new verifier's first execution. The execution used a clean
checkout at the exact public source pin. The analytical construction and
static reviews preceded execution; this was not a blind discovery experiment.

| Field | Recorded value |
| --- | --- |
| Public source pin | [eeb69c75f14d5bfe5b2358540740a9cf0b01d0d5](https://github.com/mathorn1973/twist-j/commit/eeb69c75f14d5bfe5b2358540740a9cf0b01d0d5) |
| Parent/base | 0c33e2b281e39127c269ef5dd7f5b529a62e9e65 |
| Reservation | [#1868](https://github.com/mathorn1973/twist-j/issues/1868) |
| Started (UTC) | 2026-11-03T06:24:04.241678+00:00 |
| Finished (UTC) | 2026-11-03T06:25:14.289526+00:00 |
| Operating system | Linux |
| Architecture | x86_64 |
| Python | 3.13.5 |
| Command from repository root | python3 -I notes/C-CONTACT-FUNDED-TWO-PASS-RENEWAL-N/verify.py |
| Assertions | enabled; optimized invocation is rejected |
| Exit code | 0 |
| Stdout bytes | 1013 |
| Stdout SHA-256 | 65b74d7cc56a19b6ce71b49b4a7ea8a6ed785dedfb8414a189c44d5e3a8f4448 |
| Stderr bytes | 0 |
| Stderr SHA-256 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| Verifier SHA-256 | 443817e09a60b7c901f2f10e354aa3bc92e099b5aa22e876e5859d1968338ee4 |
| Specification SHA-256 | e4e02cce8e9b236005a73558db911bbdc08fcf11cd45be917af9341f9765b619 |
| Proof SHA-256 | 9d8d0c6b4d1e69274d4917c7718625cb6dc12e92c5e159589f1e88cc43a9f759 |

The first run passed every assertion, exited zero and wrote no stderr.
Its actual stdout was saved before adoption, unchanged, as
[EXPECTED.txt](EXPECTED.txt). No scientific retry or source correction was
needed. The proof, specification and verifier remain byte-identical to the
source pin. The evidence commit adds the actual stdout, this neutral record
and a hash manifest, and updates the README.

## Measured output

All **4160 complete two-pass cases and 4160 complete native inverses** passed.
The 4096 consecutive-parameter cases and 64 declared large-integer cases each
include all four supplied initial charts. The measured totals are

    707200 primitive calls = 270400 enabled + 436800 refused.

The complete-output fingerprint is

    b1b4c85bc263651167cfe5cceb82e516175df8cfbb58ce4a2219267001272e7e

Its ordered serialization is fixed in [REPLAY-SPEC.md](REPLAY-SPEC.md).
It includes every final source port, both depth archives, all four spent
donors and the two unchanged old archives. The audit checks both real
quadratic embedding accounts before taking the trace, the positive integer
account, the sum and all labelled residues.

Both source renewals act on the actual occupied output of their preceding
native pass. The current-state readers return the stated scalar, chart and
depth. Galois comparisons hold at all 34 corresponding powered-contact
boundaries on the 33-slot cores. The two commonly supplied old archive values
are retained literally and excluded from that Galois comparison.

At h=0 the executed scalar chain is 3 -> 5 -> 1. The initial donor account is
14368; the final donor residues cost 14798, the new records cost 1650 and the
final ready source costs 272. Their sum equals the initial core account 16720.

## Interpretation

This is one scientific execution on Linux x86_64. Static mathematical reviews
are not additional executed implementations. The required repository
architecture jobs do not select this notes-only verifier, so their success
cannot be counted as a second scientific architecture.

The executed word includes two funded renewals on the declared cylinder
n=64h+3 and the preselected depth word (1,4). It does not autonomously select
an unknown valuation branch. The donor coefficients and schedule encode
this finite itinerary, and the initial bank is supplied explicitly.

The general finite-itinerary compilation corollary is supported by its
analytical proof. It was not added to or inferred by extrapolation from this
finite corpus. No minimum-funding, indefinite-renewal, Collatz-convergence,
physical-calibration or public Canon promotion is claimed.
