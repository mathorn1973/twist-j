# Result: P-INTEGER-K1-SCALED-BRIDGE-4

Status: NON-CANONICAL (`L1`, `RESULT=PASS`)

Public lock: `#1635`.
Predecessor probe: `P-INTEGER-SOURCE-HOLONOMY-1` (`PR #1633`, issue `#1632`).
Abandoned pins disclosed before pin:
- `P-INTEGER-K1-SCALED-BRIDGE-1` (`632f59e97c169abe937e00a6d92642f32378d767`, closed `Status: ABANDONED` at `1d7085545f26563ea4ebfd5faf0ea9fad10a9cd7`, PR `#1636`);
- `P-INTEGER-K1-SCALED-BRIDGE-2` (`fd4e5a2734fd99d94480b6bef30d2c657f6debc3`, closed `Status: ABANDONED` at `0847cf6cc8fe0af0d0fde9e580184a8d40acff2d`, PR `#1637`);
- `P-INTEGER-K1-SCALED-BRIDGE-3` (`989c4ba195d1e6a5ecce9baed437ae2fa1372543`, closed `Status: ABANDONED` at `497e809b8d06fc8d6dc0dc9d9543739f6ff85b57`, PR `#1638`).

Immutable pin commit: `fda020d27b2ea57eafe143a2bc7a3b59a52ef6ce`.
Verifier SHA-256: `d4553c2ebe156717098e0cb2666d898b86bb082aa4a45208f0ad409ba5f5d1ed`.
Breaker SHA-256: `5cd90aafaa4814c213191f1257e4d333a48a3b0d2fb8d6f4a963c6f299e8bbc3`.
Frozen manifest SHA-256: `6eb11eea15c60875b5d25f54c23327ff8fe9091498aaac99818a1c138ec9a4bd`.
Expected stdout SHA-256: `61a71ef6ccee63c4e0e8ebc1f2c08ec48f11768cfa604d3969b2201bf8089ed1` (`1409` bytes, `27` lines).

## 1. Fired Falsifiers

`NONE` (`F1` through `F7` all passed).

## 2. Summary of Earned `L1` Results

1. **Universal Domain-and-Bank Reflection Bijection (`Claim B1`):**
   On the unrestricted scaled K1 integer carrier
   `Omega_K1 = Z^5 x Z^5 x Z_(>=1) x Z_(>=0) x {-1, +1}` (`13` integer
   coordinates) with forward map `T_K1^(+1)(U, W, k) = (C U - 104976 W, U, k + 1)`,
   backward divisibility domain
   `D_- = {(U, W, k) : k >= 2 and C W - U == 0 (mod 104976)}`, backward map
   `T_K1^(-1)(U, W, k) = (W, (C W - U) / 104976, k - 1)`, and positive integer
   cost `E_K1(U, W, k) = 1 + k + ||U||_2^2 + ||W||_2^2`, the Domain-and-Bank
   Reflection rule `F_K1` is a **total bijection on the entire unrestricted
   carrier** with exact inverse `F_K1^-1 = R_K1 o F_K1 o R_K1` and exact
   conservation of `E_K1 + b`. Audited across `2,184` states (`140` forward/backward
   steps, `984` domain-congruence reflections, `1,060` bank reflections).

2. **Exact Scaled K1 Representation and Lossless Periodic Bounce Cycles (`Claim B2`):**
   For every canonical word `w in W` (`|W| = 10`) and counter `n >= 1`,
   `x_n^(w) = (U_n^(w), W_n^(w), n) = (T_K1^(+1))^(n-1)(x_1^(w))` satisfies
   `R_K1(x_n^(w)) = U_n^(w) / (2 * 324^n) = h_n^(w)` and
   `T_K1^(-1)(x_(n+1)^(w)) = x_n^(w)`. Because `E_K1(x_n^(w))` is strictly
   increasing in `n`, funding `x_1^(w)` with the sharp horizon bank
   `B_sharp^(w)(N) = E_K1(x_N^(w)) - E_K1(x_1^(w))` reaches `k = N` with bank
   `0` at step `N - 1`, reflects on step `N` (bank reflection), returns through
   `x_(N-1)^(w), ..., x_1^(w)`, and reflects at `k = 1` on step `2N` (lower
   domain boundary `k < 2`), executing a lossless cycle of exact minimal period
   `2N`. Funding with `B_sharp^(w)(N) - 1` reflects at `k = N - 1` with exact
   minimal period `2(N - 1)`. Verified across all `30` sharp and `30`
   underfunded bounce cycles (`N in {2, 3, 4}`). For `w = 0010`:
   - `E_K1(x_1^(0010)) = 209956`,
   - `E_K1(x_2^(0010)) = 36215040387` (`B_sharp^(0010)(2) = 36214830431`),
   - `E_K1(x_3^(0010)) = 3267670173822148` (`B_sharp^(0010)(3) = 3267670173612192`),
   - `E_K1(x_4^(0010)) = 222607735087755236549`.

3. **Unconditional 3-Adic Quadratic Precision Lower Bound (`Claim B3`):**
   For every exact integer representation `(P_n, D_n) in Z^5 x Z_(>=1)` of
   `h_n^(w) = P_n / D_n` (`w in W, n >= 1`), `v_3(d_n) = 4(n - 1)`,
   `v_3(gcd(U_n^(w), 2 * 324^n)) = 4`, and Cauchy-Schwarz establishes the
   unconditional quadratic precision lower bound:

   ```text
   sum_(r=0)^4 P_n(r)^2 + D_n^2 >= (6/5) * D_n^2 >= (6/5) * d_n^2 >= (6/5) * 3^(8(n-1)).
   ```

   Audited across all `240` word-step pairs (`10` words, `1 <= n <= 24`).

4. **Additive Transverse Metric Readout (`Claim B4`):**
   The additive perturbation readout
   `g_r(U, k) = eta + diag(0, U_r / (2 * 324^k), -U_r / (2 * 324^k), 0)`
   represents the K1 transverse metric directly over `Q` without single-form
   `GL_4(Q(sqrt(5)))` frame congruence (whose obstruction `3/4 notin (Q(sqrt(5))^x)^2`
   was proved in `#1633`), and satisfies `1 + h_n(r) > 1/100`, `1 - h_n(r) > 1/100`,
   and `det g_r(U_n, n) < -199/10000 < 0` across all `1,250` site-step pairs
   (`10` words, `0 <= n <= 24`, `5` sites).

5. **Coupled 7-Phase, 40-Integer Source-Holonomy-K1 Apparatus (`Claim B5`):**
   Coupling the 6-phase Hermitian source-holonomy loop `(s, q, H, R, Z)` over
   `O = Z[j]` with the scaled K1 step `(U, W, k)` in phase `p = 6` yields a
   total bijection `F_bridge` on the `40`-integer carrier `X_bridge` with
   `F_bridge^-1 = R_bridge o F_bridge o R_bridge` and exact conservation of
   `E_bridge + b` (audited on `4,032` states). Starting from `x_1^(0010)`,
   `s = a in {-1, +1}`, `q = 0`, `H = R = diag(0, 1)`, and occupied detector
   `Z_0 = [[1, j], [bar(j), 1]]`:
   - Prefix energies are `(209981, 209981, 209993, 210013, 210097, 210327, 210697, 36215041128)`
     for `s = -1` (sharp 7-phase bank `36214831147`) and
     `(209981, 209981, 209993, 210013, 210097, 210327, 210753, 36215041184)`
     for `s = +1` (sharp 7-phase bank `36214831203`).
   - At bank `772`, both signs complete phases `0..5` (writing `coeff_j(Z_01) = 0`
     or `2` into the occupied detector), reflect at phase `6`, and unwind in
     `6` steps to the exact initial 40-integer state with `epsilon = -1`.
   - At bank `36214831147`, `s = -1` completes all `7` phases to `k = 2` while
     `s = +1` reflects at phase `6` (short by `56`).
   - At bank `36214831203`, both signs complete all `7` phases to `k = 2` with
     final banks `56` and `0`, exact source readout `coeff_j(Z_01) - 1 = s`,
     detector baseline recovery `Z - H + R = Z_0`, rational slice readout
     `R_K1(U, W, k) = h_2^(0010)`, and step-by-step inverse reconstruction.

## 3. Scope Boundaries

This result is `NON-CANONICAL` at `L1`. The integer accounting functionals
`E_K1` and `E_bridge` and the 7-phase coupling schedule are declared `L1`
constructions; they do not claim canonical uniqueness under `DEF-EVOLUTION` or
an `L1 -> L2` derivation of the Einstein source law (`O-G-EINSTEIN-SOURCE-LAW-1`).
