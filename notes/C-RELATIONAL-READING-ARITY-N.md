# C-RELATIONAL-READING-ARITY-N

**NON-CANONICAL / INCUBATION / STOP-DEFINITION FOR PHYSICAL USE**

Date: 2026-09-07. Basis: Public Canon v80, public main and activation
commit `4577448dba85c492b27773a64e5fd557abc02b30`;
content `b00171ef21ecb0d905593224f66f5e8a0f6c28e5`;
Canon SHA-256 `8b076ee3d940e4a3639d3ffca06ae86e7df69dfc87f90d06ea99d4f9fca6b66c`,
541516 bytes. The identifier names an incubation, not public status C.
H and T-candidate below are proposed local roles, not Registry entries.
This note records a research program and elementary arguments. Section 8 links
the separately preregistered first formal attack; this document itself grants
no physical realization, new Canon status or status transition.

## 1. Proposed relational principle

**[H, proposed] A reading belongs to a typed relation in a declared context.**
Its admissible algebraic forms should be classified from the relation,
symmetries, composition laws and output type before comparison with desired
physical outputs. The algebraic type may constrain a family rather than select
one invariant. Global uniqueness of the decoder is not required.

The motivating stronger proposal is that internal relations can have different
types while a measurement creates a binary relation between the system (which
may itself be a composite relation) and a record. A suitable binary incidence
could then explain a quadratic measurement weight. This is an open selection
and realization problem: binary incidence alone does not imply a square.

The intended division is

```text
Flow: a typed native relation R
  -> Snap: a physically realized record relation E_c(R, record)
  -> an independently justified record valuation
  -> an ordered event stream and its statistical interpretation.
```

These arrows are proposed obligations. This note supplies no new dynamics for
Flow or Snap, and no feedback from decoder outputs to U. An observer means a
specified apparatus/record carrier; consciousness is not a premise.

The phrase "Born as the law of a binary cut into a record" is a motivating
hypothesis. The precise target is a theorem about an independently defined
class of physical record mechanisms, with sufficient premises stated below.
The stronger statement "a record has two sides, therefore its measure is
quadratic" already fails as an unrestricted mathematical implication.

## 2. What v80 establishes

The authoritative statements are in [Canon section 2](../canon/CANON.md) and
the [Registry](../canon/REGISTRY.tsv), under these exact identifiers:

- `QDD-SIMPLEX-PAIR-INCIDENCE [T]`: for the chosen regular-simplex P/Q split,
  integer source z, s=sum z_i and S2=sum z_i^2,
  A=s^2 and B=N sum_(i<j)(z_i-z_j)^2 are ordered Cartesian-pair counts.
  The least universal integral scale is U=N(N-1). The corresponding squared
  branch norms are A/U and B/U. At N=5, U=20 and B=5(4S2-s^2).
- `A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS [T]`: the complete rational A4 frame
  domain admits positive normalized nonquadratic weights. Positivity and
  noncontextual complete-frame additivity on that domain do not select the
  adopted quadratic reading. This does not assert that those alternatives
  are physically realized or refute results on a different measurement domain.
- `READING-SPLIT [D]` and [CORE](../canon/CORE.md) permit multiple admissible
  typed readings. Their context, equality, overlap compatibility and any
  independent selection/occurrence rule must be supplied at the claimed scope.

In v80 the two factors of each Cartesian square are mathematical amplitude
fibres. They have not been identified with a physical system and its material
record. The proposed identification is a new bridge, not part of the pair
theorem. In particular, complete incidence is stronger than a matching of
corresponding units.

## 3. Aim A: pair theorem and its exact premises

**[T-candidate, elementary proof supplied here; no public promotion]**

### A1. Complete Cartesian counting

Let X and Y be finite sets, E a subset of X x Y, and count each ordered pair
once. Write m=|X| and n=|Y|. Then

```text
0 <= |E| <= mn,
|E| = mn iff E = X x Y.
```

Proof: X x Y has mn elements; omitting any pair strictly decreases the count.
If m=n=d, complete incidence has d^2 pairs. A fixed positive integer
multiplicity c gives c*d^2. Equal cardinalities, completeness, ordering and
multiplicity are explicit premises, not consequences of there being two sides.

### A2. Separate additivity characterizes a product on unstructured sets

Let F(X,Y) take nonnegative real values, depend only on the separate bijection
classes of finite X and Y, and be additive under disjoint union in each
argument. Put c=F({*},{*}). Decompose both sets into singletons. Repeated
additivity gives

```text
F(X,Y) = c |X| |Y|.
```

Thus restricting to equal cardinalities gives c*d^2. Fix c=1 for unit pair
counting. This theorem concerns unstructured sets: a distinguished diagonal,
orientation, exclusion constraint or coupling kernel changes the domain and
the admissible symmetries. Its hypotheses must be justified for an apparatus
before it can be used as a physical selection argument.

### A3. From signed source coordinates to quadratic forms

Fix integer linear forms ell_j on z in Z^r and fixed positive integer
channel multiplicities c_j. If each channel first produces a residual fibre
of size |ell_j(z)| and then realizes its complete ordered Cartesian square,
the total count is

```text
W(z) = sum_j c_j ell_j(z)^2 = z^T G z,
G = sum_j c_j ell_j^T ell_j.
```

G is symmetric positive semidefinite. Conversely is not claimed for arbitrary
integer quadratic forms with these integral channel constraints. With fixed
rational coefficients, one must separately specify a denominator-clearing
scale before interpreting values as integer counts.

This proves a conditional form, not the selection of ell_j, c_j or a physical
apparatus. A nonlinear preprocessing ell(z)=z^2 gives |ell(z)|^2=z^4 in the
original coordinate; degree is relative to the frozen source representation.

Signed reduction is a substantive premise. Two raw arrivals +1 and -1 have
four ordered raw pairs; their net signed residual has size zero and its square
has zero pairs. A physical process that forms the residual before counting
must be specified. The related [unmerged incidence breaker review #812](https://github.com/mathorn1973/twist-j/pull/812)
is non-canonical context, not evidence supplied by this note.

For complex coherent amplitudes, |a+b|^2 includes 2 Re(conj(a)b), which can be
negative. It is not the unsigned cardinality of all raw arrivals. A complex
extension must independently justify composition, conjugation, the positive
pairing and cancellation. Replacing them by a squared norm assumes structure
that this incubation is meant to investigate.

### A4. Counterexamples that every stronger statement must face

| Declared relation | Exact count or value | Missing premise exposed |
| --- | --- | --- |
| Full X x Y, X has m elements and Y has n | mn | Equal sizes are needed for a square |
| Diagonal {(x,x):x in X}, X has d elements | d | Correspondence is not complete incidence |
| Ordered unequal pairs on X | d(d-1) | Excluding self-pairs changes the polynomial |
| Unordered distinct pairs on X | d(d-1)/2 | Equality/order conventions matter |
| Complete triple X x X x X | d^3 | Product counting follows the actual relation |
| Raw signs (+1,-1) versus reduced residual | 4 versus 0 | Reduction cannot be hidden |
| Equal binary fibres after z -> z^2 | z^4 | Binary arity does not fix degree in z |

These are exact counterexamples to omitted-premise extensions, not falsifiers
of v80's fully specified simplex theorem. At d=2 the first four equal-side
counts are respectively 4, 2, 2 and 1.

## 4. Aim B: census by relation type

**[T/C exploration, proposed]** Classify admissible invariants of named native
relations. "Minimal" requires a criterion: generating set, lowest separating
degree, minimal integral scale or minimal sufficient quotient are different
questions. Each census entry must choose one before claiming minimality.

An entry must freeze

```text
relation_id; source_ids and coefficient ring; domain and codomain;
arity and ordered/oriented incidence; equality; context and allowed symmetries;
composition and coarse-graining; invariant versus covariant output type;
admissible invariant family; minimality order and tie equivalence;
known choices; comparison-only physical target; existing Canon dependencies.
```

Starting inventory (existing scopes retained; no completed new census):

| Native input | Algebraic object to classify | Specific unresolved question |
| --- | --- | --- |
| `CODEC-TR4 [T]` | Linear covectors on the frozen integer step module | What follows from its specific eigen-covector law, rather than from calling the source one object? |
| `QDD-SIMPLEX-PAIR-INCIDENCE [T]` | Prepared simplex relation and integer pair counts | Which target-independent premises select these channel forms and complete incidence? |
| `PISTON-2X2-RESHAPE-WEDGE [T]` | Determinant on a marked balanced-piston reshape | Under which admitted relabelings is the output signed, absolute, squared or only covariant? |
| `COLOR-TORSOR-HOLONOMY [T]` | Torsor transport and its registered holonomy | Which part survives the declared change of frame, and which invariant distinguishes the resulting classes? |
| `MAXWELL-BIANCHI [T]` | Edge cochain A, face cochain F=dA and dF=0 | How do incidence and orientation determine the linear boundary law on this frozen complex? |
| `TT-VECTOR-MOMENT-UNDERDETERMINATION [T]` | The six frozen comparison laws and their polynomial moments | Retain the proved minimal separating degree four; do not infer a unique law from lower moments or claim the six laws are exhaustive |

The provisional examples in the proposal need these qualifications:

- A triple does not canonically supply a scalar determinant. A volume form,
  dimension and transformation group must be fixed; an alternating form can
  change sign. An invariant under one group may be a covariant under another.
- For a simplex, oriented determinant volume and metric squared volume have
  different required data and different degrees.
- A loop product is generally a group-valued holonomy; taking its trace also
  chooses a representation. A network contraction requires chosen tensors and
  pairings, including an output type for any uncontracted indices.
- Moments and cumulants require an ensemble or expectation functional, or an
  explicitly defined finite empirical average. Repetition alone supplies none.

The census must allow several inequivalent invariants at one relation type.
Finding them is not a failure unless a frozen claim asserted uniqueness.
Strong interaction, baryon singlets, spin and physical curvature remain
motivating comparison targets, with no identification inferred from an
algebraic resemblance.

## 5. Aim C: physical measurement cut

**[H, proposed / STOP-DEFINITION]** Determine whether a target-independent
physical apparatus class admits a nontrivial binary record factorization and
whether independent laws of that class force the premises of Aim A (or a
specified sesquilinear extension).

Two separate targets are required:

1. **Factorization:** construct and classify the cut, its carriers, equalities,
   contexts and record-producing maps.
2. **Valuation and occurrence:** establish complete incidence or another exact
   positive pairing, then independently justify the event and sampling laws.

Factorization alone cannot establish the second target. Any relation on
A x B x C can be retyped as a binary relation on (A x B) x C. This grouping is
mathematically valid but supplies no counting rule, independent physical
subsystems, tensor product, coupling or apparatus. Likewise a classical
finite-symbol copy s -> (s,record(s)) has a functional binary graph, not a
complete Cartesian relation. Physical admissibility of any such example must
be decided by the frozen class; it cannot be excluded merely because its
valuation is not the desired square.

For a nontrivial target, publish in advance:

- An independently specified apparatus class, source and record carriers,
  context keys, ready states, allowed memory and complete apparatus equality.
- A native source-to-relation map and a relation-to-record coupling, with
  exact domains, zero/unsupported dispositions, composition and persistence.
- The relation instance being counted: all possible source-record pairs,
  selected pairs, transitions, residual fibres or completed events. These
  choices cannot be interchanged after a result is seen.
- A preselected invariant/valuation family and the laws that select among its
  members. Each use of a norm, effect, normalization, ensemble or sampling law
  must be classified as derived, adopted or unresolved.
- A target-independent event rule and an ordered stream, including reset,
  repeated-trial resources and coarse-graining consistency. State whether
  frequencies exist, under what dynamics or ensemble, and with which exact
  limit or finite-sample claim.
- A completeness argument covering the whole claimed apparatus class. One
  successful construction proves existence only. Universal physical coverage
  remains open until its domain and coverage evidence are supplied.

The existing [typed apparatus/record contract](canon/DEF-TYPED-APPARATUS-RECORD-CONTRACT.md)
and [issue #539](https://github.com/mathorn1973/twist-j/issues/539) own the
reusable schema. The [realization and occurrence contract](TWISTJ-REALIZATION-OCCURRENCE-CONTRACT-1.md)
is an existing conditional model. This incubation studies selection premises;
it does not replace those contracts or treat their syntax as realization.

### Probability and recording remain separate

Use W_o(R,c) for a proposed algebraic weight. Only with W_o>=0 and a positive
finite total can W_o/sum_j W_j be a normalized number. That arithmetic does
not establish an occurrence law or an empirical frequency limit. At zero
total return an explicit unsupported/no-event result, not a normalized zero.

The existing `QDD-INCIDENCE-FIRST-HIT-CLASSIFICATION [T]` is a direct warning:
the same full-cycle incidence ratios do not determine first-hit statistics;
the frozen chronological and permutation scan classes have different laws and
the latter imports an order carrier and law. Counting records and explaining
their observed distribution are distinct tasks even after a square is known.

For comparison, the standard quantum target is p(o|rho,c)=tr(rho E_(o,c)),
with positive effects summing to identity. Pure-state rank-one measurements
give a scalar amplitude square; general outcomes can give a sum of such
squares, and mixed states need not have one state-vector amplitude. This
comparison applies to composite systems as well. Busch's theorem characterizes
the trace rule under assumptions on valuations on the full set of effects;
those assumptions are not supplied by binary arity or the rational A4 domain.
See [Busch, 2003](https://arxiv.org/html/quant-ph/9909073v3).

Writing A_o=sqrt(p_o) after choosing the probability is a tautological
factorization and cannot satisfy this program. A_o, its composition law and
its pairing must have an independent construction. Calling Born a theory of
record writing is an interpretation to investigate; it does not remove the
need to recover the statistical predictions at a declared physical scope.

### Layer and status boundaries

| Obligation | Required distinction |
| --- | --- |
| Native algebra to L4 support | Exact carrier, adapter and named bridge; a table of invariants supplies no physical lift |
| L4 support to L5 records | Realized coupling, event ownership, persistence/reset and named gate |
| L5 records to L6 measure | Independently justified measure/occurrence interpretation and named gate; normalized counts remain counts |

No gate is created or passed by this note. `QDD-INSTRUMENT-APPARATUS`,
`QDD-INSTRUMENT-CLASS-COMPLETENESS` and `QDD-TERMINAL-EVENT-SEMANTICS` remain
their existing O / STOP owners. Algebraic generality does not close them.

## 6. Decisions and counterexamples

| Target | Positive result at its exact scope | Refutation or STOP |
| --- | --- | --- |
| Pair premises | Complete proof under published set/weight/coupling assumptions | An exact counterexample inside those assumptions refutes the statement; the counterexamples in section 3 already refute unrestricted two-sides claims |
| Relation census | Exhaustive classification/minimality proof for a frozen class, or an explicitly finite exact census | An admitted omitted invariant refutes completeness; multiple invariants refute only a promised uniqueness claim |
| Measurement cut | Nontrivial factorization for every member of an independently defined class | An admitted nonfactoring mechanism refutes that class-wide claim; missing carriers or a circular class definition are STOP |
| Forced quadratic valuation | All admissible valuations satisfy the derived form under target-independent laws | One admissible nonquadratic valuation refutes selection; excluding it using Born itself is STOP |
| Event statistics | Derived finite/limiting law agreeing with the frozen target and supplied apparatus evidence | Exact incompatible event law or discrepancy beyond a preregistered empirical tolerance refutes that scope; missing event law is STOP |

Internal trilinear invariants do not imply cubic measurement probabilities or
third-order interference. In a prospective interference test, freeze source,
contexts, apparatus changes and calibration before constructing the comparison.
An experimental precedent is [Sinha et al., 2010](https://arxiv.org/abs/1007.4193),
which reported a three-path interference bound below 10^-2 of expected two-path
interference in its photon setup. This is historical context, not a current
best bound, a tolerance adopted here or evidence for this hypothesis.

## 7. First bounded step

Start with Aim A: freeze the admissible finite set/weighted relation class and
classify the effect of dropping each of equal fibre sizes, full Cartesian
occupancy, fixed multiplicity, linear preprocessing and separate additivity.
Retain the explicit counterexamples before proposing a physical selection
principle. The scientific target is to discover which of these premises a
native record mechanism can justify independently.

Then populate Aim B using the native starting inventory, keeping comparison
physics out of invariant selection. Aim C proceeds only when its physical
class, record equality and bridges are defined. Any future formal probe needs
its own public identifier, claim lock, preregistration and frozen evidence.
This note itself authorizes no formal execution or Canon fold.

## 8. First attack completed: the missing selection premise

The separate proof-first probe
[P-BINARY-RECORD-QUADRATIC-SELECTION-1](https://github.com/mathorn1973/twist-j/pull/886)
was publicly pinned at `c157fa9258ed01fb71320feba5a2c223daeb749e` before
execution. Its all-domain arguments are in
[PROOF.md](https://github.com/mathorn1973/twist-j/blob/c157fa9258ed01fb71320feba5a2c223daeb749e/probes/P-BINARY-RECORD-QUADRATIC-SELECTION-1/PROOF.md).
The first Linux audit and both GitHub architectures matched the same exact
stdout, with 109538 checks. These are mathematical results under their stated
premises; no Canon promotion or physical realization is inferred.

**Aim A, decided at the frozen scope.** On equality-only binary carriers with
injection-stable nonnegative atomic weights, the complete class is

```text
W(d)=a*d+b*d*(d-1),
W(d)=c*d^2 for all d iff a=b=c.
```

A total involutive faithful writer can retain its source and older cells,
respect all simultaneous symbol relabelings and still produce a diagonal
active graph of size d. Thus binary structure, reversibility and faithful
writing do not force the full Cartesian count. A nonnegative separately
additive pairing on signed groups must vanish, exposing a separate obstacle
to deriving unsigned counts directly from signed composition.

**Aim B, one complete elementary census.** Equality-only k-ary relations split
into equality-partition orbits of size (d)_r. Their injection-stable atomic
valuations are exactly nonnegative combinations of those orbit counts.
Triples can consequently have linear, quadratic or cubic counts. The broader
census of native relations with additional algebraic structure remains open.

**Native scalar test.** Keeping the adopted v80 channel forms, every positive
integer power p gives normalized weights from |sum z|^p and
5*sum_(i<j)|z_i-z_j|^p with the listed sign/permutation symmetries, scaling
behavior and zero classes. At (1,1,0,0), LOW is 1/11 for p=1 and 1/6 for p=2.
These scalar laws therefore do not select p=2. Full rational-frame additivity,
QDD record conformance and physical admission are not claimed for p=1.

**Aim C, revised decision.** The unrestricted structural implication from
binary faithful recording to a square is refuted. The physical measurement-cut
hypothesis remains STOP-DEFINITION. At the classified binary scope a positive
physical route must independently justify equal matching/nonmatching weights
(or a different explicitly typed positive pairing) and then its event law.
Replacing correspondence-preserving symmetry by independent permutations of
unmarked carriers is an additional premise: transporting a matching under
relabeling does not erase it. The next physical target must explain that
premise or declare a narrower independently motivated mechanism, rather than
derive it from the desired square.
