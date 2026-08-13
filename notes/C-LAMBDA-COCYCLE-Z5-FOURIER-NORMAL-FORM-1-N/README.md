# C-LAMBDA-COCYCLE-Z5-FOURIER-NORMAL-FORM-1-N

```text
STATUS:       NON-CANONICAL INCUBATION NOTE
AUTHORITY:    none
PUBLIC BASIS: Public Canon v46, mathorn1973/twist-j main
ISSUE LOCK:   #363
LAYER:        L6 measure/spectral only; no other L1-L6 lift
COMPUTATION:  none; the result is proof-first
PROMOTION:    none
```

This package records one exact `Z_5` Fourier normal form for the public
lambda-cocycle grid and one proof-level attack on its conductor tail. It
creates no public claim, Registry row, evidence, probe permission, or status
change. RH remains open and `LAMBDA-COCYCLE-ANGLES [H]` remains unchanged.

The owner proposed Toeplitz and 5-adic continuity attacks before issue #363
was opened. The session had also identified the possible finite-profile
obstruction. This is exposed preparation, not preregistered evidence. The
package re-derives the statements and records the resulting no-go openly.

The new result of the attack is in [ATTACK.md](ATTACK.md).

## 1. Public basis and collision boundary

At the lock, `STATUS.md` declared:

```text
STATE:          ACTIVE
CANON:          Public Canon v46
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v46
CONTENT_COMMIT: 62628ca4da2d938e4e3a122d35c0d93a6debc27f
CANON_SHA256:   6c57e714c441bd679b9f6c673352cfae44ac993433d7c4624cd9c3c93df291ff
CANON_BYTES:    222760
main snapshot:  6545c1d0de61ff4696eb3de1a258139e8891f436
```

The tag resolves to the displayed activation commit, the content commit is
its ancestor, the Canon hash and byte count agree, and the policy, Canon, and
ledger checks pass.

The following content already exists and is not counted again here.

[PUBLIC T] `LAMBDA-COCYCLE-BRANCH-COLLAPSE` gives the Cayley spectral measure,
the exact residual identity, its pointwise bounds, and the localization of a
failed tail limit to one ordinate.

[PUBLIC T] `LAMBDA-COCYCLE-GRID-EQUIVALENCE` proves that the point spectrum of
the public `U_J` carrier is exactly

```text
2 pi (1/4) Z[1/5],
```

equivalently the circle grid

```text
G = union_(A>=0) {z : z^(4*5^A)=1},
```

and proves the registered cocycle-vector equivalence.

[PUBLIC H] `LAMBDA-COCYCLE-ANGLES` remains the statement that a cocycle vector
exists, equivalently that RH holds and every Cayley angle lies on this grid.

[NON-CANONICAL PREDECESSORS]

- `notes/j-li-schoenberg-2/README.md` records the already known
  `J-LI-TOEPLITZ-EQUIVALENCE` and its Herglotz normal form;
- `notes/j-li-schoenberg-2/ATOM_TEST.md`, `FEJER_SCALING.md`, and
  `CYCLIC_CARRIER_DIMENSION.md` record the atom, averaged-tail, and
  finite-support boundaries;
- `notes/C-LI-COCYCLE-1/C-LI-COCYCLE-1.md` records the parallel cocycle
  formulation;
- `probes/P-LAMBDA-COCYCLE-ANGLES-1/` and
  `probes/P-LAMBDA-COCYCLE-ANGLES-2/` are the sealed public evidence for the
  current theorem rows.

[CORRECTION BOUNDARY] Issue #293 and its v39 correction withdrew an earlier
general finite-profile nonfalsifiability sentence. The sealed predecessor had
proved only the pointwise residual bounds, not that every compatible finite
profile has a grid-supported realization. Public Canon v46 correctly makes no
such general claim. The strict-positive finite-profile theorem proved in
`ATTACK.md` is the missing theorem, with its exact hypothesis and boundary.

The new delta here is only:

1. the exact `Z_5` Fourier extension criterion;
2. the exact conductor-tail extractor and modulus comparison;
3. the strict-positive finite-profile grid-realization theorem and its
   arbitrary-slow-tail no-go.

## 2. Frozen abstract object

Let `t=(t_n)_(n in Z)` be a positive-definite sequence with

```text
t_(-n) = conjugate(t_n),
t_0    = M.
```

By Herglotz, it has one finite positive representing measure `sigma` on the
unit circle:

```text
t_n = integral_T z^n d sigma(z).
```

Define

```text
F(m) = t_(4m),                         m in Z,
G_A  = {z in T : z^(4*5^A)=1},
G    = union_(A>=0) G_A,
nu   = (z -> z^4)_* sigma,
R_A  = sigma(T minus G_A)
     = nu(T minus mu_(5^A)).
```

The factor `4` is not suppressed: it is the residue-order part of the public
grid. A measure is said to be **carried by** `G` when `sigma(T minus G)=0`.
This does not mean that its topological support is a subset of `G`; a dense
atomic measure can have the whole circle as its topological support.

## 3. Z5 Fourier extension theorem

[NON-CANONICAL candidate-T, classical harmonic analysis packaged at the
public grid]

The following are equivalent:

```text
E1  F is uniformly continuous on Z for the 5-adic metric.

E2  F has a unique continuous positive-definite extension F_tilde to Z_5.

E3  sigma is carried by G.

E4  R_A -> 0.
```

When these conditions hold, the extension has the unique uniformly
convergent Fourier expansion

```text
F_tilde(x)
  = sum_(chi in mu_(5^infinity)) a_chi chi(x),

a_chi >= 0,
sum_chi a_chi = M,
a_chi = nu({chi}).
```

### Proof

The sequence `F(m)=t_(4m)` is the Fourier transform of the pushforward
`nu=(z -> z^4)_* sigma`. If `F` extends continuously and positively
definitely to the compact group `Z_5`, Bochner's theorem represents the
extension by a positive measure on the discrete dual

```text
dual(Z_5) = mu_(5^infinity).
```

Such a measure is an absolutely summable nonnegative family `a_chi`.
Restricting to the dense subgroup `Z` gives all Fourier coefficients of
`nu`. Uniqueness of finite circle measures from all Fourier coefficients
therefore identifies `nu` with this atomic dual measure. Hence `nu` is carried
by `mu_(5^infinity)`.

Conversely, if `nu` is carried by `mu_(5^infinity)`, the displayed series is
absolutely and uniformly convergent on `Z_5`, is positive definite, and
restricts to `F` on `Z`.

Finally,

```text
(z -> z^4)^(-1)(mu_(5^infinity)) = G,
```

so the pushforward condition is equivalent to `sigma(T minus G)=0`.
Because the complements of the finite sets `G_A` decrease to `T minus G`,
continuity from above for the finite measure gives

```text
R_A -> sigma(T minus G).
```

This proves `E2 <=> E3 <=> E4`. A uniformly continuous function on the dense
subgroup `Z` extends uniquely to the completion `Z_5`; positive definiteness
passes to limits. This proves `E1 <=> E2`.

## 4. Exact conductor-tail identities

[NON-CANONICAL candidate-T]

Define the low-conductor truncation

```text
F_(<=A)(x)
  = sum_(chi^(5^A)=1) a_chi chi(x).
```

Then

```text
||F_tilde-F_(<=A)||_infinity = R_A.
```

The upper bound is the triangle inequality. Equality holds at `x=0`, where
every character equals one.

Let `dh_A` be normalized Haar measure on the subgroup `5^A Z_5`. Character
orthogonality gives

```text
R_A
  = M - integral_(5^A Z_5) Re F_tilde(h) dh_A.
```

Equivalently, using only the integer moments,

```text
R_A
  = M - limit_(K->infinity)
      (1/K) sum_(m=0)^(K-1) t_(4*5^A*m).
```

Indeed, the Cesaro average of `chi^(5^A m)` is one for
`chi^(5^A)=1` and tends to zero otherwise; dominated convergence applies to
the summable family `a_chi`.

Define the 5-adic congruence modulus

```text
delta_A
  = sup {|t_(4m)-t_(4m')| : m=m' mod 5^A}.
```

Then

```text
R_A <= delta_A <= 2 R_A.
```

For the upper bound, every character of conductor at most `5^A` agrees on
one congruence class, so only the tail contributes. For the lower bound,
integer multiples of `5^A` are dense in `5^A Z_5`; hence

```text
delta_A
  >= sup_(h in 5^A Z_5) |M-F_tilde(h)|
  >= integral_(5^A Z_5) (M-Re F_tilde(h)) dh_A
  = R_A.
```

Thus an effective conductor-tail estimate and an effective 5-adic modulus of
continuity are equivalent up to the universal factor two. This factor is
sharp: for `B>=1`, a single tail atom whose pushforward has order `5^(A+B)` gives
`delta_A/R_A = 2 cos(pi/(2*5^B))`, which tends to two as `B` tends to
infinity.

## 5. Li-cocycle specialization

Freeze

```text
lambda_0 = 0,
t_0      = 2 lambda_1,
t_(-n)   = t_n,
t_n      = lambda_(n+1)+lambda_(n-1)-2 lambda_n,  n>=1,
M        = t_0.
```

Inside the public cocycle class, RH follows from Li positivity and the
Herglotz measure is the Cayley measure

```text
sigma
  = sum_(gamma>0)
      (delta_(exp(i alpha_gamma))+delta_(exp(-i alpha_gamma)))
      /(1/4+gamma^2),

alpha_gamma = 2 arctan(1/(2 gamma)).
```

The positive ordinates are counted with multiplicity.

Consequently the public grid condition is exactly `E3`, and hence exactly
the existence of the continuous positive-definite extension in `E2`.

The extension theorem is a normal form, not progress on RH. It translates
the stronger public hypothesis into a statement about one continuous
positive-definite function on `Z_5`.

## 6. Decision boundary

The attack in `ATTACK.md` proves that no fixed strict-positive finite moment
profile can give a nontrivial conductor-tail bound. It does not say that an
indefinite or singular finite Toeplitz block is harmless, and it does not
construct one all-index cocycle vector.

The surviving global targets are

```text
delta_A -> 0
```

or, equivalently,

```text
M - limit_(K->infinity)
      (1/K) sum_(m=0)^(K-1) t_(4*5^A*m)
  -> 0.
```

Any effective attack must control infinitely many moments, a complete
arithmetic average, or one exact ordinate. A finite numerical enclosure of a
dense grid cannot decide membership.

## 7. Sources and status firewall

The harmonic-analysis inputs are the classical Herglotz theorem for positive
definite sequences, Bochner duality for compact abelian groups, character
orthogonality on `Z_5`, Fejer-Riesz factorization, and Caratheodory convexity.
The needed instances and hypotheses are proved or reduced explicitly in this
package; no untyped appeal to a carrier is made.

Repository source boundaries:

- `canon/REGISTRY.tsv`, rows `LAMBDA-COCYCLE-ANGLES`,
  `LAMBDA-COCYCLE-BRANCH-COLLAPSE`, and
  `LAMBDA-COCYCLE-GRID-EQUIVALENCE`;
- `probes/P-LAMBDA-COCYCLE-ANGLES-1/{PREREG.md,RESULT.md}`;
- `probes/P-LAMBDA-COCYCLE-ANGLES-2/{PREREG.md,RESULT.md}`;
- `notes/j-li-schoenberg-2/README.md` and the boundary files named in
  section 1;
- issue #293 and merged PR #294 for the withdrawn overclaim and controlling
  corrected public scope.

No RH/GRH evidence or status movement, no Canon/Registry/frontier edit, no
physical/Born/decoder reading, no new `J`-native carrier, no role for
`zeta_8`, and no L1-L5 claim follow from this package.
