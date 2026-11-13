# Sharp finite-environment loading capacity and a guarded two-pair source

**NON-CANONICAL, L1. Authored analytical candidate-T; independent acceptance pending.**
The assembly claims are conditional on the specified source/history construction
of PR #1758 at `243379459e3c7493368473cbae1a17eb99ee8316`. The finite-dimensional
capacity theorem and reaction identities below are self-contained. They do not
certify that candidate's inherited capture proofs or promote any Canon claim.
Public reservation: issue #1760. Author: A. M. Thorn. License: Apache-2.0.

## 1. Frozen question, complete carrier and equality

Let one environment pair consist of a hot qubit of energy 3 epsilon and a cold
qubit of energy epsilon, epsilon>0, in the specified diagonal product state

    tau_h=diag(2/3,1/3),  tau_c=diag(4/5,1/5).

For N independent pairs put R_N=(tau_h tensor tau_c)^tensor N. The environment
Hamiltonian is epsilon E_N, E_N=sum_i(3 n_hi+n_ci). Add only the source s and
initial cursor t, both of gap epsilon and initially |00>. The desired loaded
state of these TWO registers is |11>, not merely an occupied source.

For the optimization class allow every total unitary V on these 2N+2 qubits
satisfying [V,E_N+n_s+n_t]=0. There is no additional changed workspace, bath,
energy store, auxiliary degeneracy, or postselection in this class. Other data
and reference are tensor spectators. The success functional is the ordinary
L1 squared-norm/trace weight

    q(V)=Tr[(I_env tensor |11><11|) V(R_N tensor |00><00|)V*].       (1)

Its use defines no empirical occurrence law or single realized event.
An unchanged pure spectator does not enlarge the class. A changed archive or
a variable-energy data reservoir DOES enlarge it and invalidates its optimality
claim. The subsequent history construction adds explicitly specified empty
hardware; its dynamic success weight is proved separately, not inferred solely
from this abstract optimization.

## 2. A sharp energy-sector capacity formula

Let d_N(E) be the coefficient of x^E in

    (1+x)^N(1+x^3)^N,

and set it to zero outside 0<=E<=4N. In shell E, list the d_N(E) positive
input eigenvalues of R_N in nonincreasing order as lambda_(E,k). Then

    q_N^max = sum_E sum_(k=1)^min(d_N(E),d_N(E-2)) lambda_(E,k).    (2)

### Proof, including achievability on the complete space

In total-energy shell E the input support consists of d_N(E) environment
vectors with source/cursor 00. Its density operator has the listed positive
eigenvalues and zeros on the rest of the full shell. The target projector has
rank d_N(E-2), because its source/cursor contribution is two.

For a rank-r projector P and a positive operator with descending eigenvalues
lambda_i, write Tr(P rho)=sum_i lambda_i p_i in an eigenbasis, where
0<=p_i<=1 and sum_i p_i=r. This expression is at most the sum of the largest
r eigenvalues: transferring available weight from a lower lambda to a higher
lambda cannot decrease it. Energy conservation restricts V to each shell,
so this bounds (1) by (2), without a classicality assumption on V.

For achievability, in each shell select the corresponding largest input basis
weights and inject their basis labels into distinct target bath labels at
energy E-2. Swap each |u,00> with its assigned |v,11>. These are disjoint
pairs: all input words have source/cursor 00, all output words have 11, and
within each side the labels are distinct. Leave every remaining full basis
state fixed, including the 01 and 10 source/cursor states. The resulting
permutation is an involution, is unitary on ALL states, preserves energy, and
attains (2). No failed input has been deleted. This also constructs the
inverse. The statement is about endpoint unitaries, not their local runtime.

### Exact evaluation without enumerating 4^N configurations

An environment word with a hot and b cold excitations has

    E=3a+b,  multiplicity C(N,a) C(N,b),
    individual weight = 2^(3N-a-2b)/15^N.                         (3)

At fixed E the numerator is 2^(3N-2E+5a), so larger a is higher weight.
Allocate d_N(E-2) output slots to these groups in decreasing a order, stopping
at d_N(E) input states. This gives (2) using integer binomial coefficients and
powers only. A declared finite table N=1,...,32 is an exact audit witness,
not an inferred all-N asymptotic statement. Ignoring the last pair proves
q_(N+1)^max>=q_N^max. The full-rank ground component also proves q_N^max<1
for every finite N. In fact the E=0 and E=1 components cannot load and give

    q_N^max <= 1 - [2^(3N)+N 2^(3N-2)]/15^N,  N>=1.              (4)

This bound is not generally sharp.

## 3. One pair is optimal at 4/15; two pairs attain 7/15

For N=1 the bath energies are 0,1,3,4, each nondegenerate, and only E=3 has
an available target E-2=1. Thus q_1^max=4/15. The source reaction of #1758
attains this narrow-class bound. It is not a universal bound on other baths,
other ready preparations, changed workspace, or other energy ledgers.

For N=2, order the bath bits h1,c1,h2,c2. The following ten resonant pairs
specify one maximizing injection f. Append 00 on every left side and 11 on
every right side for the actual source/cursor transition.

| Input bath u | Output bath f(u) | Input E | Input weight numerator /225 |
|---|---|---:|---:|
| 0101 | 0000 | 2 | 4 |
| 0010 | 0001 | 3 | 32 |
| 1000 | 0100 | 3 | 32 |
| 0011 | 0101 | 4 | 8 |
| 0111 | 0010 | 5 | 2 |
| 1101 | 1000 | 5 | 2 |
| 1010 | 0011 | 6 | 16 |
| 1011 | 0111 | 7 | 4 |
| 1110 | 1101 | 7 | 4 |
| 1111 | 1010 | 8 | 1 |

The bath multiplicities for E=0,...,8 are (1,2,1,2,4,2,1,2,1). The allocated
slot counts for E=2,...,8 are (1,2,1,2,1,2,1), and states tied in a group
have equal weight. Therefore the sector contributions are

    (4,64,8,4,16,8,1)/225,
    q_2^max=105/225=7/15.                                       (5)

The six unselected bath words are 0000,0001,0100,0110,1001,1100. Their
numerators are (64,16,16,8,8,8), summing to 120. Every one remains present.
There is no sorting outcome or classical lookup performed on an unknown bath:
the table specifies one fixed coherent operator on the entire space.

Let S denote the ten input bath words. Define on the six reaction qubits

    B_2=sum_(u in S) |f(u),11><u,00|,
    P_in=B_2* B_2,  P_out=B_2 B_2*.

Its input and output supports are orthogonal and it is a partial isometry.
P_in+P_out-B_2-B_2* is positive with spectrum contained in {0,2}, and it
commutes with the six-qubit bare energy. Its exponential at the appropriate
half-period realizes the disjoint swaps, up to bare-energy phases. This
standalone endpoint observation is not yet the autonomous loader construction.

## 4. A real composition trap and its local repair

Direct substitution of B_2 for the old input reaction is WRONG. Once the
source excitation moves into the main cursor, the local source and t0 are
again 00. Some output bath words belong to S. For example

    0011 -> 0101,  and 0101 -> 0000.

On a later main history generated from bath 0011, the unguarded reaction can
therefore consume the spent 0101 bath and create a second source/t0 pair while
the first loader and main cursor are still occupied. Energy is conserved but
the intended one-history path is not. This is an exact failed route, not a
numerical near miss or a falsification of the original one-pair construction.

Use the EXISTING final loader occupation n_ell, ell=t_(L-1), as a guard:

    C_ell=I-n_ell,
    X_0=C_ell B_2,
    D_0=C_ell(P_in+P_out),
    Q_0=C_ell P_in.                                             (6)

The guard commutes with the six-qubit reaction. It is empty at launch, becomes
occupied before handoff, and remains occupied during the main program. It
adds no register, initialized excitation, clock, measurement, or external
switch. Use (6) both in the reaction edge and its input-node potential.
Guarding the hopping alone would not reproduce the intended diagonal energy.

Every other edge X_i,D_i and vertex Q_j of #1758 HAMILTONIAN.md (H8)-(H12)
remains unchanged. In particular, the last loader hop is still controlled by
n_s and the first main hop by n_ell. Reverse main motion first restores s;
reverse loading then clears ell; the reverse reaction is consequently
available at the correct endpoint. Hermitian reverse transitions are retained.

### Full raw-space Hamiltonian, local bounds

Retain K=4L, all old data labels G_j, and

    a_i=g sqrt((i+1)(K-i))/(K+1),  v_j=g-a_(j-1)-a_j>=0.

Use the positive edge form a_i(D_i-X_i-X_i*) and positive v_j Q_j, with
(6) at i=0. Now H_0 includes two hot and two cold qubits. Define H=H_0+H_prop
exactly as in the parent. The changed reaction is a guarded direct sum of
positive two-state blocks. All unchanged raw blocks have the parent's proof.
Thus H>=0 on all states, [H_0,H_prop]=0, and H generates a total reversible
unitary flow. No off-path sector is removed. The interaction is part of H,
not an omitted external work cost.

Place the extra h2,c2 at (-3,0),(-3,-1), using the parent's source-relative
coordinates. Keep h1=(-2,0), c1=(-2,-1), s=(0,0), t0=(-1,-1), ell=(0,-1).
All seven reaction/control sites lie within Manhattan radius three of h1.
The extra sites are outside the parent's two loader columns and main/data
layout. The largest existing support/radius bounds stay at seven qubits and
radius four. The changed reaction and Q0 add two participations to ell;
it otherwise participates in its bare term, last loader edge, first main
edge and v_L Q_L, so its term valence is six. Other old counts do not grow;
each new environment qubit participates in its bare term, reaction and Q0.
The maximum term valence consequently remains six under the parent's grouping
of positive terms. No two-body decomposition of this seven-qubit primitive
is asserted. The new physical qubit count is N_data+4L+7, two above the parent.

## 5. Ten independent active paths and exact channel composition

For u in S define physical history states nu_(u,j):

- j=0: bath u, empty source, empty loader and main cursor;
- 1<=j<=L: bath f(u), source occupied, loader at t_(j-1), main empty;
- j=L+r, 1<=r<=3L: bath f(u), source empty, loader at ell, main at c_r.

Bath output labels f(u) are distinct. Histories with different j are also
orthogonal. At j=0 only the reaction acts; at loading vertices only the
adjacent loader/hand-off edges act; at main vertices the guard (6) forbids
relaunch. The inverse maps have the same properties. Every Q_j selects
exactly its vertex on each path. Each path is therefore an invariant copy
of the parent's constant-diagonal perfect-transfer history, with the SAME
data prefix F_j and edge coefficients, but bare energy epsilon(D+E(u)).
All six unselected initial bath words give stationary failure components.

For each active word the history amplitudes, apart from its common energy
phase, are

    b_j(t)=sqrt(C(K,j)) (i sin theta)^j (cos theta)^(K-j),
    theta=gt/[hbar(K+1)].                                      (7)

The bath is initially diagonal, so the different bare energies do not add
coherent cross terms between these components. The complete input and
output retain all sixteen initial bath components. There is only one actual
source and one loader/main apparatus, not ten copies of the apparatus.

The parent's loading window and comparison proof apply separately to every
active component. With p=sin^2(theta) in [1/16,1/8], bad loading weight is
at most delta_load<2(5/6)^L. The active mixture's full-state trace distance
to the loaded-source/unchanged-data/interior-loader comparison is at most
sqrt(delta_load); the complete mixture distance is at most
q_2 sqrt(delta_load). There is an additional spent-bath mixture, but its
weights and phases do not depend on the logical data/reference. The parent
L>=1024 implies the same <10^-30 loading error as its analytic proof.

Let S_ideal be the inherited unnormalized accepted physical/reference map
of the completed logical word, and let w_out(t) be the parent's binomial
completed-tail weight. Orthogonal bath/history labels, the common prefixes,
and unchanged decoding prove as an equality of maps on logical operators

    S_actual(t) = (7/15) w_out(t) S_ideal.                       (8)

Partial traces here are mathematical comparisons, not physical deletion.
All rejected histories remain in the unitary full state. Conditional on the
inherited source/filter proof, on the parent's read interval

    p_read(t)>7/300000,     r_outside<1/1000000.                 (9)

This uses w_out p_ideal>1/20000, not an assertion of physical click rates.
The former whole-input lower bound 1/75000=4/300000 has improved by the factor
7/4 in this DIFFERENT environment/reaction model. The parent's parameters and
thresholds are untouched. The normalized accepted physical map and old-memory/
reference SWAP are unchanged. Its stated conditional endpoint-retention
proof also applies path by path; no permanent memory or new event rule follows.

The upper limit (5) is NOT a claim that the inherited read weight or the full
machine is globally optimal. Nor does it optimize protocols that use extra
changed registers or replace the fixed target by a larger output subspace.

## 6. Complete energy, nonstationarity and the price of the improvement

For the four bath qubits, independence gives

    <E_env/epsilon>=12/5,   Var(E_env)=108 epsilon^2/25.

The selected table gives

    q_2=7/15,
    <(E_env/epsilon) P_in> = 412/225,
    Cov(E_env,H_prop) = (32/45) epsilon g.

Each active input has propagation mean g and variance a_0^2. Each inactive
input has propagation energy zero. Thus the complete conserved moments are

    <H> = epsilon(D+12/5)+(7/15)g,                              (10)
    Var(H) = (108/25)epsilon^2+(64/45)epsilon g
             +(56/225)g^2+(7/15)a_0^2.                        (11)

D still counts the original ready data/fuel/work and latch. Its acquisition
is not funded by this bath merely because it has been included in the mean.
Each successful path shifts the bath bare energy down by exactly two, so at
the exact endpoint its mean is 22 epsilon/15. The positive input partition

    H_in=E_env+a_0(D_0-X_0-X_0*)+v_0 Q_0

has mean 12 epsilon/5+7g/15 initially and 22 epsilon/15 at the endpoint.
The reaction is then off and all its diagonal projectors vanish on reached
states. The remainder gains exactly

    Delta<E_rem> = 14 epsilon/15+7g/15.                         (12)

Relative to the original input partition, the improvement costs an additional
6 epsilon/5+g/5 in initial mean. It is not a free efficiency improvement or
a claim about minimum manufacturing work. Environment depletion, correlations
and the initial pure hardware are retained. An attempted cyclic restoration
of the original environment while leaving the entire remaining closed state
and its energy unchanged cannot obey the same additive energy conservation:
the bath alone would have to regain 14 epsilon/15. This is a restricted
restoration statement, not an impossibility theorem for engines with supplied
fresh resources and separately accounted output storage.

Initially [H_0,rho_in]=0 but, on orthogonal active paths,

    ||[H,rho_in]||_1 = 2 q_2 a_0 = (14/15)a_0>0.               (13)

Thus there is still a prepared full-H nonstationarity. No moving clock has
been obtained from a Gibbs state of the same full Hamiltonian. The diagonal
thermal weights are state data, not a proof of empirical occurrence.

## 7. Robustness and equality boundaries

The launch mechanism is input-independent on the logical messages because
all bath/source controls tensor identity on those data during loading. With
a different bath density operator independent of the data, the accepted map
(8) still has prefactor Tr(P_S rho_env), where P_S=sum_(u in S)|u><u|.
For coherent bath inputs, off-diagonal bath terms vanish in this accepted
physical reduction because the output labels f(u) are distinct. Global bath/
clock coherences are not claimed unchanged or absent.

If the bath is correlated with the logical/reference input, the correct
replacement is S_ideal applied to the subnormalized data operator

    rho_D^S = sum_(u in S) <u|rho_env,D|u>,

rather than q S_ideal(rho_D). Independence, or the weaker exact condition
rho_D^S=q rho_D, is necessary for the advertised unchanged data map in
that generalization. Local thermal marginals alone do not supply it.

Already for one pair, fixing only excited marginals 1/3 and 1/5 permits
joint occupation t=p11 in [0,1/5]. Its actual old-reaction launch weight
q=p10=1/3-t ranges sharply over [2/15,1/3]. The product value 4/15 requires
the specified joint preparation. Those correlated diagonal examples do not
contradict the product-input optimality theorem (2).

This note supplies no physical preparation of the Gibbs pairs or empty
hardware, no calibrated coupling strength, no native checkpoint realization,
no entropy-free reset, no unlimited archive, and no occurrence measure. It
adds a finite-source capacity theorem and one guarded local replacement,
not a complete independent audit of the parent and its predecessors.

## 8. Prior art and falsification

Energy-shell rank comparisons and thermal population engineering are general
methods, not inventions of this work. Relevant primary descriptions include
Gemmer and Anders, *From single-shot towards general work extraction in a
quantum thermodynamic framework*, arXiv:1504.05061, and Brunner, Linden,
Popescu and Skrzypczyk, *Virtual qubits, virtual temperatures, and the
foundations of thermodynamics*, arXiv:1106.2138. The proof of (2) is supplied
here in full and does not import a thermodynamic theorem, bath limit or
occurrence law from those papers.

Decisive counterexamples are: an admitted energy-preserving V beating (2);
a failed full-state inverse of the displayed swaps; a changed raw-space
energy or nonpositive reaction block; an unwanted transition from a claimed
invariant path under the GUARDED law; nonzero action on an inactive initialized
component; a failure of (8) on an allowed logical/reference input; or wrong
moments (10)-(13). The unguarded relaunch is explicitly a negative control,
not a repaired successful run. The exact small audit is supporting arithmetic
and finite-operator evidence; the all-N and full-history statements rely on
the preceding proofs. No status exceeds NON-CANONICAL L1 candidate-T.
