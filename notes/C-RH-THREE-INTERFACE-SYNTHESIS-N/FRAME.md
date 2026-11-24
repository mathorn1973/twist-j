# Common-image and lattice interface

**NON-CANONICAL. No Canon authority. Candidate-D.** Paper deduction for the
same finite-dimensional and arithmetic inputs as the pinned frame interface.
Existing centered-frame work is credited to José Brox and [issue #2065][common],
the affine corank bound to [issue #2070, round 19][round19], and the integrated
source-rank chord to the [earlier Hexagon note][hexagon] and issue #2065. The
contribution here is their comparison on identical inputs and the explicit
boundary at the metric lattice. The proposed actual period replacements
remain **O**.

## 1. One word map and one common target

Rubinstein's version 2, §III.11, (H8), equation (III.330), uses one word map
\(\beta_w\) for (8a) integral inclusion, (8b) the height bound, and (8c) an
estimate on complex ranks. The exposition combines three sections and lists
the identification of their maps as an additional input. This describes the
exposition's route through Proposition M4. The Lean route uses its own lattice
theorem, with explicit data tying the estimates to the same arithmetic maps.
[Rubinstein, §III.11][rubinstein].

| Datum to retain | Use in the argument | Pinned Lean interface |
| --- | --- | --- |
| For every word, the actual \(K\)-linear pairing \(B_k(u)\colon V_u\to R^\vee\) and the specified source and target \(\mathcal O_K\)-lattices | Integral inclusion \(B_k(u)N_u\subseteq C\) in the dual lattice \(C\), with the same pairing at every local place | `RecBridge.oneMap_of_coord`, `WordFacts`, and `DivisionPackageFace.hBk` [coordinate and lattice tie][rec-coord] [height record][rec-word] [package][rec-pack] |
| All the prescribed Hermitian metrics and the \(h_u\) bounds on the same maps | The adjusted slopes of the source and the inclusion of threshold images in the target Harder–Narasimhan step | `StatementFrameF` and `theoremFSharp_of.hMle` [statement][statement] [threshold inclusion][target] |
| One target isometry \(\mathrm{SIso.eHH}\), source identifications for each word, and all the identities `Pu_eq` | Joint Gram blocks use a common target inner product, including cross terms for distinct words | `SIso` and `SConc` [realization][siso] |
| The ramified source restrictions and the fixed good-row projection | `Ball = Bf * Vr` with isometric source columns, followed by a row projection whose good coordinates equal the realization of \(B_k(u)\); the retained target is measured against the full dimension | `FrameReal_at`, `LatGeom`, and `thmF_place` [actual realization and consumer][actual-frame] [place comparison][place] |

Here \(K\) is the number field of the pinned theorem. The post-ramification
complex frame may be weighted by \(\sqrt{\gamma_u}\) because all weights are
positive and this leaves the image of each source subspace unchanged. The
arithmetic pairing used for the lattice inclusion and height is still
\(B_k(u)\). The source rank used below is the post-ramification rank. The
diagonal and second-moment estimates have already paid for that restriction.
The retained target fraction is applied once.

## 2. Frame bound on the actual threshold spaces

Let \(A_u\colon E_u\to F\) be the positively weighted complex maps, with
\(R=\sum_u\dim_{\mathbb C}E_u>0\) and \(D=\dim_{\mathbb C}F>0\). Put
\[
 C_0=\bigoplus_u A_u^*A_u,\qquad S=\sum_u A_uA_u^*,\qquad
 t=\operatorname{tr}C_0=\operatorname{tr}S.
\]
The `FrameLA1` inputs are \(\|C_0-I\|_{\mathrm{HS}}^2\le eR\),
\(0\le e\le 1/4\), and
\(\operatorname{tr}(S^2)\le (1+\eta)t^2/D\), \(\eta\ge0\).
Trace Cauchy–Schwarz gives \(t/R\ge1-\sqrt e>0\).
[Statement and original matrix proof][statement] [proof][frame-la].

Choose any retained spaces \(E'_u\le E_u\). Write \(Q\) for the orthogonal
projection onto their direct sum's complement, with rank \(\delta R\), and
\(X\) for the orthogonal projection onto the complement of
\(Y=\sum_u A_uE'_u\), with rank \(wD\). For the joint column map \(A\),
\(XA=XAQ\), so \(\operatorname{tr}(XS)\le\operatorname{tr}(QA^*A)\).
The latter trace equals \(\operatorname{tr}(QC_0)\) because \(Q\) is block
diagonal.
Center \(Q\) against \(C_0-I\) and \(X\) against \(DS/t-I\). This gives
\[
 w-\sqrt{\eta w(1-w)}
 \le \frac{\operatorname{tr}(XS)}t
 \le \frac{\operatorname{tr}(QC_0)}t
 \le \delta+\frac Rt\sqrt{e\delta(1-\delta)}.
\]
Indeed \(\|Q-\delta I\|_{\mathrm{HS}}^2=R\delta(1-\delta)\) and
\(\|X-wI\|_{\mathrm{HS}}^2=Dw(1-w)\), and the second-moment assumption
is exactly \(\|DS/t-I\|_{\mathrm{HS}}^2\le D\eta\). The inequality
\(2\sqrt{\eta w(1-w)}\le w+\eta(1-w)\) now gives the inherited affine bound
\[
 (1+\eta)w\le 2\delta+\eta+c(e),\qquad
 c(e)=\frac{\sqrt e}{1-\sqrt e}\le2\sqrt e. \tag{1}
\]

This bound applies to the actual source spaces selected by the lattice
threshold. Let \(\alpha\) list the adjusted source slopes, with normalized
rank weights. In the pinned conventions their entries are
\(2\lambda_{uj}+\mathrm{slopeNormalisingConstant}(K)-h_u\).
The hypotheses give \(E\alpha\ge s\) and \(\alpha\le s+u\), \(u\ge0\).
For \(x=s-\tau\), the excluded source fraction is exactly
\(\delta(\tau)=\Pr(\alpha<x)\). The complex dimension after base change
equals the rank over \(K\), and the realification factor \([K:\mathbb Q]\)
cancels in the normalized fraction. The integral image of the retained
source step belongs to the target step by the actual inclusion and height
hypotheses. The argument for this inclusion has no sign condition on
\(\tau\). The counting proof in `hfilt` uses the defining threshold for
every real \(\tau\); the sign restriction in its surrounding helper
`hcor` is needed for the separate tail bound. The original squared-norm
factor is already included in \(\alpha\). [Counting][count] [target step][target].

Let \(D_r\ge (1-\delta_p)D\), where \(0\le\delta_p<1\), be the retained
target dimension. The good-row projection \(P\) has kernel of dimension
\(D-D_r\). Therefore
\[
 D_r-\dim P Y=D_r-\dim Y+\dim(Y\cap\ker P)\le D-\dim Y.
\]
For the normalized target slopes \(\beta\), the resulting exact step-count
comparison is \(\Pr(\beta<x)\le\min(1,w/(1-\delta_p))\).

## 3. The integrated chord and the exact centered bound

**Candidate-D.** Suppose \(\beta\ge s-H\) with \(H>0\), exactly the slope
range input of `Frame_at`. Define \(K_0=uH/(u+H)\). For any \(z\ge-u\),
\[
 \min\{H,z_+\}\le H\frac{z+u}{H+u}.
\]
On \([-u,0]\) the right side is nonnegative. On \([0,H]\) the inequality
is \(uz\le uH\), and beyond \(H\) the right side is at least \(H\).
Insert \(z=s-\alpha\), take the weighted mean, and integrate the finite
step count. This gives
\[
 \int_0^H\delta(\tau)\,d\tau
 = E\min\{H,(s-\alpha)_+\}\le K_0 .
\]
The bound is attained for a weighted list with values \(s-H,s+u\) and
mean \(s\). Apply it directly to (1), before using any pointwise upper
envelope for \(\delta(\tau)\). Since
\(s-E\beta\le E(s-\beta)_+=\int_0^H\Pr(\beta<s-\tau)\,d\tau\), this yields
the allowance
\[
 \boxed{\mathcal B_{\mathrm{chord}}
 =\frac{2uH/(u+H)+(\eta+c(e))H}{(1-\delta_p)(1+\eta)}.} \tag{2}
\]
In the `Frame_at` convention it gives \(\mu_{\mathrm{dual}}\ge
s-\log|\mathrm{Word}|-\mathcal B_{\mathrm{chord}}\). The sharp pinned
`TheoremFSharp` convention omits the word-count term. At \(u=0\) the
integrated source loss is zero. If \(H=0\), the target lower bound alone
gives \(E\beta\ge s\).
[Wrapped consumer][frame-at] [sharp statement][statement].

On the same \(e,\eta,u,H,\delta_p\), round 19's allowance is exactly (2)
with \(uH/(u+H)\) replaced by \(u\log(1+H/u)\). Its logarithmic term has
coefficient two, down from four in the pinned statement. For \(u,H>0\),
(2) is strictly smaller because
\(H/(u+H)<\log(1+H/u)\), by integrating \(1/(1+x)\) from \(0\) to
\(H/u\). Neither comparison invokes the projector commutator gap.

The exact inherited bound of issue #2065 is at least as strong as (2) on
these same inputs. To see the order, retain
\[
 a^2=R\operatorname{tr}(C_0^2)/t^2-1,\quad
 g_a(r)=\min(1,r+a\sqrt{r(1-r)}),\quad
 f_\eta(p)=\frac{2p+\eta+\sqrt{\eta^2+4\eta p(1-p)}}{2(1+\eta)}.
\]
The normalized source trace is at most \(g_a(\delta)\) using the centered
operator \(C_0-(t/R)I\). Inverting the target quadratic gives
\(w\le f_\eta(g_a(\delta))\). Let
\(\Psi=\min(1,f_\eta\circ g_a/(1-\delta_p))\). These are the centered
quantities and monotone concave envelope of [issue #2065][common-proof].
Its all-real comparison integrates the two step functions over
\([s-H,s+u]\). The source integral is at most \(u\), since it equals
\(s+u-E\max(\alpha,s-H)\). Jensen and the lower bound on \(\beta\) give
\(s-E\beta\le\mathcal B_a=(H+u)\Psi(u/(H+u))-u\).

Put \(r_0=u/(H+u)\). Since \(\Psi\le1\),
\(\mathcal B_a\le H\Psi(r_0)\). The elementary inequality behind (1)
also gives \((1+\eta)f_\eta(p)\le2p+\eta\), while
\(2g_a(r_0)\le2r_0+a\). Finally
\(a^2\le e/(1-e)\), since minimizing
\(R^{-1}\|q C_0-I\|_{\mathrm{HS}}^2\) over positive real \(q\) gives
\(a^2/(1+a^2)\) and \(q=1\) is admissible. Thus
\(a\le\sqrt{e/(1-e)}\le c(e)\) and
\[
 \mathcal B_a\le H\Psi(r_0)\le\mathcal B_{\mathrm{chord}}.
\]
The comparison concerns a single set of source and target inputs. A new
Lean implementation of the all-real comparison would need to extract the
signature of the count identity and add finite-step Jensen. The chord arm
can use the same threshold interval already used by `Frame_at`. Neither
changes the arithmetic suppliers or establishes a new scale bound.

## 4. What the exact finite carrier can certify

**Candidate-D.** For a fixed marked joint column matrix \(A\), the exact
complex Gram matrix \(G=A^*A\) is positive semidefinite. Its nullspace is
\(\ker A\) by positivity, so its rank is the image dimension. If two
joint marked column matrices have the same Gram, \(Ax\mapsto A'x\) is a
well-defined isometry of their images. The mixed blocks are essential.
Taking each word alone allows unrelated target rotations which can change
the dimension of a sum. For instance two unit words may lie on one line
or two orthogonal lines with identical individual Grams.

A target cut belongs to this identification. The one-column matrices
\(e_1,e_2\) have the same Gram \([1]\), but projection onto the fixed
\(e_1\) row gives ranks one and zero. An isometry carrying the marked
cut, or the joint Gram of the already cut maps, suffices to transport this
rank calculation. An invertible coordinate change suffices for rank and
needs metric transport to carry a height calculation. Rational rank of
a marked arithmetic matrix survives embedding into \(\mathbb C\) by its
minors. Local module inclusions require the actual coordinate matrix and
its local divisibility. Reduction does not preserve the positivity
argument. The column \((1,2)^\top\) has rank one modulo five even though
its Gram \([5]\) reduces to zero. An equal rational Gram does not certify
integrality either: \(I_2\) and \(\frac15\left(\begin{smallmatrix}3&-4\\4&3\end{smallmatrix}\right)\)
both have Gram \(I_2\), and the latter sends \(e_1\) outside \(\mathbb Z^2\).

The public QDD bridge supplies a precise example of the extra marked
data. The signed isometry \(T\) sends the marked QDD lattice onto the
metric dual \(L^\#\) of the circular \(A_4\) lattice \(L\). Its five
projectors are individually metric self-adjoint idempotents, are pairwise
nonorthogonal with off-diagonal product trace \(1/16\), and are fractional
on \(L\). Their sum is \((5/4)I\), so their unit columns give an exact tight
frame in that fixed rank-four carrier. The choices \(T\) and \(-T\) have
the same Gram, indices and
conjugated projectors. They send the marked \(u_0=1\) to \(w_0\) and
\(-w_0\), which have distinct images in \(L^\#/L\cong\mathbb F_5\),
because \(T((\zeta_5-1)\mathbb Z[\zeta_5])=L\) and \(1\) has nonzero residue.
An output on a marked quotient thus needs the actual signed map or an
explicit compatibility identity for that output. This is a boundary for
using the specified carrier as a proof model. A replacement for the rank
supplier of (H8) must realize all the same word maps in one target, carry
both cuts, and prove the threshold rank bound at the scales quantified by
the source. An identification of this kind remains **O**.
[Public Canon v117, named QDD bridge and intertwiner][qdd].

## 5. A sharp obstruction to an unqualified slope-range transfer

**Candidate-D.** Ideal frame estimates, the same rational pairing and
integral image, equal target degree, and identical inclusion elementary
divisors still allow \(s-\mu_{\min}\) to grow with dimension.
Work first over \(\mathbb Q\) with Euclidean metrics, with ordinary slopes
given by minus log covolume per rank. For \(d\ge2\), \(N=2^d\) and
\(B=I\) on \(\mathbb Q^d\), choose the common source lattice
\[
 M=\langle e_1,\ldots,e_{d-1},Ne_d\rangle_{\mathbb Z},
\]
and compare targets
\[
 L=\mathbb Z^d,\qquad
 L'=\langle N^{-1}e_1,e_2,\ldots,e_{d-1},Ne_d\rangle_{\mathbb Z}.
\]
Both targets contain the same embedded image \(B(M)=M\). Both have
covolume one and quotient by \(M\) cyclic of order \(N\), so they have
the same local inclusion elementary divisors. The coordinate Gram of
\(B\) is \(I_d\) in both cases, and the Gram of the marked lattice
generators of its image is \(\operatorname{diag}(1,\ldots,1,N^2)\) in both.
There is one word, height zero in the common Euclidean metric, no cut,
and \(e=\eta=0\) on the ambient real spaces or their complexifications.

For a diagonal Euclidean lattice with orthogonal basis lengths \(b_i\),
each rank-\(k\) sublattice has covolume at least the product of the \(k\)
shortest basis lengths. In exterior coordinates a nonzero rank-\(k\)
wedge has at least one nonzero integer coefficient in the original
lattice basis, and every basis wedge has length at least that product.
The shortest coordinate sublattice attains it. Thus its HN slopes are
the sorted \(-\log b_i\). Here the source slopes are
\(0,\ldots,0,-\log N\), giving \(s=-\log 2\) and \(u=\log 2\),
uniformly in \(d\). The target minimum is \(0\) for \(L\) and
\(-\log N\) for \(L'\). Hence \(s-\mu_{\min}\) equals \(-\log 2\) and
\((d-1)\log 2\), respectively. The example also works over
\(\mathbb Q(i)\) with \(\mathbb Z[i]\)-lattices and the same coordinate
generators, using realification of the standard Hermitian metric. The
ordinary slopes occur twice and the squared-norm convention doubles
the displayed gaps. Common field normalizations cancel in the gaps.

There is a dimension-dependent bound when the same integral images
jointly span the target and satisfy the slope-step inclusion. A list of
\(R_{\mathrm{sl}}\) adjusted source slopes with mean at least \(s\) and
maximum at most \(s+u\) has minimum at least
\(s-(R_{\mathrm{sl}}-1)u\) by summing. Apply the step inclusion at
the minimum adjusted slope, where all source spaces are retained. Its
target step has full rank, giving the same lower bound for the target
minimum. The Euclidean example attains that endpoint for
\(R_{\mathrm{sl}}=d\). The embedded target lattice and the arithmetic
estimate of its range, supplied separately as (H9) in Rubinstein, are
therefore substantive inputs to the frame-to-slope application.
[Rubinstein, (H9)][rubinstein].

The stronger uniform double-commutator estimate for the actual periods
remains **O**. Round 17's control for projections in its common algebra
does not control every projection in the multiplicity spaces where the
maximizer may lie. That issue concerns all-subspace concentration. The
allowance in (2) concerns total lost rank at arithmetic slope thresholds.
[Round 17][round17] [round 19][round19]. No scientific computation, Lean
build, external independent validation or public promotion was performed
for this note.

[common]: https://github.com/mathorn1973/twist-j/issues/2065
[common-proof]: https://github.com/mathorn1973/twist-j/blob/18e325c068c09d98ddf8383724a8c1c9f15dc021/notes/C-RH-COMMON-GRAM-N/PROOF.md
[round17]: https://github.com/mathorn1973/twist-j/blob/948ddd240340e14d6bbac96baade3039e8b9f263/notes/C-RH-SEMISTABLE-FRAME-N/round17/REPORT.md
[round19]: https://github.com/mathorn1973/twist-j/blob/948ddd240340e14d6bbac96baade3039e8b9f263/notes/C-RH-SEMISTABLE-FRAME-N/round19/BRIDGE.md
[hexagon]: https://hexagonmath.org/2611.00828v1
[rubinstein]: https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=206
[rec-coord]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/Divisibility/RecBridge.lean#L29-L50
[rec-word]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/Divisibility/RecBridge.lean#L128-L153
[rec-pack]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/Divisibility/RecBridge.lean#L601-L636
[statement]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/StatementFrameF.lean#L11-L99
[frame-la]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L77
[place]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/TheoremFSharp.lean#L35-L156
[count]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/TheoremFSharp.lean#L216-L277
[target]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/TheoremFSharp.lean#L279-L382
[siso]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ParametersTermRelations.lean#L286-L323
[actual-frame]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L519-L599
[frame-at]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean#L188-L193
[qdd]: https://github.com/mathorn1973/twist-j/blob/6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed/canon/CANON.md#j-circular-qdd-signed-affine-projector-intertwiner-t
