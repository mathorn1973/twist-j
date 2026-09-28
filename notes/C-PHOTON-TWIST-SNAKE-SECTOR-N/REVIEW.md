# Pre-execution analytical and static review

**PUBLIC / NON-CANONICAL. Review of the prospective #1265 candidate.**

This is a review pass by assistant agents in the same working session,
not independent confirmation by another human author. It reviews
PROOF.md, PREREG.md, sample.cpp, analyze.py, run_snake.py, run_analysis.py
and test_analyze.py before their public execution pin. Within the pre-pin
rule of PREREG.md the reviewers compiled the sampler, ran `--audit`, ran
`test_analyze.py` from copies, ran exact enumeration checks of the
identities on small product spaces, ran the tiny audit schedule of every
kind through `analyze.read_run`, and ran single-point mutants of the
sampler through the audit. No declared sampling job
(`sample L k chain kind`) was executed for this review, with any
argument. Compilation, the audit, the mutants and the synthetic tests are
implementation evidence, not scientific execution evidence. The declared
basis (Public Canon v92, the merge of #1260) is the head of the public
main checkout read for this review.

## Mathematical review

PROOF.md (1)-(3): W_n and the classes are integers; (2) holds because only
the source of q_n changes between twists n and n+1. The class-preserving
reset was checked for every W_n at and away from the boundary and both
parities of n: the reset field lies in C_c(n+1) with w_n = 0 or -1, W_n is
unchanged, and no 01 plaquette of another slice is touched. Section 2's
restricted single-link law is the heat-bath law with class-leaving
candidates removed; it is a Gibbs update of nu_n^{(c)} (stationarity and
detailed balance) and the current value is always allowed, so the
normaliser is positive. Irreducibility is stated as an assumption, not
proved, and the design probes it with the twist-L^2 chains started in the
class layouts.

(6), (7): F/PB = PF/Bw = Q_{n+1}^{(c)}/Q_n^{(c)} and F/Bw = (A/B) r_n were
verified by exact enumeration on two toy product spaces with the same
slice-sum and class structure (3 slices x 3 links and 4 slices x 2 links,
k = 1, 2, 5^9 and 5^8 fields) at every n and both classes to 2e-16; F/Bw
deviates from r_n by 41 to 78 percent there. (8): the conditional law at
twist n for a boundary link of q_n carries no indicator (W_n does not
depend on that link), 1_{C_c(n)} does not depend on it at twist n+1, the
lambda_{B^w} denominator is positive on C_c(n+1), and the three
conditional forms average to (6) exactly; the sampler's
`forward_indicator`, `reverse_indicator` and `local_ratio` implement (8)
as written, and the audit's 1312 restricted local enumerations confirm
both pairings to 1e-12 on the lattice itself, with 10 enumerations in
which the indicator takes both values. (9), (10): the sum rule and class
weights follow from telescoping (7) inside a fixed class; the
delta-method standard errors of `class_sum` agree with central finite
differences to 1e-6 at several points including pi_1(-) = 0 and 1.
Section 5 (control endpoints) is bookkeeping only. One wording defect was
corrected: F, B^w and their conditional forms lie in [0, max rho_n], not
within the two-sided bounds of the unconstrained estimators, since the
indicator can vanish.

## Static implementation and protocol review

- Sampler: slice sums and W are maintained incrementally in the sweep and
  the twist step (both directions, correct order of operations) and
  compared with direct recomputation every sweep; `slice_change`,
  `twisted_link`, `restricted_cdf` (renormalised, cumulative ending
  exactly at 1.0, forbidden candidates never selected), the indicators,
  both `local_ratio` branches, `force_slice`, every declared initial
  state, the five schedules, header metadata, `run()` validation and
  seeds were read against PROOF.md and PREREG.md and found consistent.
  Mutants of `forward_indicator` (unshifted flux) and `reverse_indicator`
  (W_{n+1} instead of W_{n+1} - w_n) fail the audit; a leaking restricted
  kernel fails the 6976 direct-class law checks and the per-sweep class
  validation. Three audit gaps found by the review were closed before the
  pin: the post-reset sweep count was unobservable (every chain now prints
  its sweep total, the schedule exercise checks it against the schedule
  formula and the analyzer requires it as metadata); a reset touching a
  neighbouring slice was invisible on the all-zero layouts (the reset is
  now also checked on the fixed link pattern at twist n+1, requiring every
  link outside the 0- and 1-links of slice n unchanged); the indicator-1
  histogram bookkeeping was untested (the restricted sweep exercise now
  feeds every sweep to a scratch recorder and requires the histograms to
  follow the two indicators).
- Analyzer: manifest, byte counts, hashes, exit codes, empty stderr, audit
  transcript and environment are checked before any row is used; exits
  124 and 127 give INCOMPLETE only; every other defect gives
  FAIL_IMPLEMENTATION for all groups. Every `read_run` requirement was
  checked against the real output of every kind and chain produced with
  the audit's tiny schedule (all files accepted). Two statistical defects
  found by the review were corrected: the two-block-scale rule first
  applied to every statistic of a restricted ladder, which bounds the G7
  ratio by sqrt 2 so that G7 could never fire and the ladder-sum SE was
  blind to correlation beyond 1024 sweeps (the rule now applies only to
  the within-chain pooled variances of the G3 subsets, which have no
  degrees of freedom at 2048 sweeps; the aggregate SE, deficit, G6 and G7
  keep all three scales, and the null rates by L are stated in PREREG.md);
  and a zero mean of a restricted estimator in one chain alone raised a
  custody failure of the whole run (it is now a named equilibration
  failure of that chain, with a fixture). G6 is now also read for a
  ladder with a zero pooled mean elsewhere. G11 is read only when the
  class-sum route has fired none of its own gates. Degrees of freedom of
  every within-group variance used (P four chains x 64 blocks, restricted
  ladder two chains x 4 blocks at 512 and 1024, endpoint dwells three
  chains x 64 blocks, U as consumed) were checked. The control groups are
  read as one implementation check (any qualified failing group taints
  every main group; no qualified group caps every main group), because
  their sources 2k and 3k are unrelated to the sector structure of mode
  k; the per-chain control sums are reported. Two agreement comparisons
  of bitwise-identical constant blocks differed by one unit in the last
  place; `agree` carries a 1e-12 relative term for that case.
- Controller and wrapper: audit first with its own timeout, then the 136
  jobs largest-L first (U, C0, CM, P, control within an L) on four
  workers, outcomes and hashes preserved incrementally, no retry, fresh
  output directory, SHA256SUMS; the wrapper refuses to overwrite, records
  the analyzer's own process outcome and writes SHA256SUMS_FINAL. Stems
  and job list are identical between controller and analyzer. A stub
  executable was run through both to check the plumbing. Measured
  throughput at L=10 (1.7-1.9 ms per unrestricted sweep, 3.0 ms per
  restricted sweep at half twist, up to 5.4 ms fully twisted) gives a
  worst-case restricted job of about 1100 s against the 2400 s timeout.
- `python3 test_analyze.py` passes every fixture route and gate case on
  the frozen files, including the static check that the sampler's header
  literal, metadata keys, seed base and field count agree with the
  analyzer.

## Pre-pin history

PREREG.md requires disclosure of every pre-pin audit failure. According
to the session record: (i) the first audit run failed in the restricted
law check because `restricted_cdf`, called directly on a 0/1-link of an
untwisted slice, applied the slice change of that link although W does
not involve untwisted slices; the function now treats such links as
unrestricted (the production sweep never called it for them). (ii) The
second run failed in a restricted local enumeration whose higher-twist
class was empty over all 625 assignments; the audit now requires every
forward estimator to vanish in that case instead of forming a ratio.
(iii) The third run failed because the audit required w_0 = -1 of the hot
class-minus initial state, which is reset to the alternative layout only
when the drawn field lies outside the class; the check now requires class
membership (and w_0 = -1 for the cold start). (iv) After the review's
audit strengthening, one run failed because the reset check on the fixed
pattern was built at twist n instead of n+1, where the alternative layout
has w = 0; the fixture is now built at twist n+1. No production entry
point was invoked at any time. Analyzer defects found by the synthetic
tests before the review: the coarsening gate fired on fabricated
independent blocks at the 3 percent level with 64-block dwells (the P
group now has four chains and the P and restricted endpoint dwells 32768
sweeps), the within-chain pooled variance of a two-chain single-visit
ladder had no degrees of freedom at 2048 sweeps, and the agreement test
on constant blocks failed by roundoff. Test-generator defects (a fixture
whose lowered reverse indicator also broke naive-conditional consistency,
a hard-coded seam size, assertions on volumes that were not built, a
fixture with an inconsistent W range) were corrected in the generator,
not in the analyzer. A design critique before implementation found that
the first specification paired F with Bw, which is not exact, and that
the first seed formula reproduced every consumed job; both were corrected
before any code existed, together with the self-contained step-zero
group, the twist-L^2 class chains, the 512 post-reset sweeps and the
block extremes of W.

## Disposition and remaining review

No blocking mathematical or static protocol error remains in the
reviewed candidate. This permits freezing the prospective engineering
attempt; it does not certify finite-precision correctness, successful
execution, equilibration, irreducibility of the restricted kernel,
independence of observations, coverage of the empirical intervals or the
weight of any class. The written identities retain a candidate-T ceiling.
The numerical attempt has ZERO scientific evidential weight under its
preregistration and cannot close P1, decide a phase or promote a Canon
claim. There is no post-run review in this file. The exact public pin,
first invocation, preserved outputs, failures and diagnostic disposition
must be recorded separately after execution and must not be used to
rewrite PREREG.md or this pre-execution review.
