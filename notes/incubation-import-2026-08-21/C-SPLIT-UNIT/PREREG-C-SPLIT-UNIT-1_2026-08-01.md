# PREREG C-SPLIT-UNIT-1

NON-CANONICAL. Incubation-lane candidate in the TWIST-J claude.ai project.
No authority. No Canon change. Promotion, if ever, is a separate public fold.

```text
CANDIDATE   C-SPLIT-UNIT-1
DATE        2026-08-01
OWNER       one named session (Claude cloud seat, this session), sole owner
TARGET      public line mathorn1973/twist-j on promotion
BASIS       Public Canon v30, STATE ACTIVE, AUTHORITY mathorn1973/twist-j main
            TAG canon-v30, CONTENT_COMMIT 857223fcd5e7bc8c8e68f1df768d6e8222b24ee0
            CANON_SHA256 2a32dcbd61ee7792fc2cb990b7f223e08876d71bf7ddcf5ec432acd055f3986a
            CANON_BYTES 157167, SHA256SUMS 5 of 5 OK, tag and content commit
            verified ancestors of main in a fresh clone this session
```

## Motivating owner statement (recorded, not graded here)

The owner's sentence: the whole is multiplicatively 1, additively 0, and
internally carries a nontrivial binary distinction. This prereg freezes the
exact algebraic subclaims that either hold or fire. The ontological reading
stays [D] and the completeness claim stays [H]; neither is graded by this run.

## Falsification first

Any FAIL line in either pinned script fires the named falsifier. Fired
falsifiers are first-class results: archived, never deleted, thresholds never
moved. Named falsifiers:

```text
F1 SIZE-LINE      some unit of Z[zeta_5] with coefficients in [-4,4]^4 whose
                  size datum u*conj(u) is not an exact even power of phi, or
                  whose sigma_2 sigma_3 product is not the inverse power
                  (breaks: every unit lies on the chi_5 size line, quantized)
F2 ORBIT          a torsion element w of Z[zeta_5] with 1 + w a unit and
                  1 + w outside the Galois orbit of J, or one of the four
                  orbit members failing unit-ness
                  (breaks: J is the unique unit of shape 1 + pure phase)
F3 BIT-UNIQUE     a second subgroup of index 2 in (Z/5Z)^x, or a second real
                  nontrivial character, or the quadratic-residue set differing
                  from {+-1} at p = 5
                  (breaks: the bit is unique and triply realized)
F4 ARG-SECTOR     a nonzero trivial or chi_5 component of the principal
                  argument vector of the sigma_a(J), in exact rational
                  multiples of pi
                  (breaks: modulus and argument live in disjoint sectors)
F5 GAUSS          Gauss sum of chi_5 differing from 2 phi - 1, or its square
                  differing from 5, or the twist identity failing
F6 CHARPOLY       characteristic polynomial of multiplication by
                  (2 + zeta^2 + zeta^3) differing from (x^2 - 3x + 1)^2
                  (independent second path for the moduli)
F7 AXIOM-ANCHOR   any of N(J) = 1, Tr(J) = 3, J phi = j, (J-1)^3 = j,
                  J^5 = phi^-5 failing symbolically
```

## Gate design rule compliance (per WORKING-AGREEMENT 2026-07-31, section 2)

Every gate family names an input that would make it FAIL, and where practical
the scripts construct that input and show the discriminating computation:

```text
size line      constructed non-unit 1 - zeta: its size datum 3 - phi is shown
               NOT to be a power of phi (gate H3); a unit-only property
orbit          all ten torsion elements are enumerated; the six failures
               (norms 5, 16, 0) are asserted as failures, not skipped
bit unique     the wrong partition {1,2} vs {3,4} is constructed and shown
               non-multiplicative; subsets {1,2}, {1,3}, {1,2,3} shown not
               closed; all 16 sign maps enumerated
arg sector     a branch error at a = 2 (r_2 = +2/5 instead of -1/5) would
               break gates G3, G4, G5 simultaneously
charpoly       a wrong modulus pattern (phi, phi, phi, phi^-1) would change
               the charpoly away from (x^2 - 3x + 1)^2
```

## The six fields

### 1. Equation

Notation: zeta = zeta_5, G = (Z/5Z)^x = {1,2,3,4}, sigma_a(zeta) = zeta^a,
J = 1 + zeta^2, phi = -zeta^2 - zeta^3, R = ln phi, chi_5 the quadratic
character mod 5 (+1 on {1,4}, -1 on {2,3}), chi an order-4 character fixed by
chi(2) = i. All assertions are identities in Z[zeta_5], Z[phi], Q, or Q(i);
arguments are exact rational multiples of pi under the principal branch.

```text
E1 SIZE      sigma_a(J) sigma_(5-a)(J) = phi^(-2 chi_5(a)) in Z[phi] for all a;
             equivalently log|sigma_a(J)| = -R chi_5(a); N(J) = 1, Tr(J) = 3.
E2 GAUSS     sum_a chi_5(a) zeta^a = 2 phi - 1, and (2 phi - 1)^2 = 5;
             twist: sum_a chi_5(a) zeta^(ab) = chi_5(b) (2 phi - 1) for all b.
E3 ORBIT     { w in mu_10 : 1 + w is a unit } = { zeta, zeta^2, zeta^3,
             zeta^4 }, one Galois orbit, the orbit of J. With Kronecker's
             theorem (classical): up to Galois relabeling J is the unique
             unit of Z[zeta_5] of the form 1 + (element of modulus 1 at every
             archimedean place).
E4 BIT       G has exactly one subgroup of index 2, {1,4} = squares = {+-1};
             exactly one real nontrivial character, chi_5; the dual splits as
             {trivial, chi_5, one conjugate doublet}; among scanned primes
             {3,5,7,13} the doublet count is (p-3)/2 and equals 1 only at
             p = 5.
E5 ARG       principal arguments arg sigma_a(J) = pi r_a with
             r = (2, -1, 1, -2)/5; sum_a r_a = 0; sum_a chi_5(a) r_a = 0;
             r_a = -r_(5-a); 5 r_a = Re[(2 + i) chi(a)];
             ratio identity sigma_a(J) = zeta^(2a) sigma_(5-a)(J).
E6 LATTICE   every unit u with coefficients in [-4,4]^4 satisfies
             u conj(u) = phi^(2m) exactly for some integer m, with
             sigma_2(u) sigma_3(u) = phi^(-2m); finite-range witness of the
             classical structure U(Z[zeta_5]) = <-zeta> x <phi> (Kummer;
             Washington, Introduction to Cyclotomic Fields, Thm 4.12 and
             Cor 4.13), which gives the size lattice Z R chi_5 with J at
             quantum m = -1, minimal |m| = 1.
E7 ZERO      witnesses of the one-theorem skeleton (the trivial isotypic
             component of a nontrivial-sector object is zero):
             sum_a chi_5(a) = 0; a Fraction projector pair with [P,Q] != 0
             and Tr[P,Q] = 0; conjugation projectors e+- = (1 +- c)/2
             idempotent, orthogonal, summing to 1, with (e+ - e-)^2 = 1.
E8 ANCHORS   N(J) = 1, Tr(J) = 3, J phi = zeta, (J - 1)^3 = zeta,
             J^5 = phi^-5, ring sanity Phi_5(zeta) = 0.
```

### 2. Code

```text
verify_split_unit_1.py   the accepted exact verifier (gates A,B,C,D,E,F,G,H,I)
break_split_unit_1.py    the independent break attempt: second code paths
                         (Faddeev-LeVerrier charpoly, Sylvester resultants,
                         brute-force sign-map enumeration, direct unit
                         membership in {+-zeta^k phi^m}) plus constructed
                         counterexample attempts
```

Python standard library only, exact int and Fraction arithmetic, no float
anywhere in either file, runtime far under 120 s, deterministic stdout, exit 0
iff zero FAIL lines. Environment for every formal run:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

Both file SHA-256 are recorded below before first execution. Compilation
(py_compile) is the only pre-freeze execution, per POLICY.

### 3. Carrier or data

None. Pure algebra in Z[zeta_5] and Q(i). No external data, no Canon file is
read at run time, no measured quantity enters.

### 4. Systematics

```text
basis choice        (1, zeta, zeta^2, zeta^3), zeta^4 = -(1+zeta+zeta^2+zeta^3)
branch convention   principal argument in (-pi, pi], encoded as exact rational
                    multiples of pi via arg(1 + e^(i theta)) = theta/2 for
                    theta in (-pi, pi); no transcendental evaluation occurs
character choice    chi(2) = i fixes one of the two order-4 characters; the
                    other gives the conjugate identity (2 - i)
scan bounds         verifier coefficient box [-4,4]^4; breaker membership box
                    [-2,2]^4 with exponent window |m| <= 30; power window
                    for size lookup |exponent| <= 60. Bounds declared here,
                    never widened after a miss.
platforms           planned: local cloud sandbox x86_64 and the internal
                    aarch64 relay runner, byte-identical stdout required for
                    the computation-grade label; if only one platform runs,
                    every computational outcome is capped at candidate-C
classical imports   Kronecker's theorem; Dirichlet unit theorem; Kummer /
                    Washington Thm 4.12, Cor 4.13 (U = W x U+ for prime-power
                    cyclotomic fields); Dirichlet class number formula
                    L(1, chi_5) = 2 ln phi / sqrt 5. These are cited, not
                    re-proved; gates E6/H witness consequences at finite range.
adjacent canon      J-UNIT [T], J-PROJECTIONS [T], ALPHA-PREFACTOR-UNIFICATION
                    [T] (tau = 2 phi - 1 = sqrt 5 already registered),
                    Z2-PLACES-SPLIT [T], CARRY-PENTAD [T], A0 non-uniqueness
                    disclaimer, FIRED-COMMUTATOR-NOGO [T],
                    CURVATURE-OPERATOR-CANONICAL [O], MINIMAL-READ-DERIVATION
                    [O]. This candidate must not exceed any of their scopes.
```

### 5. Failure threshold

Any assertion failure (FAIL line, nonzero exit) in either pinned script fires
the corresponding falsifier F1..F7 and is recorded first-class in the RESULT.
No threshold, bound, or convention moves after this freeze.

### 6. Action layer

L1 state algebra only. No layer lift is claimed or used. The [D] ontological
reading (bit as resolution of identity, time as count, space as
noncommutativity) and the [H] completeness claim (split, bit, update, decoder
forced by J) are explicitly outside the scope of these runs and gain no grade
from them. Their falsifier is recorded in the candidate doc, not here.

## Freeze

SHA-256 of this file and both scripts are recorded in the run record
immediately below this freeze, before first execution.
