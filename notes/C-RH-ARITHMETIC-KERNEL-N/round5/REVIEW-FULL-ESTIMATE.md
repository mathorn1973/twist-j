# Paper review of the complete determinant envelope

NON-CANONICAL. No authority. Same-session review of `FULL-ESTIMATE.md`. The source theorem and the deduction were checked, without rerunning its numerical work or any candidate checker.

## Exact source and unit

The unversioned arXiv abstract identifies v5, dated 9 September 2026, as current in its submission history. At the pinned v5, Theorem 1.1 equation (12) gives the bound for `x>=exp(exp(10.01))` with the factors listed in the draft. The first numerical factor is exactly `517/20`, the zero-free parameter is exactly `5399/100`, and the logarithm of the logarithm of the starting argument is `1001/100`. The extra factor inside the exponent is `(1-log(5399/100)/log(log x))^(-1/5)`. Its denominator lies strictly between zero and one on the stated range. For positivity, `exp(1001/100)>exp(10)>1+10+10^2/2>5399/100`. Dropping the factor weakens the inequality while preserving the stated threshold and exponent constant. No displayed conditional input concerning zeros of `L(s,chi_5)` is involved.

For `U^(-1)`, the split local series is `1-z^2/(1-z)^2`, which has constant coefficient one and nonpositive coefficients in degrees at least two. Its absolute coefficient series is `1+z^2/(1-z)^2`. The other two given series follow directly from the inert and ramified local factors. At `z=p^(-3/4)`, the split and ramified arguments are below `1/2` by the corresponding fourth-power comparisons. The split absolute factor is at most `1+4z^2<=(1-z^2)^(-4)`, and the inert factor is bounded by the same fourth power. The ramified factor is below two. Including the positive missing factor at five in the comparison product only enlarges it. Hence `B<2 zeta(3/2)^4<162`, with the last strict inequality from integration of the decreasing function `t^(-3/2)`. This also verifies why an absolute coefficient norm, as needed for an unconditional transfer, is being estimated.

## Constant-preserving transfer

For `F(u)=u^(3/5)(log u)^(-1/5)`, its derivative tends to zero. With `L=log x` and `d<=sqrt(x)`, the threshold `x>=x0^2` puts `x/d` in the imported estimate's range. If `eta sup_(v in [L/2,L]) |F'(v)|<=1/4`, the mean value theorem gives

```
exp(-eta F(L-log d)) <= exp(-eta F(L)) d^(1/4).
```

The convolution originally contributes `|v(d)|/d`, so this is exactly the weight change to `|v(d)|/d^(3/4)` controlled by `B`. For `d>sqrt(x)`, the trivial absolute bound for `M(x/d)` leaves `d^(-1/4)<=x^(-1/8)` after extracting the same weight. This proves (3), including its constants and the split endpoint. Since `F(log x)=o(log x)`, the term `B x^(7/8)` is eventually absorbed while keeping exactly the same displayed `eta`. A source threshold is supplied, and the additional transfer threshold is described implicitly. The draft does not present it as a numerically determined threshold.

## Actual weighted energy and the signed remainder

Every time in the actual taper support is comparable to `X`, uniformly there. Since `F'` tends to zero, changing `log X` by a bounded amount changes `F` by `o(1)`. Squaring the transferred estimate and summing over the `O(X)` support gives (5) with its factor `2 eta` intact. The taper takes values between zero and one. Thus the earlier unweighted error estimate on that support transfers to the desired weighted energy. The square of the triangle inequality gives the stated `O(X^2(1+log X)^5)` addition. Conversely the nonnegativity of the weighted energy gives the lower estimate on `P_X` independently of the source Mertens bound. Absolute large-gcd pruning costs `O_epsilon(X^(2+epsilon))` on either side. This verifies both inequalities in (6) for the actual real signed `P_X^rem`; it makes no positivity assertion for that off-diagonal sum itself.

For every fixed logarithmic exponent the exponential decay absorbs the two explicit logarithms in (6). The power-sized error there can be taken with fixed `epsilon<1` for the same comparison. On the other hand the exponent reduction is `2 eta/[(log X)^(2/5)(log log X)^(1/5)]`, which tends to zero. The main upper envelope in (6) therefore does not imply any fixed power saving from `X^3`, nor does its size give a lower bound for the actual determinant sum. The required all-epsilon estimate on the actual remainder stays open. I found no mathematical fault requiring a correction.

- [Lee and Leong, arXiv version history](https://arxiv.org/abs/2208.06141)
- [Lee and Leong, pinned v5, Theorem 1.1 equation (12)](https://arxiv.org/html/2208.06141v5#Thmtheorem1.1)
