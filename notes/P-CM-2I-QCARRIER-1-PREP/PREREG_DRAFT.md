# PREREG pre-pin draft for P-CM-2I-QCARRIER-1

NON-CANONICAL PRE-PIN DRAFT. This is not `probes/.../PREREG.md`, does
not claim the probe identifier in a public issue, and authorizes no
formal execution. It hardens the proposal recorded in
`notes/C-CM-2I-QCARRIER-2` while preserving both incubation bundles.

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

Pair-coordinate
equivalence is semilinear conjugacy

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
- **E4 (single-branch Gram and transport).** The space of invariant
  sigma-Hermitian forms on the single `rho` branch is one `F`-line and
  contains the totally positive definite `H0`. For the explicit
  order-eight structure, the chosen `H_pair` obeys the balanced identity
  `B0^dagger H_pair B0 = phi^2 tau(H_pair)`. Thus the multiplier is the
  one totally positive scalar `phi^2`. No claim is made that all
  invariant forms on `V` form one line.

The future probe closes positively only if the independent proof
certificate establishes E1-E4 and the pinned verifier audits every
finite identity byte-identically on both required architectures. It
closes negatively if a named falsifier fires. It remains STOP if the
tuple, markings, equivalence, admitted map class, proof, or verifier is
not frozen exactly. A later Canon fold alone can assign public status.

## 2. Code

The accepted future `verify.py` must be a fresh, self-contained Python
3.12 standard-library program with exact rational arithmetic, no
randomness, floats, sampling, network, subprocess, or filesystem write.
It must audit:

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
8. exact balanced pair-Gram similitude, including equality of the two
   block multipliers.

`verify_draft.py` is only a code-review candidate. Its gate names,
byte output, byte count, and SHA-256 are not pins and must be regenerated
only after owner acceptance on the formal branch.

## 3. Carrier / data

The only carrier is the exact synthetic ordered pair `O_K^2 (+) O_K^2`
with the displayed `S,T` matrices and their extension to `K`. There is
no external dataset. The coefficient arithmetic is `Z[zeta]` and its
fraction field. The label `QCARRIER` does not denote decoder `QCarrier`.
No public quadratic map `Q`, checkpoint, orbit, amplitude, decoder
domain, effect, schema, or write map is an input.

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
invariant form. There is no
L1 checkpoint input, L5 stream, L6 measure, cross-layer lift, SI value,
physical U(1), decoder completion, orbit-to-amplitude bridge, or
`MatterData` write. `QUADRATIC-DECODER-DATA` and
`COLOR-MEASURE-SELECTION` remain untouched STOP rows.

The two incubation bundles exposed positive outputs before this draft.
Any later formal probe is therefore result-exposed and confirmatory,
not prospective; its preregistration must disclose that fact.
