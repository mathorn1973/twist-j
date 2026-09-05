# Reversible wave ports, cold reservoir and threshold records

**NON-CANONICAL / PRE-PIN CANDIDATE / NO SCIENTIFIC STATUS ASSIGNED**

This is one chosen mathematical adapter on the exact D3 wave carrier. Its
proposed claim is `DECODER-RESERVOIR-RECORD-ACCOUNTING`. A reversible port
coupling supplies an energy identity; a cold incoming-port convention then
supplies nonnegative reservoir accounting and deterministic threshold
records. The proof and formal decision belong to `PROOF.md`, `PREREG.md`
and the later result. This source document asserts no execution outcome.

```text
probe: P-DECODER-RESERVOIR-COUPLING-1
public_lock: https://github.com/mathorn1973/twist-j/issues/824
source_base: a353b7e2aaec3e13f458f52e68c6464b9d718e67
authority: Public Canon v76
canon_content: 07910adb8418742bf52a0d204577b84b38009b18
canon_sha256: c151a19997dba95d78836c46f38463ab2735ae1c98674f87888d519d7a500112
canon_bytes: 420539
action_layer: L1 encoded mathematical coupling and accounting
physical_completion: UNRESOLVED
feeds_U: FALSE
```

This is not the L4/L5 apparatus profile proposed in issue #539. Its wave,
port, reservoir and ordered-record types are mathematical carriers. Their
physical interpretation and all cross-layer gates remain separate.

## 1. Exact carrier and immutable context

Use the infinite marked lattice and pair order

```text
D3 = {x in Z^3 : x_0+x_1+x_2 is even},
Wave = C_c(D3,Q),
Pair(previous,current) = (u,v) in Wave x Wave.
```

Sparse wave fields have exact rational values at distinct D3 sites, sorted
lexicographically with zero values omitted. Equalities are literal function
and coordinate equality, with no wrapping, truncation, projective quotient,
phase quotient or tolerance.

The coupler context is a finite conductance field `Gamma` and a common
threshold `q`:

```text
Gamma : D3 -> Q_(>=0),
R = supp(Gamma) finite,
Gamma(x)>0 for every x in R,
q in Q_(>0).
```

Zero conductances are omitted; the empty support is allowed. Duplicate
conductance sites are rejected, not silently summed or overwritten. The
canonical context contains sorted distinct sites with their positive
conductances and the exact threshold. Context equality includes both the
whole conductance field and `q`. They are fixed input choices, not functions
of observed heat, emitted records, a desired click rate or a Born target.

Let `B` be all displacements in the complete symmetric D3 shells of squared
lengths `2,4,8,10,16`, with respective weights `6,1,15,1,1`. The unchanged
wave operator and energy convention are

```text
c_z = weight(|z|^2)/324,             sum_(z in B) c_z = 8/9,
(L v)(x) = sum_(z in B) c_z [v(x)-v(x+z)],
E(u,v) = (1/2)||v-u||^2 + (1/2)<u,Lv>.
```

On the stated finite-support domain, the existing local square
decomposition gives `E>=0`, with equality only for the zero pair. No
positive-definiteness claim on a periodic constant mode is imported.

## 2. General reversible port coupling

For each transition supply an incoming rational port field `a` supported
on `R`. This `a` is a port amplitude, not the four-component source
parameter used in preparation below. Solve pointwise for the next wave
slice `w`:

```text
p(x) = [w(x)-u(x)]/2,
f(x) = Gamma(x)[2a(x)-p(x)],
b(x) = a(x)-p(x),                   x in R,

w(x) = [2v(x)-(Lv)(x)-(1-Gamma(x)/2)u(x)+2Gamma(x)a(x)]
       / [1+Gamma(x)/2].
```

Outside `R`, take `Gamma=a=f=0`; `b` is a port field only on `R`. The wave
recurrence is exactly `w=2v-u-Lv+f`. Every denominator is positive, so the
formula is total on its declared domain and uses no implicit solve or
branch selection. Its finite stencil preserves finite support at every
finite transition.

The complete local coupling is the map

```text
((u,v),a) -> ((v,w),b).
```

Its inverse uses the same conductance context and the signed outgoing port:

```text
u(x) = [2v(x)-(Lv)(x)-(1-Gamma(x)/2)w(x)+2Gamma(x)b(x)]
       / [1+Gamma(x)/2],
a(x) = b(x)+[w(x)-u(x)]/2,          x in R.
```

Away from `R`, the inverse is the ordinary free reverse recurrence. The
outgoing signs are essential information; replacing `b` by `b^2` is not
this inverse.

The proposed exact energy identity is

```text
E(v,w) + sum_(x in R) Gamma(x)b(x)^2
 = E(u,v) + sum_(x in R) Gamma(x)a(x)^2.
```

Indeed the forced wave work is `sum_x p(x)f(x)`, and each port satisfies
`p f=Gamma(a^2-b^2)`. General incoming fields can supply energy. The word
passive refers to this energy balance, not to an assertion that the wave
is unchanged by the coupling.

## 3. Cold process, tape and energy accounting

The selected forward process supplies a fresh zero incoming field at each
transition:

```text
a_t=0,
(P_(t+1),b_t)=Couple(P_t,0),
delta_h_(t,x)=Gamma(x)b_t(x)^2,
h_(0,x)=0,
h_(t+1,x)=h_(t,x)+delta_h_(t,x).
```

Here `P_t` is a wave pair. Each outgoing signed field `b_t` is retained in
an immutable ordered tape. Previously emitted port fields are not supplied
again as incoming fields. Fresh zero ports and unbounded fresh tape capacity
are explicit model choices, not a derived thermal environment or a finite
apparatus realization. Every finite prefix uses only finitely many sites
and tape entries.

The heat account is a derived function of the tape:

```text
h_(t,x)=sum_(s=0)^(t-1) Gamma(x)b_s(x)^2,
E(P_t)+sum_(x in R) h_(t,x)=E(P_0).
```

Thus wave energy is nonincreasing, each heat account is nondecreasing, and
every account is nonnegative. The complete port law is reversible even
though this selected cold reduced evolution loses wave energy. No claim is
made that the cold convention is the only admissible reservoir preparation.

The tape carries the outgoing port data and their energy. `h`, the counters
below and their record labels are bookkeeping of the same transferred
energy, not additional independent stores. Do not add tape energy, heat
and threshold energy together in one conservation equation.

## 4. Source preparation and clock convention

Use the preceding retarded-energy construction's explicit source choice.
For `z=(z_0,z_1,z_2,z_3) in Q^4`, define

```text
y_0=(0,0,0), y_1=(1,1,0), y_2=(1,0,1),
y_3=(0,1,1), y_4=(2,0,0),
c(z)=(z_0,z_1,z_2,z_3,0)-(sum_i z_i)/5*(1,1,1,1,1),
S(z)=sum_(j=0)^4 c_j(z) delta_(y_j),
P_0=(0,S(z)),
m(z)=sum_i z_i^2-(sum_i z_i)^2/5,
E(P_0)=m(z)/2.
```

`P_0` is already the post-kick pair. Preparation occurs before switching on
the cold coupling; its input energy is accounted for by `E(P_0)`. It is not
an unrecorded cold transition. The exposed match `||S(z)||^2=m(z)` agrees
with QDD total weight on its balanced subset, but it does not derive a
physical source coupling or a LOW/HIGH detector.

New batch tick `0` describes the first coupled transition `P_0 -> P_1`.
After `t` completed coupled transitions there are `t` tape entries, the
pair is `P_t`, and the accounts are `h_t`. A record for a transition is
available only after the new current slice and outgoing field exist.
This elapsed transition index is not a new autonomous U counter or SI time.

## 5. Threshold records and immutable history

For each conductance site, define cumulative threshold count and remainder

```text
N_(t,x)=floor(h_(t,x)/q),
r_(t,x)=h_(t,x)-q*N_(t,x),
N_(0,x)=0,
0 <= r_(t,x) < q.
```

On transition `t`, the new record labels at site `x` are exactly the
integers

```text
N_(t,x)+1, ..., N_(t+1,x).
```

All these labels, at every site, belong to one atomic transition batch.
Canonical serialization orders sites lexicographically and ordinals
increasingly within each site. Serialization does not introduce successive
interactions inside a batch. A jump through several thresholds produces
every intervening ordinal, not just one record or a Boolean flag. Exact
equality `h=k*q` has count `k` and zero remainder.

The ledger identity is

```text
h_(t,x)=q*N_(t,x)+r_(t,x),
E(P_t)+sum_(x in R)[q*N_(t,x)+r_(t,x)]=E(P_0).
```

No heat is discarded when a record is emitted. No click drains the account
a second time, changes `Gamma` or `q`, or kicks the wave. A label is a
mathematical threshold record; it is not a photon count, a Born branch,
an independent trial or an L6 outcome. The total number of labels in a
finite prefix is energy-bounded, but no finite time to complete absorption
or to cross a positive threshold is asserted.

Zero source gives the zero pair, zero outgoing ports, zero accounts and
empty batches. Empty conductance support gives free propagation and no
threshold records. A nonzero source can also yield an empty batch, including
after positive subthreshold transfer. Thus an empty batch never certifies
zero source or failed physical preparation.

Persistent continuation extends the exact pair, tape and derived ledger;
it never resets them. There is no reset or mutating history-truncation
operation. Constructing a fresh history is distinct from extending one.
Histories and batches are immutable; passive rereading of an existing
record creates no transition or new ordinal. Complete history equality
retains context, order, wave/post-state and signed port information. A
quotient retaining only counts is not silently substituted for it.

## 6. Local queries and ownership

Queries over finite D3 regions are passive views of one fixed coupled
history. Heat increments, accumulated heat, counts and remainders are sums
over the queried sites intersected with `R`. For any such additive quantity
`F`, overlapping regions satisfy

```text
F(A union B)=F(A)+F(B)-F(A intersect B).
```

Record labels retain their site and transition identity; querying the same
label twice does not produce two interactions. Distinct conductance or
threshold contexts define distinct coupled evolutions. Their histories
cannot be combined as though they were overlapping views of one history.

The wave law owns the pair update; the coupling owns signed port fields
and transferred energy; the tape owns ordered port storage; the ledger
owns derived heat, counts and remainders; each atomic batch owns the newly
crossed ordinals. Public functions must name these typed sources explicitly.
The frozen implementation supplies concrete signatures and lossless exact
serialization. None supplies a write port to `Omega`, `U`, its selector or
kernel generators. New wave dynamics is not a modification of the earlier
free-wave probe or its pinned source.

## 7. Concrete API and encoding

`coupling.py` uses the preceding immutable probe's `transport.py` as
`wave`. `Field` is its canonical sparse rational wave encoding. A port
field is a `Field` restricted to the conductance support. Record names
and their fields are

```text
Context(gamma, quantum),
Interaction(after, outgoing, forcing, transfer),
State(pair, heat, tick),
Crossing(site, first, last),
Batch(tick, outgoing, deposit, crossings, kind),
History(context, initial, state, batches).
```

`Context.quantum` encodes the mathematical threshold `q`; the name does
not identify a physical quantum. `Interaction.after` is the pair `(v,w)`;
its signed `transfer` field is `Gamma*(b^2-a^2)`, which can be negative for
general incoming ports. `Batch.deposit` is instead the nonnegative
`Gamma*b^2` of a cold step. Sparse outgoing, forcing, transfer, deposit,
heat and remainder fields omit zeros. An empty sparse value is the exact
zero field, not a missing result.

The maps are

```text
couple(pair, context, incoming=()) -> Interaction,
reverse(after, context, outgoing) -> (before_pair, incoming),
port_energy(port, context) -> Q_(>=0),
ready(pair) -> State(pair, (), 0),
advance(state, context) -> (next_state, batch),
threshold_counts(heat, context) -> tuple[(site, integer)],
remainders(heat, context) -> Field,
history_from_pair(pair, context, steps) -> History,
prefix(source_Q4, context, steps) -> History,
extend(history, steps) -> History.
```

`threshold_counts` includes every conductance site, even those whose count
is zero. A `Crossing` stores a nonempty inclusive integer interval; its
derived `.count` is `last-first+1`. This finite interval encoding names
all new ordinals without requiring a materialized record for each one.
`Batch.crossings` orders such ranges by site. Its kind is exactly
`THRESHOLD_CROSSINGS` when that tuple is nonempty and `NO_CROSSINGS`
otherwise, including a positive deposit below threshold.

`ready(pair)` sets only the ledger and elapsed tick to zero; it does not
alter or create energy in the supplied pair. Source `prefix` supplies
`wave.prepare(source_Q4)` as that initial pair. `steps` is a nonnegative
integer. With zero steps the history contains its initial state and no
batches; positive steps emit one batch per completed cold transition.
`extend` continues from the existing state with the same context and
preserves the initial pair and all earlier batches. The ordered outgoing
fields inside `History.batches` are the tape.

A threshold ordinal is identified by its history, site and positive integer
value. Its batch tick supplies transition provenance; that tick is not
another event identity or an additional interaction. Independently created
histories do not share an occurrence identity merely because an ordinal
or a numeric record agrees. Complete equality is literal equality of the
declared records, recursively including context, initial/final wave data
and signed ordered tape; it supplies no physical equality or inter-history
occurrence identification. Merely assembling record objects is not an
independent certificate that a history was generated by the recurrence.

## 8. Choices and scope boundaries

| Choice ID | Explicit chosen datum |
|---|---|
| `CH-RRC-DOMAIN` | Finite rational wave and port fields on the infinite marked D3 lattice; literal equalities. |
| `CH-RRC-ENERGY` | The inherited two-slice energy convention and port energy `Gamma*a^2`. |
| `CH-RRC-COUPLING` | The displayed midpoint port law, with an immutable finite positive conductance field. |
| `CH-RRC-COLD` | Fresh zero incoming ports at every step, no recycling, unbounded fresh tape capacity. |
| `CH-RRC-PREPARATION` | Centered five-site QDD-norm-exposed injection, post-kick pair before coupling, batch tick zero on the first coupled step. |
| `CH-RRC-THRESHOLD` | One positive rational threshold, exact floor accounting and all new ordinals in one batch. |
| `CH-RRC-HISTORY` | Signed immutable tape, persistent continuation, derived accounts, no reset or count-only equality. |
| `CH-RRC-REGIONS` | Passive additive region queries within one context, with inclusion-exclusion on overlaps. |

These choices are not derived from J, from a uniqueness principle, from
the existence of a dilation or from observed target rates. `Gamma` and `q`
are new mathematical context inputs; no claim that their physical values
are selected or that they introduce no physical free parameter is made.

The predecessor supplies a mathematical wave/energy source, not physical
authority for the new coupling. The unrelated U-induced fiber-record lane
`P-QDD-INSTRUMENT-U-INDUCED-2` and rational instrument-dilation closeout are
not resumed or altered. Their frozen classes are not enlarged by this
probe. The proposal-local Q2 reversible-apparatus class is likewise not
silently identified with these wave ports.

Physical source, coupling, environment, apparatus capacity, calibrated
energy, threshold, pointer and post-state identification remain unresolved.
So do physical occurrence and sampling, Born weights/frequencies, complete
physical-family membership/equality, physical terminality and COMM-SAT,
Bell claims, and every L6 probability or measure claim. A deterministic
mathematical event map is not a physical realization certificate.

The public boundaries remain unchanged:

- [#539](https://github.com/mathorn1973/twist-j/issues/539) remains the
  STOP-DEFINITION L4/L5 apparatus-profile lane. This L1 adapter does not
  instantiate or pass its cross-layer gate.
- `QDD-INSTRUMENT-APPARATUS`, `QDD-TERMINAL-EVENT-SEMANTICS` and
  `QDD-INSTRUMENT-CLASS-COMPLETENESS` remain open. No target-controlled
  selection or physical saturation law is introduced.
- [#744](https://github.com/mathorn1973/twist-j/issues/744) still owns the
  missing photon pole/residue/polarization and normalization chain.
- [#756](https://github.com/mathorn1973/twist-j/issues/756#issuecomment-5500304645)
  retains F3 NOT_SATISFIED; production
  [#742](https://github.com/mathorn1973/twist-j/issues/742) remains FORBIDDEN.
  This probe executes no dual/Ward ensemble or production phase experiment.

Only the named conditional mathematical claim may receive a later earned
disposition. No Canon, prior probe, workflow, production freeze or physical
gate changes through this contract.
