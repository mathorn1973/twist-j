# Hodge–Tate CM5: exact realization in Markman's general F-construction

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v83 and the companion notes
`HODGE-AND-TATE-CM5-CALIBRATION-2026-09-11.md`,
`HODGE-TATE-CM5-INTEGRAL-HOMOLOGY-CALIBRATION-2026-09-11.md`,
`HODGE-TATE-CM5-HODGE-CENSUS-2026-09-11.md`,
`HODGE-TATE-CM5-GENERALIZED-WEIL-EIGHTFOLD-2026-09-11.md`, and
`HODGE-TATE-CM5-HERMITIAN-SPLIT-W1-2026-09-11.md`.

**Date:** 2026-09-11.

This note carries out the next comparison step in the direct CM5 generalized-Weil lane. It places the explicit TWIST-seeded split Weil eightfold inside Eyal Markman's general construction from a totally real field `F`, an `F`-linear polarization on an abelian variety `X`, and a CM quadratic extension `K/F`.

No `canon/` file is changed, no public claim is registered, no formal public probe is started, and no algebraicity theorem is claimed.

---

## 1. Result

Put

\[
K=\mathbf Q(j)=\mathbf Q(\zeta_5),
\qquad
F=K^+=\mathbf Q(\sqrt5),
\]

and let

\[
\tau(j)=j^2,
\qquad
\iota=\tau^2.
\]

Thus `Gal(K/Q)=<tau> ~= C4` and `iota` is complex conjugation.

Let

\[
B=\operatorname{Jac}(y^2=x^5-1)
\]

with the CM realization established in the preceding notes. Set

\[
X=B\times B.
\]

There is an exact `F`-action

\[
\widehat\eta(a)
=\operatorname{diag}(a,\tau(a)),
\qquad a\in F,
\]

and an exact `F`-valued alternating polarization `Theta` on `X` whose rational trace is the product principal polarization.

For the intrinsic CM generator

\[
s:=j-j^{-1}
\]

one has

\[
\boxed{s^2=-q},
\qquad
\boxed{q=\varphi+2=\frac{5+\sqrt5}{2}\in F},
\]

with `q` totally positive.

Applying Markman's general `F`-construction to

\[
(F,K,X,\widehat\eta,\Theta,q)
\]

produces a `K`-action on

\[
A=X\times\widehat X.
\]

After identifying `Xhat` with `X` rationally through the product principal polarization, this Markman action is explicitly conjugate over `K` to

\[
\boxed{
\eta_{\rm TW}(z)
=\operatorname{diag}
\bigl(z,\tau(z),\tau^2(z),\tau^3(z)\bigr),
\qquad z\in K,
}
\]

which is exactly the four-Galois-branch `K`-action used in the preceding TWIST generalized-Weil note.

The same conjugation sends Markman's canonical split half-dimensional `K`-isotropic subspace to

\[
\boxed{
K(e_0+e_2)\oplus K(e_1+e_3),
}
\]

which is exactly the isotropic plane found independently in Gate W1.

Thus the TWIST-seeded eightfold is not merely analogous to Markman's general CM-field construction. At the rational/isogeny level it is an explicit specialization of it.

The present comparison is **not** an integral `GL(Z)` identification. The conjugating matrices contain elements of `K`; the conclusion is an equality of rational endomorphism data, equivalently an isogeny-level statement.

---

## 2. The intrinsic quadratic extension K/F

Define

\[
s=j-j^{-1}=j-j^4.
\]

Complex conjugation gives

\[
\bar s=-s.
\]

Using

\[
j^2+j^3=-\varphi,
\]

one obtains

\[
s^2
=j^2+j^3-2
=-\varphi-2.
\]

Hence

\[
\boxed{
K=F(s),
\qquad
s^2=-q,
\qquad
q=\varphi+2=\frac{5+\sqrt5}{2}.
}
\]

The conjugate real embedding of `F` sends

\[
q\longmapsto
\frac{5-\sqrt5}{2}>0,
\]

so `q` is totally positive, exactly as required in Markman's split-Weil setup.

Let

\[
\beta=\varphi^{-1}.
\]

Direct cyclotomic reduction gives

\[
\boxed{\tau(s)=\beta s},
\]

and therefore

\[
\boxed{
\tau(q)=\beta^2q
=\frac{5-\sqrt5}{2}.
}
\]

This already records an important difference from the biquadratic special cases: here

\[
q\notin\mathbf Q.
\]

---

## 3. An exact F-polarization on X=B x B

The previous calibration identifies

\[
H_1(B,\mathbf Q)\simeq K
\]

with the principal alternating form `Omega_1`.

Define the `F`-valued alternating form

\[
\theta_0(x,y)
:=\frac1{5}
\operatorname{Tr}_{K/F}
\bigl(sx\bar y\bigr),
\qquad x,y\in K.
\]

Because `bar(s)=-s`, the form is alternating. It is `F`-bilinear for the natural `F`-action, and

\[
\operatorname{Tr}_{F/\mathbf Q}\theta_0(x,y)
=
\frac1{5}
\operatorname{Tr}_{K/\mathbf Q}
(sx\bar y)
=\Omega_1(x,y).
\]

On the second copy of `B`, let `F` act through the nontrivial real automorphism `tau|_F`, and define

\[
\theta_1(x,y):=\tau\bigl(\theta_0(x,y)\bigr).
\]

Then

\[
\theta_1(\tau(a)x,y)
=a\theta_1(x,y)
\qquad(a\in F),
\]

so `theta_1` is `F`-bilinear for the twisted action. Moreover

\[
\operatorname{Tr}_{F/\mathbf Q}\theta_1
=
\operatorname{Tr}_{F/\mathbf Q}\theta_0
=\Omega_1.
\]

Therefore on

\[
X=B\times B
\]

we may take

\[
\boxed{
\Theta=\theta_0\oplus\theta_1.
}
\]

Its rational trace is

\[
\boxed{
\operatorname{Tr}_{F/\mathbf Q}\Theta
=\Omega_1\oplus\Omega_1,
}
\]

the product principal polarization on `X`.

Thus the exact TWIST CM data satisfy the input hypotheses of Markman's general `F` construction without adding a foreign field or a foreign polarization.

---

## 4. Markman's maximal isotropic subspace

Let `U` denote the rank-four `F` carrier underlying the first rational (co)homology of `X`. Let

\[
L:U^*\longrightarrow U
\]

be contraction with `Theta`.

For

\[
K=F(s),
\qquad s^2=-q,
\]

Markman's pure-spinor construction uses the maximal isotropic `K`-subspace

\[
W
=
\left\{
(-sL\lambda,\lambda):
\lambda\in U^*\otimes_FK
\right\}
\subset
(U\oplus U^*)\otimes_FK.
\]

Its complex-conjugate partner is

\[
\iota(W)
=
\left\{
(sL\lambda,\lambda):
\lambda\in U^*\otimes_FK
\right\}.
\]

Markman's `K`-action is characterized by scalar multiplication by `z` on `W` and by `iota(z)` on `iota(W)`.

The next section writes this action as an explicit rational block matrix.

---

## 5. Exact block formula for the K-action

Write

\[
z=a+bs,
\qquad a,b\in F.
\]

On `U\oplus U^*`, the action characterized above is

\[
\boxed{
\eta_z(u,v)
=
\bigl(
\widehat\eta(a)u
+
\widehat\eta(bq)Lv,
\quad
\widehat\eta(a)v
-
\widehat\eta(b)L^{-1}u
\bigr).
}
\]

Indeed, for a vector of `W`,

\[
(u,v)=(-sL\lambda,\lambda),
\]

the first component becomes

\[
-a sL\lambda+bqL\lambda
=-s(a+bs)L\lambda,
\]

because `s^2=-q`, while the second becomes

\[
a\lambda+bs\lambda=(a+bs)\lambda.
\]

Thus `W` has eigencharacter `z`; the conjugate calculation gives eigencharacter `iota(z)` on `iota(W)`.

After using `L` to identify `U^*` with `U`, the same action has the compact form

\[
\boxed{
\eta_{a+bs}
=
\begin{pmatrix}
\widehat\eta(a)&\widehat\eta(bq)\\
-\widehat\eta(b)&\widehat\eta(a)
\end{pmatrix}.
}
\]

This formula is the exact bridge between Markman's `F` construction and the four-branch TWIST action.

---

## 6. Splitting into the two real embeddings of F

The `F`-action on

\[
X=B\times B
\]

was chosen as

\[
\widehat\eta(a)=\operatorname{diag}(a,\tau(a)).
\]

Hence the displayed Markman matrix splits into two independent `2 x 2` blocks.

For the first real embedding:

\[
M_z^{(0)}
=
\begin{pmatrix}
a&bq\\
-b&a
\end{pmatrix}.
\]

For the second:

\[
M_z^{(1)}
=
\begin{pmatrix}
\tau(a)&\tau(bq)\\
-\tau(b)&\tau(a)
\end{pmatrix}.
\]

Both blocks can be diagonalized over `K` by a completely explicit basis change.

---

## 7. Exact diagonalization to the four TWIST Galois branches

Define

\[
C_0
=
\begin{pmatrix}
-s&s\\
1&1
\end{pmatrix},
\qquad
C_1
=
\begin{pmatrix}
-\tau(s)&\tau(s)\\
1&1
\end{pmatrix}.
\]

Their determinants are

\[
-2s\neq0,
\qquad
-2\tau(s)\neq0,
\]

so both are invertible over `K`.

A direct multiplication using `s^2=-q` gives

\[
\boxed{
C_0^{-1}M_z^{(0)}C_0
=
\operatorname{diag}
\bigl(z,\iota(z)\bigr).
}
\]

Applying `tau` to the same identity gives

\[
\boxed{
C_1^{-1}M_z^{(1)}C_1
=
\operatorname{diag}
\bigl(\tau(z),\tau^3(z)\bigr).
}
\]

Therefore, with

\[
C=C_0\oplus C_1
\]

and one fixed permutation of the middle coordinates,

\[
\boxed{
C^{-1}\eta_z C
=
\operatorname{diag}
\bigl(
z,\tau(z),\tau^2(z),\tau^3(z)
\bigr).
}
\]

This is precisely the `K`-action frozen in
`HODGE-TATE-CM5-GENERALIZED-WEIL-EIGHTFOLD-2026-09-11.md`.

Consequently

\[
\boxed{
\text{TWIST four-branch seed}
\simeq_{\mathbf Q,\,\mathrm{isog}}
\text{Markman general-F seed}.
}
\]

The equality is rational/isogeny-level. It is not asserted that `C` preserves the integral homology lattice.

---

## 8. Matching the split plane with Gate W1

Markman's splitness construction starts from a maximal `F`-isotropic subspace for `Theta`. Since

\[
\Theta=\theta_0\oplus\theta_1
\]

is the orthogonal sum of two rank-two alternating `F` spaces, choose one nonzero isotropic vector

\[
y_0
\]

from the first summand and one

\[
y_1
\]

from the second. Their span is a maximal `F`-isotropic plane.

The corresponding Markman `K`-plane in the `U^*` half is

\[
Z
=
K(0,y_0)
\oplus
K(0,y_1).
\]

In the first `2 x 2` block,

\[
\binom01
=
\frac12
\left[
\binom{-s}{1}
+
\binom{s}{1}
\right].
\]

Thus the diagonalization by `C_0` sends the first Markman isotropic direction to the sum of the `z` and `iota(z)` eigendirections.

Similarly, the second block sends the second isotropic direction to the sum of the `tau(z)` and `tau^3(z)` eigendirections.

After ordering the four branches as

\[
(1,\tau,\iota,\tau^3),
\]

we obtain

\[
\boxed{
Z
\longmapsto
K(e_0+e_2)
\oplus
K(e_1+e_3).
}
\]

This is exactly the maximal isotropic plane obtained independently in Gate W1 from the explicit Hermitian form

\[
H=\operatorname{diag}(1,-\beta,-1,\beta).
\]

Hence the split geometry agrees at the level of the actual isotropic half-space, not only at the level of a determinant or signature.

---

## 9. Polarization caveat

There are two related but distinct compatible polarizations in the present discussion.

1. Gate W1 used the product principal polarization on `B^4` and proved directly that its `K`-Hermitian form is split.
2. Markman's Section 8 constructs an ample compatible polarization `Xi_t` from a suitable totally imaginary `t in K_-` and proves splitness using the `F`-isotropic plane above.

The present note identifies the rational `K`-action and the split plane exactly. It does **not** claim that Markman's particular `Xi_t` is literally equal to the product polarization used in W1.

That equality is unnecessary for the present bridge: both structures lie on the same rational split `K` carrier, and the TWIST seed already has an independently verified compatible split polarization.

---

## 10. Why the cyclic C4 case is not Markman's currently explicit sheaf example

The general Markman construction applies to an arbitrary CM field `K/F`. His current survey explicitly formulates the secant-space and deformation strategy for general CM fields, while the fully implemented algebraicity theorem is still restricted to lower-dimensional cases with imaginary quadratic `K`.

The detailed companion paper goes further for real multiplication, but its explicit quartic example in Section 11.2.1 is the case

\[
[K:\mathbf Q]=4,
\qquad
\operatorname{Gal}(K/\mathbf Q)
\cong C_2\times C_2.
\]

Our field is instead

\[
\boxed{
K=\mathbf Q(\zeta_5),
\qquad
\operatorname{Gal}(K/\mathbf Q)\cong C_4.
}
\]

The obstruction is already visible in the exact extension parameter:

\[
q=\frac{5+\sqrt5}{2}
\in F\setminus\mathbf Q,
\]

and

\[
\tau(q)=\frac{5-\sqrt5}{2}\neq q.
\]

Thus the specialized biquadratic secant-sheaf formulas cannot simply be copied into the CM5 lane.

This is a precise boundary, not a failure of the general `F` construction. The general `F` construction matches our seed exactly; the missing step is the **explicit cyclic-C4 secant-sheaf realization** needed to push the algebraicity method further.

---

## 11. The general secant space is nevertheless present

For Markman's general construction the secant space `mathcal B` has dimension

\[
\dim_{\mathbf Q}\mathcal B
=2^{[F:\mathbf Q]}.
\]

Here

\[
[F:\mathbf Q]=2,
\]

so

\[
\boxed{
\dim_{\mathbf Q}\mathcal B=4.
}
\]

Therefore

\[
\boxed{
\dim_{\mathbf Q}(\mathcal B\otimes\mathcal B)=16.
}
\]

The Weil-Hodge target has

\[
\boxed{
\dim_{\mathbf Q}HW=4.
}
\]

Markman's general criterion provides a Zariski-open condition in
`mathcal B tensor mathcal B` under which the normalized characteristic class has a nonzero Weil component. That criterion is formulated before the later specialized sheaf examples and therefore belongs to the general CM-field construction.

So the next obstacle is not a dimension shortage and not absence of a cohomological map. It is to find **explicit algebraic representatives** in the cyclic-C4 secant space with the required nonzero Weil projection, and then control their deformation/semiregularity.

---

## 12. Gate W2A verdict

The comparison asked for in this note closes positively:

\[
\boxed{
\text{Gate W2A: Markman-F realization = AGREE.}
}
\]

More explicitly:

```text
native TWIST field K=Q(zeta5)
        |
        |  F=Q(sqrt5),  s=j-j^-1,  s^2=-q
        v
X=B x B with F-action diag(a,tau(a))
        |
        |  exact F-polarization Theta
        v
Markman A=X x Xhat
        |
        |  explicit K-rational diagonalization
        v
four Galois branches
(z, tau z, tau^2 z, tau^3 z)
        |
        |  split-plane comparison
        v
K(e0+e2) + K(e1+e3)
```

Every arrow above is exact rational algebra.

---

## 13. Next gate: W2B, cyclic-C4 secant criterion

The next gate should stay inside the same field and should not jump to a biquadratic substitute.

### Gate W2B: explicit CM5 secant pair

Freeze the following obligations.

1. Construct the four-dimensional rational secant space
   `mathcal B subset H^even(X,Q)` explicitly for
   \[
   X=B^2,
   \qquad
   F=\mathbf Q(\sqrt5),
   \qquad
   K=\mathbf Q(\zeta_5).
   \]
2. Express its four pure-spinor generators exactly in the divisor-generated cohomology of `B^2`.
3. Compute the general Markman map
   \[
   \mathcal B\otimes\mathcal B
   \longrightarrow
   HW(A,\eta)
   \]
   in a fixed rational basis.
4. Exhibit explicit rational
   \[
   \alpha,\beta\in\mathcal B
   \]
   whose tensor has nonzero Weil projection and satisfies the full general open-condition criterion.
5. Only after the cohomological gate passes, ask whether `alpha` and `beta` are Chern characters of actual coherent/perfect objects with the deformation properties required by the secant-sheaf method.
6. Treat semiregularity as an independent final gate; do not infer it from the cohomological calculation.

Gate E is useful here: every rational Hodge class on `B^2` is already generated by divisors and therefore algebraic. This makes the seed cohomology unusually explicit. It does **not** by itself supply the coherent sheaves or semiregularity required for deformation to a generic Weil eightfold.

---

## 14. Breakers and nonclaims

This note is weakened or falsified if any of the following exact statements fails:

1. `s^2=-(phi+2)`;
2. `q=(5+sqrt5)/2` is not totally positive;
3. `Tr_(F/Q)(Theta)` is not the product `Omega_1` polarization;
4. the block formula for Markman's `K` action fails to have `W` and `iota(W)` as the two eigen-subspaces;
5. either matrix `C_0` or `C_1` fails to diagonalize its block as stated;
6. the resulting four characters differ from `(1,tau,tau^2,tau^3)`;
7. Markman's split plane does not map to the W1 plane.

No such breaker is presently seen.

The note does **not** claim:

- an integral equivalence of the Markman and TWIST lattices;
- equality of Markman's `Xi_t` with the product polarization;
- existence of a cyclic-C4 secant sheaf satisfying the required deformation theorem;
- semiregularity of any object in the present eightfold case;
- algebraicity of the generic four-dimensional CM5 Weil space;
- a new theorem on the Hodge conjecture;
- any physical L1-to-L6 lift.

---

## 15. External references

- E. Markman, *Secant sheaves and Weil classes on abelian varieties*, arXiv:2509.23403, current v2 (2026). The paper formulates the general CM-field construction, the split-Weil period domain, the secant-space strategy, and states that full implementation is currently limited to lower-dimensional imaginary-quadratic cases.
- E. Markman, *Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication*, arXiv:2509.23079 (2025). This contains the detailed general-`F` construction and the explicit quartic examples; its Section 11.2.1 treats the biquadratic `C2 x C2` quartic case.

## Internal anchors

- `notes/HODGE-TATE-CM5-INTEGRAL-HOMOLOGY-CALIBRATION-2026-09-11.md`
- `notes/HODGE-TATE-CM5-HODGE-CENSUS-2026-09-11.md`
- `notes/HODGE-TATE-CM5-GENERALIZED-WEIL-EIGHTFOLD-2026-09-11.md`
- `notes/HODGE-TATE-CM5-HERMITIAN-SPLIT-W1-2026-09-11.md`
- `canon/CANON.md`, Public Canon v83.
