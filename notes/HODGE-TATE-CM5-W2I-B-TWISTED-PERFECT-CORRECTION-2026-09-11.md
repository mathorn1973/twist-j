# Hodge-Tate CM5: W2I-B exact twisted perfect correction

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v84 and the companion Hodge-Tate / Markman / Perry CM5 notes through the corrected
`HODGE-TATE-CM5-W2I-MIXED-ORDER80-QUOTIENT-2026-09-11.md`.

**Date:** 2026-09-11.

This note continues **Gate W2I-B** on the mixed order-80 quotient

\[
\pi:X\longrightarrow \bar X=X/H_{\rm mix}
\]

and the square-root gerbe

\[
\mathfrak X=\sqrt[2]{\bar{\mathcal L}/\bar X}.
\]

The previous note left one geometric obligation: realize the primitive correction class `bar Q` at scale one. For an **effective curve** this remains open. For Perry's twisted **perfect-complex** framework, however, the obstruction can be removed exactly.

The main result is:

\[
\boxed{
\text{there exists a weight-one perfect complex }\mathscr T\in\operatorname{Perf}(\mathfrak X)
\text{ with }\operatorname{ch}(\mathscr T)=\bar Q.
}
\]

Consequently there exists a weight-one perfect source representative with Chern character `bar delta` at scale one. It is not yet proved Schur/simple, and its deformation dimension `r_H` is not yet controlled. Thus this note closes the **perfect-realization** part of W2I-B but not the semiregularity gate.

No `canon/` or registry file is changed. No algebraicity theorem beyond the explicit cycle calculation below is claimed.

---

## 1. Integral divisor lattice used for the certificate

Write the standard integral Neron-Severi basis upstairs as

\[
N_0,\ldots,N_7.
\]

It is defined from the principal polarization on `B` and the Hermitian description

\[
\operatorname{NS}(B^2)
\simeq
\operatorname{Herm}_2(\mathcal O_K).
\]

Explicitly:

- `N_0,N_1` are the first-factor classes corresponding to `1,phi in O_F`;
- `N_2,N_3` are the same two classes on the second factor;
- for `k=0,1,2,3`, `N_(4+k)` is the cross Hermitian class corresponding to
  \[
  \begin{pmatrix}0&j^k\\ \bar j^k&0\end{pmatrix}.
  \]

The companion verifier writes these alternating forms in the public CM5 homology basis and checks integrality directly.

Define eight divisor classes

\[
D_0,\ldots,D_7\in\operatorname{NS}(\bar X)
\]

by the pullback relation

\[
\bigl(\pi^*D_0,\ldots,\pi^*D_7\bigr)
=
(N_0,\ldots,N_7)\,C,
\]

with

\[
\boxed{
C=
\begin{pmatrix}
0&-12&0&0&-8&2&10&-2\\
0&0&0&0&6&0&-10&2\\
-10&0&0&-8&0&-6&0&-2\\
10&-4&10&6&0&6&0&2\\
0&-4&-20&0&0&-2&0&2\\
0&-4&0&0&0&0&0&0\\
0&-4&0&0&0&0&0&2\\
0&-16&-20&0&0&0&0&2
\end{pmatrix}.
}
\]

For every column, the transformed alternating form

\[
B_{\rm mix}^{T}\left(\sum_r C_{ri}N_r\right)B_{\rm mix}
\]

is integral. Hence each column is an honest integral `(1,1)` class on `bar X`, and therefore an algebraic divisor class by Lefschetz `(1,1)`.

This basis is only a certificate basis; no nefness or effectivity of the individual `D_i` is asserted.

---

## 2. Exact integral divisor decomposition of bar Q

Using the corrected seven-term quotient coordinates of `bar Q`, exact exterior algebra gives

\[
\boxed{
\begin{aligned}
\bar Q={}&D_0D_3D_6
+2D_0D_5D_7
+2D_0D_7^2
+D_2D_3D_7\\
&-D_2D_4D_7
-2D_2D_7^2
+D_3^2D_4
+2D_3D_4D_7
-D_5D_6D_7.
\end{aligned}
}
\]

All coefficients are integers, and the equality is in integral degree-six cohomology.

Thus the primitive class `bar Q` lies in the **integral divisor-generated algebraic cycle lattice**. This is stronger than the earlier rational Hodge-generation statement.

The formula is signed. It does **not** prove that `bar Q` is the class of one effective curve. It does prove that no integral-Hodge obstruction remains for a perfect correction.

---

## 3. Koszul K-classes

For divisor classes `A,B,C` on `bar X`, define the virtual/perfect Koszul class

\[
\mathcal K(A,B,C)
:=
(1-[\mathcal O(-A)])
(1-[\mathcal O(-B)])
(1-[\mathcal O(-C)])
\in K_0(\bar X).
\]

It is represented by the tensor product of the three two-term complexes

\[
[\mathcal O(-A)\to\mathcal O],
\quad
[\mathcal O(-B)\to\mathcal O],
\quad
[\mathcal O(-C)\to\mathcal O],
\]

with arbitrary sections replaced by the corresponding formal perfect K-class when effectivity is not chosen.

On the abelian fourfold, `td(bar X)=1`, and through codimension four

\[
\operatorname{ch}\mathcal K(A,B,C)
=
ABC
-rac12ABC(A+B+C).
\]

Apply to the nine terms of Section 2 with the same integer coefficients. Let `K_Q` be the resulting signed perfect K-class.

The degree-six part is exactly `bar Q`. The degree-eight coefficient is also exact:

\[
\boxed{
\operatorname{ch}(K_Q)
=
\bar Q-9[\mathrm{pt}].
}
\]

The individual top terms, in the order of the nine monomials in Section 2, are

\[
-125,\ -15,\ -10,\ 90,\ 0,\ -50,\ -10,\ -12,\ -10,
\]

and after multiplication by the coefficients

\[
1,2,2,1,-1,-2,1,2,-1
\]

they sum to `-9`.

Thus the top-degree defect is integral and tiny.

---

## 4. Move to the weight-one root-gerbe sector

Let

\[
p:\mathfrak X\to\bar X
\]

be the square-root gerbe and let `mathscr M` be its tautological weight-one line object:

\[
\mathscr M^{\otimes2}\simeq p^*\bar{\mathcal L},
\qquad
\operatorname{ch}(\mathscr M)=e^{\bar L/2}.
\]

The corrected quotient arithmetic gives

\[
\boxed{
\int_{\bar X}\bar L\,\bar Q=10.
}
\]

Set

\[
K_Q':=K_Q+4[\mathcal O_p]
\]

for four skyscraper sheaves at points of `bar X`. Then

\[
\operatorname{ch}(K_Q')
=
\bar Q-5[\mathrm{pt}].
\]

Now tensor with the tautological weight-one line:

\[
\boxed{
\mathscr T
:=
\mathscr M\otimes p^*K_Q'.
}
\]

Because `bar Q` has codimension three, the only extra term from `e^(bar L/2)` is top degree:

\[
\operatorname{ch}(\mathscr T)
=
\bar Q
+rac12\bar L\bar Q
-5[\mathrm{pt}].
\]

Since

\[
\frac12\int\bar L\bar Q=5,
\]

the top term cancels exactly. Therefore

\[
\boxed{
\operatorname{ch}(\mathscr T)=\bar Q.
}
\]

This is an exact scale-one weight-one perfect correction.

---

## 5. A scale-one twisted perfect source exists

Choose a divisor

\[
\bar Y\in|\bar L|
\]

and write `i:bar Y -> bar X`. On the root gerbe, define

\[
\mathscr F_0:=i_*(\mathscr M|_{\bar Y}).
\]

As in the previous notes,

\[
\operatorname{ch}(\mathscr F_0)
=
\bar L+rac1{24}\bar L^3
=
\bar\delta+\bar Q.
\]

Consequently the perfect object

\[
\boxed{
\mathscr G_{\rm perf}
:=
\mathscr F_0\oplus\mathscr T[1]
}
\]

lies entirely in the weight-one twisted sector and satisfies

\[
\boxed{
\operatorname{ch}(\mathscr G_{\rm perf})
=
\bar\delta.
}
\]

Thus the **scale-one twisted perfect realization problem closes AGREE**.

The displayed representative is deliberately only an existence witness. It is decomposable, so it is not yet a useful semiregularity candidate.

---

## 6. What this resolves

The chain of possible obstructions is now shorter:

```text
mixed order-80 quotient                  DONE
corrected primitive bar Q                DONE
bar Q rational Hodge                     DONE
bar Q integral divisor-generated cycle   DONE
weight-one perfect correction ch=bar Q   DONE
scale-one twisted perfect ch=bar delta   DONE
Schur/simple twisted representative      OPEN
exact r_H                                OPEN
r_H <= 30                                OPEN
final invariant Postnikov semiregularity OPEN
```

In particular, W2I-B no longer depends on finding a single effective curve of class `bar Q`. Such a curve would still be geometrically interesting, but Perry's perfect/twisted framework does not require it for existence of the source K-class.

---

## 7. Next gate: W2J Schurization and deformation count

The useful next step is no longer cycle algebra. It is categorical.

Starting from the exact K-class above:

1. replace the decomposable witness `mathscr F_0 + mathscr T[1]` by a non-split twisted perfect object with the same Chern character;
2. prove
   \[
   \operatorname{End}(\mathscr G)=\mathbf C;
   \]
3. compute
   \[
   r_H=\dim\operatorname{Ext}^1(\mathscr G,\mathscr G);
   \]
4. test the W2H-B window
   \[
   \boxed{12\le r_H\le30.}
   \]

A cone or Postnikov construction using morphisms between the divisor-supported term and the correction complex is the natural next candidate. Unlike the old outer-product obstruction, this is now a finite dg-endomorphism problem on one fixed twisted K-class.

---

## 8. Reproduction

The companion verifier

```text
notes/HODGE-TATE-CM5-W2I-B-PERFECT-CORRECTION-VERIFY.py
```

reconstructs the eight quotient divisor classes from the integral CM5 Hermitian NS basis, verifies their quotient integrality, and checks exactly:

```text
bar Q divisor-triple identity      PASS
nine Koszul top defect             -9
integral Lbar.Qbar                 10
base correction after 4 points     Qbar - 5[pt]
weight-one gerbe correction         Qbar
```

No floating point is used in the mathematical checks.

---

## 9. Verdict

W2I-B closes positively at the perfect-complex level:

\[
\boxed{
\exists\,\mathscr G_{\rm perf}\in\operatorname{Perf}(\mathfrak X)_{\rm wt=1},
\qquad
\operatorname{ch}(\mathscr G_{\rm perf})=\bar\delta.
}
\]

The remaining gate is not algebraicity of the correction class. It is **Schurization plus deformation control**.