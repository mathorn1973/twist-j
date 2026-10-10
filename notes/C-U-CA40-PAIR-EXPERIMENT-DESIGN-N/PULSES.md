# Pulse protocol for one occupied pair in seven Ca40 ions

**PUBLIC / NON-CANONICAL / proposed experiment; no execution.**
Author: A. M. Thorn. Original text Apache-2.0. Date: 2026-10-10.
Reservation: [#1448][claim]. Public base:
`6aae5de19bd2e04049b4d6893f18291e8465bf1a`, Canon v101.
This is an analytical pulse specification with explicit calibration gates.
No waveform was numerically searched, no apparatus was operated, and no
seven-ion implementation or measured error is claimed.

## 1. Fixed carrier, edge and optical resources

Keep the physical order `s:1, x:2, u:3, y:4, w:5, q:6, r:7` and directly
encode centered labels. Test the adjacent pair `(4,5)=(y,w)`; this edge accounts
for 16 of the previous compiler's 56 G gates. Ions `1,2,3,6,7` are spectators.
The desired endpoint, after declared local corrections, is

```text
G_45(theta) tensor I_(1,2,3,6,7),   theta=+4pi/5 or -4pi/5,
G(theta)|jk> = exp(i theta*[j!=k]) |jk>.
```

Use the [Hrmo 2023][hrmo] Fig. 1 encoding:

| Label | Ca40+ level |
|---|---|
| 0 | S_(1/2), m=-1/2 |
| 1,2,3,4 | D_(5/2), m=-3/2,-1/2,-5/2,+1/2, respectively |
| a, temporary shelf | D_(5/2), m=+3/2 |

The published two-ion apparatus uses crossed broad 401.2 nm beams for a
light-shift (LS) force, and 729 nm carrier rotations; its approximate 35 us
number is one LS loop. Eqs. (1)-(3) use a single-mode effective force and
neglect differences among the small D-state shifts. These observations do
not certify five hidden D levels or seven-ion mode closure.

Our primary route keeps a static seven-ion chain, illuminates it broadly
with LS light, and shelves all five spectators. Every 729 nm operation is
individually addressed. The S(-1/2)-D(+3/2) shelf transition is demonstrated
in [Hilder 2022][hilder], published Appendix A2, p. 10; its use there includes
optical pumping, which is **not** part of our coherent shelving interval.
The six-level S-plus-five-D control space and phase-stable shelf laser are
additional resources. Neither unused population nor perfect spectral
resolution is assumed without calibration.
For the separate eight-S/D-basis readout calibration, a resolved 729 nm path
`0 -> a -> S(+1/2) -> D(+5/2)` uses allowed absolute magnetic-number changes
2,1,2; stop after the second transfer to prepare the other S state.
These extra calibration transitions, their phase/polarization control and
trial budget are prerequisites, not main-panel pulses; a direct
`0 -> D(+5/2)` change of three is not the proposed preparation.

## 2. Explicit preparations and true inverse shelving

Fix the rotation convention on one ion:

```text
R_0j(beta,phi)=exp[-i beta(cos(phi)X_0j+sin(phi)Y_0j)/2],
X_0j=|0><j|+|j><0|,  Y_0j=-i|0><j|+i|j><0|,
R_0j(pi,phi)|0>=-i exp(i phi)|j>,
R_0j(pi,phi)|j>=-i exp(-i phi)|0>.
```

These are rotating-frame phases relative to a declared common reference.
All other levels are fixed by the ideal rotation, not by the uncalibrated
physical laser. Calibrate carrier frequency, pulse area, phase, leakage and
off-resonant effects separately for each ion and each used transition.

For a fresh test shot, cool before preparing the data, optically pump each
ion to |0>, and verify/calibrate this preparation. For a known target
`|chi>=sum_j exp(i chi_j)|j>/sqrt(5)`, with chi_0=0, apply chronologically

```text
j = 4,3,2,1:
  R_0j(2 asin(1/sqrt(j+1)), pi/2+chi_j).
```

At each step the remaining |0> amplitude is positive; the deposited j
amplitude is exp(i chi_j)/sqrt(5). Thus this is an exact four-pulse ideal
preparation, not an appeal to an unspecified Fourier implementation.
The common spectator challenge is `|F q_i>`, where

```text
(i,q_i) = (1,0),(2,1),(3,2),(6,3),(7,4),
|F q_i> = sum_(j=0)^4 exp(2pi i q_i j/5)|j>/sqrt(5).
```

All five amplitudes are nonzero on every spectator; four spectators have
nontrivial relative phases. The source ion 1 is |F0>=|+> in this fixed test.
The same formula permits a separately preregistered source-phase challenge,
for example q_1=1, without changing pulse counts. Do not silently substitute
that extra challenge for the fixed measurement ensemble.
Prepare the active pair according to the declared measurement setting;
|+>|+> uses the same four pulses per ion with chi_j=0.

Hide each spectator with `V=R_0a(pi,pi/2)`. On the code,

```text
V|0>=|a>,  V|j>=|j> for j=1,...,4.
```

Its actual adjoint is `V^dagger=R_0a(pi,-pi/2)` (equivalently a negative
angle at the original phase). Using the same positive pi pulse twice would
give a minus sign on the transferred amplitude and is not this inverse.
Apply no repumping, fluorescence, quenching or recooling during the coherent
interval. For an unknown source/spectator, omit test initialization and
preserve its input through this same isometry and its inverse; preparation
of a known test state is not permission to reset an unknown input.

## 3. The chronological G pulse word, including its phases

For either separately calibrated sign setting sigma, execute:

1. Hide ions 1,2,3,6,7; turn off all resonant carrier drives.
2. Apply one complete, all-mode-closed LS waveform `L_sigma`.
3. With LS light off, apply the following X5 to ion 4 and ion 5:

```text
chronological transition j:   1       2        3       4
pi-pulse phase phi_j:         pi/2   -pi/2     pi/2   -pi/2
```

4. Repeat steps 2-3 five times in total, including the fifth X5.
5. Unhide each spectator with its calibrated V^dagger, then apply the
   declared local phase corrections before the output boundary or analysis.

Freeze two control arms with the same preparation, hiding and terminal
analysis: E blanks each LS waveform while retaining every addressed echo;
I replaces both LS and echo stages by waits. Match total protected duration
by declared waits, including any arm-specific physical phase corrections.
Calibrate and freeze those corrections before validation; the sham's actual
errors are measured rather than assumed absent.

The four-pulse word maps `0->1->2->3->4->0` with coefficient **+1 on each
column**: input 1 and input 3 each accumulate two minus signs, and the
remaining inputs acquire none. Consequently X5^5=I with no hidden relative
phase. The two ions may receive the corresponding pulse simultaneously only
if their addressed amplitudes, frequencies and optical phases are controlled
independently. Serial addressed pulses are the default safe schedule.

A global 729 nm X5 is invalid here: it would drive spectator amplitudes
already occupying D_1,...,D_4 back into S. Hiding |0> does not make those
four amplitudes dark to common carrier pulses. Avoid unintended excitation
of the shelf transition as well. The published echo convention need not be
copied literally: our phase-exact word fixes the permutation required by
this specific endpoint and must itself be experimentally calibrated.

Known one-ion Zeeman/storage/light-shift phases, including source phases,
are generally nonzero. Record a five-entry phase frame for each ion. A
calibrated physical diagonal correction restores the specified state and is
the default for the primary protected-endpoint claim. An analysis-frame
update alone supports only a separately labeled corrected-frame claim, not
physical restoration at the output boundary. State which was used and count
physical corrections in the protected block. Neither procedure removes drift, leakage or
phases conditioned on another ion. A common scalar phase is immaterial to
this unconditional gate channel but must be retained if a later experiment
coherently controls whether the entire pulse program is applied.

## 4. A finite calibration specification for both signs and all modes

Characterize the seven axial normal modes, their participation and optical
force phases, and any appreciably coupled radial modes. Measure the 401 nm
force profile on S and **all five hidden D levels**, not just its average.
The adjacent pair need not have a useful traveling-wave phase merely because
it is adjacent. Fix its positions/geometry and verify a nonzero interaction.
The published two-ion spacing calibration is a starting technique, not a
seven-ion waveform or an entitlement to reuse its trap frequencies.

Within a frozen Lamb-Dicke, rotating-wave, harmonic model, a concrete finite
waveform ansatz is K piecewise-constant complex force amplitudes u_k on a
declared partition `0=t_0<...<t_K=T`, with `K>=2M+1` for M included modes.
Suppose the profile factors as

```text
F_m(t;ell)=u_k exp(i delta_m t) sum_i c_(im,ell_i),   t in interval k,
A_mk=integral_(t_(k-1))^(t_k) exp(i delta_m t) dt,
alpha_m(ell)=-i sum_i c_(im,ell_i) (A u)_m.
```

The c coefficients include mode participation and the state-dependent
spatial force; ell labels the active and hidden states during that loop.
Thus `A u=0` closes every branch in this **fixed-profile** model. This is a
linear finite calibration constraint, not a computed waveform. Nonzero
nullspace dimension alone says nothing about available power, bandwidth,
robustness or achievable entangling phase. Switching transients, drifting
profiles, nonlinear response, additional modes and simultaneous noncommuting
drives require an enlarged model and actual pulse measurements.

On closed loops the geometric phase is a real quadratic form in u, with
state-dependent coefficients. Five identical loops plus the declared X5
cycles must produce the normalized equality-phase target and spectator
identity, up to calibrated local phases. Solve/measure that phase condition
in addition to closure. Uniformly scaling a feasible force envelope scales
its geometric phase quadratically and preserves ideal closure; the optical
power-to-force conversion must be measured, not guessed.

For sigma=+ and sigma=-, independently preregister and validate a waveform
with theta_sigma=+4pi/5 and -4pi/5 modulo 2pi. Reversing the orientation of a
single isolated phase-space loop by changing detuning sign can reverse its
geometric phase. In seven modes, changing detuning changes all closure
conditions: recalibrate the entire waveform and its force geometry. The
substitution `u->-u` alone does **not** reverse a quadratic geometric phase.
Alternatively, reaching the same normalized -4pi/5 phase by a calibrated
positive 6pi/5 phase is allowed, with its actual longer/power cost recorded.
Feasible solutions for both signs, with compatible spectator phases, are
an entry condition; this note proves no hardware existence theorem.

Even exact loop closure does not establish spectator isolation. Require the
final diagonal phase to factor into the prescribed pair phase and one-ion
phases. Nonzero mixed phase differences between pair and spectator labels,
or between two spectators, violate this requirement. Scalar force on each
hidden five-D space is sufficient to prevent label imprint through that
force; Hrmo's small-D-shift approximation does not establish this condition.
Use the coherent tests and residual-motion checks of the experiment contract
to diagnose their effects on tested inputs; these finite tests do not
establish full branch-independent factorization. A 35 us COM loop alone
cannot pass this gate.

## 5. Counts, timing record and endpoint checks

One sign's contact block has five LS waveforms, 40 one-ion echo pi pulses,
and 10 one-ion shelf/unshelf pi pulses. Thus it has 50 ideal carrier pulses,
or 30 temporal carrier slots if only the matching pair echoes run in
parallel. Composite transfers, phase corrections and dead time add to these
counts. The seven equal-amplitude preparations add 28 pulses; other input
settings use their own frozen words. Analysis and readout are additional.

For maximum computational pi time t_pi and shelf time t_a, a conditional
contact-block budget is

```text
T_block <= 5 T_LS + 40 t_pi + 10 t_a + T_corrections + T_overhead  (serial),
T_block <= 5 T_LS + 20 t_pi + 10 t_a + T_corrections + T_overhead  (paired).
```

If, illustratively, each calibrated loop were 35 us and both pi-time bounds
10 us, these terms give 675 us serial or 475 us paired before corrections
and overhead, plus at most 280 us for the seven displayed preparations.
These are assumed scales, not a seven-ion gate-time claim. The actual
register includes cooling, initialization, input preparation, each shelf
storage interval, switching, analysis and fluorescence time, and uncertainty.
Register both sign-specific pulse files, calibrated intensities, frequencies,
phases, envelopes, durations and local corrections **before** validation.

The all-superposition test has the exact ideal endpoint

```text
|Psi_theta>_(4,5) tensor product_(i=1,2,3,6,7)|F q_i>,
|Psi_theta> = (1/5) sum_(j,k=0)^4 exp(i theta*[j!=k])|jk>.
```

Returning every spectator through its own inverse preparation should give
|0> ideally; it does not certify arbitrary input or reference preservation
by itself. A pair population table also cannot determine theta or its sign.
Use the preregistered coherent measurements, sham-echo and matched-idle arms
in the [experiment contract](README.md), with their stated confidence and
claim limits. Gate followed by its inverse alone can conceal a common
miscalibration and is not the sole acceptance test.

Individually addressed 401 nm force could avoid shelving, but is a different
isolation implementation. The [2026 DPG abstract][dpg] describes development
of that capability, without the required seven-ion performance certificate.
It must have its own pulse files and validation; do not combine its prospective
benefits with the measured outcome of the broad-force shelving experiment.

[claim]: https://github.com/mathorn1973/twist-j/issues/1448
[hrmo]: https://www.nature.com/articles/s41467-023-37375-2
[hilder]: https://journals.aps.org/prx/pdf/10.1103/PhysRevX.12.011032
[dpg]: https://www.dpg-verhandlungen.de/year/2026/conference/mainz/part/q/session/67/contribution/9
