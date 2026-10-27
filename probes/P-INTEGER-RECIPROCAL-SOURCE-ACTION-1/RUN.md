# First local formal run

pin_commit: a369fbf85feb79a2a10716b8bd7efd9ff8da5814
command: python3 probes/P-INTEGER-RECIPROCAL-SOURCE-ACTION-1/verify.py
verifier_sha256: 2af1a3074b5d934075d33c9dd946bec51b5c982bd04bdc491a6370dfcb41c426
platform: Windows 11 10.0.26300
architecture: x86_64
python: 3.12.10
exit_code: 0
stdout_sha256: 31e352459901a944bccf26ddae6b75408a9a986f2c66ce770080c823f634444a
stdout_bytes: 35
stdout_lines: 2
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-10-19T12:15:08.305849+00:00
completed_utc: 2026-10-19T12:15:09.518899+00:00
prereg_sha256: 591130cef486d8832d98643c32551f971eaacb0a3c05a57e293d6b7f600d21f0
proof_sha256: 10ab191db049880abf6f6c4f615de7277094707db02cb05793e4681c63f4f8d4
source_sha256: fe4e51dc1b21b01bfaa23ccd09839a081a4fc475edfad038113139e0b02b88fd
breaker_sha256: 8486ed7ee12349433f1e5d252d4dc3ec6a75d762a5a0ace6753856ae9ecf394c
frozen_manifest_sha256: 35596bfd44ef37edd639d509b005685c968ae6375d3965e23a3627c75593e1a7

## Execution custody

This was the first scientific execution of the pinned implementation.
Before execution, all six frozen files were public and were fetched back
from the immutable pin a369fbf85feb79a2a10716b8bd7efd9ff8da5814 with
byte-identical contents (tree eb07b550e7a11474eb905cacf91ae812ceb387fb).
The public prospective receipt is
https://github.com/mathorn1973/twist-j/issues/1642#issuecomment-6266947969.

On this first formal run, verify.py completed with exit code 0, empty
stderr, and the 35-byte, 2-line stdout:

    FALSIFIER=INITIAL_DATA
    RESULT=FAIL

The falsifier fired in audit_coupling_selection() at
require(parity_dipole(p1, p0) == expected_beta, "INITIAL_DATA") on word
0100 because the literal beta(w) column in WORDS recorded 0 instead of +1
for word 0100 and 0 instead of -1 for word 1101. Per POLICY.md Section 3,
this completed FAIL is preserved with its exact EXPECTED.txt, RUN.md, and
RESULT.md, leaving all six frozen files unchanged, and the probe is
retargeted under the fresh identifier P-INTEGER-RECIPROCAL-SOURCE-ACTION-2.
