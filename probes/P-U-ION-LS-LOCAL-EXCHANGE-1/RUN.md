# First formal execution

NON-CANONICAL. This is the recorded exact audit of the frozen local
construction, not a laboratory run or a physical calibration.

- Public preregistration pin: `b1b2019f35fc2cc3bc5b3d364f9d6ad8c2051a11`.
- [Immutable public candidate](https://github.com/mathorn1973/twist-j/tree/b1b2019f35fc2cc3bc5b3d364f9d6ad8c2051a11/probes/P-U-ION-LS-LOCAL-EXCHANGE-1).
- Public readback: `2026-10-04T14:23:45.706608+00:00`; all nine pinned
  files matched their local and Git-object bytes. The worktree was clean.
- Primary SHA-256: `0a12e3ff056638ee4b9c373f7848b338b7a7c335ea5876c620ea0d0b2a530eee`.
- INPUTS.json SHA-256: `66691a0298ed37e8e56dfaa6ffd9db9468b863fd430eab404dca2f8e2d65f3a5`.

Machine-readable record; command runs from the repository root:

```text
pin_commit: b1b2019f35fc2cc3bc5b3d364f9d6ad8c2051a11
verifier_sha256: 0a12e3ff056638ee4b9c373f7848b338b7a7c335ea5876c620ea0d0b2a530eee
command: python3 probes/P-U-ION-LS-LOCAL-EXCHANGE-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: CPython 3.10.12
exit_code: 0
stdout_sha256: baa2242ce69f4d28872a88048697e3447acb5ac60e48e26150649861fe7106fd
stdout_bytes: 767
stdout_lines: 10
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

| Field | Observed value |
| --- | --- |
| Platform | Ubuntu 22.04.5 LTS |
| Architecture | x86_64 |
| Interpreter | CPython 3.10.12 |
| Start UTC | 2026-10-04T14:24:02.624412+00:00 |
| Finish UTC | 2026-10-04T14:24:05.419136+00:00 |
| Elapsed seconds | 2.7966009359952295 |
| Outer timeout seconds | 600 |
| Independent subprocess timeout seconds | 300 |
| Timeout reached | No |
| Exit code | 0 |
| stdout | 767 bytes, 10 LF-terminated lines |
| stdout SHA-256 | `baa2242ce69f4d28872a88048697e3447acb5ac60e48e26150649861fe7106fd` |
| stderr | 0 bytes |
| stderr SHA-256 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

The environment fixed `LC_ALL=C`, `LANG=C`, `PYTHONHASHSEED=0`,
`PYTHONDONTWRITEBYTECODE=1` and `TZ=UTC`. The accepted independent checker
ran in a separate Python `-I` process. Its successful exact JSON stdout
had SHA-256 `0e058e684cc312f77d34a9bb68ec27b9b0112dcf4a79e5899f04d98eff98280f`,
as recorded by the primary output.

The actual successful stdout was copied byte-for-byte into
[EXPECTED.txt](EXPECTED.txt) only after completion. No accepted scientific
file or input was changed, and no failed scientific execution preceded this
run. Pre-pin work was analytical derivation, static review, AST parsing and
administrative/source inspection as disclosed in REVIEW-PREREG.md.

The local run audits the finite exact code path on one architecture.
Required public architecture jobs provide their separate same-head replay;
their success does not establish a physical device error bound.
