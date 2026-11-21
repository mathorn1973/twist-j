# A fixed-contact root clock and one fixed receiver for five actual dynamics

**NON-CANONICAL / L1. Conditional analytical candidate-T.**

This is an additive proof-first continuation. It preserves the earlier frozen
source and results. Its algebra was derived by hand before the separately
preregistered receiver audit. It neither selects a physical quantum phase nor
compiles the complete field-action controller of FULL-FIELD-PHASE.md.

The question has two different versions. Five characters assigned to an
unchanged label history are alternative readings, not five different inputs
to a receiver. Here five explicit contact dynamics produce different states
from one common preparation. A single unchanged receiver can then distinguish
them. This construction separates an actual test from a change of terminology.

## 1. The complete ordinary-contact clock

Use O=Z[j], rho=j^2, Q(a)=Tr(a abar)/2, and the ordinary total contact C.
On an admitted pair (p,q), with s=(p+q)/2 and t=(p-q)/2 in O, C sends it
to (s+rho t,s-rho t); the refused complement is fixed. C is a complete
bijection, preserves sum and Q(p)+Q(q), and C^5=I. Its inverse is C^4.

Prepare five neutral pairs (z_k,-z_k), k=0,...,4. Their amplitude carrier
is O^5, and their complete quadratic account is

    E_clock=2 sum_k Q(z_k).                               (R1)

On a neutral pair, C^3 multiplies the amplitude by rho^3=j. Consider

    V(z0,z1,z2,z3,z4)=(j z4,z0,z1,z2,z3).                (R2)

A fixed ordinary-contact/swap word implements V. First swap entire pairs
in the order (3,4),(2,3),(1,2),(0,1), rotating the list right by one. Each
pair swap consists of two ordinary whole-slot swaps. Then apply C^3 to
pair zero. This is eight slot swaps and three ordinary contacts, with no
state-dependent choice of the word. All admission tests remain the
inherited contact tests.

The word is a total account-preserving bijection on arbitrary occupied
states in O^10, not merely on the neutral preparation. Its inverse first
applies C^2 to pair zero, then reverses the pair swaps. On the neutral
subcarrier it has the exact linear action (R2).

Five ticks apply multiplication by j once to every amplitude:

    V^5=j I,       V^25=I.                              (R3)

More generally, on the entire occupied-pair carrier five ticks apply C^3
to every pair, so the twenty-fifth power is identity there too. A nonzero
neutral state has least period25: its period divides25, but V^5 z=jz
cannot equal z unless z=0. The zero neutral state is fixed.

The preparation z0=1, z1=...=z4=0 has account4. This is the minimum
nonzero account within this five-neutral-pair carrier. Indeed if
h(a)=A+B phi for nonzero a in O, then

    Q(a)^2-5B^2=4 N_(Q(j)/Q)(a) >=4,

so the positive integer Q(a) is at least2; Q(1)=2 attains it. This is a
restricted account minimum, not a minimum slot count or physical clock
cost. The clock occupies ten O slots, and its calendar is supplied.

## 2. Five laws with one old calibration

For m=0,...,4 define

    V_m=j^m V=V^(1+5m),
    V_m(z)=(j^(m+1) z4,j^m z0,j^m z1,j^m z2,j^m z3).    (R4)

Each has the same nearest-neighbor cyclic support, preserves (R1), and
satisfies

    V_m^5=j I,       V_m^25=I.                          (R5)

Every nonzero neutral state again has least period25. Thus the original
five-tick calibration does not determine which one-tick law is used.
This statement concerns an explicitly given five-member family, not a
classification of all possible contact clocks.

One fixed word for V_m performs the same pair rotation, then C to power
3(m+1) modulo5 on pair zero and power3m modulo5 on each remaining pair.
Its complete occupied-state inverse reverses the word and the contact
powers. Five repetitions apply C^3 to each pair even off the neutral
subcarrier, so the total twenty-fifth-power identity holds there as well.

If equal literal attempt counts are desired, they can be supplied explicitly.
Perform the eight slot swaps, C^3 on pair zero, and then C^k on every
pair, where k is the representative of3m modulo5 in {0,...,4}. Finally
apply4-k blocks of C^5 on the fixed pair four. Every member then uses

    3+5k+5(4-k)=23 ordinary contact attempts

and the same eight slot swaps. Since C^5=I on the entire ordinary pair
carrier, the padding changes no base endpoint. It is a supplied calendar,
not a derivation of physical duration. It also need not be invisible to a
separately added phase-action accumulator: a closed source contact loop
can carry such an increment. No additional action register is part of
this padded clock word. Equal attempt counts do not prove equal physical
time, identical intermediate paths or equal geometrical action.

The common preparation is the basis token e0, with amplitude1 at pair
zero and zero elsewhere. After one V_m tick,

    e0 -> j^m e1.                                       (R6)

The location is known in advance and is the same for all five laws. The
amplitude at that location is an actual different O element. This is not
merely a different interpretation of an unchanged pointer label.

## 3. One fixed calorimetric receiver at the known port

Attach the same extra O slot

    R=3+4j+2j^2=1+2a,       a=1+2j+j^2,
    Q(R)=32.                                           (R7)

After the single clock tick, take (p,q) to be clock pair one. Apply the
following fixed ten-contact word, independent of m:

    [ C_(p,R), C_(p,q) ] repeated five times.            (R8)

Read the final quadratic account Q(R_out). The other four clock pairs
are not touched. The literal inverse is the reversed word with every
contact replaced by C^4, followed by the inverse clock word. Thus the
complete preparation, including the stock, is recovered when the newly
created receiver state is erased.

Here is a hand derivation of the response. For input (p,q)=(j^b,-j^b),
R modulo2 is1. Before the stock contact admits, C_(p,R) refuses unless
p modulo2 is1, while the following balanced contact multiplies p by rho.
The first admitted stock contact is therefore block k=2b modulo5, with
blocks indexed0,...,4. At that cut p=1 and q=-1.

After n admitted stock contacts the two contacted slots are

    p_n=1+a-rho^n a,       R_n=1+a+rho^n a.              (R9)

For n=1,...,4 the balanced contact with q refuses: modulo2 its difference
is (1-rho^n)a, which is nonzero in O/2O=F16 because a modulo2=J is
nonzero and rho has order5. At n=5 the balanced contact can admit again,
but the stock has already returned and its final account is unaffected.
Hence n=5-k at the last stock cut.

The exact quadratic identities are Q(a)=7 and Q(1+a)=10. The cyclic
five-coefficient product (1+a) abar has coefficients (7,4,1,2,6), with
sum20. Consequently

    Q(R_n)=17+Tr((1+a) abar rho^-n)
          =17+5 w_(2n mod5)-20,
    (Q(R_1),...,Q(R_5))=(2,27,17,7,32).                 (R10)

The single unchanged receiver therefore gives

| Actual law | Clock amplitude at pair1 | Final Q(R) | Total account |
|---|---|---:|---:|
| V_0 | 1 | 32 | 36 |
| V_1 | j | 17 | 36 |
| V_2 | j^2 | 2 | 36 |
| V_3 | j^3 | 7 | 36 |
| V_4 | j^4 | 27 | 36 |

Every output is distinct. The common account is clock4 plus stock32.
If a neutral complete preparation is required, add a completely untouched
slot -R. The total ring sum is then zero and the account is68. This
spectator is retained in every inverse and is not a free uncounted source.

Backreaction is explicit. The stock transfers respectively0,15,30,25,5
units of Q to the clock pair. Its final account is a record of an actual
contact response, not a phase label rewritten after the experiment. The
clock pair is generally disturbed and need not remain on the original
neutral token orbit. No nondemolition reading, fresh stock on repetition,
permanent record after complete reversal, or minimal receiver price is
claimed. Q is still the declared mathematical account; empirical
calorimetry and coherent interference are separate questions.

The same stock reader can be attached to the high pair of the existing
two-pair25-state pointer. In that different apparatus the common account
is8+32=40. Neither construction alone implements the full source-field
Gamma-dependent controller or selects which physical model occurs.

A second fixed experiment connects directly to the previously exposed action
residue13. Perform thirteen V_m clock ticks before attaching the same stock
reader at the now-known pair three. Exactly

    V_m^13 e0=j^(2+3m) e3.

The five receiver outputs for m=0,...,4 are then2,32,7,17,27. This is an
actual clock word and actual stock interaction, not just a relabeling of
an unchanged register. Its account remains36, or68 with -R. The input
thirteen is an explicitly supplied test horizon. No general physical
source-to-clock controller follows from this one prescribed experiment.
The companion RECEIVER-CONTACT.md and its prospective audit specify the
same stock mechanism and its full occupied-state checks.

## 4. Exact mode preparation requires a larger scalar carrier

Let K=Q(j), choose an abstract lambda with lambda^5=j, and put L=K(lambda).
The characteristic polynomial of V over K is X^5-j. This polynomial is
irreducible. Indeed Phi25(X)=X^20+X^15+X^10+X^5+1 is irreducible over Q:
Phi25(X+1) is Eisenstein at5, since modulo5 it is X^20 and its constant
term is5, not divisible by25. Thus [Q(lambda):Q]=20, while [K:Q]=4,
and [L:K]=5. This also proves that an original O coordinate cannot be a
primitive twenty-fifth root.

On the principal complex embedding the five eigenvalues are

    lambda_t=zeta25^(1+5t),       t=0,...,4,

and corresponding right vectors are

    w_t=(1,lambda_t^-1,lambda_t^-2,lambda_t^-3,lambda_t^-4).

The left vector is (1,lambda_t,lambda_t^2,lambda_t^3,lambda_t^4), whose
pairing with w_t is5. Thus the coefficient of the t-th spectral component
of z in K^5 is

    (1/5) sum_(k=0)^4 z_k lambda_t^k.                   (R11)

If z is nonzero, its polynomial in (R11) has degree at most4 and cannot
vanish at any lambda_t. Every nonzero K-valued state therefore has
NONZERO projection onto all five complex eigenmodes. In particular no
nonzero original O^5 state is an exact single eigenmode.

The same irreducibility gives two precise filter statements. Any operator
P(V) with coefficients in K is either zero or invertible: reduce P modulo
X^5-j and use the field K[X]/(X^5-j). Moreover every K-linear operator
commuting with V belongs to this field, since it is determined by its
value on the cyclic vector e0. Its only idempotents are0 andI. There is
no nontrivial exact K-linear spectral projector, and no nonzero finite
polynomial filter can annihilate four of these modes while retaining one.

These are finite-carrier assertions, not objections to integer encodings
of algebraic numbers. Adjoining L, enlarging the representation, selecting
an archimedean limit, or changing the preparation contract changes the
question. No such preparation is supplied merely by declaring an
eigenvector over the larger field.

The dimension bound is sharp in its stated class. Any nonzero finite
K-vector space carrying an operator W with W^5=jI has minimal polynomial
X^5-j, so its dimension is a positive multiple of5. At least five
K-amplitude slots, equivalently twenty rational dimensions, are required.
V attains this bound. It is not a lower bound for nonlinear finite-state
pointers, which have a different carrier and output contract.

## 5. Positivity and locality do not finish the selection

The principal-embedding norm underlying the arithmetic account has no
spectral preference: every normalized complex eigenmode has the same norm.
The actual account is its trace on K-valued states, where an isolated
complex eigenmode is not exactly preparable. A different positive
Hermitian operator can be proposed:

    H_m=(I-V_m)^*(I-V_m)
       =2I-j^m V-j^-m V^*,       m=0,...,4.             (R12)

Each has the same nearest-neighbor cyclic support and positive quadratic
form. Their connection product around the cycle is the same j. On the
fixed V eigenmode w_t its eigenvalue is

    2-2 cos(2pi[1+5(t+m)]/25).                          (R13)

For H_0 the unique principal-embedding minimum is t=0: its angle magnitude
2pi/25 is smaller than the other principal magnitudes8pi/25,12pi/25,
18pi/25,22pi/25. H_m selects t=-m modulo5 as its corresponding complex
ground mode. The minimum vector is not a nonzero state in the original
K^5 carrier, by (R11).

There is an essential gauge qualification. With

    D_m=diag(1,j^m,j^(2m),j^(3m),j^(4m)),

one has V_m=D_m V D_m^-1 and H_m=D_m H_0 D_m^-1. These are exact O-unitary
conjugacies. They do not establish physically inequivalent predictions
when the preparation, receiver references and reading are all transformed
at the same time. In the experiment (R6)-(R10), e0 is unchanged by D_m,
but the stock reference is deliberately held fixed, so the complete
marked experiment is different and its different response is observable
inside the declared model. A source-only basis transformation is not a
transformation of that complete apparatus.

Nor does a positive H automatically prepare its ground mode. The actual
unitary clocks V_m preserve spectral magnitudes; so does unitary evolution
generated by any H_m. Relaxation, postselection, a dissipative reservoir
or normalized imaginary-time evolution would be an additional law with
its own energy, record, preparation and occurrence obligations. Finite
polynomial evolution over K still cannot yield exact one-mode isolation.
An asymptotic approximation can be studied separately, with an explicit
error bound and resource account.

Thus the proposed lowest-frequency/positive-ground rule may define a
comparison model, but it adds a Hamiltonian, a marked frame or gauge
convention, a scalar embedding and a ground-state preparation mechanism.
The older j calibration, locality and positive conserved account alone
have not supplied those choices.

## 6. What this continuation adds

There is now a fixed ordinary-contact/swap implementation of a25-period
root clock, a complete occupied-state inverse, and an explicit fixed
loaded receiver that distinguishes five actual root-clock laws with a
common preparation. The response has genuine backreaction and a finite
account36, or68 with the retained neutralizing spectator. The natural
linear root carrier has a sharp five-dimensional K minimum, but exact
single-mode preparation and finite exact filtering fail on that original
carrier. Positive local candidate energies have been exhibited with their
proper gauge and preparation qualifications.

This is a constructive discrimination experiment and a finite exact
selection boundary. It does not turn five semantic character readings of
one unchanged apparatus into five measurable alternatives, choose the
physical law, prove coherent quantum phase, or determine alpha. If every
source, receiver and reference is transformed together by D_m, m may be
only a convention and need not be physically selected at all. The actual
operational object is their relative coupling in a complete experiment.
The next obligation is therefore to derive the common coupling/reference
frame independently, or prove all complete predictions gauge invariant.
It is not to find a preferred root numerically. The fixed-R comparison
above freezes that frame and tests literal different coupled dynamics;
it does not assign intrinsic physical meaning to chi_t in isolation.
