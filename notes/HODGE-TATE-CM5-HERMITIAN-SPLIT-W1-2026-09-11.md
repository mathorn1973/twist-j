# Hodge–Tate CM5: exact Hermitian split test W1

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v83 and the companion notes
`HODGE-AND-TATE-CM5-CALIBRATION-2026-09-11.md`,
`HODGE-TATE-CM5-INTEGRAL-HOMOLOGY-CALIBRATION-2026-09-11.md`,
`HODGE-TATE-CM5-HODGE-CENSUS-2026-09-11.md`, and
`HODGE-TATE-CM5-GENERALIZED-WEIL-EIGHTFOLD-2026-09-11.md`.

**Date:** 2026-09-11.

This note closes **Gate W1** of the direct CM5 generalized-Weil eightfold lane.
It changes no `canon/` file, registers no public claim, starts no formal public
probe, and makes no algebraicity claim.

The result is constructive: the product polarization on the TWIST-seeded
Weil eightfold gives an explicit rank-four `K`-Hermitian form which is the
direct sum of two hyperbolic planes.

---

## 1. Result

Put

\[
K=\mathbf Q(j)=\mathbf Q(\zeta_5),
\qquad
K^+=\mathbf Q(\sqrt5),
\qquad
\beta=\varphi^{-1}.
\]

Let

\[
B=\operatorname{Jac}(y^2=x^5-1),
\qquad
A_0=B_0\times B_1\times B_2\times B_3,
\]

and let

\[
\tau(j)=j^2.
\]

The `K` action on the four factors is

\[
\eta(a)|_{B_k}=\tau^k(a).
\]

Give `A_0` the product of the four canonical principal polarizations.
After identifying the four twisted rank-one `K` modules with one standard
`K` coordinate on each factor, the compatible `K`-Hermitian form is

\[
\boxed{
H=\operatorname{diag}(1,-\beta,-1,\beta).
}
\]

Its determinant is

\[
\boxed{\det H=\beta^2.}
\]

Since `beta` belongs to `K+`,

\[
\beta^2=N_{K/K^+}(\beta),
\]

so the determinant class is trivial in

\[
K^{+\times}/N_{K/K^+}(K^\times).
\]

More strongly, the two-dimensional `K` subspace

\[
\boxed{
U=K(e_0+e_2)\oplus K(e_1+e_3)
}
\]

is totally isotropic. Hence the Witt index is two and

\[
\boxed{(H_1(A_0,\mathbf Q),H)\text{ is split}.}
\]

Therefore

\[
\boxed{(A_0,\eta,h_0)\text{ is a polarized abelian variety of split Weil type}}
\]

in the standard CM-field sense.

This closes Gate W1 **AGREE** at note level.

---

## 2. One-factor polarization datum

The integral-homology calibration identified the canonical Jacobian
polarization with the public TWIST form `Omega_1`. In the cyclotomic model it
has trace form

\[
E_B(x,y)
=
\operatorname{Tr}_{K/\mathbf Q}
\bigl(\xi\,x\bar y\bigr),
\]

where, after fixing the global sign convention,

\[
\xi=\frac{\lambda_1}{5},
\qquad
\lambda_1=j-j^{-1}.
\]

Put also

\[
\lambda_2=j^2-j^{-2}.
\]

The public CM pencil gives

\[
\lambda_2=\beta\lambda_1,
\qquad
\beta=\varphi^{-1}.
\]

The relevant Galois orbit is exact:

\[
\tau(\lambda_1)=\lambda_2,
\]

\[
\tau^2(\lambda_1)=-\lambda_1,
\]

\[
\tau^3(\lambda_1)=-\lambda_2.
\]

Equivalently,

\[
\tau^{-k}(\lambda_1)
=
\lambda_1\,(1,-\beta,-1,\beta)_k,
\qquad k=0,1,2,3.
\]

This four-term orbit is the entire Hermitian calculation.

---

## 3. Untwisting the four `K` modules

On the `k`-th factor the scalar action is

\[
a\cdot x=\tau^k(a)x.
\]

Define

\[
F_k:K_{\tau^k}\longrightarrow K,
\qquad
F_k(x)=\tau^{-k}(x).
\]

Then `F_k` is `K`-linear because

\[
F_k(\tau^k(a)x)
=aF_k(x).
\]

Write

\[
z_k=F_k(x_k),
\qquad
w_k=F_k(y_k).
\]

Thus

\[
x_k=\tau^k(z_k),
\qquad
y_k=\tau^k(w_k).
\]

The product Riemann form is

\[
E_0(x,y)
=
\sum_{k=0}^3
\operatorname{Tr}_{K/\mathbf Q}
\bigl(\xi\,x_k\bar y_k\bigr).
\]

Substituting the untwisted coordinates gives

\[
E_0(z,w)
=
\sum_{k=0}^3
\operatorname{Tr}_{K/\mathbf Q}
\bigl(\xi\,\tau^k(z_k\bar w_k)\bigr).
\]

Trace invariance under Galois transforms this into

\[
E_0(z,w)
=
\sum_{k=0}^3
\operatorname{Tr}_{K/\mathbf Q}
\bigl(\tau^{-k}(\xi)z_k\bar w_k\bigr).
\]

Factor out the single fixed imaginary parameter `xi`:

\[
E_0(z,w)
=
\operatorname{Tr}_{K/\mathbf Q}
\bigl(\xi H(z,w)\bigr),
\]

where

\[
H(z,w)=
\sum_{k=0}^3 h_k z_k\bar w_k,
\qquad
h_k=\frac{\tau^{-k}(\xi)}{\xi}.
\]

The factor `1/5` cancels, and the Galois orbit above gives

\[
(h_0,h_1,h_2,h_3)
=(1,-\beta,-1,\beta).
\]

Therefore

\[
\boxed{
H=\operatorname{diag}(1,-\beta,-1,\beta).
}
\]

No numerical period calculation enters.

---

## 4. Signature check at both real places

The real field `K+` has two embeddings.

At the physical positive embedding,

\[
\beta=\varphi^{-1}>0,
\]

so

\[
H\sim(+,-,-,+)
\]

and the signature is `(2,2)`.

At the conjugate real embedding,

\[
\beta\longmapsto-\varphi<0,
\]

so

\[
H\sim(+,+,-,-)
\]

and the signature is again `(2,2)`.

Thus the Hermitian form has the correct balanced signature at every real
place of `K+`.

---

## 5. Determinant and discriminant class

Directly,

\[
\det H
=1\cdot(-\beta)\cdot(-1)\cdot\beta
=\beta^2.
\]

Because `beta` is fixed by complex conjugation,

\[
N_{K/K^+}(\beta)
=\beta\bar\beta
=\beta^2.
\]

Hence

\[
\boxed{
[\det H]=1
\quad\text{in}\quad
K^{+\times}/N_{K/K^+}(K^\times).
}
\]

For rank four, the conventional Hermitian discriminant differs from the
determinant by the factor

\[
(-1)^{4\cdot3/2}=1,
\]

so its class is also trivial.

This is consistent with splitness, but by itself would not be enough to prove
splitness. The next section gives an explicit maximal isotropic plane.

---

## 6. Explicit maximal isotropic plane

Let

\[
e_0,e_1,e_2,e_3
\]

be the standard basis of `K^4` in which `H` is diagonal.

Set

\[
p_1=e_0+e_2,
\qquad
p_2=e_1+e_3.
\]

Then

\[
H(p_1,p_1)=1-1=0,
\]

\[
H(p_2,p_2)=-\beta+\beta=0,
\]

and, because the form is diagonal,

\[
H(p_1,p_2)=0.
\]

Therefore

\[
U=Kp_1\oplus Kp_2
\]

is a totally isotropic `K`-plane.

Since the full Hermitian space has `K`-dimension four, `U` has maximal
possible dimension. Hence the Witt index is exactly two.

This already proves the split verdict.

---

## 7. Explicit hyperbolic basis

The result can be strengthened to an exact hyperbolic normal form.

Define

\[
q_1=\frac{e_0-e_2}{2},
\]

and

\[
q_2=\frac{e_3-e_1}{2\beta}.
\]

Then

\[
H(p_1,p_1)=H(q_1,q_1)=0,
\qquad
H(p_1,q_1)=1,
\]

and

\[
H(p_2,p_2)=H(q_2,q_2)=0,
\qquad
H(p_2,q_2)=1.
\]

All cross-pairings between the first and second pairs vanish.

Thus, in the ordered basis

\[
(p_1,q_1,p_2,q_2),
\]

the Gram matrix is

\[
\boxed{
\begin{pmatrix}
0&1&0&0\\
1&0&0&0\\
0&0&0&1\\
0&0&1&0
\end{pmatrix}.
}
\]

Therefore

\[
\boxed{
(K^4,H)\simeq\mathbb H_K\oplus\mathbb H_K,
}
\]

where `H_K` denotes the standard Hermitian hyperbolic plane.

This is a constructive split certificate, not merely a classification by
invariants.

---

## 8. Relation to the `X x Xhat` split construction

Markman's current formulation defines a polarized abelian variety of split
Weil type precisely by the existence of a half-dimensional isotropic subspace
for the associated `K`-Hermitian form.

The calculation above meets that definition exactly.

At the level of the rational polarized `K`-Hermitian carrier, the datum is
therefore equivalent to the standard split carrier underlying the
`X x Pic^0(X)` construction: both are rank-four split Hermitian spaces and
both are isometric to two hyperbolic planes.

There is also a simple geometric shadow at the special CM seed:

\[
A_0=B^4=(B^2)\times(B^2),
\]

and the principal polarization on `B` identifies `B^2` with its dual up to the
chosen polarization convention. Hence the underlying polarized abelian
variety already has the product shape

\[
X\times\hat X,
\qquad X=B^2.
\]

What is **not** claimed here is that the particular displayed isotropic
`K`-basis `(p_1,p_2)` is itself the homology of a distinguished pair of
abelian subvarieties `X` and `Xhat`. The split-Weil condition does not require
that stronger statement.

For the modern deformation theory, the load-bearing datum is the rational
split Hermitian space together with the compatible Hodge structure and
polarization. W1 supplies exactly that datum.

---

## 9. Consequence for the eight-dimensional deformation lane

The previous note found an eight-complex-dimensional deformation space of
`K`-Weil structures through the TWIST CM seed.

The Hermitian form just computed is part of the rational polarized datum and
is fixed under those deformations. Therefore every point in the connected
period component determined by this datum remains split.

So the earlier lane can be strengthened from

```text
generic generalized-Weil deformation
```

to

```text
generic split-Weil deformation
```

with the same native field

\[
K=\mathbf Q(\zeta_5).
\]

The four-dimensional Weil-Hodge space

\[
HW=\bigwedge_K^4H^1
\]

persists throughout this split family.

At the special CM seed `B^4`, Gate E forces it into the divisor algebra. At a
generic point of the split component it is exceptional, i.e. complementary
to the algebra generated by divisor classes.

Thus the TWIST-seeded construction now lands directly inside the modern
**split-Weil** framework rather than merely in the broader generalized-Weil
class.

---

## 10. External benchmark

The current version of Eyal Markman's
*Secant sheaves and Weil classes on abelian varieties*
(arXiv:2509.23403v2, revised 2026-02-11) uses exactly this definition:
a polarized abelian variety of Weil type is called split when its associated
`K`-Hermitian form has an isotropic subspace of half the `K`-dimension.

The paper develops a general strategy for algebraicity of Weil classes for
CM fields and implements the proof completely in the currently treated
low-dimensional cases, in particular dimensions at most six with `K`
imaginary quadratic.

Our datum has

\[
[K:\mathbf Q]=4,
\qquad
\dim A=8,
\qquad
\dim_KH^1=4,
\]

so it lies beyond those fully implemented low-dimensional cases, while now
satisfying the same split hypothesis exactly.

Reference:

- E. Markman, *Secant sheaves and Weil classes on abelian varieties*,
  arXiv:2509.23403v2, 2026.
  https://arxiv.org/abs/2509.23403

This is why W1 matters: it removes the first structural obstruction to applying
that program to the direct CM5 eightfold lane.

---

## 11. Breakers and scope

W1 would fail if any of the following exact statements failed:

1. `tau(lambda_1)=lambda_2`;
2. `lambda_2=beta lambda_1`;
3. the four untwisted trace coefficients were not
   `(1,-beta,-1,beta)`;
4. the determinant differed from `beta^2`;
5. `K(e_0+e_2) + K(e_1+e_3)` were not a two-dimensional totally isotropic
   plane;
6. the displayed hyperbolic basis failed to give two standard hyperbolic
   blocks.

No such breaker occurs.

The note does **not** claim:

- algebraicity of the generic `HW` space;
- semiregularity of a Markman secant sheaf in dimension eight;
- an explicit algebraic cycle representing a generic Weil class;
- a canonical decomposition of `A_0` into isotropic abelian subvarieties;
- any new public Canon theorem;
- any physical TWIST interpretation or L1-to-L6 lift.

---

## 12. Verdict and next gate

Gate W1 closes

\[
\boxed{\text{AGREE}.}
\]

The exact TWIST-seeded eightfold is not merely of generalized Weil type. Its
compatible Hermitian form is split:

\[
\boxed{
H\simeq\mathbb H_K\oplus\mathbb H_K.
}
\]

The direct CM5 lane is therefore now

\[
\boxed{
\text{TWIST CM surface}
\to
B^4
\to
\text{split CM5 Weil eightfold}
\to
\text{four exceptional }(2,2)\text{ classes generically}.
}
\]

The next genuinely difficult gate is no longer a classification problem.
It is a **cycle-construction gate**:

> Can the split CM5 eightfold be placed inside the secant-sheaf construction
> strongly enough to produce an algebraic cycle whose class has a nonzero
> component in `HW`, and can that cycle be shown to deform across the relevant
> split-Weil component?

A useful exact precursor is to build the corresponding `F=Q(sqrt5)`
real-multiplication surface `X=B^2`, write Markman's `K` embedding on
`X x Xhat` explicitly, and compare its Hermitian matrix with the hyperbolic
normal form above.

That will be Gate W2.
