# P-KERNEL-SUBSET-LANDSCAPE-1 formal run record

Date: 2026-08-20

Status: local formal record. The public two-architecture gate is completed
by the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 5613256fcaa5271ac9559e9c2fd8108618cab67c
verifier_sha256: ac2ed2573ee26666e0636ba074b1732b35e930a68b93f96fd90ee4fd79e22722
command: python3 probes/P-KERNEL-SUBSET-LANDSCAPE-1/verify.py
platform: Ubuntu 24.04.4 LTS
architecture: x86_64
python: CPython 3.11.15
exit_code: 0
stdout_sha256: c0874fe27b81d520e32e1038150cabe1b34e0ef401c7aea731f6eb58b31dc313
stdout_bytes: 1785
stdout_lines: 44
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: 9315af5d0aeef1cd9470e1a499e948bf5772be60e3a90fba9414dde78fb78987
PREREG bytes:  6431
PREREG blob:   8ec809fce75a700311c3c1bc1e63dc1e39237560
verify bytes:  8946
verify blob:   8542c9301b6fc855dcdcab3ea67b2583d4c0cce7
public pin comment: issue #449, comment 5353402844
```

The verifier was executed once, formally, from a clean checkout of the
public repository at the pushed pin commit, from the repository root.
Before execution the SHA-256 of both pinned files was read back from that
checkout and matched the values recorded at the pin and in the public pin
comment. `EXPECTED.txt` is the exact raw stdout of that one execution, LF
line endings, final LF. The process exited zero and wrote no stderr.

Environment for the accepted run:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

No external data exist in this probe. Wall time about one second, within
the 120 second budget declared in `PREREG.md`. As disclosed in `PREREG.md`,
the probe is result-exposed; the candidate file was smoke-executed once
before the pin, outside the repository, revealing nothing not declared.

## Accepted run

```text
checks:   7/7 PASS
decision: the 32-entry landscape is decided; connectivity holds exactly
          at dim U_S = 6, connected subsets acde and abcde
```
