# P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2 preregistration

Status: FORMAL L6/L8 ZERO-EVIDENCE ENGINEERING PREREGISTRATION / UNEXECUTED

- Owner: A. M. Thorn
- Public reservation: issue #756, receipt `issuecomment-5498022449`
- Consumed cross-check: `P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1`, merge
  `ebf1d8a2100cb26c58721edaade67a278a0004a7`, terminal
  `STOP_DUAL_MIXING`
- Qualified mobility carrier: `P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1`,
  result `d5fc9af9596dfa9fbd6fceb9bb0958301e48fdea`, merge
  `072113d6a22fccef6468d2d647d006c262b6bf2d`
- Immutable positive kernel component: PR #767, merge
  `3bb9087cdea293c494ae86b5824e9d8d221fbbfb`
- Transcript-policy precursor: PR #773, merge
  `d0bc920b27117ea4a409282e3481340f50433763`
- Parent production experiment: issue #742
- Production firewall: issue #757, clause F3
- Branch: `probe/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2`
- Directory: `probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2/`
- Public base: `d0bc920b27117ea4a409282e3481340f50433763`
- Canon: Public Canon v74

This is the fresh F3-capable successor reserved only after the mobility
qualification passed and issue #756 publicly accepted the exact
sector-umbrella construction as a wrapper retaining #767 at positive weight.
It neither reopens nor edits CROSSCHECK-1.  In particular, no reported Ward
residual from that consumed run selected any seed, start, schedule,
separation, threshold, block size or terminal below.

No `L=6` or `L=8` decision state, including a fresh dual state or a primal
replay state, may be constructed until this document, every source and input,
the combined fixture, the exact schemas, and both manifests are committed,
pushed, publicly pinned on issue #756 and read back.  Before that pin only
static checks, compilation and the hard-coded `L=3,4` development fixtures
are allowed.  A claimed pin is one shot: there is no restart, extension,
replacement, repair run or seed substitution.

The present experiment has zero phase-evidential weight.  Only a merged and
publicly read-back `DUAL_CROSSCHECK_PASS` can satisfy #757/F3.  Every other
modeled terminal consumes this identifier and leaves production #742
forbidden.

## Field 1: paired finite-volume measures and identities

For `L in {6,8}`, put `K_L=(Z/LZ)^4`.  The primal carrier and exact weight are

```text
A in C^1(K_L;Z5),
F=dA,
mu_L(A) proportional product_p W(F_p),
W(f)=2+2 cos(2 pi f/5).
```

The independent dual carrier and bottom target are

```text
n in {0,1,4}^{6 L^4},
partial n=0 mod 5,
tilde(n)_p in {0,+1,-1},
nu_L(n) proportional 2^(-|supp n|),
j=partial tilde(n)/5.
```

Positive plaquette orientations are ordered exactly

```text
(01),(02),(03),(12),(13),(23).
```

The real score extension is

```text
X(f)=sin(2 pi f/5)/(1+cos(2 pi f/5)),
kappa=tan(pi/5),
kappa^2=5-2 sqrt(5),
G=(0,1,2+sqrt(5),-(2+sqrt(5)),-1).
```

The two finite-volume identities under test are

```text
E_mu X_p^2 + 2 E_nu n_p^2 = 1,                         (C)
Cov_mu(G_p,G_q)+kappa^(-2) Cov_nu(n_p,n_q)=0            (O)
```

for the contact face and the four frozen distinct-face families in Field 6.
For reporting only, with `lambda_L=4 sin^2(pi/L)` and `rho=dX`, the package
also evaluates

```text
R_L(q)=[25 tr S_j(q)+tr S_rho(q)]/lambda_L.
```

`R_L` has no equality target, phase threshold or terminal authority beyond
the frozen quality gates on its constituent series.

## Field 2: one exact sector-umbrella transition

The product chain has levels

```text
s=0,...,S,                 S=max(15,L^2),
pi_s(n) proportional 2^(-|supp n|+s B(n)),
B(n)=1[j(n)!=0]+1[H_2(n)!=0].
```

The bottom marginal `pi_0` is exactly `nu_L`.  Every transition consumes four
selector bits and chooses one fixed random-scan component:

```text
selector 0       hold                                      probability 1/16
selector 1       immutable-#767 random-word Metropolis     probability 1/16
selector 2       charge conjugation                        probability 1/16
selectors 3..5   cube-orbit heat bath                      probability 3/16
selectors 6..9   tri-star-orbit heat bath                  probability 4/16
selectors 10..11 translated-plane-orbit heat bath          probability 2/16
selectors 12..15 adjacent replica swap                     probability 4/16
```

The #767 component acts only at level zero and is not replaced.  Its proposal
word has `P(length=m)=2^(-(m+1))`; every letter selects an oriented cube
boundary or one of six fixed coordinate two-tori and a sign using exact fair
bits and bounded rejection.  Hard-support failures are rejected.  Otherwise
the exact acceptance probability is `min(1,2^(-Delta support))`.

Each local orbit heat bath enumerates all `k in Z5` for which `n+k g` remains
hard.  At level `s` its exact integer mass is proportional to

```text
2^(-|supp(n+k g)|+s B(n+k g)).
```

Adjacent replicas at `s,s+1` swap with probability

```text
min(1,2^(B(x)-B(y))).
```

All transition decisions use integer arithmetic and fair SHA-256 bits.  The
stream is MSB first from consecutive blocks

```text
SHA256(ASCII domain || 16 seed bytes || 16 counter bytes),
domain = photon-z5-dual-mobility-qualification-1,
```

with the counter unsigned 128-bit big endian from zero.  Keeping the qualified
domain is part of the exact-wrapper freeze; the fresh seeds below make the
formal streams disjoint from the qualification streams.

## Field 3: source, inputs and independence

The accepted new-source inventory is exactly

```text
PREREG.md
CROSSCHECK_PIN.md
README.md
primal_replay.cpp
crosscheck2_engine.cpp
state_reader.py
analyze_crosscheck2.py
engine_fixture.py
reader_fixture.py
run_crosscheck2.py
verify.py
FIXTURE_EXPECTED.txt
```

`SOURCE_SHA256SUMS` fixes these twelve entries in this order.  It does not
list itself; its exact bytes and digest are owned by the public pin and pin
receipt.  `INPUT_SHA256SUMS` fixes every external byte actually opened by the
runner, reader, analyzer or verifier.  It includes the immutable #767
component, the successful mobility-qualification contract, the pilot-2
statistical implementation and all eight accepted pilot-2 primal logs.  Four
source-only CROSSCHECK-1 invariance inputs (`PREREG.md`, `dual_chain.py`,
`analyze_crosscheck.py`, `primal_replay.cpp`) support the hash-checked semantic
fixture for the frozen Ward dictionary, separations and estimators.  It
contains no `P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1` raw dual transcript,
`ANALYSIS.txt`, `EXPECTED.txt`, `RUN.md`, `RESULT.md` or output manifest.

The input manifest also opens the public production-freeze Markdown/schema,
the #767 result bytes, and the mobility qualification's pin, run and expected
record.  These bind the F3 wording, accepted wrapper and successful schedule
without importing the consumed CROSSCHECK-1 Ward residual split.

The primal wrapper includes the accepted pilot-2 C++ source without changing
its transition.  Exactly four selected public chains are regenerated after
the pin:

```text
output                    pilot-2 source  L  start  seed                thermal samples between
primal_L6_cold_r1.log     L6_cold_r1.log  6  cold   0xe755060000000101  512     512     4
primal_L6_hot_r1.log      L6_hot_r1.log   6  hot    0xe755060000000201  512     512     4
primal_L8_cold_r1.log     L8_cold_r1.log  8  cold   0xe755080000000101  1024    512     8
primal_L8_hot_r1.log      L8_hot_r1.log   8  hot    0xe755080000000201  1024    512     8
```

Their required complete output bytes are frozen prospectively:

```text
primal_L6_cold_r1.log  bytes=265645 sha256=607b9d73b6b24a6a8c22375ecb6de6c1aedc5c6cd512f642ea40fe12b327043b
primal_L6_hot_r1.log   bytes=265613 sha256=6d981042cd9f94d3450d53705b5c85b834f2d3ac8083709cb8e2cd94a63d6d2f
primal_L8_cold_r1.log  bytes=267498 sha256=0c0c180d0953bfaeaa2eb99b1f11f253bc07048eb2e7a70f99f6f30c3a6b7f87
primal_L8_hot_r1.log   bytes=267532 sha256=645cb1d3d6992d585ed0903a3e28f72f226572ae0732fbc728b69244adf8e0b5
```

Thus the new files are byte-identical deterministic replays, not new primal
Monte Carlo choices.  All eight pilot-2 chains remain exact contact inputs;
only these four carry the distinct-face and `rho` replay series.

The dual engine imports no primal transition source.  Its full state stream
is consumed only through an OS pipe by the pinned independent reader.  No
unfiltered engine stream is ever a file, runtime input to a later run, or
committed artifact.  This package is not issue #748 and does not satisfy that
separate independent-reader obligation.

## Field 4: fresh dual seeds and schedule

The public seed anchor is the mobility-qualification merge

```text
072113d6a22fccef6468d2d647d006c262b6bf2d.
```

For each row, form exactly the ASCII preimage

```text
P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2|072113d6a22fccef6468d2d647d006c262b6bf2d|L=<L>|start=<start>|replica=<r>
```

with decimal `L,r`, lowercase start, no LF or NUL.  Its SHA-256 is shown
below; the seed is the first 16 digest bytes interpreted big endian.

```text
label             SHA256                                                            seed
L6_cold_r1        bc2def7bcee975913c3b3b3999e83ad3ec5a159fe7bf5775c0ace3824a35b219  0xbc2def7bcee975913c3b3b3999e83ad3
L6_cold_r2        1a7ab1ad0011b62c04dcf48da9be340377e3f0b9a21a8e5b28eb98daaf6c2654  0x1a7ab1ad0011b62c04dcf48da9be3403
L6_stratified_r1  5f0f36673dd145755b9a49e703aef3d6cfe3ca5bb474ccc6e106fb8b6cdc9ee8  0x5f0f36673dd145755b9a49e703aef3d6
L6_stratified_r2  2b19daecb5c523f30bee3be7c047eb40d3ff106b7fd941c9b6d0d840c766a8b2  0x2b19daecb5c523f30bee3be7c047eb40
L8_cold_r1        46ba01f80aec780ff9cc8b7e876c700c2dfe2457398c867cf91dc27ca64bf013  0x46ba01f80aec780ff9cc8b7e876c700c
L8_cold_r2        2e0ccaa683e5f39f1237f05193b299c409fe2ebb85994aedcd00db4969cd1d31  0x2e0ccaa683e5f39f1237f05193b299c4
L8_stratified_r1  f8f631709b4b9ce34f8a658bef3e1d0a678c2fa4e138bd6e7d0d556752ced23a  0xf8f631709b4b9ce34f8a658bef3e1d0a
L8_stratified_r2  fcd563ecc8bf8179b96c20db2c388307235ed3ee622912f209065bd192200c21  0xfcd563ecc8bf8179b96c20db2c388307
```

The engine independently accepts only these eight lowercase seed tokens with
their matching `L/start`.  `cold` initializes every level at zero.
`stratified` initializes level zero at zero and cycles levels `1..S` through
the fixed 21-face current witness, its conjugate, the positive `(01)` homology
plane and its conjugate.  No start is sampled.

The successful qualification map gives the literal per-chain schedule:

```text
L  warm_bottom  checkpoints  thin  validation_stride  transition_cap
6  98,304       2,048        1,536 1,536              1,073,741,824
8  262,144      2,048        4,096 4,096              4,294,967,296
```

`warm_bottom` and `thin` count bottom-edge swap attempts, while
`transition_cap` counts all product transitions.  The warm endpoint is not a
sample.  Checkpoint `i` follows exactly `i*thin` post-warm bottom attempts.
Full exact state validation occurs at start, finish and every checkpoint
because `validation_stride=thin`.  Four subprocess pipelines run
concurrently.  Immediately after both attempt refs have been claimed and the
public ref read back, one monotonic 172,800-second (48-hour) supervisor
deadline begins.  It covers toolchain probes, compilation, fixtures, primal
replay, all dual pipelines, analysis, record construction and formal capture.
All eight specs are submitted exactly once within that same deadline.
Timeout, crash, nonzero exit, nonempty stderr or incomplete output abandons
the pin; it never authorizes a rerun.

## Field 5: raw state, reader and transcript schema

The engine emits one run record, 2,048 checkpoint records and one summary.
Every checkpoint carries the complete hard state in the following canonical
format:

```text
state_encoding       2bit-site-major-pairs-v1
unpacked entries     6 L^4
packed bytes         ceil(6 L^4 / 4)
entry order          site*6+orientation
site order           x0*L^3+x1*L^2+x2*L+x3, x3 fastest
orientation order    01,02,03,12,13,23
codes                00 -> 0, 01 -> 1, 10 -> 4, 11 forbidden
within-byte order    shifts 6,4,2,0 (MSB first)
tail                 unused low bits zero
text                 canonical RFC 4648 base64 with `=` padding
state_sha256         SHA256 of unpacked residue bytes
packed_state_sha256  SHA256 of packed bytes
```

The independent reader validates all 2,048 complete frames, recomputes hard
support, modular boundary, integer-current divisibility and `partial j=0`,
and derives all sufficient statistics.  Engine input is pipe-only.  The runner
caps it at 8,388,608 bytes at L6 and 20,971,520 bytes at L8; the reader
independently has a 100,000,000-byte total emergency cap and a 262,144-byte
raw-line cap, so the smaller L-specific runner limits are authoritative.

The reader's only persistent output is the exact allowlisted file

```text
dual_L{6|8}_{cold|stratified}_r{1|2}.jsonl.
```

It contains exactly 2,050 nonempty LF-terminated canonical ASCII JSON
records: run, samples with one-based checkpoints `1..2048`, summary.  Every
sample retains all sufficient statistics and both state hashes.  A full
`state_2bit_base64` audit frame is retained if and only if
`checkpoint % 16 == 0`, exactly 128 frames including checkpoint 2048.  The
final reader transcript cap is exactly 5,000,000 bytes per chain.

The summary binds the omitted states with

```text
SHA256(
  ASCII "P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2\0packed-state-stream-v1\0L=<L>\0"
  || packed_frame_1 || ... || packed_frame_2048
).
```

There are no separators between fixed-length packed frames.  The verifier
redecodes all 128 retained frames, rederives their sufficient statistics and
both per-frame hashes, and checks the exact audit-frame census.  It checks the
rolling digest's syntax and byte custody but cannot recompute it without the
1,920 intentionally omitted frames.  The digest is a commitment created by
the pinned reader during the sole run, not a post-hoc proof that those omitted
bytes can be reconstructed.

Malformed JSON, duplicate or unknown keys, noncanonical numbers, wrong
schema/version, missing sample, wrong schedule, broken rolling digest,
invalid retained state, inconsistent sufficient statistics or a missing
audit frame is a modeled integrity failure.  An incomplete 2,050-record
stream, child failure or cap violation is outside the terminal grammar and
abandons the pin.

## Field 6: frozen Ward observables and uncertainty

Every configuration supplies global means of `G`, `G^2`, `n`, and `n^2` over
all positive plaquettes.  For orientation `(a,b)`, let `c` be the least axis
outside `{a,b}`.  The four and only four distinct-face families are

```text
inline1      q=(x+e_a,a,b)
transverse1  q=(x+e_c,a,b)
inline2      q=(x+2e_a,a,b)
transverse2  q=(x+2e_c,a,b).
```

Each statistic averages over every anchor and all six orientations.  The
covariance estimator is

```text
mean(pair_product)-mean(field)^2.
```

For each lowest nonzero momentum axis, the reader retains dual `j` power and
longitudinal checks, while the primal replay retains the matching `rho`
power.  No observable or separation is selected after looking at this run.

All 2,048 dual checkpoints enter mobility and Ward analysis.  The dual block
length is exactly 128 consecutive checkpoints, giving 16 blocks per chain.
The primal replay retains its frozen 512-sample, 32-sample block definition.
Blocks never cross chain boundaries.  Nonlinear covariance uncertainty uses
a delete-one-block jackknife of complete sufficient-statistic means.  The
independent primal and dual standard errors combine by hypotenuse.  All
reported floating values must be finite.

## Field 7: gates and lazy evaluation

### 7.1 Exact mobility and qualification mixing

Every chain must pass the successful qualification's dimensionless gates.
Current entry/exit, current dwell and quartile coverage, H2 visits and
changes, ladder transport/flux, band/top events, swap counts and walker round
trips use the complete post-warm census.  Cryptographic state/current
distinctness is deliberately checkpoint-only: require at least 32 distinct
nonzero-current checkpoint hashes, the frozen walker-diversity threshold, and
unique checkpoint fractions at least `0.75` overall and `0.50` per quartile.
Further require swap acceptance at least `0.70`, per-edge attempt balance
`[0.95,1.05]`, at least 64 measured walker round trips, and at least
`ceil(3(S+1)/4)` walkers with a round trip.  The exact integer thresholds are
those frozen in the qualification analysis; no L3-to-L4 anti-collapse
extrapolation is applied.

For its 15 frozen checkpoint series, every chain must have positive finite
variance, Geyer IMS ESS at least 128, rank-normalized and folded split Rhat at
most 1.03, pooled bulk ESS at least 400, pooled tail ESS at least 200, every
chain drift `|z|<=4`, and cold/stratified conservative separation `|z|<=4`.

### 7.2 Ward-series mixing and precision

The primal decision series are `g_mean`, `x2_mean`, four pair products and
four lowest-momentum `rho` powers.  The dual series are `n_mean`, `n2_mean`,
four pair products, `j2_mean`, `j_nonzero_density` and four lowest-momentum
`j` powers.  For every such series require positive finite chain variance,
Geyer IMS ESS at least 64, rank-normalized and folded split Rhat at most 1.10
for the two primal chains and 1.05 for the four dual chains, pooled bulk ESS
at least 200, every chain drift `|z|<=4`, cold/hot primal separation `|z|<=4`,
cold/stratified dual separation `|z|<=4`, and distinct state fingerprints at
least 0.99 per chain.

After mixing passes, require four-SE half-width at most 0.03 for contact and
0.02 for every distinct-face residual at both L.  Each residual must satisfy

```text
abs(residual) <= 4*combined_jackknife_SE + 5e-15.
```

Analysis is deliberately lazy.  Raw/schema/state integrity is decided first.
If it fails, no mobility, Ward-mixing, precision or residual verdict is
computed.  If mobility or qualification mixing fails, no Ward identity is
evaluated.  If Ward mixing or precision fails, no character residual is
tested.  A Monte Carlo residual never becomes an exact breaker.

## Field 8: terminal precedence

Every complete modeled record selects exactly one terminal in this order:

```text
1 BREAK_DUAL_DICTIONARY
    only an independently reproduced exact finite certificate or a
    mathematical contradiction to the declared character dictionary;

2 STOP_DUAL_INTEGRITY
    any raw/schema/state/support/boundary/current/schedule/custody check fails;

3 STOP_DUAL_MIXING
    integrity passes but a frozen mobility, qualification-mixing,
    Ward-series mixing or precision gate fails;

4 STOP_DUAL_INTEGRITY
    all prior gates pass but a statistical character residual lies outside
    the prospective four-SE budget;

5 DUAL_CROSSCHECK_PASS
    every exact, mobility, mixing, precision and dictionary gate passes.
```

`BREAK_DUAL_DICTIONARY` cannot be emitted from floating Monte Carlo output.
The repeated integrity label preserves the public four-terminal vocabulary.
A source/input/fixture mismatch, public-pin failure, attempt-ref failure,
compile failure, timeout, child nonzero exit, stderr, cap violation, driver
crash or incomplete transcript occurs outside this grammar: no terminal is
created and the claimed pin is `ABANDONED_PIN`.

## Field 9: public pin, one-shot execution and replay

The formal receipt must be a comment by GitHub user `mathorn1973` on issue
#756 with exactly these ten lines and nine LF separators after placeholder
replacement.  There is no terminal LF:

```text
P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2 PUBLIC EXECUTION PIN
probe: P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2
branch: probe/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2
pin_commit: PIN_COMMIT
parent_commit: d0bc920b27117ea4a409282e3481340f50433763
source_manifest_sha256: SOURCE_MANIFEST_SHA256
input_manifest_sha256: INPUT_MANIFEST_SHA256
attempt_ref: refs/heads/probe-attempts/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2
formal_data_opened: NO
authorization: SOLE_FORMAL_RUN
```

Before compilation or construction of the first formal state, the runner
requires exact repository-root cwd, clean `HEAD` at the unique-child pin,
literal HTTPS origin, public branch at the pin, exact package inventory,
source/input manifest custody, byte equality to `git show PIN:path`, and an
exact API readback of that receipt.  It also reads back the public wrapper
governance comment `5497635560` (UTF-8 bytes 2,494,
SHA-256 `9c4cb1ac6c3dd176a2480a779b568fe67a449364656a13578263a9cccecdc5a2`)
and reservation `5498022449` (UTF-8 bytes 1,764,
SHA-256 `7f837669ab1e2da337c107d45453db77c2862a6684902275b7492e6b011cdaec`),
including exact author, issue and URL.  It then atomically creates

```text
refs/probe-attempts/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2
refs/heads/probe-attempts/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2
```

at the pin, with zero as the required old object, validates the API response
and immediately reads the public ref back from the literal repository URL.
Neither ref is removed.  Only after both claims may compilation, fixtures,
primal replay or a formal dual state begin.

The frozen formal host is Ubuntu 22.04.5 LTS x86_64, CPython 3.10.12, `g++`
11.4.0, Boost `BOOST_VERSION=107400`, Git 2.34.1, and GitHub CLI exact first
line `gh version 2.4.0+dfsg1 (2022-03-23 Ubuntu 2.4.0+dfsg1-2)`, authenticated
as `mathorn1973`.  Locale is `C`, timezone is UTC, and
`PYTHONDONTWRITEBYTECODE=1` and `PYTHONHASHSEED=0`.  The sole run must use a
fresh full clone created and checked out by Linux.  Its `.git` entry must be a
real nonsymlink directory, not a linked-worktree indirection file, and its
origin must be the exact public HTTPS URL.  A Windows-created linked worktree
whose `.git` file names a host path is therefore not admissible.  A full clone
created by WSL under `/mnt/<drive>` is admissible.  Builds use one explicit
repository-root slot; a stale or concurrent slot fails closed.  The sole
command is

```text
python3 probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2/run_crosscheck2.py \
  --formal --pin-commit FULL_SHA \
  --pin-receipt https://github.com/mathorn1973/twist-j/issues/756#issuecomment-N
```

Allowed post-pin additions are exactly the four primal logs, eight filtered
dual logs, `PRIMAL_RUNS.tsv`, `DUAL_RUNS.tsv`, `OUTPUT_SHA256SUMS`,
`ANALYSIS.txt`, `EXPECTED.txt`, `RUN.md` and `RESULT.md`.  The first result
commit must be the direct child of the pin and change exactly those nineteen
paths.  The public attempt ref remains at the pin; the public probe branch
must point to that direct result commit.

`RUN.md` is exactly the following thirty LF-terminated ASCII lines after
substitution.  `RAW_BYTES` is the sum of the twelve raw transcript lengths and
`OUTPUT_BYTES` is the sum of the fifteen `OUTPUT_FILES` lengths.  After
analysis and output-manifest construction, but before formal capture, the sole
runner generates `RUN.md` and `RESULT.md` itself with exclusive creation.  The
formal-capture verifier requires both exact records in its inventory and
validates them byte for byte.  Only after successful capture does the runner
exclusively write `EXPECTED.txt`; no manual result prose is allowed.

```text
# P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2 formal run
status: COMPLETE_MODELED_RECORD
pin_commit: PIN_COMMIT
pin_receipt: PIN_RECEIPT
local_attempt_ref: refs/probe-attempts/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2
public_attempt_ref: refs/heads/probe-attempts/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2
source_manifest_sha256: SOURCE_MANIFEST_SHA256
input_manifest_sha256: INPUT_MANIFEST_SHA256
receipt_body_sha256: RECEIPT_BODY_SHA256
output_manifest_sha256: OUTPUT_MANIFEST_SHA256
analysis_sha256: ANALYSIS_SHA256
formal_command: python3 probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2/run_crosscheck2.py --formal --pin-commit PIN_COMMIT --pin-receipt PIN_RECEIPT
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: CPython 3.10.12
compiler: g++ 11.4.0
boost_headers: BOOST_VERSION=107400
git: 2.34.1
github_cli: 2.4.0+dfsg1 (Ubuntu 2.4.0+dfsg1-2)
github_identity: mathorn1973
environment: LC_ALL=C LANG=C TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
output_file_count: 15
output_bytes: OUTPUT_BYTES
raw_file_count: 12
raw_bytes: RAW_BYTES
formal_data_child_exit_codes: all 0
formal_data_child_stderr_bytes: all 0
driver_record_stage: before_formal_capture_and_successful_return
formal_attempts: 1
formal_rerun: NO
```

`RESULT.md` is exactly nine LF-terminated ASCII lines.  `TERMINAL` is the one
analysis terminal.  For `DUAL_CROSSCHECK_PASS`, `F3_STATUS` is
`ELIGIBLE_ON_MERGE_AND_PUBLIC_READBACK` and `PRODUCTION_STATUS` is
`REMAINS_FORBIDDEN_UNTIL_MERGE_AND_PUBLIC_READBACK`; for every other terminal
they are `NOT_SATISFIED` and `FORBIDDEN`.

```text
# P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2 result
terminal: TERMINAL
evidential_status: ZERO_ENGINEERING_ONLY
f3_status: F3_STATUS
production_742: PRODUCTION_STATUS
canon: Public Canon v74
canon_movement: NONE
output_manifest_sha256: OUTPUT_MANIFEST_SHA256
analysis_sha256: ANALYSIS_SHA256
```

The no-argument verifier is read-only.  It checks the immutable source/input
and committed-output custody, redecodes the 128 audit frames, and reruns only
the pinned reader/analyzer logic over committed raw transcripts.  It never
compiles or invokes either Monte Carlo engine and never resamples a chain.

```text
action layer:        L6/L8 finite-volume measure/observable engineering
consumed carrier:    L1 exact Z5 links and exact closed dual two-chains
cross-layer claim:   none
maximum status:      ZERO_ENGINEERING_ONLY / production prerequisite F3
Canon movement:      forbidden
```

No terminal proves a thermodynamic photon phase, pole, polarization, SI
speed, Born selection, matter/light split, contraction/expansion or any
cosmological statement.  Public Canon remains v74.
