# Arithmetic cancellation: further conductor deletion and a joint slow estimate

**NON-CANONICAL, no authority. Candidate-D paper deductions; candidate-C finite audits.**
Owner: A. M. Thorn / ChatGPT arithmetic-kernel session, 24 November 2026.
Claim: [#2087](https://github.com/mathorn1973/twist-j/issues/2087).
Action layer: NOT_APPLICABLE. No Canon promotion or independent RH proof.

The first result bounds the moving support d^3 <= n^2 unconditionally.
The latest continuation removes additional families from the remaining
three-prime-or-more conductor core at the required error scale. It also
improves the unconditional bound for a specified slow observation of the
core jointly with its exact prime correction. The full signed estimate
remains open.

## Further conductor deletion and the joint low-frequency estimate

**Candidate-D, paper only.** The [round-seven report](round7/REPORT.md)
defines one fixed successor and gives all error and observation scopes.
All previous proofs and finite evidence remain unchanged.

| Actual object or method | Proved estimate or boundary | Proof |
|---|---|---|
| Core conductors with a large product of small prime divisors | A shellwise density bound controls the complete packet. The fixed union using primes through \(\log X\) and \((\log X)^2\) has squared deletion error \(O_\varepsilon(X^{2+\varepsilon})\), including all original numerators. Both classes contain additional actual nonzero modes. | [SMOOTH-DIVISOR-AND-TRANSFER](round7/SMOOTH-DIVISOR-AND-TRANSFER.md) |
| Cube-root correction and its mixed term | \(C_z(n)\) has leading term \(\kappa(\log2-1/2)n/\log^2n\). Core energy, both mixed orders and correction energy have leading coefficients \(1,-2,1\); the exact mixed term stays. | [PRIME-PUSHFORWARD](round7/PRIME-PUSHFORWARD.md) |
| Balanced carrier for the actual \(t\) coefficients | Exact allocation of both affine terms permits raw denominators at most \(4X\). A longer unit cutoff removes the complete unit tail with inverse-all-logarithmic norm error. | [COMPACT-BALANCED-BAND](round7/COMPACT-BALANCED-BAND.md) |
| Smooth time observation of the joint core and correction | Double coefficient cancellation and the signed unit give a strictly larger saving constant than the inherited Mertens envelope on this observation. The proved bound holds throughout the block, including its endpoints, but remains above the square-root scale. | [Balanced scope](round7/COMPACT-BALANCED-BAND.md#6-exact-scope-of-the-comparison) |
| Absolute pair bounds below the cube-root transfer | Actual positive pairs have subtotal at least \((D/z)^3/\log^8X\) for \(z=D^\beta\), \(1/4<\beta<1/3\), and a corresponding bound for every fixed \(0<\beta<1/3\). This excludes an absolute majorization, not signed cancellation. | [Divisor section 2](round7/SMOOTH-DIVISOR-AND-TRANSFER.md#2-the-actual-below-cube-root-discrepancy-has-a-large-positive-subtotal) |
| Generic induction from smaller arguments | Integer unit-step sequences with square-root size, bounded weighted energy and any fixed number of zero Mellin moments still give prime-correction energy \(X^{5/2}/\log^{2k+2}X\) on input scale \(\sqrt X\). These sequences are not the actual \(T\). | [Prime section 4](round7/PRIME-PUSHFORWARD.md#4-a-power-loss-even-with-finitely-many-exact-moment-cancellations) |

For the fixed remaining spectrum \(G_7\) and its original restricted pair
sum \(P_7\), the precise outstanding target is

\[
 (Q_7)_+\ll_\varepsilon X^{2+\varepsilon},\qquad
 Q_7=P_7+2\operatorname{Re}\langle G_7,C_z\rangle_w+\|C_z\|_w^2,
\]

for every fixed positive epsilon and all sufficiently late dyadic blocks.
**O:** this complete jointly signed bound is not proved here. The
[report](round7/REPORT.md) gives the equivalent criterion and the exact
conductors still present. The three proof reviews, synthesis review and the
[promotion handoff](round7/PROMO-C-RH-ARITHMETIC-KERNEL-N.md) retain
candidate-D status; same-session review and repository CI supply no
external mathematical confirmation.

## Low-height continuation

**Candidate-D, paper only.** The [round-six report](round6/REPORT.md)
gives the actual cancellations, exact replacement and remaining criterion.
All earlier proofs and finite evidence are preserved.

| Actual object | Proved estimate or boundary | Proof |
|---|---|---|
| Largest-prime conductor classes above and below `sqrt(4X)` | Each within-class signed sum has leading term `+kappa^2 M_X`; both mixed orders give `-2kappa^2 M_X`, where `M_X` has order `X^3/log^4 X`. This persists for heights at most `log^14 X`. The two classes cannot separately meet the square-root target. | [MARKED-PRIME-CANCELLATION](round6/MARKED-PRIME-CANCELLATION.md) |
| Exact large-prime arithmetic profile | Its difference from the actual marked low-height packet has squared norm `O_epsilon(X^(2+epsilon))`. The resulting centered signed square is controlled at this scale, using exact prime counts and smaller actual coefficients. | [Marked-prime section 5](round6/MARKED-PRIME-CANCELLATION.md#5-replacing-the-marked-family-by-an-exact-smaller-argument-profile) |
| Primitive conductor cut versus original support cut | Their exact discrepancy has support at most `D/z`; finite large-sieve control pays the transfer for `z>=D^(1/3)`. The smaller-argument replacement includes single primes and unordered prime pairs, including `p=q`. | [CUBE-ROOT-TRANSFER](round6/CUBE-ROOT-TRANSFER.md) |
| Remaining conductor domain | After also deleting `r<=D^(2/3)`, every remaining conductor has at least three distinct split primes, all at most `D^(1/3)`. Its mixed term with the exact replacement remains in the equivalent target. | [Cube-root section 3](round6/CUBE-ROOT-TRANSFER.md#3-every-remaining-fourier-conductor-has-at-least-three-distinct-split-prime-factors) |
| Compact-spectrum smoothing | Actual short sums pay every fixed logarithmic saving at `H=ceil(sqrt X log^B X)`. This controls the error and smooth annuli; its frequency cap is wider than the already frozen star cap and is not a further removal from that spectrum. | [SHORT-SPECTRAL-SCALES](round6/SHORT-SPECTRAL-SCALES.md) |
| Signed coefficient unit and balanced carrier | `sum_(k<=x)u(k)=C_U x^(1/3)+O_sigma(x^sigma)`, with positive `C_U` and `log 2/log 11<sigma<1/3`. The negative square, cubic correction and long affine terms give a balanced comparison with finite total late error. | [BALANCED-UNIT-TAIL](round6/BALANCED-UNIT-TAIL.md) |

With `D=4X`, `z=D^(1/3)`, let `G_core` be exactly the original star
spectrum restricted to `D^(2/3)<r<=D` and
`(log X)^2<P^+(r)<=D^(1/3)`. The explicit replacement is

\[
 C_z(n)=-2\sum_{z<p\le n}T(\lfloor n/p\rfloor)
        -4\sum_{\substack{z<p\le q\\pq\le n}}
                   T(\lfloor n/(pq)\rfloor),
\]

with split primes throughout and the diagonal `p=q` retained. All T
arguments have size `O(X^(2/3))`. The bound
`||T-(G_core+C_z)||_w^2 <<_epsilon X^(2+epsilon)` transfers the target to

\[
 Q_{\rm core}=P_{\rm core}
       +2\operatorname{Re}\langle G_{\rm core},C_z\rangle_w
       +\|C_z\|_w^2.
\]

**O:** establish `(Q_core)_+ <<_epsilon X^(2+epsilon)` for every fixed
positive epsilon on all sufficiently late dyadic blocks. The exact
profile and mixed term are required. Smaller arguments do not by
themselves close an induction. Four same-session opposition records,
the paper scope records and the
[promotion handoff](round6/PROMO-C-RH-ARITHMETIC-KERNEL-N.md) retain
candidate-D status. No new scientific computation or external independent
confirmation is claimed.

## Signed-estimate continuation

**Candidate-D, paper only.** The [round-five report](round5/REPORT.md) contains
the full synthesis, the fixed combined cuts and their precise limitation.
All original coefficients and earlier finite evidence are retained.

| Actual object | Proved estimate or boundary | Proof |
|---|---|---|
| All retained pairs whose larger height `X abs(a)/r` is at least `Y` | Absolute value of their signed sum is `O_epsilon(X^epsilon (X^3/Y^2+X^2))` for `640 ceil(3 log_2 X)<=Y<=10 sqrt X`, including threshold-crossing pairs. At `Y=X^delta` this saves a power against their genuine absolute mass. | [NUMERATOR-ESTIMATE](round5/NUMERATOR-ESTIMATE.md) |
| Original triangular smoothing error | `sum abs(T-Tcal_H)^2 << XH^2/log^A X` for every fixed `A`, throughout `X^(1/3+eta)<=H<=X^(1-eta)`. Thus every fixed logarithmic widening of `sqrt X` costs less than `X^2/log^K X` for each fixed `K`. This does not estimate `Tcal_H` itself. | [SHORT-SUM-TRANSFER](round5/SHORT-SUM-TRANSFER.md) |
| Complete signed remainder | Two-sided estimate with lower error `-O_epsilon(X^(2+epsilon))` and upper `O(X^3 log^2 X exp(-2 eta (log X)^(3/5)/(log log X)^(1/5)))+O_epsilon(X^(2+epsilon))`, using the stated classical Mertens input. The exponent reduction tends to zero. | [FULL-ESTIMATE](round5/FULL-ESTIMATE.md) |
| Smooth original supports and, separately, smooth Fourier conductors | Each cutoff `P^+ <= (log X)^(2+o(1))` has square-root-with-epsilon deletion error. The strict absolute `O(sqrt X)` boundary and superquadratic-logarithm obstruction are proved for the actual kernel, crediting the neighboring owner. | [SMOOTH-SUPPORT](round5/SMOOTH-SUPPORT.md) |
| Uniform initial intervals of the first harmonic | The separate all-prefix power bound also excludes zeros of `L(s,chi_5)` to the right of the stated line. It is a stronger obligation than the zeta-only joint criterion. | [PREFIX-PANEL-SCOPE](round5/PREFIX-PANEL-SCOPE.md) |

One fixed combined target retains only conductors with
`P^+(r)>(log X)^2` and heights
`X abs(a)/r<sqrt X exp(-sqrt(log X))`, in addition to every original
numerator, determinant-strip and small-gcd condition. Its signed pair sum
`P_X^star` satisfies

\[
 \mathrm{RH}\quad\Longleftrightarrow\quad
 (P_X^\star)_+\ll_\varepsilon X^{2+\varepsilon}
 \quad\text{for every fixed }\varepsilon>0
 \text{ on all sufficiently late dyadic blocks}.
\]

**O:** prove this remaining joint bound. The deleted packets have proved
square-norm costs; their mixed pair contribution is not bounded separately
without justification. A genuine same-sign positive subtotal of order
`X^3` survives both cuts. The proof and the exact scope of each estimate
are in the [report](round5/REPORT.md).

The new scope records cover the [complete bound](round5/PREREG-FULL.md),
[numerators](round5/PREREG-NUMERATOR.md),
[short sums](round5/PREREG-SHORT.md) and
[smooth supports](round5/PREREG-SUPPORT.md). Internal reviews and the
[promotion handoff](round5/PROMO-C-RH-ARITHMETIC-KERNEL-N.md) retain
candidate-D status. No new scientific computation or external independent
confirmation is claimed.

## Finite-time continuation

All new deductions below are **candidate-D**. This is paper research with
internal same-session opposition. The existing finite audits are unchanged.
The scope records are [finite time](round4/PREREG-FINITE.md),
[local coefficients](round4/PREREG-LOCAL.md),
[prime counts](round4/PREREG-HIERARCHY.md) and
[critical coefficient unit](round4/PREREG-CRITICAL.md).

| Result | Proved gain and remaining boundary | Proof |
|---|---|---|
| Compact time taper | A nonnegative rational weight equals one on the dyadic block and is supported inside `[7X/8,17X/8]`. Removing all frequency pairs farther than `64 k/X`, with `k=ceil(3 log_2 X)`, costs `O(X^-6 (1+log X)^4)` in total absolute value. | [FINITE-TAPER, sections 1–2](round4/FINITE-TAPER.md) |
| Large common divisors | On shells `r~R`, `s~S`, the close pairs with `gcd(r,s)>=max(1,RS min(R/abs(a),S/abs(b))/X^2)` cost `O_epsilon(X^(2+epsilon))` absolutely. The remaining pairs lie on explicit primitive integer progressions. | [Section 3](round4/FINITE-TAPER.md) |
| Actual positive and negative terms | The fixed numerator pair `a=b=1` on `3X<r,s<=4X` has positive contributions at least `cX^3`, even after that pruning. Its full signed sum is `O_B(X^3/log^B X)` for every fixed `B`, from a classical unconditional input. A power saving for the full remaining sum is open. | [Sections 4–5](round4/FINITE-TAPER.md) |
| Rational finite smoothing | At width `H`, diagonal error costs `O(XH)` and common divisors at least `G` cost `O(XH^2/G)`. For `H=X^(1/2+delta)` the choice `G=ceil(H^2/X)` leaves a low-gcd signed target. Actual coprime prime pairs defeat entrywise positive control. | [TRIANGULAR-SMOOTHING](round4/TRIANGULAR-SMOOTHING.md) |
| Dilation correlations | For each reduced ratio `a:b`, the multiplier average has an exact periodic formula and an explicit error. Any finite choice of prescribed prime-power factors also admits a bounded multiplicative sequence with positive mean, so that limited data alone cannot force cancellation. | [DILATION-CORRELATION](round4/DILATION-CORRELATION.md) |
| Two large primes | For fixed `1/3<a<1/2`, the tail splits into exactly zero, one or two prime factors above `X^a`. A unique fixed cutoff cancels the union's `X/log^2 X` term, but leaves a strictly negative `X/log^3 X` term paired with the no-large-prime part. | [LARGE-PRIME-HIERARCHY](round4/LARGE-PRIME-HIERARCHY.md) |
| Critical transfer cost | Both absolute coefficient series equal `zeta(2s)` times a series converging absolutely for `Re s>1/3`. Their weighted critical norms grow as a positive constant times `log x`. Termwise square-root/logarithm transfer therefore costs one logarithm in each direction. | [CRITICAL-UNIT](round4/CRITICAL-UNIT.md) |

For the frozen round-three coefficients `z_theta`, the new primary target is
the real signed sum `P_X^rem` of

\[
 z_{a/(5r)}\overline{z_{b/(5s)}}
 \sum_n w_X(n)e\!\left(n\left(\frac a{5r}-\frac b{5s}\right)\right)
\]

over ordered unequal conductors, the original numerator cutoffs, and exactly

\[
 0<|as-br|\le\frac{320krs}{X},\qquad
 \gcd(r,s)<\max\left(1,\frac{RS}{X^2}
                 \min\left(\frac R{|a|},\frac S{|b|}\right)\right).
\]

Here `r` and `s` belong to their fixed shells `(R,2R]` and `(S,2S]`.
The theorem is

\[
 \mathrm{RH}\quad\Longleftrightarrow\quad
 (P_X^{\mathrm{rem}})_+\ll_\varepsilon X^{2+\varepsilon}
 \quad\text{for every }\varepsilon>0
 \text{ and all sufficiently large dyadic }X.
\]

**O:** prove this signed arithmetic estimate. Both removals have proved
costs; the remaining coefficient sums and signs stay intact. The finite
support of `w_X` lies where the same frozen arithmetic sum agrees with `T`.
Thus this reduction needs no separate zero statement for `L(s,chi_5)`.
It does not assert that distant terms in the original sharp Dirichlet
kernel can simply be deleted.

The independently owned [draft #2093](https://github.com/mathorn1973/twist-j/pull/2093)
supplies the matched absolute-mass input and a comparison with the distinct
rapidity augmentation carrier. Its signed pairing remains a separate
obligation. The new [draft #2092](https://github.com/mathorn1973/twist-j/pull/2092)
has an optimal four-unit separator in one return-factor case; that readout
does not supply the needed whole-block arithmetic estimate. Exact pins and
read scope are in [SOURCES](SOURCES.md).

Reviews: [finite taper](round4/REVIEW-FINITE-TAPER.md),
[prime hierarchy](round4/REVIEW-HIERARCHY.md),
[local correlations](round4/REVIEW-LOCAL-CORRELATIONS.md) and
[critical unit](round4/REVIEW-CRITICAL-UNIT.md).
The [promotion handoff](round4/PROMO-C-RH-ARITHMETIC-KERNEL-N.md) states
what is proved and the remaining arithmetic question. Nothing here changes
the public Canon or claims an independent proof of RH.

## Earlier signed continuation

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
The earlier exact target is the signed sum `D_X` of all
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
this extension of the time interval. The finite-time continuation now also
removes distant pairs after replacing the sharp time weight by the specified
compact taper; its enlarged local support is fully controlled.

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
