# ETH-QDD-1: selected effective measurement model

PUBLIC; owner-selected theoretical construction; NON-CANONICAL.
Probe P-QDD-SELECTED-MEASUREMENT-LAW-1, lock
https://github.com/mathorn1973/twist-j/issues/1093.
Base 822ae98c63545d9e800b4d145c0eec8c7bca29a6, Public Canon v90 ACTIVE.

The author has chosen to complete an explicit theoretical measurement
model before attempting a laboratory test. This document specifies that
model. Choice is not forcedness, and mathematical consistency is not
empirical validation. The Born occurrence law below is an added physical
postulate; it is not deduced from J or the deterministic native update U.
The selected intervention model does not complete or modify the existing
read-only native decoder. No Canon authority or gate changes in this probe.

## 1. Source, equality and native comparison

Let S=C^4 with G=I_4-11^T/5. The eigenvalues of G are 1,1,1,1/5.
For operators define X^sharp=G^-1 X^* G, with G^-1=I_4+11^T.
A state rho is a G-self-adjoint positive operator with tr(rho)=1:
G rho is Hermitian positive semidefinite. For a nonzero vector v,

    rho_v = v v^* G/(v^* G v).

Equality of states means equality of these operators. A global phase
of v changes no state. This convention must not be confused with the
covariance matrix C=rho G^-1: C is ordinarily positive and tr(G C)=1.
Both descriptions have exactly the same physical content when transformed
with their different, explicitly stated rules.

The source is the complex-linear extension of the shifted cyclotomic
chart A(v)=sum_(i=1)^4 v_i j^i. For rational coefficients this is an
element of K=Q(j). For complex coefficients it means the formal element
of K tensor_Q C, equivalently the four source-basis columns; it does not
mean evaluation of that sum as a single number in the principal embedding.
Such evaluation would collapse the four-dimensional source. Galois acts
on the K factor and the coefficient extension is separately C-linear.
Adopt its positive form and the specific
correlated Galois-fiber encoding already proved in
P-U-GALOIS-FIBER-CODE-1/PROOF.md. For n>=3 write W_n for the four-column
isometry into the four freely evolved endpoints; W_n^*W_n=G. Operators
transport by rho -> W_n rho W_n^-1 on that code. The covariance instead
transports by C -> W_n C W_n^*.

The native free step maps W_n v to W_(n+1) v. Thus it is the identity on
the logical source coordinates in this moving description. This is not a
global unitary extension of U, and a source vector is not one checkpoint.
The physical availability of the correlated preparation is CH-SOURCE.
The same marked Galois code is selected throughout this model; it is not
interchanged with the captured-source incidence construction.

## 2. Five marked settings

Freeze the G-isometry

    R = [[0,0,0,-1], [1,0,0,-1], [0,1,0,-1], [0,0,1,-1]].

It represents multiplication by j, not by J, and R^5=I. For k in Z/5,

    P_0=11^T/4, Q_0=I-P_0,
    P_k=R^k P_0 R^-k, Q_k=I-P_k.

The ordered outcomes are LOW,HIGH, with effects P_k,Q_k respectively
within the selected physical dictionary. An algebraic projector identifier
is not thereby identified with an existing canonical physical-effect ID.
The prospective model identifiers are ETH-QDD-EFFECT-k-LOW/HIGH.

Context equality is literal equality of k and of the declared preparation,
invocation, free-wait and control conventions. The five settings are chosen
because they form the marked cyclotomic orbit without continuous fitting.
Their availability is CH-CONTEXT, an external coherent-control assumption.
Changing k is not a free U step. At endpoint time n, the comparison operator
is W_n P_k W_n^-1 on the code and zero on its unused complement when an
ambient operator is needed. Arbitrary off-code physical inputs are excluded.

An admitted protocol supplies a deterministic causal setting policy:
at invocation j, k_j is a specified function of the already recorded word.
A fixed setting list is a special case. Externally randomized choices would
need their own declared law and are not silently included. Each protocol
also supplies increasing known native comparison times n_j>=3. They are
labels, not a derivation of SI duration or a physical oscillator.

## 3. Channel type and the post-state selection principle

CH-CP admits completely positive linear channels on the entire operator
algebra, including extensions by the identity on arbitrary finite reference
systems. Positivity without complete positivity is insufficient here.
No reduction of an initially correlated apparatus is presumed to be a
state-independent CP map; all operative quantum memory must be explicitly
included or reset as specified below.

Require each outcome to have its stated sharp effect and ordinary
repeatability at that same setting. The inherited mixed-branch theorem then
gives I_(k,H)(X)=E_k(Q_k X Q_k) for an arbitrary trace-preserving CP channel
on HIGH. On rank-one LOW the corresponding reduced channel is fixed.

To select E_k, identify W_0=range Q_0 with the basis

    w_1=e_1-e_4, w_2=e_2-e_4, w_3=e_3-e_4,
    H=I_3+11^T,
    A=[[-1,-1,-3/4],[0,0,1/4],[1,0,1/4]],
    B_t=(A^sharp_H)^t A^t, t=1,2,3.

G restricts to the ordinary Euclidean form on the sum-zero subspace;
the displayed basis therefore has exactly Gram H. This is an explicit
metric identification with the inherited attenuation theorem. A is this
registered attenuation map, not Q_0 R Q_0 and not a free native step.
Transport A and the three tests to W_k=R^k W_0 by R^k.

CH-ATTENUATION says that the post-HIGH channel preserves all three tests
for every supported state, equivalently E_k^*(B_(k,t))=B_(k,t).
The existing full CP theorem forces E_k=id. Hence the selected maps are

    I_(k,L)(X)=P_k X P_k, I_(k,H)(X)=Q_k X Q_k.             (1)

This is a conditional selection within the stated CP class. The physical
preservation principle is a choice, not a new proof that U implements it.
The three tests are fixed without inspecting E_k; a single fitted preparation
per test would not meet the universal condition. Their physical availability
and preservation are separately testable assumptions. The known two-test
and depolarizing counterexamples remain counterexamples to weaker premises.

## 4. Occurrence and the complete ordered law

CH-BORN postulates that exactly one supported outcome is realized with

    p(o|rho,k)=tr(I_(k,o)(rho)).                            (2)

On a positive-probability branch the next state is I_(k,o)(rho)/p.
A zero-probability branch has no normalized successor and cannot be
selected. Zero raw vector preparation has the typed disposition
ZERO_SUPPORT; it is neither a normalized state nor a random LOW/HIGH trial.

For a causal policy and a finite history h=(o_1,...,o_N), evaluate its
settings successively along h and define the unnormalized branch state

    rho_h=I_(k_N(h_<N),o_N) ... I_(k_1,o_1)(rho_0),
    Pr(h)=tr(rho_h).                                      (3)

Specified preparation or other admitted channels are inserted in their
declared chronological positions. PROOF.md establishes normalization,
prefix consistency, conditional states and the extension to a fixed infinite
causal policy when the indefinitely supplied resources are explicitly
assumed. A probability law is not a deterministic selection algorithm.
No random seed or sampling device is being derived or secretly introduced
into Omega. Equations (2)-(3) define an effective statistical theory.

With declared finite operative memory M, rho_h is instead a joint S-M
operator, the read branch is I_(k,o) tensor id_M, intervening operations
are specified joint CPTP maps, and Pr(h) is the full joint trace. This
permits initial correlations inside the declared system; it does not
replace their dynamics by a guessed reduced source channel. The special
free-wait and repetition statements presume no additional joint memory
interaction beyond the operations they explicitly name.

## 5. Pointer, completed event and ordered archive

One reference pointer is C^3 with orthonormal labels BLANK,LOW,HIGH.
Let S_L exchange BLANK and LOW, and S_H exchange BLANK and HIGH.

    V_k=P_k tensor S_L+Q_k tensor S_H.

This explicit controlled unitary sends v tensor BLANK to
P_k v tensor LOW+Q_k v tensor HIGH. It fixes the relative amplitudes
within HIGH and creates no finer HIGH record. Pointer Born readout with
orthogonal record labels yields exactly (1). Before readout the state
retains joint LOW/HIGH coherence; after ignoring a recorded outcome the
reduced source is the sum of the two branches.

The pointer is a reference dilation. Its BLANK slice embeds into the
five-valued archive used by P-QDD-ION-SIDEBAND-WRITER-1. Agreement on that
slice is sufficient for this instrument comparison; the two complete
unitaries are not asserted equal on dirty pointer inputs. No new pulse
count or physical implementation is inferred for the extra context controls.

CH-RECORD supplies one initially BLANK cell per invocation and a passive
archive. A completed record is the literal tuple

    (preparation_id, invocation_id, n, context_k, outcome).

IDs and n are supplied by the protocol; outcome comes from (2). Event
completion means the selected label is appended once to the ordered archive
and retained. An actual history is one sample point of (3), postulated
as realized. Its existence as a theoretical event is not a detector report.

prepare initializes the declared source and cells; step applies V_k and the
postulated readout; emit forms the tuple; append extends the ordered word;
persist acts as the identity on earlier records while the source undergoes
its declared continuation; terminal is true exactly after this append.
A passive reread returns an existing tuple, does not invoke (1), and does
not append a fresh measurement event. ZERO_SUPPORT produces a separate
no-event status, never a fabricated LOW or HIGH record.

A horizon N reserves N fresh cells. A further invocation without a supplied
cell is RESOURCE_EXHAUSTED, outside the supported trial domain. The all-N
theorem is a family of finite-resource protocols, not an infinite-capacity
finite apparatus. Infinite histories additionally require indefinitely
available cells. Full record equality preserves order, settings, IDs and
times; matching a LOW proportion is not equality of histories.

## 6. Renewal and memory

CH-RENEWAL distinguishes source preservation from new preparation. A fresh
source state sigma is prepared by the replacement channel

    Re_sigma(X)=sigma tr(X).

On source S, any operative memory M and old archive A, the required reset
is (sigma tensor eta_M) tensor tr_(SM)(X_SMA), with a specified fresh
memory state eta_M. It leaves the old archive marginal intact and breaks
its correlations with the replaced system. This is a completely positive
trace-preserving operation, not a reversible clean erasure. A reservoir
and preparation control are supplied resources. Their microscopic cost,
physical realization and native origin are not deduced here.

With this full replacement, identical fixed-setting preparations give a
product law. With adaptive settings, conditional factors can still depend
on the past through the chosen setting; unconditional independence is not
claimed. Resetting only the pointer leaves the post-measurement source and
its correlations untouched and therefore does not create a new trial.

The selected reference model has no hidden operative memory. Comparisons
may adjoin any declared finite memory; its state, transitions and resetting
must be specified. Equality of whole apparatuses is equality of all future
ordered output laws under every admitted protocol and preparation, including
renewal operations, rather than equality of one outcome effect. We provide
a fully specified representative, not a classification theorem for every
such apparatus, for unbounded hidden memory or for nonlinear theories.

## 7. Choice ledger and physical scope

| Choice | Content | What would challenge its physical use |
| --- | --- | --- |
| CH-SOURCE | Selected coherent Galois code and positive norm | Preparations fail its interference and norm predictions |
| CH-CONTEXT | Five coherent cyclotomic settings | Measured context operations disagree with the marked maps |
| CH-CP | Complete positivity and declared system boundary | The proposed reduced description fails with an untouched reference |
| CH-ATTENUATION | Three exact tests preserved on every HIGH preparation | A certified violation of any one required test |
| CH-BORN | Single-event Born occurrence and conditional branch state | A preregistered ordered statistical consequence fails |
| CH-RECORD | Orthogonal coarse record, passive retention, fresh cells | Fine HIGH information leaks or a retained label changes |
| CH-RENEWAL | Joint replacement before a new independent preparation | Residual memory changes subsequent conditional laws |
| CH-CONTROL | External settings, clock and coupling resources | The claimed controlled map is not physically realized |

These are qualitative physical tests, not laboratory thresholds invented
without a device. A future empirical protocol freezes errors, sample sizes
and decisions before new data. Known algebraic 1/16 overlaps and the Born
law have already been exposed; adopting them earns no blind prediction
credit. Generic quantum-instrument composition is standard mathematics;
the contribution is its exact specialization and complete resource accounting.

Proposed layer bridges, to be treated separately in a future Canon fold:

    GATE-L1-L4-SELECTED-QDD-SOURCE: chosen code as physical support;
    GATE-L4-L5-SELECTED-QDD-RECORD: chosen instrument as event and record;
    GATE-L5-L6-SELECTED-QDD-BORN: chosen occurrence law on histories.

They are named prospective dictionary boundaries, not passed empirical or
native-derivation gates. Conditional operator proofs, formal record laws,
and normalized mathematical measures do not establish these physical
identifications by themselves. No current gate is changed by this probe.

The old QDD apparatus, terminal-event and complete-family obligations
retain their stronger scopes. Their debt is not erased by narrowing this
model. No total physical decoder, derivation of Born from U, Bell mechanism,
physical time scale, TT state, coupling dictionary or universality is claimed.
In particular the selected input interaction changes a checkpoint in the
comparison and cannot be certified as feeds_U=false. The current read-only
decoder and deterministic Omega remain unchanged; the effective intervention
branch is an explicitly additional physical description.
