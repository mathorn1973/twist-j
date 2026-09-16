# Hodge-Tate CM5: W2K-A universally-gluable outer repair

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v84 and the companion Hodge-Tate / Markman / Perry CM5 notes through
`HODGE-TATE-CM5-W2J-C-CONNECTED-SCHUR-SOURCE-2026-09-12.md`.

**Date:** 2026-09-12.

This note opens **Gate W2K** and corrects one missing hypothesis in the earlier W2H outer construction.

Perry's abelian semiregularity theorem requires the final perfect complex `E` to satisfy

\[
\boxed{\operatorname{Ext}^{<0}(E,E)=0.}
\]

The W2H object

\[
\operatorname{Fib}(P^{\oplus2}\to P[2])
\]

was useful and correct as a non-external representative with the desired K-class, but its repeated identical cells force a two-dimensional `Ext^{-1}`. Hence it is **not** itself a legitimate final input to Perry's theorem.

The present note repairs this by replacing the repeated cells with three pairwise generically Picard-twisted copies of the W2J-C Schur source. The new three-cell outer object has:

\[
\boxed{
\operatorname{ch}(R)=\operatorname{ch}(P),
\qquad
\operatorname{Ext}^{<0}(R,R)=0,
}
\]

while retaining two independent degree-two Postnikov arrows and breaking the old factorwise kernel mechanism.

Semiregularity itself remains open and is Gate **W2K-B**.

No `canon/` or registry file is changed. No Hodge-conjecture theorem is claimed.

---

## 1. Perry's negativity hypothesis

Perry's Theorem 1.2 for families of abelian varieties assumes that the weakly equivariantly semiregular perfect complex `E_0` also satisfies

\[
\operatorname{Ext}^{<0}(E_0,E_0)=0.
\]

This is independent of semiregularity. It is the standard universal-gluability condition required for the deformation space of the object to behave as an algebraic space near the given point.

Reference:

- A. Perry, *The semiregularity theorem for equivariant noncommutative varieties*, arXiv:2604.00511v2, Theorems 1.1 and 1.2.

Perry also explicitly emphasizes that perfect complexes and twisted derived categories are allowed, so the derived/root-gerbe source lane remains within the intended framework.

---

## 2. Correction to the W2H final-Perry interpretation

Let

\[
P=\mathscr G\boxtimes\mathscr G^\vee
\]

be the outer product of a source object, and consider the W2H two-cell object

\[
R_{\rm old}
=\operatorname{Fib}
\left(P^{\oplus2}\xrightarrow{(\mu,\nu)}P[2]\right).
\]

As a twisted two-cell complex it has cells

\[
U=P^{\oplus2},
\qquad
V=P[1],
\]

with the degree-one twisting arrow `q:U -> V[1]`.

The degree `-1` endomorphism complex contains

\[
\operatorname{Hom}^{-1}(U,V)
=\operatorname{Hom}(P^{\oplus2},P)
\simeq\mathbf C^2.
\]

Both `q` and these degree `-1` maps have the same source and target. Their graded commutators therefore vanish: neither composition is defined through a third cell. Thus the two-dimensional space survives the twisted differential.

Hence

\[
\boxed{
\dim\operatorname{Ext}^{-1}(R_{\rm old},R_{\rm old})\ge2.
}
\]

So the precise correction is:

```text
W2H same-K non-external representative        VALID
W2H removal of xi box id formal obstruction   VALID
W2H as final Perry Theorem 1.2 object          INVALID: Ext^{-1} != 0
```

This note replaces only the last line.

---

## 3. The W2J-C source is already universally gluable

Let

\[
\mathscr G
\in\operatorname{Perf}(\mathfrak X)_{\rm wt=1}
\]

be the Schur source constructed in W2J-C on the mixed order-80 quotient root gerbe. Recall

\[
\operatorname{ch}(\mathscr G)=\bar\delta,
\qquad
\operatorname{End}(\mathscr G)=\mathbf C,
\qquad
8\le r_H:=\dim\operatorname{Ext}^1(\mathscr G,\mathscr G)\le30.
\]

Its graded model has the three cells

\[
F,
\qquad
A[-1],
\qquad
B[-1],
\]

with arrows

\[
B[-1]\to F\to A[-1].
\]

There are no negative self-Ext groups.

Indeed the only potentially new degree `-1` maps are of the form

\[
A[-1]\to F[-1],
\qquad
B[-1]\to F[-1],
\]

which are ordinary maps from the curve sheaves to the divisor core. The core is generically rank one and torsion-free on the Cartier divisor while the curves have smaller-dimensional support, so these maps vanish. All other degree `-1` and lower cell maps are negative Ext groups of coherent sheaves and vanish.

Therefore

\[
\boxed{
\operatorname{Ext}^{<0}(\mathscr G,\mathscr G)=0.
}
\]

The same argument applies after tensoring by a degree-zero line bundle pulled back from `bar X`.

---

## 4. Generic Picard twists are Hom-orthogonal

For

\[
\alpha\in\operatorname{Pic}^0(\bar X)
\]

put

\[
\mathscr G_\alpha:=\mathscr G\otimes p^*\alpha.
\]

Tensoring by `alpha` preserves the root-gerbe weight and the Chern character.

We need twists for which

\[
\operatorname{Hom}(\mathscr G_\alpha,\mathscr G)=0
\quad\text{and}\quad
\operatorname{Hom}(\mathscr G,\mathscr G_\alpha)=0.
\]

For the explicit three-cell model this is a direct generic-vanishing statement.

First, for the divisor core `F=i_*O_Y`,

\[
\operatorname{Hom}(F\otimes\alpha,F)
=H^0(Y,\alpha^{-1}|_Y).
\]

Restriction

\[
\operatorname{Pic}^0(\bar X)\to\operatorname{Pic}^0(Y)
\]

is injective for an ample Cartier divisor. A nontrivial numerically trivial line bundle on a connected projective variety has no nonzero section. Hence this Hom group vanishes for every nontrivial `alpha`.

For either curve cell `T=j_*N`,

\[
\operatorname{Hom}(T\otimes\alpha,T)
=H^0(C,\alpha^{-1}|_C),
\]

which vanishes outside the proper kernel of

\[
\operatorname{Pic}^0(\bar X)\to\operatorname{Pic}^0(C).
\]

Between the two distinct curve supports there is no degree-zero Hom because they share no irreducible component.

Finally W2J-C gave

\[
\operatorname{Ext}^k(F,T)
\cong
H^k(C,N)\oplus H^{k-1}(C,N\otimes\bar L|_C).
\]

Therefore

\[
\operatorname{Ext}^3(F,T)=0,
\]

and CY4 Serre duality gives

\[
\operatorname{Ext}^1(T,F)=0.
\]

These are precisely the shifted core-curve terms which could otherwise appear in degree-zero maps of the three-cell source.

Consequently there is a dense open set

\[
U\subset\operatorname{Pic}^0(\bar X)
\]

such that for every `alpha in U`

\[
\boxed{
\operatorname{Hom}(\mathscr G_\alpha,\mathscr G)
=
\operatorname{Hom}(\mathscr G,\mathscr G_\alpha)
=0.
}
\]

The negative cross-Ext groups vanish as well by the same cell-degree argument used in Section 3.

Choose

\[
\alpha,\beta\in U
\]

so that also

\[
\alpha\beta^{-1},\ \beta\alpha^{-1}\in U.
\]

Then the three objects

\[
\mathscr G_0:=\mathscr G,
\qquad
\mathscr G_1:=\mathscr G_\alpha,
\qquad
\mathscr G_2:=\mathscr G_\beta
\]

are pairwise Hom-orthogonal in both directions and pairwise have no negative Ext.

---

## 5. There are automatically enough degree-two arrows

W2J-C gives the invariant/source self Euler characteristic

\[
\boxed{
\chi(\mathscr G,\mathscr G)=10.
}
\]

A degree-zero Picard twist has trivial Chern character, hence for every `alpha`

\[
\chi(\mathscr G_\alpha,\mathscr G)=10.
\]

For the generic twists chosen above, degree zero vanishes in both directions. CY4 Serre duality therefore also gives

\[
\operatorname{Ext}^4(\mathscr G_\alpha,\mathscr G)=0.
\]

There are no negative Ext groups, and on a fourfold there are no Ext groups above degree four. Thus if

\[
e_i(\alpha)
:=
\dim\operatorname{Ext}^i(\mathscr G_\alpha,\mathscr G),
\]

then

\[
10=-e_1(\alpha)+e_2(\alpha)-e_3(\alpha).
\]

Hence

\[
\boxed{
e_2(\alpha)
=10+e_1(\alpha)+e_3(\alpha)
\ge10.
}
\]

The same statement holds for the dual twists needed below.

So the universally-gluable repair does not trade away the required Postnikov arrows: every admissible generic twist supplies at least a ten-dimensional space of degree-two arrows.

---

## 6. Three numerically identical outer cells

Work in the source product category underlying the Markman transform. Put

\[
P_0
:=
\mathscr G_0\boxtimes\mathscr G_0^\vee,
\]

\[
P_1
:=
\mathscr G_1\boxtimes\mathscr G_0^\vee,
\]

and

\[
P_2
:=
\mathscr G_0\boxtimes\mathscr G_2^\vee.
\]

Because `alpha,beta in Pic^0`,

\[
\operatorname{ch}(\mathscr G_1)
=
\operatorname{ch}(\mathscr G_2)
=
\operatorname{ch}(\mathscr G_0).
\]

Therefore

\[
\boxed{
\operatorname{ch}(P_0)
=\operatorname{ch}(P_1)
=\operatorname{ch}(P_2).
}
\]

Choose nonzero classes

\[
a\in\operatorname{Ext}^2(\mathscr G_1,\mathscr G_0),
\]

and

\[
b\in\operatorname{Ext}^2(\mathscr G_2^\vee,\mathscr G_0^\vee).
\]

They give outer degree-two maps

\[
\mu:=a\boxtimes\operatorname{id}_{\mathscr G_0^\vee}
\in\operatorname{Ext}^2(P_1,P_0),
\]

\[
\nu:=
\operatorname{id}_{\mathscr G_0}\boxtimes b
\in\operatorname{Ext}^2(P_2,P_0).
\]

Set

\[
U:=P_1\oplus P_2.
\]

---

## 7. The corrected outer Postnikov object

Define

\[
\boxed{
R_{\alpha,\beta}
:=
\operatorname{Fib}
\left(
U\xrightarrow{(\mu,\nu)}P_0[2]
\right).
}
\]

Its K-class is

\[
[R_{\alpha,\beta}]
=[P_1]+[P_2]-[P_0].
\]

Since all three Chern characters agree,

\[
\boxed{
\operatorname{ch}(R_{\alpha,\beta})
=\operatorname{ch}(P_0).
}
\]

After the Markman/Orlov equivalence the normalized class, the `BB_0` and `BB_1` data, and the nonzero projection to the four-dimensional Hodge-Weil space are therefore exactly the same as in W2B-W2H.

Thus the repair changes only the derived representative, not the Hodge class being transported.

---

## 8. The corrected object has no negative self-Ext

Represent `R_(alpha,beta)` by the two-cell twisted object with cells

\[
U=P_1\oplus P_2,
\qquad
V=P_0[1],
\]

and degree-one twisting arrow `q=(mu,nu)`.

All pairwise negative Ext groups between `P_0,P_1,P_2` vanish because they are external products of the pairwise universally-gluable source twists from Section 4.

The only additional degree `-1` term introduced by the shift of `V` is

\[
\operatorname{Hom}(U,P_0)
=
\operatorname{Hom}(P_1,P_0)
\oplus
\operatorname{Hom}(P_2,P_0).
\]

Kunneth and Section 4 give

\[
\operatorname{Hom}(P_1,P_0)
=
\operatorname{Hom}(\mathscr G_1,\mathscr G_0)
\otimes
\operatorname{End}(\mathscr G_0^\vee)
=0,
\]

and similarly

\[
\operatorname{Hom}(P_2,P_0)=0.
\]

Hence the entire degree `-1` endomorphism term vanishes. Lower degrees vanish for the same pairwise-negative-Ext reason.

Therefore

\[
\boxed{
\operatorname{Ext}^{<0}
(R_{\alpha,\beta},R_{\alpha,\beta})=0.
}
\]

This is the missing Perry hypothesis.

---

## 9. Why the old factorwise kernel is no longer formal

The W2G-B no-go for the original product object used the canonical embedding

\[
\xi
\longmapsto
\xi\boxtimes\operatorname{id}
\]

of a source semiregularity kernel into the outer obstruction space.

For the present object, an endomorphism class must be compatible with two different Picard-twisted cells and with the two Postnikov arrows

\[
P_1\xrightarrow{\mu}P_0[2],
\qquad
P_2\xrightarrow{\nu}P_0[2].
\]

There is no common identity factor which canonically extends an arbitrary source class across all three cells. Compatibility is a genuine twisted-dg condition.

Moreover the displayed cell diagram uses a first-factor Picard displacement in `P_1` and a second-factor displacement in `P_2`. A factorwise two-stage external-product construction can vary only one factor across its Postnikov cells; realizing both independent Picard directions would require the missing fourth cross cell

\[
\mathscr G_1\boxtimes\mathscr G_2^\vee.
\]

Thus the three-cell `L`-shaped Postnikov diagram is not the tensor product of two one-factor two-cell diagrams. This is the categorical feature required to avoid the old inherited-kernel argument.

The note does not need a stronger classification theorem asserting that no accidental external-product presentation exists after arbitrary derived equivalence. Perry semiregularity is tested directly on the explicit universally-gluable object above.

---

## 10. Equivariance survives the repair

The source object `mathscr G` lives on the mixed order-80 quotient/root-gerbe category, equivalently in the corresponding `H_mix`-equivariant twisted category upstairs.

A line bundle `alpha in Pic^0(bar X)` pulls back with its canonical descent linearization. Therefore the Picard-twisted sources `G_1,G_2`, the outer cells `P_i`, the degree-two arrows chosen in the quotient/invariant Ext groups, and the final object `R_(alpha,beta)` all define equivariant objects in the same finite-group framework.

After the Markman equivalence the finite group becomes a subgroup of the identity-component Rouquier group of the split-Weil abelian eightfold, exactly as required by Perry's abelian theorem.

---

## 11. W2K-A verdict

The Perry-prerequisite repair closes **AGREE**:

\[
\boxed{
\exists\ R_{\alpha,\beta}
\text{ with }
\operatorname{ch}(R_{\alpha,\beta})
=\operatorname{ch}(P_0)
}
\]

and

\[
\boxed{
\operatorname{Ext}^{<0}(R_{\alpha,\beta},R_{\alpha,\beta})=0.
}
\]

The object remains equivariant, has the same Markman/Hodge-Weil class, and no longer carries the repeated-cell `Ext^{-1}` defect of W2H.

The final unresolved gate is now precisely:

> **W2K-B:** compute the equivariant/weak semiregularity map
> \[
> \sigma^2_{R_{\alpha,\beta}}:
> \operatorname{Ext}^2(R_{\alpha,\beta},R_{\alpha,\beta})^G
> \longrightarrow HH_{-2}
> \]
> (or equivalently the semiregularity map of its lift in the invariant/twisted category) and prove or disprove injectivity.

No additional source-side or universal-gluability obligation remains.

---

## 12. Boundary

```text
W2H old same-class nonexternal witness          VALID
W2H old object Ext<0=0                          FAIL (Ext^-1 >= 2)
W2J-C Schur source                              DONE
W2J-C source Ext<0=0                            DONE
generic Picard Hom-orthogonal source twists     DONE
cross Ext^2 arrows                              >= 10-dimensional
same outer Chern/Markman class                   DONE
corrected outer Ext<0=0                         DONE
equivariance/descent                            DONE
final Perry semiregularity map                   OPEN (W2K-B)
```
