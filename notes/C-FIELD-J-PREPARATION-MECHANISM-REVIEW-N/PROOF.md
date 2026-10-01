# Independent local-loading argument and limitations

**PUBLIC, NON-CANONICAL. Independent proof candidate for the frozen L1
contract; not an execution report or final author-source review.**
Owner: A. M. Thorn / preparation_breaker. Original work, Apache-2.0.
Prepared 2 October 2026. Source and exposure are fixed in PREREG.md.

## 1. A total dilation, not an erasing pointer map

Write e_j for the even pointer mode |2j>, with indices modulo L>=3.
The odd modes and every other Stage-C factor remain part of the carrier.
Let d=(e_j-e_(j+1))/sqrt(2), s=(e_j+e_(j+1))/sqrt(2). They are orthogonal
unit vectors. On pointer times bath put x=d|0>, y=s|1> and
nu=(x-y)/sqrt(2). The rank-one projector H=|nu><nu| obeys H^2=H=H^*.
Consequently U=I-2H has U^*=U and U^2=I. In particular Ux=y, Uy=x,
and U fixes their joint orthogonal complement, including every odd mode.
This determines U on the complete carrier, not only a fresh-bath slice.

All Hamiltonians hbar*g(t)H at this edge commute at different times.
Their time-ordered exponential at integral g=pi is
I+(exp(-i*pi)-1)H=I-2H. The pulse area and the chosen projector coupling
are supplied controls. An exchange Hamiltonian with unwanted swap phases
cannot be substituted without changing the primitive.

For input bath zero split psi=Q psi+d<d,psi>, Q=I-|d><d|.
The first summand is fixed and the second goes to s<d,psi>|1>.
Thus V psi=Q psi|0>+J psi|1>, J=|s><d|. Since
Q^*Q+J^*J=Q+|d><d|=I, this is an isometry and its partial trace is the
stated channel. This identity holds with arbitrary finite ancillary factors
and all pointer/ancilla correlations by applying it to ket and bra.

Use a distinct initially independent pure bath zero at each invocation.
Multiplying the isometries gives the full retained operator
sum_(u,v) K_u Omega K_v^* tensor |u><v|. The order of factors in K_u
is the actual script order; there is no measurement or removal of cross
terms. Reversing the actual reflections in reverse order gives the exact
inverse for every initial state, even when the incoming baths are dirty.
The reduced Q/J channel needs bath freshness; the inverse does not.

The complete energy is the inherited C energy plus B constant bath units.
Each operation touches only the degenerate pointer/bath factors and is
identity on the packet fields, reserves, latch and flags. It therefore
commutes with the entire bare-energy operator, including every dirty C
state. This is a chosen degeneracy and a conservation statement. It gives
neither a cost for the pulse drive nor a physical thermal interpretation.

## 2. Exact one-edge gain and a sweep estimate

All operators in this section act on the even L-dimensional sector.
Let E=L^(-1/2)sum e_j, P=|E><E|. Then Q_j E=E and
<E,s_j>=sqrt(2/L), <E,d_j>=0. It follows directly that

```text
Phi_j^*(P)=Q_j P Q_j+J_j^* P J_j=P+(2/L)P_j.
```

For a positive input this proves the exact fidelity increment and its
nonnegativity. It also proves that each channel fixes P itself, since
Q_j E=E and J_j E=0.

Define B_0=I, B_(j+1)=Q_j B_j and A=B_L. A partial sweep's reduced state
is a sum of positive Kraus contributions. Its all-zero bath word is
B_j rho B_j^*. Thus the sum of all L fidelity increments is at least
(2/L)sum_j Tr(P_j B_j rho B_j^*). The exact operator telescoping identity

```text
sum_j B_j^* P_j B_j
 = sum_j (B_j^*B_j-B_(j+1)^*B_(j+1)) = I-A^*A
```

proves Phi^*(P)-P >= (2/L)(I-A^*A). This is an operator inequality
because it holds against every positive rho. No jump history was
postselected; one positive term per partial sweep was only used as a
lower bound on the full gain.

For any vector psi set a_j=<d_j,B_j psi>, b_j=<d_j,psi>. The recursion
B_j psi=psi-sum_(k<j)d_k a_k gives
b_j=a_j+sum_(k<j)<d_j,d_k>a_k. Distinct cycle edges have inner product
-1/2 when adjacent and zero otherwise. At L=3 each edge has the other
two as its distinct neighbors; the same equations remain valid:

```text
b_0=a_0,
b_j=a_j-a_(j-1)/2                  (1<=j<=L-2),
b_(L-1)=a_(L-1)-a_(L-2)/2-a_0/2.
```

Let M be this coefficient matrix. Its absolute row and column sums are
at most two. Explicit weighted Cauchy-Schwarz gives

```text
sum_j |sum_k M_jk a_k|^2
 <= sum_j (sum_k |M_jk|) sum_k |M_jk| |a_k|^2
 <= 4 sum_k |a_k|^2.
```

Also sum |a_j|^2=||psi||^2-||A psi||^2 by the orthogonal projection
loss identity at each step, whereas sum |b_j|^2=<psi,G psi> for
G=sum P_j. Hence G <= 4(I-A^*A) on the whole even space.

To find G's gap, let zeta=exp(2pi*i/L) and
v_k=L^(-1/2)sum_j zeta^(kj)e_j. A direct coordinate calculation gives
G v_k=[1-(zeta^k+zeta^(-k))/2]v_k. The v_k are an orthonormal basis
by the finite geometric-sum identity. Only k=0 has zero eigenvalue;
the smallest other eigenvalue is lambda=1-cos(2pi/L). Therefore
G>=lambda(I-P). On [0,pi/2], concavity of sin gives sin x>=2x/pi.
For x=pi/L, L>=3, this yields
lambda=2sin^2(pi/L)>=8/L^2. Combining these exact estimates proves

```text
I-A^*A >= (lambda/4)(I-P) >= (2/L^2)(I-P),
Phi^*(P)-P >= (lambda/(2L))(I-P) >= (4/L^3)(I-P).
```

The constant is uniform, conservative and never fitted to a numerical gap.
Put r=1-4/L^3, so 0<r<1. Taking traces against a density and iterating
gives 1-F_n<=r^n(1-F_0), including n=0. The sharper lambda factor
follows the same way. Fidelity tending to one implies trace distance
to P tends to zero: purify rho, project the purification onto E, and
compare the resulting pure vectors to obtain D(rho,P)<=sqrt(1-F).
A stationary density must have 1-F<=r(1-F), hence F=1. Positivity then
forces support in the one-dimensional E line, so the sole even-sector
stationary density is P. No odd-sector or phase-mismatched uniqueness is
being inferred. Fixed sweep order need not be translation covariant.

## 3. A whole correlated bank and its actual remainder

Let m=K+1 and let Q denote all pointers. The initial density may correlate
all even-supported pointers with one another and with Z. Fresh baths
are a pure independent tensor product. Operations on other pointers and
their baths do not change pointer i's marginal; the reduced evolution
of that marginal is exactly Phi^(n_i). This follows either by partial
trace of the retained isometries or by the dual identity on observables
of pointer i. Thus each final deficit is at most
d_i=r^(n_i)(1-F_(i,0)).

The commuting pointer projectors P_i satisfy the operator union bound
I-product P_i <= sum_i(I-P_i). Consequently, with R=product P_i and
t=1-Tr(R Omega_out), one has t<=min(1,sum_i d_i)=delta. Retain every
bath in Z'. The product projection has rank one on Q; hence

```text
R Omega_out R = P^(tensor m) tensor tau,
Tr tau = 1-t.
```

The actual marginal eta=Tr_Q Omega_out decomposes as tau+xi, where
xi=Tr_Q[(I-R)Omega_out(I-R)] is positive and has trace t. The cross
terms vanish under this partial trace because their pointer supports
are orthogonal. Neither eta nor xi is required to be fresh, independent
of source preparation, or free of the old pointer information.

For completeness the unnormalized gentle estimate is exact without an
assumption of purity. Purify Omega_out to a unit vector psi and let
phi=R psi. Then ||phi||^2=1-t and psi=phi+chi with phi orthogonal to chi,
||chi||^2=t. On their two-dimensional span the difference
|psi><psi|-|phi><phi| has trace norm sqrt(t(4-3t))<=2sqrt(t), with the
endpoints t=0,1 given by continuity/direct evaluation. Partial-trace
contractivity gives ||Omega_out-R Omega_out R||_1<=2sqrt(t).
The triangle inequality now yields

```text
D(Omega_out, P^(tensor m) tensor eta)
 <= sqrt(t)+t/2 <= sqrt(delta)+delta/2.
```

Both compared operators are densities, so clipping at one is valid.
This is a complete-state decoupling bound against the actual output
remainder. It does not assert that the environment was reset or that
all source/bath correlations disappeared. The original Z marginal is
exactly unchanged under a trace-preserving operation confined to Q and
its independent baths, even for initially correlated QZ.

If an un-clipped sum d_i is at most 4e^2/9 with 0<e<=1, then
sqrt(delta)+delta/2<=2e/3+2e^2/9<=8e/9<=e. The stated sufficient
budget is therefore valid (and deliberately not tight). Every finite
m and positive e has some finite budget because r^n tends to zero.
An entirely rational stronger-budget certificate is also available:
for a=4/L^3, (1-a)^(-n)>=(1+a)^n>=1+na by the binomial theorem, so
(1-a)^n<=1/(1+na). Choosing an integer n with
c/(1+na)<=4e^2/9, c=m or m(1-1/L), suffices without simulating n
collisions or numerically estimating a logarithm. This is used only to
audit existence and accounting; it does not improve the claimed rate.

## 4. Finite protocols, prefixes and conditioning

Use identical declared finite C protocols on the actual loaded state
and on P^(tensor m) tensor eta. The loading baths are retained and acted
on by identity. The prescribed C source and other untouched preparation
marginals in eta are the same as before loading. Under the stipulated
clean source/geometry/flag descriptor the ideal comparison therefore
satisfies C's ready interface, with its enlarged untouched reference.
A loader alone does not supply that separate descriptor.

For a fixed finite causal tree the operation producing all outcomes in
an orthogonal register, retaining every leaf/status, is CPTP. The local
instrument branches are CP; trace preservation follows successively
from the complete branch sum at each internal node, including bounded
stopping. Zero branches are still present as zero operators. Applying
the same CPTP map contracts the trace distance established above. One
bank was loaded once; this argument compares one complete map and has
no extra multiplicative horizon h. Any unmentioned bath feedback or
separately supplied approximate later intervention is a different problem.

Further partial trace and classical reading also contract distance.
Hence the formal outcome-register trace law has total variation at most
epsilon and every prefix event has weight error at most epsilon. This
is a comparison of quantum traces only; it defines no actual outcome.
Selecting one branch gives unnormalized operators A,B with
||A-B||_1<=2epsilon. This follows from positivity and trace
nonincrease applied to the positive and negative parts of a Hermitian
input difference. If p=Tr A and q=Tr B are both positive, then

```text
||A/p-B/q||_1 <= (||A-B||_1+|p-q|)/p
                         <= 4epsilon/p,
```

and symmetrically with q. Thus the weaker symmetric stated bound
D(A/p,B/q)<=min(1,2epsilon/min(p,q)) is certainly valid. No uniform
small bound survives arbitrarily rare branches. If the ideal branch
has q=0, actual weight p is at most epsilon by the event-weight bound,
but it need not vanish. Never discard it to restore exact C support.

## 5. Distinguishing mechanism predictions and its failure controls

The fresh bath's one projector has expectation Tr(J rho J^*)=Tr(P_j rho).
The edge gain identity in section 2 is therefore exactly (2/L)q_j.
Summing along any fixed fresh-bath script on one pointer gives
sum q=(L/2)(F_final-F_initial). The sum is the expectation of the sum
of the distinct retained bath-mark projectors; no independence or actual
mark selection is needed. For a basis blank, F_initial=1/L; every finite
sum is at most (L-1)/2 and the infinite-sweep limit is that value. At
L=613 it is 306. A marked bath state has the same assigned bare energy
as an unmarked one; marks are not emitted energy quanta.

For rho=I/L, one collision gives
(Q_j+|s_j><s_j|)/L = I/L+(|e_j><e_(j+1)|+|e_(j+1)><e_j|)/L.
Thus all position populations stay 1/L while exactly the two neighboring
off-diagonal entries become 1/L and q=1/L. In contrast P is fixed and
has q=0. Both initial densities are translation-conjugation invariant;
only P is supported on the invariant-vector line. This bath/coherence
diagnostic is separate from fitting the Stage-C parity-instrument target.

With incoming bath one, use the orthogonal projection onto s instead:
U(E|1>)=(I-|s><s|)E|1>+d<s,E>|0>. Its E overlap in the second term
vanishes and in the first is 1-2/L. The reduced fidelity is exactly
(1-2/L)^2. Hence arbitrary used baths do not inherit the cooling channel.
Odd pointers are fixed, so off-even states do not inherit its convergence.
Archive flags are untouched; a used record is neither erased nor made
fresh by this loader. Applying the pulses to stored records can change
those records and is outside C's passive-retention promise.

For phases z_j of modulus one, the common dark equations are
psi_(j+1)=z_j psi_j. A nonzero solution forces product z_j=1; conversely
that condition supplies the unique line with psi_0 arbitrary and all
later values fixed by successive products. Every magnitude is equal.
The vector E itself solves the equations only if every z_j=1. Common
kernel existence is the exact statement here. Inconsistent holonomy is
not a claim that every other stationary density has been classified.

At zero phases write the four nonzero coordinates of 2nu as
(1,-1,-1,-1). Thus U=I-zz^T/2 has dyadic entries, and so do Q and J.
Finite matrix products, sums, conjugation and partial traces preserve the
ring Z[1/2]. A dyadic initial density and basis baths therefore give a
dyadic reduced density after every finite unconditional sequence. The
target P has diagonal entry 1/613, which is not in that ring: if it were
a/2^k, the odd integer 613 would divide 2^k. Exact finite preparation
from the specified basis blanks is consequently impossible within this
particular class. For basis-blank pointers tensored with arbitrary rho_Z,
the pointer marginal is dyadic and the untouched Z drops out of this
calculation. Already supplied P, nondyadic input densities,
postselection with normalization and different primitives are not covered.

## 6. Resource and claim audit

The coherent pointer bank is not placed in the basis-blank input. Instead
the model supplies a new mode graph, coherent signed couplings, exact
pulses, independent pure bath bits, storage and an external script. These
resources can transfer purity and create off-diagonal pointer coherence.
Afterward every bath remains present and may store old pointer information
and correlations; calling it fresh again would add a new unsupported
preparation assumption. Unitary inversion restores the complete old state
jointly, not a free reusable supply preserving all old records.

The graph is local in the newly declared internal mode adjacency. No
derivation of B spatial locality or of a microscopic drive from J/native U
is supplied. The classical boundary control fields have no claimed closed
quantum microstate or physical work calculation. Source-code loading,
context rotations, source renewal, zero archive flags, address/timing
control, event semantics and an actual-record law remain supplied/open.
Flat bare energy and trace identities do not close any of those debts.

The positive result is conditional approximate pointer loading on a
nonempty even-supported domain, with an explicit joint error and finite
resource budget. The finite obstruction excludes exact basis-blank loading
only in the dyadic zero-phase primitive class. Neither conclusion promotes
the physical QDD owners or the canonical ledger. These conclusions remain
subject to the frozen independent audit and later author-source comparison.
