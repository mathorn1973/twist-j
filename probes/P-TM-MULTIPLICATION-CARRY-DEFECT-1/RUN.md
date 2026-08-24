# P-TM-MULTIPLICATION-CARRY-DEFECT-1 local run record

Date: 2026-08-10

Status: local reproduction record only. This record does not satisfy the public
two-architecture gate by itself and changes no Canon status.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: fdabf9a15bf5f20875b5db77e6a8b5dbc5a05298
verifier_sha256: 2d5ead2b4a506faddb8f86d9740cf4920ac375ec87af515532e19b1ac7ab055d
command: python3 probes/P-TM-MULTIPLICATION-CARRY-DEFECT-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: d10538998b533f2dc0f6a2796024b90368fb225b7edf21b993fd26b14851e2dc
stdout_bytes: 876
stdout_lines: 19
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: df69655203b307c06136357a83afdaec460c331cc9a65553e8cecf76934a98bf
PREREG bytes:  11404
PREREG blob:   f4d116726a4a8d24ca519e01c1fe4c790651a49e
verify bytes:  8265
verify blob:   d4f94cd32be0782eefb4c2f2fbf557cbec905904
```

The verifier was executed from a local byte-identical copy of the public pinned
`verify.py`. Before execution, both its SHA-256 and Git blob identity were
checked against the public remote. The canonical repository reproduction
command is the machine-readable `command` field above.

Environment for the accepted run:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

No external data were opened.

## Accepted run

```text
checks:   15/15 PASS
decision: CARRY-PASS
```

`EXPECTED.txt` is the exact accepted stdout and has the same byte count, line
count, and SHA-256 recorded above.

The written proof in `PREREG.md`, not this finite audit, carries the universal
quantifiers. A future x86_64/aarch64 GitHub byte-identity run is required before
the probe evidence gate is complete.
