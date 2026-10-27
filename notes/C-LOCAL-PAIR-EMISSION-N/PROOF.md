# A local core with two simultaneous outgoing excitations

Status: NON-CANONICAL; L1; candidate-T. This is a theorem candidate about
the supplied operator below, not a particle identification or Canon claim.

All energies are dimensionless model energies and `hbar = 1`. No measured
particle value fixes any coefficient. The equations and proposed targets
were recorded in [issue #1798](https://github.com/mathorn1973/twist-j/issues/1798).

## 1. Carrier and one fixed law

Write `J3` for the all-ones matrix, and set

```text
u = (1,1,1)^T,       b = u/sqrt(3),
D = {c in C^3: u* c = 0},
p = (1,-1,0)^T/sqrt(2) in D,
Hc = I + 3 J3.
```

The residual label `p` is a supplied choice, not a dynamically selected
direction. On `l2(N0)`, define the unilateral shift `S|n> = |n+1>` and

```text
L = 2I - S - S*,       delta = |0> tensor |0>.
```

The complete state space is

```text
K = C^3 direct_sum (C p tensor l2(N0) tensor l2(N0)).
```

The second summand contains a residual core and two simultaneous outgoing
excitations, with independent positions `x` and `y`. It is not a direct
sum of alternative one-excitation channels. We suppress the fixed unit
vector `p` in formulas on that summand.

For a supplied rational `0 < g <= 1/4`, set

```text
A = 3I + L tensor I + 2I tensor L,
H = [[Hc,                 g |u><delta|],
     [g |delta><u|,       A          ]].                 (1)
```

The fixed witness throughout is `g = 1/4`. Considering the displayed
parameter interval proves uniform bounds for that witness; it does not
retune the witness during its evolution.

The energy dictionary on the paired sector is explicitly

```text
residual energy = 1,
he = 2I + L,       hnu = 2L,
A = 1I + he tensor I + I tensor hnu.                     (2)
```

Thus `spec(he) = [2,6]` and `spec(hnu) = [0,8]`. The massive/gapless names
refer only to these declared gaps. The sine-transform dispersions are
`2 + 2 - 2 cos(k)` and `4 - 4 cos(k)`. The latter is quadratic at zero,
not a Weyl dispersion. The half-line boundary and residual core are pinned;
no recoil or translation-invariant total momentum is asserted.

In the coordinate basis, the core diagonal entries are `4`, its
off-diagonal entries are `3`, the pair diagonal entries are `9`, the two
pair hopping entries are `-1` and `-2`, and each source entry is `g`.
All entries are rational; `4H` has integer entries at the fixed witness.
Writing `Htilde = 4H` is only a change of energy and time units:
`exp(-it Htilde) = exp(-i(4t)H)`. It is not a native integer state update.

## 2. Boundedness, positivity, locality and stable states

The operators `L`, `Hc` and `A` are bounded and selfadjoint. Their spectra
are respectively `[0,4]`, `{1,10}`, and `[3,15]`. The off-diagonal part
of (1) has norm `sqrt(3) g`, so

```text
(1 - sqrt(3) g) I <= H <= (15 + sqrt(3) g) I.
```

Since `sqrt(3) < 2` and `g <= 1/4`, in particular

```text
H > I/2,              ||H|| < 31/2.                     (3)
```

Equation (1) has nearest-neighbor hopping in each outgoing coordinate,
finite internal core couplings, and pair creation/absorption only at
`x = y = 0`. This is finite-range locality on the explicitly declared
configuration graph. Both excitations are created at the same physical
endpoint. No global many-body realization outside this carrier is claimed.

Every `d in D` obeys

```text
H (d direct_sum 0) = d direct_sum 0.                    (4)
```

These are two exact stable core states of energy `1`, below the paired
continuum threshold `3`. The orthogonal active subspace consists of the
single bright state `b` and the paired sector. In that subspace, (1) is
the scalar discrete-level model

```text
Hactive = [[10,              beta <delta|],
           [beta |delta>,    A           ]],
beta = sqrt(3) g.                                       (5)
```

## 3. Exact paired spectral measure

The unitary sine transform diagonalizes `L`. The endpoint spectral measure
of `|0>` is the probability density

```text
sigma(e) = sqrt(e(4-e))/(2 pi),       0 < e < 4,          (6)
```

and zero elsewhere. Indeed `e = 2 - 2 cos(k)` and the endpoint sine
weight is `(2/pi) sin(k)^2 dk`. In particular,

```text
integral sigma(e) de = 1,
integral e sigma(e) de = 2.
```

For `2L` the corresponding density is

```text
sigma2(v) = sqrt(v(8-v))/(8 pi),      0 < v < 8.          (7)
```

The endpoint spectral density of `A` is their translated convolution:

```text
rho(E) = integral sigma(e) sigma2(E-3-e) de.             (8)
```

Consequently `rho(E) > 0` for every `3 < E < 15`, and it vanishes
outside `[3,15]`. The square-root densities, extended by zero, are compact
Hölder functions, so their convolution is compact and Hölder. Near either
outer endpoint, substituting `e = t v` into the convolution shows
`rho(3+t) = O(t^2)` and `rho(15-t) = O(t^2)` as `t` tends down to zero.
In particular the endpoint Green values are finite.

Define the physical resolvent, initially off the real spectrum, by

```text
m(z) = <delta, (z-A)^(-1) delta>
     = integral_3^15 rho(E)/(z-E) dE.                   (9)
```

The half-line Green function for `2L` follows either by eliminating its
endpoint or by solving its scalar quadratic equation:

```text
m2(w) = (w - 4 - sqrt((w-4)^2 - 16))/8,                 (10)
```

where the square root is fixed by `m2(w) ~ 1/w` at infinity. Hence

```text
m(z) = integral_0^4 sigma(e) m2(z-3-e) de.              (11)
```

The bright Green function is the exact Schur complement

```text
G(z) = <b, (z-H)^(-1) b>
     = 1 / d(z),
d(z) = z - 10 - 3 g^2 m(z).                            (12)
```

## 4. No hidden bright bound or singular component

At the lower edge, positivity and inverse monotonicity give

```text
0 <= -m(3-) = <delta, (L tensor I + 2I tensor L)^(-1) delta>
             <= <0, L^(-1) 0> = 1.                    (13)
```

All inverse matrix elements in (13) mean monotone limits from positive
resolvent parameters. The final value follows from the endpoint Green
function of `L` at zero. This argument does not require a bounded inverse
of `L` on its whole Hilbert space.

Multiplication by `(-1)^(x+y)` maps `A` to `18I-A`. Thus
`m(15+) = -m(3-)`, also between zero and one. Consequently

```text
d(3-)  <= -7 + 3g^2 < 0,
d(15+) >=  5 - 3g^2 > 0.                               (14)
```

For real `z` outside `[3,15]`,

```text
m'(z) = - integral rho(E)/(z-E)^2 dE < 0,
d'(z) > 1.                                             (15)
```

Equations (14)-(15) exclude every exterior zero of `d`. At each interior
energy the boundary identity is

```text
m(E+i0) = PV integral rho(t)/(E-t) dt - i pi rho(E).
```

Its strictly negative imaginary part makes the imaginary part of
`d(E+i0)` strictly positive. There is therefore no interior bright
eigenvalue. Equation (14) excludes threshold eigenvalues as well.

For completeness, this also excludes an unrecorded singular spectral
component. Compact Hölder regularity in (8) gives continuous, finite
boundary values of `m` by subtracting `rho(E)` in the principal-value
integral. The endpoint estimate supplies the same statement at `3,15`.
The denominator is nowhere zero on this compact interval by the preceding
argument, and is bounded away from zero. Thus `G` has continuous boundary
values there and no singular spectral measure. Its bright probability
density is exactly

```text
w_b(E) = 3g^2 rho(E) /
         ((E-10-3g^2 Re m(E+i0))^2 + (3g^2 pi rho(E))^2),
                    3 < E < 15.                        (16)
```

There are no exterior poles and `G(z) ~ 1/z`, so this density integrates
to one. Equivalently this normalization follows from the spectral theorem
and the exclusion of all singular components. To cover the whole paired
space, the product endpoint spectral transform represents `A` as
multiplication by `3+e+v` against
`sigma(e) sigma2(v) de dv`. Every vector has a spectral measure obtained
by pushing forward an integrable density `|f(e,v)|^2` times that product
measure. Fubini's theorem shows that this pushforward is absolutely
continuous. Hence all of the free paired operator is absolutely
continuous, not merely the endpoint cyclic measure. The part of the
paired space orthogonal to the cyclic subspace generated by `delta` is
unchanged by the coupling and remains absolutely continuous. The complete
operator therefore has precisely the stable core eigenspace (4) and an
absolutely continuous complement.

For the initial bright state define

```text
a_b(t) = <b, exp(-itH) b> = integral exp(-itE) w_b(E) dE.
```

Since `w_b` is integrable, the Riemann-Lebesgue lemma gives

```text
a_b(t) -> 0,
Prob(core at time t | initial b) = |a_b(t)|^2 -> 0,
Prob(pair at time t | initial b) = 1 - |a_b(t)|^2 -> 1.  (17)
```

The initially absent dark component remains absent. Thus (17) concerns
genuine asymptotic emission into a simultaneous pair sector, not merely
temporary core depletion or a mixture with an undisclosed bound atom.

## 5. Local continuation and an explicit resonance width

We now continue (11) from the upper half-plane through the regular real
interval `(7,11)`. No global two-sheet description is needed or asserted.
For each `0 <= e <= 4`, the argument `z-3-e` lies inside the `2L` band
when `z` is real in `(7,11)`. Thus the continuation in a neighborhood of
`z = 10` is

```text
mII(z) = (z - 9 - i F(z))/8,
F(z) = integral_0^4 sigma(e)
       sqrt((z-3-e)(11+e-z)) de,                        (18)
```

with the analytic square root positive for real `z` near `10`. The two
linear factors have no zero for `|z-10| < 1`, so these branches and the
integral are analytic throughout that disk. Formula (18) agrees with the
upper physical boundary and specifies the adjacent continuation below it.

On the closed smaller disk `|z-10| <= 1/2`, put
`a = z-3-e`, `c = 11+e-z`. Elementary rational bounds give

```text
|a c| <= (15/2-e)(3/2+e) <= 81/4,
|a c| >= (13/2-e)(1/2+e) >= 13/4.
```

The first quadratic has maximum `81/4` at `e=3`; the second is concave
and its minimum on `[0,4]` is `13/4` at `e=0`. Since `sigma` is a
probability density,

```text
|F(z)| <= 9/2,
|mII(z)| <= ((3/2)+(9/2))/8 = 3/4.                      (19)
```

At the center,

```text
7 <= (7-e)(1+e) <= 16,
sqrt(7) <= F(10) <= 4.                                  (20)
```

Differentiating the square root in (18) yields
`(c-a)/(2 sqrt(a c))`. On the same disk, `|c-a| <= 7`.
Consequently

```text
|F'(z)| <= 7/sqrt(13).                                  (21)
```

The continued denominator is

```text
dII(z) = z - 10 - 3g^2 mII(z).
```

On `|z-10|=1/2`, (19) gives

```text
|3g^2 mII(z)| <= 9g^2/4 <= 9/64 < 1/2.
```

Rouche's theorem therefore gives exactly one zero `z_*`, counted with
multiplicity, inside this disk. It is simple, and the numerator of (12)
is one, so it is an actual simple pole of the continued bright resolvent.
At that zero,

```text
z_* - 10 = 3g^2 mII(z_*),
|z_* - 10| <= 9g^2/4.                                   (22)
```

Using (21)-(22) along the straight segment from `10` to `z_*`,

```text
|F(z_*) - F(10)| <= 63g^2/(4 sqrt(13))
                 <= 63/(64 sqrt(13)) < 21/64.           (23)
```

Let `y = Im z_*`. Taking imaginary parts in (18) and (22) gives the exact
identity

```text
y (1 - 3g^2/8) = -(3g^2/8) Re F(z_*),
Gamma := -2y = [(3g^2/4)/(1-3g^2/8)] Re F(z_*).          (24)
```

Equations (20),(23), `sqrt(7)>5/2`, and `g<=1/4` imply

```text
Re F(z_*) > 5/2 - 21/64 = 139/64,
Re F(z_*) < 4 + 21/64 = 277/64,
125/128 <= 1 - 3g^2/8 < 1.
```

In particular `y<0`. For the lower width bound,

```text
Gamma > (417/256)g^2 > (3/2)g^2.
```

For the upper bound,

```text
Gamma < (3/4)(128/125)(277/64)g^2
      = (831/250)g^2 < (7/2)g^2.
```

We have proved, without numerical evaluation,

```text
(3/2) g^2 < Gamma < (7/2) g^2,
g=1/4:             3/32 < Gamma < 7/32.                 (25)
```

Under the optional unit change `Htilde=4H`, the width is
`Gammatilde=4Gamma`, so `3/8 < Gammatilde < 7/8`. No coefficient or
frozen physical model is changed by that bookkeeping convention.

Analytic implicit differentiation also supplies the small-coupling
expansion, with its remainder understood analytically as `g -> 0`:

```text
z_* = 10 + (3g^2/8)(1 - iF(10)) + O(g^4),
Gamma = (3/4)F(10)g^2 + O(g^4).                         (26)
```

This is an exact resonance statement with rigorous finite-coupling bounds.
It is not a proof of an interval of approximately exponential survival:
such an interval would require a separate bound on the non-pole part of
the spectral integral. In particular no equality
`|a_b(t)|^2 = exp(-Gamma t)` is asserted. The short-time behavior below
already excludes that equality.

## 6. Exact emission, charges, energy and local currents

Write a general state as `c(t) direct_sum psi(t)`. Schrödinger evolution is

```text
i c_dot = Hc c + g u psi(0,0),
i psi_dot = A psi + g delta (u* c).                      (27)
```

For initial `c(0)=b`, `psi(0)=0`, boundedness of `H` permits a norm-convergent
Taylor expansion:

```text
psi(t) = -i sqrt(3) g t delta + O(t^2),
Prob(pair at time t) = 3g^2 t^2 + O(t^4).                (28)
```

The even remainder follows because the matrix and initial vector are real,
so the probability is unchanged by `t -> -t`. Thus the emitted amplitude
is nonzero already at first order in time; the quadratic probability law
is not inferred from a truncation error.

The declared charge assignment is: dark residual/core charge `+1`, bright
core charge `0`, massive excitation charge `-1`, and gapless excitation
charge `0`. On the complete carrier the total charge operator is

```text
Q = P_D direct_sum 0.
```

Since `P_D u=0` and `[P_D,Hc]=0`,

```text
[H,Q] = 0.                                              (29)
```

In the paired sector the zero charge is the sum `1-1+0`. This assignment
is a supplied exact dictionary, not a derivation of electric charge. The
two outgoing number operators both equal the paired-sector projector,
so unmatched single-output states are absent by the declared carrier.
Any additional paired quantum-number assignments must be declared in the
same way; none is inferred here from a particle name.

The energy account is exact because the law is time independent:

```text
E = <c,Hc c> + <psi,A psi>
    + 2g Re(conj(psi(0,0)) u* c),
dE/dt = 0.                                              (30)
```

The interaction term in (30) must not be dropped during emission. For the
initial bright state,

```text
<H> = 10,
Var(H) = 3g^2.                                          (31)
```

It is therefore not a sharp-energy initial state. From (17), the core
energy and interaction expectation tend to zero, and the final paired
energy expectation tends to `10`. By (2), this splits into residual
expectation `1` and combined outgoing expectation `9`. These are exact
expectation accounts; no sharp separate outgoing energies are asserted.

The local pair probability currents in the positive coordinate directions
are

```text
j_e(x,y)  = 2 Im(conj(psi(x,y)) psi(x+1,y)),
j_nu(x,y) = 4 Im(conj(psi(x,y)) psi(x,y+1)),
s(t)      = 2g Im(conj(psi(0,0)) u* c).                  (32)
```

Set nonexistent boundary currents to zero. Equation (27) gives, at every
pair site,

```text
d |psi(x,y)|^2 / dt
 = j_e(x-1,y) - j_e(x,y)
 + j_nu(x,y-1) - j_nu(x,y)
 + indicator_(x=y=0) s(t),
d ||c||^2 / dt = -s(t).                                 (33)
```

Thus the source transfers probability to both-output configurations
locally, while each coordinate carries its own nearest-neighbor current.

An exact local energy continuity law can also be given without assigning
the interaction energy to an unphysical external battery. Let `P_v` be a
coordinate-vertex projector on the full graph, including the three core
vertices, and define

```text
h_v = (P_v H + H P_v)/2,
e_v(t) = <h_v>,
J^E_(v to w)(t) = i <[h_v,h_w]>.
```

Then `sum_v h_v = H`, the current is real and antisymmetric, and

```text
d e_v/dt = - sum_w J^E_(v to w).                        (34)
```

Each `h_v` is supported on the star of `v`, so the commutator vanishes
when the graph distance exceeds two. All sums needed at a fixed vertex
are finite. The bounded degree and bounded matrix entries also make the
total energy sum absolutely convergent on normalized states by
Cauchy-Schwarz. Local energy densities need not individually be positive;
the total operator satisfies (3).

## 7. Both outgoing coordinates escape every bounded endpoint interval

The paired-sector probability in (17) can be strengthened to actual
spatial escape. The following argument also constructs the asymptotic
free paired state; it uses no numerical estimate or scattering-theorem
assumption.

Extend `sigma` and `sigma2` by zero to the real line. Their endpoint
behavior is a square root, and their weak first derivatives behave as
the inverse square root. Consequently both belong to
`W^(1,4/3)(R)`: raising the derivative singularity to the power `4/3`
gives the integrable power `x^(-2/3)`. There is no endpoint delta term
because the densities themselves vanish at the endpoints.

Young's convolution inequality, with
`1/(4/3) + 1/(4/3) = 1 + 1/2`, gives

```text
rho'' = sigma' * sigma2'       in L2(R),
rho'  = sigma' * sigma2        in L2(R),
rho   = sigma  * sigma2        in L2(R),                 (35)
```

up to the harmless translation by `3`. Thus `rho` is compactly supported
and belongs to `H^2(R)`. The one-dimensional Sobolev embedding gives
continuous first derivatives, so both `rho` and `rho'` vanish at the
outer endpoints of their support.

Write

```text
h(E) = Re m(E+i0) = PV integral rho(t)/(E-t) dt.
```

This is `pi` times the Hilbert transform with its usual `1/pi`
normalization. The normalized Hilbert transform has a Fourier multiplier
of absolute value one away from zero and commutes with weak derivatives.
Therefore `h in H^2(R)`.
On a bounded interval containing `[3,15]`, the real denominator

```text
B(E) = (E-10-3g^2 h(E))^2 + (3g^2 pi rho(E))^2
```

belongs to `H^2` and is bounded below by a positive constant, by Section 4
and continuity. Products and smooth reciprocal composition preserve
`H^2` on that interval: this follows directly by differentiating twice,
using that functions and first derivatives in one-dimensional `H^2`
are bounded, while their second derivatives are square integrable.
Multiplying `1/B` by a smooth cutoff equal to one on `[3,15]` consequently
shows that the zero-extended density

```text
w_b(E) = 3g^2 rho(E)/B(E)
```

is compactly supported in `H^2(R)`. In particular `w_b'' in L1(R)` by
Cauchy-Schwarz on its compact support, and `w_b,w_b'` have zero endpoint
traces. Twice integrating its Fourier integral by parts yields

```text
|a_b(t)| <= ||w_b''||_1 / t^2       for t != 0,
|a_b(t)| <= 1,
a_b in L1([0,infinity)).                                (36)
```

This polynomial bound is an asymptotic regularity consequence; it is
neither an exponential approximation nor a fitted lifetime.

For initial bright state, `c(t)=a_b(t)b`. Duhamel's formula applied to
(27) is exactly

```text
psi(t) = -i beta exp(-itA)
         integral_0^t exp(iAs) delta a_b(s) ds.
```

By (36), the Hilbert-space-valued integral

```text
chi = -i beta integral_0^infinity exp(iAs) delta a_b(s) ds
```

converges in norm, and

```text
||psi(t)-exp(-itA)chi||
 <= beta integral_t^infinity |a_b(s)| ds = O(1/t).        (37)
```

Equation (17), norm preservation under `exp(-itA)`, and (37) imply
`||chi||=1`.

Let `P_R` project onto half-line sites `0,...,R`. For every half-line
vector `f`, absolute continuity of `L` and the Riemann-Lebesgue lemma
give

```text
||P_R exp(-itL) f|| -> 0.                                (38)
```

To see this without a uniform-in-state assumption, each matrix element
`<n,exp(-itL)f>` is the Fourier transform of an integrable cross-spectral
density, integrable by Cauchy-Schwarz. There are only `R+1` terms in the
projected norm. The same argument applies to `2L`.

The free pair group factorizes as
`exp(-itA)=exp(-3it) exp(-itL) tensor exp(-2itL)`.
Applying (38) first to finite sums of simple tensors and then using their
norm density gives, for the particular normalized `chi` above,

```text
||(P_R tensor I) exp(-itA)chi|| -> 0,
||(I tensor P_R) exp(-itA)chi|| -> 0.                     (39)
```

The approximation is uniform in time because all evolution and projection
operators have norm at most one. Equation (37) transfers (39) to the
actual coupled evolution. The probability of the union of the two strips
is bounded by the sum of their probabilities. Hence, for every fixed
finite `R`,

```text
Prob(pair with x>R and y>R at time t | initial b) -> 1.   (40)
```

Thus both excitations eventually leave every fixed bounded endpoint
region in probability, while the specified residual core remains pinned.
This claim concerns joint escape, not statistical independence of the
two outgoing energy or position distributions.

## 8. The boundary of the result

Equations (17), (25), (28)-(34), and (40) establish a genuine local
two-output mechanism, stable states, complete bright emission and joint
escape, a resolvent resonance, and exact conservation accounts in one
fixed positive Hamiltonian. They
do not establish particle names, spin, statistics, a physical mass ratio,
recoil, a native origin for the coupling, or physical occurrence.

There is also a simple obstruction to silently renaming the gapless
channel as a positive-energy Weyl channel. Let a translation-invariant
finite-range one-particle Hamiltonian have a differentiable Hermitian
symbol `h(k) >= 0`, and let `v in ker h(k0)`. For every direction `a`,
the scalar function `<v,h(k0+t a)v>` has a minimum zero at `t=0`, so

```text
<v, (a dot grad h)(k0) v> = 0.
```

Polarization gives `P0 (a dot grad h)(k0) P0 = 0` on the kernel. Hence
there is no nonzero linear band splitting at a genuine zero-energy
minimum. A signed Dirac crossing, an energy-offset crossing, or a
different field carrier requires a separately stated construction.
Nothing in the Fourier truncation of an independent clock supplies it.

No recurrence or exact exponential law is claimed for this infinite
spatial carrier. The resonance width comes from the actual paired
continuum in (8), not from a clock's finite approximation horizon.
