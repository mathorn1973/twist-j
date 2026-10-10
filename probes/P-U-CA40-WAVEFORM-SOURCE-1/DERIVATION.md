# Shared-waveform derivation and complete-source criterion

PUBLIC NON-CANONICAL analytical derivation, 2026-10-10. No solver, scientific executable,
simulation or benchmark was run for this derivation. This is a conditional
harmonic model, not a calibrated seven-ion device or native admission.
It extends the prior pair experiment's pulse contract and source analysis,
without changing either prior result. The numerical manifest and public pin
must fix all parameters, conventions and acceptance tolerances before runs.

## 1. Carrier, chronology and declared idealizations

Physical ion order is `(s,x,u,y,w,q,r)`. The active pair is `A=(4,5)`;
the protected group is `P=(1,2,3,6,7)`, containing source `(s,q,r)`.
Electronic input labels are `z_i in {0,1,2,3,4}`. Each protected ion is
hidden by the isometry `V|0>=|a>, V|j>=|j>` for j=1,...,4, and returned
by its actual adjoint. No unknown input is initialized or reset.

During loop l=0,...,4 the active physical labels are `(z_i+l) mod 5`.
After each LS block, including the fifth, apply the previously fixed
phase-exact X5 to ions 4 and 5 only. Its four chronological pi-pulse
phases on transitions 01,02,03,04 are `(pi/2,-pi/2,pi/2,-pi/2)`.
Thus the final electronic permutation is the identity, including P.
All carrier pulses are ideal and of zero duration in this first model.
LS amplitude is zero during their application. This removes no real-world
carrier error, storage phase, finite-time cost, scattering or heating.

The proposed theoretical manifest uses the seven axial modes of the
Coulomb equilibrium of seven identical Ca40+ ions in a harmonic axial
trap. Its proposed scales are omega_z=2pi*1 MHz, mu=omega_z+2pi*20 kHz,
tau_LS=100 us and K=16 equal segments. The coupling is

```text
eta_mi = Delta_k b_mi sqrt(hbar/(2 M omega_m)) exp(i Delta_k x_i),
Delta_k = 2pi/(397 nm),        delta_m = omega_m-mu.
```

Here b is a real orthonormal normal-mode matrix, M is the declared ion
mass, and the displayed Delta_k is a theoretical effective wavevector
choice, not the measured wavevector geometry of the published 401 nm
Ca40+ experiment. The complex spatial phase exp(i Delta_k x_i) is retained;
there is no implicit local compensation of the traveling-wave phase.
Mode signs are arbitrary provided eta is used consistently.
Axial stability, equilibrium residuals, orthonormality and
mode frequencies require numerical checks; radial decoupling is assumed.

For the nominal profile, active level S has response 1 and every active
D level has response 0; every hidden protected level has response 0.
A proposed stress profile assigns hidden original label j the response
epsilon*(j-2), epsilon=0.002, including original j=0 on shelf a.
This is a declared synthetic differential D response, not Ca40+ data.
Keep this label-to-shelf map explicit rather than applying j-2 to the
physical shelf index. The nominal thermal occupation is nbar_m=0.05.
The shift delta_m+2pi*100 Hz (equivalently lowering mu), force-amplitude
+0.005 fraction, and the differential
D profile are separate proposed contexts; their precise composition is
fixed by the manifest. A fractional force change is not automatically
the same fractional laser-power change.

## 2. Hamiltonian and exact segment formulas

Use one interaction frame and one absolute clock through all five loops.
For a fixed electronic input branch z, define

```text
H_z(t)/hbar = sum_m [ f_m(t,z) a_m^dagger + conj(f_m(t,z)) a_m ]
             + d_z(t) I,
f_m(t,z) = u_k exp(i delta_m t) g_ml(z),
g_ml(z) = sum_i eta_mi response_i(z_i,l),
D(alpha) = exp(sum_m alpha_m a_m^dagger-conj(alpha_m) a_m),
U_z(t) = exp(i Phi_z(t)) D(alpha_z(t)).
```

u has units of inverse seconds, eta and response are dimensionless,
alpha is dimensionless, and Phi is an angle. d is a real diagonal
electronic frequency; the first ideal model sets it to zero explicitly.
Fixed one-ion corrections can instead be included as declared unary
phases. There is no free branch-dependent correction fitted after a run.
Real negative u means a pi change of force phase, not negative intensity.

Since the force is linear in independent harmonic oscillators, its
commutator is a scalar on each branch. Magnus terminates after order two:

```text
alpha_m(t) = -i integral_0^t f_m(v,z) dv,
Phi_z(t) = sum_m Im integral_(t1>t2) f_m(t1,z) conj(f_m(t2,z)) dt1 dt2
           - integral_0^t d_z(v) dv.                         (1)
```

For one segment [t0,t0+Delta] with fixed F_m=u_k*g_ml(z), let

```text
I_m = Delta exp(i delta_m*(t0+Delta/2)) sinc(delta_m*Delta/2),
beta_m = -i F_m I_m,
q_m = (delta_m*Delta-sin(delta_m*Delta))/delta_m^2,
chi = sum_m |F_m|^2 q_m - integral_segment d_z(t) dt.       (2)
```

sinc(x)=sin(x)/x with sinc(0)=1. At delta=0, I=Delta and q=0;
for small x=delta*Delta use q=Delta^2*(x/6-x^3/120+...), not
subtraction of nearly equal numbers. The exact chronological append is

```text
Phi <- Phi + chi + Im sum_m beta_m conj(alpha_m),
alpha <- alpha + beta.                                    (3)
```

The old alpha is used in the first line. This follows from
`D(beta)D(alpha)=exp(i Im sum beta*conj(alpha))D(beta+alpha)`.
Later segments multiply on the left. Omitting this cross term, resetting
alpha after an imperfect loop, or resetting exp(i delta*t) at a cycle
boundary changes the model. Absolute phase remains continuous even in
stress contexts in which nominally closed loops no longer close.

A useful exact sign fixture is the chronological displacement rectangle
`1,i,-1,-i`: final alpha=0 and Phi=2. Reversing its traversal changes
Phi to -2; negating all four displacements preserves Phi=2.

## 3. Closure and a concrete finite pulse family

For one loop with time-independent profile, put
`A_mk=integral_(k Delta)^((k+1)Delta) exp(i delta_m t)dt`, k=0,...,15.
Then alpha_m=-i*g_m(z)*(A u)_m. Therefore Au=0 closes every
electronic branch of that loop, irrespective of the profile coefficients.
The real-amplitude system stacks Re A and Im A into a real 14 by 16
matrix. Its nullity is at least two. For complex amplitudes the real
matrix is `[Re A,-Im A; Im A,Re A]`, of size 14 by 32.

There is also a direct analytical construction on this equal partition:

```text
P(w) = product_(m=1)^7 [w^2-2 cos(delta_m Delta) w+1],
sum_(k=0)^15 u_k w^k = (a+b w) P(w),       a,b real.       (4)
```

Indeed A_mk=J_m exp(i delta_m*k*Delta), where
J_m=integral_0^Delta exp(i delta_m t)dt; evaluation of (4) at
w=exp(i delta_m Delta) vanishes. The two coefficient vectors P and
wP are linearly independent. Coincident roots or J_m=0 cause no
failure of closure, though the full nullspace may then be larger.
For delta_m=0 the factor (w-1)^2 also enforces closure.
This is an algebraic cross-check, not a claim of numerical stability of
root-polynomial coefficients or a replacement for a frozen solver.

For a real envelope u, the one-loop phase for mode m is
`Q_m(u)=u^T Q_m u`, with

```text
(Q_m)_kk = (delta_m Delta-sin(delta_m Delta))/delta_m^2,
(Q_m)_kl = (Q_m)_lk = (1/2) Im(A_mk conj(A_ml)),  k>l.    (5)
```

Projecting the desired interaction quadratic form onto an orthonormal
closure basis and diagonalizing the resulting small real symmetric
matrix supplies a finite candidate direction. The largest absolute
eigenvalue minimizes the squared envelope norm at fixed absolute
interaction in that declared subspace. It does not optimize peak
amplitude, bandwidth, robustness or hardware gate time. A zero interaction
form, unacceptable residuals, excessive scale or imposed power limits
must produce INCOMPLETE, not a fabricated gate. Rank alone is insufficient.

## 4. Both gate angles and the actual common phase

With nominal zero D responses, write the active labels a,b and
`g_ml=eta_m4*1[a+l=0]+eta_m5*1[b+l=0]` (labels modulo 5).
For five identical individually closed blocks, sums of indicators give

```text
kappa = sum_m Q_m(u) (|eta_m4|^2+|eta_m5|^2),
beta  = 2 sum_m Q_m(u) Re(eta_m4 conj(eta_m5)),
Phi(a,b) = kappa + beta*1[a=b],
U_pair = exp(i gamma) G(theta),
gamma=kappa+beta,       theta=-beta mod 2pi,
G(theta)|a,b> = exp(i theta*1[a!=b])|a,b>.                (6)
```

A common label-independent hidden force B_m only adds the common phase
`sum_m Q_m [5|B_m|^2+2 Re(conj(B_m)*(eta_m4+eta_m5))]`.
It must not be discarded if the entire program is coherently controlled.
For an ordinary unconditional electronic channel a single global phase
is immaterial. Keep raw kappa, beta and gamma in the receipt anyway.

Scaling u by lambda preserves nominal closure and multiplies kappa,
beta and gamma by lambda^2. If a direction has nonzero unwrapped
theta0=-beta0, both targets can use its same orientation:

| sign(theta0) | unwrapped theta for target +4pi/5 | for target -4pi/5 |
|---|---|---|
| positive | +4pi/5 | +6pi/5 |
| negative | -6pi/5 | -4pi/5 |

Choose lambda_sigma=sqrt(theta_unwrapped_sigma/theta0), which is real
in this table. The two frozen envelopes really differ in amplitude;
the larger phase uses sqrt(3/2) times the force and 3/2 times its squared
norm. Which target needs that larger amplitude depends on orientation.
Changing u to -u or multiplying it by a common unit complex phase does
not reverse the quadratic geometric phase. Reversing detuning requires
a new closure calculation for every mode.

For the simple same-direction broad-count primitive `exp(i chi n0^2)`,
five cycles have gamma=4chi and theta=-2chi. Positive chi=3pi/5 yields
target +4pi/5, whereas chi=2pi/5 yields target -4pi/5. Their raw common
phases are 12pi/5 and 8pi/5. With opposite active forces, theta=+2chi
and the assignment reverses. Do not confuse a one-loop area chi with
the normalized two-ion angle theta or inherit a different oracle's
global phase by replacing only its target label.

Stress contexts must use the frozen envelopes and nominal correction.
They are not independently retuned after seeing the stress result.

## 5. Coefficient reduction retains the same joint evolution

Under this diagonal linear-force and local-monomial-carrier model,
alpha is a sum of one-ion functions. Phi is a sum of constant, one-ion
and two-ion functions, including all chronological Weyl terms. Products
arise only between two additive force contributions. There is no
three-ion term unless additional interactions or controls are introduced.

Anchor every input label at 0. Then alpha has seven complex constants
and 7 modes * 7 ions * 4 nonzero-label increments: 203 complex entries.
Phi has one common constant, 7*4=28 unary and C(7,2)*4^2=336 pair
entries. The previously stated 364 phase entries exclude the separately
retained common phase. Unary and pair entries can be obtained by anchored
finite differences; a general phase needs at most 365 anchor branches.
These are coefficients derived from (1)-(3), not independent inputs.
Independent direct branch integration must check this reconstruction.

For a product thermal bus initially independent of all electronic and
reference systems, nu_m=nbar_m+1/2. Tracing the final bus gives

```text
K(z,z') = exp(i[Phi(z)-Phi(z')+Im sum_m conj(alpha_m(z')) alpha_m(z)])
          * exp(-sum_m nu_m |alpha_m(z)-alpha_m(z')|^2).   (7)
```

The imaginary term is the Weyl phase. Thermal damping alone, a vacuum
replacement, or independent noise after each loop does not implement (7).
This exact reduction assumes a closed harmonic bath with fixed initial
state; intermediate heating, scattering or damping require their own
environmental dynamics and cannot be inferred from endpoint alpha.

## 6. Uniform source-and-reference preservation certificate

Write z=(p,a), with all 3125 protected labels p and all 25 active labels a.
Use the actual corrected Phi and final alpha. Suppose the final protected
permutation is p itself and the active permutation pi(a) is independent
of p. Anchor p0=(0,0,0,0,0) and define the reference joint evolution

```text
W0 |p,a> |bath> = exp(i Phi(p0,a)) |p,pi(a)> D(alpha(p0,a))|bath>.
```

It is `I_P tensor W_(A,bus)` and may have nonzero active-dependent bus
displacement. Thus it preserves every PR marginal, including inputs
with arbitrary correlations or entanglement between P,A and an arbitrary
reference R. Only the bus input is fixed and independent. Neither A
nor P need initially be pure, factorized or a selected Fourier state.

For comparison with the actual evolution, put

```text
dalpha(p,a)=alpha(p,a)-alpha(p0,a),
r_pa=sum_m nu_m |dalpha_m(p,a)|^2,
delta_pa=Phi(p,a)-Phi(p0,a)
         +Im sum_m conj(alpha_m(p0,a))*alpha_m(p,a),
v_pa=exp(-r_pa)*exp(i delta_pa).                          (8)
```

The last term in delta is essential. It is the phase in
`D(alpha(p0,a))^dagger D(alpha(p,a))`. Purify the thermal bus, using
the same fixed purification for actual and reference isometries.
Their column overlap is v_pa; distinct electronic output branches are
orthogonal. Therefore their operator-norm distance is exactly

```text
e_P = max_(p,a) sqrt(2-2 Re v_pa),
(1/2)||Lambda-Lambda0||_diamond <= min(1,e_P).             (9)
```

The bound follows by applying the two isometries to an arbitrary input
with a reference, bounding pure-state trace distance by vector distance,
then using contractivity when the purified bath is discarded. It is
dimension independent. In particular, for every initial rho_PAR,

```text
(1/2)||rho'_PR-rho_PR||_1 <= min(1,e_P).                 (10)
```

Tracing part of P gives the same bound for the source (s,q,r) and any
retained reference. The comparator is a complete channel on the active
pair, not an uncorrelated guessed output state for that pair.

For reporting, rP=max r_pa and etaP=max|wrap(delta_pa)| give, when
etaP<=pi/2, the conservative bound
`min(1,sqrt(2-2 exp(-rP) cos(etaP)))`. Evaluate its squared interior
stably as `-2 expm1(-rP)+4 exp(-rP) sin(etaP/2)^2`.
Outside that useful phase range report the trivial bound 1 or use (9).
These are rigorous bounds for exact coefficients of the declared model.
Floating-point maxima and the resulting reported bounds are numerical
estimates unless proven numerical error margins enlarge rP and etaP.
Agreement of two floating-point calculations is not an interval certificate.

Exact independence of alpha and exp(i Phi) from p gives e_P=0 and
operator factorization for every bus input, a stronger statement than
the thermal-bound certificate. A common bus displacement need not be
zero for source protection. Conversely a source-dependent scalar phase
can disturb coherences even when every alpha is zero. Known local
protected phases are restored only by declared physical corrections;
an analysis frame must be labeled as such. Mixed protected-protected
phases cannot be removed by one-ion corrections.

With zero hidden responses, even the detuning and amplitude contexts
remain structurally independent of p: their source certificate can be
exact while the active gate is poor. The D-response context is a real
source challenge. In perfectly closed identical loops its active-P
cross terms sum to unary P phases, but the term `5|B_m(p)|^2` can still
contain protected-protected conditional phases. Closure does not remove it.

## 7. Gate bound and informative-contact negative control

For the whole desired gate use the reference isometry
`I_P tensor G(theta_sigma) tensor I_bus`, with the one declared common
phase gamma removed. Set

```text
rG=max_z sum_m nu_m |alpha_m(z)|^2,
etaG=max_z |wrap(Phi(z)-gamma-theta_sigma*1[z4!=z5])|.
```

The same purified-bus proof gives the above half-diamond bound with
rG,etaG. Its exact per-branch form is (9) with alpha0=0 and target Phi.
Thus gate failure and source failure are distinct outputs. Passing a
finite measurement panel alone would not establish either uniform bound.

The full informative contact is a different unitary:
`U_C|s,v>=|s,C_s(v)>`, where u shifts by -2(y-x)s and w by +2(y-x)s
over F5. At a fixed receiver basis v with h=y-x nonzero, its five outputs
`|C_s(v)>` are mutually orthogonal. Hence the source channel is exactly
`rho_S -> sum_s rho_ss |s><s|`. Input |+> becomes I5/5: purity 1/5,
fidelity with the original pure state 1/5, and trace distance 4/5.
For the initial Bell source-reference state
`|Omega>=sum_s |s>_S|s>_R/sqrt(5)`, the final SR marginal is
`sum_s |ss><ss|/5`, again fidelity 1/5 and trace distance 4/5.
These conclusions follow from the actual contact permutation, independent
of its monomial phases; q,r are spectators to this contact. They are not
inferred from imperfect pair pulses. A simulator claiming universal
full-source preservation for this informative case must fail this control.

## 8. Attribution and boundary

The linear-force propagator, multimode closure and pulse construction are
established trapped-ion methods, not a newly claimed general theorem.
Choi et al., PRL 112, 190502 (2014), p.2 Eqs.(1)-(3), give a multimode
displacement/phase description and segmented-pulse closure; their force,
Pauli and detuning conventions differ, so signs above were derived from
the displayed Hamiltonian rather than copied. Their experiment is a
five-ion Yb171+ qubit experiment, not seven Ca40+ ququints.
[Primary full text](https://iontrap.duke.edu/files/2025/03/PhysRevLett.112.190502.pdf).

Blumel et al., npj Quantum Information 7, 147 (2021), Results Eqs.(3)-(4)
and Methods, describe nullspace projection and interaction-matrix
diagonalization. We use that established finite linear-algebra method,
without inheriting a calibrated pulse or an unrestricted optimality claim.
[Primary paper](https://www.nature.com/articles/s41534-021-00489-w).

Hrmo et al., Nature Communications 14, 2242 (2023), Eqs.(1)-(3), motivate
the Ca40+ LS force and cyclic equality-phase gate. The present seven-mode,
zero-duration-carrier waveform model is an additional theoretical extension.
[Primary paper](https://www.nature.com/articles/s41467-023-37375-2).

The prior public pair pulse contract is
`notes/C-U-CA40-PAIR-EXPERIMENT-DESIGN-N/PULSES.md`, sections 2-4;
the full-source distinction and informative-contact control are already
proved in `notes/C-U-CONTACT-FULL-SOURCE-ADMISSION-N/SOURCE-PROOF.md`,
sections 3-8. This draft specializes them to one shared waveform model.
It does not certify physical carrier preparation, pulse power, timing,
work or heat, omitted modes, spontaneous emission, finite carrier errors,
or conservation of the full source throughout intermediate times.
