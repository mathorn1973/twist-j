# P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2 preregistration

Status: FORMAL PREREGISTRATION / ZERO-EVIDENCE ENGINEERING PILOT / UNEXECUTED

Owner: A. M. Thorn
Public reservation: [issue #755](https://github.com/mathorn1973/twist-j/issues/755)
Parent experiment: [issue #742](https://github.com/mathorn1973/twist-j/issues/742)
Branch: `probe/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2`
Directory: `probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/`
Date: 2026-09-01

This document freezes the second and newly consumed photon mixing pilot. The
first pilot remains sealed in PR #746 at merge
`46be0601a78827fb4e98d5892ffa7966652d1c25`; it is not resumed, repaired,
renamed or reinterpreted. Its honest result was a mixing/integrity STOP.

The exact local-kernel dependency is the public package merged by PR #760 at
`5c2d469880828f29023e3cf592e86abbe352cd59`. That package proves exact
single-link heat-bath sampling, complete-sweep finite-volume ergodicity and a
flat holonomy symmetry. It proves no useful mixing time and no phase.

No `L=6` or `L=8` decision chain may run until this preregistration, all
accepted source, the independent fixture, the analyzer and `PILOT_PIN.md` are
committed, pushed and publicly read back byte for byte. Compilation, static
checks and small `L=3,4` integrity fixtures are development checks, not pilot
data. The pilot has zero phase-evidential weight under every terminal.

## 0. Authority and scope lock

```text
STATE:                 ACTIVE
CANON:                 Public Canon v74
PUBLIC MAIN AT CLAIM:  5c2d469880828f29023e3cf592e86abbe352cd59
TAG:                   canon-v74
CONTENT_COMMIT:        2561f7dcadcbbf683ce7b36219ea67378d879a5a
CANON_SHA256:          2db550cb68f6f4ee33b9194f1f6b3bc4d8fec19cd79e79a702c5357577a92c0e
CANON_BYTES:           389246
```

The pilot asks only whether a prospectively frozen implementation and schedule
mix sufficiently to justify drafting the separate production preregistration
owned by issue #757. It cannot return `PHOTON_EVIDENCE`, a phase label, a
Canon status, a Registry change or a gate closure.

## Field 1: equation and transition kernels

### 1.1 Fixed finite-volume measure

For `L in {6,8}`, the carrier is the periodic four-torus

```text
K_L=(Z/LZ)^4,
A in C^1(K_L;Z5),
F=dA in C^2(K_L;Z5).
```

Link-field equality is literal equality of all `4L^4` oriented link values.
No gauge quotient and no topological sector is removed. The unnormalised
target measure is fixed at the one and only physical pilot point `t=1`:

```text
mu_L(A) proportional product_p W(F_p),
W=(4,1+phi,2-phi,2-phi,1+phi) in Z[phi]^5,
phi^2=phi+1.
```

All five weights are strictly positive in the real embedding. There is no
coupling scan and no `W^t` diagnostic in this pilot.

### 1.2 Exact local heat bath

For an oriented link, let its six incident residual fluxes be `r_i`, with
incidence signs `epsilon_i`. For candidate absolute link value `a in Z5`,

```text
L_a=product_(i=1)^6 W(r_i+epsilon_i a mod 5),
P(a | exterior)=L_a/sum_b L_b.
```

The implementation stores every coefficient of every mass as an unbounded
integer pair `(u,v)` representing `u+v phi`. Floating point is forbidden in
all categorical decisions.

### 1.3 Exact noncontractible-line heat bath

For direction `mu` and a transverse anchor with `x_mu=0`, let `ell` be the
closed length-`L` line of all `mu`-links through that anchor. Candidate
`delta in Z5` adds the same `delta` to every link of `ell`. Exactly `6L`
adjacent plaquettes change for `L=6,8`; their exact orbit masses are

```text
M_delta=product_(p incident to ell) W(F_p+s_p delta mod 5),
P(delta | line exterior)=M_delta/sum_h M_h.
```

One line sweep visits all `4L^3` noncontractible lines exactly once. Since
`gcd(L,5)=1` for both pilot sizes, a nonzero selected shift changes that
line's holonomy. Each line kernel is a heat bath on its five-point orbit and
preserves the same finite-volume measure.

### 1.4 Exact prefix decision

For positive masses `q_0,...,q_4 in Z[phi]`, put

```text
S=sum_j q_j,
C_j=sum_(i<j) q_i.
```

After `n` random bits the sampled real lies in the half-open dyadic interval
`[m/2^n,(m+1)/2^n)`. Category `j` is returned only after the exact tests

```text
m S       >= 2^n C_j,
(m+1) S   <= 2^n C_(j+1)
```

both hold in the real embedding of `Z[phi]`. The production implementation
refines by 64-bit blocks at `n=64,128,192,256`; block refinement is the same
prefix algorithm as bitwise refinement. If no category is certified by 256
bits, the pilot immediately returns `STOP_INTEGRITY`. It never rounds and
never falls back to a fixed-width allocation.

For exactly `N=439418880` capped local and line heat-bath decisions, the
ideal-bit union bound on
any 256-bit exhaustion is `4 N 2^-256 < 1.52e-68`. This bound is about the
ideal random-bit algorithm, not a claim that the deterministic counter stream
is physical randomness.

### 1.5 Measure-preserving auxiliary moves

For each direction once per macrocycle, draw exact uniform `h in Z5` and add
`h` to every `mu`-link whose starting coordinate has `x_mu=0`. This flat
sheet changes the corresponding noncontractible holonomy but leaves every
plaquette and the complete flux cache byte-identical. It rotates Polyakov
phases but does not change their radii; it therefore cannot replace the line
heat bath.

After the four sheets, apply global charge conjugation `A -> -A` with exact
probability `1/2`. Since `W(f)=W(-f)`, it also preserves the target measure.

## Field 2: accepted code and randomness

The accepted implementation consists of the exact fourteen-file ordered
inventory pinned by `PILOT_PIN.md` and `SHA256SUMS`: the three Markdown
controls, the five-file C++ generator, the analyzer,
the independent reference, the verifier, the one-shot driver and the two
frozen fixture transcripts. The C++ generator uses Boost's header-only unbounded
`cpp_int`; fixed-width integers may be used only for lattice indices, counters
and Philox words. The independent Python fixture shares no C++ code.

The random source is Philox4x32-10 keyed by the public 64-bit chain seed.
Every use is a pure function of

```text
(seed, kind, macrocycle, ordinal, block),
```

with disjoint `kind` namespaces for hot initialization, local heat bath, line
heat bath, flat sheets and charge conjugation. Variable prefix consumption in
one decision cannot shift any later decision. Exact uniform `Z5` values use
rejection; the fair charge bit uses one counter bit.

The pre-pilot fixture must pass all of the following without opening decision
chains:

1. Philox known-answer vectors and namespace collision census;
2. exact `Z[phi]` sign, multiplication and endpoint comparisons;
3. accepted lower- and upper-threshold equality cases;
4. a forced unresolved prefix that returns the modeled bit-cap STOP;
5. all local masses against independent Python recomputation;
6. line-orbit masses against full action recomputation on `L=3,4`;
7. pairwise detailed balance for local and line kernels;
8. flat-sheet curvature and byte-identical flux-cache checks;
9. charge-conjugation weight identity;
10. identical C++ and Python state hashes after two small-lattice macrocycles.

Any ordinary implementation mismatch is `STOP_INTEGRITY`. `BREAK_KERNEL` is
reserved for an independently reproduced exact counterexample to the public
mathematical kernel contract of PR #760, not for a compiler or coding defect.

## Field 3: carrier, starts, schedules and raw data

One `macrocycle` is exactly:

```text
1. one complete single-link heat-bath sweep over all 4L^4 links;
2. one complete line heat-bath sweep over all 4L^3 noncontractible lines;
3. one exact-uniform flat sheet in each direction mu=0,1,2,3;
4. one exact-fair global charge-conjugation decision.
```

Even-numbered macrocycles use forward lexicographic link and line order;
odd-numbered macrocycles use the exact reverse order. Thermal cycles run
first. Before each recorded sample, exactly `between` further macrocycles run;
there is no sample at the thermal endpoint itself.

The cold start has every link zero. The hot start assigns every link an
independent exact-uniform `Z5` value from the hot-init namespace. Exactly these
eight chains enter the decision:

```text
L=6 cold replica=1 seed=0xE755060000000101 thermal=512 samples=512 between=4
L=6 cold replica=2 seed=0xE755060000000102 thermal=512 samples=512 between=4
L=6 hot  replica=1 seed=0xE755060000000201 thermal=512 samples=512 between=4
L=6 hot  replica=2 seed=0xE755060000000202 thermal=512 samples=512 between=4
L=8 cold replica=1 seed=0xE755080000000101 thermal=1024 samples=512 between=8
L=8 cold replica=2 seed=0xE755080000000102 thermal=1024 samples=512 between=8
L=8 hot  replica=1 seed=0xE755080000000201 thermal=1024 samples=512 between=8
L=8 hot  replica=2 seed=0xE755080000000202 thermal=1024 samples=512 between=8
```

No other chain, restart, extension or discarded warmup may enter the terminal
decision. A failed or unmixed chain is preserved, not rerun with a new seed.

Each sample records the sixteen frozen mixing metrics

```text
logw
polyakov_radius_mean
polyakov_radius_0
polyakov_radius_1
polyakov_radius_2
polyakov_radius_3
vortex_density
monopole_density
score_mean
flux_asym_14
flux_asym_23
flux_fraction_0
flux_fraction_1
flux_fraction_2
flux_fraction_3
flux_fraction_4
```

and also the exact integer diagnostics `flux_count_0` through `flux_count_4`,
state/cache hashes, prefix-depth counters, nonzero line-move counts and
flat-sheet cache checks. The five counts must sum exactly to `6L^4`; each
fraction must agree with its count divided by `6L^4` within `1e-15`, the five
fractions must sum to one within `1e-6`, and the fractions also enter the
frozen mixing gates. The integer counts are diagnostics, not additional
mixing metrics.
The predecessor's wrapping proxy and correlator do not enter this pilot: the
former lacks a complete charged homology classification and the latter lacks
the raw block covariance owned by issue #748.

Each raw log must be ASCII with LF endings, exit zero, empty stderr and a
SHA-256 entry in the post-run manifest. No raw log may exceed 5 MiB.
Their names and order are exactly

```text
L6_cold_r1.log
L6_cold_r2.log
L6_hot_r1.log
L6_hot_r2.log
L8_cold_r1.log
L8_cold_r2.log
L8_hot_r1.log
L8_hot_r2.log
```

`PILOT_RUNS.tsv` has exactly one header and those eight rows. Its header is

```text
filename<TAB>L<TAB>start<TAB>replica<TAB>seed<TAB>thermal_cycles<TAB>measurements<TAB>between_cycles<TAB>bytes<TAB>sha256<TAB>exit_code<TAB>stderr_bytes
```

Seeds use lowercase `0x` plus sixteen hexadecimal digits. Byte counts and
hashes cover the exact raw stdout. Every row must record `exit_code=0` and
`stderr_bytes=0`.

## Field 4: systematics and frozen analysis

The analyzer uses only the Python standard library and reads exactly the eight
named raw logs in their canonical basename order. Before statistics it requires
printable ASCII, LF-only records with a final LF, and the exact positional
layout `RUN + 512 SAMPLE + UPDATE_DIAGNOSTICS + two status footers`. It verifies
the exact record-field inventories, schedule, seed, consecutive sample order,
finite numeric fields, exact flux-count totals, state/cache hashes, canonical
diagnostics and the frozen local, line, sheet and charge decision totals.

For each of the sixteen metrics and each `L`, all of these are required:

1. every chain has at least `0.99` distinct state hashes per sample;
2. every chain has finite, strictly positive sample variance;
3. every chain's Geyer initial-monotone-sequence ESS is at least `64`;
4. rank-normalized split `Rhat` is at most `1.05`;
5. folded rank-normalized split `Rhat` is at most `1.05`;
6. pooled rank-normalized bulk ESS is at least `400`;
7. pooled 5%/95% indicator tail ESS is at least `200`;
8. the two-replica hot/cold mean difference is at most `z=4`. For each start,
   the group mean is the arithmetic mean of the two replica means and its
   standard error is
   `max(hypot(MCSE_1,MCSE_2)/2, stdev(replica_means)/sqrt(2))`; the hot/cold
   denominator is the hypotenuse of the two group standard errors;
9. the first-half/second-half drift in each chain is at most `z=4`, again
   using autocorrelation-corrected MCSE.

Ranks use average ranks for ties and Blom probabilities
`(rank-3/8)/(N+1/4)`. Split chains have length 256. The folded diagnostic
rank-normalizes absolute deviations from the pooled median. Geyer's estimator
forms adjacent autocorrelation pairs, truncates at the first nonpositive pair
and applies the initial monotone minimum sequence before summation. Tail ESS
is the minimum multichain ESS of indicators below the pooled empirical 5%
quantile and above the 95% quantile. Each empirical quantile is the linearly
interpolated order statistic at position `p*(N-1)` (the usual type-7
convention); the indicator comparisons are inclusive (`<=q05`, `>=q95`).

In addition, each chain must record at least one selected nonzero line move in
every direction; every scheduled flat-sheet move must report zero flux-cache
change; no prefix may exceed 256 bits; all expected local, line, sheet and
charge decision counts must match exactly.

No metric, threshold, rank convention, tie rule, quantile convention, sample,
chain or terminal precedence may change after the public pin.

## Field 5: failure thresholds and terminal grammar

Exactly one terminal is selected in this strict precedence:

```text
1. BREAK_KERNEL
2. STOP_INTEGRITY
3. STOP_MIXING
4. PILOT_READY_FOR_PRODUCTION_PREREG
```

### `BREAK_KERNEL`

Return only when the wrapper's exhaustive exact recalculation, implemented
independently of the public kernel verifier merged in #760, exhibits a concrete
counterexample to that public kernel theorem. Record the complete minimal
witness. The frozen reference fixture is replayed separately on every
non-break path; a C++/Python mismatch, reference mismatch, cache defect, bit
exhaustion or malformed log is not this terminal.

### `STOP_INTEGRITY`

Return when no theorem-level breaker exists but any source/pin hash, fixture,
counter namespace, cache identity, bit cap, process exit/stderr, schedule,
seed, sample count, raw hash or custody check fails. A modeled 256-bit
exhaustion is this terminal and is never rounded away.

### `STOP_MIXING`

Return when kernel and record integrity pass but at least one frozen mixing
gate in Field 4 fails. Every failed gate and its value is retained. No chain is
extended and no threshold is relaxed.

### `PILOT_READY_FOR_PRODUCTION_PREREG`

Return only when every integrity and mixing gate passes. This authorizes only
drafting the separate final production preregistration under issue #757. It is
not phase evidence, does not start production and does not discharge the
independent dual/Ward obligation #756 or reader obligation #748.

A completed modeled terminal exits zero with empty stderr and exact stdout.
A crash, nonzero process exit or fixture failure that produces no complete
terminal record is not silently relabeled: the pin is closed as `ABANDONED`
under repository policy, without `EXPECTED.txt` or `RUN.md`.

## Field 6: action layer and public disposition

```text
action layer: L6 finite-volume measure/mixing engineering
consumed state implementation: L1 exact Z5 links and flux cache
cross-layer claim: none
Canon gate movement: forbidden in this probe
maximum status: zero-evidence engineering readiness
```

This probe neither constructs an apparatus nor identifies any measured pole
with the Public Canon v74 spatial/temporal characteristic. It proves no
thermodynamic limit, massless phase, photon, polarization, causal cone, Born
selection, physical contraction/expansion, matter/light split, visible or
invisible sector, continuum limit or SI quantity.

## 7. Immutable source table

The table below freezes the other thirteen immutable source files as lowercase
SHA-256, byte count and filename. `PREREG.md` cannot contain its own digest
without a self-reference; its final digest and byte count are fixed by its row
in `SHA256SUMS` and by the public pin commit/readback. `SHA256SUMS` is itself
fixed by that same public commit/readback and is not self-listed.

```text
7739505d240eac75ed91dca3b80cb57e91da7b8ca28f5f9247c6a3730cb68c52  1426  PILOT_PIN.md
4dc520e24b16594bcfd7ee4996d0febba85ca8f1b6e177c6e6522bb1d7b7f2c4  3619  README.md
68232b2f44bca6fd71514547e2f5aa0ad8aa85b9d298dde5d9a4109ac2151e14  124  photon_z5.cpp
263b631d6322526296cef5b32104f9bbc34184a8506f30fc15962687fcd6727a  19733  photon_z5_part1.inc
7d1183e0f8368310be259fb88fac54aaba9e8661c64112e2577e9929e8ea379d  18505  photon_z5_part2.inc
c6f5776e5c401618bd8478cf98bf99ad9020f50b0dc4495e53e2eea4a971686a  12672  photon_z5_part3.inc
442f79534fc7849fa4801d46908c24abf2d22e0b31a5fdec2e4b068bfd66db4b  17593  photon_z5_part4.inc
d3d2ffba5ade37863f8e34a9b6c8198cf3e222aa8f12a6ba78b621d5c5bef4ce  31530  analyze_pilot.py
e9250fb3d6179c00ac110c540e5e88683c364fe32df084ece10a679ba17ac1ec  20491  reference_check.py
3857ca1e08ea027c86c6696dd78e80adff6bef8fe75bf939d071410c324896d1  28017  verify.py
f329b21ae24c1ae3e8432ab6295f57117e6b6398c1d634d87fd3311cf237abd7  12427  run_pilot.py
621f95193d744e3b33d1c469e45d83d84d7b44f8cc571ca7695457f08e9a43da  671  SELFTEST_EXPECTED.txt
6c86ca3be9c94b0581fe9af2fde41352db0b7f20c48d6b7e066bcebe1476d7be  753  REFERENCE_EXPECTED.txt
```

## 8. Execution and custody lock

The public pin commit is the first commit containing the final
`PILOT_PIN.md`. After public branch and contents readback, only the exact
commands in `README.md` may compile the pinned generator, execute the fixture,
run the eight chains and analyze their immutable logs. The sole local formal
command is `python3 run_pilot.py`; the driver invokes the accepted verifier
exactly once and writes its captured stdout byte for byte as `EXPECTED.txt`.
Environment:

```text
LC_ALL=C
LANG=C
TZ=UTC
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
```

Post-pin commits may add only the eight raw logs, `PILOT_RUNS.tsv`, exact
analyzer stdout as `PILOT_ANALYSIS.txt`, exact verifier stdout as
`EXPECTED.txt`, `RUN.md` and `RESULT.md`. Pinned files never change. No amend,
rebase, squash, force-push, threshold change or post-result schedule change is
permitted.
