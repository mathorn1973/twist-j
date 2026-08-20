# Second architecture leg, disclosed and additive

```text
STATUS:   NON-CANONICAL. Additive reproduction record, added after both
          preregistrations were frozen and after both audits had run. It
          changes no label, no threshold, no scope and no pinned artifact.
          Nothing in this file upgrades a candidate label: this bundle is a
          notes handoff, not a public probe, and POLICY grants
          computation-grade status only through the probe procedure.
DATE:     2026-08-20
```

## What was run

Every program of this bundle was executed a second time on a different
architecture, and every one produced stdout byte-identical to the recorded
stdout of the first leg.

```text
first leg   Linux x86_64, CPython 3.11.15
second leg  macOS 26.5.2, arm64, CPython 3.13.13
environment LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

```text
program                            stdout sha256                     match
verify_lambda_grid_audit_1.py      24ce684ad69cda9e38eff107bf8614af  yes
                                   5d0ded85535ebf34c6abf026b710c7c5
verify_lambda_grid_audit_1b.py     b7bb08dbd05cda11042abb312c61c31a  yes
                                   4087df6d3ac4b34f453ec958ae677e77
breaker_lambda_grid_audit_1.py     5fca4696670eb5e89d89ec9e39d3cf50  yes
                                   de7ef17539ca7c9e23c45cc30ca080af
audit_qdd_centralizer_1.py         f997225df4a73c29bd3ee4209792089d  yes
                                   a2ec3064f8571c4833970588834e34cc
```

Standard error was empty in all four runs. Exit codes were unchanged: zero
for the correction leg, the breaker and the QDD audit; one for
`verify_lambda_grid_audit_1.py`, which is the recorded A3-07 audit-code
defect described in section 6 of its audit record and not a new event.

## The one disclosed difference

`breaker_lambda_grid_audit_1.py` and `audit_qdd_centralizer_1.py` open a
repository checkout by absolute path. For the second leg the single path
assignment in each was redirected to the local checkout used here, and the
runs used those edited copies:

```text
edited copy of breaker_lambda_grid_audit_1.py
  sha256 8b59c5f48a6c039ea53b394911c9f728465a2378d0d7c253b5f7968b91527dda
edited copy of audit_qdd_centralizer_1.py
  sha256 0c1d59aae490ca705b0d2bb527ac5089660d20839ee008d017741cd8fbc322e8
```

Nothing else was changed, and the shipped files are the unedited originals.
The edit is exactly the reproduction step described in section 6 of the
README.

## What this second leg also demonstrates

The reproduction checks inside those two programs re-ran the sealed public
verifiers on this second architecture as well, and all of them passed:

```text
probes/P-LAMBDA-COCYCLE-ANGLES-1/verify.py   sealed stdout hash matched
probes/P-LAMBDA-COCYCLE-ANGLES-2/verify.py   sealed stdout hash matched
probes/P-QDD-J-CENTRALIZER-TERMINALITY-1/verify.py
                                             EXPECTED.txt matched byte for byte
```

The checkout used for the second leg is at Public Canon v57, and the sealed
probe files there are byte-identical to the v56 state the audits used, as
recorded in section 1 of the README.
