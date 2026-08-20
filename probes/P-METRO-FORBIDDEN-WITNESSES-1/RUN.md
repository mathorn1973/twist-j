# P-METRO-FORBIDDEN-WITNESSES-1 formal run record

Date: 2026-08-20

Status: local formal record. The public two-architecture gate is completed by
the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: e5e94fe4d933c1b7d9da32a1df9a3a0421b87fa4
verifier_sha256: 884d9a51deee630e6d5fe3b1db085166809a7bf57dae98109629c7ad03a45ca5
command: python3 probes/P-METRO-FORBIDDEN-WITNESSES-1/verify.py
platform: Ubuntu 24.04.4 LTS
architecture: x86_64
python: CPython 3.11.15
exit_code: 0
stdout_sha256: df0adcbf79fd1f56d4ff22f71e409d8a6d178593759a8add4fa15d4071d7dc24
stdout_bytes: 2159
stdout_lines: 33
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: 3613112f4053810f5aa3518f531d0b7312d49d05bced216dc5aa2671ac318c7d
PREREG bytes:  14765
PREREG blob:   a395a97cf7e4c273b64b85635e2cfe2c2eea37d0
verify bytes:  14817
verify blob:   178fe92cd0b6aaa2b57a329882f046d1e67126ab
FOLD-ROWS.tsv sha256:
               0ac27c589e20b473b1587fedd3b8a54597174cf48d5e9e77601f2a16785b0f7c
FOLD-EDITS.md sha256:
               437aabfc1a813231acd73559ad3ce42858584bb3c5c4ebd31405de6f3cab0ea1
```

The verifier was executed once, formally, from a clean checkout of the probe
branch at the pin commit, from the repository root. Before execution the
SHA-256 of both pinned files was read back from that checkout and matched the
values recorded at the pin. `EXPECTED.txt` is the exact raw stdout of that one
execution, LF line endings, final LF. The process exited zero and wrote no
stderr.

Environment for the accepted run:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

No external data exist in this probe. Wall time about five and a half seconds,
within the 120 second budget declared in `PREREG.md`.

## Pin strength, stated plainly

The protocol's pin is a pushed commit. This pin was a local commit at the time
of the accepted run and was pushed afterwards, in the same session, before the
pull request. Two mitigations are recorded and neither is a substitute:

```text
1  The pinned commit was never amended, rebased or force-pushed. It contains
   only PREREG.md, verify.py and the two frozen fold files; EXPECTED.txt,
   RUN.md and RESULT.md arrive in a separate later commit, so the ordering is
   visible in the history.
2  Every expected value in PREREG.md was written before the pin and the
   accepted run reproduced all of them, including the six census counts, the
   4329 commuting tuples, the 13320 report count and the five witness
   positions.
```

Disclosed and not smoothed over: the verifier is carried in from the
incubation lane rather than rewritten, exactly as `PREREG.md` declares under
Provenance, with two non-semantic edits. A smoke execution of that adapted file
was performed once outside the repository before the pin.

## Interpreter sweep

Run from the same clean checkout, outside the accepted single execution, as an
integrity check on determinism rather than as evidence:

```text
CPython 3.10  stdout_sha256 df0adcbf79fd1f56d4ff22f71e409d8a6d178593759a8add4fa15d4071d7dc24
CPython 3.11  stdout_sha256 df0adcbf79fd1f56d4ff22f71e409d8a6d178593759a8add4fa15d4071d7dc24
CPython 3.12  stdout_sha256 df0adcbf79fd1f56d4ff22f71e409d8a6d178593759a8add4fa15d4071d7dc24
CPython 3.13  stdout_sha256 df0adcbf79fd1f56d4ff22f71e409d8a6d178593759a8add4fa15d4071d7dc24
```

All four byte identical, empty stderr in every case. The verifier carries no
`sys.version_info` guard by choice: a frozen guard would turn a runner
resolving a different minor version into an integrity STOP on a probe that
cannot be repaired in place.

## Accepted run

```text
checks:   12/12 PASS
decision: each of the five forbidden entries of section 15, under the ratified
          readings, admits an exact functional obstruction; the four admitted
          arrows exhibit none; obligation B is discharged for those five
          entries and the parent stays open
```
