# P-QDD-EVENT-CARRY-BANK-1 formal run record

Date: 2026-08-21

Status: one accepted local formal execution. The theorem-grade written proofs
are in the immutable preregistration. The required public pull-request workflow
must replay the pinned verifier against the complete public checkout on x86_64
and aarch64 and compare stdout byte for byte with `EXPECTED.txt`.

```text
pin_commit: ec0035bc527e12d91697526d3b18cf1afed19ef3
verifier_sha256: dc14af829c95b9b989c3032f72cab82125c597b9e6b2f19a37bba94ceba0854a
command: python3 probes/P-QDD-EVENT-CARRY-BANK-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: b654c73efcf84510d3d10f6e426ef5fbb122cad3ed57417165f8f2624e43c68c
stdout_bytes: 1357
stdout_lines: 19
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649c934ca495991b7852b855
stderr_bytes: 0
```

## Pin and source audit

```text
parent_commit: a25e2c640295962a7983f16d940347b2b7c1525e
prereg_sha256: 2fc41987819e603882c86039ef3b8a951e2f82b5cb84745286b21f19e8c0de10
prereg_bytes: 16100
prereg_lines: 536
prereg_blob: ccfc2be219d433780a728c29c8a6b273c97567ae
verify_bytes: 11039
verify_lines: 316
verify_blob: 4c602dcea3fd1665d49d3e15fbaee5f92b460388
formal_start_utc: 2026-08-21T20:29:42Z
formal_finish_utc: 2026-08-21T20:30:06Z
deterministic_executions: 1
stdout_cr_bytes: 0
stdout_final_byte: 0a
```

Both accepted files were publicly read back from the exact pin by Git object
identity before execution. Their public blobs, SHA-256 hashes, byte counts, LF
line counts, absence of CR bytes, and final LF matched the frozen local bytes.
Static AST parsing passed before the pin. The accepted verifier was neither
imported nor executed before the pin and was executed exactly once afterward.
It was not rerun.

The local architecture boundary used a repository-shaped exact consumed-source
capsule. `canon/CORE.md`, `canon/FRONTIER.md`, and `canon/GATES.tsv` were the
complete public files at the pin ancestry. `canon/CANON.md` was the exact
749-byte `QDD-FRESH-RECORD-EXTENSION` clause copied verbatim from public Canon
blob `899019650e53bde77a1b0fdbd73b6c246e70edda`, fetched in the public line
range 1320 to 1490. It contained no locally authored text and had SHA-256
`52a23f14bb1871c82ec3b7aa135ae1bcea20473d96efe107a0fc449fb37cdbb2`.
The local record does not claim this capsule is the complete Canon file. The
required GitHub replays use the complete 314310-byte public Canon and therefore
independently test the same pinned architecture gate against the full checkout.

## Accepted result

```text
checks: 14/14 ALL PASS
decision: CARRY-BANK-BOUNDARY
contexts: 22
coordinate_phase_total: 1374
commuting_pair_phase_states: 843152
short_schedule_audit: 245411 schedules at two phase vectors
bank_size: 19702414515172535913561087541248
bank_bit_length: 104
bank_factorization: 2^66 * 3^2 * 7^4 * 11 * 13^2 * 17^2 * 23
O1_status: OPEN
sampling_status: NOT PROVIDED
layer: L1 exact arithmetic plus candidate L1-to-L5 event protocol
```
