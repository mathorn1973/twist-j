# PREREG: C-SCALE-MINIMAL-FIELD-1

```text
ID:          C-SCALE-MINIMAL-FIELD-1
STATUS:      INTERNAL, NON-CANONICAL. Candidate. No authority. Promotes
             nothing by existing.
TARGET LINE: public, mathorn1973/twist-j, as a THIRD entry beside the two
             existing "why five" answers in canon/CORE.md, section
             "Why five, twice", if and only if it survives validation.
BASIS:       Public Canon v58, gate run this session (see
             PREREG-AUDIT-BELL-SHARPNESS-CLOSURE-1.md for the gate
             transcript fields).
LAYER:       L1 state. Pure arithmetic. No decoder, no measure, no
             physical selection, no lift to L2-L6 is claimed or attempted.
ORIGIN:      the Boolean meta-layer question: does "anchor + distinction +
             join + closure" select p = 5. The Boolean half of that
             question is answered NEGATIVELY here and that negative is
             part of the preregistration, not a discovered escape.
```

## The claim, stated so it can be killed

```text
S0  [candidate-F, preregistered as a NEGATIVE]
    {1, XOR, AND} is functionally complete on {0,1}^n (Zhegalkin/ANF), and
    a + b = (a XOR b) + 2(a AND b) generates integer addition. Therefore
    the Boolean layer represents EVERY finite structure and selects NO
    prime, no field and no J. Boolean completeness has zero selection
    power. This is asserted as a defeat, in advance.

S1  [candidate-T]  Among ALL number fields K with a unit of infinite order
    (equivalently unit rank r_1 + r_2 - 1 >= 1), Q(sqrt5) is the unique
    minimizer of |disc K|, with minimum 5.

S2  [candidate-T]  Among ALL cyclotomic fields Q(zeta_n), n >= 1, with a
    unit of infinite order, Q(zeta_5) is the unique minimizer of
    |disc|, with minimum 125.

S3  [candidate-C]  Exhaustive finite witness for S1 and S2: all quadratic
    fields with |disc| <= 200, all n <= 200 for the cyclotomic family,
    with the tail closed by an exact rational Minkowski bound rather than
    by sampling.

S4  [candidate-O, stated as the surviving gap]
    S1 and S2 select the FIELD. They do not select the ELEMENT
    J = 1 + zeta_5^2 inside it. 1 + zeta_5 and 1 + zeta_5^2 are both
    units, of moduli phi and phi^-1; nothing here chooses between them.
    The remaining step is open and is named, not hidden.
```

## The six fields

**1. Equation.** Exact integer arithmetic only.

```text
E1  quadratic: d squarefree, |d| > 1; disc = d if d = 1 mod 4 else 4d;
    unit rank = 1 for d > 0, 0 for d < 0. Minimize |disc| over rank >= 1.
E2  cyclotomic: for n > 2 the field Q(zeta_n) is totally complex,
    r_1 = 0, r_2 = phi(n)/2, rank = phi(n)/2 - 1; rank >= 1 iff
    phi(n) >= 4. disc by the exact integer conductor-discriminant form
    disc(Q(zeta_n)) = (-1)^(phi(n)/2) n^phi(n) / prod_(p | n) p^(phi(n)/(p-1)).
E3  degree tail: the Minkowski lower bound
    sqrt|disc| >= (m^m / m!) (pi/4)^(r_2), r_2 <= m/2, evaluated with a
    rational under-approximation of pi (pi > 314159/100000), gives an
    exact integer lower bound on |disc| by degree m.
```

**2. Code.** `verify_scale_minimal_field_1.py` and an independent
`breaker_scale_minimal_field_1.py`. Python standard library only, integers
and Fractions only, no float in any assertion, no sympy, no table lookup
of discriminants: every discriminant is computed from the formula and
cross-checked by an independent route in the breaker.

**3. Carrier.** Quadratic: all squarefree d with |d| <= 200. Cyclotomic:
all n <= 200. Degrees m = 3..40 for the Minkowski tail. Independent
cross-check in the breaker: disc(Q(zeta_p)) = (-1)^((p-1)/2) p^(p-2) for
odd primes p, and the ring-of-integers discriminant computed as the
determinant of the trace form on the power basis for n <= 24.

**4. Systematics.** Single platform this session, one leg, so every
computation-grade row stays at most candidate-C. The candidate-T labels
rest on the finite case analysis plus the Minkowski tail, not on the
sweep. Two byte-identical runs, empty stderr. Failure mode explicitly
watched: a wrong sign convention on disc, a missed n = 2 mod 4 duplicate
(Q(zeta_2m) = Q(zeta_m) for odd m), and the r_1/r_2 signature of the
real quadratic case.

**5. Failure threshold.**

```text
S1 FIRES if any number field with |disc| < 5 has unit rank >= 1, or if
   any field other than Q(sqrt5) attains |disc| = 5 with rank >= 1, or if
   the Minkowski tail fails to exclude every degree m >= 3 at |disc| <= 5.
S2 FIRES if any n with phi(n) >= 4 gives |disc(Q(zeta_n))| < 125, or if
   a second n gives exactly 125 with a field different from Q(zeta_5).
   (n in {5,10} give the SAME field and are not a falsifier; the claim is
   about the field, per the correction already recorded in
   claude/AUDIT-LI2-PENTAGON-BALANCE_2026-08-01.md.)
S3 FIRES on any disagreement between the formula route and the trace-form
   route on the common range.
S0 is already a negative and cannot fire; it can only be shown to be too
   weak, which would be a finding against this preregistration.
```

**6. Action layer.** L1. On survival the output is
`PROMO-C-SCALE-MINIMAL-FIELD-1`, proposing one new [T] row in the
"Why five" class of canon/CORE.md, with S4 attached to it as the explicit
non-selection caveat, in the same style the two existing answers already
carry. No promotion happens in this project.

## Explicit falsifier, one line

```text
Exhibit a number field of absolute discriminant less than 5 that contains
a unit of infinite order, or a cyclotomic field other than Q(zeta_5) of
absolute discriminant at most 125 that contains one.
```

Frozen before first execution. No computation has been run on S0-S4 at the
time of this freeze.
