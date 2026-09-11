# Hodge-Tate CM5: W2K-C generic IT2 breaker

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v84 and the companion Hodge-Tate / Markman / Perry CM5 notes through
`HODGE-TATE-CM5-W2K-B-CONTRACTION-RANKS-2026-09-12.md`.

**Date:** 2026-09-12.

W2K-B reduced final semiregularity to the single upper bound

\[
\dim\operatorname{Ext}^2(R,R)\le104.
\]

It suggested one natural route: choose Picard twists so that every nontrivial source cross-complex is IT2,

\[
\operatorname{Ext}^k(\mathscr G_\alpha,\mathscr G)=0
\quad(k\ne2),
\qquad
\dim\operatorname{Ext}^2(\mathscr G_\alpha,\mathscr G)=10.
\]

The present note proves that this route is impossible. Under exactly that IT2 hypothesis, the two degree-two outer arrows of W2K-A are forced to be factorwise. The twisted endomorphism differential is then too sparse and one gets the exact formula

\[
\boxed{
\dim\operatorname{Ext}^2(R,R)
=3r^2+26r+32,
}
\]

where

\[
r=\dim\operatorname{Ext}^1(\mathscr G,\mathscr G).
\]

Since W2E-A gives `r>=12`, the smallest possible value is

\[
\boxed{776>104.}
\]

Thus the generic-IT2 shortcut closes **FAIL**. The next construction must deliberately retain nonzero source cross-`Ext^1` or cross-`Ext^3` so that the outer degree-two Postnikov arrows acquire genuinely mixed Kunneth components.

No `canon/` or registry file is changed. No semiregularity theorem is claimed.

---

## 1. Source self-Ext dimensions

Let `G` be a Schur source in the mixed order-80 quotient/twisted category. Put

\[
r:=\dim\operatorname{Ext}^1(G,G).
\]

The invariant/source Euler characteristic is

\[
\chi(G,G)=10.
\]

CY4 Serre duality and Schurity give

\[
\boxed{
\dim\operatorname{Ext}^{0,1,2,3,4}(G,G)
=(1,r,8+2r,r,1).
}
\]

Write

\[
s_0=1,\quad s_1=r,\quad s_2=8+2r,\quad s_3=r,\quad s_4=1.
\]

---

## 2. The IT2 hypothesis

Choose pairwise Hom-orthogonal Picard twists `G_0,G_1,G_2` as in W2K-A and assume the strongest generic-vanishing profile

\[
\boxed{
\operatorname{Ext}^\bullet(G_i,G_j)
=(0,0,10,0,0)
\quad(i\ne j).
}
\]

This profile has the correct Euler characteristic `10` and is compatible with CY4 duality.

Form the three outer cells

\[
P_0=G_0\boxtimes G_0^\vee,
\qquad
P_1=G_1\boxtimes G_0^\vee,
\qquad
P_2=G_0\boxtimes G_2^\vee.
\]

The self-Ext dimensions of any `P_i` are the convolution `s*s`. In particular

\[
\boxed{
\dim\operatorname{Ext}^1(P_i,P_i)=2r,
}
\]

and

\[
\boxed{
\dim\operatorname{Ext}^2(P_i,P_i)
=r^2+4r+16.
}
\]

For `P_1` and `P_0`, Kunneth gives

\[
\operatorname{Ext}^n(P_1,P_0)
\cong
\operatorname{Ext}^2(G_1,G_0)
\otimes
\operatorname{Ext}^{n-2}(G_0^\vee,G_0^\vee).
\]

Hence the cross dimensions are

\[
\boxed{
10,\ 10r,\ 10(8+2r),\ 10r,\ 10
}
\]

in degrees `2,...,6`. The same holds for `P_2` versus `P_0`.

Finally

\[
\operatorname{Ext}^\bullet(P_1,P_2)
\]

is concentrated in degree four, where it has dimension `100`.

---

## 3. Every degree-two arrow is factorwise

Under the IT2 assumption,

\[
\operatorname{Ext}^2(P_1,P_0)
=
\operatorname{Ext}^2(G_1,G_0)
\otimes
\operatorname{End}(G_0^\vee).
\]

Since `G_0` is Schur,

\[
\operatorname{End}(G_0^\vee)=\mathbf C.
\]

Therefore every nonzero degree-two arrow has the form

\[
\boxed{\mu=a\boxtimes\operatorname{id}.}
\]

Likewise every degree-two arrow from `P_2` to `P_0` has the form

\[
\boxed{\nu=\operatorname{id}\boxtimes b.}
\]

So the IT2 hypothesis removes exactly the mixed Kunneth components that would be needed to make the outer twisting differential large.

---

## 4. Raw endomorphism dimensions of the W2K-A object

Let

\[
R=\operatorname{Fib}
\left(
P_1\oplus P_2
\xrightarrow{(\mu,\nu)}P_0[2]
\right).
\]

Represent it by the two-cell twisted object with

\[
U=P_1\oplus P_2,
\qquad
V=P_0[1].
\]

Let `D^n` be the degree-`n` term of the raw twisted endomorphism complex.

From the self and cross dimensions above one obtains

\[
\boxed{
\dim D^1=6r+20,
}
\]

and

\[
\boxed{
\dim D^2=3r^2+32r+48.
}
\]

The formulas are direct Kunneth bookkeeping:

- three diagonal self-Ext contributions;
- the two shifted `P_i -> P_0` cross contributions;
- no degree-two `P_1 <-> P_2` term, because that cross group begins in degree four.

---

## 5. Exact ranks of d1 and d2

The twisted differential is the graded commutator with

\[
q=(\mu,\nu).
\]

The IT2 condition makes its rank completely transparent.

### 5.1. Rank of d1

Consider `mu=a box id`. A positive-degree self class in the **first** source factor cannot compose nontrivially with `a`, because that would land in a cross Ext group of degree strictly larger than two, which vanishes by IT2.

The only degree-one classes detected by `mu` are therefore the degree-one self classes in the unchanged second factor. Their difference across the two cells gives rank `r`.

The arrow `nu=id box b` analogously detects the degree-one classes in the unchanged first factor, again with rank `r`.

The two image blocks lie in independent cross summands. Hence

\[
\boxed{\operatorname{rank}(d_1)=2r.}
\]

### 5.2. Rank of d2

The same argument in degree two shows that `mu` only sees the unchanged-factor group

\[
\operatorname{Ext}^2(G_0^\vee,G_0^\vee)
\]

of dimension

\[
8+2r,
\]

and `nu` sees the corresponding degree-two group in the first factor. Again the two image blocks are independent.

The reverse degree-two cross classes pair with `a` or `b` only into top degree and therefore contribute to later differentials, not to additional rank in `d_2:D^2->D^3` beyond these two unchanged-factor blocks.

Thus

\[
\boxed{
\operatorname{rank}(d_2)=2(8+2r)=16+4r.
}
\]

The companion verifier realizes the minimal graded category explicitly and reproduces these ranks by exact finite-field row reduction.

---

## 6. Exact Ext2 dimension

Since

\[
\operatorname{Ext}^2(R,R)
=\ker d_2/\operatorname{im}d_1,
\]

Sections 4 and 5 give

\[
\begin{aligned}
\dim\operatorname{Ext}^2(R,R)
&=(3r^2+32r+48)
-(2r)
-(16+4r)\\
&=\boxed{3r^2+26r+32}.
\end{aligned}
\]

The order-80 theta audit gave

\[
r\ge12.
\]

Therefore

\[
\boxed{
\dim\operatorname{Ext}^2(R,R)
\ge
3\cdot12^2+26\cdot12+32
=776.
}
\]

But W2K-B proved that semiregularity would require

\[
\dim\operatorname{Ext}^2(R,R)=104.
\]

Hence

\[
\boxed{776>104.}
\]

The generic-IT2 route is impossible by a factor of more than seven even at the smallest allowed source deformation dimension.

---

## 7. What the breaker teaches us

The failure is structural, not a bad choice of the two vectors `a,b`.

Under IT2, the degree-two arrow space itself factorizes:

\[
\operatorname{Ext}^2(P_1,P_0)
=V_{10}\otimes\mathbf C\operatorname{id},
\]

so no choice of `a` can create a mixed Kunneth term. The differential has no access to the large first-factor self-Ext algebra.

To obtain a genuinely large twisting differential one must retain source cross groups in odd degree. For example, if

\[
\operatorname{Ext}^1(G_1,G_0)\ne0,
\]

then

\[
\operatorname{Ext}^2(P_1,P_0)
\]

contains the additional mixed summand

\[
\operatorname{Ext}^1(G_1,G_0)
\otimes
\operatorname{Ext}^1(G_0^\vee,G_0^\vee).
\]

This is exactly the kind of component which can couple both factors simultaneously.

Therefore the next gate must **not** maximize generic vanishing. It must design a universally-gluable pair of numerically identical source objects with

\[
\boxed{
\operatorname{Hom}=0,
\qquad
\operatorname{Ext}^1\ne0,
}
\]

while preserving enough degree-two arrows and the order-80 equivariant structure.

Call that redesign **W2K-D**.

---

## 8. Boundary

```text
W2K-B required Ext2 target              104
generic source cross IT2 profile        (0,0,10,0,0)
outer degree-2 arrows under IT2          factorwise only
rank d1                                 2 r
rank d2                                 16+4 r
Ext2 final formula                       3r^2+26r+32
minimum r                                12
minimum Ext2 under IT2                   776
IT2 route                                FAIL
required next feature                    Hom=0 but cross Ext1 !=0
```
