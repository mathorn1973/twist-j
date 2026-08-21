# PREREG. P-QDD-EVENT-CARRY-BANK-1

Public lock: issue #516. Base: Public Canon v59, public `main` commit
`a25e2c640295962a7983f16d940347b2b7c1525e`; Canon content commit
`5da6b883defebd8edc470db1e2e7ebde095ef20a`.

```text
LAYER:  L1 exact arithmetic and one named L1 to L5 deterministic event protocol.
TARGET: O1 of QDD-INSTRUMENT-APPARATUS [O] only.
MODE:   result-exposed, proof-first; exact finite carrier plus universal automata proofs.
GATE:   GATE-L1-L5-QDD-EVENT-CARRY-BANK, candidate only, absent from canon/GATES.tsv.
```

## Authority and collision declaration

At lock time `STATUS.md` declared Public Canon v59 ACTIVE with tag
`canon-v59`, content commit
`5da6b883defebd8edc470db1e2e7ebde095ef20a`, Canon SHA-256
`7fdea700589a21303109dbb6c33fecd2d8243d0d09184ab9d471f0a59687f641`,
and 314310 Canon bytes. The tag and content commit are ancestors of the base.
The five normative hashes in `canon/SHA256SUMS` agree with the active release.

`STATUS.md`, `POLICY.md`, `AGENTS.md`, `canon/CORE.md`,
`canon/FRONTIER.md`, `canon/GATES.tsv`, the QDD section of
`canon/CANON.md`, and the immediate predecessor probe were read from public
`main` before this claim.

Search found no issue, pull request, branch, probe path, Registry row, or
candidate claim under `P-QDD-EVENT-CARRY-BANK-1` or the candidate row names
below. This probe owns exactly

```text
branch: probe/P-QDD-EVENT-CARRY-BANK-1
path:   probes/P-QDD-EVENT-CARRY-BANK-1/
owner:  A. M. Thorn / qdd-event-carry-bank-20260821
```

The immediate predecessor is merged
`P-QDD-DETERMINISTIC-EVENT-SAMPLER-1`, pin
`2be3c0426791921a258e9354c4694c49d03f607a`. It proves the exact fixed-context
lower mechanical word, the 22-value QDD probability table, denominator ceiling
256, phase nonselection for one context, the global-counter schedule no-go,
and the changing-preparation order boundary. It does not supply a
schedule-invariant multi-context memory, a context key, a ready phase, or a
public L1-to-L5 gate.

## Result-exposure disclosure

The predecessor exposes the complete probability table and the fixed-context
result. Before issue #516, non-canonical reasoning identified the expected
probability-keyed product carry bank, the product-state lower bound, the
minimal-machine classification, and the remaining context-key and ready-state
boundary. Those calculations and formulations are discovery context only and
are not evidence.

The accepted `verify.py` is newly authored. It imports no predecessor verifier,
expected output, result, run record, or scratch helper. Static parsing is
allowed before the pin. Importing or executing the accepted verifier before the
public pin and readback is STOP.

## Frozen Route A context alphabet

The balanced section is

```text
ell(0)=0, ell(1)=1, ell(2)=2, ell(3)=-2, ell(4)=-1.
```

For a piston head `x in F_5^4`, put

```text
v      = ell(x) in Z^4,
s(v)   = sum_i v_i,
q(v)   = sum_i v_i^2,
m(v)   = q(v)-s(v)^2/5,
w_low  = s(v)^2/20,
w_high = q(v)-s(v)^2/4.
```

On `m(v)>0`, define the reduced Route A probability

```text
p(v)=p_low(v)=w_low/m=a(v)/b(v),  gcd(a,b)=1, 0<=a<=b.
```

On `m(v)=0`, the piston is `ZERO_SUPPORT` and carries no event context.
Positive definiteness of `G=I-(1/5)11^T` makes the zero piston the only
zero-support piston.

The exact supported piston table is frozen as

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

There are 22 distinct contexts. Their denominator multiset in that order is

```text
1,256,176,136,96,56,46,26,224,16,104,17,64,32,6,7,16,8,8,14,64,1.
```

The sum of the coordinate sizes is 1374. The product is

```text
B = product_p b_p
  = 2^66 * 3^2 * 7^4 * 11 * 13^2 * 17^2 * 23.
```

The accepted verifier computes and prints the exact integer B from the frozen
carrier. The factorization, not a decimal approximation, is the frozen value.

## T1. Euclidean carry transducer

For each context `p=a/b`, define the residue carrier

```text
C_p={0,1,...,b-1}=Z/bZ.
```

For residue state `c in C_p`, Euclidean division of `c+a` by b gives unique
`e in {0,1}` and `c' in C_p` with

```text
c+a=c'+b e.
```

Explicitly,

```text
e=1 iff c+a>=b,
c'=c+a-b e=(c+a) mod b.
```

Read `e=1` as LOW and `e=0` as HIGH. Because `gcd(a,b)=1` for every interior
reduced probability, translation by a is one b-cycle. At `p=0` and `p=1`,
`b=1` and the unique state emits respectively HIGH and LOW.

Starting from residue phase `c_0=phi`, induction gives

```text
c_r = (phi+r a) mod b,
```

and the r-th event is

```text
L_(p,phi)(r)
  = floor((phi+(r+1)a)/b)-floor((phi+r a)/b).
```

The cumulative count telescopes:

```text
sum_(r=0)^(N-1) L_(p,phi)(r)
  = floor((phi+N a)/b)-floor(phi/b).
```

Since `0<=phi<b`, zero phase gives

```text
#LOW_p(N)=floor(Na/b),
0<=Na/b-#LOW_p(N)<1.
```

This is the exact carry form of the predecessor's lower mechanical word. The
predecessor used invocation phase; the present carrier uses the equivalent
Euclidean residue phase. Multiplication by a permutes the b phase labels.

## T2. Probability-keyed carry bank

Let `P` be the frozen 22-element context alphabet and define

```text
C_bank = product_(p in P) C_p.
```

For bank state `c=(c_p)` and one input context p, apply the T1 update only to
coordinate p and leave every other coordinate fixed. Denote the transition by
`T_p` and its emitted bit by `E_p`.

For distinct p and q,

```text
T_p T_q = T_q T_p,
```

because the maps act on disjoint coordinates. Their event bits are likewise
independent of the other coordinate.

For a finite schedule

```text
w=p_0 p_1 ... p_(N-1),
```

let

```text
rank_p(j)=|{i<j:p_i=p}|.
```

Induction on j gives

```text
c_p(j)=(phi_p+rank_p(j) a_p) mod b_p,
```

and therefore, when `p_j=p`,

```text
E_j=L_(p,phi_p)(rank_p(j)).
```

Thus the p-subsequence depends only on its own invocation rank. Arbitrary gaps
and interleavings by other probability contexts do not alter it. For every p
and every schedule prefix with `N_p` occurrences of p,

```text
#LOW_p
  = floor((phi_p+N_p a_p)/b_p)-floor(phi_p/b_p),
```

and zero phase gives `floor(N_p p)` with discrepancy below one.

This removes the predecessor's order defect inside the explicitly frozen
probability-keyed bank. It does not prove that reduced probability is Nature's
physical context key.

## T3. State lower bound

Freeze the complete machine class `A_bank`:

```text
M=(S,s_0,{delta_p},{epsilon_p})
```

where S is finite, `s_0 in S`, and each context `p in P` supplies a deterministic
transition `delta_p:S->S` and one emitted bit `epsilon_p:S->{0,1}`. The required
rank-exact law is:

```text
for every finite input word w and next context p,
the next output equals L_(p,0)(N_p(w)),
```

where `N_p(w)` is the number of p letters in w. No commuting-transition
hypothesis is assumed.

For one interior p, the lower mechanical word has least period b. Hence its b
cyclic tails are pairwise distinct. If two residue vectors

```text
r,s in product_p Z/b_p Z
```

differ at coordinate p, some future p-only word distinguishes the two tails.
Every residue vector is reachable from the zero state because multiplication
by each reduced numerator `a_p` is a permutation of `Z/b_p Z` and the context
letters can be applied independently. Therefore two different residue vectors
cannot reach the same deterministic machine state: from one state, the same
future input has only one output word.

Consequently every machine in `A_bank` has at least

```text
B=product_p b_p
```

reachable states.

The carry bank has exactly B states and realizes the law, so it is state-minimal.
This lower bound is about the frozen probability-keyed arbitrary-interleaving
class. It is not a lower bound for one fixed probability, a restricted schedule,
an infinite-state machine, or another physical context alphabet.

## T4. Minimal-machine classification

Let M in `A_bank` be reachable and have exactly B states. Associate to every
input word its count-residue vector

```text
r_p=N_p(w) mod b_p.
```

The T3 distinguishability proof shows that the B canonical count-residue
vectors reach B different states. Since M has exactly B reachable states,
count-residue vector to machine state is a bijection. Reading one additional p
letter advances only `r_p` by one and emits the corresponding mechanical bit.
Composing this bijection with `r_p -> a_p r_p mod b_p` intertwines every
transition and output with the Euclidean product carry bank.

Hence every reachable state-minimal machine in the frozen class is isomorphic
to `C_bank`. This is a classification up to deterministic-machine isomorphism,
not a physical uniqueness theorem.

## T5. Phase nonselection

For every phase vector

```text
phi in C_bank,
```

use phi as the initial bank state. T1 and T2 show that all B choices preserve
exact per-context frequencies, discrepancies, and arbitrary-interleaving
invariance. T3 shows the phase vectors are pairwise distinguishable by future
context words.

Therefore

```text
exact weights
+ arbitrary-interleaving invariance
+ state minimality
```

do not select the all-zero ready state. The zero vector is one additional
ready-state convention. No post-result phase choice is allowed.

## T6. Current architecture boundary

The active public architecture says:

```text
Omega=N_0 x F_5^6,
```

with one global counter and a 15625-state finite checkpoint. Decoder outputs do
not feed the state update. `QDD-FRESH-RECORD-EXTENSION [T]` is an L4 reversible
fresh-cell existence theorem and explicitly not an L5 event stream, sampling
law, or `D_clock` identification. `canon/GATES.tsv` contains no
`GATE-L1-L5-QDD-EVENT-CARRY-BANK`.

The complete bank has B states and

```text
B > 5^6=15625.
```

Therefore the finite checkpoint alone cannot carry the complete minimal
22-context bank. A full append-only schedule can reconstruct all context ranks
only if a new history-to-apparatus feedback bridge is admitted; the published
fresh-record no-feedback class does not provide one. A single global counter
cannot recover the vector of per-context ranks under arbitrary interleaving.

The probe may identify, but does not adopt, the physical dictionary candidates

```text
QDD-EVENT-CONTEXT-KEY [D candidate]
  the sampler context is the reduced Route A probability p_low;

QDD-EVENT-BANK-READY [D candidate]
  a prepared apparatus carries the all-zero probability-keyed carry bank and
  preserves it across interleaved invocations.
```

The T statements do not earn either D row. They also do not register the
candidate layer gate.

## Frozen decision routes

```text
CARRY-BANK-BOUNDARY
  T1-T6 pass. The probability-keyed carry bank is an exact schedule-invariant
  and state-minimal deterministic sampler for all 22 weights, but the active
  architecture supplies neither the physical context-key law nor the ready
  phase. O1 remains open and SAMPLING NOT PROVIDED.

O1-CARRY-BANK-CLOSE
  the active public architecture already contains a complete typed context key,
  all-zero ready state, persistence law, and registered L1-to-L5 gate, with no
  new physical premise.

CARRIER-F
  the 625-piston carrier, 22-value table, denominator multiset, or factorization
  differs.

CARRY-F
  one Euclidean identity, cycle, shifted-word, or cumulative-count statement
  fails.

INTERLEAVING-F
  one context subsequence changes under an interleaving or distinct-context
  updates fail to commute.

MINIMALITY-F
  two residue vectors are future-output equivalent or a smaller machine in the
  complete frozen class realizes the rank-exact law.

PHASE-F
  one phase changes the exact frequency or two claimed distinguishable phases
  have identical future output.

ARCHITECTURE-F
  the active public architecture already contains the frozen bank carrier,
  context key, ready state, feedback bridge, and registered gate contrary to
  the source audit.

STOP
  authority drift, collision, stale base, accepted-verifier pre-execution or
  import, post-pin byte mutation, incomplete context alphabet, hidden context
  choice, unregistered layer strengthening, nondeterminism, runtime, security,
  or evidence-integrity failure.
```

Scientific negative routes exit zero with exact witnesses. STOP carries no
scientific conclusion.

## Candidate theorem ceiling

After one immutable public pin, one formal execution, theorem-grade review, and
byte-identical x86_64/aarch64 replay, a later separate fold may register at
most:

```text
QDD-EVENT-EUCLIDEAN-CARRY             [T]
QDD-EVENT-CONTEXT-BANK                [T]
QDD-EVENT-SCHEDULE-INVARIANCE         [T]
QDD-EVENT-BANK-MINIMALITY             [T]
QDD-EVENT-BANK-PHASE-NONSELECTION     [T]
QDD-EVENT-BANK-ARCHITECTURE-BOUNDARY  [T]
```

All are restricted to the declared probability-keyed L1/L5 protocol. No row
closes O1 by itself.

## Frozen fields

```text
EQUATION
  T1-T6 exactly as stated above.

CODE
  probes/P-QDD-EVENT-CARRY-BANK-1/verify.py
  Python standard library only; integers and Fraction only; deterministic;
  read-only access to the inherited public Canon files for T6; no randomness,
  floating point, network, subprocess, environment-dependent output, or write.

CARRIER
  all 625 balanced pistons; the exact 22-value context table; every phase state
  of every context; every ordered pair of distinct contexts and every
  two-coordinate phase state; every schedule of length at most four at zero and
  one nonzero bank phase; all cyclic tails; exact denominator product and prime
  factorization; the active CORE, CANON, FRONTIER and GATES source clauses.

SYSTEMATICS
  result-exposed, proof-first. Finite sweeps audit the exact carrier. T3 and T4
  are universal deterministic-automata proofs and do not derive theorem status
  from a truncated schedule sweep. The input alphabet is exactly the reduced
  LOW probability, not full preparation or effect context. No L6 measure,
  independence, entropy, or randomness statement is in scope.

THRESHOLD
  the routes and failure conditions above. No tolerance. Audit PASS requires
  exit 0, empty stderr, exact frozen transcript labels, and byte identity on the
  required architectures.

LAYER
  L1 exact arithmetic plus one explicitly named candidate L1-to-L5 event
  protocol. The gate is not registered or passed by this probe alone.
```

## Frozen transcript grammar

The accepted verifier emits exactly fourteen labeled gates in this order:

```text
CARRIER
CONTEXTS
CARRY
CYCLES
FIXED
COMMUTE
INTERLEAVE
BANKSIZE
TAILS
MINIMAL
PHASE
CHECKPOINT
ARCH
DECISION
```

The computed exact integer B, pair-state count, schedule count, and bit length
are report fields determined by the pinned verifier. The terminal route is
`CARRY-BANK-BOUNDARY` unless a frozen scientific falsifier fires. No output
value may be repaired after pin.

## Scope firewall

- O2 is untouched.
- No intrinsic randomness, Bernoulli independence, entropy, Bell, locality,
  no-signalling, or causal claim.
- No claim that Nature keys sampler memory by reduced probability rather than
  full preparation, effect, apparatus, or another context.
- No claim that the finite checkpoint, global counter, or old record already
  implements the bank.
- No target data may choose a phase after execution.
- No Canon, Registry, Frontier, Evidence, Gate, workflow, release, or
  existing-probe edit in the probe pull request.
- One probe, one branch, one directory. No amend, rebase, squash, force-push,
  threshold move, or reuse after pin.

## Formal procedure

1. Commit and push this file and the newly authored accepted `verify.py`
   together as the immutable pin.
2. Read back the exact branch SHA, both Git blobs, SHA-256 hashes, byte counts,
   LF endings, and decoded bytes from public GitHub.
3. Execute the pinned verifier exactly once from repository root.
4. Add only `EXPECTED.txt`, `RUN.md`, and `RESULT.md`, without changing either
   pinned file.
5. Open one probe-only pull request and require byte-identical x86_64 and
   aarch64 replay plus aggregate `check`.
6. Merge any valid scientific or falsified route by merge commit only.
