# Hodge–Tate CM5: explicit cyclic-C4 Markman secant pair W2B

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v83 and the companion notes
`HODGE-AND-TATE-CM5-CALIBRATION-2026-09-11.md`,
`HODGE-TATE-CM5-INTEGRAL-HOMOLOGY-CALIBRATION-2026-09-11.md`,
`HODGE-TATE-CM5-HODGE-CENSUS-2026-09-11.md`,
`HODGE-TATE-CM5-GENERALIZED-WEIL-EIGHTFOLD-2026-09-11.md`,
`HODGE-TATE-CM5-HERMITIAN-SPLIT-W1-2026-09-11.md`, and
`HODGE-TATE-CM5-MARKMAN-F-REALIZATION-W2A-2026-09-11.md`.

**Date:** 2026-09-11.

This note closes the cohomological **Gate W2B**. It constructs the four-dimensional Markman secant space for the cyclic quartic field

\[
K=\mathbf Q(j)=\mathbf Q(\zeta_5),
\qquad
\operatorname{Gal}(K/\mathbf Q)=\langle\tau\rangle\simeq C_4,
\qquad
\tau(j)=j^2,
\]

and gives an explicit rational pair

\[
\alpha,\beta\in B
\]

whose tensor has non-zero Markman Weil projection. In fact the same pair also has non-zero scalar/rank component, so it satisfies the two cohomological non-vanishing conditions in Markman's Proposition 10.2.1.

No `canon/` file is changed, no public claim is registered, no formal public probe is started, and no coherent-sheaf or algebraicity claim is made.

---

## 1. Markman's general criterion used here

For the split Weil datum from W2A, Markman's secant space

\[
B\subset H^{ev}(X,\mathbf Q),
\qquad X=B_0\times B_0,
\]

has dimension

\[
\dim_{\mathbf Q}B=2^{[F:\mathbf Q]}=4,
\qquad F=\mathbf Q(\sqrt5).
\]

After extension to the Galois closure, which here is simply `K`, the space splits as the direct sum of four pure-spinor lines

\[
B_K:=B\otimes_{\mathbf Q}K
 =\ell_{T_0}\oplus\ell_{T_1}\oplus\ell_{T_2}\oplus\ell_{T_3}.
\]

Markman's grading gives

\[
B\otimes B=BB_0\oplus BB_1\oplus BB_2,
\]

where `BB_k` is spanned by ordered pairs of CM types having exactly `k` common values.

For `[K:Q]=4`,

\[
\dim BB_1=8,
\qquad
\dim HW=4.
\]

Markman's map

\[
\Pi:BB_1\longrightarrow HW
\]

is the degree-four part of his cohomological Orlov/Chevalley transform. For a pair `(T,T')` with one common embedding `sigma`, the restriction

\[
\ell_T\otimes\ell_{T'}\longrightarrow \bigwedge_K^4 V_\sigma
\]

is an isomorphism of one-dimensional lines. Its kernel on `BB_1` is therefore described by one linear relation for each `sigma`: the contributions of all ordered pairs having singleton intersection `{sigma}` must sum to zero.

The current Markman source is:

- E. Markman, *Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication*, arXiv:2509.23079, especially Sections 7, 10 and 11.

The relevant statements are Markman's equations (10.1.2), (10.1.6) and Proposition 10.2.1.

---

## 2. The four CM types in cyclic order

Write the four complex embeddings as

\[
\sigma_r:=\tau^r,
\qquad r\in\mathbf Z/4\mathbf Z,
\]

with complex conjugation

\[
\iota=\tau^2.
\]

The two real embeddings of `F` correspond to the conjugate pairs

\[
\{\sigma_0,\sigma_2\},
\qquad
\{\sigma_1,\sigma_3\}.
\]

A CM type chooses one embedding from each pair. Label the four types cyclically by

\[
\begin{aligned}
T_0&=\{\sigma_0,\sigma_1\},\\
T_1&=\{\sigma_1,\sigma_2\},\\
T_2&=\{\sigma_2,\sigma_3\},\\
T_3&=\{\sigma_3,\sigma_0\}.
\end{aligned}
\]

Thus

\[
\tau(T_r)=T_{r+1}.
\]

The intersection rule is exact:

\[
|T_r\cap T_s|=
\begin{cases}
2,&s=r,\\
1,&s=r\pm1,\\
0,&s=r+2,
\end{cases}
\qquad \text{mod }4.
\]

Hence:

- equal indices give `BB_2`;
- adjacent indices give `BB_1`;
- opposite indices give `BB_0`.

---

## 3. Canonically normalized pure spinors

Markman's general-F construction supplies for each CM type the pure spinor

\[
p_r
:=
\exp\left(
\sum_{\hat\sigma\in\hat\Sigma}
T_r(\hat\sigma)(s)\,\Theta_{\hat\sigma}
\right),
\qquad
s=j-j^{-1},
\]

spanning `ell_(T_r)`. This is Markman's exponential normalization from equation (11.1.2).

Each exponential has degree-zero term `1`. That removes the otherwise irrelevant scalar ambiguity in the pure-spinor line and gives the exact Galois covariance

\[
\boxed{\tau(p_r)=p_{r+1}.}
\]

Consequently

\[
B_K=Kp_0\oplus Kp_1\oplus Kp_2\oplus Kp_3
\]

with the semilinear `C4` action obtained by applying `tau` both to coefficients and to the cyclic index.

---

## 4. Exact rational descent: B is a copy of K as a Q-vector space

For `a in K`, define

\[
v(a):=
\sum_{r=0}^{3}\tau^r(a)p_r.
\]

Then

\[
\tau(v(a))
=
\sum_{r=0}^{3}\tau^{r+1}(a)p_{r+1}
=v(a),
\]

so

\[
v(a)\in B.
\]

The map

\[
\boxed{
v:K\longrightarrow B,
\qquad
a\longmapsto v(a)
}
\]

is Q-linear. It is injective because the four `p_r` are linearly independent over `K`, and both sides have Q-dimension four. Hence

\[
\boxed{B\simeq_{\mathbf Q}K.}
\]

A completely explicit rational basis is therefore

\[
\boxed{
 v(1),\ v(j),\ v(j^2),\ v(j^3).
}
\]

This is the cyclic-C4 analogue of the decompositions Markman obtains from quadratic subfields in his biquadratic example, but it uses no imaginary-quadratic subfield because `Q(zeta_5)` has none.

---

## 5. The explicit W2B pair

Take

\[
\boxed{\alpha:=v(1)=p_0+p_1+p_2+p_3}
\]

and

\[
\boxed{
\beta:=v(j)
 =j p_0+j^2p_1+j^4p_2+j^3p_3.
}
\]

Both are rational classes in `B` by the descent calculation above.

Set

\[
c:=\alpha\otimes\beta\in B\otimes B.
\]

We now compute its `BB_1` component exactly.

---

## 6. The BB1 component

Write

\[
(b_0,b_1,b_2,b_3)
=(j,j^2,j^4,j^3),
\]

so that

\[
\beta=\sum_s b_s p_s.
\]

The adjacent ordered pairs are precisely the eight basis lines contributing to `BB_1`:

\[
(T_r,T_{r+1}),
\qquad
(T_{r+1},T_r),
\qquad r\in\mathbf Z/4\mathbf Z.
\]

For each singleton embedding there are exactly two ordered pairs:

\[
\begin{array}{c|c}
\text{singleton} & \text{ordered pairs}\\
\hline
\{\sigma_0\}&(T_3,T_0),(T_0,T_3)\\
\{\sigma_1\}&(T_0,T_1),(T_1,T_0)\\
\{\sigma_2\}&(T_1,T_2),(T_2,T_1)\\
\{\sigma_3\}&(T_2,T_3),(T_3,T_2).
\end{array}
\]

Markman's Chevalley map is symmetric on the degree-four component relevant here. Concretely, the local half-spin bilinear form for an eight-dimensional hyperbolic factor is symmetric, and reversing a Clifford product of degree four contributes

\[
(-1)^{4\cdot3/2}=+1.
\]

Therefore the two ordered lines for a fixed singleton embedding have the same canonical degree-four normalization. In the kernel coordinates of Markman's equation (10.1.2), the coefficient for each singleton is proportional to the sum of the two tensor coefficients.

For our `c=alpha tensor beta` these four sums are

\[
\begin{array}{c|c}
\text{Weil line}&\text{coefficient up to a common non-zero line normalization}\\
\hline
\bigwedge_K^4V_{\sigma_0}&j+j^3\\
\bigwedge_K^4V_{\sigma_1}&j+j^2\\
\bigwedge_K^4V_{\sigma_2}&j^2+j^4\\
\bigwedge_K^4V_{\sigma_3}&j^3+j^4.
\end{array}
\]

None vanishes. For example, an equality

\[
j^a+j^b=0
\]

with `a != b mod 5` would imply that a fifth root of unity equals `-1`, impossible.

Hence every one of the four Weil components is non-zero:

\[
\boxed{\Pi(c_1)_\sigma\neq0\quad\text{for every }\sigma\in\Sigma.}
\]

In particular,

\[
\boxed{c_1\notin KB_1.}
\]

This already closes the originally stated W2B target.

---

## 7. The BB0 scalar component is non-zero as well

The opposite pairs contributing to `BB_0` are

\[
(T_0,T_2),\ (T_2,T_0),\ (T_1,T_3),\ (T_3,T_1).
\]

For complementary CM types the exponential parameters have opposite signs at both real embeddings. In the standard exterior-algebra spin model the scalar Chevalley pairing of

\[
\exp(\omega)
\quad\text{and}\quad
\exp(-\omega)
\]

is non-zero. In the present two-real-embedding factorization, its value is independent of the sign choices because each local contribution is quadratic in the purely imaginary parameter. The product is proportional to

\[
N_{F/\mathbf Q}(q),
\qquad
q=-s^2=\frac{5+\sqrt5}{2}.
\]

Here

\[
N_{F/\mathbf Q}(q)
=
\frac{5+\sqrt5}{2}\frac{5-\sqrt5}{2}
=5,
\]

so the common scalar normalization is non-zero and rational.

The coefficient sum of the four opposite ordered pairs in `c` is

\[
j^4+j+j^3+j^2
=\operatorname{Tr}_{K/\mathbf Q}(j)
=-1.
\]

Therefore the degree-zero scalar of Markman's cohomological transform is non-zero:

\[
\boxed{\check\phi(c)_0\neq0.}
\]

Equivalently, the corresponding normalized cohomological class has non-zero formal rank.

---

## 8. Markman's cohomological criterion is satisfied

In our lane

\[
d=4>2.
\]

Sections 6 and 7 give

\[
c_1\notin KB_1
\]

and

\[
\check\phi(c)_0\neq0.
\]

Thus the explicit rational tensor

\[
\boxed{
c=
\bigl(p_0+p_1+p_2+p_3\bigr)
\otimes
\bigl(jp_0+j^2p_1+j^4p_2+j^3p_3\bigr)
}
\]

satisfies the two cohomological non-vanishing hypotheses of Markman's Proposition 10.2.1.

Consequently the normalized degree-four class obtained from `c` has a non-zero component in

\[
HW(X\times\hat X,\eta).
\]

More strongly, its Weil projection has non-zero component on all four complex Weil lines.

This is an exact cyclic-C4 replacement for the biquadratic genericity construction in Markman's Section 11.2.1.

---

## 9. Why this is genuinely new relative to the biquadratic shortcut

Markman's explicit degree-four example assumes a biquadratic quartic CM field with

\[
\operatorname{Gal}(K/\mathbf Q)\simeq C_2\times C_2
\]

and uses two imaginary quadratic subfields to split `B` into two rational secant planes.

Our field is

\[
\operatorname{Gal}(\mathbf Q(\zeta_5)/\mathbf Q)\simeq C_4
\]

and has no imaginary quadratic subfield. Moreover

\[
q=\frac{5+\sqrt5}{2}\notin\mathbf Q.
\]

The present construction therefore cannot be obtained by applying Markman's Section 11.2.1 verbatim.

Instead, the cyclic Galois orbit itself supplies the rational descent:

\[
K\xrightarrow{\sim}B,
\qquad
a\mapsto\sum_r\tau^r(a)p_r.
\]

The pair `v(1),v(j)` is the smallest natural pair in this descended basis, and its non-vanishing is controlled directly by the fifth-root identities.

---

## 10. Relation to the previous TWIST data

There are now three exact descriptions of the same rational split-Weil datum:

```text
TWIST CM5 side
    four Galois branches
    diag(z,tau(z),tau^2(z),tau^3(z))

Hermitian W1 side
    H = diag(1,-beta,-1,beta)
    maximal isotropic K-plane

Markman secant side
    B ~=_Q K
    alpha = v(1)
    beta  = v(j)
    Pi((alpha tensor beta)_1) != 0
```

The same cyclic generator `j` that defines the public TWIST cyclotomic carrier now also supplies the explicit second secant class `beta=v(j)`.

No additional quadratic field or auxiliary root of unity is introduced.

---

## 11. What is and is not closed

### Closed at NON-CANONICAL note level

1. the exact four-dimensional secant space `B` for the cyclic `C4` CM5 datum;
2. a Q-linear identification `B ~= K`;
3. an explicit rational pair `alpha=v(1)`, `beta=v(j)`;
4. an exact `BB_1` census;
5. non-zero projection to every Weil line;
6. non-zero degree-zero/rank component;
7. satisfaction of Markman's cohomological genericity criterion.

### Not closed

1. `alpha` and `beta` have not been exhibited as Chern characters of **single coherent sheaves** on `X`;
2. no semiregularity statement is proved;
3. no flat deformation of an algebraic class is constructed;
4. no algebraicity theorem for the generic CM5 Weil classes is claimed;
5. nothing here changes Canon v83 or the public non-selection boundary.

At the special seed `X=B_0^2`, Gate E implies that the rational Hodge classes `alpha` and `beta` are algebraic combinations of divisor classes. This does **not** by itself provide the specific secant sheaves required by Markman's deformation argument.

---

## 12. The next gate: W2C

The remaining gap is no longer the Weil projection. It is the geometric realization of the explicit cohomological pair.

### Gate W2C: cyclic-C4 secant sheaf realization

For

\[
\alpha=v(1),
\qquad
\beta=v(j),
\]

seek coherent sheaves or explicit perfect complexes `G,G'` on

\[
X=B_0^2
\]

such that, after a single declared rational/integral scaling if required,

\[
ch(G)=\alpha,
\qquad
ch(G')=\beta.
\]

If exact equality by single sheaves is impossible, determine the minimal K-theoretic realization and identify the precise obstruction to replacing it by actual sheaves.

Only after such a realization survives should semiregularity of

\[
\Phi(G\boxtimes G'^\vee)
\]

be tested.

The breaker is explicit: if the cyclic-C4 rational pair cannot be represented by admissible secant sheaves, Markman's current sheaf mechanism does not yet close the algebraicity step for this TWIST-seeded family even though the cohomological genericity gate is solved.

---

## 13. Verdict

Gate W2B closes **AGREE** at the cohomological level.

The key exact statement is

\[
\boxed{
B\simeq_{\mathbf Q}K,
\qquad
\alpha=v(1),
\qquad
\beta=v(j),
\qquad
\Pi((\alpha\otimes\beta)_1)\neq0.
}
\]

In fact the chosen tensor also has non-zero scalar/rank component.

The unresolved problem has therefore moved cleanly from representation theory to geometry:

```text
CM5 carrier
 -> split Weil datum
 -> Markman F realization
 -> explicit rational secant pair        DONE
 -> actual secant sheaves                OPEN
 -> semiregularity                       OPEN
 -> algebraic deformation of HW          OPEN
```

That is the correct boundary after W2B.