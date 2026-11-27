# C-H3-CAPTURE-CLOCK-N

NON-CANONICAL / NO AUTHORITY. L1 mathematical and finite H3 results.
Reservation #2119, result-exposed successor diagnostics D and E.
Public Canon v117 base 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.
Predecessor draft #2118, immutable head 873c5cd84d1a4dd059e01915e42df2660e17e850.
No formal public probe or cross-layer claim. All previous failed tests retained.

## 1. Carrier and five-step timing obstruction

Use O=Z[j], Phi5(j)=0, rho=j^2, J=1+rho, L=1-rho,
h(z)=z conjugate(z), T=h(J). The unchanged native H3 law is the
public reproduce/h3-referenced-record/verify.py at the base,
Git blob fd215e24fefbbebf83cf3985d8ebcedd590aa709.
All fields here have size 8 by 2, matching bit initially zero.

For a height-two column, both vertical matching choices are the
same unordered pair. An admitted C preserves the center and
multiplies the difference by rho. It preserves the parity guard,
and its fifth power is identity because rho^5=1. A refused pair
is stationary. If no B has acted on the material and CLK rails
of a reader column, these two pairs therefore repeat with period
dividing five at pre-B cuts, independently of incoming CORR.
In particular, for a common initial preparation, an earlier
identical incoming CORR at the fixed row and the same tick
residue modulo five gives precisely the same local B inputs
as the desired write, even on another member of the input
family. No such freely rotating local clock can postpone the
first write to the later cut while keeping every earlier B idle.
This is a conditional obstruction, not a general clock no-go.

A replays the predecessor's 143 successful raw-root stocks and
all 202 recorded source-return/record times from the immutable
B.txt input. The original source column, full accounts and
two-class reader histories are rechecked. The copied B_PREV.txt
is the exact predecessor transcript, not a new independent
result. It is included as the bounded input roster for replay.

All 202 target positive CORR values occurred earlier at the
same port in at least one of the five histories. For 183 there
is also an earlier occurrence congruent modulo five; all 143
earliest qualifying times have such an occurrence. The
remaining 19 do not have a same-residue occurrence in this
test. Thus the five-step obstruction applies to the earliest
targets, and not to every later target. EXPECTED.txt records
the actual earliest witnesses.

## 2. B: capture early, then restore the equal-account source

Use the raw-root source of #2118 B, not the original moving
8-by-8 two-track motor. Let m=2-rho and gs=2Jm.
At column zero the material half-differences are (p,3j),
p in {1,j,j^2,j^3,j^4}, with opposite material rails.
Both source CLK are gs; source CORR is (0,gs).
The common reader row-one CORR is gs in all eight columns;
the initial row-zero reader CORR at columns 1..7 is

    (0,2v,2v,b,b,b,m*rho+2a),
    a=n*L*j^l, b=m*rho+J*a-4J*n*j^l.

B restricts the old stock family to v=0. The previously
frozen parity filter is unchanged. For each admitted stock
the pre-B CORR observations of the original five histories
determine candidate capture cuts at the fixed port (6,0)
during ticks 3..12. No other port or output definition is
selected. Candidate ready material pair at column6 is

    D_ready=(J^-1*f,J^-1*f+2w),

where f is a nonzero binary-coefficient power-basis element
times 1,3 or 5, and w is a signed fifth root. Initialize the
pair by inverse C^t of D_ready, and both CLK by g=Rpos+2f,
with Rpos the positive pre-B CORR at target tick t.
The inverse is used only to synthesize common initial stock.
There are no external steps during native evolution.

The guard pretest requires B0 in both reader rows for every
earlier cut on every input, and B1 at the selected row only
for p=j at the target. Subsequent exact native replay checks
the original source and all CORR slots through t-1, the actual
pre-B receiver and write at t, and a common even full source
return with continuous exact port/reference hold and complete
two-class reader histories. The screen uses p=1,j before a
five-input replay; a lost hold cannot later satisfy continuous
hold. Complete H, sums and inverse are checked on all executed
ticks. No future desired output is written by the verifier.

In frozen order the first successful stock is n=-3,l=0,v=0,
t=6, f=w=1. There are 1,561 tried candidates: 100 fail the
guard pretest, 1,461 pass it, 1,460 of those fail the two-input
held-return screen and the last passes the complete five-input
test. The search stops here as preregistered; no full-family
success rate or optimality claim follows.

The actual initial and ready material half-difference pairs
at the receiver are, in power-basis coordinates,

    D_initial=((1,-1,-1,-1),(1,-1,-1,1)),
    D_ready=((0,-1,-1,0),(2,-1,-1,0)).

The free clock has exact period five and makes genuine changes.
At ticks 1..5 B is idle in the receiver. At t6 the actual
positive incoming CORR is (4,-2,12,1); the common CLK is
g=(6,-2,12,1). The positive half-difference of the radiation
pair is 1, the positive material half-difference is J^-1.
Hence B1 qualifies and writes

    g+(J^-1-1) = (5,-3,11,1).

The four other roots leave g unchanged. The adjacent CLK
reference remains g. B1 also changes the positive material
difference to 1. At that cut the material and CLK differences
between rows are no longer even in the positive history;
vertical C then refuses those pairs. This explains the local
retention mechanism without asserting that all future B
contacts are idle. The full native replay proves the finite
hold, not a perpetual lock.

All five initial fields have the same complete accounts:

    material sum = (0,0,0,0)
    radiation sum = (88,11,109,17)
    H = (1658,0,662,662)
    Q = 2654.

All source columns, i.e. all eight ring slots of column0,
including the fixed material reference and both radiation
pairs, equal their own initial values at even full ticks
16,30,44,58,72,86,100. The matching bit is then zero.
At every full and post-C cut since full6 through full110
and post-C111 the fixed port and adjacent reference retain
the exact values above; the first failure is full111.
The complete reader history has exactly the two classes
{j},{1,j^2,j^3,j^4} from tick2 through tick160. There are also
source returns at 114 and 144, but these fail the required
continuous record hold. Full return of the entire coupled
field or fresh-input operation is not claimed. The repeated
14-tick spacing in the bounded interval is not a proved
renewal period.

## 3. C and D: retained failures and necessity control

Standalone clock C was frozen before calculation with ready
pair (J^-1,J^-1+2j), target t3, common g=2 and fixed incoming
CORR. Its actual first B occurs at t2, so the prediction
fails. The complete trajectory is retained in EXPECTED.txt.
This failure is not retuned or reclassified as a pass.

D is a separately declared control of the selected B device.
Only the initial two material half-differences of the receiver
are rotated by C^q, q=0..4, and every other slot is identical.
Thus the complete initial H, Q=2654, and sums are identical
across phases and inputs. All 25 complete fields are checked
through t160, with inverse and accounts. The first receiver
write on the positive root is:

| Initial phase q | First write | Held-return cuts under fixed t6 contract |
|---:|---|---|
| 0 | 6 | 16,30,44,58,72,86,100 |
| 1 | none through 160 | none |
| 2 | none through 160 | none |
| 3 | none through 160 | none |
| 4 | 7 | none |

No negative input has a receiver B write through 160 in
these controls. The original fixed tick-six contract is
not changed to accept the later write. D.txt records all
source returns, port/reference outputs and reader partitions.

The separate static control sets both initial material
half-differences to J^-1, with the same g and all other slots.
It does not rotate before the first write. It has Q=2630
rather than 2654, first positive write at t6, and the same
seven qualifying held source returns and first hold failure
at full111. Its four negative reader histories also remain
identical through160. Thus phase of the moving clock matters
within the rotating preparations, but a moving clock is NOT
necessary for the selected coupled readout. The simpler
static preparation meets the same endpoint/hold contract
at a smaller account. The result is not evidence that a
new independent clock is required in that device.

## 4. E: constant-input native time gate

E is a new standalone successor to failed C, declared before
its execution. It does not repair C or replace B/D controls.
Choose w=2+j. At column6 use neutral material pairs with
half-differences

    d0=w+rho^q, d1=w-rho^q, q=0..4.

Take D*=w+rho^3=2+2j, f=J D*, g=2f. Both CLK in
column6 equal g, all other CLK zero. Row0 CORR is zero,
row1 CORR is g everywhere, and all other material is zero.
Before the first B the vertical C is active on both material
rails and all radiation is unchanged. Thus after t C steps

    d0(t)=w+rho^(q+t), d1(t)=w-rho^(q+t).

The exact norms of w+j^k for k=0..4 are

    7+3phi, 4+4phi, 3+phi, 4-phi, 2+3phi,

where phi=-j^2-j^3. They are distinct in Q(phi).
The first B1 balance at row0 requires h(d0)=h(D*),
since its constant f is J D*. No B2 qualifies beforehand:
none of these five norms equals T^2 h(D*), as verified by
exact reduction. Row1 has zero radiation half-difference.
Every other cell has zero material. Consequently the first
actual write occurs at the unique t in {1,...,5} with
q+t=3 mod5, while the entire incoming radiation and CLK
values remain the same before that write. The complete
initial H and Q=360 are independent of q, because
h(w+rho^q)+h(w-rho^q)=2h(w)+2.

The literal first-write times in q order are (3,2,1,5,4).
Every output is the same raw value (4,4,2,2). All five
complete histories through tick12, including exact inverse,
sums and H, pass. Static ready pair (D*,D*) writes at t1
with Q=368. This establishes finite internal timing by the
material clock with constant supplied radiation, not
time dependence supplied by a changing incoming pulse.
The output/reference of every standalone case first changes
at the next post-C cut; no storage or renewal claim for E.

## 5. Status boundary

The five-step obstruction and conditional contact algebra
are mathematical candidate-T at L1. The finite reference
replay, selected equal-account source-return/capture device,
phase controls, timing witness and failed searches are
candidate-C at L1. B's moving-clock necessity is specifically
not established. The first selected stock is not a resource
minimum. No autonomous reset, repeated fresh-input read,
restoration of the original paired moving Galois motor,
simultaneous two-source equality or general arbitrary-vector
extension follows. No physical measurement, energy
identification, quantum inference, curvature selection,
RH bound, native-U equivalence or unnamed higher-layer lift.

The separate five-cyclic-coefficient implementation replays
the A census, C failure, selected B witness via D, all D
controls and all E cases. Its respective transcripts agree
byte for byte. It does not repeat the primary B enumeration;
reproduction of that enumeration is a separate architecture
replay of the same primary code. The alternate is result-
exposed, not a blind independent review. No formal repository
scientific gate or Canon promotion is asserted.
