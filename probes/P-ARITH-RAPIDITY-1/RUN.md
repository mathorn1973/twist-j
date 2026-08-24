# P-ARITH-RAPIDITY-1 local run record

Date: 2026-08-11

Status: local reproduction record only. This record does not satisfy the public
two-architecture gate by itself and changes no Canon status.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 1c4ed7e1c04c9d1813fb412a9a685465e78c5c70
verifier_sha256: 6a7dad0baa248b3566cf8288b129749ad0e69174b589579e7feb31a1f9a7d1c4
command: python3 probes/P-ARITH-RAPIDITY-1/verify.py
platform: Debian GNU/Linux 13
architecture: aarch64
python: 3.13.5
exit_code: 0
stdout_sha256: 67c6aa8aad59fe21b45e068582841ac14da46446194fe8826d41adcb1952a598
stdout_bytes: 2896
stdout_lines: 63
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: e008765f71d9b9ec4fa8ebdb8701c32d18a511b7338cd25e936547b2dd8caf08
PREREG bytes:  15826
PREREG blob:   2b1d31d8d782d1d9320dae61ebff9660252f17ed
verify bytes:  12590
verify blob:   bdbace5977f8bedd7cae6aeaf047da077b7dec8c
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

No external data were opened. Wall time 11 seconds, within the 120 second
budget declared in PREREG.md.

## Accepted run

```text
checks:   26/26 PASS
decision: ARITH-RAPIDITY-PASS
```

`EXPECTED.txt` is the exact accepted stdout and has the same byte count, line
count, and SHA-256 recorded above. The run was executed twice on the local
platform with byte-identical stdout, and reproduced byte-identically on a
second architecture (Ubuntu 22.04, x86_64, Python 3.10.12) from its own fresh
clone of the pinned branch before this record was committed. The
repository-required GitHub x86_64 and aarch64 jobs at pull-request time
complete the public two-architecture gate.

The written proofs embedded in `PREREG.md`, not this finite audit, carry the
universal quantifiers of claims A and C; claim B consumes standard Dirichlet
unit theory.
