# J-LI-SCHOENBERG-3 AArch64 audit reproduction

```text
STATUS:             NON-CANONICAL INCUBATION RUN
PUBLIC CLAIMS:      none created by this record
DATE_UTC:           2026-07-16T06:39:12Z
PLATFORM:           Ubuntu 24.04.4 LTS
ARCHITECTURE:       aarch64
PYTHON:             3.12.3
```

This record reproduces the immutable `J-LI-SCHOENBERG-3` verifier preserved
in this directory.  It is the second architecture for the finite incubation
certificate.  It is not a formal public probe run and does not create a Canon
or registry status.

## Frozen inputs

```text
verify_lambda3_t2.py
  sha256  49cdaa5769104fda39a18d5a3e75dd4f2da6526e4a2e93201f89345058ebad2a
  bytes   10833
  lines   350

LAMBDA3_T2_EXPECTED.txt
  sha256  678bd1b4e88b12f074c5c46ed06c69f98984570cc3c312a64921a9ac4b0ef60a
  bytes   1542
  lines   28
```

## Execution

The neutral execution environment was fixed by

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

and ran the equivalent of

```text
python3 verify_lambda3_t2.py
```

The result was

```text
exit_code       0
stderr_bytes    0
stderr_sha256   e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stdout_bytes    1542
stdout_lines    28
stdout_sha256   678bd1b4e88b12f074c5c46ed06c69f98984570cc3c312a64921a9ac4b0ef60a
byte_compare    PASS
assertions      11 PASS, 0 FAIL
```

The stdout is byte-identical to `LAMBDA3_T2_EXPECTED.txt` and to the earlier
x86_64 incubation run.

The final line of the immutable expected output still says
`single architecture`.  It is historical output emitted by the pinned source
and must not be edited after the run.  This surrounding record supplies the
later second-architecture fact.

## Status boundary

```text
J-LI-SCHOENBERG-3        two-architecture incubation certificate;
                         candidate-T-ready, public unregistered
J-LI-COCYCLE-REALIZATION O
RH                        O
```

Public promotion would still require a newly preregistered public probe,
immutable public pins, the repository checks, and authoritative registration.
