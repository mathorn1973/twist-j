# P-QDD-RECORD-COMPLETE-STABILIZER-1 formal run record

Date: 2026-08-20

Status: local formal record. The public two-architecture gate is completed by
the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: b52bcf7bba11eac1f3f1e0839997ca5ec7731719
verifier_sha256: 273ee81df0100ab56360f82c56515c0c2b25a70fae66ad256a7897740bcdea7b
command: python3 probes/P-QDD-RECORD-COMPLETE-STABILIZER-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: 0a48a36c5b25fffc73b5e9ae297d960360d9b174373da959998f72745f58d7cc
stdout_bytes: 860
stdout_lines: 22
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
parent commit: 1ca497af6e3b9f9ec389e9fd1cc241003aca1688
PREREG sha256: c3d3484cdea76bec7b2518591668a20948a765cc37906f58b63412d409a16625
PREREG bytes: 10065
PREREG blob: a68642137796fac2756c1d177cbd10d2b1e7e40f
verify bytes: 14583
verify blob: c65faf563e9b4244b7a4b64ea6c8d3118f8ec7b9
public pin comment: issue #474, comment 5360655393
```

The first attempted Git transport failed at DNS resolution before checkout and
before the verifier process existed. The formal execution count therefore
remained zero. The accepted process was then run once from a clean local
repository-shaped directory containing exactly the two publicly read-back
pinned files under the declared path. Before execution, both SHA-256 values
matched the public pin comment and both local bytes matched the recorded remote
Git blobs.

The accepted process began at `2026-08-20T19:26:03Z` and finished at
`2026-08-20T19:26:05Z`. It used exact standard-library `Fraction` arithmetic
and no external data. The environment was:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

`EXPECTED.txt` is the complete raw process stdout, with LF endings and final
LF. The process wrote zero stderr bytes. The surrounding execution service
emitted `TERM environment variable not set` only after the verifier process,
capture files, and explicit exit record had completed. That service warning is
outside the verifier process and is not part of `EXPECTED.txt` or captured
stderr. The verifier was not rerun.

## Accepted run

```text
checks: 12/12 PASS
decision: RECORD-COMPLETE-SELECTION
positive route: full S4 record-partition covariance leaves one physical class
boundary: affine C4 covariance leaves a three-dimensional centralizer
witness: R-C commutes with C4 but fails 16 of 24 S4 commutation tests per token
target: token 2 gives P_2=E_low and Q_2=E_high
premise: record-partition completeness remains an extra law
boundary: global O2 unchanged; O1 untouched; SAMPLING NOT PROVIDED
```
