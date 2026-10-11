# Direct sine versus full-linear evolution in a moving frame

Analytical contract for `P-U-CA40-SINUS-COMPARISON-1`, reservation #1456.
NON-CANONICAL; a conditional seven-mode calculation, not physical admission.
This derivation was prepared without executing or importing scientific code.
The exposed input is the sealed `P-U-CA40-TRAJECTORY-VALIDITY-1` model and
its two frozen envelopes. No waveform, geometry or phase is retuned.

## 1. Fixed question and scope

Compare the compensated sine parent S with its full first-order
linearization L, including both rotating and counterrotating terms. Keep
all seven harmonic axial modes, the 500-us absolute clock, five repeated
100-us loops, 16 amplitude segments per loop, and the inherited ideal
instantaneous X5 carriers. The active ions are 4 and 5 in physical order
`(s,x,u,y,w,q,r)`; the other five ions are exactly dark by premise.

The electronic panel is only `(4,3)`, `(4,4)`, `(1,1)`, for both frozen
angle envelopes. The first pair resolves the previously exposed RWA/L
coherence witness; `(1,1)` samples a previously exposed large excursion.
These choices are not an all-25-branch or full-contact certificate.

Write, with real inherited kappa and real envelope u,

```text
X_i(t) = sum_m kappa_mi [a_m exp(-i omega_m t)
                        + a_m^dagger exp(i omega_m t)],
chi_i(t) = k x_i - mu t,
s_i(z,l) = 1[z_i+l=0 mod 5],  i=4,5,
H_S/hbar = 2u sum_i s_i [sin(chi_i+X_i)-sin(chi_i)],
H_L/hbar = 2u sum_i s_i cos(chi_i) X_i.                 (1)
```

The complex spatial coefficient is `eta_mi=kappa_mi exp(i k x_i)`.
The inherited full-linear solution uses

```text
f_L,m = u [g_m exp(i(omega_m-mu)t)
           + conj(g_m) exp(i(omega_m+mu)t)],
g_m = sum_i eta_mi s_i,
dot(alpha_L,m) = -i f_L,m,
dot(Phi_L) = Im sum_m dot(alpha_L,m) conj(alpha_L,m),
U_L,z = exp(i Phi_L,z) D(alpha_L,z).                   (2)
```

The same unary compensation in S and L cancels in their relative
evolution. For the inherited repeated word, `mu*100 us=2pi*102`, and each
active ion visits S once, so the uncompensated sine parent differs at the
endpoint by the previously derived common phase. This does not justify
resetting the absolute optical or oscillator clock between loops.

## 2. Exact moving-frame equation

Define `W_z=U_L,z^dagger U_S,z`, initially identity. Since
`D(alpha)^dagger a D(alpha)=a+alpha`,

```text
i dot(W_z) = R_z(t) W_z,
m_i(t,z) = 2 sum_m kappa_mi Re[alpha_L,m(t,z) exp(-i omega_m t)],
R_z = 2u sum_i s_i [sin(chi_i+m_i+X_i)-sin(chi_i)
                    -cos(chi_i)(m_i+X_i)].             (3)
```

Equation (3) removes the known large coherent displacement without
discarding its effect on the nonlinear potential. It retains every mode,
the full thermal input, time ordering and all Weyl phases. When both
responses vanish, R is zero and W is constant; that interval can be
skipped computationally while the absolute time advances. Branch `(4,3)`
has two occupied loops; the two equal-label branches each have one.

For `beta_im(t)=i kappa_mi exp(i omega_m t)`,

```text
exp(i X_i)=D(beta_i),
sin(A_i+X_i)=[exp(i A_i)D(beta_i)
              -exp(-i A_i)D(-beta_i)]/(2i),
A_i=chi_i+m_i.                                        (4)
```

All oscillator operators in (3)-(4) remain those of the same seven-mode
Hilbert space. An independently damped or freshly thermalized bus after
each loop would define a different model.

## 3. Total-phonon Galerkin space and the true sine

Let P_L project onto `|n|=sum_m n_m <= L`, Q_L=I-P_L. Its dimension is
`d_L=binomial(L+7,7)`: d_4=330 and d_6=1716. This retains every mode and
limits their joint occupation; it does not omit six modes or freeze them
in vacuum. The exact projected equation is

```text
i dot(psi_L)=P_L R_z(t) P_L psi_L.                    (5)
```

For B=`sum_m conj(beta_m) a_m`, normal ordering gives the useful identity

```text
P_L D(beta) P_L
 = exp(-||beta||^2/2)
   exp(P_L B^dagger P_L) exp(-P_L B P_L).              (6)
```

Both exponentials on the right are finite polynomials through degree L.
To prove (6), annihilation acts first and only lowers total occupation.
Creation then only raises it. A creation path that crosses L cannot
return to P_L, so intermediate projections remove no path contributing
to the final projected matrix element. The proof also gives
`P_(L+1) D(beta) P_L` using one additional creation shell if needed.

Thus (4) and (6) compute `P_L sin(A+X) P_L`, the projection of the full
operator. It is generally different from `sin(A+P_L X P_L)`. The latter
would artificially close excursions at the cutoff and is not used.
The exact projected displacement is a contraction, with
`[P_L D(beta) P_L]^dagger=P_L D(-beta) P_L`; it is not unitary.
Consequently (5) has a Hermitian generator and its exact solution is
unitary within P_L. Floating-point evaluation and RK4 are separate
approximations to this exact Galerkin statement.

Sparse lowering/raising actions cost O(7 d_L); the polynomial application
costs O(7 L d_L) per vector, without a dense d_L-by-d_L displacement.
This is an operation-count observation, not a measured runtime promise.

## 4. Deterministic thermal mixture, with its omitted mass exposed

Each mode has the inherited mean occupation 0.05, so r=1/21 and

```text
rho_th = sum_n p_n |n><n|,
p_n=(1-r)^7 r^|n|,
q_K = sum_(|n|<=K) p_n
    = (1-r)^7 sum_(j=0)^K binomial(j+6,6) r^j,
p_tail = 1-q_K.                                      (7)
```

This campaign fixes K=3, hence 120 deterministic initial Fock states,
all contained in both Galerkin spaces. Their weights remain
UNNORMALIZED p_n. No Monte Carlo sample or vacuum substitution is used.
The exact finite rational sum (7) defines the initial thermal tail.
For an optional symbolic upper estimate, the first omitted total-number
weight w_(K+1) has subsequent ratios no larger than
`r*(K+8)/(K+2)`, giving `p_tail <= w_(K+1)/(1-r*(K+8)/(K+2))`.

States can be propagated in batches. For a given initial n, retain the
complex amplitudes and their electronic branch phases until all required
overlaps are formed. Summing probabilities before those overlaps, or
averaging state amplitudes between different n, would change the answer.
This weighted construction is equivalent to using the purification

```text
|Omega>_BE = sum_n sqrt(p_n) |n>_B |n>_E,              (8)
```

where E is an untouched reference. It avoids storing a dense thermofield
tensor while preserving exactly the same retained reference correlations.

## 5. Overlaps, restored laboratory-frame coherences and error scope

For each branch the moving-frame overlap is

```text
C_z = Tr(rho_th W_z),
C_z,ret = sum_(|n|<=3) p_n <n|W_z|n>.                 (9)
```

If the retained states were evolved exactly, the omitted terms give the
complex-disc bound `|C_z-C_z,ret|<=p_tail`. Its squared modulus is the
overlap of the two corresponding fixed thermal purifications. It must
not be relabeled as the Uhlmann fidelity of their reduced bus states.
The complex phase must be reported: separate phase fits for each branch
can erase a physically observable electronic error.

For a common phase gamma and any chosen panel branch,

```text
||[(U_S,z-exp(i gamma)U_L,z) tensor I_E]|Omega>||^2
 = 2-2 Re[exp(-i gamma) C_z].                         (10)
```

The maximum square-root over panel branches bounds the corresponding
fixed-bus Stinespring distance, and therefore the half-diamond channel
distance on that panel, including arbitrary electronic references. This
is a mathematical consequence if all numerical errors are bounded; the
present convergence diagnostics alone do not provide such certification.

To compare electronic coherences of distinct branches a,b, restore their
different linear frames:

```text
K_S(a,b)=Tr[rho_th W_b^dagger U_L,b^dagger U_L,a W_a],
U_L,b^dagger U_L,a = exp(i theta_ab) D(delta_alpha_ab),
delta_alpha_ab=alpha_L,a-alpha_L,b,
theta_ab=Phi_L,a-Phi_L,b
         +Im sum_m conj(alpha_L,b,m) alpha_L,a,m.      (11)
```

The retained estimator is the weighted sum of these matrix elements
between propagated vectors. Equation (6) gives the exact projected
matrix element of the displacement in (11); its loss of unitarity after
projection must not be patched by renormalization. Using only
`<W_b n|W_a n>` would omit physical relative displacement and Weyl phase.
The analytic full-thermal linear reference is

```text
K_L(a,b)=exp(i theta_ab)
         exp[-sum_m (nbar_m+1/2)|delta_alpha_ab,m|^2]. (12)
```

For exact retained dynamics, `|K_S-K_S,ret|<=p_tail`. A two-branch Bell
input has output trace distance `D_Bell=|K_S-K_L|/2`, hence lies between
`max(0,|K_S,ret-K_L|-p_tail)/2` and
`min(1,(|K_S,ret-K_L|+p_tail)/2)`. These are thermal-tail allowances only;
projection, time discretization and roundoff must be added or explicitly
left uncertified. In particular, they are not standalone certified
infinite-dimensional error bars on the executed numerical estimators.

If normalized numerical state errors were independently bounded by
epsilon_(z,n), the additional C error is at most `sum_n p_n epsilon_(z,n)`
and the additional Gram error is at most
`sum_n p_n [epsilon_(a,n)+epsilon_(b,n)]` for exact normalized comparison
states. Norm drift in computed states requires its own allowance; no
silent state renormalization is authorized by these formulas.

## 6. Dynamical cutoff leakage: a meaningful sampled diagnostic

For the exact Galerkin path, Duhamel gives

```text
||U_R(t)|n>-psi_L,n(t)||
 <= integral_0^t ||Q_L R(v) psi_L,n(v)|| dv.           (13)
```

The full and projected initial states agree because K<=L. Equation (13)
requires the full residual integral, not just norm conservation inside
P_L or agreement between two cutoffs. For any psi in P_L,

```text
ell_D,plus/minus^2
 = ||psi||^2-||P_L D(plus/minus beta_i)P_L psi||^2,
ell_X,i^2
 = ||kappa_i||^2 ||psi_top||^2
   +||sum_m kappa_mi exp(-i omega_m t) a_m psi_top||^2,
psi_top = projection onto |n|=L of psi.               (14)
```

The first identity follows from unitarity of the full displacement; the
second from `Q_L X_i psi=B_i^dagger psi_top` and the canonical commutator.
The constant terms in (3) cannot leave P_L. A usable bound is therefore

```text
||Q_L R psi|| <= 2|u| sum_i |s_i|
  [(ell_D,plus+ell_D,minus)/2 + |cos(chi_i)| ell_X,i]. (15)
```

Evaluate the frozen sampled version of (14)-(15), retaining raw negative
norm-deficit diagnostics because subtraction can be cancellation
sensitive. A tolerance or a displayed square-root clamp is numerical
handling, not an interval proof of positivity. No large guard basis is
required. The weighted purification residual uses
`sqrt(sum_n p_n ||Q_L R psi_n||^2)`; (15) can bound its summands.

The implemented sampled grid is every RK4 stage of every occupied step.
For each retained thermal column accumulate
`e_n += h*(rho_1+2 rho_2+2 rho_3+rho_4)/6`, with rho from (15), h the
step duration, and the actual intermediate RK stage vectors. Report the
branch aggregate `sqrt(sum_n p_n e_n^2)` with unnormalized weights.
The intermediate vectors are RK approximations, not exact trajectory
samples or exact midpoint states; these weighted sums are not certified
quadrature bounds. Record the minimum raw projected-displacement norm
deficit. A deficit below `-1e-10*(1+||psi||^2)` fails numerical integrity;
smaller negative values are clamped only for the diagnostic square root.
Also retain maximum boundary population and norm drift, without any
state renormalization. In exact arithmetic, if each e_n bounded its true
residual integral, the same weighted aggregate would bound the retained
purification error. The sampled computation does not assert that premise.

A tighter theoretical alternative, not required by this campaign, writes
T=`sum_i s_i sin(A_i+X_i)` and V=`sum_i s_i cos(chi_i)X_i`. At equal time
the X_i commute, so `<T^2>` is expressible with D(beta_i+/-beta_j) through
the sine-product identity. Then the exact leakage squared is

```text
||Q_L R psi||^2 = 4u^2 [<T^2>-||P_L T psi||^2
                       +||Q_L V psi||^2
                       -2 Re<shell_(L+1) T psi,Q_L V psi>]. (16)
```

Only V reaches the single shell L+1. Equation (16) explains a possible
future improvement; it is not a claim that this kernel evaluates it.
Neither sampled (15) nor sampled (16) becomes a rigorous integrated
bound without a controlled quadrature/enclosure and floating-point
allowance. The campaign reports leakage diagnostics, not that missing
certificate. Thermal occupation tail and dynamical cutoff leakage are
different errors and are not interchangeable.

## 7. Frozen time scheme and interpretation of convergence

Use classical explicit RK4 for (5), without state renormalization. Each
6.25-us constant-amplitude segment has the fixed number of equal
substeps below. Force switches coincide with segment boundaries; evaluate
the smooth expression on each occupied segment using that segment's
fixed response and amplitude. Absolute-time phases are evaluated at
each RK stage. Zero-response segments advance the clock exactly and do
not require RK work.

The complete fixed panel is, in this order:

| Total cutoff L | Substeps per segment | Purpose |
|---|---:|---|
| 4 | 128 | Smaller dynamical space |
| 6 | 128 | Cutoff comparison at the same step |
| 6 | 256 | First time refinement |
| 6 | 512 | Second time refinement |

K remains 3 throughout. Kernel launches and runs have one 1800-s budget
measured from entry including setup; final validation, comparison and
archival can extend the overall wall time. The campaign preserves
completed partial results and does not retry or add L=8,
K=4, adaptive steps or a retuned pulse after seeing an outcome.
RK4 is fourth order for the finite smooth equation within each segment;
observed refinement ratios, norm drift, cutoff agreement and sampled
leakage are diagnostics, not proofs of an infinite-bus error bound.
The previous large continuous Duhamel upper bound was inconclusive; this
calculation tests its actual nonlinear dynamics on the stated panel.
It cannot retroactively turn that upper bound into an observed error.

## 8. What the comparison can and cannot decide

All seven declared axial modes are present. Thus no omitted axial-mode
tail is used. Radial motion, trap anharmonicity, finite carrier duration,
scattering, heating, optical realization and imperfect hiding remain
external model assumptions. A thermal tail controls only initial
occupation; it does not bound those omitted physical interactions.

The exact dark-protected premise makes both full propagators act as
identity on the five protected registers, even when those registers are
entangled with an external reference. This is a structural result of the
conditional model, not a numerical test of hardware darkness. It does
not restore complete-source preservation for the previously studied
informative full contact, whose source/reference obstruction is distinct.

A useful outcome is a reproducible finite-panel nonlinear/linear
coherence discrepancy or a clearly stated converged numerical estimate,
with thermal tail, cutoff, step-size, norm and leakage diagnostics shown
separately. Incomplete or nonconverged output remains an honest limited
result. No all-state physical admission or full 56-G contact conclusion
follows from this study.
