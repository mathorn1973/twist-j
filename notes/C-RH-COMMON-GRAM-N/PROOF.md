# An exact concave refinement of Brox's centered frame comparison

NON-CANONICAL. Candidate-D. No Canon authority.

Item: C-RH-COMMON-GRAM-N. Action layer: NOT_APPLICABLE.
Author: A. M. Thorn, with Astra/Sol mathematical assistance.
Basis and source correspondence: [SOURCE_MAP.md](SOURCE_MAP.md).
Frozen original scope record: [PREREG.md](PREREG.md).

## Attribution and scope

Jose Brox's earlier frame-degree compatibility note already proves the
centered projection inequality, its scale-invariant source defect, a
comparison over the whole slope interval, and zero loss for an uncut
perfect frame. Its first recorded public-repository commit is
28fcc17cc06b4ed6dad0e4b2967f877629d11f56, dated 21 November 2026.
His companion bridge applies that comparison to the actual arithmetic
maps; his later one-sided note gives different bounds with additional
operator information. The full references are in SOURCE_MAP.md.

Relative to those notes, the refinement here is to invert the centered
target inequality exactly, compose the capped source and target
envelopes, and apply finite Jensen to that composition. The note also
audits every real threshold in the pinned Lean application, records an
elementary upper bound, and retains a least-eigenvalue counterexample.
No general priority claim is made for any classical inequality or for
the method of full-distribution comparison.

The original attribution review missed Brox. Its correction is appended
in REVIEW.md without rewriting that historical review. The present
paper theorem is not Lean-checked. No scientific numerical computation,
new RH exponent, arithmetic construction, or Canon promotion is claimed.

## 1. Statement

Keep the original arithmetic hypotheses of TheoremFSharp. Write U,H for
its nonnegative source-spread and target lower-slope budgets. Its matrix
hypotheses give a raw source error bound 0<=e<=1/4, a target isotropy
bound eta>=0, and a lost-row bound 0<=delta<1.

For the same comparison matrices, define the block-diagonal source
operator T and target operator Q as in section 2, and put
S=dim(source), M=tr(T)=tr(Q)>0, nu=M/S. Use the exact centered defect

\[
 a^2=\frac{S\operatorname{tr}(T^2)}{M^2}-1
     =\frac{S\|T-\nu I\|_{\rm HS}^2}{M^2},\qquad a\ge0.
\]

For r,p in [0,1], define

\[
 g_a(r)=\min\{1,r+a\sqrt{r(1-r)}\},\qquad
 f_\eta(p)=
 \frac{2p+\eta+\sqrt{\eta^2+4\eta p(1-p)}}{2(1+\eta)},
\]

\[
 \Psi(r)=\min\left\{1,\frac{f_\eta(g_a(r))}{1-\delta}\right\}.
\]

Then, for H+U>0,

\[
 \boxed{
 s-\mu(C)\le (H+U)\Psi\!\left(\frac{U}{H+U}\right)-U.
 }\tag{1}
\]

If H=U=0, the conclusion is directly mu(C)>=s. The function Psi is
nondecreasing, concave, and at least the identity.

The raw source parameter is an upper bound, not generally the exact
centered defect. Section 3 proves

\[
 a^2\le\frac e{1-e}.
\]

Thus the originally recorded bound with
g_e(r)=min(1,r+sqrt(e*r*(1-r)/(1-e))) and
Phi_e=min(1,f_eta(g_e)/(1-delta)) remains a valid corollary, and (1)
is never larger when eta and delta are held fixed. PREREG.md retains
that original scope and formula unchanged.

One may use the exact target values
eta_0=D*tr(Q^2)/M^2-1 and delta_0=1-d/D, or certified upper bounds
eta>=eta_0, delta>=delta_0. All comparisons with Brox below use the SAME
eta and delta on both sides. A bound evaluated at coarse inputs is
not claimed to beat another bound evaluated at better actual inputs.

In the centered perfect-frame case a=eta=delta=0 the loss is zero, as
already established by Brox. The target slope distribution then
dominates the adjusted source distribution. All integral maps, metrics,
lattice degrees, local denominators and height bounds remain those of
the original theorem.

## 2. Source and target trace conventions

Let V_i and H_amb be finite-dimensional complex inner-product spaces.
Set S=sum_i dim(V_i)>0 and D=dim(H_amb)>0. Let c_i>0 and
B_i:V_i->H_amb. Define

\[
 K_i=c_iB_i^*B_i,\qquad
 T=\bigoplus_iK_i,\qquad Q=\sum_i c_iB_iB_i^*.
\]

T is block diagonal; for a redundant family it is not the full Gram
operator of the concatenated maps. The original hypotheses supply

\[
 \|T-I\|_{\rm HS}^2\le eS,\quad 0\le e<1,\qquad
 \operatorname{tr}(Q^2)\le(1+\eta)\frac{\operatorname{tr}(Q)^2}{D},
 \quad\eta\ge0.\tag{2}
\]

Trace cyclicity gives M=tr(T)=tr(Q). Cauchy-Schwarz gives
|nu-1|<=sqrt(e)<1, so M>0. The centered frame argument itself needs
only M>0 and the target inequality; (2) supplies them in the original
arithmetic application. If the target dimension is zero, all target
coranks vanish and no trace normalization is used.

Choose retained subspaces N_i<=V_i. Let P_i be the orthogonal projection
onto their complements, and put

\[
 P=\bigoplus_iP_i,\qquad r=\frac{\operatorname{tr}P}{S},\qquad
 L=\sum_i c_iB_iP_iB_i^*,\qquad Q'=Q-L.
\]

Both L and Q' are positive semidefinite. The range of Q' is
W=sum_i B_i(N_i): its kernel is the intersection of the kernels of
the adjoints of the retained maps. Define the discarded trace fraction

\[
 p=\frac{\operatorname{tr}L}{M}
  =\frac{\operatorname{tr}(PT)}M\in[0,1].
\]

No coordinate alignment is assumed. The B_i may be rectangular,
redundant, singular, or zero.

## 3. The exact centered source defect

Centering both operators gives

\[
 \operatorname{tr}((P-rI)(T-\nu I))=M(p-r),\qquad
 \|P-rI\|_{\rm HS}^2=Sr(1-r).
\]

Hilbert-Schmidt Cauchy-Schwarz therefore proves

\[
 |p-r|\le a\sqrt{r(1-r)},\qquad p\le g_a(r).\tag{3}
\]

This is the source side of Brox's centered projection argument,
written for discarded rather than retained directions.

For the exact raw error e_act=||T-I||_HS^2/S, the identity is

\[
 a^2=\frac{e_{\rm act}-(\nu-1)^2}{\nu^2}.
\]

If e is only the supplied bound e_act<=e<1, this gives an inequality,
not equality with e. The scalar calculation

\[
 \frac e{1-e}
 -\frac{e-(\nu-1)^2}{\nu^2}
 =\frac{(\nu-(1-e))^2}{(1-e)\nu^2}\ge0
\]

proves a^2<=e/(1-e) and recovers the original
(1-e)(p-r)^2<=e*r*(1-r).

For completeness, Brox's optimal common normalization is exact. Under
c_i -> t*c_i with t>0, write U_s=tr(T^2). Then

\[
 e(t)=\frac{t^2U_s-2tM+S}{S},\qquad
 t_*=\frac M{U_s},\qquad
 e_*=1-\frac{M^2}{S U_s}=\frac{a^2}{1+a^2}.
\]

The parameter a and the normalized target defect are unchanged by
this rescaling. Moreover sqrt(e_*/(1-e_*))=a. This concerns the
auxiliary comparison matrices and their scalar weights; no arithmetic
map is multiplied by a nonintegral scalar and no global height is
changed. Formula (1) can simply use a from the original matrices
without performing any rescaling.

## 4. The exact target envelope

Let R_W project onto W-perp and put z=dim(W-perp)/D and
b=tr(R_W Q)/M. Since R_W Q'=0 and 0<=R_W<=I, positivity gives
0<=b<=p. With mu=M/D, equation (2) implies

\[
 \|Q-\mu I\|_{\rm HS}^2\le\eta M^2/D,\qquad
 \|R_W-zI\|_{\rm HS}^2=Dz(1-z).
\]

Centering the target trace proves

\[
 (z-b)^2\le\eta z(1-z).\tag{4}
\]

This is the target side of Brox's centered argument. If z>p, then
(z-p)^2<=(z-b)^2. Solving the resulting quadratic gives the larger
root f_eta(p). If z<=p, use f_eta(p)>=p. Thus

\[
 z\le f_\eta(p)\le f_\eta(g_a(r)).\tag{5}
\]

Monotonicity used here is proved in section 6. This is a corank
bound, not a positive least-eigenvalue bound. At r=0 it gives
z<=eta/(1+eta), with no source-defect contribution.

## 5. Projection to the original target

Let pi:H_amb->C_v be the original surjective row projection,
d=dim(C_v)>0, and d>=(1-delta)D. Every subspace W satisfies

\[
 d-\dim\pi(W)\le D-\dim W.
\]

The projected missing fraction is consequently at most z/(1-delta)
and at most one, hence at most Psi(r). This is a complex-vector-space
rank estimate on the original maps; it replaces no integral lattice.

## 6. Monotonicity and concavity

For a=0, g_a is the identity. For a>0, the function
r+a*sqrt(r(1-r)) is concave and is at least one exactly on
[1/(1+a^2),1]. Its derivative at the left endpoint of that interval
is (1+a^2)/2>0. It is therefore increasing up to that endpoint;
capping at one leaves a nondecreasing concave function.

For eta=0, f_eta is the identity. For eta>0, its expression is a
linear function plus a positive multiple of the square root of the
positive concave quadratic eta^2+4*eta*p*(1-p). It is concave and
has derivative zero at p=1, so it is nondecreasing throughout [0,1].
Its endpoints are eta/(1+eta) and one, and f_eta(p)>=p.

Composition with a nondecreasing concave outer function preserves
concavity. Positive scaling and capping by a constant also preserve
concavity; for the latter, intersect the hypograph with a half-space.
Consequently

\[
 0\le r\le\Psi(r)\le1,\qquad \Psi(1)=1,\tag{6}
\]

and Psi is nondecreasing and concave.

## 7. Finite full-distribution comparison

Let alpha and beta denote finite lists with normalized positive
weights. E means a finite weighted average. Write
F_alpha(x)=Pr(alpha<x), F_beta(x)=Pr(beta<x) for the corresponding
weighted fractions, with no physical probability interpretation.
Assume at every real threshold

\[
 F_\beta(x)\le\Psi(F_\alpha(x)),\qquad
 E\alpha\ge s,\quad \alpha\le s+U,\quad \beta\ge s-H.\tag{7}
\]

Set ell=s-H, h=s+U, and L_0=H+U>0. Integrating the finite step
functions gives exactly

\[
 \int_\ell^h F_\alpha(x)\,dx
 =h-E\max(\alpha,\ell)\le h-E\alpha\le U,
\qquad
 E\beta\ge E\min(\beta,h)=h-\int_\ell^hF_\beta(x)\,dx.
\]

Apply Jensen to the finitely many intervals on which F_alpha is
constant, and then use monotonicity:

\[
 \int_\ell^hF_\beta(x)\,dx
 \le\int_\ell^h\Psi(F_\alpha(x))\,dx
 \le L_0\Psi\!\left(\frac1{L_0}\int_\ell^hF_\alpha(x)\,dx\right)
 \le L_0\Psi(U/L_0).
\]

This proves (1). The interval, source clipping and ideal-frame mean
comparison are already present in Brox. The refinement applies Jensen
to the exact composed envelope before estimating its separate errors.
Strict versus weak counts differ only at finitely many endpoints.

If H=0, the target lower bound already proves the result and the
formula is U*Psi(1)-U=0. If U=0<H, every alpha equals s, and the
formula is H*min(1,eta/((1+eta)(1-delta))). If H=U=0, no quotient
is introduced.

The last Jensen bound is sharp as a statement about finite lists with
arbitrary real weights satisfying (7). Put alpha at ell and h with
weights r0=U/L_0 and 1-r0; put beta at the same endpoints with weights
Psi(r0) and 1-Psi(r0). Omit zero-weight entries. The source mean is s,
the CDF condition holds, and equality holds in (1). This observation
does not construct frame matrices or arithmetic lattices realizing
those lists, and asserts no such optimality for the arithmetic theorem.

## 8. All thresholds in the pinned Lean application

In the pinned TheoremFSharp.lean, the adjusted realified source slopes
are alpha_ij=2*lambda_ij+slopeNormalisingConstant(K)-h_i. For tau=s-x,
the exact count below x is

    [K:Q] * sum_i (dim_K V_i - rank_K N_i(tau)).

The total realified source rank is [K:Q]*S, so the discarded complex
dimension fraction is F_alpha(x). The original mean and maximum
assumptions give E alpha>=s and alpha<=s+U.

The original hMle is proved for every real tau: the sum of the images
of N_i(tau) is in the target HN step at threshold x. Equation (5)
and the row projection therefore imply (7) for every real x.
The original hlow gives beta>=s-H and hmean identifies E beta=mu(C).

The restriction tau>=0 belongs to the separate coarse envelope
F_alpha(s-tau)<=U/(U+tau), not to the structural image inclusion
or the exact counting argument. The local helper hfilt lies inside
hcor, but its proof does not use that sign hypothesis. A Lean port
must extract this count identity with an all-real signature, then
supply finite-step Jensen/integration. It cannot silently reuse the
old smooth-envelope continuity argument.

The source-to-target inclusion has no log(card I) loss. The field
degree [K:Q] cancels from the normalized rank fractions. The factor
two is already included in alpha_ij and in the source threshold
(x+h_i-slopeNormalisingConstant(K))/2, in the original squared-norm
units; no additional factor is inserted in (1). Brox already supplied
an actual-source bridge; this section records the precise hMle/hfilt
audit at our source pin.

## 9. Comparisons and an elementary upper bound

Let L_0=H+U>0, r0=U/L_0 and B_a=L_0*Psi(r0)-U.
By (6), 0<=B_a<=H. Since a<=sqrt(e/(1-e)), monotonicity also gives
B_a<=B_e, where B_e is the originally recorded raw-e expression.

### Comparison with Brox (3.2)

Use the same a, eta and delta in both bounds. Define

\[
 \Phi_{\rm B}(U,H)=
 \begin{cases}
 \sqrt{UH},& U\le H,\\
 (U+H)/2,& U>H,
 \end{cases}
\qquad
 B_{\rm B}=
 \frac{\delta U+a\Phi_{\rm B}(U,H)+\sqrt{\eta}(U+H)/2}{1-\delta}.
\]

For z=f_eta(p), the defining quadratic and z>=p give
z-p=sqrt(eta*z*(1-z))<=sqrt(eta)/2. Also
g_a(r0)<=r0+a*sqrt(r0*(1-r0)). Consequently

\[
 B_a\le
 \frac{\delta U+a\sqrt{UH}+\sqrt{\eta}L_0/2}{1-\delta}
 \le B_{\rm B}.
\]

Together,

\[
 B_a\le\min\{H,B_{\rm B},B_e\}.\tag{9}
\]

If Brox uses exact eta_0,delta_0, use those exact values here too.
No dominance is asserted over his one-sided bounds when they have
additional positive-trace or operator-majorant information.

For example, B=I_D with common weight c=3/4 has raw e=1/16 but
a=eta=delta=0. With U=3,H=5, the old raw-e expression is one,
whereas the centered expression and Brox (3.2) are zero. This is
why the invariant parameter is retained.

### The below-s comparator and its missing chord justification

Let Z=s-alpha. Then Z>=-U and E Z<=0. For every z>=-U,

\[
 \min\{H,z_+\}\le\frac{H(z+U)}{H+U}.
\]

For -U<=z<=0 this follows from positivity of the right side; for
0<=z<=H it follows from U*z<=U*H, including U=0; for z>=H the right side is at
least H. Taking means proves

\[
 \int_{s-H}^{s}F_\alpha(x)\,dx
 =E\min\{H,Z_+\}\le K_0:=\frac{UH}{U+H}.
\]

This is the integrated rank-loss chord bound also used in the
Hexagon note 2611.00828v1. For H>0, finite Jensen on [s-H,s] gives
the valid below-s allowance H*Psi(K_0/H)=H*Psi(r0), because
s-E beta<=E(s-beta)_+. The case H=0 is immediate. Thus the exact
difference between these two displayed allowances is

\[
 H\Psi(r0)-B_a=U(1-\Psi(r0))\ge0.
\]

This justifies the comparator which the earlier version stated
without proof.

### Elementary bounds and the original allowance

Set E_0=a*sqrt(UH). From
L_0*g_a(r0)<=U+E_0 and
f_eta(p)-p<=eta+sqrt(eta*p), one obtains

\[
 \boxed{
 B_a\le\min\left\{H,
 \frac{\delta U+E_0+\eta L_0+
       \sqrt{\eta L_0(U+E_0)}}{1-\delta}\right\}.
 }\tag{8}
\]

The second scalar inequality follows directly from the formula for
f_eta and sqrt(x+y)<=sqrt(x)+sqrt(y). Substituting the upper bound
a<=sqrt(e/(1-e)) recovers the former raw-e version of (8).

Also z=f_eta(p) obeys
z<=p+sqrt(eta*z)<=p+(eta+z)/2, hence z<=2p+eta.
Use g_a(r)<=r+a*sqrt(r) and B_a<=H*Psi(r0) to obtain

\[
 B_a\le
 \frac{\eta H+2K_0+2a\sqrt{H K_0}}{1-\delta}
 \le
 \frac{\eta H+2K_0+
       2\sqrt{e H K_0/(1-e)}}{1-\delta}.
\]

For e<=1/4 and K_0<=H, this is at most
[eta H+4 K_0+4 sqrt(e)H]/(1-delta).
For U>0, K_0<=U log(1+H/U); at U=0 use the separate formula in
section 7. This compares the new allowance with the original
displayed TheoremFSharp allowance. None of these upper-bound
comparisons asserts attainment by the actual arithmetic lattices.

## 10. A failed stronger shortcut

The abstract frame hypotheses do not imply a positive least-eigenvalue
bound depending only on the defects uniformly in dimension. For D>=2,
take two one-dimensional unit sources in every direction
e_1,...,e_(D-1). Then K_i=I, e=a=0, no source directions are discarded,
and

\[
 Q=2I_{D-1}\oplus0,\qquad \eta=\frac1{D-1}
\]

satisfies (2) with equality. The target defect can be arbitrarily
small while Q has a kernel. This is an abstract family, not a
claimed automorphic theta construction.

For a positive-definite version, replace the two e_1 sources by
sqrt(1-t)e_1+sqrt(t)e_D and sqrt(1-t)e_1-sqrt(t)e_D, 0<t<1/2.
Then

\[
 Q=\operatorname{diag}(2(1-t),2,\ldots,2,2t),\qquad
 \operatorname{tr}(Q^2)=4(D-1)-8t(1-t).
\]

The same eta works while the least eigenvalue tends to zero at fixed D.
Rational vectors are obtained from sqrt(t)=2u/(1+u^2) and
sqrt(1-t)=(1-u^2)/(1+u^2) for sufficiently small positive rational u.
This is a symbolic family, not a numerical experiment.

## 11. Remaining scope

This is an exact concave refinement of a centered frame comparison
already established by Brox. It does not construct theta maps, supply
their arithmetic hypotheses, remove the other local or archimedean
errors, or prove uniform windows. Brox's bridge already records that
the four normalized error shapes have contributions before the frame
comparison. No change in the global square-root exponent is claimed.

The note establishes an abstract paper derivation and its conditional
source-level substitution. A Lean implementation and any public
promotion are separate work. No common algebra, TWIST-J physical
carrier, rapidity identification, or new semistability candidate is
asserted. Status remains candidate-D.
