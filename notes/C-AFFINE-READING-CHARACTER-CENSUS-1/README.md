# notes/C-AFFINE-READING-CHARACTER-CENSUS-1

NON-CANONICAL. Incubation candidate, no authority, no Canon change, no `canon/`
file touched. Durable git handoff of a candidate developed 2026-08-23 against
Public Canon v60 (tag `canon-v60`, content commit
`18b21bdaf2c2236c9444b120900277ccfb63e050`), with public `main` at
`f9b7438747e612eeebf63cb3ac95283fcb2a7085` at the moment of the freeze.

It closes the linear reading question in every linear character sector of
`G = AGL_1(F_5)`, not only the invariant one, computes the character graded
census of `Sym^d V` through degree five with the Molien series through degree
twelve, exhibits the unique cubic invariant with an exact closed form, and
records the counterweight that refutes the informal reading of the result.

## Contents

```text
C-AFFINE-READING-CHARACTER-CENSUS-1.md            candidate claim and scope doc
README.md                                          this manifest
PREREG-C-AFFINE-READING-CHARACTER-CENSUS-1.md      frozen prereg, before the run
verify_C-AFFINE-READING-CHARACTER-CENSUS-1.py      pinned verifier, gates G1 to G9
EXPECTED.txt                                       committed stdout of the verifier
RESULT-C-AFFINE-READING-CHARACTER-CENSUS-1.md      recorded run, outcome, fired self-check
BREAK-C-AFFINE-READING-CHARACTER-CENSUS-1.py       independent third code path
BREAK.stdout.txt                                   committed stdout of the break attempt
PROMO-C-AFFINE-READING-CHARACTER-CENSUS-1.md       promotion proposal for a public fold
SHA256SUMS                                         hashes of the files above
```

File names are the names carried in the frozen preregistration and are not
renamed to house style, because the frozen documents reference each other by
name.

## Reproduction

From this directory:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 verify_C-AFFINE-READING-CHARACTER-CENSUS-1.py
```

Expected: exit 0, empty stderr, stdout byte identical to `EXPECTED.txt`,
decision line `READING-CENSUS-CERTIFIED`. Recorded leg: Ubuntu 24.04, x86_64,
Python 3.12.3, 1473 ms as an engineering readout. One architecture only. These
are incubation pins, not a public probe, and the POLICY section 4 two
architecture gate is not claimed.

The break attempt is relocatable and resolves its own directory:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 BREAK-C-AFFINE-READING-CHARACTER-CENSUS-1.py
```

Expected: exit 0, empty stderr, stdout byte identical to `BREAK.stdout.txt`. It
reads the frozen numbers back from `EXPECTED.txt` rather than recomputing them,
so its agreement lines compare a third route against the recorded result.

## Frozen pins, recorded before the recorded run

```text
473f64da93c9b6c488ffe266bb33c1b9c54705c8debc85166757b80aa192ba40
  PREREG-C-AFFINE-READING-CHARACTER-CENSUS-1.md (11599 bytes, 264 lines)
829f91d1269f4802c2dfb0e0afba1b9bd78e0830bb665547719f5371bc2ff430
  verify_C-AFFINE-READING-CHARACTER-CENSUS-1.py (13274 bytes)
4a3813fa115f875d6f8da44c6d26c8a3c161cef9a273221b7f66539e6fab35f5
  EXPECTED.txt (1101 bytes)
```

The preregistration was frozen and hashed before the verifier was written, and
the verifier was written before any gate value was opened.

## Status

candidate-T at L1, decision `READING-CENSUS-CERTIFIED`, gates G1 to G8 pass and
G9 is recorded as `SEPARATING-AT-5` with zero collisions.

The central negative is that `m_lambda(1) = 0` in all four linear character
sectors, so no nonzero linear reading of the carrier exists, invariant or phase
weighted. The central positive is the refutation that comes with it: the
smallest odd invariant degree is three, the unique cubic invariant satisfies
`3K = p_1^3 + 6 p_1 q_+ - 25 p_3`, and the degree five fingerprint separates
orbits, so the state is recoverable up to the twenty element orbit. What is
unreadable is the state linearly, not the state.

The frozen verifier carries one recorded defect in basis extraction which
degrades power and not soundness; it is characterized exactly in the result
record and its fix is a precondition of public pinning. Promotion is deferred
to a public probe under POLICY.md; nothing here promotes anything.
