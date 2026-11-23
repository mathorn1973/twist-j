# Centered frame bounds and a full-distribution slope comparison

NON-CANONICAL. Candidate-D. No Canon authority.

Item: C-RH-COMMON-GRAM-N. Action layer: NOT_APPLICABLE.
Author: A. M. Thorn, with Astra/Sol mathematical assistance.
Basis and source correspondence: [SOURCE_MAP.md](SOURCE_MAP.md).
Scope record: [PREREG.md](PREREG.md).

This note gives a paper derivation under the hypotheses of the pinned
`FrameLA1` and `TheoremFSharp`. The replacement theorem has not been checked
by Lean. No scientific numerical computation is used. The Hilbert-Schmidt
and projection inequalities are classical; no priority claim is made for
them. The contribution relative to the inspected source is to retain their
centered forms and compare the full slope distributions before taking a
mean. No global RH exponent or arithmetic construction is changed here.

## 1. Statement

Under the original hypotheses of `TheoremFSharp`, write U,H for its
nonnegative spread and target lower-slope budgets, e,eta for its two Gram
errors, and delta for its lost target-row fraction. Thus 0<=e<=1/4,
eta>=0 and 0<=delta<1. Define on [0,1]

\[
g_e(r)=\min\left\{1,r+\sqrt{\frac{e}{1-e}r(1-r)}\right\},
\qquad
f_\eta(p)=\frac{2p+\eta+\sqrt{\eta^2+4\eta p(1-p)}}{2(1+\eta)},
\]

\[
\Phi(r)=\min\left\{1,\frac{f_\eta(g_e(r))}{1-\delta}\right\}.
\]

Then the following replacement for the conclusion of that theorem holds:

\[
\boxed{
 s-\mu(C)\le (H+U)\Phi\!\left(\frac{U}{H+U}\right)-U
}\tag{1}
\]

when H+U>0. If H=U=0, the conclusion is directly mu(C)>=s.

In particular, e=eta=delta=0 gives mu(C)>=s for every U,H. More precisely,
the target slope distribution dominates the adjusted source distribution,
so its mean is at least the actual source mean, not only its lower bound s.

All integral maps, metrics, lattice degrees, local denominators and height
bounds are those of the original theorem. Its hypotheses are not weakened
or replaced by a conjectured symmetry or a least-eigenvalue bound.

## 2. Source and target trace conventions

Let V_i and H_amb be finite-dimensional complex inner-product spaces. Set
S=sum_i dim V_i>0 and D=dim H_amb>0. Let c_i>0 and B_i:V_i->H_amb. Define

\[
 K_i=c_i B_i^*B_i,\qquad
 T=\bigoplus_i K_i,\qquad Q=\sum_i c_iB_iB_i^*.
\]

The operator T is block diagonal. In a redundant family it is not the full
source Gram operator of the concatenated maps. Assume

\[
 \|T-I\|_{\rm HS}^2\le eS,\qquad 0\le e<1,
 \qquad
 \operatorname{tr}(Q^2)\le
 (1+\eta)\frac{\operatorname{tr}(Q)^2}{D},\qquad \eta\ge0.\tag{2}
\]

Trace cyclicity gives tr T=tr Q. If nu=tr T/S, Cauchy-Schwarz gives
|nu-1|<=sqrt(e), hence nu>0. Thus all trace fractions below are defined.
The original frame theorem has e<=1/4 and is within this domain. If D=0,
all target coranks are zero and no trace normalization is needed.

Choose arbitrary retained subspaces N_i<=V_i. Let P_i be the orthogonal
projection onto their complements, and put

\[
 P=\bigoplus_i P_i,\qquad
 r=\frac{\operatorname{tr}P}{S},\qquad
 L=\sum_i c_iB_iP_iB_i^*,\qquad Q'=Q-L.
\]

Then Q',L are positive semidefinite. The range of Q' is exactly
W=sum_i B_i(N_i): its kernel is the intersection of the kernels of the
adjoints of the retained maps. Put

\[
 p=\frac{\operatorname{tr}L}{\operatorname{tr}Q}
  =\frac{\operatorname{tr}(PT)}{\operatorname{tr}T}\in[0,1].
\]

No coordinate alignment of the N_i is assumed, and the B_i need not be
invertible or square.

## 3. Center the source projection

The identities

\[
 \|P-rI\|_{\rm HS}^2=Sr(1-r),\qquad
 \|T-\nu I\|_{\rm HS}^2
 =\|T-I\|_{\rm HS}^2-S(\nu-1)^2
 \le S\{e-(\nu-1)^2\}
\]

and the vanishing trace of P-rI give

\[
 (p-r)^2\le r(1-r)\frac{e-(\nu-1)^2}{\nu^2}.
\]

The remaining scalar comparison is exact:

\[
 \frac e{1-e}-\frac{e-(\nu-1)^2}{\nu^2}
 =\frac{(\nu-(1-e))^2}{(1-e)\nu^2}\ge0.
\]

Consequently

\[
 (1-e)(p-r)^2\le e r(1-r),\qquad p\le g_e(r).\tag{3}
\]

This normalization preserves the dependence of the error on the actual
discarded fraction. If r=0, the discarded trace is zero even when e>0.

## 4. Center the target projection

Let R_W be the orthogonal projection onto W-perp and let z=dim(W-perp)/D.
Write

\[
 b=\frac{\operatorname{tr}(R_WQ)}{\operatorname{tr}Q}.
\]

Since R_W Q'=0 and 0<=R_W<=I, positivity gives 0<=b<=p. With
mu=tr Q/D, equation (2) implies

\[
 \|Q-\mu I\|_{\rm HS}^2\le
 \eta\frac{\operatorname{tr}(Q)^2}{D},\qquad
 \|R_W-zI\|_{\rm HS}^2=Dz(1-z).
\]

Centering both terms in tr(R_W Q)-z tr Q therefore gives

\[
 (z-b)^2\le\eta z(1-z).\tag{4}
\]

If z>p, then (z-p)^2<=(z-b)^2. The larger root of
(z-p)^2<=eta z(1-z) is f_eta(p). If z<=p, the same conclusion follows
from f_eta(p)>=p. Thus, using monotonicity established below,

\[
 z\le f_\eta(p)\le f_\eta(g_e(r)).\tag{5}
\]

This is a corank conclusion. It does not assert that Q or Q' has a
uniformly positive least eigenvalue. At r=0 it gives z<=eta/(1+eta),
with no contribution from e.

## 5. Projection to the original target

Let pi:H_amb->C_v be the original surjective row projection, with
d=dim C_v>=(1-delta)D. For every subspace W<=H_amb,

\[
 d-\dim\pi(W)\le D-\dim W.
\]

The projected missing fraction is therefore at most z/(1-delta), and at
most 1. It is at most Phi(r). No integral lattice is replaced in taking
this complex vector-space rank estimate.

## 6. Monotonicity and concavity

For e=0, g_e is the identity. For 0<e<1, the function
r+sqrt(e/(1-e))*sqrt(r(1-r)) is concave. It is at least 1 exactly on
[1-e,1]. Its derivative at 1-e is 1/[2(1-e)]>0, so it is increasing up
to that point. Capping it at 1 leaves a nondecreasing concave function.

For eta=0, f_eta is the identity. For eta>0, it is a linear function plus
a positive multiple of the square root of the positive concave quadratic
eta^2+4 eta p(1-p). Hence it is concave. Its derivative at p=1 is zero,
so concavity makes it nondecreasing throughout [0,1]. Its endpoints are
f_eta(0)=eta/(1+eta), f_eta(1)=1. Directly from its defining quadratic,
f_eta(p)>=p.

A nondecreasing concave function composed with a concave function is
concave. Positive scaling preserves concavity, and capping a concave
function by a constant does too, as can be seen by intersecting their
hypographs. Consequently Phi is concave and nondecreasing, and

\[
 0\le r\le\Phi(r)\le1,\qquad \Phi(1)=1.\tag{6}
\]

## 7. Full-distribution comparison

Let a and b denote finite lists with their normalized positive dimension
weights. E denotes a finite weighted mean only. Write
F_a(x)=Pr(a<x), F_b(x)=Pr(b<x), meaning the corresponding weighted
fractions of entries, with no probabilistic or physical interpretation.

Suppose, for every real threshold x,

\[
 F_b(x)\le\Phi(F_a(x)),\qquad
 E a\ge s,\quad a\le s+U,\quad b\ge s-H.\tag{7}
\]

Let ell=s-H, h=s+U and ell_width=H+U>0. Elementary integration of finite
step functions gives

\[
 \int_\ell^h F_a(x)\,dx
 =h-E\max(a,\ell)\le h-Ea\le U,
\]

\[
 Eb\ge E\min(b,h)=h-\int_\ell^hF_b(x)\,dx.
\]

Apply finite Jensen on the intervals on which F_a is constant, followed
by monotonicity of Phi. Then

\[
 \int_\ell^h F_b(x)\,dx
 \le\int_\ell^h\Phi(F_a(x))\,dx
 \le (H+U)\Phi\!\left(\frac{U}{H+U}\right).
\]

Substitution proves (1). Strict and weak distribution conventions differ
at finitely many points only; the source correspondence uses strict ones
consistently. This proof needs no continuous approximation and no estimate
of each separate threshold by U/(U+tau).

If H=0, b>=s already gives the conclusion, and for U>0 the formula gives
U Phi(1)-U=0. If U=0<H, all a equal s, and the formula gives
H min(1,eta/((1+eta)(1-delta))). If H=U=0, no quotient is introduced.

## 8. Why (7) follows from the actual source

In the pinned `TheoremFSharp.lean`, the adjusted realified source slopes
are a_ij=2*lambda_ij+slopeNormalisingConstant(K)-h_i. For tau=s-x,
the exact count below x equals

    [K:Q] * sum_i (dim_K V_i - rank_K N_i(tau)).

The total realified source rank is [K:Q]*S. Thus the discarded complex
dimension fraction is exactly F_a(x). The original mean and maximum
assumptions give Ea>=s and a<=s+U.

The original `hMle` holds for every real tau: the sum of the images of
N_i(tau) is contained in the target Harder-Narasimhan step at threshold x.
Together with (5) and the original row projection, this gives
F_b(x)<=Phi(F_a(x)) for every real x. The original `hlow` gives b>=s-H
and `hmean` identifies Eb=mu(C).

The original restriction tau>=0 occurs only in the separate bound on
F_a(s-tau) by U/(U+tau), not in the structural inclusion or rank identities.
Using the exact fraction avoids that restriction. The sharper original
image-inclusion argument has no log(card I) loss. Neither a factor 2 nor
[K:Q] remains after the normalized counting.

This is a paper replacement of the original derivation. Lean would need a
new theorem and a finite-step integration argument; the existing file
uses continuity of the old smooth envelope. It cannot be changed by just
substituting a new expression in the final line.

## 9. Exact comparisons and an elementary error bound

Put r0=U/(H+U). Relative to integration only below s, the saving is

\[
 H\Phi(r_0)-\{(H+U)\Phi(r_0)-U\}=U(1-\Phi(r_0))\ge0.
\]

The new loss is between 0 and H. In the ideal case it is exactly zero.
This is not a claim that the bound is globally sharp for arithmetic
lattices.

For an elementary upper bound define

\[
 E_0=\sqrt{\frac{e}{1-e}UH},\qquad L_0=H+U.
\]

The exact expression in (1) satisfies

\[
 \boxed{
 (H+U)\Phi(r_0)-U
 \le\min\left\{H,
 \frac{\delta U+E_0+\eta L_0+
 \sqrt{\eta L_0(U+E_0)}}{1-\delta}\right\}.
 }\tag{8}
\]

Indeed L_0 g_e(r0)<=U+E_0, and
f_eta(p)-p<=eta+sqrt(eta*p), from sqrt(a+b)<=sqrt(a)+sqrt(b).
Using Phi<=f_eta(g_e)/(1-delta) proves (8). This bound displays how the
errors couple to the source spread; no independent term proportional to
U survives when e=eta=delta=0.

The new loss also does not exceed the earlier below-threshold bound

\[
 \frac{\eta H+2D_0+2\sqrt{eHD_0/(1-e)}}{1-\delta},
 \qquad D_0=\frac{UH}{U+H},
\]

To see this directly, set z=f_eta(p). Its quadratic relation implies
z<=p+sqrt(eta*z)<=p+(eta+z)/2, hence f_eta(p)<=2p+eta. Combine this
with g_e(r)<=r+sqrt(e*r/(1-e)), Hr0=D0, and the preceding exact saving.

For e<=1/4, it therefore does not exceed
[eta H+4 D_0+4 sqrt(e)H]/(1-delta). Finally
D_0<=U log(1+H/U) for U>0, so it improves the original displayed
`TheoremFSharp` allowance. At U=0 use the separate expression above.
This is an upper-bound comparison, not a lower bound on the old actual
loss or a claim that either allowance is attained by the actual lattices.

## 10. A failed stronger shortcut

The abstract frame hypotheses do not imply a positive least-eigenvalue
bound depending only on e and eta uniformly in dimension. Let D>=2 and
take two one-dimensional unit sources in every direction e_1,...,e_(D-1).
Then K_i=I, e=0, no directions are discarded, and

\[
 Q=2I_{D-1}\oplus0,\qquad \eta=\frac1{D-1}
\]

satisfies (2) with equality. The error eta can be arbitrarily small while
Q has a kernel. This example belongs to the exact abstract domain; no
claim is made that it is an automorphic theta family.

For a strictly positive version, replace the two e_1 sources by
sqrt(1-t)e_1+sqrt(t)e_D and sqrt(1-t)e_1-sqrt(t)e_D, 0<t<1/2. Then

\[
 Q=\operatorname{diag}(2(1-t),2,\ldots,2,2t),\qquad
 \operatorname{tr}(Q^2)=4(D-1)-8t(1-t).
\]

The same eta works and the least eigenvalue tends to zero at fixed D.
For rational examples choose sqrt(t)=2u/(1+u^2) and
sqrt(1-t)=(1-u^2)/(1+u^2) with positive rational u tending to zero.
This is an explicit symbolic family, not a numerical experiment.

## 11. Remaining scope

The statement strengthens one frame-to-slope comparison. It does not
construct the theta maps, justify their arithmetic inputs, remove their
other local or archimedean errors, or provide uniform windows. In the
published error bookkeeping, terms of the shape x/m and m arise already
before this comparison. No change in the global square-root exponent is
claimed. No relation to a TWIST-J physical or rapidity carrier is asserted.

The proof is complete as an abstract finite-dimensional derivation and as
a conditional source-level replacement. Formal Lean implementation and
public promotion are separate work. The candidate status remains D.
