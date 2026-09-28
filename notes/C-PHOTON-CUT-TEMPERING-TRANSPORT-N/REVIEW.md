# Prospective independent assistant review

**PUBLIC / NON-CANONICAL. Static review before the first execution.**

Item: C-PHOTON-CUT-TEMPERING-TRANSPORT-N, issue #1261.
Reviewer: a separate delegated assistant in the same session, distinct from
the proof, sampler, analyzer and controller authors. This is not independent
confirmation by another human or an executed reproduction.

Reviewed PROOF.md, PREREG.md, sample.cpp, analyze.py, test_analyze.py and
run_pilot.py, together with the consumed endpoint and snake proof packages.
No sampler, audit, analyzer or analyzer fixture was executed for this review.
The authors report syntax/compilation checks only before pinning. The
prospective verdict is **READY TO FREEZE**, within the limited scope below.

## Mathematical target and kernel

The cut contains the complete seam, so the bulk action is independent of
the endpoint bit. At lambda=1 the target is the pair of unnormalized native
weights divided by Z_0+Z_k. It is not the equal mixture of the two separately
normalized endpoints. At lambda=0 only the cut factors disappear; no
uniformity or independence of the remaining link measure is assumed.

The coherent sheet cochain changes the 01 flux with plus sign at x1=j and
minus sign at x1=j-1. The 02 and 03 differences cancel over the complete
transverse sheet; all changed plaquettes are inside the cut. The five-state
orbit heat bath therefore has precisely the displayed cut-weight ratio,
is reversible within its orbit, and becomes uniform at lambda=0. The
alternative start has winding minus the sign of the represented source
for each of the four declared (k,base) groups.

Single-link conditionals use exponent lambda only on cut plaquettes. The
lazy endpoint ratio is exp(lambda times the cut-score difference). Replica
exchange uses (lambda_left-lambda_right) times
(cut_score_right-cut_score_left); the two bulk actions cancel. Their fixed
composition preserves the product law without requiring the full sweep to
be reversible. Positive conditional assignments and the lazy endpoint
choice justify the stated finite-state irreducibility and aperiodicity;
they provide no useful mixing-time bound.

The derivative sign was independently checked: i C_k=-R_k E Y, hence
C_k=i R_k E Y. The positive and negative parts in the reported signed
contrast have one common full-pair denominator. They are parts of the dual
score, not a derived distribution of original surface-flux signs. For the
control pair the involution (s,alpha) -> (1-s,-alpha) preserves every
tempered law and reverses Y and integer slice winding. Its population
endpoint masses are equal. Neither this involution nor the control's
normalizer is substituted for the main-pair law.

The additional old whole-volume beta=0 calculation was checked separately:
distinct plaquette curls are pairwise independent uniform F_5 variables
because their boundary rows are nonproportional. The five log weights give
variance 16(log 2)^2/25+16(log phi)^2/5 per plaquette and hence 6L^4 times
that variance in total. The note correctly does not transfer this
uniform-link argument to the new bulk-weighted cut ensemble or turn it
into an acceptance or mixing theorem.

## Implementation and prospective analysis

The sampler's direct curl, signed incidences and reordered cut-factor
lookup agree. Evenness of W justifies the signed-staple lookup despite
the source. Native and cut scores change together for endpoint and sheet
updates; full states and their traveling labels move together in exchanges.
Every production observation comes from the fixed lambda=1 slot. The
round-trip state resets at production and counts complete low-high-low
traversals. No state is accepted or rejected according to the observed
sign of Y or its winding branch.

The declared audit compares isolated-link and coherent-sheet changes with
direct curls, checks the conditional and exchange ratios, validates actual
local and sheet sweeps on deterministic fixtures, tests control reversal,
and requires deliberately corrupted caches to be rejected. These checks
remain prospective and use floating arithmetic; an eventual PASS is an
implementation check, not exact scientific evidence.

The analyzer preserves signed means and both nonnegative parts, validates
custody, budgets, seeds and arithmetic relations, and requires all four
groups to pass mobility before applying stationary control identities.
Leave-one-chain-out comparisons avoid comparing a chain to a pool
containing itself. Half comparisons and pooled coarsening comparisons use
the four preregistered scales. A zero winding error does not force a
possibly negligible branch to appear; zero core errors remain unresolved.

Two review findings were corrected before the pin:

1. Pooled batch errors initially included dispersion between chain means.
   The final formula centers batch residuals separately within each chain
   and combines their sample variances. The separate error from chain
   means remains descriptive and cannot enlarge the error used by the
   agreement gates. A prospective fixture uses incompatible constant chain
   means to check this distinction.
2. The analyzer now refuses unexpected stdout tables, including tables not
   listed in the execution manifest. Temporary mutation fixtures are
   removed after inspection so they do not contaminate later custody tests.

The prospective fixtures also cover gate precedence, a shifted exact
control, separated starts, missing jobs, malformed seed/nonfinite/sign
records, wrong custody hashes, and the joint-residual ratio calculation.
Their invented sufficient sums are explicitly not lattice observations.
No fixture result is claimed here.

The controller creates a new output directory, permits one audit and one
fixture invocation, declares twenty jobs with fixed limits, never retries
and invokes the analyzer once after production even if a job fails. It
captures analyzer exit code, stderr and hashes separately, addressing the
missing analyzer return-code record in the old endpoint attempt. Failure
before production prevents production and preserves the attempted output.
The formal run record must still state the actual environment, compiler,
command, pin and observed return codes; this review supplies none of those
future observations.

## Scope and publication boundary

The pin must contain all seven declared files, be pushed and publicly read
back before the first audit, fixture or sampler invocation. The consumed
#1249 and #1259 outcomes stay unchanged. Every failure of this attempt must
be preserved without a retry or a changed threshold; a successor needs a
new identifier and pin.

Even TRANSPORT_QUALIFIED would mean only that the declared finite L=4
engineering diagnostics passed. Neither the empirical four-SE comparisons
nor their agreement provide rigorous coverage or establish equilibrium.
The signed quantities remain NONINFERENTIAL_ESTIMATE; no squared contrast
interval, phase verdict, thermodynamic lower bound or P1 closure is formed.
The complete finite identities have candidate-T scope after review; all
floating outputs have ZERO scientific evidential weight. Public Canon v92
and the original lower-bound obligation remain unchanged.
