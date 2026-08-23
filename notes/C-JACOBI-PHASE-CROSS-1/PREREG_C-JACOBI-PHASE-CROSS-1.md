# PREREG C-JACOBI-PHASE-CROSS-1 (frozen before the census run)

**NON-CANONICAL.** Incubation lane (`notes/`). This document registers
nothing, freezes nothing in the Canon, and earns no public status. It exists
so that the chi-square decision line is fixed on paper before any
contingency table is computed or seen.

```text
CANDIDATE:   C-JACOBI-PHASE-CROSS-1
DATE:        2026-08-23
SESSION:     jacobi-phase-cross, this project
LANE:        notes/ incubation, non-canonical, no registry or frontier edit
ORIGIN:      NADHLED note of 2026-08-22 (non-canonical, parallel session),
             section 5: "mikro-selftest" then "C-JACOBI-PHASE-CROSS-1"
AUTHORITY:   none. Public Canon v26, tag canon-v26, content commit
             138eec5b22a823469e1fa651505815a3d5b36761, is read-only context.
LAYER:       L5 finite exact statements over Z[zeta_5] and Z[phi].
             No lift, no measure, no physical reading.
```

## 0. What is being tested

The origin note claims a cross: for `p = 1 mod 5` the pentagon carries two
integer avatars of the same prime, polar-orthogonal to each other.

```text
w_p   the modulus avatar   generator of a prime of Z[phi] above p;
                           carries the rapidity eta_p, phase content trivial
J_p   the phase avatar     quintic Jacobi sum in Z[zeta_5]; all four
                           embeddings have modulus exactly sqrt(p) (Weil),
                           so its rapidity projection is the zero vector
```

The micro-selftest (`verify_jacobi_selftest.py`, already executed, see
`stdout_jacobi_selftest.txt`) is the exact anchor of the second row. It is a
theorem check with no free parameter and no decision line, so it was not
subject to this freeze.

The census probe asks the one question the two avatars can be asked
together: **is the angular datum of `J_p` independent of the rapidity datum
of `w_p`, prime by prime?**

## 1. Frozen definitions

### 1.1 Carrier

```text
carrier:  every prime p with p = 1 mod 5 and 11 <= p <= 30000
count:    808 primes (asserted by the verifier from its own sieve)
p = 5     excluded, ramified.  p = 4 mod 5 excluded: no quintic character.
```

### 1.2 The ring and its exact real/imaginary parts

`Z[zeta_5]` in the integral basis `(1, zeta, zeta^2, zeta^3)`,
`zeta^4 = -1 - zeta - zeta^2 - zeta^3`. Principal embedding
`zeta -> exp(2 pi i / 5)`. For `X = A + B zeta + C zeta^2 + D zeta^3`:

```text
2 Re X = (2A - B) + (B - C - D) phi                        in Z[phi]
2 Im X = sqrt(3 - phi) * ((C - D) + B phi),  3 - phi = |1 - zeta|^2 > 0
```

Both signs are therefore exact `Z[phi]` sign tests; `sqrt(3 - phi) > 0` never
enters a comparison. No floating point is used in any assertion.

### 1.3 The phase avatar `J_p` and its angular datum

```text
g_p        the least primitive root modulo p
chi_p      the quintic character with chi_p(g_p) = zeta_5,
           i.e. chi_p(x) = zeta_5^(ind_{g_p}(x) mod 5)
J_p        J(chi_p, chi_p) = sum_{x = 2}^{p-1} chi_p(x) chi_p(1 - x)
```

`J_p` depends on the choice of quintic character; the selftest gate S4
records the exact dependence `J(chi^a, chi^a) = sigma_a(J(chi, chi))`. The
least-primitive-root convention above is **frozen** as the primary one.

```text
QUAD(p)    the open quadrant of sigma_1(J_p) in the principal embedding,
           coded 0,1,2,3 for quadrants I,II,III,IV.
           Re sigma_1(J_p) = 0 or Im sigma_1(J_p) = 0 is impossible
           (it would force J_p^2 = +-p in Q(zeta_5)); the verifier asserts
           this rather than assuming it.
```

Galois-invariant secondary datum, free of the character convention:

```text
SGN(p)     the unordered pair { sign Re sigma_1(J_p), sign Re sigma_2(J_p) },
           coded 0 for (+,+), 1 for mixed, 2 for (-,-).
           Invariant under chi -> chi^a because Re sigma_a = Re sigma_{5-a}
           and sigma_2 permutes the two conjugate pairs.
```

### 1.4 The modulus avatar `w_p` and its rapidity datum

`Z[phi]` is a PID, fundamental unit `phi`, `N(phi) = -1`,
`L := log phi`.

```text
r_p        the smaller of the two roots of x^2 - x - 1 = 0 mod p in [0, p)
frak_p     the prime ideal (p, phi - r_p) of Z[phi]
w_p        the shortest nonzero vector of frak_p under the positive definite
           form Q(a + b phi) = |sigma_1|^2 + |sigma_2|^2 = 2a^2 + 2ab + 3b^2,
           obtained by exact Gauss reduction of the basis
           {(p, 0), (-r_p, 1)}.
```

Minkowski on the 2-dimensional lattice gives `Q(w_p) <= (2/sqrt3) p sqrt5 <
2.582 p`, while every nonzero element of `frak_p` has
`Q >= 2 |N| >= 2p`. Hence `|N(w_p)| <= 1.291 p` and `|N(w_p)|` is a positive
multiple of `p`, so `|N(w_p)| = p` exactly and `w_p` generates `frak_p`. The
verifier asserts `|N(w_p)| = p` for every carrier prime rather than relying on
the argument.

Rapidity, normalized into one fold period:

```text
A2 := sigma_1(w_p)^2 = (a^2 + b^2) + (2ab + b^2) phi        in Z[phi], > 0
multiply A2 by phi^(2k) until  p <= A2 < p phi^2            (exact in Z[phi])
eta_p := (1/2) log(A2 / p)  in  [0, L)
```

Associates of `w_p` are `+- w_p phi^k`, and `phi' = -1/phi`, so `eta_p` is
well defined in `R / L Z` given `frak_p`; the choice `r_p = min` fixes which
of the two primes above `p` is used, hence fixes the sign convention.

Frozen exact bins (all comparisons squared into `Z[phi]`, `Y := A2^2`):

```text
QUART(p) = j   iff   p^2 phi^j <= Y < p^2 phi^(j+1),  j = 0,1,2,3
H(p)     = 0   if QUART(p) in {0,1}   (eta_p in [0, L/2))
H(p)     = 1   if QUART(p) in {2,3}   (eta_p in [L/2, L))
```

`H` is the seam bit of the fold `t <-> L - t`. **Reconstruction notice:** the
origin note names a "half-class h" without giving its construction, and no
definition of `h`, `w_p`, or `eta_p` exists anywhere in this repository at
Public Canon v26. `H` above is this session's reconstruction from the note's
own section 4, which reads the cross as the joint law of
`(eta_p mod L; arg J_p)`. If the originating session used a different `h`,
every table below must be recomputed; that is a stated falsifier of the
comparison, not of the arithmetic.

## 2. The three frozen tests

All statistics are Pearson chi-square of independence on a contingency table,
computed as an **exact rational** with `fractions.Fraction`. Thresholds are
the tabulated 0.99 quantiles rounded to three decimals and are frozen as
exact decimals.

```text
T1  primary     QUAD(p) x H(p)          4 x 2   df 3   crit 11.345
T2  secondary   SGN(p)  x H(p)          3 x 2   df 2   crit  9.210
T3  secondary   QUAD(p) x QUART(p)      4 x 4   df 9   crit 21.666
```

Decision rule, identical for all three and frozen:

```text
VOID       if any expected cell < 5
VOID       if |X^2 - crit| <= 1/1000            (threshold rounding band)
REJECT     if X^2 > crit + 1/1000               (independence falsified)
NOT-REJECT if X^2 < crit - 1/1000
```

`REJECT` on T1 is the only outcome that would make the cross an interesting
object rather than a null. Anything else is reported as a null and the note's
section 5 offer is answered "no coupling detected at this range and this
line".

Declared descriptive output, carrying **no** decision: the marginal counts of
`QUAD`, `SGN`, `H`, `QUART`; the smallest and largest carrier prime; the
exact rational value of each statistic; a decimal witness of each statistic
labelled as a witness.

## 3. Six preregistration fields

```text
equation:      sections 1.2 to 1.4 exactly as written, plus the Pearson
               statistic X^2 = sum (O - E)^2 / E with E = row*col/N as an
               exact rational.
code:          verify_jacobi_phase_cross.py in this directory, Python 3
               standard library only, no float in any gate or decision, no
               randomness, no external data, no file write.
carrier:       the 808 primes p = 1 mod 5 with 11 <= p <= 30000, generated
               by the verifier's own sieve.
systematics:   least primitive root convention for chi_p; r_p = min root;
               shortest-vector generator under 2a^2+2ab+3b^2; fold interval
               [0, L) with L = log phi; open quadrants only, boundary
               asserted impossible; thresholds as exact decimals with a
               1/1000 rounding band.
failure
threshold:     any exact gate FAIL, any boundary case, any expected cell < 5,
               or any statistic inside the rounding band voids the run.
               Thresholds never move; the carrier is never re-binned, split,
               or extended after the run.
action layer:  L5 only. No L6 measure, no Weil form, no RH statement, no
               physical reading, no registry, frontier, or Canon edit.
```

## 4. Out of scope, explicitly

- no claim about RH, its equivalences, or any zero of any L-function;
- no claim that `H` reproduces the origin note's `h`;
- no promotion of the selftest theorem check to a TWIST-J result: the
  modulus statement is Weil's theorem for the Fermat quintic, imported;
- no second carrier range, no second character convention, no re-run;
- no public probe under `probes/`, no branch claiming a `P-` identity.

## 5. Execution

```text
cd <repo root>
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 notes/C-JACOBI-PHASE-CROSS-1/verify_jacobi_phase_cross.py
```

This document and the verifier are committed together before the single
census execution. Their SHA-256 values are recorded in `SHA256SUMS`.
