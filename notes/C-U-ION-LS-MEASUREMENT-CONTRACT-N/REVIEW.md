# Static review

**NON-CANONICAL.** Date: 2026-10-05. This is review of the analytical
measurement-contract note, not an independent scientific execution or a
device validation. Three separate review agents inspected the written
README; the coordinating agent integrated their corrections.

## Mathematical mixture review

The reviewer confirmed the exact equivalence

```text
Hp=g(Zp) on the full simplex
  <=> ker([1^T; Z]) subset ker(H)
  <=> H=c*1^T+A*Z.
```

The proof through normalized positive and negative parts of a signed kernel
vector has the correct domain and requires no regularity. Ordinary quantum
mixture-linearity does not imply this additional mean-sufficiency condition.
The reviewer confirmed the restriction of the affine corollary to the full
checkpoint mixture family and the separate-boundary caveat.

Two wording corrections were incorporated: the two protocols agree at
deterministic checkpoints only if g agrees with f there; nonzero in the
mixture corollary means nonzero on this checkpoint family, not solely outside
it.

## Physical and source review

The reviewer confirmed that the inspected public MODEL specifies symbolic
optical parameters and intensity constraints, but supplies neither a
numerical profile nor a physically selected four-coordinate rule. The
existing CALIBRATION document is a conditional specification, not data.

The Q_z coarse projectors and O_j score observables are valid. The reviewer
confirmed the distinction between their outcome statistics and an instrument
that would protect the archive, and between joint-shot data and calibrated
ensemble phase/mean access. The Watrous chapter sections cited for standard
mixture and measurement definitions were checked.

A domain correction was incorporated: comparing g with f at a response mean
requires an extension of f from its finite spectrum to its convex hull.

## Coherent-domain and genericity review

The reviewer confirmed the code-subspace expectation identity under a
coherent basis mapping and diagonal scored measurement, and the algebraic
genericity argument for unrestricted profiles. Neither statement certifies
an apparatus family or a global all-time Hodge representation.

The reviewer also derived the stronger right-restricted operator-action
identity. It was added with an explicit unitary-extension assumption and
the reminder that diagonal score measurements cannot verify preservation
of coherence. The full-space operator identity remains unclaimed.

## Disposition

Analytical review passed with the above wording/domain clarifications
incorporated. The unresolved profile, detector, decoder, continuation and
statistical inputs remain explicitly unresolved. No scientific program,
calibration experiment, pulse synthesis or public mutation was performed.
The contract is not ready to serve as a completed experimental preregistration.

## Follow-up clarification review

After the user's measurement-continuation comments, the README was expanded
to distinguish common affine coefficients from their uniqueness, identify
the adopted Born probability rule, state the limited streaming/histogram
claim, and specify an instrument and retained classical record for a measured
continuation. The original three-agent review above predates these additions.

One separate review agent read the actual expanded file and confirmed:

- uniqueness of extension coefficients exactly when rank(T)=7;
- empirical averaging without an implied statistical or minimal-record claim;
- valid completely positive instrument maps, their effects and joint output;
- valid same-effect Lueders and measure-prepare examples;
- explicit separation of endpoint copies from one measured continuing device.

The follow-up review passed without a substantive correction. The sample
count is explicitly positive, grouped tests use separate accumulators and
invalid records follow the fixed rule. No new scientific execution occurred.
