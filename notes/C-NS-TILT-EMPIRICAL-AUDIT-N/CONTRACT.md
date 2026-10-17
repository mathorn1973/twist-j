# Frozen empirical summary audit of NS-TILT

NON-CANONICAL / NO AUTHORITY. Owner: A. M. Thorn.
Reservation: #1400. Layer: NOT_APPLICABLE, as in the NS-TILT public row.
This is a retrospective summary comparison, not a formal public probe.

## Basis and custody

Public main: `7d7f588c42422c2cf37b04d76ebc13ca55eb96dc`, Public Canon v100.
Tag `canon-v100` peels to `807dae3fe97dd6a872d5d1305a0133e8e8d856ea`;
content is `a4cc9666662967527abe711441833ff600c00337`. The Canon is
980212 bytes with SHA-256
`5e4de2da8d57ff2f7e4b873e6236b0695677e20d173d894ee70562c1389648c4`.

STATUS, POLICY, AGENTS, CORE, FRONTIER and the relevant Canon, registry
and normative entries were read through the GitHub connector. The source
main's run 37518751601 passes both architecture jobs and check. Its exact
x86_64 log records successful Canon/hash, ledger and gate validators.
No fresh local full-repository replay is asserted. A normal shell remote
scan failed DNS; 210 branch names were enumerated through the connector.
Topic/exact issue and PR searches and the recursive main tree found no
collision. #1399 is a distinct contact note, not consumed or merged here.
The owner has temporarily authorized the connector's noreply commit email.

## Question fixed before arithmetic

Compare the committed hypothesis `n_star = 1 - 5 alpha` against four
specified, published scalar-index summaries, without fitting its integer
coefficient or alpha. The source alpha is ALPHA-FORM [D], with its existing
ALPHA-VALUE-DIGITS [C] witness, not measured CODATA alpha.
The witness in `reproduce/alpha-value/EXPECTED.txt`, blob
`f8a4ece073ff2ad0396078e362447cea0e7c1fb2`, verifies nine-decimal rounding
of inverse alpha to 137.035999190. Therefore use the conservative exact
rounding enclosure

    A = 1/alpha in [137.0359991895, 137.0359991905],
    n_star in [1-5/A_lower, 1-5/A_upper].

This is a numerical enclosure of the committed expression, not a bound on
unknown physical/model corrections. NS-TILT is read literally for this
audit; no unregistered remainder, scale dependence or retuning is added.

`inputs.json` fixes the four rows and their order: Planck 2018 baseline,
P-ACT DR6 without BAO, SPA+BK, and SPA+BK+DESI DR2. Every row has a
primary-source version, model, pivot, uncertainty convention and locator.
P-ACT is not ACT alone. The main pair uses LambdaCDM+r and the published
tensor consistency condition. These are conditions of the literature
inference, not new native TWIST-J theorems. The rows overlap, and their
model/prior differences prevent interpreting them as independent trials.
No exhaustive census of every cosmological analysis is asserted.

The main two means and the CMB-S4 support decision were quoted earlier in
this conversation; prior exposure is explicit. Primary text was read to
verify them. The Planck and ACT rows are contextual source checks, not a
prospective selection made without looking at data. No source-unverified
number enters the audit. Values are taken from text equations, not figures
or table cells: the web PDF screenshot service failed internally.

## Exact diagnostic and rounding convention

For each reported mean m and symmetric 68 percent halfwidth s, compute

    z = (m - n_star)/s.

This is a signed Gaussian-summary diagnostic only. A quoted 68 percent
interval need not equal one standard deviation of an exactly Gaussian
posterior. We do not infer any tail probability, Bayes factor, full-profile
likelihood, independent exclusion count or hypothesis decision from z.

Treat each printed decimal as a rounded measured summary, not an exact
physical value. Under the explicit nearest-rounding convention, give both
m and s their own half-last-digit interval. For n in [n_lower,n_upper],

    numerator in [m-dm-n_upper, m+dm-n_lower],
    denominator in [s-ds,s+ds], with s-ds>0.

The range of the ratio is bounded by the minimum and maximum of its four
corner ratios. The nominal printed-summary range uses dm=ds=0. The wider
box is sensitivity to reporting precision, not added experimental noise
or a confidence interval for the hypothesis. Print rational endpoints and
outward-rounded computed decimal witnesses, using integers only.

`audit.py` is standalone standard-library code. It reads only its adjacent
frozen input file, uses Fraction for science, and writes one JSON stdout.
Basic positive, negative, mixed-sign and zero controls and exact identity
checks run in the same program; they are not independent confirmation.
No raw chain, likelihood, new observation or cosmological solver is run.

## Execution and disposition

Publish this contract, inputs and code in Git before the first execution;
record the exact public commit and SHA-256 values. Static parsing and
source/file checks before the pin are permitted. Run once with a real
30-second timeout, deterministic locale/hash settings and isolated Python.
Preserve exit, stdout and stderr, including an initial failure. Do not
repair a frozen failed run or move its inputs to obtain a preferred result.
A separate successor is required for changed science code or inputs.

The local arithmetic is at most candidate-C. There is no independent
agent/human review claim. Ordinary repository CI does not execute this
notes script, and does not supply its scientific two-architecture gate.
The generic interval argument does not independently verify a measured
cosmological posterior. The empirical hypothesis remains H.

The official CMB-S4 support decision is a separate administrative fact.
It neither confirms nor falsifies NS-TILT. Its old registered test wording
is not silently replaced. Any future decision requires a new explicit
model, dataset/version, nuisance/transfer treatment, statistic and rule.
Already inspected data must not be described as blind prospective data.

The result must distinguish a fit of one scalar formula inside an adopted
effective cosmology from an integer-derived primordial perturbation model.
No planar two-band ETH-TT example may be substituted for an isotropic CMB
spectrum. Canon, registry, frontier, gates, workflows, releases, other
notes and sealed probes are outside the write scope. Publish a draft PR
and a PROMO disposition proposal, without a canonical fold.

Original prose and code: Apache-2.0. Input metadata transcribe only factual
numerical summaries with source attribution. No third-party redistribution.
