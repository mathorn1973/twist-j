# Round 12 source map and authority record

**NON-CANONICAL. No authority. No Canon status change.**

The proofs apply to the genuine supplied automorphic realization. A
source declaration identifies an interface or a supplied construction;
reading it is not a Lean build. In particular, none of the new deductions
is asserted for arbitrary abstract matrices satisfying only the frame
estimates. This is the existing candidate C-RH-SEMISTABLE-FRAME-N.

## 1. Basis, ownership and custody

PUBLIC was selected. On 2026-11-23, STATUS was read first at public main
`ed3b1878d95825ab9473c16416c8db76cc152079`, Public Canon v116 ACTIVE.
POLICY, AGENTS, CORE, FRONTIER and the normative hash manifest were read
at that exact main and compared with the previously read authority.
The declared content commit is
`0b6ae8e23d7086715b908cce6e1755d2898f55fc`.
Annotated tag `canon-v116`, object
`bf514bdd92d711c10131bebb8ba2b678e999d72d`, dereferences to
`93c36089db57032a6cbca482ff62c95884567d0f`.
Both the content commit and tag target are ancestors of this public main.
All five normative files matched their declared byte counts and SHA-256
hashes. Exact-main check `138025181448` and architecture checks
`138022828681` and `138022828135` succeeded. These facts authenticate
the public basis; they do not establish the new paper claims.

The full remote branch inventory, 100 recent open issues, the relevant
RH branches and the registry were checked before editing. Issue #2070
was updated to claim the paper scope for
`ChatGPT-Astra-Sol-20261123-R12` before writing round 12. The separate
centered-frame issue #2065 / PR #2067 remains separately owned. This
continuation uses the same draft PR #2071 and branch as rounds 8-11.

The round 11 starting commit is
`d06393ec835263c57478822c832a2dae80d7e2e8`, tree
`abd5e4b65e807c77186a704b276d5ddc7f80d4f3`.
Only round12/ and the candidate's parent README/handoff are changed.
No earlier scientific record, verifier, first-run output, frozen contract,
proof or review is revised.

The mathematical pin remains
[40e56bab026552e089d7afcfeff08d2defb9c005](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005).
All line references below use it. The package contains original
exposition and links, not copies of third-party papers or Lean code.

## 2. Exact source correspondences

| Input | Pinned declaration and role |
|---|---|
| Actual normalized relative vector | [HidaSetting.lean, 151-156, 302-321](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L151-L156). `IsWu` includes equivariance, pointwise convolution reproduction, continuity, integrability and squared norm one. `Wu_spec` supplies it for each actual word and the actual quotient measure. Blob `7f21195438209fd7fc4d0b081fe53297f07fb9c4`. |
| Actual infinity representation | [HidaSetting.lean, 193-205](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L193-L205). Signature, discrete series, minimal compact vector, and actual convolution. |
| Schur projector identities | [ProjRows.lean, 22-54, 112-120](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/ProjRows.lean#L22-L54). `phOf` is the formal degree times the conjugated coefficient; `IsRowProj` includes self-adjointness, idempotence and the matrix-unit identity. Rank one is asserted on the irreducible representation itself, not on its entire automorphic isotypic space. Blob `a0b8bc392e40367f66384bb2bf49b9e936149bb7`. |
| Full row correspondence | [RowsDef.lean, 19-20 and 49-65](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/RowsDef.lean#L49-L65). `RowsBij` identifies the full range through evaluation at the fixed row vector. Its genuine supplier and the full finite-dimensionality/transport from round 11 are retained. Blob `713c562806ba024c53e9545072004dc59435091e`. |
| Conjugation and actual period | [ThetaIdentityOfMapsAll.lean, 77-81, 94-117, 128-133](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/LatticeFrames/ThetaIdentityOfMapsAll.lean#L94-L133). `EvalAll` uses the conjugated row; `SBes` fixes characters and embeddings; `PerLaw` retains the outer variable and finite translate. Its bare existential complex constant does not prove nonzero normalization. Blob `12a4fbcb56d1bac8afa3fa498c3695c863411d69`. |
| Positive normalization | [FoldIntegralBesselQuotientSupportedFunctionsStatement.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/FoldIntegralBesselQuotientSupportedFunctionsStatement.lean). The quantified measure identity explicitly supplies a positive real constant for all nonnegative measurable supported functions with the named invariances. Blob `0656ea02e3b4111a229957ba14c4cc97bacb88c4`. This permits the absolute-fold extension in PROOF Section 5. |
| Actual unfolding constructor | [UnfoldedPeriodEqIntegralBesselPeriods.lean, 73-98](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/UnfoldedPeriodEqIntegralBesselPeriods.lean#L73-L98). `unfoldedPer` chooses that positive real measure factor and then coerces it to the complex constant. Its displayed bounded-row statement is extended to the full actual row range by the already retained square-integrable absolute seed periodization, not by assuming all discrete rows bounded. Blob `5c0f1c119bdd58e31f4f6f3908ef69ae120f78b2`. |
| Actual seeds and maps | [PoincareInHH.lean, 135-210](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/PoincareInHH.lean#L135-L210), with round 8 absolute-fold hypotheses and round 11 fixed abstract/concrete identification. Blob `7bf59cba2a1bbcb1c81a5182c4155de354f9def4`. |
| Compact smooth type and real sign order | [RelevantZeroGramTerms.lean, 61-96, 165-170](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean#L165-L170). The minimal compact type gives the compact Casimir scalar for analytic ellipticity. `lamS`, `epsS`, and the round 11 gap argument give the initial k positive signs followed by the alternating tail. Blob `d008b93b66125f83b7adb112628b058dde3b1096`. |
| Distinct word types | [DataS.lean, 19-32](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/DataS.lean#L19-L32), blob `05d6c08d180bf9804c8cf33b5873fc0c43e93bb4`; [StandingHypothesesHoldFamily.lean, data8 at 770-783](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/StandingHypothesesHoldFamily.lean#L770-L783), blob `ceb0d69e48222f5f0cfcc8e9db7e58f7a64aa88f`; HidaSetting `piLoc_type` and product identification at 275-300. Distinct words give distinct compact types at each real place. |

## 3. Selected fresh-source comparison

The external live main was read at
[c9852685b4adcb11a08fe855824817b44c81dd69](https://github.com/leanprover-community/riemann-hypothesis/commit/c9852685b4adcb11a08fe855824817b44c81dd69),
commit timestamp 2026-11-23T21:33:14Z. Its latest change concerns fragment
publication. The following comparisons use fetched file content, not an
inference from the latest commit message.

| File | Fresh blob | Scope actually compared |
|---|---|---|
| HidaSetting.lean | `71bdf47e1603e75a19e3934a39519c37d4c35a9d` | Original lines 151-156, 193-205 and 275-321 occur verbatim in the fresh file. |
| ProjRows.lean | `0a5611c4e4233b6a8704990c715f923154f8c26b` | Original lines 22-54 and 112-120 occur verbatim. |
| ThetaIdentityOfMapsAll.lean | `4f20702240ab57cc10650f99b9bdab137300368b` | Original lines 77-81, 94-117 and 128-133 occur verbatim. |
| UnfoldedPeriodEqIntegralBesselPeriods.lean | `63356f036c609da0a86db2b715ad01f2eaf3ac50` | The quantified `unfoldedPer` statement is unchanged. The positive-real-constant selection and its coercion were read in the fresh constructor. The surrounding block is not byte-identical. |
| StandingHypothesesHoldFamily.lean | `d24e5f72a3aa481dd1cf0c7c0eff6478aadd64da` | Original data8 lines 770-783 and row_parameter_gaps_large lines 1347-1391 occur verbatim. |

Whole files differ. No live-source compilation or certification of the
whole current RH repository is inferred. The mathematical claims retain
their immutable pin and all realization hypotheses.

## 4. Primary literature and retrieval limits

| Primary source | Exact use |
|---|---|
| [Jiang-Sun-Zhu, Uniqueness of Bessel models: the archimedean case](https://arxiv.org/pdf/0908.1728) | Theorem A and Section 2 give at most one continuous Bessel functional for the actual U(k+r,r+1), U(k) pair. The anisotropic-line sign and generic character were checked. The r=0 case is restriction U(k,1) to U(k). This theorem says at most one, not at least one; the actual W supplies the latter reference model. |
| [Morrey-Nirenberg, On the analyticity of the solutions of linear elliptic systems](https://doi.org/10.1002/cpa.3160100204) | Classical analytic elliptic regularity after the explicit scalar elliptic reduction in PROOF Section 6. The publisher bibliographic record was retrieved; the complete publisher paper was not. No novel analytic regularity assertion is claimed. |
| [Yamashita, Associated varieties and Gelfand-Kirillov dimensions for the discrete series](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/0826-03.pdf) | Theorems 3.1-3.2 identify the annihilator variety from noncompact negative roots. The finite-center hypothesis is applied to SU(p,q), with the compact center then restored. Our triangular rank-and-chain argument computes the resulting hook. |
| [Matumoto, Whittaker vectors and associated varieties](https://doi.org/10.1007/BF01404678) | Theorem 2 and Corollary 4, printed pp. 222-223, give the orbit-containment obstruction. The indexed full scan was read; its direct historical PDF endpoint returned 404. No converse for real rational orbits is used. |
| [Landherr, Aequivalenz Hermitescher Formen](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/landherr.pdf) | The rational Hermitian isotropy criterion on p. 248. GLOBAL_OBSTRUCTIONS also gives a Hasse-Minkowski proof from the underlying quadratic form. This determines the ambient rational Witt index, not a nonzero Fourier coefficient. |
| [Jiang-Zhang, Arthur parameters and cuspidal automorphic modules](https://arxiv.org/pdf/1508.03205) | Proposition 2.2 and Section 2.4 separate the largest nonzero Bessel index of a specified cuspidal realization from its rational orbit. The explicit anisotropic-vector parametrization is retained. Generic summand assertions are not treated as a lower bound for the desired index. |
| [Jiang-Zhang, Bessel descents and branching problems](https://arxiv.org/pdf/1905.02307) | Proposition 5.1 and Question 5.2 state the first-occurrence issue with its cuspidal-realization scope. The period-to-central-value implication does not create a nonzero period for the selected tests. |
| [Li, Non-existence of singular cusp forms](https://www.numdam.org/article/CM_1992__83_1_43_0.pdf) | Main Theorem, printed p. 44. Its nonsingular central Fourier coefficient has square-zero type and does not imply the required positive-rank odd hook. |
| [Beuzart-Plessis-Chaudouard, Global Gan-Gross-Prasad II](https://doi.org/10.1017/fmp.2025.8) | The exact quantifier and temperedness restrictions checked in round 11 remain in force. This round does not turn an existence theorem for a parameter pair and form into the prescribed finite-family rank bound. |

## 5. Execution boundary

No scientific program, finite enumeration, independent code audit or
Lean build was planned or run in round 12. Accordingly there is no new
computation preregistration or candidate-C claim. Hashes, textual
comparisons and the repository's policy/canon checks are custody and
delivery checks. They are not mathematical verification of these proofs.
