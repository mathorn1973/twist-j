# C-H3-SEPARATED-SOURCE-READER-N

NON-CANONICAL / NO AUTHORITY. L1 mathematical and finite H3 results.
Reservation #2115 and result-exposed successor D (comment 7220474250).
Public Canon v117 base 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.
Predecessor drafts #2114 at dc7fae61abf084ee5ad492a35b520d8c55f5d1b9
and #2112 at 85c17c40506645f18a7ee699cbdc78bb4e2efc0e.
No formal public probe or cross-layer claim.

## 1. Strict material-history preservation prevents active reading

Write O=Z[j], Phi5(j)=0, rho=j^2, J=1+rho,
h(z)=z conjugate(z), T=h(J). Use the exact H3 source in
reproduce/h3-referenced-record/verify.py at the base commit,
Git blob fd215e24fefbbebf83cf3985d8ebcedd590aa709.
Its material and CLK transport is vertical; CORR transport
is horizontal. Its B1/B2 local changes are reciprocal
multiplication by J and J^-1 on the two half-differences,
with pair centers retained and unchanged parity/balance refusal.

Consider the reference paired family on 8 by 8, b=1,c=1
in the notation of #2112. The two source columns 0,1 have
independent address indices r,u in 0..3. Their material
half-differences are (-1)^y except j,j^2 at y=-2r,4-2r
on column 0 and j^3,j^4 at y=-2u,4-2u on column 1.
Opposite material rails are retained. The common initial
radiation is CLK=0, CORR=2J(-1)^(x+y). The exact replay
checks all sixteen preparations, including complete return
at 160, complete accounts and inverse at every tick.
The single-track family with just column 0 marked is
also checked for all four r. In both families all actual
radiation full/post-C transcripts and complete B-tag
transcripts are common across the input family over the
entire 160-tick interval. Full return with bit zero
extends this equality indefinitely.

Conditional on these common reference branch histories,
there is an exact locality obstruction. In the coupled
field suppose all initial radiation and all initial
material outside the complete source columns are common
across the inputs. Arbitrary common initial reader stocks
are allowed. Require the two source material rails to
follow their corresponding reference values at every
full cut from the initial cut through the chosen horizon.
The material C on each source column is then determined
by those values, and its post-C material is also the
reference material. A nonzero material half-difference d
and its post-B value uniquely determine the exponent
e in {-1,0,1} in J^e d, since J has infinite order.
For d=0 only the idle branch is possible, by the
nonzero guard and positive h. This reasoning also covers
parity refusal (with half-difference interpreted over
the field). Thus every actual B tag at a source site
must equal the reference B tag and is input-independent.
Inductively all radiation C inputs are common; radiation
B at each source site uses a common branch, and outside
the source columns all local inputs are common, because
material C does not cross columns. All other material,
all radiation and every B tag therefore remain common.
No deterministic observation of those reader slots,
even of their whole history, can distinguish the source
inputs in this strict-preservation class.

This is a proof of an implication at the stated
partition and initialization, not a general measurement
impossibility theorem. Its application to the specific
reference family uses the exact finite reference replay
and periodicity above. It leaves open transient source
disturbance followed by endpoint recovery.

## 2. B: a separate active interrogation of one source column

The following new supplied preparation uses only column 0
of the faster single-track reference as the source, not
the entire original moving motor. Every source slot is
exactly its reference initial value multiplied by the
same fixed eta=(1-rho)^4. All other seven columns have
zero material and CLK initially, and a common CORR stock
synthesized below without the input address r. The
source has no input-dependent auxiliary copies or
phase-dependent reader stock. The native H3 evolution
uses exactly the pinned 8-by-8 geometry and matching bit.

The source is scaled to clear denominators in the stock
synthesis, not because a scaled full original motor
has already been joined to the apparatus. In O,

    eta = (-5,-10,-10,-5) in power-basis coordinates.

The element 1-rho is invertible modulo 2 (its norm is
5); therefore eta is also invertible there, and scaling
does not alter parity decisions. Norm balance equations
scale by h(eta). The inverse-neighbor calculation uses
O localized at 1-rho, with parity modulo 2 well-defined.
After the single initial scale, every raw slot is an
integer in O and all later evolution uses literal H3.

For clarity the unscaled synthesis is as follows.
Let A=(1+rho)/2, B=(1-rho)/2, where these letters denote
transport coefficients, not additional contact operators.
For any current CORR value c and desired next value w
set

    partner(c,w) = c + (w-c)/B.

If the pair difference is even in the localized ring,
the admitted C sends the first value to
A*c+B*partner(c,w)=w. The inverse coefficient is explicit:

    B^-1 = (2/5)(4+3rho+2rho^2+rho^3).

For the first horizontal contact choose reader column
1 initially -2J*s, with s=(-1)^y, and source CORR
2J*s. C rotates this opposite pair by rho. On every
source row the first material C either refuses
distinct root residues or rotates an opposite pair
of equal root residue; the resulting h(d)=1.
Consequently B1 acts at every source row and

    g1 = rho^2*s,   c1 = (J+1)*rho*s,

where g,c are source CLK,CORR. Reader column 1's
post-C CORR is c11=-2J*rho*s.

For the next three source contacts prescribe common
radiation half-differences by row:

| Tick | y=0 | y!=0 |
|---|---|---|
| 2 | J^2 | -s |
| 3 | J^3 | 0 |
| 4 | J^2 | 0 |

For ticks 2 and 3 the prescribed B exponents on the
source are respectively (+1,-1) and (+1,0) on
(y=0,y!=0). The common source pre-B CLK g_t^- is
computed from the actual vertical C on g_(t-1).
The desired pre-B CORR is c_t^-=g_t^- -2 f_t.
For ticks 2,3 post-B values are determined by
delta=(J^-e-1)f_t, g_t=g_t^-+delta,
c_t=c_t^- -delta.

The reader columns have no B events. The rowwise
inverse synthesis in PREREG.md and verify.py solves
their required CORR values in causal order. The
left-going pulses delivered at ticks 2 and 4 use
columns 7 and 6; the right-going pulses delivered
at tick 3 and the final record reference at tick 5
use columns 1,2,3 and 4. Every equation is a
partner(c,w) equation or the pair-sum identity
of C. At most four successive divisions by 1-rho
are needed, because the longest backward path in
that system is the determination of c41.
The only remaining initial pair is (4,5), obtained
by the actual inverse C on its prescribed first
outputs, including parity refusal. The audits
verify each partner parity, inverse pair and every
scaled initial slot's integrality. They check the
actual source pre-B half-differences at all rows
in ticks 1..4. No prescribed B exponent is used
as an external update.

## 3. Native dependence and remote output

Before material C at tick 4, the selected row zero
has material half-difference J^3 times a signed root,
and row seven has a signed root of norm one.
In O/2O=F16, J^3=j^3 and the five powers of j remain
distinct. Thus equality of their residues can depend
on the source address. For the exact first three
native steps of this preparation the four results
are:

| r | C at rows (7,0) at t=4 | B at source (0,0) |
|---|---|---|
| 0 | admits, changes | idle |
| 1 | admits, changes | idle |
| 2 | refuses | B2 |
| 3 | admits, changes | idle |

The source at all other rows has f4=0, so no B
there. The exact pre/post-material values are
recorded in EXPECTED.txt. This is a finite audit
of actual branches, not selection by a source label
supplied to the evolution.

In the positive case r=2 the source half-difference
before B is J^3 times a root, while the actual
radiation half-difference is J^2, all multiplied
by eta. This is B2 balance. In the other three
cases the material C produces the recorded unequal
norms and B is idle. Thus at tick 4 the source
CORR is cP=c_4^- -rho*f4 in the positive case and
c_4^- in the negative cases, before multiplying
by eta. In the common initial stock synthesis
reader column 1 was chosen to have

    c14=cP+2

at tick 4. Since the difference of the two source
outcomes is rho*J^2, a unit modulo 2, the tick-five
horizontal C at the port admits only the positive
case, with input difference -2. Reader column 1
therefore changes by rho-1 in unscaled coordinates.
The literal full tick-five remote CORR at (1,0)
is

    Rpos = (5,-15,-15,-25)  if r=2,
    Rneg = (-5,-35,-30,-30) otherwise.

These are raw integer values in the power basis
(1,j,j^2,j^3). No externally computed bit is
written. The reader has zero material throughout
B's evolution and hence B idle there. In the
unshifted pulse all reader slots and their complete
histories are identical across the four inputs up
to full tick 4, and exactly two classes through
tick 12. The two classes are {2} and {0,1,3}.
The specified remote value itself holds for all
four only at the tested fifth cut; it is a
passing record, not yet an archive.

Even vertical translation by -2l commutes with the
native matching layers and B. Translating only
the common reader pulse accordingly interrogates
r=l+2 mod4 at the fixed translated port (1,-2l).
All sixteen separately prepared (l,r) cases pass
the declared exact tests. These are four different
address queries, each applied to four possible
inputs. They are NOT sixteen independent paired
source inputs in a simultaneous equality comparator.

The complete account Q is 110208, common to all
sixteen preparations. The initial data-containing
column contributes Q=5200: h(eta)=(2+phi)^4=50+75phi
and its unscaled H is 8(2+4T), with T=2-phi.
The large remaining stock is counted, not a
minimum. All complete ring accounts and linear sums
are conserved and the inverse is checked on every
executed native tick.

## 4. C: no source recovery in the declared horizon

For the unshifted pulse, all four sources agree
with their corresponding eta-scaled unmodified
material and complete-column histories at tick 1.
At every full tick 2..160, none of the four
agrees with its corresponding reference, even on
just the material column. No material column
equals its own initial data at any full tick
1..160. These are exact negative results for
the declared new preparation, including the
original stroke cuts 40,80,120,160.
This does not prove that no endpoint echo is
possible with a different supplied stock or
at a later time.

## 5. D: a separate fixed native capture register

The result-exposed successor D was declared before
its new stock search. It keeps B's source and
pulse stock exactly and adds only common stock in
reader column 1. At every row in that column set

    CLK=g=Rpos+2a.

At row zero set the neutral material pair
(J^-1*a,-J^-1*a), and leave the other material
rows zero. Candidate a=n*v ranges over 15 nonzero
binary power-basis coefficient vectors v and the
eight odd positive n<=15, in the frozen order.
Because a and J^-1*a are nonzero modulo 2, the
added material pair cannot transport vertically
into the neighboring zeros while it stays on
this J-orbit. Initially the CLK is common along
the column. First test the four earlier actual
CORR inputs at the receiver against the new
common cell. All 120 candidates have B0 in
these early tests, and their full native
replays verify the same early idle behavior.
In particular the source complete history
through tick 5 is unchanged from B.

On the positive remote input Rpos at tick 5,
the radiation half-difference is a. This has
the exact B1 balance with J^-1*a. On the other
input Rneg the parity is refused because
Rpos-Rneg=eta*(rho-1) is nonzero modulo 2.
Consequently the actual CLK register at (1,0)
is

    g+(J^-1-1)a if r=2,   g otherwise.

The local reference CLK at (1,1) equals g.
This is a genuine B write in a separate
receiver column, not just inspection of the
transport flag. For each of the 120 stocks
all four phases were replayed through tick12,
including exact complete accounts and inverse.
The common exact hold of the port and its
reference (counting subsequent C/B substeps)
is one for 112 stocks, and at least fourteen
for eight stocks (the horizon ends at full12).
By the frozen longest-hold and first-in-order
rule the chosen a is (1,1,1,1)=-j^4. The
actual values in power-basis coordinates are

    reference g = (7,-13,-13,-23),
    positive    = (7,-13,-14,-24).

The difference is exactly

    phi = -j^2-j^3.

Both the reference and the two possible actual
port values hold through every full/post-C cut
from full tick5 to full tick12. No claim is
made beyond that certified interval.
The complete reader sector, including the added
material and reference registers and all its
earlier full/post-C cuts, still has just the
two input classes {2},{0,1,3} through tick12.
This is stronger than a single port returning
a binary result, but limited to these four
supplied source inputs and this interval.

All sixteen translated queries of the selected
capture stock pass with the same hold and
values at the translated port/reference.
The complete Q=121478 is common, including
the reference and added receiver pair. For the
unshifted selected capture the same reference
recovery test through tick160 again has no
match for any r after tick1, and no source
material initial return. D does not repair C.

## 6. Status and remaining issue

The strict-preservation implication and elementary
contact-synthesis identities are conditional algebra
at L1 (candidate-T at the stated hypotheses).
The reference and active finite witnesses,
archive hold and bounded negative recovery are
candidate-C. Both implementations are separately
written but result-exposed, not blind independent
reviewers. No formal scientific gate is asserted.

This is a separate common-stock active source
interrogation and an actual native fixed-register
capture of one phase predicate. It is not a
nondestructive attachment to the full paired
periodic motor, not the native equality of two
independent phase addresses, not a reduction of
the earlier four-position coincidence strip, and
not a native circuit for preparing or resetting
the reader. The common reader stock is explicitly
synthesized and supplied, not generated by the
source. The source remains disturbed. The next
test is a transient interaction plus exact
endpoint recovery with the separated record
retained. A continuous undisturbed source history
is ruled out in the declared class, while an
endpoint echo remains open.

No physical measurement, physical energy,
curvature selection, RH estimate, native-U
equivalence or unnamed cross-layer lift follows.
