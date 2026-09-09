# Canon proposal: selected hybrid closure of FRW-INHOM

**NON-CANONICAL / CANON PATCH PROPOSAL / ANALYTIC PROOF / NO STATUS CHANGE**

```text
proposal object: C-FRW-INHOM-HYBRID-CLOSURE-D
authority basis: Public Canon v82
public main basis: 1926ad238da998c6dbeac215ab526bf3c628ee72
content commit: 4e65adf0b483311d2a031cf2a23a65f2caf5af8a
canon tag: canon-v82
historical owner: FRW-INHOM [O]
proposed disposition: FRW-INHOM O -> D at the displayed selected scope
proposed definition: DEF-K1-HYBRID-FRW-CELL-METRIC, L1
proposed reading: K1-HYBRID-FRW-CELL-METRIC-DICTIONARY
proposed gate: GATE-L1-L2-K1-HYBRID-FRW-CELL-METRIC, DICTIONARY_LIFT
new registered claim identifiers: NONE
new formal probe or execution: NONE
```

This proposal makes the author-authorized construction and its complete
analytical justification public before a separate fold. The current Canon,
Registry, Frontier, and gates are unchanged. Every D status and closed
dictionary gate displayed below is proposed fold content.

## Historical decision and proposed disposition

The current [FRW-INHOM row at the public basis](https://github.com/mathorn1973/twist-j/blob/8806e298ca4ca453bcd64ba866d230a1f57c38ff/canon/REGISTRY.tsv)
has scope `the inhomogeneous sector, the named classical horizon` and
the exact decision clause:

> closes positively by an inhomogeneous source construction that reproduces the public FRW-CANONICAL-FORM identities in the homogeneous limit; closes negatively if every inhomogeneous extension breaks the exact chain of twelves

The proposed disposition is **positive at D for the one explicitly
selected hybrid reading below**. The action has nonzero spatially
inhomogeneous K1 fields, derived local energy/current, and solved scalar
and vector constraints. One common variational functional also supplies
the sourced continuous homogeneous background for all future time.
Removing the inhomogeneous fields gives the public FRW action literally,
for arbitrary admitted homogeneous matter.

This supplies the existential positive construction required by the
historical clause. It does not attempt the universal negative branch or
a classification of every gravitational reading. D records adoption of
this concrete geometry and clock dictionary; the accompanying algebra
does not establish a physical occurrence law, full GR, or unique reading.

The author has authorized explicit selection of this construction without
using any target observation. Its source words, output carriers, equality,
unit chart cells, branch, action, and overlap boundaries are fixed in
the insert. The complete admitted source class is the ten unchanged K1
words at the stated context; no selector depends on a measured result.
Only FRW-INHOM is proposed to leave the live Frontier. TT-SOURCE and
TT-VECTOR-STATE-NORMALIZATION retain their complete O decision clauses.

## Evidence and its exact division of scope

[PR #925](https://github.com/mathorn1973/twist-j/pull/925) merged the
frozen `P-FRW-INHOM-K1-BACKREACTION-3` result at
`8806e298ca4ca453bcd64ba866d230a1f57c38ff`. Its accepted pin remains
`1f3a3d5b074547991919ad52824d6c7f6f591550`. The committed
[RESULT.md](https://github.com/mathorn1973/twist-j/blob/8806e298ca4ca453bcd64ba866d230a1f57c38ff/probes/P-FRW-INHOM-K1-BACKREACTION-3/RESULT.md)
records PASS-CONSTRUCT for the specified typed source construction.
The [final-head CI run](https://github.com/mathorn1973/twist-j/actions/runs/34343106636)
at `09591da8eb32c58db7a3ba81f8b5229f8a6525a8` completed both
`architecture-x86_64` and `architecture-aarch64`, including their
changed-probe replay steps, and the aggregate `check` successfully.

That probe supports its frozen source, balance, coefficient and constraint
statements. Its G9 is the source-off restriction; it does not certify the
new cell bridge or the jointly sourced continuous history. The latter
have the complete independent analytic proof in the insert below.
No new result is assigned to #923, and no frozen verifier or result is
edited or reinterpreted here.

[The public K1 theorem](https://github.com/mathorn1973/twist-j/blob/4e65adf0b483311d2a031cf2a23a65f2caf5af8a/canon/CANON.md)
supplies the unchanged initial data, recurrence and uniform signature
bound. The [public gravity-chain action](https://github.com/mathorn1973/twist-j/blob/8806e298ca4ca453bcd64ba866d230a1f57c38ff/reproduce/gravity-chain/verify.py)
supplies FRW-CANONICAL-FORM. The
[one-point composition](https://github.com/mathorn1973/twist-j/blob/8806e298ca4ca453bcd64ba866d230a1f57c38ff/notes/V82-FRW-K1-HOMOGENEOUS-2JET-COMPOSITION-1.md)
contains the local first-variation reading; this proposal specifies its
vacuum continuation through the single joint action.

POLICY section 4 permits a self-contained exact proof in the Canon.
That is the evidence route for the new joint existence result. The chosen
lift is separately and explicitly a DICTIONARY_LIFT, rather than a
computation-only T claim. This note adds no executable or scientific
run. Existing repository checks and release checks remain required.

## Exact Canon insert

Insert the complete block in section 13, `Gravity and cosmology`,
before section 14. The block has no development chronology and is the
proposed normative statement. The companion fold removes only the
FRW-INHOM live Frontier entry and updates references to its former open
status at this exact adopted scope.

<!-- BEGIN FRW-INHOM HYBRID CANON INSERT -->
### DEF-K1-HYBRID-FRW-CELL-METRIC

This definition fixes one mathematical construction on the unchanged ten-word
K1 packet of `DEF-K1-LINEAR-METRIC`, at its fixed unit amplitude. The source
word, both local initial squares and the public rational propagator are
retained. `K1-LINEAR-METRIC-COMPLETION` supplies the exact all-counter bound
used below; its independent proof and original L1 scope remain in section 14.

The additional choices are the cell-integrated homogeneous lapse, its
attachment to the discrete source, the absence of homogeneous scale factors
in the TT/constraint terms, the expanding vacuum background, and the metric
reading defined below. They are explicit dictionary choices, not consequences
of the axiom. The mathematical functional is an L1 definition; only the
separately named gate of `FRW-INHOM` adopts its stated L2 output.

The cubic polynomial in the inhomogeneous fields and multipliers is the exact
defining functional of this restricted hybrid model. It is not an
approximation asserted to control the remainder of a larger gravitational
action. No all-order local gauge symmetry, Einstein-Hilbert identification
or physical TT radiation equation of state is assumed.

#### Carriers, time cells, and the action domain

Let `X=(Z/5)^3`. An oriented edge is `(x,a,k)` with tail `x` and head
`x+k e_a`, for `a=1,2,3` and `k=1,2`. Define

```text
(Bf)(x,a,k)=f(x+k e_a)-f(x),
w_1=29/324, w_2=65/324, W=diag(w_k),
<f,g>_V=(1/25) sum_X f g,
<u,v>_E=(1/25) sum_edges u v,
L3=B^top W B, V0=<1,1>_V=5.
```

`B^top` is the adjoint for these products. The graph is connected, all weights
are positive, and `ker L3` consists exactly of constants. Consequently `L3`
is invertible on the mean-zero vertex space `V_perp`. Its inverse there is
rational in a rational basis. Write `Pi_0` for subtraction of the spatial
mean and `K_E=ker B^top` for the co-closed edge space.

The planar embedding is `(iota f)(x)=f(x_3)`. Direct substitution gives

```text
<iota f,iota g>_V=sum_(r in Z/5) f(r)g(r),
L3 iota=iota L,
L=[188I-29(S+S^-1)-65(S^2+S^-2)]/324.
```

There are two distinct time carriers:

* Continuous chart time `t>=0` carries the homogeneous fields
  `chi(t)=log a(t)` and `nu(t)>0`. They are locally smooth enough for the
  displayed variations; `chi` and `nu` may be taken smooth. This chart has
  no SI calibration.
* Integer and half-integer labels carry the finite-space fields. `h_n` is
  a vertex field at integers; `tau_(n+1/2)` and `ell_(n+1/2)` belong to
  `V_perp`; `p_n` belongs to `K_E`, and the shift multiplier `N_n` is an
  arbitrary edge field, at integers `n>=1`.

The new, explicit bridge is

```text
I_n=[n,n+1],
eta_n=integral_(I_n) nu(t) dt,
ell_hom,n=eta_n-1.
```

Here a counter step is assigned one unit of the chosen coordinate chart,
and `eta_n` is its homogeneous lapse integral. This is a mathematical
clock dictionary. It does not assert that the native counter already was
measured cosmic time. The distinguished solution uses `nu=1`, so every
cell has unit proper-time length in this dictionary. The local fields are
not silently interpolated into continuous functions of `t`.

For precision, define the action first on `[0,T_max]` with integer `T_max>=2`.
TT links and half-slice variables have `0<=n<T_max`; integer shift and
co-closed variables have `1<=n<T_max`. Fix the homogeneous and TT endpoint
values when varying. The TT field at an interior integer is varied
independently before selecting its initial data. Lapse variations have
compact support in `(0,T_max)`. Other interior variations are arbitrary in
their declared linear spaces. No `h_-1`, `tau_-1/2`, or `j_0` is consumed.

The future-time action means stationarity against finite-support
variations, equivalently these compatible finite restrictions. It does
not mean that an infinite numerical action sum converges. There is no
boundary equation imposed at `t=0` in addition to the chosen initial data.

#### Discrete source and the single joint action

For `0<=n<T_max` and `1<=m<T_max`, put

```text
d_n=h_(n+1)-h_n,
g_n=B h_n,
q_m=h_(m+1)-h_(m-1),
R_m=h_(m+1)-2h_m+h_(m-1)+L3 h_m,

e_(n+1/2)(x)=d_n(x)^2/2
  +(1/4) sum_(edge e incident to x) w_e g_(n+1)(e)g_n(e),
j_m(e)=(w_e/4)g_m(e)[q_m(tail e)+q_m(head e)],

E_n=<1,e_(n+1/2)>_V
   =(1/2)[<d_n,d_n>_V+<h_(n+1),L3 h_n>_V],
P_m=WB[tau_(m+1/2)-tau_(m-1/2)]+p_m.
```

The endpoint polarization gives the exact identities

```text
e_(m+1/2)-e_(m-1/2)+B^top j_m=(q_m*R_m)/2,
E_m-E_(m-1)=<q_m,R_m>_V/2.
```

For example, the kinetic difference is
`q_m(h_(m+1)-2h_m+h_(m-1))/2`. On each oriented edge, the difference
of the endpoint-split spatial product plus the incidence divergence is
the endpoint contribution to `q_m L3 h_m/2`. Summing edges proves the
pointwise identity; summing vertices cancels the divergence. This is an
algebraic identity, without a statistical or continuum approximation.

Let `rho_m(chi)` be any smooth matter density function admitted by the
public homogeneous action. It is a fixed matter input, independent of
the K1 word. The common functional is

```text
S_(T_max) = S_FRW,T_max[rho_m] + (1/(2 lambda)) A_(T_max),
lambda=216 pi,

S_FRW,T_max[rho_m] = V0 integral_0^T_max dt nu exp(3chi)
                 [-(3/lambda)(dot chi/nu)^2-rho_m(chi)],

A_(T_max) = sum_(n=0)^(T_max-1) {
        (1/2)[<d_n,d_n>_V-<h_n,L3 h_n>_V]
        -(eta_n-1) E_n
        +2<ell_(n+1/2),L3 tau_(n+1/2)>_V
        -<ell_(n+1/2),e_(n+1/2)>_V
      }
      +sum_(m=1)^(T_max-1) {
        2<N_m,P_m>_E+<N_m,j_m>_E
      }.
```

This is the only action chosen here. There is no additional
`-integral nu E/(2 lambda)` term and no additional homogeneous
`-ell_hom E/(2 lambda)` term. The source occurs exactly once.

In particular, replacing `-(eta_n-1)E_n` by `-eta_n E_n` is not harmless:
`E_n` is a quadratic functional of the varied `h`, not a constant during
that variation. At `eta=1` the displayed coupling has zero `h` variation
while retaining its nonzero lapse variation. This is why the original K1
equation survives. No on-shell substitution is made before variation.

The TT and local constraint terms contain no `chi`. This absence is an
explicit continuation choice of this dictionary, not a claim about how an
actual gravitational wave redshifts.

The action is local on the declared discrete time cells and graph, with
the homogeneous lapse integrated over its own cell. It is not presented
as a pointwise continuous Lagrangian density in all fields. In particular,
no continuous velocity is assigned to `h` or `tau`.

#### Explicit selected solution and every field variation

The total explicit decoder below has one of the ten unchanged K1 words
as its input, and fixes vacuum matter `rho_m=0`. The action also has the
source-off restriction for arbitrary `rho_m` proved below; that functional
statement does not require a total decoder for arbitrary
matter histories.

For a word `w=(w_0,w_1,w_2,w_3)`, retain

```text
u_t=w_(t+2)-w_t,
h_t=iota[(delta_(r,u_t)+delta_(r,u_t+1))/2], t=0,1,
h_(n+1)=(2I-L3)h_n-h_(n-1), n>=1.
```

This is the unchanged planar K1 evolution at every integer. Its rational
initial pair and rational recurrence give one rational history.
Conservation gives `E_n=E(w)` at every link. Direct substitution in the
initial pair gives

| abs(u_1-u_0) | E(w) |
| --- | --- |
| 0 | 53/432 |
| 1 | 713/2592 |
| 2 | 67/162 |

For displacement zero, `<h_0,Lh_0>=53/216` and `d_0=0`. For displacement
one the squared difference and cross pairing are `1/2` and `65/1296`.
For displacement two they are `1` and `-14/81`. These give the three
entries and prove strict positivity for every word. No occurrence law is
needed. Local `e(x)` is not claimed pointwise nonnegative.

Define for every link and interior integer

```text
tau_(n+1/2)=(1/2)(L3|V_perp)^(-1) Pi_0 e_(n+1/2),
p_m=-j_m/2-WB[tau_(m+1/2)-tau_(m-1/2)],
ell_(n+1/2)=0, N_m=0, nu(t)=1.
```

The energy balance and the two adjacent tau equations imply `B^top p_m=0`.
Thus `p_m` belongs to the space in which it is varied; this is not an
extra projector applied to discard an unsatisfied source component.
All these records are rational and determined by the marked K1 history.

The continuous background is

```text
H0=sqrt(E/(6V0))=sqrt(E/30), choosing the positive root,
F(t)=1+(3/2)H0 t,
a(t)=F(t)^(2/3), chi(t)=(2/3)log F(t),
H(t)=H0/F(t), nu(t)=1, t>=0.
```

`F(t)>0` for all future time, so this background exists smoothly on the
entire stated domain. No finite upper time cutoff is selected from data.
At `t=0`, `H^2=E/30`, `dot H=-E/20`, and `ddot a=-E/60`.
Consequently `a(t)^2=1+2sqrt(E/30)t+(E/60)t^2 mod t^3`. The action
selects the displayed entire continuation; a local 2-jet alone does not
uniquely select it.

All variations are checked on this representative, after retaining the
full independent variables in the action:

**TT field.** At `eta=1`, `ell=N=0`, the first variation with respect to
an interior `h_m` is `-<R_m,delta h_m>_V/(2 lambda)`. The source-coupling
variations vanish because their multipliers vanish. The recurrence makes
every such variation zero.

**Mean-zero lapse.** Its equation is exactly
`2L3 tau_(n+1/2)-Pi_0 e_(n+1/2)=0`, solved by the displayed unique tau.

**Shift.** Its equation is exactly `2P_m+j_m=0`, solved by the displayed
co-closed `p_m`, including any harmonic or coexact current.

**Co-closed field.** Variation inside `K_E` gives
`2 Proj_(K_E) N_m=0` in the declared unweighted edge product. It holds
because `N_m=0`.

**Tau.** With absent endpoint shifts interpreted only for this equation
as `N_0=N_(T_max)=0`, its expression before the common factor is

```text
2[L3 ell_(n+1/2)+B^top W(N_n-N_(n+1))].
```

It lies in `V_perp` and vanishes for `ell=N=0`. This includes the first
and last half-slice equations of every finite restriction.

**Continuous homogeneous lapse.** An arbitrary smooth variation inside
a time cell has `delta eta_n=integral_(I_n) delta nu dt`. Holding the
independent `h` variables fixed during this variation gives

```text
delta_nu A_(T_max)=-sum_n E_n integral_(I_n) delta nu dt.
```

Since the selected K1 solution has the same E on every cell, this is
exactly `-integral_0^T_max E delta nu dt`, including variations that cross
cell boundaries. There are no point impulses at the boundaries. The
resulting homogeneous equation is

```text
3H^2=lambda rho_m(chi)+E/(2V0 a^3).
```

It is an equation obtained from the one common action, not an equation
added afterwards. On the explicit vacuum solution,
`a^3=F^2` and `3H0^2=E/(2V0)`, so it holds for every `t>=0`.

**Homogeneous scale.** The discrete terms have zero chi variation. The
remaining equation, in the selected proper-time gauge, is

```text
(6/lambda) dot H+(9/lambda) H^2-3rho_m-partial_chi rho_m=0.
```

In vacuum `dot H=-(3/2)H^2`, which proves this equation for every future
time. Therefore every independent field equation of `S_(T_max)` holds on
every finite restriction of the selected history.

This proves existence of a solution of the full stated hybrid variational
model, not uniqueness of every solution of that action. The explicit
decoder is unique after its input, branch, gauge, initial scale, clock
bridge, and representative have been selected.

#### Source interpretation, conservation, and canonical background

On the proved representative the homogeneous equations can be written
using

```text
rho_K(t)=E/(2 lambda V0 a(t)^3), p_K(t)=0,
rho_total=rho_m+rho_K,
partial_chi rho_K=-3rho_K.
```

The constant comoving source is a consequence of the selected action and
its on-shell K1 conservation. Thus the homogeneous fixed-charge
functional `S_FRW[rho_m]-integral nu E/(2 lambda)` reproduces the
homogeneous variations on this solution. It is **not** asserted to be a
Routh reduction of the full TT action; it must not be added to that action.

The scale equation is exactly the public scale equation for this total
source because `3rho_K+partial_chi rho_K=0`. Define the matter pressure
as in the public homogeneous continuity clause,
`p_matter=-rho_m-(partial_chi rho_m)/3`, distinct from the edge field `p_m`.
The total source then obeys

```text
dot rho_total=-3H(rho_total+p_matter),
2dot H=-lambda(rho_total+p_matter),
3H^2=lambda rho_total.
```

These identities apply wherever the proved on-shell constant E and a
homogeneous solution occur; the explicit global witness is vacuum.
For that witness they hold at every future time, with `p_matter=0`.

The homogeneous canonical variables on the witness are

```text
pi_chi=-6V0 a^3 H/lambda=-6V0 H0 F/lambda,
C_H=-lambda pi_chi^2/(12V0 a^3)+V0 a^3 rho_total=0,
dot pi_chi=-3E/(2lambda).
```

Both public homogeneous Hamilton equations follow from these expressions.
This is the canonical description of the homogeneous solution and source;
it does not claim a fully continuous Hamiltonian formulation of all the
discrete fields. The public `lambda=216 pi`, `lambda/3=72 pi`, chain
`864=12*72=4*216`, and forced fiber identity remain unchanged dependencies.

The local constraint propagation is exact at every interior integer:
the two tau equations and
`e_(m+1/2)-e_(m-1/2)+B^top j_m=0` imply the required co-closed momentum
solution. No large-time estimate replaces this identity.

The source balance and the complete first-variation calculation prove the
stated existence and propagation assertions. They make no claim of an
all-order local gauge symmetry for the exact cubic action.

#### Literal source-off action and compatible restrictions

For arbitrary homogeneous fields `chi,nu` and arbitrary admitted
`rho_m(chi)`, set all inhomogeneous fields to zero:

```text
h=0, tau=0, p=0, ell=0, N=0.
```

Then `d=e=j=E=P=0` and the full functional restricts **literally** to
`S_FRW,T_max[rho_m]`. This holds before any homogeneous equation or vacuum
specialization. It recovers every public homogeneous identity by the
same variations and the same constants, not merely one numerical
Friedmann equality. At this restriction the inhomogeneous first
variations vanish as well, so any admitted public homogeneous solution
embeds as a source-off solution of the hybrid model.

The formal source-off object is not an eleventh K1 word or an adjustable
K1 amplitude. In the explicit vacuum decoder it has `E=0`, `H0=0`,
`a=nu=1`, giving the Minkowski background and emitted matrices.

For two finite endpoints `T_max<T_max'`, the continuous solution restricts from
`[0,T_max']` to `[0,T_max]`; the discrete arrays restrict to exactly the links
and interior integers of the action domain above. Each tau depends on its
own link source and each interior p on its adjacent links. No constructor
uses the final horizon. Thus the solution family and its marked outputs
are compatible under every such restriction.

#### Named metric reading and equality

`K1-HYBRID-FRW-CELL-METRIC-DICTIONARY` reads the preceding construction
through `GATE-L1-L2-K1-HYBRID-FRW-CELL-METRIC`. Its continuous homogeneous
output is the metric on the selected chart `M=(0,infinity) x R^3`, with
coordinates `(t,y_1,y_2,y_3)` and the smooth one-sided extension to `t=0`,

```text
g_FRW = -nu(t)^2 dt^2 + a(t)^2 (dy_1^2+dy_2^2+dy_3^2).
```

`V0=5` is the normalization of the graph inner product. It is not the
Euclidean volume of this chart. The chart and the unit cell-clock bridge
are selected coordinate conventions, with no SI calibration. No point of
the finite graph is silently identified with a point of `R^3`.

Separately, at marked integer counters and finite sites, emit

```text
g_n(x)=diag(-nu(n)^2,
            a(n)^2(1+h_n(x)),
            a(n)^2(1-h_n(x)),
            a(n)^2), n>=0, x in X.
```

The output also retains the complete labelled `h`, half-slice `e,tau`, and
interior integer `j,P,p` records. The auxiliary tau and edge momentum solve
the scalar/vector constraints of this action. Tau is not identified with
an additional component of the emitted metric and is not discarded when
its multiplier is zero. There is no continuous inhomogeneous interpolation
in time or space: these inhomogeneous matrices remain separate marked
records on the finite torus. They are not a complete `GeometryData` object.

The public K1 bound `-59/100<h_n(x)<99/100`, together with `a(n)>0` and
`nu=1`, proves Lorentz signature of every emitted inhomogeneous matrix at
every nonnegative integer. The continuous homogeneous metric is Lorentzian
on its entire stated domain. This is a signature result for these outputs,
not an Einstein-Hilbert identification of the joint action.

Equality is literal equality of every marked source label, all displayed
fields, continuous homogeneous functions, and metric records in the chosen
chart. The context fixes the graph, cell-clock bridge, action, source packet,
vacuum matter, expanding branch, `a(0)=nu=1`, and representative. No sign or
coordinate quotient or adjustable K1 amplitude is implicit. All discrete
`h,e,j,tau,P,p` source and constraint records are rational. The emitted
integer metric entries are exact real algebraic numbers and need not be
rational. The continuous output is the exact displayed real function with
positive algebraic constant `H0`. No floating equality or numerical
integration is used. Words sharing energy and homogeneous background are
not identified when their complete labelled outputs differ.

This dictionary admits precisely this one selected reading in the stated
context, with the separate zero-source restriction. It neither asserts that
other readings are impossible nor claims global completeness of a physical
reading family. No target observation selects a word, branch or convention.

### FRW-INHOM [D]

The registered positive existence clause is adjudicated literally:

> closes positively by an inhomogeneous source construction that reproduces the public FRW-CANONICAL-FORM identities in the homogeneous limit; closes negatively if every inhomogeneous extension breaks the exact chain of twelves

`DEF-K1-HYBRID-FRW-CELL-METRIC` gives one such source construction. Its
nonconstant finite source and full labelled scalar/vector constraints belong
to the same joint action as the continuous homogeneous background. Every
independent first variation vanishes on the displayed solution for every
K1 word and every finite future restriction. The explicit nonzero source
obeys the public homogeneous equations with `rho_total`; setting the
inhomogeneous fields to zero recovers the public FRW action literally for
arbitrary admitted matter. The exact chain of twelves is unchanged.

`FRW-INHOM` therefore adopts `K1-HYBRID-FRW-CELL-METRIC-DICTIONARY` through
the named `DICTIONARY_LIFT` gate from L1 to L2. The positive clause asks for
existence of one construction; the proof does not invoke its universal
negative alternative. The adopted status is a dictionary, not a new
theorem claiming that this reading is forced by the axiom.

The L2 output consists exactly of the continuous homogeneous metric on its
declared chart together with the separate marked finite inhomogeneous
metric and auxiliary records. It supplies no complete continuous
inhomogeneous spacetime, full GR or Einstein equations for those records,
all-order gauge completion, tau-to-full-metric identification, arbitrary
matter-jet continuation, physical occurrence or emission law, physical
radiation pressure, scalar fluctuation spectrum, numerical `r_T`, or SI
scale. `TT-SOURCE [O]` and `TT-VECTOR-STATE-NORMALIZATION [O]` retain their
full decision clauses. The broader inhomogeneous scalar action excluded by
`CONFORMAL-PREFACTOR` is still unsupplied: its homogeneous coefficient does
not acquire an inhomogeneous action or a new L5-to-L2 interpretation from
this selected hybrid construction. Its SI boundary remains with
`METRO-EDGE-SCALE [O]`.

The joint action is even in `h`, its `e,j,E` sources are quadratic, and at
`nu=1,ell=N=0` the h equation is the homogeneous recurrence `R[h]=0`:
there is no independent emitting variable or additive source in that
equation. A zero initial pair remains identically zero even on an admitted
nonzero-matter homogeneous background, while nonzero K1 histories enter
through their imposed initial pair; this explains why this construction
does not supply `TT-SOURCE`, without asserting a universal negative
emission theorem.

The exact proof is the complete construction and first-variation argument
above, together with the separately proved K1 bound in this Canon. No
external draft or numerical source fixture is a premise of this closure.
<!-- END FRW-INHOM HYBRID CANON INSERT -->

## Exact proposed companion rows

These are proposed fold operations, not edits performed by this note.
Replace the existing FRW-INHOM row in each relevant table; append the
new definition and gate once. Headers below identify the existing schema.

### canon/REGISTRY.tsv

```tsv
claim_id	status	scope	canon_section	evidence	falsifier
FRW-INHOM	D	the selected K1-HYBRID-FRW-CELL-METRIC-DICTIONARY of DEF-K1-HYBRID-FRW-CELL-METRIC reads each unchanged K1 word as one solution of the displayed joint cubic cell-lapse and continuous homogeneous FRW action: all independent field variations vanish on every finite restriction, the conserved positive K1 energy sources the explicit expanding vacuum background for all t>=0, all labelled scalar/vector constraint records are retained, and the source-off action is literally FRW-CANONICAL-FORM for arbitrary admitted matter; the L2 output is the continuous homogeneous FRW metric on the selected chart together with separately marked finite inhomogeneous metric records; this positive existence closure selects one mathematical reading, with no complete continuous inhomogeneous metric, Einstein-Hilbert identification, all-order gauge symmetry, physical TT emission, scalar-spectrum comparison, r_T, SI calibration or reading uniqueness	13. Gravity and cosmology	inline	fires if an admitted K1 word fails a stated independent field equation, conserved-energy value, total future output, prefix restriction, Lorentz signature, or literal source-off FRW action identity; an assertion outside the selected dictionary scope requires a separate decision and is not supplied by this row
```

### canon/NORMATIVE.tsv

```tsv
item_id	item_type	claim_id	status	layer	gate_ids	statement_source
DEF-K1-HYBRID-FRW-CELL-METRIC	DEFINITION			L1		canon/CANON.md::DEF-K1-HYBRID-FRW-CELL-METRIC
FRW-INHOM	DICTIONARY	FRW-INHOM	D	L2	GATE-L1-L2-K1-HYBRID-FRW-CELL-METRIC	canon/CANON.md::FRW-INHOM
```

### canon/GATES.tsv

```tsv
gate_id	owner_item_id	from_layer	to_layer	gate_kind	decision_condition
GATE-L1-L2-K1-HYBRID-FRW-CELL-METRIC	FRW-INHOM	L1	L2	DICTIONARY_LIFT	adopt exactly DEF-K1-HYBRID-FRW-CELL-METRIC on the unchanged ten-word K1 domain and the separate source-off restriction, with fixed cell lapse integral, expanding vacuum branch, a(0)=nu=1, graph normalization V0=5, literal marked equality, and the displayed joint-action proof; the L2 output is the continuous homogeneous FRW metric on (0,infinity) x R^3 with its smooth one-sided t=0 extension, accompanied by separate finite inhomogeneous metric and constraint records; no continuous inhomogeneous interpolation, full GeometryData, physical occurrence, emission, SI scale, scalar spectrum or unique reading is adopted
```

The definition is an L1 mathematical object, not a second registered claim.
FRW-INHOM is the D dictionary owner at the concrete L2 target. The gate
therefore has the required DICTIONARY/D owner contract and distinct
concrete layer endpoints.

The fold must retain the public FRW theorem dependency, record the new
definition and unchanged K1 construction as actual dependencies, and keep
TT-SOURCE and TT-VECTOR-STATE-NORMALIZATION as scope boundaries rather than
claimed solved premises. It must update the existing inline evidence
scope hash deterministically, append an immutable O-to-D History event
with the old decision and this new scope, regenerate derived views, and
remove only FRW-INHOM from the live Frontier.

No new Registry identifier or T theorem badge is proposed. Relative to
v82, with this disposition alone, the 407 registered claims remain 407;
D rises from 45 to 46, O falls from 28 to 27, and live H/O falls from 30
to 29. Other status counts are unchanged. Wider scalar-action wording,
including CONFORMAL-PREFACTOR boundaries, must retain its actual limits.

## Bounded source-coupling audit

This paragraph is non-canonical review context and introduces no new
probe, F result, or universal negative. If the normalized TT functional
is changed by adding `sum_m <J_m,h_m>_V`, its TT equation becomes
`R_m=J_m`; the same balance gives
`Delta e+B^Tj=q_m J_m/2`. Keeping the same tau and momentum recipe then
gives `B^T p_m=-Pi_0(q_m J_m)/4`. For `h_0=h_1=0` and
`J_1=iota delta_0`, one has `q_1=iota delta_0`, so this divergence
is `-Pi_0(iota delta_0)/4 != 0`. The bare added source therefore breaks
the selected co-closed momentum completion. An emitter extension would
need to account for the compensating work/current; this audit neither
constructs that extension nor closes TT-SOURCE.

## Review and publication boundary

The complete displayed hybrid action and all-field solution have received
independent analytic review. The scope distinguishes the exact restricted
cubic model from an all-order gauge theory, a homogeneous metric on the
selected continuous chart from finite inhomogeneous records, and source
conservation from a physical emission law. The source/auxiliary rationality
claim explicitly excludes the generally algebraic emitted metric entries.

This proposal changes one Markdown file under notes/canon. It introduces
no executable, formal run, workflow, external-data payload, or change to
the frozen probe. A separate reviewed fold must adopt the exact scientific
choices, apply the ledgers and derived views, preserve the historical
replay context of every frozen verifier, and pass the existing complete
release checks. This note by itself changes no authority or gate status.
