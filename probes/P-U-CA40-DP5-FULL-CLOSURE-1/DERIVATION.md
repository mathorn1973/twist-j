# DP5/N384 full-word numerical error closure

PUBLIC NON-CANONICAL. Conditional L1 numerical enclosures.
Original work Apache-2.0, A. M. Thorn, 2026-10-12.
Probe: `P-U-CA40-DP5-FULL-CLOSURE-1`.
Reservation: [#1472](https://github.com/mathorn1973/twist-j/issues/1472).
Authority baseline: `5f54015ed8361e3a64cb10894397020ddfadd104`.

The preceding local-window and continuous-prefix results were exposed before
this design. This document adapts the DP5 and cumulative-defect derivation of
`P-U-CA40-DP5-CONTINUOUS-PREFIX-1` and the restored-coherence/thermal budget of
`P-U-CA40-BALL-CLOSURE-1`. It is not a blinded numerical replication or a new
integration theorem. No result, physical ion experiment or Canon promotion
is claimed before the frozen full-word calculation.

## 1. The unchanged model and single candidate method

In the declared oscillator interaction and electronic toggling frames,

\[
 H_{S,z}/\hbar=2u\sum_i s_i[\sin(\chi_i+X_i)-\sin\chi_i],\qquad
 H_{L,z}/\hbar=2u\sum_i s_i\cos\chi_i X_i.
\]

The same seven-mode full two-frequency linear reference is retained, with
`U_L,z=exp(i Phi_z)D(alpha_z)`. Write `U_S,z=U_L,z W_z`; the self-adjoint
moving-frame residual is

\[
 i\dot W_z=R_z W_z,\qquad W_z(0)=I,
\]

\[
 R_z=2u\sum_i s_i\{\sin(\chi_i+m_i+X_i)-\sin\chi_i
                   -\cos\chi_i(m_i+X_i)\},
 \qquad m_i=2\sum_m\kappa_{mi}\operatorname{Re}(\alpha_m e^{-i\omega_m t}).
\]

The exact decimal input, coherent force coefficients, absolute clock, five
100-microsecond loops and ideal electronic cycle are unchanged. This is the
compensated sine parent compared with its full-linear prediction, not a
new laboratory target or a reoptimized pulse. The six cases are `(4,3)`,
`(4,4)`, `(1,1)` for the positive angle, then the same three for the negative
angle. The comparison endpoint is the common physical time `T=500 us`.

Propagate in total-excitation space `P_L`, L=8. Enclose the full residual
using guard `P_G`, G=10, plus its analytic outside-guard tail. There are 120
initial columns with total occupation at most K=3. Each trajectory starts
once at `|n>` and carries its stored endpoint and cumulative certificate
through the complete word. No normalization or checkpoint reset is admitted.

Use 384 certificate cells per original constant-amplitude segment, two
successive DP5 halfsteps per cell, and one three-point quintic Hermite curve.
Thus there are 768 candidate halfsteps per occupied segment, not 384.
The same sixteen-node residual enclosure is evaluated for every cell.
There is no embedded acceptance controller, rejected step, adaptive
refinement, fallback method or second RK4 timing arm in this campaign.
All finite stored coefficients define exact dyadic polynomial coefficients
for the certifier; accurate coefficient construction is not assumed.

## 2. DP5 coefficient authority and exact order audit

The mathematical DP5 coefficients are those of Dormand and Prince (1980).
The primary implementation by Hairer and Wanner gives the coefficient table
in `CDOPRI`, lines 650--676 of
[dopri5.f](https://www.unige.ch/~hairer/prog/nonstiff/dopri5.f).
This probe inherits the predecessor's original C++ implementation of those
mathematical coefficients, written independently of the cited Fortran solver,
adaptive controller and dense-output code. Its step implementation and table
are unchanged; this is not an independent numerical replication.
The original method is described in
[Dormand and Prince, JCAM 6 (1980), 19--26](https://doi.org/10.1016/0771-050X(80)90013-3).

Write the explicit tableau as `(A,b,c)`, with seven stages. The adjacent
`dp5_tableau.hpp` stores each coefficient as an integer pair. The verifier
reads those actual pairs and checks them against an independent transcription.
It also checks strict lower triangularity, `c=A1`, `A[6,:]=b`, and `b[6]=0`.

For a rooted tree `t=[t_1,...,t_k]`, let

\[
 |t|=1+\sum_j|t_j|,\qquad
 \gamma(t)=|t|\prod_j\gamma(t_j),\qquad
 g_i(\bullet)=1,\quad
 g_i(t)=\prod_j\sum_\ell A_{i\ell}g_\ell(t_j).
\]

The exact order conditions are `b^T g(t)=1/gamma(t)` for every tree through
order five. There are `1,1,2,4,9` trees at orders one through five: 17 conditions.
The row-sum identity admits the autonomous augmentation `(t,y)'=(1,F(t,y))`,
so these conditions also cover a smooth nonautonomous right-hand side.
This is existing Runge--Kutta theory, not a new theorem; a primary recursive
proof and enumeration are in
[Bornemann, sections 4--5](https://arxiv.org/html/math/0211049v1).

There is an explicit order-six obstruction. On the six-vertex chain,

\[
 b^T A^5\mathbf1
 =\frac{11}{84}\frac{-5103}{18656}\frac{-212}{729}
   \frac{32}{9}\frac9{40}\frac15
 =\frac1{600}\ne\frac1{720}.
\]

Thus no sixth-order endpoint claim is made.

## 3. Two halfsteps and the midpoint reuse rule

For a certificate cell `[t_0,t_0+h]`, apply DP5 with step `h/2` twice.
Before sharing an evaluation this is the 14-stage tableau

\[
 A_* =\begin{pmatrix}A/2&0\\\mathbf1b^T/2&A/2\end{pmatrix},\quad
 b_*=(b/2,b/2),\quad c_*=(c/2,(1+c)/2).
\]

The verifier checks all 17 order conditions for this tableau as well.
The first halfstep's last stage evaluates `F(t_0+h/2,y_m)` at its actual
stored endpoint `y_m`. That same value is the second halfstep's first stage.
Sharing it requires 13 right-hand-side calls instead of 14.
The first halfstep's sixth stage has the same time but a different state;
it must not be substituted for the seventh stage.
No evaluation is reused across a physical amplitude discontinuity.

The normalized stage times are

\[
 (0,1/10,3/20,2/5,4/9,1/2,1/2),\qquad
 (1/2,3/5,13/20,9/10,17/18,1,1).
\]

Every stage lies in the current constant-amplitude segment. The analytic
linear history and the absolute clock continue to be used at each stage.
The numerical state is initialized only once. Neither its clock, state nor
cumulative certificate is reset at a checkpoint.

The two-half composition remains fifth order. For the scalar linear equation,
its stability polynomial has coefficient `161/115200` at degree six, whereas
the exact exponential has `1/720=160/115200`. This is an exact negative fixture,
not a claim about the physical generator's error constant.

## 4. A single quintic from values and derivatives

Let `theta=(t-t_0)/h`, and obtain

\[
 y_0,\ y_m,\ y_1,\qquad
 d_0=hF(t_0,y_0),\ d_m=hF(t_0+h/2,y_m),\ d_1=hF(t_0+h,y_1).
\]

All three `d` values are derivatives with respect to the full-cell coordinate
`theta`; scaling them by `h/2` would be wrong.
The six constraints `P(i)=y_i`, `P'(i)=d_i`, at `i=0,1/2,1`, determine one
polynomial of degree at most five. To see uniqueness, their difference would
have a double zero at each of three distinct points and hence either vanish
identically or have degree at least six.

Let `L_i` be the quadratic Lagrange basis for those three points. Then

\[
 H_i(\theta)=[1-2L_i'(i)(\theta-i)]L_i(\theta)^2,\qquad
 K_i(\theta)=(\theta-i)L_i(\theta)^2,
\]

and `P=sum_i(y_i H_i+d_i K_i)` satisfies the constraints directly.
For implementation using differences, set

\[
 a=y_m-y_0-d_0/2,\quad b=d_m-d_0,\quad
 c=y_1-y_0-d_0,\quad d=d_1-d_0.
\]

The coefficients in ascending powers are

\[
\begin{aligned}
 p_0&=y_0,&p_1&=d_0,\\
 p_2&=16a-8b+7c-d,&
 p_3&=-32a+32b-34c+5d,\\
 p_4&=16a-40b+52c-8d,&
 p_5&=16b-24c+4d.
\end{aligned}
\]

The constant coefficient is copied from the initial stored state. This
preserves the existing certifier's assumption `P(0)=y_0` exactly.
Coefficient rounding may prevent the other five constraints from being
exact binary64 identities; certification uses the actual stored curve and
encloses its final jump to the actual serialized endpoint.
There is no separate midpoint jump because the certified curve is one
polynomial, not a concatenation of two polynomial pieces.

The exact verifier checks all cardinal constraints and reproduction of every
monomial through degree five. Degree six is deliberately not reproduced:
for `f(theta)=theta^6`,

\[
 f(\theta)-P(\theta)=\theta^2(\theta-1/2)^2(\theta-1)^2,
 \qquad f(1/4)-P(1/4)=9/4096.
\]

For smooth exact dynamics in fixed `P_L`, fifth-order halfsteps give local
value errors `O(h^6)` and scaled derivative errors `O(h^7)`. Exact three-point
Hermite interpolation gives a curve error `O(h^6)` and derivative error
`O(h^5)`. This explains a possible improvement in the time-residual bound.
It is not a numerical guarantee, a roundoff proof, or a bound on projection
error. The interval certifier determines the actual enclosures.

The old acceleration estimator used `F(t+-delta,y+-delta f)` with `delta=h/128`.
Its derivative error is generally `O(delta^2)`. Merely replacing RK4 endpoints
while retaining that estimator would not justify a fifth-order dense-curve
claim. The inherited DP5 candidate removes this estimator completely.

## 5. Cumulative full-space error without a reset

Let `U_R(t,s)` be the exact unitary propagator of the frozen self-adjoint
moving-frame residual. The target for one retained initial column is
`psi(t)=U_R(t,0)|n>=W_z(t)|n>` in the full oscillator Hilbert space.
Finite-support polynomial curves lie in the required generator domain.
For cell `[t_{j-1},t_j]`, let `p_j(t)` be the exact polynomial defined by its
stored dyadic coefficients and let `y_j` be the stored numerical endpoint.
The incoming coefficient is an exact copy:

\[
 p_j(t_{j-1})=y_{j-1}.
\]

Define the cell defect and final jump

\[
 d_j=\int_{t_{j-1}}^{t_j}\|i\dot p_j(t)-R_z(t)p_j(t)\|\,dt,
 \qquad J_j=\|p_j(t_j)-y_j\|.
\]

Variation of constants and unitarity imply

\[
 \|y_j-U_R(t_j,t_{j-1})y_{j-1}\|\le d_j+J_j.
\]

Consequently, if `E_{j-1}` encloses the error relative to the original target,

\[
\begin{aligned}
 \|y_j-\psi(t_j)\|
 &\le \|y_j-U_R(t_j,t_{j-1})y_{j-1}\|
       +\|U_R(t_j,t_{j-1})(y_{j-1}-\psi(t_{j-1}))\|\\
 &\le d_j+J_j+E_{j-1}.
\end{aligned}
\]

Induction gives the cumulative certificate

\[
 E_j\ge E_0+\sum_{k=1}^{j}(d_k+J_k),\qquad E_0=0.
\]

This is a sum of full-space defects of the *actual carried numerical curve*.
It is not a sum of independent reset-window estimates or an extrapolation
of the previous local panel. No Gronwall factor, normalization, projected
unitarity assumption, or convergence-rate fit is required. An evolving
numerical state may have norm different from one; its actual coefficient
norms enter each newly computed bound.

The jump from the polynomial to each stored endpoint is charged once. The
next polynomial starts at that same stored endpoint, so no second copy of
that jump is due. At a checkpoint the state and certificate are copied for
output; this creates no mathematical jump. If a state were changed, rounded
to a different representation, projected again, normalized, or reinitialized,
the resulting extra jump would have to be bounded explicitly. None is admitted.

The inherited `certify` updates cumulative guard, omitted-tail, continuum,
and jump components using upward arithmetic, and recomputes their outward
sum as `total`. Preserve that `Certificate` across every cell and checkpoint.
Every component and `total` is finite, nonnegative and nondecreasing. Do not
add the already cumulative totals of consecutive checkpoints: that would
count earlier defects again. Report checkpoint totals and, if desired,
clearly labeled changes, never treat a difference of rounded upper bounds
as a separately certified block defect.

An internal arithmetic ball can begin at radius zero for an exact stored
dyadic vector or coefficient: it encloses evaluation of that numerical
object. The prior *dynamical* error is separately carried in the cumulative
certificate and is preserved by the recurrence above. Resetting internal
scratch evaluation radii is distinct from resetting the trajectory's `E_j`.

## 6. The inherited cell enclosure remains applicable

The inherited DP5 candidate supplies six dyadic coefficient vectors of degree five.
Directed polynomial evaluation, coefficient norms, displacement guard,
analytic outside-guard tail, arithmetic balls and the continuum enclosure
are recomputed from that cell's actual carried state and coefficients.
The Bernstein-ellipse estimate uses a bound on `R_z P_L`, not a boundedness
claim for the full unbounded oscillator generator:

\[
 M\ge h^{-1}\sum_{j=1}^5 j\|p_j\|r^{j-1}
       +\sup_{E_\rho}\|R_z P_L\|\sum_{j=0}^5\|p_j\|r^j,
 \qquad r=1/2+(\rho+\rho^{-1})/4.
\]

The 16-node normalized-integral allowance remains
`4 M rho^(-15)/(rho-1)`. The finite guard and analytic tail jointly enclose
the full Hilbert-space defect; keeping `L8/G10` is not a claim that no
population can leave either finite space. The real integration cell cannot
straddle an amplitude switch. The ellipse uses analytic continuation of
that cell's fixed segment formula, as before.

Sampled time-node and projection-node diagnostics are not separate
continuous-time certificates. The continuum allowance belongs to the combined
defect. Arithmetic-node diagnostics are already included in the guard bound
and must not be added to `total` again. A small norm drift is not a substitute
for the defect certificate.

These bounds remain conditional on the inherited model, domain,
directed-arithmetic and execution contracts. An exact rational support audit
alone establishes neither the compiled floating calculation nor its measured
accuracy. The cumulative proof applies through the complete piecewise-smooth word; it
does not relax any cell enclosure or runtime requirement.

## 7. Piecewise unitarity, ideal switches and inactive history

An original segment lasts `Delta=1/160000` seconds. There are 80 segments,
with sixteen per loop. For the two active labels define

\[
 s_i(\mathrm{seg})=1[(z_i+\lfloor\mathrm{seg}/16\rfloor)\bmod5=0].
\]

Every real integration cell lies inside one such segment. At a force
amplitude or indicator switch, the self-adjoint Hamiltonian can change
its one-sided value while the oscillator state remains continuous. There
is no delta-function kick in the frozen motional model. Finite-support
polynomials are in the generator domain; the bounded sine terms and linear
oscillator terms give the stated unitary piecewise propagators. Compose
these unitary propagators at segment boundaries. Values at isolated switch
points do not change the defect integral.

Apply section 5 independently to the last old-segment cell and the first
new-segment cell. Their common stored endpoint is carried unchanged;
`poly[0]` equals that endpoint, and the previous final polynomial jump was
already charged once. The new derivative uses the new segment formula.
Do not reuse a derivative across the physical switch. No additional
Gronwall or stability factor appears, and a switch is not permission to
reset the accumulated bound. The same-segment analytic continuation used
by a cell's Bernstein ellipse is not the piecewise physical Hamiltonian
outside the real cell.

The instantaneous ideal X5 operations act on electronic labels. Following
each initial label in its toggling-frame branch changes the subsequent
active indicators but does not reset, renormalize or project the bus state.
The fifth cycle is included. After all five cycles the electronic label
permutation is the identity; this does not say that the conditional bus
unitary or its accumulated error is the identity.

| Labels, for either sign | Occupied original segments | First onset | End of last occupied segment |
| --- | --- | ---: | ---: |
| (4,3) | 16 through 47 | 100 us | 300 us |
| (4,4) | 16 through 31 | 100 us | 200 us |
| (1,1) | 64 through 79 | 400 us | 500 us |

On every interval with both active indicators zero, `H_S=H_L=R_z=0` in
the declared frames. Hence the exact W-frame state and its accumulated
error account carry unchanged across that interval, even if they are
already nontrivial from an earlier force. Before the first occupied
segment this gives `U_L=I`, `W=I` and the exact initial basis vector. After
the last occupied segment it gives the same saved W-frame endpoint at
T=500 us. Skipping these identities is not a physical reset or a claim
that an untransformed laboratory oscillator does not evolve.

The coefficient preparer must advance the original absolute segment clock
and analytic linear history over all 80 segments, including inactive ones.
The compressed occupied-cell list may omit only exact-zero residual
intervals. Original segment order, all occupied cells and their complete
subcell indices must be checked. In particular, reporting a state after
the `(4,4)` force as a 200-us physical pair endpoint would be wrong when
restoration uses the common 500-us word endpoint.

For an occupied original segment s, cell j=0,...,383, half r=0,1 and
DP node c_i, the absolute stage time is

\[
 t_{s,j,r,i}=\Delta\left(s+\frac{j}{384}+\frac{r+c_i}{768}\right).
\]

All candidate and Gauss nodes use that segment's actual history and the
same fixed formula. Cell endpoints, segment transitions and inactive gaps
therefore share one declared initial-value problem from time zero to T.
There are 12288 occupied cells per `(4,3)` column and 6144 per other column.
Across both signs and all 120 columns, this is 5898240 column-cells or
737280 eight-column certificate cells. These counts are an inventory,
not a prediction of runtime or bound width.

For the uncompensated sine parent the exact scalar relation is

\[
 U_{\mathrm{raw},z}(t)=e^{i\lambda_z(t)}U_{S,z}(t),\qquad
 \lambda_z(t)=-2\int_0^t u(v)\sum_i s_i(v)\sin\chi_i(v)\,dv.
\]

A prefix scalar need not be common across branches. This calculation
retains the compensated parent; it does not silently remove relative
prefix phases or assert a physical implementation of the counterterm.
Any claimed raw-parent equivalence requires its separately established
full-word phase condition, not a change of convention after seeing data.

## 8. Common-time linear-frame restoration

Only after each branch has completed its full occupied-cell inventory,
with exact inactive continuation through T, may the preparer's `final`,
`delta`, `rotation` and full-linear overlaps be used as endpoint data.
The branch-dependent restoration cannot be dropped from a cross-branch
observable. With `D(beta)D(alpha)=exp(i Im(beta alpha*))D(beta+alpha)`,

\[
 U_{L,b}(T)^\dagger U_{L,a}(T)
   =e^{i\theta_{ab}}D(\delta_{ab}),\qquad
 \delta_{ab}=\alpha_a-\alpha_b,
\]

\[
 \theta_{ab}=\Phi_a-\Phi_b+
       \operatorname{Im}\sum_m\overline{\alpha_{b,m}}\alpha_{a,m}.
\]

For stored W-frame endpoints y and retained thermal occupations define

\[
 \widehat\Gamma_{S,\mathrm{ret}}
 =e^{i\theta_{ab}}\sum_{n\in K}p_n
      \langle y_{b,n}|D(\delta_{ab})|y_{a,n}\rangle.
\]

The full initial thermal state's exact linear prediction is

\[
 \Gamma_L=e^{i\theta_{ab}}
   \exp\!\left[-\sum_m(\bar n_m+1/2)|\delta_{ab,m}|^2\right].
\]

The one-mode normal-ordered displacement implementation evaluates
`P_L D(delta) P_L`. Its matrix element between the two stored finite-support
vectors is the full displacement matrix element, not an approximation by
`exp(i P_L X P_L)`. No extra restoration projection tail is needed for that
finite-vector matrix element. Its coefficient, Gaussian and interval
arithmetic uncertainty still has to be enclosed. The propagated-vector
errors below control replacement of the exact infinite-space vectors.

Raw overlaps `<y_b|y_a>`, independent branch phase fits or normalization
of the saved vectors would change this observable. They are not allowed.
No intermediate pair quantity is inferred from case-dependent checkpoint
times. A common physical time and its own restoration would be needed.

## 9. Unnormalized thermal, dynamical and arithmetic budget

For seven initially independent modes with nbar=1/20,

\[
 p_n=(20/21)^7(1/21)^{|n|},\quad |n|\le3,\qquad
 q=\sum_{n\in K}p_n,\quad
 p_{\mathrm{tail}}=1-q=\frac{680046581}{794280046581}.
\]

All 120 unequal weights are retained without renormalization. This initial
thermal omission is separate from the dynamical projection/guard error.
For each branch the per-column cumulative certificate e gives outward
bounds on the weighted purification error and stored-vector norm:

\[
 E_z=\left(\sum_{n\in K}p_n e_{z,n}^2\right)^{1/2},\qquad
 A_z=\left(\sum_{n\in K}p_n\|y_{z,n}\|^2\right)^{1/2}.
\]

The true W-frame vectors have norm one. Their retained purification norm
is sqrt(q), while the stored vectors need not have that norm. Adding and
subtracting one mixed exact/approximate overlap and using weighted
Cauchy--Schwarz gives

\[
 |\Gamma_{S,\mathrm{ret}}-\widehat\Gamma_{S,\mathrm{ret}}|
 \le B_{ab}:=\min\{\sqrt q E_a+A_aE_b,\ \sqrt q E_b+A_bE_a\}.
\]

For example, expand into the error of branch a paired with exact branch b
and the error of b paired with stored a. This gives the first expression;
interchanging branches gives the second. Unitary restoration preserves
these norms. Replacing B by E_a+E_b without controlling the stored norms
would be unjustified. Each E_z already includes cumulative guard, analytic
tail, continuum and jumps; sampled subdivisions are not added again.

The omitted thermal contribution to the complex sine coherence has modulus
at most p_tail by unitarity and the original positive weights. The linear
reference above is already full thermal, so there is only one such omitted
mass in this comparison, not two and not a renormalization correction.
For a normalized two-branch Bell input, the reduced electronic/reference
trace distance between the declared sine and full-linear channels is

\[
 D_{ab}=\tfrac12|\Gamma_S-\Gamma_L|.
\]

All branches here belong to the same angle and share T. There are three
within-angle pairs per sign, hence six selected witness distances.
These witnesses do not constitute an all-input channel guarantee.

Let directed restoration/evaluation produce a complex interval for
`Gamma_hat_ret-Gamma_L`, and let

\[
 [c_-,c_+]\supseteq\tfrac12
        |\widehat\Gamma_{S,\mathrm{ret}}-\Gamma_L|.
\]

This magnitude interval includes restoration and linear-reference interval
uncertainty. The reported account is

\[
 r_{\mathrm{num}}=\tfrac12 B_{ab},\qquad
 r_{\mathrm{th}}=\tfrac12p_{\mathrm{tail}},\qquad
 r_{\mathrm{arith}}\ge\tfrac12(c_+-c_-),
\]

\[
 r_{\mathrm{total}}\ge r_{\mathrm{num}}+r_{\mathrm{th}}+r_{\mathrm{arith}},
\]

\[
 D_{ab}\in
 [\max(0,c_- -r_{\mathrm{num}}-r_{\mathrm{th}}),
  \min(1,c_+ +r_{\mathrm{num}}+r_{\mathrm{th}})].
\]

All operations are outward. The total radius bounds the distance from the
exact midpoint of [c_-,c_+]; no unaccounted rounding of a displayed midpoint
is allowed. Do not add r_arith once more when expanding the already
interval-valued [c_-,c_+]. Conversely, omitting its halfwidth from the
precision test would falsely accept a wide arithmetic interval. Report
both the interval and all three radius components, including on failure.

The fixed K3 thermal radius alone is approximately 4.28e-4, leaving only
about 5.72e-4 of a 1e-3 total-radius goal for dynamical and arithmetic
contributions. This is a budget constraint, not an accuracy prediction.
A completed interval can be mathematically valid but too wide for the goal.

## 10. Decisions, checkpoints and first-outcome rules

Two logically separate questions use the exact rational threshold 1/1000:

1. **Numerical precision.** Pass only if every one of the six outward total
   pair radii is at most 1/1000. A valid wider result leaves this goal
   unresolved. Invalid arithmetic, missing endpoints, failed runtime
   invariants or broken custody give no numerical certificate.
2. **Nonlinear discrepancy.** For each pair, a distance lower endpoint
   strictly above 1/1000 certifies above-threshold deviation of the frozen
   sine prediction from the full-linear prediction. An upper endpoint at
   most 1/1000 certifies that selected witness is within the threshold;
   otherwise that comparison is unresolved. At least one certified
   above-threshold pair in each sign establishes this limited discrepancy
   statement for both angles. It is not deviation from a physical target,
   a measured apparatus error or a universal nonlinear no-go theorem.

These decisions are independent. A wide but valid interval might resolve
a discrepancy while missing the precision target; a narrow interval might
instead place the discrepancy below threshold. Compare the exact rational
values of saved dyadic endpoints with 1/1000, never a rounded decimal
threshold. No precision or discrepancy outcome follows from the earlier
short-prefix comparison or a formal DP5 order test.

Checkpoint records identify the original segment/loop, absolute physical
time, completed occupied cells, cumulative per-column components and state
continuity. Carry one state and one Certificate per case/batch throughout.
Required invariants include exact incoming poly[0], no missing/repeated
cells, finite nondecreasing cumulative components, immutable snapshots,
no state/certificate reset, and unchanged source/input/binary custody.
A checkpoint does not authorize a restart or phase correction. Intermediate
upper-bound growth is diagnostic; it is not itself physical falsification
or proof that a later final-width goal cannot succeed.

Preserve the first outcome under the fixed single-configuration 24-hour
resource contract in PREREG.md. There is no hidden pilot, replacement run,
automatic higher cutoff or smaller step, discarded warmup, repaired pin,
longer budget or post hoc relaxed threshold. If resource limits or an
integrity failure stop the calculation, preserve partial states, progress
and component records as available, without manufacturing final witnesses.
Exact support-verifier success does not replace missing numerical output.

## 11. What successful closure would and would not establish

Successful runtime enclosures give full-harmonic-Hilbert-space errors for
these propagated columns and controlled full-initial-thermal electronic
pair witnesses through the stated omitted-mass account. This does not
reconstruct the complete motional state, cover all 25 electronic labels,
certify an all-input diamond norm, or admit a physical ion implementation.
The seven harmonic modes, ideal electronic pulses, frozen geometry and
classical controls remain model assumptions; heating, scattering, radial
motion, finite-control errors and a full energy/work ledger are absent.

Protected electronic/source-reference factorization still assumes exact
zero response of the protected registers. No source operation, physical
reset or information archive is introduced. This conditional identity is
not preservation of an unknown complete source by an informative contact;
the established full-source obstruction remains unchanged. All results
remain public non-canonical conditional L1 evidence, including unsuccessful
or unresolved first outcomes.
