# Run record

pin_commit: 3ae3ea66e1e3c633c048ece10e3baf43f144d8c7
command: python3 probes/P-INTEGER-RECIPROCAL-SOURCE-ACTION-2/verify.py
verifier_sha256: be41170c18795ec68de7ceaaa7be7c5181aea0e6e0a456db32a97f4ba2e3153e
platform: Windows 11 10.0.26300
architecture: x86_64
python: 3.12.10
exit_code: 0
stdout_sha256: 857a26b1a8caf10e90b56f0f2df222ea1d8557eb2f60a24ff6b32a8093d1bdd8
stdout_bytes: 844
stdout_lines: 27
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-10-19T12:29:03Z
completed_utc: 2026-10-19T12:29:06Z
prereg_sha256: f73255e855e8c0c284791294357461f6f63028b08a96419e58f51fa2776bba63
proof_sha256: 3b3cd3b9f910b5414e1dcb1a01ccc925e564ccf475504865a1763f239a2e0390
source_sha256: 8628b2008eaecf99a749b9bd56b07fa229034f2f0b3640f057b65395efd4c447
breaker_sha256: 6cd89a8624867659603ff3431ada649bbfd6e4bbd8ec765876ad4984faddcc63
frozen_manifest_sha256: fa9b15fcea9d4d25ad419ff69f892449ccf35f54e406b38f1d8875c91c72b746

## Execution custody

This was the first scientific execution of either pinned implementation for
P-INTEGER-RECIPROCAL-SOURCE-ACTION-2. Before execution, all six frozen files
were pushed to origin/probe/P-INTEGER-RECIPROCAL-SOURCE-ACTION-2 and read back
from GitHub at commit 3ae3ea66e1e3c633c048ece10e3baf43f144d8c7 (tree
0b0be6c87eebda2477a3dfad7879d481316611e8) with byte-for-byte identity.
The public prospective pin receipt was posted on ownership issue #1642 before
execution at https://github.com/mathorn1973/twist-j/issues/1642#issuecomment-6267215932.
The consumed predecessor pin P-INTEGER-RECIPROCAL-SOURCE-ACTION-1 was closed on
its own branch and Draft PR #1643 without reusing its directory or overwriting
its fail record.

Environment was set to LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, and TZ=UTC. The primary launched breaker.py with the same Python
executable and -I in a separate process. Both completed with exit code zero and
empty stderr; breaker.py emitted the exact same 25-line certificate bytes as
verify.py, including every final LF, and verify.py appended its two terminal
success lines to form the 27-line stdout.

EXPECTED.txt is the unmodified 844-byte first stdout of verify.py. No frozen
definition, source, proof, fixture, or implementation changed after the pin.

## Required architecture gate

This record states the observed local run only. The draft PR workflow will
replay this exact verifier on x86_64 and aarch64 with Python 3.12 and compare
to the same EXPECTED.txt. The actual workflow and job receipts will be recorded
in the PR and its public comments after their results are observed. Local
x86_64 execution alone does not assert that two architectures have already
passed.
