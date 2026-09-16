# Hodge-Tate CM5: W2H non-decomposable Postnikov outer representative

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v84 and the companion Hodge-Tate / Markman / Perry CM5 notes through
`HODGE-TATE-CM5-W2G-B-WEAK-OUTER-NOGO-2026-09-11.md`.

**Date:** 2026-09-11.

This note opens **Gate W2H**. The preceding W2G-B no-go applies to the current Markman outer object because it is literally an external product. The goal here is to construct a genuinely non-external-product derived representative with the **same K-theory class and hence the same Markman cohomological Weil projection**.

The construction succeeds. It does not yet prove semiregularity. It produces a concrete new object on which the old factorwise obstruction `xi box id` is no longer automatic, and it reduces the next semiregularity calculation to one explicit finite dg endomorphism complex.

No `canon/` or registry file is changed. No algebraicity theorem is claimed.

---

## 1. The product object and its Ext decomposition

Let

\[
X=B\times B,
\qquad
B=\operatorname{Jac}(y^2=x^5-1),
\]

and let `G_1` be the simple scale-one secant sheaf from W2E-B,

\[
\operatorname{ch}(G_1)=\delta=-\gamma.
\]

Put

\[
Z:=X\times X,
\qquad
P:=G_1\boxtimes G_1^\vee.
\]

Since `G_1` is simple,

\[
\operatorname{End}(G_1)=\mathbf C,
\qquad
\operatorname{End}(G_1^\vee)=\mathbf C,
\]

and therefore

\[
\boxed{\operatorname{End}(P)=\mathbf C.}
\]

Write

\[
E_i:=\operatorname{Ext}^i_X(G_1,G_1),
\qquad
E_i^\vee:=\operatorname{Ext}^i_X(G_1^\vee,G_1^\vee).
\]

Kunneth gives

\[
\boxed{
\operatorname{Ext}^1_Z(P,P)
\cong E_1\oplus E_1^\vee.
}
\]

There is **no mixed first-order deformation direction**.

In degree two,

\[
\boxed{
\operatorname{Ext}^2_Z(P,P)
\cong
E_2
\oplus
(E_1\otimes E_1^\vee)
\oplus
E_2^\vee.
}
\]

The mixed factor

\[
\boxed{M:=E_1\otimes E_1^\vee}
\]

appears first in obstruction degree two.

W2E-B proved

\[
\dim E_1\ge399.
\]

Hence

\[
\boxed{
\dim M\ge399^2=159201.
}
\]

So the failure of the product ansatz is not a shortage of mixed data. The mixed data live one categorical degree higher than ordinary deformations.

---

## 2. Why an ordinary deformation cannot provide the desired escape

Every first-order deformation of `P` is represented by a pair

\[
(a,b)\in E_1\oplus E_1^\vee,
\]

namely a deformation of the first factor plus a deformation of the second factor.

Thus there is no first-order tangent vector which mixes the two factors.

The obvious attempts

- deform `G_1` and `G_1^vee` independently;
- translate the two factors;
- tensor by degree-zero line bundles;
- apply an identity-component Rouquier autoequivalence;

remain in the product/factorwise lane. Moreover semiregularity is invariant under derived equivalence, so merely moving `P` inside an autoequivalence orbit cannot repair the W2G-B failure.

A genuine W2H object must use the mixed degree-two sector `M` as **Postnikov data**, not as an ordinary tangent vector.

---

## 3. Choose two mixed obstruction classes

Choose

\[
\mu,\nu\in M
\subset\operatorname{Ext}^2_Z(P,P)
\]

which are linearly independent over `C`.

This is possible by the dimension estimate above. Concretely one may take

\[
\mu=a_1\boxtimes b_1,
\qquad
\nu=a_2\boxtimes b_2,
\]

with

\[
a_i\in E_1,
\qquad
b_i\in E_1^\vee,
\]

chosen so that the resulting two classes in `M` are independent.

They determine a morphism in the derived category

\[
 f_{\mu,\nu}:
 P^{\oplus2}\longrightarrow P[2],
 \qquad
 f_{\mu,\nu}=(\mu,\nu).
\]

Define

\[
\boxed{
P_{\mu,\nu}
:=\operatorname{Fib}(f_{\mu,\nu}).
}
\]

Thus there is a distinguished triangle

\[
P_{\mu,\nu}
\longrightarrow
P^{\oplus2}
\xrightarrow{(\mu,\nu)}
P[2]
\longrightarrow
P_{\mu,\nu}[1].
\]

This object is algebraic and perfect because `P` is perfect on the smooth projective variety `Z`.

---

## 4. The K-class and Chern character are exactly unchanged

In `K_0(Z)`, an even shift does not change sign. Therefore the triangle gives

\[
[P_{\mu,\nu}]
=2[P]-[P[2]]
=2[P]-[P]
=\boxed{[P]}.
\]

Consequently

\[
\boxed{
\operatorname{ch}(P_{\mu,\nu})
=\operatorname{ch}(P)
=\delta\boxtimes\delta^\vee.
}
\]

Let

\[
\Phi:D^b(Z)\xrightarrow{\sim}D^b(A)
\]

be Markman's Orlov equivalence to the split-Weil abelian eightfold

\[
A=X\times\widehat X.
\]

Set

\[
E_{\mu,\nu}:=\Phi(P_{\mu,\nu}).
\]

The cohomological Fourier-Mukai transform depends only on the Chern character, so

\[
\boxed{
\operatorname{ch}(E_{\mu,\nu})
=\operatorname{ch}(E),
}
\]

where `E=Phi(P)` is the old product-derived Markman object.

In particular the rank and first Chern class agree. Hence Markman's normalized class agrees exactly:

\[
\boxed{
\kappa(E_{\mu,\nu})=\kappa(E).
}
\]

Therefore every previously proved cohomological statement survives unchanged:

1. the class remains of Hodge type along the split-Weil deformation lane;
2. the `BB_1` component is nonzero on every required Weil line;
3. the `BB_0` scalar component is nonzero;
4. the projection to the four-dimensional space `HW` is exactly the same as before.

So W2H changes the **derived representative**, not the target Hodge class.

---

## 5. Its Postnikov data are explicit

Use the standard t-structure on `D^b(Z)`. Since `P` is a sheaf in degree zero and the defining map has cohomological degree two, the long exact cohomology sequence gives

\[
\boxed{
\mathcal H^{-1}(P_{\mu,\nu})\simeq P,
\qquad
\mathcal H^{0}(P_{\mu,\nu})\simeq P^{\oplus2},
}
\]

and all other cohomology sheaves vanish.

The only nontrivial Postnikov invariant is precisely

\[
\boxed{
(\mu,\nu)
\in
\operatorname{Ext}^2(P^{\oplus2},P).
}
\]

Thus the mixed outer information is now part of the object itself rather than merely an obstruction space around an external product.

---

## 6. The new object is indecomposable

Suppose

\[
P_{\mu,\nu}\simeq Q_1\oplus Q_2.
\]

Cohomology is additive. Since

\[
\mathcal H^{-1}(P_{\mu,\nu})\simeq P
\]

and `P` is simple, hence indecomposable, after relabelling we must have

\[
\mathcal H^{-1}(Q_1)=P,
\qquad
\mathcal H^{-1}(Q_2)=0.
\]

The second summand then has only degree-zero cohomology, so

\[
Q_2\simeq\mathcal H^0(Q_2).
\]

Moreover `H^0(Q_2)` is a direct summand of `P^2`. Since `End(P)=C`, every nonzero proper direct summand of `P^2` is isomorphic to one copy of `P` and corresponds to a one-dimensional subspace

\[
\ell\subset\mathbf C^2.
\]

Such a summand splits off the Postnikov object if and only if the Postnikov map vanishes on `ell`, i.e. if there is a nonzero pair `(a,b)` with

\[
a\mu+b\nu=0.
\]

But `mu,nu` were chosen linearly independent. Hence no such line exists.

Therefore

\[
\boxed{
P_{\mu,\nu}\text{ is indecomposable.}
}
\]

Equivalently, the endomorphism algebra is local: modulo the nilpotent ideal of endomorphisms acting trivially on cohomology, its degree-zero quotient is only the scalar algebra `C`.

---

## 7. It is not an external product

The stronger point needed for W2H is that `P_(mu,nu)` cannot be written

\[
P_{\mu,\nu}\simeq U\boxtimes V
\]

for objects `U,V in D^b(X)`.

For external products over `C`, t-cohomology satisfies the direct Kunneth decomposition

\[
\mathcal H^n(U\boxtimes V)
\simeq
\bigoplus_{p+q=n}
\mathcal H^p(U)\boxtimes\mathcal H^q(V).
\]

Our object has cohomology only in degrees `-1` and `0`, with the degree `-1` term equal to the simple external product `P=G_1 box G_1^vee`.

If both `U` and `V` had nonzero cohomology in two adjacent degrees, then the Kunneth decomposition would produce a nonzero degree `-2` term. Hence, after an overall shift, at most one factor can carry the two-step Postnikov structure; the other factor is concentrated in a single cohomological degree.

Therefore the Postnikov invariant of an external-product object with these cohomology sheaves must lie entirely in one of the two factorwise summands

\[
E_2\otimes 1
\qquad\text{or}\qquad
1\otimes E_2^\vee
\]

inside

\[
\operatorname{Ext}^2(P,P)
=
E_2
\oplus
(E_1\otimes E_1^\vee)
\oplus
E_2^\vee.
\]

But by construction both `mu` and `nu` lie in the **middle mixed summand**

\[
E_1\otimes E_1^\vee.
\]

This is impossible for an external product.

Hence

\[
\boxed{
P_{\mu,\nu}\text{ is genuinely non-external-product.}
}
\]

This is the first representative in the CM5 lane which preserves the exact Markman class while removing the categorical factorization used by the W2G-B no-go.

---

## 8. Why the previous kernel argument no longer applies formally

For the old object

\[
P=G_1\boxtimes G_1^\vee,
\]

a source class

\[
\xi\in\operatorname{Ext}^2(G_1,G_1)
\]

produced the canonical outer class

\[
\xi\boxtimes\operatorname{id}_{G_1^\vee}.
\]

That was the load-bearing W2G-B obstruction.

For `P_(mu,nu)`, an endomorphism of the cells descends to an endomorphism of the Postnikov object only if it is compatible with the `k`-invariant `(mu,nu)`. A source obstruction therefore has to commute with, or preserve, the two-dimensional mixed Postnikov datum.

There is no longer a formal factorwise map

\[
\ker\sigma_{G_1}^2
\longrightarrow
\ker\sigma_{P_{\mu,\nu}}^2
\]

obtained merely by tensoring with an identity.

This does **not** prove semiregularity. It proves that the precise mechanism which killed W2G-B has been removed.

---

## 9. Exact dg model for the next semiregularity calculation

Put

\[
\mathcal A:=\operatorname{RHom}_Z(P,P).
\]

The Kunneth quasi-isomorphism identifies it with

\[
\operatorname{RHom}_X(G_1,G_1)
\otimes
\operatorname{RHom}_X(G_1^\vee,G_1^\vee).
\]

Choose a connective dg model for `A`. The Postnikov object is represented as the two-cell perfect `A`-module

\[
\mathcal A^{\oplus2}\oplus\mathcal A[1]
\]

with twisting differential given by the row `(mu,nu)`.

Its derived endomorphism dg complex has, before taking cohomology, degree-`n` term

\[
\boxed{
C^n
=
M_2(\mathcal A^n)
\oplus
\mathcal A^n
\oplus
(\mathcal A^{n+1})^{\oplus2}
\oplus
(\mathcal A^{n-1})^{\oplus2},
}
\]

with differential

\[
\boxed{
d_C(x)=d_{\mathcal A}(x)+[q,x],
\qquad q=(\mu,\nu).
}
\]

Therefore

\[
\boxed{
\operatorname{Ext}^2(P_{\mu,\nu},P_{\mu,\nu})
=H^2(C^\bullet).
}
\]

This is now the exact W2H-B computational target. There is no need to search over arbitrary perfect complexes.

The semiregularity map can be evaluated on this same model using the Atiyah class of the twisted two-cell complex. The free parameters are only the choice of the two-dimensional subspace

\[
\langle\mu,\nu\rangle
\subset
E_1\otimes E_1^\vee.
\]

---

## 10. Relation to Markman and Perry

Markman's general CM construction uses the Chern character of the source outer object to produce the normalized class whose degree-four component projects nontrivially to `HW`. Since `P_(mu,nu)` has exactly the same K-class as `P`, this part of the argument is unchanged.

Perry's semiregularity theorem applies to perfect derived objects, so replacing the external-product representative by the present perfect Postnikov representative is compatible with the deformation-theoretic framework.

References:

- E. Markman, *Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication*, arXiv:2509.23079, current 2026 version.
- A. Perry, *The semiregularity theorem for equivariant noncommutative varieties*, arXiv:2604.00511, 2026.

---

## 11. W2H verdict

The **existence** part of W2H closes **AGREE**:

\[
\boxed{
\exists\,P_{\mu,\nu}\in D^b(X\times X)
\text{ such that }
[P_{\mu,\nu}]=[G_1\boxtimes G_1^\vee],
}
\]

with

\[
\boxed{
P_{\mu,\nu}
\text{ indecomposable and not an external product.}
}
\]

After Orlov transform it produces an object `E_(mu,nu)` with **exactly the same normalized Markman class and the same nonzero Weil projection** as the old object.

The semiregularity part remains open:

\[
\boxed{
\text{W2H-B: compute }H^2(C^\bullet)
\text{ and the semiregularity map for a mixed two-plane }\langle\mu,\nu\rangle.
}
\]

This is a genuine new lane. Unlike the previous product, scale, theta-descent, and weak-outer attempts, it removes the factorization responsible for the inherited source kernel rather than trying to suppress that kernel by symmetry.

---

## 12. Boundary

```text
current decomposable outer object          FAIL (W2G-B)
ordinary deformation to mixed object       NO MIXED Ext^1 DIRECTION
mixed Ext^2 Postnikov data                  AVAILABLE, dimension >=159201
same K-class / same Markman class           YES
indecomposable representative               YES
non-external-product representative         YES
old xi box id obstruction automatic         NO
semiregularity of new representative         OPEN
```

The next useful calculation is no longer another secant-class search. It is the explicit dg cohomology and Atiyah/semiregularity calculation for the two-cell Postnikov object above.