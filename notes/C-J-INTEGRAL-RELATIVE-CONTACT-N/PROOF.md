# Integral relative contact: rigidity, a total extension, and its boundary

NON-CANONICAL / L1 / conditional analytical candidate-T.
Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
Reservation: #1832. No public status or original-U law changes.

## 1. Exact objects and additional premises

Let O=Z[j]=Z[X]/(1+X+X^2+X^3+X^4), K=Q(j), and conjugation j -> j^-1.
Use the marked coefficient basis (1,j,j^2,j^3), with literal equality.
The inherited identities are J=1+j^2, J^-1=-j-j^2, and (J-1)^3=j.
Set rho=J-1=j^2. Thus rho^5=1 and rho conjugate(rho)=1.

We deliberately supply the Cartesian carrier O^N, separately marked slots,
and the arithmetic account

    q(a)=Tr_K/Q(a conjugate(a))/2,
    E(x)=sum_i q(x_i).                                           (1)

This account and integer phase contacts already occur in #1419. No discovery
of either general construction is claimed. E is not identified with a
Hamiltonian, physical energy, or the energy of native U.

The proposed pair operation is specified independently of the output examples:

    x'+y'=x+y,
    x'-y'=rho(x-y).                                              (2)

Conservation of the sum, the assignment of rho to the relative coordinate,
and the identification of the two slots as intervention/readout ports are
NEW premises, not consequences of the axiom J. When (2) has no integral
solution, we choose identity on the COMPLETE pair. This completion is also
a premise. No uniqueness among all possible off-domain completions is asserted.

All statements below concern these complete integer states, not amplitudes
over configurations. There is no probabilistic rule or physical layer lift.

## 2. A self-contained minimum-norm lemma

For a=sum_(k=0)^3 a_k j^k, the trace of j^r is 4 if 5 divides r and -1 otherwise.
Therefore

    2q(a)=5 sum_k a_k^2-(sum_k a_k)^2.                           (3)

This is even, since squares equal their bases modulo two. Its matrix is
5I-11^T, with eigenvalues 1,5,5,5, so

    q(a)>= (sum_k a_k^2)/2.                                    (4)

In particular q is a positive integer on nonzero a and has finite bounded
sublevel sets.

Append a_4=0. Another exact form of (3) is

    2q(a)=sum_(0<=i<k<=4) (a_i-a_k)^2.                          (5)

If a is nonzero, the five coefficients are not all equal. Split them at their
minimum, with k occurrences of that minimum, 1<=k<=4. There are k(5-k)>=4
crossing pairs, each with squared difference at least one. Hence q(a)>=2.
Equality forces k=1 or 4, the two groups each constant, with their values
one apart. In O, these are exactly

    q(a)=2  iff  a in {+j^r,-j^r : 0<=r<5}.                    (6)

This proves the minimum and the complete minimum-shell classification without
a bounded search or an imported root-of-unity theorem.

## 3. Rigidity on the unrestricted Cartesian lattice

Fix any integer N>=1. Let A:O^N -> O^N be additive, commute with simultaneous
multiplication by J, and satisfy E(Ax)=E(x) for every x in O^N.

Additivity makes A Z-linear. Commutation with J implies commutation with
j=(J-I)^3, hence with every element of O. Thus A is O-linear, represented
by an N by N matrix over O.

Each standard column has input account q(1)=2. By (6), its image has exactly
one nonzero entry, belonging to {+j^r,-j^r}. Distinct columns must occupy
distinct rows: if columns i,k had entries u,v in the same row, the nonzero
input with components v,-u in positions i,k would map to zero. That violates
positive-account preservation. There are N columns and N rows, so

    (Ax)_i = u_i x_(pi(i)),  u_i in {+j^r,-j^r}, pi a permutation. (7)

Conversely each map (7) has all the stated properties.
If additionally sum_i(Ax)_i=sum_i x_i for every x, comparison of each column
forces u_i=1. Only whole-slot permutations remain.
An affine map preserving E must fix zero, so the same conclusion applies to
that affine class.

This is a complete scoped classification. It does not exclude nonlinear
maps, proper sublattices, other account forms, other scalar actions or larger
architectures. In particular it does not say all integer physics is trivial.

## 4. Exact integral admission and the total map

Over K, (2) has the unique solution

    x'=[J x+(2-J)y]/2,
    y'=[(2-J)x+J y]/2.                                         (8)

Let d=x-y. The first equation also reads x'=y+Jd/2. Since J is a unit of O,
x' is integral iff d belongs to 2O. Sum conservation then makes y' integral
as well. Thus the exact domain is

    Gamma={(x,y) in O^2 : x-y in 2O}.                           (9)

The map O^2 -> O/2O, (x,y) -> x-y, is onto; its kernel is Gamma.
Since O has rank four, [O^2:Gamma]=16. This index is a counting statement,
not a probability or an independently selected physical fraction.

Define the complete law C on ALL O^2:

    if (x,y) in Gamma:
        s=(x+y)/2, t=(x-y)/2,
        C(x,y)=(s+rho t,s-rho t);
    otherwise:
        C(x,y)=(x,y).                                         (10)

Both exact divisions occur only on the declared domain. No rounding,
postselection, discarded output, added bank or unrecorded error is used.
All eight integer coefficients remain part of the state.

The image of an accepted pair has difference 2rho t and remains in Gamma.
Its inverse is the same formula with rho^-1. The rejected complement is
fixed and is disjoint from Gamma. Consequently C is a total bijection and

    C^k(x,y)=(s+rho^k t,s-rho^k t) on Gamma,
    C^5=I on all O^2.                                         (11)

Its order is exactly five, as witnessed by (2,0). The fixed states are the
whole rejected complement together with the diagonal x=y inside Gamma.

On the accepted branch, before taking traces,

    x' conjugate(x')+y' conjugate(y')
      =2s conjugate(s)+2t conjugate(t)
      =x conjugate(x)+y conjugate(y).                         (12)

The rejected branch is identity. Thus C preserves both the total O-valued
sum and E on the entire carrier, including occupied and refused states.

C is translation covariant, exchange covariant, and common-J covariant:

    C(x+a,y+a)=C(x,y)+(a,a),
    C(y,x)=swap C(x,y),
    C(Jx,Jy)=J C(x,y).                                        (13)

For the last identity, multiplication by the unit J preserves membership in
2O. None of (13) asserts that an actual native-U operation implements C.
C is NOT additive: C(1,0)=(1,0), while

    C(2,0)=(1+rho,1-rho) != (2,0).                            (14)

Thus (10) evades precisely the additivity hypothesis of Section 3, rather
than contradicting its classification. On Gamma alone, in the (s,t) chart,
it is just (s,t)->(s,rho t). The physical meaning of the original slot split
is therefore still an explicit interface debt.

## 5. Repeated source sensitivity, with exact limits

Use two preparations at one common origin, (0,0) and (2,0). At every n=5k,
k>=0, their current receiver y is identically zero and the full pairs are
again (0,0) and (2,0). One step later their receivers are respectively

    0  and  1-rho != 0.                                      (15)

This gives an unbounded sequence of actual, common-time source-sensitive
transitions of one unchanged autonomous map. No intermediate reset or clock
control is inserted. It is strictly weaker than continuously loading new
independent messages: the SAME original distinction recurs.

The complete orbit from (2,0) is

    C^n(2,0)=(1+rho^n,1-rho^n).                               (16)

The chosen slot accounts are

    n=0 mod5:  (q(x),q(y))=(8,0),
    n!=0 mod5: (q(x),q(y))=(3,5).                             (17)

To check (17), for a nontrivial fifth root u, Tr(u)=Tr(u^-1)=-1,
q(1+u)=3 and q(1-u)=5. At the fifth step the transfer is undone exactly.
There is no newly permanent record, dissipative arrow, fresh-input source,
physical clock, proper time or relativistic geometry in this result.

The conserved account is not a bare-J invariant: q(1)=2 but q(J)=3.
Appending componentwise J as a free step would therefore invalidate account
conservation unless a separate complete law supplied its compensation.
Commutation in (13) does not repair this difference.

## 6. Reduction: an exact obstruction to naive finite checkpoints

Write lambda=1-j. The quotient O/(lambda) is F5 by setting j=1 in Phi5.
On Gamma, (10) gives

    x'-x=(rho-1)t, y'-y=-(rho-1)t.                             (18)

Since rho-1=j^2-1 belongs to (lambda), every slot is unchanged in this
quotient. The rejected branch is already identity. The induced map modulo
(lambda) is therefore the identity on the full pair.

This is NOT the same quotient as O/(5). The latter retains four coefficient
residues, and j^2-1 is nonzero there. It also is not the six-coordinate
original checkpoint F5^6.

There is no deterministic factor of C through coefficientwise reduction
modulo ANY rational integer M>=2 on the full Cartesian O^2. A factor would
require equal reduced inputs to have equal reduced outputs.

If M is even, compare (0,0) with (M,0). They have the same residue modulo M.
Both are admitted, and the second output receiver is

    (M/2)(1-rho),                                             (19)

whose constant and j^2 coefficients are M/2 and -M/2, not divisible by M.

If M is odd, M>=3, compare (2,0) with (M+2,0). Their residues agree.
The first is admitted and produces receiver 1-rho. The second has unequal
coefficient parity and is fixed, with receiver zero. Since 1-rho has
coefficients (1,0,-1,0), the reduced outputs differ.

These two witnesses prove the all-M statement. In particular, adding a
single fixed coefficient modulus such as 10 does not give a closed exact
update on all full states. Finite bounded-account shells can of course be
encoded separately; the theorem concerns this specific reduction map and
unbounded carrier. It does not exclude all finite-state encodings, bounded
preparations, histories or differently typed native bridges.

## 7. A deliberately supplied two-edge composition

On O^3, let C_12 and C_23 act on the respective complete pairs. Define

    T=C_23 C_12, with the rightmost operation performed first. (20)

The order, graph and slot interpretation are declared model inputs. T is
one time-independent map with no mutable program state. It is a bijection,
with T^-1=C_12^-1 C_23^-1, and conserves the full sum and E. Each substep
reads only its own two slots. This is algebraic locality on the given graph,
not emergence of physical space.

For x=(4,0,0), the exact first full step is

    T(x)=(2(1+rho), 1-rho^2, (1-rho)^2).                       (21)

Both pair contacts are admitted. The original third slot was zero and now
contains a nonzero datum supplied through the two edges. The respective
accounts are

    (32,0,0) -> (12,5,15).                                   (22)

The final value 15 follows by expanding (2-rho-rho^-1)^2 and taking half
its trace: [6*4+(-1)+(-1)-4(-1)-4(-1)]/2=15.

Order is consequential. Reversing the two edges on the SAME input gives

    C_12 C_23(4,0,0)=(2(1+rho),2(1-rho),0),                    (23)

with accounts (12,20,0). This is an exact warning against calling the edge
order unphysical without an additional equivalence theorem. The pair law
does not select a global geometry, ordering or composition principle.

More generally any fixed finite word of these pair maps on a fixed finite
number of slots is a conservative bijection. By (4), every orbit with a
fixed finite E lies in a finite set, and is therefore periodic from its
initial state. No transient merger or information loss occurs, but no
unlimited archive or thermalization theorem follows either.

## 8. What has and has not been constrained

The scoped universal rigidity theorem is Section 3. The integral admission
condition is forced by (2), not selected to fit a desired output. The total
completion, sum/difference prescription, arithmetic account interpretation,
slot interface and graph/order remain supplied choices. In particular the
choice rho=j^2 is marked by J but the decision to apply it to a relative
coordinate is not forced by the scalar identity J=1+j^2.

No claim is made that these premises select the only possible interaction
law. Replacing rho by another nontrivial fifth root gives the corresponding
conjugate/inverse family. The identity rejection rule is not derived from
reversibility alone. The all-M obstruction and order witness delimit two
specific costs of the construction rather than closing a physical owner.

Relative to #1419, the delta is the full Cartesian rigidity classification,
the exact pair admission set, a total nonlinear completion including refused
states, and its finite-reduction boundary. Its four-channel proper-lattice
phase construction and trace account remain credited predecessors.
Relative to #1831, the changed assumptions are the state carrier and the law.
This is not an implementation, extension-with-proved-projection, compilation
or hidden re-reading of U. None of U's fired restrictions is reopened.

All proofs here are authored analytical candidates. Supplementary finite
execution, if later recorded, checks only its frozen inventory. It does not
constitute independent theorem acceptance, experimental evidence, or public
Canon promotion.
