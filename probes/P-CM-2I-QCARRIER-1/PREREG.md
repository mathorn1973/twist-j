# P-CM-2I-QCARRIER-1

Preregistration for the public probe P-CM-2I-QCARRIER-1: marked CM
twists of the registered integral 2I lift and the order-eight closure
of the arithmetic quarter-turn on the branch pair.

Owner: A. M. Thorn / mathorn1973 / Claude Fable 5 owner session.
Claim issue: #245, opened before this branch, path, pin, and any
formal execution. Base: public `main` commit
`a2198c477898963a815a09c34b8bb45c40d4a7b9` under Public Canon v30
(STATE ACTIVE, tag `canon-v30`, content commit
`857223fcd5e7bc8c8e68f1df768d6e8222b24ee0`, canon SHA-256
`2a32dcbd61ee7792fc2cb990b7f223e08876d71bf7ddcf5ec432acd055f3986a`,
157167 bytes, `canon/SHA256SUMS` 5 of 5 OK, tag and content commit
verified ancestors of `main`).

## 0. Collision and provenance guard

Before issue #245 the probe name was checked against open issues, pull
requests, remote branches, `probes/`, and the public registry and
frontier; no collision exists. The identifier fragment `QCARRIER`
denotes only the paired CM representation carrier of this probe. It is
not the decoder `QCarrier` type; exact `Q`, `QCarrier` equality,
Gram/dagger/transpose decoder data, the common total domain,
orbit-to-amplitude map, effects, Born pairing, `MatterData`, write map,
and dependencies remain owned by `QUADRATIC-DECODER-DATA [O]` and are
not imported. `COLOR-MEASURE-SELECTION [O]` remains STOP and untouched.
`SPIN-LIFT-FORCED [F]` is respected: nothing below selects or
uniquifies a marked lift.

Incubation provenance: the sealed bundles `notes/C-CM-2I-QCARRIER-1`
and `notes/C-CM-2I-QCARRIER-2` on `main`, hardened by the reviewed
pre-pin surface `notes/P-CM-2I-QCARRIER-1-PREP` (PR #244, commit
`873fec4`), whose static review was accepted by the owner.

DISCLOSURE: the incubation outputs were known before this pin. This
probe is therefore RESULT-EXPOSED and confirmatory, not prospective.
No threshold moves after the pin; a FAIL line is a fired falsifier and
is retained and merged.

## 1. Equation

Freeze the following data exactly.

- `K = Q(zeta)` with `zeta^4 + zeta^3 + zeta^2 + zeta + 1 = 0`,
  `O_K = Z[zeta]`, `tau(zeta) = zeta^2`, `sigma = tau^2`, and
  `F = K^sigma = Q(sqrt(5))`. Put
  `phi = -(zeta^2 + zeta^3) = (1 + sqrt(5))/2`, so
  `phi^-1 = phi - 1`. Here `dagger` is transpose followed by `sigma`
  and `N_K/F(x) = x sigma(x)`.
- `L0 = O_K^2`, `V0 = K tensor_(O_K) L0 = K^2`,
  `rho(S) = [[0,-1],[1,0]]`, and
  `rho(T) = [[zeta,1],[0,zeta^-1]]`; `G = <S,T>` is the abstract group
  marked by these two displayed matrices. The result is relative to
  this registered representative only. No uniqueness or selection of
  a marked 2I lift is part of the probe.
- `rho^a(g) = a(rho(g))` for `a` in `Gal(K/Q)`,
  `L = L0 (+) L0`, `V = V0 (+) V0`, and
  `Pi(g) = diag(rho(g), rho^tau(g))`, with the branch order fixed.
- `H0 = sum_(g in G) rho(g)^dagger rho(g)` on the single `rho` branch.
  The pair form used for transport is
  `H_pair = diag(H0, tau(H0))`; no uniqueness of all pair forms is
  asserted.
- A tau-semilinear structure is an invertible map
  `nu_B(v) = B tau(v)` with `B in GL4(K)` satisfying
  `nu_B Pi(g) = Pi(g) nu_B` for the two marked generators, hence for
  all `g in G`.

For `gamma in Gal(K/Q)`, marked twist-isomorphism means exactly the
existence of one `P_gamma in GL2(K)` satisfying

```text
P_gamma gamma(S) P_gamma^-1 = S,
P_gamma gamma(T) P_gamma^-1 = T.
```

Equality of unlabeled character multisets is not this equivalence.
Freeze

```text
q  = zeta - zeta^4 = 1 + 2 zeta + zeta^2 + zeta^3,
C0 = [[1,q],[-q,1]].
```

Pair-coordinate equivalence is semilinear conjugacy

```text
B' = A B tau(A)^-1,
A in Aut_G(V,Pi) = Z_GL4(K)(Pi(G))
  = {diag(r I2,s I2) : r,s in K^x},
```

and preserves the ordered pair and the displayed markings. Zero and
singular semilinear maps are outside the admitted class.

The frozen decisions are:

- **E1 (marked twist stabilizer, not descent).** The set of
  `a in Gal(K/Q)` for which `rho^a` is marked-twist-isomorphic to
  `rho` is exactly `{1,sigma}`. The coset `{tau,tau^3}` changes the
  marked trace of `T` from `phi^-1` to `-phi`. Thus `tau` exchanges the
  two golden trace values customarily attached to `5a` and `5b`; no
  identification of conjugacy classes or explicit outer automorphism
  is frozen. E1 asserts neither an `F`-form nor a sigma-semilinear
  involution.
- **E2 (pair and Hom data).** `rho` and `rho^tau` are absolutely
  irreducible and inequivalent; their endomorphism algebras are `K`.
  The ordered pair has Q-valued character. Its `K`-isomorphism class is
  Galois-stable by the exact pair intertwiners built from `C0`,
  `tau(C0)`, and `I2`; rationality alone is not used as descent data.
  This is not a Q-form or a coherent `C4` descent datum. In the block
  order used in E3, the four exact spaces are

  ```text
  Hom_G(rho^tau,rho)           = 0,
  Hom_G(rho^sigma,rho)         = K C0,
  End_G(rho^tau)               = K I2,
  Hom_G(rho^sigma,rho^tau)     = 0.
  ```
- **E3 (semilinear obstruction and attainable order).** With the
  primitive frozen intertwiner `C0 sigma(rho(g)) = rho(g) C0`, every
  admitted structure has

  ```text
  B = [[0, a C0], [d I2, 0]],       a,d in K^x.
  ```

  The representative cocycle is
  `mu0 = C0 sigma(C0) = -phi^2`, while rescaling replaces it by
  `N_K/F(a) mu0`; therefore its invariant norm class is
  `[-1] in F^x/N_K/F(K^x)`. Order four is impossible for every
  admitted structure. Order eight is achievable, and is the smallest
  attainable finite order, by `a = 1`, `d = phi`, for which
  `nu^4 = -I` and `nu^8 = I`. This does not say that every admitted
  `nu` has finite order or order eight. The order-eight map is a
  central tau-semilinear lift, not a `C4` Galois descent datum.
  (Notation note: the order-four condition may be written
  `N(d) = tau(mu^-1)` or `N(d) = tau^3(mu^-1)`; the two agree because
  `mu` lies in `F` and both `tau` and `tau^3` restrict to the
  nontrivial automorphism of `F`.)
- **E4 (single-branch Gram and transport).** The space of invariant
  sigma-Hermitian forms on the single `rho` branch is one `F`-line and
  contains the totally positive definite `H0`. For the explicit
  order-eight structure, the chosen `H_pair` obeys the balanced identity
  `B0^dagger H_pair B0 = phi^2 tau(H_pair)`. Thus the multiplier is the
  one totally positive scalar `phi^2`. No claim is made that all
  invariant forms on `V` form one line.

## 2. Code

The accepted verifier is `probes/P-CM-2I-QCARRIER-1/verify.py`, a
self-contained Python 3 standard-library program with exact rational
arithmetic, no randomness, floats, sampling, network, subprocess, or
filesystem write. It is adopted from the reviewed pre-pin candidate
`notes/P-CM-2I-QCARRIER-1-PREP/verify_draft.py` (PR #244, commit
`873fec4`) with only the header comment changed; its 19 gates audit:

1. the 120-element marked lift and marked twist-isomorphism facts;
2. the rational pair character and explicit Galois stability of its
   isomorphism class, without asserting a Q-form;
3. scalar centralizers, irreducibility, branch inequivalence, both
   vanishing diagonal Hom spaces, and the sigma-intertwiner line;
4. the complete antidiagonal tau-semilinear block classification;
5. `mu0 = -phi^2`, total negativity, norm-class invariance, and the
   universal order-four obstruction;
6. the explicit `d = phi` order-eight structure, equivariance, branch
   swap, and powers;
7. single-branch Gram existence, total positivity and line uniqueness;
8. exact balanced pair-Gram similitude.

The pin commit and file hashes are recorded in `RUN.md`.

## 3. Carrier and data

The only carrier is the exact synthetic ordered pair `O_K^2 (+) O_K^2`
with the displayed `S,T` matrices and their extension to `K`. There is
no external dataset. The coefficient arithmetic is `Z[zeta]` and its
fraction field. The label `QCARRIER` does not denote decoder
`QCarrier`. No public quadratic map `Q`, checkpoint, orbit, amplitude,
decoder domain, effect, schema, or write map is an input.

## 4. Systematics

- Group enumeration uses the fixed generator order `(S,T)` and exact
  tuple ordering only for deterministic presentation.
- Every nullspace and rank uses rational RREF with columns ordered by
  matrix position and the basis `(1,zeta,zeta^2,zeta^3)`.
- `C0` is the primitive integral vector selected by the first free
  column with positive first nonzero coefficient.
- Solvability at order eight uses the displayed witness `d = phi`.
  The impossibility of order four is the universal total-positivity
  proof, not a bounded search. No coefficient box is a proof premise.
- `H0` is the exact 120-term group average. Positivity is decided at
  both real embeddings by exact rational comparisons.

## 5. Failure threshold

Formal acceptance requires exit 0, empty stderr, and stdout
byte-identical to one committed `EXPECTED.txt` on both required
architectures. Any `FAIL` line fires the corresponding falsifier:

- **F-CM-1:** the marked twist-isomorphism-class stabilizer differs
  from `{1,sigma}` -- in particular, the frozen `C0` sigma-intertwiner
  fails or a marked intertwiner exists for `tau` or `tau^3`;
- **F-CM-2:** a nonzero diagonal block or another off-diagonal Hom
  direction in an equivariant tau-semilinear map;
- **F-CM-3:** an admitted order-four structure;
- **F-CM-4:** failure of the explicit order-eight structure;
- **F-CM-5:** a second `F`-line of invariant single-branch Hermitian
  forms or failure of total positivity/Gram transport.

No numeric tolerance exists. A hash, byte, runtime, or implementation
failure is an integrity STOP unless it supplies an exact witnessed
negation of a frozen equation. A scientific falsifier fires only on
such an exact witness, and a fired falsifier is retained and merged.

## 6. Action layer

L4 support only: a fixed algebraic carrier, marked group action,
twist compatibility, semilinear central lift, obstruction class, and
invariant form. There is no L1 checkpoint input, L5 stream, L6
measure, cross-layer lift, SI value, physical U(1), decoder
completion, orbit-to-amplitude bridge, or `MatterData` write.
`QUADRATIC-DECODER-DATA` and `COLOR-MEASURE-SELECTION` remain
untouched STOP rows.

## 7. Proof

### 7.1 Fixed relative setting

Let `K = Q(zeta5)`, `tau(zeta5) = zeta5^2`, `sigma = tau^2`, and
`F = K^sigma = Q(sqrt(5))`. Let `rho` be the marked representation
generated by the displayed `S`, `T`. Exact closure gives 120
determinant-one matrices. Everything below is relative to this
representative. `SPIN-LIFT-FORCED [F]` forbids reading the argument as
uniqueness or canonical selection of a marked lift.

Write `rho^a(g) = a(rho(g))`. The marked trace of `T` is `phi^-1`;
`sigma` fixes it, while `tau` and `tau^3` send the two golden trace
values into one another. All traces of `rho` lie in `F`. The explicit
intertwiner below proves `rho^sigma ~= rho`; the changed labeled trace
proves `rho^tau` and `rho^(tau^3)` are not marked-twist-isomorphic to
`rho`. Hence the marked twist-isomorphism stabilizer is exactly
`{1,sigma}`. This is not a descent subgroup: section 7.4 proves that
the sigma-intertwiner cannot be normalized to square to one. The
character sum `chi_rho + tau(chi_rho)` is rational on every group
element, so the ordered branch pair has rational character. Its
Galois-stable `K`-isomorphism class is certified separately by the
explicit pair intertwiners in section 7.3. Rational character does not
by itself produce a Q-form or coherent C4 datum.

### 7.2 Irreducibility and the required Hom spaces

Over characteristic zero the finite-group representations are
semisimple. Exact rational linear systems for an unknown `2 x 2`
matrix over `K` give the following nullities:

```text
Hom_G(rho,rho)                 4 over Q = 1 over K,
Hom_G(rho^tau,rho^tau)         4 over Q = 1 over K,
Hom_G(rho^tau,rho)             0,
Hom_G(rho^sigma,rho)           4 over Q = 1 over K,
Hom_G(rho^sigma,rho^tau)       0.
```

The four matrices `I2,S,T,ST` span `M2(K)` on each branch. Together
with the scalar centralizers and semisimplicity, this proves absolute
irreducibility. The zero Hom spaces prove branch inequivalence and the
two diagonal vanishings needed below. A primitive generator of the
non-scalar intertwiner line is

```text
q  = zeta5 - zeta5^4 = 1 + 2 zeta5 + zeta5^2 + zeta5^3,
C0 = [[1,q],[-q,1]].
```

Direct multiplication gives

```text
C0 sigma(rho(g)) = rho(g) C0       for g = S,T,
det(C0) != 0,
C0 sigma(C0) = -phi^2 I2.
```

The generator equations imply the equation for every group element.

### 7.3 Complete tau-semilinear block form

On `V = K^2 (+) K^2` put `Pi = rho (+) rho^tau`. Write an admitted map
as `nu = B tau` and decompose `B = [[B11,B12],[B21,B22]]`.
Equivariance is

```text
B tau(Pi(g)) = Pi(g) B.
```

Its four blocks lie respectively in

```text
Hom_G(rho^tau,rho),
Hom_G(rho^sigma,rho),
End_G(rho^tau),
Hom_G(rho^sigma,rho^tau).
```

The Hom calculation therefore forces, and exhausts,

```text
B = [[0,a C0],[d I2,0]],            a,d in K.
```

Invertibility is equivalent to `a,d != 0`. Thus no zero map or
singular map enters the order decision, and no semilinear structure
outside the antidiagonal Schur form is omitted.

For completeness, Galois stability of the pair is witnessed directly.
Intertwiners from the indicated twist back to `Pi` may be chosen as

```text
P_tau     = [[0,C0],[I2,0]],
P_sigma   = diag(C0,tau(C0)),
P_tau^3   = [[0,I2],[tau(C0),0]].
```

Each is invertible and satisfies
`P_gamma gamma(Pi(g)) = Pi(g) P_gamma` for `g = S,T`. These separate
isomorphisms are not asserted to obey a descent cocycle.

### 7.4 Cocycle class and the universal order-four obstruction

For `C = a C0`,

```text
mu(a) = C sigma(C) = N_K/F(a) (-phi^2) I2.
```

Consequently the class of its scalar in `F^x/N_K/F(K^x)` is always
`[-1]`. This is also invariant under the declared `G`-equivariant
semilinear coordinate conjugacy, which changes the representative only
by norm factors.

In particular, a sigma-semilinear involution on the single branch
would require rescaling `C` so that `C sigma(C) = I`. The same
total-negativity argument below forbids that normalization. Thus the
twist isomorphism at `sigma` does not supply an `F`-descent datum.

Let `N(d) = d sigma(d)`. Fourfold composition gives

```text
nu^4 = diag(mu(a) tau(N(d)), N(d) tau(mu(a))).
```

If `nu^4 = I`, then necessarily

```text
N(d) = tau(mu(a)^-1).
```

At each real place of `F`, every nonzero CM norm from `K` is a squared
complex modulus and is strictly positive. The scalar `mu(a)` is
totally negative because `-phi^2` is totally negative and `N(a)` is
totally positive. Its inverse and its `tau` conjugate are therefore
totally negative. The displayed norm equation has no solution. This is
a universal sign proof; a finite coefficient search is neither used
nor needed.

### 7.5 Exact order eight and minimality

Take `a = 1` and `d = phi`. Because `phi` lies in `F`,
`N_K/F(phi) = phi^2`. Substitution in the fourfold formula gives

```text
nu^4 = -I4,
nu^8 = I4.
```

The map is equivariant by the block equations and is invertible. Its
semilinear twist is `tau`, of order four, so an identity power must be
a multiple of four. Order four has just been excluded and order eight
is exhibited; hence eight is the smallest attainable finite order.
This proves attainability and minimality, not that every admitted map
has finite order. The witness is a central tau-semilinear lift of
order eight, not a coherent `C4` Galois descent datum.

### 7.6 The single-branch Gram statement

Define

```text
H0 = sum_(g in G) rho(g)^dagger rho(g).
```

It is sigma-Hermitian and invariant by reindexing the finite group. At
either real place of `F`, extended to a complex embedding of `K`,
`v^* H0 v = sum_g ||rho(g)v||^2 > 0` for `v != 0`; hence `H0` is
totally positive definite. The exact diagonal and determinant sign
tests audit the same statement.

Let `H` be any invariant sigma-Hermitian form and put
`A = H0^-1 H`. The two invariance equations imply
`A rho(g) = rho(g) A` for every `g`. The scalar-centralizer result in
section 7.2 gives `A = lambda I2` with `lambda in K`. Since both `H`
and `H0` are sigma-Hermitian, `lambda = sigma(lambda)`, hence
`lambda in F`. This proves intrinsically that the invariant forms are
exactly the single line `F H0`. The verifier's eight-parameter
invariance system supplies a separate audit: it has rational rank six,
so its kernel has dimension two over `Q`, exactly the dimension of
`F H0`.

For the pair use the chosen form `H_pair = diag(H0,tau(H0))`. With
`B = [[0,C0],[phi I2,0]]`, exact multiplication yields the declared
balanced identity

```text
B^dagger H_pair B = phi^2 tau(H_pair).
```

Indeed `C0^dagger H0 C0 = phi^2 sigma(H0)` and `N_K/F(phi) = phi^2`.
Thus the single common multiplier is totally positive. The argument
does not claim that the whole space of invariant pair forms is
one-dimensional.

Review addendum (accepted): the scalar in
`C0^dagger H0 C0 = kappa sigma(H0)` is forced, not merely computed.
Taking determinants gives `kappa^2 = N_K/F(det C0) = phi^4`, and
positive definiteness of both sides selects the positive root
`kappa = phi^2`. The balanced identity therefore cannot fail at the
formal run unless a frozen equation fails first.

### 7.7 Status and layer boundary

The universal conclusions above are pure L4 algebra relative to one
registered lift. A theorem status would require acceptance of this
proof independently of the future computation; the verifier then
audits exact certificates. Two-architecture agreement alone can earn
at most `C`. No statement here defines decoder `Q`, a `QCarrier`, an
orbit-to-amplitude map, `MatterData`, a measure, U(1), or a physical
selection, and no public registry row moves.

## 8. Decision and status discipline

The probe closes positively when the pinned verifier exits 0 with
empty stderr and stdout byte-identical to the committed `EXPECTED.txt`
on both required architectures, auditing E1-E4. It closes negatively
if a named falsifier F-CM-1 through F-CM-5 fires; the fired record is
merged, not hidden. It is an integrity STOP on any hash, byte, or
environment mismatch that does not witness an exact negation.

Status discipline: the two-architecture computation gate supports at
most `C` for the audited finite identities. `T` for E1-E4 requires
owner acceptance of the section 7 proof as an independent derivation,
with the verifier as its audit. No registry, frontier, or Canon file
is changed by this probe's pull request; any registration is a later,
separately sealed fold. PROMO deferred.
