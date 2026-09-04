# Matched hard-edge ceiling: a uniform isolated-quartet bound

NON-CANONICAL. Proof-first proposal for independent review. No scientific
computation, verifier import, numerical scan, or formal gate execution was
performed in preparing this note. No public status is changed.

Date: 2026-09-05. Public basis: Public Canon v76 on main
`1a58703ec17a4c031bb8c450f56162f5aa3e5e5a`. Independent static review checked
the exact sign reduction, uniform inequalities, first-failure definition
and grid bounds. No mathematical blocker remains in this candidate;
this is not a formal probe result or a Canon promotion.

## Source and scope

The model is the matched affine member in
[HE2 preregistration](incubation-import-2026-08-21/C-RH-HANKEL-HARD-EDGE/PREREG-P-RH-HANKEL-HARD-EDGE-2.md)
and its `V_value` in
[the sealed HE2 verifier](incubation-import-2026-08-21/C-RH-HANKEL-HARD-EDGE/verify_rh_hankel_hard_edge_2.py).
The historical
[HE2 result](incubation-import-2026-08-21/C-RH-HANKEL-HARD-EDGE/RESULT-P-RH-HANKEL-HARD-EDGE-2.md)
reported a half-unit-grid detection ceiling resembling
`T^3 = 2 delta c^2`. The source verifier was read as text only.

This note concerns the signed contribution of one isolated symmetric quartet.
At each height `T`, the polynomial parameter is matched anew to
`theta = delta^2 - T^2`. A statement about this matched family is not a
statement about one fixed polynomial detecting every height.

The theorem below starts its first-failure search at `T = delta`. It does not
start at `T = 0`. That distinction is essential: at `T = 0` the same matched
model has a real nonzero affine factor and a positive value whenever
`c^2 > 2 delta^2`. Thus the historical informal ceiling law cannot be a
global detection equivalence for every positive `T`.

## Definitions

Let `d` be a nonnegative integer, and set

\[
c=\frac{33}{4}d+21,\qquad 0<\delta\le\frac12,\qquad
\alpha=\delta+iT,\qquad \theta=\delta^2-T^2.
\]

Define

\[
q=\frac{c^2}{c^2-\alpha^2},\qquad
P_{d,c,\theta}(z)=z^d\left(z-1-\frac{\theta}{c^2}\right),
\]

\[
V_{d,\delta}(T)
=2\operatorname{Re}\left[q(2-q)P_{d,c,\theta}(q)^2\right].
\tag{1}
\]

The square in (1) is the analytic square, not an absolute square. This is
exactly the HE2 isolated-quartet sign instrument. Positive multiplicity or a
positive overall normalization would not change the sign.

Write

\[
T_0=(2\delta c^2)^{1/3},\qquad
\rho=c^{-1/3},\qquad
T_-=T_0(1-\rho),\qquad T_+=T_0(1+\rho).
\tag{2}
\]

## Proposed theorem

For every parameter choice above with `c >= 64`, equivalently for every
integer `d >= 6` on this scale, the following statements hold:

1. `T_- > delta`, and
   \[
   V_{d,\delta}(T)<0\quad\text{for }\delta\le T\le T_-.
   \tag{3}
   \]
2. There is a positive interval beyond the proposed ceiling:
   \[
   V_{d,\delta}(T)>0\quad\text{for }T_+\le T\le 2T_0.
   \tag{4}
   \]
3. The first continuous failure starting at `delta`,
   \[
   T_*:=\inf\{T\ge\delta:V_{d,\delta}(T)\ge0\},
   \]
   exists, is a zero of `V`, and satisfies
   \[
   T_-<T_*<T_+,
   \qquad
   \left|\frac{T_*}{(2\delta c^2)^{1/3}}-1\right|<c^{-1/3}.
   \tag{5}
   \]
   In particular, the explicit cubic remainder is
   \[
   \left|\frac{T_*^3}{2\delta c^2}-1\right|
   <3c^{-1/3}+3c^{-2/3}+c^{-1}.
   \tag{6}
   \]

Consequently `T_*^3/(delta c^2) -> 2` as `d -> infinity`, uniformly for
`0 < delta <= 1/2`. This conclusion concerns the continuous first failure
of the matched isolated-quartet family. Neither uniqueness of the zero in
`(T_-,T_+)` nor absence of later sign changes is asserted.

## Exact sign reduction

Set

\[
t=\frac{T^2-\delta^2}{c^2},\qquad
v=\frac{2\delta T}{c^2},\qquad n=2d+4.
\]

For `T >= delta`, one has `t >= 0` and `v > 0`. Direct substitution gives

\[
q=\frac1{1+t-iv},\qquad
q-1+ t=\frac{t^2+iv(1-t)}{1+t-iv},
\]

and therefore the exact identity

\[
\boxed{
V_{d,\delta}(T)
=2\operatorname{Re}
\frac{(1+2t-2iv)\,[t^2+iv(1-t)]^2}
     {(1+t-iv)^n}.}
\tag{7}
\]

When `0 <= t < 1`, define

\[
R=\frac{t^2}{v(1-t)},\qquad
\Phi=n\arctan\frac{v}{1+t}
       -\arctan\frac{2v}{1+2t}.
\tag{8}
\]

Both inverse tangents in (8) are their real principal values. The first
factor and denominator in (7) have net phase `Phi`; the remaining squared
factor is `v^2(1-t)^2(R+i)^2`. Thus (7) is a strictly positive real factor
times

\[
(R^2-1)\cos\Phi-2R\sin\Phi.
\tag{9}
\]

If `0 <= Phi < pi/2`, then `R >= 0` and the negative root of (9) is
`tan(Phi)-sec(Phi) < 0`. Hence

\[
\boxed{
\operatorname{sign}V_{d,\delta}(T)
=\operatorname{sign}\bigl(R-[\sec\Phi+\tan\Phi]\bigr).}
\tag{10}
\]

Equation (10), including equality at zero, is an exact sign criterion. It
retains the phase from the high power `q^(2d)`, which a fixed-degree
expansion by itself would lose.

## Uniform phase bounds in the required window

From `c >= 64` one has `0 < rho <= 1/4`. Put `A=(2 delta)^(1/3) <= 1`;
then `T_0=A c^(2/3)`. Throughout `delta <= T <= 2T_0`,

\[
0\le t\le\frac{T^2}{c^2}\le4A^2\rho^2\le\frac14,
\qquad
0<v\le2A^4\rho^4\le2\rho^4.
\tag{11}
\]

The scale and the exponent satisfy the exact useful inequality

\[
\frac c4-n=\frac d{16}+\frac54>0.
\tag{12}
\]

Let `x=v/(1+t)`. Since `t >= 0`,

\[
\arctan\frac{2v}{1+2t}\le\arctan(2x)\le2\arctan x.
\]

The second inequality follows, for example, because the derivative of
`2 arctan x - arctan(2x)` is nonnegative for `x >= 0`, and the expression
vanishes at zero. Using `n >= 4`, (8), (11), and (12) gives

\[
0\le\Phi\le n\arctan\frac{v}{1+t}\le nv
<\frac{\rho}{2}\le\frac18.
\tag{13}
\]

For `0 <= u <= 1/4`, the elementary bounds
`sin u <= u` and `cos u >= 1-u^2/2` imply

\[
1\le\sec u+\tan u
=\frac{1+\sin u}{\cos u}
\le\frac{1+u}{1-u^2/2}\le1+2u.
\]

The last inequality is equivalent to
`u(1-u/2-u^2) >= 0`. Therefore, throughout the window (11),

\[
1\le\sec\Phi+\tan\Phi<1+\rho.
\tag{14}
\]

## Negative interval below the ceiling

First, the lower endpoint in (2) is safely above the starting height:

\[
\frac{T_-}{\delta}
=\left(\frac{2c^2}{\delta^2}\right)^{1/3}(1-\rho)
\ge\frac{2(1-\rho)}{\rho^2}\ge24>1.
\tag{15}
\]

For `T >= delta`, write `eta=delta^2/T^2`. The exact scalar in (8) is

\[
R=\frac{T^3}{2\delta c^2}
  \frac{(1-\eta)^2}{1-t}.
\tag{16}
\]

On `delta <= T <= T_-`, one has `0 <= (1-eta)^2 <= 1`,
`T^3/(2 delta c^2) <= (1-rho)^3`, and `t <= rho^2`. Consequently

\[
R\le\frac{(1-\rho)^3}{1-\rho^2}
=\frac{(1-\rho)^2}{1+\rho}<1.
\tag{17}
\]

Combining (10), (14), and (17) proves (3), including both endpoints.

## Positive interval above the ceiling

At `T=T_+`,

\[
\eta=\frac{\delta^2}{T_+^2}
\le\frac{\delta^2}{T_0^2}
=\frac{A^4\rho^4}{4}\le\frac{\rho^4}{4}.
\]

Since `t >= 0`, formula (16) yields

\[
\begin{aligned}
R(T_+)
&\ge(1+\rho)^3(1-\rho^4/2)\\
&\ge(1+3\rho)(1-\rho/2)\\
&=1+\frac52\rho-\frac32\rho^2
\ge1+2\rho.
\end{aligned}
\tag{18}
\]

Here `(1-eta)^2 >= 1-2 eta`, `rho^4 <= rho`, and `rho <= 1/4`
justify every inequality. For `T > delta` with `t < 1`, all three
nonnegative factors on the right of (16) increase with `T`. Thus `R`
increases on this interval. In particular,

\[
R(T)\ge1+2\rho>\sec\Phi+\tan\Phi
\quad\text{for }T_+\le T\le2T_0,
\]

by (14). This proves (4).

The denominator in (7) never vanishes for `T >= delta`; `V` is continuous
there. Equations (3) and (4) imply that its first nonnegative value starting
at `delta` occurs at a zero strictly between `T_-` and `T_+`. This proves
(5). Cubing the two bounds in (5) gives (6). Its remainder is independent
of `delta`, establishing the stated uniform limit.

## Relation to the historical half-unit grid

The old `T_ff` is the first nonnegative value on `T=k/2`, not the continuous
quantity `T_*`. The two must not be identified.

More generally, take a grid `T=kh`, `k=1,2,...`, with step `h > 0` such that

\[
\delta\le h\le T_-.
\tag{19}
\]

Suppose the grid is available through `2T_0`. Its first failure exists and
satisfies

\[
T_-<T_{\rm ff}
\le h\left\lceil\frac{T_+}{h}\right\rceil
<T_++h.
\tag{20}
\]

Indeed, all grid points through `T_-` lie in the negative interval. The
first grid point at or above `T_+` is less than `T_++h <= 2T_0`, because
`h <= T_-=2T_0-T_+`; that point lies in the positive interval (4).
Thus the grid version has the explicit bound

\[
1-\rho<\frac{T_{\rm ff}}{T_0}
<1+\rho+\frac h{T_0}.
\tag{21}
\]

This proof does not establish
`T_ff = h ceil(T_*/h)` or a pure `h` bound on `T_ff-T_*`: possible sign
changes within `(T_-,T_+)` have not been excluded. It instead gives the
rigorous separate enclosure (20). For any historical finite grid ending at
`50`, its available height range must also be checked before applying
(20); the asymptotic theorem does not create missing grid observations.

## What this proof does not supply

- No Fourier-sign certificate beyond the degrees and members already
  certified in HE2. The present argument concerns `V` only.
- No positive or negative conclusion for the complete zeta zero sum. A
  negative isolated-quartet value is not a negative full quadratic form.
- No estimate controlling the positive critical background, competition
  among several off-critical quartets, or the archimedean and prime terms.
- No majorant uniform in the polynomial family and no exchange of a limit
  with an infinite zero sum. Those remain separate analytic obligations.
- No uniform-in-height detector built from one fixed matched polynomial.
- No new RH, J7 SOURCE, Canon, registry, or frontier status.

The independent review target is the chain (7)--(18): an exact algebraic
sign reduction followed by uniform elementary inequalities. If accepted,
it supplies a theorem for the isolated model's exponent and constant,
with the explicit remainder (6). It leaves the background and infinite-sum
questions in their original scope.
