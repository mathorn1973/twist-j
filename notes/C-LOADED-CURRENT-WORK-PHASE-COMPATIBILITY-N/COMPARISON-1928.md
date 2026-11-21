# What the cyclotomic-return comparison does and does not transfer

**NON-CANONICAL. Analytical comparison only. Independent acceptance pending.**

This additive note compares the classical-arithmetic item
[C-CYCLOTOMIC-ZETA-TRANSFER-N, issue #1928](https://github.com/mathorn1973/twist-j/issues/1928)
with this note's declared L1 source-field apparatus. It neither takes over
that item nor identifies its arithmetic carrier with the physical reading
of the source-field model. This text is a supplementary hand derivation,
not part of the first frozen source-field audit and not a new scientific run.

## 1. The imported theorem and the exact scope of the separators

For b_n(m)=(m mod n)/n and H=l2(N,1/[m(m+1)]), Bagchi's Theorem 1 states
the equivalence between RH and approximation of the constant sequence 1
by finite linear combinations of b_n. Remark 4 gives squarefree sufficiency
in the Hardy-space representation; Remark 8 states it directly for these
sequences. The same paper explains that comparable positive weights of order
m^-2 preserve this closure criterion. Thus this equivalence does not single
out one physical measure or normalization.
Source: [Bagchi, Theorem 1 and Remarks 4, 8](https://arxiv.org/pdf/math/0607733).

The finite separators in #1928 can be checked directly. With f(0)=0 and n>=2,

    L_n(f)=sum_(d|n) mu(n/d)[f(d)-f(d-1)],
    L_n(b_k)=-delta_(n,k),       L_n(1)=mu(n).

Indeed the constant 1/k term cancels because sum_(d|n)mu(n/d)=0.
When k divides n, the remaining divisor sum is
sum_(e|n/k)mu((n/k)/e), which equals one exactly when n=k.
When k does not divide n the sum is empty. Each L_n is continuous because
it uses finitely many coordinates, all of positive H weight.

For n=6 the coalesced formula is 2f(1)-f(3)-f(5)+f(6).
Its squared dual norm is 4*2+12+30+42=92. Therefore omitting b_6 prevents
approximation of 1 to squared error below 1/92. This is a lower bound,
not an asserted exact minimum.

The consequent arbitrary-index-set classification concerns the target 1:

    1 in closed span{b_n:n in A}
    iff RH and A contains every squarefree integer n>=2.

It is NOT a completeness theorem for arbitrary histories using squarefree
indices. For every nonsquarefree m>=2, L_m annihilates all squarefree b_n
but satisfies L_m(b_m)=-1. Consequently the squarefree family is not total
in H, including under RH. This distinction is directly relevant to retaining
the complete state and record of our apparatus.

The [public result of #1928](https://github.com/mathorn1973/twist-j/issues/1928#issuecomment-6699973241)
labels these separator results as a post-audit analytical addendum.
No computation from that item is claimed to test the present apparatus.

## 2. Primitive phase, trace and complete cyclic reading are different

The rational regular representation of C_n decomposes into the primitive
cyclotomic representations for all divisors of n:

    Q[C_n] = direct_sum_(d|n) Q(zeta_d).

The sawtooth has Fourier expansion

    b_n(m)=(n-1)/(2n)
           -(1/n) sum_(a=1)^(n-1) zeta_n^(am)/(1-zeta_n^(-a)).

Every displayed nonconstant coefficient is nonzero. Hence the centered
sequence b_n-(n-1)/(2n) has minimal homogeneous linear recurrence polynomial
(t^n-1)/(t-1), of degree n-1. The uncentered b_n also has a nonzero constant
mode and has polynomial t^n-1, of degree n.

In particular centered b_6 uses U_2 direct_sum U_3 direct_sum U_6, of
dimensions 1+2+2. The two-dimensional primitive U_6 alone cannot produce
that sequence by a fixed linear observation. A constant offset does not
supply the missing order-two and order-three modes.

This is only a restriction on linear realization. A nonlinear reader of
the faithful phase zeta_n^r can recover r modulo n by a finite lookup.
There is no resulting lower bound on intrinsic physical dimension.
Likewise, for coprime a,b, primitive U_a tensor U_b supplies primitive
order-ab modes, whereas the product of the complete regular cyclic
representations supplies the complete order-ab representation.
Neither mathematical operation establishes a physical interaction.

For our five-state pointer p=j^r, write p=a0+a1*j+a2*j^2+a3*j^3.
The exact affine reading

    r/5 = 2/5 + (-2a0-a1+a3)/5,      r in {0,1,2,3,4},

returns the complete cyclic label. Its constant part plus four primitive
modes suffice because five is prime. The existing fixed-contact reader of
[#1925](https://github.com/mathorn1973/twist-j/issues/1925#issuecomment-6683808099)
also obtains r as the first changed helper, after which r/5 is a supplied
rational label. In contrast c_5(r) is four at r=0 and minus one otherwise;
a trace alone cannot distinguish j from j^-1.

## 3. Why the repeated-prime length 25 must not be discarded here

The fact mu(25)=0 means that L_25(1)=0 in the RH constant-target problem.
It does not mean that a 25-state phase register or a period-25 apparatus
can be removed from a different model.

Already the centered static source lift has a five-step base return and
a nontrivial fifth-root pointer advance. The complete ready apparatus
then has period 25. Its state and its readout are not the constant
target of section 1.

The proposed energy-form action extension makes the distinction more
explicit. Let R=Z[1/6], z=1/27, B=z M^-1 E, and D=M^-1 K. The localized carrier here takes A and B in R tensor O as primary coordinates. It is not every arbitrary rational E: on weight-15 edges z/c=4/5, so unrestricted E in R tensor O need not produce B in that carrier. The marked-edge collision and free map preserve the stated A,B carrier.
For the free step,

    B'=B-D A,       A'=A+B'.

Replace the scalar trace pairing in the complete conserved energy metric
by the marked alternating pairing Omega and call the resulting form Omega_G.
The selected action increment is Gamma=Omega_G(s,T s)/4.
On a transverse modal component of eigenvalue lambda and weighted squared
spatial norm one, direct expansion gives

    Gamma_free=lambda(4-lambda) Omega(A,B)/(16z).

This is an explicitly selected alternating reading, not an identification
with physical action. Its field terms include the inherited energy cross
term. The field law is specified in
[#1926](https://github.com/mathorn1973/twist-j/issues/1926#issuecomment-6696647447).

Here is a hand-checkable witness in that actual D3/3D3 carrier.
Identify its 27 vertices with F3^3 and let f(r)=2 when the coordinate sum
is zero modulo three and f(r)=-1 otherwise. Use only direction
v=(1,-1,0), of weight c=1/54, with A_v=f and B_v=f*j.
Shift by v preserves f, so these data are transverse.
The numbers of active opposite-direction pairs in squared-length shells
2,4,8,10,16 are respectively 3,3,3,12,3. With weights 6,1,15,1,1
divided by 324, their weighted sum is 81/324. Each active character
contributes a factor three, giving lambda=3/4.
There are nine entries f=2 and eighteen f=-1, so sum f^2=54 and
c sum f^2=1. Since Omega(1,j)=1,

    Gamma_free=1053/256,
    Gamma_free mod 5=3,       Gamma_free mod 25=13.

All denominators are units modulo 5 and 25. The modal matrix is

    T = [[1-lambda, 1], [-lambda, 1]].

Modulo five lambda=2, so T has trace zero, determinant one and T^2=-I.
Thus T^4=I modulo five. Preservation of Omega_G makes the increment
constant along this free orbit, but the four-increment sum is
4*3=2 modulo five. A function Phi of the reduced base state with
Gamma=Phi(Ts)-Phi(s) modulo five cannot exist: its sum around this
closed reduced orbit would have to vanish.

This excludes precisely the proposed base-state modular-potential method
for dividing Gamma into a fifth-root carry. It excludes neither all C5
phase laws nor extra state, a different action reading, or a different
physical model.

## 4. A declared 25-label register retains the missing residue

The alternative rule

    r' = r + (Gamma mod 25),       r in Z/25Z,

needs no nonexistent base-state potential. On five static collisions,
Gamma=B(d) at each collision, hence r advances by 5B(d).
The formal character zeta_25^r then changes by j^B(d), the old closed-cycle
monodromy. Arbitrary intermediate phases of the old and new lifts are not
identified. On a centered static orbit they are related, up to the initial
offset, by r=5*r_old+2*fhat(d) modulo 25.

No literal zeta_25 amplitude belongs to O=Z[j]. The register can instead
be encoded by two neutral prepared pairs

    (j^a,-j^a), (j^b,-j^b),      r=a+5b,   0<=a,b<5.

Each pair has account four, so the code has account eight. Ordinary
pointer contact powers implement each modulo-five digit shift; the carry
between the digits is an additional explicitly supplied state-controlled
rule. The complement of this 25-codeword subset may be fixed to give a
total occupied-pointer bijection. Its inverse subtracts the same increment.

Two copies of the fixed ten-reference reader use account forty and recover
both digits. Pointer plus references therefore cost 48 in this declared
quadratic account. This is the pointer/reader subsystem, not the energy of
the source and occupied field, a global minimum, or a physical apparatus
price. Reading is invasive and its complete inverse erases the new records.
The formal 25th-root character is a label on the register, not a new
cyclotomic amplitude, demonstrated quantum coherence, or physical charge.

## 5. The transferable result

The useful transfer from #1928 is a method: retain the full cyclic read,
construct a finite separating functional, and distinguish target-specific
completeness from reconstruction of a whole history. The field witness
above similarly separates a genuine closed reduced cycle from a proposed
state-potential explanation.

Neither Bagchi's theorem, the value mu(25), tensor composition, nor the
new register selects the physical action normalization, phase coupling,
source occurrence law, electromagnetic identification, or alpha.
The direct proofs and resource accounting must remain on their separately
declared carriers.
