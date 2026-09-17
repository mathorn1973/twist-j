# Passive quadratic prediction and exact spatial calibration

**PROPOSED CONDITIONAL L1 MATHEMATICS / PROOF-FIRST.** This proof supplies
no physical source, detector, occurrence law, or Canon promotion. Formal
execution and acceptance belong to the separately pinned public records.
Earlier non-canonical mathematical explorations informed these formulas.
They are not empirical preregistration, blind validation or executions of
this public probe. The omitted origin is a held-out *algebraic input*, not
an unseen experimental dataset.

The baseline is Public Canon v87 at public main
`fd512f50d90382124e7c00afa926c8083fd56e06`. We use the selected passive
family and the stated scalar source/cold reservoir choices without changing
their domains or physical status. All definitions needed below are given
explicitly; the verifier imports no earlier verifier or external data.

## 1. Passive quadratic factorization, including the finite source

Put `u=(1,1,1,1)^T`, `chi=(1,-1,-1,1)^T`, `G=I-uu^T/5` and

```
P_t=uu^T/4, P_l=chi chi^T/4, P_r=I-P_t-P_l,
T=G P_t, L=G P_l, R=G P_r.
```

For `z in Q^4`, the atom weights are

```
t(z)=z^T T z=(sum_i z_i)^2/20,
l(z)=z^T L z=(z0-z1-z2+z3)^2/4,
r(z)=z^T R z=((z0-z3)^2+(z1-z2)^2)/2.
```

Their sum is `m=z^T G z`. Since `m>=||z||^2/5`, the coherent PI-ATOMS
record has exactly its existing five fields:

```
z=0:  (PI-ATOMS,ZERO_SUPPORT,0,(0,0,0),ZERO_DENOMINATOR),
z!=0: (PI-ATOMS,SUPPORTED,m,(t,l,r),NORMALIZED((t,l,r)/m)).
```

Equality is literal record equality. These records are equal exactly when
their three raw atom weights agree. Every other selected passive view is
a fixed coarsening, so the entire selected passive family carries no more
source information than this finest record. For the existing `K_QDD`, z
is exclusively its balanced head map beta; its image is
`Z={-2,-1,0,1,2}^4`. The Q^4 formulas are the proof extension, not a
decoder-domain extension.

**Factorization theorem.** For every rational symmetric four-by-four A,
the following are equivalent:

1. `z^T A z` is a function of the finest record on `Q^4`.
2. It is a function of that record already on Z.
3. `A=alpha T+beta L+gamma R` for rational alpha,beta,gamma.

**Proof.** Let e_i be the coordinate vectors. Their atom records agree,
so condition 2 forces `A00=A11=A22=A33=d`. The records of `e0+e3` and
`e1+e2` agree, forcing `A03=A12=a`. The records of
`e0+e1,e0+e2,e1+e3,e2+e3` agree, forcing their four matrix entries to one
value b. All those test vectors belong to Z. These seven independent
equalities leave exactly a three-dimensional matrix space. Direct matrix
substitution gives

```
alpha=5(d+a+2b), beta=d+a-2b, gamma=d-a.
```

Indeed the diagonal of `alpha T+beta L+gamma R` is d, its entries 03,12
are a, and its other four off-diagonal entries are b. Thus 2 implies 3.
Condition 3 gives `z^T A z=alpha t+beta l+gamma r` for every rational z,
so 3 implies 1; restriction gives 1 implies 2. Zero is included throughout.
This proof uses seven explicit coefficient constraints, not a finite-grid
extrapolation to an unproved universal polynomial statement.

## 2. Universal ensemble calibration requires seven further scalars

An ensemble here means any probability vector on the finite set Z, rational
or real as specified. It is a stipulated mathematical preparation law.
For a scalar function f on Z, a calibration returns its expectation.
Allow the entire passive-record probability law as initial calibration,
and allow additional expectations of arbitrary fixed rational functions
`f_1,...,f_k:Z->Q`. They may depend on neither the unknown ensemble nor a
validation outcome. The objective is to determine the expectation of
**every homogeneous quadratic** for every admitted ensemble.

Let F be the rational vector space of all functions on Z, S its subspace
of all functions constant on passive-record fibres, and V its subspace
of homogeneous quadratics. Giving the full passive-record law is exactly
giving expectations for S: its fibre indicators form a basis. In particular
S contains the constant function, so normalization is already included.
The ten monomials `z_i z_j`, `i<=j`, are independent on Z: evaluation at
e_i first fixes diagonal coefficients, then at e_i+e_j fixes the others.
Consequently `dim V=10`. Section 1 proves
`S intersect V=span(t,l,r)`, of dimension three. Hence

```
dim((S+V)/S)=7.
```

Here is the identifiability justification, including positivity. Write C
for a matrix whose rows are a basis of S followed by the k calibration
functions, evaluated on every point of Z. A target function q has the same
expectation for all probability vectors with equal C readings if and only
if q is in the row span of C. Sufficiency is direct linear combination.
For necessity, if q is outside this rational row span, rational elimination
gives d with `Cd=0` but `q d!=0`. Since C includes the constant function,
`sum d_i=0`. Starting with the uniform strictly positive probability vector,
choose a sufficiently small positive rational epsilon. The two vectors
`p_plus=p_uniform+epsilon d` and `p_minus=p_uniform-epsilon d` are still
strictly positive, have identical C readings and different q expectations.
This also disproves identifiability over real ensembles.

For all quadratic targets, therefore,
`V subset S+span(f_1,...,f_k)` is necessary and sufficient. The displayed
quotient dimension proves `k>=7`, even for arbitrary rational added scalar
functions rather than only quadratic ones. Section 4 constructs seven
fixed spatial deposited-energy functions that attain equality. Their exact
linear identities hold for rational and real probability vectors.

This is a lower bound for **universal ensemble expectation prediction**.
It is not a minimum number of scalars for a deterministic source, a single
target, a nonlinear encoding of an entire distribution into a real number,
or a calibration which returns a whole extra distribution as one scalar.
The matrix `E[zz^T]` is the raw second moment; no centered covariance
interpretation is required. Mean quadratic energies do not in general
determine threshold count laws or higher moments.

## 3. The chosen spatial response is derived independently of the target

Let `D3={x in integer triples:sum_i x_i is even}`. For each displacement d in the five
complete squared-length shells `(2,4,8,10,16)`, assign the respective
weight `(6,1,15,1,1)/324`. There are `12,6,12,24,6` displacements in these
shells, so their total weight is 8/9. Set

```
(L_wave v)(x)=sum_d c_d[v(x)-v(x+d)], H=2I-L_wave.
```

Choose the five marked source sites

```
y0=(0,0,0), y1=(1,1,0), y2=(1,0,1),
y3=(0,1,1), y4=(2,0,0).
```

With `s=sum_i z_i`, prepare `S(z)` with coefficient `(z,0)_j-s/5` at y_j
and zero elsewhere, and the wave pair `(previous,current)=(0,S(z))`.
The conditional cold reservoir at a site x has conductance gamma=1 and
zero incoming port. Its first update is

```
w(x)=(H S(z))(x)/(1+1/2), b(x)=-w(x)/2,
D_x(z)=b(x)^2=(h_x z)^2/9, h_x z=(H S(z))(x).
```

Off active ports the update is free. Distinct ports may coexist for this
first step: each output uses only the same prepared S and its own fixed
conductance. Later histories depend on the complete conductance context;
no interchangeability of later contexts is asserted.

The spatial row is obtained directly from the source and stencil. If
`k(0)=10/9` and `k(d)=c_d` for stencil displacements (zero otherwise), then

```
(h_x)_i=sum_(j=0)^4 k(y_j-x)(1_(j=i)-1/5).
```

The following exact integer rows are `1620 h_x`:

| index | site x | integer response row |
|---|---|---|
| 1 | `(1,1,0)` | `(-354,1416,-354,-354)` |
| 2 | `(1,0,1)` | `(-354,-354,1416,-354)` |
| 3 | `(0,1,1)` | `(-348,-348,-348,1422)` |
| 4 | `(2,0,0)` | `(-368,-343,-343,-373)` |
| 5 | `(-1,-1,0)` | `(8,53,-22,-22)` |
| 6 | `(-1,0,-1)` | `(8,-22,53,-22)` |
| 7 | `(-1,0,1)` | `(16,-14,-9,16)` |
| 0 | `(0,0,0)` | `(1421,-349,-349,-349)` |

Substitution into the finite sum proves every entry. The verifier builds
the stencil both by squared-norm filtering and by signed permutation
orbits. It also independently prepares the four source basis fields,
applies the full Laplacian and cold step, and compares the signed responses
and squared deposits at all eight sites. The fixed rows are therefore
checked against field-level dynamics, not only against each other.

## 4. Seven spatial expectations complete the quadratic basis

Order the ten monomials as
`00,01,02,03,11,12,13,22,23,33`. For a four-vector v let B(v) be the
coefficient row of `(v z)^2`: its diagonal entries are `v_i^2` and its
off-diagonal entries are `2v_i v_j`. Put
`a=(1,0,0,-1)`, `b=(0,1,-1,0)`. Define the explicit integer matrix M
by the ten rows

```
B(u), 5 B(chi), 10[B(a)+B(b)],
B(v1), B(v2), B(v3), B(v4), B(v5), B(v6), B(v7),
```

where v_j are the seven table rows. Its determinant is the integer identity

```
det M = -176542678173169038600000000000000000 != 0.
```

This is an explicit finite rational certificate: M scales the three atom
rows by 20 and the seven deposited-energy rows by 23619600, since
`9*1620^2=23619600`. The determinant can be checked by the fraction-free
recurrence `a'_ij=(a_kk a_ij-a_ik a_kj)/p`, where p is the preceding pivot
(initially one), exchanging rows when a pivot vanishes and retaining its
determinant sign. The displayed rows specify the entire certificate with
no external fixture. The verifier checks the integer determinant and,
independently, rank ten by rational elimination of the unscaled matrix.

Nonzero determinant proves that `t,l,r,D_1,...,D_7` form a basis of the
ten homogeneous quadratics on Q^4. Their expectations determine every
quadratic expectation. In particular, for any fixed finite linear cold
reservoir context, the complete cold recurrence on the previous/current
pair `(u,v)` is

```
w_x=[2v_x-(L_wave v)_x-(1-gamma_x/2)u_x]/(1+gamma_x/2),
b_x=-(w_x-u_x)/2 on active ports, D_x=gamma_x b_x^2,
E(u,v)=||v-u||^2/2+<u,L_wave v>/2.
```

The finite rational conductance field gamma is nonnegative, and the active
ports are its positive support. Every denominator is positive and fixed
independently of z. Finite-support preparation and a finite stencil give
finite support at every finite cut. Induction therefore makes every wave
and port coordinate linear in z, and every accumulated deposit and remaining
energy quadratic in z. All their means are consequently quadratic
expectations. This establishes sufficiency under the same stipulated
preparation ensemble and context-specific evolution. It supplies no
experimental estimate, error distribution, or occurrence law.

Together with section 2 this proves the exact universal number seven.

## 5. An explicit omitted-origin prediction and additive error certificate

Let `x=(t,l,r,D_1,...,D_7)` consist of the **unscaled** readouts, in the
table order. Coefficient-by-coefficient polynomial equality gives

```
D_0=c x,
c=( -6480865109/82312993800,
     6549292699/49387796280,
     6551015617/49387796280,
     -111027113/111030330,
     -111027113/111030330,
     -9409883/9409350,
      1556538/1568225,
     -11092/313645,
     -11092/313645,
      0 ).
```

One verifies the identity by multiplying c into the ten specified
coefficient rows and obtaining `B(v0)/23619600`. This proves it for every
rational z, and averaging proves it for every stipulated ensemble. The
verifier also solves for c independently and audits all 625 balanced z.
The final coefficient vanishes: six added deposit readings suffice for
this particular origin target. This does not weaken the seven-reading
minimum for the universal target class in section 2.

Suppose each of the three unscaled atom errors is bounded in absolute
value by epsilon_a and each unscaled deposit error by epsilon_d. Then the
prediction error obeys

```
|delta D_0| <= A epsilon_a+B epsilon_d,
A=84944136907/246938981400,
B=751911453/185050550,
A+B=64211196595109/14569399902600.
```

**Proof.** A and B are exactly the sums of absolute values of their
respective coefficient groups. The triangle inequality gives the bound.
Choosing each error at its allowed radius with the sign of its coefficient
attains equality. Thus the bound is sharp on the unrestricted componentwise
additive error box. It need not be sharp on a narrower correlated or
physically attainable error set. For a comparison to an observed origin
readout with error epsilon_0, the rejection allowance must additionally
include epsilon_0. No sampling rate, conductance/geometry mismatch bound,
or optimal experimental design is inferred from this algebraic certificate.

## 6. Finest-record equality does not determine spatial deposition

For the admitted balanced sources `e0=(1,0,0,0)` and `e1=(0,1,0,0)`, the
common finest record has total `4/5`, raw atoms `(1/20,1/4,1/2)` and
normalized atoms `(1/16,5/16,5/8)`, with the same literal ID and SUPPORTED
tag. Thus all selected coarsenings also agree. Yet the single cold origin
context above gives

```
D_0(e0)=2019241/23619600,
D_0(e1)= 121801/23619600.
```

At the fixed threshold `q=1/16` their first lifetime counts are one and
zero respectively. This follows by exact integer comparison with q and
2q. The two-point example was already present at a coarser scalar level in
the inherited TRC1 result; its role here is to show that the collision
persists after the new finest atom record is fixed, not to claim historical
novelty for the source pair. No independence, trial count or physical
frequency interpretation is added to the mathematical threshold rule.

## 7. Scope of the proposed theorem

The result concerns L1 algebraic factorization and finite-source ensemble
identifiability, with a concrete conditional spatial calibration and an
exact additive error identity. It preserves the existing K_QDD domain,
balanced head factorization, five-field passive schema and the separate
ALGEBRAIC-DMATTER record. It introduces no additional passive record field.
The seven extra readouts are separate calibration functions.

The chosen source injection, stencil, cold ports, clock convention and
preparation law are not derived physical identifications. No physical
effect, instrument, pointer, source opportunity, reset, terminal event,
occurrence law, frequency convergence or L1-to-L4/L5/L6 lift is supplied.
The QDD apparatus, terminal-event and complete-family obligations remain
open. Physical adoption is neither accomplished nor disproved by this
mathematical proof.
