# P-KERNEL-Z6-SYNCHRONIZATION-1 preregistration

Status: `PREREGISTERED CANDIDATE / RESULT-EXPOSED / NO FORMAL RUN`

This document freezes one exact L1 proof audit for
`KERNEL-Z6-SYNCHRONIZATION [O]`. It contains no verifier output and earns no
scientific or Canon status. Formal execution is forbidden until this document
and `verify.py` are committed, pushed, and read back from the public remote as
one immutable initial pin.

## Public identity, authority, and action layer

```text
program owner:       KERNEL-Z6-SYNCHRONIZATION [O]
probe:               P-KERNEL-Z6-SYNCHRONIZATION-1
public lock:         issue #160
public lock URL:     https://github.com/mathorn1973/twist-j/issues/160
probe owner:         A. M. Thorn
branch:              probe/P-KERNEL-Z6-SYNCHRONIZATION-1
path:                probes/P-KERNEL-Z6-SYNCHRONIZATION-1/
initial base:        4ac41b4fac3a3794a6e9d5be1e2027d324edb806
Public Canon tag:    canon-v23
content commit:      7830d852229ffc06c9d287d026c8ece290bf339b
Canon SHA-256:       f842b613d6f65fe07ddab92ddbe1fb9fec89217d52b781571b7380281c3fb2b1
Canon bytes:         116017
owner scope SHA-256: abcb22785e37c2fbaae7860856b1ca8762ccc2b4c1b4b50fcf763fb273bbd2e0
normative surface:   OBLIGATION / O / L1 / no gate
scheduler:           DECODER_CORE / ROOT / READY / FORMAL
sole dependency:     DEF-AUTONOMOUS-STATE [REQUIRES]
action layer:        L1 only
```

`CARRY-J-CHECKPOINT [T]` is lineage and the novelty boundary. It is not a
logical dependency. `CENSUS-313 [C]`, `CENSUS-Z5-SHEET [C]`, decoded logs,
and every L2-L6 object are excluded from the premises.

The candidate conclusion and a local analytical proof were public before
this lock in issue #156 and the non-canonical note merged by PR #157. This
probe is a pinned confirmation and adversarial proof audit, not blind
discovery. No equation, carrier, systematic, threshold, output route, or
scope may move in response to the exposed conclusion.

## Falsifier first

A single exact counterexample to any one of S1 through S4 below falsifies the
candidate. In particular, one failed restricted bijection or fixed-time
multiplicity is sufficient. A valid S3 counterexample must certify an exact
eventual period on the complete tail. A valid S4 counterexample must give a
complete finite realization and certify its equations for every `n >= 0`.
A repeated finite window is not an S3 counterexample. A finite-prefix model is
not an S4 counterexample.

A broken registered premise, unresolved index or scope, incomplete symbolic
proof, incomplete finite audit, non-independent route, invalid pin, authority
mismatch, nondeterminism, exception, malformed transcript, nonzero valid-route
exit, nonempty stderr, or cross-architecture byte mismatch is `STOP`. A proof
gap without an exact counterexample is `STOP`, not `FALSIFIED`.

With integrity green, exactly one scientific route is permitted:

```text
PROOF-SURVIVES
    every frozen universal clause, proof node, finite audit, and completeness
    condition passes;

FALSIFIED
    at least one complete exact counterexample is found, independently
    confirmed, and the lexicographically first one is emitted;

STOP
    integrity, authority, proof, audit, pin, or transcript is incomplete.
```

`PROOF-SURVIVES` does not promote `KERNEL-Z6-SYNCHRONIZATION [O]`. Any status
change is a later, separate reviewed Canon fold.

## EQUATION

All arithmetic in this section is in `F_5`. For

```text
psi = (p1,p4,p1p,p4p,q,r)
```

put

```text
X        = F_5^6,
z_6(psi) = p1+p4+p1p+p4p+q+r mod 5,
X_z      = {psi in X : z_6(psi)=z},
X_14     = X_1 union X_4.
```

Every sheet has `5^5 = 3125` states, `X` has `15625` states, and `X_14`
has `6250` states.

Freeze the five coordinate generators exactly:

```text
a(psi) =
    (p4,p1,p4p,p1p,q,r),

b(psi) =
    (-p1p,-p4p,-p1,-p4,-q,-r),

c(psi) =
    (-p1p+2,-p4p+1+r,-p1+2,-p4+1-r,1-q,-r),

d(psi) =
    (2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),

e(psi) =
    (2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).
```

All coordinates are reduced modulo five and

```text
(g_0,g_1,g_2,g_3,g_4) = (a,b,c,d,e).
```

Every generator premise includes

```text
g_i(g_i(psi)) = psi
```

for every `i` and every `psi in X`.

Let

```text
theta_n = s_2(n) mod 2,
i_n     = z_6(psi_n)+2 theta_n mod 5,
U(n,psi_n) = (n+1,g_(i_n)(psi_n)),
F_t(psi)   = g_((z_6(psi)+2t) mod 5)(psi),
E_n(psi_0) = pr_checkpoint(U^n(0,psi_0)).
```

Thus `E_0` is the identity and the update from `E_n` to `E_(n+1)` uses
`theta_n`. For `n >= 1`, define

```text
q_n = 4+2 theta_(n-1) mod 5.
```

The symbol `q_n` is a sheet label, not the checkpoint coordinate `q`.
Replacing `theta_(n-1)` by `theta_n` is a frozen index failure.

The five trace laws are

```text
z_6(a psi) =  z_6(psi),
z_6(b psi) = -z_6(psi),
z_6(c psi) = 2-z_6(psi),
z_6(d psi) = 2-z_6(psi),
z_6(e psi) = 3-z_6(psi).
```

Combining the selector with these laws gives the complete sheet table:

```text
             input sheet z
             0  1  2  3  4

t = 0        0  4  0  4  4
t = 1        2  1  1  3  1
```

Each of the ten displayed restrictions is a bijection between the indicated
input and output sheets.

### S1. Per-sheet synchronization

For every `n >= 3` and every `z in F_5`,

```text
E_n restricted to X_z : X_z -> X_(q_n)
```

is a bijection. Therefore, at every fixed known `n >= 3`,
`E_n:X->X_(q_n)` is exactly five-to-one, with one genesis preimage in each
initial sheet.

### S2. Two-sheet restriction

For every fixed known `n >= 1`, the restrictions from `X_1` and `X_4` are
separate bijections onto `X_(q_n)`. Therefore

```text
E_n restricted to X_14 : X_14 -> X_(q_n)
```

is exactly two-to-one.

All multiplicities in S1 and S2 are fixed-time fiber statements. No
unindexed checkpoint-fiber statement is made.

### S3. Checkpoint non-eventual-periodicity

For every `psi_0 in X`, neither

```text
(z_6(E_n(psi_0)))_(n>=0)
```

nor

```text
(E_n(psi_0))_(n>=0)
```

is eventually periodic.

### S4. No finite autonomous time-homogeneous realization

For every `psi_0 in X`, there do not exist a finite set `S`, a self-map
`H:S->S`, a map `pi:S->X`, and `s_0 in S` such that

```text
pi(H^n(s_0)) = E_n(psi_0)
```

for every `n >= 0`.

S4 excludes only finite autonomous time-homogeneous realizations of a
complete trajectory. It does not select a unique counter, extension, drive,
factorization, or genesis history.

## Frozen symbolic proof certificates

The symbolic proof, not the finite sweep through time six, carries the
all-`n` conclusion.

### P01. Three-step and two-sheet bases

The initial bits are

```text
(theta_0,theta_1,theta_2) = (0,1,1).
```

The complete sheet sets evolve as

```text
n=0: {0,1,2,3,4}
n=1: {0,4}
n=2: {1,2}
n=3: {1}.
```

More strongly, for every initial `z`, the three fixed branch restrictions
compose to a bijection

```text
E_3 restricted to X_z : X_z -> X_1.
```

Since `q_3=4+2 theta_2=1 mod 5`, this is the S1 base. For S2, `theta_0=0`
and the two restrictions

```text
E_1 restricted to X_1 : X_1 -> X_4,
E_1 restricted to X_4 : X_4 -> X_4
```

are separate bijections.

### P02. Four-case induction and fixed-time counting

For `t=theta_(n-1)` and `u=theta_n`, the complete adjacent-bit cases are

```text
t  u    q_n    selector i_n    q_(n+1)
0  0     4          4              4
0  1     4          1              1
1  0     1          1              4
1  1     1          3              1
```

In every case the selected generator restricts to a bijection

```text
X_(q_n) -> X_(q_(n+1)).
```

Composition proves the S1 and S2 induction steps. At a fixed `n`, the five
initial sheets form a disjoint partition of `X`, and the two sheets in
`X_14` are disjoint. Five or two separate bijections onto the same target
therefore give the stated fixed-time multiplicities.

### P03. Self-contained Thue-Morse aperiodicity

Assume that `theta_n` has period `p >= 1` after `N`. Choose arbitrarily
large `k` with `2^k-p >= N`. The indices `2^k-p` and `2^k` differ by `p`.
For `0<p<2^k`, the low `k` bits of `2^k-p` complement those of `p-1`, so

```text
s_2(2^k-p) = k-s_2(p-1),
theta_(2^k-p) = k-s_2(p-1) mod 2.
```

This parity alternates with `k`, while `theta_(2^k)=1`. Hence the assumed
eventual period fails.

The verifier also audits a constructive contradiction for arbitrary inputs
`p>=1,N>=0`. Put

```text
K = bit_length(p+N)+1,
w = s_2(p-1),
k = K + ((K-w) mod 2),
a = 2^k-p.
```

Then `a>=N`, `0<p<2^k`, `s_2(a)=k-w`, `theta_a=0`,
`theta_(2^k)=1`, and `2^k-a=p`. The complement-weight identity is certified
by its zero-width base and the two possible new-bit cases `b=0,1`.

The map `t -> 4+2t mod 5` is injective on `{0,1}`. By S1, the trace from
time three is an injective lag-one recoding of Thue-Morse. The trace is not
eventually periodic. If the checkpoint trajectory were eventually periodic,
its image under `z_6` would be eventually periodic. This proves S3.

### P04. Finite autonomous no-go

If `|S|=m` and `s_0 in S`, then `m>=1`. Among

```text
H^0(s_0),...,H^m(s_0)
```

two states coincide. Determinism of `H` propagates that equality through the
entire later orbit, so the orbit is eventually periodic. Applying the fixed
map `pi` preserves every equality. Its projection is therefore eventually
periodic, contradicting S3. This proves S4.

## CODE

The initial public pin contains exactly this file and one zero-argument
`verify.py` in the reserved probe directory. `PREREG.md` is finalized first.
Its SHA-256 is embedded literally in `verify.py`. The verifier SHA-256, byte
count, Git blob, and line-ending metadata are frozen externally by the same
public commit and remote byte readback. No self-referential verifier-hash
placeholder occurs in this document.

The verifier must:

- use only the Python standard library and exact integers modulo five;
- use no floats or true division;
- use no randomness, network, subprocess, clock, elapsed-time output,
  external file input, filesystem read, or filesystem write;
- use no adaptive range, result-dependent expected value, dynamic import,
  `eval`, or `exec`;
- reject command-line arguments deterministically;
- avoid `assert`, whose behavior changes under optimization;
- never depend on unordered set or dictionary representation in stdout;
- derive the scientific route from computed integrity, counterexample, and
  proof nodes, with no expected scientific decision constant;
- emit LF-only stdout with one final LF and write no stderr on a valid route.

The embedded preregistration hash is an identifier. The verifier does not
read this file or its own source. Pin validation belongs to the external
execution harness.

## CARRIER

The complete finite audit covers:

```text
all 15625 states of X;
all five coordinate generators on every state;
all five independent matrix-affine generators on every state;
involution, image cardinality, and all five trace laws;
all five sheets, each of cardinality 3125;
all ten bit-by-sheet restrictions and their bijectivity;
all five initial sheets separately;
all 6250 states of X_14;
direct E_n evolution for every seed at n=0,...,6;
S1 restricted maps and fixed-time fibers at n=3,...,6;
S2 restricted maps and fixed-time fibers at n=1,...,6;
the three-step base and both separate S2 base maps;
all four abstract adjacent-bit induction cases.
```

There is no external dataset. The sweep through `n=6` is a regression. It
does not replace the all-`n` proof.

## SYSTEMATICS

Two logically distinct exact routes are frozen:

1. `DIRECT`: literal coordinate generators and direct state evolution over
   all `15625` checkpoints;
2. `SHEET`: independently encoded matrix-affine generators, independently
   constructed sheets, the complete sheet automaton, cardinalities, bases,
   and four-case reconstruction without calling the direct evolution route.

The coordinate and matrix-affine generators must agree on every state. This
is an integrity cross-check, not a license for the two proof routes to share
an evolution helper. A route disagreement is `STOP`.

The aperiodicity audit checks the displayed universal complement and parity
argument plus deterministic constructive controls. No finite range of
periods is represented as a proof. The finite-state audit checks the
displayed pigeonhole implication plus exhaustive small-map controls. No
enumeration of small maps is represented as a proof for arbitrary finite
`S`.

Independent pre-pin review must cover authority, source, scope, security,
integer exactness, carrier completeness, proof completeness, determinism,
transcript grammar, and an adversarial attempt to construct a counterexample.

## THRESHOLD

Integrity is decided before science.

```text
PROOF-SURVIVES
    all S1-S4 proof obligations, both exact routes, the complete finite
    carrier, and transcript conditions pass;

FALSIFIED
    integrity passes and one exact counterexample to S1-S4 is emitted
    completely;

STOP
    any premise, authority, index, scope, proof, carrier, independence, pin,
    execution, or transcript condition is incomplete.
```

If several scientific failures are found, the verifier sorts their complete
ASCII encodings and emits exactly the first. A valid `PROOF-SURVIVES` or
`FALSIFIED` route exits zero and writes empty stderr. An explicit `STOP`
exits one. `STOP` has priority over `FALSIFIED`. A STOP seals the pin and
authorizes no repair or rerun under this probe name.

## Frozen stdout grammar

The verifier emits exactly the following ordered line forms. Decimal fields
are computed audit counts. Every status token is `PASS` or `FAIL`.

```text
P-KERNEL-Z6-SYNCHRONIZATION-1 exact verifier
authority base=<40 lowercase hex> owner_scope=<64 lowercase hex>
prereg sha256=<64 lowercase hex>
I01 RUNTIME arguments=<decimal> environment=<decimal>: <status>
I02 CARRIER states=<decimal> sheets=<decimal> sheet_size=<decimal> x14=<decimal>: <status>
I03 GENERATORS coordinate=<decimal> affine=<decimal>: <status>
A01 SHEET-TABLE transitions=<decimal>: <status>
A02 BRANCH-BIJECTIONS restrictions=<decimal> states=<decimal>: <status>
D01 DIRECT trajectories=<decimal> times=<decimal>: <status>
D02 FIXED-TIME s1_maps=<decimal> s2_maps=<decimal> fibers=<decimal>: <status>
P01 BASE s1=<decimal> s2=<decimal>: <status>
P02 INDUCTION adjacent_cases=<decimal>: <status>
P03 APERIODICITY symbolic_nodes=<decimal> controls=<decimal>: <status>
P04 FINITE-STATE symbolic_nodes=<decimal> controls=<decimal>: <status>
R01 ROUTE-AGREEMENT direct_and_sheet: <status>
SCOPE L1 only; fixed-time fibers; no autonomous-state completion
counterexample: NONE | <complete deterministic ASCII counterexample>
diagnostic: NONE | <deterministic STOP code>
run integrity: PASS | FAIL
scientific decision: PROOF-SURVIVES | FALSIFIED | STOP
route: PROOF-SURVIVES | FALSIFIED | STOP
```

No expected stdout or expected scientific route is frozen. The first three
identity lines and the scope line are literal. Normal completion emits all
twenty-one lines, in this order, with LF separators and one final LF.
Unexpected internal exceptions are converted to the same twenty-one-line
`STOP` grammar using only the exception class in the diagnostic, never its
message or traceback.

## Formal environment and execution count

After a public remote byte readback explicitly authorizes it, the first
formal leg is exactly one execution from a fresh clean detached checkout on
native Linux/aarch64:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 probes/P-KERNEL-Z6-SYNCHRONIZATION-1/verify.py
```

The return must record UTC start and finish, the exact command and
environment, pre-run and post-run clean status, stdout, stderr, exit, byte
counts, SHA-256 values, final-byte metadata, and the single route. No PR is
opened before that return. A later GitHub Linux/x86_64 leg must execute the
byte-identical pin and reproduce byte-identical stdout.

Before the public readback authorization there is no execution count to
spend. Static source and in-memory AST or compile review is allowed. Import,
`py_compile`, or any execution of `verify.py` is forbidden.

## LAYER and scope firewall

This probe is L1 only. It does not:

- make `F_5^6` the complete autonomous state;
- import a census premise or assign census meaning to `X_14`;
- make an unknown-time or unindexed checkpoint-fiber claim;
- add a decoded log or event log as state;
- select a genesis history, counter, drive, extension, or factorization;
- derive physical irreversibility or an arrow of time;
- prove a decoder total, unique, canonical, or complete;
- classify gauge, a reading quotient, or metrology;
- lift any statement to L2-L6;
- edit Canon, registry, frontier, gates, status, workflow, or release files.

The initial pin adds no `EXPECTED.txt`, `RUN.md`, `RESULT.md`, checker,
transcript, or other probe file. Any defect discovered in either immutable
initial-pin file invalidates this probe name.

## Pre-pin declaration

No formal verifier execution or import occurred before this preregistration
pin. The public prior analytical conclusion is disclosed above. The accepted
verifier is reviewed only statically before its bytes become public.
