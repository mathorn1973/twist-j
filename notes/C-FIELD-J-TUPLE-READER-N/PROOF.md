# A total reader for the bounded scalar datum, including tuple subclasses

**NON-CANONICAL. Prospective candidate-T; independent review and execution
pending.** This proof addresses only the successor contract in PREREG.md.
The original candidate's tuple-subclass false rejection remains a failure
of that immutable implementation; no result here repairs its historical pin.

## 1. Mathematical input and exact finite inverse

The admitted immutable proofs are the predecessor PROOF.md sections 1-4 at
`49dfad177c6ab698b5751de3e56629508982b05f` and independent DERIVATION.md
sections 1-2 at `c404c1c53a9af3ce1b2523de8a56a270e082e7c9`. They agree on
the following facts, all at L1 and with literal ordered equality. For
a=(a0,a1,a2,a3) define

```text
e0=sum a_i^2-a0*a2-a0*a3-a1*a3,
e1=sum a_i^2-a0*a1-a1*a2-a2*a3,
y=C a=(a1,a2-a3,a0-a1-a3,a1-2*a2+a3),
E5(a)=(e0,e1,a mod5).
```

The chart C is an integral bijection. The e0 quadratic is positive definite:
after ordering (a2,a0,a3,a1), its doubled Gram is the A4 path Cartan form.
Its inverse diagonal entries in the original order are (6,4,4,6)/5, so
metric Cauchy-Schwarz gives

```text
a0^2,a3^2<=12e0/5,       a1^2,a2^2<=8e0/5.
```

Thus every member of K5={a:e0<=5} lies in the proved box
[-3,3] x [-2,2] x [-2,2] x [-3,3]. Zero is its only e0=0 element.
For a nonzero element the positive integral norm satisfies

```text
1<=N=-e0^2+3e0*e1-e1^2
    =5e0^2/4-(e1-3e0/2)^2<=125/4,
```

so N<=31 and 1<=e1<=13. The latter follows from the positive quadratic's
roots ((3-sqrt(5))/2)e0 and ((3+sqrt(5))/2)e0. These containing bounds were
proved before enumeration and remain mathematical inputs here.

Equal e0,e1 determine both ordered positive Galois squared magnitudes A,B.
For two distinct scalars with equal data, gamma=alpha-beta would be 5 eta
for nonzero integral eta. The two embedding triangle inequalities give
N(gamma)<=16AB<=496, while integral norm multiplicativity gives
N(gamma)=625N(eta)>=625, a contradiction. Zero cannot collide because its
energy vanishes. Therefore E5 is injective on the whole sector.

Once a datum is normalized to plain integers, reject pairs outside
[0,5] x [0,13]. At e0=0 accept exactly e1=0 and four zero residues. At
e0>0 reject N outside [1,31]. For each residue coordinate enumerate its
lifts in the containing interval; the two width-five intervals give one
lift apiece and the two width-seven intervals at most two apiece. Hence
there are at most four tuples to check. Recompute both displayed energies
and return the unique matching a and C a, or None if none match.

Completeness: an actual domain element is in the box, passes the necessary
bounds and occurs among the lifts, so its exact energies match. Soundness:
an accepted tuple is integral, has the prescribed residues and energies,
and its checked e0<=5 puts it in K5. Uniqueness is the norm argument above.
An implementation may defensively reject multiple matches, but that branch
is unreachable on the admitted mathematical definitions. These statements
recognize the exact image, not just data promised beforehand to be valid.

## 2. Object syntax without user-defined behavior

An input is an existing object. Determine actual nominal tuple membership
with `issubclass(type(value), tuple)`, using the fixed builtin functions and
the builtin tuple class. `type(value)` obtains its actual dynamic type; it
does not consult value.__class__. The second argument is the builtin tuple,
not a user-controlled abstract class or metaclass with a __subclasscheck__.
Consequently this test uses real tuple inheritance without calling an input
hook. In particular a non-tuple claiming __class__=tuple is still rejected.

For any admitted tuple or subclass use exactly `tuple.__len__(value)` and
`tuple.__getitem__(value,i)`. These explicitly named base implementations
inspect the immutable tuple's real length and real slots. They do not
dispatch to the subclass's overrides, invoke the object's __getattribute__,
iterate over the subclass, or inspect its added attributes. Checking the
underlying length before accessing indices prevents an out-of-range access.
No constructor is called on the input's concrete class.

Read only the three outer slots, then check that the first two have
`type(slot) is int`. This identity test does not call any method on a slot.
It excludes bool and all int subclasses before comparisons or arithmetic.
For the third slot repeat actual tuple membership and the underlying
length-four test, then read its four slots by the same base getitem method.
Check their exact integer types before checking the residue bounds. Thus
every arithmetic comparison is on an actual builtin integer. No untrusted
comparison, truth, conversion, equality, hashing, formatting or iteration
operation occurs.

On success construct a fresh plain tuple (e0,e1,r), with r a fresh plain
tuple of those four genuine ints. On failure return None without formatting
the rejected object. This procedure is total over the declared object
contract: every non-tuple or bad shape rejects in a finite prefix, and
every good shape entails exactly seven indexed slot reads and finitely
many builtin type/bound checks. The normalized syntax check may stop earlier
on an invalid component. A hostile user method that raises or never returns
cannot affect termination because it is never invoked. Ordinary finite
object/int semantics and runtime availability are as declared in PREREG.md.

Two syntactically admitted inputs are equivalent precisely when the six
normalized integer values agree. The subsequent reader uses only those
values; it never retains or revisits the original tuple objects. Hence its
output depends only on the normalized value, including for all subclasses
with misleading methods or mutable attached metadata. The procedure writes
no input attribute or underlying slot, so input data and metadata remain
unchanged. All successful outputs are constructed from builtin integer
arithmetic and plain tuple constructors and satisfy the promised output type.

## 3. Composition and original counterexamples

Compose section 2's total normalizer with section 1's finite mathematical
inverse. The first stage returns None exactly on syntactic failure. Every
surviving value has a unique mathematical interpretation. The second stage
returns None exactly outside E5(K5), otherwise the unique pair (a,C a).
This proves totality, soundness, completeness, uniqueness, output plainness,
equivalence invariance and absence of input-hook calls at the stated scope.

For a plain subclass `class T(tuple): pass`, both

```text
T((0,0,(0,0,0,0)))
(0,0,T((0,0,0,0)))
```

normalize to (0,0,(0,0,0,0)) and return ((0,0,0,0),(0,0,0,0)). The same
conclusion holds when either or both objects use a subclass whose public
len, getitem, iteration or other hooks raise. Conversely an empty tuple
subclass whose public view pretends to contain that valid datum still
rejects: its real underlying length is zero. A residue facade with three
underlying slots also rejects even if its public view pretends to have four.

Exact integer type remains deliberately strict. An int subclass with value
zero is rejected even if it compares equal to zero, as is bool. That is an
explicit part of this successor's contract, not a post-run narrowing.
Valid-to-valid residue substitution remains accepted: residues of 1 and j
with e0=e1=1 identify different valid scalars. No error-correction theorem
or physical observation claim is added.

## 4. Audit and evidence limits

The standalone verifier will build a finite reference image using the
canonical field matrices and compare the reader's coefficient formulas
against it. The complete box, complete bounded key set and the declared
outside-key set are finite audits. Passing them in nine wrapper combinations
does not enumerate all Python subclasses; universality comes from the
base-operation and normalization proof. Hostile/lying fixture objects check
that the implementation respects that proof's crucial dispatch boundary.

No successor code has executed at this draft stage. The exposed historical
census targets are regression targets only. Independent review and actual
run records remain pending. Dependencies retain candidate-level status; no
Canon row or physical owner changes and no transport dynamics are provided.
