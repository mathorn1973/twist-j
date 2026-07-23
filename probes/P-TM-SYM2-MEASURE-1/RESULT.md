# P-TM-SYM2-MEASURE-1 result

Status: SCIENTIFIC RESULT; FORMAL AARCH64 LEG PASS;
TWO-ARCHITECTURE COMPUTATION GATE PENDING; PUBLIC CLAIM UNCHANGED

## Recorded decision

```text
route:   NEGATIVE (N2: the canonicality test returns NONCANONICAL)
exit:    0
stderr:  empty
checker: PASS (all certificates green in mode --evaluate)
```

This is a valid negative scientific return, not a technical failure. Under
the exact frozen `S_TM` definition, the complete selector class is not one
projective-linear gauge orbit. The canonicality test therefore returns
`NONCANONICAL`, and the preregistered N2 threshold fires.

## Exact classification certificate

The line-set projective stabilizer has order 60. The subgroup preserving the
registered single-sign-flip involution `sigma_line` has order 12 and is the
computed gauge group. Its action on the complete selector class is free.

The exhaustive selector class has 48 exact members and splits into exactly
four gauge orbits, each of size 12. The classification data are:

```text
selector class:               48 exact members
projective stabilizer order:  60
frozen gauge order:           12
gauge action:                 free
gauge orbits:                 4
orbit sizes:                  12, 12, 12, 12
```

Their lexicographically minimal representatives are:

```text
(0, 2, 4, 5, 3, 1)
(0, 2, 5, 4, 3, 1)
(0, 4, 2, 3, 5, 1)
(0, 4, 3, 2, 5, 1)
```

`EXPECTED.txt` records the complete membership of all four orbit blocks.
Two selectors are gauge-equivalent if and only if they occur in the same
recorded block. Thus the obstruction is an exact finite classification
certificate, not a numerical tolerance or failed search.

## Immutable pin and formal evidence

```text
public lock:          issue 130
parent commit:        390c1d254b0c3939ff7fc9e6b900eac8bd1b877a
preregistration pin: 69ff42438154bc165a74d03e914988efda9bccf9
PREREG.md SHA-256:    c504d7962786436eb68376875f9239c6bc086b57617ced86f4de95a74c7f57d7
verify.py SHA-256:    30b581a2b84e0ac8b3b333e5731f7ecdcfa9bfb975585da0603f02ab3e8ed6eb

aarch64 platform:    Ubuntu 24.04.4 LTS
aarch64 Python:      Python 3.12.3
aarch64 checkout:    clean, detached at the exact public pin
aarch64 executions:  1
aarch64 exit/stderr: 0 / 0 bytes

stdout SHA-256:      395209f15d0943f38b1d8af4f6d20769c5e113c65bac9455944613ab3b40726f
stdout bytes/lines:  9879 / 79
stdout CR/final byte:0 / 0a
result:              NEGATIVE / N2

x86_64 replay:       pending draft pull-request workflow
architecture gate:   pending
```

The complete neutral metadata and exact raw stdout are public in issue #130
comment `5056393829`; the environment-name transcription correction is
comment `5056438053`. `EXPECTED.txt` is byte-identical to that raw stdout.
The pinned `PREREG.md` and `verify.py` remain unchanged.

## What the negative result decides

The probe falsifies canonical selector choice for the exact frozen
bijective length-three contiguous carrier, centered window, coordinate-axis
pairing root, and projective-linear gauge. No selector in one of the four
blocks can be made gauge-equivalent to a selector in another block.

This closes the preregistered positive route for this candidate. It does not
authorize repairing the definition, changing the gauge, moving a threshold,
or rerunning the formal aarch64 leg under this probe id.

N3 and the positive step-6 terminal were not reached and are not claimed as
formally closed. The final checker `RESULT: PASS` certifies computation and
transcript integrity; it does not turn the scientific route positive.

## Scope firewall

The result does not falsify `GOLDEN-SIX-LINE-SYM2-FRAME [T]`, the
Thue-Morse factor language or stationary law, the registered five face
weights, `GYRON-DENSITY`, or every possible future TM-to-measure definition.
It supplies no empirical validation and no physical probability theorem.

`TM-SYM2-MEASURE` remains `[H]`. No Canon, registry, frontier, dependency,
gate, release, or authority change is made by this record. Any treatment of
the negative result in Canon is a later, separately reviewed fold.

## Architecture gate

The clean formal aarch64 execution used the exact immutable public pin,
exited zero with empty stderr, and produced the recorded 9879-byte transcript.
The required GitHub Linux x86_64 replay must still reproduce the same verifier
and stdout hashes and the same bytes. A mismatch, timeout, nonzero exit, or
nonempty stderr is STOP under the frozen protocol and is not rerun.

This file will receive only evidence metadata after the required x86_64 check.
Until then, the two-architecture computation gate remains pending.
