# Preregistration: integral Gram contact and occupied archive

Candidate: C-INTEGRAL-GRAM-CONTACT-ARCHIVE-N.
Owner: ChatGPT-integral-gram-20261031. Reservation: #1844.
Author: A. M. Thorn <thorn@twistj.com>. SPDX-License-Identifier: Apache-2.0.
Status: NON-CANONICAL / L1 / PREPARATION_ONLY before scientific execution.
Public basis: a193e389fb1ddb0bdc89165b015c95a17eb1e425, Public Canon v106.

This is an analytical candidate with a preregistered exact finite audit, not
a formal P-probe or a public T claim. The formulas and witnesses below were
derived analytically before the pin. They are not blind numerical discoveries.
An analytical reviewer saw the proposed theorem but no verifier. A separate
computational breaker will receive this frozen file alone, write its own
implementation and freeze it publicly before any output comparison.

## 1. Equation and complete carriers

O=Z[j]=Z[X]/(1+X+X^2+X^3+X^4), K=Q(j), conjugation j -> j^-1.
Use the ordered coefficient basis (1,j,j^2,j^3), with literal integer equality.
rho=j^2=J-1. For a=(a0,a1,a2,a3),

    q(a)=[5*sum(a_k^2)-(sum a_k)^2]/2
        =Tr_K/Q(a*bar(a))/2.

For any fixed N>=2, z belongs to the full Cartesian O^N and
G=z*z^dagger. The record domain is EXACTLY G_N={z*z^dagger:z in O^N};
no characterization by arbitrary integral positive matrices is assumed.

For distinct i,j, let d=z_i-z_j. The complete supplied contact C_ij^e,
e in {+1,-1}, is identity if d is not in 2O. Otherwise put

    s=(z_i+z_j)/2, t=(z_i-z_j)/2,
    z_i'=s+rho^e*t, z_j'=s-rho^e*t,

leaving all other slots unchanged. This is the contact of #1833, not native U.

For v=e_i-e_j and A=I+(rho^e-1)*v*v^T/2, define

    D_ij(G)=G_ii+G_jj-G_ij-G_ji.

The proposed record operation is A*G*A^dagger if every coefficient of
D_ij(G) is even, and identity otherwise. On G_N that condition is precisely
D_ij(G) in 2O_F. The complete O_F norm is used; its scalar trace is NOT used
to decide admission. No rounding or unrecorded residue branch is permitted.
Permutations act on G by simultaneous row/column permutation.

## 2. Analytical claims and failure conditions

A. On all O^N, d in 2O iff d*bar(d) in 2O_F iff it is in 4O_F.
The inherited binary norm descent O/(2)=F16, O_F/(2)=F4 makes this
equivalent to a^5=0 iff a=0 in a field. This application, not inertness,
is the proposed new delta.

B. The above record operation is well-defined on G_N, integral, invertible
with exponent -e, and exactly satisfies G(C_ij^e z)=C_hat_ij^e(G(z)).
It preserves the full h=sum z_i*bar(z_i), E=sum q(z_i), and S=sum z_i
(S is an additional read if its literal value is requested).
The contact has fifth power identity. The result holds on occupied/refused
states and all actual Gram fibres, without primitive or unit-only assumptions.

C. Any fixed word of these contacts and slot permutations has exact forward
and backward Gram continuation. A supplied finite cyclic program uses the
record (c,G), with no hidden representative choice. At S!=0 the stronger
record (c,G,S) recovers z_i=(sum_j G_ij)/bar(S). At S=0 it need not do so.
No minimality of G or physical acquisition of it is asserted.

D. The seven-slot program and prepared family in section 3 have the exact
endpoint, archive and finite-window properties stated there, including
arbitrary old memory and all zero inputs. Every complete state returns after
14 ticks, not merely every prepared state.

An exact admitted counterexample to A-D fires the corresponding claim.
No threshold is adjustable. Exceptions outside the frozen domain are not
repairs. A program error, arithmetic error, nonzero exit, nonempty stderr,
changed pinned input or byte/hash disagreement is recorded as an integrity
failure; it cannot be called scientific PASS. A fired mathematical claim is
retained. Universal statements rest on written proofs, not finite coverage.

## 3. One continuing receiver, full occupied continuation

Slots, in fixed order, are (S1,S2,L1,L2,R,A0,A1), indices (0,1,2,3,4,5,6).
Clock c belongs to Z/14Z. F(c,z)=(c+1 mod14,g_c(z)), with:

| c before step | g_c |
| --- | --- |
| 0 | swap R,A0 |
| 1 | swap R,L1 |
| 2 | C_S1,R |
| 3 | swap R,A1 |
| 4 | swap R,L2 |
| 5 | C_S2,R |
| 6 | identity |
| 7 | identity |
| 8 | C_S2,R^-1 |
| 9 | swap R,L2 |
| 10 | swap R,A1 |
| 11 | C_S1,R^-1 |
| 12 | swap R,L1 |
| 13 | swap R,A0 |

The full state domain is Z/14Z times O^7, not just initialized states.
The graph is the supplied seven-vertex star with centre R. Every data gate
touches one edge; the cursor/program is supplied and is not a derived local
clock, homogeneous lattice or physical three-dimensional geometry.

Initially c=0 and z=(2u1,2u2,2v1,2v2,m,0,0), with arbitrary independent
u1,u2,v1,v2,m in O. Both source/reference pairs are included at the common
origin; there is no later external loading or reset. The archives are
supplied blanks, while the receiver initially contains arbitrary m.
Define, for k=1,2,

    a_k=(1+rho)u_k+(1-rho)v_k,
    b_k=(1-rho)u_k+(1+rho)v_k.

At ticks 6,7,8 the actual state is exactly

    (a1,a2,0,0,b2,m,b1).

The first output is in R at tick3 and in A1 from tick4 through tick8.
Old receiver content m is unchanged in A0 throughout this stated window.
All original information is retained in the complete state, not copied or
erased. E=4*[q(u1)+q(u2)+q(v1)+q(v2)]+q(m) is conserved.

The record-only final reader takes (c,G), returns VALID with the principal
3x3 submatrix on ordered slots (A0,A1,R) if c in {6,7,8}, and NOT_IN_WINDOW
otherwise. A zero submatrix is still VALID in that window. This reader does
not return absolute scalar phases from G. Raw m really is preserved in A0;
G reads the retained norms and mutual relative records. There is no claim
of actual physical outcome selection or permanent storage.

The second half is the exact reverse of the first half after two hold steps,
so F^14=I on all complete states, including dirty archives and every clock.
Outside the prepared family the full law and Gram factor still hold, but the
displayed initialized endpoint and blank interpretation are not asserted.

## 4. Negative controls and phase witnesses

All controls are exact and must be retained even if a positive claim fails.

1. Binary-trace loss: d=1 has q(d)=2 even, but d is not in 2O; C(1,0)
   is rejected. Trace parity cannot replace the full norm admission test.
2. Normalization loss: (1,0) and (2,0) have equal normalized Gram matrices,
   but receiver q after contact is respectively 0 and 5. No normalized
   scale-free factor for this same contact follows.
3. Phase sensitivity: (2,2rho) and (2,2rho^-1) have identical diagonal
   input Gram entries (4,4); their receiver accounts are respectively 3
   and 13. Their source accounts are 13 and 3; total E=16 is unchanged.
4. Outside-map control: Phi(x,y)=(y,bar(x)) sends (1,1) and (j,j), whose
   Grams agree, to Grams with off-diagonal entries 1 and j^2. This known
   non-descent is not an allowed contact and prevents a universal gate claim.
5. Reference-extension loss: single-slot 2 and 2rho have identical Gram 4.
   Appending the same new reference 2 and then contacting gives receiver q
   respectively 8 and 13. A fresh absolute-phase reference cannot silently
   be appended as an operation of the old Gram state.

These are scoped obstructions, not global impossibility theorems about
binary readers, all normalized theories, all apparatuses or native physics.

## 5. Frozen finite audit inventory

Use only Python standard-library exact integer/rational operations. No
floating point, numerical tolerance, random sampling or learned data.

F1. All 16 coefficient vectors in {0,1}^4 modulo2: conjugation is Frobenius4,
norm is a^5, only zero has zero norm, all norms are conjugation-fixed, and
q modulo2, equivalently Tr_F4/F2(N_F16/F4(a)), has five nonzero zeros.
This is not the unreduced raw Tr_K/Q(a*bar(a)), which equals 2q.
Check J inverse and rho order.

F2. All 6561 ordered pairs x,y in B={-1,0,1}^4, lexicographic coefficient
order: raw admission equals Gram admission; forward/inverse, fifth power,
sum, full Hermitian h, E and exact Gram continuation. Every admitted matrix
division must have remainder zero. The universal claim is proved separately.

F3. All five controls of section4, including their specified exact values.

F4. Gram fibres beyond root-of-unity multiples. Let a=2+j, abar=2+j^-1.
Use w in the ordered three-element list

    (1,2,3,j,1+j,0,rho),
    (0,1,2,0,j,1-j,rho^-1),
    (1,1,1,1,1,1,1).

For z=a*w and z'=abar*w, for every initial clock 0..13, compare their
actual Gram records through boundaries n=0..14. Their Grams must agree
at every boundary. This is 630 paired boundary comparisons. Do not assume
abar/a is integral; a does not divide abar, as j=-2 modulo11 witnesses.

F5. All 1280 prepared inputs, nested in this exact order:
u1,u2 in U=(0,1,-1,j), then v1,v2 in V=(0,1,rho,rho^-1), then
m in M=(0,1,j,1+j,2-j). Check boundaries n=0..14, the complete endpoint
at6,7,8, first record at3 and4..8, old memory, full E/S/h conservation,
record-only final reading and all-step Gram recurrence. Every full state
returns at14. Count zero VALID records explicitly, without changing status.

F6. Occupied continuation: all lexicographic bit words of length7 over the
two ordered alphabets (1,1+2j), then (1,2rho). All 256 inputs have every
slot nonzero. Run from clock0 through n=14 and test full-state return,
invariants, Gram recurrence and reader status. Do not assert the ready
endpoint formula for this dirty family.

F7. Starting at each clock0..13, use z_k=1+2j^k, k=0..6. Check all fourteen
complete cycles and both full-state and record inverses.

## 6. Comparable certificates and provenance

The builder writes verify.py. The breaker writes break.py from this file
alone and may not read verify.py or its outputs before freezing break.py.
Both are committed/read back before either scientific run. Each source has
its own stdout; equal stdout between implementations is not required.

Both produce these two SHA-256 certificates, incrementally over UTF-8:

- Pair certificate: for each F2 pair in the specified order, one comma-separated
  line of 18 decimal integers: x[0..3],y[0..3],C(x,y).x[0..3],C(x,y).y[0..3],
  admitted-as-0-or-1,E(x,y), followed by a single newline.
- Program certificate: all F5 cases followed by F6 cases; within each case
  boundaries n=0..14. A line begins P| or O|, followed by comma-separated
  integers case_index,n,c,z_0[0..3],...,z_6[0..3],E(z), then newline.
  case_index restarts at0 for F5 and F6. F6 alphabet blocks are concatenated.

The certificates must agree between independently structured implementations.
Environment and byte-identical replays of each unchanged source are separate
evidence. A local x86_64 audit alone is not a two-architecture public gate.
The notes stay candidate-T analytically / candidate-C at finite tested scope;
external acceptance and any Canon promotion need separate work.

## 7. Dependencies, novelty and excluded physical conclusions

Contact source: #1833, d9d93f68c5cd15b7ab9cea4ba1ef3996352613d0.
Public J-BINARY-NORM-DESCENT supplies the residue fields; no new inertness
claim is made. JM-POSITIVE-REFERENCED-READING is a prior quadratic
congruence reader. QPAIR-HERM-INTEGER-NONDESCENT is the outside-map control.
OCCUPIED-RECORD-EXPORT-REUSE, INTEGER-HERMITIAN-OCCUPIED-SOURCE and
P-TWO-USE-TYPED-READOUT-CLOSURE-1 precede the archive construction. #1827
already supplies a different common finite source/clock/archive apparatus.

The new narrow result sought is exact admission plus full forward/backward
Gram factorization for the nonlinear #1833 contact, with a completely
specified two-use integer example. The graph, contact, prepared references,
blanks, clock and read window are additional premises. G is a global
quadratic record, not a demonstrated local instrument. There is no promotion
to original U/W, a quantum amplitude law, Born sampling, physical energy,
Lorentz proper time, spatial dimension, particle identity or L2-L6 measure.
