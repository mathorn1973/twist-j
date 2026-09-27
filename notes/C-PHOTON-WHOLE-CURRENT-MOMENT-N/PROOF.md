# Proof - C-PHOTON-WHOLE-CURRENT-MOMENT-N

**Status:** candidate-T, PUBLIC NON-CANONICAL.
**Owner:** #1198.
**Author:** A. M. Thorn <thorn@twistj.com>.
**Date:** 2026-09-27.
**Frozen preregistration commit:** \`769a55d44ff71b7cacc4bebbeedf300b3982ec8b\`.

No Canon status is promoted by this note.

## 1. Setup

On the even four-torus let \(K\) be one charged component of the exact
one-copy paired augmentation from \`CONNECTED-CURRENT.md\). Its current is

\[
J_K=\partial\eta_K/5.
\]

By the \(p=5\) current theorem in \`C-CURRENT-PRIME-GATE-N\`,
\(J_K(e)\in\{-1,0,1\}\), \(\partial J_K=0\), and its finite support admits an
edge-disjoint decomposition into oriented simple cycles. The same note proves

\[
[J_K]=0\in H_1(T^4,\mathbb Z).
\]

For the fixed axial pair \(01\), define as in \`SIGNED-SLICES.md\`

\[
B_K(r)=\sum_{x:x_1=r}J_K(e_0(x)),
\qquad
H_K(r)-H_K(r-1)=B_K(r),
\]

and

\[
\ell_K=\min_{h\in\mathbb Z}\sum_{r\in\mathbb Z/L\mathbb Z}|H_K(r)-h|.
\]

The definition depends only on \(B_K\), not on the neutral filling.

Let \(M_K\) be the number of current edges in \(J_K\).

## 2. \(\ell\) is subadditive

Let \(B_1,B_2\) be integer zero-sum cyclic sources. Choose primitives
\(H_1,H_2\) and minimizing integer shifts \(h_1,h_2\). Then
\(H_1+H_2\) is a primitive of \(B_1+B_2\), and \(h_1+h_2\) is an admitted
integer shift. Hence

\[
\begin{aligned}
\ell(B_1+B_2)
&\le
\sum_r |H_1(r)+H_2(r)-h_1-h_2|\\
&\le
\sum_r|H_1(r)-h_1|
+
\sum_r|H_2(r)-h_2|.
\end{aligned}
\]

Therefore

\[
\boxed{\ell(B_1+B_2)\le\ell(B_1)+\ell(B_2).}       \tag{1}
\]

No independence or probabilistic statement is used.

## 3. Zero-winding cycles

Choose any edge-disjoint simple-cycle decomposition

\[
J_K=\sum_{\alpha}\gamma_\alpha.
\]

Separate the cycles with zero winding from those with nonzero winding.
For one zero-winding simple cycle of length \(m_\alpha\), the signed-slice
lemma already proved in the all-contact quarter-turn note gives, without any
turn restriction on this deterministic inequality,

\[
\ell(\gamma_\alpha)\le\frac{m_\alpha^2}{16}.       \tag{2}
\]

Let \(M_0=\sum_{\alpha:w_\alpha=0}m_\alpha\). By (1),

\[
\ell_0
\le
\frac1{16}\sum_{\alpha:w_\alpha=0}m_\alpha^2
\le
\frac{M_0^2}{16}.                                  \tag{3}
\]

The second inequality is simply
\(\sum m_\alpha^2\le(\sum m_\alpha)^2\).

## 4. A universal cyclic transport bound

Let \(B\) be any integer zero-sum source on the cyclic coordinate
\(C_L=\mathbb Z/L\mathbb Z\). Put

\[
P=\sum_{B(r)>0}B(r)
=
-\sum_{B(r)<0}B(r)
=
\frac12\|B\|_1.
\]

Expand the positive and negative masses into \(P\) unit tokens and pair them
arbitrarily. For every positive-negative pair choose a shortest arc of the
cycle. Its length is at most \(\lfloor L/2\rfloor\).

Place one unit of flow on every oriented edge of that arc, with the sign
needed to transport the positive token to the negative token. Adding these
flows produces an integer cyclic flow \(H\) whose divergence is \(B\).
Therefore the minimizing flow defining \(\ell(B)\) satisfies

\[
\ell(B)
\le
P\lfloor L/2\rfloor
\le
\frac{\|B\|_1}{2}\frac L2.
\]

Thus

\[
\boxed{
\ell(B)\le\frac L4\|B\|_1.
}                                                       \tag{4}
\]

This is only an upper bound. The pairing need not be optimal.

## 5. Winding cycles

Let \(J_w\) be the sum of all nonzero-winding cycles in the chosen
decomposition and let \(M_w\) be their total edge length.

The projected source \(B_w\) is the signed sum of the direction-zero current
edges at each \(x_1\) slice, so cancellation can only reduce its L1 norm:

\[
\|B_w\|_1
\le
N_{0,w}
\le
M_w.                                                   \tag{5}
\]

Every simple cycle with winding vector \(w\in\mathbb Z^4\) has length at least

\[
m\ge L\|w\|_1,                                        \tag{6}
\]

because its lift must accumulate net displacement \(Lw\).

The full component has zero homology. The zero-winding block contributes no
homology, hence the winding vectors obey

\[
\sum_{\alpha:w_\alpha\ne0}w_\alpha=0.                 \tag{7}
\]

If the winding block is nonempty, (7) contains at least two nonzero integer
vectors and therefore

\[
\sum_{\alpha:w_\alpha\ne0}\|w_\alpha\|_1\ge2.
\]

Using (6),

\[
\boxed{M_w\ge2L\qquad(M_w>0).}                         \tag{8}
\]

Now (4), (5) and (8) give

\[
\ell_w
\le
\frac{L M_w}{4}
\le
\frac{M_w^2}{8}.                                      \tag{9}
\]

This step is why winding cycles must be treated collectively. Applying the
zero-winding cycle lemma to them one by one would be invalid.

## 6. Whole-component theorem

Subadditivity between the two blocks, followed by (3) and (9), gives

\[
\ell_K
\le
\frac{M_0^2}{16}
+
\frac{M_w^2}{8}.                                      \tag{10}
\]

Since \(M_K=M_0+M_w\),

\[
\frac{M_0^2}{16}+\frac{M_w^2}{8}
\le
\frac{M_0^2+M_w^2}{8}
\le
\frac{(M_0+M_w)^2}{8}.
\]

Therefore

\[
\boxed{\ell_K\le\frac{M_K^2}{8}.}                      \tag{11}
\]

If no cycle winds, \(M_w=0\), and the sharper bound survives:

\[
\boxed{\ell_K\le\frac{M_K^2}{16}.}                     \tag{12}
\]

The theorem sees only the current. Arbitrarily large neutral surface filling
does not enter \(M_K\).

## 7. Sharpness of \(1/8\) in the larger unit-flow class

Take even \(L\). Let \(\gamma_+\) be the positive coordinate loop in the
\(e_0\) direction at \(x_1=0\), and let \(\gamma_-\) be the oppositely
oriented coordinate loop at \(x_1=L/2\). Their winding vectors cancel.

The total current edge count is

\[
M=2L.
\]

The axial source is

\[
B(r)=L\delta_{r,0}-L\delta_{r,L/2}.                    \tag{13}
\]

A primitive is constant \(0\) on one half of the axial cycle and constant
\(L\) on the other half. Every median between \(0\) and \(L\) gives the same
minimum,

\[
\ell=L\frac L2=\frac{L^2}{2}.
\]

Hence

\[
\boxed{\ell=\frac{M^2}{8}.}                            \tag{14}
\]

So \(1/8\) cannot be improved for all homologically trivial unit flows.

This witness is deliberately not claimed to be the current of one admissible
ternary augmented surface component. The sharpness statement is for the
larger deterministic unit-flow class only.

## 8. Reduction of the full signed susceptibility target

The exact signed-slice bound is

\[
\Xi_L
=
\frac1V
\mathbb E_{\rm aug}
\sum_K\ell_K^2.
\]

Using (11),

\[
\boxed{
\Xi_L
\le
\frac1{64V}
\mathbb E_{\rm aug}
\sum_K M_K^4.
}                                                       \tag{15}
\]

Let \(E_L^+\) be the set of the \(4V\) canonical positively oriented lattice
edges. Current support is represented once in this set. Every component with
\(M_K\) current edges appears once for every one of those \(M_K\) edges, so

\[
\sum_{e\in E_L^+}
{\bf1}_{\{e\ {\rm charged}\}}
M_{K(e)}^3
=
\sum_K M_K\cdot M_K^3
=
\sum_K M_K^4.                                          \tag{16}
\]

Define

\[
R_3(L)
=
\frac1{4V}
\sum_{e\in E_L^+}
\mathbb E_{\rm aug}
\left[
{\bf1}_{\{e\ {\rm charged}\}}
M_{K(e)}^3
\right].
\]

Then (15)-(16) give the single sufficient current target

\[
\boxed{\Xi_L\le\frac{R_3(L)}{16}.}                     \tag{17}
\]

No equality of the four edge orientations is used. Translation invariance
only rewrites the spatial average as an average of four fixed orientation
roots when desired.

Thus

\[
\sup_L R_3(L)<\infty
\quad\Longrightarrow\quad
\sup_{L,t}\chi_L(t)<\infty                             \tag{18}
\]

for every admitted nonzero lattice frequency, through
\(\chi_L(t)\le\Xi_L\).

This does not prove the hypothesis on \(R_3\).

## 9. Exact tail form

For every integer \(M\ge1\),

\[
M^3-(M-1)^3=3M^2-3M+1.
\]

Telescoping gives

\[
\boxed{
M^3=\sum_{r=1}^M(3r^2-3r+1).
}                                                       \tag{19}
\]

Insert (19) into the rooted expectation. For a fixed positive root edge
\(e_i\) of orientation \(i\),

\[
\mathbb E_{\rm aug}
\left[
{\bf1}_{\{e_i\ {\rm charged}\}}M_{K(e_i)}^3
\right]
=
\sum_{r\ge1}
(3r^2-3r+1)
P_{\rm aug}
(e_i\ {\rm charged},M_{K(e_i)}\ge r).
\]

Therefore

\[
\boxed{
R_3(L)
=
\frac14
\sum_{i=0}^3
\sum_{r\ge1}
(3r^2-3r+1)
P_{\rm aug}
(e_i\ {\rm charged},M_{K(e_i)}\ge r).
}                                                       \tag{20}
\]

An exponential tail closes (18). More generally a uniform bound
\(P(e_i\ {\rm charged},M\ge r)\le C r^{-3-\epsilon}\) for some
\(\epsilon>0\) is sufficient.

This is now the precise probabilistic bottleneck.

## 10. What the old polymer attacks do not decide

The failed or supercritical polymer-tree majorants #1168, #1170, #1172 and
#1173 are about the size and entropy of restricted **neutral surface**
families. Equation (17) asks only for the size of the **current support**
inside an augmented component.

Those are different random variables. The public neutral-connector examples
already show why: the neutral surface can become arbitrarily long while the
current consists of two fixed elementary loops.

Therefore failure of the old neutral-area majorants does not imply divergence
of \(R_3\). It localizes the remaining problem: neutral geometry may transmit
component membership over long distance, but only growth of the number of
charged edges can make (17) large.

## 11. Prime and primitive-cycle boundary

The \(p=5\) theorem from #1196 matters here for one exact reason: it makes the
current unit-capacity, so the deterministic decomposition into edge-disjoint
cycles is available without multiplicities.

This does **not** make the full ensemble an independent loop gas.

Three obstructions remain:

1. neutral matched surfaces can put several disjoint current loops into one
   common \(K\);
2. a unit current graph can have a nonunique simple-cycle decomposition at
   a higher-valence vertex;
3. edge capacity is hard-core, so primitive cycles cannot be repeated or
   overlapped freely.

Thus a primitive-cycle Euler product is not currently an identity of the
TWIST-J current measure. A dynamical zeta function would require a new theorem:
either a multiplicative component activity or a determinant representation
that already contains these interactions.

## 12. Cyclotomic-current comparison identity

There is nevertheless one exact relation to the public \(p=5\) selector.

For an odd prime \(p\), the cyclotomic field

\[
K_p=\mathbb Q(\zeta_p)
\]

has degree

\[
D=[K_p:\mathbb Q]=p-1.                                 \tag{21}
\]

A \(D\)-dimensional hypercubic edge has

\[
2(D-1)=2(p-2)
\]

incident plaquettes. A one-hole charged edge carrying \(p\) aligned occupied
plaquettes requires

\[
p+1=2(D-1)=2(p-2).                                     \tag{22}
\]

But (22) is exactly

\[
\boxed{\frac{p-2}{p+1}=\frac12,}                       \tag{23}
\]

the equation in public P5-ROOT-SELECTION [T]. Therefore

\[
p=5,\qquad D=4.
\]

This is an exact combinatorial interpretation of the same algebraic equation
inside the declared comparison family.

It is **not** a new physical root selector. Public Canon explicitly says
P5-ROOT-SELECTION is the retained unconditional selector and that no further
unconditional support for selecting \(p=5\) is claimed. Equation (22) assumes
the comparison identification \(D=[K_p:\mathbb Q]\) and the one-hole current
star. Neither is promoted here to a variable-\(p\) physical law.

## 13. Status

- G1-G8 and the comparison identity G10: **candidate-T**;
- finite exact audit: at most **candidate-C**;
- uniform \(R_3\) bound: **OPEN in this note**;
- full \(\Xi_L\), \(P1\), positive \(b-25\chi\), massless phase and physical
  photon: **OPEN**;
- ordinary-prime Euler product for the current measure: **not claimed**.
