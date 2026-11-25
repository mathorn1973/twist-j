# Preparation cost, split capacity and the zero-record fibre

**PUBLIC / NON-CANONICAL / L1 / no authority.**
Written consequences below have candidate-T status. Canonical premises retain
their existing status and scope. This review claims no new computational run.
Author: A. M. Thorn <thorn@twistj.com>.
Owner session: codex-zero-root-20261125, existing reservation #2097.

## Basis and custody

This responds to the owner-supplied RECON report on native-write capacity
and two messages, dated 2026-11-25. Its stated calculations were not
preregistered, and its archive `twistj-recon-2026-11-25.tgz` was not available
to this review. No original scripts, 37-check transcript or unprovided
archive were replayed. The following arguments are exposed, same-session
written derivations from the displayed native maps and the current Canon.
They are not an independent audit of those missing files.

Public main and `canon-v117` remain
`6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, content ancestor
`d65e32c4b8e9a14496d3b7aba46fc384f51f81dc`. All five normative hashes were
rechecked. The reviewed note is PR #2098 at
`6c33bef6a6e08a4b9bc4db557d06bcc6d6b6c983`. Its pinned programs, thresholds
and execution records are unchanged. The report is a source of questions
and exposed predictions, not a retrospective preregistration.

## 1. Inherited structure and the actual contribution

The integral reader is an explicit trace/finite Fourier identity. The
polynomial code is a Reed-Solomon evaluation code, with the ideal filtration
intertwined with finite differences. Their identification and scope are
proved in PROOF.md; they do not introduce a new coding principle.

For the native part, KERNEL-Z6-SYNCHRONIZATION already proves entry into
X14 by tick three and sheetwise bijectivity. U-NATIVE-INVARIANT-AND-NOWRITE
already supplies the maximal invariant R={V,-V}, its full actual-orbit
recurrence, and the scope of the synchronized no-write result. The products
AB and CD in reference-PROOF.md are functions of that invariant. Their
retention is a direct application of these canonical results.

The note's construction is the specified target-fitting preparation E,
literal three-tick output, and fixed full-checkpoint reading on that family.
Its 25 inputs are a domain cardinality, not a theorem that the native
machine has maximum capacity 25. A source-independent complete receiver
is a different interface.

## 2. All affine launches with two zero receiving pistons

Take a two-pentit parameter t in F5^2 and an affine launch

    (s(t), 0, h(t), 0, q(t), r(t)).

There are 5^12 such launches, since each of the four affine scalar
functions has three coefficients. Demand that at tick three the two
receiving pistons give a prescribed affine bijection (a(t),b(t)).
This section fixes the literal tick-three target, the affine class,
zero initial receiving pistons, and origin counter zero.

The first-three-tick maps by initial total z are, with composition from
right to left,

    H0=eca, H1=d, H2=e, H3=dbd, H4=dbe.

On every nonzero initial sheet, the output receiving-piston pair of the
displayed launch is constant. If z(t) is nonconstant affine, every sheet
has five parameter values, which contradicts an injective target on any
nonzero sheet. A constant nonzero z also contradicts it. Thus z(t)=0.
On this sheet the actual prefix a,c,e gives

    a = h-r,       b = 3+s+r.

The complete solutions are exactly

    h=a+r,   s=b-3-r,   q=3-a-b-r,

where r is any affine function. Thus every prescribed affine bijection
has exactly 5^3=125 affine launches. There are

    25 |GL_2(F5)| = 25 (25-1)(25-5) = 12000

such affine target bijections. These two counts follow symbolically;
no exhaustive 5^12 search is claimed here.

For the note's a=r_1=v-2u and b=r_4=-v this implies

    q+r = 3-a-b = 3+2u.

E chooses q=3 and r=2u. One input digit is therefore present in the
canonical reference coordinate r before any tick. The two receiving
pistons are common, but the complete complementary receiver including
(q,r) is not common. If q,r are both common within this zero-sheet class,
then a+b is fixed, leaving at most five target pairs.

The last bound is restricted to this class. The canonical apparatus-only
history bound concerns the two-coordinate port (q,r). Neither statement
is a general upper bound of five on a receiver containing additional
pistons across several initial sheets.

## 3. Exact capacity of a common complementary receiver

### Contract and native premises

Choose any two of the four piston coordinates as the free source S,
with all 25 values admitted. The other two pistons K and both controls
(q,r) are common, independent of the source. The observer sees the
complete complementary receiver (P_K,q,r). All launches have counter
zero. Capacity means the number of distinct current receiver values,
or distinct ordered histories, not an internally implemented archive.

In piston order P=(p1,p4,p1p,p4p), put

    alpha=(12)(34), beta=(13)(24), gamma=alpha beta=(14)(23).

The piston maps are a:alpha P, b:-beta P,
c:-beta P+(2,1+r,2,1-r), and d,e:-P+(2,1,3,4).
The quotient rules are

| Branch | New (z,q,r) |
| --- | --- |
| a | (z,q,r) |
| b | (-z,-q,-r) |
| c | (2-z,1-q,-r) |
| d | (2-z,1-q,1-r) |
| e | (3-z,2-q,1-r) |

The selector is z+2 theta_n modulo five in order a,b,c,d,e; the first
three origin bits are 0,1,1. At fixed initial z, the two source coordinates
have a fixed sum and form a five-element affine line. Their quotient
history, signed piston permutation and affine translation are common.

Each two-element S is stabilized by exactly one nonidentity member D of
{I,alpha,beta,gamma}. Every group element either preserves S or exchanges
it with K. Therefore the current receiver distinguishes exactly one
class on that five-element line if the permutation preserves S, and
exactly five classes if it exchanges S and K. A history has five classes
on the line exactly when an exchange has occurred in one of its samples.

### Upper bounds and sharp single-time witnesses

Ignoring their nonzero scalar signs, the piston permutations by initial
z=0,1,2,3,4 are

| Cuts | Permutation row |
| --- | --- |
| 1 | (alpha,beta,beta,I,I) |
| 2 and 3 | (gamma,I,I,beta,beta) |

From cut three, every source follows the same selected branch. Only b,d,e
occur, so later permutation rows are the two displayed rows, interchanged
by left multiplication by beta. Cut four has the first row.

For the same-index pairs {1,3} and {2,4}, D=beta. Only the initial z=0
line ever exchanges with K. Thus there are at most 5+4=9 receiver
histories, and at most nine current values.

For D=alpha, the two rows exchange respectively two and three lines.
For D=gamma they exchange three and two. A current receiver consequently
has at most 5+4*3=17 values. The upper bound counts different initial
lines separately; collisions between them can only lower it.

Both bounds are sharp with common (q,r)=(0,1), for any fixed initial
values on K. At cut one the five control pairs are

    (0,1), (0,4), (1,4), (1,0), (2,0),

and at cut three they are

    (1,2), (1,0), (2,0), (2,1), (3,1).

They are pairwise distinct in each row. Thus the same-index bound nine
is attained at cut one, and the crossing bound seventeen is attained
at cut three for D=alpha and cut one for D=gamma.

### Two samples recover every crossing source

Every initial line exchanges at cut one or cut two for a crossing pair.
It remains to distinguish different initial lines. The controls at these
two cuts, for arbitrary common ready (q,r), are

| Initial z | (q1,r1) | (q2,r2) |
| --- | --- | --- |
| 0 | (q,r) | (1-q,-r) |
| 1 | (-q,-r) | (q,r) |
| 2 | (1-q,-r) | (q,r) |
| 3 | (1-q,1-r) | (q-1,r-1) |
| 4 | (2-q,1-r) | (q-2,r-1) |

Rows 1,2,3,4 are pairwise distinct at cut one. Row zero can coincide
there with rows 1,2,3,4 only at ready (0,0),(3,0),(3,3),(1,3),
respectively. Cut two separates every such ambiguity except the pair
z=0,2 at ready (3,0).

In that remaining case both paths apply c from cut one to cut two.
Its permutation beta exchanges S and K for either crossing type. The two
receiver-piston samples and the common controls thus determine all four
cut-one pistons. A collision between the initial vectors P (z=0) and
P' (z=2) would require

    alpha P = -beta P' + s0,
    P' = s0-gamma P,       s0=(2,1,2,1),

and sum P=2, since q+r=3. Both initial vectors have the same coordinates
on K. If D=gamma, gamma preserves K and those two equations require
s0_i=s0_(gamma i), false for either possible K. If D=alpha, gamma
exchanges S and K, and summing the K equations gives sum P=3, another
contradiction. There is no remaining collision.

Hence for every common preparation, the ordered receiver samples at
cuts one and two distinguish all 25 crossing sources. A reader storing
these samples can reconstruct them. This supplies neither a current
native receiver with 25 distinct records nor an endogenous two-sample
archive.

| Source pair | Maximum at one cut | Maximum from history |
| --- | ---: | ---: |
| {p1,p1p} or {p4,p4p} | 9 | 9 |
| Any other pair | 17 | 25 |

The nine is a maximum over common preparations. For example, with
S={1,3}, K zero and ready (3,0), piston sources (1,0,1,0) and
(2,0,2,0) merge at cut one, so nine is not a universal equality.
The bounds cover every common preparation, including nonlinear source
codebooks within the two free source coordinates and nonzero common
receiving pistons. They do not cover payload-dependent auxiliaries,
a different split or varying counter origin.

## 4. The zero-record fibre and the absence limit

Use the existing total reader from reference-PROOF.md, with

    A=p1+p1p, B=p4+p4p, C=p1-p1p-2, D=p4-p4p-1.

The reader returns PRESENT exactly when z belongs to {1,4}.
KERNEL-Z6-SYNCHRONIZATION therefore implies that every raw origin-zero
launch becomes PRESENT by cut three. This particular reader has no
forever-BLANK launch. Its interpretation as a completed ring record is
established only on E.

Exactly the initial sheets z=0,2 have the same first three BLANK outputs
as E(0,0): their totals through cut three are (0,0,2,1) and (2,0,2,1).
The other sheets are PRESENT either initially or at cut one. On the
cut-three sheet z=1 the zero output is equivalent to

    AB=0, CD=3.

There are nine choices of (A,B), four of (C,D), and five of q, with r
then fixed by z=1. The four piston coordinates are uniquely determined
because 2 is invertible. Thus there are 180 cut-three checkpoints.
The canonical sheetwise bijections give exactly 2*180=360 initial
checkpoints with the entire same output history as E(0,0). Exactly one
belongs to E, so 359 lie outside the prepared family. This counts output
histories, not equality of full states; precisely one of those 359
shares the complete cut-three checkpoint of the prepared zero.

## 5. Removing the source reference pistons is impossible for E

The fixed reader in reference-PROOF.md uses both source reference pistons
as well as the receiver. It cannot be replaced, even after the write, by
a fixed counter-free function of (p4,p4p,q,r) that reads all 25 E messages.

At an E cut-three state write B=p4+p4p and D=p4-p4p-1. Then
A=1, C=2, z=1, q=4, r=1-B. Choose B nonzero. Keep the complete
complementary receiver unchanged and change A to -1 while keeping C=2.
The modified checkpoint has z=-1 and canonical

    V=(-1,B,-2,-D).

It lies in the same R fibre as the E cut-three state with B'=-B,D'=D,
whose V=(1,-B,2,D). That is a different prepared message. Canonical
whole-fibre recurrence puts the modified checkpoint arbitrarily late
on its actual tail. The same receiver tuple consequently requires two
different outputs at different times. No fixed counter-free receiver
function can do that. At any fixed known n>=3, in contrast, the receiver
piston pair is a bijective affine transform of the original pair; the
previous indexed reader remains valid.

## 6. Conditional scope of the oriented-contact objection

The original contact note, its forms B,C and its archive were not
available. The reported rule "choose the +w branch iff x=w modulo 4O"
is consequently treated as an exposed premise, not a reproduced result.
For w=sqrt5*(J-Jbar), its reduction modulo 2O is j^2+j^3, which is nonzero
in the marked coefficient basis. Under the reported rule, -3w and +5w
select +w while +3w and -5w select -w. This is a congruence selector,
not the sign of the integer multiplier of w.

The native impossibility has a precise hypothesis. If the complete
preparation, initial counter and every observation input factor through
x modulo 5O, the two inputs +5w and -5w produce identical complete
native histories, and cannot yield the reported opposite branch choices.
An arbitrary supplied preparation that reads x modulo 4O beforehand can
encode the branch into a pentit. That changes the input interface; the
mere characteristic-five state carrier does not prohibit it. Such an
encoding would still not implement the full integral contact law.

## Source map and remaining scope

Canonical premises, all at the public basis above:

- KERNEL-Z6-SYNCHRONIZATION: fixed-time sheet bijections and synchronization.
- U-NATIVE-INVARIANT-AND-NOWRITE: V, R, maximal invariant and actual recurrence.
- U-NATIVE-APPARATUS-HISTORY-FACTOR: quotient rules and apparatus-only limit.
- U-NATIVE-COMMON-READY-SOURCE-RETENTION: the five complete H_z maps.
- U-NATIVE-SOURCE-RECEIVER-RECORD: the distinct one-digit source-only writer.
- RELATIVE-CONTACT-INTEGRAL-LAW: the separate integral-contact carrier.

The current Canon is [pinned here](https://github.com/mathorn1973/twist-j/blob/6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed/canon/CANON.md).
No new registry row, gate decision, physical carrier, autonomous repair,
second message, renewal or Canon promotion is supplied. The original
audit custody recorded in PROVENANCE.md remains unresolved separately.
