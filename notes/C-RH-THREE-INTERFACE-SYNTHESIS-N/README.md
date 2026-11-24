# Three interfaces for RH synthesis

**NON-CANONICAL. Authority none. All new paper deductions are candidate-D.**
Public basis: Public Canon v117 at
`6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`.
Claim: [#2091](https://github.com/mathorn1973/twist-j/issues/2091).

The three-task comparison produced a usable slope-bound synthesis, exact
local transfer limits and a stronger obstruction to norm-only augmentation
estimates. Its signed-pairing continuation now supplies at most N^2 ordinary
Dirichlet samples, exact optimal reconstruction cost and a sharp threshold
for discarding smooth direction supports. The whole-window continuation
proves vanishing deletion energy, finite global energy through direction
support N^(1/3), and a balanced bilinear reduction with quantified Fourier
removal costs. Its low-frequency continuation now proves coupled affine
cancellation, actual signed numerator bounds, double cancellation on a
smooth central band and inverse-logarithmic comparison of complete
narrowed carriers. The complete-energy continuation adds an inverse-log
additive energy projection onto weighted block means, exact two-large-factor
and asymmetric-rectangle transfers, and scoped obstructions to closing
the resulting recursion from positive levels and ordinary short increments
alone. The native positive-energy estimate for the full remaining sum is O.
These deductions do not supply an independent TWIST-J proof of RH.

## 1. What each side actually supplies

| Subject | External proof and compression project | Current TWIST-J apparatus | Result of this comparison |
|---|---|---|---|
| Full RH | The Lean FRO/Mathlib statement reports independent verification of the statement and exported proof. The compression dashboard is a separate project. | The public augmentation owner remains O for a direct derivation from the refined shell. | Do not confuse an independent new route with importing the already established external conclusion. |
| Local arithmetic | Specified CM models, integral normalized kernels, formal logarithms and a derivative-to-period pairing. | Exact O=Z[zeta_5] arithmetic and a specified CM5 Jacobian, with registered T statements at those scopes. | Residue Frobenius transfers exactly to named torsion, but iteration does not deepen the defect. A direct tangent-injective formal-group identification fails at the real-field inert primes. |
| Combined images | One arithmetic pairing with its lattices, height metrics, common complex realization and cuts. | Exact Gram and lattice carriers; existing centered-frame and actual-period candidate notes. | On matched supplier data, the integrated source-loss chord is stronger than the logarithmic weakening. The exact earlier centered bound is stronger still. |
| Signed arithmetic | A smoothed prime-power observable and arithmetic bounds throughout arbitrarily late complete windows. | Integral rapidity lift, neutral coefficient, exact augmentation to Mobius, moving support decompositions. | The two current tails have different kernels. The actual coefficient span has evaluation norm of order sqrt(N), and its top band defeats every positive diagonal Cauchy bound even after aggregation. |
| Reconstruction | Matched maps and normalizations are part of the proof, not inferred from dimension alone. | Independent rapidity coordinates permit finite product-character measurements and the ordinary Dirichlet samples in Section 3. | A dyadic modulus and cubic twist give at most N^2 samples, all different from augmentation, with minimum squared readout norm D(N). The signed window estimate remains open. |

The external statement and current sources are documented in
[SOURCES.md](SOURCES.md). Dashboard compression ratios measure specified
editable proof bodies and their imports; they do not measure the amount of
new mathematics supplied by J.

## 2. The three completed paper tasks

### Local transfer

[LOCAL.md](LOCAL.md) proves, for every p != 5, r>=1 and P above p,

\[
v_P(J^{p^r}-\sigma_p^rJ)=v_P(J^p-\sigma_pJ).
\]

For the good odd-prime CM5 model it identifies the equalizer on p-power
torsion from that exact ideal. At p=3 the depth is one for every r.
The Cartier calculation distinguishes this fixed formal group from the
height-two-logarithm model used by the external local estimate. An explicit
series satisfies the coefficient-field, torus and parity assumptions but
fails the additional kernel-integrality condition by an arbitrary power.
These are precise limits of proposed substitutions, not counterexamples to
the external proof.

### A shorter integrated slope allowance

[FRAME.md](FRAME.md) keeps the actual adjusted source slopes, whose weighted
mean is at least s and whose maximum is at most s+u. If H bounds the target
slope deficit, the integrated lost source share is at most uH/(u+H).
Combining this with the existing centered affine frame inequality gives

\[
\mathcal B_{\rm chord}
=\frac{2uH/(u+H)+(\eta+\sqrt e/(1-\sqrt e))H}
       {(1-\delta_p)(1+\eta)}.
\]

The original map, all height metrics, the source restriction and the target
cut are retained. The wrapped conclusion is
mu_dual >= s-log|Word|-B_chord. Under identical inputs the exact allowance
from #2065 is no larger than B_chord, which is strictly smaller than the
round19 logarithmic allowance when u,H>0. This is a comparison and portable
corollary of attributed existing ingredients, not a claim of priority.

The chord requires the supplier's slope list. It cannot be recovered from
only the already weakened scalar tail u/(u+tau). The note also gives a
sharp dimension-dependent example showing why target slope range H9 is
separate from exact Gram, rank, degree and inclusion-index data.

### An anchored signed-augmentation contract

[MOBIUS.md](MOBIUS.md) identifies the actual symmetric span with the basis
E_d=product_(p|d)(X_p+X_p^(-1)), for squarefree split d<=N. Its evaluation
vector has squared norm

\[
D(N)=\sum_{\substack{d\le N\\d\ \rm squarefree,\ split}}
2^{\omega(d)}=\kappa_5N+O_\epsilon(N^{1/2+\epsilon}),\quad\kappa_5>0.
\]

The coefficients on N/2<d<=N retain their exact signs and have absolute
mass D(N)-D(N/2). Every positive diagonal weighted Cauchy estimate is at
least this large, even after aggregation and even for data-dependent
weights. The note gives a short elementary proof of the neutral
O(N^(1/3)) bound and the small-orientation O(sqrt(N)) complement, and an
exact comparison with #2087's distinct N^(2/3) cutoff.

For a nonempty set of r split primes, fourth-root product characters with
the trivial sample removed give A* A=I-kk*/4^r. Their minimal reconstruction
vector z satisfies A*z=k and ||z||^2=D(N)/(1-D(N)/4^r). This fixes the
target, norm and zero reconstruction error. Estimating the signed scalar
pairing on complete windows is still necessary.

[REVIEW.md](REVIEW.md) extends the obstruction: if a positive form G is
between alpha W and beta W for some positive diagonal W, then its direct
norm-product allowance is at least sqrt(alpha/beta)[D(N)-D(N/2)]. A
sqrt(N)-strength estimate by that sole method requires the diagonal
comparison condition number to grow nearly linearly. Poor conditioning
is necessary here, not sufficient for success.

## 3. Concrete signed-pairing continuation

**Candidate-D.** [DIRICHLET-READOUT.md](DIRICHLET-READOUT.md) fixes the least
power of two m>N^2 and a cubic character theta modulo seven with
theta(11)=zeta_3. Every sample psi=theta chi, for chi modulo m, differs from
augmentation on E_11. Distinct oriented monomials give distinct rational
residues modulo m. Character orthogonality therefore gives an exact
isometry and the anchored readout

\[
 M(N)=\frac1h\sum_{\chi\bmod m}B_N(\theta\chi)
              \overline{K_N(\theta\chi)},\qquad
 h=\varphi(m)\le N^2,\qquad
 \frac1h\sum_{\chi\bmod m}|K_N(\theta\chi)|^2=D(N).
\]

One family works throughout a full window by choosing m from its upper
cutoff X. The same note expresses the square of each sampled Dirichlet
series as a ratio of four ordinary Dirichlet L functions and L(s,chi_5)^2,
times an Euler unit whose absolute coefficient norms and inverse norms
are uniform in the sample modulus for each real part greater than 1/2.
This statement continues the square and proves no zero-free region.

**Candidate-D.** [LOCAL-AVERAGES.md](LOCAL-AVERAGES.md) and the sharp converse
in [ROUND2-REVIEW.md](ROUND2-REVIEW.md) prove

\[
 \sum_{\substack{d\le N,\ d\in\mathcal D\\P^+(d)\le c(\log N)^2}}
       |\gamma_d(N)|=O_c(\sqrt N)
 \quad\Longleftrightarrow\quad 0<c<\frac1{4e^2}
 \qquad(c>0\text{ fixed}).
\]

At the endpoint the ratio is unbounded along an unbounded integer
sequence, using the actual top-band coefficients. This concerns absolute
support removal; the signed whole-window estimate can still benefit from
cancellation between those supports. A concrete allowed choice is c=1/36.

For that choice, retain d>N^(1/4) with P^+(d)>(log N)^2/36. The sum of
their E_d is an exact readout kernel K_c,N on the same raw samples.
Its minimum squared norm is the explicitly known retained mass D_c(N),
with D(N)-D_c(N)=O(sqrt(N)). Its scalar output R_c satisfies
M(N)-R_c(N)=O(sqrt(N)) on every sufficiently late integer.
Thus the original arbitrarily late whole-window criterion is equivalent
to the same criterion for this fully specified residual. That criterion
remains **O**.

The other continuation notes expose the signs and the limitations of norm
changes. [SIGNED-SAMPLES.md](SIGNED-SAMPLES.md) groups equal-cofactor
large-prime samples without discarding their arithmetic cross terms.
[LOCAL-AVERAGES.md](LOCAL-AVERAGES.md) identifies the original orientation
projection with the previously derived positive N/(log N)^2 prime tail
of #2087/#2089 and derives the compensating negative row contribution.
The signs must be combined before taking a positive part.
[MIXING.md](MIXING.md) proves the actual coefficient energy is of order N
and calculates the exact effect of a positive form with prescribed
condition number. A target-anchored norm can move the unknown overlap
into the measured component, without estimating it.

The prospective continuation was recorded in the same owner issue before
paper authoring; see [PAIRING-SCOPE.md](PAIRING-SCOPE.md). The sampling
construction and sharp endpoint argument include contributions from the
Astra reviewer, checked separately within the same session. They are joint
internal work, with no external-referee or scientific-execution claim.

## 4. Positive energy on complete late windows

**Candidate-D; native final target O.** The continuation preserves the
original R=R_(1/36), including its N^(1/4) direction cutoff. Put

\[
 Q_F(Y)=\sum_{Y\le N<Y^{3/2}}\frac{F(N)_+^2}{N(N+1)},
 \qquad
 \|F\|_Y^2=\sum_{Y\le N<Y^{3/2}}\frac{|F(N)|^2}{N(N+1)}.
\]

The target quantifiers are: for every integer r>=1 and every Y0, there
is an integer Y>=max(11,Y0) with Q_R(Y)^r<=Y. All deletions and comparisons
below hold on each sufficiently late complete window, not selected rows.

[WINDOW-BOUND.md](WINDOW-BOUND.md) proves, from unconditional fixed-modulus
Dirichlet mean-square and reciprocal-zeta estimates, that

\[
 \int_1^\infty |C_0(u)|^2u^{-3/2}\,du<\infty.
\]

Using the actual sector formula and retaining all square-power corrections,
this gives the quantitative same-window comparison

\[
 |\sqrt{Q_R(Y)}-\sqrt{Q_M(Y)}|^2
 \le \|M-R\|_Y^2
 \ll Y^{-1/8}+
 \exp\left(-\frac{(\log3-1)\log Y}{\log\log Y}\right).       \tag{1}
\]

The separate Astra derivation in [ROUND3-REVIEW.md](ROUND3-REVIEW.md),
Section 2, strengthens the critical support estimate to

\[
 \sum_{N\ge1}\frac{1}{N(N+1)}
 \left(\sum_{d\le N^{1/3}}|\gamma_d(N)|\right)^2<\infty.    \tag{2}
\]

The smooth absolute block has finite global energy as well. Therefore a
separate residual R^(1/3), with the stronger direction cutoff N^(1/3),
differs from M by a globally square-summable error in this weight. Its
positive-energy square root differs by o(1) on every late window. This
does not redefine the original R. No decay rate is asserted for the
critical tail in (2).

[PRIME-CANCELLATION.md](PRIME-CANCELLATION.md) bounds the large-prime square
corrections by O(sqrt(N)/log(N)), with finite global error energy. On each
dyadic slab X<=N<2X it also constructs finitely supported integers c_a,
equal to mu(a) through ceil(sqrt(3X)), with |c_a|<=1 and sum c_a=0.
With b=c*c, h_X=sum c_a/a and the centered midpoint sawtooth psi_d, the
complete same-argument identity is

\[
 M(N)=\sum_d b_d\psi_d(N)-(N+1/2)h_X^2.                    \tag{3}
\]

The square term is nonpositive. Removing raw denominators d<=X^(2/3),
averaging over a controlled short interval, removing high frequencies,
and then removing reduced denominators
q<=X^(2/3)/(log X)^2 leaves a precisely defined real T_low with

\[
 |\sqrt{Q_R(Y)}-\sqrt{Q_{T_{\rm low}}(Y)}|
 \ll (\log Y)^2.                                         \tag{4}
\]

The affine negative term is averaged and retained. ROUND3-REVIEW.md also
allows removal of all reduced q<=X^(2/3), at the larger whole-window norm
cost O((log Y)^4). These changes preserve the target with all its
quantifiers. The exponent 2/3 here concerns the bilinear denominator,
not the direction-support cutoff in (2). The earlier periodic covariance
and generic cutoff method of #2087/#2089 retain attribution.

[CHARACTER-WINDOW.md](CHARACTER-WINDOW.md) fixes one reader for the whole
window and proves an exact finite Mellin energy formula with both endpoint
terms. Its distant coefficient aliases begin beyond the window. The
high-height integral costs O((log Y)^4). The separate character norms,
including fourth-moment control with aliases, still give no cancellation
of the signed pairing; their Holder products are at least N^(1-epsilon).
Many of the actual sample conductors grow like Y^3. ROUND3-REVIEW.md
strengthens the frozen-reader error to the vanishing bound (1).

The complete positive energy currently inherits the classical bound

\[
 Q_R(Y)\le (C^2+o(1))Y^{3/2}
 \exp\left(-2c\,\Phi(Y^{3/2})\right),
 \quad \Phi(x)=(\log x)^{3/5}(\log\log x)^{-1/5}.
\]

Its scale is Y^(3/2-o(1)), which does not prove the target. Explicitly
importing RH instead gives Q_R(Y)<<_epsilon Y^(3 epsilon) and hence the
target on every sufficiently late window. That is a consequence of an
external premise. The native proof still needs signed control of the
surviving long, low-frequency sum together with its negative square, or
the corresponding mixed character moment. See [WINDOW-SCOPE.md](WINDOW-SCOPE.md)
for the prospective scope and internal review boundary.

## 5. Estimates on the actual long low-frequency sum

**Candidate-D; full native target O.** The next continuation keeps the
original T_low fixed and names its compared carriers separately.
The prospective scope is recorded in [LOW-ENERGY-SCOPE.md](LOW-ENERGY-SCOPE.md).
The four complete new papers supply the following deductions.

### A coupled sector cancels with its own affine terms

[BILINEAR-LOW.md](BILINEAR-LOW.md) removes the padding explicitly.
With u_a=mu(a) for a<=A, b^u=u*u, m=M(A) and h_u=sum u_a/a, it gives

\[
 T_{\rm low}
 =P_X(b^u)-L_Xh_u^2+\frac{m^2}{2}+2m-E_X,
 \qquad L_X=N+\tfrac12+J(H-1)/2.
\]

Here P_X is exactly the original smoothed spectral projection, and the
error has weighted slab norm O((1+log X)^(3/2)). The positive term m^2/2
must remain. The nonpositive square of the balanced formula alone
does not measure the benefit of balancing.

Put B_X=2X+J(H-1). Every raw denominator d>=B_X has zero floor throughout
every translated argument. For z supported on those denominators,

\[
 P_X(z)-L_X\sum_d z_d/d+\tfrac12\sum_d z_d=-E_X(z).
\]

Thus their complete coupled contribution has O((log Y)^2) norm cost
on the original whole window. A genuine primitive prime-pair family
inside this sector has isolated positive and negative weighted energies
of order at least X/log^4(X) on separate slab subintervals. Its own
allocated affine terms cancel those contributions. This is no lower
bound for the full positive energy.

The remaining unpadded object is

\[
 W_X^{<}=P_X(b^u\mathbf1_{d<B_X})-L_XA_X+C_X/2,\quad
 A_X=\sum_{d<B_X}b_d^u/d,\quad C_X=\sum_{d<B_X}b_d^u.
\]

Both affine coefficients are signed. The note factors every remaining
divisor-multiple coefficient into finite Mobius sums with an explicit
product cutoff, and writes the exact nonnegative-test supremum for
the remaining positive norm.

### Actual numerator cancellation and crossing pairs

[LOW-FREQUENCY-PAIRS.md](LOW-FREQUENCY-PAIRS.md) adapts the attributed
neighboring numerator argument to the present coefficients. At primitive
theta=a/q its cofactor is independent of a. Summing signed numerators
before taking conductor absolute values gives an amplitude bound
O_epsilon(X^(1+epsilon)/U) for a height interval
lambda=X|a|/q>=U.

For the specified compact time taper, the actual ordered unequal-denominator near pairs
whose larger height reaches U, including pairs crossing that threshold,
have signed sum

\[
 O_\epsilon\!\left(X^\epsilon(X^3/U^2+X^2)\right),
 \qquad U\ge128\lceil3\log_2 X\rceil.
\]

The proof retains the exact divisor-multiple coefficients, primitive
conditions and all time translates. At U=sqrt(X)/log^2(X), the separate
amplitude bound above permits a subpower whole-window one-sided norm
comparison; that comparison is not inferred from the crossing-pair bound
alone. A separate box estimate removes
dyadic numerator boxes B>=max(1,R^3/X^2) at denominator scale q~R.
No bound on their individual mixed energy with the retained boxes is
inferred from that norm comparison.

The review checks the same estimates after the raw mask d<B_X. They
therefore give a joint carrier
\(F^{<}=G_X^{*,<}-L_X A_X+C_X/2\) with
|sqrt(Q_(F^<))-sqrt(Q_R)|<<_epsilon Y^epsilon on every late whole
window. All-epsilon exponent slack preserves the original quantifiers.
The central-band theorem below is not automatically transported through
this sharp raw-denominator mask.

### A direct energy bound on a smooth central band

The Astra derivation in [LOW-ENERGY-REVIEW.md](LOW-ENERGY-REVIEW.md)
keeps the original balanced carrier. For a fixed smooth even cutoff
w, equal to one on [-1,1] and supported in [-2,2], let L_(X,K)
multiply its oscillatory frequencies by w(X theta/K).
For 1<=K<=X^(1/10),

\[
 \sum_{X\le N<2X}\frac{|L_{X,K}(N)|^2}{N(N+1)}
 \ll_w X(1+K)^4\log^6(2X)
       \exp[-4c\Phi(X/(8AK))].                              \tag{5}
\]

The proof unfolds the actual b=c*c before grouping equal frequencies
and applies partial summation in both integer factors. The two
cancellations use the stated unconditional classical Mertens bound.
Exact balancing removes the upper boundary faces; the smooth cutoff
removes the lower ones. The theorem includes growing
K=exp(kappa Phi(sqrt(X))) for every fixed 0<kappa<c.
It also applies to each fixed logarithmically narrowed balanced carrier
below. Even at K=1 the displayed upper bound is X^(1-o(1)), so this
estimate cannot be treated as a target-scale deletion of the central band.

### Logarithmic narrowing has a vanishing price for the entire carrier

[ONE-SIDED-LOW.md](ONE-SIDED-LOW.md) defines T_h by the complete frozen
formula with H replaced by h in the average, cutoff and affine shift.
For each fixed B>=1 put H_B=ceil(sqrt(X)(log X)^B). Then, for every
fixed K>0,

\[
 \left\|T_{H_B}-T_{\rm low}\right\|_Y
 \ll_{B,K}(\log Y)^{-K}.                                   \tag{6}
\]

This compares the full signed expressions including their affine terms.
It uses the published maximal short-Mobius theorem at its exact uniformity,
with unit-cell integration to include all integer starts. The multiplier
difference on the shared discarded modes supplies an additional power
gain; the discarded high frequencies use the uniform bound 2/5 for one
average. Both incomplete end slabs are included. Each B and K is fixed;
no simultaneous uniform assertion for growing B is made.

Equation (6) does not bound the size of either carrier. The original
full positive-energy estimate from Section 4 is still the available
unconditional full bound. Proving the target for T_(H_B), or for the
joint signed carrier \(F^{<}\) with both affine terms retained, remains O.

## 6. The complete positive energy and the remaining level estimate

**Candidate-D; native closure O.** The user asked to find the full energy
at the required scale. The three author lanes and separate opposition did
not establish that bound. They obtained the following complete-expression
transfers and tests of specific proposed closure steps.

### An additive error for the actual positive energy

On every complete \(I(Y)\), partition each intersecting dyadic slab into
integer blocks of length \(\lfloor\sqrt X(\log X)^B\rfloor\), with fixed
\(B\ge1\), keeping every partial endpoint block. With
\(w_N=1/[N(N+1)]\), let \(m_I(F)\) be the weighted mean on a block and
\(S_F(Y)=\sum_I w(I)m_I(F)_+^2\). Then, for every fixed \(K>0\),
\[
 0\le Q_F(Y)-S_F(Y)\ll_{B,K}(\log Y)^{-K},
 \qquad F=M\ \hbox{or}\ F=R.
\]
This is an additive error in the energy itself, independent of its size.
The exact inequality is
\[
 0\le Q_F-S_F\le\|(1-P)F\|^2,
\]
where \(P\) is weighted block projection. Convexity and the Lipschitz
derivative of \(x_+^2\) give this inequality after the linear terms cancel
on every block. The published short-prefix theorem controls the variance
using every forward and backward integer start; no sparse-start
exceptional-set inference is made. The small norm of \(M-R\) transfers
the variance estimate to the actual residual.

For blocks \([a,b]\), the retained mean is explicitly
\[
 w(I)m_I(M)=w(I)M(a-1)+
       \sum_{a\le n\le b}\mu(n)\left(\frac1n-\frac1{b+1}\right).
\]
Thus the large signed boundary level remains. Normalize by
\(d_I=m_I(M)/\sqrt a\), \(q_I=a w(I)\), and let
\(D_Y(t)=\sum_{d_I>t}q_I\). With \(V(Y)=\sup_{t\ge1}t^2D_Y(t)\),
\[
 V(Y)\le S_M(Y)\ll(1+V(Y))\log Y.
\]
The required statement is therefore equivalent to a subpower upper-tail
bound, simultaneously at all \(t\ge1\) on arbitrarily late complete
windows. It is not a bound holding on separately chosen windows for
different heights. [Proof and exact positive dual](FULL-LEVELS.md).

### Two large factors with the negative square retained

For \(T=\lfloor X^{1/4}\rfloor\), set
\[
 C_T(n)=\sum_{\substack{a,b>T\\ab\le n}}\mu(a)\mu(b)
                  \lfloor n/(ab)\rfloor,\qquad
 h_T=\sum_{a\le T}\mu(a)/a.
\]
The exact convolution identity
\(\mu=2u_T-u_T*u_T*\mathbf1+(\mu-u_T)*(\mu-u_T)*\mathbf1\)
eliminates both mixed rectangles. The remaining short rectangle has
weighted slab norm \(O(X^{-1/4}\log^{3/2}X)\); its entire constant
boundary costs \(O(1)\) in that norm. Consequently
\[
 Z_X(N)=U_H^J C_T(N)-L_X(N)h_T^2.
\]
Here \(L_X=N+1/2+J(H-1)/2\), with no square already included in \(L_X\).
The formula preserves the negative slope because the short rectangle
is complete. At a cutoff as large as \(X^{1/3}\), the intercept must
be retained under this proof's estimates.

For the fourth-root choice there is a stronger direct comparison.
The classical Mertens estimate makes the intercept's norm smaller
than every inverse logarithmic power. The maximal short-sum theorem
does the same for \(U_H^JM-M\), and the small rectangle has the power
saving just stated. Hence for every fixed \(K>0\),
\[
 \|Z-R\|_{I(Y)}\ll_K(\log Y)^{-K}.
\]
The positive square-root energies satisfy the same comparison.
Each of \(Z,M,R\) also has its own additive block-energy approximation;
an additive difference between different carriers' energies does not
follow from the small norm difference alone.

Hyperbola symmetry further gives
\[
 C_T(n)=
 2\sum_j D_T(n,j)\bigl(M(\lfloor n/j\rfloor)-M(T)\bigr)
 -\sum_{k\le n/(T+1)^2}
       \bigl(M(\lfloor\sqrt{n/k}\rfloor)-M(T)\bigr)^2,
\]
where \(D_T(n,j)=\sum_{a\mid j,\ T<a\le n/j}\mu(a)\).
For primes \(T<p\le\sqrt n\), the genuine coefficient is \(-1\).
The additional negative squares therefore do not justify replacing
the larger prefix arguments by their positive parts.
[Proof and quantified operator test](FULL-COUPLED-ENERGY.md).

### A larger compensated row cut, with its accumulation cost

Let \(B_X=2X+J(H-1)\) and keep the original \(A=\lceil\sqrt{3X}\rceil\).
An entire row satisfies
\[
 \sum_{b\le A}\mu(b)\lfloor n/(ab)\rfloor
 =1-\sum_{A<b\le n/a}\mu(b)
\]
in the stated boundary range. This allows replacing the unpadded
square by the actual asymmetric rectangle
\[
 a\le C=\left\lfloor B_X/A-X^{3/10}\right\rfloor,\qquad b\le A,
\]
with its own two affine coefficients, at \(O((1+\log Y)^2)\)
whole-window norm cost. Its largest raw product is below \(B_X\)
by order \(X^{4/5}\).

The cumulative norm allowance for a deeper row cut of depth \(U\) is
\(O(A^{1/2}(U+1)^{5/2}/X)\), apart from the known projection cost.
Breaking the cut into bands gives the same order; its time supports
are nested. A fixed fractional depth \(U\asymp A\) leaves an
\(X^{1/2}\) norm allowance. This is a loss in the proved upper
estimate, not a lower bound on the actual cancellation.
[Proof and exact remaining rectangle identity](LOWEST-MODES.md).

### What the unsuccessful closure tests exclude

The level paper supplies one integer partial-sum model with recurring
sign changes, the classical envelope and all-start ordinary short-prefix
savings, yet positive energy \(Y^{3/2-o(1)}\) on every late window.
The corner paper keeps the genuine divisor coefficients but varies the
prefix state: nonpositive separated pulses can produce positive corner
energy at least \(X^{1/4-o(1)}\), surviving smoothing and block means.
The slowed pulses obey the ordinary short-prefix bounds as well.
These tests do not impose coherence with the actual Mobius increments,
and do not impose the source theorem's twisted-sum conclusions.
The latter lower bound is before subtraction of the actual arithmetic
drift; it is not a lower bound for the complete \(Z_X\) or \(R\).

The opposition also displays a fixed floor kernel of both signs on
balanced coefficient vectors under the same nonnegative dual test.
Thus coefficient balance and positive tests do not supply the missing
sign. The actual upper-tail estimate or the fully coupled corner
estimate remains O. [Internal opposition](FULL-ENERGY-REVIEW.md).

## 7. Next bounded obligations

1. **Most immediate proof simplification:** port the integrated-chord lemma
   into the actual HN supplier, before the scalar tail weakening. Keep its
   complete hypotheses and compare the exact centered bound on the same
   data. Verify that one downstream H8 consumer accepts the replacement.
2. **Active independent arithmetic problem:** prove the signed whole-window
   estimate for the exact residual R_c of DIRICHLET-READOUT.md, Section 5.
   Its sampling cost and vanishing window deletion error are specified.
   The equivalent logarithmically narrowed balanced carrier keeps the
   negative square. The separately proved joint unpadded carrier keeps
   its two signed affine terms and the exact hyperbolic coefficient sums.
   Bound one of their complete positive energies, equivalently the
   simultaneous upper-tail mass of the actual weighted block means in
   FULL-LEVELS.md. The exact corner recursion must keep the relationship
   between its divisor coefficients and the same Mobius prefix state.
   The central-band estimate, short-increment inputs and controlled
   changes between carriers do not yet supply this full level bound.
3. **Smallest meaningful local bridge:** one specified required place, one
   actual normalized kernel, and one admitted integral generator pair whose
   derivative is proved to equal the source period in its normalization.
   A formal map that loses a tangent direction must account for that loss
   and its denominators explicitly.

These are distinct next obligations. The optional stronger all-subspace
period-concentration target of #2070 remains O; it is not an omitted
premise of the already checked external RH proof.

## 8. Evidence boundary

Three Sol agents developed the separate tasks. Root Astra inspected the
critical arguments and pinned sources; a separate Astra wrote the internal
opposition. No scientific executable, numerical search or Lean build was
run. The package does not claim an external referee or scientific
two-architecture confirmation. The public repository's policy and Canon
checks concern custody and the unchanged authority, not promotion of these
paper arguments. See [PROMO-C-RH-THREE-INTERFACE-SYNTHESIS-N.md](PROMO-C-RH-THREE-INTERFACE-SYNTHESIS-N.md)
for the precise handoff.
