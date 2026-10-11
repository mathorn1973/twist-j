# Continuous trajectory validity: an explicit sinus parent

Analytical preparation for `P-U-CA40-TRAJECTORY-VALIDITY-1`, 2026-10-11.
NON-CANONICAL; conditional theory, not physical admission. No new scientific
program, import, candidate evaluation or simulation was executed to write
this derivation. The prior `P-U-CA40-WAVEFORM-SOURCE-1` result is exposed
input. Its two envelopes, geometry and absolute chronology are not retuned.

## 1. Scope and the proposed parent

Keep physical ion order `(s,x,u,y,w,q,r)`, active ions `(4,5)`, the seven
declared harmonic axial modes, five 100-us loops, 16 constant-amplitude
segments per loop, and ideal instantaneous phase-exact active X5 pulses.
In the frame toggled by these pulses, electronic input labels do not move;
the response in loop l is

```text
s_i(a,b,l)=1[z_i+l=0 mod 5] for i=4,5;
s_i=0 for i=1,2,3,6,7.
```

Thus only 25 active branches and two frozen envelopes require examination.
All protected states are dark; this is an assumption, not a newly tested
spectator-isolation mechanism. Carrier duration, scattering, heating,
radial motion, electronic leakage and trap anharmonicity remain excluded.

Use real mode vectors b_mi, k=2pi/(397 nm), equilibrium positions x_i and

```text
kappa_mi = k b_mi sqrt(hbar/(2 M omega_m))              (real),
eta_mi   = kappa_mi exp(i k x_i),
X_i(t)   = k q_i(t)
         = sum_m kappa_mi [a_m exp(-i omega_m t)
                          + a_m^dagger exp(i omega_m t)],
chi_i(t) = k x_i - mu t.
```

The oscillator operators are in the interaction frame of the harmonic
trap. One explicit proposed effective optical parent is

```text
H_S(t)/hbar = 2 u(t) sum_i s_i(t)
             [sin(chi_i(t)+X_i(t))-sin(chi_i(t))].        (1)
```

Here u is real, with negative u implemented by a declared force-phase
change. Equation (1) assumes that an optical dipole potential with this
sinus profile has already been obtained. It does not establish elimination
of atomic excited levels, laser geometry, power, spontaneous-emission rate
or an apparatus realizing that profile. The original RWA force does not
uniquely select this parent: additional terms of quadratic or higher order
in X can share its first-order force. This is a named conditional model.

## 2. The unary phase ledger and this word's endpoint exception

The uncompensated optical potential is
`H_U/hbar=2u sum_i s_i sin(chi_i+X_i)`. Equation (1) additionally requires

```text
H_ct/hbar = -2u sum_i s_i sin(chi_i) I_bus.              (2)
```

Equation (2) would be a time-dependent unary electronic control if physically
applied. Alternatively it defines an exact compensated frame. It is not
generally a global phase, and no physical implementation is assumed here.
In the toggling frame it commutes with every conditional bus Hamiltonian.
Consequently the uncompensated and compensated branch propagators obey

```text
U_U,z(T) = exp(i lambda_z(T)) U_S,z(T),
lambda_z(T) = -2 integral_0^T u(t) sum_i s_i(t) sin(chi_i(t)) dt. (3)
```

For a segment `[t0,t0+h]` with constant u and response, its contribution is

```text
lambda_z,seg = -2u h sinc(mu h/2)
               sum_i s_i sin(kx_i-mu(t0+h/2)).           (4)
```

The sinc convention includes mu=0. Equal time spent in S does not by itself
prove phase cancellation for a generic absolute optical clock. This frozen
word has the stronger exact parameter identity

```text
mu tau = 2pi (1,000,000+20,000) Hz * 100 us = 2pi*102,
u(v+l tau)=u(v),           exp(-i mu l tau)=1.
```

Each active ion occupies S during exactly one full loop. Therefore, for
T=5 tau and either envelope separately,

```text
lambda_z(T) = -2 sum_(i=4,5) integral_0^tau u(v)sin(kx_i-mu v)dv
            = lambda_sigma, independent of (a,b).        (4a)
```

The uncompensated parent has exactly the same unconditional endpoint
channel as the compensated parent. No physical compensation resource is
needed for that endpoint statement. Record the raw lambda_sigma and a
numerical branch-spread diagnostic; rounding of the exact period identity
must not be mistaken for an additional physical interaction. Do not drop
lambda_sigma if the entire pulse word is coherently controlled.

At intermediate times lambda_z(t) is generally branch dependent. Full
trajectory comparison with the original RWA electronic state must include
that known unary phase or explicitly use the compensated frame. This does
not affect motional distributions. Adding the same unary Hamiltonian to
S and L preserves their comparison at every time. If the exact loop-period
identity, repeated envelope or response profile changes, recheck (4a);
the generic case requires a declared correction or a different target.

## 3. Linearization gives both motional frequencies

The exact first-order expansion of (1) is

```text
H_L/hbar = 2u sum_i s_i cos(chi_i) X_i
         = sum_m [f_L,m a_m^dagger + conj(f_L,m) a_m],
g_m(t,z) = sum_i eta_mi s_i(t,z),
f_L,m = u[g_m exp(i(omega_m-mu)t)
          + conj(g_m) exp(i(omega_m+mu)t)].             (5)
```

The second coefficient is `conj(g_m)=sum_i conj(eta_mi) s_i` because
u, s and kappa are real. There is no additional kappa factor multiplying
eta. Removing only the second frequency gives exactly the prior force

```text
f_R,m = u g_m exp(i(omega_m-mu)t).                       (6)
```

Here R means the motional RWA, not a second assertion about optical
electronic-state elimination. Preserve exp(ikx_i); replacing eta by its
absolute value changes the parent and both forces. Nominal RWA closure
does not imply closure at omega_m+mu. The two model comparisons are
separate: `S versus L` tests linearization, `L versus R` tests this RWA.

For either linear model use

```text
D(alpha)=exp(sum_m alpha_m a_m^dagger-conj(alpha_m) a_m),
U_j(t)=exp(i Phi_j(t)) D(alpha_j(t)),
dot(alpha_j,m)=-i f_j,m,
dot(Phi_j)=Im sum_m dot(alpha_j,m) conj(alpha_j,m).       (7)
```

Append a segment on the left: `Phi <- Phi+chi_seg+
Im sum beta*conj(alpha_old)` and `alpha <- alpha_old+beta`.
Both frequencies and their mixed terms contribute to chi_seg. For fixed
segment amplitudes F_d at frequencies d, define

```text
I(d,h) = integral_0^h exp(i d v)dv = h exp(i d h/2)sinc(d h/2),
beta_m = -i sum_d F_d exp(i d t0) I(d,h),
J(d,e;t0,h) = exp(i(d-e)t0)[I(d-e,h)-I(d,h)]/(-i e),
chi_seg = Im sum_m sum_(d,e) F_d conj(F_e) J(d,e;t0,h).   (8)
```

The continuous e=0 limit is the defining integral
`J=integral_(t0<t2<t1<t0+h) exp(i d t1-i e t2)dt2 dt1`.
The d=e case gives the familiar imaginary part
`(d h-sin(d h))/d^2`; at d=0 that imaginary part is zero.
Near coincident or zero frequencies use analytic limits or stable divided
differences. Adding separate plus/minus geometric areas without their
mixed terms is incorrect. No alpha, phase or clock reset occurs at a loop.

## 4. Exact fixed-thermal channel comparison for RWA

Assume the initial bus is a fixed product thermal state, independent of
the electronic system and any reference R. Put nu_m=nbar_m+1/2. For each
active branch, at any specified time, the overlap of the two propagated
copies of one fixed purification of that bus is

```text
v_z = exp(-r_z+i delta_z),
r_z = sum_m nu_m |alpha_L,m-alpha_R,m|^2,
delta_z = Phi_L-Phi_R
          +Im sum_m conj(alpha_R,m) alpha_L,m.           (9)
```

The Weyl term in delta and the mixed-frequency terms in Phi_L are needed.
Distinct electronic output branches remain orthogonal. The distance of
these two fixed-bus Stinespring isometries is therefore

```text
e_RWA(t) = max_z sqrt(2-2 exp(-r_z) cos(delta_z)),
(1/2)||Lambda_L(t)-Lambda_R(t)||_diamond <= min(1,e_RWA(t)). (10)
```

The diamond norm here varies all electronic inputs and their arbitrary
references; it does not vary the fixed bus input. It also bounds the
output retaining the physical bus. It is not an actual gate infidelity.
Unconditional channels ignore one common phase; (10) with the inherited
phase convention can be conservative. The exact endpoint phase (4a) is
already accounted for by the compensated-frame comparison. No fitted
branch-dependent phase correction is allowed. Any further common-phase
optimization must be separately preregistered.

For a preregistered endpoint common-phase optimization put
`w_z=exp(-r_z+i delta_z)` and maximize `min_z Re(exp(-i gamma)w_z)`.
A finite candidate set suffices: `arg(w_z)`, `arg(w_z)+pi`, and
`arg(w_z-w_j)+/-pi/2` for unequal pairs. Between pair intersections the
minimum is one smooth sinusoid, whose interior extrema are in the first
set. Evaluate the final error stably branchwise as
`sqrt(-2expm1(-r_z)+4exp(-r_z)sin^2((delta_z-gamma)/2))`, then maximize
and cap at 1. This is a common gauge phase, not a label-dependent correction.

### Continuous phase coverage without a second dense grid

Let `d=alpha_L-alpha_R` and delta be (9), on one branch. Differentiating
(7) and (9) cancels all terms involving the common RWA force:

```text
dot(delta_z) = Im sum_m dot(d_m) conj(alpha_L,m+alpha_R,m),
dot(d_m) = -i u conj(g_m) exp(i(omega_m+mu)t).            (10a)
```

For one entire constant-response segment of width h, obtain the analytic
state at its midpoint tc from (8) and its accumulated prefix. Define

```text
F_zm = |u| |g_zm|,
AL_zm = |alpha_L,m(tc)|+h F_zm,
AR_zm = |alpha_R,m(tc)|+(h/2)F_zm,
D_z = sum_m F_zm (AL_zm+AR_zm),
R_z = sum_m nu_m (|d_m(tc)|+(h/2)F_zm)^2.                (10b)
```

Use the labels-00 branch of the same envelope as anchor z0, with the
time-dependent common gauge `gamma(t)=delta_z0(t)`. The circular phase
distance throughout that segment is at most

```text
E_z = min(pi, |wrap(delta_z(tc)-delta_z0(tc))|
                   +(h/2)(D_z+D_z0)).                   (10c)
```

For E_z<=pi/2 a uniform segment upper bound is
`min(1,sqrt(-2expm1(-R_z)+4exp(-R_z)sin^2(E_z/2)))`.
For larger E_z report the trivial bound 1. Maximizing these bounds over
all 25 branches and 80 segments gives a separate all-time RWA channel
comparison; also report the phase and displacement envelopes, with the
phase limited to pi as the maximal circular distance, as in (10c).
This requires only an analytic midpoint per original segment, not a new
time-grid search. It may be much more conservative than the endpoint bound.

The continuous comparison is in the compensated frame, or equivalently
both models include the same known unary evolution (3). It does not imply
that the uncompensated parent is close at every time to the old d=0 model.
The source-independent global gauge is harmless for an unconditional
channel; coherent control of the entire operation requires its phase
ledger. As elsewhere, floating-point evaluation of these mathematical
enclosures is not an interval certificate.

## 5. Gaussian remainder and Duhamel bound

Use the full-linear reference L, not the RWA trajectory, for this step.
In the displaced thermal state on branch z, the spectral distribution of
X_i(t) is a real Gaussian with

```text
m_i(t,z) = 2 sum_m kappa_mi Re(alpha_L,m(t,z) exp(-i omega_m t)),
v_i = sum_m kappa_mi^2 (2 nbar_m+1),
M4(m,v) = m^4+6m^2 v+3v^2,
M6(m,v) = m^6+15m^4 v+45m^2 v^2+15v^3.                  (11)
```

Define `R_chi(X)=sin(chi+X)-sin(chi)-X cos(chi)`. For every real X,

```text
|R_chi(X)| <= X^2/2,
||R_chi(X)||_2 <= |sin chi| sqrt(M4)/2
                 +|cos chi| sqrt(M6)/6.                 (12)
```

The first inequality is the integral Taylor remainder; the second follows
by separating cosine and sine and their respective quadratic and cubic
remainders. These are global bounds, not assumptions that |X| is small.
For a sharper exact Gaussian RMS put A=sin chi, B=cos chi, theta=chi+m:

```text
rho(chi,m,v)^2 = E[R_chi(X)^2]
 = [1-exp(-2v)cos(2theta)]/2 + A^2+2ABm+B^2(m^2+v)
   -2A exp(-v/2)sin(theta)
   -2B exp(-v/2)[m sin(theta)+v cos(theta)].              (13)
```

This follows from `E exp(itX)=exp(itm-t^2 v/2)` and its derivative.
It includes the full thermal distribution, not a Fock truncation. Direct
evaluation can suffer catastrophic cancellation; a negative floating-point
answer is not physical evidence and silently clamping it is not a proof.

An equivalent nonnegative decomposition is preferable for evaluation.
Write E=exp(-v/2), retaining A, B and theta from (13):

```text
rho^2 = (E sin(theta)-A-Bm)^2
        +(sin(theta)^2/2)(1-exp(-v))^2
        +cos(theta)^2 exp(-v)(sinh(v)-v)
        +v(B-E cos(theta))^2.                            (13a)
```

To derive it, write X=m+Y for centered Gaussian Y. The first term is the
squared mean of the remainder. The even centered part has variance
`sin(theta)^2(1-exp(-v))^2/2`. Projecting the odd part on Y leaves variance
`cos(theta)^2[ E sin(Y)^2-v exp(-v) ]` and the last squared term;
the bracket is `exp(-v)(sinh(v)-v)`. All terms are nonnegative for v>=0.
Use `-expm1(-v)` and a stable small-v expression
`sinh(v)-v=v^3/6+v^5/120+...`, with an explicitly bounded tail if a machine
certificate is intended. No negative-value clamp is needed by this identity.

Let `Omega` purify the initial bus. Duhamel on each branch gives

```text
||(U_S,z(T)-U_L,z(T))Omega||
 <= integral_0^T ||[(H_S,z-H_L,z)/hbar] U_L,z(t)Omega|| dt
 <= B_z(T) := integral_0^T 2|u| sum_i |s_i| rho(chi_i,m_i,v_i) dt. (14)
```

For the stated piecewise bounded force, displaced thermal vectors have
all required quadrature moments; the linear reference lies in the domain
of the residual operator. The sine parent is bounded at each time.
The identity can equivalently be established by finite-energy regularization
and passage to the limit using the displayed integrable moment majorant.
Set `B_LD=max_(a,b) B_z`. Orthogonality of the electronic branches then gives

```text
(1/2)||Lambda_S-Lambda_L||_diamond <= min(1,B_LD),
(1/2)||Lambda_S-Lambda_R||_diamond
    <= min(1,B_LD+e_RWA(T)).                              (15)
```

There is no multiplicative factor 25, no incoherent sampling of input
branches, and no assumption that active or protected inputs are pure or
unentangled with a reference. In (14) the triangle inequality handles the
two simultaneously bright ions; it does not assume independent positions.
One may tighten it to the exact Gaussian quadratic form
`2|u| sqrt(sum_ij s_i s_j E[R_i R_j])`. Its covariance is
`v_ij=sum_m kappa_mi kappa_mj(2nbar_m+1)`, obtainable by differentiating
the joint Gaussian characteristic function. Dropping cross terms is not
an admissible tightening. The simpler bound (14) is already rigorous.

If B_LD >=1, (15) supplies no nontrivial channel accuracy guarantee. That
is an inconclusive sufficient bound, not a demonstration of large actual
error or a falsification of the exact sinus dynamics. No outcome is assumed.

## 6. A continuous-time enclosure, not just a time grid

Partition only within constant-u, constant-response segments. For a cell
of width h and midpoint tc, on each branch define

```text
F_m = 2|u| |g_m|,
A_m = |alpha_L,m(tc)| + (h/2) F_m,
D_i = 2 sum_m |kappa_mi| (F_m+omega_m A_m),
L_i = |m_i(tc)|+(h/2)D_i.                               (16)
```

These enclose `|f_L,m|`, `|alpha_L,m|`, `|dot(m_i)|`, `|m_i|`
throughout the cell. A simple certified mathematical contribution to B_z is

```text
h |u| sum_i |s_i| sqrt(M4(L_i,v_i)).                     (17)
```

A sharper enclosure retains the midpoint RMS (13). Since
`|partial_chi R|<=X^2/2` and `|partial_X R|<=|X|`, the L2 triangle
inequality applied to `X=m+sqrt(v)Z` with a fixed standard normal Z gives

```text
J_i = (|mu|/2)sqrt(M4(L_i,v_i)) + D_i sqrt(L_i^2+v_i),
rho_i(t) <= rho(chi_i(tc),m_i(tc),v_i)+(h/2)J_i.
R_i,cell = min(sqrt(M4(L_i,v_i))/2,
              rho_i(tc)+(h/2)J_i),
B_z <= sum_cells 2h|u| sum_i |s_i| R_i,cell.             (18)
```

No stochastic trajectory or quantum measurement is assumed in this
classical Gaussian representation of a single-time norm. Formula (18)
also exposes a manageable quadrature/enclosure gap: relative to the RMS
midpoint sum, the additive cell allowance is at most
`h^2 |u| sum_i |s_i| J_i`. This campaign fixes 256 equal subdivisions
per constant-amplitude segment and performs no adaptive refinement.
Any alternative subdivision budget requires a new preregistration.
Report the exact-RMS midpoint integral, continuous upper envelope and
their allowance as uncapped quantities; cap at 1 only when interpreting
a channel-distance bound. If the fixed budget does not resolve a threshold,
report INCONCLUSIVE.

Equations (16)-(18) are rigorous in exact arithmetic. A machine certificate
also requires directed/interval enclosures for the imported model data,
linear trajectory, trigonometric functions and accumulated roundoff.
Two agreeing floating-point grids or quadrature values are estimates of
the mathematical bounds, not such a certificate. Keep analytic enclosure
error distinct from floating-point error and inherited parameter uncertainty.

## 7. Continuous LD diagnostics and finite thermal tails

Report the maximum over all 25 branches, both envelopes, relevant ions and
the full interval of `sqrt(m_i(t,z)^2+v_i)`, together with its mean-excursion
and thermal components. Formula (16) gives cellwise upper envelopes.
The proposed diagnostic threshold 0.1 concerns dimensionless position kq.
It is not a necessary-and-sufficient theorem about channel accuracy.
Similarly, `nbar_m+|alpha_L,m(t,z)|^2` is a useful mode-excitation diagnostic;
small final alpha does not establish a small intermediate excursion.

The thermal position distribution has unbounded support even in vacuum.
For L>|m| its single-time tail satisfies

```text
Pr(|X|>L) = [erfc((L-m)/sqrt(2v))+erfc((L+m)/sqrt(2v))]/2
         <= 2 exp(-(L-|m|)^2/(2v)).                      (19)
```

At one time the ion positions commute; their simultaneous union event
has probability at most the sum of their marginal tails. A superposition
of electronic branches gives a mixture for position measurement, so the
maximum branch bound suffices. Uniform bounds on each single-time marginal
do not imply a joint classical path probability or justify a union over
uncountably many times. Duhamel avoids that inference entirely.

If a separate numerical method truncates initial thermal occupations to
`n_m<=N_m`, put t_m=nbar_m/(1+nbar_m). The excluded probability is

```text
p_tail=1-product_m(1-t_m^(N_m+1)) <= sum_m t_m^(N_m+1).   (20)
```

The normalized conditioned bus differs from the original thermal state by
trace distance p_tail. Therefore a half-diamond bound between two channels
proved only with this conditioned bus extends with additive allowance
`2p_tail`, capped at 1. This is an initial-state-tail statement, not a bound
for projecting the Hamiltonian onto a finite Fock basis during evolution.
The moment proof (11)-(18) needs neither truncation nor tail allowance.

## 8. Frozen decisions and limits

Before execution freeze, for each inherited envelope: final RWA comparison
(10) threshold `1e-3`; full-interval linearization bound (14)/(18) threshold
`1e-2`; and the separate continuous LD RMS diagnostic threshold `0.1`.
These numerical tolerances are chosen investigation targets, not values
supplied by the cited literature. State whether reported values are proven
enclosures or floating-point estimates. A nonpassing sufficient bound is
not actual gate infidelity. No refit of phase, amplitude, duration, geometry
or compensation may be hidden in this baseline audit.
The all-time RWA comparison (10a)-(10c) is an additional separately reported
coverage result; an endpoint pass alone is not an all-time channel guarantee.

Because all protected responses are zero in S, L and R, all three exact
operators factor as `I_P tensor U_(A,bus)`. Thus protected-source/reference
preservation is structural here; neither this LD nor RWA test establishes
real spectator darkness. The informative full contact's separate
source-coherence obstruction remains unchanged.

The seven-mode trap is still the harmonic Coulomb expansion at the prior
equilibrium. Relative-displacement/separation estimates are geometry
diagnostics only. Gaussian position distributions have nonzero weight
arbitrarily near ion coincidence; moments of the exact singular Coulomb
remainder cannot be assumed finite from these diagnostics. No global
Gaussian Duhamel certificate for the full Coulomb force is claimed.

## 9. Primary-source basis and attribution

Steane, Imreh, Home and Leibfried, *New Journal of Physics* **16**, 053049
(2014), article pp. 2-4 (PDF pp. 3-5), distinguish the walking-wave optical
potential, its LD expansion, the local light-shift phase and both oscillator
frequencies. In particular Eqs. (1), (4)-(8) retain the contributions lost
by a motional RWA. This supports separating those approximations and
recording local phases, not the present waveform's numerical validity.
[Primary full text](https://inspirehep.net/files/b4fa7012d2e81204d19a0a52c57af33f).

Hrmo et al., *Nature Communications* **14**, 2242 (2023), Results Eq. (1),
explicitly introduce their Ca40+ light-shift Hamiltonian after excited-state
elimination, LD and RWA. Results Eqs. (2)-(3) describe cyclic qudit
symmetrization; the preceding discussion explains unwanted local phases.
The present sinus parent and the explicit compensation-frame accounting
are additional declared assumptions, not a measured seven-ion Hamiltonian
from that experiment.
[Primary paper](https://www.nature.com/articles/s41467-023-37375-2).

Choi et al., *Physical Review Letters* **112**, 190502 (2014), p. 190502-2,
Eqs. (1)-(3), give multimode displacement and geometric-phase dynamics
under their stated approximations. Their qubit apparatus and conventions
differ; all signs and prefactors here were derived from (1).
[Primary full text](https://iontrap.duke.edu/files/2025/03/PhysRevLett.112.190502.pdf).

The conditional Duhamel estimate, Gaussian identities and bookkeeping above
are elementary derivations for this declared parent, not claims of a new
general approximation theorem or admission of a physical implementation.
