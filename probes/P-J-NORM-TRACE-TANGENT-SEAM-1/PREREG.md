# PREREG P-J-NORM-TRACE-TANGENT-SEAM-1

**Status:** frozen public preregistration.

**Owner:** ChatGPT owner session, 2026-08-29.

**Issue lock:** #660.

**Authority basis:** Public Canon v71.

```text
AUTHORITY:         mathorn1973/twist-j main
TAG:               canon-v71
CONTENT_COMMIT:    a77d720433c19976f9ab663d023ec9364eac34eb
ACTIVATION_COMMIT: 39e61fbfe794b0d3d3ab2a28ba9f960c13f4fe7f
CANON_SHA256:      0306abb2e7f855ceb4fcbfdf14265a9d2c5c8bd23b35868b74a92aae16b5e279
CANON_BYTES:       369836
```

The authority tuple, annotated tag, immutable release assets, normative hashes and required checks were verified before the issue lock. The probe branch starts from the activation commit above.

## 1. Action layer

```text
layer: L1
from:  L1
into:  L1
```

No layer lift is attempted.

## 2. Frozen carrier

For every finite separable extension `E/Q`, let

```text
T_E^1 := ker(N_E/Q : Res_E/Q G_m -> G_m).
```

For the cyclotomic specialization fix

```text
K   = Q(j),
j   = zeta_5,
j^5 = 1,
j != 1,
O_K = Z[j],
J   = 1+j^2,
B   = (j,j^2,j^3,j^4).
```

Define

```text
Lambda_rel := {x in O_K : Tr_K/Q(x)=0}.
```

No physical meaning is assigned to the norm-one torus, its tangent space, its real points, or `Lambda_rel`.

## 3. Frozen theorem statements

### T1. NORM-ONE-TANGENT-TRACE

For `n=[E:Q]`, prove

```text
d(N_E/Q)_1 = Tr_E/Q,
Lie(T_E^1)  = ker(Tr_E/Q),
dim T_E^1   = n-1.
```

The proof must contain the exact dual-number identity

```text
N_E/Q(1+eps x)=1+eps Tr_E/Q(x),
eps^2=0.
```

After base change to a splitting field and after an embedding order is declared, prove

```text
T_E^1
 ~= {(x_1,...,x_n) in G_m^n : product_i x_i=1}
 ~= G_m^(n-1),
```

with chart

```text
(y_1,...,y_(n-1))
 -> (y_1,...,y_(n-1),(product_(i<n)y_i)^-1).
```

No canonical orientation over `Q` may be inferred from the ordered chart.

### T2. J-INTEGRAL-NORM-TRACE-SEAM

Prove

```text
B is an integral basis of O_K,
Tr_K/Q(j^a)=-1 for a=1,2,3,4.
```

Hence

```text
Tr_K/Q(sum_a x_a j^a)=-sum_a x_a,
Lambda_rel ~= {(x_1,x_2,x_3,x_4) in Z^4 : sum_a x_a=0}
           ~= A_3.
```

Prove the exact reduction seam

```text
Lambda_rel/5Lambda_rel
 ~= ker(sum:F_5^4->F_5).
```

The right-hand side may be identified by carrier content only with the object already owned by `TRACEKERNEL-RESIDUAL-FORM [T]`. This probe does not restate or take ownership of its residual form.

### T3. J-NORMONE-DIMENSION-RANK-FIREWALL

Using `K tensor_Q R ~= C x C`, prove

```text
T_K^1(R)
 ~= {(z_1,z_2) in C^* x C^* : |z_1|^2|z_2|^2=1}
 ~= R_(>0) x S^1 x S^1,
```

and therefore

```text
dim_R T_K^1(R)=3.
```

Use the inherited public theorem `J-HARMONIC-SEAM [T]` for

```text
O_K^*=mu_10 x <phi>,
rank O_K^*=1.
```

The distinction between torus dimension and integral-unit rank is part of the theorem boundary.

### T4. J-POINT-AND-GLOBAL-TANGENT-FIREWALL

With

```text
sigma_1(j)=exp(2 pi i/5),
sigma_2(j)=exp(4 pi i/5),
phi=-(j^2+j^3),
```

prove

```text
J phi=j,
sigma_1(J)=phi^-1 exp(2 pi i/5),
sigma_2(J)=phi exp(-pi i/5),
N_K/Q(J)=1.
```

The normalized complex-place logarithmic modulus vector is

```text
(-2 log phi,+2 log phi).
```

Retain the exact counter-witnesses

```text
N(J)=1,       Tr(J)=3,
Tr(j-j^2)=0,  N(j-j^2)=5.
```

Therefore the global norm-one locus and the additive trace kernel are not equal. The positive relation is tangent-at-identity only.

## 4. Code and exact audit

Accepted verifier:

```text
probes/P-J-NORM-TRACE-TANGENT-SEAM-1/verify.py
sha256 0f6eaf58024ab9a48be68422e4b84b6c74628418debc76cf9da65c3eb20c403b
```

Same-session adversarial checker:

```text
probes/P-J-NORM-TRACE-TANGENT-SEAM-1/break.py
sha256 adc70237fb8e40f2a8afc82d855a769140cbdd1378784509748f94966edbcd03
```

The checker is pinned before the formal verifier execution. It is not independent confirmation and is not a second-architecture gate.

Both programs must use only the Python standard library and exact integer or `Fraction` arithmetic.

## 5. Public dependencies

Load-bearing inherited claims:

```text
J-UNIT [T]
J-HARMONIC-SEAM [T]
TRACEKERNEL-RESIDUAL-FORM [T]
```

Context-only comparisons, not dependencies:

```text
ARITHMETIC-RAPIDITY-DECOMPOSITION [T]
QPAIR-CROSS-SECTOR-NONDESCENT [T]
PURE-QUBIT-LOCAL-RELATION-PYTHAGORAS [T]
```

Incubation provenance, not authority:

```text
C-J-NORM-ONE-TRACE-KERNEL-SEAM-1-N
issue #659
branch notes/c-j-norm-one-trace-kernel-seam-1-n
PROMO-C-J-NORM-ONE-TRACE-KERNEL-SEAM-1-N.md
```

## 6. Systematics and negative controls

All are mandatory.

1. **Degree control.** Every quartic field has norm-one torus dimension three.
2. **Split-etale control.** `Q^4` has the same norm-one dimension.
3. **Selection boundary.** Dimension three selects neither `p=5`, `K`, nor `J`.
4. **Rank control.** Torus dimension and the free rank of integral units are different invariants.
5. **Chart control.** Ordering embeddings supplies coordinates, not a canonical physical orientation.
6. **Tangent/global control.** `Lie(T_K^1)=ker Tr` does not identify global points of the two sets.
7. **Axiom control.** The probe starts from the public `K` and `J`; it does not derive or select them.
8. **Physics firewall.** No space, force, decoder, apparatus, event, measure, probability, observer, SI, or L2-L6 claim follows.
9. **Reading firewall.** The probe does not prove global decoder uniqueness or choose one member of a public reading family.
10. **Carrier firewall.** Reciprocal product-preserving constructions on other registered carriers are comparisons only and are not identified with `T_K^1`.

## 7. Failure threshold

Scientific falsifier fires if any frozen positive identity is mathematically false, if

```text
Lambda_rel/5Lambda_rel
```

is not exactly the 125-point kernel of coordinate sum over `F_5`, if either displayed counter-witness is false, or if the result removes a mandatory negative control.

Integrity STOP occurs if the branch base, preregistration pin, verifier hash, expected stdout, exit code, stderr, architecture record, proof record, dependency typing, or one-directory scope is inconsistent without an exact mathematical negation.

Thresholds and scope may not move after this pin.

## 8. Decision rule

```text
T      exact written proof closes T1-T4 and every control survives;
       the verifier is an audit.
F      an exact counterexample fires the scientififer.
STOP  an integrity or typing condition fails without a mathematical negation.
```

A local run begins only after this preregistration and both scripts are committed and pushed on the probe branch. `EXPECTED.txt`, `RUN.md`, `PROOF.md`, and `RESULT.md` are added only after that pin.
