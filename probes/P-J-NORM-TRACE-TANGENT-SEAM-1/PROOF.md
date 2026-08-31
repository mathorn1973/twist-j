# P-J-NORM-TRACE-TANGENT-SEAM-1 proof

Date: 2026-08-29

Status: exact written proof at action layer L1. This proof establishes the frozen mathematical statements T1 to T4. It creates no Canon or Registry status by itself.

## 1. General norm-one tangent theorem

Let `E/Q` be a finite separable extension of degree `n`, and let

```text
T_E^1 := ker(N_E/Q : Res_E/Q G_m -> G_m).
```

Choose a splitting field `L` of `E/Q` and order the `n` embeddings

```text
sigma_1,...,sigma_n : E -> L.
```

After base change to `L`, restriction of scalars splits:

```text
(Res_E/Q G_m)_L ~= G_m^n,
```

and the norm becomes the coordinate product:

```text
N_E/Q(x_1,...,x_n)=product_i x_i.
```

Let `eps^2=0`. For `x in E`, exact multiplication in the dual numbers gives

```text
N_E/Q(1+eps x)
 = product_i (1+eps sigma_i(x))
 = 1+eps sum_i sigma_i(x)
 = 1+eps Tr_E/Q(x).
```

All terms containing two or more copies of `eps` vanish. Therefore

```text
d(N_E/Q)_1=Tr_E/Q.
```

The Lie algebra of a kernel is the kernel of the differential at the identity, hence

```text
Lie(T_E^1)=ker(Tr_E/Q).
```

Over `L`, the norm-one torus is

```text
(T_E^1)_L
 = {(x_1,...,x_n) in G_m^n : product_i x_i=1}.
```

The ordered chart

```text
(y_1,...,y_(n-1))
 -> (y_1,...,y_(n-1),(product_(i<n)y_i)^-1)
```

is an isomorphism with `G_m^(n-1)`. Therefore

```text
dim T_E^1=n-1.
```

The embedding order is auxiliary. It provides coordinates after splitting and does not define a canonical orientation over `Q`. This proves T1.

## 2. Integral trace-zero lattice in Q(zeta_5)

Set

```text
K=Q(j),
j=zeta_5,
O_K=Z[j].
```

The standard integral basis is

```text
B_0=(1,j,j^2,j^3).
```

Multiplication by the unit `j` sends `B_0` to

```text
B=(j,j^2,j^3,j^4).
```

Its determinant is `N_K/Q(j)=1`, so the change-of-basis matrix is unimodular. Thus `B` is an integral basis of `O_K`.

For every `a in {1,2,3,4}`, multiplication by `a` permutes the nonzero residue classes modulo five. The Galois conjugates of `j^a` are therefore the four nontrivial fifth roots. Their sum is

```text
j+j^2+j^3+j^4=-1.
```

Hence

```text
Tr_K/Q(j^a)=-1,  a=1,2,3,4.
```

For

```text
x=x_1 j+x_2 j^2+x_3 j^3+x_4 j^4,
```

linearity gives

```text
Tr_K/Q(x)=-(x_1+x_2+x_3+x_4).
```

Therefore

```text
Lambda_rel
 := O_K intersect ker(Tr_K/Q)
 ~= {(x_1,x_2,x_3,x_4) in Z^4 : sum_i x_i=0}.
```

The latter lattice is the standard root lattice `A_3`, with basis

```text
e_1-e_4,
e_2-e_4,
e_3-e_4.
```

## 3. Exact reduction modulo five

The coordinate-sum map

```text
s : Z^4 -> Z,
s(x_1,x_2,x_3,x_4)=sum_i x_i
```

is split surjective. Its kernel is `A_3`. Reducing the displayed basis modulo five gives three linearly independent vectors in `F_5^4`, all in the kernel of coordinate sum. Their span has `5^3=125` elements. The kernel of one nonzero linear functional on `F_5^4` also has `5^3` elements. Thus the inclusion is equality:

```text
Lambda_rel/5Lambda_rel
 ~= A_3/5A_3
 ~= ker(sum:F_5^4->F_5).
```

This is the exact carrier already appearing in `TRACEKERNEL-RESIDUAL-FORM [T]`. That registered claim retains ownership of its residual form and all higher content. This proof supplies only the integral tangent origin of its carrier. This proves T2.

## 4. Real norm-one group and the rank firewall

Since `K` is a quartic CM field,

```text
K tensor_Q R ~= C x C.
```

On real points, the absolute norm is

```text
N_K/Q(z_1,z_2)=|z_1|^2 |z_2|^2.
```

Therefore

```text
T_K^1(R)
 ~= {(z_1,z_2) in C^* x C^* : |z_1|^2|z_2|^2=1}.
```

Define

```text
F : R_(>0) x S^1 x S^1 -> T_K^1(R),
F(r,u,v)=(r^-1 u,r v).
```

This is a group homomorphism. It is bijective, with inverse

```text
(z_1,z_2) -> (|z_2|,z_1/|z_1|,z_2/|z_2|).
```

The norm-one condition supplies `|z_1||z_2|=1`, so the inverse is well defined. Hence

```text
T_K^1(R) ~= R_(>0) x S^1 x S^1,
dim_R T_K^1(R)=3.
```

The inherited theorem `J-HARMONIC-SEAM [T]` gives separately

```text
O_K^*=mu_10 x <phi>,
rank O_K^*=1.
```

The real Lie dimension and the free rank of integral points are different invariants. The three real directions consist of one noncompact scale-balance direction and two compact phase directions. They are not three free integral scale axes. This proves T3, with the unit-group product inherited rather than re-proved.

## 5. The point J on the norm-one carrier

Let

```text
J=1+j^2,
phi=-(j^2+j^3).
```

Using `1+j+j^2+j^3+j^4=0`, direct multiplication gives

```text
J phi
 = -(1+j^2)(j^2+j^3)
 = -(j^2+j^3+j^4+1)
 = j.
```

Thus

```text
J=j phi^-1.
```

Choose the two complex-place representatives

```text
sigma_1(j)=exp(2 pi i/5),
sigma_2(j)=exp(4 pi i/5).
```

At the first place,

```text
sigma_1(J)=phi^-1 exp(2 pi i/5).
```

The second embedding sends `phi` to `-phi^-1`. Applying it to `J phi=j` gives

```text
sigma_2(J)=sigma_2(j)/sigma_2(phi)
          =-phi j^2
          =phi exp(-pi i/5).
```

Consequently

```text
|sigma_1(J)|=phi^-1,
|sigma_2(J)|=phi,
N_K/Q(J)=|sigma_1(J)|^2 |sigma_2(J)|^2=1.
```

With normalized complex absolute values, the logarithmic modulus vector is

```text
(log |sigma_1(J)|^2,log |sigma_2(J)|^2)
 =(-2 log phi,+2 log phi).
```

Its coordinate sum is zero.

## 6. Global versus tangent sets

The regular representation satisfies

```text
N_K/Q(x)=det(M_x),
Tr_K/Q(x)=tr(M_x).
```

The general theorem is the regular-representation identity

```text
d(det)_I=tr.
```

It does not identify the determinant-one group with the trace-zero vector space. Two exact witnesses make the boundary explicit:

```text
N(J)=1,       Tr(J)=3,
Tr(j-j^2)=0,  N(j-j^2)=5.
```

For the second witness,

```text
j-j^2=j(1-j),
N(j-j^2)=N(j)N(1-j)=1*5=5,
```

and its trace is `-1-(-1)=0`. Thus

```text
T_K^1(Q) != ker(Tr_K/Q).
```

Only the tangent space of the first at the multiplicative identity equals the second. This proves T4.

## 7. Negative controls

The proof leaves all frozen controls intact.

1. `dim T_E^1=[E:Q]-1`, so every quartic field has norm-one dimension three.
2. The split etale algebra `Q^4` has the same product-one torus and the same dimension.
3. Dimension three therefore selects neither `p=5`, `K`, nor `J`.
4. An ordered splitting chart does not supply physical orientation.
5. Torus dimension three does not equal integral-unit rank one.
6. The global norm-one locus does not equal the additive trace kernel.
7. The proof starts from the public `K` and `J` and does not derive or select them.
8. No space, force, decoder, apparatus, event, measure, probability, observer, SI, or L2-L6 statement follows.
9. No global decoder uniqueness or reading-family selection follows.
10. Reciprocal product-preserving constructions on other carriers remain comparisons only.

## 8. Exact conclusion

The theorem-grade L1 seam is

```text
ker N_K/Q
 -> tangent at 1
 -> ker Tr_K/Q
 -> integral lattice A_3
 -> reduction modulo 5
 -> ker(sum:F_5^4->F_5).
```

Equivalently,

```text
Lie(ker N_K/Q)=ker Tr_K/Q,
(ker Tr_K/Q on O_K)/5=ker(sum:F_5^4->F_5).
```

The informal phrase "unity is counted inward" is a derived reading of this exact structure, not an additional theorem and not a physical claim.
