# Arithmetic cancellation: signed frequencies, paired tails and moving cuts

**NON-CANONICAL, no authority. Candidate-D paper deductions; candidate-C finite audits.**
Owner: A. M. Thorn / ChatGPT arithmetic-kernel session, 24 November 2026.
Claim: [#2087](https://github.com/mathorn1973/twist-j/issues/2087).
Action layer: NOT_APPLICABLE. No Canon promotion or independent RH proof.

The first result bounds the moving support `d^3 <= n^2` unconditionally.
The signed continuation now isolates an explicit remaining Fourier sum,
pairs the rough and mixed contributions at the same integer argument, and
proves a positive second-order term after the leading large-prime terms
cancel. The arithmetic good-window estimate remains open.

## Signed continuation

All statements in this section are **candidate-D**, with the conditional
premise and the open bound explicitly retained. The continuation is paper
work only; its [scope contract](round3/PREREG.md) and internal reviews make
no new finite-execution claim.

| Result | Exact gain and boundary | Proof |
|---|---|---|
| Actual signed spectrum | An explicit real sequence `G` has weighted squared error from `T` at most `O((1+log Y)^6)` on every window. Small conductors and high numerator modes are removed with that proved cost. The same-window good property transfers both ways. | [SIGNED-SPECTRUM](round3/SIGNED-SPECTRUM.md) |
| Exact finite-block target | RH is equivalent to the positive signed cross-conductor term being `O_epsilon(X^(2+epsilon))` for every positive epsilon and all sufficiently late dyadic `X`. The full finite Dirichlet kernel retains all pair distances. | [Section 4.1](round3/SIGNED-SPECTRUM.md) |
| Unmasked complete energy | The complete-period mean of the squared truncated sum is of order `D log D`, and its true minimum frequency gap is of order `D^-2`. Signs do not improve these two global quantities enough to extend the old large-sieve expression. This is not an incomplete-interval lower bound. | [Sections 1–2](round3/SIGNED-SPECTRUM.md) |
| Joint large-prime slice | For each fixed `2/3 <= a < 1`, the part of the actual tail with greatest prime above `X^a` is `X/(U(1) log^2 X) + O_a(X/log^3 X)`. Its complement has the opposite expansion through every fixed logarithmic order. | [LARGE-PRIME-TAIL](round3/LARGE-PRIME-TAIL.md) |
| Smooth inverse | Both full rough and mixed sums contain the same smaller-argument terms with opposite signs. A uniform bound treats a growing threshold independently of the earlier fixed-u asymptotic. | [SMOOTH-INVERSE](round3/SMOOTH-INVERSE.md) |
| Exact termwise threshold | At `z=(log X)^A`, the positive inverse slice `X/2<e<=X` has exponent `max(log(2)/log(11),1-1/A)`. For `A>2` it forbids a termwise absolute square-root bound; for `A<=2` a globally assumed square-root bound for `T` transfers to both full pieces. The premise is not proved. | [Sections 3–4](round3/SMOOTH-INVERSE.md) |
| Arbitrary moving rough cut | The short rough and mixed corrections have total weighted squared size `O((1+log Y)^6)`, uniformly over every real threshold function `z(n)`. | [MOVING-ROUGH-MASK](round3/MOVING-ROUGH-MASK.md) |

The spectral reduction uses the exact fact

\[
 T(n)-T(n-1)=(s*\chi_5)(n)\in\{-1,0,1\}.
\]

For each dyadic scale `X`, the retained modes have primitive frequencies
`a/(5r)` with `r>X^(2/3)` and the stated small-numerator cutoff.
The diagonal and pairs with the same conductor have controlled energy.
The primary remaining target is the exact signed sum `D_X` of all
cross-conductor contributions on `X <= n < 2X`:

\[
 \mathrm{RH}\quad\Longleftrightarrow\quad
 (D_X)_+\ll_\varepsilon X^{2+\varepsilon}
 \quad\text{for every }\varepsilon>0
 \text{ and all sufficiently large dyadic }X.
\]

**O:** establish that bound arithmetically, or prove the equivalent
one-sided good windows of `G` directly. The equivalence itself supplies
neither estimate. The original `T` window test is exactly rational;
the numerator-cut sequence `G` is an analytical aid. Keeping entire
conductor blocks gives a separate exactly rational reduction.

An optional positive majorant over all integer times leaves only close
pairs with `1 <= |as-br| <= 5rs/(2X)`. Its proposed polylogarithmic bound
would additionally exclude zeros of `L(s,chi_5)` with real part above
`2/3`. That further consequence was found during opposition and proved in
[MAJORANT-SCOPE](round3/MAJORANT-SCOPE.md). No contradiction to this
sufficient target is shown, and its necessity for RH is not claimed.
The exact finite-block criterion above includes distant pairs and avoids
this extension of the time interval.

The neighboring Mertens prime average was reconstructed from its reported
formula. Its coefficient is `1`, whereas the present residue-weighted
statistic has coefficient `1/U(1)`. The unavailable local rapidity files
are not treated as verified evidence. See the exact comparison in
[LARGE-PRIME-TAIL](round3/LARGE-PRIME-TAIL.md).

Internal review: [spectrum](round3/REVIEW-SPECTRUM.md),
[inverse and moving cut](round3/REVIEW-INVERSE.md), and
[large-prime term](round3/REVIEW-LARGE-PRIME.md), followed by the
[majorant and finite-block review](round3/REVIEW-MAJORANT-SCOPE.md).
The prime-five scope in
the norm formula was corrected during review. All contributing conductors
are coprime to five, so the application is unchanged.

## Main arithmetic statement

Let `chi=chi_5`, and let `H(q)=sum_{m<=q}chi(m)`, whose residue values are
`(0,1,0,-1,0)`. Define `s(d)=(-2)^omega(d)` on squarefree products of primes
congruent to `1` or `4` modulo `5`, including `s(1)=1`, and zero elsewhere.
Put

\[
 T(n)=\sum_{d\le n}s(d)H(\lfloor n/d\rfloor),\qquad
 L(n)=\sum_{d^3\le n^2}s(d)H(\lfloor n/d\rfloor),\qquad R(n)=T(n)-L(n).
\]

**Candidate-D, unconditional.** For all integer `Y>=2`,

\[
 \sum_{n=Y}^{Y^2-1}\frac{|L(n)|^2}{n(n+1)}\ll(1+\log Y)^4.
\]

The bound holds for the actual moving cutoff. The proof uses the exact
complete-period covariance

\[
 \operatorname{mean} K_dK_e
 =\frac25\chi(d/g)\chi(e/g)\frac{g^2}{de},\qquad
 g=\gcd(d,e),\quad K_d(n)=H(\lfloor n/d\rfloor).
\]

On split support the character signs are positive. The nonnegative majorant
`f=1*chi`, with `sum_{m<=x}f(m)<=x`, bounds the absolute covariance form by
`O(D(1+log D))`. A self-contained additive large sieve with spacing
`(5D)^(-2)` and the binary prefix decomposition give the moving estimate.
The proof does not assume cancellation in the coefficients `s(d)`.
[Full kernel proof](KERNEL.md), especially section 7.

For any fixed `a>2/3`, selected subsets of genuine split-prime coefficients
produce positive weighted energy at least a constant times
`X^(3a-2)/(log X)^2`. Thus extending this bound uniformly over arbitrary
coefficient masks beyond `2/3` is impossible. This lower bound is not for the
complete unmasked arithmetic sum.

## The exact remaining target

Set `D_n=max{d: d^3<=n^2}`, `A(t)=sum_{d<=t}s(d)`. The tail is exactly

\[
 R(n)=\sum_{k\le n/(D_n+1)}H(k)
 \left[A(\lfloor n/k\rfloor)
 -A\bigl(\max(D_n,\lfloor n/(k+1)\rfloor)\bigr)\right].
\]

The integer quotient index is less than `n^(1/3)`. This does not bound the
signed interval sums of `A`.

For `Q_F(Y)=sum_{n=Y}^{Y^2-1}max(F(n),0)^2/[n(n+1)]`, the new theorem gives

\[
 |\sqrt{Q_T(Y)}-\sqrt{Q_R(Y)}|\ll(1+\log Y)^2.
\]

Consequently the following good-window property transfers in both
directions, on the same windows with exponent slack:

\[
 \forall r\in\mathbb Z_{\ge1}\ \forall Y_0\ge1\quad
 \exists Y\in\mathbb Z_{\ge\max(2,Y_0)}:\quad Q_R(Y)^r\le Y.
\]

**Candidate-D:** this property is equivalent to RH by the retained signed
window foundation. **O:** prove it arithmetically for `R`. The analytic
equivalence supplies no such estimate. See [WINDOW-TAIL](WINDOW-TAIL.md) and
the self-contained [FOUNDATION](FOUNDATION.md).

## Why every fixed roughness split requires cancellation

For fixed real `u>1`, let `B_u(n)` restrict `R(n)` to integers all of whose
prime factors exceed `n^(1/u)`, and put `H_u=R-B_u`.

**Candidate-D on classical unconditional inputs.**

\[
 B_u(n)\sim-c_u\frac n{\log n},\qquad
 H_u(n)\sim+c_u\frac n{\log n},\qquad
 c_u=\rho(u-1)L(1,\chi_5)>0.
\]

Here `rho` is the classical Dickman function. At `u=3`, only prime and
distinct-semiprime supports occur in `B_u`, and
`c_3=(1-log 2)L(1,chi_5)`. The weighted prime count contributes `-1`; the
weighted semiprime count contributes `log 2`. For arbitrary fixed `u`,
the prime-product integrals sum to `-rho(u-1)`. The character quotient tail
is bounded after recombining by `d`, avoiding an unjustified unsigned
harmonic estimate.

The negative rough asymptotic uses the fixed-modulus prime number theorem.
The positive complementary asymptotic additionally uses the classical
unconditional Mertens bound and the exactly proved Dirichlet unit.
In particular, `Q_(H_u)(Y) >>_u Y^2/(log Y)^2` on every late window, while
the positive part of `B_u` eventually vanishes. Estimating the two positive
parts separately destroys the required cancellation. Every fixed `u` has a
nonzero coefficient; no uniform assertion for `u=u(n)` follows.
[Cube-root proof](ROUGH-TAIL.md) and [all fixed powers](GENERAL-ROUGH.md).

## What the parallel return-order work contributes

The full Boolean return stream of an odd squarefree modulus determines its
unit order and one sometimes invisible sign bit. It can lose the number of
split prime factors. Multiplying the equal-order primes `101` and `151` by
the common split prime `241` puts a concrete collision inside the long tail:

| Row datum at `N=3675491` | `d=24341=101*241` | `d=3675491=101*151*241` |
|---|---:|---:|
| Entire Boolean return flags | identical | identical |
| Residue modulo 150 | 41 | 41 |
| `H(floor(N/d))` | 1 | 1 |
| `d^3>N^2` | yes | yes |
| Actual signed contribution | +4 | -8 |

This collision survives common Boolean gcd/lcm windows because the two
individual prime flags coincide. It does not cover an oracle returning
the full numerical gcd or the integer modulus itself. In general, an lcm
window can collect distinct prime factors from different neighbors, a
qualification explicitly proved in the note.

Vertical prime-power orders do recover the integer modulus. For odd `d`
prime to five, `alpha=phi^2`, `h=ord_d(alpha)` and
`B=cont(1-alpha^h)`,

\[
 \operatorname{ord}_{d^k}(\alpha)
 =h\frac{d^k}{\gcd(d^k,B)}.
\]

The ratio of successive orders eventually equals `d`. This stronger
observation changes the information available, but still supplies no signed
window bound. See [RETURN-READOUT](RETURN-READOUT.md). Source ownership remains
with [PR #2085](https://github.com/mathorn1973/twist-j/pull/2085) for its
return contents, windows and equal-order witnesses.

The later [PR #2088](https://github.com/mathorn1973/twist-j/pull/2088) supplies
a genuinely stronger additive input. Its prescribed six-unit rule has content
`604=4*151` at the relevant parameter, so its gcd is `1` on `24341` and `151`
on `3675491`. It directly separates our two long-tail rows. This is outside
the Boolean-stream contract and is an explicit usable connection between
the parallel lines. It still supplies no whole-window cancellation estimate.
The actual pinned six-unit proof was checked during final readback.

## Review, evidence and reading order

Root read all proof files. A separate Sol read the complete kernel proof,
including the sharper fourth-logarithm argument. The second Astra checked
the exact tail, the positive complementary obstruction and the fixed-power
extension, with an independent reconstruction of the Dickman coefficient.
This is internal same-session mathematical review, not blind independent
confirmation, external review or proof-assistant verification.

The three finite integer audits retain their original source and inputs.
They check 841 complete kernel correlations and 512 quotient identities;
the rough decomposition through 8192 with two strict-boundary controls;
and 50 small return periods plus the equal-order witness and nine vertical
moduli. These are candidate-C checks on one architecture. The extended
`241` witness and arbitrary-`u` theorem are paper deductions, not added
finite runs. [RUN](RUN.md) states the exact evidence and path mapping.

The general gcd-square, large-sieve and oscillation machinery is classical
and has project antecedents. No historical priority claim is made. The
source scope and current parallel-work pins are in [SOURCES](SOURCES.md).
