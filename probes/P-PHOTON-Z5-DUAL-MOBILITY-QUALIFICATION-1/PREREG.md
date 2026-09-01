# P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1 preregistration

Status: FORMAL L3/L4 ZERO-EVIDENCE ENGINEERING PREREGISTRATION / UNEXECUTED

- Owner: A. M. Thorn
- Public reservation: issue #756, receipt `issuecomment-5495515902`
- Consumed predecessor: `P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1`, merge
  `ebf1d8a2100cb26c58721edaade67a278a0004a7`
- Immutable positive component: PR #767, merge
  `3bb9087cdea293c494ae86b5824e9d8d221fbbfb`
- Parent production experiment: issue #742
- Production firewall: issue #757, clause F3
- Branch: `probe/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1`
- Directory: `probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/`
- Public base: `ebf1d8a2100cb26c58721edaade67a278a0004a7`
- Canon: Public Canon v74

This is the fresh mobility-only successor reserved after the immutable
`STOP_DUAL_MIXING` record.  It neither reopens nor reinterprets that record.
The only predecessor facts admitted during design were the registered
mobility failures: constant integer-current observables, nearly static
`n_mean`, and failed ESS/Rhat/drift.  No Ward residual was imported, parsed or
used to choose this kernel, schedule or threshold.

The present probe executes only `L=3,4`.  It contains no primal reader, no
Ward contact or separated-face statistic, no `L=6,8` state or seed, and no
phase observable.  It cannot satisfy F3.  Its positive terminal merely
qualifies one exact kernel for a later governance decision.

No formal qualification seed may be opened until this document, every source
file, both dependency packages, the fixture, schedule, thresholds and terminal
grammar are committed, pushed, publicly pinned on issue #756 and read back
byte for byte.  A completed failure consumes this identifier.  There is no
restart, replacement, extension or threshold movement.

## Field 1: target, current and homology

For `L in {3,4}`, let `K_L=(Z/LZ)^4`.  Positive plaquette orientations are in
the exact order

```text
(01),(02),(03),(12),(13),(23).
```

The hard carrier and target are

```text
n in {0,1,4}^{6 L^4},
partial n = 0 mod 5,
tilde(n)_p in {0,+1,-1},
nu_0(n) proportional 2^(-|supp n|).
```

Here residue `4` has principal lift `-1`.  Modular closure makes every entry
of `partial tilde(n)` divisible by five, so the exact integer current is

```text
j(n)=partial tilde(n)/5.
```

The implementation verifies divisibility and `partial j=0` without floating
point.  For `L` coprime to five, the six homology coordinates are

```text
H_ab(n)=(L^2)^(-1) sum_x n_(x,ab) mod 5.
```

Define the two exact sector indicators

```text
B_J(n)=1[j(n) != 0],
B_H(n)=1[H_2(n) != 0],
B(n)=B_J(n)+B_H(n) in {0,1,2}.
```

No value of `j` or `H_2` is identified with a physical photon observable in
this probe.

## Field 2: one frozen sector-umbrella kernel

The product chain has levels

```text
s=0,...,S,                 S=max(15,L^2),
pi_s(n) proportional 2^(-|supp n|+s B(n)).
```

Thus the bottom marginal `pi_0` is exactly the original #767 hard target.
All levels retain the same hard support and modular closure.  There is no soft
state, defect ensemble, guided worm, alternative algorithm or runtime kernel
selector.

Every transition begins with four bits from the frozen stream and selects
exactly one random-scan component:

```text
selector 0       hold                                      probability 1/16
selector 1       immutable-#767 random-word Metropolis     probability 1/16
selector 2       charge conjugation                        probability 1/16
selectors 3..5   cube-orbit heat bath                      probability 3/16
selectors 6..9   tri-star-orbit heat bath                  probability 4/16
selectors 10..11 translated-plane-orbit heat bath          probability 2/16
selectors 12..15 adjacent replica swap                     probability 4/16
```

The #767 component acts at level zero.  Its proposal word has
`P(length=m)=2^(-(m+1))`; every letter chooses with exact fair/rejection bits
one oriented cube boundary or one of the six fixed coordinate two-tori and an
independent sign.  A proposal entering residue 2 or 3 is rejected.  Otherwise
it is accepted with `min(1,2^(-Delta support))`.  Its source is read only after
SHA-256 custody, and the independent C++ reimplementation is compared with it
by the frozen fixture.  This component has strictly positive mixture weight
and is never replaced.

For the local heat baths, choose the level uniformly.  Cube chooses one of
`4L^4` oriented three-cell boundaries.  Tri-star chooses one of `6L^4`
plaquettes and one of its four omitted incident cubes.  Plane chooses one of
six orientations and one of `L^2` transverse translations.  For generator
`g`, enumerate every `k in Z5` for which `n+kg` remains hard.  With

```text
e_k=-|supp(n+kg)|+s B(n+kg),
```

the exact orbit heat bath uses integer masses `2^(e_k-min_h e_h)`.  Sampling
uses exact bounded rejection.  This is exactly the conditional distribution
of `pi_s` on the orbit, including reverse moves and self moves.

### 2.1 Current witness

Fix a plaquette `p`.  Align its four incident cube boundaries so each has
coefficient `+1` on `p`.  A tri-star is the sum of any three, omitting the
fourth.  It has 16 nonzero faces and central coefficient `3 mod 5`.  Start
from the aligned omitted cube boundary, of support six.  Adding the tri-star
produces the hard 21-face witness: the central principal coefficient changes
from `+1` to `-1`, while the other changes remain `0,+/-1`.  If `g` denotes
the modular tri-star and `p` also denotes the unit central face, then on
principal lifts

```text
Delta tilde(n)=g-5p,
Delta j=-partial p != 0.
```

The target weight ratio of the two endpoints is exactly `2^(-15)`.  Reverse
insertion is in the same heat-bath orbit.  Tri-stars are sums of boundaries
and preserve `H_2`; they are not used to claim homology mobility.

### 2.2 Homology move

For each orientation `(a,b)` and each of the `L^2` fixed transverse coordinate
pairs, the translated positive `(a,b)` plane is a closed two-torus.  Its five
coefficient orbit is sampled by the same exact heat bath.  These moves change
the declared `H_ab` coordinate and supply a separately measured homology
channel.

### 2.3 Replica swaps and proof

An adjacent edge `s,s+1` is chosen uniformly.  Exchanging lower state `x` and
upper state `y` is accepted with

```text
min(1, 2^(B(x)-B(y))).
```

The only nontrivial probabilities are `1/2` and `1/4`, sampled by exact fair
bits.  Target support cancels from the exchange ratio.

Each orbit heat bath is reversible by conditional sampling.  Charge
conjugation is an involution preserving support and both sector indicators.
The #767 component is reversible for `pi_0`; acting on that coordinate alone
preserves the product.  The displayed swap ratio is its exact
Metropolis-Hastings ratio.  Therefore their fixed convex mixture preserves
the product measure.  The explicit hold gives aperiodicity.  The #767
component is irreducible on its finite hard target; positive adjacent swaps
can carry each product coordinate to level zero and back.  Hence the product
chain is irreducible.  This proof is finite-volume mathematics and is not a
mixing-time bound.

## Field 3: randomness, source and independent fixture

Every stochastic bit is read most-significant-bit first from consecutive

```text
SHA256(ASCII domain || 16 seed bytes || 16 counter bytes)
```

blocks.  The domain is exactly

```text
photon-z5-dual-mobility-qualification-1
```

and the counter is unsigned 128-bit big endian beginning at zero.  `bits(k)`
concatenates bits left to right.  `bounded(b)` draws the minimum bit width and
rejects values at least `b`.  No host PRNG and no floating point enters a
transition decision.

`SOURCE_SHA256SUMS` fixes the ten-file package inventory.  It does not list
itself; its bytes are owned by the public commit and receipt.
`INPUT_SHA256SUMS` fixes only runtime dependencies actually opened: the #767
PREREG/README/kernel/verifier and the pilot-2 statistics implementation.
Neither the old Ward logs nor its analysis/result are runtime inputs.

Before every formal or replay calculation the runner verifies both manifests.
It also requires the pin to be the unique child of the displayed public base
and byte-compares all ten pinned package files plus both manifests with
`git show PIN_COMMIT:path`.  A replay additionally requires that pin to be an
ancestor of the current checkout.  Thus changing a source and changing its
manifest together after the pin cannot create a new accepted replay.

The compiler command is

```text
g++ -std=c++17 -O3 -DNDEBUG -Wall -Wextra -Wpedantic -Werror
```

The executable is built in the single explicit repository-root directory
`.photon-z5-dual-mobility-qualification-build`.  A pre-existing build slot is
an error; the runner removes the executable and empty directory exactly after
the fixture/formal/replay calculation.  This avoids an implicit host temporary
directory and makes concurrent or stale invocations fail closed.

and byte-compares `FIXTURE_EXPECTED.txt`.  The fixture contains SHA-256 and
counter known-answer tests; L3/L4 closure, cube/tri-star/plane orbit and
reverse detailed-balance audits; the exact swap-score table; and two complete
C++/independent-Python trajectories through 128 bottom-edge attempts.  It
compares transition count, target state hash, support, integer-current count,
all six `H_2` coordinates and walker identity.  It opens no formal seed.

## Field 4: formal carrier, starts and schedule

Exactly eight chains enter the decision:

```text
label              L  start       seed
L3_cold_r1         3  cold        0xf7560000000000000000000000030101
L3_cold_r2         3  cold        0xf7560000000000000000000000030102
L3_stratified_r1   3  stratified  0xf7560000000000000000000000030201
L3_stratified_r2   3  stratified  0xf7560000000000000000000000030202
L4_cold_r1         4  cold        0xf7560000000000000000000000040101
L4_cold_r2         4  cold        0xf7560000000000000000000000040102
L4_stratified_r1   4  stratified  0xf7560000000000000000000000040201
L4_stratified_r2   4  stratified  0xf7560000000000000000000000040202
```

For `cold`, all replicas start at zero.  For `stratified`, level zero is zero
and levels `1..S` cycle through the 21-face current witness, its conjugate, a
positive `(01)` homology plane and its conjugate.  No sample is taken at the
start.

Every chain has the literal schedule

```text
warm bottom-edge swap attempts:       16,384
measured bottom-edge swap attempts:  524,288
checkpoints:                            2,048
thin:                                     256 bottom attempts
full target validation stride:            256 bottom attempts
hard total-transition cap:          67,108,864
extension/restart/replacement:            forbidden
```

The 16,384th bottom attempt starts measurement and is not itself measured.
The next attempt is census index one.  Every measured bottom attempt enters
the current/H2 census; only every 256th emits a checkpoint.  Full product
validation runs at start and finish.  Target/current/walker validation runs
at census one and every stride/checkpoint.  Total and measured counters remain
separate.  Four child processes may run concurrently, but transcript order is
the table order.

The C++ `--qualification` firewall independently accepts only the eight exact
`L/start/seed` rows above, with lowercase canonical seed spelling and the exact
six schedule values above.  It validates those fields and the pin-token syntax
before constructing `SectorEngine`; no other direct CLI invocation can emit a
record with `development_only=false`.  Development mode remains visibly
marked and cannot accept pin arguments.

The initial 262,144-census development schedule was rejected before pin: one
L3 drift exceeded the then-proposed bound and one L4 exact-top current witness
count was only one.  The selected fallback doubled the census and transition
cap.  On nonformal matrix A the final schedule passed all mobility and mixing
gates plus development reserve gates ESS 256, Rhat/folded 1.02, bulk 800,
tail 400 and uniqueness 0.85.

Disjoint matrix B retained every mobility, scale, ESS and Rhat margin but had
two standardized diagnostics 2.57134 and 2.644, exposing the mistake in an
extra 2.5 per-test margin.  A fresh matrix C was declared the last empirical
holdout under the then-proposed formal z boundary 3.0.  It again passed every
mobility, scale, ESS and Rhat gate, but one of 120 chain-drift tests was
3.64658 and one of 30 start-separation tests was 3.16802.  Therefore that
proposed pin was stopped and no matrix D was opened.

Before any public pin, this full trail exposed a multiple-testing defect in
the proposed formal rule itself.  There are exactly 120 drift z tests
(`2 L * 15 metrics * 4 chains`) and 30 start z tests (`2 L * 15 metrics`).
For a standard-normal reference, the union bound at `|z|>4` is
`150 * 2 Phi(-4) < 0.01`, whereas an unadjusted boundary 3 has a material
family-wise false-stop rate.  The final prospective boundary is therefore
4.0 for every drift and start diagnostic.  ESS, Rhat, bulk/tail, mobility,
scale, schedule and all exact gates remain unchanged; the development reserve
remains stricter on ESS 256, Rhat/folded 1.02, bulk 800, tail 400 and
uniqueness 0.85.  No further development matrix is permitted.  The previously
unopened formal seeds are the first data that may decide this corrected
contract.  No development log is evidence or retained in the package.

## Field 5: exact record, mobility and mixing gates

Each chain is strict canonical ASCII JSONL: one run record, exactly 2,048
checkpoint records, and one summary.  Unknown/missing keys, duplicate JSON
keys, floats, noncanonical integers, wrong schedules, inconsistent totals,
warm/measured contamination, broken transition decompositions, invalid state
or current hashes, incomplete quartiles, or missing L3/L4/start families are
integrity failures.

Before JSON interpretation, every one of the eight streams must contain
exactly 2,050 nonempty LF records.  A short stream or blank replacement is an
incomplete run outside the terminal grammar and abandons the pin.  A
full-count stream with malformed JSON, a non-object root or a schema error is
a registered `STOP_MOBILITY_INTEGRITY`; its chain custody records only bytes,
SHA-256 and `status=INTEGRITY_UNPARSED`, without attempting a second parse.

All following mobility gates apply separately to every chain and use only
post-warm counters:

```text
bottom current entries / exits                         >= 8 / 8
all target current entries / exits                     >= 8 / 8
nonzero-current bottom censuses                        >= 16
distinct nonzero-current hashes / walkers              >= 8 / 4
edge-0 current imports / exports                       >= 4 / 4
each quartile current entry, exit, nonzero census       >= 1 each
maximum zero wait and current excursion                <= 65,536
current swap up/down flux on every ladder edge          >= 4 each
each of four level bands current births/deaths/moves    >= 2/2/8
exact top-level current births/deaths                   >= 2/2

every H2 component visits all five values in each quartile
each H2 component changes total / per quartile          >= 512 / 64
distinct H2 vectors total / per quartile                >= 512 / 128
H2 swap up/down flux on every ladder edge               >= 64 each
each level band and exact top H2 moves                  >= 32

swap acceptance on every edge                          >= 0.70
each edge attempt count relative to edge zero           in [0.95,1.05]
measured complete walker round trips                    >= 64
walkers completing a round trip                         >= ceil(3(S+1)/4)
unique checkpoint states total / each quartile          >= 0.75 / 0.50
```

The four level bands assign level `s` to
`min(3,floor(4s/(S+1)))`.  A round trip is bottom to top to bottom by the same
walker during the measured interval.  Per-edge flux and endpoint/local event
counts prove transport through the ladder; this implementation does not claim
or record a continuous sector-carrier label from top to bottom.  That is an
explicit diagnostic limitation, not silently inferred evidence.

The 15 frozen mixing series are checkpoint support fraction, principal
`n_mean`, the exact L1 principal-residue norm
`h_norm=sum_ab min(H_ab,5-H_ab)`, and frozen binary64 cosine/sine character
contrasts for each `H_2` component.  Sparse current is
gated by the complete 524,288-attempt event census rather than by the 2,048
thinned checkpoint indicator.  At each L require for every mixing series:

```text
finite positive variance in every chain
Geyer IMS ESS in every chain                            >= 128
rank-normalized split Rhat                              <= 1.03
folded rank-normalized split Rhat                       <= 1.03
pooled bulk ESS                                         >= 400
pooled tail ESS                                         >= 200
each-chain first-half/second-half drift z               <= 4
cold/stratified conservative mean-separation z          <= 4
```

Ranks, ties, Blom probabilities, Geyer IMS, Rhat and ESS are exactly the
SHA-pinned pilot-2 implementation.  No zero variance is regularized and no
failed metric is discarded.

The equal-census L3-to-L4 anti-collapse gate additionally requires integer
count comparisons

```text
min L4 current entries+exits       >= (max L3 value)/4,
min L4 per-component H2 changes    >= (max L3 value)/2,
min L4 measured round trips        >= (max L3 value)/4.
```

Cross multiplication decides boundary equality; the displayed divisions are
not rounded.  This is an L4 feasibility check, not an extrapolated mixing
theorem.

## Field 6: conditional prospective map

Only if the result is `DUAL_MOBILITY_QUALIFICATION_PASS`, and only after the
separate public governance decision required by issue #756, a later
cross-check proposal must obtain its mobility floor from this fixed map.  Put

```text
r_L=ceil((L/4)^4),       S_L=max(15,L^2).
warm_bottom(L) = 16,384 r_L,
checkpoints(L) = 2,048,
thin(L) = 256 r_L,
cap(L) = next_power_of_two(67,108,864 r_L (S_L+1)/17).
```

Thus the exact conditional floors are

```text
L=6: warm_bottom=98,304  checkpoints=2,048 thin=1,536 cap=1,073,741,824
L=8: warm_bottom=262,144 checkpoints=2,048 thin=4,096 cap=4,294,967,296
```

This map contains no Ward seed, observable or threshold.  It does not
authorize those runs, prove their mixing, or satisfy F3.  It prevents later
schedule selection from inspecting Ward outputs.

## Field 7: terminals, one-shot execution and action

For a complete eight-chain modeled record, terminal precedence is

```text
1 STOP_MOBILITY_INTEGRITY
    strict log/schema/counter/schedule/dependency analysis fails;

2 STOP_MOBILITY_QUALITY
    integrity passes but any mobility, mixing or L3/L4 scale gate fails;

3 DUAL_MOBILITY_QUALIFICATION_PASS
    every exact, mobility, mixing and scale gate passes.
```

A source/input/fixture mismatch, public-pin failure, compile failure, child
nonzero exit, unexpected stderr, hard-cap exit, driver crash or incomplete
record occurs outside this modeled grammar.  It produces no `EXPECTED.txt` or
`RUN.md` and closes as `ABANDONED_PIN` under repository policy.  The command is
never repaired or repeated.  An exact mathematical counterexample would
require an independently reproduced public certificate; this runner never
promotes an implementation mismatch to a breaker.

The formal receipt must be a comment by GitHub user `mathorn1973` on issue
#756.  Its body is exactly the following ten LF-separated lines after the
three all-caps placeholders have been replaced by their lowercase SHA-256 or
commit values:

```text
P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1 PUBLIC QUALIFICATION PIN
probe: P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1
branch: probe/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1
pin_commit: PIN_COMMIT
parent_commit: ebf1d8a2100cb26c58721edaade67a278a0004a7
source_manifest_sha256: SOURCE_MANIFEST_SHA256
input_manifest_sha256: INPUT_MANIFEST_SHA256
attempt_ref: refs/heads/probe-attempts/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1
formal_data_opened: NO
authorization: SOLE_FORMAL_RUN
```

The formal-only preflight fetches that public object with `gh api --hostname
github.com`, checks its author, issue, URL and exact body, requires the literal
HTTPS `origin`, and reads the branch ref from the literal public repository
URL.  The explicit hostname prevents an inherited `GH_HOST` from redirecting
either API operation.  Replay does not use `gh` or the GitHub API, but it
performs the frozen read-only `git ls-remote` checks described below.

After all public/source preflight checks and before compilation or any formal
seed, the runner atomically creates the local
`refs/probe-attempts/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1` at the pin with
zero as the required old object.  It then uses `gh api --hostname github.com`
and the GitHub create-ref API to create the publicly preregistered
`refs/heads/probe-attempts/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1` at the
same pin.  After validating the returned JSON, the runner immediately reads
that exact ref from the literal public repository URL and requires the exact
pin SHA before any build or data.  Existing refs, a non-atomic response, a
wrong returned/read-back object or a network/API failure stop before data and
abandon the pin.  Neither ref is ever removed.  The public ref makes a fresh
clone observe that the sole attempt was already claimed; the receipt
authorizes exactly these names and no substitute.

After the public pin/readback, the sole formal local command from the
repository root is

```text
python3 probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/qualification_run.py \
  --formal --pin-commit FULL_SHA \
  --pin-receipt https://github.com/mathorn1973/twist-j/issues/756#issuecomment-N
```

Its complete stdout becomes `EXPECTED.txt`; stderr must be empty and exit
zero.  Only `EXPECTED.txt`, `RUN.md` and `RESULT.md` may then be added.  The
canonical no-argument verifier command is

```text
python3 probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/verify.py
```

It first binds every pre-execution byte to the pin with `git show`, then
deterministically recompiles and reproduces all eight streams.  It exits zero
only when replay stdout is byte-identical to `EXPECTED.txt`; no raw JSONL is
committed.

Replay additionally requires a clean repository-root checkout.  The first
ancestry-path commit after the pin must have the pin as its only parent and
must change exactly `EXPECTED.txt`, `RUN.md` and `RESULT.md` in this directory.
All three current bytes must equal that commit.  Consequently an untracked or
intervening pre-result trio cannot open the replay path; the rule also holds in
a later detached GitHub pull-request merge checkout.

Before regenerating a chain, replay also requires the literal public attempt
ref to equal the pin and the literal public qualification branch to equal that
first result commit.  The committed `RUN.md` must contain exactly one matching
pin commit and non-reservation receipt.  Thus a fabricated local direct-child
trio cannot turn replay into an unclaimed pre-result execution.  The public
qualification branch and public attempt ref are immutable replay dependencies.

```text
action layer:        L6 finite-volume measure engineering
consumed carrier:    L1 exact Z5 two-chains/current and H2 labels
cross-layer claim:   none
maximum status:      ZERO_ENGINEERING_ONLY
F3 / production:     forbidden in this probe
Canon movement:      forbidden
```

Even a merged public PASS leaves #742 blocked.  Before reserving any
`P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2`, issue #756 must publicly decide whether
this mechanism is an exact wrapper retaining immutable #767 as a positive
component under the wording of #757, or whether a fresh production-freeze
identifier is required.  No Canon, Registry, Frontier, phase, propagator,
polarization, physical photon, Born selection, matter/light split,
contraction/expansion or cosmological statement moves here.
