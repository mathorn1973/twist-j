# Review record

NON-CANONICAL. Candidate-D. No Canon authority.

Reviewed mathematical pin:
`48461bb2d9667da6284b2d220dfcb9e03743de94`.

The reviews below were carried out by separate agents reading the pinned
Git contents and the original mathematical source. They were exposed to
the formulas and research discussions. This is independent source-exposed
mathematical review, not blind two-agent computational confirmation.
The root subsequently inserted the explanatory scalar step requested in
section 9; no statement, domain, threshold or conclusion was changed.

## Astra: mathematical and source transition review

Verdict: approve at candidate-D, within the stated paper scope.

Checked source/target normalization, all-real source thresholds, the
all-real image inclusion, the row-projection factor, finite-step
integration, endpoints, equation (8), and the ideal-frame consequence.
No mathematical gap was identified. The correspondence retains the
realification factor 2 and field degree in the intermediate counts and
cancels them only after normalization.

Requested explanatory addition: state f_eta(p)<=2p+eta explicitly when
comparing the new loss to the earlier simpler bound. For z=f_eta(p),
z<=p+sqrt(eta*z)<=p+(eta+z)/2 proves it. This has been included.

## Sol 1: independent breaker and written-proof review

Verdict: approve at candidate-D, within the stated paper scope.

Independently derived the trace-fraction and target-block inequalities
before the final written proof. Checked all positive-semidefinite steps,
root inversion, monotonicity and concavity, CDF direction, strict endpoint
conventions, all boundary cases, explicit error bound (8), comparisons
and both spectral counterexamples. No blocking defect was identified.

Confirmed that equation (8) retains the term delta*U after subtraction
of U, and that integration above the old threshold produces a saving of
exactly U*(1-Phi(U/(H+U))).

## Sol 2: source, attribution and scope review

Verdict: approve without required corrections.

Confirmed all three upstream Git blob IDs. Checked that the nonnegative
tau restriction belongs to the old envelope estimate and not to the exact
rank identities or image inclusion. Confirmed correct attribution of the
previous below-threshold integration and of the classical HS method.
Checked absence of a global exponent claim, Canon promotion, physical
carrier identification or private operational material.

## What this record establishes

The package has a written derivation reviewed for mathematical validity
and source fit. It does not contain a new Lean verification receipt,
numerical experiment, finite exact audit, independent architecture run,
or a replay of the full RH proof. Source hashes and Git checks are only
administrative integrity checks. Candidate-D is retained conservatively.


## Appended erratum and correction review, 23 November 2026

The historical reviews above are retained verbatim. Their mathematical
checks do not establish completeness of the prior-work search.

The external review at
https://github.com/mathorn1973/twist-j/pull/2067#issuecomment-7101645879
examined published head f9a864ddc9b9ffd422d2197e3f74454fc6036d8f.
It found no mathematical error, but identified substantive earlier
work by Jose Brox that this package and its attribution review missed.
The authoring session accepts that objection. In particular, the
earlier Sol 2 verdict about attribution was incomplete.

### Accepted corrections

1. Brox's three notes are now cited with full commit identifiers and
   recorded dates in SOURCE_MAP.md. Centered projections, invariant
   normalization, full-interval integration, the ideal zero-loss case,
   and the actual-source bridge are attributed to that earlier work.
   The contribution is narrowed to the exact quadratic envelope and
   finite Jensen composition, the pinned all-threshold audit, elementary
   bound (8), and the minor spectral counterexample.
2. The main statement now retains the exact centered defect a.
   It distinguishes actual raw error from an upper bound and proves
   the original raw-e formula as a corollary. Comparison to Brox (3.2)
   uses identical a, eta and delta on both sides; it does not cover
   stronger one-sided data. The frozen PREREG.md is unchanged.
3. Section 9 proves the chord bound and the below-s comparator.
4. Rubinstein's "frame-comparison penalty" is explicitly identified
   as this package's interpretation, not a quotation from his draft.
5. The Lean-port obligation now explicitly includes extraction of the
   all-real hfilt identity as well as finite-step Jensen/integration.

The reviewer's finite tests are reported in the external comment.
Their programs are not in this branch and were not run by this
authoring session. This correction adopts no new computation receipt,
architecture result, or computational status from that report.

### Source-exposed review of the correction

Reviewed corrected PROOF.md Git blob:
5a77b839cb28dbbac614e678bb77f06e8098761c.

Astra mathematical review: APPROVE at candidate-D. Checked the exact
a/e_act/e distinction, concavity, endpoint cases, the finite real-weight
CDF extremizer, like-for-like comparison, the chord argument, bound (8),
and its original-theorem corollary. Two requested wording corrections
were included: U*z<=U*H handles U=0 without division, and the field-degree
rank cancellation is distinguished from the squared-norm factor two
already included in the source threshold.

Sol attribution/scope review: APPROVE after the README wording fix.
Read the three Brox notes and their recorded history, and checked the
corrected PROOF, SOURCE_MAP, README and promotion handoff. Confirmed
that commit dates are not represented as independently observed first
public-visibility times, and that no ordering against Brox's extra-input
one-sided bounds is claimed. The README now states the nonzero-width
condition and its separate zero-width case.

These are exposed paper/source reviews of the correction. They do not
constitute blind computational confirmation or a Lean verification.
Status remains NON-CANONICAL, candidate-D.
