# Stock census execution record

**NON-CANONICAL / L1. Author-side exact finite audit.**

Both recorded prospective runs passed at the same immutable source pin:

- Commit: [4d9fa863852c6054a5f10ac8e32e8b3ca642d548](https://github.com/mathorn1973/twist-j/commit/4d9fa863852c6054a5f10ac8e32e8b3ca642d548).
- Verifier: verify_stock_census.py, 15331 bytes.
- Verifier SHA-256: f63c11cd353b343b638cfe01c0563a2b020cef7a128c50a6cd320ce3c10bc422.
- Command on both architectures: python3 -I -B verify_stock_census.py.
- Working directory: notes/C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N.
- Fixed limits per run: 300 seconds wall time and 1073741824 bytes (1 GiB) memory.

## Execution receipts

STOCK-RUNS.json contains the two supplied run receipts. Their timestamp
strings are retained exactly, including precision and UTC offsets.

| Architecture | Platform | Python | started_utc | Elapsed seconds |
|---|---|---|---|---:|
| x86_64 | Ubuntu 22.04.5 LTS | 3.10.12 | 2026-11-07T09:33:54.993809+00:00 | 2.9023489769999884 |
| aarch64 | Debian GNU/Linux 12 (bookworm) | 3.11.2 | 2026-11-07T09:34:33.610440+00:00 | 8.610958935998497 |

Elapsed values are execution metadata from the receipts, not scientific
outputs. Both receipts report exit code 0, timeout false, and empty stderr.
Neither recorded run reported an assertion failure or a resource-limit
failure. No scientific failure was suppressed or repaired under this pin.

Both scientific stdout files contain 832913 assertions and PASS. They
are byte-identical:

- Length: 1438 bytes.
- SHA-256: 1afa34959c24feb5c8a2d83196e61959c0789a90b893a58b843f42df2955f280.
- Empty stderr SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.

STOCK-EXPECTED.txt is a byte copy of the recorded x86_64 stdout.
The aarch64 run used a fresh public branch clone, detached the exact source pin, and checked a clean Git state and all four source manifests before execution.
Its equality with the aarch64 stdout was checked directly. Packaging this
record involved receipt parsing, byte comparison, and hashing only; it
did not execute or import any scientific verifier.

## Public source custody before execution

The supplied pre-execution public-readback receipt identifies the same
source pin and marks all five following blobs as read back. Their Git blob
identities also match the local pinned bytes.

| Public file | Git blob |
|---|---|
| REVIEW-RESPONSE.md | 6064a4c874cda92945c7c6df947484d8826f61bc |
| STOCK-BOUND.md | 2ebbddb705e22aec8ccfac26d91e83291d2754b6 |
| STOCK-PREREG.md | b7b64cebe63003f2b98ba89cc46344b05d143fe8 |
| STOCK-SHA256SUMS | fd4f7b34e99904655a1155ec198aa72610d6ec80 |
| verify_stock_census.py | 7b47f4dab09f54949f08f0422c775f67b10b1d85 |

All four source entries in STOCK-SHA256SUMS match their declared SHA-256:

| File | SHA-256 |
|---|---|
| REVIEW-RESPONSE.md | bb49983324c55e779e964459d777d335578170580adbbdfd5cdc5978e810c1e3 |
| STOCK-BOUND.md | 54e8d832dc63f2f6f21f24488b264f45fb81ab0358ae1909eb8c632f79ce2819 |
| STOCK-PREREG.md | 7ed18ae23d9dcf6f5873d027186f5511a4dfd773412a6fef0a3e27e083837352 |
| verify_stock_census.py | f63c11cd353b343b638cfe01c0563a2b020cef7a128c50a6cd320ce3c10bc422 |

The three predecessor manifests remain byte-identical to their versions
at 3843abf4e25ff9ba61ed596796dd69c6fc9ed7a0. All their entries still verify:
SOURCE-SHA256SUMS has eight, FULLFIELD-SHA256SUMS has five, and
RECEIVER-SHA256SUMS has five. No predecessor verifier was replayed and
no frozen predecessor source or manifest was edited for this audit.

## Evidence scope

The expected stock counts were exposed in an informal external report
before this author-side preregistration. This record establishes two
architecture executions of the new pinned author verifier. It does not
establish independent acceptance or reproduce the externally reported
121374-assertion checker. The new output explicitly retains that distinction.

The audited finite scope is the prescribed stock class, ten-contact word,
five prepared inputs, terminal stock-Q readout, complete accounting and
inverse controls, and relative-frame tests in STOCK-PREREG.md. The
coordinate-bound proof and explicit Q=22 witnesses are those in the pinned
STOCK-BOUND.md. No unpinned analytical classification is used as accepted
evidence. Physical receiver selection, passive detection, a field-driven
clock controller, electromagnetic coupling, and scientific promotion are
outside this execution record.