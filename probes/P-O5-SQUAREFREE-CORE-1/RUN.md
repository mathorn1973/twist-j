# P-O5-SQUAREFREE-CORE-1 formal run

```text
status:               ACCEPTED LOCAL FORMAL LEG
pin commit:           f80ff006c5be1793772addc636d328cfb073e407
basis main:           9fbda966b134090128e6f7172e8ce167abe0de8a
platform:             Linux
architecture:         x86_64
python:               CPython 3.13.5
local PATH:           /usr/bin:/bin
resolved interpreter: /usr/bin/python3
```

## Pin readback before execution

The public connector readback established:

```text
PREREG blob:    1f20d71a19dc585f1e8f7d0e03c0b7f17a612662
PREREG SHA256:  26e57fc1986384b9680b43f3acac1bcef1da18b017b745cb2e769b1b0a7c21ee
PREREG bytes:   14992

verify blob:    61da1b9dcf18121ab1064b1d01e2987108ff8e20
verify SHA256:  0df92255bc7b770b5e521e205b2ad10e0c56ac8577dffc61194f65c62f117c4c
verify bytes:   9955
```

The pin has exactly one parent, the declared basis, and exactly two added files under this probe directory.

A direct network clone was unavailable in this runtime because public DNS resolution failed before checkout. No verifier was executed by that failed transport attempt. The local formal surface was then reconstructed from the already prepared bytes whose SHA-256 and Git blob identities had been matched to the public pin. The verifier is self-contained and reads only its own pinned source.

## Frozen startup preflight

Command:

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
```

Result:

```text
exit:          0
stdout bytes:  21
stdout SHA256: 6a35d478a26afbc04957801fbb8b5470693d3ee1f2093354dc03ea48c484ac17
stdout exact:  PYTHON_STARTUP_CLEAN + LF
stderr bytes:  0
```

The preflight passed. The scientific verifier was then invoked exactly once.

## Formal command

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 probes/P-O5-SQUAREFREE-CORE-1/verify.py
```

Result:

```text
exit:          0
stdout bytes:  476
stdout lines:  10
stdout SHA256: 830c1a1550c51c404d6c4a944c4108027b9fb795cf483306998c48f38ad69525
stderr bytes:  0
stderr SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
readout:       VERIFY RESULT 9/9 ALL PASS
```

`EXPECTED.txt` is the complete 476-byte stdout from this one accepted formal execution.

No threshold, pinned byte, mechanism, witness, or source firewall changed after the pin.
