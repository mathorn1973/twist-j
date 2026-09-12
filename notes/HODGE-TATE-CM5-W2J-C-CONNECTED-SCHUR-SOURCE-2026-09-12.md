# Hodge-Tate CM5: W2J-C connected Schur source in the equivariant window

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v84 and the companion Hodge-Tate / Markman / Perry CM5 notes through
`HODGE-TATE-CM5-W2J-B-EFFECTIVE-THETA-CURVE-CORRECTION-2026-09-12.md`.

**Date:** 2026-09-12.

This note closes the source-object part of **Gate W2J**. W2J-B replaced the virtual correction by two actual genus-two theta curves on the mixed order-80 quotient. The remaining task was to connect those correction blocks to the divisor core without leaving the deformation window found in W2H-B.

The construction below produces a weight-one twisted perfect object

\[
\mathscr G\in\operatorname{Perf}(\mathfrak X)_{\mathrm{wt}=1}
\]

on the square-root gerbe

\[
\mathfrak X=\sqrt[2]{\bar{\mathcal L}/\bar X}
\]

such that

\[
\boxed{
\operatorname{ch}(\mathscr G)=\bar\delta,
\qquad
\operatorname{End}(\mathscr G)=\mathbf C,
\qquad
\dim\operatorname{Ext}^1(\mathscr G,\mathscr G)\le30.
}
\]

For a disjoint choice of the two theta curves the stronger bound is `<=24`. The construction is robust under at most two transverse intersection points, which removes the need for a delicate disjointness theorem in the common-divisor incidence.

This does **not** prove Perry semiregularity of the final Markman outer object. It closes the Schur/source deformation bottleneck and moves the programme to the final equivariant Postnikov semiregularity map.

No `canon/` or registry file is changed. No Hodge-conjecture theorem is claimed.

---

## 1. The three geometric cells

Keep the mixed order-80 quotient

\[
\pi:X\to\bar X
\]

from W2I and the two smooth genus-two theta curves of W2J-B,

\[
C_A,C_B\subset\bar X,
\qquad
[C_A]+[C_B]=\bar Q,
\]

with

\[
\bar L\cdot C_A
=
\bar L\cdot C_B
=5.
\]

Write

\[
p:\mathfrak X\to\bar X
\]

for the root-gerbe projection and `mathscr M` for its tautological weight-one line,

\[
\mathscr M^{\otimes2}=p^*\bar{\mathcal L}.
\]

We will use three cells:

1. a divisor core
   \[
   \mathscr F:=\mathscr M\otimes i_*\mathcal O_Y,
   \]
   where `Y` is an ample Cartier divisor algebraically equivalent to `bar L` and containing both curves;
2. a curve block
   \[
   \mathscr A:=\mathscr M\otimes j_{A*}N_A;
   \]
3. a second curve block
   \[
   \mathscr B:=\mathscr M\otimes j_{B*}N_B.
   \]

All three objects lie in the same weight-one twisted sector.

The common `mathscr M` twist cancels from all Ext calculations, so the dg calculation may be performed on `bar X` using

\[
F=i_*\mathcal O_Y,
\quad
A=j_{A*}N_A,
\quad
B=j_{B*}N_B.
\]

---

## 2. A common divisor containing the two theta curves exists

Let `S_A,S_B` denote translated copies of the two quotient abelian surfaces carrying the theta curves. Their addition map is an isogeny

\[
\mu:S_A^0\times S_B^0\to\bar X
\]

of degree five. Pulling `bar L` further to the original `B x B` gives the block-diagonal scale-one polarization `L`. Since finite pullback is injective on the Neron-Severi space, the cross term of `mu^* bar L` vanishes and

\[
\boxed{
\mu^*\bar L=L_A\boxtimes L_B,
}
\]

where both restrictions have type `(1,5)` and

\[
h^0(L_A)=h^0(L_B)=5.
\]

Let `Theta_A,Theta_B` be the principal polarizations obtained in W2J-B from the quotients of `2Theta`. Put

\[
P_A:=L_A-\Theta_A,
\qquad
P_B:=L_B-\Theta_B.
\]

These are again principal ample classes. Indeed, after pullback to the original `B`, their classes are respectively

\[
2(q'-1)\Theta,
\qquad
2(q-1)\Theta,
\]

where

\[
q=\frac{5+\sqrt5}{2},
\qquad
q'=\frac{5-\sqrt5}{2},
\]

and

\[
(q-1)(q'-1)=1.
\]

Both factors are totally positive. The exact quotient matrices also have Pfaffian one.

For a translate `D_x` of the principal theta divisor on `S_A`, the line bundle

\[
L_A(-D_x)
\]

is a degree-zero twist of the principal ample bundle `P_A`, hence has exactly one section. Thus there is a unique projective section line

\[
\ell_A(x)\subset H^0(S_A,L_A)
\]

whose divisor contains `D_x`. As `x` varies, these lines form a projective surface

\[
T_A\subset\mathbf P H^0(S_A,L_A)=\mathbf P^4.
\]

The image has dimension two: a fixed divisor of class `L_A` has only finitely many irreducible components and therefore cannot contain a positive-dimensional family of distinct theta translates. The same construction gives a projective surface `T_B`.

Now let

\[
r_A:H^0(\bar X,\bar L)\to H^0(S_A,L_A)
\]

be restriction, of rank `r`. Let `Sigma_A` be the projective set of global section lines whose restriction is either zero or lies on `T_A`. Then

\[
\boxed{\dim\Sigma_A\ge2.}
\]

This requires no surjectivity assumption on `r_A`:

- if `r<=2`, the projectivized kernel already has dimension at least two;
- if `r>=3`, projective dimension gives
  \[
  \dim(T_A\cap\mathbf P\operatorname{im}r_A)\ge r-3,
  \]
  and the projective preimage of one line has dimension `5-r`, giving total dimension at least two.

The same argument gives

\[
\dim\Sigma_B\ge2.
\]

Since

\[
\mathbf P H^0(\bar X,\bar L)=\mathbf P^4,
\]

the projective dimension theorem implies

\[
\boxed{\Sigma_A\cap\Sigma_B\ne\varnothing.}
\]

Hence some nonzero section defines an ample Cartier divisor `Y` containing one principal theta translate from each quotient surface.

The same argument is valid after an algebraically trivial twist of the support line bundle. Such a twist changes no Chern class. Varying the two surface cosets, the theta translates, and this degree-zero support twist gives the standard incidence family. The two surface cosets meet in five reduced points. Requiring a theta translate to pass through any prescribed one of these points is one divisor condition on its two-dimensional translation parameter. Therefore the locus in the common-section incidence where **three or more** of the five intersection points lie on both selected theta curves is a proper closed subset. We may consequently choose the common divisor so that

\[
\boxed{m:=|C_A\cap C_B|\le2,}
\]

with transverse intersections. The disjoint case `m=0` is allowed but is not required below.

No smoothness of `Y` is needed in the subsequent Ext calculation. It is an effective ample Cartier divisor, which is enough.

---

## 3. Choose the asymmetric curve line bundles

Let

\[
D_A:=C_A\cap C_B
\]

viewed as an effective reduced divisor on `C_A`, and let `D_B` be the same intersection divisor on `C_B`. Its degree is

\[
\deg D_A=\deg D_B=m\le2.
\]

Define

\[
\boxed{
N_A:=\mathcal O_{C_A}(D_A),
}
\]

and

\[
\boxed{
N_B:=K_{C_B}\otimes(\bar L|_{C_B})^{-1}\otimes\mathcal O_{C_B}(-D_B).
}
\]

Since both curves have genus two and `deg(bar L|C)=5`,

\[
\deg N_A=m,
\qquad
\deg N_B=-3-m.
\]

Thus

\[
\boxed{\deg N_A+\deg N_B=-3.}
\]

The corresponding Euler characteristics are

\[
\chi(N_A)=m-1,
\qquad
\chi(N_B)=-4-m,
\]

so

\[
\boxed{\chi(N_A)+\chi(N_B)=-5.}
\]

---

## 4. The Chern character is exactly bar delta

Set

\[
\mathscr A:=\mathscr M\otimes j_{A*}N_A,
\qquad
\mathscr B:=\mathscr M\otimes j_{B*}N_B.
\]

For a line bundle `N` on a curve `C` in an abelian fourfold,

\[
\operatorname{ch}(j_*N)
=[C]+\chi(N)[\mathrm{pt}].
\]

Tensoring with `mathscr M` adds

\[
\frac12\bar L\cdot C=\frac52
\]

to the top coefficient of each curve block. Hence

\[
\operatorname{ch}(\mathscr A)+\operatorname{ch}(\mathscr B)
=\bar Q
+
\left(
-5+\frac12(5+5)
\right)[\mathrm{pt}]
=\boxed{\bar Q}.
\]

The divisor core has

\[
\operatorname{ch}(\mathscr F)
=\bar\delta+\bar Q.
\]

Therefore any twisted complex whose K-class is

\[
[\mathscr F]-[\mathscr A]-[\mathscr B]
\]

has exactly

\[
\boxed{\operatorname{ch}=\bar\delta.}
\]

---

## 5. Exact cross-Ext calculation with the divisor core

Because all three cells have the same root-gerbe weight, tensoring by `mathscr M^{-1}` reduces Ext to the base.

Let

\[
F=i_*\mathcal O_Y,
\qquad
T=j_*N
\]

for a smooth curve `C subset Y`. The two-term resolution

\[
\mathcal O(-Y)\to\mathcal O\to F
\]

has zero restriction of its defining map to `C`. Therefore

\[
\boxed{
\operatorname{Ext}^k(F,T)
\cong
H^k(C,N)
\oplus
H^{k-1}(C,N\otimes\bar L|_C).
}
\]

This identity only uses that the section defining `Y` vanishes on `C`; it does not require `Y` to be smooth along `C`.

Serre duality on the abelian fourfold gives

\[
\operatorname{Ext}^k(T,F)
\cong
\operatorname{Ext}^{4-k}(F,T)^*.
\]

For `N_A=O(D_A)`, there is a canonical nonzero section

\[
s_A\in H^0(C_A,N_A)
\]

vanishing on all points of `D_A`. It determines a nonzero map

\[
\boxed{a:F\to A.}
\]

For `N_B`, one has

\[
N_B^{-1}\otimes K_{C_B}\otimes(\bar L|_{C_B})^{-1}
\simeq\mathcal O_{C_B}(D_B).
\]

Thus the canonical section of `O(D_B)` determines a nonzero class

\[
\boxed{b\in\operatorname{Ext}^2(B,F).}
\]

Both spaces have dimension at most two because `m<=2` and Clifford/Riemann-Roch on a genus-two curve gives

\[
h^0(O(D_A)),h^0(O(D_B))\le2.
\]

---

## 6. Maurer-Cartan compatibility

Use the shifted graded object

\[
\boxed{
E_{\rm gr}
=F\oplus A[-1]\oplus B[-1].
}
\]

Place the two degree-one arrows

\[
B[-1]\xrightarrow{\ b\ }F
\xrightarrow{\ a\ }A[-1].
\]

Their composition is supported on `C_A cap C_B`. At every transverse intersection point, the local Yoneda product is multiplication by the value of the section defining `a`. That section is the canonical section of `O(D_A)` and vanishes at every point of `D_A=C_A cap C_B`. Hence

\[
\boxed{a\circ b=0.}
\]

Therefore the two arrows satisfy the Maurer-Cartan equation and define an actual twisted perfect object

\[
\boxed{\mathscr G.}
\]

Its K-class is

\[
[\mathscr G]
=[\mathscr F]-[\mathscr A]-[\mathscr B],
\]

so Section 4 gives

\[
\boxed{\operatorname{ch}(\mathscr G)=\bar\delta.}
\]

---

## 7. The object is Schur

Each of the three cells is Schur. Moreover

\[
\operatorname{Hom}^0(F,A[-1])
=
\operatorname{Hom}^0(A[-1],F)
=0,
\]

and the same holds for `B[-1]` and `F`.

At a transverse intersection point of two distinct curves, the local Ext groups begin in degree one, so

\[
\operatorname{Hom}^0(A[-1],B[-1])
=
\operatorname{Hom}^0(B[-1],A[-1])
=0.
\]

Thus degree-zero endomorphisms of the underlying graded object are only three scalars

\[
(\lambda_F,\lambda_A,\lambda_B)\in\mathbf C^3.
\]

The twisted differential sends them to

\[
((\lambda_A-\lambda_F)a,
(\lambda_F-\lambda_B)b).
\]

Since both arrows are nonzero, its rank is two. Hence

\[
\boxed{
\operatorname{End}(\mathscr G)
=H^0\operatorname{RHom}(\mathscr G,\mathscr G)
\simeq\mathbf C.
}
\]

So the source is Schur.

---

## 8. The first-order deformation dimension is at most 30

The self-Ext dimensions of the three cells are known exactly:

\[
\dim\operatorname{Ext}^1(F,F)=12,
\]

and, from W2J-B,

\[
\dim\operatorname{Ext}^1(A,A)
=
\dim\operatorname{Ext}^1(B,B)
=6.
\]

Thus self terms contribute

\[
12+6+6=24
\]

to degree one of the endomorphism complex.

The two core-curve arrow spaces contribute at most

\[
h^0(O(D_A))+h^0(O(D_B))\le4.
\]

At each of the `m` transverse curve intersections, a local Koszul calculation gives

\[
\dim\operatorname{Ext}^1(A,B)
=
\dim\operatorname{Ext}^1(B,A)
=1
\]

per point. Hence the two cross directions contribute at most

\[
2m\le4.
\]

Therefore the raw degree-one endomorphism space has dimension

\[
\boxed{\dim D^1\le24+4+4=32.}
\]

The degree-zero differential has rank two by Section 7. Consequently

\[
\begin{aligned}
r_H
&:=\dim\operatorname{Ext}^1(\mathscr G,\mathscr G)\\
&=\dim\ker(D^1\to D^2)-2\\
&\le\dim D^1-2\\
&\le\boxed{30}.
\end{aligned}
\]

If the curves are disjoint, `m=0` and both arrow spaces are one-dimensional. Then

\[
\dim D^1=26,
\qquad
\boxed{r_H\le24.}
\]

Thus the W2H-B upper window is satisfied without needing the next differential explicitly.

---

## 9. There are enough mixed outer directions

The identity component of the Rouquier group of an abelian fourfold has dimension eight. The Schur object `mathscr G` has finite stabilizer: its codimension-one support is an ample divisor, whose translation stabilizer is finite, and a degree-zero tensor line fixing the generic rank-one part is trivial by weak Lefschetz for an ample Cartier divisor.

Hence the Rouquier orbit injects into first-order deformations and

\[
\boxed{r_H\ge8.}
\]

Therefore

\[
\dim\left(
\operatorname{Ext}^1(\mathscr G,\mathscr G)
\otimes
\operatorname{Ext}^1(\mathscr G^\vee,\mathscr G^\vee)
\right)
\ge64.
\]

In particular there are far more than the two independent invariant mixed classes needed for the W2H non-external Postnikov construction.

Combining with Section 8,

\[
\boxed{8\le r_H\le30.}
\]

The old dimension no-go is therefore gone.

---

## 10. Relation to the order-80 equivariant object

The root-gerbe quotient description is equivalent to the corresponding `H_mix`-equivariant twisted category upstairs. Pulling `mathscr G` back along the order-80 quotient gives an `H_mix`-equivariant source object with the original scale-one secant Chern character `delta`.

Its downstairs Ext groups are precisely the invariant Ext groups upstairs. Thus the number `r_H` in Section 8 is the invariant source deformation dimension entering W2H-B.

The Markman cohomological non-vanishing criterion depends only on the Chern character, so it is unchanged from W2B/W2C.

---

## 11. W2J verdict

The Schur/source part of W2J closes positively:

\[
\boxed{
\exists\,\mathscr G
\in\operatorname{Perf}(\mathfrak X)_{\mathrm{wt}=1}
}
\]

with

\[
\boxed{
\operatorname{ch}(\mathscr G)=\bar\delta,
\qquad
\operatorname{End}(\mathscr G)=\mathbf C,
\qquad
8\le\dim\operatorname{Ext}^1(\mathscr G,\mathscr G)\le30.
}
\]

The scale-one source, integrality, effectivity, Schur property, and deformation-size bottlenecks are therefore all removed.

The remaining gate is now genuinely the final categorical one:

> choose two invariant mixed classes for the non-external outer Postnikov object and compute Perry's equivariant/weak semiregularity map itself.

Call that next gate **W2K**.

---

## 12. Boundary

```text
mixed order-80 quotient                    DONE
primitive Qbar                              DONE
effective theta-curve realization           DONE
common ample Cartier support                DONE
exact twisted source ch=bar delta           DONE
source Schur                                DONE
r_H <= 30                                   DONE
mixed outer directions >=2                  DONE
non-external outer representative           DONE (W2H)
final Perry semiregularity map               OPEN (W2K)
```

W2J-C is the first point in this lane where every source-side requirement needed for the equivariant non-external Postnikov attack is simultaneously satisfied.