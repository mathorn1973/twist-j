# P-METRO-CLASS-1 scope-owner map and class skeleton (NON-CANONICAL)

Status: `DRAFT / GOVERNANCE-MAP / DEFINITION-UNRESOLVED`

This note refines `P-METRO-CLASS-1-RULING.md`. It proposes nonoperative scope routing
without creating registry rows and corrects the proposed multidimensional
finite-state skeleton. It is not `PREREG.md`, a public definition, theorem,
verifier, run, Canon change, or status proposal.

## Authority pin

```text
Canon:              Public Canon v14
state:              ACTIVE
tag:                canon-v14
activation commit:  f278855cada75691142c02ebad1a75ecc2730db3
content commit:     ab4ea07d15ab1cfa0c403d3c2a74164011ffa0e7
Canon SHA-256:      f9f06af42a9b0b63f806603ddc671ebe6a9e5014b50d230da04a28722ed1a6a2
Canon bytes:        87061
owner row:          METRO-ADMISSIBILITY [O]
scheduler:          DECODER_CORE / ROOT / READY / FORMAL
normative layer:    NOT_APPLICABLE
gate:               GATE-L5-L6-METRO-NORMALIZATION
future probe:       P-METRO-CLASS-1
```

Here scheduler `READY` means only that the owner may choose a residual class.
The class below is not definition-ready and does not authorize the future
probe.

## 1. Proposed governance routing without claim multiplication

The table is nonoperative scheduler advice inside the existing parent scope.
It does not assign authority. The scope keys are not claims, obligations,
registry IDs, dependencies, or status-bearing rows.

| Scope key | Current public owner | Reserved lane or linked gate | Effect of this note |
| --- | --- | --- | --- |
| `HD-RATIONAL-FINITE-ACTION` | `METRO-ADMISSIBILITY` parent | #109 / future `P-METRO-CLASS-1` for one commuting digit-automatic child | none |
| `NONFINITE-STREAM` | `METRO-ADMISSIBILITY` parent | none | none |
| `ADAPTIVE-UNBOUNDED` | `METRO-ADMISSIBILITY` parent | none | none |
| `STOCHASTIC-EXACT` | `METRO-ADMISSIBILITY` parent | none | none |
| `IRRATIONAL-CARRIER` | `METRO-ADMISSIBILITY` parent | none | none |
| `CROSS-LAYER-NORMALIZATION` | `METRO-ADMISSIBILITY` parent | `GATE-L5-L6-METRO-NORMALIZATION` | none |
| `PHYSICAL-UNITS` | `METRO-ADMISSIBILITY` parent, overlapping `METRO-EDGE-SCALE` | `METRO-EDGE-SCALE` for its registered selector/SI scope | none |

Any protocol spanning more than one scope key remains parent-owned. A future
split must assign every remainder and intersection explicitly before it has
normative force.

Under active v14, a future public criterion on one named residual class is
routed through the registered gate and may affect `METRO-ADMISSIBILITY`
according to that gate. This note neither narrows that authority nor decides
the later status route. If the owner instead wants every residual class to
remain independently open, a public governance fold must change the
normative surface before preregistration.

Consequences of this note alone:

```text
METRO-ADMISSIBILITY remains O.
METRO-EDGE-SCALE remains O.
OBSERVER-WRITE-PORT remains blocked.
No scope ownership or downstream quantification changes.
```

## 2. Correct type: an N^a-indexed digit-word system, not a Z^d action

Arbitrary base-`q` digit transitions do not define an additive `N^a` action:
in general the automaton map for `n+m` is not the composite of the maps for
`n` and `m`. The exact structure is an `N^a`-indexed automatic system built
from `a` commuting coordinate actions of the digit-word monoid

```text
D_q = {0,...,q-1}^*.
```

The proposal-local child name is therefore

```text
METRO-COMMUTING-DIGIT-AUTOMATIC-CHILD-1.
```

A candidate protocol has the full shape

```text
P = (coefficient_ring,
     q, a, r,
     S, initial_scope, reachable_scope,
     {delta_(i,u)}, digit_convention,
     L5_source, raw_readout,
     measure_transport, normalization,
     L6_measure_codomain, equality,
     direct_measure, compositional_measure, admissibility,
     reductions, reduction_equivalence,
     completeness_method,
     from_layer, to_layer, gate_id).
```

Freeze

```text
coefficient_ring = Q
q >= 2                         digit base
a >= 2                         coordinate rank
r >= 1                         output rank, independent of a
S                              finite state carrier
A0 subseteq S                  nonempty allowed-start set
delta_(i,u): S -> S            coordinate-i digit transition
i in {1,...,a}, u in {0,...,q-1}.
```

For a digit word `w=u_1...u_m`, `delta_(i,w)` is the composition fixed by
the declared most-significant or least-significant convention. Actions from
different coordinates commute exactly:

```text
delta_(i,w) delta_(j,v) = delta_(j,v) delta_(i,w)   for i != j.
```

Let `enc_q(n)` be the frozen padded base-`q` word. Then

```text
state(s,n_1,...,n_a)
  = delta_(1,enc_q(n_1)) ... delta_(a,enc_q(n_a))(s).
```

This defines the `N^a` input indexing without asserting additivity. The
ordered coordinate basis and ordered output basis are distinct typed data;
no dictionary identifying `a` with `r` is inferred. Leading-zero behavior
must be frozen on the complete allowed/reachable carrier.

## 3. Raw L5 source and total L6 normalization

A pre-normalized state map would assume the L5-to-L6 bridge. Instead propose
the raw source and readout

```text
L5Raw_r = Q_(>=0)^r,
W5      : S -> L5Raw_r.
```

The proposed L5 endpoint is the complete indexed raw stream, not merely its
value alphabet:

```text
L5Stream_s : N^a -> L5Raw_r,
L5Stream_s(n) = W5(state(s,n)).
```

Define the total tagged L6 codomain

```text
Delta_r(Q) = {p in Q_(>=0)^r : sum_j p_j = 1},

Y_r = ZERO | PROBABILITY(Delta_r(Q)),

Normalize(y) = ZERO                         if sum_j y_j = 0,
               PROBABILITY(y/sum_j y_j)    otherwise.
```

Equality is tagged exact rational equality. For convergence, freeze the
metric

```text
d(ZERO,ZERO)=0,
d(ZERO,PROBABILITY(p))=1,
d(PROBABILITY(p),PROBABILITY(q))=||p-q||_infinity.
```

This supplies a candidate raw L5 source, uniform transport, and total
normalization instead of assuming every state already contains an L6
measure. All objects remain proposal-local until a normative fold adopts
them, so the public gate remains open.

## 4. Direct translated-box transport

For a reachable start `s` and

```text
R(t,N) = product_i {t_i,...,t_i+N_i-1} subset N^a,
```

define

```text
Raw_R(s)
  = (1/product_i N_i) sum_(n in R(t,N)) W5(state(s,n)),

A_R(s) = Normalize(Raw_R(s)).
```

The direct criterion is uniform translated-box convergence: there is one
`L in Y_r`, independent of the allowed reachable start, such that for every
positive rational `epsilon` an exact algorithm returns `N0(epsilon)` with

```text
d(A_R(s),L) <= epsilon
```

for every translation `t`, every allowed reachable `s`, and every box with
`min_i N_i >= N0(epsilon)`.

For anchored q-adic boxes, fix the column-function convention

```text
(M_(i,u) f)(s) = f(delta_(i,u)(s)),
B_i = sum_(u=0)^(q-1) M_(i,u),
T_i = B_i/q.
```

Treating the `r` components of `W5` as column functions gives

```text
Raw_m(s) = (T_1^(m_1) ... T_a^(m_a) W5)(s),
A_m(s)   = Normalize(Raw_m(s)).
```

This is an exact anchored integrity reduction. The full direct criterion
still requires a q-adic boundary decomposition and effective uniform modulus
for arbitrary translated boxes.

## 5. The compositional fork is still unresolved

The initial proposal used individual limits

```text
P_i = lim_(m->infinity) T_i^m
```

and then multiplied the `P_i`. That choice is not equivalent to joint box
convergence on the proposed class. A periodic peripheral mode of one
coordinate may fail to converge individually while contraction in another
coordinate kills that mode in every joint box limit.

There are two honest next choices:

```text
A. FACTORWISE / ITERATED
   Require the individual coordinate limits and every coordinate order.
   This is independent of the direct map, but direct and compositional
   admissibility may genuinely disagree.

B. JOINT SPECTRAL
   Use simultaneous primary/peripheral decomposition of the commuting
   rational matrices and one common terminal sector.
   This can certify the direct limit, but it is not an independent
   factorwise map merely because it has a different implementation.
```

The owner must choose the scientific target before a definition freeze.
Combining option A's factorwise language with option B's joint-killing
criterion would be circular and remains `STOP`.

Any joint spectral option must act only on the reachable submodule generated
by the allowed starts and the readout. Irrelevant algebraic modes cannot be
used to manufacture failure. Peripheral phases, Jordan growth, multiple
terminal sectors, and state-dependent terminal values require exact
certificates; floating tolerances are forbidden.

## 6. Exact reduction candidates

A state relabeling is a bijection `phi:S->S'` that transports the allowed
start set, every digit transition, and `W5` exactly. Unreachable-state
deletion is computed relative to the frozen allowed-start set `A0` under all
finite tuples of coordinate digit words.

The exact multi-action Nerode relation is

```text
s ~ t
  iff W5(delta_w(s)) = W5(delta_w(t))
      for every a-tuple w of coordinate digit words.
```

It must be a congruence for every digit map. The quotient transports `W5`
and all actions exactly; finite partition refinement supplies the decision
procedure.

A coordinate permutation transports the ordered coordinate basis, digit
maps, input indices, translations, and boxes. It leaves the output basis
fixed unless a separate typed output representation is declared.

The following remain forbidden:

```text
flattening N^a input geometry to a one-dimensional enumeration;
erasing named coordinate digit-word actions;
arbitrary factor weights;
output-dependent regrouping;
replacing box geometry by an unrelated ordering.
```

Common `q^k` digit blocking is `UNRESOLVED`, not automatically allowed. A
valid blocking theorem must:

1. use all length-`k` digit words as the blocked alphabet;
2. preserve the allowed/reachable carrier under the padding convention;
3. preserve `state(s,n)` and `W5(state(s,n))` pointwise for every input and
   translation, not merely the final limit decision;
4. carry every exponent residue vector in `{0,...,k-1}^a`;
5. prove the same decision and the same `L` in every residue sector.

Testing only exponents divisible by `k` can hide a peripheral phase and is
not reduction invariance.

## 7. Completeness choice

Before `READY-DEFINITION`, the owner must select one of:

```text
FINITE SURFACE:
    public bounds on q, a, r, |S|, rational denominators,
    transition encodings, and readout encodings;

ALL-PARAMETER THEOREM:
    an exact terminating decision algorithm with a completeness proof
    for every finite input tuple in the chosen child class.
```

Finite-state syntax alone is not a finite candidate surface. The class may
not claim a bounded exhaustive probe and an unbounded theorem implicitly at
the same time.

## 8. Routing and residual ledger

| Surface | Current state | Next decision |
| --- | --- | --- |
| governance ownership | proposed without new claims | owner review |
| input/action type | `N^a`-indexed commuting digit-word system; ranks separated | adopt exact digit and padding convention |
| L5/L6 transport | raw nonnegative vectors plus tagged normalization proposed | adopt or replace |
| direct map | exact target written | supply effective translated-box theorem |
| compositional map | `UNRESOLVED` fork | choose factorwise or joint role |
| reductions | partial | decide minimization and blocking proof |
| completeness | `UNRESOLVED` | finite bounds or all-parameter theorem |
| layer lift | existing gate identified | preserve exact L5 and L6 endpoints |

Future scientific routing must follow the selected fork:

```text
COMMON POSITIVE:
    the frozen exact criterion classifies the complete child and survives
    every allowed reduction;

COMMON NEGATIVE:
    normalization is not total or an allowed reduction changes the decision;

FACTORWISE NEGATIVE:
    the independently defined direct and factorwise/iterated decisions
    disagree, or required coordinate orders disagree;

JOINT-SPECTRAL INTEGRITY:
    the joint spectral route certifies the same direct property; disagreement
    with the direct decision is STOP, not a scientific negative result;

STOP:
    any type, map, matrix orientation, reduction, completeness proof,
    endpoint, gate, or selected-fork integrity check is unresolved or fails.
```

This note produces no outcome, so `METRO-ADMISSIBILITY [O]` remains unchanged.
Under active v14, any later public named-class result must be routed through
the registered gate as written. If the owner wants a residual-preserving
split instead, that governance fold must be public before preregistration.
No formal probe branch, `PREREG.md`, verifier, run, or status change is
authorized by this note.
