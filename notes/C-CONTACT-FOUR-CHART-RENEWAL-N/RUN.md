# First execution at the public source pin

**NON-CANONICAL / L1. Result-exposed finite replay, candidate-C.**

All five source files were publicly committed and read back byte-identical
before the new verifier's first execution. The execution used a clean
checkout at that exact source pin. Analytical results preceded the verifier;
this record does not call the work a blind discovery experiment.

| Field | Recorded value |
| --- | --- |
| Public source pin | [4b7e4e7d176bdae9bf77546d91fcb5a9d93fa234](https://github.com/mathorn1973/twist-j/commit/4b7e4e7d176bdae9bf77546d91fcb5a9d93fa234) |
| Parent/base | 0c33e2b281e39127c269ef5dd7f5b529a62e9e65 |
| Reservation | [#1866](https://github.com/mathorn1973/twist-j/issues/1866) |
| Started (UTC) | 2026-11-02T23:09:03.081836+00:00 |
| Operating system | Linux |
| Architecture | x86_64 |
| Python | 3.13.5 |
| Command from repository root | python3 -I notes/C-CONTACT-FOUR-CHART-RENEWAL-N/verify.py |
| Assertions | enabled; optimized invocation is rejected |
| Exit code | 0 |
| Stdout bytes | 1167 |
| Stdout SHA-256 | bc577e3d5bed6066b335f9e1c9e94b53bd84e459f61131f1be6f1a0ea6c03e7d |
| Stderr bytes | 0 |
| Stderr SHA-256 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| Verifier SHA-256 | 57062f5759311db2d92313da46d25fee09540bf21d2af4ef56012ef1abeab246 |
| Specification SHA-256 | d3024c6eb74b45ae8451ca158aa91a0d256d08f5206193ff110d42b5c036b652 |

The first run passed every assertion, exited zero and wrote no stderr.
Its actual stdout was saved before adoption, unchanged, as
[EXPECTED.txt](EXPECTED.txt). No scientific retry or source correction was
needed. Both proofs, the specification and the verifier remain byte-identical
to the public pin; the evidence commit adds this record, actual stdout and
hash manifest and updates the README.

## Exact measured output

All 12,648 complete forward cases and their complete native inverses passed.
The run made exactly 948,600 primitive calls: 243,095 enabled and 705,505
refused. The complete-output fingerprint is

    46084744671a17aa3cf4951881d2f889ebc715582ac70c46953da88854865722

Its serialized domain and order are fixed in
[REPLAY-SPEC.md](REPLAY-SPEC.md). It includes complete occupied outputs,
not only decoded scalar answers. Galois comparisons cover every corresponding
powered-contact boundary; the fixed old archives are checked literally
and are excluded from the core-only Galois comparison.

The eight depth-13/14 saturation witnesses returned the prescribed boundary
result. They are not accepted arithmetic cases within depth twelve. The
original construction was executed separately in the same frozen audit to
check the record costs and compare resource conditions.

## Interpretation

This is one scientific execution on Linux x86_64. Static mathematical
reviews are not additional executed implementations. The repository's
required architecture jobs do not select this notes-only verifier, so their
success cannot supply a second scientific architecture.

The actual executed words create the stated one-pass outputs and invert them.
They do not reload a source, autonomously select the next chart, or convert
an occupied original E output into the new F source. Necessary funding
inequalities are not experimentally attained minima. Infinite record-horizon,
ideal-filtration and affine-loader statements are supported by their proofs,
not by extrapolating this finite inventory. No public Canon status changes.
