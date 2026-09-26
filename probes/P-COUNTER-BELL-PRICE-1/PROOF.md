# P-COUNTER-BELL-PRICE-1 proofs

Notation as in PREREG.md. For a counter model put
`nu(lambda) = min_(x,y) mu_xy(lambda)` and `r_xy = mu_xy - nu`.

## (C1) Canonical split

`nu >= 0` because every `mu_xy >= 0`, and `r_xy >= 0` by the definition of
the minimum. Since every `mu_xy` has mass one,
`mass(r_xy) = 1 - mass(nu) = eps` for every setting pair.

## (C2) Determinization

Replace `lambda` by `(lambda, s, t)`, where `s` and `t` are deterministic
response strings, with weight

    w(s,t|lambda) = prod_x alpha(s_x|x,lambda) prod_y beta(t_y|y,lambda),
    mu'_xy(lambda,s,t) = mu_xy(lambda) w(s,t|lambda).

Summing over the strings other than `s_x` and `t_y` returns
`alpha(a|x,lambda) beta(b|y,lambda)`, so the behaviour is unchanged. Because
`w` does not depend on the settings and is nonnegative,
`min_xy mu'_xy(lambda,s,t) = w(s,t|lambda) nu(lambda)`, and summing over the
strings gives the same common mass. So eps is unchanged, and every bound
below may be proved for deterministic responses.

## (C3) CHSH

With deterministic responses `A_x(lambda), B_y(lambda)` in `{+1,-1}` and
signs `sigma = (+,+,+,-)`,

    S = sum_lambda nu(lambda) s(lambda)
        + sum_(x,y) sigma_xy sum_lambda r_xy(lambda) A_x B_y,
    s(lambda) = A_0 (B_0 + B_1) + A_1 (B_0 - B_1) in {-2, +2}.

The first sum has absolute value at most `2 mass(nu) = 2(1 - eps)`. Each of
the four remaining terms has absolute value at most `mass(r_xy) = eps`.
Hence `|S| <= 2 + 2 eps`.

Attainment. Take latent points `c` and `lambda_xy` for the four setting
pairs, `mu_xy = (1 - eps) delta_c + eps delta_(lambda_xy)`. Let `c` answer
`+1` everywhere, so `s(c) = 2`. Let `lambda_xy` answer `+1` on Alice at `x`
and `sigma_xy` on Bob at `y`. Then `E_xy = (1 - eps) + eps sigma_xy` for the
three plus pairs and `E_11 = (1 - eps) - eps`, so `S = 2 + 2 eps`. The
common mass is `1 - eps` at `c` and zero at each `lambda_xy`, which is used
by one setting pair only; the overlap is exactly eps.

Tsirelson value. `2 + 2 eps = 2 sqrt 2` if and only if
`eps = sqrt 2 - 1`, which lies strictly between 0 and 1. The construction
above with `eps = sqrt 2 - 1`, evaluated in `Q(sqrt 2)`, gives
`S = 2 sqrt 2` exactly. Since the bound is linear and strictly increasing in
eps, the supremum of `|S|` over the class with overlap at most `e` is
`min(4, 2 + 2e)`; no value of `e` makes `2 sqrt 2` a ceiling except that one
tuned value.

## (C4) Five-context functional

For a deterministic type with LOW sets `A`, `B` put `a = |A|`, `b = |B|`,
`c = |A intersect B|`. The functional of that type is `2c - (ab - c) =
3c - ab <= 3c - c^2 <= 2`, as in the registered proof of
QDD-FIVE-CONTEXT-BELL-SEPARATION. On the `r` part, each of the five diagonal
terms contributes at most `2 mass(r_kk) = 2 eps` and each off-diagonal term
contributes at most zero. Hence

    B <= 2 (1 - eps) + 10 eps = 2 + 8 eps.

Attainment. `mu_xy = (1 - eps) delta_c + eps delta_(lambda_xy)` with
`c = ({0},{0})`, `lambda_kk = ({k},{k})` and `lambda_kl = (empty, empty)` for
`k != l`. Then `B = 2(1 - eps) + 10 eps` and the overlap is eps.
`2 + 8 eps = 35/16` exactly when `eps = 3/128`.

## (C5) The complete ETH-QDD-2 table

Lemma, direction one. Let a counter model reproduce `P` with overlap eps.
The `nu` part defines the setting-independent local behaviour
`N(a,b|x,y) = sum_lambda nu(lambda) alpha beta` of mass `1 - eps`, and
`N <= P` entrywise because `nu <= mu_xy`. Thus `P = (1 - eps) L + eps Q` with
`L = N / (1 - eps)` local and setting independent and `Q = (P - N) / eps`
a behaviour, so `1 - eps <= w*`.

Lemma, direction two. Given `P = w L + (1 - w) Q`, write `w L` as a
nonnegative combination `sum_d y_d L_d` of deterministic types and add, for
each setting pair `(x,y)` and outcome pair `(a,b)`, one latent copy used only
at `(x,y)` with weight `(1 - w) Q(a,b|x,y)` and responses `a` and `b`. This
counter model reproduces `P`; its common mass is `sum_d y_d = w`, because
each copy appears at one setting pair only. So the minimal overlap is
exactly `1 - w*`.

Zeros. `P(LH|k,k) = P(HL|k,k) = 0`, so every type with positive weight in
`w L` has `A = B`.

Primal point. Weight `10/64` on each of the five types `A = B = {k}` and
`1/64` on each of the ten types `A = B = {k,l}`; total `50/64 + 10/64 =
15/16`. Entrywise, with the local sum on the left:

    diagonal LL   10/64 + 4/64  = 14/64 <= 16/64
    diagonal HH   40/64 + 6/64  = 46/64 <= 48/64
    diagonal LH, HL                 0 <= 0
    off LL                      1/64  <= 1/64
    off LH, HL    10/64 + 3/64  = 13/64 <= 15/64
    off HH        30/64 + 3/64  = 33/64 <= 33/64

Dual certificate. Let `z = 1` on every diagonal LH and HL entry,
`z = 1/4` on every off-diagonal LL entry, `z = 1/12` on every off-diagonal
HH entry, and `z = 0` elsewhere. For a type with `A != B` some diagonal
entry is LH or HL, so it collects at least 1. For `A = B = S` with
`|S| = s` it collects

    s(s-1)/4 + (5-s)(4-s)/12,

which equals `5/3, 1, 1, 5/3, 3, 5` for `s = 0, ..., 5`, never below 1. For
any feasible `y`,

    sum_d y_d <= sum_d y_d sum_e z_e L_d(e) = sum_e z_e sum_d y_d L_d(e)
              <= sum_e z_e P(e) = 20 (1/64)(1/4) + 20 (33/64)(1/12)
               = 5/64 + 55/64 = 15/16.

So `w* = 15/16` and the minimal overlap is `1/16`.

## (C6) Signalling

`p_A(a|x,y) = sum_lambda nu(lambda) alpha(a|x,lambda)
+ sum_lambda r_xy(lambda) alpha(a|x,lambda)`. The first sum does not depend
on `y`; the second lies in `[0, eps]`. Hence the difference for `y, y'` has
absolute value at most eps, and likewise for Bob. Attainment: latent points
`c`, `g0`, `g1` with `mu_xy = (1 - eps) delta_c + eps delta_(g_y)`, where
Alice answers the first letter at `c` and `g0` and the second letter at
`g1`. Then `p_A(first|x,0) - p_A(first|x,1) = eps`, and the overlap is eps.

## Scope

These are finite theorems on the stated comparison classes at L6. Nothing
here identifies the latent variable with a TWIST-J state or chooses a causal
mechanism.
