# PREREG. P-TWOLOGPHI-INVARIANTS-1

Preregistration frozen before any gate execution. Public probe under
`POLICY.md` and `AGENTS.md`, which govern over this file wherever they
differ. Result-exposed, proof-first: the universal clauses are carried by
written proofs and the verifier is their exact finite audit.

The constant `2 log phi` is the program's most quoted number. Public Canon
v55 anchors it nowhere: the strings `Mahler`, `regulator` and `class number`
applied to `Q(zeta_5)` occur in `canon/CANON.md` zero, zero and zero times.
This probe supplies the arithmetic anchor.

## Falsifier, first

```text
J-MAHLER-MEASURE          an exact conjugate modulus of J off {phi, phi^-1};
                          a factorization of x^4 - 3x^3 + 4x^2 - 2x + 1 over
                          Z; a Mahler measure differing from phi^2; or an
                          exact refutation of trace 3 and norm 1 for phi^2.
REGULATOR-TWO-LOG-PHI     a unit of Z[phi] strictly between 1 and phi; a
                          real embedding of Q(zeta_5); an exact refutation
                          of phi^2 = phi + 1 or phi (phi - 1) = 1 in
                          Z[zeta_5]; or a regulator entry off 2 log phi.
CYCLOTOMIC-CLASS-NUMBER-  a trace-form discriminant differing from 125; an
ONE                       exact rational enclosure of pi violating
                          1125 < 16 pi^4; or an exact refutation of
                          5 < 16 for the real quadratic bound.
J-TORAL-PERIODIC-POINTS   a value of |N(J^n - 1)| on 1 <= n <= 40 differing
                          between the three exact routes; a Lucas closed
                          form failing at any n divisible by 5 in that
                          range; a second perfect square among the 32
                          off-residue values; or a bracket violation at any
                          n in that range.
```

Operationally: any pinned gate FAIL on rerun kills the probe. A fired
falsifier is merged and archived, never hidden, and the threshold never
moves afterwards.

## Public identity, authority, and action layer

```text
probe:           P-TWOLOGPHI-INVARIANTS-1
probe owner:     A. M. Thorn / delegated session twologphi-probe-2026-08-20
branch:          probe/P-TWOLOGPHI-INVARIANTS-1
basis:           Public Canon v55, main 362e9c3, tag canon-v55,
                 CONTENT_COMMIT 6236c10c, SHA256SUMS 5 of 5 OK,
                 verified by fresh fetch on 2026-08-20
action layer:    L1 for the three arithmetic rows, L2 for the periodic
                 point row. No lift between them, no gate consumed or
                 opened, no physical claim, no canon edit by this probe.
lineage:         carries in the mathematics of the incubation promotion
                 PROMO-C-TWOLOGPHI-INVARIANTS-4 (2026-08-20). This probe
                 re-derives everything from the definitions with new
                 files; the incubation verifier source was deliberately
                 not read, so the two code paths are independent. Two
                 deviations from that proposal are declared below.
```

## The six fields

```text
EQUATION     with j = zeta_5, J = 1 + j^2, Jbar = 1 + j^3,
             phi = -j^2 - j^3, M_J the matrix of multiplication by J on
             Z[zeta_5] = Z^4 in the basis 1, j, j^2, j^3, and T_J the
             induced automorphism of R^4/Z^4:
               I   M(J) = phi^2 exactly, so log M(J) = 2 log phi;
                   minpoly_Q(J) = x^4 - 3x^3 + 4x^2 - 2x + 1 = Phi_5(x - 1),
                   irreducible over Q; J . Jbar = 2 - phi = phi^-2 with
                   characteristic polynomial (x^2 - 3x + 1)^2; phi^2 has
                   minimal polynomial x^2 - 3x + 1, trace 3 = Tr(J),
                   norm 1 = N(J); phi < 2 < phi^2.
               II  Reg(Q(zeta_5)) = 2 log phi; r_1 = 0, r_2 = 2, unit
                   rank 1; phi is a unit of Z[zeta_5] and the fundamental
                   unit of Z[phi].
               III h(Q(zeta_5)) = 1 and h(Q(sqrt5)) = 1 by Minkowski;
                   disc = 125 and 1125 < 16 pi^4; 5 < 16.
               IV  for 5 | n: |N(J^n - 1)| = L_n^2 when n = 5 mod 10 and
                   (L_n - 2)^2 when n = 0 mod 10; exactly one of the 32
                   values with 5 does not divide n, 1 <= n <= 40, is a
                   perfect square, namely n = 1; and for every n >= 1
                   (phi^n - 1)^2 (1 - phi^-n)^2 <= |N(J^n - 1)|
                                                <= (phi^n + 1)^2 (1 + phi^-n)^2.
CODE         probes/P-TWOLOGPHI-INVARIANTS-1/verify.py, Python standard
             library only, exact integer and Fraction arithmetic and
             exact Z[phi] ordering, no float anywhere, deterministic, no
             randomness, no network, under 120 s, run from repository
             root with LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
             PYTHONHASHSEED=0 TZ=UTC.
CARRIER      Z[zeta_5] in the public basis 1, j, j^2, j^3 with the public
             multiplication-by-J matrix M_J of J-STEP [T]; the real
             quadratic order Z[phi]; the field discriminant 5^3 of
             QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T]; and the
             torus R^4/Z^4 of J-TORAL-ENTROPY [T] when Public Canon v56
             is live, see the conditional clause below.
SYSTEMATICS  the declared values of section IV, the first six values
             1, 11, 31, 55, 121, 341, the pin 1860496 at n = 15 and the
             single off-residue square at n = 1 were computed in the
             incubation lane and again in this session's exploration
             before this file was frozen; they are declared here in
             advance and bind the run. Nothing else was opened. The
             finite range 1 <= n <= 40 is declared, not chosen after
             looking; results outside it are outside scope. Three named
             classical imports are consumed and none is reproved:
             the unit index Q = 1 for prime cyclotomic fields, the
             Minkowski bound, and the maximality of Z[zeta_5] in
             Q(zeta_5). The regulator route does NOT use the analytic
             class number formula, so section III is independent of
             section II rather than an input to it. Disclosed: the
             candidate verifier was smoke-executed once before the pin,
             on a copy outside the repository, and revealed nothing not
             already declared above. Two gates, C5 and D4, were
             strengthened during authoring and before that smoke run,
             because each asserted less than its own description
             claimed; the pinned file is the strengthened one and the
             declared expected result never changed.
THRESHOLD    any gate FAIL kills the probe. Exact equality only, no
             tolerance, no float comparison anywhere.
LAYER        L1 for rows I, II, III; L2 for row IV. No lift between the
             arithmetic and the torus is asserted or performed. No gate
             is created. ENTROPY-LAYER-BRIDGE [O] is untouched.
```

## The written proofs

### I. Mahler measure

`M_J` is built column by column from the basis products `J . j^k`. Its
characteristic polynomial by exact Faddeev-LeVerrier is
`x^4 - 3x^3 + 4x^2 - 2x + 1`, which equals `Phi_5(x - 1)` by independent
integer polynomial expansion. That polynomial is irreducible over `Q`:
it is monic with constant term 1, so by Gauss's lemma any factorization is
into monic integer factors whose constant terms multiply to 1. A linear
factor forces a root in `{1, -1}`, and the values at `1` and `-1` are
`1` and `11`. A quadratic factorization `(x^2 + ax + b)(x^2 + cx + d)`
forces `b = d = 1` or `b = d = -1`; the coefficient equations then have no
integer solution. The enumeration is exhaustive over a derived range, not
a search.

Since the polynomial is irreducible, it is the minimal polynomial of `J`
and the characteristic polynomial of `M_J`, so the four archimedean
conjugates of `J` are exactly its roots. Complex conjugation is `j -> j^4`,
so `Jbar = 1 + j^3` and `|sigma(J)|^2 = sigma(J . Jbar)` for every
embedding, because `J . Jbar` is totally real. In `Z[zeta_5]`,
`J . Jbar = 2 + j^2 + j^3 = 2 - phi = phi^-2`, and the characteristic
polynomial of multiplication by it is `(x^2 - 3x + 1)^2`, whose roots are
`phi^2` and `phi^-2`. The four squared moduli are therefore
`phi^2, phi^2, phi^-2, phi^-2`; exactly two conjugates lie outside the
unit circle, both of modulus `phi`. The Mahler measure of a monic integer
polynomial is the product of the moduli of its roots outside the unit
circle, hence

```text
M(J) = phi . phi = phi^2,     log M(J) = 2 log phi.
```

`phi^2 = phi + 1` satisfies `x^2 - 3x + 1`, whose trace `3` equals `Tr(J)`
and whose norm `1` equals `N(J)`. Finally `phi < 2 < phi^2` exactly, since
`sqrt5 < 3` and `phi > 1`; consequently `1 < log_phi 2 < 2`.

### II. Regulator

`Phi_5` has no real root: `(x - 1) Phi_5(x) = x^5 - 1`, the only real
solution of `x^5 = 1` is `x = 1`, and `Phi_5(1) = 5`. Hence `Q(zeta_5)` is
totally complex, `r_1 = 0`, `r_2 = 2`, and the unit rank is
`r_1 + r_2 - 1 = 1`.

`phi = -j^2 - j^3` lies in `Z[zeta_5]`, is fixed by `j -> j^4` and is
therefore totally real. It satisfies `phi^2 = phi + 1` and
`phi (phi - 1) = 1` exactly in the ring, so it is a unit, and
`N_(Q(zeta_5)/Q)(phi) = 1`.

`phi` is the fundamental unit of `Z[phi]`. Let `u = a + b phi` be a unit
with `1 < u < phi`. Then `|u'| = 1/u` lies in `(1/phi, 1)`, so
`|u + u'| < phi + 1 = phi^2` and `|u - u'| < phi + 1`. Since
`u + u' = 2a + b` and `u - u' = b sqrt5`, this forces `|2a + b| <= 2` and
`|b| <= 1`, hence `a in {-1, 0, 1}`. The nine candidates are enumerated
exhaustively and none is a unit in `(1, phi)`. The verifier additionally
sweeps the wider box `|a| <= 4`, `|b| <= 4` and confirms that every unit
in it exceeding `1` is at least `phi`.

The free part of `Z[zeta_5]^*` is generated by `phi` modulo torsion. The
step from "fundamental unit of the real subfield" to "generator of the
free part of the full cyclotomic unit group" is the unit index `Q = 1`
for prime cyclotomic fields, together with `h^+ = 1`; both are named
classical imports and neither is proved here. With unit rank one and both
infinite places complex of local degree 2, the regulator is the `1 x 1`
determinant

```text
Reg(Q(zeta_5)) = |2 log |sigma_1(phi)|| = 2 log phi,
```

since `sigma_1(phi) = phi` and `|sigma_2(phi)| = phi^-1` give the same
value up to sign. The analytic class number formula is not used.

### III. Class number one

The trace form on the basis `1, j, j^2, j^3` has determinant `125`,
matching `disc(K_5) = 5^3` of the public census row; `Z[zeta_5]` is the
maximal order is the labeled import. The Minkowski bound for
`n = 4`, `r_2 = 2`, `|d_K| = 125` is

```text
M_K = (4/pi)^2 (4!/4^4) sqrt125 = (15 sqrt5)/(2 pi^2),
M_K < 2  <=>  15 sqrt5 < 4 pi^2  <=>  1125 < 16 pi^4.
```

`pi` is enclosed exactly by Machin's formula
`pi/4 = 4 arctan(1/5) - arctan(1/239)` with rational partial sums and the
alternating-series tail bound, giving rational `pi_lo < pi < pi_hi`. Then
`16 pi_lo^4 > 1125` as exact rationals, so `M_K < 2`, every ideal class
contains an ideal of norm `1`, and `h(Q(zeta_5)) = 1`.

For `Q(sqrt5)` the bound is `sqrt5/2 < 2`, equivalent to `5 < 16`, with no
transcendental input at all, so `h(Q(sqrt5)) = 1`. This is stated because
`SPLIT-PRIME-RAPIDITY-CLASS [T]` already consumes class number one for
that field; supplying its exact proof changes no existing row, adds no
edge to one, and is recorded here as an observation for a later fold.

### IV. Periodic points

For `5 | n`, `J^n = phi^-n` lies in the real quadratic subfield, so
`N_(Q(zeta_5)/Q)(J^n - 1) = N_(Q(sqrt5)/Q)(phi^-n - 1)^2`. With
`phi' = -phi^-1` one has `(phi')^-n = (-phi)^n`, so for odd `n` the inner
norm is `phi^n - phi^-n = L_n` and for even `n` it is
`2 - (phi^n + phi^-n) = 2 - L_n`. Taking absolute values and squaring:

```text
n = 5 mod 10   ->   |N(J^n - 1)| = L_n^2,
n = 0 mod 10   ->   |N(J^n - 1)| = (L_n - 2)^2.
```

The bracket is the triangle inequality applied to the two conjugate pairs.
The moduli of the four conjugates of `J` are `phi^-1, phi^-1, phi, phi`, so

```text
|N(J^n - 1)| = |sigma_1(J)^n - 1|^2 . |sigma_2(J)^n - 1|^2,
phi^n - 1 <= |sigma_2(J)^n - 1| <= phi^n + 1,
1 - phi^-n <= |sigma_1(J)^n - 1| <= 1 + phi^-n,
```

each factor non-negative for every `n >= 1` because `phi > 1`. Squaring
and multiplying gives the two-sided bracket for every `n >= 1`. This
clause is proved for all `n`; it is audited on the declared finite range.

The perfect-square census is a finite exhaustive statement on the declared
range and carries no general claim.

## Declared expected values, frozen before execution

```text
M_J                = [[1,0,-1,1],[0,1,-1,0],[1,0,0,0],[0,1,-1,1]]
det M_J            = 1,   trace M_J = 3
charpoly M_J       = x^4 - 3x^3 + 4x^2 - 2x + 1
charpoly M_(J.Jbar)= x^4 - 6x^3 + 11x^2 - 6x + 1 = (x^2 - 3x + 1)^2
J . Jbar           = 2 - phi = phi^-2
trace-form disc    = 125
|N(J^n - 1)|, n=1..6 = 1, 11, 31, 55, 121, 341
|N(J^15 - 1)|      = 1860496 = 1364^2 = L_15^2
off-residue squares on 1..40 = exactly one, at n = 1, value 1
units in (1, phi)  = none
RESULT             = 29/29 ALL PASS, exit 0, empty stderr
```

## Proposed fold edits (a later sealed fold, not this probe)

Four registry rows. Verbatim tab-separated text in `FOLD-ROWS.tsv` beside
this file. Frontier: no change; all four are closed statuses. Ledger
delta: claims +4, T +3, C +1.

```text
J-MAHLER-MEASURE           T  1. The axiom and the two projections  L1
REGULATOR-TWO-LOG-PHI      T  4. The two places                     L1
CYCLOTOMIC-CLASS-NUMBER-ONE T 4. The two places                     L1
J-TORAL-PERIODIC-POINTS    C  2. Time, space, and the decoder       L2
```

Dependency edges:

```text
J-MAHLER-MEASURE            -> J-STEP                    REQUIRES
J-MAHLER-MEASURE            -> ENTROPY-LAYER-BRIDGE      BOUNDED_BY
REGULATOR-TWO-LOG-PHI       -> J-PROJECTIONS             REQUIRES
REGULATOR-TWO-LOG-PHI       -> ENTROPY-LAYER-BRIDGE      BOUNDED_BY
CYCLOTOMIC-CLASS-NUMBER-ONE -> QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS
                                                         REQUIRES
J-TORAL-PERIODIC-POINTS     -> ENTROPY-LAYER-BRIDGE      BOUNDED_BY
J-TORAL-PERIODIC-POINTS     -> (see the conditional clause)
```

Each `BOUNDED_BY` edge to `ENTROPY-LAYER-BRIDGE [O]` is the fence, made a
ledger fact rather than prose: these rows and the toral entropy row carry
the same constant, and that is a fact about the number, not a bridge
between the layers.

### The conditional clause on row IV

Public Canon v56 is prepared and carries `J-TORAL-ENTROPY [T]`, which
registers `#Fix(T_J^n) = |det(M_J^n - I)| = |N(J^n - 1)|` and the witness
`#Fix(T_J^15) = 1860496`. Row IV must not restate it. The fold therefore
has two branches and the fold, not this probe, chooses by reading
`STATUS.md` at that time:

```text
branch A, v56 live (expected)   row IV carries only the Lucas closed
                                forms, the off-residue census and the
                                bracket, and REQUIRES J-TORAL-ENTROPY.
branch B, v56 not landed        row IV additionally carries the identity
                                and the n = 15 pin, and REQUIRES J-STEP.
```

Both row texts are supplied verbatim in `FOLD-ROWS.tsv`. The mathematics
of this probe is identical under both branches; only the row scoping
differs. If the fold cannot determine which branch applies, it stops.

## Deviations from PROMO-C-TWOLOGPHI-INVARIANTS-4, declared

```text
1  The class number clause is split out as its own row
   CYCLOTOMIC-CLASS-NUMBER-ONE [T]. It has its own falsifier and its own
   proof, and my regulator route does not consume it, so bundling it into
   the regulator row would misstate the dependency.
2  The bracket is claimed for every n >= 1, not for n >= 6. The triangle
   inequality proves it for every n >= 1 and the audit confirms it on
   1 <= n <= 40 including n = 1..5.
3  The proposal's cotangent identity route to the regulator is not used.
   The route here is the unit group directly.
4  Row I is narrower than the proposal's. The conjugate moduli
   (phi^-1, phi, phi, phi^-1) are already public in J-UNIT [T], and at
   v56 the characteristic polynomial is public too, so the row claims the
   Mahler measure, the irreducibility and the phi^2 coincidence, and does
   not restate what is already registered.
```

## Non-claims

```text
No entropy, rate, measure, physical or dynamical statement is made
anywhere. The word entropy occurs only in the name of a registered row
and of the open obligation.

That four independent invariants carry the constant 2 log phi is a fact
about the number phi, not evidence that any rate of the decoder or of the
plenum equals it. That step is exactly ENTROPY-LAYER-BRIDGE [O] and it
stays open, at its exact scope, in both branches.

No claim is made that phi or 2 log phi is derived from J in any sense
beyond the stated arithmetic. No lift from L1 to L2 is performed: rows I
to III are arithmetic about J and its field, row IV is about the torus,
and the fact that they meet at one constant is not a bridge.

The three named imports are not reproved and no result here strengthens
them. RH, the Li ladder and every carrier row are untouched.
```
