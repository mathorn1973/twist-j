# P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1 preregistration

Status: FORMAL ZERO-EVIDENCE ENGINEERING PREREGISTRATION / UNEXECUTED

- Owner: A. M. Thorn
- Public reservation: issue #756, successor receipt `issuecomment-5494663082`
- Parent production experiment: issue #742
- Production firewall: issue #757, clause F3
- Branch: `probe/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1`
- Directory: `probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/`
- Public base: `ec84f7bd153a32068b8a267ea75dfc179ad8ba47`
- Canon: Public Canon v74

This is the separately pinned `L=6,8` execution promised by the sealed source
freeze `P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1`.  That predecessor remains
immutable at PR #767 merge
`3bb9087cdea293c494ae86b5824e9d8d221fbbfb`; this is a fresh identifier and
does not resume, rename or edit it.

No `L=6` or `L=8` decision transition may run until this document, every
accepted source, fixture, dependency/input manifest, schedule, statistic,
threshold and terminal is committed, pushed and read back byte for byte from
the public branch.  Development runs are restricted in code to `L<=4`.

This package has zero phase-evidential weight.  Its only possible positive
effect is satisfying production-firewall clause F3 after a merged, publicly
read-back `DUAL_CROSSCHECK_PASS`.  Every other terminal leaves #742 blocked.

## Field 1: equations and exact transition

### 1.1 Paired finite-volume measures

For `L in {6,8}` the primal carrier and exact weight are

```text
K_L=(Z/LZ)^4,
A in C^1(K_L;Z5),
F=dA,
mu_L(A) proportional product_p W(F_p),
W(f)=2+2 cos(2 pi f/5).
```

The independent character carrier is

```text
n in {-1,0,+1}^P,
partial n=0 mod 5,
nu_L(n) proportional 2^(-|supp n|),
j=partial n/5.
```

Plaquette orientations are ordered

```text
(01),(02),(03),(12),(13),(23).
```

The real score extension is exactly

```text
X(f)=sin(2 pi f/5)/(1+cos(2 pi f/5)),
kappa=tan(pi/5),
kappa^2=5-2 sqrt(5),
G=(0,1,2+sqrt(5),-(2+sqrt(5)),-1).
```

The identities under test are the finite-volume contact equation

```text
E_mu X_p^2 + 2 E_nu n_p^2 = 1,                         (C)
```

and, for distinct faces,

```text
Cov_mu(G_p,G_q)+kappa^(-2) Cov_nu(n_p,n_q)=0.           (O)
```

For the reported lowest-nonzero-momentum diagnostic put
`lambda_L=4 sin^2(pi/L)` and `rho=dX`.  The package reports

```text
R_L(q)=[25 tr S_j(q)+tr S_rho(q)]/lambda_L
```

with its block uncertainty.  It has no equality target or phase threshold in
this probe.  In particular, it is not forced to equal the contact baseline
`3[1-E_nu n_p^2]`; its possible displacement from that baseline is part of
the screening information and has no decision authority here.

### 1.2 Frozen dual transition

The transition law is byte-for-byte the mathematical kernel frozen by PR
#767.  A proposal word has geometric length

```text
P(N=m)=2^(-(m+1)).
```

Every letter selects, with fair bits and exact rejection sampling, either a
boundary of an oriented 3-cell or one of the six positive coordinate
homology 2-tori, plus an independent sign.  The SHA-256 counter bitstream has
domain `dual756`; it is independent of the primal Philox stream.

A candidate containing residue 2 or 3 is rejected exactly.  Otherwise, for
`d=|supp n'|-|supp n|`, accept always when `d<=0` and accept for `d>0` iff the
frozen fair-bit test for probability `2^-d` succeeds.  Sparse incremental
updates do not change this law.  Complete allowed-support, modular-boundary,
integer-divisibility and `partial j=0` checks run at the start and every saved
sample.

## Field 2: code, dependencies and independence

The accepted new source inventory is fixed by `SOURCE_SHA256SUMS` and the
public pin.  It contains:

```text
PREREG.md
CROSSCHECK_PIN.md
README.md
primal_replay.cpp
dual_chain.py
analyze_crosscheck.py
run_crosscheck.py
verify.py
FIXTURE_EXPECTED.txt
```

`SOURCE_SHA256SUMS` cannot recursively list itself; its exact bytes and hash
are owned by the public pin and readback receipt.

The primal wrapper includes, without editing, the accepted pilot-2 C++ source
at merge `a91ec3c2a38c64a9c0b1be4db55947ce0c97e937` and source pin
`b43ba8c33d244961783c0de42c89b7038fefe561`.  It calls the same exact
`Z[phi]` local and noncontractible-line heat baths, flat sheets, charge
conjugation and Philox namespaces.  Every replay sample must match the already
public pilot state/cache fingerprints and flux histogram exactly.

The dual code imports no primal transition source.  It independently owns its
cell indexing, cycle generators, SHA-256 bitstream, support firewall,
Metropolis rule, integer boundary/current and Fourier summaries.  The small
development fixture checks byte equality of its transitions against the
sealed PR #767 implementation at `L=2,3`; it opens no `L=6,8` data.

The complete frozen external dependency and public raw-input hashes are in
`INPUT_SHA256SUMS`.  They include the sealed dual kernel/verifier, the
accepted primal source/manifest and all eight immutable pilot logs.

## Field 3: carriers, inputs, starts and schedules

### 3.1 Primal public replay input

Contact statistic (C) uses all four already public pilot-2 chains at each L,
reconstructed solely from their exact flux counts.  Distinct-face and current
statistics replay exactly these two public chains at each L:

```text
L=6 cold r1 seed=0xe755060000000101 thermal=512  samples=512 between=4
L=6 hot  r1 seed=0xe755060000000201 thermal=512  samples=512 between=4
L=8 cold r1 seed=0xe755080000000101 thermal=1024 samples=512 between=8
L=8 hot  r1 seed=0xe755080000000201 thermal=1024 samples=512 between=8
```

There is no new primal random choice.  The replay is accepted only if all 512
sample indices, state/cache fingerprints and five integer flux counts match
the selected public pilot log.  A mismatch is `STOP_DUAL_INTEGRITY`.

### 3.2 Independent dual chains

Exactly four dual chains run for each L:

```text
L=6 cold    r1 seed=0xe756060000000101 thermal_steps=663552  samples=512 between_steps=2592
L=6 cold    r2 seed=0xe756060000000102 thermal_steps=663552  samples=512 between_steps=2592
L=6 surface r1 seed=0xe756060000000201 thermal_steps=663552  samples=512 between_steps=2592
L=6 surface r2 seed=0xe756060000000202 thermal_steps=663552  samples=512 between_steps=2592

L=8 cold    r1 seed=0xe756080000000101 thermal_steps=2097152 samples=512 between_steps=8192
L=8 cold    r2 seed=0xe756080000000102 thermal_steps=2097152 samples=512 between_steps=8192
L=8 surface r1 seed=0xe756080000000201 thermal_steps=2097152 samples=512 between_steps=8192
L=8 surface r2 seed=0xe756080000000202 thermal_steps=2097152 samples=512 between_steps=8192
```

One nominal boundary-generator coverage is `2*(4L^4)` Markov steps because
the expected number of boundary-generator letters per step is `1/2`.
Thermalisation is therefore 64 nominal coverages.  Measurement spacing is
one quarter nominal coverage.  These are engineering schedules, not proven
mixing times; section 5 decides whether they were adequate.

`cold` is the zero 2-chain.  `surface` is the positive sum of boundaries of
all `(0,1,2)` cubes whose four anchor coordinates are even.  These cube
boundaries are disjoint for even L.  The complete support/closure validator
must accept the start before the first transition.

No chain is restarted, extended, replaced or thinned differently.  There is
no sample at the thermal endpoint; every sample follows exactly the frozen
`between_steps` transitions.

## Field 4: frozen observables and estimators

### 4.1 Face statistics and separation census

Every configuration records global means of `G`, `G^2`, `n`, and `n^2` over
all `6L^4` positive plaquettes.  For each orientation `(a,b)`, let `c` be the
least coordinate axis outside `{a,b}`.  The four distinct-face families are

```text
inline1      q=(x+e_a,a,b)
transverse1  q=(x+e_c,a,b)
inline2      q=(x+2e_a,a,b)
transverse2  q=(x+2e_c,a,b).
```

Each sample statistic averages products over every anchor and all six
orientations.  No separation may be added or removed after the pin.

The covariance estimator for either field is

```text
mean(pair_product)-mean(field)^2
```

using the complete accepted sample set.

### 4.2 Integer current and lowest momentum

The dual code computes the principal integer boundary and requires every
entry to be divisible by five before setting `j=partial n/5`.  It records
`j^2`, nonzero density, exact direction sums and exact `partial j=0`.

For each `r=0,1,2,3`, put `q_r=2 pi e_r/L`.  With anchor coordinate `x`,

```text
S_j_trace(q_r)
 = L^-4 sum_mu |sum_x j_mu(x) exp(-i q_r x_r)|^2.
```

The primal replay forms `rho=dX` on all four oriented 3-cell types and
records the analogous trace `S_rho_trace(q_r)`.  Direction-wise values and
the dual longitudinal component are retained.  The arithmetic means over the
four lowest momentum axes enter only the reported `R_L`.  The value of `R_L`
has no identity or threshold authority.  Only the frozen mixing/quality gates
on its constituent `rho` and `j` series can return `STOP_DUAL_MIXING`.

### 4.3 Blocking and uncertainty

Samples remain in their original chains.  The block length is exactly 32,
giving 16 complete blocks per chain.  Blocks never cross chain boundaries.

Nonlinear covariances are evaluated from complete sufficient-statistic means.
Their standard errors use a delete-one-block jackknife.  Primal and dual runs
are independent, so the standard error of a residual is the hypotenuse of the
two marginal jackknife standard errors.  The character-dictionary comparison
budget is a two-sided four-standard-error interval; no Gaussian p-value is
used.

Floating point appears only in measured summaries, Fourier transforms and
statistics.  Exact transition, state, count, support, boundary and current
checks remain integer or algebraic.  Every numeric output must be finite.

## Field 5: mixing, precision and failure thresholds

### 5.1 Frozen mixing gates

The primal decision series are `g_mean`, `x2_mean`, the four pair products and
the four lowest-momentum `rho` powers.  The dual decision series are `n_mean`,
`n2_mean`, the four pair products, `j2_mean`, `j_nonzero_density` and the four
lowest-momentum `j` powers.  The odd one-point series are gated because their
squares enter the off-contact covariance estimators.

The primal mixing gates apply to the two exact replay chains at each L, because
only those replays carry the new distinct-face and `rho` observables.  Contact
(C) additionally uses the cold/hot r2 public pilot inputs already qualified by
the accepted pilot-2 mixing gate; those immutable r2 inputs are not re-gated in
this probe.

For every such series:

```text
sample variance in every chain                     > 0
Geyer IMS ESS in every chain                       >= 64
rank-normalized split Rhat, primal two chains      <= 1.10
folded rank-normalized split Rhat, primal           <= 1.10
rank-normalized split Rhat, dual four chains        <= 1.05
folded rank-normalized split Rhat, dual              <= 1.05
pooled rank-normalized bulk ESS                     >= 200
first-half / second-half drift in every chain       <= z 4
primal cold/hot mean separation                     <= z 4
dual cold/surface group mean separation             <= z 4
distinct state fingerprints in every chain          >= 0.99
```

Ranks, ties, Blom probabilities and Geyer initial-monotone-sequence rules are
the accepted pilot-2 definitions.  A failure returns `STOP_DUAL_MIXING`.

### 5.2 Frozen precision and character-dictionary budgets

After mixing passes, require

```text
face-contact residual four-SE half-width            <= 0.03
each off-contact residual four-SE half-width        <= 0.02
```

at both L values.  A wider interval is insufficient precision and returns
`STOP_DUAL_MIXING`.

For (C) and every preregistered instance of (O) at both L values, the
numerical residual must satisfy

```text
abs(residual) <= 4*combined_jackknife_SE + 5e-15.
```

Once integrity, mixing and precision have passed, a residual outside that
prospective budget returns `STOP_DUAL_INTEGRITY` with reason
`DICTIONARY_RESIDUAL_OUTSIDE_BUDGET`.  It is not phase evidence and is not
promoted to `BREAK_DUAL_DICTIONARY`.

`BREAK_DUAL_DICTIONARY` is reserved exclusively for an independently
reproduced exact finite counterexample or a mathematical contradiction to
the declared character dictionary.  No floating Monte Carlo residual can
fire it.

## Field 6: exact terminal grammar and action layer

Every completed modeled record selects exactly one terminal in this logical
order:

```text
1 BREAK_DUAL_DICTIONARY
    an exact finite or mathematical counterexample exists;

2 STOP_DUAL_INTEGRITY
    any modeled public replay fingerprint, exact state, support, modular
    boundary, integer current, current closure, schedule, record or schema
    check fails;

3 STOP_DUAL_MIXING
    integrity passes but a frozen mixing or precision gate fails;

4 STOP_DUAL_INTEGRITY
    mixing and precision pass but a statistical character-dictionary residual
    lies outside its frozen four-SE budget;

5 DUAL_CROSSCHECK_PASS
    all exact, mixing, precision and character-dictionary gates pass.
```

The repeated integrity label makes the public four-terminal vocabulary total
for completed modeled records without miscalling a statistical mismatch an
exact dictionary breaker.  Source/input/output hash failure, preflight failure,
nonzero child exit, unexpected stderr or driver crash occurs outside the
modeled record: no terminal, no `EXPECTED.txt` or `RUN.md`, and the public pin
is `ABANDONED_PIN` under the repository execution policy.

```text
action layer:        L6 finite-volume measure/observable engineering
consumed state:      L1 exact Z5 links and independent dual 2-chains
cross-layer claim:   none
maximum status:      ZERO_ENGINEERING_ONLY / production prerequisite F3
Canon movement:      forbidden
```

No terminal is evidence for or against a photon phase.  This probe proves no
thermodynamic limit, pole identification, polarization, SI speed, matter/light
split, contraction/expansion or cosmological statement.

## 7. Pin, one-shot execution and custody

Before the pin only static checks, compilation and `L<=4` fixtures are
allowed.  `CROSSCHECK_PIN.md` declares that the first commit containing its
final bytes is the immutable pin.  After public push and byte-for-byte
readback, the sole formal local command from this directory is

```text
python3 run_crosscheck.py
```

The frozen environment is

```text
platform            Linux x86_64
Python              3.10.12
C++ compiler         g++ 11.4.0 (Ubuntu 11.4.0-1ubuntu1~22.04.3)
Boost headers        libboost-dev 1.74.0.3ubuntu7 (BOOST_VERSION=107400)
compile flags        -std=c++20 -O3 -DNDEBUG -Wall -Wextra -Wpedantic
LC_ALL / LANG        C / C
TZ                   UTC
PYTHONDONTWRITEBYTECODE 1
PYTHONHASHSEED       0
primal concurrency  4 subprocesses
dual concurrency    4 subprocesses
```

The one-shot driver refuses every other platform, architecture, Python or
compiler version and requires its working directory to be this package
directory.  Before any fixture or decision transition it also preprocesses a
minimal `boost/version.hpp` translation unit and requires exactly
`BOOST_VERSION=107400`; a missing or different Boost.Multiprecision header set
is a preflight stop.

The driver refuses any pre-existing decision artifact, verifies every pinned
source and public input, runs the small fixtures, then runs the four primal
replays and eight dual chains exactly once.  It writes only the preregistered
ASCII/LF raw logs, custody manifests, `ANALYSIS.txt`, and the exact captured
stdout of one verifier invocation as `EXPECTED.txt`.

After the pin, allowed additions are exactly

```text
four primal replay logs
eight dual chain logs
PRIMAL_RUNS.tsv
DUAL_RUNS.tsv
OUTPUT_SHA256SUMS
ANALYSIS.txt
EXPECTED.txt
RUN.md
RESULT.md
```

A crash, nonzero process exit or failure to produce a complete modeled
terminal consumes this identifier under the abandoned-pin rule.  It is not
repaired or rerun.  Source, inputs, seeds, schedules, separations, statistics,
thresholds and terminal precedence never change after the public pin.

Only a merged and publicly read-back `DUAL_CROSSCHECK_PASS` satisfies F3.
Production #742 remains forbidden throughout this probe.
