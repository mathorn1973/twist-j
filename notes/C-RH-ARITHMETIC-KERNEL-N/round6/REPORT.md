# Cancellation at low height and an exact smaller-argument replacement

**NON-CANONICAL. No authority. All deductions candidate-D. The complete
signed power estimate remains O.** Same owner issue
[2087](https://github.com/mathorn1973/twist-j/issues/2087) and draft
[2089](https://github.com/mathorn1973/twist-j/pull/2089). This continuation
starts at `f55cbcd1bf0eff6de99449c37ac8c03916b8acfe`.

The low-height attack has two concrete outcomes. First, three actual
signed conductor sums have explicitly opposing main terms already at
heights at most `(log X)^14`. Second, all conductors with a prime factor
above `(4X)^(1/3)` can be replaced by an exact arithmetic function using
only smaller arguments of T, with the required all-epsilon square-norm
error. The remaining Fourier conductors have at least three distinct
split prime factors. Their interaction with that arithmetic function is
still part of the open estimate.

## 1. Fixed carrier and meaning of the error scale

Let chi be the quadratic character modulo five, let
`H(q)=sum_(m<=q) chi(m)`, and let `s(d)=(-2)^omega(d)` on squarefree
products of primes congruent to one or four modulo five, zero elsewhere.
Include `s(1)=1`. The actual arithmetic function is

\[
 T(n)=\sum_{d\le n}s(d)H(\lfloor n/d\rfloor),\qquad
 t(n)=T(n)-T(n-1),\qquad |t(n)|\le1.
\]

Use dyadic X, D=4X, and the unchanged nonnegative rational taper w from
[FINITE-TAPER](../round4/FINITE-TAPER.md), supported on
`[7X/8,17X/8]` and equal to one on `[X,2X)`. Write
`||f||_w^2=sum_n w(n)|f(n)|^2`. The genuine spectrum G_X^star of
[round five](../round5/REPORT.md) retains all original coefficients,
coprime cofactors, primitive frequencies `theta=a/(5r)`, shell and
numerator conditions, and the fixed cuts

\[
 P^+(r)>(\log X)^2,\qquad
 h(\theta)=X|a|/r<\sqrt X\exp(-\sqrt{\log X}).
\]

Its signed pair sum P_X^star retains the original unequal-conductor,
determinant-strip and small-gcd conditions. The inherited facts are

\[
 \|T-G_X^\star\|_w^2\ll_\varepsilon X^{2+\varepsilon},\qquad
 \|G_X^\star\|_w^2=P_X^\star+O_\varepsilon(X^{2+\varepsilon}).
\]

The all-epsilon positive-part bound for P_X^star on all sufficiently
late dyadic blocks is equivalent to zeta RH. Here and below this is an
equivalence of mathematical targets. RH is not an input to the new proofs.

## 2. Opposing actual main terms at small heights

Partition the conductors of G_X^star into `P^+(r)>sqrt D` and its
complement. Denote their amplitudes by G_+ and G_-, where the labels name
the two sets, not the signs of individual coefficients. Let P_++ and
P_-- be the signed pair sums within these sets. Let P_mix contain both
orders of the mixed pairs, with every original pair restriction intact.

Put `kappa=1/U(1)>0`, with U the fixed coefficient unit, and

\[
 M_X=\sum_n w(n)\frac{n^2}{(\log n)^4}
       \asymp \frac{X^3}{(\log X)^4}.
\]

**Candidate-D.** On every sufficiently late dyadic block,

\[
 \begin{aligned}
 P_{++}&=\kappa^2 M_X+O(X^3/(\log X)^5),\\
 P_{--}&=\kappa^2 M_X+O(X^3/(\log X)^5),\\
 P_{\rm mix}&=-2\kappa^2 M_X+O(X^3/(\log X)^5).
 \end{aligned}                                                     \tag{1}
\]

The same assertions hold when both frequencies are further restricted
to `h<=(log X)^14`. These are actual signed sums, with their original
arithmetic weights. Consequently an attempted bound
`O_epsilon(X^(2+epsilon))` for each of the two within-set sums separately
is false, for every fixed epsilon below one. Their mixed contribution
must be retained. Equation (1) exhibits the cancellation but does not
bound its remaining error at square-root scale.

The exact reason for the leading terms is the marked-prime identity

\[
 \Phi_{pq}(n)=\Phi_q(\lfloor n/p\rfloor)-\Phi_q(n)/p,
 \qquad A_{pq}(D)=-2A_q(D/p)\quad(p>\sqrt D).
\]

It compares the primitive conductor cut with the original support cut,
rather than identifying them. The correction has size O(sqrt X).
The raw large-prime sum is
`-2 sum_(p>sqrt D, split) T(floor(n/p))`. Fixed-modulus prime counting
and the zero zeroth Mellin moment of T give its main term
`kappa n/(log n)^2`. The complementary amplitude has the opposite main
term because the full T has the inherited unconditional savings of
every fixed logarithmic order.

To reach genuinely low heights, the proof also establishes the uniform
mean-square numerator bound

\[
 \|G_{h\in I}\|_w
 \ll \frac{X^{3/2}(1+\log X)^{10}}{Y},
 \qquad I\subset[Y,10\sqrt X],                                  \tag{2}
\]

for a single height interval and any conductor mask depending only on r.
It sums the actual character-bearing numerators before taking conductor
absolute values. The translated divisor bound
`sum_(m<=7X) tau_3(m)^2 << X(1+log X)^8` replaces the previous
pointwise X^epsilon cost. Equation (2) controls both rectangles crossing
the height boundary. At Y=(log X)^14 it preserves (1); it does not
permit deleting that whole height tail at the all-epsilon target scale.

[Full derivation](MARKED-PRIME-CANCELLATION.md) and
[same-session opposition](REVIEW-MARKED-PRIME.md).

## 3. Exact cancellation at the target scale for the marked packet

Let Pi count split primes and define the exact profile

\[
 C_X(n)=-2\sum_{m\le n/\sqrt D}
       t(m)\bigl[\Pi(n/m)-\Pi(\sqrt D)\bigr].
\]

All its coefficient arguments on the taper satisfy
`m<=17 sqrt(X)/16`. For the full G_X^star cutoff, the marked-prime
comparison and the proven spectral errors imply

\[
 \|G_+-C_X\|_w^2\ll_\varepsilon X^{2+\varepsilon}.              \tag{3}
\]

In particular,

\[
 P_{++}-2\operatorname{Re}\langle G_+,C_X\rangle_w
       +\|C_X\|_w^2=O_\varepsilon(X^{2+\varepsilon}).            \tag{4}
\]

The three terms in (4) individually have absolute order
`X^3/(log X)^4`. Their signed combination is paid at the target scale.
The profile is determined by exact finite prime counts and actual
smaller coefficients. Substituting only its leading asymptotic term
would lose this precision. Equation (3) is proved for the original
full star cutoff, not for the much smaller `(log X)^14` packet alone.

## 4. Transfer down to the cube root and the concrete remaining sum

There is a stronger replacement than (3). For an arbitrary threshold z,
let L_z be the complete primitive projection with `P^+(r)<=z` and B_z
the original support sum with `P^+(d)<=z`. The exact factorization
`d=e q`, with `P^+(e)<=z<P^-(q)`, gives

\[
 L_z(n)-B_z(n)=
 \sum_{\substack{e\le D/z\\P^+(e)\le z}}s(e)K_e(n)
 \sum_{\substack{1<q\le D/e\\P^-(q)>z}}\frac{s(q)}q.            \tag{5}
\]

The discrepancy has only short support `e<=E=D/z`. Its weighted
square norm, also after the original smoothing multiplier, is at most

\[
 O\bigl((1+\log D)^5(XE+E^3)\bigr).                             \tag{6}
\]

Thus `z>=D^(1/3)` suffices at the target scale. This comes from the
shorter support and the finite large sieve. A pointwise absolute
estimate for (5) alone would only pay the square-root threshold.

Fix from now on `z=D^(1/3)`. The entire high-prime packet can be replaced
by the exact function

\[
 C_z(n)=-2\sum_{z<p\le n}T(\lfloor n/p\rfloor)
       -4\sum_{\substack{z<p\le q\\pq\le n}}
                         T(\lfloor n/(pq)\rfloor),             \tag{7}
\]

where all displayed primes are split. The diagonal p=q is essential.
It removes repeated-prime contributions introduced by replacing a
coprime cofactor sum with T. Every single-prime argument in (7) is at
most `n/z=O(X^(2/3))`; every double-prime argument is at most
`n/z^2=O(X^(1/3))`.

Finally the remaining conductors through `z^2=D^(2/3)` can also be
removed with squared norm O(X^2 log^3 X). Let G_core retain exactly
the original star modes with

\[
 D^{2/3}<r\le D,\qquad
 (\log X)^2<P^+(r)\le D^{1/3}.                                  \tag{8}
\]

Every nonzero r in (8) is squarefree and has at least three distinct
split prime factors. All original cofactor and numerator conditions
remain. The result is

\[
 \|T-(G_{\rm core}+C_z)\|_w^2
       \ll_\varepsilon X^{2+\varepsilon}.                       \tag{9}
\]

Write P_core for the original restricted determinant sum on pairs of
these conductors. Define

\[
 Q_{\rm core}(X)=P_{\rm core}(X)
       +2\operatorname{Re}\langle G_{\rm core},C_z\rangle_w
       +\|C_z\|_w^2.                                             \tag{10}
\]

**Candidate-D, exact remaining criterion.**

\[
 \mathrm{RH}\quad\Longleftrightarrow\quad
 (Q_{\rm core}(X))_+\ll_\varepsilon X^{2+\varepsilon}
 \quad\text{for every fixed }\varepsilon>0
 \text{ and all sufficiently late dyadic }X.                    \tag{11}
\]

The proof uses (9), the norm triangle inequality and the unchanged
restricted energy identity. It never assumes an unconditional small
difference between two pair sums. The exact C_z and its mixed term
stay in (10). Smaller arguments alone supply no contraction or
induction closing (11). The cube-root cutoff is proved sufficient;
its optimality is not claimed.

[Proof](CUBE-ROOT-TRANSFER.md) and [opposition](REVIEW-CUBE-ROOT.md).

## 5. Two supporting estimates and their limits

**Candidate-D.** The actual short sums of t also pay the error of the
positive compact-spectrum Jackson smoother J_H, rather than just the
earlier rational triangular smoother:

\[
 \sum_{X/2\le n\le3X}|F_D(n)-J_HF_D(n)|^2
       \ll_{\eta,A}XH^2/(\log X)^A,
 \quad X^{1/3+\eta}\le H\le X^{1-2\eta}.
\]

Here eta is fixed in `(0,1/12)` and A is any fixed positive exponent.
For `H=ceil(sqrt X (log X)^B)`, fixed B, this error is below
`X^2/(log X)^A` for every fixed A. Smooth frequency annuli obey the
same cost without dividing by a multiplier that can vanish. This
improves control of the actual smoothing error. The corresponding
frequency cap is wider than the existing round-five star cap, so it
is not a further removal from that already smaller spectrum. A separate
integer-increment model demonstrates that these inherited short-sum
budgets and spectral geometry alone do not force the missing power
bound. The model does not have the actual arithmetic coefficients.
[Proof](SHORT-SPECTRAL-SCALES.md), [review](REVIEW-SPECTRAL-SCALES.md).

**Candidate-D.** The signed coefficients of U have a cubic main term:

\[
 \sum_{k\le x}u(k)=C_Ux^{1/3}+O_\sigma(x^\sigma),\qquad
 C_U>0,\qquad \frac{\log2}{\log11}<\sigma<\frac13.
\]

This differs from the square-root growth of their absolute mass. It
follows by extracting `L(2s,chi) zeta(3s) L(3s,chi)` and using a direct
signed square/cube summation. Transferring the neighboring balanced
Mertens identity to t retains a nonpositive square drift and an
explicit signed cubic correction. A controlled balanced residual
F_bal then satisfies

\[
 \sum_{N\ge Y}\frac{|T(N)-F_{\rm bal}(N)|^2}{N(N+1)}
       \ll_\sigma(\log Y)^{-5/3}.
\]

The same-window criterion transfers, with no sign assigned to the
cubic correction and no omission of long affine terms. This is a
separate equivalent carrier, not a new estimate for the positive part
of (10). [Proof](BALANCED-UNIT-TAIL.md),
[review](REVIEW-BALANCED-UNIT.md).

## 6. Sources, opposition and status

The new head of neighboring [2093](https://github.com/mathorn1973/twist-j/pull/2093)
is `2147cba363d90d2772c3d5f883d79c326260d9c9`. Its balanced Mertens
construction and sawtooth covariance retain attribution. Its orientation
residual, window convention and open target are not identified with ours.
The fixed-modulus prime theorem and the published MRSTT short-interval
input were checked in their primary sources. No source computation was
rerun and no external RH proof is a premise.

Two Astra and two Sol participants, including root, derived and opposed
the paper arguments. Root read all four proofs and every retained review,
checked the exact projector algebra, error costs and whole-block
quantifiers, and proposed the further finite-conductor deletion in (8).
Four opposition records are retained. This is same-session review, not
external independent confirmation or proof-assistant verification.

There was no new scientific executable, numerical sum or finite audit.
Earlier evidence and scientific files remain unchanged. All results
stay candidate-D; (11) remains O. Repository checks establish custody
and required process integrity, not mathematical promotion.
