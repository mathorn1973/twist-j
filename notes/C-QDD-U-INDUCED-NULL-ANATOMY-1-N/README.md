# notes/C-QDD-U-INDUCED-NULL-ANATOMY-1-N

NON-CANONICAL. Incubation candidate, no authority, no Canon change, no `canon/`
file touched, no registry row edited, no status moved. Durable git handoff of
two documents produced 2026-08-16 against Public Canon v49 (tag `canon-v49`,
content commit `dc80228522a4ccb9495550dfbef8ba73b33b2157`).

The subject is how to read the negative half of the probe
`P-QDD-INSTRUMENT-U-INDUCED-1` (claim lock issue #395, pull request #396, pin
`45cad3384c69d7f2e187d88e63c10ecbad965f0d`), which returned `CHANNEL-PASS`
together with `NO-REALIZATION` over the complete class `R x D` and
`POST-UNDEFINED-OR-ZERO-900`.

Two claims are made here and both are modest:

1. the null quantifies over a narrow, exactly stateable class, and it must be
   archived with that class attached or it will be over-read;
2. inside that class the frozen occurrence law has a large exact zero set, 44
   of the 312 nonzero classes, on which the frozen rules are absolute rather
   than statistical, and the published tags cannot tell whether the null lives
   there or on the remaining 268 classes.

The second point is a hypothesis with a stated measurement, not a result.

## Contents

```text
README.md                                            this manifest
C-QDD-U-INDUCED-NULL-ANATOMY-1-N.md                  the archive: class
                                                     definition, target-law
                                                     anatomy, hypothesis H-ZT,
                                                     positive residue, exits
PREREG-DRAFT-P-QDD-OBSTRUCTION-LOCUS-1_2026-08-16.md draft preregistration for
                                                     the diagnostic that would
                                                     decide H-ZT; awaits owner
                                                     ANO on blocks B1 to B5
null_anatomy.py                                      static anatomy script,
                                                     6 gates, stdlib, exact
null_anatomy.stdout.txt                              committed stdout
SHA256SUMS                                           hashes of the files above
```

## Reproduction

From this directory:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 null_anatomy.py
```

Expected: exit 0, empty stderr, stdout byte-identical to the committed
`null_anatomy.stdout.txt` (`SUMMARY 6/6 ALL PASS`).

Reproduction legs recorded while preparing this note, both exit 0 with empty
stderr and stdout SHA-256
`41732b19708218bdf1b18191c30f1c199edd8ecfb30366784a48ea6142c2c531`:

```text
platform: Ubuntu 24.04 LTS   architecture: x86_64   python: 3.11.15
platform: macOS              architecture: arm64    python: 3.9.6
```

These are informal incubation legs recorded for auditability. They are not
formal run records and they do not satisfy the POLICY section 4
two-architecture computation gate, which is defined by the repository workflow
jobs and is not claimed here.

`null_anatomy.py` computes only definitional arithmetic on formulas published
in Canon v49 (sections 2 and 3, `KERNEL-Z6-SYNCHRONIZATION`, `DEF-QDD-*`). It
iterates no orbit, reads no window, sweeps no seed, and recomputes no sealed
probe quantity beyond the Canon-level audit expectations 313 / 25 / 22, which
it reproduces as a transcription check. It is an incubation-lane script and not
a public probe: the POLICY section 4 two-architecture computation gate is not
claimed for it.

## What the script establishes

```text
A1  the five generators are involutions and (bc) has exact order 5
A2  313 classes, 25 ZERO checkpoints, 625 oriented pre-cells,
    22 distinct occurrence values           (reproduces the Canon expectations)
A3  the nonzero classes split 42 / 2 / 268 into LOW-zero target, HIGH-zero
    target, and both branches strictly positive; the two families are disjoint
    and m is strictly positive off the ZERO class
A4  the closure of z_6 splits: the piston half S = p1+p4+p1p+p4p and the fiber
    half s = q+r close separately under every generator
A5  z_6 = S + s is recovered from the two one-dimensional maps and the
    KERNEL-Z6-SYNCHRONIZATION sheet table is reproduced
A6  all six fiber functionals of Lambda_0 are autonomous; s = q+r is the unique
    one entering the selector
```

A3 is the load-bearing input to the archive. A4 to A6 are the structural reason
the measured information locus is exactly the functional `q + r`.

## Status

Nothing here is promoted. `QDD-INSTRUMENT-APPARATUS [O]` is unchanged and both
its blockers O1 and O2 remain at STOP. `QUADRATIC-DECODER-DATA [O]` is
untouched. No `DEF-QDD-*` definition is altered. The sealed probe is not
reopened, amended, renamed or resumed.

The next step is an owner ruling on the draft preregistration, in particular on
whether restricting a sealed quantifier to the positive sector is admissible at
all after the null has been seen. That question is stated explicitly at the end
of the draft.
