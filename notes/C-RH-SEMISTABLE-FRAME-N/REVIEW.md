# Same-session development and opposition record

NON-CANONICAL. No authority. Candidate-D deductions and one-lane candidate-C
audit only. No external reviewer was available for this round.

## Team and separation

The requested team was scheduled in stages because only four agents could
run simultaneously. The development side comprised the root, one additional
Astra, and two Sol agents. The opposition side comprised an Astra and three
Sol agents. All worked under the root's single claimed item, issue 2070.

| Role | Work and contribution |
|---|---|
| Root Astra | Source/authority validation, kernel and rank formulation, synthesis, final source bridge and code/output review |
| Development Astra | Common N, raw seed injectivity, rational character conjugacy, period factorization |
| Development Sol, balance | One-prime source regularity and target counting route |
| Development Sol, rank | Paper rank/certificate review and frozen verify.py |
| Opposition Astra | Frame lifts, factor count, conjugacy signs, L2-domain repair, PMat/SIso/counting identification, certificate |
| Opposition Sol, seeds | Independent paper challenge of raw seed injectivity and averaging counterexample |
| Opposition Sol, balance | Torsion proof, lift-character normalization, admissible projectors, counting premises, sharp total variation |
| Opposition Sol, finite audit | Blind break.py from the frozen contract; no verify.py access before freezing |

Paper exchanges were adversarial but shared within one research session.
Only the finite-program separation was blind. No agent is characterized as
an external independent reviewer. Neither program was used as the other
agent's verification implementation.

## Objections and dispositions

1. **Missing residue factors.** The full frame-fixed group has f factors
   above each rational prime, hence 2f factors in total. Corrected.
2. **A finite quotient action might be projective.** Retained-prime
   character phases are removed by controlled lifts or explicit untwisting.
   Added to the source-regularity proof.
3. **Source freeness used an unnecessarily large dimension.** A local
   split-prime torsion argument gives the sufficient threshold g_i-1>k.
   The standing inequalities imply it at either prime.
4. **Only an upper trace bound?** Re-reading found le_dc_of_conC as well as
   dc_le_of_conC. Both are used, subject to the actual counting premises.
5. **Full ambient centrality.** The narrower PCount wrapper requires it;
   the universal PointsLemma uses IsAdmIdem instead. The argument explicitly
   takes the latter route and retains CountData and its analytic premises.
6. **Two marginals do not determine a joint distribution.** Accepted.
   Only one-prime decompositions are claimed. The fixed counterexample has
   identical marginals and joint total variation 1/2.
7. **Zero seed does not immediately imply zero column.** Added the
   spanning argument and the final column-covariance step.
8. **L2 evaluation on a fixed orbit is not well defined.** Accepted and
   repaired. The common Fourier-kernel statement uses L2_loc, absolute
   unfolding and fiber integration. Pointwise period formulas retain their
   representative/evaluation assumptions.
9. **Good-row EE is not full HH.** Accepted. The actual source constructs
   PMat on full HH, extends its good-row basis, and uses PMat as Bf.
   A fixed SIso transports the full maps. Arbitrary MatS witnesses are
   explicitly excluded from that conclusion.
10. **Counted spectral dimension could differ by an archimedean factor.**
    RowsBij and finrank_HH_eq_Dcount give exact equality for the same
    realization and replacement projector. Its hypotheses remain explicit.
11. **A determinant only proves zero defect.** The quantitative rank
    certificate bounds every positive defect. Its normalization was checked
    independently; the classical noncommutative rank equivalence is credited.
12. **Post-run output labels were too broad.** Root found that 615/146
    describe local reduced block conditions, not global zero defect.
    RESULTS.md records the erratum. Frozen code/output were not changed.

## What survived, and what remains open

The paper arguments in PROOF.md are recorded as candidate-D after these
same-session challenges. The actual-map application is conditional on a
concrete Hida realization, SIso, the chosen PMat witness, and the stated
replacement-projector counting hypotheses. No Lean verification was run.

The final synthesis at local commit 954c3c70 received another read-only
review by the opposition Astra and the development source/balance authors.
No blocking mathematical objection was raised. Their precision edits were
incorporated: Bf versus Ball, the reference word for the Fourier character,
the weighted intrinsic-defect sum, zero-dimensional columns, the
pre-character level for intertwining, the complement of all hyperbolic
pairs, and the exact scope of representative hypotheses.

The blind finite audit passes its frozen assertions on both implementations.
It does not validate the automorphic realization or its analytic hypotheses.

No bound on the actual intrinsic period-rank defects or the common
Fourier-blind kernel has been obtained. A tentative full joint source
distribution argument proposed during development is not part of the
accepted results, because it did not receive the same completed review.
