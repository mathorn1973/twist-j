# First public-pin execution

**Status: NON-CANONICAL finite evidence; result-exposed replay.**

The analytical results and explicit witnesses preceded this integrated
verifier. All five source files were publicly committed and read back
byte-identical before the verifier's first execution. The run below was
performed from a clean checkout at that exact public source pin.

| Field | Recorded value |
| --- | --- |
| Source pin | [`7f06f306d95342f8d6c0cc99a22024654db369d9`](https://github.com/mathorn1973/twist-j/commit/7f06f306d95342f8d6c0cc99a22024654db369d9) |
| Parent/base | `0c33e2b281e39127c269ef5dd7f5b529a62e9e65` |
| Reservation | [#1861](https://github.com/mathorn1973/twist-j/issues/1861) |
| Started (UTC) | `2026-11-02T22:33:19.933984+00:00` |
| Operating system | `Linux` |
| Architecture | `x86_64` |
| Python | `3.13.5` |
| Command from repository root | `python3 -I notes/C-COLLATZ-ODD-HEAD-RETURN-N/verify.py` |
| Assertions | enabled; the verifier rejects optimized execution |
| Exit code | `0` |
| Stdout bytes | `1159` |
| Stdout SHA-256 | `d0be33d7076c9606e1c587f66426c7f6c292d396998d4d73196eced15ae6033b` |
| Stderr bytes | `0` |
| Stderr SHA-256 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| Verifier SHA-256 | `070f73f4649c68a7301d18e06728e9fda2557517a5cd05fcb0909c0a589fefeb` |
| Specification SHA-256 | `db6dd58d56c0626248511b6ab357dca6bd2357246e2fa81357868407ae781855` |

The actual first stdout was preserved before being adopted unchanged as
[EXPECTED.txt](EXPECTED.txt). It contains 2299 admissible inverse inputs
in the declared finite box; this count was not guessed before execution.
No assertion failed, stderr was empty, and the run exited zero. The source
was not changed and no retry was needed.

## What this execution establishes

Every assertion in the fixed [inventory](REPLAY-SPEC.md) passed. This
includes actual accelerated-step endpoints, integer inverse reconstruction,
exact residue-cell counts, carry identities, the finite growth family and
its Mersenne boundary, finite block words, affine compositions and rational
moment partial sums. The infinite laws and all-input claims remain the
analytical conclusions of [PROOF.md](PROOF.md) and
[MEASURE.md](MEASURE.md), not finite extrapolations.

This is one scientific execution on Linux x86_64. Required repository CI
runs on two architectures, but its changed-path selectors do not execute
this notes-only verifier. Those jobs must not be counted as a second
scientific reproduction or a two-architecture scientific gate. No Canon,
registry status or global Collatz conclusion is changed.

The four scientific files (`PROOF.md`, `MEASURE.md`, `REPLAY-SPEC.md`,
`verify.py`) remain byte-identical to the source pin. The subsequent
commit adds this neutral record, actual stdout and the hash manifest, and
updates only the README to link the completed evidence.
