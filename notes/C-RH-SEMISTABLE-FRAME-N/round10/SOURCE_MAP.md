# Round 10 source map

NON-CANONICAL. Paper reading and derivation, not a Lean build.
No source status is promoted.

## Basis and fresh source check

The public TWIST-J authority check used main
93c36089db57032a6cbca482ff62c95884567d0f, Public Canon v116 and its
declared content commit 0b6ae8e23d7086715b908cce6e1755d2898f55fc.
The declared tag, ancestry, five normative hashes/byte counts and successful
base checks were read back. They authenticate the project basis only.

The mathematical source pin for this investigation is the version supplied
in the earlier audit:
[leanprover-community/riemann-hypothesis at 40e56bab026552e089d7afcfeff08d2defb9c005](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005).

On 2026-11-23 the live external main was also read at
[a771b25435b26f5c58b9954d3a84a3eef0985a6e](https://github.com/leanprover-community/riemann-hypothesis/commit/a771b25435b26f5c58b9954d3a84a3eef0985a6e),
whose last change is runner-contributor documentation. It is a descendant
of the pinned version. The seven files below were compared directly, not
inferred unchanged from the last commit message:

| File stem | Original blob | Current blob | Relevant comparison |
|---|---|---|---|
| HidaSetting | 7f21195438209fd7fc4d0b081fe53297f07fb9c4 | 71bdf47e1603e75a19e3934a39519c37d4c35a9d | Nfin, psiFin, OneOff, norm and translate fields unchanged; module/import changes and a changed type spelling in Fu_fixed |
| PoincareInHH | 7bf59cba2a1bbcb1c81a5182c4155de354f9def4 | 078306ae43e7d04bea93bec89caaf85b4b590cb3 | H, level, columns and seed definitions unchanged; ColsLink wrapper removed |
| InHHCut | 7ead8c1bf99029cef1a4ce5384a206b76ecaa2f0 | 5cf6773cae91d417d99c5ad693b262bcf11c810c | LevelDec statement unchanged; import and tactic changes |
| InHHAlg | a0818d20735e89ef490514da89a899443b6e90f1 | 6f0f680a2fb1c8e5fb861ca300a66defa5b98b33 | levelDec_of argument unchanged; separate wrappers/lemmas removed |
| ColsDim | 7aace7e1570fb2ca1bf4201f50b11e80c6d9695a | da66b8a570ab85f7e16929a7262dde9b1cc38d5c | columns_dimension retained; other wrappers removed and syntax adjusted |
| TopDensityNGeSixteen | cbccb968fd96afe14797b8890f4e5dc63bd11d26 | 65ad092e896982f416bebb706d97872f557934d0 | MatS_at, MatSF and MatK_at bodies unchanged; changes elsewhere |
| ThetaIdentityOfMapsAll | 12a4fbcb56d1bac8afa3fa498c3695c863411d69 | 4f20702240ab57cc10650f99b9bdab137300368b | EvalAll, RowFun, SBes and PerLaw bodies unchanged; other declarations removed |

In Fu_fixed the displayed LFlag type changes from VS(D) to D.sp.Y(0).
This reading records that difference; it is not a new compilation or a
certification of all current realization suppliers. The proof and all
line references remain scoped to the original immutable pin.

The live [Brox distillation](https://github.com/JoseBrox/GRH_distillation)
was read at fd38313e5c7018c3c988ba20510e6b0b3bca0519. Its recorded latest
change concerns dyadic Bernoulli units, weighted lattice sums and the
signed height test. Round 10 does not attribute its new local rank or
vanishing deductions to Brox.

The adjacent TWIST-J issue #2065 / PR #2067 owns the centered-frame
refinement. This continuation keeps issue #2070 / PR #2071 and does not
reclaim that neighboring item.

## Source declarations used

All links in this table use the original external pin.

| Point in round 10 | Source and exact role |
|---|---|
| Actual N and its trace character | [HidaSetting, lines 23–44 and 103–116](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L103-L116). The two split components and their terminal vector/covector are derived in the paper. |
| Character conductor | [HidaSetting, lines 65–69 and 228–231](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L228-L231). Both integrality and the rational product law are used. |
| Hyperbolic pairing, norm, lattice | [HidaSetting, lines 207–226](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L207-L226). Primitivity and the complete-splitting supplier are retained from round 9. |
| x_u is identity off g | [OneOff at lines 95–99](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L95-L99) and [xu_one at lines 267–273](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L267-L273). Apply all powers of a prime coprime to g. |
| Smaller-group column realization | [PoincareInHH, lines 62–145 and 156–210](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/PoincareInHH.lean#L62-L145). Factorization of the actual level and character is required. |
| Exact column class dimensions | [ColsDim, lines 406–416](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/SiegelMassRatios/ColsDim.lean#L406-L416). Coarse-level torsion exclusion is proved separately in Section 2. |
| Split primes and large retained level | [StandingNumericalData, lines 84–136](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/StandingNumericalData.lean#L84-L136), with its suppliers, including [residEv_of_GL](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/StandingHypothesesHoldFamily.lean#L2143-L2164). HidaSetting alone is insufficient. |
| Individual kernels | [MatSF](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L740-L744), [MatK_at](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L807-L818) and the actual full PMat construction described in round 9. |
| Absolute unfolding on all L2 rows | [PoincareSeriesSquareIntegrable, lines 15–61](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/PoincareSeriesSquareIntegrable.lean#L15-L61). The same IsFoldDatum and multiplicity integral apply to the absolute seed. Fundamental domains, finiteness and Haar hypotheses remain explicit. |
| Actual selected period | [EvalAll, RowFun, SBes and PerLaw](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/LatticeFrames/ThetaIdentityOfMapsAll.lean#L94-L138). The conjugated row, particular column vector and outer integral are retained. |
| Full target transport | [SIso and Pu_eq](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ParametersTermRelations.lean#L286-L323). One fixed realization is required throughout. |
| Rational common-H transport | [cOf_eq and T_norm](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalRingCardinality/RhoDetPrimeEqMuTildeMulChiPow.lean#L142-L154), with the explicit conjugacy of round 8. |
| Distinct actual evaluation orbits | [LevelDec](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/InHHCut.lean#L116-L121) and [levelDec_of](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/InHHAlg.lean#L371-L404). The argument is conditional on these actual suppliers. |
| Selected archimedean words | [piLoc_type and orthonormal frames](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L275-L300) and [data2, data8, data7](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/StandingHypothesesHoldFamily.lean#L755-L813). Local type distinction is not injectivity of the word-prime assignment. |

## Classical primary references and what they supply

1. Hiraku Atobe, Satoshi Kondo and Seidai Yasuda,
   [Local newforms for the general linear groups over a non-archimedean local field](https://arxiv.org/pdf/2110.09070),
   [published version](https://doi.org/10.1017/fmp.2022.17).
   The all-irreducible local newform rule is used as established in
   round 9. No newform theorem is being proved by our finite audit.

2. A. V. Zelevinsky,
   [Induced representations of reductive p-adic groups II](https://www.numdam.org/article/ASENS_1980_4_13_2_165_0.pdf),
   Example 3.2 and Theorem 4.2.
   They supply the determinant-character segment representation and
   irreducibility for pairwise unlinked segments. The height-interval
   construction is explained in our proof.

3. I. N. Bernstein and A. V. Zelevinsky,
   [Induced representations of reductive p-adic groups I](https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BZ-induced-1.pdf),
   Sections 5.3–5.4, 5.11 and 5.14.
   These are the smooth-section and orbit-filtration framework. The
   trace-annihilator cutoff and the uniform compact averaging on each
   support are proved explicitly in our Section 5.

4. Hee Oh,
   [Uniform pointwise bounds for matrix coefficients of unitary representations and applications to Kazhdan constants](https://bpb-us-w2.wpmucdn.com/campuspress.yale.edu/dist/5/5177/files/2025/11/mat.pdf),
   Theorem 1.1 and Section 3.7.3, Duke Mathematical Journal 113 (2002).
   They give the quantitative bound (3q-1)/(q(q+1)) on the local
   Hecke compression after excluding SL-invariant vectors. They do not
   bound the selected automorphic period.

5. Yifeng Liu,
   [Relative trace formulae toward Bessel and Fourier-Jacobi periods of unitary groups](https://arxiv.org/pdf/1012.4538),
   Sections 2.1–2.2 and Appendix 6, equation (6.1).
   These fix the split Bessel/Whittaker integral coordinates used to check
   the uniformizer in the character. Applying this model requires its
   representation and normalization hypotheses.

6. Andrew R. Booker, M. Krishnamurthy and Min Lee,
   [Test vectors for Rankin-Selberg L-functions](https://arxiv.org/pdf/1903.03458),
   [published paper](https://doi.org/10.1016/j.jnt.2019.08.010), Theorem 1.1
   and Section 3.
   Read as a comparison for the adjacent generic case: selected unipotent
   averages can produce nonzero normalized tests. No theorem here
   transfers that conclusion to the actual higher-gap period.

All listed papers were read as primary mathematical sources. The root
reader reopened the sources used in the report. The finite programs and
proof exposition are newly authored. No third-party Lean implementation,
paper PDF, or repository payload is copied into this package.

## Scope of verification

This is a source-level paper investigation. No complete Lean build,
dependency verification or new proof of the original RH claim was run.
The two finite programs test only PREREG.md. In particular, their successful
finite stabilizer test is not verification of every p-adic flag stratum,
the L2 disintegration argument, or an actual automorphic spectrum.
