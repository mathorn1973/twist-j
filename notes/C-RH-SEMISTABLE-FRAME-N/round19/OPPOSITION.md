# Round 19 opposition

**NON-CANONICAL. No authority.** All deductions below are candidate-D paper results. The actual period gap remains **O**.

## Exact aggregate moments do not recover incidence

Take integers N≥3 and N/2<k<N, and set t=k/N. In a complex plane the first family comprises k coordinate lines of the first kind and N−k of the second. In the second family the N unit generators are
\((\sqrt t,\sqrt{1-t}\,\zeta_N^j)\), for a primitive Nth root and all residues j. In both families the sum S of the line projections is diag(k,N−k), by the sum of roots of unity. Hence every aggregate ordered cycle sum, tr(S^l), agrees exactly for every positive length l. The first defect is t−1/2. The second is zero because the N lines are distinct, and a proper nonzero target subspace contains at most one. The second family becomes tight after one common invertible diagonal change of target coordinates and renormalization of its generators. This example concerns aggregate moments only. It does not satisfy every sharp pair bound of the source.

## Finite noisy labelled cycles

Use the [round 9 equal-rank model](../round9/PROOF.md), with m words, target dimension D, word rank d, and md=sD for an integer s. A semistable tuple of these same dimensions exists. Place md consecutive slots cyclically modulo D into m successive groups of d slots. Each group gives d distinct coordinate directions, and each direction appears s times. The resulting projections sum to sI, so the projection trace inequality gives defect zero.

In the complex variety Gr(d,D)^m, the positive-defect locus is closed in the Zariski topology. Indeed take the finite union over ranks w and integers k_u with sum(k_u)/(md)>w/D of the loci where some w-plane W has dim(W∩I_u)≥k_u for every u. These incidence inequalities are closed by minors, and projection along the projective Grassmannian for W is closed. The semistable locus is therefore nonempty and open, hence dense also in the usual topology of this irreducible complex variety. The orthogonal projections vary continuously in that topology.

Consequently for every finite length cutoff and every strictly positive tolerance one can approximate the round 9 tuple by a zero-defect tuple whose true labelled projection-cycle traces through that length match within the tolerance, with exact isometries as inclusions. Each pair bound persists with arbitrary strictly positive relative slack by continuity. The cutoff and tolerance can depend on the dimensions. The initial tuple has the square-root defect proved in round 9. This only obstructs stable reconstruction near that tuple. It does not obstruct one-sided tests excluding its neighborhood, an exact labelled identity, or bounds special to actual periods.

## Coarse and refined algebras

Tensor the bad round 9 tuple with the identity of a common matrix factor. The factor has exact source and target mass proportions and its multiplicity-space projections are the original commuting incidence projections. Their double-commutator Laplacian kills every diagonal matrix, including nonzero traceless ones, while the frame operator has nonconstant diagonal. Thus exact coarse balance, full action on the common factor and sharp pair bounds need not give a multiplicity gap. Refining by the joint coordinate patterns of all incidence projections makes each word either zero or the identity on each pattern. Its internal centered frame operator vanishes there, but the positive block mass imbalance is exactly the original defect: a coordinate with K incidences contributes (K/s−1)/D before taking the positive part. A finer algebra can simply move the obstruction into its block weights. No realization by actual period maps is claimed.

## A nontight rational family passes the exact gap test

In the complex plane use the lines through (1,0), (0,1), (1,1), (1,−1), and (3,4), with their orthogonal projections. Every projection has rational entries. The sum is 2I plus the last projection, so the centered sum has operator norm 1/2. For an orthogonal basis, half the sum of the double commutators with its two projections is identity minus orthogonal projection onto its diagonal matrix space. The traceless diagonal directions for the first and second bases are Hilbert–Schmidt orthogonal. On traceless Hermitian matrices the two basis contributions therefore sum to at least identity. The last projection adds a positive semidefinite form. This proves gap at least one, sufficient for the exact centered-norm test. Directly, a proper nonzero target subspace contains at most one of these five distinct lines.

## Independent check of the averaged near-isometry transfer

Write R for total source dimension and D for target dimension. Let H_u project onto the range of A_u, B_u=A_u A_u*, and Δ_u=B_u−H_u. Suppose the sum of squared Hilbert–Schmidt errors of A_u* A_u from identity is at most eR. The nonzero squared singular values give
\[
 \sum_u\|\Delta_u\|_{HS}^2\le eR,\qquad
 \sum_u\|\Delta_u\|_1\le R\sqrt e,\qquad
 \kappa=R^{-1}\sum_u\dim\ker A_u\le e .
\]
The trace-norm bound uses summed ranks at most R. For every orthogonal projection X, its commutator with Δ retains the two off-diagonal blocks with opposite signs, hence contracts the Hilbert–Schmidt norm. The triangle inequality squared gives
\[
 \tfrac12\sum_u\|[X,H_u]\|_{HS}^2
 \ge \tfrac14\sum_u\|[X,B_u]\|_{HS}^2-eR/2 .
\]
In the compression of H_u to ran X, its unit eigenspace is the intersection. Each eigenvalue strictly between zero and one satisfies λ≥λ(1−λ). Thus the trace minus the intersection dimension pays at least half the squared commutator norm.

For a canonical block projection write X as the identity on each common simple factor tensored with X_β. Subtract x_β I in each multiplicity block, where x_β is the rank fraction of X_β, to get Y. Since its operator norm is at most one, replacing the centered trace against the sum of H_u by that against the sum of B_u costs at most R√e. In a multiplicity block tr((Y_β)_+)=||Y_β||²_HS. Consequently the trace of Y_β against any Hermitian matrix is at most that matrix's spectral diameter times ||Y_β||²_HS. If the normalized B-Laplacian (D/(2R)) times the sum of double commutators has traceless gap γ_β and the normalized frame operator (D/R) times the sum of B_u has diameter at most γ_β/2 there, the retained half-gap pays the entire centered term. For a one-dimensional block it vanishes. Clipping the normalized frame to such an interval and leaving an error L_β costs at most its trace norm, with global weight s_β/D. The resulting bound is
\[
 \epsilon\le\kappa+\sum_\beta(b_\beta-q_\beta)_+
 +\sqrt e+e/2+D^{-1}\sum_\beta s_\beta\|L_\beta\|_1.
\]
Here b uses actual image ranks, q uses target dimensions, and L is zero when no clipping is required. The canonical maximizing projection follows from the common action and the largest maximizer as in round 17. An arbitrary conditional expectation of a projection need not be scalar in each block; the trace-norm identity uses this specific blockwise centering.

**O.** No audited actual-period estimate supplies this multiplicity gap and frame-diameter or trace-tail control. Absolute majorants for individual summands of cycles do not compute the signed ordered traces needed in lifted operator moments. A formal additive-character average does not itself estimate the actual character slice. No scientific computation, formal build or external independent confirmation was performed.

## Scope correction for small source loss

**Candidate-D.** The all-subspace criterion in rounds 17 and 18 is an optional stronger goal. The source-loss test in the Zhang span argument concerns the codimension of the surviving span after a *total* small loss in the source. Its elementary centered estimate has a different scale. Let C be the direct sum of A_u* A_u, t=tr(C)>0, and set η=D⁻¹||DS/t−I||²_HS for S=Σ B_u. Let the discarded orthogonal source directions have total rank αR, with block projector Z. If W is the orthogonal complement of the surviving span and w=dim(W)/D, positivity gives tr(XS)≤tr(ZC) for X the projector onto W. Centering the source trace at t/R gives
\[
 \operatorname{tr}(ZC)/t\le a=\alpha+(R/t)\sqrt{e\alpha(1-\alpha)} .
\]
Indeed ||Z−αI||²_HS=Rα(1−α) and ||C−(t/R)I||²_HS≤eR. Centering the target test gives tr(XS)/t≥w−√(ηw(1−w)). Replace a by min(a,1). When w>a squaring yields a quadratic, and when w≤a the same upper bound holds:
\[
 w\le \frac{2a+\eta+\sqrt{\eta^2+4\eta a(1-a)}}{2(1+\eta)}
 \le a+\sqrt{\eta a}+\eta .
\]
At zero source loss this yields w≤η/(1+η), including singular maps. Equality is possible for a target frame scalar on its support and zero on its orthogonal complement. Small positive loss therefore incurs a mixed square-root term, in place of a uniform square root of the variance. The estimate holds for the specified direct sum of surviving source spaces, including skew subspaces within individual words. Substituting known tail fractions α into a slope integral gives a pointwise improvement wherever they are small. Any improved family endpoint needs those fractions, the integration range and the source normalization; this inequality alone gives no new RH or HN conclusion.

## Semistability can escape the exact test in every target metric

**Candidate-D.** In the complex plane take the four word lines spanned by e1, e1, e2 and e1+e2. The defect is zero because no line occurs more than twice. The repeated line W attains equality. For every Hermitian target inner product at least one of the remaining two distinct lines is not perpendicular to W, and neither equals W. Thus at least one compressed projection has an eigenvalue strictly between zero and one. For that eigenvalue the principal-angle leakage inequality is strict, since λ−λ(1−λ)=λ²>0. An exact, tail-free projector gap at least the centered frame diameter would then give strictly negative defect at W, contradicting its equality. Common invertible changes of target coordinates and normalization of the line generators cannot make this family pass the test. This concerns exact certification and does not rule out approximation.
