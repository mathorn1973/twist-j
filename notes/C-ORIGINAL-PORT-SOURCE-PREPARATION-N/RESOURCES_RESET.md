# Preparation resources, occupied data and reset boundaries

**NON-CANONICAL, L1. Conditional analytical candidate-T; independent
acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.

This note separates finite thermal preparation of auxiliary registers
from preparation of the original spatial source. Its gates are explicit
conditional implementation assumptions. They are not derived from the
six-pentit transition, and no scientific program or expanded circuit has
been executed. The source target and its exact contrast are those of
[#1775](https://github.com/mathorn1973/twist-j/issues/1775), including the
[declared active-source supplement](https://github.com/mathorn1973/twist-j/issues/1775#issuecomment-6399077081).

## 1. The original source and a stationary-preparation obstruction

Keep the original complete U_rec and its nominated energy

    Q=E0 f(U_rec),    E0>0,    exp(-iQ/E0)=U_rec.

Identities on an arbitrary passive reference are implicit. On the source
space without the old receiver/reference, write

    chi_s=alpha_(97,0),    d_s=(U^2-U^(-2))chi_s,
    <chi_s,d_s>=0,
    Z=(39521+154 sqrt(5))/15625,
    ||d_s||^2=Z-1,    psi_±=(chi_s±d_s)/sqrt(Z).       (R1)

Here U=U0 C is the unchanged uncalibrated source step. Both target
supports lie to the left of the receiver. With any admitted old state
on K tensor R, K=span(d1,...,d25), let rho_+ denote the complete positive
setting's target density. Its initial receiver write probability is zero.
The source proof gives, after three forward macrosteps,

    p_+ - p_- = Delta_p > 1/50,    p_- >=0.           (R2)

This includes mixed old data and arbitrary reference correlations.

**Proposition 1.** Every normal state sigma satisfying
U_rec sigma U_rec*=sigma obeys

    D(rho_+,sigma)>=p_+/2>1/100,                     (R3)

where D is trace distance, one half the trace norm. In particular this
holds when sigma commutes with the same original Q.

**Proof.** Put q=Tr(P_W sigma), with P_W the original receiver projector
onto d0, and delta=D(rho_+,sigma). Comparing the initial receiver
probabilities gives q<=delta. Invariance and unitary invariance of trace
distance give D(U_rec^3 rho_+ U_rec^(-3),sigma)=delta, so
|p_+-q|<=delta. Thus p_+<=2delta. Equation (R2) proves (R3). No separate
evaluation of p_+, spectral-equality assertion or pure-state hypothesis
is needed. QED.

The obstruction uses the ORIGINAL Q-bearing source and receiver. It does
not apply to a different zero-energy dictionary merely because its
decoded channel agrees with the original memory channel. In particular,
it does not undo the differently typed funded decoder of
[#1774](https://github.com/mathorn1973/twist-j/pull/1774).

### 1.1 A quantitative asymmetry resource requirement

Let Lambda be a trace-preserving preparation channel covariant under the
input and output energy time translations. For example, an energy-conserving
joint unitary followed by a partial trace gives such a channel. Every
stationary comparison input omega then has stationary output Lambda(omega).
If its actual input tau produces a state within delta_prep of rho_+,
contractivity and the triangle inequality give, for every such omega,

    D(tau,omega)>=D(Lambda(tau),Lambda(omega))
       >=p_+/2-delta_prep>1/100-delta_prep.           (R4)

Taking the infimum over available stationary comparison inputs gives
the corresponding distance-to-stationarity lower bound. No existence
of a normalized Gibbs state of the infinite original source is assumed.
At delta_prep<=1/1000, the required input distance is strictly greater
than 9/1000. This is a quantitative asymmetry statement, not an energy
in joules, a work lower bound or a claimed amount necessarily lost by
one particular resource subsystem.

A sharp battery energy eigenstate is stationary. Independent Gibbs
ancillas at one or several temperatures are stationary under their
declared bare sums. If the ENTIRE input is stationary under the original
source energy plus these resource energies, an exactly conserving
preparation cannot meet delta_prep<=1/1000. A covariant success branch
also maps a stationary input to a stationary unnormalized output, so
normalizing a nonzero such branch does not evade (R3). An asymmetric
measurement or control would instead be another resource.

This statement does not cover an arbitrary Gibbs state of an interacting
Hamiltonian that fails to commute with the nominated bare sum. Nor does
it cover an already asymmetric localized source seed. The specified
original basis seed

    u2=|R=97,r=0,e2; y=97,t0>

is an input resource, not an output of the zero-energy reset construction
below. Indeed the one-step object stream has zero overlap with that
initial coordinate/coin port, so <u2,Uu2>=0. With any fixed admitted pure
old-memory/reference state, its calibrated complete seed is not a Q
eigenvector and its pure density is not stationary. Its localization,
coin state and associated Q asymmetry must not be called a free Gibbs
ready state.

## 2. Complete thermal reset of zero-energy helpers

Let T be one zero-energy helper qubit, with ready state 0 and bad state 1.
For every use supply a fresh hot qubit H and cold qubit C, each with gap
d_h>0. Their independent Gibbs excitation probabilities are

    p=1/(1+exp(beta_h d_h))=1/3,
    gamma=1/(1+exp(beta_c d_h)),    0<gamma<1/2.       (R5)

Thus beta_h d_h=ln 2. The helper may be dirty and correlated with a
reference R; only the fresh donor pair is initially independent of it.

Define the full eight-dimensional Hermitian unitary S by

    |1,0,1>_(H,C,T) <-> |0,1,0>_(H,C,T),             (R6)

with identity on the other six basis states. Both exchanged vectors
have donor energy d_h. Hence S commutes with d_h(n_H+n_C), including
all dirty and complementary sectors. No initialized control is hidden
in this primitive. Conditional on admitting its interaction, the positive
pulse Hamiltonian lambda(I-S), lambda>0, realizes S in time
pi hbar/(2lambda) in the interaction picture. The commuting bare evolution
does not change this reduced readiness channel for the diagonal Gibbs
donors. Its timing/switching or autonomous implementation is
an additional controller contract, not an extra pure timer supplied here.

**Proposition 2.** After tracing the donor pair for the purpose of a
reduced-channel statement, the exact helper/reference channel is

    (Phi tensor id_R)(rho_TR)
      =ell rho_TR+a |0><0| tensor rho_R
                   +b |1><1| tensor rho_R,
    a=p(1-gamma),    b=(1-p)gamma,    ell=1-a-b.       (R7)

**Proof.** For donor input 10, the two target basis states are sent to
target 0 and orthogonal donor states 10 and 01. This is replacement by
0 after tracing the donors, including off-diagonal target/reference
terms. Donor input 01 gives replacement by 1. Inputs 00 and 11 leave
the target unchanged. Their probabilities give (R7). The changed donors
are still physical parts of the apparatus. QED.

With tau_*=(a|0><0|+b|1><1|)/(a+b), fresh independent repetitions give

    Phi^r=ell^r id+(1-ell^r) R_(tau_*),
    ell=(2-gamma)/3<=2/3,
    b/(a+b)=2gamma/(1+gamma)<=2gamma.                (R8)

The replacement-channel identity R_(tau_*)^2=R_(tau_*) proves the first
formula. Consequently, for every dirty rho_TR,

    D((Phi^r tensor id_R)(rho_TR), |0><0| tensor rho_R)
       <=ell^r+(1-ell^r)b/(a+b)
       <=(2/3)^r+2gamma.                             (R9)

This is uniform over reference dimension. Applying the channels to M
helpers, with fresh pairs for every helper and repetition, and telescoping
against ideal replacement gives

    epsilon_reg<=M[(2/3)^r+2gamma].                 (R10)

There are exactly Mr hot donors and Mr cold donors, hence 2Mr physical
donor qubits. None is reused by this bound. They and their correlations
must remain available as spent resources; reducing the channel is not
physical deletion of those states.

### 2.1 Explicit temperatures, digits and energy ledger

For any chosen 0<epsilon<1, a sufficient finite prescription is

    r=2 ceil(log2(2M/epsilon)),
    beta_c d_h>=ln(4M/epsilon).                      (R11)

Indeed (2/3)^r<(1/2)^(r/2)<=epsilon/(2M), while
gamma<exp(-beta_c d_h)<=epsilon/(4M). Equations (R10)-(R11) give
epsilon_reg<epsilon. For the useful allocation epsilon=1/4000,

    r=2 ceil(log2(8000M)),
    beta_c d_h>=ln(16000M).                          (R12)

Every thermal helper initially has I/2, not a pure zero-energy state.
For such a target, its exact bad population after r rounds is

    x_r=x_*+(1/2-x_*)ell^r,
    x_*=2gamma/(1+gamma).                            (R13)

For independent identical thermal helpers, their reduced state is a
product of these diagonal states and its exact distance from |0^M> is
1-(1-x_r)^M. The more conservative (R10) also allows arbitrary initially
correlated dirty helpers.

Initially the donor bank has mean energy Mr d_h(p+gamma). Its entropy,
in units with Boltzmann's constant one, is
Mr[h(p)+h(gamma)], with h(x)=-x ln x-(1-x)ln(1-x). The M thermal
helpers contribute M ln 2. Every reset conserves the donor energy sum.
For a target with initial bad population x_0, the total hot donor energy
change over its r rounds is -d_h(x_0-x_r), and the cold donor change is
+d_h(x_0-x_r). These follow directly from the exchanged occupations in
(R6). Entropy and old target information reside in the changed donors
and correlations. The donor bank is not restored merely because the
helper is nearly ready.

Finite positive-temperature inputs have nonzero errors. More generally,
a unitary on a finite full-rank total input leaves it full rank, and
each reduced density remains full rank. Such an input cannot yield an
exact pure helper by unitary evolution and partial trace alone. The
construction above claims finite accuracy, not exact thermal purity.

## 3. Reduced-reference error versus full donor decoupling

In (R9)-(R10), R can contain the unknown old memory and every passive
reference, but it does not include the spent donors that have just been
traced. If those donors are untouched during the subsequent source
circuit, contractivity propagates the linear error epsilon_reg to the
retained source/helper/old-memory/reference output. There is no need to
claim that the donors are exactly decoupled.

A generic comparison of the ENTIRE post-reset joint state needs a
different statement. Let tau_TB include all M targets and all other
systems, including the donors. Suppose its probability of the joint
ready projector P=|0^M><0^M| tensor I_B is at least 1-epsilon_reg. Then

    D(tau_TB, |0^M><0^M| tensor tau_B)
       <=sqrt(epsilon_reg)+epsilon_reg.             (R14)

To prove this, let p=Tr(P tau), and let tau_B^0 be the normalized ready
conditional state. Projection of a purification has overlap sqrt(p),
so D(tau,|0^M><0^M| tensor tau_B^0)<=sqrt(1-p). Tracing the targets
kills their ready/nonready cross terms, giving
tau_B=p tau_B^0+(1-p)tau_B^1. Thus
D(tau_B^0,tau_B)<=1-p. The triangle inequality proves (R14).

The comparison rest state in (R14) is the actual changed tau_B, not the
original donor product. A linear reduced-reference bound must not be
silently substituted for this general global decoupling bound. In the
special completely diagonal thermal input and permutation-only cooling
panel, direct classical decomposition gives the stronger global bound
D(tau_TB,|0^M><0^M| tensor tau_B)=1-p. Formula (R14) remains the safe
statement for arbitrary dirty/reference-correlated input.

## 4. Applying the helper budget to the proposed source circuit

The circuit's core auxiliary readiness consists of three helper bits.
Let c_set be one when a locally prepared classical setting bit is also
required, and zero when the setting is hard-coded or supplied as admitted
information. With M_bus further ready routing or workspace bits, put

    M=3+c_set+M_bus.                                 (R15)

A supplied coherent setting is an information input and must not be
reset. Its physical qubit still belongs to the apparatus inventory when
c_set=0. A hard-coded setting does not eliminate the couplings/control
that implement it. Any additional detector, latch or controller ready
bits must be added explicitly; (R15) does not count an unspecified clock.

For a known classical setting, cooling prepares 0 to the bound above;
the negative setting can use a separately counted X on that zero-energy
bit. No pure helper input has been assumed. Conversely, neither cooling
nor this X prepares the original u2 seed, supplies a Q phase reference,
or certifies the source gates' physical precision.

Condition on the companion ideal source circuit having the complete
three-helper contract: from u2, ready helpers and the declared setting,
it prepares the specified original psi_±, returns those helpers to their
ready state, and acts as identity on the arbitrary old memory/reference.
For a deterministic circuit of that type, if the seed error is
delta_seed and the complete implemented circuit's half-diamond error is
epsilon_gate, the retained preparation error obeys

    delta_prep<=delta_seed+epsilon_reg+epsilon_gate.  (R16)

All three bounds must hold on the declared joint input domain. For
example, allocating at most 1/4000 to each leaves room below 1/1000
for one further explicitly specified error budget. Equation (R16) does
not establish delta_seed or epsilon_gate: these are the remaining
original-source preparation and implementation obligations. Approximate
elementary gate errors may be summed by a standard channel telescoping
bound; their admissibility and precision require a concrete gate list.
Here delta_seed is a joint comparison with u2 and the declared setting,
old-memory and reference state, not merely a source-marginal comparison.

If instead a preparation retains a success flag with ideal probability
p0>0, a complete-instrument error epsilon gives actual probability at
least p0-epsilon and conditional trace error at most epsilon/p0, provided
epsilon<p0. For completeness, write A,B for its actual and ideal success
substates, with traces p,p0. The complete flag instrument bounds
(||A-B||_1+|p-p0|)/2 by epsilon. Multiplying the normalized-state
comparison by p0 and using the triangle inequality proves the stated
bound. The rejected branch and physical flag/detector must be retained
in the resource account. A mathematical conditional state is not itself
a supplied occurrence or storage mechanism.

## 5. The setting cannot be erased without a record

Equation (R1) gives the exact nonzero overlap

    s=<psi_+,psi_->=(2-Z)/Z,    2<Z<3,
    -1/3<s<0.                                       (R17)

Suppose an exact unitary takes two orthogonal setting inputs and the
same pure ready seed/environment to the pure sources psi_±, while
resetting the setting register to one common state. For fixed pure old data and
reference, the output must have the form

    |setting0> |psi_±> |g_±>.

Preservation of the initial zero overlap requires
0=s<g_+,g_->. Because s is nonzero, g_+ and g_- are orthogonal. The
setting information has moved to a distinguishable physical record;
it has not disappeared. For N independent settings with product source
outputs and a reset common controller, every pair of source words has
nonzero overlap, a product of factors s. Their garbage states must all
be mutually orthogonal, requiring at least 2^N distinguishable states.
This is an exact dimension bound under the stated fixed-ready isometric
contract, not a numerical heat cost or an approximate compression bound.

The common-loader phase selector of #1775 is F=I-2P_src and satisfies
F psi_+=-psi_-. A coherent controlled application therefore gives

    (alpha|0>+beta|1>)|psi_+>
       ->alpha|0>|psi_+>-beta|1>|psi_->.             (R18)

The minus is immaterial for each separate classical setting. It is a
relative phase for a coherent selector. One must retain (R18) as the
declared joint isometry, or explicitly count a Z on the setting qubit
to obtain the convention with a plus sign in both terms. Tracing the
setting instead removes its off-diagonal coherence. Neither operation
is an unannounced coherent setting erasure.

## 6. The 25-state memory contract and a counted extension

At its completed endpoint the source circuit leaves the unknown
receiver/reference untouched; intermediate controlled spatial steps may
interact with it and later restore it.
The admitted receiver input K=d0-perpendicular is supplied information,
not a register to be cooled. A receiver-only effect F with zero response
on all unchanged old states and unit response on d0 must satisfy
K subset ker F and Fd0=d0. Positivity and self-adjointness imply
K perpendicular d0 and dim K<=25. Thus an arbitrary full 26-state input
cannot be silently called flag-ready.

As a purely information-theoretic extension, one additional ready qubit
E suffices to encode full 26-state old data into K tensor E without
losing any reference information. Use the full unitary exchanging

    |d0,0>_(D,E) <-> |d1,1>_(D,E),                   (R19)

with identity on its complement. On input E=0, d0 goes to d1 with E=1,
while d_j, j>=1, remains d_j with E=0. The receiver is now in K, and
the complete 26-state input is stored isometrically in D,E. With an
epsilon-ready E, the complete-channel error is at most epsilon by
contractivity, and E must be added to M when it is thermally prepared.

This extension changes the resource contract: E carries old information
and correlations and cannot simply be reset afterward. Its dimension
bound is minimal, since 26 orthogonal inputs cannot fit into a 25-state
receiver alone. Equation (R19) is not asserted to conserve the original
nonfactorizing Q or to be a native gate. Its energetic funding and actual
local implementation would need a separate proof. No such extension is
silently inserted into the current K-input experiment.

## 7. Clean auxiliaries do not make a closed reusable source

The source-preparation circuit's ideal helper return is valuable: those
specific helpers need not store the prepared source. It does not restore
the consumed u2 seed, the changed donor pairs, an erased setting record,
or a timing/detection controller. Inverting the complete preparation
before export also undoes the prepared source. Keeping the output while
renewing the apparatus requires separately counted storage, new inputs
or a demonstrated reset process.

There is also an exact general obstruction to restoring every resource
uncorrelated. Suppose the product of an initially stationary source
sigma_S and a resource tau_B undergoes an energy-conserving unitary and
produces exactly rho_S tensor tau_B, with all other resources included in B. Let F denote
root fidelity. Time-translation covariance, unitary invariance and
multiplicativity give, for every real t,

    F(tau_B,tau_B(t))
       =F(rho_S,rho_S(t)) F(tau_B,tau_B(t)).          (R20)

The resource fidelity is continuous and positive near t=0. Therefore
F(rho_S,rho_S(t))=1 there, making rho_S stationary, contrary to the
desired original source. This proof concerns exact continuous energy
covariance and exact uncorrelated restoration. It does not exclude
approximate catalysts, changed resource correlations or an already
asymmetric seed; those must retain their actual errors and resources.

The conclusions are therefore conditional and finite: all zero-energy
helper readiness can be purchased to an explicit accuracy with counted
thermal donors under (R6), while the original-source asymmetry, concrete
gate law, controller, output instrument and renewal remain separate
obligations. No all-temperature no-go, autonomous stopping, permanent
record or independently accepted source realization is claimed.
