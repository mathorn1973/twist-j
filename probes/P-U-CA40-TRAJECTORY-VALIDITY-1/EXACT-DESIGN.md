# Proposed exact audit: trajectory validity

PUBLIC PRE-PIN PREPARATION. NON-CANONICAL. Conditional action layer L1.
Reserved lane: P-U-CA40-TRAJECTORY-VALIDITY-1, issue
https://github.com/mathorn1973/twist-j/issues/1454.
No verifier has been executed or imported for this design. This file does
not preregister a public run or assert that the proposed thresholds pass.

This is a specification for a small independent Python-standard-library
verifier of new algebraic identities. It does not copy the previous large
source/contact verifier, solve a pulse, evaluate a floating trajectory, or
provide an oracle for anticipated numerical results. The predecessor is
P-U-CA40-WAVEFORM-SOURCE-1 at source pin
`1e078f6281b8f9ce813b6f08200d9caedf1bac14`. Reusing its pulse model is declared;
the rational checks below should be implemented independently.

## 1. Model contract to freeze before implementation

For real piecewise-constant u and real electronic responses s_i, use

```text
chi_i(t) = k x_i - mu t,
X_i(t) = sum_m kappa_mi [a_m exp(-i omega_m t)
                        + a_m^dagger exp(+i omega_m t)],
H_sin/hbar = 2u sum_i s_i [sin(chi_i+X_i) - sin(chi_i)],
H_L/hbar   = 2u sum_i s_i cos(chi_i) X_i.
```

The scalar subtraction is an explicit compensated-frame choice, or a
controlled unary counterterm if physically implemented. It cannot generally
be silently omitted. For this frozen word, however, mu*tau=2*pi*102 exactly,
the same envelope repeats in every loop, and each active ion is bright for
exactly one whole loop. Thus the uncompensated endpoint differs only by one
branch-independent scalar phase. No physical counterterm is needed for the
unconditional endpoint channel. Intermediate unary phases remain real and
branch dependent; a coherently controlled whole word must retain its common
endpoint phase. Changing the clock/profile requires a fresh phase ledger.
With real kappa and `g_m=sum_i kappa_mi exp(i k x_i) s_i`, the creation force is

```text
f_L,m(t) = u [g_m exp(i(omega_m-mu)t)
               + conj(g_m) exp(i(omega_m+mu)t)].
```

The rotating-wave comparator H_R drops only the second frequency. The
linearization error and rotating-wave error are separate comparisons.
All use one absolute time origin across pulse segments and carrier cycles.
These are conditional Hamiltonians, not a calibrated Ca40 apparatus model.

## 2. Two-frequency segment identities

Write one-mode force `f(t)=sum_(p=1,2) F_p exp(i nu_p t)` on [t0,t0+D].
Define `J(nu,D)=integral_0^D exp(i nu t) dt`, including J(0,D)=D, and

```text
B_p = F_p exp(i nu_p t0),
beta = -i sum_p B_p J(nu_p,D),
K(p,q,D) = integral_(0<v<t<D) exp(i nu_p t-i nu_q v) dv dt,
K(p,q,D) = [J(nu_p,D)-J(nu_p-nu_q,D)]/(i nu_q), nu_q != 0,
K(p,q,D) = integral_0^D t exp(i nu_p t) dt,             nu_q == 0,
gamma = Im sum_(p,q) B_p conj(B_q) K(p,q,D).
```

Both p != q terms are essential. The diagonal p=q term alone is not the
two-frequency area. When a separate scalar d is present, subtract its
integral from gamma. For chronological append, using the OLD alpha,

```text
Phi_next = Phi + gamma + Im(beta conj(alpha)),
alpha_next = alpha + beta,
D(beta) D(alpha) = exp(i Im(beta conj(alpha))) D(alpha+beta).
```

The same identities sum over independent modes. No bath reset is allowed.
They follow by direct integration/Magnus termination for a linear force;
finite rational fixtures audit the implementation, not this analytic theorem
for every transcendental frequency and duration.

### Exact implementation plan

Use Fraction pairs for complex rationals and truncated formal polynomials
in a symbol lambda. Expand `exp(i nu lambda t)` exactly through the required
degree, using coefficients `(i nu t)^j/j!`. Segment endpoints are rational
multiples of lambda. This is a formal identity test, never evaluation at
lambda=1 by truncation. No sin, cos, exp, sqrt, float, RNG or downloaded data.

Compare beta and gamma coefficients through degree 8 in three ways:
(a) the displayed J/K formulas, including their zero-frequency branch;
(b) independently integrated force products over the ordered time triangle;
(c) integration of alpha'=-if and Phi'=Im(alpha' conj(alpha)).
Implement the reference integrators independently of the J/K helper.

Freeze 24 single-segment fixtures: frequency pairs
`(0,0),(0,1),(1,0),(1,1),(1,-1),(2,-3)` crossed with amplitudes
`(1,i),(1,1),(1+i,1-2i),(0,1)`; use t0=lambda/3, D=lambda/2.
Freeze 24 two-segment fixtures with these first segments and a second
duration 2lambda/3, amplitudes `(-F_2,F_1+i F_2)`, contiguous absolute time.
Compare chronological append against one direct piecewise triangle integral.
These synthetic forces audit a larger algebraic class than real-u/conjugate-g
hardware-shaped forces; no claim that each fixture is a physical pulse.

Expose wrong Weyl sign, omitted off-diagonal frequency terms, wrong temporal
order, and reset absolute clock using named fixtures that must disagree.
An identically vanishing witness cannot count as exposure of a mutation.
Degree 8 is the exact finite audit depth, not a convergence/trajectory bound.

## 3. Gaussian moments through order six

For a displaced thermal bus under H_L, the spectral distribution of X_i is
a real Gaussian with mean m_i and variance v_i:

```text
m_i = 2 sum_m kappa_mi Re(alpha_L,m exp(-i omega_m t)),
v_i = sum_m kappa_mi^2 (2 nbar_m + 1),
M2 = m^2 + v,
M4 = m^4 + 6 m^2 v + 3 v^2,
M6 = m^6 + 15 m^4 v + 45 m^2 v^2 + 15 v^3.
```

Audit these as polynomial identities, not only selected numerical examples:
construct moments independently by the recurrence
`M_(j+1)=m M_j + j v M_(j-1)` and by coefficients of the formal generating
function `exp(m t+v t^2/2)`. Check all coefficients through degree 6.
Also check 20 rational fixtures: m in `{-2,-1/2,0,1/3,3}` and v in
`{0,1/4,1,5/2}`. Variance zero is an algebraic limit, not the physical vacuum
of a nonzero canonical quadrature. A physical vacuum has v=sum kappa^2.

Expose a wrong 45 coefficient, replacement of v by nbar, and omission of
the displacement mean. Full thermal Gaussian moments need no Fock cutoff.

## 4. Taylor remainder and Duhamel contract

For a self-adjoint X and real chi, write

```text
R = sin(chi+X)-sin(chi)-X cos(chi)
  = sin(chi)(cos X-1) + cos(chi)(sin X-X).
```

The scalar integral-remainder bounds are global:
`|cos x-1|<=x^2/2`, `|sin x-x|<=|x|^3/6` and `|R|<=x^2/2`.
Spectral calculus and the triangle inequality in the purified-state norm give

```text
||R Psi_L|| <= min(sqrt(M4)/2,
                  |sin chi| sqrt(M4)/2 + |cos chi| sqrt(M6)/6).
```

The first bound uses the second derivative of sin(chi+x) directly. A cubic
M6-only bound is generally false: chi=pi/2 gives cos X-1 with a quadratic
leading term. This is a mandatory negative control, demonstrated by its
nonzero formal quadratic coefficient, not a floating small-x experiment.

For the same initial normalized purified thermal bus and branch a,

```text
d_a <= integral_0^T 2|u(t)| sum_i |s_i(a,t)| ||R_i Psi_L,a(t)|| dt,
epsilon_LD <= min(1,max_a d_a).
```

This follows from Duhamel using the LINEAR trajectory in the residual:
`(U_sin-U_L)Psi0 = -i integral U_sin(T,t) DeltaH(t)/hbar U_L(t)Psi0 dt`.
Piecewise bounded controls, the stated self-adjoint evolutions and finite
Gaussian moments supply the domain/integrability assumptions. This is not
an unconstrained oscillator operator-norm estimate: X is unbounded.

For a fixed independent thermal bus, the electronic/reference half-diamond
distance is bounded by max_a d_a. Electronic output labels remain orthogonal,
so squared column norms are averaged with input probabilities; there is no
extra factor 25, 5^7 or reference dimension. Arbitrary electronic/reference
correlations are allowed; an arbitrary correlated initial bus is not covered
by the fixed-thermal comparison.

The exact verifier audits algebraic majorants without computing square roots.
For rational t>=0,r>=0, let |m|=t, v=r^2 and
`q4=t^2+3r^2`, `q6=t^3+8tr^2+4r^3`. Check polynomial identities

```text
q4^2-M4 = 6r^4,
q6^2-M6 = t^4 r^2+8t^3 r^3+19t^2 r^4+64t r^5+r^6 >= 0.
```

These deliberately conservative rational fixtures establish admissible
majorants. They are not substituted for the eventual trajectory estimator.
Given a rational piecewise upper envelope B_j for the integrand, exact
summation `sum_j duration_j B_j` must respect a frozen rational error budget.
Include one fixture below, one equal to, and one above 1/100; equality passes
the <= rule. No sampled endpoint maximum may impersonate an envelope.
A rational bump `t^2(1-t)^2` vanishes at 0 and 1 but is 1/16 at 1/2;
use it as the explicit negative control for that substitution.

For the separate RWA comparison, use the already derived Gaussian overlap
with BOTH displacement difference and Weyl phase. Its analytic purified
isometry bound can be added to epsilon_LD by the channel triangle inequality.
The exact audit checks rational displacement/Weyl signs; it does not turn a
floating exponential/phase maximum into an interval certificate.

## 5. Finite carrier word and source factorization

Use physical order `(s,x,u,y,w,q,r)`, active ions (4,5), protected (1,2,3,6,7).
Represent a local six-level monomial map by its output label and phase in
integer quarter turns. Independently implement

```text
R_(0,j)(pi,phi)|0> = -i exp(i phi)|j>,
R_(0,j)(pi,phi)|j> = -i exp(-i phi)|0>.
```

The chronological four rotations j=1,2,3,4 with phi=+,-,+,- pi/2 implement
the phase-free cycle `(0 1 2 3 4)` and fix shelf level 5. Check all six
columns, all six fifth-power columns and the shelf/unhide adjoint on all
six columns. Shelving uses phi=+pi/2 and unhide phi=-pi/2.

Check all 25 active input pairs over all five cycles (125 response pairs).
Each active label visits S0 exactly once; equal input labels visit together
once, unequal labels never do. For each protected code input 0..4, verify
that shelving, no active-only echo, and adjoint unhide leave zero response
at every force segment and restore its exact label and phase.

Consequently every full branch z=(p,a) has the SAME Hamiltonian as branch
a, under H_sin, H_L and H_R, and the endpoint is `I_P tensor V_(A,bus)`.
This proves why 25 active trajectories cover all 5^7 electronic inputs;
it is not extrapolation from 25 sampled states. It preserves any P/reference
marginal, even with arbitrary initial P/A/bus correlations. The Gaussian
error estimates above retain their narrower independent-thermal-bus premise.

Expose global echo, missing fifth cycle, wrong unhide and an admitted nonzero
protected response. In the last case the 25-branch reduction is invalid:
the implementation must widen its coverage or mark that context INCOMPLETE,
not silently reuse nominal factorization. This does not revisit the previous
informative full-contact C no-imprinting result; auxiliary G is a different map.

Also audit mu/(2*pi)=1,020,000 Hz and tau=1/10,000 s, whose product is the
integer 102. For two arbitrary rational pairs of single-loop unary integrals,
check all 25 branch sums are identical. Expose a non-integer loop-phase
advance by an exact quarter-turn fixture whose branch sums differ. This
audits the endpoint exception without approximating the optical phase.

## 6. Proposed classification and frozen thresholds

Freeze the separate engineering targets `epsilon_RWA<=1/1000` at the
endpoint, `epsilon_LD<=1/100` over the full interval, and dimensionless
full-interval position RMS <=1/10 as a separate heuristic LD diagnostic.
These are investigation targets, not universal validity criteria. Both
channel-bound targets together imply a combined sufficient bound <=11/1000;
the RMS diagnostic is not an additional term or proof of channel accuracy.
Gate-to-target error is a third term if a total target-channel conclusion is
requested. The rational 1/100 comparison fixture above tests the LD budget
semantics only and predicts no outcome of either actual envelope.

- EXACT_AUDIT_PASS: all finite rational identities, word columns and named
  negative controls pass. No numerical trajectory or apparatus is certified.
- EXACT_AUDIT_FAIL: an identity or required mutation exposure fails. Preserve
  the full failure; do not run a changed verifier under the same public pin.
- NUMERICAL_SCREEN_PASS: a completed frozen estimator reports both target
  signs meeting the separate RWA and LD bound targets and every declared
  consistency check. Report the RMS diagnostic disposition separately;
  it is not a necessary-and-sufficient channel guarantee.
  Label it a floating estimate unless continuous-time and roundoff enclosures
  have independently been supplied. Passing an LD ratio alone is insufficient.
- NOT_CERTIFIED_BY_THIS_BOUND: that completed estimator exceeds a frozen
  upper-bound target for either sign and no lower witness fires. This fails
  the chosen sufficient-bound screen, not the physical model itself; a large
  upper bound is not a lower bound on actual error.
- INCOMPLETE: missing full-time coverage, missing required residual/trajectory,
  invalid source reduction, unsupported domain/tail assumptions, timeout or
  absent numerical outputs prevent evaluation of the declared screen.
- VALIDATED_BOUND_PASS is reserved for certified enclosures of the full-time
  integrals, endpoint RWA comparator and arithmetic errors within the budget.
  Finite meshes, agreement of two FP codes and small endpoint alpha do not
  earn this label. If not implemented, declare this route unavailable up front.

A direct state-error witness above the corresponding channel-comparison
budget is a separate model counterexample only with its own stated
numerical/enclosure status; it is not implied by a nonpassing upper screen. Failure
of RMS<=1/10 is only failure of that heuristic diagnostic, never a channel
counterexample. No post-run threshold change or favorable arm substitution.

## 7. Interface, custody and exclusions

The intended verifier imports only fractions, itertools, json and sys; it is
import-safe, reads no files, has no network/subprocess access, accepts no CLI
arguments and emits one deterministic ASCII JSON line with an explicit LF.
Scientific stdout distinguishes algebraic audit counts from numerical claims.
It must state `trajectory_numerics_verified=false`,
`continuous_time_certificate=false` and `hardware_admission=false`.

The analytic Taylor/Duhamel proof belongs in a reviewed derivation alongside
the verifier. Finite formal-series checks are not proofs of global analytic
inequalities; their purpose is to catch coding/sign/combinatorial errors.
No Gaussian probability claim over a continuum of times follows from a
same-time marginal tail. If a later Fock truncation is introduced, its tail
and effect on two-channel comparison require a separate declared budget.

Before the first scientific execution: reserve the lane, freeze six policy
preregistration fields, all exact/numerical sources, manifest and criterion,
commit/push and read back immutable bytes. Static compilation is distinct
from scientific execution. Preserve every first-run failure and report the
exact and floating dispositions separately. This draft authorizes no run.
