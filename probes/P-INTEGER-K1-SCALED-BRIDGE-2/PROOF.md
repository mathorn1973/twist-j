# Proofs for P-INTEGER-K1-SCALED-BRIDGE-2

Status: NON-CANONICAL. Conditional `L1` proofs for the declared scaled K1
reflection carrier and coupled source-holonomy bridge, plus unconditional `L1`
proof of the 3-adic quadratic precision lower bound on `DEF-K1-LINEAR-METRIC`.

## 1. Universal Domain-and-Bank Reflection Bijection Lemma: Claim B1

Let `X` be a countable carrier, let `D_+, D_-` be subsets of `X`, and let
`T^(+1) : D_+ -> D_-` be a bijection with inverse `T^(-1) : D_- -> D_+`. Let
`E : X -> Z_(>=1)` be a positive integer functional. On the funded state space
`Omega = X x Z_(>=0) x {-1, +1}`, define `R(x, b, epsilon) = (x, b, -epsilon)`
and

```text
F(x, b, epsilon) = (T^epsilon(x), b + E(x) - E(T^epsilon(x)), epsilon)
                   if x in D_epsilon and b + E(x) - E(T^epsilon(x)) >= 0,
                 = (x, b, -epsilon)
                   otherwise.
```

**Theorem 1 (Total Bijectivity and Involution-Conjugate Inverse).**
`F` maps `Omega` into `Omega`, preserves `E(x) + b` on every state, and is a
bijection of `Omega` onto itself with exact inverse `F^-1 = R o F o R`.

**Proof.**
If `(x, b, epsilon)` satisfies the guard (`x in D_epsilon` and
`c = b + E(x) - E(y) >= 0` where `y = T^epsilon(x)`), then `c in Z_(>=0)` and
`E(y) + c = E(x) + b`. If the guard fails, `F(x, b, epsilon) = (x, b, -epsilon)`
keeps `b in Z_(>=0)` and `E(x) + b` unchanged. Thus `F : Omega -> Omega` is
well-defined and energy-conserving.

Now evaluate `(R o F o R)(F(x, b, epsilon))` in the two cases:

1. **Case 1 (`(x, b, epsilon)` passes the guard):**
   Then `F(x, b, epsilon) = (y, c, epsilon)` with `y = T^epsilon(x) in D_(-epsilon)`,
   `T^(-epsilon)(y) = x`, and `c = b + E(x) - E(y) >= 0`. Applying `R` gives
   `(y, c, -epsilon)`. Since `y in D_(-epsilon)` and
   `c + E(y) - E(T^(-epsilon)(y)) = c + E(y) - E(x) = b >= 0`, `(y, c, -epsilon)`
   passes the guard of `F` in direction `-epsilon` and maps under `F` to
   `(x, b, -epsilon)`. Applying `R` returns `(x, b, epsilon)`.
2. **Case 2 (`(x, b, epsilon)` fails the guard):**
   Then either `x notin D_epsilon` or `b + E(x) - E(T^epsilon(x)) < 0`, and
   `F(x, b, epsilon) = (x, b, -epsilon)`. Applying `R` gives `(x, b, epsilon)`,
   which fails the identical guard and maps under `F` to `(x, b, -epsilon)`.
   Applying `R` returns `(x, b, epsilon)`.

Since `R^2 = id_Omega`, setting `G = R o F o R` gives `G o F = id_Omega`, and
conjugating by `R` gives `F o G = R o (G o F) o R = id_Omega`. This proves
that `F` is a bijection on `Omega` with `F^-1 = R o F o R`.

### Application to `F_K1` and `F_bridge`

1. **For `X_K1 = Z^5 x Z^5 x Z_(>=1)`:**
   Set `D_+ = X_K1` and `T_K1^(+1)(U, W, k) = (C U - 104976 W, U, k + 1)`.
   If `T_K1^(+1)(U, W, k) = (U', W', k')`, then `k' = k + 1 >= 2`, `W' = U`,
   and `C W' - U' = 104976 W == 0 (mod 104976)`, so `(U', W', k') in D_-` and
   `T_K1^(-1)(U', W', k') = (W', (C W' - U') / 104976, k' - 1) = (U, W, k)`.
   Conversely, for any `(U', W', k') in D_-`, `(W', (C W' - U') / 104976, k' - 1)`
   lies in `X_K1 = D_+` and maps under `T_K1^(+1)` to `(U', W', k')`. Thus
   `T_K1^(+1) : D_+ -> D_-` is a bijection with inverse `T_K1^(-1)`.
   Moreover, on a fixed shell `E_K1(U, W, k) + b = M`, `1 <= k <= M - 1`,
   `sum_r U_r^2 <= M - 2`, `sum_r W_r^2 <= M - 2`, and `0 <= b <= M - 2`, so
   the shell is finite and every `F_K1`-orbit is purely periodic.
2. **For `X_bridge`:**
   Phases `0..5` are bijections on the full carrier (by Section 3 of #1633's
   `PROOF.md`), and Phase `6` acts by `T_K1^(+1)` on `(U, W, k)` while fixing
   all other registers and incrementing `p : 6 -> 0`. Hence `D_+ = X_bridge`,
   `D_-` restricts only `(p == 0, epsilon == -1)` to `(U, W, k) in D_-(K1)`,
   and `T_bridge^(+1) : D_+ -> D_-` is a bijection with inverse `T_bridge^(-1)`.
   Theorem 1 therefore establishes Claim B1 for both `F_K1` and `F_bridge`.

---

## 2. Exact Scaled K1 Representation and Lossless Bounce Cycles: Claim B2

In `DEF-K1-LINEAR-METRIC`, the rational five-vectors `h_n^(w) in Q^5` satisfy
`h_0^(w) = U0^(w) / 2`, `h_1^(w) = U1^(w) / 2`, and for `n >= 1`:

```text
h_(n+1)^(w) = (C h_n^(w)) / 324 - h_(n-1)^(w).
```

Define `U_n^(w) = 2 * 324^n h_n^(w)` for `n >= 0` and
`x_n^(w) = (U_n^(w), U_(n-1)^(w), n)` for `n >= 1`. At `n = 1`,
`x_1^(w) = (324 * U1^(w), U0^(w), 1) in X_K1`. Multiplying the K1 recurrence
by `2 * 324^(n+1)` yields:

```text
U_(n+1)^(w) = C U_n^(w) - 324^2 U_(n-1)^(w) = C U_n^(w) - 104976 U_(n-1)^(w).
```

By induction on `n >= 1`, `x_(n+1)^(w) = T_K1^(+1)(x_n^(w)) in X_K1`, and the
current-state rational reader satisfies

```text
R_K1(x_n^(w)) = U_n^(w) / (2 * 324^n) = h_n^(w)   for all n >= 1.
```

### Strict monotonicity of `E_K1(x_n^(w))` and sharp bounce cycles

Because `sum_(r=0)^4 h_n^(w)(r) = 1` for all `n >= 0`, we have
`sum_(r=0)^4 U_n^(w)(r) = 2 * 324^n`. By Cauchy-Schwarz on `R^5`,

```text
sum_(r=0)^4 (U_n^(w)(r))^2 >= (2 * 324^n)^2 / 5 = (4/5) * 324^(2n).
```

On the other hand, by `K1-LINEAR-METRIC-COMPLETION`, `-59/100 < h_n^(w)(r) < 99/100`,
so `|U_n^(w)(r)| < 2 * 324^n` and `sum_(r=0)^4 (U_n^(w)(r))^2 < 20 * 324^(2n)`.
Since `(4/5) * 324^(2(n+1)) = (4/5) * 104976 * 324^(2n) = 83980.8 * 324^(2n) > 20 * 324^(2n)`,
we have `||U_(n+1)^(w)||_2^2 > ||U_n^(w)||_2^2` for every `n >= 0`, and hence

```text
E_K1(x_1^(w)) < E_K1(x_2^(w)) < ... < E_K1(x_N^(w)) < E_K1(x_(N+1)^(w)).
```

Consequently, for any target horizon `N >= 1` and initial bank
`B_sharp^(w)(N) = E_K1(x_N^(w)) - E_K1(x_1^(w))`:

1. Starting at `S_0 = (x_1^(w), B_sharp^(w)(N), +1)`, for each step `1 <= m <= N - 1`,
   the remaining bank after moving to `x_(m+1)^(w)` is
   `E_K1(x_N^(w)) - E_K1(x_(m+1)^(w)) >= 0`, so `F_K1` advances to
   `S_(N-1) = (x_N^(w), 0, +1)`.
2. At `S_(N-1)`, attempting `x_N^(w) -> x_(N+1)^(w)` yields proposed bank
   `E_K1(x_N^(w)) - E_K1(x_(N+1)^(w)) < 0`, so `F_K1` reflects to
   `S_N = (x_N^(w), 0, -1)`.
3. For the next `N - 1` steps in direction `epsilon = -1`, each `x_m^(w)` (`m >= 2`)
   lies in `D_- = T_K1^(+1)(X_K1)` and releases positive energy
   `E_K1(x_m^(w)) - E_K1(x_(m-1)^(w)) > 0` into the bank, reaching
   `S_(2N-1) = (x_1^(w), B_sharp^(w)(N), -1)`.
4. At `S_(2N-1)`, `k = 1 < 2`, so `x_1^(w) notin D_-`, and `F_K1` reflects at
   the lower domain boundary to `S_(2N) = (x_1^(w), B_sharp^(w)(N), +1) = S_0`.

If instead the initial bank is `B_sharp^(w)(N) - 1` (`N >= 2`), all steps up
to `x_(N-1)^(w)` succeed with positive bank `E_K1(x_N^(w)) - E_K1(x_(N-1)^(w)) - 1 >= 0`,
while the step `x_(N-1)^(w) -> x_N^(w)` has proposed bank `-1 < 0` and reflects
at `k = N - 1`, closing a lossless cycle of length `2(N - 1)`. This proves Claim B2.

---

## 3. Unconditional 3-Adic Quadratic Precision Lower Bound: Claim B3

By Section 8 of `P-INTEGER-SOURCE-HOLONOMY-1` (`PROOF.md`), for every word
`w in W` and every counter `n >= 1`, the least positive common denominator
`d_n` of the reduced rational entries of `h_n^(w) in Q^5` satisfies

```text
v_3(d_n) = 4(n - 1).
```

Let `(P_n, D_n) in Z^5 x Z_(>=1)` be **any** integer representation of `h_n^(w)`
such that `h_n^(w)(r) = P_n(r) / D_n` for `r = 0, 1, 2, 3, 4`.

1. By definition of the least positive common denominator `d_n`, `d_n` divides
   `D_n`. Since `D_n >= 1` and `3^(4(n-1))` divides `d_n`, we have
   `D_n >= d_n >= 3^(4(n-1))`.
2. Since `sum_(r=0)^4 h_n^(w)(r) = 1`, summing `P_n(r) = D_n h_n^(w)(r)` gives
   `sum_(r=0)^4 P_n(r) = D_n`. By the pigeonhole principle, at least one
   coordinate satisfies `P_n(r) >= ceil(D_n / 5) >= ceil(3^(4(n-1)) / 5)`.
3. By the Cauchy-Schwarz inequality on `R^5`,

   ```text
   5 * sum_(r=0)^4 P_n(r)^2 >= (sum_(r=0)^4 P_n(r))^2 = D_n^2.
   ```

   Adding `5 D_n^2` to both sides and dividing by `5` gives the exact universal
   lower bound:

   ```text
   sum_(r=0)^4 P_n(r)^2 + D_n^2 >= (6/5) D_n^2 >= (6/5) d_n^2 >= (6/5) * 3^(8(n-1)).
   ```

This proves Claim B3 across all integer numerator/denominator encodings.

---

## 4. Additive Transverse Metric Readout: Claim B4

For any state `(U, W, k) in X_K1`, the additive transverse metric at site
`r in Z/5` is

```text
g_r(U, k) = diag(-1, 1 + h_k(r), 1 - h_k(r), 1),   h_k(r) = U_r / (2 * 324^k).
```

On every reachable K1 state `x_k^(w)` (`w in W, k >= 1`), `h_k(r) = h_k^(w)(r)`.
By `K1-LINEAR-METRIC-COMPLETION [T]` (`canon/CANON.md`), every site and counter
satisfies `-59/100 < h_k^(w)(r) < 99/100`. Therefore:

```text
1 + h_k^(w)(r) > 41/100 > 1/100,
1 - h_k^(w)(r) > 1/100,
|h_k^(w)(r)| < 99/100  =>  1 - (h_k^(w)(r))^2 > 1 - 9801/10000 = 199/10000 > 0,
det g_r(U, k) = -(1 - (h_k^(w)(r))^2) < -199/10000 < 0.
```

Because `g_r(U, k)` is formed by adding the traceless perturbation
`diag(0, h_k(r), -h_k(r), 0)` to `eta = diag(-1, 1, 1, 1)` rather than
conjugating a single fixed form `Q_0` by a frame in `GL_4(Q(sqrt(5)))`, the
non-square determinant ratio `det g_(1/2) / det g_0 = 3/4` is represented
directly without any field-extension square root. This proves Claim B4.

---

## 5. Coupled 7-Phase Source-Holonomy and K1 Precision Gate: Claim B5

Consider the coupled 40-integer state `X_bridge` starting at

```text
s = a in {-1, +1}, q = 0, H = R = D = diag(0, 1), Z = Z0 = [[1, j], [bar(j), 1]],
(U, W, k) = x_1^(0010) = ((324, 324, 0, 0, 0), (0, 1, 1, 0, 0), 1),
p = 0, epsilon = +1.
```

During phases `p = 0, 1, 2, 3, 4, 5`, `(U, W, k)` is retained with constant K1
account contribution

```text
k + ||U||_2^2 + ||W||_2^2 = 1 + (324^2 + 324^2) + (1^2 + 1^2) = 209955.
```

Adding `209955` to the 6-phase Hermitian costs `(26, 26, 38, 58, 142, 372, 742)`
for `a = -1` and `(26, 26, 38, 58, 142, 372, 798)` for `a = +1` gives the exact
prefix costs through phase 5:

```text
a = -1: (209981, 209981, 209993, 210013, 210097, 210327, 210697),
a = +1: (209981, 209981, 209993, 210013, 210097, 210327, 210753).
```

At phase `p = 6`, the K1 step advances `x_1^(0010)` to `x_2^(0010)` using
`U_1^(0010) = (324, 324, 0, 0, 0)` and `W_1^(0010) = (0, 1, 1, 0, 0)`:

- At `r = 0`: `C U_1(0) = 460*324 + 29*(324 + 0) + 65*(0 + 0) = 158436`,
  minus `104976 * W_1(0) = 0` gives `U_2(0) = 158436`.
- At `r = 1`: `C U_1(1) = 460*324 + 29*(0 + 324) + 65*(0 + 0) = 158436`,
  minus `104976 * W_1(1) = 104976` gives `U_2(1) = 53460`.
- At `r = 2`: `C U_1(2) = 29*324 + 65*324 = 30456`,
  minus `104976 * W_1(2) = 104976` gives `U_2(2) = -74520`.
- At `r = 3`: `C U_1(3) = 65*324 + 65*324 = 42120`,
  minus `104976 * W_1(3) = 0` gives `U_2(3) = 42120`.
- At `r = 4`: `C U_1(4) = 29*324 + 65*324 = 30456`,
  minus `104976 * W_1(4) = 0` gives `U_2(4) = 30456`.

Thus `U_2^(0010) = (158436, 53460, -74520, 42120, 30456)` (with sum
`209952 = 2 * 324^2`), `W_2^(0010) = (324, 324, 0, 0, 0)`, `k = 2`, and:

```text
158436^2 + 53460^2 + (-74520)^2 + 42120^2 + 30456^2
  = 25101966096 + 2857971600 + 5553230400 + 1774094400 + 927567936
  = 36214830432.
```

Thus at `k = 2`:

```text
k + ||U_2||_2^2 + ||W_2||_2^2 = 2 + 36214830432 + 209952 = 36215040386,
Delta E_K1(1 -> 2) = 36215040386 - 209955 = 36214830431.
```

Therefore, the post-phase-6 total energy is:

```text
a = -1: E_7(-1) = 210697 + 36214830431 = 36215041128,
        sharp 7-phase bank = 36215041128 - 209981 = 36214831147;
a = +1: E_7(+1) = 210753 + 36214830431 = 36215041184,
        sharp 7-phase bank = 36215041184 - 209981 = 36214831203.
```

At bank `b = 772`, all 6 Hermitian phases succeed (leaving bank `56` for
`a = -1` and `0` for `a = +1` at `p = 6`, with `coeff_j(Z01) = 0` or `2`), and
phase `6` reflects because `56 < 36214830431` and `0 < 36214830431`. At bank
`36214831147`, `a = -1` completes all 7 phases with final bank `0` while
`a = +1` reflects at phase `6` (short by `56`). At bank `36214831203`, both
signs complete all 7 phases with final banks `56` and `0`. This proves Claim B5.
