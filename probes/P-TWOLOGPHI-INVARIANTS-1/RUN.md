# P-TWOLOGPHI-INVARIANTS-1 formal run record

Date: 2026-08-20

Status: local formal record. The public two-architecture gate is completed
by the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.
That leg has not run: this probe has not been pushed, see the disclosure
below.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: caf3ddf7d473c2c6fcef934e0a11943c6d2a4611
verifier_sha256: 32fb2110a3414ba8a6e958ca6107122ae3a89b9be0cadf82db128095eefd52b0
command: python3 probes/P-TWOLOGPHI-INVARIANTS-1/verify.py
platform: Ubuntu 24.04.4 LTS
architecture: x86_64
python: CPython 3.11.15
exit_code: 0
stdout_sha256: ffa3e76b645cc9c29905ece590aff69c841b3aaaee9223c577e3d0acb86f8e20
stdout_bytes: 4745
stdout_lines: 48
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: 63761d4ad04ebdbdbc8092f08ec729f20d7a714f03b7f5c7323c3be5b1b558df
PREREG bytes:  17406
PREREG blob:   778781a9b09991cae34c1e83ad5aa3c5b5951c7c
verify bytes:  18730
verify blob:   50f7eee987cf55dc11dd23e0fa878fc49f8866c7
FOLD-ROWS.tsv sha256:
               6d1d181858cfbb6a75c41f335fcaa0999413d441b3b661f6298a9fe5fafb7fa7
FOLD-ROWS-BRANCH-B.tsv sha256:
               f1acd18a622ed3973cb0811dcc19be71e3372db31f7b1db8342edd2d475e72fc
public pin comment: NOT PUBLISHED. This session had no push credential for
               mathorn1973/twist-j; the git proxy refused the repository as
               outside the session's authorized set. The pin is a local
               commit and a delivered git bundle, and it is weaker than a
               pushed pin for exactly that reason. See "Pin strength".
```

The verifier was executed once, formally, from a clean checkout of the
probe branch at the pin commit, from the repository root. Before execution
the SHA-256 of both pinned files was read back from that checkout and
matched the values recorded at the pin. `EXPECTED.txt` is the exact raw
stdout of that one execution, LF line endings, final LF. The process exited
zero and wrote no stderr.

Environment for the accepted run:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

No external data exist in this probe. Wall time under two seconds, within
the 120 second budget declared in `PREREG.md`. As disclosed in `PREREG.md`,
the probe is result-exposed; the candidate verifier was smoke-executed once
before the pin, on a copy outside the repository, revealing nothing not
already declared.

## Pin strength, stated plainly

The protocol's pin is a pushed commit. This one is not pushed, so nothing
outside this session witnessed the pinned bytes before the run. Two
mitigations are recorded and neither is a substitute:

```text
1  The pinned commit was never amended, rebased or force-pushed, and the
   delivered bundle contains it with the run records committed on top as
   separate later commits, so the ordering is visible in the history.
2  Every declared expected value in PREREG.md was written before the pin
   and the accepted run reproduced all of them, including the count
   29/29 and the pin value 1860496.
```

The owner should treat the run as reproducible evidence and the pin as
provisional until the branch is pushed and the pull-request check has run
on both architectures.

## Interpreter sweep

Run from the same clean checkout, outside the accepted single execution,
as an integrity check on determinism rather than as evidence:

```text
CPython 3.10  stdout_sha256 ffa3e76b645cc9c29905ece590aff69c841b3aaaee9223c577e3d0acb86f8e20
CPython 3.11  stdout_sha256 ffa3e76b645cc9c29905ece590aff69c841b3aaaee9223c577e3d0acb86f8e20
CPython 3.12  stdout_sha256 ffa3e76b645cc9c29905ece590aff69c841b3aaaee9223c577e3d0acb86f8e20
CPython 3.13  stdout_sha256 ffa3e76b645cc9c29905ece590aff69c841b3aaaee9223c577e3d0acb86f8e20
```

All four byte identical, empty stderr in every case. The verifier carries no
`sys.version_info` guard by choice: a frozen guard would turn a runner
resolving a different minor version into an integrity STOP on a probe that
cannot be repaired in place.

## Accepted run

```text
checks:   29/29 PASS
decision: 2 log phi is anchored arithmetically as log M(J) and as
          Reg(Q(zeta_5)); no layer bridge is created
```
