# C-JACOBI-PHASE-CROSS-1. The phase avatar is exactly on the critical circle; the cross to the modulus avatar is null at 3 x 10^4

**NON-CANONICAL.** Incubation lane (`notes/`). This document registers no
claim, edits no Canon file, and earns no public status. Public Canon v26,
tag `canon-v26`, content commit
`138eec5b22a823469e1fa651505815a3d5b36761`, is read-only context.

```text
CANDIDATE:   C-JACOBI-PHASE-CROSS-1
DATE:        2026-08-23
ORIGIN:      NADHLED note of 2026-08-22 (non-canonical, parallel session),
             section 5: "mikro-selftest", then "C-JACOBI-PHASE-CROSS-1"
PIN:         2841517ab1df229bbdd98b7e879af18d766b78e5
LAYER:       L5 finite exact statements. No lift, no measure, no reading.
```

## 1. What was asked and what was done

The origin note proposes that a split prime `p = 1 mod 5` carries two
integer avatars in `Z[zeta_5]`, polar-orthogonal to each other, and that
their joint law is the one object worth measuring:

```text
w_p   modulus avatar   generator of a prime of Z[phi] above p;
                       carries the rapidity eta_p, phase content trivial
J_p   phase avatar     quintic Jacobi sum; all four Galois embeddings have
                       modulus exactly sqrt(p), so the rapidity is zero
```

Two pieces of work, in the order the note asks for them:

1. **Micro-selftest.** Exact verification, in `Z[zeta_5]`, that the phase
   avatar's rapidity vector is exactly the zero vector.
2. **Census C-JACOBI-PHASE-CROSS-1.** All 808 primes `p = 1 mod 5` with
   `11 <= p <= 30000`, joint contingency table of the angular datum of
   `J_p` against the rapidity datum of `w_p`, chi-square line frozen before
   the table was computed.

## 2. Micro-selftest: PASS, and it is stronger than the note states

`verify_jacobi_selftest.py`, stdout in `stdout_jacobi_selftest.txt`, all
gates PASS on 26 primes from 11 to 29921.

The note asks for "rapidity of `J_p` = zero vector" as a self-test of a
phase engine. The check does not need four modulus computations. It is one
exact identity in the ring:

```text
S1     J_p * conj(J_p) = p          exactly in Z[zeta_5]
```

Because `Gal(Q(zeta_5)/Q)` is abelian, conjugation commutes with every
`sigma_a`, so S1 applied under `sigma_a` gives
`sigma_a(J_p) * conj(sigma_a(J_p)) = p`, that is
`|sigma_a(J_p)|^2 = p` for all four embeddings simultaneously. The rapidity
vector

```text
eta_a(J_p) = (1/2) log( |sigma_a(J_p)|^2 / p ) = (1/2) log 1 = 0
```

is therefore the zero vector for a reason that never leaves integer
arithmetic. No floating point is used anywhere in the gate. Gate S3
nevertheless checks all four embeddings separately, so the implication is
audited and not merely asserted.

Other gates, all PASS:

```text
S0d  the axiom J = 1 + zeta^2 has N(J) = 1, |J| = 1/phi, arg J = 2 pi/5
S2   N(J_p) = p^2
S4   J(chi^a, chi^a) = sigma_a(J(chi, chi))   -- the character choice acts
     by Galois, so the *modulus* statement is convention free but the
     *angle* is not; this is why the census had to freeze a convention
S5   J_p = -1 mod (1 - zeta)^2
S6   the modulus avatar w_p is never on the critical circle
S7   4 |sigma_a J_p|^2 = 4p re-derived through the exact Re/Im machinery,
     with 3 - phi = |1 - zeta|^2, the same constant the Canon carries in
     GRAVITY-BRIDGE-LAW
```

S7 matters procedurally: the census needs signs of `Re` and `Im` in the
principal embedding, and S7 audits that machinery against a quantity whose
value is known exactly in advance.

The imported content is Weil's theorem for the Fermat quintic (`|J| =
sqrt p`); the exact arithmetic is a reproduction of it, not a TWIST-J
result. The selftest earns its place as an anchor for any future phase
engine, exactly as the note proposes.

## 3. Census: three frozen tests, three nulls

`verify_jacobi_phase_cross.py`, stdout in
`stdout_jacobi_phase_cross.txt`. Exact gates G1-G12 PASS on all 808
carrier primes. Frozen definitions and thresholds are in
`PREREG_C-JACOBI-PHASE-CROSS-1.md`, committed before the run.

```text
test  table                 df   X^2 (exact)   crit     decision
T1    QUAD(J_p) x H(w_p)     3    3.162197     11.345   NOT-REJECTED
T2    SGN(J_p)  x H(w_p)     2    0.105260      9.210   NOT-REJECTED
T3    QUAD(J_p) x QUART(w_p) 9   10.185963     21.666   NOT-REJECTED
```

`QUAD` is the quadrant of `sigma_1(J_p)`; `SGN` is the Galois-invariant,
character-convention-free sign pair
`{sign Re sigma_1 J_p, sign Re sigma_2 J_p}`; `H` and `QUART` are the fold
half and fold quartile of `eta_p` in `[0, L)`, `L = log phi`. Every bin
boundary is an exact `Z[phi]` comparison; the chi-square statistics are
exact rationals compared against frozen exact decimals.

**Conclusion at the frozen line:** at this carrier and this resolution, the
angular datum of the phase avatar and the rapidity datum of the modulus
avatar are statistically independent. T2 in particular is convention free
and is as null as a table can be (`X^2 = 0.105` against a `9.210` line).
The cross does not couple.

That is the answer to the note's section 5: the pairing exists as a
construction, it is exactly computable, and it carries no measurable
correlation at `3 x 10^4`. Nothing here moves the wall.

## 4. One descriptive observation, explicitly not a decision

The preregistration declared the marginal counts descriptive and attached
no threshold to them. Reported as such, with no status:

```text
QUAD    QI 224   QII 205   QIII 192   QIV 187          (n = 808)
SGN     (+,+) 193   mixed 407   (-,-) 208
H       h=0 366   h=1 442
QUART   k=0 155   k=1 211   k=2 202   k=3 240
```

The rapidity marginals are not flat. Unpreregistered uniformity statistics,
for orientation only: `H` gives `7.15` on `df 1`, `QUART` gives `18.49` on
`df 3`. Both would clear a 0.01 line that was never frozen, on statistics
that were chosen after seeing the table. They are therefore not findings.

The diagnostic that does matter is exact and convention-theoretic. The two
primes above `p` are conjugate, and conjugation sends `eta_p` to
`L - eta_p`; the preregistration broke the tie by `r_p = min` root of
`x^2 - x - 1 mod p`. Folding the quartiles into the conjugation-invariant
pairing removes the whole effect:

```text
{k = 0 or 3}  395      {k = 1 or 2}  413      X^2 = 0.401 on df 1
```

So the entire marginal skew lives in the `r_p = min` tie-break and none of
it survives conjugation folding. The convention-free content of the
rapidity marginal is flat. Whether "the smaller root systematically sits in
the upper fold half" is an arithmetic fact or a finite-size artifact is a
well-posed question, and it is the only thing this run turned up that
deserves its own preregistration.

## 5. Scope, honestly

- No claim about RH, about zeros of any L-function, or about Weil
  positivity is made or implied. The note's section 3 layering is not
  tested here in any direction.
- The exact modulus statement is Weil's theorem, imported. This run
  reproduces it in `Z[zeta_5]`; it does not strengthen it.
- `H` is this session's **reconstruction** of the note's "half-class h".
  No definition of `h`, `w_p`, or `eta_p` exists anywhere in this
  repository at Public Canon v26; the reconstruction is stated in full in
  the preregistration, section 1.4. If the originating session used a
  different `h`, T1 and T3 must be recomputed. T2's null is unaffected in
  its angular half but shares the same `H`.
- Single platform, `arm64`, non-formal. No two-architecture gate. Under
  `POLICY.md` a one-architecture finite result is at most `C`, and this one
  is not even a public probe; it is `notes/` material.

## 6. Offered continuations, none started

```text
1  preregister the conjugation tie-break question directly: does
   r_p = min correlate with the fold half of eta_p, carrier to 10^6,
   threshold frozen, both tie-breaks reported
2  extend the cross carrier to 10^6 with the same frozen T1/T2/T3 lines;
   a null there is a much sharper null, and costs only compute
3  ask the originating session for the exact construction of its h, w_p
   and eta_p, and re-run T1/T3 against it before anything is compared
```

Nothing in this directory is proposed for promotion.

## 7. Files

```text
PREREG_C-JACOBI-PHASE-CROSS-1.md   frozen decision surface, committed first
verify_jacobi_selftest.py          micro-selftest, exact
stdout_jacobi_selftest.txt         its stdout
verify_jacobi_phase_cross.py       census, exact gates and exact chi-square
stdout_jacobi_phase_cross.txt      its stdout
RUN.md                             pins, environment, hashes, disclosures
SHA256SUMS                         hashes of the files above
```
