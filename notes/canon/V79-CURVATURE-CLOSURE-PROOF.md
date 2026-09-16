# Complete native-word curvature class and its trace-readout obstruction

**NON-CANONICAL / review input for the proposed Public Canon v79 fold.**
No new verifier, scientific execution, numerical enumeration, or formal run
is reported. Until the reviewed fold is adopted, the normative authority is
Public Canon v78, as declared in `STATUS.md`: content commit
`767b136713ae12f5f30869642852dcb8a3f671b0`, Canon SHA-256
`82b29c75eb007c71d73dc33e63270d0e0895fdf41886499fcf79b928826855b5`,
473631 bytes. The coordinator verified public main
`07b123a4082f174c37bf09c9aa8815bd2c0e1660` before this review.

This package proposes one explicit adoption of the previously unfixed
operator class, followed by an exact proof at that class. Its two decisions
are `RAW_NONUNIQUE` and `TRACE_READOUT_UNDERDETERMINED`. The adoption is
a dictionary choice; it is not proved forced by J or by the earlier
architecture. The second decision concerns one completely specified scalar
subrecord, not all `GeometryData` and not physical spatial geometry.

## 1. Public premises and governance boundary

The native affine generators and selector are the public architecture.
`CURVATURE-HISTORICAL-TRACE [T]` supplies the exact historical carrier and
ordinary trace, and `CURVATURE-HISTORICAL-GAUSS-SPLIT [T]` supplies the
ambient/intrinsic equality for that particular historical pair:

```text
X = F5^6, H = <b,d>, V = (Q^X)^H intersect 1_X^perp,
dim(V) = 818,
K_hist = P[T_a,T_c]P|V,
Tr_V(K_hist^2) = -881/8,
K_hist = [PT_aP,PT_cP]|V.
```

Evidence is the unchanged public bundles
[P-CURVATURE-TRACE-VALUE-1](../../probes/P-CURVATURE-TRACE-VALUE-1/RESULT.md)
and
[P-CURVATURE-GAUSS-SPLIT-1](../../probes/P-CURVATURE-GAUSS-SPLIT-1/RESULT.md).
Their trace value is an inherited theorem, not a newly computed prediction.

The current owner guidance is the
[v39 redefinition in issue #108](https://github.com/mathorn1973/twist-j/issues/108#issuecomment-5221531571),
reaffirmed by the later v61 cleanup comment. It supersedes the v15 demand
that all four outcome labels remain reachable. It separates raw operator
classification from totality, representation independence, and uniqueness
of a declared geometric readout. The old identifier
`P-CURVATURE-OPERATOR-CANONICAL-1` remains retired; this document does not
create or resume a probe under that name.

The v39 instruction requires normative adoption before a later formal
readout probe. The proposed v79 content fold can adopt the definitions and
include this exact inline proof without executing such a probe. No result
from the old 640-row child is promoted. The new class below contains all
self-adjoint native-word Koopman operators, with no word-length cutoff.
The gate transfer and row scopes must be explicit in that fold.

The operator and scalar conclusions retain the registered exact L2
curvature scope of the historical theorem. Native L1 generator identities
are premises. No continuum manifold, metric field, embedding theorem,
physical curvature, or additional layer lift follows from the finite
linear algebra.

## 2. Declared choices and complete candidate syntax

The proposed dictionary explicitly chooses the following previously
unfixed data:

1. the historical full checkpoint carrier `X=F5^6` and function space
   `F=Q^X`;
2. the unnormalized counting form `<f,h>=sum_(x in X) f(x)h(x)`;
3. the historical projection subgroup `H=<b,d>`, its exact Reynolds
   projector, and removal of the constant function;
4. every self-adjoint native-word Koopman permutation, paired with every
   other such permutation, in both ambient and intrinsic commutator modes;
5. coefficients `+1,-1`, with ordered pairs retaining their actual signs,
   and with zero operators retained;
6. equivalence induced by every selector-preserving relabeling of the
   complete finite architecture, including nonaffine relabelings;
7. the exact carrier/Gram/ordinary-trace-square subrecord in Section 8.

These choices introduce no measured target or fitted scalar. Choosing the
historical projection is nevertheless a choice, not a uniqueness theorem
about all possible projections. The declared word class does not exhaust
arbitrary linear combinations, other carriers, other projections, or every
possible physical curvature dictionary. Its completeness is exactly the
complete generative class specified here, now proposed for adoption as the
missing class of the raw-operator question.

For `x=(p1,p4,p1p,p4p,q,r)`, all checkpoint arithmetic is in `F5`:

```text
a(x) = (p4,p1,p4p,p1p,q,r),
b(x) = (-p1p,-p4p,-p1,-p4,-q,-r),
c(x) = (-p1p+2,-p4p+1+r,-p1+2,-p4+1-r,1-q,-r),
d(x) = (2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
e(x) = (2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).
```

Let `Gamma=<a,b,c,d,e>` be the subgroup of permutations of `X` generated
by all finite words in these maps. The generators are involutions, so
positive words already generate the group. Define

```text
(T_g f)(x) = f(g^(-1)x),
I_Gamma = {g in Gamma : g^2=id},
R_H = (1/|H|) sum_(h in H) T_h,
P0 f = f - (1/|X|)(sum_x f(x)) 1_X,
P = P0 R_H = R_H P0,
V = image(P).
```

The identity belongs to `I_Gamma`. The full admitted presentation set is

```text
I_Gamma x I_Gamma x {AMB,INT}.

K_AMB(u,v) = P(T_u T_v - T_v T_u)P|V,
K_INT(u,v) = [(PT_uP)|V,(PT_vP)|V].
```

Ordered pairs, including equal pairs, are admitted. Swapping a pair
produces the actual negative operator; it is not an independently licensed
sign quotient. Mode and word labels are provenance. Presentations yielding
the same typed linear operator represent one operator. No rank, nonzero,
trace, historical-value, spectral, or output filter is applied.

## 3. All-word completeness and exact finite bounds

Every native generator is affine and invertible on `F5^6`; composition
remains affine and invertible. Consequently

```text
Gamma <= AGL_6(F5),
|Gamma| <= B,
B = 5^6 product_(j=0,...,5) (5^6-5^j).
```

The product counts ordered independent columns of an invertible matrix;
`5^6` counts translations. This is an exact finite bound, not an observed
group order. A shortest word for any group element has no repeated prefix
element: deleting a segment between equal prefixes would shorten it.
Therefore every element of `Gamma` has a representative of length at most
`|Gamma|-1 <= B-1`.

An exact breadth-first closure starting with the identity, composing by all
five generators, and retaining distinct affine pairs `(M,t)` terminates
after at most `B` elements. Its closure under generators proves that every
native word is represented; induction on word length proves that nothing
outside `Gamma` is inserted. Equality of affine pairs is equality of the
underlying permutations, as evaluation at zero and the six coordinate
vectors recovers `t` and `M`. Testing `g^2=id` gives exactly `I_Gamma`.
There are at most `2 B^2` semantic presentations of the admitted operators.

This supplies a terminating full-class construction, independently of the
two witnesses used below. It supplies no practical running-time claim and
no computed value of `|Gamma|`, `|I_Gamma|`, or the number of operator
classes. None of that enumeration is executed for this proof.

The involution condition has an exact structural meaning. Counting makes
every Koopman permutation orthogonal and

```text
T_g^star = T_(g^(-1)).
```

The action on `Q^X` is faithful. Hence `T_g` is self-adjoint if and only if
`g=g^(-1)`, equivalently `g^2=id`. Thus `I_Gamma` contains **all**, and
exactly, the self-adjoint native-word Koopman permutations. It is not a
convenient short-word sample. An unrestricted word need not be an
involution; its raw commutator need not be skew-adjoint. Such words are
outside this stated self-adjoint class, rather than silently included.

## 4. Canonical finite carrier, Gram matrix, and operator equality

Order `X` lexicographically using representatives `0,1,2,3,4`. Order the
`H`-orbits `O0,...,O_(m-1)` by their least points and put `n_i=|O_i|`.
Every orbit is nonempty. The invariant functions are exactly the functions
constant on each orbit, so their mean-zero subspace has dimension `m-1`.
The inherited historical dimension gives `m=819`.

A canonical rational basis of `V` is

```text
b_i = 1_(O_i) - (n_i/n_0) 1_(O_0),      i=1,...,m-1.
```

The vectors are mean-zero and independent by evaluation on `O_i`.
Every invariant mean-zero function is their linear combination, again by
its values on those orbits. Their counting Gram matrix is

```text
G_ij = delta_ij n_i + n_i n_j/n_0.
```

It is positive definite because it is the restriction of a positive
counting form to a basis. Reynolds averaging acts as exact orbit averaging.
It commutes with `P0`, so `P` is the rational orthogonal projector onto
exactly this `V`.

For any admitted presentation, apply its operator expression to all
`m-1=818` basis vectors. The output is invariant and mean-zero because of
the surrounding projectors. Its unique coordinate vector consists of its
constant values on `O_i`, `i>0`. This constructs an exact rational matrix
`M_K`. Two operators on this fixed typed carrier are equal if and only if
these complete matrices agree entrywise. This is a terminating equality
decision, not a sampled-column test, trace test, spectrum test, or hash
substitute.

For every admitted presentation, its operator maps `V` to `V`, has rational
coefficients, and is skew-adjoint. Indeed the two uncompressed Koopman
operators are self-adjoint, as are their orthogonal compressions, and a
commutator of self-adjoint operators is skew-adjoint. The standard
compression identity is

```text
K_AMB(u,v) - K_INT(u,v)
 = (PT_u(I-P)T_vP - PT_v(I-P)T_uP)|V.
```

Its exterior term is diagnostic, not a third candidate mode. Its
vanishing is not asserted for all pairs: the inherited zero exterior term
concerns the historical pair `(a,c)` only.

## 5. Every selector-preserving architecture relabeling

Write `g_0=a,...,g_4=e` and `z(x)=sum(x) in F5`. The adopted relabeling
group consists of **all** pairs `(h,pi)`, with `h` an arbitrary permutation
of `X` and `pi` a permutation of the numeric generator labels, satisfying

```text
h g_i h^(-1) = g_(pi(i))                         for every i,
pi(z(x)+2 epsilon) = z(h(x))+2 epsilon           for every x and epsilon=0,1.
```

The clock and its driver bit are fixed. The identity, inverses, and
composites satisfy these equations, so this is a group. No assumption that
`h` is affine is made.

Since `z` is surjective, comparison of the selector equations at zero and
one gives

```text
pi(z+2)=pi(z)+2          for every z in F5.
```

Because two generates the additive group of `F5`, it follows that
`pi(z)=z+c` for one constant `c`. Conjugacy by any permutation preserves
the number of fixed points. The complete generator fixed-point counts
follow directly from the displayed native formulas:

| Generator | Fixed-point constraints | Count |
| --- | --- | ---: |
| `a` | `p1=p4`, `p1p=p4p`; `q,r` free | `5^4=625` |
| `b` | `p1p=-p1`, `p4p=-p4`, `q=r=0` | `5^2=25` |
| `c` | `p1p=2-p1`, `p4p=1-p4`, `q=3,r=0` | `5^2=25` |
| `d` | the single point `(1,3,4,2,3,3)` | `1` |
| `e` | the single point `(1,3,4,2,1,3)` | `1` |

Thus `a` is the unique generator with 625 fixed points. Necessarily
`pi(0)=0`, so `c=0` and `pi=id`. Every allowed `h` therefore commutes with
each of the five generators, hence with every word in `Gamma`, and
preserves `z`.

The corresponding `T_h` commutes with `R_H` and with `P0`, preserves `V`,
and is an isometry of its counting form. It commutes with each candidate
operator in both modes. Therefore

```text
(T_h|V) K (T_h|V)^(-1) = K
```

for every admitted operator and every allowed relabeling. The full induced
architecture equivalence

```text
K ~K K' iff K'=(T_h|V)K(T_h|V)^(-1) for some allowed h
```

is consequently **exact operator equality**. The converse uses the
identity relabeling. The canonical matrix decision of Section 4 decides
this complete equivalence. No automorphism census, affine restriction,
unproved rigidity theorem, or rational-isometry existence algorithm is
needed. The group of `h` itself is not asserted to be trivial; its action
on this entire operator class is proved trivial.

## 6. Exact complete-class decision and certificate

Let `K_adm` be the set of typed operator values of all presentations in
Section 2. It is finite by Section 3 and carries the exact equivalence of
Section 5. A full decision procedure can enumerate `Gamma`, retain
`I_Gamma`, form both modes for every ordered pair, and collapse exact
matrices. Its zero/one/at-least-two decision is complete by the all-word
construction. This is a mathematical termination proof, not a report that
the procedure has been run.

For the negative decision an exact certificate consists of two admitted
presentations and a proved invariant discrepancy. Such a certificate
decides that the **entire** admitted class has at least two classes: adding
its remaining members cannot identify two already inequivalent operators.
It need not enumerate the whole quotient or state its exact cardinality.
The all-word completeness, total operator construction, and decidable
equivalence are proved independently above. A negative certificate is not
being substituted for any of those definitions or proofs.

The certificate in Section 7 uses literal native words and the inherited
trace theorem. A checker of it verifies the displayed generator identities,
their membership in `I_Gamma`, the historical projector/carrier identity,
and the trace discrepancy. The proof here supplies those checks in exact
algebra. No new scientific verifier or formal run is introduced.

## 7. Raw nonuniqueness on the adopted complete class

The words `a,b,c` all lie in `I_Gamma`. Direct composition gives

```text
a b(x) = b a(x)
       = (-p4p,-p1p,-p4,-p1,-q,-r).
```

Hence the admitted ambient pair `(a,b)` gives

```text
K0 = K_AMB(a,b) = 0.
```

The admitted ambient pair `(a,c)` is exactly the historical operator:

```text
K1 = K_AMB(a,c) = K_hist,
Tr_V(K0^2)=0,
Tr_V(K1^2)=-881/8.
```

In particular `K1!=0`. The discrepancy excludes equivalence under the
complete adopted relation, and even under every invertible intertwiner,
since ordinary trace is similarity invariant. Both operators use the same
carrier, projection, form, normalization, and candidate mode. Their
distinction cannot be attributed to different carrier dimensions or a free
scalar normalization.

Therefore `K_adm/~K` is nonempty and has at least two elements:

```text
RAW_NONUNIQUE.
```

The intrinsic historical presentation gives the same `K1` by the inherited
Gauss-split theorem and is collapsed as exact equality. No full class count,
canonical representative selection, preferred operator, or continuum
interpretation is part of the conclusion.

## 8. Total trace subrecord and its failed output uniqueness

Define one complete formal subrecord `GeometryData_space_trace` with these
fields and no implicit additional fields:

```text
carrier_id   = the X,H,V carrier of Sections 2 and 4,
basis_id     = the canonical orbit basis of Section 4,
gram         = its exact rational counting Gram matrix G,
trace_square = a rational scalar t.
```

The carrier and basis identifiers refer to the full definitions above.
They do not stand for an unspecified physical space. Equality is literal
equality of those identifiers, entrywise equality of the Gram matrices,
and equality in `Q` of the scalar. Define the adopted readout

```text
R_space(K) = (carrier_id,basis_id,G,Tr_V(K^2)).
```

Every admitted operator is a finite rational endomorphism, so its ordinary
trace is defined exactly. Thus `R_space` is total on **all** of `K_adm`.
Equivalent presentations give the same operator and hence the same
record. More generally the scalar trace is invariant under every
intertwiner; the declared relabelings also preserve the carrier form.
The readout therefore descends to

```text
bar(R_space): K_adm/~K -> GeometryData_space_trace.
```

But `R_space(K0)` and `R_space(K1)` have unequal trace-square fields, zero
and `-881/8`. Its descended image has at least two values. Consequently
the proposed output-uniqueness assertion is false:

```text
TRACE_READOUT_UNDERDETERMINED.
```

This is a complete negative decision for the declared trace subrecord.
It is not a failure of totality or representation independence, and it
does not rule out a different declared readout that identifies these
operators. It supplies no complete `GeometryData`, physical spatial
curvature, empirical geometry, or positive L1-to-L2 realization. No
operator is selected after inspecting its trace. A constant or otherwise
coarser new readout would be a different future definition, not a repair
of this failed uniqueness assertion.

## 9. Proposed ledger and gate disposition

The following are proposals for the reviewed normative fold, not status
changes effected by this note:

* `CURVATURE-OPERATOR-CANONICAL`: `O -> T`, with its scope rewritten as the
  exact `RAW_NONUNIQUE` theorem for the now-declared complete
  self-adjoint-native-word class, historical carrier/projection, both
  modes, and full selector-preserving relabeling equivalence. The T is
  nonuniqueness, not a theorem that any operator is canonical.
* `CURVATURE-TRACE-READOUT-UNIQUE`: new `F`, asserting the failed
  single-output property of the exact total trace subrecord above, with
  the two admitted operators as its falsifier.
* `GATE-L1-L2-CURVATURE-CANONICAL`: explicitly transfer its owner to that
  trace-readout row and record `FIRED_NEGATIVE` at the declared subrecord
  scope. Preserve its history; raw operator multiplicity alone is not
  misreported as a failure of every geometric reading.
* The adopted carrier, class, equivalence, and readout are declared
  dictionary/definition choices. Their adoption is not promoted to an
  unconditional theorem of selection from the earlier architecture.

The affected dependencies must retain the unchanged historical inputs and
make the new dictionary premises and gate ownership explicit. No negative
conclusion is transferred to `TRACEKERNEL-CURVATURE-FORCING`: that separate
row still requires its exact L2-to-L1 carrier bridge and complete
admissibility contract. No conclusion here settles `METRO`, minimal-read
derivation, sqrt-phi time/gravity, or the QDD apparatus obligations.

## 10. Falsifiers and limits of the proof

An exact refutation of any of the following defeats its corresponding
proposed claim:

1. a native generator fails the declared affine/involution identities, the
   all-word class escapes the finite affine bound, or an admitted word is
   missing from the proved group-closure construction;
2. the canonical orbit basis, rational projector, skew-adjointness, or
   exact-equality decision fails on an admitted presentation;
3. a selector-preserving architecture relabeling has a nonidentity label
   permutation or moves an admitted operator under conjugation;
4. `a,b` fail to commute, either displayed presentation is inadmissible,
   the inherited historical trace theorem fails, or an admitted
   equivalence identifies the zero and nonzero witnesses;
5. an admitted operator lacks the defined trace subrecord, equivalent
   presentations have unequal records, or the two displayed trace-square
   values agree.

Any source/hash mismatch is an integrity failure, not a mathematical
counterexample. A changed carrier, projection, normalization, word class,
equivalence, or output equality changes the declared question; it cannot
retroactively erase this result. The earlier `-21/8` trace proposal remains
falsified at its historical scope. The inherited `-881/8` theorem remains
unchanged. No new scientific execution or old-probe rerun is required by
this inline proof.
