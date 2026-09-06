# Native protected record: exact algebra and write boundary

Status: NON-CANONICAL; candidate proof; L1 only. This is the analytical
part of frozen work packages A, E and F. Computational audits and the clock
frequency certificate are recorded separately. No public Canon status is
created by this note.

## 1. A coordinate chart using the present checkpoint only

All arithmetic in this section is in F5. Put

    A=p1+p1p, B=p4+p4p,
    C=p1-p1p-2, D=p4-p4p-1,
    v=V(x)=(A,B,chi(z)*C,chi(z)*D),
    chi(1)=1, chi(4)=-1.

The map x -> (z,v,r) is a bijection from X14 onto
{1,4} x F5^4 x F5. For v=(a,b,c,d), its inverse is

    C=chi(z)*c, D=chi(z)*d,
    p1=3*(a+2+C), p1p=3*(a-2-C),
    p4=3*(b+1+D), p4p=3*(b-1-D),
    q=z-a-b-r.

Here 3 is the inverse of 2 in F5; substitution verifies every coordinate.
The letters C,D in these formulas are the centered differences, not the
unshifted piston differences.

On z=1 the control bits 0 and 1 choose b and d respectively; on z=4 the
control bits 0 and 1 choose e and b respectively. The selected b operation
is therefore, in these coordinates,

    B0(z,v,r)=(5-z,-v,-r).

The selected d or e operation is

    C0(z,v,r)=(z,-v,1-r).

To check this directly, b negates both piston sums, preserves the two
centered differences, swaps z=1 with z=4, and negates r. Each of d,e
negates both piston sums and both centered differences, preserves its
selected phase, and sends r to 1-r. Thus both permitted control choices
satisfy V(next)=-V(x), and the unordered sign class

    R(x)={V(x),-V(x)}

is preserved. This is an identity for every point of X14 and both bits;
it does not require statistical properties of the Thue-Morse word.

## 2. Complete connected-fibre classification

Both B0 and C0 are involutions. Their composition is

    K=C0 o B0: (z,v,r) -> (5-z,v,r+1).

Its k-th power is

    K^k(z,v,r)=(z if k is even else 5-z, v, r+k).

For k=0,...,9, the pair (k mod 2,k mod 5) runs through all ten pairs.
Consequently the K-orbit contains every phase and r value with fixed v.
Applying B0 also supplies every phase and r value with -v. Conversely,
the transition identity already proved prohibits leaving {v,-v}.
Every R-fibre is therefore exactly one strongly connected component of
the directed graph allowing both control choices. No probabilistic or
Thue-Morse admissibility claim is used in this graph argument.

Because the field has odd characteristic, v=-v holds precisely for v=0.
There is one component of size 10 and (625-1)/2=312 components of size 20.
The total is 10+312*20=6250, covering X14 without overlap.

For any finite alphabet A, a fixed reader f:X14->A satisfies

    f(next)=f(x) for every x in X14 and both control choices

if and only if there is a function g on the 313 sign classes with

    f=g o R.

Necessity follows by transporting equality along all graph paths, and
sufficiency follows from invariance of R. Since R is onto, g is unique.
This classifies all readers with the stated invariance property, including
nonlinear readers and arbitrary lookup tables. A reader may merge sign
classes, but cannot split one while retaining that property.

## 3. The actual clock orbit requires its own support proof

The directed graph above permits arbitrary sequences of controls. Its
connectivity alone cannot establish support or frequency for the fixed
Thue-Morse sequence. CLOCK-PROOF.md independently proves the actual
fixed-origin clock densities along all prefix lengths; the following
argument transports that result to these fibres.

Let w=(alpha,beta,gamma,delta) be the first four labels in the frozen
native chart, and let epsilon be the fifth. Substitution in the frozen
odd/even chart formulas gives

    odd  n=2m+1: V(x_n)=w,
    even n=2m+2: V(x_n)=-w.

For the odd formula chi(z)=(-1)^(1+u)=h; for the even formula
chi(z)=(-1)^u=-h. These identities establish the signs above.
For fixed epsilon, the odd formula maps (s,u) bijectively onto the ten
points with V=w: u fixes z and s fixes r=epsilon+s-1. The even formula
maps (s,u) bijectively onto the ten points with V=-w through
r=-(epsilon+s-1) and its phase formula.

CLOCK-PROOF.md establishes the limiting frequency 1/10 for every pair
(S(m) mod 5,theta_m)=(s,u), using its explicit integer primitive certificate
and a bound valid for every prefix length. Thus the actual checkpoint
orbit of every fixed chart label has positive limiting frequency at every
point of its R-fibre. Its support is the full 20-point component when
w is nonzero, with weight 1/20 at each point, and the full 10-point
component when w=0, with weight 1/10 at each point. The first finitely
many checkpoints have no effect on these frequencies. This conclusion
uses the all-length clock proof; stationarity or graph connectivity by
itself would be insufficient.

## 4. Eventual constancy excludes a permanent internal write in this class

Suppose a sequence visits every point of a finite set C infinitely often,
and f:C->A is fixed. If f(x_n)=a for every n>=N, then f(y)=a for every
y in C: choose an occurrence of y after N. In particular, positive
limiting frequency for every y is sufficient; no mixing assumption is
needed.

Apply this lemma to an actual synchronized chart trajectory using the
positive support established in section 3. If a fixed checkpoint reader
is eventually constant on that trajectory, it is constant on the whole
R-fibre and had that same value at every synchronized checkpoint of the
trajectory. Thus it cannot be BLANK at one synchronized checkpoint and
later change permanently to a distinct WRITTEN value under unchanged U.

This statement concerns a fixed reading of the checkpoint alone and
permanent constancy after synchronization. It does not exclude finite
retention times, transient event values, clock-dependent readings,
interventions, ancillary registers, changes of reader context, or memory
outside the frozen class. It also makes no claim about the initial
unsynchronized transient.

## 5. Target-independent storage and exact readback

Take the message alphabet to be F5^4/{+1,-1}. Choose the lexicographically
least representative w=(a,b,c,d) of each class using the residues 0,...,4.
Define its preparation E([w]) by the inverse in section 1 with z=1,r=0:

    E([w])=(3*(a+2+c), 3*(b+1+d),
            3*(a-2-c), 3*(b-1-d), 1-a-b, 0).

Its phase is 1 and V(E([w]))=w. Readback is the same fixed map R at every
subsequent tick. The transition identity proves

    R(x_n)=[w]

for every control sequence, when initialized at E([w]). In particular this
holds for the prescribed native clock, with no saved counter, additional
register or target-dependent decoder choice. There are exactly 313
distinguishable invariant messages, and section 2 proves this is maximal
for an invariant checkpoint reader on all X14. The choice of representative
is only a deterministic preparation convention; it is not a physical
selection law.

This construction prescribes a correlated native preparation. It is not
an endogenous write process, an independent system/apparatus preparation,
or a proof that a physical apparatus realizes the encoding. Section 4 gives
the permanent-write obstruction within the frozen synchronized reader
class even though this mathematical static storage is available.

## 6. The protected record does not recover the original QDD record

The number 313 also appears in the original four-piston QDD sign quotient,
but equality of cardinalities does not identify these two partitions.
For example, the synchronized checkpoint

    x=(1,0,0,0,0,0)

and its permitted d-successor

    y=(1,1,3,4,1,1)

have the same R. This controlled transition is also realizable on an actual
origin-zero synchronized trajectory: at n=8 the reachable sheet is z=1,
theta_8=1, and the inherited chart covers every point of that sheet.
Their balanced piston vectors are respectively
(1,0,0,0) and (1,1,-2,-1). The inherited QDD formulas give normalized LOW
weights 1/16 and 1/136 respectively: for x, m=4/5 and wL=1/20;
for y, m=34/5 and wL=1/20. Thus R does not even determine the current
QDD LOW weight on all synchronized checkpoints.

For the original-head record, the inherited first-tick merger is stronger.
The two supported heads

    (4,1,0,0,0,0), (2,1,1,2,1,0)

both become (1,4,0,0,0,0) under their native origin-zero first tick,
but their original normalized LOW weights are 0 and 9/14. Every later
checkpoint is identical for these heads. Consequently no function of that
later checkpoint, including R, can recover both original records.

The inherited three-state saved-class repair changes the admitted memory
surface and remains unaffected. Static storage in a different native
partition cannot reconstruct information already erased by a merger.

## 7. Disposition

The protected-register algebra is a positive exact result at L1, subject
to its registered finite audit: present-state storage exists and its full
invariant-reader quotient is the 313-element sign class above. The permanent
post-synchronization write obstruction follows using the separately proved
exact clock support. Neither conclusion supplies event selection or a
physical occurrence rule. The fixed-event-reader route is disposed of by
the separate all-length frequency and whole-atom allocation proof; its
success or failure must not be inferred from storage cardinality.
