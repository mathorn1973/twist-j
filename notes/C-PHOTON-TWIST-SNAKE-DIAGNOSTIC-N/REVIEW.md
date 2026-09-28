# Pre-execution analytical and static review

**PUBLIC / NON-CANONICAL. Review of the prospective #1259 candidate.**

This is a separate review pass by an assistant agent in the same working
session, not independent confirmation by another human author. It reviews
PROOF.md, PREREG.md, sample.cpp, analyze.py, run_snake.py, run_analysis.py
and test_analyze.py before their public execution pin. Within the pre-pin
rule of PREREG.md the reviewer compiled the sampler, ran `--audit`, ran
`test_analyze.py` and ran short exact Python checks of the identities. No
declared sampling job (`sample L k chain base`) was executed for this
review, with any argument. Compilation, the audit and the synthetic tests
are implementation evidence, not scientific execution evidence. The
declared basis (Public Canon v92, the merge of #1258) is the head of the
public main checkout read for this review.

## Mathematical review

Sections 1-2 cite R_k in (0,1], -iC_k = R_k E Y_k, E Y_0 = 0, E Y_0^2 <= 1
and Var(R_k Y_k) <= R_k(R_k+1) <= 2 from the #1249 proof, whose equations
(E.5)-(E.7), (E.12), (E.13) exist unmodified. Every h_n is a product of
positive values of W, so nu_n is strictly positive and the telescoping (3)
is exact. Sections 3-4: (4), (5) are E_{nu_n} h_{n+1}/h_n = Q_{n+1}/Q_n and
its reverse. The value sets and bounds (6) were recomputed: k=1 gives
phi^2/4, phi^-4, 1, phi^4, 4/phi^2, extremes [0.1459, 6.854]; k=2 gives
phi^-2/4, phi^-4, phi^4, 4 phi^2, 1, extremes [0.09549, 10.47]; analyzer
RATIO and RATIO_BOUNDS agree to 1e-12. (8) is the conditional expectation
given alpha_{-e}; the tower property gives (9), (11); lambda_n(e) is a
convex combination of values of rho_n, so within (6) and independent of
alpha_e; (10) is the conditional-variance identity plus convexity. These
were checked exactly on random finite product spaces (three F_5 links,
five plaquettes) to 1e-12, including own-link invariance. The caveat that
(10) bounds single-sample variances, not the asymptotic variance of a
correlated time average, is correct and necessary.

Section 5: (12) uses Z(c) = Z(-c) with -3k = 2k, -2k = 3k mod 5, checked
for k = 1, 2. (13) holds because 1 - S_{mL} is the set of rows x_3 >= m,
which an x_3 translation maps to S_{(L-m)L} while the whole-seam source
and the periodic weight are translation invariant; the middle-block sums
vanish for 1 <= m < L/2, which C2 tests. E_{2k} Y = -E_{3k} Y follows from
pi_{3k}(alpha) = pi_{2k}(-alpha) and the odd, 5-periodic tangent. The
Fourier inversion (14) was verified on 1000 random symmetric laws:
R_k = sum_a p_a cos(k theta a) inverts to the stated p_a to 1e-13 with
cos(2 pi/5) = 1/(2 phi), cos(4 pi/5) = -phi/2, and (15) is equivalent to
p_{+-2} >= 0 and p_{+-1} >= 0 respectively. Sections 6-7: the integer
curl over a closed 01-torus sums to zero, so w is an integer; one link
update changes a slice sum by 0 or +-5 (checked over all cases), so w is
bookkeeping, not a charge; the chain-4 layout gives w = -1 on twisted and
w = 0 on untwisted slices for k = 1, 2. (16) is labelled a finite-sample
construction; the Jensen constants 1.925, 2.349, 0.424 in PREREG.md were
recomputed. All identities are candidate-T finite-volume statements; no
mixing, equilibrium, thermodynamic, phase or P1 statement is made.

## Static implementation and protocol review

- Sampler: the oriented curl, six incident plaquettes per link, the seam
  at x0 = x1 = 0 ordered x2-fastest and the slice index of each 01
  plaquette agree with the proof and are self-checked at construction.
  The heat bath reduces each incident factor to W(b_i + a) by evenness;
  the cumulative table and its inversion are audited; the uniform link
  sampler is unbiased. The twist cache updates one plaquette and the
  score. Naive and conditional estimators, Y with its L^-2 normalisation,
  the odd tangent table and the sector labels follow the proof; chain 4
  is the declared layout at n = L^2. The schedule (warmup, dwell, L^2-1
  visits, far dwell, visits back, 32 discarded sweeps per step, every
  production sweep measured, 39-field rows, validation after every block
  and step), seeds, sizes, chains, bases and metadata match the analyzer
  and PREREG.md exactly.
- Audit: compiled with the declared command (GCC 13.3.0, x86_64), the
  binary reproduced the SHA-256 declared in PREREG.md. `--audit` exited 0
  with empty stderr and a 238-byte transcript, SHA-256
  `1e2f30627085f6d5b46ae16e1e1249c1041e74ca01447dd8dd73bf0e6c90a41d`,
  byte-identical to `analyze.py` EXPECTED_AUDIT and to PREREG.md; the
  printed counts were rederived from the loop structure.
- Analyzer: manifest, byte counts, hashes, exit codes, empty stderr, audit
  transcript and environment are checked before any row is used; exits
  124 and 127 give INCOMPLETE only; every other defect gives
  FAIL_IMPLEMENTATION for all groups. Rows are checked for schema, frozen
  metadata, block order, moments, histogram counts, naive sums against
  histograms, conditional means within the exact bounds, sector totals
  and flips <= count. The regrouped estimator, inverse-variance weights,
  log corrections, per-batch influence, within-segment coarsening and the
  maximum over scales match PREREG.md; the deficit uses unit weights; G3,
  G4, G5, G9 use pooled within-group variances; G4 uses the intermediate
  ensembles; G8a uses chains 0 and 1, whose law is reversal symmetric at
  every sweep; G10 uses batch-SE corners; zero SE fails G7; the Bennett
  equation has the correct orientation (400 exact two-ensemble examples).
  Controls C1-C3 (total, middle blocks for 1 <= m < L/2, Y antisymmetry)
  use the same partial-sum influence. Precedence, GATES_PASSED, the volume
  rule, the control taint and the INCOMPLETE cap are implemented as
  written. Remark: 2 is the supremum of
  the coarse-over-fine SE ratio; the max/min form of G7 also fires under
  strong block anticorrelation, which is conservative; under an
  independent-block null the twisted-dwell mean-Y ratio has mean 1.10 and
  standard deviation 0.065, so 1.5 is well above four null standard
  deviations. No change is needed.
- Controller and wrapper: audit first with its own timeout, then the 56
  jobs largest-first on four workers, outcomes and hashes preserved
  incrementally, no retry, fresh output directory, SHA256SUMS; the wrapper
  refuses to overwrite, records the analyzer's own process outcome and
  writes SHA256SUMS_FINAL. `python3 test_analyze.py` passed all ten
  fixture routes and fifteen per-gate cases; the generator draws the
  reverse flux law as the exact pushforward p_f W(f+k)/W(f)/r_n.

## Pre-pin history

PREREG.md requires disclosure of every pre-pin audit failure. According to
the session record, and consistent with the files: the compiled sampler
passed its deterministic audit at its first execution, and every later
extension of the audit (exact 625-assignment local enumeration, invariance
under the estimator's own link, cumulative-table inversion, base-2
fixtures, the buffered schedule exercise of the complete chain code path,
the sector labels of the declared initial states) also passed at first
execution; no audit failure occurred at any point. The two preserved
pre-pin transcripts are byte-identical and came from binaries of identical
hash. Pre-pin execution consisted of `--audit` runs, `python3
test_analyze.py` on fabricated records, and `run_snake.py` and
`run_analysis.py` with a stub executable and fabricated records (the
preserved stub run shows 56 stub jobs and the wrapper recording the
analyzer's rejection of them). Additionally the frozen #1249 sampler, not
this one, was compiled and two of its jobs re-executed for wall-clock
timing only.

Analyzer defects found and fixed before the pin: (i) the standard error
of the forward-reverse deficit statistic (G2) was first computed with the
inverse-variance weights of the log R influence instead of unit weights,
understating it by about a factor two; found by a synthetic null
calibration and fixed; (ii) the Bennett acceptance-ratio estimating
equation was first written with the wrong orientation; found by an exact
two-valued example and fixed; (iii) a fabricated test fixture whose
reverse histograms were not consistent with its forward histograms was
corrected in the test generator, not in the analyzer.

Three adversarial reviews by separate assistant agents were obtained
before the pin and led to: a chain-4 initial-state check and the removal
of two vacuous checks in the audit; the flips <= count invariant in the
analyzer; the G7 threshold lowered from 2 (the supremum of the statistic
for a stationary process) to 1.5; pooled within-group batch variances for
G3, G4, G5 and G9 in place of pooled variances over all chains; G4 formed
over complete intermediate-ensemble contributions; G10 formed from
batch-SE intervals; explicit degenerate-SE failures; GATES_PASSED
separated from the closed status set; INCOMPLETE control groups capping
their volume; G8a restricted to chains 0 and 1 and G8b reclassified as an
equilibration gate; a corrected Jensen statement, the plateau-sector
attribution reworded as a hypothesis and notational fixes in PROOF.md;
and per-gate fixture tests in test_analyze.py. Each is present in the
reviewed files.

## Disposition and remaining review

No blocking mathematical or static protocol error remains in the reviewed
candidate. This permits freezing the prospective engineering attempt; it
does not certify finite-precision correctness, successful execution,
equilibration, independence of observations, coverage of the empirical
intervals or the weight of any sector. The written identities retain a
candidate-T ceiling. The numerical attempt has ZERO scientific evidential
weight under its preregistration and cannot close P1, decide a phase or
promote a Canon claim. There is no post-run review in this file. The
exact public pin, first invocation, preserved outputs, failures and
diagnostic disposition must be recorded separately after execution and
must not be used to rewrite PREREG.md or this pre-execution review.
