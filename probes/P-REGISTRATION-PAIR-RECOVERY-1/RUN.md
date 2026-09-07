# First pinned run

pin_commit: d71a413ede89cfedec7ad58cd4ff47e73f993f6c
verifier_sha256: 9f6bc87bbb5628713a3c5622248a7711a20aa75b44d709e09ba6cf3639b229cc
command: python3 probes/P-REGISTRATION-PAIR-RECOVERY-1/verify.py
platform: Linux
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: aaf88823ee75bbfd3a613f371fbadaded05728f81431ab6f923ce7bedc7cb24a
stdout_bytes: 1397
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

Environment:

```
LC_ALL: C
LANG: C
TZ: UTC
PYTHONHASHSEED: 0
PYTHONDONTWRITEBYTECODE: 1
elapsed seconds: 0.6589003099943511
```

Command, from the repository root:

```
python3 probes/P-REGISTRATION-PAIR-RECOVERY-1/verify.py
```

The three accepted sources were committed and pushed before this first
execution. Their complete bytes were fetched from the GitHub contents API at
the full pin, SHA-256 compared with the local files, and checked again by the
run launcher before execution. Static proof/code reviews and AST parsing were
the only pre-pin code inspections; no prior import or scientific run occurred.

| Accepted source | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 8200 | `24df25470d72d0bd47e96496334552f034ce7a29bcb170c368a5ede463050a36` |
| PROOF.md | 10932 | `7e765df044f11d0cb48f6447d34e8db282369cbe9c1b8c314ac370be67b09dbe` |
| verify.py | 22654 | `9f6bc87bbb5628713a3c5622248a7711a20aa75b44d709e09ba6cf3639b229cc` |

Raw stdout was preserved without editing as EXPECTED.txt:

```
stdout SHA-256: aaf88823ee75bbfd3a613f371fbadaded05728f81431ab6f923ce7bedc7cb24a
stderr SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Result: PROOF_AUDIT_PASS, 20,531 checks, failure_count=0 and an empty failure
list. The intended exact counterexamples survive. No external measurement
file, network input, floating-point fit or stochastic simulation was used.

Required PR CI separately replays the unchanged verifier with Python3.12 on
x86_64 and aarch64 and compares raw stdout with this same EXPECTED.txt.
Those workflow records supply the independent architecture checks; this file
records only the first pinned execution and makes no advance CI claim.
