# Signed estimates and the remaining low-height sum

**NON-CANONICAL. No authority. All deductions candidate-D; the final
power estimate O.** Same candidate, owner issue [2087](https://github.com/mathorn1973/twist-j/issues/2087)
and draft [2089](https://github.com/mathorn1973/twist-j/pull/2089).
This round answers the request to attack the estimate itself. It proves
signed bounds for two actual families and a quantitative bound for the
complete remainder. The full X^(2+epsilon) estimate is not established.

## 1. What has been estimated

Use the frozen finite taper and actual coefficients of
[FINITE-TAPER](../round4/FINITE-TAPER.md). For a frequency theta=a/(5r),
define its dimensionless height h(theta)=X|a|/r, and let P_X^rem(Y)
retain the exact ordered pairs of P_X^rem whose larger height is at
least Y. All original coefficient, primitivity, strip and gcd conditions
remain in force.

**Candidate-D, unconditional.** With k=ceil(3 log_2 X),

\[
 |P_X^{\mathrm{rem}}(Y)|\ll_\varepsilon
 X^\varepsilon\left(\frac{X^3}{Y^2}+X^2\right),
 \qquad 640k\le Y\le10\sqrt X.                                  \tag{1}
\]

The estimate includes the pairs crossing the height threshold, not only
pairs with both heights above it. The proof first sums the actual
character-bearing numerators. The resulting geometric resonances are
counted as divisors of positive integers n+j or n-j, with the zero
multiple handled separately. Only afterward are conductor absolute
values used. The three height rectangles and the taper account for
all threshold-crossing pairs. [Full proof](NUMERATOR-ESTIMATE.md) and
[opposition](REVIEW-NUMERATOR.md).

For Y=X^delta, 0<delta<1/2, the absolute values of these same actual
contributions have total at least X^(3-delta-epsilon), up to a positive
constant. Their signed total is bounded by X^(3-2delta+epsilon).
For instance delta=1/4 gives the exponents 11/4 and 5/2, respectively.
This is a real power saving on that family. Neither assertion estimates
the complementary low-height sum.

A second actual signed estimate concerns the error of the original
rational triangular average, written Tcal_H. For every fixed eta>0
in the nonempty stated range, and every fixed A>0,

\[
 \sum_{X\le n<2X}|T(n)-\mathcal T_H(n)|^2
 \ll_{\eta,A}\frac{XH^2}{(\log X)^A},
 \qquad X^{1/3+\eta}\le H\le X^{1-\eta}.                         \tag{2}
\]

This transfers the published unconditional short Mobius theorem through
t=mu*v. The transfer proves the exact real-to-integer grid step and
separately bounds divisors d>H, where the rescaled interval is shorter
than one. At H=floor(sqrt X (log X)^B), fixed B>=0, the error is
O_{B,K}(X^2/(log X)^K) for every fixed K>0. With the single common cutoff
G=ceil(exp(sqrt(log X))), its signed off-diagonal low-gcd expression
also obeys that bound. For B=2 an actual coprime prime subfamily of
positive entries contributes at least a constant times X^2(log X)^2.
Their cancellation in the full signed error is therefore quantified.
[Full proof](SHORT-SUM-TRANSFER.md), [review](REVIEW-SHORT-SUM.md).

Equation (2) bounds the smoothing **error**. It supplies no estimate
of the energy of Tcal_H itself. At H=X^(1/2+delta) for fixed delta>0,
its proved right side is X^(2+2delta)/(log X)^A, leaving a power gap.

## 2. A quantitative bound for the full remainder

Let F(u)=u^(3/5)/(log u)^(1/5). From the current unconditional
Lee--Leong Mertens estimate and the exact coefficient unit, there is
a fixed eta>0 such that, for every epsilon>0,

\[
 -C_\varepsilon X^{2+\varepsilon}
 \le P_X^{\mathrm{rem}}
 \le C X^3(\log X)^2 e^{-2\eta F(\log X)}
       +C_\varepsilon X^{2+\varepsilon}.                         \tag{3}
\]

The transfer retains the source exponent constant. A purely analytic
bound for the absolute unit norm at 3/4 is less than 162. The source
constants and starting range are named exactly in the
[proof](FULL-ESTIMATE.md), with a [separate review](REVIEW-FULL-ESTIMATE.md).
No source computation was rerun. This proves every fixed logarithmic
saving for the complete sum, not just the earlier top panel.

The exponent reduction is
2 eta/[(log X)^(2/5)(log log X)^(1/5)], which tends to zero.
Thus (3) does not prove any fixed power saving from X^3. This is a
limitation of the displayed upper bound, not a lower bound or a
counterexample to the desired bound on the actual sum.

## 3. Two further cuts and one precise surviving target

**Candidate-D.** The original split-support terms with
P^+(d)<=(log X)^(2+o(1)) can be removed from T and from its long tail
with pointwise error O_epsilon(X^(1/2+epsilon)) on the block. A separate
argument removes Fourier conductors r with the same smoothness condition
at that error scale, retaining the full original coprime cofactor A_r
on every surviving conductor. The masks in d and r are not identified.
[Proof and sharp boundaries](SMOOTH-SUPPORT.md),
[opposition](REVIEW-SMOOTH-SUPPORT.md).

For the stricter absolute bound O(sqrt n), the actual residue tail has
the sharp threshold c<1/(4e^2) in c(log n)^2. The neighboring owner
[2093](https://github.com/mathorn1973/twist-j/pull/2093) already proved
that threshold for its orientation carrier. Our proof credits it,
evaluates the shared weighted saddle through its positive endpoint
term, and verifies the transfer to the present residue kernel. For a
fixed exponent A>2 the absolute deletion error has squared size at
least X^(3-2/A-o(1)) on an unbounded sequence of blocks. None of these
absolute lower bounds asserts a signed lower bound.

Here is one concrete combined reduction, with no moving research choices.
For all sufficiently large dyadic X put

\[
 y_X=(\log X)^2,\qquad
 Y_X=\sqrt X\exp(-\sqrt{\log X}).
\]

Let G_X^star retain exactly the original modes satisfying
P^+(r)>y_X and h(theta)<Y_X. Define P_X^star by the original ordered
unequal-conductor determinant strip and gcd cut on this spectrum.
Its actual summands and coefficients are unchanged.

The high-height packet has pointwise size
O_epsilon(X^(1+epsilon)/Y_X) by the numerator proof, so its tapered
square norm is O_epsilon(X^(2+epsilon)) after shrinking input epsilon.
The smooth-conductor packet has the same square-norm bound, uniformly
under the additional numerator restriction by the absolute proof.
Combining both with the inherited approximation gives

\[
 \sum_n w_X(n)|T(n)-G_X^\star(n)|^2
       \ll_\varepsilon X^{2+\varepsilon}.                       \tag{4}
\]

The finite energy identity, far-pair bound and large-gcd pruning apply
to this smaller spectrum and give

\[
 \sum_n w_X(n)|G_X^\star(n)|^2
       =P_X^\star+O_\varepsilon(X^{2+\varepsilon}).               \tag{5}
\]

The norm triangle inequality and the prior finite-block Mellin argument
prove the exact remaining criterion

\[
 \mathrm{RH}\quad\Longleftrightarrow\quad
 (P_X^\star)_+\ll_\varepsilon X^{2+\varepsilon}
 \quad\text{for every fixed }\varepsilon>0
 \text{ on all sufficiently late dyadic blocks}.                 \tag{6}
\]

This criterion concerns the joint low-height, rough-conductor sum.
Its genuine numerator-one same-sign positive subtotal is still of
order X^3. The high-height and smooth-support estimates do not close it.
Equation (4), rather than an unproved bound on the difference of the
two pair sums, justifies the conductor deletion. An unconditional
X^(2+epsilon) estimate of the deleted mixed energy is not asserted.

## 4. A proposed shortcut which demands more

[PREFIX-PANEL-SCOPE](PREFIX-PANEL-SCOPE.md) proves that a separate
X^(2+epsilon) bound for the positive part of every first-harmonic
prefix 2X<r,s<=u<=4X would imply square-root bounds for
sum_{r<=v}s(r). Its Dirichlet series is 1/[zeta(s)L(s,chi_5)U(s)],
so this would also exclude L(s,chi_5) zeros to the right of 1/2.
The full joint sum has the zeta-only equivalence (6). The added
character consequence belongs to the separate, uniform prefix demand.
No such consequence is inferred from one fixed endpoint panel, and
no logical independence between the two zero statements is claimed.

## Review and scientific status

Two Astra and two Sol participants, including root, developed and
opposed the paper arguments. Root read every mathematical file,
checked the primary source statements and combined the estimates in
(4)--(6). The five retained opposition files identify their scope.
This is same-session review, not external independent confirmation.
No new scientific executable, numerical experiment or formal verifier
was run. Earlier finite evidence stays candidate-C and byte unchanged.
All new deductions stay candidate-D and the signed bound (6) stays O.
No Canon, registry, workflow, merge or release is part of this round.
