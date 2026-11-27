# C-H3-READER-ARCHIVE-RESET-N

NON-CANONICAL / NO AUTHORITY. L1 mathematical and finite H3 results.
Reservation #2121 and separately frozen result-exposed successor D.
Public Canon v117 base 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.
Predecessor draft #2120 at 1505baef63e9be942832835e3a81f60d5bc8a02f.
No formal public probe or cross-layer claim.

## 1. Carrier and exact reset contracts

Use O=Z[j], Phi5(j)=0, rho=j^2, J=1+rho, L=1-rho,
h(z)=z conjugate(z). The original H3 update, including its
integral parity and balance guards, is imported from
reproduce/h3-referenced-record/verify.py at the base,
Git blob fd215e24fefbbebf83cf3985d8ebcedd590aa709.
All fields are on 8 by 2 with matching bit initially zero.

The initial source is the entire column zero, with material
half-differences p,3j for p in {1,j,j^2,j^3,j^4}, opposite
rails, both CLK=gs=2J(2-rho), and CORR=(0,gs).
The worker is entire column6. Its working store is the six
material/CLK slots, excluding both communication CORR slots.
The archive sector is the six other columns 1..5,7.
The target predicate is p=j. A full endpoint return of the
source means all eight source slots equal their own initial
values, not merely the input root or its norm. A complete
worker reset similarly requires all eight worker slots.
The weaker store reset requires the six specified slots.
All reset endpoints tested for combined source/worker readiness
are even full cuts, with bit zero. A reset is not by itself
fresh-input operation.

The two exact predecessor preparations used in A are n=-3,l=0,v=0.
Let m=2-rho, a=-3L, b=m*rho+Ja+12J.
Row0 CORR at columns 1..7 is (0,0,0,b,b,b,m*rho+2a);
row1 CORR=gs at every column. Both worker CLK initially equal
g=(6,-2,12,1) in the power basis (1,j,j^2,j^3). Its material
half-differences are (J^-1,J^-1) in the static variant,
and ((1,-1,-1,-1),(1,-1,-1,1)) in the rotating variant.
All other material and CLK are zero. Reader stock is common
to all five p. Full H and linear sums agree across the
input family in each preparation; Q=2630 or 2654.

## 2. A and D1: exact recovery census of the existing device

The literal pinned full-field update and its inverse are
checked for all ten preparations through tick4096.
The predecessor write at tick6, the seven held source returns
through tick100 and first fixed-record loss at full111 are
reproduced. The four negative complete reader histories remain
identical across the entire audited interval.

In the static variant the first complete working-store
return after the write is full111. In the first joint
period the combined even source and store return cuts are

    114,384,758,928.

At the first three there are actual archive sector states
distinguishing exactly the two predicate classes, with
respectively 2,2,1 single raw archive radiation ports
taking distinct values on those classes. At 928 the
entire five-field tuple including the common matching bit
returns to its initial tuple. Its preceding 928 states
(including the initial one) are pairwise distinct.
Therefore the exact joint period is 928, not merely an
observed repeated source cut. Induction by determinism
extends the period forever. At all three nonzero source+store
reset cuts in that period, the complete worker column
is not common across inputs. At 928 the complete source
and worker do reset, but the entire field returns and
the present archive is again identical across inputs.
Thus for this particular static preparation no even
full cut at any time gives simultaneous complete source
and worker initial reset with a retained current archive
record. Nor is there such a cut with the same six-slot
store reset and a different common complete-worker context.
No such universal statement for other preparations follows.

Through 4096 the static variant has 18 combined even
source+store resets, including 14 current two-class
archive records and four complete field returns at
928,1856,2784,3712. The rotating variant first restores
the six-slot worker store at 115 (an odd cut); none of
its even cuts through4096 simultaneously restores source
and store. These are bounded negative results for that
variant, not an all-time period claim.

The first static weak endpoint is t114. The first
lexicographic actual archive port is CORR(5,0):

    negative (7,-2,12,-2),
    positive (1,-5,6,-2).

The port values first change at post-C116. This record
is outside the worker but the worker still has
input-dependent communication stock. Its row0 CORR
at t114 is (7,-2,12,-2) for the negative class and
(1,-5,12,-8) for the positive case. The latter is not
the initial common CORR, and the total eight-slot
worker is not restored.

The complete sector accounts at this endpoint are
computed from actual slots. On the negative class
all three sectors retain their initial sums and H.
On the positive case the source deltas vanish, and
the worker and archive deltas are opposite:

| Sector | Material sum delta | Radiation sum delta | H delta |
|---|---|---|---|
| Worker | 0 | (-6,-3,0,-6) | (132,0,69,69) |
| Archive | 0 | (6,3,0,6) | (-132,0,-69,-69) |

Hence worker scalar Q has increased by 195 and archive
Q decreased by 195. This is a precisely located imbalance
relative to initial sector accounts, not a violation of
global conservation or a physical energy identification.

## 3. B: early separated archive search

B leaves both source and worker initial slots unchanged.
At one archive column it adds common CLK stock G=Rpos+2f
on both rows and neutral material half-differences
(J^-1*f,0). Rpos is the actual positive pre-B CORR
at the frozen candidate cut t=7..24 of the old device.
The candidate f ranges over the 15 nonzero binary
power-basis vectors times 1,3,5. The odd material
difference makes its vertical C refuse before B.
No changed transport or collision guard is used.

The exact early-idle pretest requires B0 at both added
cells for every earlier input and B1 at the selected row
only for p=j at the target. Subsequent native screen
on p=1,j checks actual source/worker history through
t-1, the native write and the continuous fixed
port/reference record until a common even full source
and complete worker reset. The weaker six-slot reset
is also recorded, without promotion.

Across both variants, six columns, and 18 candidate
cuts there are 124 cut rejections on lack of a suitable
two-class incoming value. 92 cuts remain, with 45
candidate stocks each: 4140 tried. Of these 3164 fail
the guard pretest, 976 pass it and all 976 fail the
two-input held-reset screen through the horizon256
(no complete-worker or weaker working-store reset
with the required continuous record). None qualifies
for a conditional full-five continuation. This is
a bounded negative result, not a general no-go for
archive attachment. No frozen threshold is altered.

## 4. D2: native delayed archive at the weak reset cut

D2 was separately preregistered after A/B, before the
late capture pretest and its replay. It selects among
the three qualifying weak static cuts in the first
joint period, 114,384,758, in ascending order, with
the specified archive port order and fixed y=0.
A target cut with an earlier identical incoming
CORR congruent modulo five would be excluded for
a free local C clock by the previous #2120 result.

The first cut and port (114,5) are eligible. At that
port there is no earlier identical incoming value at
the same residue of the five-step clock. The first
tested new stock passes the entire declared continuation.
Use f=j^3 and w=1. The ready archive material pair is
(J^-1*f,J^-1*f+2w), and the initial pair is its
inverse C^114, prepared once before evolution:

    d_init=((1,1,0,1),(1,1,2,1)).

Opposite material rails are retained. The initial CLK
at both archive rows is

    G=Rpos+2f=(1,-5,6,0).

All remaining initial slots, in particular both source
and worker columns and all CORR slots, are unchanged.
Through tick113 the new archive B is idle in both rows,
and the actual source, worker and all CORR histories
are equal to the old device. At 114 the positive
radiation half-difference is f and the positive
material difference is J^-1*f, so the exact native
guard admits B1. All four negative inputs and the
other archive row are idle. The actual archive CLK
at (5,0) is

    G+(J^-1-1)f=(1,-4,7,0) if p=j,
    G otherwise.

Since (J^-1-1)j^3=j+j^2, the positive mark relative
to the adjacent fixed CLK(5,1)=G is exactly j+j^2.
The complete initial accounts are equal across the
five raw-root inputs, including the archive stock,
with Q=2952. At the full114 cut all eight source
slots and all six working-store slots are initial,
the bit is zero, and the archive current states and
complete reader histories distinguish precisely the
two predicate classes. This is an actual native
separate archive write, not just a CORR observation.

The full worker column is still input-dependent:
its two CORR slots have the same residual difference
as in A. The sector account deltas are the same as
the A table above. The new archive B redistributes
its own stock while preserving its sector sums and
H at that local contact. In particular it has not
paid back the residual worker account. The entire
field is audited to 114+256. The exact fixed archive
CLK and reference first fail their continuous hold
at full115 (post-C115 still holds). Within this hold
there is one qualifying weak return, full114, and
no qualifying common-complete-worker or initial
complete-worker return. A later change of the
fixed record is not a proof that every reader
register has lost all information.

No fresh input was inserted or subsequently measured.
This positive result is a working-store reset plus
native separate archive, not reset of the complete
reader or a reusable measuring apparatus.

## 5. C: conserved account and finite-history boundary

At any complete source and worker initial reset,
conservation of the two linear sums and H implies
the remaining archive sector has exactly its own
initial two sums and H. This does not force its
state to be its initial state: there can be distinct
states with equal accounts. But a change of just
one radiation slot with every other radiation slot
unchanged cannot preserve the radiation sum. Such
a local archive mark needs compensating changes
elsewhere in that sector. The actual weak endpoint
above fails the full reset and its two sector
deltas exhibit the compensating transfer exactly.

For any finite H3 geometry with finite fixed total
Q, its admissible raw integer states form a finite
set. For a slot z=sum_(i=0)^3 a_i j^i,
the positive scalar account is

    q(z)=Tr(h(z))/2=(5 sum_i a_i^2-(sum_i a_i)^2)/2
         >= (sum_i a_i^2)/2.

This is the trace Gram form 5I-11^T, whose least
eigenvalue is one. Thus finite total Q bounds every
integer coefficient. The matching bit adds only a
finite factor. Suppose n independently supplied
binary outcomes are all required to remain
distinguishable at the same fixed source/worker
context, with all other degrees of freedom outside
the declared archive reset identically. There must
then be at least 2^n distinct admissible archive
states, by injectivity of the required history
reading. A fixed finite archive cannot retain an
unbounded independent history under these conditions.
This is a conditional counting statement; overwriting,
releasing old records, or transferring information
elsewhere changes that contract. It is not a
thermodynamic law or a minimum physical energy.

## 6. Status and evidence

The finite witnesses and finite exclusions are
candidate-C at L1. The conditional conservation,
finite-history count and periodicity implication
are exact mathematical reasoning within this scope.
No formal computation grade or Canon status claimed.
The separate five-cyclic-coefficient implementation
replays A, D1 and the selected D2 witness, including
its guards, full history, hold and sector accounts.
It does not independently repeat B's bounded search;
architecture replay of that same code is reproduction.
Both implementations are result-exposed, not blind
independent reviewers. No physical measurement,
quantum inference, RH, curvature, native-U equivalence
or unnamed cross-layer lift follows.

The precise next engineering target is an endpoint
that restores both communication CORR slots as well
as the six-slot working store, while retaining a
compensated archive record. A valid next-input
experiment must then be separately declared and tested.
