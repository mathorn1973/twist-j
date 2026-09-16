# Proposed Public Canon v88 insertion

**NON-CANONICAL DRAFT.** Insert after the selected passive-family section
only after all three named public probes have complete immutable results,
independent review and required two-architecture checks. The proposed T
labels below are candidates. This file changes no active Canon or authority.

## Conditional predictions and memory of the selected passive family

The following results are conditional on the existing selected five passive
QDD maps. They neither force that choice nor complete a physical apparatus.
Write `Z={-2,-1,0,1,2}^4` for the image of the unchanged balanced head
map on K_QDD, with coordinates indexed 0 through 3. The rational formulas
on Q^4 are mathematical extensions, not extensions of the decoder domain.
With `u=(1,1,1,1)`, `chi=(1,-1,-1,1)` and `G=I-uu^T/5`, put

```text
P_t=uu^T/4, P_l=chi chi^T/4, P_r=I-P_t-P_l,
T=GP_t, L_q=GP_l, R=GP_r,
t=(sum_i z_i)^2/20, l=(z0-z1-z2+z3)^2/4,
r=((z0-z3)^2+(z1-z2)^2)/2, m=t+l+r.
```

The IDs and ordered blocks remain PI-ALL `((t,l,r))`, PI-TRACE
`((t),(l,r))`, PI-LEG `((t,r),(l))`, PI-PAIR `((t,l),(r))` and
PI-ATOMS `((t),(l),(r))`. A record retains exactly partition_id,
support_state, total_weight, ordered block_weights and
normalized_weight_state. At z=0 these are the literal ZERO_SUPPORT,
zero-total/zero-block and ZERO_DENOMINATOR fields. At z!=0 they are
SUPPORTED, positive total m, the block sums and NORMALIZED(raw/m).
Thus the PI-ATOMS record is equivalent to its raw tuple `(t,l,r)`;
all five records together contain the same information as that tuple.
No record field is removed or added by the results below.

### QDD-PASSIVE-QUADRATIC-CALIBRATION [T]

For every rational symmetric A, the homogeneous quadratic `z^T A z`
factors through the complete PI-ATOMS record on Q^4 exactly when
`A in span_Q(T,L_q,R)`. The same equivalence already holds on Z.
For arbitrary rational or real probability vectors on Z, supplied as
mathematical preparation data, the entire passive-record law requires
exactly seven further fixed scalar expectations to identify every
homogeneous quadratic mean. The lower bound allows arbitrary rational
functions Z->Q as the added scalar observables, fixed independently of the
unknown preparation law and validation output. It is a universal ensemble
expectation statement, not a minimum for one source or one target.

**Proof of the information boundary.** All four coordinate vectors have
equal atom records, forcing the four diagonal entries of A to one value d.
Equal records of `e0+e3,e1+e2` force `A03=A12=a`; equal records of
`e0+e1,e0+e2,e1+e3,e2+e3` force the other four off-diagonal entries to b.
These seven independent constraints use only points of Z. Conversely,

```text
A=5(d+a+2b)T+(d+a-2b)L_q+(d-a)R
```

has exactly those entries and its quadratic is the corresponding linear
combination of t,l,r on all Q^4. Let S be all rational functions on Z
constant on passive-record fibers and V all homogeneous quadratics.
The full record law supplies expectations for every function in S, which
includes the constant function. Coordinate and pair-sum evaluations give
`dim V=10`; the factor theorem gives `dim(S intersect V)=3`. Hence
`dim((S+V)/S)=7`. Each added scalar expectation supplies at most one
quotient dimension. Necessity holds for probability laws, not only formal
signed vectors: failure of row-span containment gives a rational kernel
vector of zero total and nonzero target pairing; sufficiently small positive
and negative rational perturbations of the uniform law remain strictly
positive and have equal calibrations but unequal target means.

A concrete seven-observable completion uses the existing conditional scalar
source and cold reservoir. Write ZZ for the integers and let
`D3={x in ZZ^3:sum_i x_i is even}`. Select the full displacement shells of
squared norms `(2,4,8,10,16)` with per-vector weights `(6,1,15,1,1)/324`.
Their sizes are `(12,6,12,24,6)` and total weight is 8/9. Let
`(L_s f)(x)=sum_d c_d[f(x)-f(x+d)]`, `H=2I-L_s`. At the five marked sites

```text
y=((0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0))
```

prepare `S(z)=sum_j ((z,0)_j-sum_i z_i/5)delta_(y_j)` and the two-slice
state `(0,S(z))`. A first cold port with conductance one has signed output
`b_x=-(H S(z))_x/3` and deposit `D_x=(h_x z)^2/9`, where

```text
(h_x)_i=sum_(j=0)^4 k(y_j-x)(1_(j=i)-1/5),
k(0)=10/9, k(d)=c_d on the stencil, k=0 otherwise.
```

The exact integer response rows `v_j=1620h_(x_j)` are:

| j | x_j | v_j |
|---|---|---|
| 1 | (1,1,0) | (-354,1416,-354,-354) |
| 2 | (1,0,1) | (-354,-354,1416,-354) |
| 3 | (0,1,1) | (-348,-348,-348,1422) |
| 4 | (2,0,0) | (-368,-343,-343,-373) |
| 5 | (-1,-1,0) | (8,53,-22,-22) |
| 6 | (-1,0,-1) | (8,-22,53,-22) |
| 7 | (-1,0,1) | (16,-14,-9,16) |
| 0 | (0,0,0) | (1421,-349,-349,-349) |

In monomial order `00,01,02,03,11,12,13,22,23,33`, let B(v) have diagonal
coefficients `v_i^2` and cross coefficients `2v_i v_j`. The ten-row integer
matrix with rows

```text
B(u), 5B(chi), 10[B(1,0,0,-1)+B(0,1,-1,0)], B(v1),...,B(v7)
```

has determinant `-176542678173169038600000000000000000`. The first three
rows are twenty times the atom forms; the last seven are 23619600 times
the deposit forms. Thus `t,l,r,D1,...,D7` form a quadratic basis, proving
that seven suffice. These first-step ports can coexist because each uses
the same prepared S and its own conductance. More generally the fixed cold
recurrence on a previous/current pair `(u,v)` is

```text
w_x=[2v_x-(L_s v)_x-(1-gamma_x/2)u_x]/(1+gamma_x/2),
b_x=-(w_x-u_x)/2 on active ports, D_x=gamma_x b_x^2,
E(u,v)=||v-u||^2/2+<u,L_s v>/2.
```

For a finite nonnegative rational conductance field, the active ports are
its positive support. The denominators are positive and fixed independently
of z. Finite support and the finite stencil
give finite support at each finite cut. Induction makes wave and port
coordinates linear, and deposits and remaining energy quadratic in z.
Their means are therefore determined for the same preparation law using
their actual context-specific quadratic forms.

For the unscaled tuple `x=(t,l,r,D1,...,D7)`, coefficient comparison gives
`D0=c x`, where

```text
c=(-6480865109/82312993800,
   6549292699/49387796280,6551015617/49387796280,
   -111027113/111030330,-111027113/111030330,
   -9409883/9409350,1556538/1568225,-11092/313645,-11092/313645,0).
```

The final zero means six added deposits suffice for this particular target;
seven is the minimum for all quadratic means. Componentwise additive errors
bounded by epsilon_a on each atom and epsilon_d on each deposit obey

```text
|delta D0| <= A epsilon_a+B epsilon_d,
A=84944136907/246938981400, B=751911453/185050550.
```

These are the absolute coefficient sums. Choosing the signs independently
attains the bound on the unrestricted additive error box. It bounds neither
sampling error nor geometry/conductance mismatch; comparison with a measured
origin adds that origin readout's own error allowance.

The information loss is concrete: e0 and e1 have the same full passive
family, with atoms `(1/20,1/4,1/2)` and total 4/5, but deposits
`2019241/23619600` and `121801/23619600` at the origin. At threshold 1/16
their first counts are one and zero. This extends the existing scalar
TRC1 collision to the newly selected finest record. It supplies no physical
preparation, calibrated port or occurrence law.

The standalone public audit is
`probes/P-QDD-PASSIVE-QUADRATIC-CALIBRATION-1`. Its proof and coefficient
certificates, not numerical sampling, establish the universal scope.

### QDD-PASSIVE-THRESHOLD-MOMENT-COMPLETION [T]

Fix the same source and one cold origin port with conductance one, zero
initial heat, one update and threshold `q=1/10`. Let E be **all** rational
preparation laws on Z whose entire passive-record law is the point law
with atoms `(0,1,5)` and whose raw second-moment matrix is

```text
Sigma=((1,0,-1/2,-1/2),(0,3/2,-3/2,0),
       (-1/2,-3/2,5/2,-1/2),(-1/2,0,-1/2,1)).
```

The exact attainable count laws on `(0,1,5)` are

```text
(Pr(C=0),Pr(C=1),Pr(C=5))=(3a,1-4a,a),
a rational, 0<=a<=1/4.
```

No other count occurs. Real preparation laws give the same real segment.
Consequently `1/4<=Pr(C>0)<=1` and `1<=E[C]<=5/4` are sharp, despite
equality of the complete passive law and every quadratic expectation.

**Proof and endpoint construction.** The passive-law condition is exactly
support in `F={z in Z:(t,l,r)=(0,1,5)}`. It implies s=0 and total six.
The origin row above gives `D0=(3481/26244)z0^2`. For y=z0^2 in {0,1,4},
exact flooring at q=1/10 gives C=0,1,5: `1<=34810/26244<2` and
`5<=139240/26244<6`. The fixed Sigma gives E[y]=1. If a=Pr(y=4),
normalization gives Pr(y=1)=1-4a and Pr(y=0)=3a, proving containment.
The following sources all lie in F:

| P source | mass | Q source | mass |
|---|---:|---|---:|
| (0,1,-2,1) | 1/2 | (1,-2,1,0) | 1/4 |
| (0,2,-1,-1) | 1/4 | (1,0,1,-2) | 1/4 |
| (2,0,-1,-1) | 1/4 | (1,1,-2,0) | 1/2 |

Their outer-product averages both equal Sigma; P has a=1/4 and Q has a=0.
For every admitted rational a, `4a P+(1-4a)Q` is an admitted rational
law attaining that point. This proves equality with the complete prediction
set rather than a bound for a restricted ansatz. Every quadratic mean is
fixed by Sigma, so additional mean energy calibrations cannot remove this
ambiguity in any fixed linear cold context.

One additional scalar expectation is necessary and sufficient to identify
this frozen count law. Take `M4=E[z0^4]`; then

```text
M4=1+12a, 1<=M4<=4,
(Pr(C=0),Pr(C=1),Pr(C=5))
  =((M4-1)/4,(4-M4)/3,(M4-1)/12),
Pr(C>0)=(5-M4)/4, E[C]=(11+M4)/12,
M4=(26244/3481)^2 E[D0^2].
```

These identities prove sufficiency. P and Q prove that zero additional
expectations cannot suffice. The minimum is for this target law and fixed
information class; it does not identify every source weight or arbitrary
future nonlinear response. The added observable is separate from the five
passive record fields and has no physical calibration certificate here.

Sigma is a raw second moment: P and Q have different means. Independently
replacing each atom z by equally weighted z and -z preserves every even
quantity used above and yields two zero-mean endpoints, where Sigma is also
the centered covariance. The ambient source includes zero and its zero
count. Its absence from F follows from the stipulated passive law; no
zero-count outcome is discarded or conditionally renormalized. The public
proof and exact audit are in `probes/P-QDD-PASSIVE-THRESHOLD-MOMENT-1`.

### QDD-PASSIVE-NATIVE-MEMORY [T]

Let `F_n(x)` be the actual checkpoint at counter n from native head `(0,x)`
and `rho_pi(x)=R_pi(kappa_x)` its original complete passive record. The
existing native chart theorem gives 3125 F3 fibers of five heads each, one
per initial phase z(x)=sum(x) mod5, and bijective transport of these fibers
between every later reachable sheet. For any preparation subset A and
fixed n>=3, an unaugmented current-checkpoint reader exists exactly when
rho_pi is constant on each F3 fiber intersected with A.

Every chosen partition and the joint family require exactly three added
distinguishable read-time states on the full domain or on supported heads
only, both for each n>=3 and for universal all-time readback. The upper
bound is the explicitly initialized static tag

```text
c(x)=0 for z(x)=0, 1 for z(x) in {1,2}, 2 for z(x) in {3,4},
U'(n,x,c)=(U(n,x),c).
```

This tag is added information, not a state variable present in unchanged U.

**Proof.** Equal current inputs must have equal outputs; constancy on F3
fibers is sufficient by the inherited inverse chart. With generator
composition read right to left, the first-three-tick phase maps are
`eca,d,e,dbd,dbe`; their inverse heads over y in the phase-one sheet are
`ace(y),d(y),e(y),dbd(y),ebd(y)`. The second and third have the same four
pistons, as do the fourth and fifth. The saved phase class selects the
original piston tuple, hence all passive records. For n<3, any conflicting
same-checkpoint/same-tag pair would remain conflicting after deterministic
continuation to F3, which is impossible. Thus the construction works at
every clock on correctly initialized reachable inputs.

For necessity, the supported origins
`(4,4,4,0,4,4)`, `(2,1,3,3,2,1)` and `(0,4,0,0,3,2)` all reach
`(0,0,0,1,0,0)` at n=3, but have original total weights `6/5,64/5,4/5`.
All five record schemas retain this field, so their three distinct outputs
require at least three auxiliary states. This bound permits an evolving
register and imposes no three-state requirement on n=0 alone.

The complete finite inventories are:

| ID | Initial distinct records | (2,2,1) fibers | (3,2) | (4,1) | (5) | Maximum preparations |
|---|---:|---:|---:|---:|---:|---:|
| PI-ALL | 19 | 2510 | 200 | 385 | 30 | 7310 |
| PI-TRACE | 35 | 2774 | 116 | 226 | 9 | 6845 |
| PI-LEG | 62 | 2922 | 58 | 142 | 3 | 6601 |
| PI-PAIR | 63 | 2924 | 56 | 143 | 2 | 6598 |
| PI-ATOMS | 65 | 2946 | 54 | 123 | 2 | 6556 |

Here the pattern lists sizes of equal-complete-record classes in an F3
fiber. To specify the census independently, let `y=(a,b,c,d,q,r)`, take
`a,b,c,d,r` freely in F5, and set `q=1-a-b-c-d-r`. The three inverse
piston classes, with multiplicities 1,2,2, are

```text
A=(d+3-r,c+4,b+4+r,a),
B=(2-a,1-b,3-c,4-d), C=(-c,-d,-a,-b).
```

For balanced pistons v, integer atom keys are
`T0=(sum v)^2`, `L0=5(v0-v1-v2+v3)^2`,
`R0=10((v0-v3)^2+(v1-v2)^2)`. The five partition keys are
`(T0+L0+R0)`, `(T0,L0+R0)`, `(T0+R0,L0)`, `(T0+L0,R0)` and
`(T0,L0,R0)`, respectively. These are twenty times their raw block tuples
and preserve complete-record equality at each literal ID. Summing the
four possible A/B/C equality indicators over the 3125 free tuples gives
the table, audited against all actual native trajectories by
`probes/P-QDD-PASSIVE-NATIVE-MEMORY-1`.

An admissible unaugmented preparation can choose at most one equal-record
class per fiber. Selecting a largest class in every fiber attains
`2n221+3n32+4n41+5n5`, proving the displayed maxima. The same maxima hold
with only supported heads: at most one of A,B,C can be the zero piston
tuple, its class has size at most two, and a supported multiplicity-two
class always survives. Removing zero heads therefore never reduces a
fiber maximum. These are cardinality optima, not selected physical
preparation laws. They also permit simultaneous unaugmented all-time
readback on the selected subsets by the same continuation argument.

The original head-retaining K_QDD decoder remains valid. This theorem
classifies recovery from a different, explicitly smaller current-state
input and a declared initialized extension. It implies no physical memory
cost, recording device, source occurrence or apparatus realization.

All three theorems concern conditional L1 mathematics. None selects a
physical preparation or effect, a post-state instrument, ready phase,
pointer, reset, event-completion law or occurrence measure. The three
physical QDD O owners, Bell accounting and every other existing live
decision clause remain unchanged. The physical comparison must separately
identify the source, port, clock, observable, preparation law and uncertainty.
