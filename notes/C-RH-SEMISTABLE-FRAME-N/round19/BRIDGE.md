# Round 19. The actual Gram input and its two-copy test

**NON-CANONICAL. No authority. Candidate-D under the stated hypotheses.**
The new estimate for the actual periods remains **O**. No scientific
computation or Lean build was performed.

## 1. A transfer that does not divide by small singular values

Retain the genuine full normalized period maps of [round 18](../round18/SOURCE.md),
not an arbitrary existential matrix witness. Write

$$
 A_u:E_u\longrightarrow F,\quad D=\dim F>0,\quad
 R=\sum_u\dim E_u>0,\quad B_u=A_uA_u^*.
$$

Here $B_u$ is a positive endomorphism of the full target, **not** the
arithmetic cut map called $B_k$ in the source. Let $H_u$ be the orthogonal
projection onto $\operatorname{im}A_u$. Assume the actual diagonal estimate

$$
 \sum_u\|A_u^*A_u-I\|_{\rm HS}^2\le eR. \tag{19.B1}
$$

This is the only approximation hypothesis in this transfer. For
$\Delta_u=B_u-H_u$, the nonzero squared singular values of $A_u$ give

$$
 \kappa=R^{-1}\sum_u\dim\ker A_u\le e,\qquad
 \sum_u\|\Delta_u\|_{\rm HS}^2\le eR,\qquad
 \sum_u\|\Delta_u\|_1\le R\sqrt e. \tag{19.B2}
$$

The last inequality applies Cauchy--Schwarz to all the nonzero singular
directions together; their number is at most $R$. It does not assert a
small operator norm for any individual $\Delta_u$.

For any orthogonal projection $X$, its commutator with a Hermitian matrix
retains just the two off-diagonal blocks relative to $X$. Hence
$\|[X,\Delta_u]\|_{\rm HS}^2\le\|\Delta_u\|_{\rm HS}^2$.
The squared triangle inequality and [the principal-angle loss](PROOF.md)
therefore give

$$
 \begin{aligned}
 \operatorname{tr}(XH_u)-\dim(\operatorname{ran}X\cap\operatorname{im}A_u)
   &\ge \tfrac12\|[X,H_u]\|_{\rm HS}^2,\\
 \tfrac12\sum_u\|[X,H_u]\|_{\rm HS}^2
   &\ge \tfrac14\sum_u\|[X,B_u]\|_{\rm HS}^2-\tfrac12 eR.
 \end{aligned} \tag{19.B3}
$$

This averaged estimate avoids polar inversion and does not discard a
singular direction. Its loss remains independent of the dimensions.

## 2. A sufficient test in the existing multiplicity blocks

Keep the common image-preserving star algebra and its actual intertwiners
from [round 17](../round17/REPORT.md). In its notation,

$$
 F=\bigoplus_\beta\mathbb C^{s_\beta}\otimes M_\beta,\qquad
 A_u=\bigoplus_\beta I_{s_\beta}\otimes a_{u,\beta}.
$$

Use only nonzero target blocks. Put $m_\beta=\dim M_\beta$,
$B_{u,\beta}=a_{u,\beta}a_{u,\beta}^*$ and

$$
 q_\beta=\frac{s_\beta m_\beta}{D},\qquad
 b_\beta=\frac{s_\beta\sum_u\operatorname{rank}a_{u,\beta}}R,
 \qquad Q_\beta=\frac DR\sum_u B_{u,\beta}.
$$

Define a normalized positive operator on the matrix space of $M_\beta$ by

$$
 \mathcal L_{B,\beta}(Y)=\frac D{2R}
       \sum_u[B_{u,\beta},[B_{u,\beta},Y]]. \tag{19.B4}
$$

Suppose its quadratic form on traceless Hermitian matrices is at least
$\gamma_\beta\|Y\|_{\rm HS}^2$, with $\gamma_\beta\ge0$.
Suppose also that there is a decomposition into Hermitian matrices

$$
 Q_\beta=C_\beta+L_\beta,\qquad
 \lambda_{\max}(C_\beta)-\lambda_{\min}(C_\beta)
       \le\gamma_\beta/2. \tag{19.B5}
$$

This can be a spectral clipping of $Q_\beta$ to an interval, but no
commutation between the two terms is needed in the proof. In a
one-dimensional block take $C_\beta=Q_\beta$, $L_\beta=0$.

**Candidate-D.** The full concentration defect satisfies

$$
 \boxed{
 \epsilon(A)\le\kappa+\sum_\beta(b_\beta-q_\beta)_+
       +\sqrt e+\frac e2
       +\frac1D\sum_\beta s_\beta\|L_\beta\|_1 .}
       \tag{19.B6}
$$

To prove this, take the largest maximizing subspace. The common algebra
makes its projection $X=\bigoplus_\beta I_{s_\beta}\otimes X_\beta$.
Write $x_\beta=\operatorname{rank}X_\beta/m_\beta$ and
$Y_\beta=X_\beta-x_\beta I$. The scalar part of its incidence bound is
$\kappa+\sum_\beta(b_\beta-q_\beta)x_\beta$.
Replacing the remaining trace against $\sum H_u$ by the trace against
$\sum B_u$ costs at most $\sqrt e$ by (19.B2), since
$\|\bigoplus I_{s_\beta}\otimes Y_\beta\|_{\rm op}\le1$.
The second line of (19.B3), after division by $R$, retains at least
half of (19.B4) with weight $s_\beta/D$ and costs $e/2$.

The positive and negative parts of $Y_\beta$ both have trace
$m_\beta x_\beta(1-x_\beta)=\|Y_\beta\|_{\rm HS}^2$.
Consequently (19.B5) implies
$\operatorname{tr}(Y_\beta C_\beta)
 \le(\gamma_\beta/2)\|Y_\beta\|_{\rm HS}^2$.
This is paid by the retained half-gap. Trace duality bounds the remainder
by $\|L_\beta\|_1$. Maximizing the scalar terms proves (19.B6).

In the absence of tails the new condition is simply
$\operatorname{diam}(Q_\beta)\le\gamma_\beta/2$.
It permits a nonzero diameter. It does not require an exponentially small
centered variance. With exact image projectors instead of $B_u$, the
sharper threshold is gap at least diameter, as proved in PROOF.md.

Under the strong suppliers retained in round 17, $e$ and the kernel and
coarse block-mass errors have exponential bounds. Thus (19.B6) would give
an exponential all-subspace bound if (19.B4)--(19.B5) held with an
exponentially small weighted tail. After the actual cuts, retain the
source fraction $\alpha>0$ and target fraction $\beta>0$. The existing
cut lemma gives

$$
 \epsilon(B_k^{\rm arithmetic})
 \le\frac{\epsilon(A)+\max(1-\alpha,1-\beta)}{\alpha}.
 \tag{19.B7}
$$

**O.** No uniform actual-period estimate for (19.B4)--(19.B5) has been
established. A bound for all projections in the round 17 algebra is not a
bound for (19.B4). Refining the algebra by all image projectors also
changes the central masses, which need a fresh estimate.

## 3. Which ordered traces would test the gap?

On one matrix space, before normalization, set

$$
 \Psi_B(Y)=\sum_u B_uYB_u,\qquad S_2=\sum_u B_u^2.
$$

**Candidate-D.** Vectorization gives

$$
 \mathcal L_B=\tfrac12(L_{S_2}+R_{S_2})-\Psi_B,
 \qquad
 \operatorname{tr}_{\operatorname{End}F}(\Psi_B^\ell)
   =\sum_{u_1,\ldots,u_\ell}
       \left|\operatorname{tr}_F(B_{u_1}\cdots B_{u_\ell})\right|^2.
 \tag{19.B8}
$$

Here $L_{S_2}$ and $R_{S_2}$ mean left and right multiplication, respectively.
The formula follows because $Y\mapsto CY C^*$ has matrix-space trace
$|\operatorname{tr}C|^2$, and a product of the summands in $\Psi_B$
has $C=B_{u_1}\cdots B_{u_\ell}$. For $G_{uv}=A_u^*A_v$,

$$
 \operatorname{tr}_F(B_{u_1}\cdots B_{u_\ell})
 =\operatorname{tr}_{E_{u_1}}
       (G_{u_1u_2}\cdots G_{u_\ell u_1}). \tag{19.B9}
$$

Round 18 provides each ordered cycle in (19.B9) as an absolutely
convergent geometric expansion. Its absolute square pairs two copies of
that expansion. The finite level factor of such a pair is

$$
 \chi_2(k_\circ)\overline{\chi_2(k'_\circ)}.
 \tag{19.B10}
$$

Both closing rational elements are special unitary in the stated
two-prime realization, but this relative additive phase need not be one.
Absolute summability justifies taking the product for each fixed finite
cycle and then summing its finitely many word tuples. It supplies no
cancellation estimate for (19.B10). The antiunitary class-coordinate
conjugation from round 18 disappears in the absolute square.

The moments of $\sum_uB_u$ sum the traces (19.B9). The two-copy operator
sums their absolute squares and, in mixed words of its Laplacian, retains
additional left/right multiplication terms. These are different data.
Even all moments of the summed frame fail to determine concentration, by
the exact example in [OPPOSITION.md](OPPOSITION.md). Conversely, finitely
many unlocalized moments of $\Psi_B$ need not bound the desired restricted
gap. A gap proof must separate the known zero modes and control the
smallest remaining eigenvalue. The block projectors must also be inserted
correctly; a general non-diagonal source projector cannot be deleted from
the geometric cycle formula.

## 4. The weaker quantity used by the original slope argument

The original linear-algebra interface concerns the span after a small
**total source loss**. Its bounds do not require the new gap test. The
following is the centered compression argument already familiar from
the Brox reading: it is the complementary-subspace form of his
`frame-degree-compatibility.md`, equation (2.1), solved for the missing
target fraction. The derivation is included to fix the quantifiers.
The precise current source and literature interfaces are in [SOURCE.md](SOURCE.md).

Choose retained source spaces $E'_u\le E_u$, and write

$$
 \delta=R^{-1}\sum_u\operatorname{codim}E'_u,\qquad
 w=D^{-1}\operatorname{codim}\left(\sum_u A_uE'_u\right).
$$

Let $t=\sum_u\operatorname{tr}B_u>0$ and let
$\eta=D^{-1}\|D\sum_uB_u/t-I\|_{\rm HS}^2$.
With the same $e$ as in (19.B1), put
$a=\min(1,\delta+(R/t)\sqrt{e\delta(1-\delta)})$.
For the orthogonal complement of the surviving span, its projection $X$
satisfies $XA_u|_{E'_u}=0$. Centering the trace on the discarded source
directions gives an upper bound $a$, while centering it on the target
gives the lower bound $w-\sqrt{\eta w(1-w)}$. Solving the resulting
quadratic gives

$$
 \boxed{
 w\le\frac{2a+\eta+\sqrt{\eta^2+4\eta a(1-a)}}{2(1+\eta)}
   \le a+\sqrt{\eta a}+\eta .} \tag{19.B11}
$$

In particular, zero source loss gives $w\le\eta/(1+\eta)$, of variance
order rather than square-root order. This endpoint is sharp for an
operator scalar on its support and zero off it. The square-root
all-subspace concentration obstruction is therefore not an obstruction
to this original span estimate. The filtration by arithmetic slopes
selects the retained source spaces and supplies their loss fractions;
the span estimate then controls the fraction of low target slopes.
Integration and the other arithmetic bounds retain their original
hypotheses. No new family endpoint or replacement proof of RH follows
from (19.B11) alone.

The two tasks should be distinguished: explaining the original
loss-to-span-to-slope passage, and finding a stronger algebraic route
that could replace some of its estimates. The open commutator comparison
belongs to the second task.

## 5. A sharper bound in the actual mean-slope interface

Here reuse $R$ for the total source rank **after** the initial ramified
restriction, and $D$ for the full target dimension before the good-row
projection. This is the normalization in the current `FrameLA1` and
`thmF_place` interfaces. Normalize the complex maps by the square roots
of their positive coefficients in `FrameLA1`; this preserves their
images and the retained source spaces. Their input $e$ and $\eta$
already include the initial source restriction. No second charge for
that restriction is made in this section.

Let $0\le e\le1/4$, $\eta\ge0$, and let the actual lost source fraction
be at most $\varepsilon$. The argument of Section 4 is valid also when
$\eta$ is an upper bound for the actual normalized variance. The elementary
inequality

$$
 2\sqrt{\eta w(1-w)}\le w+\eta(1-w)
$$

gives $(1+\eta)w\le2a+\eta$. Since $2\sqrt{\delta(1-\delta)}\le1$
and $t/R\ge1-\sqrt e>0$, it follows directly that

$$
 \boxed{
 w\le\min\left(1,
       \frac{2\varepsilon+\eta+c(e)}{1+\eta}\right),
 \qquad c(e)=\frac{\sqrt e}{1-\sqrt e}\le2\sqrt e .}
 \tag{19.B12}
$$

Thus this paper lemma strengthens the conclusion
$w\le\eta+4\varepsilon+4\sqrt e$ of the actual `FrameLA1`
with the same matrix hypotheses. Keeping the minimum also makes the
upper envelope monotone in a variance upper bound; alternatively one
can apply the displayed elementary inequality directly at that upper
bound. No assertion that $\eta$ is the exact variance is needed.

The source's actual threshold spaces satisfy
$\varepsilon(\tau)=u/(u+\tau)$, with $u>0$, at every $\tau\ge0$.
More precisely their actual lost rank share is at most this number.
Their images lie in the target threshold space at normalized slope
$s-\tau$. The factor two between the source's raw slopes and these
normalized slopes is already canceled by the definition of the
threshold and the dimension identity. The source trace and dimension
checks are documented in SOURCE.md; in particular the complex rank is
the post-restriction rank just specified.

Let $0\le\delta_p<1$ be the good-row loss bound and let $H>0$ satisfy
$s-\mu_{\min,\mathrm{dual}}\le H$, exactly as in `Frame_at`.
Projection to the retained target costs at most $(1-\delta_p)^{-1}$
in normalized corank. Integrating (19.B12) on $[0,H]$, with the
same layer-cake formula for normalized target slopes as the source,
gives the following **candidate-D paper replacement** of that
interface:

$$
 \boxed{
 \mu_{\mathrm{dual}}\ge s-\log|\mathrm{Word}|
 -\frac{2u\log(1+H/u)+(\eta+c(e))H}
        {(1-\delta_p)(1+\eta)} .}
 \tag{19.B13}
$$

The source's sharp slope branch gives the analogous expression without
the $\log|\mathrm{Word}|$ loss. Formula (19.B13) keeps that loss to
match the existing `Frame_at` consumer. For $u=0$ the logarithmic term
is interpreted as zero: the source tail share is zero for every
$\tau>0$, and the single endpoint has no effect on the integral.

The original interface has numerator
$4u\log(1+H/u)+(\eta+4\sqrt e)H$ and denominator
$1-\delta_p$. Formula (19.B13) reduces those constants under the
same finite-dimensional and threshold inputs. It leaves the
polynomial $\eta H$ contribution at its existing order. This is an
improvement of that step, not a new bound for the arithmetic suppliers
or a newly formalized proof. No downstream constant, Lean source,
formal theorem or theorem statement has been changed.

There is a more precise zero-error comparison. If $e=0$, set
$J_0=u\log(1+H/u)$. Applying the quadratic envelope before integration
gives

$$
 (1+\eta)\int_0^H w(\tau)\,d\tau
 \le\eta H+\min\left\{2J_0,\,
 J_0+2\sqrt{\eta u}\left(\sqrt H-
             \sqrt u\arctan\sqrt{H/u}\right)\right\}. \tag{19.B14}
$$

Indeed the upper root in (19.B11) is increasing in its loss argument.
It is bounded both by $(2a+\eta)/(1+\eta)$ and by
$(a+\eta+\sqrt{\eta a(1-a)})/(1+\eta)$.
At $a=u/(u+\tau)$ the mixed integral is
$\int_0^H\sqrt{u\tau}/(u+\tau)\,d\tau
=2\sqrt u(\sqrt H-\sqrt u\arctan\sqrt{H/u})$.
At $\eta=e=0$ the logarithmic coefficient is one. These refinements
do not require the commutator certificate.
