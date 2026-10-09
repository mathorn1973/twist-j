# First completed unit-reader audit

pin_commit: ceb9e07e0842b17086bc990547af3f04a1e66bc0
verifier_sha256: 90a908b81d8cb7e71934fa3a83138ba30da5922441757d3db53ba6297f6b1478
command: python3 probes/P-HYPOTHETICAL-UNIT-READER-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: b0ddf5d82629e707ed9aafe9100e477100e75db5ea454fd277413d83d75f3745
stdout_bytes: 2839
stdout_lines: 252
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-10-09T13:06:14.165014+00:00
completed_utc: 2026-10-09T13:06:15.951139+00:00
elapsed_seconds: 1.786082
public_input_readback_utc: 2026-10-09 13:05:34 UTC

## Complete public input custody

All nine pre-run files were committed as A. M. Thorn, pushed and fetched
back independently through public GitHub at the full pin above. Every
fetched base64 payload matched the reviewed local bytes. The local
committed Git blobs also matched those bytes. The first execution began
on the clean exact pinned tree.

The final verifier contains the manifest SHA-256
bfe0d650bd273864985159cd63a6623f7fa40df11c8b1525d79c1ab1ee813b34.
INPUTS.sha256 binds the seven listed documentation/science inputs.
Its own bytes and the wrapper are bound by the public commit; the wrapper's
final digest is recorded above. All nine hashes were unchanged after the run.

## Actual first execution

The command above ran from the repository root. The parent environment
used LC_ALL=C.UTF-8, LANG=C.UTF-8, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1. The accepted wrapper invoked both scientific
programs using the same Python with -I -B, with a 55-second limit each.

Both completed with exit zero and empty stderr. Their entire sorted JSON
reports were byte-identical. The common report includes the independently
computed transition-table hash, all frozen witness outcomes and thirteen
complete boundaries of the twelve-step example.

This was the first execution of model.py's scientific functions and of both
new audit programs. No scientific input, source, predicate or threshold was
changed after the pin. EXPECTED.txt is copied from the actual captured
stdout; it is not reconstructed from anticipated values. The exact parent
streams and administrative receipt were retained from this execution.

The actual transition-table SHA-256 is
7c52a4fb34110c9edc53b72d28f65df689b5c7ba44d1bbc9ba450b6f456e19b7.
The report audits 211200 complete raw states, including 26400 with calibrated
zero flags, twelve two-write preparations, six disconnection pairs at 78
boundaries, the context/fault/energy witnesses and the complete return.

## Interpretation and public replay

This record establishes one local x86_64 audit with the stated Python.
The existing required workflow independently replays the same accepted
verifier under Python 3.12 on x86_64 and aarch64, comparing against the
single EXPECTED.txt and final verifier hash. Live PR checks provide that
gate; this first-run record does not pretend those jobs had already run.

Universal results are separately reviewed written proofs in MODEL.md.
The finite domain N<=8 is a computational audit, not an infinite-domain
argument, a laboratory measurement or a derivation of the new contact
from U/J. Physical status remains a working hypothesis.
