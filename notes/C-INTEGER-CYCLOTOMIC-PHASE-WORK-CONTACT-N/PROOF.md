# An integer phase contact with one conserved positive energy

NON-CANONICAL. Reservation #1419. Conditional candidate-T.
A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

## 1. What this construction answers

Issue #1418 closes the fixed point-to-basis, monomial-contact, diagonal-record
route for equal microscopic diagonals. A different possibility is to make
relative phase itself retained INTEGER COEFFICIENT DATA, rather than a
coefficient of a quantum superposition of ontic configurations. We construct
that possibility here. It demonstrates exact reciprocal energy exchange;
it does not derive this new carrier or contact from unchanged native U.

The full state consists of sixteen unbounded integers subject to explicit
linear congruences. No Hilbert space of physical states, probability law,
continuous time, measurement postulate or energy-deficit register is used.
The arithmetic architecture and its energy interpretation are selected.

## 2. Scalar arithmetic and integer energy

Let O=Z[j], Phi_5(j)=1+j+j^2+j^3+j^4=0, and conjugation j -> j^4.
The ordered integer basis is (1,j,j^2,j^3). For
alpha=sum_(k=0)^3 x_k j^k, define

    q(alpha)=Tr_(Q(j)/Q)(alpha conjugate(alpha))/2.

The four embeddings are sigma_a(j)=j^a, a=1,2,3,4. Their traces obey

    t(k)=Tr(j^k)=4 if k=0 mod5, and -1 otherwise.

Consequently

    2q(alpha)=5 sum_k x_k^2-(sum_k x_k)^2,
    q(alpha)=2 sum_k x_k^2-sum_(k<l) x_k x_l.       (1)

The form is even before division by two: integer squares have the same
parity as their bases. The Gram of 2q, Q=5I-ones, has eigenvalues 1,5,5,5,
so q is a positive integer on every nonzero alpha and q(0)=0.
In particular q(alpha)>=sum x_k^2/2. This is coercive on the whole
rank-four lattice, not just in the marked principal embedding.

Multiplication by j is an integer bijection and preserves q because
j conjugate(j)=1. With phi=-j^2-j^3 and J=1+j^2,

    phi J=j.                                      (2)

Thus the order-five phase is an algebraic part of the known cyclotomic
arithmetic. Choosing it as a contact is different from executing the full J:
q(1)=2 whereas q(J)=3. We do not relabel the radial J action as this phase.

## 3. The complete admitted lattice and full inverse

Fix the real sign matrix already used by the Galois code:

    H=((1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1)).

Direct multiplication gives H=H^T and H^2=4I. Declare

    L=H O^4 subset O^4.                            (3)

Equivalently b belongs to L iff every coefficient of every component of
Hb is divisible by four. The inverse chart is a=Hb/4, so every a in O^4
gives exactly one b in L. The carrier has Z-rank sixteen. Since
abs(det H)=16, its index in O^4 is 16^4=65536.
It is infinite and full rank, but it is a proper sublattice.

For r in Z/5Z define

    P_r=diag(j^r,1,1,1),
    B_r=H P_r H/4=I+(j^r-1) ones_(4x4)/4.          (4)

The fractions in the ambient matrix do not create fractional admitted
states. If b=Ha, then B_r b=H P_r a belongs to L. Hence

    B_r B_t=B_(r+t), B_r^-1=B_-r, B_r^5=I.         (5)

These identities hold on EVERY occupied admitted state, not only on the
two preparations below. Exact division in (3) is part of the declared
domain. For r!=0 the matrix is not an integer map on all of O^4:
the image of (1,0,0,0) has other entries (j^r-1)/4, which are not in O.
That ambient input also fails admission. B_0=I is ambient integral.
No off-lattice rounding or modulo reduction is supplied.

## 4. One energy, four channels, and a declared split

Define fixed nonnegative channel costs

    E_i(b)=q(b_i), E(b)=sum_(i=0)^3 E_i(b).

Orthogonality of H gives the FIELD identity

    sum_i (B_r b)_i conjugate((B_r b)_i)
    =sum_i b_i conjugate(b_i).                     (6)

Indeed H^T H=4I and P_r^*P_r=I. Taking half the field trace proves
E(B_r b)=E(b). The same identity preserves the sum of squared magnitudes
at every embedding, but those separate readings are not integer q.

Fix the split by the signs of H's second column (+,-,+,-):

    F=E_0+E_2, M=E_1+E_3.                         (7)

Both parts are actual sums of fixed positive channel costs. They are not
updated by assigning an energy discrepancy. From (6), for every b in L,

    Delta F(b)=F(B_r b)-F(b)=-Delta M(b).           (8)

This structural split is a chosen convention of the constructed example.
Its physical identification as field versus matter is NOT asserted. The
symbols F/M here denote two arithmetic channel groups, not #1413's
unbounded lattice Hamiltonian components. Selecting physical channels,
their locality and an accepted energy law is a separate obligation.

## 5. Complete relative-phase and work account

Take literal integer configurations

    b_s=(4,4j^s,0,0), s=+1,-1.                    (9)

Both belong to L: their chart is
a=(1+j^s,1-j^s,1+j^s,1-j^s). Their initial costs are
(E_0,E_1,E_2,E_3)=(32,32,0,0), F=M=32 and E=64.
The third and fourth channels start at zero and remain explicit in the
output. The phase orientations have identical initial channel energies;
their integer coefficients, and therefore their complete states, differ.

For delta=(j^r-1)(1+j^s), equation (4) gives

    B_r b_s=(4+delta,4j^s+delta,delta,delta).        (10)

Using t(k) from section 2, expansion of (1) yields

    E'_0=26+2t(r)+3t(r+s)-t(r-s),
    E'_1=26+2t(r)+3t(r-s)-t(r+s),
    E'_2=E'_3=6-2t(r)-t(r+s)-t(r-s).              (11)

Thus the complete fixed-split exchange is

    Delta F=2[t(r+s)-t(r-s)]
           =10(1_(r=-s mod5)-1_(r=s mod5)),
    Delta M=-Delta F.                             (12)

For the contact r=1 the full account is

| Input | Integer output | Channel costs | (F,M) |
|---|---|---|---|
| b_+ | (3+j^2,-1+4j+j^2,j^2-1,j^2-1) | (17,37,5,5) | (22,42) |
| b_- | (4+j-j^-1,j+3j^-1,j-j^-1,j-j^-1) | (37,17,5,5) | (42,22) |

Therefore Delta F_+=-10, Delta F_-=+10, with the opposite M changes.
The individual E_0 changes are -15 and +5; they are NOT a symmetric pair.
The balanced values refer precisely to split (7). For r=0 the map is
identity. Contacts r=2,3 give (22,22,10,10) for either s, with zero F/M
change. Contact r=4 reverses the r=1 accounts. Nothing is discarded.

For integer N, multiplying all sixteen coefficients by N multiplies every
energy and every change by N^2. The carrier and outputs are unbounded.

## 6. What the additional information and contact actually are

The reduced datum (E_0,E_1,E_2,E_3) cannot determine the contact account:
(9) has the same datum and opposite exchanges. The missing information
is retained integer relative phase, including the cross terms in (10).
No probability distribution or quantum off-diagonal density is required.

In the chart a=Hb/4 the entire contact is only a_0 -> j^r a_0; the other
slots are fixed and their separate q values remain constant. The b-channel
costs are quadratic interference readings in that chart. This observation
locates the selected structure, rather than eliminating it: we have fixed
b as the material channel frame in the example, and that frame is NOT
selected physically by the arithmetic. The prior occurrence of H in a
Galois code does not make (4) an operation of original U.

Independent factors j^(r_i) and permutations of the b slots preserve the multiset
of channel q values. They cannot produce (17,37,5,5) from (32,32,0,0).
The missing native implementation is therefore a channel mixing/reading
contact at this declared scope, not more independent phase rotations.
This is not a theorem about every possible native-U encoding or limit.

As a deterministic bijection of whole points L, B_r still has a permutation
address lift on ell2(L). Mixing four arithmetic coordinates is not mixing
quantum amplitudes over those ontic points. The two preparations (9) are
distinct point states; their point densities do NOT have equal diagonals.
Consequently #1418 is neither contradicted nor circumvented inside its
fixed class. This example instead changes the state/observable dictionary.

## 7. Why this is not yet the endpoint quantum bridge

Before taking the trace, expansion of the witness split gives the exact
field identity

    Delta[(b_0 conjugate(b_0)+b_2 conjugate(b_2))/2]
       =(j^r-j^-r)(j^s-j^-s).                     (13)

Its trace is (12). This also gives the separate principal comparison:

For the optional marked principal reading e_i=|b_i|^2/2, the same contact
preserves the sum, with initial e=(8,8,0,0). It gives

    Delta(e_0+e_2)=-4 sin(2pi r/5) sin(2pi s/5).

At r=1 this is -(phi+2) and +(phi+2), not the trace values -10,+10.
The principal reading is not the coercive rank-sixteen integer energy.
We choose neither as measured SI energy, and do not rescale either to
the inherited instantaneous Hamiltonian target +/-sin(2pi/5)/2.

The period-five contacts supply a finite-step exchange, not continuous
Hamiltonian time, a current commutator, or the complete #1413 common
charge/field operator. No map is supplied from an endpoint configuration
to this coefficient carrier with the same charge and electric observables.
There is no physical preparation, Gauss constraint, fermion, particle,
spatial propagation, photon phase, Born occurrence or apparatus closure.

The next physical/native bridge must independently specify that map,
realize (3)-(4) in an admitted complete native carrier, and justify the
b-channel energy frame and its coupling. A change of coordinates or a
transported work matrix cannot replace these obligations.

## 8. Relation to the existing Galois option and evidence ceiling

Public P-U-GALOIS-FIBER-CODE-1 proves a correlated coherent code for the
free, noninjective linear pushforward of U. Its isometry is restricted to
the code; it is not the literal archive permutation of #1417. For example,
normalized coded 1 and j have identical initial microdiagonals 1/16 on
the sixteen addresses. Raw final LOW probabilities are 1 and 1/16,
whereas literal archive-and-trace gives uniform four-point populations
for both. A point-only continuation cannot reconcile them by #1418.
That route therefore still needs a physically justified code/mixing contact.

P-QDD-STABILIZER-APPARATUS-1 already treats rational mixers and common
lattices, including a multiple-setting obstruction. Here all B_r share
one fixed lattice and commute. We assert no common lattice for its
incompatible settings, universality or novel general lattice theorem.

The integer phase j=phi J and its positive trace metric are inherited
arithmetic, also used in draft #1415. Issue #985, C-J-SOURCE-COUPLED-METER-N,
already studies chosen source-sensitive integer contacts and a classical
Fourier response involving J; its physical/native implementation remains
open. The Canon also has conservative integer-chain work constructions.
No priority is claimed for reversible integer energy transfer in general.
The return here is this full fixed-lattice phase contact and its exact
relative-phase-dependent positive channel account.

This original constructive contact, exact integer energy table and audit
are Apache-2.0. Internal static reviews are not independent public acceptance.
Finite fixtures audit formulas; the all-state statements rest on the proofs.
No canonical status, old scientific source or physical owner is changed.
