# Native point-port capacity and sharp comparison bounds

**NON-CANONICAL proof draft. No earned public T/C status or formal run.**
Adapted and expanded from A. M. Thorn's Apache-2.0 issue #1036 proof,
accepted tree `462e9721ad4b9f60f2df6c98715b0bfcc1976425`, proof blob
`ab03fc5ab37ec787ea3794862a1a9b69048f0749`. This is a new adaptation,
not a byte-for-byte copy of that source. All scope and random-variable conditions in the
adjacent preregistration draft are part of the statements below.

## 1. Explicit target and inherited native quotient

Write a checkpoint as `x=(a,b,c,d,q,r)` over `F5`, and set
`Q(x)=(z,q,r)` with `z=a+b+c+d+q+r`. The five native generators are

```text
g0(x)=(b,a,d,c,q,r)
g1(x)=(-c,-d,-a,-b,-q,-r)
g2(x)=(2-c,1-d+r,2-a,1-b-r,1-q,-r)
g3(x)=(2-a,1-b,3-c,4-d,1-q,1-r)
g4(x)=(2-a,1-b,3-c,4-d,2-q,1-r).
```

Their exact induced quotient actions, by summing coordinates, are

```text
(z,q,r), (-z,-q,-r), (2-z,1-q,-r),
(2-z,1-q,1-r), (3-z,2-q,1-r).
```

The selected generator index is `(z+2 theta_n) mod 5`. Consequently Q
evolves autonomously for any common binary driver. These identities and
their all-time history consequence are inherited from
`probes/P-U-PREPARATION-EVENT-RECORD-1/NATIVE-PROOF.md`, sections 2, 5--7;
they are recalled to make the argument readable, not registered again.

For original label `p`, put `v=ell(p)` with `ell=(0,1,2,-2,-1)`,
`s=sum v`, `N=sum v_i^2`, `G=I-11^T/5`. On `p!=0`,

```text
m = v^T G v = N-s^2/5 > 0,
LOW mass = v^T (11^T/20) v = s^2/20,
beta(p) = s^2/[4(5N-s^2)].
```

Cauchy's inequality gives `s^2<=4N`; hence positivity and `0<=beta<=1`.
The original zero has both masses zero and the separate tag ZERO_SUPPORT.
Its normalized weight is undefined.

## 2. Universal application to fixed nonlinear point encoders

Let `f:P->F5^4` be fixed deterministic, and `k(p)=sum f(p) mod 5`.
For any fixed auxiliary value `xi`, equal k gives equal initial Q because
the ready is common. Quotient induction gives equal entire Q and A histories
for the common driver. The downstream processors start with equal states
and receive equal inputs. Induction therefore gives equal complete
transcripts, including outputs, resets, stops and silence. An arbitrary
measurable function of the full history also preserves this equality.

Couple comparisons using the same xi. Since its law is independent of p,
integration of the pathwise equality gives the same transcript laws for
all sources in a k fibre. For a fixed completion event E and LOW event L,
both `Pr(E)` and `Pr(L intersect E)` agree within each fibre. Whenever
`Pr(E)>0`, their ratio agrees. A zero completion probability at a supported
source does not meet the total completed-event request.

Thus every admitted LOW response is `r(p)=c_(k(p))`, with at most five
values. The same equality holds for any defined deterministic transcript
frequency. This does not claim five distinct responses at every ready;
some readies or encoders identify more sources. In particular the inherited
exceptional ready `(3,0)` has only four apparatus-history classes.

Direct target substitution gives

| Balanced vector | beta |
| --- | ---: |
| `(1,-1,0,0)` | 0 |
| `(1,0,0,0)` | 1/16 |
| `(1,1,0,0)` | 1/6 |
| `(1,1,1,0)` | 3/8 |
| `(2,1,1,2)` | 9/14 |
| `(1,1,1,1)` | 1 |

Six unequal required values cannot factor through five labels. This proves
the exact event-law obstruction without the full target census or a finite
trajectory run. It excludes a full cycle requiring this first event in the
declared class, without deciding all physically admissible apparatuses.

## 3. Finite target certificate with a complete combinatorial derivation

The prospective exact census is:

| beta | Multiplicity | beta | Multiplicity |
| ---: | ---: | ---: | ---: |
| 0 | 84 | 2/17 | 24 |
| 1/256 | 24 | 9/64 | 24 |
| 1/176 | 48 | 5/32 | 8 |
| 1/136 | 32 | 1/6 | 24 |
| 1/96 | 24 | 2/7 | 24 |
| 1/56 | 48 | 5/16 | 24 |
| 1/46 | 36 | 3/8 | 16 |
| 1/26 | 48 | 5/8 | 8 |
| 9/224 | 24 | 9/14 | 12 |
| 1/16 | 56 | 49/64 | 8 |
| 9/104 | 24 | 1 | 4 |

Here is a finite arithmetic certificate of completeness that does not use
a random ensemble or assume an equal-probability source law. For every
nonnegative tuple `(n_-2,n_-1,n_0,n_1,n_2)` of sum 4 except `(0,0,4,0,0)`,
form

```text
s = sum_(a=-2)^2 a n_a,
N = sum_(a=-2)^2 a^2 n_a,
b = s^2/[4(5N-s^2)],
M = 24 / product_(a=-2)^2 (n_a!).
```

There are `binomial(8,4)-1=69` tuples. Each represents exactly M coordinate
permutations and every supported balanced vector occurs once. Summing M
for each rational b gives the displayed table. Equivalently expand
`(1+X Y+X^-1 Y+X^2 Y^4+X^-2 Y^4)^4`; the coefficient of `X^s Y^N`
counts its vectors and maps to b by the same formula, with the constant
null removed. The total is `5^4-1=624`.

The draft verifier compares direct point enumeration, the 69-pattern
formula, and this explicit frozen table. The table and its finite
arithmetic evaluation still require independent review and formal audit
before any public status is assigned. The universal obstruction above
does not depend on trusting that evaluation. Twenty-two response values
are necessary for exact deterministic finite-message realization of beta;
this is not a Hilbert-space or physical mode-dimension claim.

## 4. Arbitrary deterministic encoding: epsilon = 9/128

Minimize `max_(p in P*) |beta(p)-c_(k(p))|` over arbitrary five-valued k
and `c_j in [0,1]`. Every such k can be encoded as native points, for
example by `f(p)=(k(p),0,0,0)`; this encodes only the message and need not
preserve the original source.

The six field-label sources `0014,0012,0112,1112,1222,1111` have weights

```text
0, 9/64, 2/7, 5/8, 49/64, 1.
```

Their adjacent differences are at least `9/64` (in particular
`2/7-9/64=65/448 > 9/64`, and `49/64-5/8=9/64`). Two must share a
response center; the triangle inequality gives worst error at least
`(9/64)/2=9/128`. This is an analytic lower certificate.

The following disjoint blocks cover all values of section 3:

| Block extremes | Center | Radius |
| --- | ---: | ---: |
| `[0,1/46]` | 1/92 | 1/92 |
| `[1/26,1/6]` | 4/39 | 5/78 |
| `[2/7,3/8]` | 37/112 | 5/112 |
| `[5/8,49/64]` | 89/128 | 9/128 |
| `[1,1]` | 1 | 0 |

All radii are at most `9/128`, so the lower bound is attained in the
five-response comparison. For a separate complete optimization audit,
sort the distinct target values; assigning each value to a nearest sorted
center cannot increase the error and yields consecutive blocks. A block
with extremes a,b has optimal center `(a+b)/2` and radius `(b-a)/2`.
Thus enumerating four cuts is complete. The independent diameter recurrence
`D(t,j)=min_(t-1<=i<j) max(D(t-1,i),a_j-a_(i+1))`, with `D(0,0)=0`,
gives the same optimum `D(5,22)/2`.

Actual A observation can transmit these five comparison messages at ready
`(0,1)`, counter zero: initial piston sums `0,1,2,3,4` give first A values
`(0,4),(1,4),(1,0),(2,0),(0,1)`, respectively. Decode that observation and
compare one externally supplied uniform integer in a common denominator
range with the selected rational center. The resulting formal LOW law is
the center. This demonstrates sharpness only in the deliberately relaxed
class with external randomization. It neither derives random occurrence
from U nor promises null recognition. The grouping is openly target-aware.

## 5. Faithful encoding: epsilon = 27/64 and a separate null obstruction

When f is a permutation of all 625 labels, each native sum fibre has 125
source preimages: choose the first three coordinates freely and the fourth
is fixed by the sum. Removing the original null leaves supported group
sizes `124,125,125,125,125` in some order.

First count exactly the weights strictly above `5/32`. This is equivalent
to `13s^2>25N`. For a mixed-sign vector reverse its global sign to make
s nonnegative, and retain only one negative entry `-d`, removing any others.
Removing the others increases s and decreases N, so cannot lower `s^2/N`.
Let A be the sum of at most three remaining positive entries. If s is zero
the desired bound is immediate; otherwise `A>=d`, `A<=6`, `d>=1`. Cauchy
gives positive squared norm at least `A^2/3`. With `t=A/d` in `[1,6]`,

```text
s^2/N <= 3(t-1)^2/(t^2+3) <= 25/13.
```

The last function has derivative `6(t-1)(t+3)/(t^2+3)^2>=0` and value
`25/13` at t=6. Thus mixed signs cannot give a strict high weight.
For common-sign vectors, one nonzero entry fails; two nonzero entries
pass exactly when their magnitudes agree. Every three-entry vector passes
(weights `3/8,2/7,5/16`), as does every four-entry vector (weights
`1,5/8,9/14,49/64`). The exact high count is

```text
2*binomial(4,2)*2 + 2*binomial(4,3)*2^3 + 2*2^4
= 24+64+32 = 120.
```

A message fibre containing a beta=1 source contains at least 124 supported
sources, so also one of weight at most `5/32`. A single response has
maximum error at least `(1-5/32)/2=27/64`.

For attainment, sort all supported labels by `(beta(p),p)` and partition
into sizes `124,125,125,125,125`. The prospective table gives the following
extremes and midpoint centers:

| Supported size | Extremes | Center |
| ---: | --- | ---: |
| 124 | `[0,1/176]` | 1/352 |
| 125 | `[1/176,1/56]` | 29/2464 |
| 125 | `[1/56,1/16]` | 9/224 |
| 125 | `[1/16,5/32]` | 7/64 |
| 125 | `[5/32,1]` | 37/64 |

Every radius is at most `27/64`, attained by the last block. Send each
block in order bijectively to the lexicographically ordered native fibre
of sums `0,1,2,3,4`, and send the null to the remaining last point of fibre
zero. This is a full 625-point permutation. The same ready `(0,1)` and
external uniform-variable construction of section 4 realizes the centers.

The five-case sorted-capacity audit is exhaustive: for `a<=b`, `c<=d`,
if crossed assignments `a->d,b->c` have errors at most e, then
`a>=d-e>=c-e` and `a<=b<=c+e`, while `b>=a>=d-e` and
`b<=c+e<=d+e`. Uncrossing to `a->c,b->d` does not increase error and
preserves every center's occupancy. Repeating yields consecutive blocks;
only the five positions of the 124-member block remain. The analytic lower
and explicit first placement already suffice for sharpness once the table
is checked; the extra placements are an audit, not a needed new claim.

Separately, every faithful encoder puts the null in a sum fibre with 124
supported sources. Their complete transcript laws agree. They cannot give
ZERO_SUPPORT almost surely for the null and SUPPORTED almost surely for
all the others. This exact classification obstruction never uses beta(0).

## 6. Scope and remaining acceptance work

The argument requires one fixed deterministic encoded native point, common
origin-zero timing, source-independent ready/randomness, the stated port
and unchanged U. A seed-dependent encoder, source-dependent stochastic
loading, source-dependent external acceptance or clock, another observed
coordinate, a native intervention or coherent multipoint preparation is a
different class. For example the source-dependent mixing law
`K(p)=(1-beta(p),beta(p))` with responses `(0,1)` succeeds by placing the
target in the loader; it is an explicit hypothesis-change control, not a
derived preparation. The coherent public Galois code is outside this proof.

The five-class extension, six-source obstruction, both analytic lower
bounds and faithful null obstruction have explicit proofs above. Acceptance
of the complete census and both sharp equalities also requires independent
review of the finite upper certificates and the newly pinned public audit.
No formal verifier has run in this preparation. No physical apparatus
owner, event law, material record/reset, physical selection or layer gate
is supplied, and no public claim is promoted by this document.
