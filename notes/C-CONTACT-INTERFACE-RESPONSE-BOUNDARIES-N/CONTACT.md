# Exact boundaries of finite contact interfaces

NON-CANONICAL / L1 / conditional analytical candidate.

This note proves conditional statements about finite total-contact words.
It introduces no physical interpretation, executable, search or census.
The supplied contact definition is the one stated in [#1917](https://github.com/mathorn1973/twist-j/pull/1917),
whose [immutable source proof](https://github.com/mathorn1973/twist-j/blob/43fe4fef2cff6952cf753df888bb7b1928dd744d/probes/P-OVERLAPPING-CONTACT-WORK-CLOCK-1/PROOF.md)
is pinned at `43fe4fef2cff6952cf753df888bb7b1928dd744d`.
Only its integral contact law is used here, not its added real controller.
The arguments below are written proofs, not reports of newly executed checks.

## 1. Total contacts and their realized linear branches

Let K=Q(j), where j is a primitive fifth root of unity, and let
O=Z[j] be its ring of integers. Set rho=j^2, A=O[1/2] and lambda=1-j.
A bar denotes complex conjugation; a star denotes conjugate transpose.
The two selected embeddings send j to exp(2*pi*i/5) and exp(4*pi*i/5).
Define the positive quadratic account

    Q(a)=Tr_(K/Q)(a*bar(a))/2
        =|sigma_1(a)|^2+|sigma_2(a)|^2,
    E(z)=sum_i Q(z_i).

For integral power coefficients a=(a0,a1,a2,a3),
2Q(a)=5*sum_c a_c^2-(sum_c a_c)^2. Thus E is positive definite on
O^n, viewed as a lattice of rank 4n. Calling E an account assigns no
physical energy, action, elapsed time or work unit.

For an unordered pair e={i,k}, the total contact C_e holds the complete
state when z_i-z_k is not in 2O. Otherwise put s=(z_i+z_k)/2 and
d=(z_i-z_k)/2, and replace that pair by (s+rho*d,s-rho*d).
Both s and d are integral on the admitted branch. All other slots hold.
The pair sum is fixed and its difference is multiplied by rho.
Admission is therefore invariant under that same pair contact, and
C_e^5=identity, including the refused branch. The inverse is C_e^4.

Write b_e=e_i-e_k and L_e=b_e*b_e^T. The admitted linear matrix is

    E_e=I-((1-rho)/2)*L_e.                              (1)

It acts by 1 on b_e's orthogonal complement and by rho on b_e.
Consequently E_e^*E_e=I, E_e*1=1 and 1^T*E_e=1^T.
These identities hold in K and in every complex embedding.
In particular each total contact preserves both the sum and E.

A finite word has a realized admission itinerary at each input. Replace
its admitted touches by (1) and its refused touches by I, and multiply
in chronological action order, with the first touch on the right.
The resulting branch matrix M satisfies

    M in Mat_n(A), M^*M=I, M*1=1, 1^T*M=1^T.           (2)

This is a statement about a realized branch, not a globally linear law
for the total word. Different input states can select different matrices.
A contact on an equal pair is admitted and has matrix (1), even though
its action on that particular pair of equal values is the identity.

## 1a. Four chronological staircase contacts

The following explicit preparation admits one fixed four-contact word.
Fix r,tau in O and put delta=(1-rho)*tau. Prepare five slots as

    z0=(r+2tau, r+2tau+delta, r+2tau+2delta,
        r+2tau+3delta, r).

Apply the same four contacts, in chronological order,

    (1,5), (2,5), (3,5), (4,5).                       (S1)

Immediately before contact (i,5), the fifth slot is r+(i-1)*delta,
while the untouched ith slot is r+2tau+(i-1)*delta. Their difference
is exactly 2tau, so admission holds for every tau in O. The contact
replaces a pair (h+2tau,h) by (h+(1+rho)*tau,h+(1-rho)*tau).
Thus the ith slot loses delta and the fifth slot gains delta.
Induction proves the endpoint displacement

    z_final-z0=delta*(-1,-1,-1,-1,4).                  (S2)

The preparation and the chronological order are part of this statement.
It claims neither that another ordering has the same endpoint nor that
all alternative orderings have been classified. For tau!=0 the four
initial leaf values are distinct, so this is not a two-level input of
the kind considered in section 6.

Four contacts are minimal for this specified endpoint when tau!=0.
For any candidate word, form the undirected graph of its actually
accepted contacts on the five slots. The sum of coordinates within
each connected component is preserved: every effective pair update is
internal to one component, and refused contacts do not change the state.
No nonempty proper subset has zero sum of the displacement in (S2).
A subset of k leaves without slot5 has sum -k*delta; one containing
slot5 and k<4 leaves has sum (4-k)*delta. Both are nonzero in K.
Hence the accepted graph must be connected. A graph on five vertices
needs at least four distinct edges to be connected, so any such word
has at least four accepted touches and at least four touches in total.
Word (S1) achieves the bound. For tau=0 the state is unchanged and
this nonzero-displacement lower bound does not apply.

With r fixed, this entire preparation family is only one affine
parameter tau. Even though tau ranges over O, it does not independently
vary all five coordinates and does not establish the rank premise below.

## 2. Returned auxiliaries require a full-rank variation hypothesis

Partition the coordinates into a free block F and a returned block R.
Fix one word, one realized branch matrix M, and one auxiliary preparation
r in O^R. Let D be a set of free preparations x in O^F that all select
this same branch. Assume the returned output is exactly r for every x:

    M_RF*x+M_RR*r=r, for every x in D.                  (3)

The required rank condition is

    span_K {x-y : x,y in D}=K^F.                       (4)

Subtracting (3) at x and y proves M_RF=0. Write M in block form as
[[U,V],[0,T]]. From M^*M=I, U^*U=I, hence U is invertible, and
U^*V=0 gives V=0. The remaining equation gives T^*T=I. Therefore

    M=diag(U,T), U^*U=I, T^*T=I, T*r=r.                (5)

The fixed total-one vector in (2) now gives U*1_F=1_F and T*1_R=1_R.
The free output is U*x, with no additive contribution from r.
Equation (3) for one fixed r does not prove T=I on other preparations.

A whole independent congruence class x0+2^m*O^F satisfies (4): its
differences include 2^m times each coordinate basis vector. The claim
must concern a single branch on that class; restoration across inputs
with different branches does not permit subtraction using one M.
More generally, only the actual K-linear span of the allowed differences
is annihilated by M_RF. The parameter's range cannot replace this rank.

For example, varying one tau over all O in x(tau)=x0+tau*v still gives
at most the one-dimensional span K*v. Independently varied bank inputs
cannot be inferred from such a correlated channel/bank preparation.
A finite set can satisfy (4), but that rank must be proved explicitly;
the number of sampled points alone is not a rank argument.

There is an exact counterexample to the weaker channel-only premise.
Take F={p,b}, R={r}, vary p arbitrarily, and prepare b=r=0. The single
contact C_{b,r} is admitted and leaves the actual b,r values zero for
every p. Thus the auxiliary returns on every channel congruence class.
Nevertheless its branch matrix mixes b and r, and its accepted cross-edge
count is one. The same example works with fixed b=r=c. It violates (4),
because the bank coordinate was never independently varied.

## 3. First ramified order and the cross-edge count condition

Since rho=(1-lambda)^2,

    (1-rho)/2=lambda-lambda^2/2,
    E_e=I-lambda*L_e modulo lambda^2*A.                (6)

The quotient A/lambda*A is F_5: setting j=1 in Phi_5(j)=0 gives 5=0,
and 2 remains invertible. Multiplying (6) along a realized itinerary gives

    M=I-lambda*sum_(accepted e) L_e modulo lambda^2*A. (7)

All products containing two first-order terms disappear in this quotient.
For distinct coordinates i,k, let n_ik be the number of accepted direct
touches on that unordered pair. Since (L_e)_ik=-1 exactly on that pair,

    M_ik=lambda*n_ik modulo lambda^2*A.               (8)

If an exact off-block entry M_ik is zero, then lambda*n_ik belongs to
lambda^2*A. Cancellation in this domain gives n_ik in lambda*A.
An integer has zero residue in F_5 exactly when it is divisible by five.
Thus exact decoupling forces each direct accepted F-R edge count to be
zero modulo five. This applies to each pair, not merely the total count.

The condition is necessary only. Multiples of five remove the first
ramified-order obstruction; higher-order off-block terms may remain.
Nor may exact decoupling be assumed from restoration that lacks (4).
An inverse symbol contributes a negative first-order count; alternatively
expand it as four positive contacts and use ordinary accepted counts.
With uniformizer 1-rho instead, the coefficient in (6) is divided by two;
the displayed normalization explicitly uses lambda=1-j.

## 4. Norm-one elements of the localized ring

**Arithmetic lemma.** If mu in A satisfies mu*bar(mu)=1, then

    mu belongs to {+j^k,-j^k : k=0,1,2,3,4}.           (9)

First, Phi_5(T)=T^4+T^3+T^2+T+1 is irreducible modulo two. It has no
root in F_2. The sole monic irreducible quadratic over F_2 is
T^2+T+1, and dividing Phi_5 by it leaves T+1. A reducible quartic
without a linear factor would have such a quadratic factor. Hence
O/2O is the field F_16, and conjugation induces an automorphism of it.

Write mu=a/2^m with a in O and m>=0 minimal. If m>0, then a is nonzero
modulo 2, while mu*bar(mu)=1 gives a*bar(a)=2^(2m). Reducing modulo 2
would multiply two nonzero elements of F_16 to zero, a contradiction.
Thus mu is in O; its inverse bar(mu) is also integral.

Every embedding sigma of K commutes with conjugation, so
|sigma(mu)|^2=sigma(mu*bar(mu))=1. Here is a bounded-conjugate proof
that mu is a root of unity. Each power mu^n is an algebraic integer
of degree at most four whose conjugates all have modulus one.
The coefficients of its monic minimal polynomial are integer elementary
symmetric sums of those conjugates, bounded in absolute value by the
corresponding binomial coefficients. There are only finitely many such
integer polynomials and finitely many roots among them. Two powers of
mu therefore coincide. Since mu is nonzero, a positive power equals one.

If its order is m, then Q(zeta_m) is a subfield of K, so phi(m) divides
four. The possibilities are m=1,2,3,4,5,6,8,10,12. The Galois group
of K is the cyclic group (Z/5Z)^*, of order four; it has a unique
quadratic subfield, Q(sqrt(5)), fixed by complex conjugation and real.
Orders 3 or 6 would introduce Q(sqrt(-3)); orders 4,8 or 12 would
introduce Q(i). Those possibilities are excluded. The remaining orders
are exactly the roots in (9), proving the lemma.

We also need their ramified divisibility. The identity

    5=product_(k=1,...,4) (1-j^k)                     (10)

follows by evaluating Phi_5 at 1. Each factor is lambda times
1+j+...+j^(k-1), whose residue modulo lambda is k, nonzero in F_5.
The latter factor is a unit: its field norm is 5/5=1. Thus 5 is a
unit times lambda^4. For k=1,...,4, the element 1-j^k has lambda
valuation one, while 1+j^k has valuation zero. Consequently

    mu in (9), 1-mu in 5*A  implies  mu=1.             (11)

Localizing at two changes none of these lambda valuations.

## 5. Classification of a decoupled two-slot free block

Assume the hypotheses of section 2 with F={p,b}. Its matrix U is unitary,
has entries in A and fixes (1,1). The orthogonal complement of that fixed
line is the line spanned by (1,-1), so for a scalar mu in A,

    U=(1/2)*[[1+mu,1-mu],[1-mu,1+mu]],
    mu*bar(mu)=1.                                    (12)

The arithmetic lemma gives mu=+/-j^k. Equation (7) also gives U=I
modulo lambda, so mu=1 modulo lambda. Negative roots reduce to -1,
which differs from 1 in F_5. Therefore mu is a fifth root of unity.
Since rho=j^2 generates those roots, there is a unique k modulo five with

    U=E_{p,b}^k.                                    (13)

This classification includes a hold and four nontrivial pair rotations.
It does not classify programs whose bank/reference inputs are correlated
in a way that defeats the rank hypothesis of section 2.

Taking the off-diagonal entry of (13) modulo lambda^2 gives lambda*k.
Comparing with (8) identifies k=n_pb modulo five, the number of accepted
direct p-b touches in the realized branch. Cross-block contacts already
have multiplicity zero modulo five under the exact block hypothesis.
This is a classification and a residue count, not a shortest-word result.

## 6. A five-slot two-level endpoint obstruction

Consider a finite total-contact word on exactly five slots, with input
(a,a,a,a,b) and output (c,c,c,c,d), all in O. Its realized matrix M
satisfies (2), irrespective of how parity selected that itinerary.
If a=b, every touch acts on an equal pair and the state never changes.
Assume a!=b and let e_5 be the fifth coordinate basis vector. Then

    M*e_5=r*1+mu*e_5,
    r=(c-a)/(b-a), mu=(d-c)/(b-a).                    (14)

In particular r=M_15 and mu=M_55-M_15 belong to A. Taking coordinate
sums in (14) gives 5r+mu=1. Since M fixes 1, the vector
v=e_5-(1/5)*1 satisfies M*v=mu*v. Unitarity gives mu*bar(mu)=1.
The arithmetic lemma applies, while r in A gives 1-mu=5r in 5A.
Equation (11) forces mu=1 and r=0. Hence

    c=a and d=b.                                    (15)

This excludes changed two-level endpoints. It does not exclude nonempty
contact words, nontrivial intermediate states or loops with this endpoint.
Preservation of the sum and the single account E alone is not the proof:
the realized matrix, all-embedding unitarity and localized arithmetic are
essential. If one additionally restricts the relative scalar to be real,
its norm-one alternatives are +/-1; the putative -1 reflection would give
c=(3a+2b)/5 and d=(8a-3b)/5. Equation (11) excludes that branch as well.

The same conclusion holds with returned auxiliaries only under a stated
additional hypothesis: on a fixed branch, vary all five free coordinates
with differences spanning K^5, while the auxiliary preparation is fixed
and returned. Section 2 then produces a decoupled five-by-five matrix U
with the same properties (2), and the proof applies to U verbatim.
A one-parameter preparation or channel-only variation does not establish
this reduction. No general returned-catalyst theorem is asserted here.

## 7. A retained channel transfer needs an account destination

Suppose a prepared balanced pair is p=r+S, q=r-S and the requested output
is r+F*S, r-F*S, with r unchanged and an input-independent F in K.
The parallelogram identity for Q gives

    Q(r+S)+Q(r-S)=2Q(r)+2Q(S).                         (16)

If every other coordinate, including every bank, returns exactly to its
input value, conservation of E therefore requires Q(F*S)=Q(S).
If this holds for every S in K, then |sigma_i(F)|=1 for i=1,2.
To see the last implication without extrapolation, put
h_i=|sigma_i(F)|^2-1. Inputs S=1 and S=u=1-j give

    h_1+h_2=0,
    h_1*|sigma_1(u)|^2+h_2*|sigma_2(u)|^2=0.

The two u weights are (5-sqrt(5))/2 and (5+sqrt(5))/2, which differ.
The equations force h_1=h_2=0. A family consisting only of rational
multiples of one S supplies only one equation and is not sufficient.

If some explicit outgoing coordinates are permitted to change while all
other auxiliaries return, their total account change must instead be

    Delta E_out=2*(Q(S)-Q(F*S)).                      (17)

For attenuation this is positive. Equation (17) is necessary bookkeeping,
not a construction of that outgoing load or a choice of its physical meaning.
Changed fresh banks can carry this account. Their complete forward
regeneration while retaining an attenuated channel transfer requires a
further declared destination. Reversing the entire word restores the banks
while also undoing its channel transfer; that is a different operation.

A reuse attempt leaving a nonzero clock residue also fails the stated
ready-state return condition. Such a residue cannot be ignored merely
because the channel coordinates have the desired values.

## 8. Erasing a clock-only identity segment

Let a chronological program be prefix u, clock-only segment c, suffix v.
Let D be its declared input family. Suppose c touches only clock slots
and returns those slots exactly for every state in T_u(D). Then c fixes
the complete state at every such boundary, not just a readout:

    T_c(T_u(z))=T_u(z),
    T_v(T_c(T_u(z)))=T_v(T_u(z)), for z in D.           (18)

Thus deleting c preserves the boundary transfer and every subsequent
admission decision. The suffix is deterministic and starts in precisely
the same complete state. This applies to a segment of any length,
provided its exact identity premise is proved on the declared family.
The intermediate trace and word length change. No equality of elapsed
physical time or action follows, and an external timer is not part of
this total-contact law. Finite tests establish (18) only for their tested
family unless a separate argument proves the universal premise.

## 9. Finite integral orbits and an infinite formal matrix product

For fixed n and fixed initial E, the positive definite norm shell in the
lattice O^n is finite. Every total contact preserves E and is invertible.
Thus the orbit of any fixed integral input under arbitrary total-contact
words is finite. This does not bound one universal orbit size across all
initial accounts or across a growing number of coordinates.

The corresponding formal admitted matrices need not form a finite group.
On three slots consider E_01*E_12, whether or not an infinite repetition
of that admitted itinerary is legal for a chosen integral state. With
a=(1+rho)/2, direct diagonal multiplication gives

    Tr(E_01*E_12)=2a+a^2=(rho^2+6rho+5)/4.             (19)

Modulo two the numerator is (rho+1)^2, nonzero in F_16: the residue of
rho has order five, since it is not 1 and satisfies rho^5=1.
Therefore (19) is not integral at two. A finite-order matrix in
characteristic zero has roots of unity as eigenvalues, so its trace is
an algebraic integer. Equation (19) proves this formal product has
infinite order. It does not supply an indefinitely admitted integral orbit.

There is no contradiction. Formal admitted matrices act on K^n and may
introduce dyadic denominators; the total rule holds a contact when its
integrality admission fails. Infinite formal matrix order alone proves
neither density in a unitary group nor approximation of a specified
amplitude by admissible total words. Finite fixed-input orbits likewise
exclude no approximation claim that explicitly changes its resource family.

## 10. The limited finite-bit frequency statement

A deterministic event on a uniform sample of exactly 2^N equally weighted
outcomes has frequency m/2^N. It cannot have exact frequency 3/5.
This is a counting statement with an explicit sampling measure, not a
probability law supplied by a deterministic contact program.

For a length-L word on n slots, its admission itinerary is determined
by the initial residue modulo 2^L*O^n. Indeed, initially congruent states
differ by 2^L times an integral vector. At each touch their admission
agrees while the remaining divisibility exponent is at least one; an
admitted linear map loses at most one factor of two, and a refusal loses
none. Induction covers every decision through touch L.
A uniform sample of that full residue space has 2^(4*n*L) elements.
Every itinerary event under this particular uniform sample has a dyadic
frequency. The conclusion is about itineraries, not arbitrary unbounded
endpoint predicates. No numerical census is being asserted.

Conditioning on a subset with non-power-of-two size, choosing unequal
weights, or taking a limit changes the premise. For example, three of
five conditioned outcomes have frequency 3/5 without contradicting it.
For a rational a in A, some 2^m*a is a rational algebraic integer and
therefore an integer. Thus A intersect Q=Z[1/2], excluding 3/5 as a
literal rational entry
of a fixed branch matrix. It does not exclude 3/5 as a normalized readout,
a conditional frequency or a Taylor coefficient. In particular the
coefficient in (1+x/5)^(-5)=1-x+(3/5)*x^2+O(x^3) is not a fixed matrix
amplitude; a response theorem requires its own load and parameter hypotheses.

Proof text supplied under the repository Apache-2.0 license.
