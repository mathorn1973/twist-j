# Binary-fiber sector cap and the integer defect lattice

**PUBLIC / NON-CANONICAL / candidate-T analytical note.**
No Canon authority or public status promotion.

Owner: A. M. Thorn / binary-fiber-sector-cap-20260927, issue #1225.
This is a self-contained finite-volume proof. The connection to the
upstream P1 comparison is a separately identified conditional corollary.

## 1. Exact finite probability space

Let L>=4 be even, and let K_L=(Z/LZ)^4 be the periodic cubical lattice.
Write E and P for its positively labelled links and plaquettes; a
plaquette (x,mu,nu) has mu<nu. All cochain and boundary constraints below
are over F_5. For a link cochain a, use

\[
(da)_{\mu\nu}(x)
=a_\nu(x+e_\mu)-a_\nu(x)-a_\mu(x+e_\nu)+a_\mu(x).
\]

The boundary operator is the transpose incidence map, so
<n,da>=<partial n,a>. Define the 01 seam Sigma by Sigma_(x,01)=1
when x_0=x_1=0, and zero otherwise. It contains exactly L^2 plaquettes.
The pairing with this integer 0/1 seam is an integer before any reduction
modulo five. Coordinate 0 is the temporal direction of the source notes.

Set zeta=exp(2*pi*i/5), phi=1+zeta+zeta^(-1), so phi^2=phi+1.
For each plaquette cochain b define

\[
W(f)=2+\zeta^f+\zeta^{-f},\qquad
Z_L[b]=\sum_{a\in\mathbb F_5^E}\prod_{p\in P}W((da)_p+b_p).
\]

These are the fixed local weight and discrete source convention of #1220.

Let

\[
\mathcal P=\{(S,T):S,T\in\{0,1\}^{P(K_L)},\ \partial S=\partial T\pmod5\}.
\]

Write n=S-T, F=<n,Sigma>, and let N be the cardinality of the displayed
ordered-pair set. Thus N counts pairs, not plaquettes.

For each beta in F_5^E let
B_beta={S in {0,1}^P: partial S=beta}. The factorization
W(f)=(1+zeta^f)(1+zeta^(-f)), followed by independent character
orthogonality on every link, proves

\[
5^{-|E|}Z_L[b]
=\sum_{(S,T)\in\mathcal P}\zeta^{\langle S-T,b\rangle}
=\sum_\beta\left|\sum_{S\in\mathcal B_\beta}
                   \zeta^{\langle S,b\rangle}\right|^2.
\]

In particular N=5^(-|E|)Z_L[0]=sum_beta |B_beta|^2>0.
Give every ordered pair equal probability 1/N. For a fixed admissible
ternary n, exactly 2^(number of zero plaquettes of n) pairs have S-T=n:
each zero has choices (0,0),(1,1), and each nonzero fixes its binary pair.
Thus this pair law induces exactly the unsourced character law from the
expansion of the fixed plaquette weight. This is a finite identity, not an
adoption of an additional physical measure or a new physical layer gate.

Define

\[
Q_a=\#\{(S,T)\in\mathcal P:F\equiv a\pmod5\},\quad
p_a=Q_a/N,\quad
m_a=\mathbb E[F\,1_{F\equiv a}].
\]

Swapping S,T gives p_a=p_{-a}, m_a=-m_{-a}, m_0=0 and EF=0.
Put

\[
C_k=\mathbb E[F\zeta^{kF}],\quad
\mathcal D=|C_1|^2+|C_2|^2,\quad
H=\sum_a\frac{m_a^2}{p_a}.
\]

When p_a=0, m_a=0 and the corresponding quotient is defined as zero.
In the target model all residue sectors are nonempty. A wrapping 01 plane
at fixed x_2,x_3 is a binary 2-cycle with one plaquette in Sigma. Taking
it as S with T=0 gives F=1; two disjoint such planes give F=2.
Swapping S,T gives -1 and -2. The zero pair gives residue zero.

Finite Fourier orthogonality gives

\[
\sum_{k=0}^4|C_k|^2=5\sum_a m_a^2.
\]

C_0=0 and the two conjugate mode pairs imply

\[
\boxed{\mathcal D=5(m_1^2+m_2^2)},\qquad
H=2\left(\frac{m_1^2}{p_1}+\frac{m_2^2}{p_2}\right).
\tag{1}
\]

## 2. An exact integer cap

For a boundary beta let B_beta be its binary fiber, b_beta=|B_beta|,
and

\[
c_{\beta,r}=\#\{S\in\mathcal B_\beta:\langle S,\Sigma\rangle\equiv r\pmod5\}.
\]

The pair matching rule yields exactly

\[
N=\sum_\beta b_\beta^2,\qquad
Q_a=\sum_\beta\sum_{r\in\mathbb F_5}c_{\beta,r}c_{\beta,r-a}.
\tag{2}
\]

For each a!=0, the five unordered edges {r,r-a} form a five-cycle,
each edge occurring once. For any nonnegative vector x on a five-cycle,

\[
4\sum_{\{r,s\}\in E(C_5)}x_rx_s\le\left(\sum_r x_r\right)^2.
\tag{3}
\]

Self-contained proof: normalize the sum to one (the zero case is trivial).
If supported vertices u,v are nonadjacent, redistribute their total mass
to the one with the greater sum of neighboring masses. There is no x_u x_v
term, so the edge polynomial is affine during this redistribution and
cannot decrease. The number of supported vertices decreases. Repeating
ends on a clique of the cycle, which has at most two vertices. Its edge
polynomial is at most x(1-x)<=1/4. This proves (3).

Apply (3) to each integer vector c_beta and sum over beta in (2):

\[
\boxed{4Q_a\le N\quad(a\ne0)},\qquad
\boxed{p_a\le\tfrac14\quad(a\ne0)}.
\tag{4}
\]

The argument uses conditional independent identical distributions in
each binary boundary fiber, not just positivity of source partition sums.

## 3. A doubled sufficient coefficient

Equations (1) and (4) give

\[
\boxed{H\ge8(m_1^2+m_2^2)=\frac85\mathcal D.}
\tag{5}
\]

Section 4 derives the integer identity of #1220 directly with these same
definitions. Conditional on the Delta_L(q)>=H_L consequence asserted by
the NON-CANONICAL candidates #1213/#1216, it gives

\[
\boxed{
\Delta_L(q)\ge H_L\ge\frac85 L^4\frac{A_L^2+B_L^2}{N_L^2}
}
\tag{6}
\]

for every temporal character q admitted by those source candidates. Here
Delta_L(q) denotes their comparison quantity; the sole additional premise
used by this corollary is exactly Delta_L(q)>=H_L. Neither that comparison
nor its physical interpretation is proved or promoted in this note.
This changes the former sufficient coefficient 4/5 to
8/5, without changing any measure, observable, limit order, or physical
dictionary. The upstream Delta inequality remains at its candidate scope.

The coefficient 8/5 is sharp for the general pair-Gram construction:
one fiber with two equiprobable objects of integer seam values 0 and 1
has P(F=0)=1/2, P(F=+/-1)=1/4. It gives H=1/2 and D=5/16.
This example is not the fixed four-dimensional lattice model and does
not establish sharpness within that narrower model. If strictly positive
probabilities in all residues are required in the broader class, a
vanishing mixture with other fibers approaches the same ratio.

## 4. The defect vector belongs to an index-five integer lattice

Fix p in Sigma and define the signed integer counts

\[
t_a=\sum_{(S,T)\in\mathcal P}(S_p-T_p)\,1_{F\equiv a\pmod5}.
\tag{7}
\]

Swap symmetry gives t_{-a}=-t_a and t_0=0. Translations parallel to the
seam act transitively on its plaquettes and preserve F. Therefore

\[
Nm_a=L^2t_a.
\tag{8}
\]

Let delta_p be the unit source at p. Define the same normalized discrete
defect as #1220 by

\[
\widehat\Delta
=5^{-|E|}\bigl(Z_L[\Sigma-\delta_p]-Z_L[\Sigma+\delta_p]\bigr).
\]

The Gram expansion in section 1 gives directly

\[
\widehat\Delta
=\sum_{(S,T)\in\mathcal P}\zeta^F(\zeta^{-n_p}-\zeta^{n_p}).
\]

Since n_p is 0,+1,-1,

\[
\widehat\Delta
=-(\zeta-\zeta^{-1})
\left[t_1(\zeta-\zeta^{-1})+t_2(\zeta^2-\zeta^{-2})\right].
\]

With phi^2=phi+1 the two products evaluate exactly to

\[
\widehat\Delta=(2+\varphi)t_1+(2\varphi-1)t_2.
\]

Consequently the defect has unique integer coefficients A,B in
widehat Delta=A+B phi, with

\[
\boxed{A=2t_1-t_2,\quad B=t_1+2t_2},\qquad
\boxed{A^2+B^2=5(t_1^2+t_2^2)}.
\tag{9}
\]

Equivalently, 2A+B=5t_1 and 2B-A=5t_2. The determinant of the integer
map in (9) is five. There is no restriction on whether L is divisible by
five. This is a necessary lattice condition, not a proof that every
vector in this sublattice is realized by the fixed model.

Combining (1), (8) and (9) also proves, without importing an upstream
derivative calculation,

\[
\boxed{\mathcal D
=5\frac{L^4}{N^2}(t_1^2+t_2^2)
=L^4\frac{A^2+B^2}{N^2}.}
\]

This is the integer two-mode identity used in (6).

For the positive Q_1,Q_2 of the target model, (8) also retains the full
Fisher quantity as an exact rational counting expression:

\[
\boxed{
H_L=\frac{2L^4}{N_L}
\left(\frac{t_1^2}{Q_1}+\frac{t_2^2}{Q_2}\right).
}
\tag{10}
\]

Thus the stronger H route need not be discarded when an unweighted
two-mode bound loses information about small sector probabilities.

## 5. The thermodynamic obstruction is unchanged

No estimate in this note proves

\[
\liminf_{L\to\infty,\ L\ {\rm even}}
L^4\frac{A_L^2+B_L^2}{N_L^2}>0.
\]

By (9) this is equivalent to a positive lower limit for
5 L^4(t_1^2+t_2^2)/N_L^2. The required model-specific theorem must
control the signed local imbalance on the scale N_L/L^2.

If the defect is nonzero, (9) strengthens its integer norm bound from
one to five. This still supplies only the bound 8L^4/N_L^2 in (6).
Moreover N_L>=2^(6L^4), because all diagonal pairs S=T occur on the
four-torus with 6L^4 plaquettes. Consequently this elementary floor is
not uniform and cannot prove P1.

Failure of this sufficient D route would not by itself disprove P1 or
even the potentially broader H route. P1, P2, S7 and the public
PHOTON-MASSLESS-PHASE obligation remain open.
