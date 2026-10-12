# DP5/N384 and RK4/N512 on matching local windows

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering comparison.
Probe: `P-U-CA40-DP5-384-COMPARISON-1`.
Reservation: [#1468](https://github.com/mathorn1973/twist-j/issues/1468).
Authority baseline: `99094c18e668213a44532b7fb6053ca434293e9d`.
Prepared 2026-10-12. The preceding DP5/N256 results were visible when this
follow-up was designed. This is a new frozen comparison, not a reinterpretation
or retry of that probe's failed bound screen.
This derivation neither reports a numerical result nor promotes a Canon claim.
It specifies theoretical and numerical work only; no ion experiment is involved.

## 1. The unchanged target and the two candidate arms

The frozen full seven-mode sine Hamiltonian and the analytic linear moving
frame define the same self-adjoint residual generator `R_z(t)` in every arm:

\[
 i\dot W_z(t)=R_z(t)W_z(t).
\]

The candidate state is stored in the total-excitation space `P_L`, with `L=8`;
the residual is enclosed using guard space `P_G`, with `G=10`, and an analytic
bound outside that guard. The initial thermal index set remains `|n|<=3`,
containing 120 columns. No normalized replacement of a stored endpoint is made.

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
This probe independently implements those mathematical coefficients; it does
not copy their Fortran solver, adaptive controller, or dense-output code.
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
Only the numerical state is reinitialized at the beginning of a test window.

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

## 5. Why the full-space residual proof is unchanged

For any piecewise differentiable finite-support curve `p(t)`, unitarity gives

\[
 \|p(b)-U(b,a)p(a)\|
 \le \int_a^b\|i\dot p(t)-R_z(t)p(t)\|\,dt
\]

with any inter-piece and final endpoint jumps added by the triangle inequality.
This statement does not require `p` to be generated by RK4, DP5, or any solver.
It also does not require the numerical candidate to be normalized.

Arm C retains six dyadic coefficient vectors and degree five. Therefore the
same directed polynomial evaluation, coefficient norms, displacement guard,
analytic omitted tail, ball roundoff allowances, and analytic continuum
enclosure apply. In particular the Bernstein-ellipse bound still uses

\[
 M\ge h^{-1}\sum_{j=1}^5 j\|p_j\|r^{j-1}
       +\|R_z\|_{E_\rho}\sum_{j=0}^5\|p_j\|r^j,
 \qquad r=1/2+(\rho+\rho^{-1})/4.
\]

The 16-node interpolation allowance remains `4 M rho^(-15)/(rho-1)` in
the cell's normalized integral bound. Actual coefficients and all resulting
numeric bounds are recomputed; old numerical values are not inherited.
The real integration cell never straddles an amplitude switch. Analytic
continuation for its ellipse uses that cell's constant-segment formula.

The certificate remains conditional on its existing directed-arithmetic,
model-enclosure and execution contracts. Checking rational RK identities
does not validate compiler behavior, MPFR intervals, AVX rounding, underflow,
or a particular numerical trajectory. Those remain runtime/static obligations.

## 6. Exact geometry of the nonnested grids

One original constant-amplitude segment lasts `Delta=1/160000` seconds.
For each active label pair `(4,3)`, `(4,4)`, `(1,1)`, define the ordered
occupied segment list by

\[
 S_z=\{s\in\{0,\ldots,79\}:\exists j\in\{4,5\},\ (z_j+\lfloor s/16\rfloor)\bmod5=0\}.
\]

Its size is 32 for `(4,3)` and 16 for either equal-label pair. Select occupied
ordinals `0`, `floor((size-1)/3)`, `floor(2(size-1)/3)`, and `size-1`.
For the selected absolute segment `s`, the four starting subcell indices are

\[
 q_A=(0,256,256,508),\qquad q_C=(0,192,192,381).
\]

For every window, `q_A/512=q_C/384`. Arm A uses four cells and C uses three:

\[
 a=\Delta(s+q_A/512)=\Delta(s+q_C/384),\qquad
 b-a=4\Delta/512=3\Delta/384=1/20480000\ \mathrm{s}.
\]

Thus both target the same 48.828125 ns interval, entirely inside its original
segment. Their certificate-cell boundary sets intersect only at `a,b`:
in normalized window coordinates they are `{0,1/4,1/2,3/4,1}` and
`{0,1/3,2/3,1}`. Neither grid is a subset of the other. C's six *halfstep*
boundaries also meet A at the window midpoint; this does not make the
certificate-cell grids nested.

Within C cell `j=0,1,2`, halfstep `r=0,1`, tableau node `c_i`, the exact clock is

\[
 t_{j,r,i}=\Delta\left(s+\frac{q_C+j}{384}+\frac{r+c_i}{768}\right).
\]

All 24 windows retain the absolute clock and analytic linear history. Reusing
the old N256 halfstep denominator or starting a new clock at zero is invalid.
The two-grid comparator compares only matching window endpoints; it does not
pair interior cells, interpolate between grids, or fit any global phase.
Per window A uses 4 RK4 substeps and 36 RHS evaluations; C uses 6 DP5 halfsteps
and 39 RHS evaluations. These counts alone predict neither timing nor bounds.

## 7. The local comparison and its decision boundary

Both arms use the same four physical windows, six active cases, and
120 initial basis columns: 24 groups and 2,880 local targets. Each target is
`U_z(b,a)|n>` in the moving frame, with the original full linear history.
This state generally differs from the state reached by nonlinear evolution
from the beginning of the complete pulse. The windows cannot be chained by
adding their errors or interpreted as physical resets.

For two arms `X,Y` and one common target `psi`, valid individual radii imply

\[
 \|\widehat\psi_X-\widehat\psi_Y\|\le\epsilon_X+\epsilon_Y.
\]

Given a directed distance interval `[d_lo,d_hi]` and an upward radius sum `R`,
`d_lo>R` is `INCONSISTENT`; `d_hi<=R` is `COMPATIBLE`; otherwise the result is
`UNRESOLVED`. A large upper endpoint alone does not prove a contradiction.
The A/C pairs are checked after children 2 and 4, oriented as runs `1/2` and
`4/3`, so A is always the reference and C the candidate.

The separate engineering screen requires `epsilon_C<=epsilon_A` in every
column, using exact rational comparisons of the stored binary64 upper bounds.
This compares upper bounds, not actual errors. No tolerance or exemption is
added for small positive differences. The independent speed criterion requires
the exact sum of the two observed C end-to-end times to be strictly smaller
than the corresponding A sum, equivalently their two-observation medians.
Four children run in fixed order `A C C A`, with two observations per arm.
Each child is limited to 300 seconds, each comparator to 90 seconds, and the
whole campaign to 1200 seconds including setup, validation and comparison.
The remaining total time further limits each launch. There are no retries.
Neither screen is established by the present derivation or exact verifier.
No result here is a full-trajectory, final pair-coherence, physical-contact,
or hardware-feasibility certificate.

## 8. Exposed negative cases and source scope

The prior DP5/N256 campaign failed its bound nonincrease rule on column 36
of window 0, cases 0 and 3, the two signs of `(4,3)`. These results motivated
this follow-up and are not evidence for its outcome. The complete unchanged
120-column panel remains the acceptance set, including those two columns.

The basis is ordered first by total occupation and then lexicographically by
the seven mode occupations in ascending order. Grades 0,1,2 contain `1+7+28=36`
vectors, so zero-based index 36 is the first grade-three vector
`(0,0,0,0,0,0,3)`. Its unnormalized thermal weight is `20^7/21^10`.
The window/case/column flat indices are 36 and 396. The exact verifier checks
these identities, an off-by-one mutant, reversed modes, and improper omission
by a grade-two cutoff. It does not prove the compiled basis implementation.

All source-protection statements retain the unchanged conditional dark-source
model. No new source control, phase convention, physical reset, or source
restoration operation is introduced. Protected-source factorization in that
model does not imply preservation of every source state by an informative
controlled contact. The previous full-source obstruction remains unchanged.
