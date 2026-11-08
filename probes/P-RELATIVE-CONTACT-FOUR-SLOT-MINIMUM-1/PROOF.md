# Complete finite reduction and physical boundary

NON-CANONICAL / L1 / conditional candidate-T, with the finite exclusion
conditional on the pinned verifier completing and independent review.
Author A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

## 1. The declared law

Let O=Z[j], j^4=-(1+j+j^2+j^3), rho=j^2, pi=1-j.
Define C^k on x-y in2O by preserving x+y and multiplying x-y by rho^k;
fix the complete pair otherwise. This is the added contact of #1833.
The admitted set is invariant since its difference becomes rho^k(x-y).
Its inverse uses 5-k, and C^5=I. Set s=(x+y)/2 and t=(x-y)/2.
Since rho*bar(rho)=1, the sum of squared Hermitian norms is
2s*bar(s)+2t*bar(t) both before and after. Thus S and h are conserved.
All these statements include refused and occupied states.

For x=sum c_i*j^i,

    q(x)=(5*sum c_i^2-(sum c_i)^2)/2 >= sum c_i^2/2.

This follows from (sum c_i)^2<=4*sum c_i^2. q is integer since squares
equal their arguments modulo2; equality q=0 forces x=0. Positive bounded
q-shells are finite. The matrices and physical roles are premises.

## 2. Why only three energy levels and these bank residues remain

O/(pi)=F5, with residue r(x)=sum c_i modulo5. An admitted contact changes
x by (rho^k-1)(x-y)/2 in pi*O; refused contacts do nothing. Hence each
slot keeps its pi residue between permutations, and the full histogram
is invariant. Input data have histogram (21,1,0,0,0); positive output
data have (18,0,0,4,0), in residue order0..4.

Exactly four auxiliary slots are available. Therefore ALL four initial
auxiliary residues must be3 and the final bank residues must be0,0,0,1.
The data norm is36 at both ends. Thus h(b)=h(a), q(b)=q(a), and S(b)=S(a)-6.
These are necessary, not sufficient, endpoint tests.

Modulo5 the formula for q gives 2q=-r^2, or q=2r^2. At r=3,
q=3 modulo5; positivity therefore gives q>=3 without a numerical search.
The total auxiliary energy is12 modulo5 and at least12. Consequently
the only totals below27 are12,17,22. Every constituent has q<=22 and
sum c_i^2<=44; the coefficient box [-6,6]^4 is complete. Every initial
multiset of four residue3 entries and every final multiset with three
residue0 entries and one residue1 entry in this box is explicitly enumerated.
The recursion uses the nondecreasing (q,coefficient-vector) scalar order
and prunes only when the remaining number times the current smallest q
exceeds the remaining budget. This is a complete multiset enumeration.
No Galois reduction or unproved orbit representatives are used.

## 3. Parity and reachability certificates

For each class r in O/2O, the parity of the number of slots in class r
is invariant. Every admitted contact removes two entries in one common
class and adds two entries in one common class. Refused contacts and
permutations preserve these parities. The sixteen-bit XOR is thus a
necessary exact filter, not a complete invariant classification.

After it, the code treats the complete state as a sorted tuple of26
values. This is an exact reachability quotient because arbitrary
whole-slot permutations are allowed. Each step selects an unordered
pair of distinct existing values in a common parity class and every
power k=1..4. Equal-value pairs and mismatched-parity pairs are identities.
Both orientations give the same unordered output pair. Zeros remain
in the tuple; a nonzero-zero contact is included. Thus every generator
edge is included. Reverse edges occur with5-k.

Breadth-first exploration certifies a component only when the queue is
empty. If it would contain more than60 states, it returns UNKNOWN.
For each account-compatible, parity-compatible pair, a closed target
component not containing the source, or a closed source component not
containing the target, proves disconnection. The arbitrary cap contributes
no inference. If even one pair has neither certificate, the verifier
cannot conclude the lower bound. Hashes summarize regenerated certificates;
the actual mathematical evidence is complete graph closure, not a hash.

## 4. Upper bounds, signed minimum, and honest costs

The positive sixteen-contact witness and its fixed-address transcription
are from the author's Průzkum4 note and its follow-up of2026-11-01.
Its input bank is (-1-j,1+2j,2+j^3,2+j^2), with accounts(3,8,8,8).
Its final bank is (1,-1+j,-2-2j-j^3,2j+j^2+2j^3), with accounts(2,5,10,10).
Both have h=14-phi, q=27. Their sums differ by-6. A full successful
replay proves the upper bound27, without finding every account27 path.

For signed output(-3,3,3,3), initial bank residues must include2,3,3,3.
Each costs at least3, so four slots and account12 are lower bounds.
The compressed fourteen-power-contact word sends the bank
(eta,-eta,-eta,-eta), eta=1+j, to(-2eta,0,0,0). Full multiset equality
and inverse are checked. This proves attainment, not minimal length.

The auxiliary energy at either endpoint is unchanged. Accounts12 and27
are prepared capacity, not dissipated work. Contact count is not physical
elapsed time; a C^k token may require multiple primitive contacts.

## 5. Retained-output renewal and the prospective physical advance

For N retained signed outputs, histogram balance forces the initial total
changing auxiliary to contain N residues2 and3N residues3. For N positive
outputs it needs4N residues3. Returning other resources can be cancelled
from both sides. Thus L_aux>=4N and E_aux>=12N. Independent signed
witness copies attain(4N,12N). Positive copies give the upper bound27N,
but the single-output minimum does not prove a27N many-output lower bound.
No clean reset of the used bank can keep the prepared output and restore
every other resource: its residue histogram differs. Reversing the whole
word restores the bank while undoing the output; exchanging with a fresh
bank transfers the changed state to that bank. Neither is free renewal.
These analytical consequences were already in #1847 and the author notes;
they are interpretation and scope, not newly discovered assertions here.

For a fixed word, contacts preserve the complete residue vector, while
permutations act by one input-independent permutation. Therefore residue
Hamming distance between any two input states is preserved by that word.
A common-bank encoder that increases this distance is impossible in this
alphabet. This accounts for the two-input obstruction in #1847, regardless
of added common-bank size or energy. A known-input preparation does not
prove a common unknown-input encoder. Adaptive selection of permutations
is an added controller whose own state and reversibility need accounting.

The defensible physical direction is a complete preparation, response,
retained record and renewal model on one carrier, with a common law and
specified source family. This probe establishes only its preparation
resource constraint. Identifying q with measured energy, or the endpoint
with a physical event, needs its own bridge; two-architecture replay
cannot supply it. The current native, occurrence and apparatus owners
remain open. There is no automatic promotion of #1833 or #1845.
