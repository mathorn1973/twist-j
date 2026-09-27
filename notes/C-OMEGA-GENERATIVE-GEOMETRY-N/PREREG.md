# C-OMEGA-GENERATIVE-GEOMETRY-N: prospective contract

PUBLIC NON-CANONICAL incubation. No Canon authority.
Owner: A. M. Thorn / omega-generative-geometry-20260927; issue #1245.
Date: 2026-09-27. Basis: Public Canon v92, main
c25ec66f1991c15eb94429ca17a52e860d1cb21e.

## Scope and source boundary

Construct and delimit a finite-prefix geometry generator, rather than another
point reader. Source input is a legal origin-zero native checkpoint prefix
H_N=(x_0,...,x_N), containing N transitions of unchanged U. Its length supplies
the native generation counter. No future source input or feedback to U is
allowed. The growing archive is decoder output, NOT an added physical native
memory. A checked prefix uniquely determines every previously emitted record.

Registered source inputs: RELATIONAL-GROWTH-SATURATION-BOUNDARY [T] and
OCCURRENCE-ADDRESS-AND-LOG-EQUALITY [T]. Their optional torsion-free cover and
layer tags are retained as choices, not identified with finite native F5^6.
In particular the fired-commutator lift is NOT the silent-spatial-commutator
channel of TIME-CUT-READING and supplies no new curvature-forcing result.

Exact public source hashes:
- probes/P-RELATIONAL-GROWTH-SATURATION-1/PROOF.md:
  19435a7bd5b33f2b7995262c2dbfc8eb8fa36b6112723fe15dc957aed60ef5c4
- probes/P-SNAP-OCCURRENCE-IDENTITY-1/PROOF.md:
  81106a51b4b40da00f4f1eeff847159c9563d85288206275d2e2b841665b9a19
- probes/P-U-COUNTER-AMPLITUDE-CLASS-1/verify.py:
  d811afdd74cc11891282d93bf4575e7fc087a2ee209d74729e4ba1e3feb0e703
- notes/C-HODGE-EVENT-CAUCHY-N/model.py:
  adc99adac6ff1e3d9e76d4952b97af16fcdbe919021c5947bdb6c0feb7b3a772
- notes/C-HODGE-EVENT-CAUCHY-N/PROOF.md:
  6ebac7c63bcadba55791db017d273aa2136cdbf8867a72b3006c1d46bae823af

The last note's selected event geometry and scalar law are NON-CANONICAL
inputs. A composition here does not promote them. Fix one resolution h>=3
throughout each archive; enlarging a prefix never changes h or old coordinates.

## G1: from tagged hexagonal balls to actual lattice coordinates

Let H_r={(x,y) in Z^2:max(|x|,|y|,|x-y|)<=r}, r>=0. Put

    M=max(0,x,y), c=r-M,
    Phi(r,x,y)=(x+c,y+c,c).

Prove that Phi bijects H_r onto
{(a,b,c) in {0,...,r}^3:max(a,b,c)=r}, with inverse
(r,x,y)=(max(a,b,c),a-c,b-c). Thus the disjoint accumulated carrier of
all tagged H_r maps onto N_0^3 with completed radius-R cube (R+1)^3.
Do not infer an isometry from this bijection.

Select independent coordinate signs, identifying exactly equal signed triples
and requiring sign + at zero. This completion yields Z^3 with no duplicates.
Its centered cube C_R has (2R+1)^3 vertices and its radius-r shell has
24r^2+2 vertices for r>=1 (one vertex for r=0). Signing is an extra choice.

## G2: all-prefix native serialization and immutable geometry

At the start of each radius-r shell, freeze the bit b=i_a mod2 of the actual
native selected generator at the current generation index a. Within a shell,
order by the number of coordinates of absolute value r (ascending), then
lexicographically if b=0, reverse lexicographically if b=1. r=0 is the origin.
Append one spatial vertex record for every native transition. The record has
immutable integer coordinates, e_h(0,z), and all already present nearest
neighbors (at most six). Edges are append-only undirected records, added once
when their later endpoint arrives. Old edge endpoints/weights never change.

Prove all prefixes are connected and have distinct vertices; the first
N_R=(2R+1)^3 records cover exactly C_R. Every z in Z^3 appears at finite
index. A pure decoding of an extended legal source prefix restricts literally
to the old record list, including coordinates and all old edge records.
The native bit may change record order but must not change a completed cube.

## G3: fixed metric, rather than inferring dimension from a count

Use the inherited positive spatial projection P_s(v)=v-tau(v)t in E_+.
For q=e_h(0,z)-e_h(0,z') define

    d_h(z,z')^2=g(q,q)+ct*tau(q)^2.

This is NOT the unprojected Lorentz interval and NOT an evolving shortest-path
metric. The ideal comparison metric is

    d_0(z,z')^2=h^-2 sum_i a_i(z_i-z'_i)^2,
    ct=(2+sqrt5)/8,
    (a1,a2,a3)=(2sqrt5/5,6sqrt5/5,3sqrt5/2).

Using R0=10-9sqrt5/5<6 and the inherited rounding error, prove uniformly for
all integer z,z' and h>=3 that d_h is a metric and

    (5/9)d_0 <= d_h <= (13/9)d_0.

Consequently prove two-sided cubic growth of its metric balls at fixed h,
with fixed positive constants. Pairwise metric values remain unchanged on
all prefix overlaps. This proves a geometric property of a CHOSEN target,
not a derivation of physical dimension from native U.

## G4: dependency-closed spacetime and scalar field records

In a separate output mode, freeze

    K_R={(m,z):m>=0, m+||z||_infty<=R}.

Order increasing R, then increasing m within a shell, then the same signed
spatial shell order, with the shell's native selector bit frozen at opening.
Prove

    |K_R|=(R+1)^2(2(R+1)^2-1).

Emit actual e_h(m,z) and one scalar value. Freeze two finite-support F-valued
initial slices f0,f1, F=Q(sqrt5), and a separately supplied computable source
j_m(z) (zero by default). Use exactly the inherited recurrence

    f_m(z)=(2-2A)f_(m-1)(z)
            +sum_i alpha_i[f_(m-1)(z+ei)+f_(m-1)(z-ei)]
            -f_(m-2)(z)+h^-2 j_(m-1)(z),
    alpha=((5+2sqrt5)/16,(5+2sqrt5)/48,(5+2sqrt5)/60),
    A=sum alpha.

For m>=2 prove every predecessor is emitted earlier, even when it has the
same shell radius. Hence each value is computed once and agrees EXACTLY
with the unique infinite-grid solution on every K_R, without imposing an
artificial finite-box boundary. Old values never change under enlargement.
No inference of conservation on a truncated aperture is allowed without
its boundary flux. Inherited global energy/stability conclusions stay at
their original scope.

## G5: distinguish generation budget from geometric time

With at most c new ATOMIC vertex records per native transition, the exact
spatial completion cost is ceil((2R+1)^3/c). With at most c new ATOMIC
spacetime/field records it is ceil(|K_R|/c). The constructions attain these
bounds by batching their serial streams. A spatial slice costs order R^3;
this spacetime history costs order R^4. A single symbolic record describing
many vertices is outside this materialized-atom budget. Constant record count
does not assert constant bit size, arithmetic work, physical memory or
physical emission rate.

Generation index N is NOT event time m. In particular spatial records are
on slice m=0 and event patches include previously generated event times.
These are growing descriptions, not a claim that spatial matter is created
at the native publication tick. They do not satisfy the predecessor's
point-reader m=N alignment and are not presented as if they did.

## G6: explicit nonselection and source dependence test

In the broad class of computable finite metric-record families satisfying
causal prefix dependence, immutable overlaps, finite batch additions and
cubic spatial growth, prove that these conditions alone do not select a
geometry. Any preassigned computable nested finite family with the given
append budget can be read from native prefix length. Give inequivalent
squared-metric controls q0=dx^2+dy^2+dz^2 and q1=dx^2+2dy^2+3dz^2 with the
same vertex growth and distinct unit-distance multiplicities. These controls
are not claimed to satisfy the additional fixed Hodge-metric premise.

Audit multiple native heads: selector-dependent partial order may differ,
but completed spatial cubes and the selected limiting Hodge geometry do not.
Thus construction existence is not a native metric-selection theorem.
No physical Galois equivalence, window forcing or native dimension follows.

## Named candidate bridges and audit

CB-NATIVE-PREFIX-GEOMETRY: the declared L1 native-prefix input (optionally
presented as its derived L5 record) -> selected L2 finite metric data.
CB-GEOMETRY-FIELD-PREFIX: selected L2 labeled event patches -> L5 scalar
history records. These are candidate-D choices, not new public GATES.tsv
entries or closures. The decoder never feeds U.

Commit PREREG.md, generate.py and verify.py and publicly read back all three
before any scientific execution. Standard-library exact arithmetic only;
integers, Fraction and hash-pinned Q(sqrt5) arithmetic. Finite audit grids:
hex/signed shells through r=8, native spatial prefixes through C_3 on five
initial trace-phase heads, event metric controls at h=3,5,8, and field patch
K_4 against independent infinite-grid sparse recurrence for fixed rational
fixtures with/without forcing. Every prefix and predecessor is checked.
Universal conclusions require PROOF.md; no finite extrapolation or blind
independent-agent confirmation. Integrity/runtime failure is STOP; exact
counterexamples fire their frozen clauses without moved thresholds.

Only this candidate notes directory may change. No Canon, Registry,
Frontier, public gate, existing note, workflow or tool edits. The inherited
microscopic spacelike-response limitation, global D3/measure/polarization,
Galois physical selection, native realization, SI and curvature debts remain.
