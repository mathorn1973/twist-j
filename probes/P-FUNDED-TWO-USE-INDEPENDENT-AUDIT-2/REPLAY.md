# Exact two-architecture scientific replay

PUBLIC / NON-CANONICAL / L1. A. M. Thorn, 2026-10-15.

The required unchanged repository workflow completed successfully at PR #1517
head 653b5a859ef00f022bb8b9400bc9aa37190f6c50. This is actual scientific
execution, not a notes-only CI badge.

- Run: https://github.com/mathorn1973/twist-j/actions/runs/38727305980
- x86_64: https://github.com/mathorn1973/twist-j/actions/runs/38727305980/job/116396241644
- aarch64: https://github.com/mathorn1973/twist-j/actions/runs/38727305980/job/116396242132
- Aggregate: https://github.com/mathorn1973/twist-j/actions/runs/38727305980/job/116396747265

Both architecture jobs used Python 3.12.15. They passed policy, repository
unit tests, Canon, ledger, gate-contract checks, changed-probe scientific
replay and changed-reproduction checks. Both actual scientific steps logged
VERIFY ARCHITECTURE with their respective architectures and VERIFY PASS for
P-FUNDED-TWO-USE-INDEPENDENT-AUDIT-2 with identical hashes:

```text
verifier_sha256: ca69ea36e59013f9867d316ddcd4ea7b35382a72f554e972df346f21a0233c47
stdout_sha256: ced7a6aec4b4acd83e0ec35abcdd5c4c200787b71eee235417e19b73681f2075
stdout_bytes: 4722
stdout_lines: 49
exit_code: 0
stderr_bytes: 0
```

The logs match the actual verifier/EXPECTED Git blobs. The aggregate logged
TWO-ARCHITECTURE CHECK PASS. CI checkout was synthetic merge
67cb1a0096da07004c49e14908440f945062d687, whose tree
9b3ab725c3eb719f44ee9ac2ce847168f527f1e1 is identical to that PR head.
The verifier retains the repository's 600-second limit and deterministic
environment. No workflow or runner changed.

All ten scientific-pin files still match
4947a92a5e5ca471e7acde009ef255e17a61a493 byte for byte. The first-run record
beeabbe9cbb493212b0868b7d25ebacfdab6785e and own comparison receipt remain
public. This replay establishes cross-architecture byte identity of this
one implementation. It is not cross-implementation equality or independent
proof acceptance. I2 comparison remains pending its new pin and first-run
receipt; no counterpart scientific content has been opened.

This documentation-only receipt is a descendant of the reviewed run head;
its own required current-head CI must also succeed before final submission.
The source pin and exact expected scientific stdout remain unchanged.
