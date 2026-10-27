# A finite Hamiltonian clock with an energy-sharp source and an exact accepted channel

**NON-CANONICAL, L1, conditional candidate-T. Independent review pending.**
Author: A. M. Thorn. Public reservation: issue #1750. Apache-2.0.

The general history-clock and perfect-transfer constructions are prior art.
The contribution claimed here is their precisely scoped energy-sector and
record interface to the complete forward-filter candidate. Concurrent #1749
owns the separate geometrically local compiler and resource-preparation route;
this note does not supply or claim that route. There is no claim
of a new universal clock, a native TWIST-J realization or a physical experiment.
The general lemmas below are proved independently of the candidate filter.
The numerical filter consequences are conditional on its still-unaccepted
source and spectral proofs.

## 1. Fixed inputs, changed model, and the target word

Public authority is main/canon-v105
`892a0b11089d34e241e1eb76d2c03247022d18e6`. The candidate inputs are:

- #1746 at `01acc42b78f75095587765e9a5b91ee70dc28f37`,
  `notes/C-FORWARD-ONLY-CAPTURE-FILTER-N/PROOF.md`;
- #1748 at `ecb3460977cd2ee8a120797ffa53ba88cbe14171`,
  `notes/C-FORWARD-AUTONOMOUS-CLOCK-N/{CLOCK,ENERGY}.md`.

Those files are not changed or promoted. Only the word through the completed
acceptance flag is reused. The H native release steps and cyclic wrap of
#1748 are NOT part of the present word. Instead an identity tail is added.
This changes the autonomous scheduling model, not the pinned filter.

Let D=327680, P=D+1=327681 be the pentit count including the loader, and
B=2D+3=655363 the binary target count including the final flag. With the short
native transport T=2, the #1748 count through the final flag is

    L = 5 + T + 3D + B = 1638410.

Let G_0,...,G_(L-1) be that fully specified unitary word on a finite data
space H_D. It includes the loader, native contact/transport, every filter
register and every rejected history, and the reversible Boolean predicate.
All work targets start at zero. The final flag f is a fresh target, untouched
until the last G_(L-1), which writes the full acceptance predicate. Thus on
the prescribed ready family the flag is exactly zero at every prefix j<L.
The arbitrary logical source label, occupied receiver and a passive reference
R are not part of the fixed ready preparation and may be mutually entangled.

Choose M=2L, set G_j=I for L<=j<M, and use clock labels j=0,...,M. Write

    V_0=I,    V_j=G_(j-1)...G_0,    V=V_L.

Thus V_j=V throughout the identity tail L<=j<=M. These definitions give
3,276,821 clock states, not the cyclic clock count in #1748.

A finite spatial realization is fixed before this construction. For the
source at s=99, choose the finite cyclic box of #1748 CLOCK section 5 with
H=0 and margins for all prefixes: R_box=|s|+T+D+3=327784, with coordinate
representatives [-R_box,R_box]. The gates are total finite unitaries, with
periodic translations and the declared contact/calibration factors. Every
ideal prefix on the prescribed source remains away from the artificial seam.
The inherited infinite-space bound projector will be evaluated by the fixed
zero-extension isometry on these reached states; finite and infinite spectra
are not identified. Clock evolution below stays in the span of these prefixes,
so it introduces no additional spatial truncation of the initial experiment.

## 2. A time-independent Hermitian generator with exact execution

Define h_j=sqrt((j+1)(M-j)), for 0<=j<M, and

    K = sum_j h_j ( |j+1><j| tensor G_j
                       + |j><j+1| tensor G_j* ).             (1)

This is a bounded Hermitian matrix. In particular it includes the reverse
clock edges and their adjoint data blocks. The TARGET word contains no W*
instruction, but the MICROSCOPIC Hamiltonian is not a strictly forward-hop
law. Omitting those reverse terms would violate Hermiticity. This admitted
change of microscopic control class is essential, not hidden.

Let J_M be the scalar tridiagonal matrix with off-diagonal entries h_j, and
let Z=sum_j |j><j| tensor V_j. Then Z is unitary and

    K = Z (J_M tensor I_D) Z*.                               (2)

Indeed V_(j+1)V_j*=G_j. Equation (2) is an all-state identity, with no ready
assumption, postselection, commuting-gate assumption or discarded history.

### Candidate theorem 1: exact history amplitudes

For any vector psi, including any passive reference, and any real t,

    exp(-i kappa t K)(|0> tensor psi)
      = sum_(j=0)^M a_j(t) |j> tensor V_j psi,

    a_j(t)=sqrt(C(M,j)) (-i sin(kappa t))^j
                          cos(kappa t)^(M-j).                (3)

Proof: on M two-state factors, sum_a X_a preserves the symmetric subspace.
In its normalized weight-j basis the matrix is J_M. Its exponential is the
product of M commuting factors exp(-i kappa t X_a). Expanding their action
on |0>^M gives (3), and conjugating by Z proves the data statement. This
also proves spec(J_M)={M-2r:0<=r<=M} and ||K||=M.

At

    t_star = pi/(2 kappa),

only j=M survives, and

    exp(-i kappa t_star K)(|0> tensor psi)
       = (-i)^M |M> tensor V psi.                           (4)

Thus endpoint execution is exact for the COMPLETE target unitary, not just
its accepted effect. It holds uniformly for all data/reference inputs.
Intermediate clock motion is a coherent distribution over prefixes, not a
monotone classical counter trajectory.

### Integer-coordinate certificate, not a native integer dynamics claim

In the unnormalized symmetric basis b_j=sum_(|x|=j)|x>, the clock Gram is
G_clock=diag(C(M,j)) and the raw matrix has entries

    (J_raw)_(j+1,j)=j+1,    (J_raw)_(j,j+1)=M-j.              (5)

The identity C(M,j+1)(j+1)=C(M,j)(M-j) gives
J_raw* G_clock=G_clock J_raw. Gate-labelled raw blocks have the same integer
multipliers times G_j or G_j*. The square roots in (1) arise only from
orthonormalizing this stated positive Gram. This supplies an integer-weighted
certificate for the clock structure. It is not a claim that continuous-time
amplitudes are integers, that the Gram is physically selected, or that the
original native checkpoint law realizes these degrees of freedom.

## 3. A different, explicitly selected energy account

The following choice is NOT the spatial-square account of #1748. Its narrower
purpose is to fund the clock and the complete auxiliary record while retaining
exactly the specified accepted PHYSICAL reduced channel. No close-product
comparison of the entire history/battery state is claimed.

Choose a positive energy unit epsilon and the integer diagonal data account

    A = I_pulse + sum_(a=1)^P (I-|0><0|)_pentit_a
                    + sum_(b=1)^B |1><1|_bit_b,
    0 <= A <= R I,      R=1+P+B=983045.                       (6)

Object positions, object/pulse coins, carrier position, logical labels and
receiver messages are DEGENERATE in this account. This is an explicit new
energy choice, not the canonical kinetic/spectral energy, and not a claim
that Nature supplies these degeneracies. In particular it does not solve
identification of physical kinetic energy or the original energy-selection
obligations. References are identity factors.

Let C=sum_j j|j><j| and N=C+A on S=H_clock tensor H_D. Set

    Q=M+R=4259865.

Use battery levels n=0,...,Q, integer operator B_num, and prepare precisely
|Q>_battery. The initial full ready data has A=0, clock 0, so its total
N+B_num equals Q for EVERY logical/reference input. The battery is an energy
basis state, not a flat coherent superposition. Its initial energy is
Q epsilon and its dimension is Q+1=4259866. Preparation of this energized
basis state remains a resource; no physical preparation protocol is assumed.

### Bounded battery-level changes of each named gate

Each G_j changes A by at most one. A Fourier or loader transposition acts
on one counted pentit; a Boolean involution flips one counted bit; native
contact/transport changes only pulse presence in (6); object-only controlled
steps and diagonal phase gates preserve A. Padding is identity. Thus with
A's projections Pi_a,

    G_(j,delta)=sum_a Pi_(a+delta) G_j Pi_a,
    G_j=sum_(delta=-1)^1 G_(j,delta).                         (7)

These are matrix blocks, not energy measurements. Every term is inherited
from one declared gate. For gate supports on which (6) is additive, only the
energies of the acted-on factors enter delta; no projection on all other
registers needs to be physically measured.

Define finite downward shifts S_d|n>=|n-d> when 0<=n-d<=Q, and zero otherwise,
for d=0,1,2. Set

    E_j=sum_(delta=-1)^1 G_(j,delta) tensor S_(1+delta),
    K_f=sum_j h_j ( |j+1><j| tensor E_j
                         + |j><j+1| tensor E_j* ).           (8)

Each forward clock edge lowers the battery by 0, 1 or 2 levels; reverse edges
reverse the corresponding transfer. There are no arbitrarily large battery
jumps hidden in a named gate under this account. This is adjacency in battery
LEVEL, not a proof of physical spatial locality of a shared battery.

## 4. Full Hamiltonian, positivity and exact additive conservation

Put

    E_0=epsilon(N+B_num),
    H_tot=E_0 + kappa(K_f+M I),      kappa>0.                 (9)

This defines the generator on EVERY state, including every battery boundary
and every total-energy sector, not only on the prepared subspace. There is
no global projector switching the generator on at the selected total energy.
Finite shifts in (8) and their adjoints give its full boundary action.

### Candidate theorem 2: a positive finite generator and a full energy ledger

H_tot is Hermitian and nonnegative; [K_f,E_0]=[H_tot,E_0]=0. It generates
one time-independent unitary flow, exp(-it H_tot), on the complete finite
space. Every off-diagonal transition in (8) changes clock by +1, A by delta
and battery by -(1+delta), so its total account is unchanged, even at the
finite boundary. This proves the commutator directly.

To prove positivity, embed the battery in l2(Z). The corresponding E_j on
the bilateral ladder is a unitary: with T|n>=|n+1> and
D_A=sum_a Pi_a tensor T^a, it is

    (I tensor T^-1) D_A* (G_j tensor I) D_A.

The finite E_j is its compression to battery levels 0,...,Q, so ||E_j||<=1.
For a clock-decomposed vector xi=(xi_0,...,xi_M),

    |<xi,K_f xi>| <= 2 sum_j h_j ||xi_(j+1)|| ||xi_j||
                   <= M sum_j ||xi_j||^2,

using ||J_M||=M. Therefore -M I<=K_f<=M I and K_f+M I>=0.
The interaction term in (9) is explicitly included in the generator energy;
it is not omitted by calling E_0 a conserved quantity. Both E_0 and H_tot
are conserved. The bound is 0<=H_tot<=2 epsilon Q I+2 kappa M I.

For every state the exact account is

    Delta<E_battery>=-epsilon Delta<C+A>.                   (10)

The interaction mean is also conserved. On the initial clock-zero family it
is kappa M, since K_f has no diagonal clock block. The total initial mean is
therefore epsilon Q+kappa M, not just the stored battery energy.

The full prepared state is NOT stationary under H_tot merely because its
battery has sharp E_B. Its generator variance is exactly

    Var(H_tot)_initial = kappa^2 M.                         (10a)

Indeed E_0 is constant on the initialized sector, K_f has zero initial mean,
and its only initial clock transition has squared norm h_0^2=M. This is
coherence relative to the true generator carried by the localized clock and
its interaction, even though E_0 and E_B have definite initial values.
Preparing that state is a remaining resource. A stationary total input cannot
become this nonstationary state by a unitary commuting with H_tot, since such
a unitary preserves the commutator [rho,H_tot]=0. No claim of creating a
working clock from completely stationary free resources is made.

If g is a supplied maximum permitted clock-edge block strength, choosing

    kappa=2g/(M+1)

makes ||kappa h_j E_j||<=g. Then t_star=pi(M+1)/(4g). Completion time scales
with program length when this strength is fixed; no constant-time execution
of an arbitrarily large program is obtained. The value g and its units have
not been physically calibrated.

### Candidate theorem 3: exact full-sector execution

For 0<=q<=Q let P_q be the N projections. The map

    J_Q psi=sum_q P_q psi tensor |Q-q>                       (11)

is an isometry onto the entire total-energy-Q sector; every q is supported
by a battery level. Equations (7)-(8) give

    K_f J_Q=J_Q K,
    exp(-it H_tot) J_Q
       = exp[-it(epsilon Q+kappa M)] J_Q exp(-i kappa t K).   (12)

This proves exact complete-state dynamics ON THAT ENCODED SECTOR, for every
reference. The prescribed unencoded initial state is already J_Q(|0>psi_0),
because N(|0>psi_0)=0. In particular at t_star its output is, up to one global
phase, J_Q(|M>V psi_0). No coherent battery approximation is needed for (12).

However J_Q(|M>V psi_0) is generally not |M>V psi_0 tensor a fixed battery.
The battery stores correlations with clock and auxiliary-energy values. A
claim of equality to the predecessor's complete product output would be
false. Every rejected history remains in this unitary state. Partial traces
below are observational comparisons, not physical deletion of that history.

## 5. Exact accepted physical channel and a read window

Let H_phys denote the object, carrier position/bank/arrangement and logical
label, occupied receiver and passive reference. Let H_aux contain all loader,
filter and Boolean registers, including f. Write F=|1><1|_f. For the prepared
logical family, F V_j psi_0=0 if j<L. For j>=L it equals F V psi_0 and is
supported in the pulse arrangement selected by the final predicate. On this
accepted sector the account (6) equals 1+A_aux, with identity on H_phys.
It has no hidden dependence on the unknown logical messages or reference.

Define the unnormalized ideal accepted physical state

    sigma_acc=Tr_aux[ F V |psi_0><psi_0| V* F ].

For a mixed logical/reference input use its density matrix in the same
formula; all statements extend by linearity or purification. Put

    w(t)=sum_(j=L)^M C(M,j) sin(kappa t)^(2j)
                              cos(kappa t)^(2(M-j)).         (13)

### Candidate theorem 4: exact reduced-channel identity

For the actual funded continuous evolution from |0>psi_0|Q>,

    Tr_(clock,aux,battery)[ F rho(t) F ] = w(t) sigma_acc.    (14)

To prove (14), use (3) and (12). The clock trace removes different j terms.
All accepted prefixes have the same V. Within a fixed j, trace over an
orthonormal A_aux eigenbasis. Its battery label Q-j-1-a is independent of
the physical vector and the logical/reference labels. Attaching it changes
none of the surviving matrix elements on H_phys. This gives precisely (14).
The argument holds as an equality of linear maps on the complete logical
input operator algebra, including off-diagonal matrix units, so it preserves
all reference correlations, not only basis populations.

Thus, whenever w(t)>0, the normalized accepted PHYSICAL state is exactly the
ideal one. No inverse small-acceptance factor and no 5^22 coherent-battery
width are needed for this particular comparison. This is not an improvement
of #1748's stronger whole-state product norm claim under the same ledger:
the ledger, battery input and comparison channel have all been explicitly
changed. Interference tests involving the retained auxiliary histories can
distinguish the two complete states.

### Candidate corollary: an explicit high-weight read interval

For theta=kappa t in [pi/3,2pi/3], let p=sin^2 theta>=3/4. The algebraic
weights in (13) are those of a binomial expansion. If X denotes the formal
count in that expansion, then

    1-w(t)=Pr(X<L) <= 3^L E[3^-X]
             =3^L(1-p+p/3)^(2L) <= (3/4)^L=:delta_clock.    (15)

This auxiliary binomial notation proves a polynomial-weight inequality;
it assigns no law of actual physical occurrence. Since L>=400 and
(3/4)^4=81/256<1/2, delta_clock<2^-100<10^-30. The interval has nonzero width
pi/(3 kappa), rather than a single infinitely precise read time. At t_star,
w(t_star)=1 exactly.

The #1746 candidate gives the more explicit pre-threshold bound

    p_ideal > (2/5)(1024/15625)(99/50000) =: p_0,
    r_ideal < 50000/(99*2^29) < 1/10^6.                      (16)

Because (99/100)p_0>1/20000 and w(t)>99/100 throughout (15), equation (14)
conditionally transfers

    p_actual(t)>1/20000,      r_actual(t)=r_ideal<1/10^6      (17)

on that entire read interval, provided the #1746 source/filter proofs hold.
The band observable is evaluated on the same physical output, not on a new
finite-box spectral projector. The accepted logical channel remains exactly
the source/old-memory SWAP with arbitrary reference. For source label 1 the
receiver reads exactly d1 on this accepted physical state. All these weights
remain L1 Hilbert data, not measured frequencies or a terminal-event law.

## 6. Record retention after a mathematical accepted read

The preceding identity compares reads at different times of the unmeasured
experiment. It does not by itself give a joint law or the continuation after
conditioning. The following is a distinct, stated continuation contract.

At t_star the clock is exactly M. Apply the mathematical flag-1 projection
and normalize, if its weight is nonzero. Start the SAME H_tot from this
post-state. This defines a hypothetical instrument continuation, not an
occurrence mechanism or an already implemented external readout.

### Candidate theorem 5: finite continuous retention with an explicit bound

Assume source label 1. For every delay 0<=tau<=pi/(6 kappa), the wrong-receiver
weight after this conditional endpoint read satisfies

    Tr[(I-|d1><d1|) rho_post(tau)] <= (3/4)^L < 10^-30.      (18)

Proof: every post-state is in total-energy sector Q and at clock M. Pull it
back by J_Q. For an arbitrary endpoint data/reference vector phi, (2) gives
clock amplitudes for motion from M with data V_j V_M* phi. If j>=L, V_j=V_M,
so the data is unchanged. In particular the receiver stays d1 on this entire
clock portion. Dressing with J_Q acts trivially on receiver labels. If
r=sin^2(kappa tau)<=1/4, the number Y=M-j of downward moves has formal
binomial weights with parameter r. The bad portion j<L has Y>L and is bounded
by 3^-L E[3^Y]<=3^-L(1+2r)^(2L)<=(3/4)^L. The wrong-record projection
annihilates the good portion; orthogonal clock sectors eliminate its cross
terms. This proves the LINEAR bad-weight bound, including arbitrary retained
history/battery/reference correlations at the endpoint.

This is not exact permanent storage. A bounded continuous generator generally
has small nonzero long-distance clock amplitudes immediately. A strictly
one-way halt was not added. The unconditioned initially ready full-sector
state returns, up to global phase, after pi/kappa by the integer spectrum of
K. The later conditional evolution is governed by its specified projected
state, not falsely equated with a fresh preparation.

In this model prolonged storage is purchased by an identity tail and the
clock time/strength/capacity, not by increasing the source's native flight
horizon and suppressing its extreme-front weight. That changes the physical
control premise: the original native law is held off in the tail. It is not
a theorem that the original U_rec alone protects the record this long.

## 7. Locality, integer physics, and what is still open

Equations (8)-(9) are an explicit finite positive Hamiltonian, not a formal
logarithm of a black-box step. They are nearest-neighbour in the HISTORY
CLOCK, and each named forward gate changes the battery level by at most two.
No claim of bounded-range locality on the full physical spatial lattice is
made. A global controlled W, its control distribution, the common battery,
and position-predicate access still require an explicit spatial layout and
couplings. A small clock displacement and a small battery-level jump do not
prove those couplings physically local. The interaction energy and operator
norm are specified, but g, epsilon and the Hilbert-time parameter have no SI
calibration and no derivation from the original integer axiom or checkpoint U.

The chronological target is forward-only. The Hamiltonian deliberately has
adjoint reverse edges, so this result does not satisfy a stronger prohibition
on every microscopic adjoint coupling. The data and history evolve coherently;
no collapse or stochastic event is generated merely by their correlations.

Finite capacity includes all auxiliary registers, the clock, the finite data
box, and the Q+1 battery levels. There is no discarded bath, implicit infinite
energy reference, freely renewed source, complete reset, or unlimited archive.
The initial charged basis state is simpler mathematically than a prescribed
large coherent superposition; its physical preparation and deployment remain
open. The inverse flow restores information but is not a record-preserving
reset. The accepted subchannel identity is on the stated prepared family;
arbitrary dirty or energy-superposed data inputs have not been assigned it.

A future spatial compilation can replace each G_j by a local subword and
apply the general clock theorem with its new, fully counted L. That is an
available construction route, not a claim that such a compilation has already
been supplied. No present scientific owner or public Canon status closes here.

## 8. Prior art, falsification and evidence

Perfect-transfer chains with fixed nonuniform couplings are established,
for example Christandl, Datta, Ekert and Landahl, *Perfect state transfer in
quantum spin networks*, quant-ph/0309131, Phys. Rev. Lett. 92, 187902 (2004).
History-labelled circuit Hamiltonians are also established; see Breuckmann
and Terhal, *Space-Time Circuit-to-Hamiltonian Construction and Its
Applications*, arXiv:1311.6101. The self-contained symmetric-tensor proof above
supplies every clock identity used here; neither citation is an unverified
import of a new TWIST-J theorem or a claim that these methods originated here.

The exact small audit, pinned before its first run, checks integer Gram and
mirror identities, labelled clock conjugacy, finite energy-edge commutators,
sector intertwining, reduced-channel matrix units, and the displayed rational
count/weight certificates. It does NOT simulate all 1,638,410 gates, compile
physical locality, prove #1746's pending source/spectral results, or establish
independent scientific acceptance. Theorems here rely on their analytical
proofs and stated assumptions, not extrapolation from that finite audit.

Decisive falsifiers are: a failure of (2) or (3); an admitted boundary
transition violating energy conservation or positivity; a failure of (12);
a ready prefix with a premature nonzero final flag; an accepted physical
energy dependence invalidating (14); or violation of (15)/(18) under the
specified continuation. Changing to the spatial-square ledger without a new
channel proof, removing reverse edges, or claiming a product full-state output
would violate the contract rather than extend the theorem.
