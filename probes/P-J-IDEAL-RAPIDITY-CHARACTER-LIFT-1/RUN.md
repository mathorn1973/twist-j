# P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1 formal run record

Date: 2026-08-27

Status: local accepted formal record. The public two-architecture gate is
pending the pull-request workflow, which must rerun the unchanged pinned
verifier on x86_64 and aarch64 and compare stdout byte for byte with the one
committed EXPECTED.txt.

The flat fields below are the machine-readable execution record.

```text
pin_commit: c20e30cca7a0e80bdaf0790d2e7f14ba0d5c5899
verifier_sha256: 8ce993749dee1cb348e52d9d1bbe06c80ce0fcfd1be0a0a5366287d8cf92aae8
command: python3 probes/P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1/verify.py
platform: macOS 26.5.2 (build 25F84)
architecture: aarch64
python: CPython 3.9.6
exit_code: 0
stdout_sha256: 22b2f87614a52875088e6c07ce7e0a3cdcde89ef632a45714ae6b89509538f42
stdout_bytes: 496
stdout_lines: 11
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: 3203f9432b1ee3da5bdfa92f13167233b9edcf2ca0b1fa1513788d6505b716bd
PREREG bytes:  26859
PREREG blob:   964d528a8846b1bc24d654654a9ce4d71f43f310
verify bytes:  35244
verify blob:   4dbc03892f0f77a13ff87aa145a256d8f13aa109
public pin comment: issue #583, comment 5436433702
```

The verifier was executed once, formally, from a fresh clone of the public
repository detached at the pushed pin. Before execution, the full commit,
SHA-256, byte count, Git blob, and LF-only line endings of both pinned files
were read back and matched the public pin comment. EXPECTED.txt is the exact
raw stdout of that execution, with LF line endings and a final LF. The process
exited zero and wrote no stderr.

Accepted environment:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

No external mathematical data were opened. Before the public pin, the
accepted verifier was only read, reviewed, and parsed statically; it was not
imported or executed. Earlier incubation computations are reconnaissance and
are not evidence for this record.

## Accepted readout

```text
checks: 10/10 PASS
root/ideal cross-label: PASS through p<=997
actual ideal-choice local factors: PASS through exponent 8
global refined convolution and augmentation: PASS through n=20000
ternary squarefree shells: PASS on all frozen subsets and multipliers
zero channel C0: PASS through n=10000 by two routes
orientation factor O5 and C0*O5: PASS through n=5000 by two routes
direct-l1 lower-bound gate: PASS through n=5000
Reynolds non-identification and source firewall: PASS
negative witnesses: 11,11,5,11,5,209
```

The pinned PREREG.md and verify.py were not changed after the pin.
