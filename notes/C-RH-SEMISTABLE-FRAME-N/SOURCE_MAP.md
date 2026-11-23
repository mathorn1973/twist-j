# Source map and literature

NON-CANONICAL. No authority. Source declarations support the stated premises;
they are not claimed to contain our newly derived candidate-D theorems.

## Pinned source

The analysis uses the original external source commit
40e56bab026552e089d7afcfeff08d2defb9c005. References below were read by the
team; the root separately re-read the central norm, frame, counting, PMat,
SIso and RowsBij interfaces. No Lean compilation was performed.

| Topic | Pinned file and anchor | Relevant declaration or scope |
|---|---|---|
| Word norm relation | [RhoDetPrimeEqMuTildeMulChiPow.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalRingCardinality/RhoDetPrimeEqMuTildeMulChiPow.lean#L144-L151) | T_norm, cOf_ne, cOf_eq |
| Unipotent group and characters | [HidaSetting.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L23-L65) | InN, nxt, rootCoord, psiR, Ninf, psiInf |
| Integral frame and level | [HidaSetting.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L207-L273) | zu_norm, integral frame, e_eq, xu |
| Column representation | [HidaSetting.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L274-L312) | piU_rep, piLoc_type, tensor laws, Wu_spec |
| Word injectivity | [DataS.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/DataS.lean#L19-L32) | Del_pos, letter_inj, u_letter |
| Highest-weight type | [RelevantZeroGramTerms.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean#L61-L98) | IsKTypeOf, IsHCTypeU |
| Lowest type convention | [StatementDS.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/FormalDegreeBessel/StatementDS.lean#L14) | lowK |
| Finite definite class fibers | [ColsDim.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/SiegelMassRatios/ColsDim.lean#L35-L77) | Cols covariance and fiber decomposition |
| Rational finite order | [InHHFinOrd.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/InHHFinOrd.lean#L257-L373) | Finite order from a preserved lattice and a definite complement |
| Local torsion exclusion | [DecorationStabilizerTrivialUnipotent.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/Columns/DecorationStabilizerTrivialUnipotent.lean#L345-L413) | Unipotent reduction and torsion |
| Prime and dimension scales | [StandingNumericalData.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/StandingNumericalData.lean#L97-L136) | Splitting, m^4<=f<=k and large g_i |
| Paired split places | [AllRowsRedKer.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/AllRowsRedKer.lean#L78-L113) | Disjoint and exhaustive conjugate pairs |
| Full residue product | [AllRowsRhoX.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/AllRowsRhoX.lean#L18-L35) | Product over each pair at both primes |
| Admissible test projector | [GlobAut.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/GlobAut.lean#L197-L217) | Dcount, Dstar, IsAdmIdem |
| Universal spectral count | [PlaceDegreeData.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/PlaceDegreeData.lean#L364-L378) | PointsLemma; CountData at L183-L192 |
| Conditional counting supplier | [ExplicitFormulaBoundHolds.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/ExplicitFormulaBoundHolds.lean#L57-L88) | points_bound_of_volumeCountGeometryConditions, both dimension inequalities |
| Exact counted-row dimension | [RowsDef.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/RowsDef.lean#L49-L102) | RowsBij, eHomEquivHH, finrank_HH_eq_Dcount |
| Full-space coordinate map | [TopDensityNGeSixteen.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L1011-L1015) | PMat; matK_at_of at L1097-L1104; rowBasis at L1171; blockReal_at_of at L1283 |
| Concrete/abstract transport | [ParametersTermRelations.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ParametersTermRelations.lean#L286-L323) | SIso with Pu_eq; SConc existential package |
| Good-row space distinction | [RowDict.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RowDict.lean#L100-L149) | goodSub, EEC, RowDictTie |
| Actual seed and periodization | [PoincareInHH.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/PoincareInHH.lean#L144-L199) | Cu, IsDec, phVal, PhWellDef, Pser, InHH |
| Absolute folding | [PoincareSeriesSquareIntegrable.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/PoincareSeriesSquareIntegrable.lean#L15-L61) | Multiplicity integral and square-integrable sum |
| Fold condition for seeds | [InHHCut.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/InHHCut.lean#L331-L339) | IsFoldDatum input |
| Rational Levi quotient | [InHHAlg.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/InHHAlg.lean#L575-L582) | Rational decomposition and trivial product character |
| Evaluated seed | [FourierCoefficientBessel.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/FourierCoefficientBessel.lean#L30-L110) | psiInfU_of_mem_Hinf, Ph_of_dec at L47, ph_colForm |
| Representative hypotheses | [ThetaIdentityOfMapsAll.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/LatticeFrames/ThetaIdentityOfMapsAll.lean#L94-L130) | EvalAll, RowFun, SBes, PerLaw |
| Unfolded period | [UnfoldedPeriodEqIntegralBesselPeriods.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/UnfoldedPeriodEqIntegralBesselPeriods.lean#L73-L78) | unfoldedPer and positive constructed constant |
| Period identity | [ConjugateRowPairingPoincareSeriesBesselPeriods.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ConjugateRowPairingPoincareSeriesBesselPeriods.lean#L17) | perLaw_holds |

## Literature, with its actual scope

- [Ivanyos, Qiao and Subrahmanyam, Constructive Non-Commutative Rank Computation Is in Deterministic Polynomial Time (ITCS 2017)](https://drops.dagstuhl.de/storage/00lipics/lipics-vol067-itcs2017/LIPIcs.ITCS.2017.55/LIPIcs.ITCS.2017.55.pdf): maximal shrunk subspaces and finite blow-up rank certificates. The noncommutative-rank theorem used in PROOF.md is classical.
- [Iwamasa, Oki and Soma, Algorithmic aspects of semistability of quiver representations, arXiv:2407.06493v3, 12 May 2025](https://arxiv.org/abs/2407.06493v3): algorithms for semistability, maximizers of King's criterion and Harder-Narasimhan filtrations. This supports an algorithmic route once actual matrices are supplied; it does not prove their semistability.
- [Chindris and Derksen, Algebraicity of the Brascamp-Lieb constants, arXiv:2603.09057v2, 4 July 2026](https://arxiv.org/abs/2603.09057v2): semialgebraicity on the feasible locus, with rationality assumptions on exponents added in v2. Feasibility is a premise, not a consequence for our data.
- [Bonnafe and Kessar, On the endomorphism algebra of modular Gelfand-Graev representations](https://arxiv.org/abs/0708.3540): the characteristic-zero Gelfand-Graev corner and its characters; the finite general-linear case gives the generic multiplicity-one input.
- [Patel and Singla, A multiplicity one theorem for groups of type A over discrete valuation rings](https://arxiv.org/abs/1809.08743): the more general finite-ring theorem is background; our one-prime argument only needs finite fields.

## Current online context, distinct from the proof pin

On 23 November 2026 we read the external RH repository's then-current head
ef349ac02c55f6fa50f7e8c1db3a5cbe2218e927 and its
[README](https://github.com/leanprover-community/riemann-hypothesis/blob/ef349ac02c55f6fa50f7e8c1db3a5cbe2218e927/README.md).
The repository describes ongoing community maintenance, statement-comparison
and kernel-checking procedures. We did not execute these procedures and do
not turn that description into an independent RH validation. Its main had
advanced beyond the frozen original; this package does not claim a complete
re-audit of those changes. The README identifies 40e56bab as the unmodified
published source, which is the intentionally fixed basis used here.

The external README states that the original submission was published without
a license. This package imports no external Lean implementation, and does not
relicense it. Its Python programs and mathematical exposition were newly
authored; external declarations are linked for inspection.
