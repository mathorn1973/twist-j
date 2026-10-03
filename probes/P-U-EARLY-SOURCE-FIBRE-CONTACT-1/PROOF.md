# Actual early U steps do not give SUM in the frozen affine class

NON-CANONICAL L1 proof candidate. This text proves the mathematical
nonexistence statement in `PREREG.md`; it reports no executed gate,
public pin, architecture result, or public status. The negative target was
exposed during class design and disclosed in that contract.

## 1. The inherited later boundary

For origin-zero native trajectories put E_n(psi0)=pr_checkpoint U^n(0,psi0).
The registered synchronization theorem gives, for every n>=3,

    z(E_n(psi0))=4+2 theta_(n-1).

Thus at a common time n>=3 every reached checkpoint selects the same
generator: e for (theta_(n-1),theta_n)=(0,0), d for (1,1), and b for
unequal bits. Each generator's fibre map depends only on the current
fibre. If two reached checkpoints have the same (q,r) at time n, they
therefore have the same fibre at n+1. Induction proves equality at every
later common time. Since these fibre maps are bijections, unequal fibres
also cannot merge during such a common tail.

This is an inherited corollary, not a new claim. Its owners are
KERNEL-Z6-SYNCHRONIZATION [T], QDD-U-INDUCED-CHANNEL [T], and
U-NATIVE-APPARATUS-HISTORY-FACTOR [T]. The existing evidence
`probes/P-U-PREPARATION-EVENT-RECORD-1/RESULT.md`, under "Late tails carry
less information", already states that the late updates are common
bijections and tails agree exactly when A3 agrees. #1342 A5(iv) explicitly
records the common-selector rule used above.

The domain is the origin-zero reachable sheet at the stated time, not
arbitrary F5^6 checkpoints assigned that counter. The conclusion does not
erase information written earlier, restrict piston reading, or exclude an
extra interaction. It supplies no new physical writing theorem.

## 2. Source-sum reduction is exact

Write a full checkpoint as (P,u), with P=(p1,p4,p1p,p4p), u=(q,r),
kappa=sum(P), and z=kappa+q+r. Summing the four piston components of
each exact public generator gives

| Generator | kappa' | q' | r' |
| --- | --- | --- | --- |
| a | kappa | q | r |
| b | -kappa | -q | -r |
| c | 1-kappa | 1-q | -r |
| d | -kappa | 1-q | 1-r |
| e | -kappa | 2-q | 1-r |

For c, the piston constants sum to 6=1 and its two r terms cancel.
For d and e, the piston constants sum to 10=0. The selector
z+2 theta_n also depends only on this triple and n. The projection of
each full native step therefore commutes with the displayed projected
step. Induction proves complete fibre-history dependence only on the
initial triple and the common native counter. This recovers the existing
native history factor directly from its defining formulas.

For an admitted affine preparation P=P0+v x, u=F0+w y, the triple uses
the source only through k0=sum(P0) and s=sum(v). Every full candidate
maps to the receiver class in the contract. Conversely all k0,s are
attainable with a nonzero source line: for s!=0 use
P0=(k0,0,0,0), v=(s,0,0,0), A=(s^-1,0,0,0); for s=0 use
v=(1,-1,0,0), A=(1,0,0,0). In each case A.v=1 and the affine constant
a=-A.P0 supplies the initial source decoding. No receiver coordinate
depends initially on x.

Consequently an obstruction to the receiver equation in every reduced
configuration excludes the complete full class, including its independent
source-output preservation requirement. It does not assert that satisfying
the receiver equation alone would be sufficient for a full SUM operation.

## 3. The first three steps are selected by U itself

The origin-zero driver bits for the three transitions are 0,1,1. Let z
and u denote the initial total trace and fibre. At the first transition
the generator index is exactly z. The native trace maps are

    a:z->z, b:z->-z, c:z->2-z, d:z->2-z, e:z->3-z.

Substitution gives the following table. The words are consequences of
the selector applied at each actual counter, not admitted external controls.

| Initial z | Actual indices at n=0,1,2 | z1 | z2 | z3 |
| --- | --- | --- | --- | --- |
| 0 | 0,2,4 (a,c,e) | 0 | 2 | 1 |
| 1 | 1,1,3 (b,b,d) | 4 | 1 | 1 |
| 2 | 2,2,4 (c,c,e) | 0 | 2 | 1 |
| 3 | 3,1,3 (d,b,d) | 4 | 1 | 1 |
| 4 | 4,1,3 (e,b,d) | 4 | 1 | 1 |

Composing their actual fibre updates in temporal order yields

| z | F1(z,u) | F2(z,u) | F3(z,u) |
| --- | --- | --- | --- |
| 0 | u | -u+(1,0) | u+(1,1) |
| 1 | -u | u | -u+(1,1) |
| 2 | -u+(1,0) | u | -u+(2,1) |
| 3 | -u+(1,1) | u-(1,1) | -u+(2,2) |
| 4 | -u+(2,1) | u-(2,1) | -u+(3,2) |

In particular F2(1,u)=F2(2,u) and, for every z,u,

    F3(z,u)=F1(z,u)+(1,1).

These universal formulas will be audited against the complete native
six-coordinate trajectories. Their derivation has not frozen a word
independently of the state and has not discarded feedback into the piston
block: the closed triple accounts for its effect on all later selectors.

## 4. Complete receiver obstruction

Let the candidate receiver line be u_y=F0+w y and its fixed affine reader
be B.u+b, where B.w=1. Set h(y)=k0+q0+r0+(w_q+w_r)y. The initial total
trace at input (x,y) is z=s x+h(y).

If s=0, the closed triple and all its fibre outputs are independent of x
at fixed y. No receiver-only reader can then return y+x for all five x.
This settles every time when s=0.

Now assume s!=0. At fixed y, letting x run through F5 makes z run
through every value exactly once; the demanded receiver output is

    x+y=s^-1 z + y-s^-1 h(y).

Its difference between consecutive z values is the nonzero s^-1.

At t=1 compare z=1,2,3 using the table. The corresponding differences
of readouts are B_q and B_r, so both must equal s^-1. Comparing z=0
and z=1 gives

    B.(-u_y)+b - (B.u_y+b)=-2 B.u_y=s^-1.

This must hold for every y. Subtracting its y=0 instance from its y=1
instance gives -2 B.w=0, hence B.w=0 in F5. This contradicts B.w=1.
The argument allows any affine constant b, so it is stronger than needed
for the stipulated b=-B.F0.

At t=2, the two inputs at the same y with z=1 and z=2 have distinct x
but exactly the same fibre u_y. Their target values differ by s^-1.
No function of that fibre can return both values. This part does not even
require reader affinity.

At t=3 the universal translation identity gives

    B.F3(z,u_y)+b=B.F1(z,u_y)+(b+B.(1,1)).

A successful t=3 reader would therefore supply a t=1 affine reader with
the same B.w=1 and a shifted constant. The t=1 proof excludes it.

All possible s and all three target times are covered. No receiver
configuration in the contract succeeds, and therefore no complete source
and receiver candidate realizes (x,y)->(x,y+x) for all 25 pairs.

## 5. Classification and limits

The different early-contact owners #987 (q-source carry into a piston
pointer) and #1003 (q-source/common-piston endpoint partitions) are retained
at their own scopes. This theorem is about piston source to fibre receiver
and full addition with an independently variable receiver. It does not
claim the first native source-dependent transient or reserve those older
partitions. The synchronized permanent-write result owned by #862 is also
distinct from this three-step preparation/reader classification.

The complete negative class is exactly the independent affine source and
receiver preparations, same fixed affine block-local initial/output
readers, origin-zero counter, and actual first one, two or three native
steps specified in the contract. Source retention remains a requirement;
receiver impossibility is sufficient to refute their conjunction.

This does not exclude nonlinear preparations/readers, another partition
of native coordinates, a history reader, an input-dependent protocol,
another launch contract, or an enlarged architecture. It does not claim a
positive physical operation, conservation law, native inverse, renewal,
reusable contact, apparatus, occurrence measure, or the stronger complete
state/counter preservation and timing contract of #1349.

The theorem is analytic. Formal exact finite audits and independent code
review are still required by the intended public probe process; none is
reported by this pre-run document.
