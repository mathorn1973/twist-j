# PREREG-AUDIT-LAMBDA-GRID-1

```text
KIND:        independent audit of the angular clause of LAMBDA-COCYCLE-ANGLES [H]
             and of its two public theorem companions, at the owner's direction
             "zkus to overit, promyslet" (the grid placement, not RH)
SESSION:     AUDIT-LAMBDA-COCYCLE-GRID (one named session, this audit only)
AUTHORITY:   none. Project-side audit. No repo edit, no registry motion,
             no canon change, no probe, no fold. NON-CANONICAL.
BASIS:       Public Canon v56 ACTIVE, mathorn1973/twist-j main,
             clone HEAD 4ed6cb72ab1110b68ed0574115e9dacbaf65e954,
             TAG canon-v56, CONTENT_COMMIT b36c93ed8ce24a9cbd771168094db04f5a5ac06c,
             CANON_SHA256 b284ed6e78341aa6e3a74652d6f1f8f4079c270461f28bf32f2d95a6bd8b6645,
             CANON_BYTES 288492, SHA256SUMS 5 of 5 OK, tag and content commit
             verified ancestors of main.
LAYER:       L6 measure and spectral only. No lift.
DATE:        2026-08-20
```

## Falsifiers first

The public row's own falsifier (quoted scope, not restated stronger): the row
fires if RH is disproved, or if one nontrivial zero is exactly proved not to be
rho = 1/(1 - xi) with xi != 1 and xi^(4 . 5^a) = 1 for any integer a >= 0.
This audit does not attempt either and cannot: the grid ordinates are dense in
the reals, so no finite enclosure decides membership.

Local falsifiers of THIS audit, each a first class outcome if fired:

```text
AF1  any registered exact fact fails under the independent recomputation:
     ord_lambda(J) = 4; |(O/lambda^k)^x| = 4 . 5^(k-1);
     ord_(lambda^(4m))(J) = 4 . 5^m for m = 1..3;
     the valuation ladder v_lambda(J^4 - 1) = 1, v_lambda(J^20 - 1) = 6,
     v_lambda(J^(4 . 5^m) - 1) = 4m + 2 for m = 1..6;
     the order table ord_(lambda^k)(J) = 4 . 5^ceil((k-1)/4) for k = 1..14.
AF2  the three grid constructions disagree on any reduced fraction with
     denominator up to 500: orbit generated set, arithmetic set
     {p/q : q = 2^e 5^f, e <= 2}, lambda-adic torsion realizability set.
AF3  any torsion certificate fails: mu_4 Hensel lift to 5^60; mu_3 or mu_8
     admitting a residue root mod 5; an Eisenstein certificate for
     Phi_5(x+1), Phi_25(x+1), Phi_125(x+1) failing.
AF4  any symbolic identity fails: the Cayley unit and half angle triple,
     the reciprocal square collapse, the second difference identity,
     the Fejer second difference at the declared exact-cosine angles,
     the template chain of ring identities listed in field one.
AF5  the finite shadow of the all-real annihilation lemma fails: a declared
     grid fraction not annihilated at its level, or a declared off-grid
     fraction at distance below 1/q from Z at some index A <= 12.
AF6  an adversarial synthetic tail check fails: a grid-supported synthetic
     measure whose residual M - t_(n_A) does not vanish exactly beyond its
     level, or an off-grid atom (denominators 3, 8, 12) whose residual drops
     below its exact positive bound at any A <= 12.
AF7  reproduction failure: the two pinned public verifiers, run unmodified
     from the clone, exit nonzero or produce stdout whose SHA-256 differs
     from the sealed values 9e46f7f56d7e4b22683e3b595707f5bb880ef707771ac75
     aaa35a8dcc2584688 (probe 1) and 7c5b661401dc245e9469e9cc7b6e9129f4a773b
     44226410ff557770d35727eeb (probe 2).
AF8  the two independent valuation routes disagree anywhere: norm route
     v_lambda = v_5(N(.)) in the verifier against the lambda-division route
     in the breaker; or the matrix route ord of M_J in GL_4(Z/5^m) disagrees
     with the ring route at m = 1..6.
```

A fired AF is archived, not deleted, and no threshold moves.

## Field one: equation (what is audited)

Notation as in the public probes: zeta = zeta_5, O = Z[zeta], lambda = 1 - zeta,
J = 1 + zeta^2, phi = -zeta^2 - zeta^3, U_J the Koopman operator of
multiplication by J on L^2(O_lambda, Haar), grid = 2 pi (1/4) Z[1/5],
n_A = 4 . 5^A, alpha_gamma = 2 arctan(1/(2 gamma)), t_n and M = 2 lambda_1 the
Li second difference data, D_n the Fejer kernel square with D_0 = 0, D_1 = 1.

Audited claims, with the grade each check can earn here (single platform,
candidate labels only):

```text
A1  ring anchors and the template chain [candidate-T, exact finite identities]:
    J phi = zeta; N(J) = 1; Tr(J) = 3; (J-1)^3 = zeta; J = 2 mod lambda;
    lambda^4 = 5 u with u = -zeta + zeta^2 - zeta^3 a unit;
    the Cayley triangle step 1/(1 - J) = -zeta^3 exactly;
    the template point rho_T = 1/(1 - xi) at xi = -zeta^3 satisfies
    rho_T = phi zeta, rho_T + conj = 1 (real part exactly 1/2),
    |rho_T|^2 = phi^2, cot^2(pi/10) = 4 phi^2 - 1 = 4 phi + 3 in Z[phi],
    1 - 1/rho_T = -zeta^3, and -zeta^3 has order 10, turn 1/10, a grid point;
    the uniformizer identity (1 - zeta^4)(-zeta) = 1 - zeta, hence
    e^(2 i theta) = -zeta for theta = arg(1 - zeta), so the turn of lambda
    lies in {7/20, 17/20} mod 1: on the grid, and in neither case in
    (1/2) Z[1/5]: the factor 1/4 is forced already by the uniformizer.
A2  the registered orbit and valuation structure of GRID-EQUIVALENCE [T],
    recomputed by an independent code path [candidate-T]: values in AF1.
A3  grid canonicity three ways [candidate-T for the finite checks; the prose
    proofs are standard local field theory]: the orbit generated angle set,
    the arithmetic set, and the lambda-adic torsion realizability set agree;
    mu(Q_5(mu_(5^infinity))) = mu_4 x mu_(5^infinity), certified at finite
    level by: mu_4 Hensel lift in Z_5; no mu_3 or mu_8 residue root mod 5;
    Eisenstein certificates for the total ramification of the 5-tower.
    Consequence stated for the audit: the grid equals the set of angles of
    roots of unity that exist in the lambda-adic cyclotomic tower, so it is
    maximal for every lambda-adic torsion transport, not only for U_J.
A4  the all-real annihilation lemma, finite rational shadow [candidate-C]:
    grid fractions annihilated at their level; off-grid denominators
    3, 7, 8, 9, 11, 12, 16, 24, 60 at distance >= 1/q for all A <= 12.
A5  the second difference mechanism [candidate-T]: X^(n+1) + X^(n-1) - 2 X^n
    = X^(n-1)(X - 1)^2; the Cayley unit identities of BRANCH-COLLAPSE R1
    re-verified symbolically over Q[g] by cross multiplication; the Fejer
    second difference D_(n+1) + D_(n-1) - 2 D_n = 2 cos(n theta) verified
    exactly in Z[phi]/2 cosine arithmetic at theta in
    {2 pi/5, pi/5, pi/2, 2 pi/3} for n = 1..60, D_1 = 1; the two initial
    value induction rebuild.
A6  adversarial synthetic tails [candidate-T, exact rationals]: grid atoms at
    turns 1/20, 7/100, 1/4 with rational masses, plus a shared angle merge:
    residual exactly zero for all A >= 2; off-grid atoms at turns 1/3, 1/8,
    5/12: residual exactly 3 m, 4 m, 3 m respectively for every A (period
    argument 5^A mod 3 in {1, 2}, and frac(5^A/2) = 1/2), never decaying.
A7  reproduction of the sealed evidence [reproduction only, same architecture
    class as the probes' local legs]: run both pinned verifiers, compare
    stdout SHA-256 to the sealed values.
```

## Field two: code

Two programs, Python standard library only, integers and Fraction, no float
anywhere, deterministic output, fixed check order, exit nonzero on any FAIL:

```text
verify_lambda_grid_audit_1.py   A1..A6 on the primary independent path:
   circulant 5-vector representation of Z[zeta] in Z[x]/(x^5 - 1) with
   canonical reduction modulo the constant vector (deliberately not the
   4-tuple basis of the sealed probes); norms as full conjugate products;
   v_lambda = v_5(N(.)); Z[phi] pairs for cosine arithmetic; Q[g]
   polynomial pairs for the symbolic identities.
breaker_lambda_grid_audit_1.py  the attack pass: lambda-division valuation
   route (second, independent within this audit); M_J matrix route in
   GL_4(Z/5^m) built from the axiom step map; refutation of the naive
   boundary guess v_lambda(J^20 - 1) = 5; mu_3 and mu_8 Hensel attack
   obstruction; adversarial shared-angle and off-grid synthetics; A7
   reproduction runs with hash comparison.
```

Frozen command for both:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 <file>
```

## Field three: carrier or data

No external dataset. No zeta ordinate is instantiated anywhere; ordinates
appear only as the free polynomial variable g. The carrier is Z[zeta_5] in the
circulant representation, its quotients Z/5^M with M = 40 (valuations up to 30
are decidable and none above 26 is asserted), Z[phi] pairs, and Fraction.
Frozen ranges: order levels k = 1..14; ladder m = 0..6; grid levels a <= 3
(denominators to 500); annihilation indices A <= 12; Fejer range n = 1..60;
Hensel precision 5^60; reproduction targets: the two sealed stdout hashes.

## Field four: systematics

Branch conventions: the u-ratio z/sigma_4(z) determines the turn only mod 1/2;
membership in the grid is invariant under a 1/2 shift because 1/2 = 2/4 lies in
(1/4) Z[1/5]; where a single branch is asserted (the lambda quadrant) it is
fixed by exact sign certificates on real and imaginary parts using the rational
sandwich 3/2 < phi < 2 from 4 < 5 < 9. Reduction conventions: equality in the
circulant representation means the difference is a constant vector. The
reproduction step depends on the pinned files as present in the clone at HEAD
4ed6cb72; their hashes are compared against the sealed RESULT records first.
No tolerance, no retry, no threshold movement after this freeze.

## Field five: failure threshold

Any FAIL line in either program is a fired local falsifier AF1..AF8, recorded
as a finding in the audit; agreement failures between independent routes (AF8)
are diagnosed before any claim against a public row is voiced; a finding that
survives both routes is reported against the corresponding public row with its
exact witness. PASS earns candidate labels only, as declared per check.
Single platform: nothing here can earn a public T, and no summary of this
audit may exceed candidate grade or the sealed rows' own scope.

## Field six: action layer

L6 measure and spectral only. No L1..L5 claim, no decoder, no physics reading,
no SI statement. The commentary on J = 2 mod lambda as the doubling residue is
labeled commentary and carries no layer lift.

## Order of operations declaration

This file is frozen and hashed before either program is executed. Both
programs are then written, statically reviewed, executed once each under the
frozen command, and their stdout captured and hashed. Findings are recorded
as-is. Exploration before this freeze was symbolic derivation and repository
reading only; no formal gate was executed.
