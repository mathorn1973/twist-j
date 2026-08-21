# PREREG. P-QDD-DETERMINISTIC-EVENT-SAMPLER-1

Public lock: issue #512. Base: Public Canon v59, public `main` commit
`307e872d529ed053c972a726c2f456378850e92a`; Canon content commit
`5da6b883defebd8edc470db1e2e7ebde095ef20a`.

```text
LAYER:  L1 exact finite arithmetic and one named L1 to L5 repeated-event protocol.
TARGET: O1 of QDD-INSTRUMENT-APPARATUS [O] only.
MODE:   result-exposed, proof-first; exact finite census plus universal integer proofs.
```

## Authority, correction, and collision declaration

At claim time `STATUS.md` declared Public Canon v59 ACTIVE with tag
`canon-v59`, content commit
`5da6b883defebd8edc470db1e2e7ebde095ef20a`, Canon SHA-256
`7fdea700589a21303109dbb6c33fecd2d8243d0d09184ab9d471f0a59687f641`,
and 314310 Canon bytes. The tag and content commit were both ancestors of the
claimed public `main` base.

The first issue text made one pre-pin counting error. It said that 25 of the
625 piston vectors were zero-support. The correct carrier statement is:

```text
piston carrier:      1 zero-support + 624 supported = 625,
fiber multiplicity:  25 per piston,
checkpoint carrier: 25 zero-support + 15600 supported = 15625.
```

Issue #512 was corrected before this file, branch, accepted verifier, pin, or
formal execution existed. No threshold or route changed after a pin because no
pin existed.

Search before claim found no issue, pull request, branch, probe path, Registry
row, or candidate claim under this identifier. The immediate public boundary
is:

- `QDD-ALGEBRAIC-FACTORIZATION [T]` gives exact Route A occurrence weights.
- `QDD-INSTRUMENT-NONSELECTION [T]` and the v59 apparatus rows address O2,
  physical post-state-law selection, not O1.
- `QDD-U-INDUCED-FINITE-NONSELECTION [C]` classifies exactly its frozen 900
  record-delay pairs and explicitly excludes a global sampling-impossibility
  conclusion.
- `QDD-INSTRUMENT-APPARATUS [O]` keeps O1 as a typed realized-event and
  sampling map and says `SAMPLING NOT PROVIDED`, not `SAMPLING IMPOSSIBLE`.

This probe attacks O1 only. O2 is untouched.

## Result-exposure disclosure

Before the public claim, non-canonical reasoning enumerated the expected 22
probability values, found the denominator ceiling 256, and identified the
lower mechanical word, its cyclic phases, the finite-memory lower bound, the
global-schedule breaker, and a changing-preparation order witness. Those
calculations are discovery context only. They are not public evidence.

The accepted `verify.py` is newly authored. It imports no predecessor verifier,
expected output, run record, or helper. It must be pinned and publicly read back
before its first execution.

## Frozen Route A carrier

The balanced section is

```text
ell(0)=0, ell(1)=1, ell(2)=2, ell(3)=-2, ell(4)=-1.
```

For a piston head `p in F_5^4`, write

```text
v = ell(p) in Z^4,
s(v) = v_1+v_2+v_3+v_4,
q(v) = v_1^2+v_2^2+v_3^2+v_4^2,
m(v) = q(v)-s(v)^2/5,
w_low(v) = s(v)^2/20,
w_high(v) = q(v)-s(v)^2/4.
```

These are the public Route A closed forms. On `m(v)>0`, define

```text
p_low(v) = w_low(v)/m(v) = a(v)/b(v)
```

in lowest terms, with `0<=a<=b`, and `p_high=1-p_low`. On `m(v)=0`, the
record is `ZERO_SUPPORT` and no event law is defined.

Since the Gram form is `G=I-(1/5)11^T`, its eigenvalues are
`1,1,1,1/5`; it is positive definite. Therefore `m(v)=v^T G v=0` iff
`v=0`. Exactly one of the 625 balanced pistons is zero-support. The two fiber
coordinates contribute 25 checkpoint states over each piston, giving the
public 25/15600 checkpoint split.

## Frozen event protocol

Fix one supported prepared input `v`, hence one reduced rational `p=a/b`.
Let `r in N_0` count invocations of this same prepared apparatus. Define

```text
L_p(r) = floor((r+1)a/b)-floor(r a/b) in {0,1}.
```

Read `L_p(r)=1` as LOW and `L_p(r)=0` as HIGH. This is the zero-phase lower
mechanical word. Equivalently, the integer residue `ra mod b` emits LOW exactly
when adding `a` crosses `b`.

The protocol freezes the lower convention and the origin `r=0`. It does not
claim that either is already derived from Public Canon v59. No random input,
float, fitted number, post-result threshold change, or hidden offset is
admitted.

## T1. Complete QDD weight census

### Statement

Exact enumeration of all 625 balanced pistons gives:

```text
ZERO_SUPPORT pistons: 1
SUPPORTED pistons:    624
distinct p_low:       22
```

The exact piston-multiplicity table is

```text
0:84
1/256:24
1/176:48
1/136:32
1/96:24
1/56:48
1/46:36
1/26:48
9/224:24
1/16:56
9/104:24
2/17:24
9/64:24
5/32:8
1/6:24
2/7:24
5/16:24
3/8:16
5/8:8
9/14:12
49/64:8
1:4
```

The reduced denominator set is exactly

```text
{1,6,7,8,14,16,17,26,32,46,56,64,96,104,136,176,224,256}.
```

The maximum denominator is 256. Multiplication by the 25 fiber states gives
25 zero-support and 15600 supported checkpoints.

### Proof status

This is a complete finite exact census. The verifier visits every piston and
uses `Fraction`; there is no sampling or approximation. The two-architecture
public workflow is required before any later T registration.

## T2. Lower mechanical sampler theorem

For every reduced `p=a/b` in the census:

```text
sum_(r=0)^(N-1) L_p(r) = floor(Na/b).
```

**Proof.** The sum telescopes:

```text
sum [floor((r+1)a/b)-floor(ra/b)]
  = floor(Na/b)-floor(0)
  = floor(Na/b).
```

Therefore

```text
0 <= Na/b - #LOW(0,...,N-1) < 1.
```

For every start `t`, a block of length `b` has exactly `a` LOW events:

```text
sum_(r=t)^(t+b-1) L_p(r)
  = floor((t+b)a/b)-floor(ta/b)
  = a.
```

The word has period `b`, because adding `b` to `r` adds the integer `a` to both
floor arguments. If `0<a<b` and a smaller positive period `d` existed, one
period would have an integer LOW count `c` with

```text
c/d = a/b.
```

Since `gcd(a,b)=1`, `b` divides `d`, impossible for `0<d<b`. Thus the least
period is exactly `b`. The endpoint words `p=0,1` are constant.

The cumulative count law uniquely determines every bit by first difference.
Thus the lower word is unique after the zero-phase lower rule is frozen. This
is not uniqueness from the weight alone.

## T3. Event-phase nonselection

For an interior reduced `a/b`, the word has least period `b`, so its `b` cyclic
shifts are distinct. Every shift has the same exact count `a` in each period
and the same asymptotic frequency `a/b`.

Therefore an exact Born weight does not determine the realized event at
invocation zero. Selecting the frozen lower word requires both:

```text
counter origin r=0,
lower-rounding convention.
```

This is a theorem-level nonselection boundary. No randomness claim is made.
Across the 20 interior QDD probabilities, the exact number of distinct cyclic
phases in this frozen family is 1372.

## T4. Finite-memory lower bound

Let a deterministic autonomous finite-state sampler on one fixed input start
on a state cycle of length `L`, and let its cycle contain `c` LOW outputs. If
its reduced LOW frequency is `a/b`, then

```text
c/L = a/b,
```

so `aL=bc`; `gcd(a,b)=1` implies `b|L`. Hence `L>=b`, and the persistent state
set has at least `b` elements. In particular a realization of the frozen
least-period word needs at least `b` persistent states.

The QDD census contains `p_low=1/256` on 24 pistons. Therefore every universal
sampler in this restricted finite-state-cycle class needs at least 256
persistent states.

The v59 J-simplex apparatus uses a binary pointer and a five-token phase-memory
label register, giving 10 basis labels. If persistent sampler memory is
restricted to those labels alone, with no system carrier, global counter,
local invocation count, or appended-record count, 10 states cannot realize the
full QDD denominator census.

This is a restricted no-go. It does not exclude any larger or differently
typed architecture.

## T5. Local counter and global schedule theorem

Distinguish:

```text
r_local   local apparatus invocation count,
n_global  public autonomous counter,
N_record  number of appended result records.
```

If `r_local=N_record`, gaps in `n_global` do not alter the word: the `j`-th
invocation always uses `L_p(j)`. This is schedule invariance by invocation
order.

If one substitutes `n_global` for `r_local`, consecutive ticks reproduce the
mechanical word, but arbitrary subsequence scheduling destroys its frequency.
For every nonconstant periodic binary word, both sets

```text
S_LOW  = {n : L_p(n)=1},
S_HIGH = {n : L_p(n)=0}
```

are infinite. Scheduling only `S_LOW` yields an all-LOW stream; scheduling only
`S_HIGH` yields an all-HIGH stream. Thus a global-counter formula is not
schedule invariant without a separately frozen admissible schedule.

Public Canon v59 makes `D_clock` terminal in functional order, says decoder
outputs do not feed the autonomous update, and does not register a bridge from
apparatus records or `ObservableHistory` to an L4/L5 post-state invocation
counter. Functional terminality may not be strengthened into apparatus memory.
Therefore the exact local-counter sampler is not derived by the current public
architecture.

## T6. Changing-preparation order boundary

For a changing exact probability sequence `p_0,p_1,...`, freeze the natural
carried accumulator

```text
x_0=0,
e_j=1 iff x_j+p_j>=1,
x_(j+1)=x_j+p_j-e_j.
```

Since `0<=x_j<1` and `0<=p_j<=1`, `e_j=floor(x_j+p_j)` and induction gives

```text
sum_(j=0)^(N-1) e_j = floor(sum_(j=0)^(N-1) p_j),
x_N = fractional_part(sum_(j=0)^(N-1) p_j).
```

The cumulative count depends only on the sum, but the realized event word can
depend on order. The exact QDD witness uses the same multiset

```text
{1/256, 2/7, 49/64}.
```

Two orders give

```text
(1/256,49/64,2/7) -> H,H,L,
(49/64,2/7,1/256) -> H,L,H,
```

with the same final residual `99/1792`. Therefore a changing-preparation
protocol requires an independently frozen reset, carry, or state-update law.
It cannot be left implicit.

## Frozen decision routes

```text
MECHANICAL-SAMPLER-BOUNDARY
  T1-T6 pass. Exact Route A weights admit a deterministic integer event word
  after a local invocation count, phase origin, and preparation law are frozen.
  The current public architecture supplies neither the local counter bridge nor
  the changing-preparation rule. O1 remains open and SAMPLING NOT PROVIDED.

O1-CONSTRUCTIVE-CLOSE
  every typed field required by O1, including the realized-event map, counter
  source, phase origin, preparation/reset rule, and public bridge, is already
  present and the exact sampler closes O1 without a new premise.

WEIGHT-F
  the exact carrier count, probability table, denominator set, or checkpoint
  lift differs.

SAMPLER-F
  one floor-count, discrepancy, block-count, period, or endpoint theorem fails.

PHASE-F
  an interior word has fewer than b distinct cyclic phases or one phase has a
  different exact frequency.

MEMORY-F
  a deterministic state cycle shorter than a reduced denominator realizes
  that exact reduced frequency, or the 1/256 and 10-state boundary is false.

SCHEDULE-F
  the local invocation word depends on global gaps, or a nonconstant global
  word is invariant under its LOW-only and HIGH-only subsequences.

STATE-UPDATE-F
  the carried accumulator fails the floor-sum law or the exact order witness.

TYPE-F
  the current public architecture already contains the complete local-counter,
  phase-origin, and preparation bridge contrary to the frozen audit.

STOP
  authority, collision, pin, stale base, accepted-verifier pre-execution,
  accepted-byte mutation, incomplete carrier, unregistered layer lift,
  nondeterministic output, runtime, security, or evidence integrity failure.
```

Scientific negative routes exit zero with exact witnesses. STOP carries no
scientific conclusion.

## Candidate ceilings

After the immutable pin, one formal execution, theorem-grade review, and
byte-identical x86_64/aarch64 replay, a later separate Canon fold may register
at most:

```text
QDD-WEIGHT-DENOMINATOR-CENSUS            [T]
QDD-MECHANICAL-EVENT-SAMPLER             [T]
QDD-EVENT-PHASE-NONSELECTION             [T]
QDD-EVENT-FINITE-MEMORY-LOWER-BOUND      [T]
QDD-GLOBAL-COUNTER-SCHEDULE-NOGO         [T]
QDD-EVENT-COUNTER-ARCHITECTURE-BOUNDARY  [T]
QDD-EVENT-PREPARATION-ORDER-BOUNDARY     [T]
```

The computation audits the finite parts; the written proofs carry the
universal statements. None of these rows by itself closes O1 or supplies a
physical law.

## Frozen fields

```text
EQUATION
  T1-T6 exactly as stated above.

CODE
  probes/P-QDD-DETERMINISTIC-EVENT-SAMPLER-1/verify.py
  Python standard library only; Fraction and integers only; deterministic;
  no input, files, network, randomness, floating point, subprocesses, or
  environment-dependent output.

CARRIER
  all 625 balanced pistons; the exact 22-value probability table; every reduced
  denominator; every prefix through 4b+17; every cyclic block and every smaller
  candidate period; all cyclic phases; every possible state-cycle fraction for
  lengths below 256 against 1/256; three explicit global-gap schedules; every
  ordered triple of the 22 exact probabilities; the exact order witness.

SYSTEMATICS
  result-exposed, proof-first. No dataset, approximation, random sample, fit,
  or external measurement. The lower convention is frozen, not derived. The
  finite-memory no-go is restricted to autonomous cycle memory. The schedule
  no-go allows arbitrary subsequences and therefore does not claim that every
  physical schedule is adversarial. The architecture boundary is a textual
  theorem from the active public Canon and is not upgraded by the verifier.

THRESHOLD
  the scientific routes and failure conditions above. PASS requires the exact
  frozen transcript below, exit 0, empty stderr, and byte identity on required
  architectures. No threshold, phase, reset, or schedule class may move after
  the pin.

LAYER
  L1 exact finite arithmetic plus one explicitly named L1 to L5 event-stream
  construction. No L6 measure, no silent lift.
```

## Frozen accepted transcript

```text
TWIST-J QDD deterministic event sampler probe
Exact arithmetic on ell(F_5)^4; LOW=1, HIGH=0; lower mechanical word at zero phase

PASS 01 CARRIER    pistons 625 = ZERO_SUPPORT 1 + SUPPORTED 624
PASS 02 CHECKPOINT fiber lift gives ZERO_SUPPORT 25 and SUPPORTED 15600 checkpoints
PASS 03 TABLE      exact LOW table has 22 values and piston multiplicity 624
       table      0:84 1/256:24 1/176:48 1/136:32 1/96:24 1/56:48 1/46:36 1/26:48 9/224:24 1/16:56 9/104:24 2/17:24 9/64:24 5/32:8 1/6:24 2/7:24 5/16:24 3/8:16 5/8:8 9/14:12 49/64:8 1:4
PASS 04 DENOMS     reduced denominators 1,6,7,8,14,16,17,26,32,46,56,64,96,104,136,176,224,256; maximum 256
PASS 05 PREFIX     #LOW(0..N-1)=floor(N a/b) and discrepancy < 1 for every audited prefix
PASS 06 PERIOD     interior words have least period b; endpoint words are constant
PASS 07 BLOCKS     every cyclic block of length b contains exactly a LOW events
PASS 08 PHASE      interior weights admit 1372 distinct cyclic phases in total
PASS 09 MEMORY     p_low=1/256 occurs on 24 pistons; no cycle shorter than 256 realizes it; 10 < 256
PASS 10 LOCAL      local invocation word is unchanged by arbitrary audited gaps in the global counter
PASS 11 GLOBAL     LOW-position and HIGH-position subsequences break global-counter schedule invariance
PASS 12 VARIABLE   carried accumulator gives floor(sum p_j) on all 22^3 ordered triples
PASS 13 ORDER      same multiset {1/256,2/7,49/64} gives HHL versus HLH, residual 99/1792
PASS 14 DECISION   MECHANICAL-SAMPLER-BOUNDARY; O1 remains open and SAMPLING NOT PROVIDED

RESULT 14/14 ALL PASS
```

Every gate uses an explicit Boolean condition and contributes to the final
result. `DECISION` runs last and is PASS only if every preceding gate passed.

## Scope firewall

- O2 instrument selection is untouched.
- `SAMPLING NOT PROVIDED` remains the public status unless a later owner-approved
  fold adopts a typed local-counter, phase-origin, and preparation law.
- No intrinsic randomness, independence, Bell, locality, no-signalling, causal,
  SI, force, or decoder-completion claim.
- No L6 measure.
- No global counter is silently renamed as a local invocation count.
- No target data choose a phase, reset, schedule, threshold, or offset after
  execution.
- The 10-label statement is only the restricted pointer-memory-only class. It
  does not exhaust the system carrier, global counter, record, or every
  apparatus architecture.
- No Canon, Registry, Frontier, gate table, workflow, release, or existing
  probe change in this probe.

## Procedure

The public pin must contain exactly this `PREREG.md` and the accepted
`verify.py` together. Before the pin, static AST compilation is allowed but the
accepted verifier may not be executed or imported. After commit and push, read
back the exact branch SHA, both Git blobs, SHA-256 hashes, byte counts, LF
endings, final LF, and bytes. Only then execute the accepted verifier once.

After pin: no amend, rebase, squash, force-push, accepted-byte change, scope
movement, threshold repair, phase change, reset change, or schedule-class
change. `EXPECTED.txt`, `RUN.md`, and `RESULT.md` are result-commit files only.
