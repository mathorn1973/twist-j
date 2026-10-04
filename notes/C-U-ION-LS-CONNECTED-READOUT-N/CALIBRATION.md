# Independent calibration and a conditional measurement contract

**NON-CANONICAL; prospective apparatus specification, not an executed
protocol or public preregistration.** The readout response is defined in
[README.md](README.md). Numerical calibration, a state-resolved detector,
actual continuation after n=1 and the complete preparation/resource account
have not been provided. No field below is to be fitted from Hodge residuals.

## 1. What is measured and what is derived

The existing ideal model supplies coherent LS loops and star carriers.
A diagonal loop acting on one basis configuration produces a phase; that
alone is not a detector record or a measurement of AA^dagger.

The six target response observables are the commuting diagonal operators

$$
Z_k=(D_{M1}-d_0I)(D_{R1,k}-d_0I)/B.
$$

One explicit conditional measurement of them is the joint level POVM on
M1 and the six R1 ions,

$$
P_{m,x_1,\ldots,x_6}=|m,x_1,\ldots,x_6\rangle
\langle m,x_1,\ldots,x_6|\otimes I_{\rm remaining},
$$

followed by the fixed response assignment
z_k=(d_m-d_0)(d_(x_k)-d_0)/B. For a general state use the mean of the
*joint-shot product*, not the product of separately averaged populations.
On the declared basis checkpoints the ideal value is deterministic.

This specifies a measurement mathematically. Ideal joint level detection
of these seven addressed ions in the seventeen-ion apparatus is an additional
physical obligation, not an
inherited theorem of #1371. The protocol does not assume nondemolition
readout: different horizon endpoints require separate complete preparations
unless a nondemolition instrument has independently been demonstrated.

## 2. Profile and geometry calibration before native comparisons

Keep the physical level dictionary and the zero reference from #1371.
Determine d_j-d_0 from independently prepared reference transitions under
the same optical configuration. Determine c_i, g_k, eta, delta and the
usable intensity independently, or calibrate the connected response
coefficient directly by the phase protocol below. Record uncertainties,
drift bounds, correlations, Rabi rates and detector response. The common
normalization B is derived from those data, not estimated from a Hodge fit.

Use real calibration values with their uncertainties. Do not replace them
by nearby elements of Q(sqrt5) to manufacture exact equalities. The exact
symbolic proof and a finite-error device test are different contracts.

If the uncertainties prove (d1-d0)(d2-d0)(d1-d2)!=0, README's obstruction
already closes the entire exact affine-reading class for that profile.
An interval containing zero is not evidence of exact degeneracy or a
Hodge-resonant ratio. The analytical obstruction provides no numerical
lower bound for approximate residuals near the exceptional set.

## 3. Independent Ramsey check of the interaction response

For one edge k, independently prepare every spectator in a fixed reference
state and use calibration copies with partner k in x or 0. These reference
configurations need not belong to the native reachable family and must not
be counted as native continuation tests.

For m!=0, use the source carrier convention on the M1 star pair {0,m}:

$$
P=R(\pi/2,\pi/2),\qquad
A_\alpha=R(\pi/2,\alpha-\pi/2),\qquad
V_\alpha=A_\alpha U_{\rm loop}P,\quad
\alpha\in\{0,\pi/2\}.
$$

Apply the same raw-loop intensity in both partner settings. If the
additional population effect Pi_0 is admitted, the actual measurement
effect is F_alpha=V_alpha^dagger Pi_0 V_alpha. On the calibration input
|0,x_rest>, direct two-level multiplication gives

$$
p_0(\alpha)=\frac{1+\cos(\Delta-\alpha)}2,\qquad
\Delta=\Theta(0,x_{\rm rest})-\Theta(m,x_{\rm rest}).
$$

These two fixed quadratures determine the relative-phase phasor. The
carrier phase origin and detector response require a separate equal-duration
LS-off reference in the same phase-tracked frame, retaining or explicitly
compensating the known laboratory free phase. F_alpha is generally a joint
effect depending on all illuminated
ions; it is not a projective measurement of AA^dagger.

Let the measured relative phase for partner x correspond to
-[Theta(m,x)-Theta(0,x)]. Its difference from the partner-0 reference is

$$
-[\Theta(m,x)-\Theta(0,x)-\Theta(m,0)+\Theta(0,0)]
=-2\kappa\lambda^2g_k(d_m-d_0)(d_x-d_0).
$$

Thus self terms, stationary local residuals and fixed spectator terms cancel
in the comparison. The ideal phasor ratio is sufficient: at the inherited
lambda_k the connected phase lies in [-pi/50,pi/50]. Phase noise must be
bounded before interpreting the measured principal argument. For m=0 or
x=0 the connected contrast is zero by its definition, not a fitted offset.

This is a proposed calibration using the same coherent interaction. It
does not isolate one physical edge inside a raw loop, certify a detector,
or measure a native archive without disturbing it. Reference preparation,
readout light, analysis pulses, shot count, heating, cooling and re-preparation
have their own time, energy and error costs. M2 and N are occupied resources;
neither may be silently substituted as a free measurement ancilla.

## 4. What must be fixed before any successor test

The following are required inputs for a future experimental or numerical
device claim, not completed fields of this analytical note:

| Field | Required independent choice |
| --- | --- |
| Source and continuation | Complete preparation and the actual F through the stated horizon; same original U and counter dictionary |
| Physical calibration | d, geometry or measured edge coefficients, intensities, phases and uncertainties from reference calibration |
| Measurement | Level POVM/instrument implementation, analysis settings, record definition, SPAM model and remainder treatment |
| Response class | Exactly which raw observables, fixed local frames, subtractions and normalization are allowed |
| Decoder | A complete target-independent rule converting responses to the claimed coordinates, including units and amplitude |
| Comparison | Exact identities or explicit tolerance/statistical decision; declared nonzero axial signal criterion |
| New predictions | Preparations or later boundaries not used to choose the decoder, with independently justified reachable-domain coverage |
| Resources | Preparation copies, detectors, laser pulses, waiting, work, measurement/reset disturbance and error accumulation |

The present source fixes the six Z_k and their normalization, but not a
privileged four-dimensional decoder. A more flexible decoder must not be
chosen by solving the already known Hodge trajectory table. With an active
predictive register, the update and any new resources need their own
independent mechanism; the old retained archive remains separately counted.

For the natural collision comparison, exchanging M1 levels 3 and 4 at fixed
t and n in {1,2,3} stays in the displayed internal family. A causal physical
intervention also needs matched or demonstrably irrelevant inherited
remainder states. Arbitrary memory resets or relabelings need not remain in
that family.

No execution command or success record is supplied: this document specifies
what would have to be calibrated, and the analytical proof already excludes
the affine response class under its stated condition. A future formal
computation must have its own public pin before execution.
