# K1 geometry admission: an explicit metric map and its restricted rejection

**NON-CANONICAL / ANALYTIC ADMISSION REVIEW / NO FORMAL RUN OR PHYSICAL TEST**

```text
basis_main: c6d90f148f6ea7295cb42c629b6cf735060ebfd4 (merged #906)
authority: ACTIVE Public Canon v81
scientific owner: TT-VECTOR-STATE-NORMALIZATION [O], unchanged
candidate disposition: rejected for the stated TT identification
general K1-to-physical-geometry bridge: NOT SUPPLIED
new registered status / original O/H closure / execution: NONE
```

This review applies one existing metric equation to the fixed K1. K1 is
the **input coordinate field** of this candidate metric reading, not a
stress source and not the metric deformation itself. The candidate gives
an explicit geometric output and a scalar from that same output. Its
traceless component is identically zero and cannot equal the nonzero
registered TT square on K1. This rejects this particular identification;
it does not reject K1, the declared metric, or all TT normalizations.

The [K1 electric-field reading](V81-K1-LOCAL-SQUARE-OBSERVATION-1.md)
therefore remains a precise conditional observation model. It is not an
immediately ready route to a physical tensor-to-scalar ratio. The next
theoretical obligation is the missing geometric law, not further adjustment
of its finite correlation, source weights, polarization or number of points.

## 1. What the existing equations actually provide

The following are the public inputs, with their original statuses and scope:

| Input | Equation and scope relevant here |
| --- | --- |
| `KAHLER-CAPACITY [T]`, [Canon section 13](../canon/CANON.md#13-gravity-and-cosmology) and [gravity-chain](../reproduce/gravity-chain/verify.py), JET/CAPACITY blocks | The declared metric coefficient is `m_K(xi)=phi^2/(1+|xi|^2)`, with `phi=(1+sqrt(5))/2`. Its capacity and jets do not identify `xi` with an electric field or a spacetime coordinate, or supply the realification below. This is the existing scalar coefficient equation applied here. |
| `TT-SQUARING-DECODER [D]`, `POL-READ [D]`, [Canon section 14](../canon/CANON.md#14-the-gravitational-wave-program) | `Q(v)=[[Re(v^2),Im(v^2)],[Im(v^2),-Re(v^2)]]`, with the doubled-angle law and `det(I+Q)=1-|v|^4`. These specify a square/readout, not a field-to-metric dynamical coupling. |
| `FRW-CANONICAL-FORM [T]`, [gravity-chain](../reproduce/gravity-chain/verify.py), LAPSE block | `S=V0 int dt nu exp(3 Phi)[-(3/lambda)(Phidot/nu)^2-rho(Phi)]`, `lambda=216 pi`; lapse variation gives `3H^2=lambda rho`. The displayed action has one homogeneous scale, not an inhomogeneous scalar or a TT field with gradients and a source. |
| `CONFORMAL-PREFACTOR [D]`, [registry](../canon/REGISTRY.tsv) | `K_chi5=1/(864 pi)` and `c_hom=1/(72 pi)` at homogeneous L5 scope. The inhomogeneous scalar action and SI clause remain open. |
| `TT-QUADRATIC-GERM [D]` and Schwarzschild endpoint, [coupling-metrology](../reproduce/coupling-metrology/verify.py), GERM/RW-ENDPOINT blocks | `mu=1`, `Z_L2=1/2` are explicit dictionary inputs, not a derived action germ or pullback. `1-s^2` occurs in `V_s=f[L/r^2+2M(1-s^2)/r^3]`; it does not specify a K1 time update or identify K1's sample index with Schwarzschild radius. |

The partial decoder remains
`D_geom: dom(D_geom) subset K x MatterData -> GeometryData`.
Its fields exist where registered claims define them. The named interface
does not itself supply a TT metric component, a K1 injection into that
component, or an action coupling. The homogeneous action above cannot be
varied with respect to an absent tensor field to obtain that coupling.
Adding spatial or tensor terms would be a new law, not an application of
the displayed rank-one action.

## 2. One candidate: K1 as input to the declared metric coefficient

Retain exactly the [K1 ten-word source and joint law](V81-TT-K1-SOURCE-MAP-1.md).
For `r in Z/5`, `t in {0,1}`, its local field and intensity are

```text
b_r(w,t) = [delta_(r,u_t(w))+delta_(r,u_t(w)+1)]/sqrt(2),
h_r(w,t) = b_r(w,t)^2 in {0,1/2},       h_r^2=h_r/2.
```

The two labels `t` retain the existing overlapping-window law. There is
no added random rotation, translation or time evolution. Choose a finite
common `a>0`, the dimensionless amplitude already explicit in the field
reading. The one new candidate injection is `xi_r(w,t)=a b_r(w,t)`.
It is a proposed identification of K1 with the argument of the declared
metric equation, not an already registered physical dictionary.

For this candidate, choose the explicit complex one-dimensional metric
interpretation `ds_K^2=m_K(xi)|d xi|^2`, and identify its two real coordinate
axes with the fixed comparison frame. This realification is an additional
candidate convention, not an identification proved by the capacity theorem. The candidate
map into positive real symmetric two-by-two matrices is

```text
G_r(w,t) = m_K(xi_r(w,t)) I2
         = phi^2/[1+a^2 h_r(w,t)] I2,
G_ref = G(xi=0) = phi^2 I2,
g_r = G_r/phi^2,                      Delta_g_r=g_r-I2.
```

This is **pointwise evaluation of a metric coefficient in a fixed frame**.
It is not the pullback of that metric along a spacetime map `xi(X)`;
a pullback would contain derivatives/Jacobians that are absent here. Nor
does it construct a Lorentzian four-dimensional metric. The candidate
tests the proposed direct transverse identification only. A common factor
of two in a different realification convention cancels against `G_ref`.
No state-dependent change of frame or new derivative term is introduced.

The reason for testing this map is concrete: it is a literal composition
with a metric equation already public in the gravity chain, with no
coefficient chosen from a desired correlation or `r_T`. Its physical
admission remains a question. This scope does not presume that every
geometric reading must use this composition.

## 3. Exact tensor and scalar outputs of that same map

On the two-level K1 support put

```text
kappa(a) = a^2/(1+a^2/2),              0<kappa(a)<2.
```

Then the candidate simplifies exactly:

```text
g_r = [1-kappa(a) h_r] I2,
s_r = Tr(Delta_g_r)/2 = -kappa(a) h_r,
T_r = STF(Delta_g_r)
    = Delta_g_r - Tr(Delta_g_r) I2/2 = 0.
```

The simplification follows from
`(1+a^2 h)(1-kappa h)=1+[a^2-kappa-a^2 kappa/2]h=1`.
It is exact for this support, not an identity for arbitrary field values.
All eigenvalues of `g_r` are positive. They are both `1` at an empty
site and both `(1+a^2/2)^(-1)` at an occupied site.

The scalar `s` is the relative trace/conformal change of this candidate
metric in the same fixed reference frame. Its reference, units and
normalization are specified without a tensor-to-scalar target: `xi`, `a`,
`g` and `s` are dimensionless. The construction supplies no SI length for
the coordinate chart. A physical line element would require a separately
justified coordinate interpretation and length conversion.

For completeness, the [already derived full local covariance](V81-K1-LOCAL-SQUARE-OBSERVATION-1.md#4-full-covariance-including-spatial-and-time-cross-terms)
gives the entire scalar output, not just spectral diagonals:

```text
mu_s = -kappa(a) mu_h,
Gamma_s(t,t') = kappa(a)^2 Gamma_h(t,t'),
mu_h = (2,2,1,0,1)^T/6.
```

For the same unitary finite Fourier transform let
`omega=exp(2 pi i/5)`, `d_x=(1+omega^x)/sqrt(20)` and
`f(x)=(omega^(-x)+1+omega^x)/3`. Its connected scalar channel variance is

```text
Var(shat_x) = kappa(a)^2 |d_x|^2 [1-f(x)^2] > 0,    x!=0 mod 5.
shat_0 = -kappa(a)/sqrt(5)                          (constant).
```

For nonzero `x`, `|d_x|>0`; averaging the three distinct unit phases in
`f(x)` has modulus less than one, proving the strict inequality. All
off-diagonal and two-time terms are multiplied by the same `kappa(a)^2`.
Thus this candidate does have a nonzero finite scalar comparison on the
four nonzero channels. A zero scalar variance is not the reason it fails
the tensor admission test.

This scalar is not identified with a cosmological curvature or density
perturbation. Its finite variance is consequently not an admitted
cosmological `P_S(k)`. Neither the homogeneous FRW coefficient nor the
hypothesis `n_s-1=-5 alpha` supplies that missing identification, action,
physical epoch or power normalization. A nonzero finite denominator by
itself is insufficient.

## 4. The admission test fails on every occupied site

The proposed comparison uses the same local K1 input as the TT square:

```text
Q_r = Q(a b_r) = a^2 h_r diag(1,-1).
```

To admit this particular metric reading as the geometric realization of
that square, require `T_r=Q_r` in the fixed reference frame. At each
occupied site, for every admitted finite `a>0`,

```text
T_r=0,                  Q_r=diag(a^2/2,-a^2/2)!=0.
```

Every K1 source/window has two occupied sites, so the incompatibility is
nonvacuous on every source realization. A common nonzero calibration or
normalization cannot turn the zero tensor into this nonzero one. Normalizing
the two equal metric eigenvalues by their local mean also leaves zero
anisotropy. The candidate is therefore **rejected for this TT identification**.

This conclusion does not need a selected value of `a`, a numerical run,
a fitted `r_T`, or a probability estimate. It follows directly from the
image of the explicit map. It is not a counterexample to the TT square:
that square was never proved to be this metric's traceless part.

The candidate also has a separate, exact response consequence: in the
fixed frame its two principal metrical coefficients change equally. The
occupied/empty coefficient ratio is `(1+a^2/2)^(-1)` and the corresponding
length ratio is `(1+a^2/2)^(-1/2)`. The coefficient equation is invariant
under `xi -> exp(i theta) xi`, whereas the nonzero square transforms with
double angle. This is a consequence of the proposed law, not permission
to rotate or average the fixed K1 source. These would be independently
testable geometric responses only after qualifying an actual physical
metric observable; no such measurement is claimed here.

Do not report the formal quotient of zero tensor variance and the positive
finite scalar variance as a physical `r_T=0`. The candidate already fails
the required square identification, and its scalar lacks a cosmological
admission. Failure of this map is not the universal negative clause of
`TT-VECTOR-STATE-NORMALIZATION`.

## 5. Decision and the next theoretical obligation

The three admission questions now have definite answers for this candidate:

| Question | Decision |
| --- | --- |
| K1's role | Input coordinate field `xi=a b` to one evaluated metric equation. It is neither a stress tensor/source nor the metric deformation itself. |
| Connecting law | `G=phi^2/(1+|xi|^2) I2`, with explicit injection, realification and fixed-frame comparison. It yields only a conformal response and fails `STF(Delta_g)=Q(a b)` on the K1 support. |
| Same-context scalar | `s=Tr(Delta_g)/2=-kappa(a)h`, with complete inherited covariance and nonzero finite channel variance. It is a geometric trace scalar of the candidate, not a qualified cosmological scalar power. |

The broader physical geometric bridge is still absent in the inspected
public equations. K1 stays at its exact field-reading scope. The next
theoretical work must supply a particular geometric decoder or action
coupling whose actual metric output can satisfy the stated square relation,
with the scalar perturbation and its normalization in that same context.
Merely renaming `Q` as metric strain would impose the equation rather than
derive or independently justify it. An added law must declare its new
physical input and a consequence testable independently of imposed source
weights or the desired ratio.

Global decoder uniqueness is not required. A context with a determined
output, or an independent rule selecting among alternatives that change
it, is sufficient under the public reading-family policy. This review
classifies only the one stated candidate; it does not change the original
TT, source or inhomogeneous-scalar owners. No formal verification is armed
on the basis of a missing physical coupling. TRC1 remains a conditional
paired equation with its active archive search finished as recorded in #906.
