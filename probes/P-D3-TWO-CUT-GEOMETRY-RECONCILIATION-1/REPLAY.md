# Two-architecture scientific replay

**NON-CANONICAL / L1 / CONFIRMED finite geometry.**
A. M. Thorn, 2026-10-15. Apache-2.0.

Scientific pin: `a96646c22267d59179a5a96a161c5f6f95ba6255`.
Executed result head: `82ad219401d87c3900011d1e8801ffef4221e05b`.
PR #1514, policy workflow run 38723965951. Both jobs and aggregate check
completed successfully. The actual job logs, not just check names, were read.

| Job | Actual job ID | Scientific evidence |
|---|---:|---|
| x86_64 | 116385133190 | VERIFY ARCHITECTURE x86_64 and byte-identical VERIFY PASS |
| aarch64 | 116385133523 | VERIFY ARCHITECTURE aarch64 and byte-identical VERIFY PASS |

Both logs contain the exact line:

    VERIFY PASS P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1 2fcdec303d95782d1b779283eb6aaf238b3ec884b99a8d3aae6142dfb9caf95d 7850a1ef320738aed5966cad4d9f1f4663b3ae3cabfd328895ce1ebb29d8c8a8

Job links:
https://github.com/mathorn1973/twist-j/actions/runs/38723965951/job/116385133190
https://github.com/mathorn1973/twist-j/actions/runs/38723965951/job/116385133523

The shared 5799-byte stdout is EXPECTED.txt, including the complete DOMAIN.tsv
block. Verifier SHA-256 is 2fcdec303d95782d1b779283eb6aaf238b3ec884b99a8d3aae6142dfb9caf95d;
stdout SHA-256 is 7850a1ef320738aed5966cad4d9f1f4663b3ae3cabfd328895ce1ebb29d8c8a8.
Exit zero and empty stderr are enforced by the unchanged repository runner.
The 5029-byte standalone DOMAIN.tsv has SHA-256
2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0.

Six frozen input files, exact stdout, RUN, point list, geometry manifest and
CORRECTION are unchanged by this record. This descendant records successful
replay and updates only RESULT.md plus this receipt; its own required checks
still apply. No mathematical threshold, source set or expected bytes changed.

Program G1 release: https://github.com/mathorn1973/twist-j/issues/1506#issuecomment-6190487767.
New I2 #1515 and V2 #1516 were published with exact body hashes and original
owners notified in #1507/#1508. They are released for claim, not implicitly
running. Old negative records remain unchanged. The corrected input is not
a successful device audit, native realization, experiment or Canon fold.
