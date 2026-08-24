# P-ENTROPY-RESIDUE-MATH-1 preregistration

Status: `PREREGISTERED / RESULT-EXPOSED / PROOF-FIRST`

Three carrier-independent entropy rows: the toral entropy of the step,
the zero entropy of the driver, and the exact residue bracket between
them. The universal statements are carried by the written proofs below
with imports labeled; the verifier audits every exact algebraic identity
and the finite counts. The result is exposed before execution: every gate
passes. This probe closes a documented gap: the entropy rate 2 log phi,
the program's most physical arithmetic quantity, currently appears
nowhere in the public canon.

## Public identity, authority, and action layer

```text
probe:           P-ENTROPY-RESIDUE-MATH-1
public claim:    issue #451
probe owner:     A. M. Thorn / delegated session cleanup-batch-2026-08-20
branch:          probe/P-ENTROPY-RESIDUE-MATH-1
basis:           Public Canon v54, main 70e1c480, tag canon-v54,
                 SHA256SUMS 5 of 5 OK
action layer:    L1 and L2 (arithmetic and the toral manifold); the
                 driver row is L5 (stream). No lift to L6 and no
                 physical-measure claim: ENTROPY-LAYER-BRIDGE [O] is
                 untouched, and "the cosmogenesis produces 2 log phi per
                 tick" remains exactly as open as that row says.
lineage:         carries in the mathematics of the incubation candidate
                 C-ENTROPY-RESIDUE-1 rev 2 (2026-07-14), restricted to
                 its carrier-independent rows; the lane's fired clauses
                 (F-BRIDGE-PINSKER-SOURCE, TM-BIT-INFORMATION-CONFLATION)
                 are archived lane history and none of their content is
                 asserted here. The bridge and canonicity rows of that
                 candidate (ENTROPY-LAYER-BRIDGE edits,
                 CANONICAL-BINARY-READ [H]) are explicitly NOT carried.
```

## Falsifier, first

For J-TORAL-ENTROPY: an exact eigenvalue-modulus computation off the pair
{phi, 1/phi}, or a fixed-point count differing from |N(J^n - 1)| at any
n. For TM-ENTROPY-ZERO: a factor count contradicting the pinned table or
superlinear growth exhibited at any window length. For
BINARY-READ-RELATIVE-ENTROPY: an exact refutation of the bracket algebra
(phi^2 - 2 = 1/phi > 0, the split identity, the norm gates).
Operationally: any pinned gate FAIL on rerun.

## The six fields

```text
EQUATION     (1) h_top(T_J) = h_Haar(T_J) = 2 log phi for the toral
             automorphism induced on R^4/Z^4 by the step matrix of
             J = 1 + zeta_5^2, with #Fix(T_J^n) = |det(M^n - I)|
             = |N(J^n - 1)| and the pinned witness
             #Fix(T_J^15) = 1860496.
             (2) the Thue-Morse driver theta_n = s_2(n) mod 2 has linear
             factor complexity, hence entropy rate 0; exact counts
             p(1..4) = 2, 4, 6, 10 and p(20) = 60.
             (3) for any binary factor q of a system at rate 2 log phi:
             R(q) = 2 log phi - h(q) lies in [log(phi^2/2), 2 log phi],
             the floor is strictly positive (phi^2 - 2 = 1/phi > 0), the
             split identity 2 log phi = log 2 + log(phi^2/2) is exact,
             the deterministic driver attains the ceiling, and 2 log phi
             is the log of no rational and is Q-linearly independent of
             log 2 and log 5 (norm gates on {phi^2, 2, 5}).
CODE         probes/P-ENTROPY-RESIDUE-MATH-1/verify.py, stdlib only,
             exact Fraction, Z[phi] and Z[zeta_5] arithmetic, no float
             anywhere, deterministic, well under 120 s, run from the
             repository root with LC_ALL=C LANG=C
             PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
CARRIER      none external. The step matrix is the anchored step
             (a,b,c,d) -> (a-c+d, b-c, a, b-c+d); the driver is the
             parity of the binary digit sum.
SYSTEMATICS  the entropy value rests on the exact factorization of the
             characteristic polynomial over Z[phi] plus the imported
             entropy formula; the fixed-point identity is audited by two
             independent exact paths (integer determinants against
             Galois norms in Z[zeta_5]); the factor counts carry a
             stabilization witness (prefix 2^16 equals prefix 2^17);
             universal linearity of TM complexity is the labeled import.
THRESHOLD    any gate FAIL kills the probe. Exact equality only.
LAYER        as declared above; no gate to L6 is consumed or opened.
```

## The written proofs

J-TORAL-ENTROPY. The characteristic polynomial of the step matrix is
x^4 - 3x^3 + 4x^2 - 2x + 1 (E1, exact), which factors over Z[phi] as
(x^2 - phi^2 x + phi^2)(x^2 - (2 - phi) x + (2 - phi)) (E2a, exact
coefficient identities). Both discriminants are negative (E2b, exact
signs), so the eigenvalues are two complex conjugate pairs with squared
moduli phi^2 and 2 - phi = phi^-2 exactly. Imports: for a hyperbolic
toral automorphism, topological entropy equals Haar-measure entropy and
equals the sum of the logs of the expanding moduli. Hence
h = log phi + log phi = 2 log phi. No eigenvalue is a root of unity
(the moduli differ from 1), so #Fix(T^n) = |det(M^n - I)|, and
det(M^n - I) = prod (lambda^n - 1) = N(J^n - 1); the verifier checks the
two paths agree for n = 1..15 (E3) with the witness 1860496 at n = 15.

TM-ENTROPY-ZERO. The driver is the fixed point of the copy-and-flip
substitution; its factor complexity is linear (import: the exact
Thue-Morse complexity formula of Brlek and of de Luca-Varricchio).
Linear complexity gives topological entropy 0 for the driver subshift.
The verifier pins the exact counts to L = 20 with a stabilization
witness between prefixes 2^16 and 2^17 (E4).

BINARY-READ-RELATIVE-ENTROPY. For any factor map onto a binary process,
h(q) <= log 2 (binary alphabet) and h(q) <= 2 log phi (import: entropy
never increases under factors). Define R(q) = 2 log phi - h(q). Then
R(q) lies in [2 log phi - log 2, 2 log phi] = [log(phi^2/2), 2 log phi],
the floor is strictly positive because phi^2 - 2 = phi - 1 = 1/phi > 0
exactly (E5a), and the split identity 2 log phi = log 2 + log(phi^2/2)
is the exact factorization phi^2 = 2 (phi^2/2) (E5b). Any deterministic
schedule (the TM driver read among them) has h = 0 and attains the
ceiling. Whether any J-canonical read attains the floor is NOT claimed
(that is the lane's separate [H], not carried here). Exactness of the
ceiling: phi^2 is irrational, so 2 log phi is the log of no rational;
and the norm gates N(phi^2) = 1, N(2) = 4, N(5) = 25 with phi of
infinite order give multiplicative independence of {phi^2, 2, 5}, hence
Q-linear independence of their logs (E5c): the residue ceiling equals
neither log 5 nor log 4 in any fixed base.

## Proposed fold edits (a later sealed fold, not this probe)

Registry, three rows (tab-separated):

```text
J-TORAL-ENTROPY	T	the step matrix of J = 1 + zeta_5^2 induces a hyperbolic toral automorphism of R^4/Z^4 with eigenvalue moduli exactly phi, phi, 1/phi, 1/phi (characteristic polynomial x^4-3x^3+4x^2-2x+1 factoring over Z[phi] with complex pairs of squared moduli phi^2 and 2-phi); h_top = h_Haar = 2 log phi by the entropy formula for toral automorphisms (import labeled); #Fix(T^n) = |det(M^n - I)| = |N(J^n - 1)| with witness #Fix(T^15) = 1860496 by two exact paths	2. Time, space, and the decoder	probes/P-ENTROPY-RESIDUE-MATH-1	an exact eigenvalue-modulus off {phi, 1/phi} or a fixed-point count differing from |N(J^n - 1)|
TM-ENTROPY-ZERO	T	the Thue-Morse driver theta_n = s_2(n) mod 2 has linear factor complexity (exact counts p(1..4) = 2, 4, 6, 10 and p(20) = 60, stabilized; the universal linear formula is the labeled import), hence the driver subshift has entropy rate 0	3. The kernel and the census	probes/P-ENTROPY-RESIDUE-MATH-1	a factor count off the pinned table, or superlinear complexity exhibited at any window length
BINARY-READ-RELATIVE-ENTROPY	T	for any binary factor q of a system at entropy rate 2 log phi, the residue R(q) = 2 log phi - h(q) lies in [log(phi^2/2), 2 log phi] with strictly positive floor (phi^2 - 2 = 1/phi > 0 exactly) and exact split identity 2 log phi = log 2 + log(phi^2/2); deterministic schedules attain the ceiling; floor attainability is not claimed; 2 log phi is the log of no rational and is Q-linearly independent of log 2 and log 5 by the norm gates on {phi^2, 2, 5}	2. Time, space, and the decoder	probes/P-ENTROPY-RESIDUE-MATH-1	an exact refutation of the bracket algebra, the split identity, or the norm gates
```

Frontier: no change; ENTROPY-LAYER-BRIDGE [O] keeps its exact scope and
this probe must never be cited as closing or weakening it. Ledger delta:
claims +3, T +3.

## Non-claims

No physical measure, no L6 lift, no claim that the cosmogenesis produces
2 log phi per tick (that identification is exactly ENTROPY-LAYER-BRIDGE
[O] and stays open), no canonical binary read (the lane's [H] is not
carried), no edit to any ENTROPY-* census row.
