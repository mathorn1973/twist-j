# Full-measure twist endpoint pilot

**PUBLIC / NON-CANONICAL. Prospective engineering diagnostic.**

- Item: C-PHOTON-TWIST-ENDPOINT-DIAGNOSTIC-N, issue #1249.
- Author: A. M. Thorn.
- Basis: Public Canon v92; main `de4576b8dba5caf4764cd743e5545ec11e664da3`.
- Scope: L6 finite measure; numerical output has ZERO scientific evidential weight.
- Written estimator identities: candidate-T, independently reviewed before execution.
- No thermodynamic lower bound, P1, phase or physical-photon decision is authorized.

## Prior knowledge and execution boundary

The user requested a prospectively frozen full-measure diagnostic after the
sector-polarization proof attempt failed. Known pointwise positive-sign
arguments fail even for one occupied component. The preceding #1210
sector-flux diagnostic is a separate consumed attempt; no old pin, code,
run, threshold or identifier is resumed. Its existence and purpose were
known before this design. The present signed primal estimator differs from
its squared empirical sector means. The #1220 discrete-defect identities
are prior candidate mathematics; the proof here derives the required
source identity directly and does not promote #1220.

No sampler, sampler audit, pilot analysis or scientific fixture is executed
before the complete sources, proof, this file and the static review are
committed, pushed and read back publicly. Compilation and syntax checks
are allowed. The first scientific invocation is preserved, including
failure. No numerical expected values are asserted in advance.

## Fixed carrier and observable

For L in {4,6,8}, use the periodic positively oriented cubical four-torus,
links alpha in F5 and W(f)=2+2cos(2pi f/5). The seam Sigma contains the
L^2 positive 01 plaquettes at x0=x1=0. Independently for k=1,2, sample the
positive endpoint pair (s,alpha), s in {0,1}, with weight

    product_p W((d alpha)_p+s k Sigma_p).

All link fields and both endpoints remain admitted. Define

    Y = L^-2 sum_(p parallel 01) tan(pi((d alpha)_p+s k Sigma_p)/5),
    T = 1_(s=1) Y,  I0 = 1_(s=0),  c_k = -i C_k = E T / E I0.

The exact proof gives E I0>=1/2 and E T^2<=1. The sampler does not replace
the full measure by selected supports, winding sectors or signs. Finite
sample estimates of these bounds may fluctuate. Every production sweep
contributes; selection of first endpoint arrivals is forbidden.

## Fixed numerical kernel and budget

The standard-library C++17 sampler uses 2L+1 replicas at
beta_j=j/(2L), j=0,...,2L. Each replica has weight
[product W]^beta_j, with the same endpoint variable s. Beta=0 is uniform
and beta=1 is the required endpoint pair. No fractional plaquette source
is inserted. Each sweep consists of all-link five-state heat baths,
independent probability-1/2 proposals to flip s with Metropolis acceptance,
and one parity of adjacent replica exchanges, alternating parity each
sweep. Exact-arithmetic ideal kernels preserve the product measure;
floating point and finite pseudorandom numbers are engineering approximations.

There are four fresh chains for each (L,k):

| Chain | Links in every initial replica | Endpoint in every replica |
|---|---|---|
| 0 | all zero | 0 |
| 1 | independently uniform | 0 |
| 2 | all zero | 1 |
| 3 | independently uniform | 1 |

The seed is 202609270000+1000 L+100 k+chain. Each chain has exactly 512
warmup sweeps and 4096 production sweeps. All 4096 target observations are
saved as sufficient sums in 32 consecutive blocks of 128 sweeps. Metadata
records seeds, counts, per-edge swap attempts/acceptances and complete
labelled-replica round trips from beta=0 through beta=1 back to beta=0.
No adaptive temperature, weight, duration, seed, threshold or stopping rule
is allowed after observation.

The controller runs one deterministic sampler audit (120-second timeout),
then the declared 24 jobs, at most eight concurrently, with a 900-second
timeout per job. Audit failure prevents all sampling. All 24 sampling
jobs are declared in advance: a failed job is preserved and is not retried;
other declared jobs may complete. Timeout, nonzero exit or nonempty stderr
prevents a usable result for the affected group. The output directory must
not already exist. No extension of the frozen budget is part of this item.

## Implementation checks

The post-pin deterministic audit checks oriented incidence, mod-five
curvature reconstruction and d-squared zero, source flips, conditional
heat-bath probabilities, exchange ratios, and the explicit mutation
controls stated in the sampler. Every 128 sweeps and at completion,
cached plaquettes are compared exactly modulo five with reconstructed
link curvature plus source. Energy-cache comparisons use a declared
floating tolerance and are engineering checks. A broken implementation
is not a scientific counterexample to the estimator identity.

## Prospective analysis and gates

For every chain and block scale 128,256,512 sweeps, analyze the signed
ratio c=sum(T)/sum(I0). Its empirical batch standard error uses the block
residual Tbar-c I0bar, divided by mean(I0). Pooling keeps all four chains.
The final reported standard error is at least the maximum over the three
block scales and the four-chain mean standard error. Intervals are c+/-4SE.
The independent-chain error is computed from each chain's ratio residual
at the pooled ratio, divided by the pooled endpoint-zero fraction.
These are empirical engineering intervals with NO rigorous coverage claim.

All the following gates are required for each (L,k):

- Every chain contributes all 4096 production observations, with at least
  256 observations at each endpoint and at least 16 target endpoint changes,
  counting changes caused by exchanges as well as direct proposals.
- Every chain records at least eight complete replica round trips.
- Every adjacent replica edge in every chain has production acceptance
  fraction at least 0.05 among proposed exchanges.
- Each chain estimate agrees with the pooled estimate within four combined
  empirical standard errors; each chain's first and second production
  halves agree under the same rule. These agreement gates use the maximum
  batch-scale error only, excluding the added between-chain error so that
  disagreement cannot enlarge its own acceptance threshold.
- The largest divided by smallest pooled standard error across block
  scales is at most two. Degenerate zero-error output is unresolved.
- An apparent normalization violation Ehat(I0)+4SE(I0)<1/2 is inconclusive.

Missing records give INCOMPLETE; malformed records, failed exact cache
checks or nonfinite values give FAIL_IMPLEMENTATION. Any mobility or
stability gate failure gives INCONCLUSIVE_MOBILITY. Passing these checks
does not prove equilibrium or a mixing time.

Only if both modes at one L pass all gates, both 4SE half-widths are at
most 0.05, and at least one signed interval excludes zero, report
RESOLVED_SIGNED_CONTRAST at that finite L. Otherwise report UNRESOLVED
when no implementation or mobility failure applies. Do not tune the
thresholds after seeing a result.

The sum of squares is evaluated from the nearest and farthest points of
the two signed intervals, never from the squared noisy mean alone. Its
interval has the same engineering limitation. No fitted asymptotic law,
noncollapse/collapse decision, thermodynamic lower bound or Canon
promotion may be inferred from these three finite sizes.

## Custody and publication

Freeze sample.cpp, analyze.py, run_pilot.py, PROOF.md, PREREG.md and the
static review. Record their public commit and SHA-256 before running.
Compile outside the repository with `g++ -std=c++17 -O3 -Wall -Wextra
-pedantic sample.cpp -o <binary>`; do not use fast-math. The controller
command is `python3 run_pilot.py <binary> <new-output-directory>`.
Run `python3 analyze.py <output-directory>` once the controller finishes.
The analyzer checks execution.json, exit codes, stderr, byte counts,
SHA-256, completion metadata and the preserved TSV blocks before admitting
any usable diagnostic. The predicted audit transcript is three geometries,
twelve fixture states, twenty-four caught mutations and PASS, as read from
the frozen source; this prediction is not an observed run. Record the exact pin,
commands, architecture, compiler, exit codes, byte counts and hashes in
RUN.md, and preserve the complete public numerical block records and
summary. Machine nicknames and private paths do not belong in the record.

All results remain under this notes-only path. The C++ engine is not a
standard-library exact probe verifier, and the pilot is not a formal
two-architecture scientific computation gate. The normal repository
checks still apply to publication. Existing notes, Canon, Registry,
Frontier, formal probes, workflows and releases remain untouched.
