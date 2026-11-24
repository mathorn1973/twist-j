# First run: P-BOUND-PAIR-CAPTURE-MOMENTUM-1

Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

```text
pin_commit: 8ceec7a35f68aa6d78c1f8dee698956a74bf4ef3
verifier_sha256: 353841176f0d3bfc61de312a0006e2674f039498789a895b56bd449f4a2b12d4
prereg_sha256: 6453c2292b392246ef4dd228c3a8d9cfc6b7b338d8ae16e94b8205956fd6207a
command: python3 probes/P-BOUND-PAIR-CAPTURE-MOMENTUM-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 9e440107eadca6c01197ba25fdf1837c212187a6f0308e1e508d7ab351132985
stdout_bytes: 700
stdout_lines: 15
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
timeout_seconds: 60
public_readback_utc: 2026-10-27 20:38:47 UTC
started_utc: 2026-10-27T20:39:06.524163+00:00
ended_utc: 2026-10-27T20:39:07.614813+00:00
```

## Prospective custody

The complete eight-file analytical and executable package was committed,
pushed to the reserved public branch, and fetched from GitHub at the exact
pin above before the first scientific execution. All eight public files
were compared byte for byte with the accepted local files. Both accepted
proofs and the complete source manifest were present in that pin.

| Pinned file | Bytes | SHA-256 |
|---|---:|---|
| `notes/C-BOUND-PAIR-CAPTURE-MOMENTUM-N/PROOF_CAPTURE_PROFILE.md` | 12556 | `855c20e2878ceeb5df87abe468f6925ef0302645fc11b44eb2f9db48bfbb45f5` |
| `notes/C-BOUND-PAIR-CAPTURE-MOMENTUM-N/PROOF_PORT_LIFT.md` | 17023 | `81eb9ed502d31af2340b63c787ec0d005ec501d3699980eeabc25f0c1db04d70` |
| `notes/C-BOUND-PAIR-CAPTURE-MOMENTUM-N/README.md` | 4130 | `fcb07d92acda3f790c8f61197ea48b9b4a93f3de1f0001c57aeda32ecd853466` |
| `notes/C-BOUND-PAIR-CAPTURE-MOMENTUM-N/SOURCES.md` | 3679 | `852772da8d4fef61ed2a902080d80adfaf5b1d2e39ad2ce162ad41acd96e4b06` |
| `notes/C-BOUND-PAIR-CAPTURE-MOMENTUM-N/VALIDATION.md` | 3641 | `b5bbca4446a1ca6b25ac3f7840ee9df41f4fa233d03ad9ed46178a52c574efcd` |
| `probes/P-BOUND-PAIR-CAPTURE-MOMENTUM-1/PREREG.md` | 7032 | `6453c2292b392246ef4dd228c3a8d9cfc6b7b338d8ae16e94b8205956fd6207a` |
| `probes/P-BOUND-PAIR-CAPTURE-MOMENTUM-1/README.md` | 768 | `a5934130fdb5c5b8d099c0bb18fb262e1fd530f631fe3603a68e00fe678271b3` |
| `probes/P-BOUND-PAIR-CAPTURE-MOMENTUM-1/verify.py` | 7718 | `353841176f0d3bfc61de312a0006e2674f039498789a895b56bd449f4a2b12d4` |

The clean repository root and the pinned verifier/preregistration hashes
were checked before execution. The displayed command was launched once
under a 60-second outer timeout with stdout and stderr captured separately.
The original streams and neutral metadata were first retained outside the
worktree. The worktree was still clean after execution, and the verifier
hash was rechecked before adding the actual stdout as `EXPECTED.txt`.

The first execution completed normally in the frozen budget: 86 checks,
11 centers, exit 0 and empty stderr. No scientific repair, retry, omitted
center or changed threshold occurred. There was no earlier numerical scan
or incubation execution in this task. Analytical derivation and static
review were disclosed in the preregistration; this is not blind empirical
confirmation.

This local x86_64 run alone does not satisfy the two-architecture gate.
The required PR workflow must replay this same verifier and exact output
on clean x86_64 and aarch64 runners. CI evidence is linked from the PR;
a passing computation does not independently admit the analytical theorem
or promote a Canon claim.

## Required architecture replay observed

The public workflow at result commit
`1dd68997a198e09b778b222cff482080ed12a14f` completed successfully:
[run 40580478120](https://github.com/mathorn1973/twist-j/actions/runs/40580478120).

| Job | Architecture | Disposition |
|---|---|---|
| 122458200433 | aarch64 | `VERIFY PASS`, exact verifier and stdout digests above |
| 122458200929 | x86_64 | `VERIFY PASS`, exact verifier and stdout digests above |
| 122458675108 | aggregate `check` | success |

Both architecture logs were fetched and their printed verifier/stdout
SHA-256 values checked against this first-run record. The workflow also
passed the repository policy, tests, Canon, ledger and gate checks. This
satisfies the two-architecture computation gate for the unchanged
verifier. Any later documentation head is additionally subject to its
own required PR check; the PR links that latest workflow.
