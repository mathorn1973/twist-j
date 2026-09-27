# Proof - C-PHOTON-COMPONENT-DELETION-ACTIVITY-N

**Status:** candidate-T, PUBLIC NON-CANONICAL.
**Owner:** #1200.
**Author:** A. M. Thorn <thorn@twistj.com>.
**Date:** 2026-09-27.
**Frozen preregistration commit:** \`318522229afbbf7f97d152ef8812ca74d8414d7a\`.

No Canon status is asserted here.

## 1. Exact deletion of one augmented component

Take one consistent unsigned augmented structure \((S,\mathcal M)\). Its exact
weight is

\[
\widetilde w(S,\mathcal M)
=
2^{k-|S|}
\prod_{e:d_e\ {\rm even}}\frac1{r_e!},
\qquad
r_e=d_e/2.
\]

Fix one complete component \(K\). Let \(A_K\) be its number of occupied faces.

At a neutral lattice edge \(e\), the matching \(\mathcal M\) consists of
\(r_e\) positive-negative pairs. A matching pair is itself a graph link, so if
one face of a pair lies in \(K\), the other face lies in \(K\) as well. Let
\(t_e\) be the number of matching pairs at \(e\) belonging to \(K\).

At a charged edge all five incident occupied faces are linked into one
component. Hence either all five belong to \(K\), or none do.

Delete every face of \(K\) and every link incident to those faces.

At a neutral edge the remaining pairs are literally the untouched
\(r_e-t_e\) pairs, still positive-negative matched. At a charged edge belonging
to \(K\), all five faces disappear and the edge becomes empty. Every cycle in
the remaining face-link graph was already a cycle of the original consistent
graph, so its relative-sign product remains \(+1\). Thus deletion produces a
valid consistent augmented structure.

Exactly one connected component was removed, so

\[
k\longmapsto k-1,
\qquad
|S|\longmapsto |S|-A_K.
\]

All factorials at untouched edges cancel in the ratio. Therefore

\[
\begin{aligned}
\frac{\widetilde w({\rm full})}
     {\widetilde w({\rm full}\setminus K)}
&=
\frac{2^{k-|S|}}
     {2^{k-1-(|S|-A_K)}}
\prod_{e:t_e>0}
\frac{(r_e-t_e)!}{r_e!}\\
&=
\boxed{
2^{1-A_K}
\prod_{e:t_e>0}
\frac{(r_e-t_e)!}{r_e!}.
}
\end{aligned}                                          \tag{1}
\]

For integers \(r\ge t\ge0\),

\[
\frac{r!}{(r-t)!}
=
r(r-1)\cdots(r-t+1)
\ge
t!,
\]

hence

\[
\frac{(r-t)!}{r!}\le\frac1{t!}.                        \tag{2}
\]

Combining (1) and (2),

\[
\boxed{
\frac{\widetilde w({\rm full})}
     {\widetilde w({\rm full}\setminus K)}
\le
z(K):=
2^{1-A_K}
\prod_{e:t_e>0}\frac1{t_e!}.
}                                                       \tag{3}
\]

If the same marked component stands alone, its neutral degree at \(e\) is
\(2t_e\), so its exact unsigned standalone weight is precisely the right side
of (3). Thus the name "standalone activity" is literal.

## 2. Probability of one fixed marked component

A marked component pattern fixes its face set and all of its internal links.
Consistency then fixes all relative face signs up to the one global reversal
already represented by the factor \(2\) in \(z(K)\).

Let \(\Omega_K\) be the set of complete unsigned augmented structures in
which this exact marked pattern occurs.

Deletion defines

\[
D_K:\Omega_K\longrightarrow\Omega_{\rm aug}.
\]

The map is injective. If \(D_K(\omega_1)=D_K(\omega_2)\), adjoining the same
fixed faces and the same fixed links of \(K\) reconstructs the same union of
face sets and the same matching at every lattice edge, so
\(\omega_1=\omega_2\).

Equation (3) holds pointwise on \(\Omega_K\). Therefore, with \(Z_{\rm aug}\)
the complete augmented partition sum,

\[
\begin{aligned}
P_{\rm aug}(K\ {\rm occurs})
&=
Z_{\rm aug}^{-1}\sum_{\omega\in\Omega_K}\widetilde w(\omega)\\
&\le
z(K)Z_{\rm aug}^{-1}
\sum_{\omega\in\Omega_K}\widetilde w(D_K\omega)\\
&\le
z(K).
\end{aligned}
\]

Hence

\[
\boxed{
P_{\rm aug}(K\ {\rm occurs})\le z(K).
}                                                       \tag{4}
\]

No exterior face is frozen. The deletion image may contain arbitrary charged
and neutral components. Surjectivity is unnecessary.

## 3. Generic incidence floor

Let \(M_K\) be the number of charged edges of \(K\). Every charged edge has
exactly five incident occupied faces, all belonging to \(K\). Thus there are
exactly \(5M_K\) incidences of a face of \(K\) with a charged edge.

Each plaquette has four boundary edges, so its contribution to that incidence
count is at most four. Therefore

\[
5M_K\le4A_K,
\]

or

\[
\boxed{A_K\ge\frac54M_K.}                              \tag{5}
\]

This is deliberately only an incidence floor. It says nothing about the
entropy of the possible components.

## 4. The four-cup defect

Use the public cubical convention

\[
\partial c_{abc}(x)
=
p_{bc}(x+e_a)-p_{bc}(x)
-p_{ac}(x+e_b)+p_{ac}(x)
+p_{ab}(x+e_c)-p_{ab}(x).
\]

Define

\[
U(x)
=
-c_{012}(x)+c_{012}(x-e_2)
-c_{013}(x)+c_{013}(x-e_3),
\]

\[
a(x)=\partial U(x)-5p_{01}(x).
\]

Since \(\partial^2=0\),

\[
\boxed{\partial a(x)=-5\partial p_{01}(x).}            \tag{6}
\]

Direct expansion gives 21 nonzero plaquettes, every coefficient \(+1\) or
\(-1\). The five \(01\)-faces are

\[
p_{01}(x-e_2),\quad
p_{01}(x-e_3),\quad
p_{01}(x),\quad
p_{01}(x+e_3),\quad
p_{01}(x+e_2),
\]

all with coefficient \(-1\). The remaining sixteen faces are the four side
faces of each of the four cups.

Thus one defect has

\[
A_1=21,
\qquad
M_1=4.                                                  \tag{7}
\]

Every neutral occupied edge has degree two and each of the four edges of the
central \(01\)-plaquette is charged with degree five. Its augmented face graph
is connected.

## 5. The diagonal cancellation motif

Put

\[
v=e_2+e_3.
\]

Compare \(a(0)\) and \(a(-v)\). Their supports meet in exactly the two faces

\[
p_{01}(-e_2),
\qquad
p_{01}(-e_3),                                          \tag{8}
\]

and both defects give coefficient \(-1\) on both faces.

Therefore the alternating combination

\[
a(0)-a(-v)
\]

cancels both common faces. Since each cancelled face was counted once in each
21-face support, the union loses four support counts:

\[
21+21-4=38.                                            \tag{9}
\]

After the cancellation, the two remaining face sets are linked across eight
neutral degree-two edges. Four have direction \(0\) and four direction \(1\).
For example, at the edge \(((0),(0,0,-1,0))\), the surviving faces

\[
p_{02}(0,0,-1,0)
\quad\hbox{and}\quad
p_{03}(0,0,-1,-1)
\]

have opposite signed incidence; the seven translated/parallel companions give
the other cross-links. Hence the combined augmented face graph is connected.

The same direct expansion also shows

\[
{\rm supp}\,a(0)\cap{\rm supp}\,a(-sv)=\varnothing,
\]

and even their boundary-edge sets are disjoint, for every integer \(s\ge2\).
Thus only nearest neighbors in the diagonal sequence interact.

## 6. Infinite exact defect chain

For \(N\ge1\), define

\[
x_i=-iv,
\qquad
n_N=\sum_{i=0}^{N-1}(-1)^i a(x_i).                    \tag{10}
\]

The two faces used by the interface \((i,i+1)\) are the forward pair of one
defect and the backward pair of the next. For an interior defect these are
distinct from the two faces used at the other interface. There is no triple
face overlap. Non-neighboring defects share neither faces nor boundary edges.

Consequently every interface repeats exactly the local cancellation motif of
section 5, independently of the other interfaces.

Starting from \(A_1=21\), every added defect contributes 21 faces and cancels
two old plus two new support occurrences, for net increment 17:

\[
A_N
=
21+17(N-1)
=
\boxed{17N+4}.                                         \tag{11}
\]

Because all surviving coefficients come from one defect only, \(n_N\) is
ternary.

Taking the boundary and using (6),

\[
\boxed{
j_N
=
\frac{\partial n_N}{5}
=
-\sum_{i=0}^{N-1}(-1)^i\partial p_{01}(x_i).
}                                                       \tag{12}
\]

The central plaquettes lie on distinct transverse \((x_2,x_3)\) coordinates.
Their four-edge boundaries are pairwise edge-disjoint. Hence

\[
\boxed{M_N=|{\rm supp}\,j_N|=4N.}                      \tag{13}
\]

The one-defect motif has only neutral degree two and charged degree five.
The two-defect interface motif preserves exactly those degrees, and
non-neighboring motifs have disjoint edge sets. Induction therefore gives for
the whole chain:

\[
E_{2,N}=24N+8,
\qquad
E_{5,N}=4N,                                            \tag{14}
\]

where \(E_{d,N}\) counts occupied lattice edges of degree \(d\).
Indeed

\[
2E_{2,N}+5E_{5,N}
=
2(24N+8)+20N
=
68N+16
=
4A_N,
\]

as required by face-edge incidence.

All neutral edges have degree two, so their matching is unique. The
single-defect face graph is connected, and every new defect is joined to the
previous one by the eight neutral cross-links of section 5. Hence induction
also gives one connected augmented component for every \(N\).

The construction is finite on \(\mathbb Z^4\) and embeds without
identification in any sufficiently large four-torus.

Since every neutral edge has \(t_e=1\), all factorials in the standalone
activity are one. Therefore

\[
\boxed{
z_N
=
2^{1-A_N}
=
2^{-17N-3}.
}                                                       \tag{15}
\]

Finally,

\[
\boxed{
\frac{A_N}{M_N}
=
\frac{17N+4}{4N}
=
\frac{17}{4}+\frac1N
\longrightarrow\frac{17}{4}.
}                                                       \tag{16}
\]

## 7. The 21/4 extrapolation is false

For one elementary current loop, the defect has \(A=21,M=4\), hence
\(A/M=21/4\).

But already \(N=2\) in (16) gives

\[
\frac{A_2}{M_2}
=
\frac{38}{8}
=
\frac{19}{4}
<
\frac{21}{4}.
\]

Thus the universal extrapolation

\[
A_K\ge\frac{21}{4}M_K
\]

is false.

Moreover (16) proves that any proposed universal asymptotic linear lower
coefficient for \(A_K/M_K\) cannot exceed \(17/4\).

Nothing here proves the converse inequality

\[
A_K\ge\frac{17}{4}M_K.
\]

A future component with smaller ratio would be new information, not a
falsifier of the present theorem.

## 8. Consequence and remaining entropy debt

Equations (3)-(4) are the useful positive result:

\[
P_{\rm aug}(K\ {\rm occurs})
\le
2^{1-A_K}
\prod_e\frac1{t_e!}.                                   \tag{17}
\]

They sum every allowed exterior component exactly through the deletion
injection.

But \(R_3\) requires summing (17) over **all marked components** containing a
root current edge. The number and geometry of their neutral decorations are
not bounded by this theorem.

The generic incidence estimate (5) alone gives only
\(2^{1-5M_K/4}\), far too weak to declare the component entropy summable
without an independent counting theorem.

Therefore the exact state after this note is:

\[
\boxed{
\text{fixed component activity controlled;}
\qquad
\text{component entropy still open.}
}
\]

This sharpens the next \(R_3\) problem without claiming its solution.
