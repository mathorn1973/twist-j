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

## 1. Scope

```text
layer: L1
from:  L1
into:  L1
```

No layer lift is attempted. No physical meaning is assigned to any carrier below.

For every finite separable extension `E/Q`, define

```text
T_E^1 := ker(N_E/Q : Res_E/Q G_m -> G_m).
```

For the specialization fix

```text
K=Q(j), j=zeta_5, j^5=1, j!=1,
O_K=Z[j], J=1+j^2,
B=(j,j^2,j^3,j^4),
Lambda_rel={x in O_K : Tr_K/Q(x)=0}.
```

## 2. Frozen theorem statements

### T1 NORM-ONE-TANGENT-TRACE

For `n=[E:Q]`, prove

```text
d(N_E/Q)_1=Tr_E/Q,
Lie(T_E^1)=ker(Tr_E/Q),
dim T_E^1=n-1.
```

The proof must include

```text
N_E/Q(1+eps x)=1+eps Tr_E/Q(x), eps^2=0.
```

After base change to a splitting field and after an embedding order is declared, prove

```text
T_E^1 ~= {(x_1,...,x_n) in G_m^n : product_i x_i=1}
      ~= G_m^(n-1),
```

with last coordinate `(product_(i<n) x_i)^-1`. The ordered chart does not define a canonical orientation over `Q`.

### T2 J-INTEGRAL-NORM-TRACE-SEAM

Prove

```text
B is an integral basis of O_K,
Tr_K/Q(j^a)=-1 for a=1,2,3,4,
Tr_K/Q(sum_a x_a j^a)=-sum_a x_a,
Lambda_rel ~= {(x_1,x_2,x_3,x_4) in Z^4 : sum_a x_a=0}
           ~= A_3,
Lambda_rel/5Lambda_rel ~= ker(sum:F_5^4->F_5).
```

The final carrier may be identified by content only with the object already owned by `TRACEKERNEL-RESIDUAL-FORM [T]`. This probe does not restate or take ownership of its residual form.

### T3 J-NORMONE-DIMENSION-RANK-FIREWALL

Using `K tensor_Q R ~= C x C`, prove

```text
T_K^1(R)
 ~= {(z_1,z_2) in C^* x C^* : |z_1|^2|z_2|^2=1}
 ~= R_(>0) x S^1 x S^1,
dim_R T_K^1(R)=3.
```

Use inherited `J-HARMONIC-SEAM [T]` for

```text
O_K^*=mu_10 x <phi>, rank O_K^*=1.
```

Torus dimension and integral-unit rank are different invariants.

### T4 J-POINT-AND-GLOBAL-TANGENT-FIREWALL

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
N_K/Q(J)=1,
log-modulus vector=(-2 log phi,+2 log phi).
```

Retain the exact counter-witnesses

```text
N(J)=1,       Tr(J)=3,
Tr(j-j^2)=0,  N(j-j^2)=5.
```

Thus the global norm-one locus is not the additive trace kernel. Their positive relation is tangent-at-identity only.

## 3. Accepted code

```text
probes/P-J-NORM-TRACE-TANGENT-SEAM-1/verify.py
sha256 0f6eaf58024ab9a48be68422e4b84b6c74628418debc76cf9da65c3eb20c403b

probes/P-J-NORM-TRACE-TANGENT-SEAM-1/break.py
sha256 adc70237fb8e40f2a8afc82d855a769140cbdd1378784509748f94966edbcd03
```

Both scripts use only the Python standard library and exact integer or `Fraction` arithmetic. `break.py` is a same-session adversarial checker, pinned before formal `verify.py` execution. It is not independent confirmation and not a second-architecture gate.

## 4. Dependencies

Load-bearing inherited claims:

```text
J-UNIT [T]
J-HARMONIC-SEAM [T]
TRACEKERNEL-RESIDUAL-FORM [T]
```

Context only, not dependencies:

```text
ARITHMETIC-RAPIDITY-DECOMPOSITION [T]
QPAIR-CROSS-SECTOR-NONDESCENT [T]
PURE-QUBIT-LOCAL-RELATION-PYTHAGORAS [T]
```

Incubation provenance, not authority: `C-J-NORM-ONE-TRACE-KERNEL-SEAM-1-N`, issue #659, branch `notes/c-j-norm-one-trace-kernel-seam-1-n`.

## 5. Mandatory controls

1. Every quartic field has norm-one torus dimension three.
2. The split etale algebra `Q^4` has the same dimension.
3. Dimension three selects neither `p=5`, `K`, nor `J`.
4. Torus dimension and integral-unit rank are distinct.
5. An embedding order supplies coordinates, not physical orientation.
6. `Lie(T_K^1)=ker Tr` does not identify their global points.
7. The probe starts from public `K` and `J`; it does not derive or select them.
8. No space, force, decoder, apparatus, event, measure, probability, observer, SI, or L2-L6 claim follows.
9. No global decoder uniqueness or reading-family selection follows.
10. Reciprocal product-preserving constructions on other carriers are comparisons only.

## 6. Failure threshold

Scientific falsifier fires if a frozen positive identity is false, if `Lambda_rel/5Lambda_rel` is not exactly the 125-point kernel of coordinate sum over `F_5`, if either counter-witness is false, or if a mandatory control is removed.

Integrity STOP occurs if the branch base, final preregistration pin, verifier hash, expected stdout, exit code, stderr, architecture record, proof record, dependency typing, or one-directory scope is inconsistent without an exact mathematical negation.

Thresholds and scope may not move after the final pin.

## 7. Decision rule

```text
T      exact written proof closes T1-T4 and every control survives;
       the verifier is an audit.
F      an exact counterexample fires the scientific falsifier.
STOP  an integrity or typing condition fails without mathematical negation.
```

A local run begins only after this final preregistration and both scripts are committed and pushed on the probe branch. `EXPECTED.txt`, `RUN.md`, `PROOF.md`, and `RESULT.md` are added only after that pin.
