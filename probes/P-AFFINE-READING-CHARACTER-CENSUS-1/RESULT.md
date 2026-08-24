# P-AFFINE-READING-CHARACTER-CENSUS-1 result

Decision: **READING-CENSUS-CERTIFIED**. Fourteen of fourteen frozen gates
passed on the first formal run. Layer **L1 only**.

This probe changes no Canon, Registry or Frontier row. It seals a mathematical
result and its evidence. Any promotion is a later and separate sealed fold.

## What was established

**The linear void is complete.** `m_lambda(1) = 0` for every one of the four
linear characters of `G = AGL_1(F_5)`, by two independent methods. No nonzero
linear reading of the carrier exists, invariant or phase weighted. The public
row `AFFINE-READING-DEGREE-CENSUS` had established this in the invariant sector
alone; a covariant reading with a phase weight is now closed off as well.

**The quadratic degree carries exactly two lines.** The invariant `q_+` and the
epsilon graded `q_-`, and nothing in either order four sector. Both
transformation laws were verified on all twenty group elements.

**The graded census.**

```text
d   dim   1   eps   i   ibar   V
0     1   1     0   0      0   0
1     4   0     0   0      0   1
2    10   1     1   0      0   2
3    20   1     1   1      1   4
4    35   3     2   1      1   7
5    56   3     3   3      3  11
```

Degree three reproduces the regular representation of `G` exactly:
multiplicities `(1,1,1,1,4)` and dimension `20 = |G|`.

Molien coefficients through degree twelve.

```text
invariant sector   1 0 1 1 3 3 5 6 10 11 16 18 25
epsilon sector     0 0 1 1 2 3 5 6  9 11 16 18 24
each order four    0 0 0 1 1 3 3 6  7 11 13 18 21
```

**The invariant ring is not concentrated in even degrees.** No element of `G`
acts as `-I` and `chi_V` takes values in `{-1, 0, 4}`, so `x` and `-x` lie in
different orbits for generic `x`; over characteristic zero the invariant ring
separates orbits, so an odd invariant must exist. The smallest odd invariant
degree is exactly three. The degree three invariant space is one dimensional
and is spanned by

```text
K = (p_1^3 + 6 p_1 q_+ - 25 p_3)/3,
```

with `p_1` the coordinate sum and `p_3` the sum of cubes. `K` has integer
coefficients, exactly twenty monomials, coefficient set exactly `{-4, 3}`, and
is fixed coefficientwise by all twenty group elements. Being an odd form, it
reads the sign of the state.

**Readings recover the state up to the orbit, and degree five is minimal.** On
the exhaustive test set of 624 vectors the cumulative invariant fingerprint
gives

```text
d          0     1     2     3    4    5
invariants 1     1     2     3    6    9
classes    1     1    18    45   84   86
collisions 619 619   474   264    8    0
```

and the exact number of `G` orbits on that set, computed independently by
canonical orbit representatives rather than from any fingerprint, is also 86.
Degree five separates, degree four does not, so five is the minimal separating
degree here.

## What this refutes

The informal reading that only even or contractive quantities are observable is
**false at L1**. An odd invariant exists at degree three and the invariants
separate orbits. The correct statement is narrower and sharper: the state is
unreadable **linearly**, not unreadable. The central negative and this
counterweight travel together and neither may be quoted without the other.

## Provenance and the corrected defect

The mathematics was developed as incubation candidate
`C-AFFINE-READING-CHARACTER-CENSUS-1`, published on branch
`notes/C-AFFINE-READING-CHARACTER-CENSUS-1`, which changes no `canon/` file.
That candidate recorded a fired self-check: its verifier extracted an invariant
basis from the pivots of the transposed projector, so at degree three the
extracted representative was the zero polynomial and at degree five only one of
three was independent. Soundness was unaffected there, but power was.

The verifier pinned here extracts from the projector itself and adds **G12**,
which requires at every degree that the extracted family have rank exactly the
computed multiplicity, contain no zero polynomial, and be fixed by the
projector. G12 passed. The corrected extraction is also what makes **G14**
meaningful, since the minimal separating degree cannot be gated from a
degenerate family.

Two further corrections were carried in from the candidate audit. Every gate
now prints from its own boolean rather than from an aggregate, so a failure
names itself. No gate is a constant that is true by inspection.

## Scope firewall

L1 only. No measurement, apparatus, instrument, observer, decoder, Born rule,
probability, effect, record, photon, light, matter, energy density, radiation
density, cosmology, expansion, contraction, dark sector, hidden fraction, SI
value, or L2 to L6 lift is assumed or concluded. This probe does **not**
establish that any physical apparatus is unable to record a linear datum.

That passage remains an open obligation, named in `PREREG.md` as
`O-LINEAR-READING-APPARATUS-LIFT`, with the falsifier: exhibit one registered
L4 or L5 readout whose emitted record is a nonzero linear function of the L1
carrier state. Proposing that row is the business of a later fold, not of this
probe.

## Status of this record

The mathematical statement is theorem grade at L1 within the pinned scope, and
the computation is reproduced byte identically across architectures by the
required pull-request check. The registry row proposed in
`notes/C-AFFINE-READING-CHARACTER-CENSUS-1/PROMO-C-AFFINE-READING-CHARACTER-CENSUS-1.md`
is not created by this probe. No summary of this probe may exceed L1 or claim a
status this directory has not earned.

## Basis movement during the probe, recorded

Public `main` advanced from `f9b7438747e612eeebf63cb3ac95283fcb2a7085` to the
Public Canon v61 fold while this probe was open. The pin parent, and therefore
every basis field frozen in `PREREG.md`, names v60. `PREREG.md` is pinned and
is not edited; this section records the movement instead.

The movement was checked for substance before this probe was merged, not waved
through:

```text
AFFINE-READING-DEGREE-CENSUS       still present, still T, row not modified
AFFINE-QUADRATIC-FORM-UNIQUENESS   still present, still T, row not modified
rows added by v61                  J-BINARY-NORM-INDEX, J-BINARY-NORM-ORDER-CENSUS,
                                   RECORD-QUOTIENT-CALCULUS, J-ODD-MOTOR-MEDIATED-BRIDGE
collision with this probe          none
```

Both rows this probe depends on are unchanged in text and status, and none of
the four rows folded at v61 covers a graded or character graded reading census.
The carrier itself is fixed by the axiom and does not move with a Canon
version, so no gate value depends on the fold.

The consequence is confined to provenance: the frozen basis fields in
`PREREG.md` describe v60 and are correct as of the pin, and a reader at v61 or
later should read them as the state at the pin rather than as a current
statement. Any later fold that proposes a registry row from this probe must
perform its own currency gate against the head of the day.
