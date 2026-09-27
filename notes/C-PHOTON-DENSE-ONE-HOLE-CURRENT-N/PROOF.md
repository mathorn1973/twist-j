# Proof - C-PHOTON-DENSE-ONE-HOLE-CURRENT-N

**Status:** candidate-T, PUBLIC NON-CANONICAL.
**Owner:** #1204.
**Author:** A. M. Thorn <thorn@twistj.com>.
**Date:** 2026-09-27.
**Frozen preregistration commit:** \`5ad0eac6708e1df2d100769943bf3805f203b3a4\`.

No Canon status is asserted here.

## 1. Cross-section matching

Let

\[
Y=(\mathbb Z/L\mathbb Z)^3,
\qquad
y=(x_1,x_2,x_3),
\]

with even \(L\). Define \(P\) to contain the positive \(e_1\)-edge based at
\(y\) exactly when

\[
x_1\equiv x_2\pmod2.
\]

At a vertex \(y\), the two incident \(e_1\)-edges have bases \(y\) and
\(y-e_1\). Their base \(x_1\) parities are opposite. Exactly one therefore
satisfies the displayed condition. Hence

\[
\boxed{P\text{ is a perfect matching of }Y.}             \tag{1}
\]

Let \(G=Y\setminus P\). All \(e_2\)- and \(e_3\)-edges remain in \(G\).
To cross from \(x_1\) to \(x_1+1\), the positive \(e_1\)-edge at the current
vertex must have \(x_1\not\equiv x_2\pmod2\). If this fails, take one \(e_2\)
step, which flips the parity of \(x_2\), use the now available \(e_1\)-edge,
and later undo the auxiliary \(e_2\) displacement if desired.

Thus arbitrary changes in \(x_1,x_2,x_3\) can be composed from edges of \(G\).
Therefore

\[
\boxed{G\text{ is connected}.}                           \tag{2}
\]

## 2. The plaquette field

Put

\[
\sigma(y)=(-1)^{x_1+x_2+x_3}.
\]

Define a two-chain \(n_L\) independent of \(x_0\) by

\[
n_{02}(x)=n_{03}(x)=\sigma(y),
\]

and

\[
n_{01}(x)
=
\begin{cases}
0,&(y,y+e_1)\in P,\\
\sigma(y),&\text{otherwise}.
\end{cases}                                             \tag{3}
\]

All spatial plaquettes vanish. Every coefficient is in
\(\{-1,0,1\}\).

Use the standard oriented boundary

\[
\partial p_{0i}(x)
=
e_0(x)+e_i(x+e_0)-e_0(x+e_i)-e_i(x).
\]

For a fixed \(e_0(x)\), the two incident \(0i\)-plaquettes contribute

\[
n_{0i}(x)-n_{0i}(x-e_i).                               \tag{4}
\]

For \(i=2,3\), both faces are occupied and \(\sigma(y-e_i)=-\sigma(y)\), so
each pair contributes \(2\sigma(y)\).

For \(i=1\), exactly one of the two faces
\(p_{01}(x)\) and \(p_{01}(x-e_1)\) is deleted by the perfect matching.
If \(p_{01}(x)\) is deleted, then

\[
0-n_{01}(x-e_1)
=
-\sigma(y-e_1)
=
\sigma(y).
\]

If the other face is deleted, the contribution is directly \(\sigma(y)\).
Thus the \(01\) pair contributes one further \(\sigma(y)\).

Therefore

\[
\boxed{
\partial n_L(e_0(x))
=
5\sigma(y).
}                                                       \tag{5}
\]

Now fix a spatial edge \(e_i\), \(i=1,2,3\). The only nonzero incident
plaquettes containing that edge are \(p_{0i}\). They occur as a pair shifted
by \(e_0\). Since \(n_L\) is independent of \(x_0\), their signed boundary
contributions cancel exactly. Hence

\[
\boxed{
\partial n_L(e_i(x))=0,\qquad i=1,2,3.
}                                                       \tag{6}
\]

So

\[
j_L:=\partial n_L/5
\]

is the integer conserved current

\[
\boxed{
j_L(e_0(x))=\sigma(y),\qquad
j_L(e_i(x))=0\ (i=1,2,3).
}                                                       \tag{7}
\]

Every \(e_0\)-edge is charged and no spatial edge is charged. Therefore

\[
\boxed{M_L=|{\rm supp}\,j_L|=L^4.}                      \tag{8}
\]

## 3. Zero total homology

For each \(y\in Y\), the \(e_0\)-edges with that fixed cross-section
coordinate form one noncontractible coordinate loop of winding
\(\sigma(y)e_0\).

The total winding is therefore

\[
e_0\sum_{y\in Y}\sigma(y).
\]

Because \(L\) is even,

\[
\sum_{x_i=0}^{L-1}(-1)^{x_i}=0
\]

for each cross-section coordinate. Hence

\[
\sum_{y\in Y}\sigma(y)
=
\left(\sum_{x_1}(-1)^{x_1}\right)
\left(\sum_{x_2}(-1)^{x_2}\right)
\left(\sum_{x_3}(-1)^{x_3}\right)
=
0.
\]

Thus

\[
\boxed{[j_L]=0\in H_1(T^4,\mathbb Z).}                  \tag{9}
\]

This is consistent with \(j_L=\partial n_L/5\).

## 4. Exact face count

All \(02\)- and \(03\)-plaquettes are occupied, contributing

\[
2L^4.
\]

For \(01\)-plaquettes, at every fixed \((x_0,x_2,x_3)\) the condition
\(x_1\equiv x_2\pmod2\) holds for exactly \(L/2\) values of \(x_1\). Those are
deleted, leaving \(L/2\) occupied \(01\)-plaquettes. Therefore the \(01\)
support has size \(L^4/2\).

Hence

\[
\boxed{
A_L=|{\rm supp}\,n_L|
=
\frac52L^4.
}                                                       \tag{10}
\]

Combining (8) and (10),

\[
\boxed{\frac{A_L}{M_L}=\frac52.}                        \tag{11}
\]

So any universal support inequality \(A_K\ge cM_K\) valid for all augmented
components must have \(c\le5/2\).

## 5. Edge degrees

Consider one \(e_0(x)\). The incident pair of \(01\)-plaquettes contributes
exactly one occupied face. Both \(02\)-plaquettes are occupied and both
\(03\)-plaquettes are occupied. Thus its occupied degree is

\[
1+2+2=5.
\]

Equation (5) says their five signed incidences are aligned. Every \(e_0\)-edge
is therefore a charged degree-five junction.

Now consider a spatial \(e_1\)-edge. Its two incident \(01\)-plaquettes are
shifted only in \(x_0\), and the occupancy rule is independent of \(x_0\).
Hence either both are missing, giving degree zero, or both are occupied.
In the occupied case their boundary signs are opposite, so the edge is
neutral degree two.

Every \(e_2\)- and \(e_3\)-edge has exactly its two \(0i\)-plaquettes occupied,
again with opposite signed incidences. These are neutral degree-two edges.

Therefore the only occupied degrees are

\[
\boxed{d_e\in\{2,5\},}                                  \tag{12}
\]

and every neutral matching is unique.

The exact census is

\[
E_5=L^4,
\qquad
E_2=\frac52L^4,
\qquad
E_0=\frac12L^4.
\]

Indeed

\[
5E_5+2E_2
=
5L^4+5L^4
=
10L^4
=
4A_L.
\]

## 6. One augmented component

Associate to every occupied cross-section edge \(g\in G\) the strip of
\(0i\)-plaquettes above \(g\) as \(x_0\) runs around the torus.

Along a fixed strip, consecutive plaquettes share the corresponding spatial
edge. That edge is neutral degree two, so its unique matching joins the strip
cyclically in the \(x_0\) direction.

At a cross-section vertex \(y\), the \(e_0\)-edge above it is charged degree
five. Its five incident faces are precisely the five strips corresponding to
the five edges of \(G\) incident to \(y\): the sixth cross-section edge is the
unique matching edge in \(P\) and has no \(01\)-face.

Thus, after contracting each neutral strip, the augmented face-link graph is
the incidence graph of \(G\). By (2), \(G\) is connected. Hence the full
augmented support is connected.

Therefore \(n_L\) is one augmented component \(K_L\), with

\[
\boxed{
M_{K_L}=L^4,
\qquad
A_{K_L}=\frac52L^4.
}                                                       \tag{13}
\]

All neutral matching factorials are \(1!\), so its standalone activity is

\[
\boxed{
z(K_L)
=
2^{1-A_{K_L}}
=
2^{1-(5/2)L^4}.
}                                                       \tag{14}
\]

## 7. Exact signed axial cancellation

For the \(01\) signed-slice channel,

\[
B_{K_L}(r)
=
\sum_{x:x_1=r}j_L(e_0(x)).
\]

Using (7),

\[
B_{K_L}(r)
=
\sum_{x_0,x_2,x_3}
(-1)^{r+x_2+x_3}.
\]

The \(x_0\) sum gives a factor \(L\), while either of the even-length
checkerboard sums in \(x_2,x_3\) vanishes. Hence

\[
\boxed{
B_{K_L}(r)=0
\quad\text{for every }r.
}                                                       \tag{15}
\]

A cyclic primitive is constant. Therefore

\[
\boxed{\ell_{K_L}=0.}                                  \tag{16}
\]

This is exact cancellation inside one macroscopic current component.

## 8. The \(R_3\) size majorant can be arbitrarily loose

The deterministic whole-component bound from #1198 replaces
\(\ell_K\) by a function of \(M_K\). For this component,

\[
\frac{M_{K_L}^4}{4L^4}
=
\frac{(L^4)^4}{4L^4}
=
\boxed{\frac{L^{12}}4}.                                \tag{17}
\]

But its exact signed-slice contribution is

\[
\frac{\ell_{K_L}^2}{L^4}=0.
\]

Thus the ratio between the size majorant and the exact signed quantity is not
merely large. The exact quantity vanishes while the majorant grows like
\(L^{12}\).

This does not show that the ensemble expectation \(R_3(L)\) grows. The
configuration activity (14) is extremely small. What it proves is purely
deterministic and sufficient for route selection:

\[
\boxed{
\text{large current-component size does not imply large infrared slice cost.}
}                                                       \tag{18}
\]

Therefore a proof of P1 that first replaces \(\ell_K\) by \(M_K^2/8\) can
discard arbitrarily strong signed cancellation.

## 9. Consequence for the current program

The exact inequality

\[
\Xi_L\le R_3(L)/16
\]

remains mathematically valid. This note does not retract it.

But (16)-(17) show that \(R_3\) is a potentially very expensive sufficient
target. Even a single exact component can have macroscopic current support and
zero axial infrared cost.

The next analytical attack should therefore keep at least the signed projected
source

\[
B_K(r)
\]

or its optimal primitive \(H_K\) visible, rather than reduce immediately to
the unsigned current count \(M_K\).

The component-deletion activity theorem from #1200 remains useful because it
can weight **signed component patterns** without forcing a size-only
majorization.

## 10. Status

- dense family construction, exact boundary, one-component connectivity and
  exact cancellation: **candidate-T**;
- finite checks at \(L=4,6,8,10\): **candidate-C**;
- divergence or boundedness of ensemble \(R_3\): **not claimed**;
- full \(\Xi_L\), strict \(b-25\chi\), P1, massless phase and physical photon:
  **open**.
