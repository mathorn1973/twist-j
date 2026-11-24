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
removal costs. The native positive-energy estimate for the full remaining
sum is O. These deductions do not supply an independent TWIST-J proof of RH.

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

## 5. Next bounded obligations

1. **Most immediate proof simplification:** port the integrated-chord lemma
   into the actual HN supplier, before the scalar tail weakening. Keep its
   complete hypotheses and compare the exact centered bound on the same
   data. Verify that one downstream H8 consumer accepts the replacement.
2. **Active independent arithmetic problem:** prove the signed whole-window
   estimate for the exact residual R_c of DIRICHLET-READOUT.md, Section 5.
   Its sampling cost and vanishing window deletion error are specified.
   The equivalent residual T_low in PRIME-CANCELLATION.md keeps the
   negative square and the remaining long frequencies. Separate norm
   bounds and the lower-argument recurrence's X^(5/12) allowance do not
   supply the needed cancellation.
3. **Smallest meaningful local bridge:** one specified required place, one
   actual normalized kernel, and one admitted integral generator pair whose
   derivative is proved to equal the source period in its normalization.
   A formal map that loses a tangent direction must account for that loss
   and its denominators explicitly.

These are distinct next obligations. The optional stronger all-subspace
period-concentration target of #2070 remains O; it is not an omitted
premise of the already checked external RH proof.

## 6. Evidence boundary

Three Sol agents developed the separate tasks. Root Astra inspected the
critical arguments and pinned sources; a separate Astra wrote the internal
opposition. No scientific executable, numerical search or Lean build was
run. The package does not claim an external referee or scientific
two-architecture confirmation. The public repository's policy and Canon
checks concern custody and the unchanged authority, not promotion of these
paper arguments. See [PROMO-C-RH-THREE-INTERFACE-SYNTHESIS-N.md](PROMO-C-RH-THREE-INTERFACE-SYNTHESIS-N.md)
for the precise handoff.
