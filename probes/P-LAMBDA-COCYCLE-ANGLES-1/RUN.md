# P-LAMBDA-COCYCLE-ANGLES-1 formal run record

The preregistration and verifier were committed, pushed, and read back from the
public branch before execution. The local formal leg below invoked the pinned
verifier exactly once from the repository root on a clean worktree. The
pull-request architecture gate is pending.

pin_commit: d7ad9d9973a7859e030b42e572b7f64a1f926b2d
base_commit: 11a059cc1578f2d48037b523c670196a49ae8f40
prereg_sha256: 736b9bd8b6a189c9c9a4a80ac128c7f259c4f87a0d7539f3ae66adcdb761b783
prereg_bytes: 19332
prereg_git_blob: 22456b519aae74558aea2d13b3dbe6e7c023bd30
verifier_sha256: 3263191dd30c07f9895f1b2c95f347d3d9a45ecb8dfcf136e1a34997891f62b1
verifier_bytes: 16208
verifier_git_blob: 8138eb42247fa794f20667994ea4d1f7ed045dc4
command: python3 probes/P-LAMBDA-COCYCLE-ANGLES-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04
architecture: x86_64
python: CPython major 3 minor 11 patch 15
compatibility_basis: standard-library CPython with a portable process environment and no system-dependent verifier operations
run_started_utc: 2026-08-06T14:22:10Z
run_finished_utc: 2026-08-06T14:22:10Z
pre_run_clean: yes
post_run_clean: yes
deterministic_executions: 1
exit_code: 0
stdout_sha256: 9e46f7f56d7e4b22683e3b595707f5bb880ef707771ac75aaa35a8dcc2584688
stdout_bytes: 2118
stdout_lines: 32
stdout_cr_bytes: 0
stdout_final_byte: 0a
stdout_git_blob: 3f4b7d203cf5a4b587699988eb09d2b383a52b66
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: 31/31 ALL PASS
architecture_gate: pending; the required GitHub Linux x86_64 and aarch64 jobs must reproduce EXPECTED.txt byte for byte
public_lock: issue 284

## Integrity notes

`EXPECTED.txt` is the exact raw standard output from the one formal local
execution. It is LF-only, contains all 32 lines, ends in LF, and has the hash
and byte count recorded above. Standard error is the exact empty byte string.

The remote readback preceding execution compared the two pinned blobs as stored
by the remote against the local worktree. Both agreed:

```text
origin/claude/pracovni-ukoly-s1rdl3 = d7ad9d9973a7859e030b42e572b7f64a1f926b2d
PREREG.md  remote sha256 736b9bd8b6a189c9c9a4a80ac128c7f259c4f87a0d7539f3ae66adcdb761b783
verify.py  remote sha256 3263191dd30c07f9895f1b2c95f347d3d9a45ecb8dfcf136e1a34997891f62b1
```

The verifier forms no floating-point value, reads no external file, and imports
only `fractions` and `sys`. Before the pin it was checked to produce byte
identical standard output under `LC_ALL=C TZ=UTC PYTHONHASHSEED=0` and under
`LC_ALL=cs_CZ.UTF-8 TZ=Asia/Tokyo PYTHONHASHSEED=1`, so the recorded bytes do
not depend on locale, timezone, or hash seed. That determinism check was run on
a development copy outside the repository; the pinned file's first execution is
the formal leg recorded above.

The local leg is Linux x86_64. The required workflow supplies clean Linux
x86_64 and Linux aarch64 executions, and its full-byte comparisons are required
before the architecture gate can pass. No conclusion relies on a machine name
or on an operating-system-specific operation.
