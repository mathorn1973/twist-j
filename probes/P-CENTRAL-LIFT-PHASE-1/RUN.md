# RUN P-CENTRAL-LIFT-PHASE-1

## Immutable pin

```text
pin_commit: 0c8adc4ea22b88c5fb65f78ea567cd4e04f9aa26
prereg_sha256: dfd55508116db2020c21a0b5cf424d201a1d3e034833b072dcf451f87be6fb3a
prereg_bytes: 12907
prereg_blob: ed12d90527cec30fc37d5221b5045e68ebf45bbb
verifier_sha256: d062a009a98db0e1c26f1c95b2e3df04f04f14a79f68df4ec7784a9d8d40e163
verifier_bytes: 4706
verifier_blob: 9157af72c144074a20dd01a46c5c3053f21eda76
```

Issue #251 was opened before the branch, probe path, pin, and formal
execution. The branch started from public `main` commit
`60228fa5784f10df69ea6e3d96872b6652909628`. The immutable pin above is
its one direct child and contains exactly `PREREG.md` and `verify.py`.
It was pushed to public branch `probe/P-CENTRAL-LIFT-PHASE-1` before the
first formal execution. The owner accepted the exact section 7 proof
and scope as theorem-grade before the pin.

## Formal run

```text
command: python3 probes/P-CENTRAL-LIFT-PHASE-1/verify.py
platform: Ubuntu 24.04
architecture: x86_64
python: Python 3.12.3
exit_code: 0
stdout_sha256: 0609c48f3df68d79c0cea9fd38cbccaab14ad908590f00767a51322944a994cc
stdout_bytes: 826
stdout_lines: 11
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
start_utc: 2026-08-02T12:46:29Z
finish_utc: 2026-08-02T12:46:29Z
deterministic_executions: 1
gates: 10 of 10 PASS
```

The command was executed once from the repository root with
`LC_ALL=C`, `LANG=C`, `PYTHONDONTWRITEBYTECODE=1`,
`PYTHONHASHSEED=0`, and `TZ=UTC`. The frozen verifier exited 0, wrote
no stderr, and its exact raw stdout is `EXPECTED.txt`.

The required GitHub x86_64 and aarch64 jobs have not yet run on this
result tree. No two-architecture computation gate is claimed by this
record.
