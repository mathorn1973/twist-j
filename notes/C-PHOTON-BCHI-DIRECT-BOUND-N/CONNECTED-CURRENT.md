# Full current covariance: paired surfaces and the missing distance estimate

**PUBLIC, NON-CANONICAL; candidate-T written derivation.** Working item
C-PHOTON-BCHI-DIRECT-BOUND-N, [#1143](https://github.com/mathorn1973/twist-j/issues/1143).
Author: A. M. Thorn. Date: 24 September 2026. Original text/code: Apache-2.0.
Basis: Public Canon v91, public main
`316c3a2f413dbb37937e43fca123b1fe212a16af`.

**The requested distance-decay theorem is not obtained.** This continuation
gives an exact, finer representation of the full edge-current covariance,
an all-distance obstruction to switching disconnected current loops with
their occupied face support fixed, and substantially stronger local bounds.
The remaining sufficient quantities below are defined but not evaluated
uniformly in volume. P1 and the photon phase remain open.

This extends occupied-face switching [#1112](https://github.com/mathorn1973/twist-j/issues/1112).
The source inequality used in section 5 is already proved in
[PHOTON-LOW-CONFLICT-CURRENT-PATHS.md](../canon/PHOTON-LOW-CONFLICT-CURRENT-PATHS.md),
at its stated scope. Its periodic, zero-conditioned block specialization is
derived here. The normalization step is from
[MARGINAL-CURRENT-BOUND.md](MARGINAL-CURRENT-BOUND.md). Neither prior method
is claimed as a new theorem in this continuation.

## 1. An exact auxiliary measure

Use the same even periodic four-dimensional lattice, L>=4, with

```
Omega = {n in {-1,0,1}^P : partial n = 0 mod 5},
mu(n) = Z^-1 2^(-|supp n|),        j = partial n/5.
```

Let S=supp(n), epsilon(e,p) be the oriented incidence and d_e the number
of occupied faces incident on e. The six available faces permit exactly:

- d_e=0,2,4,6: the signed incidences balance, so j_e=0;
- d_e=5: all five incidences have one sign, so j_e=+1 or -1.

Degrees 1 and 3 are impossible. At each neutral edge of degree 2r, choose
uniformly a perfect matching between its r positive and r negative
incidences. There are r! choices, independently at each edge conditional
on n. At degree five join all five incident faces.

An unsigned structure (S,M) records the occupied faces and the neutral
matchings. For a matched pair p,q, the face orientations obey

```
n_q = -epsilon(e,p)epsilon(e,q)n_p        (neutral pair),
n_q = +epsilon(e,p)epsilon(e,q)n_p        (degree-five junction).
```

Build the graph on S with these links. A structure is consistent if every
cycle has relative-sign product +1. Inconsistent structures have zero
weight. Each connected component K of a consistent structure has exactly
two orientations. If k(S,M) is the number of components, the exact unsigned
weight is

\[
 \widetilde w(S,M)=2^{k(S,M)-|S|}
       \prod_{e:d_e\ \mathrm{even}}\frac1{(d_e/2)!}.             \tag{1}
\]

Its partition sum is the original Z. Indeed, each original orientation n
has exactly product_e (d_e/2)! compatible matchings. Multiplying each by
the reciprocal factor cancels this multiplicity. Conversely, a consistent
structure has exactly 2^k equally weighted signings. Thus (1) is an exact
augmentation of mu, not a new physical measure or independence assumption.

The factors at degrees 2,4,6 are 1,1/2,1/6. Fixing one arbitrary matching
instead of summing them does not preserve the original law.

## 2. Exact full-current covariance and two sufficient bounds

Choose one reference signing eta_K on each component, extended by zero
outside K. Each neutral pair cancels separately within K, and each
degree-five junction lies entirely in one K. Therefore

\[
 J_K=\partial\eta_K/5
\]

is an integer conserved current. It is zero for a component containing no
degree-five edge. Conditional on (S,M), independent uniform signs sigma_K
give j=sum_K sigma_K J_K. Global reversal also gives E_mu j_e=0. Hence

\[
 \boxed{\operatorname{Cov}_\mu(j)
       =\mathbb E_{\rm aug}\sum_K J_K\otimes J_K.}           \tag{2}
\]

For two charged edges in the same K, let tau(e,f)=J_K(e)J_K(f). This sign
does not depend on the reference signing. Then

\[
 C_j(e,f)=\mathbb E_{\rm aug}\!\left[
   \tau(e,f){\bf1}_{d_e=d_f=5,\ K(e)=K(f)}\right],
\qquad
 |C_j(e,f)|\le P_L(e,f),                                  \tag{3}
\]

where P_L is the probability of the displayed event. The exact signed
expression may be strictly smaller than its probability bound. The
connection can pass through neutral faces.

There are two useful finite-volume consequences. Write
chi_L(t)=S^L_(j,00)(t e_1)/lambda(t), lambda(t)=4 sin^2(t/2), at an
allowed nonzero frequency. The exact total current in each orientation
is zero. With centered integer displacement representatives x on the
torus, this gives

\[
 S^L_{j,00}(te_1)=\sum_x(\cos(tx_1)-1)C^L_j(00;x).
\]

For every integer m, 1-cos(tm)<=m^2(1-cos t). Consequently

\[
 \boxed{0\le\chi_L(t)\le
    \frac12\sum_x x_1^2 P_L((0,0),(x,0)).}                  \tag{4}
\]

No infinite-volume connection event is substituted for P_L. A uniformly
evaluated bound on the finite sums in (4) would bound every admitted
ordered profile. Identification with an infinite-volume moment formula
would additionally require control of the tails; local convergence alone
does not identify connections whose paths could escape to infinity.

A second bound avoids the spatial second moment. Let m_01(K) count the
01-oriented faces in K, and for one fixed 01 face p define

\[
 M_L=\mathbb E_{\rm aug}\!\left[
   {\bf1}_{p\in S,\ K(p)\ \mathrm{charged}}m_{01}(K(p))\right].
\]

Here charged means containing at least one degree-five junction, not that
every face touches a current. The quantity is zero when p is absent.
The exact axis boundary identity applies to each K separately, so (2)
gives, with V=L^4,

\[
 \chi_L(t)=\frac1{25V}\mathbb E_{\rm aug}
   \sum_{K\ \mathrm{charged}}\left|
        \sum_{p\in K,\operatorname{ori}(p)=01}
                \eta_K(p)e^{-it c_{p,1}}\right|^2
 \le \frac1{25V}\mathbb E_{\rm aug}
   \sum_{K\ \mathrm{charged}}m_{01}(K)^2
 =\frac{M_L}{25}.                                       \tag{5}
\]

The last equality is translation invariance and counting each 01 face
in its own component. Neutral components contribute exactly zero to
this current bound. Neither the sum in (4) nor M_L has yet been bounded
uniformly with useful evaluated constants. Equations (4)-(5) are
sufficient targets, not the missing estimate itself.

## 3. The refinement is strict

Take the union of the boundaries of c_012(0) and c_023(-e_2). These two
unit cubes meet only along the edge (0,0). There are twelve distinct faces,
one degree-four edge and twenty-two degree-two edges, with no charge.
The four independent choices of the two cube orientations are all valid.

There are three unsigned matchings at their common edge. The matching
within each cube gives two paired components and weight 2^(2-12)/2.
Each cross matching gives one component and weight 2^(1-12)/2. Conditional
on this support, their probabilities are exactly 1/2,1/4,1/4.

The occupied-face graph of #1112 is connected, whereas the new graph
splits with probability 1/2. The two cross matchings encode opposite
relative orientations; their cross-face covariance contributions cancel.
All three structures carry zero current. This fixture demonstrates face
covariance cancellation and strict graph refinement; it does not itself
exhibit a strict numerical improvement of the current bound (3).

## 4. Two disconnected charged loops linked by one neutral tube

Use positively oriented cells and the usual cubical boundary

```
partial c_abc(x) = p_bc(x+e_a)-p_bc(x)
                  -p_ac(x+e_b)+p_ac(x)
                  +p_ab(x+e_c)-p_ab(x).
```

Define the four-cup defect

```
U(x) = -c_012(x)+c_012(x-e_2)-c_013(x)+c_013(x-e_3),
a(x) = partial U(x)-5p_01(x).
```

Its central face has coefficient -1, its twenty other faces have
coefficients +/-1, and partial a(x)=-5 partial p_01(x). Each of the four
outer 01 caps has coefficient -1. For every integer D>=3, put

```
T_D = sum_(k=0)^(D-1) c_013(e_2+k e_3),
n_D = a(0)-a(D e_3)-partial T_D,           L=2D+4.
```

The caps of partial T_D are p_01(e_2+D e_3)-p_01(e_2). They cancel
one cap of each defect. The remaining tube has four lateral faces per
unit length, of orientations 03 and 13, at x_2=1. They are disjoint from
the remaining defect faces and meet them only at the removed cap edges.
D>=3 separates the defects; the stated even torus preserves these
incidences without identification. It follows for every D, not only
the finitely audited values, that

```
|supp n_D| = 4D+40,
j_D = -partial p_01(0)+partial p_01(D e_3),
degree-five occupied edges = 8,
degree-two occupied edges = 8D+60.
```

Every seam replaces one removed face by one tube face; every other neutral
edge has degree two. The degree-two count also follows from
2 E_2+5*8=4(4D+40). All coefficients remain ternary. The two current
components are four-edge loops separated by distance D.

The matching is unique at every neutral edge and the face graph is
connected. Every incidence constraint fixes a relative sign. The displayed
n_D proves consistency, so the support has exactly two signings, n_D and
-n_D. For e=(0,0), f=(D e_3,0), conditioning on this entire unsigned
support, including the empty exterior, gives

\[
 \mathbb E[j_e\mid S]=\mathbb E[j_f\mid S]=0,
 \qquad\mathbb E[j_ej_f\mid S]=-1.                         \tag{6}
\]

Thus independent sign reversal of each component of supp(j), with S fixed,
is false. A componentwise switching proof cannot restrict (3) to a path
consisting only of charged edges. Nor are five disjoint long neutral
connections required: just one sheet from each defect is joined by the
tube; the other four pieces remain local.

This does **not** disprove decay of the unconditional covariance, nor
exclude a different ensemble inequality using further cancellations.
The support's exact unnormalized mass is 2^(-(4D+39)), and its probability
is that number divided by Z_L. Other supports can cancel its contribution.
Moreover, the two opposite loops are translated along e_3: their complete
j_0 form factors cancel identically at t e_1. Equation (6) therefore gives
no positive lower bound on the target susceptibility. It makes the need
to retain the signed sum in (2) explicit.

## 5. A stronger integrated bound for local circulation patterns

Retain Q_T^S(a) from the previous marginal note, with selected current a
on S, zero current on disjoint T, and all other currents summed. Let f be
a real edge cochain supported on S. Finite character expansion, with
continuous Haar integration on S union T and Z5 averaging elsewhere,
gives exactly

\[
 e^{5\langle a,f\rangle}Q_T^S(a)=\int
 e^{-5i\langle a,A_S\rangle}
 \prod_p[1+\cos((dA)_p-i(df)_p)]\,d\nu.
\]

The identity |1+cos(theta-iy)|=cosh(y)+cos(theta) follows by squaring;
the right side is nonnegative. After taking absolute values and removing
the character, expand the product again. It imposes zero current on
S union T. Every admissible n then has its original weight multiplied by
product_(p:n_p=0) cosh((df)_p), bounded by the product over all faces.
This proves the existing complex-source comparison at the present scope:

\[
 Q_T^S(a)\le e^{-5\langle a,f\rangle}
           \prod_p\cosh((df)_p)\,Q_T^S(0).                 \tag{7}
\]

Let S contain k four-edge plaquette boundaries with pairwise disjoint
21-face neighborhoods, and let every a_e be +1 or -1. Take f_e=h a_e
on S and zero elsewhere. Each block has twenty exterior curls of
magnitude h and one central curl of magnitude at most 4h. Therefore

\[
 Q_T^S(a)\le c(h)^k Q_T^S(0),\qquad
 c(h)=e^{-20h}\cosh(4h)\cosh(h)^{20}.
\]

The convenient exact choice h=log 3 yields

\[
 \boxed{c=\frac{3281\,5^{20}}{3^{44}}
 =\frac{312900543212890625}{984770902183611232881}
 <\frac1{3000}.}                                        \tag{8}
\]

The last comparison is 938701629638671875000 < 984770902183611232881.
The choice h is not claimed optimal. This integrated bound improves the
previous partial-marginal estimate; it does not contradict the sharp
pointwise Fourier constant 1/16 at a fixed exterior angle environment.

For the same oriented local circulation variables Y_p as before, disjoint
event masses and global reversal give

\[
 \Pr(|Y_{p_i}|=1\ \forall i)
 \le\frac{(2c)^k}{1+(2c)^k}<\frac1{1+1500^k},
\]
\[
 \left|\mathbb E\prod_iY_{p_i}\right|
 \le\frac{2^{k-1}c^k}{1+2^{k-1}c^k}
 <\frac1{1+2\,1500^k}\quad(k\ \mathrm{even}).                \tag{9}
\]

Odd moments vanish. In particular a single circulation has probability
less than 1/1501, compatible-pair occurrence is less than 1/2250001,
and their absolute covariance is less than 1/4500001. These are genuine
full-measure bounds, also with the permitted zero-current conditioning.
They do not condition on arbitrary nonzero exterior currents or on a
fixed exterior plaquette assignment.

## 6. What remains to be proved

The constants in (9) have no distance variable and concern selected local
patterns, not every current configuration. The existing long thin-rectangle
construction in the source note carries an arbitrarily large current loop
without any fully charged elementary plaquette. Thus these blocks cannot
be extracted from every long current configuration.

The generic source/contact bound 25 C_j<=partial diag Pr(n_p=0) d is
already known. Its scalar ceiling 25 chi<=a accompanies b<=a, so these
two estimates alone cannot make b_lower-25 chi_upper positive.

The next actual estimate must control the charged paired components in
(4) or (5), or retain enough signed cancellation in (2)-(3) to bound chi
directly. It must have evaluated constants uniform in the required volume
and ordered limit profile. A compatible transverse lower bound is still
needed. None of those missing quantities is supplied by the finite audit
or by a rare local pattern. This continuation narrows the obstruction and
strengthens usable local estimates; it does not close the phase problem.
