# PREREG C-CASIMIR-COEFFICIENT-1

Candidate id: C-CASIMIR-COEFFICIENT-1. Incubation lane, this project. NO AUTHORITY.
Target line on promotion: public, mathorn1973/twist-j.
Basis (currency gate, this session): Public Canon v25, STATE ACTIVE,
AUTHORITY mathorn1973/twist-j main, TAG canon-v25,
CONTENT_COMMIT b914755b422bf79a8be637993b2edaa12a4333f8,
CANON_SHA256 53fa5acc9f2d910b26293d5152d93deac6596abd012997c7ff195397d9e476bb,
CANON_BYTES 136831, canon/SHA256SUMS 5 of 5 OK, tag and content commit both
ancestors of main. Internal line NOT REACHABLE from this session (no
credentials); the v184 pin is therefore assumed, not verified, and nothing
below rests on it.

Prior art disclosed: the owner has previously explored a Casimir reading of
the coefficient 240 along a zeta_5 to 2I / A_5 path. That exploration is not
in Canon, not in the public registry, and not in this project's documents.
This preregistration is written to decide it, not to confirm it.

## 0. Falsifier first

The arithmetic identity in F1 is, once the definitions are fixed, a tautology.
It is not the claim. The claim under test is that the LETTERS are forced. The
decisive gates are G3 and G5, and both are written to kill.

```
F1  ARITHMETIC. If the exact identity
        F_Casimir / A = - hbar c . p L / (d (d+1) a^4)
    fails over Q with L := Re Li_2(J) = pi^2 / (2p)^2, p = 5, d = 3, against
    the standard ideal parallel-plate electromagnetic Casimir coefficient
    pi^2 / 240, the candidate dies outright.
F2  ROUTE. If zeta(-3) != 1/120, or 120 != |SL(2, F_5)| = p(p^2 - 1) at
    p = 5, or 30 != p(p+1) at p = 5, or the reflection route from zeta(4)
    does not reproduce zeta(-3) exactly, the route reading dies.
F3  FAMILY (the break). If the agreement "denominator of the Bernoulli
    number B_(d+1) equals the Canon edge count p(p+1)" does not extend to a
    structural family over d, then the identification of 120 with the
    icosahedral order is a d = 3 coincidence and the READING caps at R.
    The arithmetic of F1 is unaffected.
F4  SEARCH SPACE. If the preregistered Canon integer set S admits two or
    more distinct exact hits of the target ratio 5/12 by the family a/b with
    a, b in S, the reading "the letters are forced" caps at R, whatever G1
    returns.
F5  SCOPE. Any statement assigning J a physical lattice constant, or any SI
    statement about plate separation, force in newtons, or an absolute
    length, fires the candidate immediately. The plenum has no spacing.
    O-METRO-EDGE-SCALE is open and this candidate does not touch it.
```

Author's unverified scratch expectation, disclosed, binding nothing: G1 and
G2 pass, G3 fails, G5 returns multiplicity two or more. Expected earned label
therefore C for the arithmetic and R for the reading. The gates decide.

## 1. Equation

```
Canon inputs, all already sealed, none re-derived here:
    p = 5, d = 3                                    (Part XX, thirteen witnesses)
    L := Re Li_2(J) = pi^2 / (2p)^2 = pi^2 / 100    (Stone 2, LOCK)
    rho_0 = 1/6, the gyron density                  (SS104, T-LOCK)
    |2I| = |SL(2, F_5)| = 120                       (T-COLOR-CORE-2I, T)
    (V, F, E) = (2(p+1), p(p-1), p(p+1)) = (12, 20, 30)   (T-VFE-PRIME, T)
    k = d(d+1) = 12, the chain of twelves           (T-FRW-CANONICAL-FORM-COVARIANT, T)

External input, standard textbook, imported and labeled as import:
    ideal parallel perfect conductors, zero temperature, massless EM field,
    energy per area   E/A = - pi^2 hbar c / (720 a^3)
    force per area    F/A = - pi^2 hbar c / (240 a^4)
    massless scalar, Dirichlet, is exactly half of each.

Candidate statement, dimensionless content only:
    C1   pi^2 / 240 = p L / (d (d + 1))            exactly in Q[pi^2]
    C2   pi^2 / 720 = rho_0 . pi^2 / |2I|          exactly, equivalently
         pi^2 / 720 = zeta(2) . zeta(-3)           exactly
    C3   zeta(-3) = - B_4 / 4 = 1 / (p (p^2 - 1))  at p = 5
    C4   denominator(B_4) = 30 = p (p + 1)         at p = 5, and equals the
         von Staudt-Clausen product over primes q with (q - 1) | 4
    C5   the polarization 2 relating scalar to EM is the TT vector doublet
         already sealed at D-TT-VECTOR-DOUBLET; no new input.
```

## 2. Code

One verifier, Python standard library only, `fractions.Fraction` and integers.
No float in any assertion. pi carried as a formal symbol with an integer
exponent; every assertion is an assertion about rationals. Runtime under
120 seconds. Environment
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.
Bernoulli numbers computed from scratch by the recursive definition, not
tabulated. Deterministic ordered output, one line per gate.

## 3. Carrier

Pure arithmetic over Q with a formal pi. No kernel state, no census, no
stream, no measure. Declared layer L1. No lift to any other layer is claimed
or performed. The external Casimir coefficient is an IMPORT and is labeled as
such wherever it appears; nothing in this candidate derives it.

## 4. Systematics

```
S1  The identity C1 is definitional once L, p, d are fixed. Its evidential
    value is zero on its own. G5 measures exactly that.
S2  The 30 of B_4 has an independent classical explanation (von Staudt-
    Clausen). Two explanations landing on one integer is not a derivation.
S3  The standard Casimir coefficient depends on the boundary condition and
    on the field content. The imported value is the ideal conductor case
    only. No real-material, finite-temperature or roughness correction is
    considered, and none may be quoted.
S4  Both zeta(4) and zeta(-3) routes reach the same number. Agreement
    between them tests the code, not the physics.
```

## 5. Failure threshold

```
G1  C1 exact                                   -> pass or the candidate dies (F1)
G2  C2, C3, C4 exact, both routes agree        -> pass or the route dies (F2)
G3  family scan: denominator(B_(d+1)) against p(p+1) and against p(p^2-1)
    for d = 2 .. 10 with the Canon prime; a structural family must hold for
    at least three consecutive d, else F3 fires and the reading caps at R
G4  von Staudt-Clausen: p = 5 divides denominator(B_D) iff (p-1) | D; report
    every D <= 40 where the vSC prime set is exactly {2, d, p} = {2, 3, 5}
G5  search-space control on the preregistered set S below: count ordered
    pairs (a, b) in S x S with a/b = 5/12, and count distinct values of a/b;
    multiplicity >= 2 fires F4 and caps the reading at R
G6  scope guard: the verifier asserts that no SI quantity, no length and no
    plate separation appears anywhere in its own output (F5)
```

Preregistered Canon integer set S, frozen here, chosen before any count:

```
S = {1, 2, 3, 4, 5, 6, 8, 10, 12, 13, 15, 18, 20, 24, 25, 27, 30, 32, 33,
     36, 40, 60, 63, 64, 72, 89, 100, 120, 144, 200, 240, 313, 720, 864,
     1250, 1728}
```

Every member is a number already carried in Canon or in the standard Casimir
constants. The set is frozen; it may not be grown after the count.

## 6. Action layer

L1 state. No L2 manifold, no L3 boundary, no L4 support, no L5 stream, no L6
measure claim. Any lift needs its own named gate. No SI clause. No promotion
of any kind follows from this document.

## Amendment 1 (disclosed, written before first execution)

Added from author-side scratch reasoning, no code run, no data opened. G3 as
written above scans one family only, denominator(B_(d+1)) against p(p+1) and
p(p^2-1). Scratch reasoning identified a second, structurally different family
which G3 would have missed, and it would be dishonest to find it after a
negative G3 and then present it as preregistered. It is therefore frozen here,
before execution, with its own falsifier.

```
G3b FAMILY, CYCLOTOMIC ROUTE. In Canon, d = dim ker(Tr_(p-1)) = p - 2, so the
    spacetime dimension is D = d + 1 = p - 1. Von Staudt-Clausen states that
    the denominator of B_D is the product of primes q with (q - 1) | D. Since
    (p - 1) = D divides itself, p divides denominator(B_D) NECESSARILY, for
    every prime p, not only p = 5. Gate: verify d = p - 2 and D = p - 1 as
    integers and verify p | denominator(B_(p-1)) for every prime p in
    {3, 5, 7, 11, 13, 17, 19, 23}. Additionally report, at p = 5 only, whether
    the von Staudt-Clausen prime set at D = 4 is EXACTLY {2, d, p} = {2, 3, 5}
    and for which other D <= 40 that set occurs.
F3b If p does not divide denominator(B_(p-1)) for any tested prime, or if
    d != p - 2 in the Canon assignment, the cyclotomic family reading dies.
```

Note on the split this amendment forces. G3b, if it passes, is a family and
therefore theorem-shaped: it says the prime appears in the even-dimensional
Casimir constant by arithmetic necessity once d = p - 2 is granted. G3a, G5
and C3 test something weaker and different: whether the SPECIFIC integer 120
is the icosahedral order rather than an accident. The two must be reported
separately and may not be quoted as one result.

## Two-platform gate

The verifier must produce byte-identical stdout on aarch64 and on x86_64
before any result is recorded above C. Fleet legs: Linux aarch64 leg (aarch64) and
Linux x86_64 leg (x86_64).

## Non-claims

This candidate does not derive the Casimir effect, does not compute a force,
does not assign a length, does not touch O-METRO-EDGE-SCALE, does not touch
the public registry, and promotes nothing. It decides one arithmetic
question and one honesty question.
