# DP5/N384 and RK4/N512 on one continuous short prefix

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering comparison.
Probe: `P-U-CA40-DP5-CONTINUOUS-PREFIX-1`.
Reservation: [#1470](https://github.com/mathorn1973/twist-j/issues/1470).
Authority baseline: `200ebb118bc62b02c634afa9e68bd91a7de3191b`.
Prepared 2026-10-12. The preceding N256 and N384 local-reset results were
visible when this follow-up was designed. The change is persistent state and
error accumulation across four checkpoints, not a new integration formula.
This derivation neither reports a numerical result nor promotes a Canon claim.
It specifies theoretical and numerical work only; no ion experiment is involved.

## 1. The unchanged target and the two candidate arms

The frozen full seven-mode sine Hamiltonian and the analytic linear moving
frame define the same self-adjoint residual generator `R_z(t)` in every arm:

\[
 i\dot W_z(t)=R_z(t)W_z(t),\qquad W_z(0)=I.
\]

The candidate state is stored in the total-excitation space `P_L`, with `L=8`;
the residual is enclosed using guard space `P_G`, with `G=10`, and an analytic
bound outside that guard. The initial thermal index set remains `|n|<=3`,
containing 120 columns. Each numerical trajectory begins once at the exact
unit vector `|n>` and thereafter carries its endpoint and cumulative error.
No normalized replacement or checkpoint reinitialization is made.

The arms are:

| Arm | Candidate | Certificate cells per original segment | Candidate substeps |
| --- | --- | ---: | ---: |
| A | Existing RK4 and endpoint-acceleration quintic | 512 | 512 RK4 steps |
| C | Two successive DP5 halfsteps and three-point quintic Hermite | 384 | 768 DP5 halfsteps |

The `384` label in C counts certificate cells, not DP5 substeps. Each C cell
uses one quintic curve and the same 16-node residual quadrature as an A cell.
No adaptive step choice, embedded error estimator, step rejection, or fallback
is used. All candidate coefficients are stored binary64 values; the certifier
treats each finite stored value as an exact dyadic coefficient of its curve.

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
claim. Arm C removes this estimator completely.

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

Each method still supplies six dyadic coefficient vectors of degree five.
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
accuracy. The new prefix proof changes how valid cell bounds compose; it
does not relax any cell enclosure or runtime requirement.

## 7. The inactive beginning is an exact identity in the stated frame

An original constant-amplitude segment lasts `Delta=1/160000` seconds.
For a retained branch `z`, the ideal electronic cycle makes active indicator
` s_i(seg)=1[(z_i+floor(seg/16)) mod 5=0] ` for the two active-ion labels.
The first occupied segment and its physical onset are

| Labels | First occupied segment | Onset a_z |
| --- | ---: | ---: |
| (4,3) | 16 | 100 microseconds |
| (4,4) | 16 | 100 microseconds |
| (1,1) | 64 | 400 microseconds |

The same onsets apply to both signs. On every preceding segment both
indicators vanish. In the compensated interaction/toggling-frame parent,

\[
 H_S/\hbar=2u\sum_i s_i[\sin(\chi_i+X_i)-\sin\chi_i],\qquad
 H_L/\hbar=2u\sum_i s_i\cos\chi_i X_i,
\]

so `H_S=H_L=R_z=0` there. Thus `U_L(a_z)=I`, `W_z(a_z)=I`, and the initial
moving-frame vector remains exactly `|n>`. Skipping these inactive segments
introduces zero motional defect and is not a physical state reset. Free
oscillator motion and the ideal electronic relabeling have already been
factored into the declared frames; this identity is not a claim about an
untransformed laboratory state or imperfect control operations.

At onset the stored basis vector therefore represents the true initial
condition propagated from pulse time zero. After onset the state must be
carried. Unlike a reset in a later occupied segment, no unknown prior
nonlinear evolution is discarded. The coefficient preparer must still use
the original absolute times `a_z+t`, never restart the oscillator or force
phase clock at onset.

For the *uncompensated* sine parent, removing the scalar counterterm gives

\[
 U_{\mathrm{raw},z}(t)=e^{i\lambda_z(t)}U_{S,z}(t),\qquad
 \lambda_z(t)=-2\int_0^t u(v)\sum_i s_i(v)\sin\chi_i(v)\,dv.
\]

This known branch scalar need not be a common global phase at a prefix.
The full-word endpoint cancellation does not justify dropping relative
prefix phases. This probe keeps the compensated parent and compares the
same frame in both arms. Any future raw-parent coherence calculation must
restore its scalar and the other declared frames consistently. A common
exact unitary restoration preserves the per-column error norm, but its
numerical implementation would require its own enclosure.

## 8. Four checkpoints on one uninterrupted occupied prefix

Set the fixed block duration

\[
 \delta=\Delta/128=1/20480000\ \mathrm{s}=48.828125\ \mathrm{ns}.
\]

For checkpoint `k=1,2,3,4`, both methods end at the same branch-specific time

\[
 t_{z,k}=a_z+k\delta
        =\Delta(s_z+4k/512)=\Delta(s_z+3k/384).
\]

Arm A advances a single trajectory through 16 consecutive N512 cells and
copies checkpoints after cells `4,8,12,16`. Arm C advances through 12
consecutive N384 cells and copies checkpoints after `3,6,9,12`.
The maximum occupied evolution is 195.3125 ns. All checkpoints lie inside
the first occupied 6.25-microsecond segment; the panel tests accumulation
across cells and checkpoint blocks, not crossing a later amplitude switch.

Each block's certificate grids are nonnested: after translation and scaling,
A has boundaries `{0,1/4,1/2,3/4,1}` and C has `{0,1/3,2/3,1}`.
Only the block endpoints are shared. C's halfstep boundaries additionally
meet A at the midpoint; this is not an extra common certificate-cell boundary.
For C cell `j=0,...,11`, half `r=0,1`, and DP node `c_i`, the exact clock is

\[
 t_{j,r,i}=\Delta\left(s_z+\frac{j}{384}+\frac{r+c_i}{768}\right).
\]

There are 90 persistent case/batch trajectories: six cases times fifteen
batches of eight initial columns. The four checkpoint copies yield 24
checkpoint/case groups and 2880 recorded column targets. Per trajectory,
A uses 16 RK4 steps and 144 RHS calls; C uses 24 DP5 halfsteps and 156 RHS
calls. Their certificates use 256 and 192 Gauss nodes respectively. Counts
alone do not establish speed or a smaller bound.

Checkpoints within one case are actual successive prefixes of the original
initial-value problem. Different cases have different onsets. In particular,
case `(1,1)` at approximately 400 microseconds cannot be combined with a
case `(4,3)` at approximately 100 microseconds into a common-time pair
coherence. This panel computes individual column bounds and A/C consistency,
not an all-branch channel at one simultaneous time.

The inherited preparer's fields `final`, `delta`, `rotation`, and its full
linear pair overlaps refer to the complete 500-microsecond word. They must
not be reported or used as prefix quantities. The cell generator retains
its correct prefix linear displacement; this suffices for the moving-frame
column calculation. This study introduces no final-coherence reconstruction.

## 9. Checkpoint comparison and required invariants

For each checkpoint, branch and retained initial occupation, both arms
approximate the same full-space target `W_z(t_{z,k})|n>`. Valid cumulative
radii therefore imply

\[
 \|\widehat\psi_A-\widehat\psi_C\|\le E_A+E_C.
\]

Given a directed endpoint-distance interval `[d_lo,d_hi]` and the upward sum
`R=up(E_A+E_C)`, classify `d_lo>R` as `INCONSISTENT`, `d_hi<=R` as
`COMPATIBLE`, and the remainder as `UNRESOLVED`. No normalization, fitted
phase or tolerance is added. Compatibility alone need not mean small error.

The short comparison keeps four children `A C C A`, matched pairs `1/2`
and `4/3`, 300 seconds per child, 90 seconds per comparator and 1200 seconds
total, including preparation, validation and comparisons. Each launch is
also limited by the remaining total budget. There is no retry or automatic
longer run. The separate frozen engineering screens require `E_C<=E_A` on
all 2880 checkpoints/columns in both pairs, and a strictly smaller exact sum
of the two observed C program end-to-end times than the two A times.
Neither screen follows from the derivation or the previous reset-window run.

The implementation and preserved records must establish:

- exactly one unit-vector initialization and one zero cumulative certificate
  per case/batch trajectory, before its first active cell;
- carried endpoint bytes and an exact incoming polynomial coefficient at
  every cell, including both sides of each checkpoint;
- monotone finite cumulative components, unchanged by checkpoint copying;
- no missing or repeated active cells, and exact common checkpoint times;
- independent immutable copies of all checkpoint endpoints and certificates;
- the same 120 graded basis columns, including index 36, occupation
  `(0,0,0,0,0,0,3)`, for both signs and every checkpoint;
- no use of full-word final linear metadata as prefix evidence.

Resetting the certificate while retaining a biased state loses prior error:
for identity subsequent evolution its new local defect can be zero while
the old discrepancy remains. Resetting the state while retaining the ledger
changes the initial-value problem and creates an uncharged jump. These are
separate negative controls. Adding checkpoint totals again double-counts
history; losing an endpoint jump undercounts it. Exact rational composition
fixtures can audit these supporting identities, but cannot prove that the
compiled harness obeys the state-carry contract.

## 10. Scope of a successful short prefix result

A successful runtime enclosure gives a cumulative full-Hilbert-space vector
error for each retained initial column at each stated prefix checkpoint,
conditional on the frozen model and arithmetic contracts. It does not
certify the remainder of the pulse, every intermediate serialized state,
a thermal channel on all oscillator inputs, final pair/source-reference
coherences, or a physical ion experiment. The finite thermal-column panel
is not silently promoted to an all-input diamond-norm certificate.

All source-protection statements retain the unchanged conditional dark-source
model. No source operation, physical reset or restoration is introduced.
Protected-source factorization in that model does not imply preservation
of every unknown source state by an informative controlled contact. The
previous full-source obstruction remains unchanged. The new contribution
is the bounded no-reset prefix test and its explicit cumulative accounting;
no Canon claim is promoted by this document.
