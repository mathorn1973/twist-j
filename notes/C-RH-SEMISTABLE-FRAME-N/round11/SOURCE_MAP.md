# Round 11 source map

**NON-CANONICAL. No authority. No Canon status change.**

This is a paper investigation. A source declaration identifies an input or
a supplied construction; reading it is not a Lean build and does not prove
that every abstract data package has the genuine geometric realization.
All deductions in PROOF.md retain their named hypotheses.

## 1. Public basis and immutable mathematical source

On 2026-11-23 the public authority was read at main
93c36089db57032a6cbca482ff62c95884567d0f, Public Canon v116.
Its declared content commit is 0b6ae8e23d7086715b908cce6e1755d2898f55fc.
The annotated tag object bf514bdd92d711c10131bebb8ba2b678e999d72d
dereferenced to that main. Content ancestry, all five normative file
hashes and byte counts, and successful exact-main checks were verified.
The architecture check runs 136930733692 and 136930733975 and aggregate
136931056530 succeeded; publication checks 136931466606 and 136932523158
also succeeded. This authenticates the public basis, not this new note.

Before delivery, main had advanced to
420b39ac7d6f4d8c8a2779fea3944f5cd6d9db20. Work paused for a fresh
STATUS-first authority check. STATUS, POLICY, AGENTS and every normative
file were compared byte for byte and are unchanged; the declared content
and tag target remain ancestors. The changes concern separate notes and
a separate probe, with no collision with this item. On the new exact main,
architecture checks 138017496568 and 138017497222 and aggregate
138018134920 succeeded. This revalidates the authority basis without
rebasing or changing any frozen scientific history.

The mathematical pin remains
[40e56bab026552e089d7afcfeff08d2defb9c005](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005).
The inherited round 10 delivery is
bb90f8bd2769b951c73a33be4e4d0acaf9f6b5ec, tree
42b479e0e3e09b5a26d2b0456e4c74b18bb3316a.

The complete remote-head inventory, recent open issues, relevant existing
RH branches and the registry were inspected before round 11 editing.
The round 11 paper scope was claimed in issue #2070 before editing.
This is the same candidate and draft PR #2071. The centered-frame
issue #2065 / PR #2067 remains a separate owned item.

## 2. Exact source correspondences

All links below use the immutable mathematical pin above.

| Proof input | Source location and exact role |
|---|---|
| Ambient ranks and field degree | [Params.lean, 6-40](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalRingCardinality/Params.lean#L6-L40): k,m even, m>=2, k>=m+3, f>=m; n_G=k+m-1 and r_S=m/2-1. The genuine field realization identifies f with the real degree. In particular r_S=0 is allowed. |
| Actual odd-hook character | [HidaSetting.lean, 23-44 and 103-116](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L103-L116), with the norm/pairing fields at 207-226. Round 10 derives the split matrix A and ell(z)=-T_u. Section 2 identifies its neutral pair; it is not merely a dimension comparison. |
| lamS and the definition of IsDS | [RelevantZeroGramTerms.lean, 72-76 and 159-167](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean#L159-L167). IsDS specifies unitary irreducibility, square integrability and the Vogan-minimal K-type; the Harish-Chandra normalization is proved separately. |
| Minimal K-type weight | [StatementDS.lean, 11-14](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/FormalDegreeBessel/StatementDS.lean#L11-L14). The formula is lambda+rho_noncompact-rho_compact, not lambda itself. |
| Every adjacent gap, including the join | [row_parameter_gaps_large, 1347-1391](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/StandingHypothesesHoldFamily.lean#L1347-L1391). Its ParameterChoice' assumption yields C_l k m^4+n_G m^10 < lambda_i-lambda_(i+1) whenever C_l<=P.Cgap. Choosing C_l=0 proves every gap exceeds one. The join is treated at 1373-1384. |
| Parameter-family supplier | [StandingHypothesesHoldFamily.lean, 1602-1629](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/StandingHypothesesHoldFamily.lean#L1602-L1629). Fm.params provides the choice once x>Fm.x1. Using the gap lemma does not require the additional residual assumptions of the subsequent full standing-hypotheses theorem. |
| Alternative explicit gap assumption | [StandingNumericalData.lean, 106-136](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/StandingNumericalData.lean#L106-L136), especially 133-136. The gap belongs to StandingHypotheses, not the preceding structure StandingNumericalData. |
| Concrete archimedean data and convolution | [HidaSetting.lean, 193-205](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L193-L205). pl_infty, n_eq, lam_eq and the discrete-series/minimal-type fields identify the actual infinity representation; Rph and Rph_spec specify the bounded convolution. |
| Full target rather than a selected finite subspace | [RowsDef.lean, 19-20, 49-81 and 129-131](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/RowsDef.lean#L19-L81). HH is the entire range of Re.comp T on automorphic L2. RowsBij and RowsFinDim are named propositions/interfaces, whose actual suppliers remain required. Defining them alone does not prove them. |
| Actual HHX and P_u | [PoincareInHH.lean, 185-210](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/PoincareInHH.lean#L185-L210). HHX at 206 is the concrete HHB. |
| Finite full range and fixed abstract/concrete transport | [ParametersTermRelations.lean, 170-175, 247-248 and 286-323](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ParametersTermRelations.lean#L286-L323). FinX.finHH concerns the full HHX; sOf.HH identifies that target. SConc supplies the Hida setting, full data, FinX, seed integrability and SIso. One fixed genuine realization is retained throughout. |
| Actual selected periods and global-kernel inclusion | The [round 10 source map](../round10/SOURCE_MAP.md) retains the absolute unfolding, common rational-type conjugacy, Pu_eq, actual column vector, row translate and outer integral. Round 11 does not remove those hypotheses. |

## 3. Fresh external-main comparison

The live external main was read at
[90cc2e125ba4b6ca10be17d918857800ba6c39cc](https://github.com/leanprover-community/riemann-hypothesis/commit/90cc2e125ba4b6ca10be17d918857800ba6c39cc),
timestamp 2026-11-23T20:59:51Z. The latest commit concerns the batch queue.
The following selected source comparisons were performed by reading both
complete files. Their unchanged declarations were not inferred from that
commit message.

| File | Pinned blob | Live blob | Result |
|---|---|---|---|
| RowsDef.lean | 713c562806ba024c53e9545072004dc59435091e | f0f45e752ec9fdbee9651b61f7c4aafcd4e874c9 | HH, RowsBij and RowsFinDim definitions unchanged; whole files differ. |
| StandingHypothesesHoldFamily.lean | ceb0d69e48222f5f0cfcc8e9db7e58f7a64aa88f | d24e5f72a3aa481dd1cf0c7c0eff6478aadd64da | row_parameter_gaps_large statement and proof unchanged; whole files differ. |

This selected comparison neither compiles nor certifies the entire live
repository. Proof scope and line references remain pinned. The separate
round 10 comparisons are preserved in their original record.

## 4. Primary literature and exact uses

The full references and links are in [PROOF.md](PROOF.md). The root reader
opened the sources supporting the reported conclusions; the two paper
lanes also checked the crucial hypotheses independently.

| Reference | Exact use and limit |
|---|---|
| Gomez-Gourevitch-Sahi, Generalized and degenerate Whittaker models | Definition 2.5.1 and Lemma 2.5.2 identify the neutral model; Theorem E gives orbit-closure nonvanishing for GL_n; Theorem F and Section 4.4 relate the hook to derivatives. Theorem 4.3.1 restates the maximal-orbit theorem of Moeglin-Waldspurger with the dyadic extension. No one-dimensionality claim for every interior hook is used. |
| Zelevinsky, Induced representations II | Theorem 8.1 identifies the highest derivative by segment truncation. For the degree-one height intervals the derivative order is their number. Round 9 supplies the spherical segment description. |
| Bernstein-Zelevinsky, Induced representations I | The smooth orbit-section filtration supports the direct converse in Section 2.4. Exactness of twisted Jacquet, not mere right exactness, is needed. |
| Harris-Kobayashi-Speh, Translation functors and restriction of coherent cohomology | Definition 2.7, equation (2.24), fixes the classical minimal-K-type formula. Section 3.1 recovers the actual Harish-Chandra parameter from the source's specified type. |
| Labesse, Changement de base CM et series discretes | Corollary 5.3, pages 42-43, applies to discrete automorphic unitary representations under condition (*) and the real-degree hypothesis. It gives matching at every unramified or split place and compatible infinity characters. The particular chosen split place needs that stronger matching statement. |
| Shin, On the cohomological base change for unitary similitude groups | Page 2 explicitly records regular highest weight and real degree at least two as the relevant sufficient case for Labesse. We use Labesse for the unitary group; we do not import an extra imaginary-quadratic-subfield assumption from Shin's separate similitude extension. |
| Moeglin-Waldspurger, Le spectre residuel de GL(n) | The classification theorem, pages 605-606, gives the Speh factors of the discrete GL transfer. A nontrivial length forces unit-spaced infinitesimal-character entries. |
| Jacquet-Shalika, On Euler products I | Proposition 2.3, equation (18), pages 518-519, and Corollary 2.5(ii), page 525. The scanned original pages were inspected. The resulting strict one-half annulus is common to all unitary cuspidal factors and excludes cross-factor adjacency; it is weaker than temperedness. |
| Beuzart-Plessis-Chaudouard, Global Gan-Gross-Prasad II | Theorem 1.3.3.1 concerns a given discrete Hermitian pair, central-value nonvanishing and existence on some Hermitian form. Theorem 1.3.6.1 additionally requires an everywhere-tempered cuspidal pair and gives the refined formula for specified factorizable vectors. Neither theorem supplies the required ranks of the selected matrices. |

The full 1987 Moeglin-Waldspurger publisher text was not available in this
review. Its maximal-orbit result is used through the explicit primary
restatement in GGS; the interior-orbit converse is attributed to GGS.

No paper PDF, third-party implementation or external repository payload
is incorporated in this package. These files contain newly written
proofs, source locations and links. No new exact finite execution,
architecture check or Lean verification is claimed.
