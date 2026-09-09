# Pair-local incidence and faithful census (NON-CANONICAL)

```text
STATUS:              PROOF-FIRST CANDIDATE / LOCAL DEVELOPMENT
PUBLIC BASE:         fbf33fa1116d9e3526ac4ae057356cf2d2bddb6e
CANON:               Public Canon v75, unchanged
SCOPE:               L1 finite-set mathematics and a formal apparatus model
FORMAL PROBE:        NONE; no identifier or claim reserved
FORMAL EXECUTION:    NONE
NEW PHYSICAL LAW:    NOT ADOPTED
COINCIDENCE-RECORD-FREQUENCY:
                     candidate-H / UNTESTED / STOP, unchanged
QDD-INSTRUMENT-APPARATUS:
                     O / STOP, unchanged
```

This candidate develops the A/U5 route adopted in PR #811. It gives a
precise class in which full pair incidence is forced, proves a sharper
separate-additivity characterization, and constructs a reversible finite
one-cut census witness. It does not infer that Nature realizes the class,
adopt a frequency law, or identify the census with individual self-location.

The mathematical term `record` below names an element of a finite set or an
active bank address. A physical event, observer, detector or L5 stream is
not supplied by that terminology.

## 1. Inputs and inherited results

Keep the fixed marked cell set K={0,1,2,3,4}. A permitted preparation is a
nonzero d in the centered plenum lattice

```text
L_D = {d in Z^5 : sum_k d_k=0 and d_i=d_j mod 5 for all i,j}.
A   = 1+g^2-g^3-g^4,       g e_k=e_(k+1 mod 5),
a   = A^n d,              n>=0,
U5  = A/sqrt(5),          q(a)=sum_k a_k^2.
```

The physical preparation class can be a specified subset of L_D. It must
not be inferred merely from membership in the mathematical lattice. If all
d_k are congruent to t modulo 5, every (Ad)_k is congruent to
(1+1-1-1)t=0; also sum_k(Ad)_k=0. Thus the displayed lattice is A-stable
directly, without relying on the fired centering audit. The count input
remains integral. Raw J, B and nonintegral U5 outputs are not inputs here.

The independently confirmed algebraic inputs are the orbit separation of
PR #805 claim B, the copy/Gram and compression results of #807, and the
residual-fibre/product results of #810. In particular

```text
q(A^n d)=5^n q(d),
(A^n d)_k^2/q(A^n d)=(U5^n d)_k^2/q(U5^n d).
```

The fired combined claim A of #805 is not revived or reclaimed here. This
candidate does not require a new 80/40 group census.

For each cell let X_k,Y_k be two finite input fibres with common cardinality
m_k=|a_k|. They have distinct roles. Their represented ordinal labels are
fresh at a read cut. A physical source-to-d map is still an input obligation.

## 2. Independent permutations: exact theorem and exact limit

For nonempty finite X,Y, the action of Sym(X) x Sym(Y) on X x Y is
transitive. A fixed relation R subset X x Y invariant under every independent
pair of permutations is therefore either empty or X x Y.

Proof: if (x0,y0) is in R, independent permutations can send x0 to any x and
y0 to any y. Invariance places every (x,y) in R. Conversely the empty and
full relations are invariant. This also handles singleton fibres. If one
fibre is empty, the product and every relation are empty.

Thus independent invariance plus nonemptiness in each occupied cell forces
full incidence. Nonemptiness only somewhere in the whole apparatus does not
force every occupied cell to respond.

This theorem concerns a fixed output, not merely a covariant family. For an
equivariant deterministic apparatus map T and an invariant complete ready
state s0, T(s0) is invariant. If s0 contains a hidden matching or distinguished
seed, it need not be invariant; equivariance then supplies no saturation.

There is an especially relevant control. The existing representations
X={S} x U and Y={R} x U carry a canonical matching (S,u)<->(R,u). If this
matching is retained as apparatus data, its automorphisms are diagonal
permutations, not independent ones. For |U|>=2 their pair orbits are the
diagonal and off-diagonal. The diagonal relation is then a valid invariant
alternative of size |U|. Fresh ordinal labels do not themselves erase the
matching. The independent two-port interface is a substantive premise.

Nor does symmetry alone fix multiplicity. For a finite formal record set E
with an equivariant endpoint map p:E->X x Y, transitivity makes every fibre
p^-1(x,y) have the same size c. It gives |E|=c|X||Y|. Applied separately in
the five cells, this permits c_k m_k^2 and hence a distorted normalized
profile. Cell relabelling alone can still permit c_k to depend on the local
multiplicity m_k or the sign. A common response law is required.

## 3. Stronger theorem: separate finite additivity forces product records

Let F(X,Y) be a finite formal record set for two independently variable finite
sets. It assigns maps F(i,j) to injections of either input, preserves
identities and composition, and is the same rule in every cell and sign
sector at the frozen apparatus setting.

Use the following explicit disjoint-union axioms:

```text
F(empty,Y)=empty,             F(X,empty)=empty;
F(X1,Y) disjoint-union F(X2,Y) -> F(X1 disjoint-union X2,Y)
F(X,Y1) disjoint-union F(X,Y2) -> F(X,Y1 disjoint-union Y2)
```

Both displayed maps, induced by the component injections, are bijections.
These are axioms about independently combined input parts, not numerical
assumptions about squared totals. On finite sets and injections we call them
disjoint additivity, not preservation of categorical coproducts. One may
alternatively work on all finite-set maps and require genuine separate finite
coproduct preservation.

Set Q=F(1,1), where 1 is a singleton. Then there is a canonical natural
bijection

```text
theta_(X,Y): X x Y x Q -> F(X,Y),
theta(x,y,r)=F(i_x,i_y)(r),
```

where i_x:1->X and i_y:1->Y name the two elements.

Proof: decompose X as the disjoint union of its singleton subsets. First-input
additivity gives the disjoint union of F({x},Y) over x. Decompose Y into its
singletons and use second-input additivity. This gives the disjoint union of
F({x},{y}) over all (x,y). Functoriality identifies each component with Q,
and the resulting component map is exactly theta. It is a bijection because
the two disjoint-union comparisons are bijections. Naturality follows from
F(i,j)F(i_x,i_y)=F(i_(i(x)),i_(j(y))). No selected enumeration is used.

If endpoint maps s:F(X,Y)->X and t:F(X,Y)->Y are natural, they must send
theta(x,y,r) to x,y: the endpoints on F(1,1) are unique, and naturality with
the singleton injections fixes the general endpoints.

Consequences:

1. |F(X,Y)|=|Q| |X| |Y|, with the same gain |Q| at every size for this rule.
2. If singleton calibration gives |Q|=1, the endpoint map is a bijection:
   exactly one formal record for every ordered pair and no other record.
3. If 0<|Q|<infinity is common to all cells, normalized census already has
   the square profile. The stronger existing once-per-pair hypothesis fixes
   |Q|=1, including its absolute total law.

The theorem forces product formation inside the declared class. It does not
derive that class from J, absence of labels, or equal marginal cardinalities.
Separate additivity forbids suppression, enhancement, merging or splitting
of an existing component's records merely because another same-role component
is added. It is an exact unsaturated, pair-local response condition. It is
not spatial locality, Bell locality, or an independence probability law.

The extension to independently variable X,Y is essential. Defining a rule
only on two matched copies of one U admits the unary rule F(U)=U. Equal-sized
diagonal data do not establish the two-input additivity assumptions. The
arity two and the common singleton calibration are explicit apparatus inputs.

### 3.1 Full five-cell classification exposes the coincidence selector

The most general separately disjoint-additive two-input rule on five-coloured
finite sets has the form

```text
F(X,Y) ~= disjoint-union_(i,j) X_i x Y_j x W_ij,
W_ij   = F(1_i,1_j).
```

Here 1_i is one token in cell i and no token elsewhere. Decomposing both
coloured inputs into their coloured singletons proves this formula by the
same component-injection argument. Injections preserve cell labels.

With the output labelled by the system endpoint i and w_ij=|W_ij|, equal
input cardinalities m_i give N_i=m_i sum_j w_ij m_j. Therefore separate
additivity alone does not select a diagonal square. Even cyclic cell
covariance permits a circulant response matrix with off-diagonal entries.

The exact coincidence calibration is

```text
W_ii is a singleton for every i;
W_ij is empty for every i!=j.
```

This is a condition on the response to elementary input pairs, not an assumed
population formula. Together with separate additivity it yields N_i=m_i^2.
It must be common to the admitted signs, settings, sizes and read cuts;
otherwise those metadata can index distinct response matrices. The current
proposal uses sign-blind response after signed reduction at the cut.

The independently adjustable input-port extension and this 25-entry
calibration are formal apparatus premises. Their operational accessibility
is not provided by the equal-input plenum preparations. Defining a
coincidence to mean same-cell incidence does not prove that a physical device
realizes precisely this calibration.

## 4. Conditional A/U5 census theorem

At a fixed read cut, apply the same calibrated rule F to each (X_k,Y_k), and
combine cells by disjoint union:

```text
E(a)=disjoint-union_k F(X_k,Y_k),
label:E(a)->K,                label(e)=its cell k.
```

If |Q|=1, theorem 3 gives

```text
|E_k(a)|=m_k^2=a_k^2,
|E(a)|=q(a),
|E_k(a)|/|E(a)|=a_k^2/q(a).
```

A faithful complete census is a specified bijection from the readout entries
onto E(a), preserving cell labels. Under that condition the readout has
exactly the same counts. Combined with a=A^n d, its normalized population
census is the U5 square profile and its total is 5^n q(d).

This is the completed conditional mathematical chain. Calling E(a) a physically
realized population and calling its census an observed frequency remain the
existing physical hypothesis. A census theorem does not establish which
record an individual observer occupies. The self-location clause in the
original H is not replaced by this weaker census conclusion.

## 5. Concrete reversible one-cut witness

Here is a formal apparatus that satisfies the one-record calibration and the
local response condition. It demonstrates consistency and constructibility
of the declared class. It does not prove physical implementation.

Let X be the disjoint union of X_k and Y the disjoint union of Y_k. Write
c_X,c_Y for their cell maps. The available address carrier is P=X x Y,
including cross-cell addresses. Allocate one bit b_(x,y) at every address,
retain the immutable input data, and prepare the bank b=0.

Define the pointwise gate

```text
T_a(b)_(x,y)=b_(x,y) XOR [c_X(x)=c_Y(y)].
```

The gate uses cell equality only. It does not inspect magnitudes, quadratic
norms, normalized target values, ordinal equality or a stochastic seed.
It explicitly assumes the availability of the two-input address bank and
uniform activation of all its sites.

For every bank, T_a(T_a(b))=b. Thus the map on the complete state (a,b) is
an involution; it retains a and has no feedback into the count input. The
empty bank is invariant under all independent within-cell relabellings,
and the gate is equivariant under them. After one activation,

```text
b_(x,y)=1 iff c_X(x)=c_Y(y).
```

Name one formal record for each active address and label it by the common
cell. This is a bijection with the full within-cell pair relation. Reading
all active sites once proves the census theorem directly. Restricting an
input to any disjoint component restricts the active-site output to that
component, so this witness realizes the disjoint-additivity comparisons.

One activation is essential. Reapplying T_a erases the written mask. The
specified program is therefore prepare blank -> activate once -> retain
the snapshot under the storage identity -> census once. An implementation
must supply the actual trigger, retention interval and read control. The
proof of a reversible gate alone is not a proof of an autonomous latch or
a persistent physical record.

The distinct cut tag nu belongs to every stored record name (nu,x,y).
Persistence here is persistence of a frozen bank, not continuation of a
residual ordinal through a subsequent A update. A later cut requires its
own bank or an explicitly specified reset protocol. Retaining all cuts
requires additional capacity.

This witness is a finite classical set/bit construction. It is not identified
with a quantum device, the tensor coefficient K a, a Born measurement or the
global autonomous TWIST-J update. The earlier linear Cayley copy and Gram
contraction remain separate algebraic comparison objects.

## 6. Resource and calibration controls

If L(a)=sum_k |a_k|, the full bank has L(a)^2 addresses and q(a) active sites.
By Cauchy-Schwarz L(a)^2<=5q(a). The bank is finite at each finite cut, but
q(A^n d)=5^n q(d) is unbounded over unrestricted n. A fixed finite device
cannot implement all cuts; a physical package must declare its preparation
and cut bounds or an explicit resource extension.

Two exact witnesses are

| Count input | Full bank sites | Active cell counts | Active total |
|---|---:|---|---:|
| (4,-1,-1,-1,-1) | 64 | (16,1,1,1,1) | 20 |
| (5,0,5,-5,-5)=A(4,-1,-1,-1,-1) | 400 | (25,0,25,25,25) | 100 |

These follow by hand from the formulas. They are not a new run transcript.
The accompanying candidate_model.py is an unexecuted implementation with
explicit resource bounds. It creates no accepted verifier or result record.

Sharp controls for a future audit:

- Shared ordinal matching permits m records instead of m^2.
- Equivariance with a hidden matching in the ready state need not produce
  a symmetric fixed output.
- A fixed invariant relation can still be empty; liveness/calibration matters.
- Independent endpoint symmetry allows c_k copies per pair. If c_k=|a_k|,
  cell covariance still holds but active totals have a cubic profile.
- A common Q with two elements gives 2m^2: normalized profile survives while
  the once-per-pair and absolute-total clauses fail.
- A nonblank bank can introduce off-cell records or cancel desired ones.
- A second gate activation removes all blank-start active records.
- Capacity truncation or selective census changes the output population.
- Unequal readout multiplicities can change the observed-count ratio even
  when the active population has exactly the square profile.
- A unary or higher-arity apparatus can also be symmetric. The two-role
  structure cannot be derived from permutation symmetry alone.

## 7. Physical contract still required

This is a candidate realization of part of COINCIDENCE-RECORD-FREQUENCY,
not its adoption or a new registered H. To give the model physical force,
the same apparatus and read cut must supply:

1. A supported source-to-d preparation and ownership of the A read cut.
2. The two independently addressable role fibres, with the shared ordinal
   matching unavailable to the response law, or a proof that it is ignored.
3. Actual pair-local disjoint additivity, uniform singleton response and
   adequate capacity, or an independently justified implementation such as
   the gate above. The symbols alone establish none of them.
4. One physical occurrence for each active record, with calibrated blankness,
   activation, retention, backgrounds and resolution.
5. Faithful complete readout and the separately justified connection, if any,
   to individual self-location rather than merely population census.
6. Typed layer bridges appropriate to this source and target. The existing
   L5-to-L6 Born dictionary cannot be transported by its name alone.

The separate B channel is not placed into the bank input. At the formal model
level the gate does not read B and leaves a unchanged. Independence from B
in a physical apparatus still requires a source/coupling/calibration contract;
[U5,B]=0 does not prove it. No gravity, physical clock or SI interpretation
is assigned to B here.

## 8. Novelty and next formal boundary

PR #810 already establishes that a chosen Cartesian relation has square
cardinality. This candidate adds: (i) a sharp independent-symmetry and
multiplicity boundary; (ii) uniqueness of product records inside one explicit
separately additive two-input class, with the full five-cell response-matrix
classification; (iii) a reversible one-cut implementation and a faithful-census
implication, with adversarial controls.

The registered QDD-FRESH-RECORD-EXTENSION already supplies a reversible
fresh-record construction in a different frozen class, and
QDD-LAW-NATURALITY-VS-GAUGE-BOUNDARY already separates strict microscopic
naturality from weaker quotient covariance. Neither result is reclaimed.
The proposed novelty is the finite two-fibre incidence characterization and
its exact A/U5 census interface, not the first reversible record model or a
derivation of physical symmetry from anonymity.

A later proof-first probe can audit precisely those L1 claims. Its universal
proof must include the singleton decomposition, natural endpoints and common
calibration; finite matrices or sampled fibre sizes cannot replace it.
The physical hypothesis and individual self-location must remain UNTESTED
regardless of those audit outcomes. Any formal probe needs a fresh public
lock, immutable preregistration plus accepted verifier, public readback,
the prescribed execution and independent architecture checks. This local
candidate does not reserve that lane or execute it.

The strongest present conclusion is therefore a product-selection theorem
inside a declared response class and a complete mathematical population-census
model for the owner-selected A/U5 route. Physical instantiation and the
self-location clause remain the exact outstanding bridge.

## Sources

- [PR #805](https://github.com/mathorn1973/twist-j/pull/805): orbit separation;
  claim A remains fired.
- [PR #807](https://github.com/mathorn1973/twist-j/pull/807): full-cell copy,
  Gram contraction and conditional PSD support theorem.
- [PR #810](https://github.com/mathorn1973/twist-j/pull/810): residual units,
  product cardinality and relation nonselection.
- [PR #811](https://github.com/mathorn1973/twist-j/pull/811): A/U5 owner route
  and typed tensor/incidence boundary.
- [Current physical obligation](https://github.com/mathorn1973/twist-j/blob/fbf33fa1116d9e3526ac4ae057356cf2d2bddb6e/canon/REGISTRY.tsv#L301).
