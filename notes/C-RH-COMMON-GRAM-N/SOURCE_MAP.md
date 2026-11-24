# Source correspondence and prior work

NON-CANONICAL. C-RH-COMMON-GRAM-N. Candidate-D. No Canon authority.

## Brox's prior centered comparison

The first version of this package omitted the following work by Jose
Brox. The omission affected the stated contribution and the attribution
review. The mathematical statement survived; its positioning did not.
REVIEW.md appends the correction to the historical review.

| Note in JoseBrox/GRH_distillation | First recorded commit | Commit date, Europe/Prague | Relevant content |
| --- | --- | --- | --- |
| notes/frame-degree-compatibility.md | 28fcc17cc06b4ed6dad0e4b2967f877629d11f56 | 2026-11-21 19:03:37 +0100 | Exact rank expansion (1.1)-(1.2), centered inequality (2.1), optimum normalization (3.1), full-interval slope bound (3.2), zero ideal loss and sharp target cut |
| notes/rh-centered-frame-bridge.md | 28fcc17cc06b4ed6dad0e4b2967f877629d11f56 | 2026-11-21 19:03:37 +0100 | Same-map arithmetic bridge and surviving pre-frame error terms |
| notes/one-sided-frame-slope.md | 0016a6bf61ea84b02ccbc35d7182b0bba9521d0b | 2026-11-21 20:44:08 +0100 | One-sided operator and positive-trace alternatives, including restrictions |

Pinned documents:

- [Frame-degree compatibility](https://github.com/JoseBrox/GRH_distillation/blob/28fcc17cc06b4ed6dad0e4b2967f877629d11f56/notes/frame-degree-compatibility.md).
- [Actual RH comparison](https://github.com/JoseBrox/GRH_distillation/blob/28fcc17cc06b4ed6dad0e4b2967f877629d11f56/notes/rh-centered-frame-bridge.md).
- [One-sided comparison](https://github.com/JoseBrox/GRH_distillation/blob/0016a6bf61ea84b02ccbc35d7182b0bba9521d0b/notes/one-sided-frame-slope.md).

The dates are verified Git commit metadata and file-path history, not
independently observed first-publication timestamps. The chronology and
substantive overlap require attribution to this earlier recorded work.

Brox uses the exact centered source defect. With our notation it is
a^2=S*tr(T^2)/M^2-1, and his optimum raw normalization gives
e_*=a^2/(1+a^2). The first version of our note used only the coarser
a^2<=e/(1-e). Its raw-e bound and Brox (3.2) were not uniformly
ordered. PROOF.md now retains a, with the old statement as a corollary.

Relative to these inspected notes, the contribution is the exact
quadratic root f_eta, its capped composition with g_a, and finite Jensen
applied before separate source/target error estimates. This yields a
bound no larger than Brox (3.2) when both are evaluated at identical
a, eta and delta. No analogous ordering is claimed against one-sided
bounds supplied with additional information. The all-real hMle/hfilt
audit below, elementary bound (8), and spectral example are separately
scoped supporting work. We make no broader priority assertion.

## Pinned Lean mathematical source

Repository: https://github.com/leanprover-community/riemann-hypothesis
Commit: 40e56bab026552e089d7afcfeff08d2defb9c005.

| Path under src/ | Git blob | Role |
| --- | --- | --- |
| Formalism/HarderNarasimhan/StatementFrameF.lean | 3f17f6e4ae975f00dbeafdc3fb9e8b66f8c60c1d | Exact hypotheses and conclusions of FrameLA1 and TheoremFSharp |
| Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean | 7b95526eb3a09eb56d7d5536a495bc37ff542f0f | Original trace/HS proof and final coarse scalar bound |
| Formalism/HarderNarasimhan/HarderNarasimhanProofs/TheoremFSharp.lean | a8f8c3bf7560fbab8302f3127fcaf0f5d9eacff8 | Actual HN subspaces, row projection and integration |

[StatementFrameF](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/StatementFrameF.lean)
contains FrameLA1 and TheoremFSharp. The latter has no log(card I) term.

[FrameLinearAlgebraFirst](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean)
already derives a sqrt(e*r) term before weakening it. The
Hilbert-Schmidt method is classical. Brox subsequently retains its
centered form; our note refines the resulting scalar comparison.

All cited code and external prose remain at their source repositories.
The paper derivation is authored for this package under the
repository's Apache-2.0 terms.

## Exact transition in TheoremFSharp

[TheoremFSharp](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/TheoremFSharp.lean)
contains these obligations.

| Source item | Use here |
| --- | --- |
| thmF_place | Arbitrary source subspaces and full rows followed by projection |
| hNτ and hT rank identities | Coordinate changes preserve field ranks |
| hSdim, hPS, hkerP | Projection cannot increase absolute missing dimension |
| θ, Nt, hrkNt, hfilt in theoremFSharp_of | Exact source count for every real threshold |
| hx/hs and hmax | Adjusted source mean at least s and maximum at most s+U |
| hMle: forall tau, M tau <= St tau | Image inclusion with no sign condition on tau |
| hrkM and hcnt rank/count identity | Target low-slope fraction is bounded by image corank |
| hlow | Target slopes are at least s-H |
| hmean | Their weighted mean equals the target muDef |

The tau>=0 restriction occurs in thmF_share and its coarse use in
hcor, which bounds the discarded source fraction by U/(U+tau).
The helper hfilt is nested inside hcor, but its count proof does not
use the sign assumption. A Lean port must extract that identity with
an all-real statement. The comparison uses tau in [-U,H].

The source uses continuity of a smooth envelope in its integration.
Our empirical distributions are finite step functions. A Lean port
needs a finite-weight Jensen/integration lemma and cannot silently
reuse the earlier continuity hypothesis.

The source threshold is
(x+h_i-slopeNormalisingConstant(K))/2. The factor two is already
included in the adjusted squared-norm slope convention; the field
degree cancels from normalized rank counts. No extra factor or
log(card I) term is introduced.

## Other working expositions

Michael O. Rubinstein's working draft, version 2, 22 November 2026:
https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf

Section III.8 describes the frame inputs. Section III.11, Proposition
M7, equations (III.336)-(III.347), decomposes the error into K0, LoP,
MLo and the contribution imported from the mean-slope lemma. Calling
the latter a "frame-comparison penalty" is OUR interpretation of the
decomposition, not a quoted term or label from Rubinstein's text.
Equations (III.357)-(III.359) exhibit x/m, xm/k, m and k/n^2 in
the normalized bookkeeping. Brox's pinned bridge gives the more
explicit argument that all four shapes have pre-frame contributions.

This working exposition supplies no independent proof here of its
imported arithmetic hypotheses. The replacement theorem rests on
the pinned Lean interface and the explicit derivation above.

The related preprint is
[Three simplifications in the Alpoge-Claude argument for Dirichlet GRH](https://hexagonmath.org/2611.00828v1),
version 1, 21 November 2026. Its integrated rank-loss proposition
provides the chord estimate
E min(H,(s-alpha)_+)<=UH/(U+H). PROOF.md section 9 now includes a
direct proof, and uses it to justify the below-s comparator. Brox,
rather than this package, already covers full-interval comparison.

## Public project scope

Public Canon v116 at main 93c36089db57032a6cbca482ff62c95884567d0f
was reconfirmed unchanged. Authority and release checks were previously
verified and read again where needed, not rerun as scientific evidence.

The original public collision scan preceded issue #2065. Issues
#1939, #1941 and #1944 concern other Nyman-Beurling carriers. This
correction remains within the same proof-only note and preserves its
frozen PREREG.md. The external attribution search was incomplete;
that fact is not concealed by the successful project collision scan.

No new semistability, common-algebra, rapidity or physical candidate
is opened here. No Canon claim or status is altered.
