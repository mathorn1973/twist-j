# Hodge-Tate CM5: W2K-B exact contraction ranks and the 104-dimensional target

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v84 and the companion Hodge-Tate / Markman / Perry CM5 notes through
`HODGE-TATE-CM5-W2K-A-UNIVERSALLY-GLUABLE-OUTER-2026-09-12.md`.

**Date:** 2026-09-12.

This note starts the actual semiregularity calculation of **Gate W2K-B**. The result is an exact reduction: the source contraction map has rank `20`, the outer contraction map has rank `104`, and therefore the final semiregularity problem will close as soon as the corrected W2K-A outer object is shown to have

\[
\dim \operatorname{Ext}^2=104.
\]

The calculation also rules out a tempting shortcut: the W2J-C source cannot itself be semiregular, because its invariant/source `Ext^2` is already larger than the entire source semiregularity target.

No `canon/` or registry file is changed. No Hodge-conjecture theorem is claimed.

---

## 1. Markman's semiregularity diagram

For a perfect object `E` on a smooth projective variety, Markman's form of the Buchweitz-Flenner diagram is

\[
\begin{array}{ccc}
HT^2 &\xrightarrow{\operatorname{ob}_E}& \operatorname{Ext}^2(E,E)\\
\downarrow{\lrcorner\,\operatorname{ch}(E)}&&\downarrow\sigma_E\\
H\Omega_{-2}&=&H\Omega_{-2}.
\end{array}
\]

Thus

\[
\boxed{
(\,\cdot\,\lrcorner\operatorname{ch}(E))
=\sigma_E\circ\operatorname{ob}_E.
}
\]

Markman's Lemma 8.2.4 (numbering in the current 2026 HTML version of arXiv:2502.03415) states that if `ob_E` is surjective and its kernel equals the annihilator of `ch(E)`, then `E` is semiregular. We will use the even simpler rank consequence of the commutative diagram.

References:

- E. Markman, *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds*, arXiv:2502.03415, Section 8.2.
- A. Perry, *The semiregularity theorem for equivariant noncommutative varieties*, arXiv:2604.00511v2.

---

## 2. Split Hodge coordinates for the CM5 source class

The source is the mixed order-80 quotient of the CM5 abelian fourfold. Isogeny does not change the complex contraction rank, so compute upstairs in the real-embedding splitting used throughout the CM5 notes.

Let

\[
A=u_1+u_2,
\qquad
B=u_3+u_4,
\]

where `u_i=dz_i wedge dbar(z_i)` and `A^3=B^3=0`. Put

\[
q=\frac{5+\sqrt5}{2},
\qquad
q'=\frac{5-\sqrt5}{2},
\qquad
\varphi=\frac{1+\sqrt5}{2}.
\]

The scale-one secant Chern character is

\[
\boxed{
\bar\delta
=L+\delta_6,
}
\]

with

\[
\boxed{
L=2q'A+2qB
}
\]

and

\[
\boxed{
\delta_6
=-5\varphi^2A^2B
-5\varphi^{-2}AB^2.
}
\]

These are exactly the components of `delta=-v(j-j^{-1})` derived in W2C/W2E.

---

## 3. The source HT2 contraction has rank 20

For an abelian fourfold,

\[
HT^2
=H^2(O)\oplus H^1(T)\oplus H^0(\wedge^2T)
\]

has dimension

\[
6+16+6=28.
\]

The cap action on `bar delta=L+delta_6` separates into two independent Hodge blocks.

### 3.1. Middle target H^{1,3}

The summands

\[
H^2(O)\oplus H^0(\wedge^2T)
\]

map to `H^{1,3}` by

\[
(\eta,\xi)
\longmapsto
\eta\wedge L+\xi\lrcorner\delta_6.
\]

The exact twelve-column matrix over `Q(sqrt(5))` has

\[
\boxed{\operatorname{rank}=10.}
\]

Each six-column half separately has rank six; their images overlap in dimension two.

### 3.2. End target H^{0,2} plus H^{2,4}

The sixteen-dimensional summand `H^1(T)` maps by

\[
\theta
\longmapsto
(\theta\lrcorner L,\ \theta\lrcorner\delta_6)
\]

to

\[
H^{0,2}\oplus H^{2,4},
\]

and the exact matrix has

\[
\boxed{\operatorname{rank}=10.}
\]

The two Hodge targets in Sections 3.1 and 3.2 are disjoint. Therefore

\[
\boxed{
\operatorname{rank}
\bigl(HT^2(\bar X)\xrightarrow{\lrcorner\bar\delta}H\Omega_{-2}(\bar X)\bigr)
=20.
}
\]

Hence

\[
\boxed{
\dim\operatorname{ann}_{HT^2}(\bar\delta)=28-20=8.
}
\]

This rank is intrinsic and therefore unchanged by the order-80 isogeny/root-gerbe presentation.

---

## 4. The HT1 action is injective

Similarly

\[
HT^1=H^1(O)\oplus H^0(T)
\]

has dimension eight. The first summand wedges with `bar delta` and the second contracts it.

The exact eight-column matrix has rank

\[
\boxed{8.}
\]

so

\[
\boxed{
\operatorname{ann}_{HT^1}(\bar\delta)=0.
}
\]

This is the source hypothesis which appears in Markman's outer-product kernel calculation.

---

## 5. The source itself cannot be semiregular

W2H-B gave, for every order-80 source realization compatible with the theta descent,

\[
\boxed{r_H:=\dim\operatorname{Ext}^1(\mathscr G,\mathscr G)\ge12.}
\]

W2J-C constructed a Schur source. On the Calabi-Yau-four dimensional abelian/root-gerbe category, Serre duality and

\[
\chi(\mathscr G,\mathscr G)=10
\]

give

\[
\dim\operatorname{Ext}^2(\mathscr G,\mathscr G)
=8+2r_H
\ge32.
\]

But

\[
\dim H\Omega_{-2}(\bar X)
=\binom42+4^2+\binom42
=28.
\]

Thus

\[
\boxed{
\mathscr G\text{ cannot be semiregular.}
}
\]

This closes the possible shortcut through source semiregularity. The outer construction is genuinely necessary.

---

## 6. The outer contraction rank is 104

Let

\[
P=\mathscr G\boxtimes\mathscr G^\vee.
\]

The degree-two generalized deformation space decomposes as

\[
HT^2(\bar X\times\bar X)
\cong
HT^2(\bar X)
\oplus
\bigl(HT^1(\bar X)\otimes HT^1(\bar X)\bigr)
\oplus
HT^2(\bar X).
\]

Its dimension is

\[
28+64+28=120.
\]

For the external-product Chern character, the first and third summands act on one factor. Their kernels are the two eight-dimensional copies of

\[
\operatorname{ann}_{HT^2}(\bar\delta).
\]

The middle summand acts by the tensor product of the two `HT^1` actions. Section 4 shows these actions are injective, so the middle summand contributes no additional kernel.

Equivalently this is the linear-algebra content of Markman's outer-product kernel lemma.

Therefore

\[
\boxed{
\ker(\,\lrcorner\operatorname{ch}(P))
\cong
\operatorname{ann}_{HT^2}(\bar\delta)
\oplus
\operatorname{ann}_{HT^2}(\bar\delta),
}
\]

and

\[
\boxed{\dim\ker=16.}
\]

Hence

\[
\boxed{
\operatorname{rank}
\bigl(HT^2(\bar X\times\bar X)
\xrightarrow{\lrcorner\operatorname{ch}(P)}H\Omega_{-2}\bigr)
=120-16=104.
}
\]

Every W2H/W2K outer representative constructed in this lane has exactly the same Chern character, so the same rank `104` applies to the corrected universally-gluable object `R_(alpha,beta)` from W2K-A.

---

## 7. The final W2K-B criterion is only Ext2 <= 104

For

\[
R=R_{\alpha,\beta}
\]

from W2K-A, the semiregularity diagram gives

\[
(\,\cdot\,\lrcorner\operatorname{ch}(R))
=\sigma_R\circ\operatorname{ob}_R.
\]

Section 6 proves that the left side has rank `104`. Therefore

\[
\boxed{
\operatorname{rank}(\operatorname{ob}_R)\ge104.
}
\]

In particular

\[
\dim\operatorname{Ext}^2(R,R)\ge104.
\]

Now suppose one proves the opposite numerical inequality

\[
\boxed{
\dim\operatorname{Ext}^2(R,R)\le104.
}
\]

Then every inequality is forced to equality:

\[
\dim\operatorname{Ext}^2(R,R)=104,
\]

`ob_R` is surjective, and the semiregularity map has rank `104` on a `104`-dimensional domain. Hence

\[
\boxed{\sigma_R\text{ is injective}.}
\]

So the entire remaining semiregularity gate has been reduced to one exact Ext-dimension calculation.

No separate computation of the Atiyah trace matrix is needed if this upper bound is obtained.

---

## 8. Next gate

Call the remaining calculation **W2K-C**:

> Choose the generic Picard twists and the two degree-two arrows of W2K-A so that
> \[
> \dim\operatorname{Ext}^2(R_{\alpha,\beta},R_{\alpha,\beta})\le104.
> \]

A natural sufficient route is to prove that the generic cross-source complexes are IT2 with

\[
\operatorname{Ext}^k(\mathscr G\otimes\alpha,\mathscr G)=0
\quad(k\ne2),
\qquad
\dim\operatorname{Ext}^2=10,
\]

and then compute the finite two-cell dg differential for the outer three-cell diagram. The W2J-C model makes this a finite generic-rank problem.

---

## 9. Boundary

```text
source HT2 contraction rank               20
source HT2 annihilator dimension          8
source HT1 contraction rank               8
source semiregularity                      IMPOSSIBLE (Ext2 >=32 >28)
outer HT2 dimension                        120
outer Chern contraction rank               104
outer Chern annihilator dimension          16
W2K-A Ext<0=0                              DONE
final semiregularity sufficient condition  dim Ext2 <=104
final Ext2 upper bound                     OPEN (W2K-C)
```
