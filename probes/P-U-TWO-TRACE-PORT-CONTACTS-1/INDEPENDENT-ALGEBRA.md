# Independent symbolic check of trace exchange and two carry contacts

2026-10-04, NON-CANONICAL L1. This note checks the coordinator's disclosed
equations before exposure to the construction implementation. No new
construction code has been read, imported or run. The complete construction
contract was not yet available when this derivation was written, so this
is a review of the exact algebra below, not an acceptance of an unseen
contract or a two-architecture result. The #987 carry mechanism is prior
work, not a new claim here.

## Declared exchange

For one receiver checkpoint `(P,q,r)` put `kappa=sum(P)` and
`z=kappa+q+r`. For an additional source slot `s in F5` define

    C(s,P,q,r)=(kappa+q+r, P, s-kappa-r, r).

The source slot on the right is the old total trace; the receiver's new
total trace is s. P and r are preserved. Applying C twice returns the
source slot and all six receiver coordinates exactly: the second new q
is `(kappa+q+r)-kappa-r=q`. Thus C is one fixed bijection/involution on
the full seven-coordinate carrier, not a source-dependent choice of map.
It changes no clock variable. Availability of C is an added assumption;
it is not an operation derived from the unchanged U.

## Three native ticks from the declared ready class

Let `A=p1+p1p`, `B=p4+p4p` in F5. The exact native generator equations
give

| Generator | (A',B') |
| --- | --- |
| a | (B,A) |
| b | (-A,-B) |
| c | (4-A,2-B) |
| d | (-A,-B) |
| e | (-A,-B) |

The c row follows because its two r contributions in B cancel. Suppose
the incoming receiver satisfies A=B=0. After C its trace equals the
source slot s. For a native driver segment 011 the actual selected words,
in temporal order and source order s=0,1,2,3,4, are

    ace, bbd, cce, dbd, ebd.

These follow from the selector `z+2 theta`, not an externally requested
generator word. Applying the displayed pair maps gives

| s | After the first tick | After the second tick | After the third tick |
| --- | --- | --- | --- |
| 0 | (0,0) | (4,2) | (1,3) |
| 1 | (0,0) | (0,0) | (0,0) |
| 2 | (4,2) | (0,0) | (0,0) |
| 3 | (0,0) | (0,0) | (0,0) |
| 4 | (0,0) | (0,0) | (0,0) |

The fixed piston reader `W(P)=A^2` therefore gives exactly `1[s=0]`
after the three ticks. For canonical input digit a in {0,1,2,3,4}, encode
the source as `s=a+1 mod5`. Then `1[s=0]=floor((a+1)/5)`, the declared
carry predicate. This is a one-bit predicate, not full five-symbol SUM.
No original input, source slot, counter or history is needed by W.

Every branch has total trace one after 011. From any checkpoint of trace
one or four the actual selector chooses only b,d,e for either clock bit,
and the trace stays in {1,4}. Each branch negates A, preserving A^2.
Thus the value written above persists under all subsequent native ticks.
This statement alone does not permit subsequent applications of C to
that same receiver.

## Second receiver's untouched preparation

The declared common initial receiver is `rho=(0,0,0,0,1,0)`. Direct
substitution, without a program, gives the following complete checkpoint
history under uninterrupted U at the common native counter:

| n | Checkpoint | Total trace | Next selected generator |
| --- | --- | --- | --- |
| 0 | (0,0,0,0,1,0) | 1 | b |
| 1 | (0,0,0,0,4,0) | 4 | b |
| 2 | (0,0,0,0,1,0) | 1 | d |
| 3 | (2,1,3,4,0,1) | 1 | b |
| 4 | (2,1,3,4,0,4) | 4 | b |
| 5 | (2,1,3,4,0,1) | 1 | b |
| 6 | (2,1,3,4,0,4) | 4 | e before exchange |

At n=6 this receiver still has A=B=0, with no reset. Its pre-exchange
source slot output is consequently the old trace four. The exchange
changes q to `s-4`, retaining all other receiver coordinates. The actual
native bits at n=6,7,8 are 0,1,1, so the same proved table applies to
the second receiver's new trace s. The entry 'e before exchange' is not
used after exchange; that tick's selector is recomputed from the changed
checkpoint.

## Consequence and pending full-contract checks

If both receivers advance every native tick, C couples only the first
source/receiver at n=0 and only the second at n=6, and the two initial
source digits are independent, then the first reader is the first carry
from n=3 onward and the second is the second carry from n=9 onward. The
second contact does not alter the first receiver at that instant; its
later native ticks preserve its established reader value. This proves
the symbolic two-contact statement for the supplied preparation and
schedule, without consuming a hidden receiver reset.

The source slots, two receiver checkpoints, shared unreset counter,
scheduled applications of the added C, and both ready preparations must
remain explicit resources in the complete contract. The old trace is
retained in each used source slot; C's own bijectivity does not make U
bijective or prove that all source information survives native evolution.
Two allocated receivers are two finite cells, not indefinite reuse of a
single cell. No source acquisition, endogenous trigger, preparation
mechanism, energy, physical locality or occurrence law has been proved.

The algebra above passes. Formal acceptance of the full construction
still requires inspection of its complete frozen carrier, schedule,
controls, output/readiness convention and resource ledger. Any later
finite audit must retain its own distinct preregistration and provenance.
