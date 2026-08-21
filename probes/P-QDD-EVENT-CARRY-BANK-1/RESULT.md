# RESULT. P-QDD-EVENT-CARRY-BANK-1

```text
DECISION: CARRY-BANK-BOUNDARY
FORMAL RESULT: 14/14 ALL PASS
PUBLIC STATUS CHANGE: NONE
O1: OPEN
SAMPLING: NOT PROVIDED BY THE ACTIVE ARCHITECTURE
O2: UNTOUCHED
```

## Exact result

The complete Route A carrier has one zero-support piston, 624 supported
pistons, and exactly 22 reduced LOW-probability contexts. For every context
`p=a/b`, the Euclidean state

```text
c in Z/bZ,
c+a=c'+b e,
e in {0,1}
```

is an exact deterministic event transducer. `e=1` is LOW. For any initial
residue phase, its output is the corresponding cyclic phase of the lower
mechanical word. Zero phase gives

```text
#LOW_p(N)=floor(Na/b)
```

and discrepancy below one.

The product of the 22 residue carriers is an exact schedule-invariant sampler
under arbitrary interleaving of contexts. A context's output depends only on
its own prior invocation count and its own residue coordinate. Updates of
different contexts commute.

The complete deterministic-machine class frozen in the preregistration has
exact state lower bound

```text
B = product_p b_p
  = 19702414515172535913561087541248
  = 2^66 * 3^2 * 7^4 * 11 * 13^2 * 17^2 * 23.
```

The carry bank has exactly B states and reaches the bound. The written
Myhill-Nerode argument proves state minimality, and every reachable minimal
machine in the frozen probability-keyed rank-exact class is isomorphic to the
product carry bank. The finite sweeps are audits of the exact carrier; they are
not substituted for the universal proof.

## Phase boundary

Every one of the B initial phase vectors preserves the exact per-context
frequencies and arbitrary-interleaving invariance. The phase vectors remain
pairwise distinguishable by future context words. Therefore exact weights,
schedule invariance, and state minimality do not select the all-zero ready
state.

## Architecture boundary

The exact bank has bit length 104 and is larger than the 15625-state finite
checkpoint. The active architecture contains the global counter and finite
checkpoint, not this probability-keyed rank vector. Decoder outputs do not feed
`U`; the public fresh-record extension is an L4 no-feedback existence theorem,
not an L5 sampler memory; and the candidate carry-bank layer gate is absent.
A single global counter cannot recover all per-context ranks under arbitrary
interleaving.

Thus the mathematics constructs and classifies an exact deterministic sampler,
but the active architecture does not supply either of its remaining physical
inputs:

```text
1. a typed law saying that the physical sampler context is reduced p_low;
2. a typed ready-state law selecting one initial bank phase, in particular zero.
```

The probe identifies but does not adopt the possible dictionary rows
`QDD-EVENT-CONTEXT-KEY [D candidate]` and
`QDD-EVENT-BANK-READY [D candidate]`.

## Candidate theorem ceiling

After byte-identical public x86_64 and aarch64 replay, a later separate Canon
fold may register at most:

```text
QDD-EVENT-EUCLIDEAN-CARRY             [T]
QDD-EVENT-CONTEXT-BANK                [T]
QDD-EVENT-SCHEDULE-INVARIANCE         [T]
QDD-EVENT-BANK-MINIMALITY             [T]
QDD-EVENT-BANK-PHASE-NONSELECTION     [T]
QDD-EVENT-BANK-ARCHITECTURE-BOUNDARY  [T]
```

## Firewalls

- No O1 physical adoption or closure.
- No O2 result.
- No L6 measure.
- No intrinsic randomness, Bernoulli independence, entropy, Bell, locality,
  no-signalling, or causal statement.
- No claim that Nature keys sampler memory by reduced probability rather than
  full preparation, effect, apparatus, or another context.
- No claim that the finite checkpoint, global counter, or old record already
  implements the bank.
- No Canon, Registry, Frontier, Evidence, Gate, workflow, release, or
  existing-probe change.
