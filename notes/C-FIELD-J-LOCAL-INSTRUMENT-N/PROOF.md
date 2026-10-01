# Conditional local instruments and finite retained histories

**PUBLIC, NON-CANONICAL. Author-side proof of the frozen L1 specification;
no earned status, independent-review result or scientific execution is
asserted here.** This is disclosed coauthorship by algebra_builder and its
transport_timing_check subagent, not the fresh independent review.

Specification: `PREREG.md` at immutable public commit
`0ca0605bee475ed3ab86f9a7c1129ea00a09d86d`, SHA-256
`66f6df4102a5c88295926ea1c1afb8cbac56848d3ab19be7b84fea9e26ac8c2c`.
The accepted classical input is C-FIELD-J-CONTENT-TRANSPORT-N at
`05e2f457e9f7d69f6f6649e9ec4094f4ebb08eaa`. Public Canon remains v96;
the coordinator owns authority, reservation, publication and execution
checks. Original work under Apache-2.0, prepared 2 October 2026.

## 1. Carrier, elementary arithmetic and full energy

Throughout, N is an integer at least two, T=2N-1, M=1226 and L=613.
Reserves are nonnegative integers. A packet is the literal ordered tuple
(b,y,r), where b is zero or one and y is in Z^4. There are 2N-1 packet
slots, the receiver latch l, and its pointer p in Z/M. Inactive packets
retain their y and r. With K archive cells, each storing (p_i,z_i), the
complete stored state has 6(2N-1)+2+2K=12N-4+2K integer coordinates.
No controller state or source label is silently added to that list.

Define the field quadratic and the two integer charts by

```text
H(y)=2y0^2-2y0*y1+3y1^2+y2^2+y3^2
     +2y0*y2-y0*y3-y1*y2+3y1*y3,
C a=(a1,a2-a3,a0-a1-a3,a1-2a2+a3),
C^-1 y=(2y0-2y1+y2-y3,y0,y0-y1-y3,y0-2y1-y3).
```

Substitution gives the identity in both directions. For the quadratic H
in the specification, direct substitution gives

```text
H(Ca)=sum a_i^2-a0*a2-a0*a3-a1*a3,
2H(Ca)=a2^2+(a2-a0)^2+(a0-a3)^2+(a3-a1)^2+a1^2.
```

Consequently H is positive definite and its only zero is y=0. The doubled
Gram matrix, in the order (a2,a0,a3,a1), is the four-vertex path Cartan
matrix. Its inverse has diagonal (4,6,6,4)/5 in that order. Applying
metric Cauchy-Schwarz to the doubled Gram matrix gives, in the original
order,

```text
a0^2,a3^2 <= 12H/5,       a1^2,a2^2 <= 8H/5.
```

Thus K5={y:H(y)<=5} lies in the stated coefficient box. Its size 291 and
shell sizes (1,20,30,60,60,120) are the accepted finite arithmetic input;
the new universal arguments below do not depend on a new enumeration.

The code

```text
c(y)=1+(((a0+3)*5+(a1+2))*5+(a2+2))*7+(a3+3)
```

is one plus the mixed-radix index of that box, with radices (7,5,5,7).
Repeated Euclidean division recovers all four digits, so it is injective
on K5, with 1<=c<=1225. In particular its values are distinct modulo M.
At a=0 it is 613. Define the four selected field labels by their
coefficient tuples:

```text
f0: a=(-1,-1,-1,-1), c=395;
f1: a=( 1, 0, 0, 0), c=788;
f2: a=( 0, 1, 0, 0), c=648;
f3: a=( 0, 0, 1, 0), c=620.
```

Each has H(Ca)=1 by the displayed quadratic, and substitution gives the
listed code. Only the first is odd. The f_j denote the corresponding
orthonormal packet-basis labels; their span S4 has dimension four inside
the twenty-dimensional H=1 shell. Write P_L=|f0><f0| and
P_H=sum_(j=1..3)|fj><fj| on that subspace.

Every stored field, including an inactive field, contributes to

```text
E_total = sum_slots [b+H(y)+r]+2l+1+2K.
```

The active pointer contributes one, and each archive pointer and each
archive flag contributes one, independently of its value. At a fixed
finite bound on E_total, all reserves are bounded and positive
definiteness bounds every field coordinate. All remaining coordinates
have finite ranges. Hence the number of complete basis states below that
bound is finite. This conclusion would not follow from an energy that
omitted inactive stored fields; that is not the specified energy.

An external finite reference is explicitly tensored with identity and has
zero energy. It is not an apparatus actuator or a funding source. The
clean four-label geometry has energy 1+1+2+1+2K=5+2K: presence, field,
reserve, active pointer, and the archives, respectively.

## 2. Total classical inverse and its complex extension

Support is b=1 and y in K5. Receiver G first tests support. Unsupported
packets are fixed, whatever their reserve, latch or pointer. For supported
packets it fixes b,y and acts as follows, with pointer addition modulo M:

```text
(r,0,p), r>=2  -> (r-2,1,p+c(y));
(r,0,p), r<2   -> (r,0,p);
(r,1,p)        -> (r+2,0,p).
```

For a supported output with latch one there is exactly one preimage,
(r+2,0,p-c). For a supported output with latch zero and r>=2 the unique
preimage is (r-2,1,p). A supported output with latch zero and r<2 is its
own preimage. Unsupported outputs have unsupported preimages, because G
never changes b or y, and those preimages equal the outputs. These classes
are disjoint and exhaustive, their reserves are nonnegative, and direct
substitution verifies both inverse compositions. In particular G is not
an involution: release does not subtract c.

A is the product of the disjoint whole-packet swaps (C_j,Q_j); B is the
product of (Q_j,C_(j+1)). Each is a total involution, including occupied
slots. Therefore F=B A G has inverse G^-1 A B. Omitting the two contacts
at a fixed cut j leaves the same argument intact, with Q_j retained and
isolated. There is no state-dependent change of the cut.

A write decreases its own packet reserve by two and increases 2l by two;
a release does the reverse for the presently supported receiver packet.
Thus G preserves sum r+2l, the content/presence multiset and E_total.
The swaps preserve all three, including every inactive or occupied slot.
The inverse primitives preserve them as well. In a dirty state, a release
may fund a packet other than the one involved in an earlier write; the
conservation proof imposes no provenance restriction.

Let X_N be this complete countable classical carrier. On the dense span
of its orthonormal basis in ell^2(X_N), set U_F|s>=|F(s)>. A bijection
permutes this basis, preserves the norm of every finite linear combination,
and has the corresponding inverse basis permutation. It therefore extends
uniquely to a surjective unitary on ell^2(X_N). The same proof applies to
every primitive, inverse and fixed cut. On all complete matrix units,

```text
Ad(U_F)(|s><t|)=|F(s)><F(t)|.
```

This is the definition of the lift on dirty as well as clean states. It
is not inferred from a reduced source channel. Conjugation is continuous
on trace-class operators, so finite-rank approximation extends the identity
to arbitrary mixed states and coherences on the complete Hilbert space.
Tensoring a finite reference with identity changes none of the argument.

The diagonal energy operator has the same eigenvalue on |s> and |F(s)>.
Thus U_F commutes with every energy spectral projector and with the energy
operator on its domain. It preserves finite expectations and the extended
nonnegative energy expectation when that is infinite. On a finite energy
subspace it is a finite permutation matrix and has finite order.

For each h<=5 the shell {y:H(y)=h} is finite. An arbitrary unitary U_h
on that shell, applied for b=1 identically and separately at each r,
and extended by identity elsewhere, is an orthogonal direct sum of
unitaries. It is a total unitary, preserves r and energy, and may change
the content multiset. The latter is only an invariant of B dynamics.
These added controls can contain irrational phases; a finite-dimensional
unitary with an irrational relative eigenphase need not have a periodic
orbit. Finite order was asserted for the basis permutation, not for all
these controls.

Every pointer read projector and flag read projector is bounded and
commutes with the diagonal energy. The selective map X->Pi X Pi is
completely positive and trace nonincreasing on positive inputs; the sum
over a complete partition is trace preserving. It does not move support
between energy shells. Conditioning on a correlated outcome need not
preserve the normalized state's energy distribution. No funding is
thereby transferred to G. A conditional source control
sum_d Pi_d tensor U_d, completed by identity on unassigned orthogonal
blocks, is a total unitary by multiplying it by its adjoint blockwise.

## 3. Actual timing, funding and all-time clean transport

Initially place exactly (1,y,2), y in K5, in C0; place exact empty packets
elsewhere and take l=0. The initial pointer is arbitrary. Whole-packet
swaps give the positional cycle

```text
C0 -> C1 -> ... -> C(N-1) -> Q(N-2) -> ... -> Q0 -> C0,
```

of length T. Receiver G changes no position or field. The single present
packet is distinguished even when y=0, and every other receiver packet is
unsupported. At boundary N-1 the present packet first reaches C(N-1).
The G in the preceding step has already occurred; the first receiver
reaction is therefore the G of step N. It has reserve two and latch zero
and is precisely the funded WRITE branch.

The present packet returns to the receiver every T steps. Until its next
visit G sees unsupported emptiness. On that visit its reserve is zero
and l=1, so RELEASE restores reserve two and l=0 without translating p.
The following visit writes again. Induction on the visits proves

```text
WRITE steps   N+2mT,
RELEASE steps N+(2m+1)T,                m>=0.
```

This proves the entire future schedule, including the identity reactions
between visits. Define

```text
e(n)=0 for n<N; e(n)=1+floor((n-N)/T) for n>=N,
w(n)=0 for n<N; w(n)=1+floor((n-N)/(2T)) for n>=N.
```

They count completed reactions and completed writes, respectively. At boundary n the
packet is at position n modulo T in the displayed cycle, its reserve is
2(1-(e(n) mod 2)), and l=e(n) mod 2. All other reserves stay zero. With
S_c|p>=|p+c>, the complete clean evolution is therefore

```text
U_F^n(|y;0> tensor |p>)
  = |y;n> tensor S_(w(n)c(y))|p>.
```

This holds for all n>=0 and every pointer basis value, so also for any
coherent or mixed pointer. The notation |y;n> includes all packet,
reserve and latch coordinates except the pointer; it is not a discarded
environment.

Since N<=T, the interval of 2T actual B steps has exactly one WRITE, at N,
and one RELEASE, at N+T. At 2T the present packet is back at C0, its reserve
is two and the latch is zero. The pointer has acquired S_c exactly once.
Latch one lasts exactly boundaries N through N+T-1. This is an operative
geometry return, not restoration of an arbitrary initial source state or
pointer. Later writes accumulate S_(w c); they do not silently recreate
the first ready apparatus.

The WRITE predicate is just the local input condition
b=1, y in K5, l=0, r>=2 before G. It refers neither to parity nor to the
target projectors. On the promised clean sector it holds at step N on
every source component. Complex superposition introduces no new branch
of the classical circuit: the lifted unitary acts on those same basis
transitions. This deterministic completion statement supplies no rule
that selects one parity-read outcome.

The negative controls follow from the same local rule. With clean absence
there is no supported packet. With a lone unsupported packet, including
a=(4,0,0,0) for which H=16, there is none either. With supported reserve
zero or one and l=0, no write ever occurs, hence no release creates a
reserve. If reserve two is instead carried by a separate inactive packet,
whole-packet swaps never attach it to the underfunded supported packet;
the inactive packet cannot operate G. Equal total energy is insufficient.
A cut separates C0,...,C_j from C_(j+1),...,C(N-1), with Q_j isolated,
so a clean source on the left never operates the receiver on the right.
These are raw dynamics, not positive trials. Conversely a funded supported
packet preloaded at the receiver writes at step one. Dirty states therefore
invalidate an unconditional source-provenance interpretation of l or p.

Literal present y=0 has code 613 and performs the ordinary supported write.
It is distinct from an absent packet, and both are distinct from the zero
Hilbert vector. A zero vector has no normalized density or trial weight.
The typed ZERO_SUPPORT response, RAW_EVOLUTION, UNSUPPORTED_PROTOCOL,
OUTSIDE_TRIAL_DOMAIN and RESOURCE_EXHAUSTED are the external descriptor
interface specified in PREREG.md. Rejection retains the complete supplied
state. This dispatch is not a quantum test of an unknown apparatus, a
projection onto readiness, or postselection that creates a successful
trial from an off-domain input.

## 4. Joint matrix-unit law and complete pointer classification

Expand an arbitrary clean-geometry source/pointer/reference input as

```text
Omega = sum_ab |a;0><b;0| tensor X_ab,
```

where a,b range over all K5 labels and X_ab are pointer/reference
operators. Applying the preceding basis identity to ket and bra gives

```text
sum_ab |a;n><b;n| tensor
  (S_(w c(a)) tensor I_R) X_ab (S_(w c(b))^* tensor I_R).
```

This proves the retained joint formula for every ordered source pair,
including correlations; no product assumption has entered. Reading bin
o applies Pi_o to both sides of the pointer block. Discarding only the
pointer then gives exactly the partial-trace expression in section 5
of the specification. In particular this is not a channel determined
only by the reduced source density when X_ab initially contains apparatus
correlations.

An entirely explicit form is useful. On the pointer matrix unit
|p><q|, the ket and bra positions become p+w c(a), q+w c(b), respectively.
The selective retained block is that matrix unit if both positions lie
in D_o and zero otherwise. Its pointer partial trace is

```text
1_(p+w c(a) = q+w c(b) mod M) 1_(p+w c(a) in D_o).
```

Every pointer operator, including an irrational complex density, is a
linear combination of these units. Reference blocks simply multiply this
scalar formula. It proves the full retained and reduced maps, not just
their diagonal outcome effects.

For a product pointer density sigma at w=1, write the source/reference
input as sum_ab |a><b| tensor rho_ab. The reduced output block is
gamma_o(a,b) rho_ab, with

```text
gamma_o(a,b)
 = Tr[Pi_o S_c(a) sigma S_c(b)^*]
 = sum_p sigma_(p,p+c(a)-c(b)) 1_(p+c(a) in D_o).
```

One Pi can be removed from the two-sided expression by cyclicity of trace
and Pi^2=Pi. Complete positivity and trace preservation of the branch sum
also follow directly from the unitary, read and partial-trace construction.

If all ordered gamma coefficients agree for two apparatus preparations
and read keys, after the fixed declared outcome bijection, their maps
agree on every |a><b|, hence every source operator and finite reference.
Conversely equality of these maps forces equality on every matrix unit
and thus of the coefficients. Equality on all densities suffices: diagonal
matrix units are densities, and the usual sums and differences of the
rank-one densities of |a>+|b> and |a>+i|b> recover off-diagonal units by
complex linearity. This proves the stated necessary and sufficient
classification for all sigma and partitions. For a diagonal source-bin
projector P_o, P_o|a><b|P_o is the unit itself precisely when a and b both
belong to bin o and is zero otherwise. The target coefficient condition
is therefore equivalent to the complete Lueder instrument, not only to
its effects.

There are 291^2 such source units in the full supported sector and 16
in S4. An arbitrary finite reference introduces reference matrix units
as extra tensor factors; the maps act identically on them. Thus matrix-unit
equality proves all finite-reference and entangled-input claims without
sampling states.

## 5. Coherent parity, negative preparations and explicit Fourier control

Let

```text
|0_phase>=E=(1/sqrt(L)) sum_(j=0..L-1)|2j>,
|1_phase>=O=(1/sqrt(L)) sum_(j=0..L-1)|2j+1>.
```

Each support has L positions and their
supports are disjoint, so these are orthonormal. Translation by c bijects
one parity class to parity xor (c mod 2), with no phases. Consequently

```text
S_c |r_phase> = |(r xor beta(c))_phase>, beta(c)=c mod 2.
```

For every source pair and phase matrix unit the retained map is

```text
|a><b| tensor |r_phase><s_phase|
 -> |a><b| tensor
    |(r xor beta(c(a)))_phase><(s xor beta(c(b)))_phase|.
```

This proves invariance of the two-dimensional phase subspace, including
coherences and correlations. With an arbitrary phase density tau and
pointer parity outcome o in {0,1}, the reduced coefficient is
tau_(o xor beta(c(a)), o xor beta(c(b))). No classical random phase is
substituted for a coherent input. For example the pure (E+O)/sqrt(2)
is fixed by all translations: each parity-read branch is one half of
the identity source channel, not a sharp source parity instrument.
The pure (E+iO)/sqrt(2) has imaginary off-diagonal phase entries, which
the same formula retains; it is not a classical E/O mixture.

For pure E the translated phase is exactly the source code parity.
The gamma coefficient is one when both labels have the observed parity
and zero otherwise. Thus the entire K5 reduced instrument is precisely
P_even X P_even and P_odd X P_odd. For pure O the two reader names must
be interchanged. This establishes the known-odd variant but does not
identify E and O as the same apparatus: they are orthogonal retained
vectors, and their future interfaces must be specified separately.

For the blank sigma=|0><0|, the general coefficient formula becomes

```text
gamma_o(a,b)=1_(c(a)=c(b) mod M) 1_(c(a) in D_o).
```

Code injectivity makes every distinct-label coefficient zero. For the
diagonal-even density L^-1 sum_even |p><p|, diagonality likewise forces
c(a)=c(b) in any nonzero coefficient. With parity reading, the diagonal
effects in both cases coincide with code parity, but every distinct-label
coherence is destroyed even inside one parity bin. Diagonal-even and
coherent E have exactly the same position probabilities and different
instruments. Their distinction is off-diagonal density data.

In particular the entangled source/reference vector
(f1 tensor |0>+f2 tensor |1>)/sqrt(2) lies wholly in HIGH. Coherent E
retains its full rank-one density, including both cross terms. The blank
and diagonal-even preparations leave only its two diagonal terms after
the pointer is discarded. The full joint state before that discard is
still the output of a unitary; this is loss of a reduced coherence, not
destruction of the globally retained state.

The optional F_par consists of one length-L discrete Fourier matrix in
each parity block. Let omega=exp(2 pi i/L) and define
F_par|2j+b>=(1/sqrt(L))sum_k omega^(jk)|2k+b>, for j,k in Z/L and
b in {0,1}. For j,j' in Z/L,

```text
(1/L) sum_k omega^((j-j')k) = 1 if j=j', and 0 otherwise.
```

For unequal indices the geometric sum is zero because its ratio is a
nontrivial Lth root of unity; for equal indices it has L unit terms.
This proves orthonormal columns and therefore F_par^*F_par=I, with inverse
the adjoint. Its j=0 columns give F_par|0>=E and F_par|1>=O. Flat pointer
energy makes it energy preserving. Its other columns are different
orthonormal Fourier vectors, so it cannot reset an arbitrary dirty pointer
to E. A basis permutation preserves diagonality of a diagonal density,
and a classical mixture of such outputs remains diagonal. B permutations
cannot produce E from a diagonal initial density; adding F_par and a
ready blank is an additional preparation premise.

## 6. Exact fixed-reader uniqueness among all pointer densities

Restrict to S4 and fix LOW=odd, HIGH=even, with no compensator. Let sigma
be any positive trace-one pointer density for which the target reduced
Lueder branches hold. In particular the HIGH probability for f1 equals
one. Since its code 788 is even, this implies

```text
Tr(Pi_even sigma)=1,       Tr(Pi_odd sigma)=0.
```

For a positive density, zero trace against an orthogonal projector implies
support in its complement: Tr(Pi_odd sigma) is the squared Hilbert-Schmidt
norm of Pi_odd sigma^(1/2). Hence sigma=Pi_even sigma Pi_even, including
the vanishing of its even/odd cross blocks.

The retained coefficient of |f2><f3| in HIGH must also be one. Both codes
are even, so the parity projector is redundant on the supported density.
Using c(f2)-c(f3)=648-620=28 gives

```text
gamma_HIGH(f2,f3)=Tr(sigma S_28)=1.
```

For any unitary W and positive trace-one sigma,

```text
||(W-I) sigma^(1/2)||_HS^2 = 2-2 Re Tr(sigma W).
```

Thus Tr(sigma W)=1 forces (W-I)sigma^(1/2)=0. Equivalently the support
of sigma lies in Fix(W); this is a positivity argument for every density,
not a numerical test of selected preparations.

Here the Euclidean algorithm gives gcd(28,1226)=2. Translation by 28
therefore has exactly two cycles on Z/1226, the even and odd classes,
each of length 613. A fixed vector must have constant coefficients around
each cycle, so Fix(S_28)=span{E,O}. Intersecting with the already proved
even support leaves span{E}. A positive trace-one density supported on
that one-dimensional space is exactly |E><E|. Section 5 proves this
density is sufficient, completing the if and only if.

With a fixed parity relabeling for the known odd ready phase, the same
argument first forces odd support, and then the same fixed-space argument
gives the unique |O><O|. This uniqueness concerns only the declared
independent pointer densities, fixed reader and absent compensator on S4.
It neither chooses a physical preparation mechanism nor eliminates other
members of the broader control/read family.

## 7. G-isometric encoding and all context operator identities

In the comparison space S=C^4 let 1 denote the all-ones column and
G=I-11^*/5. On span{1}, G has eigenvalue 1/5; on its Euclidean orthogonal
complement it has eigenvalue one. It is positive definite, with
G^-1=I+11^*. Set

```text
u0=(sqrt(5)/2)(1,1,1,1),
q1=(1,-1,0,0)/sqrt(2),
q2=(1,1,-2,0)/sqrt(6),
q3=(1,1,1,-3)/sqrt(12).
```

The vector u0 has G-norm one. The three q_j have coordinate sum zero and
are Euclidean orthonormal, so their
G-inner products are also those of an orthonormal triple. They are
G-orthogonal to u0. Thus (u0,q1,q2,q3) is a G-orthonormal basis.

Define V by taking these four basis vectors to (f0,f1,f2,f3).
In those physical coordinates its first row is 1^*/(2 sqrt(5)), and its
remaining rows are q1^*,q2^*,q3^*. Directly,

```text
V^*V = (1/20)11^*+(I-11^*/4)=G,
V^sharp=G^-1 V^*,       V^sharp V=I,       V V^sharp=I_(S4).
```

For an operator A on S write A^sharp=G^-1 A^*G. Conjugation
A->V A V^sharp preserves products, trace and the appropriate adjoints.
It takes G-positive densities of trace one to ordinary positive densities
of trace one. For example a G-normalized pure vector a is represented
by a a^*G, which becomes (Va)(Va)^*. No integer field chart is involved:
the coherent vector Va is generally different from the single packet
basis vector |Ca>. A zero coherent vector is not a stored zero packet.

The rank-one G-orthogonal projector onto u0 is

```text
u0 u0^* G = 11^*/4 = P0.
```

Consequently V P0 V^sharp=P_L and V(I-P0)V^sharp=P_H.

The registered context matrix is

```text
R=[[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]].
```

For completeness its identities have a geometric algebraic proof.
In the four-dimensional zero-sum subspace of C^5 set
v_i=e_i-(1/5)1_5, i=0,...,4. The first four have Gram matrix G and
v4=-(v0+v1+v2+v3). The cyclic permutation v_i->v_(i+1 mod 5) has, in
that four-vector basis, exactly the displayed matrix R: its first three
columns shift the basis, and its last column is minus all ones.
The five-cycle preserves inner products and its fifth power is identity.
Hence R^*GR=G and R^5=I. It follows that R^-1=R^sharp, and
P_k=R^kP0R^-k and Q_k=I-P_k are complementary G-orthogonal projectors.

The physical precontrol U_k=V R^-k V^sharp is unitary on S4. Extend it
by identity on the remaining H=1 labels and other sectors, using the same
source action at each reserve as prescribed. Its adjoint on S4 is
V R^k V^sharp. Therefore

```text
U_k^* P_L U_k = V P_k V^sharp,
U_k^* P_H U_k = V Q_k V^sharp.
```

For an arbitrary physical source operator X, a clean E-ready B interaction
followed by parity read has branches P_o X P_o. Precontrol U and
postcontrol U^* consequently give

```text
X -> (U^*P_oU) X (U^*P_oU).
```

Substitute X=V rho V^sharp and U=U_k to obtain precisely
V(P_k rho P_k)V^sharp and V(Q_k rho Q_k)V^sharp. This algebra holds
for every operator, so it proves all sixteen source matrix-unit identities
and their finite-reference amplifications. It is stronger than equality
of traces. Known O readiness, with the fixed reader relabeling, gives
the same reduced identities by section 5. General U in U(4) gives the
two conjugated projectors above.

All these selected controls stay within one field-energy shell. They are
additional coherent controls; R is a comparison-space transformation,
not a native B time step. Trace identities such as
tr(P_k rho P_k)=tr(rho P_k) follow from cyclicity and idempotence, but do
not add an outcome-occurrence or empirical probability postulate.

## 8. Archive round, total inverse and its exact operational domain

On the active pointer, archive pointer i and its flag, the append gate is

```text
A_i: |p>|q>|z> -> |q>|p>|z xor 1>.
```

SWAP and flag X act on different tensor factors and commute. Applying
this formula twice is the identity on every basis state, hence on every
operator, coherence and dirty correlation. Thus A_i=A_i^-1 is a total
unitary permutation. Each of the three affected coordinates has constant
unit energy, so it preserves E_total.

For declared source unitaries D and U, the full chronological round is
D, U, 2T actual B steps, U^*, A_i. Its unitary is

```text
R_i = A_i U^* U_F^(2T) U D,
R_i^-1 = D^* U^* U_F^(-2T) U A_i.
```

The second equation is the reversed product of genuine all-state inverses.
It requires no clean preparation or event log. The controls and append
are external operations at the stated boundaries; no B-step duration for
them is asserted.

For the positive protocol, active E and the fresh cell (E_i,0) are supplied
independently of the source and reference. A pure reduced ready state
cannot conceal correlations with another system: positivity forces the
joint state into its one-dimensional support, so it factors. This is an
explicit initial preparation premise, not an autonomous preparation test.

Let P_o mean P_L or P_H and define Q_o=U^*P_oU. The one-round vector law
on the source, including an arbitrary reference, is

```text
|psi> -> sum_(o=L,H) (Q_o D tensor I_R)|psi> tensor |o_i>
         tensor |E_active> tensor |ready geometry>,
```

where H_i=E_i tensor |1> and L_i=O_i tensor |1>. Other archive cells
are retained unchanged. To prove it, apply U D to the source; section 3
gives one controlled translation and the restored packet/latch geometry;
section 5 turns that translation into the E/O parity writer; U^* gives
Q_oD; and the literal SWAP moves the complete active phase, including
entanglement, to the fresh cell while replacing active with E.

On an arbitrary source/reference operator X the unreduced record output
contains every pair of terms

```text
sum_(o,o') (Q_oD tensor I_R) X (D^*Q_o' tensor I_R)
            tensor |o_i><o_i'|.
```

A parity read selects the matching diagonal term. In particular the
source generally changes and may remain entangled with old records.
Position, reserve, latch and active E, rather than the source density,
are the renewed operative resources. The round is funded once at B step N
and released at N+T for every source component; appending does not supply
that funding or choose one of the two parity labels.

For an occupied archive, the same total map moves the old pointer into
active and changes flag one to zero. For a dirty pointer with flag zero,
active becomes that dirty pointer. Neither case promises E readiness.
Applying A_i after no WRITE still toggles the flag. Hence z_i=1 has
completed-record meaning only inside the supported protocol theorem.
It is not a universal event detector or a provenance certificate. An
attempt to replace this gate by 'append when unused, otherwise identity'
would be a different map and would not inherit the given inverse proof.

The three record vectors E_i|0>, E_i|1>, O_i|1> are mutually orthogonal.
The local reader's projectors are

```text
I_pointer tensor |0><0|               : UNUSED,
Pi_even tensor |1><1|                 : HIGH,
Pi_odd tensor |1><1|                  : LOW.
```

They are a complete partition even on dirty cells. Their syntactic labels
do not encode invocation, epoch or context. Those belong to the fixed
external program. The equality of records here is the specified ordered
flag/parity snapshot together with that program context, not an imported
physical record ontology.

A supported fresh program consumes a previously unused cell on each round,
so it can append at most K records. For K=0 no positive trial is available.
The exhausted external interface returns its status and unchanged complete
state; it does not install an absorbing state in the reversible dynamics.
The inverse round can undo a round using the retained source and all
records. It cannot both erase its correlations and preserve all those
records as independent fresh trials. Source replacement would require the
additional retained reservoir swap stated outside this construction.

## 9. Causal histories with all registers and references retained

Fix a supported finite causal program of depth at most K. At prefix w
its next D_w,U_w and fresh cell index are fixed by that prefix and the
declared external inputs. Define

```text
M_(w,o)=U_w^*P_oU_w D_w,
K_empty=I,                 K_(wo)=M_(w,o)K_w.
```

Use one common tensor product of all K ordered archive cells. Let
|record(w)> mean its complete snapshot: a used cell contains its assigned
E|1> or O|1>, and every still unused cell contains E|0>. This is also a
precise embedding of the specification's separated used-record and
unused-cell factors. The chosen positions of unused cells can depend on
w. They must not be factored out as one common unused-cell state across
different adaptive branches. Only packet geometry and active E are
automatically common.

Induct on the prefix length. At the empty prefix the source/reference
density is rho_SR and the entire archive is unused. Suppose the retained
conditional branch has source/reference block
(K_w tensor I_R)rho_SR(K_w^* tensor I_R), archive snapshot record(w),
and the ready operative factors. The next declared cell is unused in this
branch, so section 8 applies even when the source is correlated with the
reference. Reading its parity o multiplies the source block on the left
by M_(w,o), on the right by its adjoint, and puts the corresponding record
in that exact cell. This is the claimed branch for wo. Thus every retained
conditional branch is exactly

```text
(K_w tensor I_R) rho_SR (K_w^* tensor I_R)
 tensor |record(w)><record(w)|
 tensor |ready packet/reserve/latch geometry and active E><same|.
```

The geometry factor omits the source-label degree of freedom already in
rho_SR, and the record factor includes all unused cells. No register is
discarded or duplicated by this notation. Two distinct outcome histories
first differ after the same prefix and therefore write orthogonal E/O
records into the same then-selected cell. Later supported rounds do not
reuse it. Their complete archive records remain orthogonal, including
adaptive choices of subsequent indices.

For an admitted fixed-depth coherent controlled program without parity
dephasing, expand the same one-round isometries without deleting their
cross terms. Orthogonal archive control blocks apply the chosen source
unitary on the ket prefix w and its adjoint on the bra prefix v. Induction
therefore gives

```text
sum_(w,v) (K_w tensor I_R)rho_SR(K_v^* tensor I_R)
          tensor |record(w)><record(v)|
          tensor |ready operative geometry and active E><same|.
```

The complete K-cell records are essential if their allocation differs.
This formula describes the admitted coherent program and its actual
append schedule; it does not add a hidden coherent controller, an
undeclared controlled-append primitive, or a coherent realization of every
external stopping decision. For a fixed schedule the same unused-cell
factor may of course be separated again. Parity dephasing removes the
terms with distinct recorded labels. Before that operation the displayed
operator is a coherent history state, not a list of actual outcomes.

Every branch weight is nonnegative by positivity. At each prefix,

```text
sum_o M_(w,o)^* M_(w,o)
 = D_w^* U_w^*(P_L+P_H)U_w D_w = I.
```

It follows by cyclicity of trace that the sum of the child weights equals
the prefix weight. Iterating up a complete bounded stopping tree proves
that all leaf weights sum to tr(rho_SR)=1. A terminal external status
retains its branch and contributes that branch's unchanged trace. Zero
branches remain zero maps; normalized conditional states are formed only
for positive trace. These are exact identities among positive operators,
not a sampling algorithm or a postulate selecting an actual leaf.

For repeated fixed U and D_w=I, the two source maps use the same
orthogonal projectors Q_L,Q_H. Their products vanish whenever a word
changes label, while Q_o^m=Q_o. Only all-LOW and all-HIGH histories survive.
This is correlated rereading of a retained source. With changed contexts
or declared D_w the ordered products above retain all within-HIGH
coherences and subsequent interference. Replacing them by products of
single-use scalar weights would be a different, generally false law.

General correlated initial apparatus inputs do not satisfy the ready
factorization used in this induction. They remain covered by the joint
matrix-unit law and the exact primitive compositions of section 4, not
by an assertion that a dirty archive is freshly supplied on every branch.

## 10. Retention limits and coherent feedback

For a passive retained archive A and any trace-preserving operation Phi
on its complement B,

```text
Tr_B[(id_A tensor Phi)(X_AB)] = Tr_B X_AB.
```

For a Kraus representation this follows from sum_j V_j^*V_j=I by testing
against any observable on A; equivalently it follows from Phi^*(I)=I.
Thus passive marginal retention holds even for entangled initial states.
The trace-preserving qualification matters: conditioning on a later
selective outcome can change posterior weights, although summing its
complete outcome set preserves the earlier marginal.

A causal source unitary controlled by earlier archive parity is diagonal
in those record projectors. Once archive parity has been read/dephased,
it does not change earlier labels or their prefix traces. Every source
unitary in a given old branch is trace preserving. Subsequent complete
branch sums preserve those same prefix weights by section 9. Passive
rereading acts as identity on the matching record branch and zero on
the other branches.

Before dephasing, such a controlled operation acts on the archive as a
control and can change its off-diagonal marginal entries. An explicit
admitted example starts with

```text
(f0 tensor |LOW> + f1 tensor |HIGH>)/sqrt(2).
```

Choose identity on the LOW block and interchange f0 and f1 on the HIGH
block, with identity on the other source labels and unused record blocks.
This is a total energy-preserving allowed controlled source unitary.
It sends the vector to f0 tensor (|LOW>+|HIGH>)/sqrt(2). The old archive
has changed from a diagonal half-and-half marginal to a coherent pure
superposition. Its parity probabilities are unchanged. If parity had
first been dephased, this feedback could not recreate those cross terms
from that dephased mixture. Thus preservation of earlier labels does not
imply preservation of the entire quantum archive under coherent feedback.

Direct archive Fourier controls, occupied-cell exchange, and inverse
rounds are other declared ways to change records and are outside passive
retention. A second unarchived clean B round applies the controlled phase
flip again; for a fixed source label it XORs the old parity rather than
supplying a fresh E. These exact continuations preclude an inference of
permanent immutable memory for every continuation of the reversible model.

## 11. Whole-family equality and finite paired-span closure

Whole-family equality fixes the complete descriptors in the specification:
carrier parameters, cut, preparations or joint input domain, all controls,
read names and bins, protocol class, retained registers and output map.
All packets, latch, active pointer and archive cells remain output unless
a different reduced interface was separately declared. For each finite
causal protocol and complete outcome/status word, compare the resulting
unnormalized joint operator maps. This definition includes mixed inputs,
correlations and every finite reference. It neither identifies all
members of the selected family nor asserts completeness of a physical
apparatus class.

A phase permutation can establish an equivalence only if a single fixed
unitary coordinate permutation intertwines preparations, every named
transition and read, and the output identification. These intertwining
identities then propagate through every composition. Equality of a
single reduced first-use instrument alone proves none of those additional
identities. In fixed retained coordinates E and O already give unequal
preparation outputs at the empty word; the same is true of E and
(E+O)/sqrt(2). Their single-use reduced interfaces can nevertheless agree
in the specified E/O case with the declared reader relabeling. A partial
trace is an explicitly weaker output map.

Now restrict to a finite energy bound and a fixed finite labeled operation
alphabet. The retained Hilbert spaces H_1,H_2 are finite dimensional,
with dimensions d_1,d_2. Let J_i be the preparation maps from the common
finite input operator algebra and L_(i,a) the branch maps for the same
alphabet. Include zero maps for absent outcomes, and keep the declared
external status interfaces fixed. These are linear maps; an unspecified
nonlinear readiness test is not an input to this criterion.

Write Delta(X,Y)=O_1(X)-O_2(Y) in the common output coordinates. Let W_0
be the complex span of the paired seeds (J_1(E_uv),J_2(E_uv)), and set

```text
W_(n+1) = span(W_n union
  {(L_(1,a)(X),L_(2,a)(Y)) : (X,Y) in W_n, all a}).
```

Induction shows that W_n is exactly the span of paired outputs obtained
from input matrix units by words of length at most n. The forward
inclusion expands each newly applied linear map; the reverse inclusion
removes the last letter of any nonempty word. Therefore the union W is
the span of all reachable paired word outputs.

This increasing sequence lies in
End(H_1) direct-sum End(H_2), of dimension d_1^2+d_2^2. Each strict
increase raises its dimension by at least one. After at most that many
strict increases there is an n with W_(n+1)=W_n; its defining closure
then implies W_(n+m)=W_n for every m. It is enough to test Delta on a
basis of this stabilized space.

If Delta vanishes on W, it vanishes on every word output of every input
matrix unit. By linearity all word maps agree on all inputs. Their
finite-reference amplifications agree on tensor products of input and
reference matrix units. Every causal branch is a word with its choices
fixed by its prefix, so the same identity holds at all leaves of every
finite causal tree and for their declared sums. Conversely whole-word
equality gives Delta=0 on every generator of W and hence on W itself.
This proves the if and only if criterion. Full retention uses the
identity output after the fixed coordinate identification; a reduced
interface uses its stated O_i instead.

For the four-source input the seed basis has sixteen matrix units.
If the declared input is correlated with apparatus, use the matrix-unit
basis of that complete input algebra. Retained memory is already part
of H_i and is never reset in L_(i,a), so the criterion includes future
effects of readiness and memory over arbitrarily long alphabet words.

With rational or specified algebraic coefficients, exact arithmetic and
finite-dimensional linear dependence tests make this a terminating exact
algorithm. For arbitrary unspecified complex coefficients it is only a
mathematical criterion. No finite algorithm for all energies at once or
for an uncountable control alphabet follows from this argument.

## 12. Audit domain counts and scope of this proof

The frozen finite audit checks implementations of these identities. Its
loop counts can be verified without running a scientific computation:

```text
291*2*sum_(N=2..5)[2(2N-1)] = 27936,
4*sum_(N=2..5)[(N-1)2(2N-1)] = 560,
291*1226 = 356766,
4*2*1226 = 9808,
291^2*2*4 = 677448,
16*1226*15*3 = 882720,
2*1226^2 = 3006152,
sum_(d=0..3)10^d = 1111,       16*1111 = 17776.
```

For the offset count, the six positive pairwise differences of the four
codes are 393,253,225,140,168,28; their twelve signed residues are distinct
and none equals 0,1 or 613. Thus adjoining those three residues gives
exactly fifteen offsets. These are declared loop-domain counts, not
observed pass results. The inherited sector census remains an admitted
arithmetic input. The verifier's finite cases supplement rather than
replace the universal bijection, matrix-unit, positivity, history and
finite-span proofs.

All conclusions here are conditional on the selected complex lift,
energy degeneracies, coherent controls, preparations, readers and external
finite protocol. The construction determines funded WRITE completion and
complete conditional post-states, but supplies no physical preparation
mechanism, no unique actual parity event, no sampler, no native realization,
no SI account and no cross-layer dictionary. Its target-motivated code and
known projectors do not become independent physical selection. Physical
instrument, terminal-event and class-completeness obligations therefore
remain outside the result, as required by the frozen specification.
