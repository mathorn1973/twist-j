# P-J-NORM-TRACE-TANGENT-SEAM-1 local run record

Date: 2026-08-29

Status: local x86_64 reproduction and adversarial audit. This record does not satisfy a two-architecture gate by itself and changes no Canon or Registry status.

The flat fields below are the machine-readable record required by `tools/check_verifier.py`.

```text
pin_commit: 06572b7b9c59ffcccacbe14d0e163b79e4ae57cb
verifier_sha256: 0f6eaf58024ab9a48be68422e4b84b6c74628418debc76cf9da65c3eb20c403b
command: python3 probes/P-J-NORM-TRACE-TANGENT-SEAM-1/verify.py
platform: Linux 6.18.35
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: 35eed8bd25608414804228fae3d7beb7c947e56846be7761885867eb8e76c069
stdout_bytes: 729
stdout_lines: 11
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Final pin audit

```text
base commit:       39e61fbfe794b0d3d3ab2a28ba9f960c13f4fe7f
final pin commit:  06572b7b9c59ffcccacbe14d0e163b79e4ae57cb
PREREG sha256:     b0db1411c9dc2b3a2eef3d8fd2863fce0d0b95848c4abc1880f6cbf5032e72c8
PREREG bytes:      5660
PREREG Git blob:   4d94b82a5c9854785b21d980aa716ad574789c45
verify bytes:      9803
verify Git blob:   8ef21dbd6bada00c57671d4ec1fb04c2cb92c8a9
break sha256:      adc70237fb8e40f2a8afc82d855a769140cbdd1378784509748f94966edbcd03
break bytes:       4970
break Git blob:    23402b3c8fd6026164209867c41ad397000d7795
```

All three final pinned blobs were read back from the public branch before execution. The local copies had identical SHA-256 and Git blob identities.

## Pre-run transport correction

Commit `dc5d4ac67554e1ac0d53cfd07a0b9c707dfea5d1` was an initial transport commit. Readback found that its `PREREG.md` Git blob did not match the intended local blob. No verifier or breaker was executed. The preregistration was rewritten without changing carrier, equations, scope, controls, thresholds, or accepted code, and commit `06572b7b9c59ffcccacbe14d0e163b79e4ae57cb` became the final pin. Only the final pin is evidence-bearing.

## Sanitized environment

```text
OS=Debian GNU/Linux 13
LC_ALL=C
PYTHONHASHSEED=0
TZ=UTC
PATH=/opt/pyvenv/bin:/usr/bin:/bin
```

Formal command as executed:

```text
env -i PATH=/opt/pyvenv/bin:/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /opt/pyvenv/bin/python3 verify.py
```

No external data were opened.

## Accepted verifier run

The pinned verifier was executed twice after the final pin. Both executions returned:

```text
exit code:       0
stdout bytes:    729
stdout lines:    11
stdout sha256:   35eed8bd25608414804228fae3d7beb7c947e56846be7761885867eb8e76c069
stderr bytes:    0
```

The two stdout files were byte-identical. The two empty stderr files were byte-identical. The repeated execution is reproduction only.

`EXPECTED.txt` is the exact accepted stdout.

## Same-session breaker

The pinned `break.py` was also executed twice in the same sanitized environment:

```text
exit code:       0
stdout bytes:    450
stdout lines:    8
stdout sha256:   0c11844dc8cd662385aad181ecd869fec27ed9960143bbadee669d4153a5d820
stderr bytes:    0
decision:        BREAKER NO BREAK
```

The two breaker stdout files were byte-identical. This breaker was written and frozen before the positive verifier, but it is same-session work. It is not blind independent confirmation.

## Repository two-architecture reproduction

The repository workflow ran on evidence commit `83df9bde5e4d9cfe3fd41fd7e355a8816286dbbe` through pull request #661.

```text
workflow run:     33269931412
PR merge test:    931a455d178dafe55682f4bf6b992cfaa88b2d3d

x86_64:
  OS:             Ubuntu 24.04.4
  Python:         CPython 3.12.14 x64
  verifier sha:   0f6eaf58024ab9a48be68422e4b84b6c74628418debc76cf9da65c3eb20c403b
  stdout sha:     35eed8bd25608414804228fae3d7beb7c947e56846be7761885867eb8e76c069
  verdict:        PASS

aarch64:
  OS:             Ubuntu 24.04.4
  Python:         CPython 3.12.14 arm64
  verifier sha:   0f6eaf58024ab9a48be68422e4b84b6c74628418debc76cf9da65c3eb20c403b
  stdout sha:     35eed8bd25608414804228fae3d7beb7c947e56846be7761885867eb8e76c069
  verdict:        PASS

aggregate:        TWO-ARCHITECTURE CHECK PASS
```

Both architecture jobs also passed policy, 142 tool tests, Canon v71 with 342 claims, the ledger, and the gate contract. The verifier and stdout hashes match the local accepted record and each other exactly. The two architecture runs are repository reproductions of one pinned proof carrier. They are not independent mathematical confirmation.
