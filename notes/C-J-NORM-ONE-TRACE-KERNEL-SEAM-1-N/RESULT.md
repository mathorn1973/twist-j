# RESULT C-J-NORM-ONE-TRACE-KERNEL-SEAM-1-N

**Status:** NON-CANONICAL incubation result.

**Scientific label:** candidate-T at L1 for the exact algebraic seam below. Candidate-D for the phrase "unity is counted inward". No public status, no Canon edit, no Registry edit, and no L2-L6 lift.

**Authority basis:** Public Canon v71.

**Issue lock:** #659.

**Preregistration commit:** `a3f4fb2fb038497433153b7b8448f6ee0c9d7636`.

**Breaker freeze commit:** `631caadbe002ac386cb3387a27adae949cba88f8`.

**Positive verifier commit:** `1ced13ab46f4e37417f4cab5d78e8bb065a0cac8`.

## Verdict

```text
CANDIDATE-T / L1
```

All frozen clauses G1-G6 close by exact proof. All frozen breakers B1-B8 survive. The same-session breaker reports `NO BREAK`. This is not independent confirmation and it is not a two-architecture public gate.

## 1. General norm-trace theorem

Let `E/Q` be a finite separable field extension of degree `n`. Define the norm-one torus

```text
T_E^1 := ker(N_E/Q : Res_E/Q G_m -> G_m).
```

Then:

```text
d(N_E/Q)_1 = Tr_E/Q,
Lie(T_E^1)  = ker(Tr_E/Q),
dim T_E^1   = n - 1.
```

### Proof

Let `L` be a splitting field and let `sigma_1,...,sigma_n` be the embeddings of `E` into `L`. Over `L`,

```text
Res_E/Q G_m ~= G_m^n,
N_E/Q(x) = product_i sigma_i(x).
```

Use dual numbers with `eps^2=0`. For `x in E`,

```text
N_E/Q(1 + eps x)
 = product_i (1 + eps sigma_i(x))
 = 1 + eps sum_i sigma_i(x)
 = 1 + eps Tr_E/Q(x).
```

Therefore the differential of the norm at the group unit is the field trace. Taking the tangent kernel gives

```text
Lie(T_E^1) = ker Tr_E/Q.
```

After the same split base change,

```text
T_E^1
 = {(x_1,...,x_n) in G_m^n : product_i x_i = 1}.
```

After ordering the embeddings, the explicit chart is

```text
(y_1,...,y_(n-1))
 -> (y_1,...,y_(n-1),(product_(i<n) y_i)^-1).
```

Hence `T_E^1` is a torus of dimension `n-1`. The ordered chart is not a canonical orientation over `Q`. QED.

## 2. The exact inverse pattern

The frozen intuition has a precise algebraic form after a split chart is chosen.

Globally, multiplicative unity is

```text
x_1 x_2 x_3 x_4 = 1,
```

so the fourth coordinate is not added from outside:

```text
x_4 = (x_1 x_2 x_3)^-1.
```

Infinitesimally at unity, the product linearizes to a sum:

```text
v_1 + v_2 + v_3 + v_4 = 0,
```

so

```text
v_4 = -(v_1 + v_2 + v_3).
```

This is the exact content behind the word "inverse". One global closure equation leaves three internal relational directions.

## 3. The integral seam in Q(zeta_5)

Set

```text
K = Q(j),
j = zeta_5,
O_K = Z[j].
```

Use the nontrivial-root basis

```text
B = (j,j^2,j^3,j^4).
```

Multiplication by the unit `j` sends the standard integral basis `(1,j,j^2,j^3)` to `B`. Its determinant is `N(j)=1`, so `B` is an integral basis.

For every `a=1,2,3,4`, the Galois conjugates of `j^a` are all four nontrivial fifth roots. Therefore

```text
Tr_K/Q(j^a) = j + j^2 + j^3 + j^4 = -1.
```

If

```text
x = x_1 j + x_2 j^2 + x_3 j^3 + x_4 j^4,
```

then

```text
Tr_K/Q(x) = -(x_1+x_2+x_3+x_4).
```

Thus the integral tangent lattice is

```text
Lambda_rel
 := O_K intersect Lie(T_K^1)
  = ker(Tr_K/Q : O_K -> Z)
  ~= {(x_1,x_2,x_3,x_4) in Z^4 : sum_i x_i=0}.
```

This is the root lattice `A_3`. A basis is

```text
e_1-e_4,
e_2-e_4,
e_3-e_4.
```

Reduction modulo five is exact:

```text
Lambda_rel / 5 Lambda_rel
 ~= ker(sum : F_5^4 -> F_5).
```

The right-hand side has `5^3=125` points. It is exactly the L1 carrier already registered in `TRACEKERNEL-RESIDUAL-FORM [T]`, now reached as the reduction of the integral tangent lattice of the norm-one torus. The registered claim retains ownership of its residual form and all of its existing scope.

## 4. Matrix form

For the regular representation `x -> M_x`,

```text
N_E/Q(x)  = det(M_x),
Tr_E/Q(x) = tr(M_x).
```

Therefore the same theorem reads

```text
d(det)_I = tr,
Lie(SL on the regular carrier) = trace-zero regular operators.
```

For the public axiom point,

```text
N_K/Q(J)=1
```

is equivalent to

```text
det(M_J)=1.
```

This does not make `M_J` itself traceless. In fact `Tr_K/Q(J)=tr(M_J)=3`. Determinant one is the global closure; trace zero is its tangent condition at the identity.

## 5. Real form and the dimension/rank firewall

Since `K` is a quartic CM field,

```text
K tensor_Q R ~= C x C.
```

The absolute norm on real points is

```text
N(z_1,z_2)=|z_1|^2 |z_2|^2.
```

Hence

```text
T_K^1(R)
 ~= {(z_1,z_2) in C^* x C^* : |z_1|^2 |z_2|^2=1}
 ~= R_(>0) x S^1 x S^1.
```

An explicit group isomorphism is

```text
(r,u,v) -> (r^-1 u, r v),
r>0, u in S^1, v in S^1.
```

Therefore

```text
dim_R T_K^1(R)=3.
```

Separately, the public theorem `J-HARMONIC-SEAM [T]` owns

```text
O_K^* = mu_10 x <phi>.
```

Thus

```text
rank O_K^*=1.
```

These are different invariants:

```text
three real Lie directions != three free integral unit directions.
```

The real norm-one carrier has one noncompact scale-balance coordinate and two compact phase coordinates. Its integral points have one free scale exponent and finite torsion.

## 6. The J point

Let

```text
J = 1+j^2,
phi = -(j^2+j^3).
```

Direct multiplication gives

```text
J phi = j,
```

hence

```text
J = j phi^-1.
```

Choose complex-place representatives

```text
sigma_1(j)=exp(2 pi i/5),
sigma_2(j)=exp(4 pi i/5).
```

Then

```text
sigma_1(J)=phi^-1 exp(2 pi i/5).
```

The second embedding sends `phi` to `-phi^-1`, so

```text
sigma_2(J)=-phi j^2=phi exp(-pi i/5).
```

Therefore

```text
|sigma_1(J)|=phi^-1,
|sigma_2(J)|=phi,
N_K/Q(J)=|sigma_1(J)|^2 |sigma_2(J)|^2=1.
```

With the public normalized complex absolute values, the logarithmic modulus vector is

```text
(-2 log phi,+2 log phi),
```

and its sum is zero.

So `J` is one arithmetic point on the norm-one carrier. It moves inward by exchanging scale between the two complex places while the total norm stays one.

## 7. Reciprocal-factorization boundary

The registered L1 transformation

```text
(v,w) -> (lambda v,lambda^-1 w)
```

preserves the matched product `vw`. It has the same product-one grammar. This result does not identify its carrier with `T_K^1`, and it adds no Registry dependency between the claims.

## 8. Breakers that matter

### 8.1 Dimension does not select five

Every quartic field has a three-dimensional norm-one torus. The split etale algebra `Q^4` does too. Therefore

```text
dim T_K^1=3
```

comes from degree four, not uniquely from cyclotomy, `p=5`, or `J`.

The specific TWIST-J content is the marked cyclotomic basis, the public point `J`, the golden unit, and the exact reduction to the existing `F_5` trace carrier. The raw number three is not a selector.

### 8.2 Tangent kernel is not the global group

Two exact witnesses prevent the common false identification:

```text
N(J)=1,       Tr(J)=3,
Tr(j-j^2)=0,  N(j-j^2)=5.
```

Thus

```text
T_K^1(Q) != ker Tr_K/Q.
```

Only the tangent space at the multiplicative identity equals the trace kernel.

### 8.3 No physical promotion

Nothing here proves that `T_K^1(R)` is physical space. Nothing here derives a decoder, a measure, a force, an observer, SI units, or a unique reading. The possible reading

```text
physical relational space = infinitesimal norm-one carrier
```

would be a separate candidate-D statement and needs its own typed selection and occurrence gates.

## 9. What is actually new

The public ingredients existed separately:

```text
J-UNIT [T]:                         N(J)=1,
TRACEKERNEL-RESIDUAL-FORM [T]:     W_5=ker(sum:F_5^4->F_5),
J-HARMONIC-SEAM [T]:               O_K^*=mu_10 x <phi>.
```

The candidate contribution is the exact L1 seam

```text
norm-one torus
 -> tangent at 1
 -> integral trace-zero lattice A_3
 -> reduction modulo 5
 -> public residual trace carrier W_5.
```

In one line:

```text
Lie(ker N_K/Q) = ker Tr_K/Q,
(ker Tr on O_K)/5 = W_5.
```

That is the rigorous form of the intuition. Unity is not expanded by adding an external coordinate. Closure determines one coordinate inversely, leaving only internal relations to vary.

## 10. Exact local audit

One local Linux x86_64 lane, Python 3.13.5, sanitized environment:

```text
env -i PATH=/opt/pyvenv/bin:/usr/bin:/bin \
  LC_ALL=C PYTHONHASHSEED=0 TZ=UTC python3 FILE
```

Both scripts were run twice. Each pair was byte-identical, exited zero, and wrote empty stderr.

```text
break.py
  sha256(file)   f7498300ac807b4b56511ea60fec0d0b25844ddd8ea0e1c0b7f94cae375c4826
  stdout bytes   450
  stdout sha256  0c11844dc8cd662385aad181ecd869fec27ed9960143bbadee669d4153a5d820
  stderr bytes   0
  verdict        BREAKER NO BREAK

verify.py
  sha256(file)   b1ff048c01ffa51a3d77dde2d521d869aae41ed0e4c98d69450a6386abbd30f9
  stdout bytes   729
  stdout sha256  b75148ec3b000f4ea0c1a9559be7679a4fdba017643905624a33cfec15ed0c2a
  stderr bytes   0
  verdict        ALL PASS
```

This is local reproduction and audit only. The proof, not the one-lane computation, is the basis for candidate-T.
