# ETH-COS-1: scalar clock and a common cosmological transfer

PUBLIC; NON-CANONICAL. Selected theory, 2026-09-20.
Probe `P-TT-SCALAR-COSMOLOGICAL-DICTIONARY-1`, lock #1099.
Authority: Public Canon v90; base
`d4c1042d4bd164555b97ec74ae5732c40fa1c8a0`.

This completes one **conditional, classical, linear cosmological model**:
a scalar clock, its comoving-curvature perturbation, tensor perturbations,
a joint preparation and a common coordinate/time/scale dictionary. Its
finite-band tensor-to-curvature ratio is a cosmological observable of this
selected model. It is not an isotropic primordial CMB prediction or a
deduction of this model from J. The normalization owner's positive clause
is existential; this example is a proposed witness for adoption at D,
without turning its conditional theorems into a uniquely forced physics.

## 1. Decisions and their reasons

| Choice | Selected input | Reason and boundary |
| --- | --- | --- |
| CH-COS-CLOCK-ACTION | Einstein gravity plus one canonical scalar, lambda=216 pi; constant epsilon=3/2 exponential-potential solution | Supplies an actual scalar degree of freedom and its constraints. Keeps the existing decelerating homogeneous functional form, without identifying the old K1 energy bookkeeping with this matter field. |
| CH-COS-CONTINUUM-INTERFACE | Smooth finite Fourier interpolation at the outgoing onset m=2, followed by continuum propagation | Supplies spatial derivatives, a shared Cauchy surface and genuine wave numbers. It changes propagation after the interface; graph eigenvalues are not Euclidean wave numbers. |
| CH-COS-JOINT-PREPARATION | Canonical tensor seed Phi, scalar seed Pi_0 abs(Phi), equal canonical coefficients, common launch momentum q/d | Uses the rotation-invariant intensity as preparation data only and the backward impulse difference as the selected momentum interface. Relative coefficient one is a new preparation law, not forced by the actions. |
| CH-COS-POSITION-LAW | One independent uniform continuous translation of the whole prepared packet | Removes a preferred origin and gives a homogeneous ensemble. It preserves the preferred propagation axis and polarization. It is an additional occurrence input, not native randomness. |
| CH-COS-CLOCK-SCALE-READOUT | One conformal counter spacing d, common scale conversion, full metric tensor contraction and one common epoch | Fixes the observable types and polarization factor before the ratio. Physical scales remain explicit context inputs; their cancellation in this ratio is proved. |

No target observation or desired numerical ratio selects these choices.
Alternatives are not ruled out. In particular an independent scalar amplitude,
a different initial momentum, sound speed, background, state or tensor
polarization content generally changes the answer.

## 2. Scalar carrier, action and background

Use dimensionless chart coordinates and natural units. The selected continuum
action is

```text
S = integral sqrt(-g) [R/(2 lambda)
                      - (1/2) g^mu,nu partial_mu phi partial_nu phi
                      - V(phi)] d^4 x,
lambda=216 pi,  M^2=1/lambda,
V(phi)=3 H_*^2/(2 lambda) exp[-sqrt(3 lambda)(phi-phi_*)].
```

Here `H_*>0` is a declared background datum. The origin `phi_*=0` is a
field-coordinate convention. On the expanding branch with `a(0)=1`,

```text
F(t)=1+3 H_* t/2,
a(t)=F(t)^(2/3),
phi(t)=sqrt(3/lambda) log a(t),
H(t)=H_*/F(t),
epsilon=-dot H/H^2=3/2.
```

The exact homogeneous equations are `3H^2=lambda rho`,
`dot H=-lambda dot phi^2/2`, and
`ddot phi+3H dot phi+V_phi=0`. Kinetic and potential densities are
equal, so the background has `p=0`. The scalar perturbation sound speed
is nevertheless **one**, not that of pressureless dust. The expansion is
decelerating. No inflation, vacuum choice or horizon-exit prescription is
imposed.

This is a new matter realization of the homogeneous form. The existing
FRW-INHOM dictionary has word-dependent K1 backgrounds and an action with
no scale factor in its graph TT terms. It is not this action. Here `H_*`
is the same for all preparation atoms and is not inferred from either
old K1 energy or outgoing TT energy. The homogeneous scalar supplies the
background; perturbations are treated at linear order, without their
quadratic backreaction on it.

## 3. Genuine scalar perturbation and relative action normalization

In comoving gauge `delta phi=0`, use

```text
g_ij=a^2[(1+2 zeta) delta_ij + gamma_ij] + higher orders,
partial_i gamma_ij=0, gamma_ii=0,
gamma_ij=e^+_ij gamma_+ + e^x_ij gamma_x,
e^+ = diag(1,-1,0), e^x_12=e^x_21=1,
sum_ij e^A_ij e^B_ij=2 delta_AB.
```

The lapse and shift are constraint variables, not extra scalar states.
Their first-order solution and the reduced action are given in PROOF.md.
`zeta` is the comoving spatial-curvature perturbation. It is neither the
background conformal factor nor the identity `abs(gamma_+)` at later times.

Eliminating the constraints gives the selected quadratic dynamics

```text
S_S = (epsilon/lambda) integral a^2 [zeta'^2-|grad zeta|^2] d eta d^3x,
S_T = (1/(4 lambda)) integral a^2 sum_A
                                [gamma_A'^2-|grad gamma_A|^2] d eta d^3x,
q_S=a sqrt(2 epsilon/lambda) zeta,
q_T,A=a gamma_A/sqrt(2 lambda).
```

These are ordinary scalar and tensor quadratic actions, with no slow-roll
approximation in their coefficients. Their external convention source is
Maldacena, *Non-Gaussian features of primordial fluctuations in single field
inflationary models*, arXiv:astro-ph/0210603v5, equations (2.1), (2.8),
(2.10), (2.12), (2.27), (2.28):
https://arxiv.org/pdf/astro-ph/0210603v5 . The source supplies those continuum
action/gauge conventions, not our preparation, background selection,
native interface or ratio. PROOF.md supplies the conditional derivation.
No third-party source files are copied or used at runtime.

The theory used for the result is exactly this quadratic perturbation
model. Its relation to the parent nonlinear action is perturbative; no
finite-amplitude nonlinear solution or remainder bound is claimed.

## 4. Coordinates, counter, scales and Fourier normalization

Fix the full context `C=(H_*,d,A,ell_0)` with all four entries positive.
`A` is a common perturbation-amplitude parameter; results below are the
leading quadratic spectra. It cannot be adjusted independently in the
two sectors. The scalar coefficient relative to the tensor is fixed at one
in canonical variables. `H_* d` is a physical dimensionless context input,
not a choice of units.

The common comoving chart is the cubic torus
`T^3=(R/(5d Z))^3`. The fields occupy its planar sector, depending only on
`x_3`. Finite sites `r` map to `x_3=r d`. Elapsed conformal time is
`eta>=0`, with

```text
a(eta)=(1+H_* eta/2)^2,
t(eta)=2[(1+H_* eta/2)^3-1]/(3H_*),
dt=a d eta,
eta_n=(n-2)d, n>=2.
```

This is a new counter-to-conformal-time sampling convention at and after
the launch surface. It is not the unit proper-time cell convention of the
old hybrid dictionary and does not identify subsequent continuum fields
with subsequent values of the unchanged discrete outgoing history.

For any real five-vector f define

```text
fhat_j=(1/sqrt5) sum_(r=0)^4 f_r exp(-2 pi i j r/5),
If(x_3)=(1/sqrt5) sum_(j=-2)^2 fhat_j exp(i K_j x_3),
K_j=2 pi j/(5d).
```

Then `If(rd)=f_r`. Restriction to the five samples has no interpolation
ambiguity in this band. The conventional torus Fourier coefficient of
`If` is `fhat_j/sqrt5`, a factor retained in the powers below. The labels
1,4 represent +1,-1 and 2,3 represent +2,-2. All other three-dimensional
Fourier vectors have zero support. In particular no isotropy is asserted.

An eventual length calibration maps comoving distances to `ell_0 x`,
proper elapsed time to `ell_0 t/c`, and physical wave number to
`abs(K_j)/(ell_0 a)`. In natural units the corresponding dimensional
gravitational coefficient is `lambda ell_0^2`; no SI value is assigned.
The same map is used in both sectors. The context pivot is the supported
fundamental `abs(j)=1`, not a supplied observational CMB pivot. `ell_0`
remains owned by the metrology obligations.

## 5. Complete joint preparation

Retain the ten K1 words and masses from ETH-TT-1:

```text
0010 0011 0100 0101 0110 1001 1010 1011 1100 1101;
nu(0110)=nu(1001)=1/6; every other mass=1/12.
u_t=w_(t+2)-w_t,
H_t(r)=(delta_(r,u_t)+delta_(r,u_t+1))/2,
Phi=H_1-H_0,
S=Pi_0 abs(Phi), Pi_0 f=f-(sum_r f_r)/5.
```

The label `H_t` here denotes the old source profiles, not the Hubble
function. Retain the two independent fair root signs of ETH-TT-1; they
determine a square-root doublet lift but do not affect gamma or zeta.
Choose a further independent `sigma` uniformly on `[0,5d)` and translate
**both** interpolated profiles by that same sigma. No ensemble-mean
profile is subtracted before the translation.

At `eta=0`, prepare

```text
q_T,+(x)=A I Phi(x_3-sigma)/sqrt(2 lambda),
q_T,x=0,
q_S(x)=A I S(x_3-sigma)/sqrt(2 lambda),
q_T,A'=q_T,A/d, q_S'=q_S/d.
```

The launch momentum is `p=q'` in the canonical action after its explicit
time-boundary term has been removed. In metric variables it gives
`gamma_+'(0)=(1/d-H_*)gamma_+(0)` and the same relation for zeta.
The old discrete metric velocity is not simultaneously imposed.
The launch momentum imports the backward impulse difference
`h_2-h_1=Phi` over one selected conformal interval d. A discrete difference
does not mathematically force a continuum derivative; their identification
is the frozen interface choice; it does not assert `q(-d)=0` for a
backward continuum extension. The scalar receives the same impulse
profile in canonical units by the new joint preparation law. This specifies
coordinates **and** momenta, and the common label/translation specifies
their whole joint distribution. It is a classical probability law, not a
finite atomic density operator satisfying quantum canonical commutators.

The scalar is an additionally prepared clock-sector perturbation. The
previous complete K1-to-TT transfer budget is not used a second time.
Neither this co-preparation's microscopic energy source nor an apparatus
that produces it is derived. Static words prepare zero in both sectors.
The scalar seed has zero spatial mean in every atom; it carries no
homogeneous fluctuation of the background parameters.

At launch, `gamma_+=A I Phi` and `zeta=A I S/sqrt6`. Subsequently they
evolve independently by their equations. In general `I abs(Phi)` differs
from `abs(I Phi)`, and neither operation commutes with propagation.
For the tensor a pointwise persistent-sign square-root lift still exists;
it is a readout of the primary gamma equation, not a nonsingular substitute
variational equation for it.

Explicitly, at a chart point p put `b_+(p)=sqrt(max(gamma_+(p),0))`
and `b_-(p)=sqrt(max(-gamma_+(p),0))`. The continued vector state is
`v(p)=epsilon_+ b_+(p)+i epsilon_- b_-(p)`. Its square is gamma_+,
its mean is zero, and its complete two-point functions are

```text
C_v(p,q)=E_(w,sigma)[b_+(p)b_+(q)+b_-(p)b_-(q)],
P_v(p,q)=E_(w,sigma)[b_+(p)b_+(q)-b_-(p)b_-(q)]=0.
```

The last equality follows from the equal-mass Phi,-Phi pairing, which
interchanges the two roots. The same persistent signs give all higher
moments: a product of real/imaginary components vanishes if either total
sign exponent is odd, and otherwise equals the stated word/translation
average of its root factors. These finite integrals determine the full
state and all its spectra, without a Gaussian closure. The canonical
root is `v_can=(a/sqrt(2lambda))^(1/2)v`, so `v_can^2=q_T,+`.
The roots need not be smooth or band limited; it is their squared tensor
field, and the independently prepared scalar, that occupy the finite band.

## 6. Common dynamics, positive support and the observable

Write `x=eta+2/H_*`, `x_0=2/H_*`. Since epsilon is constant, both canonical
pump terms are `a''/a=2/x^2`. Every supported canonical mode obeys

```text
q''+[K_j^2-2/x^2]q=0,
q(eta)=G_j(eta)q(0), G_j(0)=1, G_j'(0)=1/d.
```

PROOF.md constructs the real analytic transfer from
`cos(Kx)-sin(Kx)/(Kx)` and `sin(Kx)+cos(Kx)/(Kx)`, whose Wronskian is K.
There is one transfer for both sectors. Existence and uniqueness hold on
the entire future domain. A transfer zero is possible; such zeros are
isolated. No finite replay substitutes for this all-time statement.

After uniform translation all nonzero Fourier means vanish. Define the
dimensionless **per-mode variances** in the normalized torus expansion by

```text
P_T(j,eta)=sum_ij E[gamma_ij,j conjugate(gamma_ij,j)]
          =2 sum_A E[abs(gamma_A,j)^2],
P_S(j,eta)=E[abs(zeta_j)^2],
r_T(j,eta)=P_T/P_S only when P_S>0.
```

These are not a claimed smooth three-dimensional density
`k^3 P(k)/(2 pi^2)`. Multiplication by an identical mode or bin factor
cancels in the ratio, but does not create an isotropic continuum spectrum.
Put `T_j=E abs(Phihat_j)^2` and `J_j=E abs(Shat_j)^2`. Then

```text
P_T=2 A^2 G_j^2 T_j/(5 a^2),
P_S=A^2 G_j^2 J_j/(30 a^2),
r_T=12 T_j/J_j.
```

The factor twelve includes the full tensor contraction and the relative
scalar kinetic coefficient. Merely importing the older finite comparison
would miss both this factor and the new preparation law.

| Modes | T_j | J_j | r_T on positive support |
| --- | --- | --- | --- |
| +1,-1 | (3+sqrt5)/24 | (5-sqrt5)/120 | 60+24 sqrt5 |
| +2,-2 | (3-sqrt5)/24 | (5+sqrt5)/120 | 60-24 sqrt5 |

Both scalar entries are strictly positive. All parameters `A,H_*,d,ell_0`
cancel from the ratio at every non-node epoch; absolute spectra, transfer
nodes and physical mode locations still depend on the context. At eta=0
all supported modes are non-nodes. At j=0, outside the prepared band, or
at a transfer node, both powers vanish and the ratio is **UNDEFINED**.
Its continuous extension through a node is not a measured nonzero power.

In fact the same T/J ratio holds for each active word separately at each
supported mode: its value is `abs(1-z^2)^2/abs(1+z^2)^2`,
`z=exp(-2 pi i j/5)`. Thus these particular ratios come from the selected
seed shapes and kinetic normalization. The Thue-Morse masses determine
the absolute spectra and full law, but do not uniquely select these ratios.

The old intensity comparison used a fixed-origin connected covariance.
Here `mu=E abs(Phi)=(1,1,1,0,1)/4` has nonzero Fourier mean before the
random translation. Consequently, for j!=0,

```text
J_j=I_j(old)+abs(muhat_j)^2=I_j(old)+1/80.
```

That mean is randomized along with the entire source, so it is part of
the present fluctuations. The two denominators concern different, openly
specified ensembles. The preparation is frozen before formal computation.
At launch the sums over the four supported modes give `sum T=1/2`,
`sum J=1/6`, and a ratio of total powers 36. A ratio of totals is not the
average of the individual ratios and need not stay 36 after propagation.

## 7. Equality, layers, and what has actually been completed

Within each fixed context equality retains the full joint field and
momentum law at all chart points and times, the coordinate/clock map and
the stated Fourier observable. It is not equality merely of two diagonal
ratios. Different contexts are not declared physically equivalent just
because this particular ratio agrees.

The mathematical claims are conditional L1 results. Proposed dictionary
gates are `GATE-L1-L2-SELECTED-COSMO-SCALAR-CLOCK`,
`GATE-L1-L4-SELECTED-COSMO-PREPARATION`, and
`GATE-L4-L6-SELECTED-COSMO-SPECTRA`. They are **UNPASSED**, unregistered
proposals pending a reviewed Canon fold. No change to Canon occurs here.

This construction supplies the previously missing scalar carrier,
its dynamics, relative action normalization and common cosmological chart
for one admitted selected model. Its limitations are concrete: classical
linear perturbations, one decelerating scalar background family, one
chosen joint preparation, one planar finite band and one polarization.
It supplies neither a unique J-derived preparation, a microscopic scalar
source, a quantum vacuum, an inflationary history, a full observational
spectrum, a metrological anchor nor a nonlinear completion. The independent
NS-TILT hypothesis is not applied to these two discrete bands.

`TT-VECTOR-STATE-NORMALIZATION` is unchanged by this probe. Its literal
positive clause asks for a public vector-doublet normalization yielding a
numerical r_T(k); it does not require uniqueness, inflation, isotropy,
an empirical CMB fit or SI calibration. This selected complete construction
is proposed as its positive witness, conditional on a separate fold
adopting the declared physical dictionary and checking its layer gates.
The resulting owner status would be D with the exact selected scope, not
T asserting that J uniquely forces it. The original decision and history,
including the universal negative alternative, must be preserved. No
classification of all admissible normalizations is claimed. The older TT
moment and square-pullback obstructions remain intact; empirical adequacy,
preparation physics and metrology remain separate obligations.
