# Euler--Hausdorff source contract and a tail bound uniform in r

**NON-CANONICAL. Proof-first, unrun candidate, 2026-09-05.** This note
proposes an unconditional prime-truncation bound. It is not a formal probe,
preregistration, computation record, public claim promotion, or Canon change.
Public Canon v76 remains the authority declared by `STATUS.md`. No scientific
code was executed in preparing this note. The source material used below is
public; no private handoff text is imported.

Independent static review checked the complete normalizations, contour
argument, endpoint cases, all parameter ranges and error enclosure. No
mathematical blocker remains in this candidate. This review creates no
formal public status or computational evidence.

The result controls the omitted prime-power sum at the ordinary-convergence
point `c = 1`, `sigma = 3/2`, uniformly over every integer `r >= 0` for each
`n >= 0`. It does not establish Hausdorff positivity. The completed
archimedean expression is kept exact; errors in its numerical evaluation need
their own enclosure.

## 1. Exact source contract

All logarithms are natural. Let

\[
\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
M(c)=\frac{\xi'}{\xi}(c+\tfrac12),\qquad \sigma=c+\tfrac12>1.
\]

Write `psi = Gamma'/Gamma`, with `psi^(0) = psi`. The ordinary Euler product
gives, with no boundary continuation,

\[
M(c)=\frac1\sigma+\frac1{\sigma-1}-\frac12\log\pi
 +\frac12\psi(\sigma/2)
 -\sum_{m\ge2}\Lambda(m)m^{-\sigma}.
\tag{1}
\]

The standard completion and Euler-product conventions agree with
[DLMF 25.4][D1] and [DLMF 25.2][D2]; the differentiation below is explicit.

Here `Lambda(m) = log p` if `m = p^k` for a prime `p` and integer `k >= 1`,
and it is zero otherwise. Thus every sum over `m` includes all prime powers.
For every integer `j >= 0`, termwise differentiation is justified locally
uniformly on `sigma > 1`, since
`Lambda(m) <= log m` and every corresponding logarithmic moment converges
absolutely. Consequently

\[
M^{(j)}(c)=(-1)^j j!\left[\sigma^{-j-1}+(\sigma-1)^{-j-1}\right]
 -\delta_{j0}\frac12\log\pi
 +2^{-j-1}\psi^{(j)}(\sigma/2)
 +(-1)^{j+1}\sum_{m\ge2}\Lambda(m)(\log m)^j m^{-\sigma}.
\tag{2}
\]

Both pole terms, the gamma argument, its chain-rule power, and the `j = 0`
constant are part of the contract. Equation (2) agrees with the full formula
in the [public prime-moment addendum, lines 163--185][S1].

At `c = 1`, define the exact completed source constants

\[
E_j=j!\left[\left(\frac23\right)^{j+1}+2^{j+1}\right]
 -\delta_{j0}\frac12\log\pi
 +(-1)^j2^{-j-1}\psi^{(j)}(3/4).
\tag{3}
\]

Then

\[
(-1)^jM^{(j)}(1)
 =E_j-\sum_{m\ge2}\Lambda(m)(\log m)^j m^{-3/2}.
\tag{4}
\]

**Source correction.** The derivative display in the [public consolidation,
lines 134--135][S2] omits `-delta_(j,0) log(pi)/2`. Its `j >= 1` expressions
are unaffected, but its displayed formula is incomplete at `j = 0`.
Equations (1)--(4) here use the complete formula already printed in [S1] and
the [earlier public Euler-source addendum, lines 187--200][S3]. This local
transcription correction is distinct from the correction to the signed Weil
pole form in the separate capacity-contraction notes. No conclusion about
that form or about capacity positivity is inferred here.

## 2. Differential normalization and the finite polynomials

For `c > 1/2`, define

\[
D_c=\frac{d}{d(c^2)}=\frac1{2c}\frac d{dc},\qquad
A_{m+1}(c)=\frac{(-1)^m}{m!}D_c^m\!\left[\frac{M(c)}{2c}\right]
\quad(m\ge0),
\]
\[
b_n(c)=c^{2n}A_{n+1}(c),\qquad
H_{n,r}(c)=\sum_{\ell=0}^r(-1)^\ell\binom r\ell b_{n+\ell}(c).
\tag{5}
\]

These are the normalizations of the [public source addendum, lines
85--126][S4]. In particular, `D_c` is not the unscaled derivative `d/dc`,
the factor `1/m!` is required, and at `c = 1` the prefactor `c^(2n)` equals
one. Every cell uses finitely many derivatives; the indices `n,r >= 0` are
independent and unbounded. There is no assertion that a finite rectangle of
cells is a complete RH criterion.

For `0 <= j <= m`, set

\[
C_{m,j}=\frac{(2m-j)!}{2^{2m-j}m!(m-j)!j!},\qquad
P_m(t)=\sum_{j=0}^m C_{m,j}t^j,
\]
\[
Q_{n,r}(t)=\sum_{\ell=0}^r(-1)^\ell\binom r\ell P_{n+\ell}(t)
 =\sum_{j=0}^{n+r}q_{n,r,j}t^j.
\tag{6}
\]

Coefficients outside `0 <= j <= m` are zero. This is an exact finite
definition, including every factorial; it does not depend on interpolated
values or a numerical Fourier transform.

The coefficients in (6) satisfy

\[
C_{m+1,j}=
\frac{(2m+1-j)C_{m,j}+C_{m,j-1}}{2(m+1)}.
\tag{7}
\]

Starting with `A_1(c) = M(c)/(2c)`, the defining differential recursion is
`A_(m+2)(c) = -A_(m+1)'(c)/(2(m+1)c)`. Equation (7) proves by induction that

\[
A_{m+1}(c)=\frac12\sum_{j=0}^m
C_{m,j}(-1)^j c^{j-2m-1}M^{(j)}(c).
\tag{8}
\]

Substituting `c = 1`, (4), and (6) into (5) therefore gives the exact source
identity

\[
\boxed{
H_{n,r}(1)=\frac12\left[
\sum_{j=0}^{n+r}q_{n,r,j}E_j
-\sum_{m\ge2}\Lambda(m)m^{-3/2}Q_{n,r}(\log m)
\right].}
\tag{9}
\]

Only finite linear combinations were interchanged here. Every individual
logarithmic moment is absolutely convergent. The factor `1/2` is retained;
it agrees with the functional-pair normalization in the [corrected public
T1 weight audit, lines 69--86][S5]. Neither RH nor that zero-side
interpretation is needed to derive (9) from (1) and (5).

As algebraic normalization checks, the definitions give

\[
P_0=1,\quad P_1=(1+t)/2,\quad P_2=(3+3t+t^2)/8,
\]
\[
H_{0,0}(1)=M(1)/2,\quad
H_{0,1}(1)=(M(1)+M'(1))/4,\quad
H_{1,1}(1)=(M(1)-M'(1)-M''(1))/16.
\]

These identities agree with the [public low-cell formulas, lines
209--223][S6]; they are not numerical checks or positivity assertions.

## 3. Fourier normalization proved from the finite definitions

For all integers `n,r >= 0`, put

\[
h_{n,r}(z)=\frac{z^{2r}}{(1+z^2)^{n+r+1}}.
\tag{10}
\]

The only poles are at `z = i,-i`. On the real line it is integrable, with
decay `O(|z|^(-2n-2))` at infinity. We use the unnormalized Fourier integral

\[
\widehat h(t)=\int_{\mathbb R}h(u)e^{-itu}\,du.
\]

The polynomial (6) satisfies exactly

\[
\widehat h_{n,r}(t)=\pi e^{-|t|}Q_{n,r}(|t|).
\tag{11}
\]

Here is a direct derivation, independent of a zero formula. For `b > 0`, the
elementary residue integral for `t != 0`, and the arctangent integral for
`t = 0`, give

\[
\int_{\mathbb R}\frac{e^{-itu}}{u^2+b^2}\,du
 =\pi b^{-1}e^{-b|t|}.
\]

Repeatedly applying `-(2(m+1)b)^(-1) d/db` differentiates the integrand
`(u^2+b^2)^(-m-1)` to `(u^2+b^2)^(-m-2)`. Differentiation under the integral
is allowed on compact subintervals of `b > 0` by an integrable majorant.
Induction gives

\[
\int_{\mathbb R}\frac{e^{-itu}}{(u^2+b^2)^{m+1}}\,du
 =\pi b^{-2m-1}e^{-b|t|}P_m(b|t|),
\]

because its polynomial recursion is

\[
P_{m+1}(t)=\frac{(2m+1+t)P_m(t)-tP_m'(t)}{2(m+1)},
\]

equivalent to (7). Finally,

\[
h_{n,r}(u)=\sum_{\ell=0}^r(-1)^\ell\binom r\ell
(1+u^2)^{-n-\ell-1}.
\]

Setting `b = 1` proves (11), also at `t = 0`. This is exactly the convention
in [S5]. The use of (11) below does not suppose that `Q_(n,r)` is positive.
The corrected public audit instead records sign changes for `r >= 1`.

## 4. Candidate theorem: Fourier envelope uniform in r

Let

\[
n,r\in\mathbb Z_{\ge0},\qquad
\frac12<a\le\frac1{\sqrt2},\qquad t\ge0,
\]
\[
\kappa_n=\frac{\binom{2n}{n}}{4^n},\qquad
B_n(a)=\kappa_n(1-a^2)^{-n-1/2}.
\]

The contour parameter `a` is independent of the source center, which stays
fixed at `c = 1`. Then

\[
\boxed{|Q_{n,r}(t)|\le B_n(a)e^{(1-a)t}.}
\tag{12}
\]

The right side is independent of `r`.

**Proof.** Shift the Fourier integral in (11) from the real axis to
`z = u - ia`. No pole is crossed because `a < 1`. For a rectangular contour
with vertical sides `z = +/-R - iv`, `0 <= v <= a`, the rational function is
`O(R^(-2n-2))` uniformly in `v`, for each fixed pair `(n,r)`. Also
`|exp(-itz)| = exp(-tv) <= 1`. Each vertical integral thus tends to zero as
`R -> infinity`. This works at `t = 0` as well as at `t > 0`; no division by
`t` is used. It follows that

\[
\pi e^{-t}Q_{n,r}(t)
 =e^{-at}\int_{\mathbb R}h_{n,r}(u-ia)e^{-itu}\,du.
\tag{13}
\]

To bound the shifted integrand, write `z = u - ia` and `D = |1+z^2|`.
Elementary identities give

\[
D^2=(u^2+(1-a)^2)(u^2+(1+a)^2),
\]
\[
D^2-|z|^4=2u^2+1-2a^2\ge0,
\]
\[
D^2-(u^2+1-a^2)^2=4a^2u^2\ge0.
\]

Since `a < 1`, all denominators and `u^2+1-a^2` are positive. Therefore

\[
|h_{n,r}(u-ia)|
 =\left(\frac{|z|^2}{D}\right)^rD^{-n-1}
 \le (u^2+1-a^2)^{-n-1}.
\tag{14}
\]

In particular, this proves absolute integrability on the shifted line.
The first inequality remains valid at the endpoint `a = 1/sqrt(2)`,
including `u = 0`; equality there causes no singularity. For `r = 0`, the
ratio raised to the zeroth power is one and the same estimate applies.

For every `b > 0`, scaling and the elementary beta integral yield

\[
\int_{\mathbb R}(u^2+b^2)^{-n-1}\,du
 =\pi\kappa_n b^{-2n-1}.
\]

Alternatively this integral follows from the `t = 0` formula in section 3,
since `P_n(0) = kappa_n`. Apply it with `b = sqrt(1-a^2)` in (13)--(14).
Dividing by `pi exp(-t)` proves (12). The final bound is independent of `r`;
the contour limit was taken for each finite `r`, so no unproved interchange
with an `r -> infinity` limit is involved. **QED.**

The standard beta-integral convention is recorded in [DLMF 5.12][D3].

## 5. Candidate theorem: prime truncation with its exact cutoff

Fix an integer `X >= 3`. Define the retained sum and the omitted tail by

\[
S_{n,r}(X)=\sum_{2\le m\le X}\Lambda(m)m^{-3/2}Q_{n,r}(\log m),
\]
\[
T_{n,r}(X)=\sum_{m>X}\Lambda(m)m^{-3/2}Q_{n,r}(\log m).
\tag{15}
\]

The cutoff is weak in the retained sum and strict in the tail. For
`1/2 < a <= 1/sqrt(2)`, let `delta = a - 1/2 > 0`. Then, simultaneously for
every integer `r >= 0`,

\[
\boxed{
|T_{n,r}(X)|\le
B_n(a)X^{-\delta}
\left(\frac{\log X}{\delta}+\frac1{\delta^2}\right).
}
\tag{16}
\]

**Proof.** By (12), the absolute tail is bounded by

\[
B_n(a)\sum_{m>X}(\log m)m^{-a-1/2}
=B_n(a)\sum_{m>X}(\log m)m^{-1-\delta}.
\]

The function `f(x) = (log x)x^(-1-delta)` is positive and decreasing for
`x >= 3`, since its derivative has the sign of
`1-(1+delta)log x < 0`. As `X` is an integer,

\[
\sum_{m=X+1}^\infty f(m)\le\int_X^\infty f(x)\,dx
 =X^{-\delta}\left(\frac{\log X}{\delta}+\frac1{\delta^2}\right).
\]

This proves (16) and absolute convergence of the majorized tail. **QED.**

The explicit rational choice `a = 2/3` gives `delta = 1/6` and

\[
\boxed{
|T_{n,r}(X)|\le
6\kappa_n\left(\frac95\right)^{n+1/2}
X^{-1/6}(\log X+6).
}
\tag{17}
\]

Since `sqrt(9/5) < 3/2`, a weaker bound with a rational prefactor is

\[
|T_{n,r}(X)|\le
9\kappa_n\left(\frac95\right)^n X^{-1/6}(\log X+6).
\tag{18}
\]

For any fixed integer `N >= 0`, using `kappa_n <= 1` gives the common bound

\[
|T_{n,r}(X)|\le
9\left(\frac95\right)^N X^{-1/6}(\log X+6)
\quad(0\le n\le N,\ r\ge0).
\tag{19}
\]

Thus prime truncation converges uniformly over all `r >= 0` in every fixed
finite band `0 <= n <= N`. There is no corresponding uniform-in-`n` claim.

If a retained sum instead uses the strict cutoff `m < X`, its omitted sum
starts at `m = X`. The exact difference is the single boundary term
`Lambda(X) X^(-3/2) Q_(n,r)(log X)`. A valid replacement for (16) is then

\[
B_n(a)\left[
(\log X)X^{-1-\delta}
 +X^{-\delta}\left(\frac{\log X}{\delta}+\frac1{\delta^2}\right)
\right].
\tag{20}
\]

No fractional cutoff, prime-only cutoff, or omitted prime-power convention
is implicit in these statements.

## 6. What error is controlled, and what remains open

Define an exactly truncated cell by

\[
H^{[X]}_{n,r}=\frac12\left[
\sum_{j=0}^{n+r}q_{n,r,j}E_j-S_{n,r}(X)\right].
\]

Equation (9) gives

\[
H_{n,r}(1)-H^{[X]}_{n,r}=-\tfrac12 T_{n,r}(X).
\tag{21}
\]

Therefore the error in this cell is at most one half of (16), (17), (18),
or (19), as applicable. The coefficient `1/2` must not be dropped.

For numerical use, suppose separately that approximations satisfy
`|E_j - Etilde_j| <= epsilon_j` and
`|S_(n,r)(X) - Stilde_(n,r)(X)| <= epsilon_S`. If

\[
\widetilde H^{[X]}_{n,r}
 =\tfrac12\left[\sum_j q_{n,r,j}\widetilde E_j
 -\widetilde S_{n,r}(X)\right]
\]

is formed exactly from these inputs, then a complete enclosure is

\[
|H_{n,r}(1)-\widetilde H^{[X]}_{n,r}|
\le\frac12\left[
\mathcal T_n(a,X)+\sum_j|q_{n,r,j}|\varepsilon_j+\varepsilon_S
\right],
\tag{22}
\]

where `mathcal T_n(a,X)` denotes the right side of (16). Rounding in the
final finite combination, if present, requires an additional enclosure.
Neither the gamma/pole errors nor the finite-sum evaluation error were
bounded by the contour argument. Uniformity in `r` for the prime tail does
not make the full numerical evaluation uniformly well conditioned.

This candidate supplies no inequality of the form `H_(n,r)(1) >= 0`. The
[corrected public T1 audit, lines 193--210][S7] leaves that global source
obligation open and warns that the oscillatory weights do not exclude every
possible positive grouping. A positive lower endpoint from (22) could
certify an individual cell after its finite source quantities are enclosed;
a finite collection of such certificates does not establish RH. The bound
also supplies no spectral carrier, lambda-cocycle realization, or layer lift.

This is a scalar Euler--Hausdorff source contract for the finite rational
test functions (10). Its proof uses no Hardy-space, model-space, Suzuki
finite-interval operator, or capacity identity. It therefore does not arm
the separate Suzuki/Hardy/capacity source contract or discharge its global
positivity and transport obligations.

The [public consolidation, lines 141--147][S8] identifies raw prime-tail
control as a practical obstruction to high derivative evaluation. The new
feature proposed here is a tail envelope independent of `r`, obtained before
taking absolute values of individual polynomial coefficients. It is not a
claim of optimal constants or practical efficiency at a specified precision.

## 7. Provenance and bounded duplication check

The source contract and Fourier convention above are rederived from the
following public texts. Their candidate status is preserved. The cited
public branch pin is an audit source, not an authority substitute.

- [Public prime-moment addendum][S1], public branch
  `notes/c-rh-weil-norm-junction-1-n`, frozen read at commit
  `bed965bd5e3c1847dfcf0596cfef6bdc1da6f621`: differential and Hausdorff
  identities, complete derivatives, and low cells.
- [Public T1 correction and weight audit][S5], frozen main read at
  `c6a2ee33e70ebc5cf24d77f3a16c9cb6d0d3d8fe`: Fourier normalization,
  moment/sign structure, and the still-open all-cell source inequality.
- [Public Ray/Pick consolidation][S2] and [Euler-source addendum][S3] at the
  same main pin: the omitted zero-order constant is identified against the
  complete formula, and the existing prime-tail limitation is recorded.

A read-only search of the current public `notes/`, `probes/`, and `canon/`,
and of the named public junction addendum, found no existing version of the
uniform-in-`r` envelope (12) or the tail bound (16). This is a bounded
repository duplication check, not a literature-priority claim. No abandoned
probe identifier is reused. A later formal audit, if selected, needs its own
fresh identifier and procedure; this note has no pin or run record.

[S1]: https://github.com/mathorn1973/twist-j/blob/bed965bd5e3c1847dfcf0596cfef6bdc1da6f621/notes/C-RH-WEIL-NORM-JUNCTION-1-N/RAY-PRIME-MOMENT-HAUSDORFF-ADDENDUM.md#L163
[S2]: https://github.com/mathorn1973/twist-j/blob/c6a2ee33e70ebc5cf24d77f3a16c9cb6d0d3d8fe/notes/incubation-import-2026-08-21/C-RAY-PICK-KERNEL-374/CONSOL-RAY-PICK-KERNEL-374_2026-08-20.md#L134
[S3]: https://github.com/mathorn1973/twist-j/blob/c6a2ee33e70ebc5cf24d77f3a16c9cb6d0d3d8fe/notes/incubation-import-2026-08-21/C-RAY-PICK-KERNEL-374/ADDENDUM-RAY-PICK-KERNEL-374_2026-08-19.md#L187
[S4]: https://github.com/mathorn1973/twist-j/blob/bed965bd5e3c1847dfcf0596cfef6bdc1da6f621/notes/C-RH-WEIL-NORM-JUNCTION-1-N/RAY-PRIME-MOMENT-HAUSDORFF-ADDENDUM.md#L85
[S5]: https://github.com/mathorn1973/twist-j/blob/c6a2ee33e70ebc5cf24d77f3a16c9cb6d0d3d8fe/notes/incubation-import-2026-08-21/SESSION-RECORDS/AUDIT-T1-WEIGHT-THEOREM_2026-08-20.md#L69
[S6]: https://github.com/mathorn1973/twist-j/blob/bed965bd5e3c1847dfcf0596cfef6bdc1da6f621/notes/C-RH-WEIL-NORM-JUNCTION-1-N/RAY-PRIME-MOMENT-HAUSDORFF-ADDENDUM.md#L209
[S7]: https://github.com/mathorn1973/twist-j/blob/c6a2ee33e70ebc5cf24d77f3a16c9cb6d0d3d8fe/notes/incubation-import-2026-08-21/SESSION-RECORDS/AUDIT-T1-WEIGHT-THEOREM_2026-08-20.md#L193
[S8]: https://github.com/mathorn1973/twist-j/blob/c6a2ee33e70ebc5cf24d77f3a16c9cb6d0d3d8fe/notes/incubation-import-2026-08-21/C-RAY-PICK-KERNEL-374/CONSOL-RAY-PICK-KERNEL-374_2026-08-20.md#L141
[D1]: https://dlmf.nist.gov/25.4
[D2]: https://dlmf.nist.gov/25.2
[D3]: https://dlmf.nist.gov/5.12
