# Contact law, finite record and entropy boundary

NON-CANONICAL. Proposed law: candidate-D. Mathematical statements below:
candidate-T, conditional on the explicitly stated carrier and reading.
Finite exact audits: candidate-C until their required gates are completed.
No Canon claim or open gate is closed by this document.

The inherited public inputs are `RELATIVE-CONTACT-INTEGRAL-LAW` and
`U-NATIVE-CHART-AND-QDD-READBACK` in the pinned `canon/REGISTRY.tsv`.
The latter's synchronized fired-letter table is explicit in
`probes/P-QDD-U-NATIVE-READBACK-1/PROOF.md`, section 1. The arguments below
rederive the contact identities used here. Existing
`U-FINITE-READER-INDEPENDENCE-OBSTRUCTION` and `TM-ENTROPY-ZERO` delimit
nearby source classes; the elementary counting bounds below are separately
proved for this probe's declared carrier and clock projection.

## 1. Primitive and proper account

Write O=Z[j] with 1+j+j^2+j^3+j^4=0 and rho=j^2. Since rho is a unit,
multiplication by rho preserves the submodule 2O. On the accepted branch
of C, the sum s=x+y is unchanged and the difference d=x-y becomes rho*d.
An even difference also makes s even. Both new coordinates are therefore
integral and the accepted branch remains accepted. On the rejected branch
C is the identity and the difference remains outside 2O. Consequently C is
a total bijection, C^5=identity and C^{-1}=C^4.

Complex conjugation sends rho to rho^{-1}. On the accepted branch,

    x*bar(x)+y*bar(y) = (s*bar(s)+d*bar(d))/2

is unchanged by d->rho*d. The rejected branch is unchanged literally.
The sum and the full Hermitian account are conserved before taking traces.

For c=c0+c1*j+c2*j^2+c3*j^3, the traces Tr(1)=4 and Tr(j^r)=-1 for
5 not dividing r give

    q(c)=Tr(c*bar(c))/2
        =(5*sum(ci^2)-(sum(ci))^2)/2.

The numerator is even, since squares equal their arguments modulo two.
The four-term square inequality gives

    2*q(c) >= sum(ci^2).

Thus q is a nonnegative integer, q(c)=0 exactly for c=0, and every set
A_E={c:q(c)<=E} is finite. A finite ring at fixed E has finitely many cell
arrays. This is a proper integer account; an uncharged hidden register would
change the carrier and invalidate this conclusion.

For an accepted contact, write d=2u. Then x'-x=(rho-1)u and
y'-y=-(rho-1)u. Since rho-1 is divisible by 1-j, each labelled cell keeps
its own residue in O/(1-j)=F_5. The same is immediate on rejection.

## 2. One autonomous forward law

Each matching consists of disjoint nearest-neighbor pairs, so its product
K_b is a bijection, K_b^5=identity, and K_b^{-1}=K_b^4. It preserves every
quantity in section 1. The parity guard is applied by C itself; no outcome
is consulted to choose a subsequent matching.

Let t(n) be popcount(n) modulo two. For n>=1, writing n=2^v*m with m odd
shows that increasing n-1 to n replaces v trailing ones by zeros and the
preceding zero by one. Hence

    t(n) XOR t(n-1) = (1-v) mod 2.

It equals one precisely for even v=nu_2(n). On the canonical synchronized
native chart the fired letter is b precisely for unequal adjacent bits.
The law therefore uses that existing clock projection b_n, not a new stored
finite program. The association of this bit with the two matchings is a
new declared choice. It is not derived by an intertwining with all native
coordinates.

The map F_N(n,z)=(n+1,K_{b_n}z), n>=3, is autonomous on its declared full
carrier. Its image is exactly the slices n>=4. On that image,

    F_N^{-1}(n,z)=(n-1,K_{b_{n-1}}^4(z)).

This proves an exact predecessor, not surjectivity onto the initial slice.
The unbounded counter is retained and is never called a finite-state clock.

## 3. The nine-state invariant class

Fix even N>=8, a nonzero odd integer a and the source pair at 1,5. Even
translations give the translated families in CONTRACT.md. In state B the
only nonzero cells are 2a,-2a. Contact through M0 or M1 therefore produces
L_1 or R_1 respectively, with the stated A_1,D_1 coordinates.

On an active pair, A_k+D_k=2a and A_k-D_k=2*rho^k*a. Its next contact
replaces rho^k by rho^{k+1}. The fifth active contact returns the base pair:
(2a,0) on the right-oriented pair and (0,2a) on the left-oriented pair.
The second source pair follows with the opposite sign.

It remains to prove the inactive matching refuses on every boundary of an
occupied pair. Modulo 2O, the four nonzero values 1+rho^k, k=1..4, have
canonical coefficient vectors

    k=1: (1,0,1,0)
    k=2: (0,1,1,1)
    k=3: (1,1,0,0)
    k=4: (1,0,0,1).

These are also the vectors of 1-rho^k modulo two. Multiplication by an odd
integer a leaves them unchanged. Thus every occupied A_k or D_k is outside
2O. In the other matching each such cell is paired with zero, so all four
boundary contacts refuse. The remaining zero pairs stay zero. N>=8 keeps
the two source neighborhoods disjoint, including across the ring boundary.

This proves the complete two-generator transition table in CONTRACT.md.
The nine states are distinct: their nonzero receiver side distinguishes L
from R and B, while distinct powers of rho distinguish k. All are reachable
by some matching word from B, and none outside this class is reachable by
any matching word. A specified fixed drive may visit only a subset; the
actual native drive visits both sides.

The complete accounts follow either from conservation or from B:

    S=0, h=8*a^2, E=16*a^2.

For a=+1 and a=-1 these are identical. All six initial non-source cells are
literally zero for both signs. This is stronger than requiring an initial
trace of zero; no information is hidden in a receiver's trace kernel.

The oddness condition is essential to this proof. For a=2, after M1 then
M0 the previously blank cell 3 equals (1-rho)^2, which is nonzero. Every
nine-state formula has cell 3 zero, so this even preparation leaves that
class. The probe checks this as an intended negative control.

## 4. A fixed readable record and its erasure

For k=1..4, Tr(rho^k)=-1. Therefore

    Tr(D_k)/5 = a.

Each D_k is nonzero. The fixed total tagged reader returns VALUE(a) at the
positive receiver and VALUE(-a) at the negative receiver, independently of
k, without looking at the clock or the original source. Its rational value
is integral on this admitted class. The left and right receivers together
give one fixed reading of a in every nonbase state. In state B they are
literally blank. The residue of each receiver modulo 1-j remains zero:
the record lies in the integral cell, not in that single F_5 residue.

Starting at n=3, the clock bits for ticks 3..9 are (1,1,1,0,1,0,1).
The boundary states at n=3..10 are therefore

    B, R1, R2, R3, R3, R4, R4, B.

The right reader has VALUE(a) at every n=4..9, including both intervening
opposite-matching attempts. Its raw cell value changes, but the fixed
decoded record does not. Tick 9 erases it; no external reset occurs. The
cell array has returned at n=10 while the counter has advanced. This is a
finite readable record followed by erasure, not a permanent archive or an
independent new trial. One initially supplied a is read again later.

## 5. Finite propagation and the marked geometry

The same disjoint matchings define maps on O^Z. Each coordinate uses only
itself and one nearest neighbor in each tick. By induction, its value after
T ticks depends only on the initial radius-T neighborhood and the shared
T-bit clock word.

The periodic extension of an even ring evolves exactly as its line
extension, because reducing indices modulo an even N preserves matching
parity. If a line array and this periodic extension agree initially on an
interval containing W+[-T,T], their complete observations in the fixed
window W agree for T ticks. The two runs must have the same initial counter.
Changing the global clock is outside this array-dependency statement.

Translation by two sites commutes with each matching update. Translation
by one site exchanges M0 and M1 and is not a symmetry at a fixed bit. The
declared graph and staggering are real ingredients, not emergent geometry.
This is locality on the constructed graph; no physical dimension, speed,
Lorentz symmetry or spacetime identification follows.

## 6. Clock-word bound and a finite ring

Let B_b(ell) count all different length-ell blocks of b_n, n>=1. Choose
q to be the least power of two at least ell, so q<2*ell except at ell=1,
where q=1. In a block of ell consecutive positive integers there is at
most one multiple of q. The starting residue modulo q fixes nu_2 at every
other position. The exceptional position, if present, supplies at most one
extra bit. Consequently

    B_b(ell) <= 2*q <= 4*ell.

Fix N and E, and let M be the finite number of ring arrays of account E.
For any fixed finite-valued readout of the current array and b_n, producing
one symbol every tick, its length-ell output word is determined by an
initial array and an ell-bit clock block. Hence

    B_out(ell) <= 4*M*ell.

For every probability law supported on these output words, block Shannon
entropy in bits obeys H_ell<=log2(4*M*ell). Thus H_ell/ell tends to zero.
The topological word growth rate also vanishes. This excludes a
nondegenerate independent output process in every order on this fixed
carrier; a successful low-order finite test could not change the bound.

The reader may not inspect an arbitrary function of the full integer n.
No-event ticks remain symbols. Event-only resampling with unbounded gaps
requires a separate argument. A fixed extra finite reader state only
multiplies M, whereas growing feedback memory changes the carrier.

## 7. An infinite line with finite total account

Now fix a finite integer E and admit all arrays on Z with total
sum_i q(z_i)=E. Since every nonzero cell has positive integer account,
there are at most E nonzero cells in the entire array. Each belongs to the
finite alphabet A_E={c:q(c)<=E}. A fixed width-w observation for ell ticks
depends on an initial interval of at most w+2*ell cells. The number of such
initial restrictions is at most

    sum_{k=0}^E binomial(w+2*ell,k)*(|A_E|-1)^k,

with the usual zero convention when k exceeds the interval length. Adding
the clock-word choices gives

    B_out(ell) <= 4*ell *
        sum_{k=0}^E binomial(w+2*ell,k)*(|A_E|-1)^k
        = O(ell^(E+1)).

Therefore the same per-tick entropy rate is zero on the infinite line in
this fixed finite-total-account class. Unlimited empty room supplies no
positive rate of new local information under these assumptions. The proof
uses the unique zero-account state and the fixed finite observation window.
Free uncharged registers, infinite total account, an information-bearing
infinite background and arbitrary sparse sampling are outside its scope.

This does not prove that every infinite-plenum model has zero entropy.
It identifies additional information-bearing resources that any such
proposal must declare, and leaves their distribution and Born reading open.
