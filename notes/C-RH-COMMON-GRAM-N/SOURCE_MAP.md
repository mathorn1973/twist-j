# Source correspondence

NON-CANONICAL. C-RH-COMMON-GRAM-N. Candidate-D. No Canon authority.

## Pinned mathematical source

Repository: https://github.com/leanprover-community/riemann-hypothesis

Commit: `40e56bab026552e089d7afcfeff08d2defb9c005`.

The following source files were read through the GitHub connector. Source
code is not vendored into this note; links identify the inspected statements
and arguments. All proof prose in this package is newly written. The note
uses the repository's Apache-2.0 terms for its own authored contents.

| Path under src/ | Git blob | Role |
| --- | --- | --- |
| Formalism/HarderNarasimhan/StatementFrameF.lean | 3f17f6e4ae975f00dbeafdc3fb9e8b66f8c60c1d | Exact hypotheses and conclusions of FrameLA1 and TheoremFSharp |
| Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean | 7b95526eb3a09eb56d7d5536a495bc37ff542f0f | Original trace/HS proof and its final coarse scalar bound |
| Formalism/HarderNarasimhan/HarderNarasimhanProofs/TheoremFSharp.lean | a8f8c3bf7560fbab8302f3127fcaf0f5d9eacff8 | Actual application to HN subspaces, row projection and layer integration |

[StatementFrameF](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/StatementFrameF.lean)
contains FrameLA1 near its start and TheoremFSharp in its second half.
The latter has no log(card I) term.

[FrameLinearAlgebraFirst](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean)
already derives a term sqrt(e*r) before weakening it. Neither this term nor
the use of a Hilbert-Schmidt second moment is claimed as new here. The note
centers both projections, retains the exact trace fractions, and uses the
full threshold range in the final integration.

## Exact transition in TheoremFSharp

[TheoremFSharp](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/TheoremFSharp.lean)
contains the following obligations and their proofs.

| Source item | Used here |
| --- | --- |
| thmF_place | Arbitrary source subspaces, not only whole-map deletions; full ambient rows followed by projection |
| hNτ and hT rank equalities in thmF_place | Complex coordinate changes preserve the field ranks |
| hSdim, hPS, hkerP | Projection cannot increase absolute missing dimension |
| θ, Nt, hrkNt, hfilt inside theoremFSharp_of | Exact relation between source slope counts and discarded source rank for every real threshold |
| hx/hs and hmax | Adjusted source mean at least s and each adjusted slope at most s+U |
| hMle : forall tau, M tau <= St tau | Every retained image lies in the target HN step; no sign condition on tau |
| hrkM and hcnt's rank-to-count identity | Target low-slope fraction is bounded by the image corank |
| hlow | Target slopes are at least s-H |
| hmean | Their normalized mean is muDef of the target lattice |

The nonnegative-tau restriction appears in `thmF_share` and its use in
`hcor`, which replaces the actual discarded fraction by U/(U+tau). The new
proof does not use that replacement. The helper `hfilt` is written inside
the proof of hcor, but its exact counting argument does not use h_tau.
The new proof uses thresholds tau in [-U,H].

The original source obtains a continuous smooth envelope for integration.
The new empirical distributions are finite step functions. A future Lean
implementation must prove the finite-weight Jensen/integration step; it
must not silently reuse the original continuity hypothesis.

## Related working exposition

Michael O. Rubinstein's working draft, version 2 dated 22 November 2026:
https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf

Section III.8 describes the frame inputs. Section III.11, Proposition M7,
equations (III.336)-(III.347), separates the frame-comparison penalty from
the terms K0, LoP and MLo. Equations (III.357)-(III.359) show the normalized
terms x/m, xm/k, m and k/n^2. In particular K0 already has contributions
of those orders before the frame-comparison penalty is added.

This exposition is a working interpretation, not an additional independent
proof of its imported arithmetic hypotheses. Our source-level theorem
depends on the pinned Lean statements above. No asymptotic improvement of
the total prime-sum error is claimed in this package.

The related three-simplification preprint is
https://hexagonmath.org/2611.00828v1 (21 November 2026).
Its integrated deficit estimate improves the below-threshold input loss.
The present note instead centers both frame estimates and includes the
above-threshold part before comparing the final means.

## Public project scope and collisions

Public Canon v116, main `93c36089db57032a6cbca482ff62c95884567d0f`, was
reconfirmed unchanged from the previously verified release. Required
authority and release checks were read, not rerun for this note.

The remote branches, public issues, probes, notes and registry were checked
before claim #2065. Issues #1939, #1941 and #1944 concern different
Nyman-Beurling approximation carriers. This item does not alter them or
claim an application to any TWIST-J rapidity or physical carrier.
