# ETH-QDD-2: a selected two-wing measurement contract

PUBLIC; NON-CANONICAL. P-QDD-SELECTED-BIPARTITE-LAW-1.
Owner: A. M. Thorn / selected-bipartite session 2026-09-20.
Public lock: [#1095](https://github.com/mathorn1973/twist-j/issues/1095).
Authority base: Public Canon v90, main
`19b88a43314fa2381ba353b9b2af614bd653ae54`.
Original mathematical text; Apache-2.0.

This extends the selected effective theory ETH-QDD-1 from
[its accepted model](../P-QDD-SELECTED-MEASUREMENT-LAW-1/MODEL.md).
The word selected matters: tensor composition, preparation, controls,
Born occurrence and the record law are declared inputs. The conclusions
proved here are conditional mathematical statements, not native deductions
of a physical Bell experiment. No experimental data or external theorem is
needed for the exact proofs in this probe.

## 1. Carriers, metrics and equality

Each wing has S=C^4, with the inherited marked real source chart and

    G=I4-ones4/5,  G^-1=I4+ones4,  X^sharp=G^-1 X* G.

A density is an endomorphism rho with rho^sharp=rho, G rho positive
semidefinite and tr(rho)=1. The star is conjugate transpose. Density
operators and covariances remain distinct: C=rho G^-1. Complex coefficients
extend four source columns, as in ETH-QDD-1; no principal-embedding collapse
of those four columns is made.

The new composite carrier is S_A tensor_C S_B, dimension 16, with metric
Gamma=G tensor G. Composite densities use the same definition with Gamma.
The partial trace is the coordinate contraction of an endomorphism with
its dual basis, for example

    (tr_B X)_(i,k)=sum_j X_(i,j;k,j).

It is not obtained by mistakenly applying a covariance formula to rho.
Adjoining local finite memories uses their stated Hilbert metrics and the
tensor product. Physical adoption of this composition is CH-TENSOR.

Source equality is equality of density operators; pure vectors differing
only by global phase define the same source. Contexts are the literal
integers 0,...,4 in the marked charts. Outcome labels LOW and HIGH are
literal labels. A record is equal only when every recorded field is equal.
Operational equality of two admitted protocols means equality of all their
finite local and joint record laws for every admitted input, not agreement
of one Bell statistic.

## 2. Local contexts and instruments

Retain the predecessor's real isometry

    R = [[0,0,0,-1],
         [1,0,0,-1],
         [0,1,0,-1],
         [0,0,1,-1]],
    P0=ones4/4,
    Pk=R^k P0 R^-k,  Qk=I4-Pk,  k=0,...,4.

Here R^5=I and R* G R=G. This R is multiplication by j in the
chosen source chart; it is neither J nor the native update U.
Each Pk has rank one and each Qk rank three. Put M_(k,L)=Pk and
M_(k,H)=Qk. The local instrument is

    I_(k,a)(X)=M_(k,a) X M_(k,a).

The predecessor's sharp-effect, repeatability, CP and three-attenuation
selection is retained. No new derivation of those adopted conditions is
claimed. In particular HIGH is coarse: no basis within its three-dimensional
support is written and subsequently forgotten.

For any composite input rho and chosen x,y, define

    K_(a,b|x,y)=M_(x,a) tensor M_(y,b),
    J_(a,b|x,y)(rho)=K_(a,b|x,y) rho K_(a,b|x,y),
    p_rho(a,b|x,y)=tr J_(a,b|x,y)(rho).                 (1)

The conditional post-state is J(rho)/p only when p>0. A zero branch
has no normalized successor. A zero raw preparation is ZERO_SUPPORT and
produces no LOW/HIGH trial. Positivity, normalization and local-order
independence are proved for every complex composite density.

The inherited writer V_k=Pk tensor S_L+Qk tensor S_H uses a local
three-state pointer with BLANK, LOW, HIGH; S_a swaps BLANK with a.
The two writers act on disjoint source-pointer factors and commute.
They produce the coherent joint branches of (1); selecting one realized
pair of outcomes remains the inherited occurrence postulate. Neither
commutation nor pointer dephasing derives single-outcome occurrence.

## 3. Selected common preparation and control law

Fix the real alignment of the two marked source charts and choose

    phi=(1/2) vec(G^-1),
    rho_Phi=phi phi* Gamma.                            (2)

Vectorization uses the ordered tensor basis e_i tensor e_j, i first.
This state has unit norm and both marginal densities I4/4. In orthonormal
coordinates it is sum_i |i,i>/2. The real alignment is part of the
preparation; an arbitrary same complex basis rotation is not silently a
symmetry of this marked vector.

The source parameter space for the primary experiment is the singleton
Lambda={rho_Phi}, with distribution delta_(rho_Phi). More general fixed
densities are used only for the stated universal channel claims and exact
controls. A hidden-variable refinement, when tested below, is a different
mathematical representation of the entire observed table.

One supported trial has the following declared order:

1. Prepare a fresh pair in (2), with local pointers BLANK, fresh archive
   capacity and local operative memories freshly initialized.
2. Two external classical controllers choose x,y independently and uniformly
   in {0,...,4}, independently of the pair preparation and the prior records.
3. Apply the chosen local instruments; realize and record one outcome at
   each wing according to the selected joint occurrence law (1).
4. Preserve the two local records. Combine them later using their common
   preparation/trial identifier. Renew the pair before the next fresh trial.

Thus the complete one-trial record law is

    Pr(x,y,a,b)=p_Phi(a,b|x,y)/25.                     (3)

The independent controllers are a selected stochastic control model. This
work constructs no material random generator and does not infer independence
from a counter or a deterministic setting scan. The probabilities 1/5 and
1/25 are explicit dimensionless inputs. Every x,y is in the control domain,
so all conditional table entries are defined. A realized record is any
positive-weight record under this law, not a claim that a laboratory trial
has been performed. No sampled pseudo-data are generated as evidence.

## 4. Complete joint table, Bell and CHSH conventions

The selected source gives the following entire 5 by 5 binary behavior:

| Settings | LOW,LOW | LOW,HIGH | HIGH,LOW | HIGH,HIGH |
| --- | ---: | ---: | ---: | ---: |
| x=y | 1/4 | 0 | 0 | 3/4 |
| x!=y | 1/64 | 15/64 | 15/64 | 33/64 |

Both LOW marginals are 1/4 for every pair of settings. Give LOW sign +1
and HIGH sign -1. The correlation is

    E(x,y)=sum_(a,b) sign(a) sign(b) p(a,b|x,y)
          =1/16+(15/16) delta_(x,y).

CHSH means E(x0,y0)+E(x0,y1)+E(x1,y0)-E(x1,y1), or any of its eight
coefficient-sign patterns having product -1. All 625 ordered setting
quadruples are admitted, including repeated settings. The exact largest
absolute CHSH value of this table is 2. This does not establish locality
of the complete five-setting table.

Define instead the fixed five-setting statistic

    B=2 sum_k p(LOW,LOW|k,k)
       -sum_(k!=l) p(LOW,LOW|k,l).                     (4)

The second sum contains all twenty ordered unequal pairs, not ten unordered
pairs. Every setting-independent Bell-local model has B<=2. The primary
source gives B=35/16. For these fixed local effects this is also the exact
maximum over all composite density operators, with rho_Phi the unique
maximizer. This is not an optimization over arbitrary local measurements.

The separately declared diagnostic noise family is

    rho_v=v rho_Phi+(1-v) I16/16,  0<=v<=1.

It gives B(v)=(45v-10)/16. This one fixed witness is violated exactly
for v>14/15. No locality threshold below that value, physical noise model,
fitted visibility or empirical error budget is asserted.

## 5. Bell premises and their precise disposition

The full comparison class consists of all measurable hidden-variable spaces
with normalized probability mu independent of x,y and normalized local
response probabilities A(a|x,lambda), B(b|y,lambda), satisfying

    p(a,b|x,y)=integral A(a|x,lambda) B(b|y,lambda) dmu(lambda).  (5)

For these finite settings and outcomes, local private randomization expands
every such behavior into a convex mixture of the 2^5 times 2^5=1024
deterministic strategies. Hence the proof of (4) decides the complete class,
not only a finite hidden-variable ansatz.

The selected table has no representation (5). Already at the declared
singleton source it fails factorization, for example p(LL|k,k)=1/4 while
p_A(L|k) p_B(L|k)=1/16. That observation alone would not exclude every
refinement; the five-setting Bell inequality supplies the stronger result.

Measurement independence is an adopted preparation/control condition in
(3), not inferred from the marginal equalities. Its necessity has a concrete
control. Let tau_(k,L)=Pk, tau_(k,H)=Qk/3, and prepare instead

    sigma_(x,y)=sum_(a,b) p_Phi(a,b|x,y)
                  tau_(x,a) tensor tau_(y,b).          (6)

These setting-dependent separable sources reproduce the entire same table
at their promised settings. Both reduced densities are still I4/4. Equivalently
lambda=(a,b) with mu_(x,y)(lambda)=p_Phi(a,b|x,y) admits deterministic
local responses, at the cost of setting-dependent mu. This is a negative
control, not the selected source. The record table alone cannot prove the
absence of such preparation/control correlation.

No superdeterministic, retrocausal or physical influence mechanism is chosen.
The failed mathematical premise is the existence of factorization (5) with
one independent source law for the complete table. CHSH is not exceeded.

## 6. Both marginal identities and the operational message test

For every fixed joint density rho,

    sum_b p_rho(a,b|x,y)=tr[(M_(x,a) tensor I) rho],
    sum_a p_rho(a,b|x,y)=tr[(I tensor M_(y,b)) rho].      (7)

The first is independent of y and the second of x. The stronger version
allows arbitrary finite local memories and local finite adaptive protocols.
Each next setting, channel, record update and bounded stopping decision may
depend on that wing's own past record and explicitly supplied local inputs.
No interwing channel, remote-controlled filtering, or remote-controlled
stopping rule is admitted. All outcomes, including any locally declared stop
or error flags in the protocol class, must be retained in its complete output.

To test controllable communication separately, hold the preparation law and
Alice's policy fixed. Bob chooses a message m by selecting any admitted local
trace-preserving protocol, possibly adaptive and using his finite memory.
Alice receives only her full local record. The theorem states that its entire
distribution is independent of m. Therefore every decision based on that
record has the same distribution, and its total-variation separation for any
two messages is zero. The converse direction holds identically. General
initial correlations are allowed if they are fixed independently of the new
message; the proof acts on the full joint state rather than guessing a
reduced CP map in a correlated environment.

This is the model's operational no-message test. No length, velocity, light
cone or laboratory separation is supplied, so it is not a measurement of a
signal's speed. A physical faster-than-light communication claim would need
additional spacetime and apparatus identification. Here there is no usable
message channel even before any speed is assigned.

Selective conditioning is different. For rho_Phi, Bob's LOW result prepares
Alice's conditional state P_y, and HIGH prepares Q_y/3. The weighted mean
is I4/4. Sorting Alice's data by Bob's outcome requires the remote record.
It does not give Alice a local control input. Similarly, allowing an actual
interwing channel or allowing Alice's prepared state to depend on Bob's
message lies outside the no-message hypotheses and can change her law.

One concrete communicated-control check uses Bob's context zero result as
a message: Alice then chooses context zero after LOW and context one after
HIGH. Her total LOW probability becomes 1/4+15/64=31/64, instead of 1/4
for fixed context zero. This requires actual access to Bob's result and
therefore tests the exclusion of a communication channel, not its absence.

## 7. Records, renewal and native comparison

Local record fields are

    (pair_preparation_id, trial_id, wing_id, local_invocation_id,
     local_comparison_index, context, outcome).

The preparation/controller owns identifiers and context, the local counter
owns the declared comparison index, and the selected instrument event owns
outcome. Each completed invocation appends once to a fresh cell. Old records
are passive; rereading one does not create a new event. Joint pairing uses
the prior trial identifier and never a fitted coincidence window or retained
outcome subset. All supported completed trials are counted. The primary
ideal trial has no hidden loss channel. Adding losses or efficiencies requires
an explicitly extended outcome/control contract.

For any declared finite horizon, sufficient fresh cells and carriers are
inputs. Exhausted capacity gives RESOURCE_EXHAUSTED outside the supported
measurement-trial domain, not an unrecorded LOW/HIGH outcome. The theory
does not store arbitrarily many records in one fixed finite register.

Fresh repetition replaces the complete operative pair and both local memories
by rho_Phi and their specified ready states, tensor the retained archive
marginal. It removes operative/archive correlations as an open-system
replacement with a reservoir or new carriers. No reversible information-free
erasure is claimed. With the independent fresh setting law, N trials have
the product of (3). Retained-pair repeated reads are a different protocol;
for example repeating the same pair of contexts without interventions repeats
its first outcome pair, instead of drawing another independent pair.

Each wing can be compared to a separately supplied coherent native code by
W_(n_A) tensor W_(n_B). The inherited local intertwining transports the
local projectors during free waiting. This is a comparison of two code
copies, not a decomposition of one checkpoint in Omega, a native pair source,
or a proof that the controlled instrument satisfies feeds_U=false.

## 8. Choice accounting, layers and completion boundary

All eight CH inputs of ETH-QDD-1 remain in force. Five further declared
choices make the two-wing contract complete:

| Choice | Content | Consequence and remaining physical assumption |
| --- | --- | --- |
| CH-TENSOR | Complex tensor composition of two supplied source spaces | Fixes what the two parts and their local operations mean; not derived from one native checkpoint. |
| CH-PAIR-SOURCE | Fixed rho_Phi in the marked real alignment, prepared independently of settings | Gives the displayed correlations; source loading and alignment are assumed. |
| CH-SETTING-INDEPENDENCE | Two independent uniform external controllers, independent of preparation and prior records in fresh trials | Makes all 25 settings accessible under one source law; no native random generator is provided. |
| CH-LOCAL-ACCESS | Only local instruments, controls and memories during the two-wing stage | Supplies the precise no-message operation class; physical isolation is an assumption. |
| CH-PAIR-RECORD | Complete local archives, identifier-based pairing and whole-pair renewal | Supplies complete future records and fresh trials; no hidden detection selection or free reset. |

The source, matrices, ranks, settings, outcomes, probabilities, Bell and CHSH
statistics, control-law weights and v are all dimensionless. The integers
n_A,n_B order code comparisons; no seconds, energy, length or SI conversion
is inferred. The five additional choices are counted even though no fitted
numerical constant was introduced. Selecting a known quantum framework gives
no claim of a parameter-free native derivation or empirical confirmation.

The mathematical results live at L1. Their proposed physical use requires
three distinct future bridges:

    GATE-L1-L4-SELECTED-QDD-PAIR
    GATE-L4-L5-SELECTED-QDD-LOCAL-RECORD
    GATE-L5-L6-SELECTED-QDD-PAIR-LAW.

These are PROPOSED, not passed ledger rows. A fold must supply appropriate
typed owners, schema-valid gate kinds and separately review any dictionary
adoption. The existing BELL-CAUSAL-ACCOUNTING, QDD-INSTRUMENT-APPARATUS,
QDD-TERMINAL-EVENT-SEMANTICS, QDD-INSTRUMENT-CLASS-COMPLETENESS and #539
retain their broader physical obligations. This one conditional theory does
not classify all physical apparatuses or determine the architecture from J.

Mathematical rejection requires an exact counterexample within the fixed
scope or a genuine proof gap. A physical failure would concern the adopted
preparation, tensor structure, controls, local-access restriction or occurrence
law, after a separate independently specified realization and error contract.
The known results are not blind predictions and no priority claim is made.
