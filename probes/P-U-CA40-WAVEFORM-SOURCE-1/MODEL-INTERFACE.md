# Waveform builder interface — preparation only

NON-CANONICAL. This file and `model_builder.py` are source preparation.
No equilibrium, eigensystem, waveform construction or scan was executed
while writing them. Numerical use starts only after the new public pin.
The prior synthetic benchmark pin is unaffected.

## Scope and constants

`build_model(config=None) -> dict` uses Python standard library only.
Importing the module runs no construction. The optional dictionary rejects
unknown keys; the scientific run must use the frozen default dictionary.
The CLI is `python3 model_builder.py --output NEW_JSON_PATH`; it refuses
to overwrite an existing file. A successful construction is labelled
`MODEL_BUILT_NOT_VALIDATED`, never a validated scientific PASS.
An unavailable/ill-conditioned construction returns `INCOMPLETE`, an
explicit reason, and whatever earlier diagnostics exist. There is no search
over alternative timing, detuning or rank tolerances after a failed attempt.

The declared model has seven identical ions of mass
`40 * 1.66053906660e-27 kg`, axial angular frequency `2*pi*1 MHz`,
`hbar=1.054571817e-34 J s`, `e=1.602176634e-19 C`, and
`epsilon0=8.8541878128e-12 F/m`. These are frozen numerical constants;
40 atomic mass units is an explicit approximation to calcium-40.
The nominal beatnote is `mu=omega_z+2*pi*20 kHz`.
The interaction-picture detuning convention is `delta_m=omega_m-mu`.
The assumed axial wavevector is `Delta_k=2*pi/(397e-9 m)`.
These parameters are theoretical assumptions, not an ion measurement.

Dimensionless equilibrium minimizes

```
V(u) = 1/2 sum_i u_i^2 + sum_(i<j) 1/(u_j-u_i),  u_1<...<u_7.
length = (e^2/(4*pi*epsilon0*mass*omega_z^2))^(1/3).
H_ii = 1 + 2 sum_(j!=i) |u_i-u_j|^-3;
H_ij = -2 |u_i-u_j|^-3.
omega_m = omega_z sqrt(lambda_m).
eta_mi = Delta_k b_mi sqrt(hbar/(2 mass omega_m)) exp(i Delta_k x_i).
```

Damped Newton keeps the ordered chamber and reflection symmetry. A
maximum-pivot Jacobi diagonalization sorts eigenvalues and fixes each
eigenvector sign by its first maximum-magnitude component. Eigensystem
residual and orthogonality are checked separately. This axial model does
not supply radial confinement or prove stability against a zigzag mode.
It also omits heating, scattering, decay and counterrotating terms. A
5 MHz drive cap is a deliberately generous theoretical cap; satisfying it
does not validate an optical power calibration or the rotating-wave and
Lamb-Dicke approximations.

The standard equilibrium/mode formulation is described by
[James, quant-ph/9702053](https://arxiv.org/abs/quant-ph/9702053).
The five-cycle equality-phase construction is motivated by
[Hrmo et al., Nature Communications (2023)](https://www.nature.com/articles/s41467-023-37375-2).
Neither source provides this seven-ion waveform or certifies its parameters.

## Construction and signs

Each LS loop is 100 microseconds, with 16 equal real-amplitude segments.
Five identical LS loops alternate with ideal, instantaneous X5 operations,
including an X5 after the last loop. Total duration is 500 microseconds.
Shelving, unshelving and permutations are ideal; no hidden motion reset or
optical spatial-phase compensation is introduced.

For one branch, `g_m=sum_i eta_mi s_i` and

```
dot(alpha_m) = -i u(t) exp(i delta_m t) g_m,
Phi_m = |g_m|^2 integral_(t>v) u(t)u(v) sin(delta_m(t-v)) dt dv.
I_k = integral_segment_k exp(i delta_m t) dt.
Q_kk = Delta/delta - sin(delta*Delta)/delta^2;
Q_kl = Q_lk = Im(I_k conj(I_l))/2, k>l.
```

Small-detuning limits use stable series; `delta=0` is supported by these
integrals, though a zero imaginary closure row fails the frozen rank gate.
The 14 real closure rows (real and imaginary parts for seven modes) are
individually normalized. Pivoted, twice-reorthogonalized Gram–Schmidt must
produce rank 14 with pivots above `1e-8`; rank tolerance is `1e-10`.
The two-dimensional orthogonal complement must have normalized closure
residual at most `1e-11`. This is a numerical rank contract, not an exact
rank proof or an interval certificate.

In the nullspace choose the unit Euclidean-L2 shape maximizing the absolute
pair phase, by the largest-absolute eigenvalue of its 2-by-2 real matrix.
This is a deterministic quadratic optimization, not a peak-power optimum.
The shape has `sum a_k^2=1`, so for scale A its RMS is A/4 and integrated
loop power is `A^2*T/16`. Near-zero projected pair phase or optical pair
cosine is an explicit `INCOMPLETE` condition.

Five nominal closed loops give `Phi=kappa+beta*[label4=label5]`, with
`beta=2 sum_m Re(eta_m4 conj(eta_m5)) a^T Q_m a * A^2`.
The desired gate has phase `theta*[label4!=label5]`; thus
`beta=-theta (mod 2*pi)`. Both signs use genuinely different drive scales:
the accessible signed beta representatives have magnitudes 4*pi/5 and
6*pi/5. Negating a real waveform would not reverse this quadratic phase.
The raw global correction is fixed to the nominal G all-zero branch,
`gamma=kappa+beta`, including numerical inter-loop terms, and is exported.
G and E subtract the same frozen gamma; I subtracts zero. Stress contexts
do not redesign the pulse or refit a correction.

For speed, each loop first produces its scalar displacement d and phase q
from all 16 segments. Cycle c has `d_c=d exp(i delta*c*T)` and branch force
g_c. The complete composition retains
`sum_c q*|g_c|^2 + sum_(c>d) Im(d_c*g_c*conj(d_d*g_d))`.
This is algebraic factoring of the full chronology, not a loop reset.
Independent validation must integrate all 80 absolute-time segments.

## Arms and contexts

G: active ions 4 and 5 undergo X5; spectator logical 0 is shelved in a,
and all five spectator logical states remain in D during LS.
E: the intentionally wrong global X5 also acts on spectator physical
levels 0..4. A spectator's shelved logical 0 stays in a; each other logical
label visits physical `(label+cycle) mod 5`, including S. Five cycles still
restore its label, so endpoint populations alone do not reveal the error.
I: zero drive, no X5, the same 500 microseconds. Profiles exported for I are
irrelevant to its identically zero force and are not an asserted pulse word.

The four frozen contexts are nominal; `delta_m + 2*pi*100 Hz`; uniform
drive scale 1.005; and spectator-only differential D response 0.002.
The last uses physical S response 1, spectator physical D_p response
`epsilon*(p-2)` for p=1..4, and auxiliary response `-2*epsilon`.
Active D response stays zero by this declared perturbation's definition.
The thermal occupation is 0.05 in every mode and context. The detuning
perturbation shifts delta upward, equivalently lowering mu, not raising it.

## JSON contract

All complex numbers are `[real, imaginary]`. Mode and ion arrays use
increasing zero-based indices; named physical ion lists are one-based.

- Top level: `schema`, `status`, `scope`, `config`, `assumptions`, `modes`,
  `pulses`, `construction_diagnostics`, `contexts`, `jobs`.
- `modes`: `omega_rad_s[7]`, `vectors_by_mode[7][7]`, `positions_m[7]`,
  `eta_by_mode_ion[7][7][2]`, dimensionless positions/Hessian/eigenvalues
  and equilibrium/eigensystem diagnostics.
- Each `pulses` entry: `sign` (+1/-1), `theta_rad`, `beta_target_rad`,
  `amplitudes_rad_s[16]`, `unit_l2_shape[16]`, `scale_rad_s`,
  `peak_abs_rad_s`, `rms_rad_s`, `loop_seconds`, `block_seconds`.
- The 24 `jobs` are ordered sign (+,-), context (as above), arm (G,E,I).
  Each has `name`, `sign`, `context`, `arm`, `theta_target_rad`,
  `delta_rad_s[7]`, `nbar_by_mode[7]`, `profiles[5][7][5]`,
  `applied_amplitudes_rad_s[16]`, `loop_responses_by_mode[7]` and
  `coefficients`. Profile labels always mean the original logical label.
- `coefficients.alpha_common[7][2]` and
  `coefficients.alpha[7][7][5][2]` reconstruct alpha as common plus the
  seven label entries. Every label-0 entry of `alpha` is exactly zero.
- `phi_common_raw`, `nominal_global_correction_subtract_rad`, and
  `phi_common_corrected` are separate. Add `phi_unary[7][5]` and the 21
  lexicographically ordered `phi_pair` entries, each
  `{ions_zero_based:[i,j], values:[5][5]}`. Label-0 unary values and the
  pair matrix's row/column zero are exactly zero.
- There are 203 independent complex alpha coefficients and 364
  nonconstant real phase coefficients, plus the global phase.
  Zero padding makes label-indexed scanning straightforward.

The builder does not scan the 78,125 branches, calculate a diamond bound,
or establish source preservation. Those are subsequent validation tasks.
Preserving the source in this auxiliary G block is distinct from the
already established no-go for retaining every coherent source state while
the full informative contact writes distinguishable receiver records.
