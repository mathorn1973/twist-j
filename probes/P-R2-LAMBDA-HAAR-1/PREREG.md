# P-R2-LAMBDA-HAAR-1 preregistration

Status: PREREGISTERED CANDIDATE; FIRST FORMAL RUN PENDING REMOTE PIN READBACK

This document freezes one proof-first public no-go probe. It contains no
formal gate output and earns no scientific status. Formal execution is
forbidden until this exact revision and `verify.py` are committed, pushed,
and read back as one immutable preregistration pin.

## Public identity and action layer

```text
program:          J-LI
probe:            P-R2-LAMBDA-HAAR-1
public lock:      issue 58
owner:            A. M. Thorn
branch:           probe/P-R2-LAMBDA-HAAR-1
path:             probes/P-R2-LAMBDA-HAAR-1/
action layer:     L6 spectral type/multiplicity; compact lambda-adic boundary Koopman class; no further lift
scientific state: candidate proof-first no-go; RH and every replacement
                  carrier remain open
```

Authority base is Public Canon v8, tag `canon-v8`, content commit
`208124ac19dbdc65c6f1cc80616ce55dbbceac51`, Canon SHA-256
`eabf29bc8058fa42104b53b44b0e6db3f02540f48fa79b54d5873c4f4fb09d0b`,
Canon byte count 65077. The probe earns at most public status `T` by the
proof frozen below; `verify.py` is an exact audit of the finite witnesses,
not the source of the theorem. The two-architecture gate is the local
`aarch64` record plus the required GitHub `x86_64` check; no prior
run is carried in as the public pin.

## Frozen preregistration body


```
CANDIDATE:  P-R2-LAMBDA-HAAR-1
SESSION:    r2-lambda-haar-2026-07-17 (one session, one owner, this doc claims it)
DIRECTIVE:  owner "Zacni R2" on the Lane A route table (R2: lambda-adic
            boundary at p = 5 plus archimedean).
TARGET:     public line on promotion. This probe carries no authority until public validation.
LAYER:      L6 (spectral type and multiplicity of the carrier). Any lift is a
            separate gate.
STATUS:     candidate. Expected honest outcome, stated up front: the compact
            boundary Koopman sub-route FIRES as candidate-F; the paired no-go
            lands as candidate-T; the cocycle-form residue is frozen as a
            candidate-H for possible separate registration with its falsifier;
            the surviving R2 corners are named.
```

## 0. Currency

Verified earlier in this same session (r4/r2 day): Public Canon v8 ACTIVE,
tag canon-v8, CONTENT_COMMIT 208124ac, canon/CANON.md fetched and hashed:
eabf29bc8058fa42104b53b44b0e6db3f02540f48fa79b54d5873c4f4fb09d0b, 65077
bytes, match. Public anchors used: ENTROPY-COUNT-MATCH [C] (the order tower
ord(J mod lambda^i) = (4, 20, 20, 20, 20, 20, 100, 100) for i = 1..8),
J-RAMIFIED-CHORD [T], PLENUM-POINT [T], J-LI-TORAL-HAAR-NOGO [T].

## 1. Claim under test (the R2 sub-route: compact boundary Koopman)

There exist a unit u of O_lambda (canonically u = J = 1 + zeta_5^2, a unit
since N(J) = 1) and data making the Haar-Koopman operator

    (U_u f)(x) = f(u x)   on   L^2(O_lambda, Haar)

an exact Li witness. Primary form (publicly anchored, the toral no-go's
format):

```
cocycle form  exists v in L^2 with ||sum_{k<n} U_u^k v||^2 = lambda_n for all
              n >= 1.
```

The unconditional theorem this probe targets for registration is the Hilbert-Schmidt
divergence ||I - U_u^n||_S2^2 = infinity (K1), which is TRUE with no external
input and places U_u outside every Hilbert-Schmidt-perturbation Li witness
class. The secondary S2 form, I - U_u Hilbert-Schmidt with
lambda_n = (1/2) ||I - U_u^n||_S2^2, and its exclusion from the specific
prior-lane S2 normal form (not yet public), is a conditional corollary, not
load-bearing. The cocycle-form verdict is the H residue of section 4 (K3).

## 2. Frozen model

```
M1  O = Z[zeta_5], lambda = 1 - zeta_5, O_lambda the completion at the
    ramified place; Eisenstein model E(x) = Phi_5(1 - x)
    = x^4 - 5x^3 + 10x^2 - 10x + 5, so O_lambda = Z_5[lambda].
M2  Valuation bridge: the place is totally ramified and Galois, so
    v_lambda(a) = v_5(N(a)) exactly for a in O, N the Q(zeta_5)/Q norm.
M3  Dual filtration: the additive characters of O_lambda form a discrete
    torsion module filtered by conductor level; level n carries 4 . 5^(n-1)
    primitive characters; U_u permutes characters, psi_c -> psi_{u c}; the
    orbit of a unit-labeled level-n character has size ord(u mod lambda^n).
M4  For u = J: J - 1 = zeta_5^2 is a unit (v_lambda = 0), so the trivial
    character is the only character-basis element fixed pointwise at every
    level. This does NOT make ker(U_J - 1) one-dimensional: every finite
    nontrivial character orbit has an invariant orbit-sum, and the disjoint
    exact-level orbits give infinitely many orthogonal such sums.
```

## 3. Imports

```
I1  J-LI-S2-NORMAL-FORM, J-LI-S2-SPECTRAL-RIGIDITY [prior lane, NOT public].
    The witness class and the forced Cayley eigenangles
    theta_gamma = 2 arctan(1/(2 gamma)). Used ONLY for the conditional
    secondary S2-form corollary and for the H-residue angle set; the
    unconditional HS-divergence theorem (K1) does not depend on them. The
    LOAD-BEARING public anchor is J-LI-TORAL-HAAR-NOGO [T].
I2  J-LI-CYCLIC-CARRIER-DIMENSION [prior lane, NOT public]. Conditional and
    non-load-bearing here: its realization measure has infinite support,
    1 in supp, and no atom at 1. Those are properties of the desired
    prior-lane realization measure, not of this Koopman operator: U_J has an
    infinite-dimensional 1-eigenspace from character-orbit sums. I2 is used
    only in motivating the conditional H-residue; neither K1 nor K2 depends
    on it.
I3  Li's criterion [classical].
I4  Pontryagin duality and the conductor filtration for local fields
    [classical].
I5  CNF block for the R2 target [classical]: L(1, chi_2) = 2 log phi / sqrt5
    (Dirichlet, h(Q(sqrt5)) = 1); the odd-character formula
    L(1, chi) = (pi i tau(chi)/5) B_{1, chibar}; h(Q(zeta_5)) = 1,
    R_K = 2 log phi, w = 10, |d| = 125.
I6  Euler-Maclaurin with one-signed-derivative envelopes [classical].
I7  PI-ENCLOSURE: 3141592653589793/10^15 < pi < 3141592653589794/10^15.
I8  Public anchor ENTROPY-COUNT-MATCH [C]: the order tower, to be
    RE-DERIVED here independently in the Eisenstein model (a break attempt
    on the public row, not a citation of it).
I9  Cited prior-lane pins to be independently reproduced (I(a) gamma_1 in
    [-0.072815845578467363, -0.072815845393082604]; I(b) M_1 in
    [0.000037100438723459, 0.000037100843555683]), from the prior cocycle-lane result.
```

## 4. The kill mechanisms (stated before computing)

```
K1 (Hilbert-Schmidt divergence, unconditional, phase-blind). For any unit
   u != 1 with t = v_lambda(u - 1) < infinity, every unit-labeled character
   of level n > t is non-fixed, so ||(I - U_u) e_psi||^2 = 2 on infinitely
   many orthonormal characters and ||I - U_u||_S2^2 = infinity. The same
   holds for every power: ||I - U_u^n||_S2^2 = infinity whenever u^n != 1
   (for u = J: all n >= 1). Indeed, under the complex embedding
   zeta_5 -> exp(2 pi i/5),
       |J|^2 = |1 + zeta_5^2|^2 = (3 - sqrt(5))/2 != 1.
   If J^n = 1 for some n >= 1, this embedding would have |J|^n = 1, a
   contradiction. Hence J is non-torsion and
   v_lambda(J^n - 1) < infinity for every n >= 1. Thus I - U_u is not
   Hilbert-Schmidt for u != 1 and U_u lies outside every
   Hilbert-Schmidt-perturbation Li witness class. This is the unconditional
   theorem candidate proved here; it needs no non-public input. The argument ignores
   phases, so it also covers affine unit actions x -> u x + b.
K2 (structure lemma). U_u permutes an orthonormal character basis with all
   orbits finite; hence U_u has pure point spectrum, every eigenvalue is a
   root of unity, and the 1-eigenspace is infinite-dimensional because each
   of infinitely many disjoint finite character orbits supplies an invariant
   orbit-sum. Every non-identity eigenvalue that appears has unbounded
   multiplicity across levels as well. For u = J the available non-identity
   eigenvalues are exactly the 4 . 5^a-th roots of unity, and the real vector
   psi_1 - psi_2 + psi_4 - psi_3 on the level-1 orbit (1 2 4 3) is an
   explicit (-1)-eigenvector.
K3 (cocycle-form residue, honest gap). In the cocycle form the spectral
   measure of every v is purely atomic with atoms only at the available
   roots of unity; a realization would force the symmetrized measure to
   equal sigma_xi, hence force EVERY Cayley angle 2 arctan(1/(2 gamma))
   into 2 pi (1/4) Z[1/5], and along n_A = 4 . 5^A the ladder second-moment
   sums t_{n_A} would tend to the full mass 2 lambda_1. This is not
   refutable unconditionally today; it is frozen as the proposed hypothesis
   LAMBDA-COCYCLE-ANGLES for possible separate registration with the
   falsifier below, and
   the sub-route is closed in the S2 class by K1 regardless.
```

## 5. Code and environment (frozen before the code exists)

```
verifier    verify.py
            Python stdlib only; exact integer arithmetic in Z[zeta_5] and
            Z[zeta_20]; exact Fraction interval arithmetic with the atanh
            log machinery and EM envelopes; no float in any assertion;
            decimal prints are labeled witnesses only.
run         first formal local leg must be aarch64/arm64 after remote pin
            readback and must repeat byte-identically three times. The required
            GitHub x86_64 leg is the later public gate; neither is claimed here.
env         LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

## 6. Failure threshold (the package FAILS to establish if any gate fails)

```
R0   N(J) = 1 by exact conjugate product in Z[zeta_5] (J is a unit).
R1   E(x) = Phi_5(1 - x) = x^4 - 5x^3 + 10x^2 - 10x + 5 by exact expansion;
     Eisenstein at 5; E(0) = 5 = N(lambda).
R2   disc(E) = Res(E, E') = 125 by exact Sylvester determinant.
R3   N(J - 1) = N(zeta_5^2) = 1, so v_lambda(J - 1) = 0.
R4   V-profile V(k) = v_5(N(J^k - 1)) for k = 1..100; the derived order
     table min{k : V(k) >= n} for n = 1..8 equals
     (4, 20, 20, 20, 20, 20, 100, 100), matching the public anchor by an
     independent model.
R5   Orbit counts 4 . 5^(n-1) / ord(n) = (1, 1, 5, 25, 125, 625, 625, 3125)
     for n = 1..8, all integral.
R6   Level-1 witnesses, exact integer linear algebra: the permutation
     (1 2 4 3) from J = 2 mod lambda; U w = -w for the real vector
     w = psi_1 - psi_2 + psi_4 - psi_3; U w_i = i w_i over Z[i] for
     w_i = psi_1 - i psi_2 + i psi_3 - psi_4.
R7   HS divergence bookkeeping: the exact-level non-fixed counts are
     4 . 5^(n-1); the partial sum 2 sum_{j<=8} 4 . 5^(j-1) = 2(5^8 - 1)
     = 781248; and V(k) < infinity for every k = 1..100 (no J-power is 1).
R8   The (-1)-multiplicity witness: all orbits at levels 1..4 have even
     size, and their count is 1 + 1 + 5 + 25 = 32.
R9   CNF target block, exact: the chi table on (Z/5)* with chi(2) = i;
     B_{1,chi} = (-3 - i)/5 and |B_{1,chi}|^2 = 2/5; tau(chi) tau(chibar)
     = 5 in Z[zeta_20]; tau(chi_2) = 2 phi - 1 in Z[zeta_5]; the symbolic
     residue identity (2 pi)^2 h R_K / (w sqrt|d|) = L(1,chi_2) |L(1,chi)|^2
     with both sides equal to (4/25) pi^2 log(phi) / sqrt5 as exact rational
     coefficients; |L(1,chi)|^2 = 2 pi^2 / 25.
R10  Junction instrumentation, independent reproduction: gamma enclosure by
     EM at N = 300 with width < 1e-12; gamma_1 enclosure contained in the
     cited pin I9(a); lambda_1 = 1 + gamma/2 - (1/2) log(4 pi) inside
     (0.0230957, 0.0230958); M_1 = 3 + gamma + gamma^2 + 2 gamma_1
     - pi^2/8 - log(4 pi) contained in the cited pin I9(b) and > 0.
```

## 7. Falsifiers

```
Of the package    any gate R0..R10 fails. A containment failure at R10
                  additionally fires a DISCREPANCY against the prior cocycle-lane result
                  pins and is reported either way, per the negative-vector
                  discipline.
Of the route      the expected outcome: the compact boundary Koopman
                  sub-route of R2 fires as candidate-F in the S2 class.
H residue         LAMBDA-COCYCLE-ANGLES: the cocycle-form lambda-adic
                  Haar route survives only if every Cayley angle
                  2 arctan(1/(2 gamma)) lies in 2 pi (1/4) Z[1/5]. Fires if
                  any single ordinate's angle is proven outside that set, or
                  if the Li second differences are shown not to approach
                  2 lambda_1 along n = 4 . 5^A.
```

## 8. Not covered (frozen honesty)

The noncompact scaling flow on L^2(K_lambda) (the lambda-adic dilation
carrier; spectral type not purely atomic); boundary-distribution plus
archimedean composites; adelic products; per-character twisted (non-unitary
or non-invariant) actions. These are the SURVIVING R2 corners and the next
construction targets, not casualties of this candidate. Nothing here bears
on RH. RH [O] before, during, and after.

## 9. Break-it-yourself plan (post-run, recorded in the PROMO)

```
a  phases (affine actions)     covered by K1 (phase-blind HS divergence).
b  choose v cleverly           cocycle form only; the residue H names the
                               exact hypothesis such a v would need.
c  enlarge the space           leaving L^2(O_lambda, Haar) leaves the frozen
                               sub-route; the scaling flow is named open.
d  u a root of unity, u = 1    u = 1 gives the zero ladder; root-of-unity u
                               gives infinite rungs off the period and zero
                               on it; both fail rung 1 = lambda_1 > 0.
```
