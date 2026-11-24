# Completed public two-architecture evidence

PUBLIC / NON-CANONICAL / L1. SPDX-License-Identifier: Apache-2.0.
Readback date: 2026-10-18.

This record attests the completed scientific result commit
a8fff343b73849d0b9d45c94f48cee897b14921d, whose accepted executable pin
is 624098e9f0b18ba5dda3f0bc57b0a669409a5d2b. It does not predeclare
checks of the later documentation commit that adds this evidence record.

## Actual run and checkout

Workflow: policy. Run: 39163382353. Attempt: 1.
Declared head: a8fff343b73849d0b9d45c94f48cee897b14921d.
Status: completed. Conclusion: success.

https://github.com/mathorn1973/twist-j/actions/runs/39163382353

The workflow actually checked out the synthetic PR merge commit
6ee0197233b041152597d735676ef9fcbfcf7adc. The GitHub Git-commit API
confirmed that this checkout and the declared result head share the exact
tree ac2b4fb042f8d212c697ca28a0e67f845d920dcf. The merge parents are
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d and the result head above.
This is verification of the tested bytes, not only the branch name.

| Job | Actual job ID | Conclusion |
|---|---|---|
| architecture-aarch64 | 117781204326 | success |
| architecture-x86_64 | 117781204476 | success |
| check | 117781381996 | success |
| publication | 117781205432 | skipped under the PR workflow condition |

The root and a separate authority reviewer each inspected the actual
completed job metadata and decoded job logs. Both architecture logs ran
the scoped public-probe replay with BASE_SHA set to the public basis
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d. Each printed its corresponding
VERIFY ARCHITECTURE value and the same exact success line:

```text
VERIFY PASS P-NATIVE-P-RECURRENCE-BOUNDARY-1 6e4490cc3cbf0e207121cadbd44bbac0ed1ad6de50c6611f9709b0b41561d160 340abf65ec084ca16869c1777f7ce6d1591e97060d4097c6b9b940e69c74b007
```

The first digest is verify.py SHA-256. The second is the exact combined
stdout SHA-256 from RUN.md and EXPECTED.txt, 1366 bytes and 19 lines.
The pinned parent executable launches break.py as a separate process;
therefore successful byte-identity replay covers both implementations.
The summary job printed TWO-ARCHITECTURE CHECK PASS.

Job evidence:

- https://github.com/mathorn1973/twist-j/actions/runs/39163382353/job/117781204326
- https://github.com/mathorn1973/twist-j/actions/runs/39163382353/job/117781204476
- https://github.com/mathorn1973/twist-j/actions/runs/39163382353/job/117781381996

Both architectures also passed the policy, Canon, ledger and gate-contract
checks and all 189 repository operational tests. Minimal reproductions
were correctly reported NOT APPLICABLE. No retry or further scientific
experiment was used to obtain this public result.

This supplies the two-architecture computation evidence for the exact
frozen audit. It does not make the result external blind confirmation,
admit the new actuation as original U, realize the full P contract, or
promote any Canon status. The dispositions in RESULT.md remain unchanged.
