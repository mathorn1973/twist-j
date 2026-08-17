# P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1 local run record

Date: 2026-08-17

Status: local reproduction record only. This record does not satisfy the public
two-architecture gate by itself and changes no Canon status.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 98cdb4f42b19445aca15656c9c3f6fe2d7e28737
verifier_sha256: a0b86d78e414825c386e3f08c654ec73e0d174c73f097cb311fa5244a07f4b67
command: python3 probes/P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1/verify.py
platform: macOS 26.5.2
architecture: aarch64
python: 3.9.6
exit_code: 0
stdout_sha256: 711bb0e825029c2f77a84f74934c8af32224d53da934bf5c8e484ff801edd59c
stdout_bytes: 3013
stdout_lines: 49
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: 569546e48301b5cde035dd248243be19274b73a4f92ba2655703663c563d8fdf
PREREG bytes:  18046
PREREG blob:   40076cce0b703f4333d08e5eb9712829ddc49259
verify bytes:  13802
verify blob:   330eec9f8c959a1c1574b55da0f8c626e0d1e26c
```

The verifier was executed from a fresh clone of the public repository at the
pushed pin commit, from the repository root. Before execution, the SHA-256 of
both pinned files was read back from the public remote clone and matched the
values recorded at the pin. The canonical repository reproduction command is
the machine-readable `command` field above.

Environment for the accepted run:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

No external data were opened. Wall time 16 seconds, within the 120 second
budget declared in PREREG.md.

## Accepted run

```text
checks:   40/40 PASS
decision: VERDICT PASS
```

`EXPECTED.txt` is the exact accepted stdout and has the same byte count, line
count, and SHA-256 recorded above. The run was executed twice on the local
system with byte-identical stdout, and reproduced byte-identically on a
second architecture (Ubuntu 24.04.4 LTS, x86_64, Python 3.12.3) from its own
fresh clone of the pinned branch before this record was committed. The same
verifier bytes had earlier produced the same stdout, byte for byte, in the
incubation lane on both of those architecture classes; the lane record is
cited by hash in `PREREG.md`. The repository-required GitHub x86_64 and
aarch64 jobs at pull-request time complete the public two-architecture gate.

The written proofs embedded in `PREREG.md`, not this finite audit, carry the
universal quantifiers of statements P1 to P7; the verifier audits them at
complete finite scope.
