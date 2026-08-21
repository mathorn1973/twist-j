# notes/C-QDD-U-INDUCED-NULL-ANATOMY-1-N

NON-CANONICAL. Incubation candidate, revision 3. No authority, no Canon change,
no `canon/` file touched, no registry row edited, no status moved. Durable git
handoff of two documents produced 2026-08-16 against Public Canon v49 (tag
`canon-v49`, content commit `dc80228522a4ccb9495550dfbef8ba73b33b2157`).

The subject is how to read the negative half of the probe
`P-QDD-INSTRUMENT-U-INDUCED-1` (claim lock issue #395, pull request #396,
verifier pin `45cad3384c69d7f2e187d88e63c10ecbad965f0d`, result commit
`7df6a605fdff4b5b8a82981795e7d22168d0a081`), which returned `CHANNEL-PASS`
together with `NO-REALIZATION` over the complete class `R x D` and
`POST-UNDEFINED-OR-ZERO-900`.

## Revision history

```text
r1  proposed H-ZT: the whole null carried by the 44 zero-target classes, the
    268-class positive sector untested
r2  owner refuted H-ZT from the published SEED-DEPENDENT-271350; three claims
    withdrawn; a denominator argument added
r3  owner corrected the denominator argument: the visit budget bounds how many
    positive classes a realizing seed may VISIT and asserts no unreachability,
    since REAL quantifies only over visited classes. One further claim and one
    arithmetic slip withdrawn; the argument replaced by a divisibility gate
```

Both r2 and r3 corrected the same kind of error: a static count carried further
than the quantifier it belongs to. Section 0 of the note lists every withdrawal
by name.

## What the archive now says

```text
1  the null quantifies over an exactly stateable narrow class, and must be
   archived with that class attached or it will be over-read
2  the frozen construction carries more than one obstruction
   A  zero-target sector, 44 of 312 classes                        OPEN
   B  seed dependence inside the positive sector                   ESTABLISHED
   C  a divisibility gate on the visit counts                      NOT RUN
3  only cause A is open, as Z-SUFFICIENT, and only for the U3 indicator alone
4  two positive results survive untouched: the channel is internal, and the
   information locus is exactly the selector-coupled functional q + r
```

Cause B gives `POS-REALIZED-SINGLE <= 38`, that is at least 862 of the 900 pairs
already fail inside the positive sector on window `W`. Its two derivations are
algebraically equivalent readings of one published count, not independent
evidence.

Cause C is a gate, not a result. `REAL` forces `q_c` to divide the visit count
of every visited positive class and oriented pre-cell, so a single seed with an
indivisible visit count would nullify all 900 pairs of that regime at once,
before the record map and the delay are chosen. Nothing here runs it.

## Contents

```text
README.md                                            this manifest
C-QDD-U-INDUCED-NULL-ANATOMY-1-N.md                  the archive, revision 3
PREREG-DRAFT-P-QDD-OBSTRUCTION-LOCUS-1_2026-08-16.md draft preregistration,
                                                     revision 3, blocks B1 to
                                                     B6; B1 has owner ANO,
                                                     B2 to B5 rebuilt from the
                                                     verdicts, B6 never ruled on
null_anatomy.py                                      static anatomy script,
                                                     8 gates, stdlib, exact
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
`null_anatomy.stdout.txt` (`SUMMARY 8/8 ALL PASS`).

Reproduction legs recorded while preparing this note, both exit 0 with empty
stderr and identical stdout:

```text
platform: Ubuntu 24.04 LTS   architecture: x86_64   python: 3.11.15
platform: macOS              architecture: arm64    python: 3.9.6
```

These are informal incubation legs recorded for auditability. They are not
formal run records and they do not satisfy the POLICY section 4
two-architecture computation gate, which is defined by the repository workflow
jobs and is not claimed here.

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
A7  from the published SEED-DEPENDENT-271350: 10350 of the 281700 triples are
    seed independent, so at most 38 pairs can satisfy REAL-POS-SINGLE and at
    least 862 already fail inside the positive sector; the complement form and
    the pigeonhole form are checked to agree, which is an arithmetic self-check
    and not corroboration by a second source
A8  the divisibility data a later probe needs: the 268 positive target
    denominators, smallest 6 and largest 256, all 268 at least 6 and 244 at
    least 8, summing to 19688; and the weak visit caps, at most 107 of 268
    positive classes on W and 245 on W2, at most 138 respectively 401 of the
    536 positive oriented pre-cells. A8 asserts no unreachability: the caps
    bound visits, and REAL quantifies only over visited classes
```

Gates A1 to A6 and A8 use only Canon v49 formulas and the two frozen window
lengths. Gate A7 additionally consumes one published integer of the sealed
probe. No orbit is iterated, no window is read and no seed is swept.

## Status

Nothing here is promoted. `QDD-INSTRUMENT-APPARATUS [O]` is unchanged and both
its blockers O1 and O2 remain at STOP. `QUADRATIC-DECODER-DATA [O]` is
untouched. No `DEF-QDD-*` definition is altered. The sealed probe is not
reopened, amended, renamed or resumed; the RESULT prose correction on the #396
branch is a separate commit touching only `RESULT.md`, with `PREREG.md`,
`verify.py`, `EXPECTED.txt` and `RUN.md` byte-identical.

The next steps belong to the owner, in this order: read revision 3 and rule on
B6, accept #396 so the result commit reaches `main`, and only then open a fresh
claim lock and a fresh probe branch. Nothing in this directory authorizes a
probe.
