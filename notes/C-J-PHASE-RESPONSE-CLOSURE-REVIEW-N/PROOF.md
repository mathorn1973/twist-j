# Whole-carrier inverse, response cuts and phase records

PUBLIC / NON-CANONICAL / L1, conditional candidate-T.
Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
Session: ChatGPT-phase-response-closure-20261020-b2c0a3fb.
This is a result-exposed successor to #1607 under #1609. The equations,
canonical implementation and earlier outcomes were available to this author.
The derivation and executable here are newly written; they are not blind
predictions. No source scientific implementation is imported by the checker.
This text is frozen before that checker's first execution. Its analytical
claims and the later execution verdict are distinct.

## 1. Exact spaces and primary maps

All wave/tape arithmetic is rational. Let

    Y=((0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0)).

The first four sites are ordered ports. The stencil consists of the
even-coordinate-sum integer displacements of squared lengths 2,4,8,10,16,
with respective weights 6,1,15,1,1 divided by 324. Include zero to form B0,
and take D=Y+B0+B0, the exact 705-site finite Dirichlet carrier bound in the
source manifest. H on Q^D has diagonal 10/9 and these off-diagonal weights
when both endpoints belong to D. Missing exterior values are zero. These
are finite-domain statements, not an infinite-lattice limit.

Let P:Q^4 -> Q^D insert coordinates at the four ordered ports; P^T extracts
them. Set Qp=PP^T, J=I-Qp, K=(I+Qp)^(-1)=I-Qp/2, and T=KH. Thus

    P^T P=I4, Qp^2=Qp, J^2=J, P^T J=0,
    KJ=J, KP=P/2, P^T K=P^T/2.

The source injection S:Q^4 -> Q^D is Sz=Pz-(sum z)/5 * 1_Y.
In particular S^T S=I4-11^T/5. All operator products act right to left.
The complete free carrier is

    X=(u,v,A0,A1,B0,B1,k) in Q^1426 x Z/2Z.

The names B0,B1 in X denote four-dimensional tape blocks, not the stencil.
At either pointer value the literal free update is

    w=K(Hv-Ju+4P A0)=Tv-Ju+2P A0,
    beta=A0-(1/2)P^T(w-u),
    F(X)=(v,w,A1,B1,beta,B0,k+1 mod 2).                 (1)

No clean or unoccupied condition is imposed in (1).

## 2. Solve the complete inverse, not a response inverse

Suppose the output is (u',v',A0',A1',B0',B1',k'). Then v=u', w=v'
and beta=B0'. At a nonport, (1) gives u=(Hv)-w. At a port it gives

    w=Hv/2+2A0,
    beta=A0-(w-u)/2=u/2-Hv/4.

Consequently u=2 beta+Hv/2 at a port. Combining these two disjoint
coordinate rules determines every old wave coordinate uniquely:

    u=J(Hu'-v')+(1/2)P P^T H u'+2P B0',
    A0=B0'+(1/2)P^T(v'-u),
    F^(-1)(X')=(u,u',A0,A0',B1',A1',k'-1 mod 2).     (2)

The expression for u also equals K(Hu'-Jv'+4P B0'). The componentwise
solution above is used for the separately written inverse implementation.
Substituting (1) into (2) returns u,v and all four original tapes; the
pointer also returns. Conversely, (2) solves both port equations and the
nonport equation uniquely for arbitrary output coordinates, so substituting
it into (1) returns every given output coordinate. This proves both
compositions are the identity on the entire stated carrier.

For fixed k these maps are linear in all 1426 rational coordinates. Hence
an exact composition check on every standard basis vector certifies the
linear identities on the whole rational space; both pointer values are
checked. This is not a finite sampling argument for a nonlinear map.

F is not an involution. Take u=v=0, A0=e0 and A1=B0=B1=0. The first
output has v=2Pe0; the second has u=2Pe0, whereas initially u=0. The
pointer returning after two steps does not make the complete state return.

## 3. Quadratic conservation with arbitrary occupied tapes

Define the actual inherited account

    E(X)=(||u||^2+||v||^2-u^T H v)/2
         +2(||A0||^2+||A1||^2+||B0||^2+||B1||^2).    (3)

H is symmetric. Rearranging (1), using the definition of beta, gives

    w+u-Hv=2P(A0+beta),
    P^T(w-u)=2(A0-beta).

Therefore the wave-energy change is

    (w-u)^T(w+u-Hv)/2
    =2(A0-beta)^T(A0+beta)
    =2(||A0||^2-||beta||^2).

The tape permutation changes only the replaced A0 norm, by the opposite
amount. Thus E(FX)=E(X) for arbitrary rational waves and all occupied tapes.
This polynomial identity proves the universal claim. Checking E on basis
vectors alone would not prove a quadratic identity, and is not presented
as doing so. The executable additionally checks the complete basis and two
full-support occupied states, supplementing this derivation.

The stencil has 12,6,12,24,6 elements in its five shells. Its off-diagonal
row bound is (12*6+6+12*15+24+6)/324=8/9. The Dirichlet restriction can
only decrease it. Thus ||H||_2<=2, and Cauchy-Schwarz proves E>=0. Its
square root is a seminorm on the rational carrier embedded in the real
vector space. No physical identification of this account follows.

## 4. Ordered cuts and a defined replacement for the old D2 expression

For V(z)=(0,Sz,0,0,0,0,k), the four incoming tape blocks in the first
four calls are zero. Define f=Sz and the following wave recurrence:

    w0=f, w1=Tf,
    w2=(T^2-J)f,
    w3=(T^3-TJ-JT)f,
    w4=(T^4-T^2J-TJT-JT^2+J^2)f.

The successive cuts are -(1/2)P^T(w1), -(1/2)P^T(w2-w0),
-(1/2)P^T(w3-w1), and -(1/2)P^T(w4-w2). Hence the four maps
Q^4 -> Q^4 are, with all domains fixed as in section 1,

    R0=-(1/2)P^T T S=-(1/4)P^T H S,
    R1=(1/2)P^T(I-T^2)S,
    D2=(1/2)P^T(T-T^3+TJ)S,
    D3=(1/2)P^T(T^2-T^4+T^2J+TJT)S.                 (4)

Only P^T J=0 and J^2=J were used to remove terms. The recurrence and
the cut extraction are separate routes to (4); the checker compares all
four columns of each with four actual full-state F updates. At the fourth
boundary the tape order is (A0,A1,B0,B1)=(R0z,R1z,D3z,D2z).

The predecessor's expression D2=R1 K_{P^T H P} has no definition of its
subscripted operator in the frozen contract. It therefore remains
STOP_UNDEFINED: neither proved, disproved nor retrospectively assigned a
meaning. Formula (4) is a newly specified replacement obligation with its
own derivation and prospective test. It is not a rescue of that old text.

## 5. Full four-dimensional determinant and inverse certificates

The six different port-to-port displacements all have squared length 2.
Thus Jp=P^T H P=(59I+11^T)/54. The fifth-site coupling column is
(1,6,6,0)^T/324. Subtracting one fifth of each five-site row sum, as
required by S, gives

    M=P^T H S=(1770I-v1^T)/1620,
    v=(349,354,354,348)^T, 1^T v=1405,
    R0=-M/4.                                        (5)

These entries follow from the actual geometry, not a supplied output
matrix. To compute the full determinant, write M=aI+gamma 1^T with
a=59/54 and gamma=-v/1620. On ker(1^T), dimension three, M acts by a;
on the one-dimensional quotient it acts by a+1^T gamma=73/324. Choosing
a basis of that kernel and one complementary vector makes M block
triangular. Therefore

    det R0=(1/4)^4 (59/54)^3 (73/324)
          =14992667/13060694016 != 0.                (6)

This is a full four-dimensional argument, not an inference from a minor.
An additional direct certificate is

    R0^(-1)=-(216/59)(I+v1^T/365).                  (7)

Indeed (1770I-v1^T)(I+v1^T/365)=1770I, since
1770-365-1405=0. The reverse product has the same cancellation. The
checker separately uses the 24-term determinant expansion and both matrix
products; it need not assume the conclusion of a Gaussian solver.

In particular M[0,0]=1421/1620. The literal old target I4-M/2 has entry
1819/3240, while the actual R0 has entry -1421/6480. Their inequality
is preserved as a false predecessor claim. The successor proves (5), not
the old target. Likewise no statement about R0^(-1) substitutes for (2).

## 6. Exact old-port controls and the actual seven-row history

The native selector is sum(x)+2 theta(n) modulo five, where theta(n) is
the parity of the binary digit sum. For x=(a,b,c,d,q,r), the five selected
generators, with every output reduced modulo five, are explicitly

    g0(x)=(b,a,d,c,q,r),
    g1(x)=(-c,-d,-a,-b,-q,-r),
    g2(x)=(2-c,1+r-d,2-a,1-r-b,1-q,-r),
    g3(x)=(2-a,1-b,3-c,4-d,1-q,1-r),
    g4(x)=(2-a,1-b,3-c,4-d,2-q,1-r).

The contact letters b,d,e below mean g1,g3,g4 respectively. The balanced
lift is ell=(0,1,2,-2,-1). For the five phase pistons

    (1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1), (4,4,4,4),

the piston sum is one. With the old ready pair (q,r)=(0,1), at n=0
the selector is 2. That generator sends the last coordinates to (1,4).
The specified control piston (2,0,0,0) instead selects 3 and sends them
to (1,0). Applying the actual lift

    eta(q,r)=(ell(q)/2,(ell(r)+1)/2,0,0)

therefore gives exactly

    z_A=(1/2,0,0,0), z_B_control=(1/2,1/2,0,0).       (8)

The old pair ((0,-1/2,0,0),(1/2,0,0,0)) is false for this nominated
history. The first-vector-equal/second-vector-different test alone would
not establish (8); the successor explicitly tests all eight coordinates.

The common-ready protocol has zero wave/tapes/buffer, signs (+1,+1)
and bank b=capacity. Rows c=0,2,3,5,6 advance both actual native heads
and n; rows 2,3,5,6 additionally execute F. Row 1 captures the current
second head's last two coordinates in d and makes contact A; row 4 makes
contact B from d. Contact with source z and sign sigma proposes v+sigma Sz,
books Delta E into work and subtracts it from the bank, flipping sigma if
and only if the proposed bank is within both bounds. The eight boundaries
are exactly (n,c)=(0,0),(1,1),(1,2),(2,3),(3,4),(3,5),(4,6),(5,7).

The #1577 control uses the original capacity 4/5. Equal source quotients
produce equal complete receiver histories by deterministic induction;
the two native heads need not be equal. The changed control differs in d
at boundary 2; the wave/tape history first differs at boundary 5, contact
B. The finite audit checks this timing and both actual guards, not just
the final decoder. It does not claim that this control transmits phase.

## 7. Literal contact prefixes and the two positive source families

For piston matrices X,Y define h=(det(X+Y)-det X-det Y)/2 in F5 and
delta=1-h^4. The supplied contact uses the literal chronological word

    Ucal_y, e_y, d_y, W_b, b_x, b_y, W_b,
    d_y, e_y, W_b, b_y, b_x, W_b, Ucal_y.             (9)

Here W_b fixes h=0. Otherwise let s=0 for h=1,2 and s=1 for h=3,4;
apply b to both cells if s differs from the old bit, and set the bit to s.
The paired b changes h to -h. Thus conjugating paired b by W_b gives
paired b at h=0, or a bit flip at h!=0. The e d translation of q and
its commutator then give q_y -> q_y+3 delta with all other data restored.
Ucal_y replaces r by P_q(r), with P0=(1 2), P1=I, P2=(0 2),
P3=P4=(0 1). Consequently (9) has the complete endpoint

    (q,r) -> (q+3delta, P_(q+3delta) P_q(r)).          (10)

The source, both pistons and bit return. Reversing the involutive leaves
gives the full inverse even for occupied q,r. The implementation executes
the leaves; (10) is a comparison formula, not a replacement for execution.

For #1579, the shared receiver piston is (1,0,0,1), initially q=r=0.
The original source j gives delta=1 and j^4 gives delta=0. Their actual
receiver endpoints are (1,0,0,1,3,1) and (1,0,0,1,0,0). The first native
tick selects 1 and 2 respectively, giving lifted vectors

    z_+=(1,0,0,0), z_-=(1/2,1/2,0,0).                (11)

Two copies contain four cells and two supplied bits, with 28 prefix
leaves. Both receiver cells are the downstream heads, not extra copies.
All four pairs use the original capacity 2.

For #1581 use references YA=(0,2,2,0), YB=(4,2,2,0), YC=(1,1,0,1).
Direct determinant polarization gives the five bit triples

    phase k:  0    1    2    3    4
    bits:    110  001  000  100  010
    M:        3    4    0    1    2    (weights 1,2,4 modulo 5).

For each reference execute (9), the stated number of whole-cell additions
into the collector, then the reversed word. Each addition fixes the
reference, so inverse contact restores source/reference/bit even when the
reference was occupied. Starting the common collector at (4,0,4,2,0,0)
leaves its piston at (1,0,0,1) and its last coordinates at (3M,M).
The first actual native tick and lift give

| M | generator | (q,r) | z | cold E |
|---|---|---|---|---|
| 0 | 2 | (1,0) | (1/2,1/2,0,0) | 3/20 |
| 1 | 1 | (2,4) | (1,0,0,0) | 2/5 |
| 2 | 0 | (1,2) | (1/2,3/2,0,0) | 17/20 |
| 3 | 4 | (3,3) | (-1,-1/2,0,0) | 2/5 |
| 4 | 3 | (4,2) | (-1/2,3/2,0,0) | 23/20 |

There are two sources, three shared references and two collector/heads,
seven cells and one restored work bit. Each source takes 3*(14+14)+7=91
leaves, hence 182 for the pair. These additions and contacts are supplied
interfaces with an externally addressed schedule. They do not advance the
old downstream counters during the prefix. All 25 pairs use capacity 5.

The first cold energy is ||Sz||^2/2. Conservation and the seminorm in
section 3 bound the two-kick energy by (sqrt(e_A)+sqrt(e_B))^2, at most
8/5<2 for (11) and 23/5<5 for the five-vector family. From cold work zero,
work equals the added classical energy and bank=capacity-work. Nonnegative
energy also enforces the upper bank bound, including negative second
increments. This proves both guards accept in both source families. The
checker nevertheless evaluates the literal guards at every boundary.

## 8. Actual record-only recovery and retention

On the accepted cold branch, linearity gives the terminal wave/tape vector
F^4 V(z_A)+F^2 V(z_B); this adds only rational coordinates, not clocks.
Direct tape wiring places the chronological cuts at (A0,A1,B1,B0).
Consequently

    b0=R0 z_A, b1=R1 z_A,
    b2=D2 z_A+R0 z_B, b3=D3 z_A+R1 z_B.             (12)

The first cut moves through B0,B1,A1,A0, while the second moves through
B0,B1,A1. Neither is overwritten by contact B. This is retention through
the stated two uses, not indefinite retention under future free updates.

The record (b0,b2,sigma_A,sigma_B,d=None), on the accepted branch, gives

    a=R0^(-1)b0, b=R0^(-1)(b2-D2 a).                (13)

Its reader receives no source cell, native head or unrecorded source label.
The two vectors in (11) and the five vectors in the table are each distinct;
(13) recovers them, proving four and 25 different ordered retained records.
The executable runs all actual prefixes and all eight protocol boundaries
before constructing that record. It implements this factorization itself;
it does not call the canonical reader or claim a new API-security result.

A limited occupied-archive extension is also exact: with u=v=A0=A1=0
but arbitrary initial outgoing tapes B0=c0,B1=c1, the incoming sequence
is 0,0,c1,c0. At cut 2, the direct c1 term cancels its 2Pc1 wave term.
At cut 3 it contributes -Jp c1/2; the direct c0 term cancels. Thus b0,b1,b2
in (12) remain unchanged, while b3 gains -Jp c1/2. The wave/tape evolution
is linear, so the eight old-archive basis columns certify this extension.
This does not extend (13) to arbitrary nonzero initial waves or A0,A1;
those would require subtraction of additional response terms. Full arbitrary
occupancy in sections 2-3 concerns F and its inverse, not that restricted
record formula.

## 9. Scientific boundaries and the inherited discrepancies

E1: the old R0 target is false; (4)-(7) supply the correctly defined result.
E2: the old exact vectors are false; (8) and its nominated history are the
replacement. E3: (2) supplies the full inverse, and (4) a defined response
replacement; the undefined old K relation remains STOP_UNDEFINED. E4:
(6)-(7) supply full determinant/inverse certificates, and section 2 gives
the noninvolution witness. E5: this document audits the actual resources.
Execution-dependent dispositions appear only in the later result record.

Three binary outputs are necessary to distinguish five labels because
two bits have at most four values. This does not prove a minimum number
of physical cells. Deleting every W_b from (9) forces delta=1; all three
weighted contributions then give M=2, independently of the source. A zero
outside-family piston also has all three bits one and aliases phase j^4.
Thus the displayed five-phase dictionary does not detect absence.

The capacities pay only for the classical wave/tape kicks. No prefix or
preparation energy, autonomous prefix controller, independently late input,
whole-apparatus renewal, native/physical admission, occurrence law or layer
lift is established. Both source messages were initially present and the
second is captured before its later kick. Source/reference/bit restoration
does not erase the retained archive or renew the full apparatus. The old
completed #1607 remains PARTIAL / CHANGES_REQUIRED with its evidence intact.
