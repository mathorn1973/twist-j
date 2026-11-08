# Independent checker run

NON-CANONICAL / L1. This file records the single formal execution of the
code-independent review checker.

## Pin and public readback

| Field | Value |
| --- | --- |
| prereg_commit | 5ea45c52be7e6e0064ed898a24c91d1f7951c36f (PREREG.md frozen before review.py existed) |
| pin_commit | c6855cb6fdd3d7c3261cc5943abeb25a280e8bd2 |
| PREREG.md | 9849 bytes, SHA-256 56d189b77bafc912bc80cfe04ce2d800fa2007489361958222d4e0f73ba91448 |
| review.py | 55881 bytes, SHA-256 d7fa6b7e49c18da08283bac915a76a3c41c11c2ed2aa5df163c078734ceb5fc3 |

Both files were pushed to `origin/claude/fervent-hawking-5kp9fb` at the pin.
They were then fetched from
`raw.githubusercontent.com/mathorn1973/twist-j/<pin_commit>/…` and found
byte-identical to the local files. Only after this readback did the first
execution start.

Before the pin, the checker writer ran only `py_compile` (with bytecode
written outside the repository) and static lint. The writer reports that it
opened no forbidden file. The coordinator inspected review.py statically for
conformance with PREREG.md and requested no change.

The writer added assertions that PREREG implies but does not list
verbatim:
- complete-memory endpoints in R10 and R11;
- the R11 intermediate digits;
- ring self-tests, including N(lambda)=5 and N(J)=1;
- the R2 port on all 625 preparations;
- the R8 trace equal to a.

The coordinator accepted these as part of the frozen contract.

## Execution

```text
command: python3 notes/C-NATIVE-RECEIVER-CARRY-MIRROR-REVIEW-N/review.py --compiler <clean checkout of aaf3ec7>/probes/P-NATIVE-RECEIVER-CARRY-MIRROR-1/arithmetic_compiler.py
cwd: repository root at pin_commit, clean worktree before and after
compiler checkout: detached worktree at aaf3ec7e925c2c0261604179ee4166d542233e14, clean
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1; PYTHONIOENCODING, PYTHONUNBUFFERED, TWISTJ_EVIDENCE_DIR unset; assertions enabled
started_utc: 2026-11-03T20:20:49Z
platform: Linux
architecture: x86_64
python: 3.13.18
exit_code: 0
stdout_bytes: 7022
stdout_lines: 1
stdout_sha256: 42176dd02ca6c268084812ddc6ecef1d9e4b8e6d778c82e84950680cf23b0407
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
elapsed_seconds_engineering: 11.19
```

EXPECTED.txt is the exact stdout. This was the first and only formal
execution. There was no failed attempt, no retry and no change to the
checker or its thresholds. The repository worktree stayed clean, and no
`__pycache__` was created.

The run is on one architecture, so it is a reproduction, not a
two-architecture gate. The target's own two-architecture gate is audited in
CI-AUDIT.md. Ordinary notes-only CI for this package checks repository
integrity. It does not replay review.py.
