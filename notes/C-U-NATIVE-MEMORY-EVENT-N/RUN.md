# Recorded incubation execution

Status: NON-CANONICAL, L1 only. No public status is earned by this run.

```text
preregistration_pin: 9eef145d285325f2b3b48efcc740adf04d574632
preregistration_sha256: 912f0c3f7897a3d0684ea8618da0d8775c7e6d9f01c52c2b4c1dbf3b42a8bcef
pin_commit: 164da1efcf5222d934ffe3b22c32baf01b9cceaf
command: python3 notes/C-U-NATIVE-MEMORY-EVENT-N/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.3
verifier_sha256: bcfc0cc415bcf8b8e2398f7d3ce63929275533ec8a91888b6d428ebddf04f459
exit_code: 0
stdout_bytes: 20271
stdout_lines: 1
stdout_sha256: 76ec658b7b1c4860952898db5d999b7d0d1987efedbd9ee2482dc77a8c457e09
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The preregistration was fetched from its public branch and its exact SHA-256
matched before scientific work. The verifier and proof package were then
committed and pushed at the separate code pin above. A subsequent fetch
returned that exact remote commit; local PREREG.md and verify.py matched
the fetched Git blobs byte for byte, and the worktree was clean before
execution. No amendment, rebase or force push was used.

The execution used Linux Python from the repository root, with LC_ALL=C,
LANG=C, TZ=UTC, PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1. A wrapper
captured the subprocess streams as bytes and saved successful stdout
without newline conversion as EXPECTED.txt. It imposed a 600-second
execution ceiling and did not modify scientific inputs.

All six work packages completed, with 463333 exact comparisons and zero
mismatches. No implementation correction or mathematical falsifier occurred
during this execution. The scientific negative conclusions about writable
records and QDD frequency realization are retained in RESULT.md; PASS means
that the audited identities and classifications agree, not that the physical
measurement route succeeds. This is one architecture only and is not a
formal two-architecture reproduction gate.

The public-main two-architecture workflow 34024518651 had passed before
the incubation. That workflow validated the basis, not this new verifier.
The local policy, Canon, ledger and gate-contract checks also passed.
The initial attempt to run repository checks through Linux Git on a Windows
worktree failed to resolve the worktree metadata path; those infrastructure
checks were rerun successfully with native Git. No scientific code was run
in that failed setup attempt.
