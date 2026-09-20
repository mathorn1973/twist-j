# Selected theory: a completion program with explicit choices

**PUBLIC; NON-CANONICAL.** This is an owner-authorized theory selection and
work program, not a Canon release or an empirical result. Its authority base
is Public Canon v90 at public commit
`822ae98c63545d9e800b4d145c0eec8c7bca29a6`. The first construction belongs to
[P-QDD-SELECTED-MEASUREMENT-LAW-1](../../probes/P-QDD-SELECTED-MEASUREMENT-LAW-1/),
public lock [#1093](https://github.com/mathorn1973/twist-j/issues/1093).
Formal run and acceptance status belong to that probe's records; this frozen
program does not anticipate them. No file under `canon/` is changed here.

## 1. What completion means

A theoretical model may be complete before it has been experimentally tested.
Completion requires specified states, dynamics, observations, probabilities
and domains, with no undeclared choice needed to calculate a claimed output.
It does not require proving that Nature follows the model. That is a separate
physical hypothesis, with consequences to test.

We therefore select one effective measurement theory and prove its internal
consequences. Its additional assumptions are inputs, not deductions from
`J = 1 + zeta_5^2` or from the autonomous update `U`. Existing impossibility
results keep their original scope. A proposed positive model in another
class does not undo them.

Three kinds of statement must remain distinguishable:

| Kind | Meaning | Proposed treatment in a future fold |
|---|---|---|
| Conditional mathematics | A specified set of assumptions implies an exact conclusion. | T only after the proof and acceptance gates support it. |
| Selected physical dictionary | The owner chooses this mathematical object as the effective description in a fixed domain. | Explicit definition and, where a claim is appropriate, at most D; no uniqueness or derivation implied. |
| Physical adequacy | Preparations and measurements in Nature obey the chosen description to a declared accuracy. | H with an independent test; no claim of experimental confirmation. |

Neither an unproved physical assertion nor a chosen target number becomes a
theorem by being placed in the second row.

## 2. Decisions selected for the first measurement theory

The profile is `ETH-QDD-1`. Its frozen choice identifiers are `CH-SOURCE`,
`CH-CONTEXT`, `CH-CP`, `CH-ATTENUATION`, `CH-BORN`, `CH-RECORD`, `CH-RENEWAL`
and `CH-CONTROL`; their detailed definitions belong to the probe. These choices
are informed by existing mathematical results and known quantum probability.
The selected Born law and already known QDD weights, including `1/16` where
applicable, receive no credit as new predictions of this selection.

The domain is the specified coherent Galois code, with source Hilbert space
`C^4` and positive Gram matrix `G = I_4 - ones_4/5`. Complex extension acts on
the four source-basis columns. It is not an additive amplitude assignment
from the finite checkpoint group into characteristic zero. States are
positive trace-one operators in this Hilbert space; computations may use any
explicitly fixed isometry to orthonormal coordinates. The zero source is
`ZERO_SUPPORT`, not a normalized preparation and not a fifth outcome.

| Choice | Adopted content | Reason and consequence | Limit |
|---|---|---|---|
| Coherent source | Use the registered Galois code and its Gram-preserving native free transfer. | It retains the full quadratic source data and supplies an exact LOW/HIGH comparison. | Physical loading of that code is an assumption; native coalescence does not select it uniquely. |
| Five contexts | Select the five rank-one projectors transported by the specified cyclic `j` action and their rank-three complements. | One complete context set is available before composing measurement histories. | This is the selected mathematical context action, not an identification of that action with native `U`. |
| Quantum operations | Admit specified finite-dimensional completely positive instruments, including explicit memory when used. | Positivity extends to entangled auxiliary systems and finite protocols compose. | This is an effective class, not a classification of all physical apparatuses. |
| Coarse post-state | Use the registered exact LOW/HIGH effects, ordinary repeatability, and preservation of the three fixed HIGH attenuation tests for every supported state. | The existing mixed-channel theorem selects the identity channel on HIGH; rank one fixes the reduced LOW channel. | Effects and attenuation preservation are adopted. Repeatability alone would not select this channel. |
| Event and occurrence | A completed measurement produces one outcome, with conditional Born probability and the associated normalized post-state. | It supplies first outcomes and a common rule for complete ordered histories. | This is an additional physical law, not a consequence of coherent branching or of deterministic `U`. |
| Record | A separate record register receives the coarse label; its chosen persistence law protects earlier labels during the declared experiment. | It makes the difference between a current pointer and a retained record explicit. | The ideal storage law is assumed; indefinite fault-free material storage is not claimed. |
| Ready and reset | Every trial declares the source state, port ready state, fresh record capacity and its reset or replacement channel. | The theory specifies the next preparation instead of hiding it in the word reset. | Replacement is an open-system operation with a discarded environment; it is not a clean energy-free erasure. |
| Control | Context, interventions and their schedule are external classical control inputs, with any adaptive dependence stated causally. | The complete finite protocol has a defined order and comparison. | The native counter is not thereby identified with a material oscillator, energy supply or trigger. |

For HIGH, the relevant pre-existing result is
`QDD-MIXED-CHANNEL-ATTENUATION-RIGIDITY [T]`. In its fixed support metric,
`B_j = (A^sharp)^j A^j`, and for the complete declared CPTP class,

```math
E^*(B_j)=B_j\quad(j=1,2,3)\quad\Longleftrightarrow\quad E=\mathrm{id}.
```

The tests mean equality on every density operator, not agreement at three
selected input values. The fixed metric, attenuation map and transport into
the selected code must be kept explicit. This theorem concerns the reduced
channel. It does not identify environments, hidden records or a complete
apparatus family. Its proof and counterexamples are in
[MIXED-PROOF.md](../../probes/P-QDD-V80-CLOSURE-BOUNDARIES-1/MIXED-PROOF.md).

For any declared finite protocol, let `K_{o_i|h}` be its unnormalized CP branch
map at step `i`, including the previously declared free transfer, intervention
and memory updates as appropriate; `h` is the preceding recorded history.
Each node's branch maps sum to a trace-preserving map. The selected law is

```math
p(o_1,\ldots,o_N)
=\operatorname{tr}\!\left[
K_{o_N|o_{<N}}\circ\cdots\circ K_{o_1|\varnothing}(\rho_0)
\right].
```

This specifies all finite horizons. Normalization and compatible prefix
marginals are mathematical obligations of the probe. There is no assertion
that a fixed finite native reader generates an infinite independent sample
stream. A conditional state is defined only at positive branch weight;
zero-weight histories have zero probability and need no division by zero.
One realized outcome remains a postulate even when the branch weights and
the coherent record isometry have been proved exactly.

Each experiment has finitely many operations and finite auxiliary dimension;
the theory ranges over every such declared experiment, without one uniform
bound on all experiments. Quantum memory is included in the joint state when
present. A reduced source map is not assumed CP in the presence of arbitrary
undeclared initial source-memory correlations. Independent repetitions require
a product preparation and suitable control assumptions. Repeatedly reading
the same retained source is a different protocol and is generally correlated.

## 3. Relation to the native theory and the apparatus contract

On the selected code the registered free transfer remains actual native
pushforward. Active loading, coupling, record transfer and reset are additional
operations of the controlled model. They are not reclassified as passive
readings of unchanged `U` because the final checkpoint returns to a free
trajectory.

The existing decoder requirement `feeds_U=false` is unchanged. This selected
controlled model runs alongside that decoder contract; it is not a completed
profile for issue [#539](https://github.com/mathorn1973/twist-j/issues/539).
The ion proposal supplies a concrete conditional implementation of a writer,
but its externally powered laser program does not derive control from `J,U`.
See [P-QDD-ION-SIDEBAND-WRITER-1](../../probes/P-QDD-ION-SIDEBAND-WRITER-1/).

The stronger owners `QDD-INSTRUMENT-APPARATUS`,
`QDD-INSTRUMENT-CLASS-COMPLETENESS` and `QDD-TERMINAL-EVENT-SEMANTICS`
retain their registered questions. In particular, selecting exact effects,
Born occurrence and a coarse post-state is not the target-independent
physical derivation required by those owners. We must not retrospectively
narrow their full class to the class chosen here.

The proposed physical dictionary needs three named, separately assessed
cross-layer gates:

| Proposed gate | Endpoints | Content and current status |
|---|---|---|
| `GATE-L1-L4-SELECTED-QDD-SOURCE` | L1 to L4 | Adoption of the specified coherent code, positive norm, preparation domain and physical support comparison. PROPOSED, not passed. |
| `GATE-L4-L5-SELECTED-QDD-RECORD` | L4 to L5 | Chosen controlled instruments, one completed event, context keys, ordered records, persistence and reset. PROPOSED, not passed. |
| `GATE-L5-L6-SELECTED-QDD-BORN` | L5 to L6 | Born law on complete ordered finite records, normalization, zero-support handling and dependence assumptions. PROPOSED, not passed. |

These names do not add registry rows or authorize a guessed gate-kind value.
A future fold must bind each to an appropriately typed owner and the current
gate schema. A formal conditional probability theorem does not by itself
pass a physical bridge.

## 4. Decisions already made, and choices not yet made

The new program should not reopen settled selections or quietly complete
unselected constructions.

| Topic | Present treatment |
|---|---|
| `COIN-MINIMAL-READ [D]` | Retain the existing choice of `beta_1`. `MINIMAL-READ-DERIVATION [O]`, which asks for necessity without that premise, remains separate. |
| `FRW-INHOM [D]` | Use its already selected cell/FRW dictionary at its registered scope. No complete inhomogeneous continuum metric is added here. |
| `TT-SOURCE [D]` | Retain the selected isolated-packet emission map, including its declared locality, onset and transfer assumptions. |
| `TT-VECTOR-STATE-NORMALIZATION [O]` | Next candidate: retain the existing K1 source ensemble and explicitly choose its full outgoing vector-state map. This note does not choose that map, scalar comparison or a numerical tensor ratio. Covariance alone cannot replace fourth moments; the existing fixed-modulus obstruction excludes Gaussian/Wick closure in its scope. |
| `METRO-EDGE-SCALE`, `SCHEME-DICTIONARY [O]` | Next candidate: one complete measurement scheme and one declared ladder representative through the existing electron-mass anchor. No representative, coefficient or conversion map is selected here. A new dimensionless parameter must be admitted as such, never called a unit conversion. |
| Photon geometry | A local long-wavelength effective domain is a possible next selection, requiring an exact domain and error bound. This note supplies neither. It does not close global null-set equality or a massless phase. |
| Dark-energy trace exponent | Do not adopt the target `w=-14/15`, `Delta_DE=1/p` or an equivalent density law as a derivation of that same target. The existing nonselection remains. |
| Generations and couplings | A desired count or measured constant is not a construction principle unless explicitly introduced as new input with its predictive cost. No such input is selected here. |

The accepted proof in
[P-ENTROPY-MEASURABLE-OBSTRUCTION-1](../../probes/P-ENTROPY-MEASURABLE-OBSTRUCTION-1/)
is a separate candidate negative closure: it excludes the entire registered
stationary product-source route. Its proposed T theorem and F disposition of
`ENTROPY-LAYER-BRIDGE` should use their own evidence. It supplies no alternate
source, outcome law or reason to identify an auxiliary proof construction
with physics.

## 5. Build order and stopping points

1. Freeze the selected preparation/instrument/record theory and its proof;
   run the exact audit only after the public pin. Accept or reject that
   mathematical result at the unchanged scope.
2. Prepare a separate Canon fold with conditional theorems, explicit selected
   definitions and at most D dictionary claims. Retain the stronger open
   owners and distinguish a formal completion from physical adequacy.
3. Extend the selected theory to a completely declared bipartite experiment:
   source, settings, control law, outcomes, correlations, factorization and
   both no-signalling tests. `BELL-CAUSAL-ACCOUNTING` is not closed by merely
   writing down a quantum trace formula.
4. Select and compute the next independent physical dictionary, preferably
   the complete TT vector state or the metrological scheme, after its full
   input contract is frozen. Do not advance by selecting the desired output.

Laboratory work is not a prerequisite for steps 1 and 2. Physical claims must
nevertheless retain explicit domains and a route to independent tests.
The first selected theory will earn its place by constraining complete future
records and post-states under fixed assumptions, while making the undeduced
inputs visible enough to replace or reject them later.
