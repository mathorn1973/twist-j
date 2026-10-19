# P-INTEGER-K1-SCALED-BRIDGE-1

Status: PREREGISTERED proposal; NON-CANONICAL.

Owner: A. M. Thorn, session `antigravity-integer-k1-scaled-bridge-2026-10-19`.
Public ownership: https://github.com/mathorn1973/twist-j/issues/1635
Branch: `probe/P-INTEGER-K1-SCALED-BRIDGE-1`.
Base: `dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`, Public Canon v103.

## 1. Equation and claims

`P-INTEGER-SOURCE-HOLONOMY-1` (PR #1633, issue #1632) constructed a 6-phase
reversible integer Hermitian source-holonomy apparatus over `O = Z[j]` and
proved that the canonical K1 metric recurrence (`DEF-K1-LINEAR-METRIC`) has
least positive common slice denominator `d_n` satisfying `v_3(d_n) = 4(n-1)`
for all `n >= 1` and all ten canonical source words. Consequently, no fixed
denominator and no fixed current-state rational reader on one finite-energy
shell of a fixed-precision carrier can represent the complete K1 history.

This probe constructs and tests the direct `L1` resolution of both bridge
obligations identified in #1633:

1. An unrestricted integer scaled two-slice + precision-depth carrier
   `X_K1 = Z^5 x Z^5 x Z_(>=1)` equipped with a **Domain-and-Bank Reflection
   Bijection** `F_K1` that turns the injective scaling step
   `(U, W, k) -> (C U - 324^2 W, U, k+1)` and its congruence-guarded inverse
   into a **total, energy-conserving bijection on the entire unrestricted
   carrier**, producing exact autonomous bounce cycles up to a sharp budget
   horizon `N_max(b)` without external clocks or rational state storage.
2. An unconditional 3-adic quadratic precision-cost lower bound
   `sum_r P_n(r)^2 + D_n^2 >= (6/5) * 3^(8(n-1))` valid for **every** exact
   integer numerator/denominator representation `h_n = P_n / D_n`.
3. A 7-phase, 40-integer-coordinate coupled apparatus `F_bridge` joining the
   Hermitian source-holonomy loop over `O = Z[j]` with the scaled K1 carrier
   and an additive transverse metric readout `g_r(U, k)` that preserves
   Lorentzian signature `(-,+,+,+)` on all reachable K1 states while bypassing
   the `GL_4(Q(sqrt(5)))` fixed-form determinant square-class obstruction.

### 1.1 Cyclotomic and Hermitian definitions

Let `O = Z[j] = Z[X]/(1 + X + X^2 + X^3 + X^4)`, `K = Q(j)`, conjugation
`bar(j) = j^-1`, `phi = -j^2 - j^3`, `J = 1 + j^2`, and `O+ = Z[phi]`. Define:

```text
A = diag(J, phi),          A^-1 = diag(-j - j^2, phi - 1),
B(q) = [[1, q], [0, 1]],   B(q)^-1 = B(-q),
v = J/phi - 1 = -2 + j - j^2,
w = v bar(v) = 9 - 5 phi = 9 + 5 j^2 + 5 j^3,
rho(M)H = M H M^dagger,
H = [[a, c], [bar(c), d]],  a, d in O+, c in O,
H8 = (a0, a1, d0, d1, c0, c1, c2, c3) in Z^8,
a = a0 + a1 phi, d = d0 + d1 phi, c = c0 + c1 j + c2 j^2 + c3 j^3,
Q(s, q) = s^2 - s q + q^2,
N(H) = Tr_(K/Q)(tr(H^2))
     = 4 a0^2 + 4 a0 a1 + 6 a1^2 + 4 d0^2 + 4 d0 d1 + 6 d1^2
       + 2 [5 sum_(i=0)^3 c_i^2 - (sum_(i=0)^3 c_i)^2].
```

### 1.2 Scaled integer K1 carrier and Domain-and-Bank Reflection Bijection

Let `S` act cyclically on `Z^5` (`(S v)_r = v_((r+1) mod 5)`) and set:

```text
SCALE = 324,               SCALE_SQ = 324^2 = 104976,
C v_r = 460 v_r + 29 (v_(r+1) + v_(r-1)) + 65 (v_(r+2) + v_(r-2)).
```

The unrestricted scaled K1 state carrier is:

```text
X_K1 = Z^5 x Z^5 x Z_(>=1),     x_K1 = (U, W, k),
E_K1(U, W, k) = 1 + k + sum_(r=0)^4 U_r^2 + sum_(r=0)^4 W_r^2.
```

Define the forward domain `D_+ = X_K1`, the backward image domain

```text
D_- = {(U, W, k) in X_K1 : k >= 2 and C W - U == 0 (mod 104976)},
```

and the partial bare steps `T_K1^(+1) : D_+ -> D_-` and `T_K1^(-1) : D_- -> D_+`:

```text
T_K1^(+1)(U, W, k) = (C U - 104976 W, U, k + 1),
T_K1^(-1)(U, W, k) = (W, (C W - U) / 104976, k - 1).
```

On the funded carrier `Omega_K1 = X_K1 x Z_(>=0) x {-1, +1}`, define:

```text
F_K1(x, b, epsilon) = (y, c, epsilon)   if x in D_epsilon and c >= 0,
                      (x, b, -epsilon)  otherwise,
where y = T_K1^epsilon(x) and c = b + E_K1(x) - E_K1(y).
```

With the direction-flip involution `R(x, b, epsilon) = (x, b, -epsilon)`, the
inverse is `F_K1^-1 = R o F_K1 o R`.

For each canonical word `w = (w0, w1, w2, w3)` in the ten-word set `W` of
`DEF-K1-LINEAR-METRIC`:

```text
W = {0010, 0011, 0100, 0101, 0110, 1001, 1010, 1011, 1100, 1101},
u_t = (w_(t+2) - w_t) mod 5   for t in {0, 1},
U0^(w)_r = [r == u_0] + [r == (u_0 + 1) mod 5],
U1^(w)_r = [r == u_1] + [r == (u_1 + 1) mod 5],
x_1^(w) = (324 * U1^(w), U0^(w), 1) in X_K1.
```

The fixed current-state rational slice and additive transverse metric readers are:

```text
R_K1(U, W, k)_r = U_r / (2 * 324^k) in Q,
g_r(U, k) = diag(-1, 1 + R_K1(U, W, k)_r, 1 - R_K1(U, W, k)_r, 1).
```

### 1.3 Coupled 7-phase, 40-integer-coordinate bridge apparatus

The complete coupled state is

```text
X_bridge = (s, q, H, R, Z, U, W, k, p, b, epsilon),
s, q in Z, H, R, Z in Herm2(O), (U, W, k) in X_K1,
p in Z/7, b in Z_(>=0), epsilon in {-1, +1},
pack_bridge(X_bridge) = [s, q, p, b, epsilon, k, *U, *W, *H8, *R8, *Z8] (40 ints).
```

For `x = (s, q, H, R, Z, U, W, k, p)`, the positive integer account is:

```text
E_bridge(x) = 1 + Q(s, q) + N(H) + N(R) + N(Z)
              + k + sum_(r=0)^4 U_r^2 + sum_(r=0)^4 W_r^2.
```

The bare forward step `T_bridge^(+1)` increments `p` modulo 7 after executing
the operation for input phase `p`:

| Input phase `p` | Forward operation (`epsilon = +1`); unmentioned registers retained |
| --- | --- |
| 0 | `(s, q) <- (s - q, s)` |
| 1 | `H <- rho(B(-q)) H` |
| 2 | `H <- rho(A^-1) H` |
| 3 | `H <- rho(B(q)) H` |
| 4 | `H <- rho(A) H` |
| 5 | `Z <- Z + H - R` |
| 6 | `(U, W, k) <- (C U - 104976 W, U, k + 1)` |

For `epsilon = -1`, `T_bridge^(-1)` decrements `p` modulo 7 and applies the
inverse of that preceding phase's operation; when the preceding phase is `6`
(so input `p == 0` with `epsilon = -1`), the step is defined iff
`(U, W, k) in D_-`, in which case `(U, W, k) <- (W, (C W - U) / 104976, k - 1)`.
The funded bijection `F_bridge` applies the attempted step when defined and
affordable (`c = b + E_bridge(x) - E_bridge(y) >= 0`), and otherwise retains
`(x, b)` and flips `epsilon <- -epsilon`. Its inverse is
`F_bridge^-1 = R o F_bridge o R`.

### 1.4 Preregistered claims B1-B5

1. **B1 (Universal Domain-and-Bank Reflection Bijection):** `F_K1` and
   `F_bridge` are total bijections of their unrestricted carriers with exact
   inverses `R o F_K1 o R` and `R o F_bridge o R`, preserving `E_K1 + b` and
   `E_bridge + b` and nonnegative `b` across all accepted moves, bank refusals,
   and domain-congruence reflections. Every fixed total-cost shell is finite
   and every orbit is purely periodic.
2. **B2 (Exact Scaled K1 Horizon and Lossless Bounce Cycles):** For all ten
   canonical words `w in W` and every horizon `N >= 1`, the current-state
   reader `R_K1` on `x_n^(w) = (T_K1^(+1))^(n-1) x_1^(w)` equals the exact
   rational slice `h_n^(w)` of `DEF-K1-LINEAR-METRIC` with sum 1 and reduced
   common denominator `v_3(d_n) = 4(n-1)`. Starting at `(x_1^(w), B_sharp^(w)(N), +1)`
   with `B_sharp^(w)(N) = E_K1(x_N^(w)) - E_K1(x_1^(w))`, `F_K1` executes an
   exact periodic bounce cycle of length `2 N` reaching peak depth `k = N` with
   zero remaining bank and returning to the exact initial state at step `2 N`,
   whereas bank `B_sharp^(w)(N) - 1` refuses the step `N - 1 -> N` and closes a
   cycle of length `2 (N - 1)`.
3. **B3 (Unconditional 3-Adic Quadratic Precision Lower Bound):** For every
   `w in W`, every `n >= 1`, and **every** integer representation `h_n^(w) = P_n / D_n`
   with `(P_n, D_n) in Z^5 x Z_(>=1)`, `D_n >= d_n >= 3^(4(n-1))`,
   `max_r P_n(r) >= ceil(3^(4(n-1)) / 5)`, and
   `sum_(r=0)^4 P_n(r)^2 + D_n^2 >= (6/5) d_n^2 >= (6/5) * 3^(8(n-1))`.
4. **B4 (Additive Transverse Metric Readout):** On every reachable K1 state
   `x_n^(w)`, the additive transverse metric `g_r(U, k)` satisfies
   `-59/100 < h_n(r) < 99/100`, positive spatial eigenvalues `> 1/100`, and
   Lorentzian determinant `det g_r(U, k) = -(1 - h_n(r)^2) < -199/10000 < 0`
   without requiring `1 - h_n(r)^2` to be a square in `Q(sqrt(5))`.
5. **B5 (Coupled 7-Phase Source-Holonomy and K1 Precision Gate):** Starting from
   `s = a in {-1, +1}`, `q = 0`, `H = R = diag(0, 1)`, `Z = Z0 = [[1, j], [bar(j), 1]]`,
   `(U, W, k) = x_1^(0010)`, `p = 0`, `epsilon = +1`:
   - At bank `b = 772` (the sharp 6-phase Hermitian budget), both `a = -1` and
     `a = +1` complete phases `0..5` (writing `coeff_j(Z01) = 0` or `2`), and
     at phase `6` reflect (`epsilon : +1 -> -1`) because the remaining bank
     (`56` or `0`) is below the K1 step cost `Delta E_K1(1->2) = 36214830431`.
   - At the sharp 7-phase budgets `b = 36214831147` (`a = -1`) and
     `b = 36214831203` (`a = +1`), all 7 phases succeed, writing the source
     sign into `Z01` and advancing `(U, W, k)` to `x_2^(0010)` (`k = 2`), with
     exact step-by-step reversal back to the initial 40-integer state.

## 2. Code and independent method

`verify.py` is the accepted entry point using only Python's standard library.
It implements `O` via 4-coefficient polynomial reduction and cross-checks K1
against exact `fractions.Fraction` slices, then runs `breaker.py` in an
isolated subprocess (`python3 -I`) and compares the full JSON certificate.
`breaker.py` implements `O` via 5-coefficient cyclic arithmetic and computes
all scaled K1 and coupled-bridge quantities purely in integer arithmetic.

## 3. Finite audit specification

1. **Scaled K1 bijection window (`K1_STEP`):** Test 1440 states `(U, W, k, b, epsilon)`
   built from 20 base pairs `(U, W)` (the 10 canonical `x_1^(w)` states, the
   10 advanced `x_2^(w)` states in `D_-`, plus off-lattice controls in `X_K1 \ D_-`
   incorporated in the fixture list), `k in (1, 2, 3)`, `epsilon in (-1, 1)`,
   and 12 bank values `(0, 1, 10, 100, 36214830430, 36214830431, 36470284994, 36470284995, 36725739558, 36725739559, 36853466840, 36853466841)`.
   Verify `F_K1^-1(F_K1(S)) == S`, `F_K1(F_K1^-1(S)) == S`, and conservation of
   `E_K1 + b` and `b >= 0`.
2. **All-word bounce cycles and 3-adic precision bounds (`K1_BOUNCE` and `K1_BOUND`):**
   - For all 10 words `w in W` and horizons `N in (2, 3, 4)`, verify the exact
     sharp bank `B_sharp^(w)(N)`, the lossless period-`2 N` bounce trajectory
     at `b = B_sharp^(w)(N)`, and the period-`2 (N - 1)` refused bounce at
     `b = B_sharp^(w)(N) - 1`.
   - For all 10 words `w in W` and counters `n in 0..24` (250 slices), verify
     exact agreement between the integer scaled reader `R_K1(x_n^(w))` and the
     rational `DEF-K1-LINEAR-METRIC` recurrence, verify `v_3(d_n) = 4(n-1)` for
     `n >= 1`, verify the lower bound `5 * (sum_r P_n(r)^2 + d_n^2) >= 6 * d_n^2 >= 6 * 3^(8(n-1))`,
     and verify `-59/100 < h_n(r) < 99/100` and `det g_r < -199/10000 < 0`.
3. **Coupled 40-integer bridge audit (`BRIDGE_STEP` and `BRIDGE_EXPERIMENT`):**
   - Test 1120 full 40-integer states across all 7 phases `p in 0..6`, both
     directions `epsilon in (-1, 1)`, source/link pairs, Hermitian fixtures,
     and K1 lattice/off-lattice fixtures; verify both inverse compositions and
     `E_bridge + b` conservation.
   - Run the 8 paired 7-phase experiments for `a in (-1, +1)` across four bank
     settings (`772`, `36214831146`, `36214831147`, `36214831203`), verifying
     exact phase-6 reflection at `b = 772`, sharp 7-phase completion vs refusal
     at `36214831146 / 36214831147 / 36214831203`, occupied detector readout,
     and exact 7-step inverse restoration.
