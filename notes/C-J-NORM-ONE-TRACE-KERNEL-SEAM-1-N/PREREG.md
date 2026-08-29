# C-J-NORM-ONE-TRACE-KERNEL-SEAM-1-N

**Status:** NON-CANONICAL incubation. No authority. No Canon or Registry effect.

**Target line:** PUBLIC.

**Owner:** ChatGPT owner session, 2026-08-29.

**Issue lock:** #659.

**Action layer:** L1 exact algebra only.

**Formal probe:** none. This directory is an incubation note under `notes/`.

## 1. Authority basis

Public Canon v71 is ACTIVE on `mathorn1973/twist-j main`.

```text
TAG:               canon-v71
CONTENT_COMMIT:    a77d720433c19976f9ab663d023ec9364eac34eb
ACTIVATION_COMMIT: 39e61fbfe794b0d3d3ab2a28ba9f960c13f4fe7f
CANON_SHA256:      0306abb2e7f855ceb4fcbfdf14265a9d2c5c8bd23b35868b74a92aae16b5e279
CANON_BYTES:       369836
```

The tag, release manifest, normative hashes and required checks were read back before issue lock. The branch starts at the activation commit above.

Public Canon v71 keeps `J` primitive, treats the rest of the architecture as separately declared, and does not require a unique global decoder. This incubation may not strengthen those boundaries.

## 2. Motivation

Formalize the intuition:

> Unity is counted inward, not outward.

The phrase has no scientific status. The exact question is whether the public norm-one and trace-kernel structures meet through a theorem-grade algebraic seam.

The proposed mathematical reading is:

```text
multiplicative unity:  total norm fixed at 1,
internal variation:    relative coordinates vary inside ker(N),
infinitesimal form:    first-order variation lies in ker(Tr).
```

## 3. Frozen carrier

Let

```text
K   = Q(j),
j   = zeta_5,
j^5 = 1,
j != 1,
O_K = Z[j],
J   = 1 + j^2.
```

For every finite separable extension `E/Q`, define

```text
T_E^1 := ker(N_E/Q : Res_E/Q G_m -> G_m).
```

For the `K` specialization use the ordered integral basis

```text
B = (j, j^2, j^3, j^4).
```

Define the integral trace-zero lattice

```text
Lambda_rel := {x in O_K : Tr_K/Q(x) = 0}.
```

No physical meaning is assigned to `T_K^1`, `Lie(T_K^1)`, `Lambda_rel`, or their reductions.

## 4. Frozen positive clauses

### G1. Norm derivative and tangent kernel

For every finite separable extension `E/Q` of degree `n`, prove

```text
d(N_E/Q)_1 = Tr_E/Q,
Lie(T_E^1)  = ker(Tr_E/Q),
dim T_E^1   = n - 1.
```

The proof must include the dual-number identity

```text
N_E/Q(1 + eps x) = 1 + eps Tr_E/Q(x),
eps^2 = 0.
```

### G2. Split coordinates

After base change to a splitting field and after ordering the embeddings `sigma_1,...,sigma_n`, prove

```text
T_E^1 = {(x_1,...,x_n) in G_m^n : product_i x_i = 1}
      ~= G_m^(n-1).
```

The chart is permitted only after an embedding order is declared. No canonical orientation over `Q` follows from the chart.

### G3. Integral trace seam in Q(zeta_5)

Prove:

```text
B = (j,j^2,j^3,j^4) is a Z-basis of O_K,
Tr_K/Q(j^a) = -1 for a=1,2,3,4.
```

Hence, for `x = sum_(a=1)^4 x_a j^a`,

```text
Tr_K/Q(x) = -sum_a x_a,
Lambda_rel ~= {(x_1,x_2,x_3,x_4) in Z^4 : sum_a x_a = 0}.
```

Prove the exact reduction statement

```text
Lambda_rel / 5 Lambda_rel
 ~= ker(sum : F_5^4 -> F_5).
```

The comparison with public `TRACEKERNEL-RESIDUAL-FORM` is by exact carrier content only. It is not a new dependency or a lift beyond L1.

### G4. Real form and dimension/rank separation

Using the two complex places of `K`, prove the Lie-group isomorphism

```text
T_K^1(R)
 ~= {(z_1,z_2) in C^* x C^* : |z_1|^2 |z_2|^2 = 1}
 ~= R_(>0) x S^1 x S^1.
```

Prove separately

```text
O_K^* = mu_10 x <phi>,
rank O_K^* = 1.
```

The firewall is part of the result:

```text
dim_R T_K^1(R) = 3,
free rank O_K^* = 1.
```

The three real Lie directions are not three independent integral axes.

### G5. The public J point

With

```text
sigma_1(j) = exp(2 pi i/5),
sigma_2(j) = exp(4 pi i/5),
```

prove

```text
sigma_1(J) = phi^-1 exp( 2 pi i/5),
sigma_2(J) = phi    exp(-  pi i/5),
N_K/Q(J) = 1.
```

Thus `J` is one arithmetic point of `T_K^1(Q)`. Its weighted logarithmic modulus vector is

```text
(2 log|sigma_1(J)|, 2 log|sigma_2(J)|)
= (-2 log phi, +2 log phi),
```

and has zero sum.

### G6. Reciprocal-factorization comparison

The registered L1 refactorization

```text
(v,w) -> (lambda v, lambda^-1 w)
```

may be cited only as an instance of the same product-one pattern. Its carrier may not be identified with `T_K^1`, and no new Registry dependency may be manufactured.

## 5. Frozen breakers and negative controls

All must be recorded in the result.

### B1. Degree control

For every quartic field `E/Q`, `dim T_E^1 = 3`. Therefore the number three does not select `K`, `j`, `J`, or `p=5`.

### B2. Split-algebra control

The split etale algebra `Q^4` also has a three-dimensional norm-one torus. Dimension alone contains no cyclotomic content.

### B3. Rank control

Torus dimension and the free rank of integral units are different invariants. Any argument equating `3` with three integral scale directions fails.

### B4. Chart control

Ordering embeddings gives a coordinate chart. It does not give a canonical physical orientation.

### B5. Physical firewall

No space, force, decoder, apparatus, event, measure, observer, probability, SI, or L2-L6 statement follows.

### B6. Axiom firewall

The work starts from the public field and public axiom. It does not derive or select `J`.

### B7. Uniqueness firewall

The seam does not prove a unique physical reading and does not narrow Public Canon v71's reading-family plurality without a separate typed gate.

### B8. Tangent/global firewall

`Lie(T_K^1)=ker Tr` is a first-order identity at the group unit. It does not identify every trace-zero additive point with a global norm-one multiplicative point.

## 6. Decision rule

```text
CANDIDATE-T  G1-G6 close by exact proof and B1-B8 survive.
PARTIAL      a proper subset closes and every missing clause is named.
F            an exact counterexample breaks a frozen positive clause.
STOP         authority, collision, typing, basis, dependency or scope is unclear.
```

`CANDIDATE-T` is incubation language only. It creates no public claim status.

## 7. Nearest registered work

- `J-UNIT [T]` owns `N_K/Q(J)=1`.
- `REGULATOR-TWO-LOG-PHI [T]` owns the rank-one unit and regulator facts.
- `TRACEKERNEL-RESIDUAL-FORM [T]` owns the residual trace kernel.
- `ARITHMETIC-RAPIDITY-DECOMPOSITION [T]` owns the norm and rapidity interval law in `Q(sqrt5)`.
- `QPAIR-CROSS-SECTOR-NONDESCENT [T]` owns the reciprocal factorization on its own carrier.
- `PURE-QUBIT-LOCAL-RELATION-PYTHAGORAS [T]` owns the pure-state local/relation identity on an external quantum carrier.

The old identifier `C-EM-UNIT-CARRIER-1` is consumed and is not reused.

## 8. Pre-execution record

At the time this file is committed:

```text
formal gate executions: 0
exact audit runs:       0
enumerations:           0
Canon edits:            0
Registry edits:         0
```

Any audit script must be added and run only after this preregistration commit exists on the public branch.