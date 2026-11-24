# Round 19. Source scope of projector counts and paired cycles

**NON-CANONICAL. No authority. No Canon status change.** The period maps and cycle identities retain the [round 18 mathematical pin][old]. The comparison revision is [community main 4d25b0edc80cbf28a7b82a9d491d95875b36e826][new], observed on 24 November 2026 by repository lookup and branch ref. The [comparison][compare] reports 809 commits ahead and zero behind, with at most 300 changed paths in the returned list. The comparison below concerns named declarations and proof fragments. The earlier comparison at `c82871e6002287776ae8a7c9a1a79926f15c3c8e` remains as recorded in [round 17](../round17/SOURCE.md#custody).

## 1. The current projector calculation

**Candidate-D.** The former geometry-supplier path is absent at the comparison revision, and the old `SphericalFunctionIntegrableOfLocal.lean` path retains only the data and Cartan distance relevant here. There is a current absolute-diagonal calculation in `GlobalTheory.abs_integral_sub_const_mul_le_of_split`. Its proof first bounds the integral of `‖K x - c‖` on the moderate set $M$ by the sum of the near and far bounds. The counting proof instantiates $K(x)=\operatorname{Re}\,\mathrm{kern}(x,x)$ and $c=(\prod_v d_v)\operatorname{Re} e(1)$, and proves $K\ge0$ by the finite kernel expansion. It supplies the deep-region integral of $K$ and bounds the measure of the complement of $M$. In the proof's notation, if $a,b$ are the near and far upper bounds and $e$ is the deep-region upper bound, these ingredients give
$$
\int |K-c|\,d\mu\le a+b+e+c\mu(M^c).
$$
The last two terms follow from $|K-c|\le K+c$ on $M^c$. The final counting statement uses this input at the level of the absolute difference of the integrated diagonal and the main term. [Old path at comparison revision][old-path] · [Split estimate, including the absolute integrand][split] · [Projector and bound inputs][row-split] · [Trace identity and rare-set measure][row-mass].

The supplier `countingTheorem_of_volumeStep` assembles finite dimension, near, far, rare-flag and deep-region bounds. `count_typed_of_volumeStep` passes to `PointsLemma` at its stated thresholds. These are actual theorem bodies with stated inputs, including `VolumeStep`. The comparison establishes a corresponding absolute-diagonal route with its own data. Transport to every geometric realization used at the earlier pin would require a separate comparison. The projector calculation measures the reproducing projector and fixes its identity contribution. A realization in its range gives no estimate of the spectrum of the individual period maps or of the operators they induce on row endomorphisms. [Current supplier][count-supply] · [Typed bridge][count-typed] · [Siegel–Weil input][siegel].

## 2. Which quantities the period estimates control

**Candidate-D.** At the comparison revision, `diag_unproj` proves the strong diagonal Hilbert–Schmidt bound from `AdmissibleBoundsFromSource.hyp` and `Conclusion1`. It uses the upper size proviso to bound the positive-pair term by $C_0 n_u/\Gamma$ inside the squared bound. `linkS_concl` combines this bound and the off-diagonal estimate with a separate row-count input. The final frame passage derives the universal total word dimension lower bound $D_*/\mathrm{sg}$ from `ChCode_at`, `ChProviso_at` and the certified dimensions. These statements have explicit conditions on the family and rank losses. They furnish neither an estimate uniform in the preimages of all row subspaces nor a two-copy estimate on arbitrary row endomorphisms. [Sharp diagonal and row-count premise][diag] · [Word count in the frame proof][word-count].

The current unfolding still constructs the operators for one ordered word pair. `RP` and `pvR` use two terms of that same pair with the common `rowOf` label, and `packageTieConc` uses the resulting comparison for the Hilbert–Schmidt square. The endomorphism trace in this round uses two *closed cycles on the same word tuple*. The coefficient includes the relative phase of the two closing elements. The audited statements use the single-edge `rowOf` label and give no comparison of these two closing elements. A bounded declaration and text search in the current sharp-restriction, period, term, and unfolding trees located no estimate for the relative-phase sum or a gap for the resulting commutator form. **O** for this supplier on the realized multiplicity spaces. [Current pair and scalar definitions][pairs] · [Unfolding][unfold] · [Norm transfer][norm] · [Round 18 cycle identity](../round18/SOURCE.md).

## 3. The rank and slope conclusion used in the original chain

**Candidate-D.** The current `FrameReal_at` identifies the arithmetic maps with isometric restrictions of full period maps and bounds the total rank discarded in these initial restrictions by `de` times total full source rank. The theorem `frame_at_of` supplies `Frame_at` with isotropy bound `5 sg + 3 sqrt de`. The family hypothesis absorbs the compression and diagonal errors by `(3 sqrt de + 4 sqrt eB) x^CH ≤ 1`, where `sg = x^(-CH)`. Written with the record's slope parameters $s,u,H$, `Frame_at` supplies the mean dual slope bound

$$
\mu_{\mathrm{dual}}
\ge s-\log |\mathrm{Word}|
-\frac{4u\log(1+H/u)+(\eta+4\sqrt e)H}{1-\mathrm{delp}},
\qquad H>0,\qquad s-\mu_{\min,\mathrm{dual}}\le H .
$$

Here `sFrame` and `uFrame` give $s,u$, and `Frame_at` quantifies over $H$ with the two indicated conditions. The succeeding slope comparison uses small total rank loss at Harder–Narasimhan thresholds. This differs in hypothesis and conclusion from prescribing an exponentially small preimage concentration defect uniformly over all targets. [Full-map comparison and original frame bound][frame-real] · [Harder–Narasimhan consumer and family bound][frame-family] · [Exact record mean-slope inequality][frame-slope] · [Zhang, §4.3 and Lemma 4.2][zhang].

The Rubinstein draft derives the related codimension bound (III.236), with retained complex target dimension $D_r$. The bound divided by $D_r$ is $(5\,\mathrm{sg}+4(\alpha_{\rm ram}+\alpha')+4\sqrt{e_0})/(1-\delta_p)$ under its three period and realization conditions and its total removed-rank budget. Brox's averaged theta energy note, §2 (2.7), gives `eta' ≤ 11 sg + 3 de` and `e' ≤ 4 e0/3` from full isotropy `eta ≤ 5 sg`, `sqrt e0 ≤ sg/2`, and source rank loss share `de ≤ 1/4`, with `0 < sg ≤ 1/20`. These inequalities preserve the polynomial order of the original compressed-isotropy estimate under the source family loss bounds. This is a finite-dimensional consequence on the same maps once the realization and full bounds are supplied. Using revised constants in subsequent arithmetic estimates would require checking those estimates. A stronger endomorphism-space estimate is an optional route to a stronger statement than this rank and slope conclusion. [Rubinstein, Corollary T2][rubinstein-t2] · [Brox compression estimates][brox-energy].

### The same Harder–Narasimhan threshold interface

**Candidate-D.** At the comparison pin, `FrameLA1` takes the positive weights, aggregate diagonal Hilbert–Schmidt defect at most $eR$ with $0\le e\le1/4$, and second moment at most $(1+\eta)t^2/D$ with $\eta\ge0$. Its proof gives $t\ge R(1-\sqrt e)$. The inputs of `thmF_place` use these quantities for the matrices `Ball` on the post-ramified source coordinates. The domain subspace at each threshold is the complex span of the corresponding lattice submodule in the chosen place coordinates. Its complex dimension equals that submodule's rank over the number field. Projection onto the arithmetic target gives the stated corank transfer. [Frame hypotheses][frame-la] · [Trace lower bound][frame-trace] · [Complex realization and projection][frame-place].

The proof of `theoremFSharp_of` uses the source Harder–Narasimhan step at $(s-\tau+h_i-\mathrm{slopeNormalisingConstant}(K))/2$. Its sum of removed ranks over the number field is at most $u/(u+\tau)$ times the sum of the **post-ramified** source ranks. In proving this inequality, the real-lattice rank factor $[K:\mathbb Q]$ cancels from both sides. The mean slope condition is weighted by those same source ranks, and each adjusted maximal slope is at most $s+u$. The hypothesis is $u\ge0$. When $u=0$, the adjusted slopes all equal $s$ on the positive-rank source parts and there is no removed rank for $\tau\ge0$. The proof next includes the sum of arithmetic images in the target Harder–Narasimhan step. Passing from the full complex target to the retained target introduces the factor $(1-\delta)^{-1}$ through their dimension inequality. The ensuing integration recovers the mean-slope bound. [Tail including the zero case][frame-share] · [Threshold and cancellation][frame-threshold] · [Target step and corank conversion][frame-target] · [Integration][frame-layer].

The source's `frame_at_of` sets $s$ to the rank-weighted mean of $\mu(N_i)-h_i$. It sets $u$ to the supremum of the shifted maximal slopes minus $s$. The theorem's proof imports the initial ramified loss through the diagonal defect and centered second-moment estimates. The threshold tail uses the ranks after that step. Hence the paper corank bound in [BRIDGE](BRIDGE.md) can replace the `FrameLA1` envelope on these same inputs. Both the retained-target dimension factor and the record's displayed word-count loss can be kept. The source separately proves a sharp branch without that word-count loss. This comparison changes the paper estimate on the matched inputs. There was no Lean run or modification of a verified theorem. [Record parameters][frame-su] · [Original ramified slope bounds with both branches][frame-branches].

## 4. Independent reading and validation scope

**Attribution.** The centered two-projection inequality used in BRIDGE,
Section 4, is Brox's equation (2.1) in [frame-degree-compatibility][brox-centered].
Taking complementary subspaces and solving its quadratic gives the
displayed corank envelope. This round matches the resulting affine
envelope to the current source's actual threshold integral. Brox's
separate centered slope bound (3.2), with square-root target-variance
dependence, is complementary. Neither frame comparison by itself
supplies an absolute geometric degree bound in prescribed arithmetic
metrics.

**Observed source reports.** The Lean FRO and Mathlib Initiative report exact comparison against [Mathlib's RH predicate][mathlib-rh] by Comparator and con-leche, and acceptance of the exported proof by several kernels. Andrew Sutherland's 23 November 23:45 UTC verification record separately reports comparison of all five headline statements by con-leche and con-ron, official Lean and independent kernel acceptances, replay of all original modules, and a sandboxed rebuild reproducing the export byte for byte. These checks concern the released proof and its declared statements. The new concentration estimate, the identification of geometric data between two revisions, and the stronger endomorphism-space supplier are separate mathematical questions. [Lean FRO and Mathlib statement][lean-blog] · [Sutherland verification record][sutherland]. Issue 41 concerns a proposed alternate dynamical stability formulation and classical axioms and is closed as not planned. It supplies no estimate used here. [Issue 41][issue41].

**O.** At [Brox commit fd38313e5c7018c3c988ba20510e6b0b3bca0519][brox], the averaged theta energy identity `tr(Q²) = Ω + 2M − R + Δ` uses the total off-diagonal pair energy. The compression result and weighted frame penalties are conditional on the actual normalized maps and the specified energy or averaged bounds. The note pins its separate Lean reading at `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de` and records the conditional Bessel and common-basis bridge. The normalized far-return bound is for the original projector kernel. The bounded comparison identifies range conditions for the period maps, with the projector-to-period-Gram transfer still open. Its Whittaker covariance obstruction explains why a full-group decay bound for that vector cannot supply the transfer. The embedded-isometry genus mean and fixed-normal-form weighted sum cover separate counting statements. The original weighted fibre correspondence `PerRowC` and the full global norm step remain open in that distillation. [Averaged frame energies][brox-energy] · [Projector and Whittaker comparison][brox-projector] · [Genus mean][brox-genus] · [Weighted normal forms][brox-normal].

The Rubinstein working draft v2 proves the finite-dimensional comparison and a conditional codimension conclusion for restricted maps with a total removed-rank budget. Section III.8 explicitly leaves the actual normalized centered second moment's order relative to $x^{-C_H}$ open. Its dependency discussion distinguishes the checked use of `CompressTraceSquareBound`, `LinkS`, `BesselId` and `TheoremF` from the draft's alternate codimension route. Robin Zhang's preliminary note §4.3 and Lemma 4.2 describe the threshold-cut spanning argument for slopes. The scopes of these conclusions give no estimate for the paired-cycle sum on the row endomorphisms. [Rubinstein v2, §III.8][rubinstein] · [Zhang preliminary note][zhang].

The comparison used repository metadata, selected source text and published verification records. No Lean run or numerical instance was used for this audit.

[old]: https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005
[new]: https://github.com/leanprover-community/riemann-hypothesis/tree/4d25b0edc80cbf28a7b82a9d491d95875b36e826
[compare]: https://github.com/leanprover-community/riemann-hypothesis/compare/40e56bab026552e089d7afcfeff08d2defb9c005...4d25b0edc80cbf28a7b82a9d491d95875b36e826
[old-path]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/SharpRestriction/CuspSpanNormBounds/BruhatCellsKronecker/SphericalFunctionIntegrableOfLocal.lean
[split]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/DiscreteSeriesCountingOfFiniteAndBounds.lean#L98-L137
[row-split]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/DiscreteSeriesCountingOfFiniteAndBounds.lean#L564-L601
[row-mass]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/DiscreteSeriesCountingOfFiniteAndBounds.lean#L602-L629
[count-supply]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/CountTypedOfVolumeStep.lean#L1755-L1767
[count-typed]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/CountTypedOfVolumeStep.lean#L1860-L1867
[siegel]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/CountConstantsOfSiegelWeil.lean#L1225-L1260
[diag]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/SharpRestriction/CuspSpanNormBounds/StandingHypothesesHoldFamily.lean#L284-L344
[word-count]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L573-L596
[frame-real]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L553-L575
[frame-family]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L630-L642
[frame-slope]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean#L230-L235
[frame-la]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/HarderNarasimhan/StatementFrameF.lean#L55-L68
[frame-trace]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/HarderNarasimhan/ShiftInvariance.lean#L732-L753
[frame-place]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/HarderNarasimhan/ShiftInvariance.lean#L1013-L1127
[frame-share]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/HarderNarasimhan/ShiftInvariance.lean#L989-L1011
[frame-threshold]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/HarderNarasimhan/ShiftInvariance.lean#L1194-L1253
[frame-target]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/HarderNarasimhan/ShiftInvariance.lean#L1255-L1315
[frame-layer]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/HarderNarasimhan/ShiftInvariance.lean#L1316-L1366
[frame-su]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L597-L634
[frame-branches]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/JointDModelAppliesUnitLattice.lean#L912-L955
[pairs]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ParametersTermRelations.lean#L217-L275
[unfold]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/DoubleCosetSingleUnfolding.lean#L518-L548
[norm]: https://github.com/leanprover-community/riemann-hypothesis/blob/4d25b0edc80cbf28a7b82a9d491d95875b36e826/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ParametersTermRelations.lean#L404-L413
[mathlib-rh]: https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html#RiemannHypothesis
[lean-blog]: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/
[sutherland]: https://math.mit.edu/~drew/grh/
[issue41]: https://github.com/leanprover-community/riemann-hypothesis/issues/41
[brox]: https://github.com/JoseBrox/GRH_distillation/tree/fd38313e5c7018c3c988ba20510e6b0b3bca0519
[brox-centered]: https://github.com/JoseBrox/GRH_distillation/blob/fd38313e5c7018c3c988ba20510e6b0b3bca0519/notes/frame-degree-compatibility.md
[brox-energy]: https://github.com/JoseBrox/GRH_distillation/blob/fd38313e5c7018c3c988ba20510e6b0b3bca0519/notes/averaged-theta-energy.md
[brox-projector]: https://github.com/JoseBrox/GRH_distillation/blob/fd38313e5c7018c3c988ba20510e6b0b3bca0519/notes/projector-kernel-tail.md#3-why-the-whittaker-transfer-is-a-separate-step
[brox-genus]: https://github.com/JoseBrox/GRH_distillation/blob/fd38313e5c7018c3c988ba20510e6b0b3bca0519/notes/embedded-isometry-genus-count.md#the-next-precise-frontier
[brox-normal]: https://github.com/JoseBrox/GRH_distillation/blob/fd38313e5c7018c3c988ba20510e6b0b3bca0519/notes/weighted-flag-lattice-sum.md#verification-and-remaining-frontier
[rubinstein]: https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=150
[rubinstein-t2]: https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=141
[zhang]: https://www.ihes.fr/~rzhang/files/GRH%20note.pdf
