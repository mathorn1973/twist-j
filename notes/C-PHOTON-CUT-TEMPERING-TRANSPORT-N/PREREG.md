# Full-measure cut-tempering transport qualification

**PUBLIC / NON-CANONICAL. Floating engineering output has ZERO scientific
evidential weight. Written identities: candidate-T pending separate review.**

- Identifier: C-PHOTON-CUT-TEMPERING-TRANSPORT-N; issue #1261.
- Owner/author: A. M. Thorn, current Codex session.
- Branch/path: `notes/C-PHOTON-CUT-TEMPERING-TRANSPORT-N` and the same
  name under `notes/`.
- Basis: public main `fe64af20c9aae768de8a25576e3316ba0b5bd352`.
- Public Canon v92: tag target `8b1132d828d94f83e653dab34d686a7e68394939`,
  content `d7eb6de16c11f6a105996de02ffd7afa32683a93`; CANON.md has 797365
  bytes and SHA-256
  `31783fcd8e5ad2a697efd92a6d9fb92c2a21c101b95b9c282ea50fa7cb245f68`.
- Authority, tag/content ancestry, both architecture checks and aggregate
  check, relevant issues and explicit remote heads were checked before claim.
- Mathematical scope: finite L6 probability measures. No cross-layer or
  physical interpretation is introduced.

## Why this is a new attempt

The consumed endpoint pilot #1249/#1250 recorded zero complete replica
round trips. The consumed snake pilot #1259/#1260 recorded opposite-sign
branches separated by initialization and failed its exact control. Its
`FAIL_CONSISTENCY` verdict is unchanged. Those observations are known design
inputs, not data of this new qualification. No old run is resumed, extended,
retuned or assigned a new inference.

This attempt first asks whether a different kernel can qualify transport on
L=4. It does not expand automatically to larger volumes. The engineering
numbers cannot prove stationarity, a thermodynamic lower bound, P1, a phase,
or a physical photon claim. No Canon, Registry, Frontier, formal probe,
policy, workflow or release changes belong to this item.

## Fixed measure and kernel

Use the four-torus, W, seam Sigma, Y and native pair measure of PROOF.md.
L=4 only; k in {1,2}; base b in {0,2}; s in {0,1}; source k(b+s)Sigma.
The tempered cut D consists of all 01 plaquettes at x0=0. The replica law
is proportional to exp(S_bulk+lambda S_cut), with native logarithmic weights
outside D. Use 65 replicas lambda_j=j/64, j=0,...,64. The lambda=1 marginal
is exactly the full native pair measure, including its unequal endpoint
weights for b=0. The b=2 pair is an independent reversal control.

Each sweep performs, in order, every single-link conditional heat bath,
all L collective sheet heat baths, a lazy endpoint Metropolis proposal with
probability 1/2 in each replica, and alternating even/odd adjacent exchanges.
The sheet at x1=j adds a in F5 to all 0-links at x0=0,x1=j, uniformly in
(x2,x3); its curl changes two sheets inside D. Its five-state conditional
weights are exact finite orbit weights exp(lambda times the changed cut
score). At lambda=0 this choice is uniform. Swaps use cut scores only.
There is no charge-conjugation symmetrization, selected-sector restriction,
adaptive bias, temperature adaptation or post-selection of trajectories.

Target observations are made after every production sweep at lambda=1.
With I_s indicating the endpoint, report the main signed ratio

    c_k = E[I_1 Y] / E[I_0]
        = (E[I_1 max(Y,0)] - E[I_1 max(-Y,0)]) / E[I_0].

Both terms use the same full-measure denominator. These are the positive
and negative parts of the dual score Y, not a newly identified distribution
of the original surface flux. The identity to the original signed Fourier
contrast is the existing finite-measure identity cited in PROOF.md.
At b=2 this ratio is only an endpoint mean, not c_k; the b=0 second-moment
bound is not asserted for the control pair.

## Fixed starts, budget and custody

Exactly twenty jobs: every (L=4,k=1,2,b=0,2,chain=0,...,4). Every replica
in a job has that chain's declared start. Chains are cold s=0, independent
uniform links s=0, cold s=1, independent uniform links s=1, and alternative
cold s=1. The last has 0-link value 2 sign(q) mod5 at x0=x1=0 for every
(x2,x3), all other links zero, q=rep(k(b+1)) in {-2,...,2}. This produces
winding -sign(q) rather than the cold winding zero.

Seeds: 202609280000 + 10000b + 1000L + 100k + chain; generator mt19937_64
with top-53-bit uniforms and rejection for exact uniform residues. Warmup
2048 sweeps; production 16384; block length 128, hence 128 blocks per job.
The complete integer curl, both cached scores and traveling replica labels
are checked every 128 sweeps and at completion. Round-trip accounting starts
anew at production; a trip is a labeled configuration's 0→64→0 traversal.

Compile with `g++ -std=c++17 -O3 -Wall -Wextra -pedantic sample.cpp -o BINARY`;
no fast-math or external libraries. The controller uses eight workers,
180-second audit, 60-second analyzer fixtures, 900-second per-job and
180-second analysis limits. Every job is declared before observation.
No timeout, nonzero return or statistical failure triggers a retry.

The frozen controller runs the audit once, then analyzer fixtures once,
then the twenty jobs, then the analyzer once. Failed audit/fixtures prevent
production; all partial records remain. A failed production job is retained
and the analyzer is still invoked to record the failure. Analyzer stdout,
stderr and return code are separately captured; this closes the missing
return-code record in the first endpoint pilot. The output directory must
not exist before invocation. Controller CLI: `python3 run_pilot.py BINARY OUT`.

Before the first invocation, commit and push exactly PREREG.md, PROOF.md,
REVIEW.md, sample.cpp, analyze.py, test_analyze.py and run_pilot.py. Record the
full commit and seven SHA-256 values in issue #1261, publicly read back the
pin and files, and execute a clean checkout of those exact bytes. No source
file may change after the pin. Static review and compilation alone may
precede it. No scientific program in this item has run at preregistration.

The audit's complete expected stdout, with actual tabs and final newline, is:

```text
NON-CANONICAL floating-point engineering audit
result	PASS
```

The analyzer fixture audit's complete expected stdout is:

```text
NON-CANONICAL analyzer fixture audit
result	PASS
```

Both must exit zero with empty stderr. The sampler audit checks geometry,
conditional ratios, endpoint and exchange ratios, collective sheet updates
against direct curls and scores, uniform sheet conditionals at lambda=0,
slice winding, control reversal and deliberately corrupted caches. The
analyzer fixtures check malformed custody/data and decisive gate cases.
Passing these is an implementation check, not an exact scientific theorem
about floating output.

## Measurements and frozen decisions

Each production block preserves endpoint counts, signed and squared score
sums, separate nonnegative score sums at endpoint one, native action,
endpoint changes, replica exchanges, trips and continuous winding summaries.
For each slice, w=(sum rep(f_01)-rep(k(b+s)))/5 must be integral. At both
endpoints record mean w and fractions of slices with w<0 and w>0. These
statistics use every target observation and do not require an entirely pure
layout. No prescribed winding branch is required to have positive mass.

Custody errors, unexpected/missing jobs, nonzero exit, nonempty stderr,
incorrect headers, budgets, seeds, block counts, nonfinite fields or broken
arithmetic relations give FAIL_IMPLEMENTATION.

Each chain must have at least 1024 observations at each endpoint, 64 target
endpoint changes, eight full round trips, and acceptance at least 0.10 on
every adjacent cut edge. Any failure gives INCONCLUSIVE_MOBILITY.

For p0 and the conditional endpoint means of Y, w, negative-w fraction and
positive-w fraction (nine metrics per group), use batch delta-method errors
from successive blocks of 128,256,512,1024 sweeps. Compare each chain to the
leave-one-chain-out pool, and each chain's first half to its second half,
at four combined standard errors. These gates use batch-only errors;
between-chain disagreement cannot inflate the error used to excuse itself.
For a pooled or leave-one-out error, center batch residuals separately
inside each chain and combine the within-chain variances with the chain's
observation weight. Report the between-chain residual error separately,
only as a descriptive error, never as the tolerance of an agreement gate.
For each pooled metric the largest/smallest nonzero error across the four
scales must be at most two; mixed zero/nonzero errors fail. Entirely zero
errors for p0 or either conditional Y are inconclusive. Entirely zero
winding errors are allowed only when the agreement tests pass; this avoids
forcing a branch of possibly zero or negligible mass to appear.

Insufficient denominators, undefined errors, disagreement or unstable errors
give INCONCLUSIVE_MOBILITY. Record raw control residuals in that case, but
do not treat stationary identities as an implementation test on an
unqualified trajectory.

Only after all four groups qualify these gates, test pooled b=2 p0=1/2
and unconditional E[Y]=0, and pooled b=0 E[Y|s=0]=0 and p0>=1/2, using
four batch-only standard errors. Failure gives FAIL_CONSISTENCY. Otherwise
the sole positive label is TRANSPORT_QUALIFIED, meaning only that these
finite engineering diagnostics passed. It is not a guarantee of mixing or
correct uncertainty coverage. Precedence is FAIL_IMPLEMENTATION, then
INCONCLUSIVE_MOBILITY, then FAIL_CONSISTENCY, then TRANSPORT_QUALIFIED.

The signed ratio and its positive/negative parts are permanently labeled
NONINFERENTIAL_ESTIMATE. No signed confidence interval, squared contrast
range D, fitted exponent, thermodynamic extrapolation or lower bound is
formed, even if every transport gate passes.

## Preservation and disposition

Preserve public-neutral records under ENGINEERING/: audit.tsv/.stderr,
analyzer_tests.tsv/.stderr, each L4_kK_bB_cC.tsv/.stderr for K=1,2;
B=0,2; C=0,...,4; environment.json, execution.json, analysis.json,
analysis.stderr, analysis_execution.json, controller_result.json and
SHA256SUMS. No hostname, private path, binary, credential, private log or
unreviewed third-party data is included. Environmental times, architecture,
versions, source/binary hashes and exact return/byte/hash records are public
custody metadata. Add concise RUN.md, RESULT.md and separate post-run review.

Preserve any failure without changed thresholds. The attempt is consumed
after its first execution; a follow-on requires a new identifier and pin.
Separate assistant review in this session is not independent confirmation by
a second human. Public Canon v92 and the open sector-polarization lower
bound, P1 and PHOTON-MASSLESS-PHASE are unchanged.
