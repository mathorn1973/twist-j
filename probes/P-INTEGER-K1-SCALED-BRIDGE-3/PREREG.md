# Preregistration: P-INTEGER-K1-SCALED-BRIDGE-3

```text
probe_id:           P-INTEGER-K1-SCALED-BRIDGE-3
status:             NON-CANONICAL
claim_level:        L1
action_layer:       L1 -> L1 (exact discrete state, scaled integer K1 carrier,
                    domain-and-bank reflection bijection, coupled 7-phase
                    source-holonomy-K1 apparatus, and additive transverse metric
                    readout; no L1 -> L2 manifold lift, no L1 -> L6 empirical
                    lift, and no Public Canon promotion)
canonical_effect:   NONE (does not edit canon/* and promotes no claim to T or C)
public_lock_issue:  https://github.com/mathorn1973/twist-j/issues/1635
predecessor_probe:  P-INTEGER-SOURCE-HOLONOMY-1 (PR #1633, issue #1632)
abandoned_pins:     P-INTEGER-K1-SCALED-BRIDGE-1 (pinned at
                    632f59e97c169abe937e00a6d92642f32378d767, closed ABANDONED
                    at 1d7085545f26563ea4ebfd5faf0ea9fad10a9cd7, PR #1636);
                    P-INTEGER-K1-SCALED-BRIDGE-2 (pinned at
                    fd4e5a2734fd99d94480b6bef30d2c657f6debc3, closed ABANDONED
                    at 0847cf6cc8fe0af0d0fde9e580184a8d40acff2d, PR #1637)
author:             A. M. Thorn <thorn@twistj.com>
```

## 0. Abandoned Predecessor Disclosure

This probe is the fresh retargeted successor to:
- `P-INTEGER-K1-SCALED-BRIDGE-1` (pinned at `632f59e97c169abe937e00a6d92642f32378d767`
  and closed with `Status: ABANDONED` at `1d7085545f26563ea4ebfd5faf0ea9fad10a9cd7`
  on `probe/P-INTEGER-K1-SCALED-BRIDGE-1`, PR `#1636`), which exited nonzero on
  line 456 due to an arithmetic sum defect (`1512 + 432 + 240 = 2184 != 3528`) in
  the `check_k1_exhaust()` state-count assertion before any stdout was emitted; and
- `P-INTEGER-K1-SCALED-BRIDGE-2` (pinned at `fd4e5a2734fd99d94480b6bef30d2c657f6debc3`
  and closed with `Status: ABANDONED` at `0847cf6cc8fe0af0d0fde9e580184a8d40acff2d`
  on `probe/P-INTEGER-K1-SCALED-BRIDGE-2`, PR `#1637`), where `check_pre_pin_integrity()`,
  `check_k1_exhaust()` (`2,184` states), and `check_k1_words_and_precision()`
  passed, after which `verify.py` exited nonzero on line 552 inside
  `check_k1_bounce_cycles()` before any stdout was emitted due to an initial-slice
  helper formula defect in `k1_init_U0_U1(word)` (`(b0+2*b1+4*b2+3*b3)%5` and
  `(b0+b1+b2+b3)%5` instead of the `DEF-K1-LINEAR-METRIC` formula
  `u_t = (bits[t + 2] - bits[t]) % 5` on the ten canonical words
  `0010, 0011, 0100, 0101, 0110, 1001, 1010, 1011, 1100, 1101`).

In accordance with `POLICY.md` Section 3 (Abandoned pins), both predecessor
identifiers are permanently consumed and are not reused, repaired, or resumed.

## 1. Purpose and Relation to `P-INTEGER-SOURCE-HOLONOMY-1` (`#1633`)

`P-INTEGER-SOURCE-HOLONOMY-1` (`PR #1633`) established an `L1` reversible
6-phase Hermitian source-holonomy apparatus over `O = Z[j]` (`29` integer
coordinates) and proved three exact structural boundaries:

1. **K1 3-adic denominator growth (`Claim I5` of `#1633`):** for every word
   `w in W` (`|W| = 10`) and every step `n >= 1` of `DEF-K1-LINEAR-METRIC`,
   the least positive common denominator `d_n` of the reduced entries of
   `h_n in Q^5` satisfies `v_3(d_n) = 4(n - 1)`. Consequently, no fixed-denominator
   decoding `h = P / D` and no current-state rational reader on a fixed
   `E + b` shell can represent an infinite exact K1 trajectory.
2. **No fixed 4D `Z^4` invariant lattice (`Claim I6` of `#1633`):** `rho(A)`
   has non-integer real trace `2 + phi` on the principal 4D subspace, ruling out
   rank-4 `Z`-lattices while leaving the rank-8 carrier `(Z[phi])^2 x Z[j]` open.
3. **No fixed-form `GL_4(Q(sqrt(5)))` frame pullback (`Claim I7` of `#1633`):**
   `det g_(1/2) / det g_0 = 3/4` is not a square in `Q(sqrt(5))`, ruling out
   generating the K1 transverse metric `g(h) = diag(-1, 1+h, 1-h, 1)` from a
   single constant quadratic form by frame conjugation over `Q(sqrt(5))`.

This follow-up probe `P-INTEGER-K1-SCALED-BRIDGE-3` resolves the two exact `L1`
constructive obligations exposed by `#1633`:

- **Obligation 1 (Variable-Precision Integer K1 Carrier + Domain-and-Bank
  Reflection Bijection):** Embed the exact K1 recurrence into an explicit
  integer carrier `X_K1 = Z^5 x Z^5 x Z_(>=1)` that stores the precision
  counter `k >= 1` and scaled numerators `(U, W)` in the state and its integer
  account `E_K1(U, W, k) = 1 + k + ||U||_2^2 + ||W||_2^2`. Prove that the
  **Domain-and-Bank Reflection** rule `F_K1` is a **total bijection on the
  entire unrestricted carrier** `X_K1 x Z_(>=0) x {-1, +1}` with exact inverse
  `F_K1^-1 = R_K1 o F_K1 o R_K1`, that any finite bank `B >= 0` produces a
  lossless periodic bounce cycle between `k = 1` and a sharp horizon `k = N`
  determined by `B_sharp^(w)(N) = E_K1(x_N^(w)) - E_K1(x_1^(w))`, and that
  every integer numerator/denominator encoding `(P_n, D_n)` of `h_n = P_n / D_n`
  satisfies the unconditional quadratic precision lower bound
  `sum_(r=0)^4 P_n(r)^2 + D_n^2 >= (6/5) * d_n^2 >= (6/5) * 3^(8(n-1))`.
- **Obligation 2 (Additive Transverse Metric Readout + Coupled 7-Phase,
  40-Integer Source-Holonomy-K1 Apparatus):** Couple the 6-phase Hermitian
  source-holonomy loop `(s, q, H, R, Z)` with the scaled K1 state `(U, W, k)`
  in a 7-phase, 40-integer-coordinate bijection `F_bridge` whose additive
  transverse metric readout
  `g_r(U, k) = eta + diag(0, U_r / (2 * 324^k), -U_r / (2 * 324^k), 0)`
  bypasses the `GL_4(Q(sqrt(5)))` single-form congruence obstruction while
  preserving `det g_r(U, k) < -199/10000 < 0` on every reachable K1 state.

## 2. Six Frozen Preregistration Fields

### 2.1 Equation

#### A. Scaled Integer K1 Carrier and Bare Partial Bijection

Let `C` be the symmetric `5 x 5` circulant integer operator of
`DEF-K1-LINEAR-METRIC` on `Z^5`:

```text
(C V)_r = 460 V_r + 29 (V_(r-1) + V_(r+1)) + 65 (V_(r-2) + V_(r+2)),   r in Z/5,
```

and let `324 = 2^2 * 3^4` and `324^2 = 104976`.

Define the scaled integer K1 core carrier:

```text
X_K1 = Z^5 x Z^5 x Z_(>=1) = { (U, W, k) : U in Z^5, W in Z^5, k in Z, k >= 1 }
```

(`11` integer coordinates). Define the forward domain `D_+ = X_K1` and backward
divisibility domain:

```text
D_- = { (U, W, k) in X_K1 : k >= 2  and  C W - U == 0 (mod 104976) }.
```

The bare forward and backward K1 maps `T_K1^(+1) : D_+ -> D_-` and
`T_K1^(-1) : D_- -> D_+` are:

```text
T_K1^(+1)(U, W, k) = (C U - 104976 W, U, k + 1),
T_K1^(-1)(U, W, k) = (W, (C W - U) / 104976, k - 1).
```

For each of the 10 canonical K1 words
`w in W = {0010, 0011, 0100, 0101, 0110, 1001, 1010, 1011, 1100, 1101}` with
bits `(b_0, b_1, b_2, b_3)`, `u_t = (b_(t+2) - b_t) mod 5` for `t in {0, 1}`,
and initial rational slices `h_t^(w)(r) = (delta_(r, u_t) + delta_(r, u_t + 1)) / 2`,
define the integer initial vectors `U_0^(w) = 2 h_0^(w) in {0, 1}^5` and
`U_1^(w) = 2 h_1^(w) in {0, 1}^5`, the initial scaled K1 state:

```text
x_1^(w) = (324 * U_1^(w), U_0^(w), 1) in X_K1,
```

and `x_n^(w) = (T_K1^(+1))^(n-1)(x_1^(w)) = (U_n^(w), W_n^(w), n)` for `n >= 1`.
The current-state rational reader `R_K1 : X_K1 -> Q^5` is:

```text
R_K1(U, W, k) = U / (2 * 324^k).
```

#### B. Positive Integer K1 Account and Total Domain-and-Bank Reflection Bijection

Define the positive integer K1 cost functional `E_K1 : X_K1 -> Z_(>=2)`:

```text
E_K1(U, W, k) = 1 + k + sum_(r=0)^4 U_r^2 + sum_(r=0)^4 W_r^2.
```

On the funded K1 state space `Omega_K1 = X_K1 x Z_(>=0) x {-1, +1}` (`13`
integer coordinates `(U, W, k, b, epsilon)`), define the direction-flip
involution `R_K1(x, b, epsilon) = (x, b, -epsilon)` and the **Domain-and-Bank
Reflection** step `F_K1 : Omega_K1 -> Omega_K1`:

```text
F_K1(x, b, epsilon) = (T_K1^epsilon(x), b + E_K1(x) - E_K1(T_K1^epsilon(x)), epsilon)
                      if x in D_epsilon and b + E_K1(x) - E_K1(T_K1^epsilon(x)) >= 0,
                    = (x, b, -epsilon)
                      otherwise (either x notin D_epsilon or bank < 0).
```

For each word `w in W` and target horizon `N >= 1`, define the sharp horizon
bank:

```text
B_sharp^(w)(N) = E_K1(x_N^(w)) - E_K1(x_1^(w)).
```

#### C. Unconditional 3-Adic Quadratic Precision Lower Bound

For any integer representation `(P_n, D_n) in Z^5 x Z_(>=1)` of the exact K1
slice `h_n^(w) = P_n / D_n` (`w in W, n >= 1`), let `d_n` be the least positive
common denominator of the reduced entries of `h_n^(w)`. Then `d_n | D_n`,
`v_3(d_n) = 4(n - 1)`, `sum_(r=0)^4 P_n(r) = D_n`, and by Cauchy-Schwarz on
`R^5`:

```text
sum_(r=0)^4 P_n(r)^2 + D_n^2 >= (6/5) * D_n^2 >= (6/5) * d_n^2 >= (6/5) * 3^(8(n-1)).
```

#### D. Additive Transverse Metric Readout

For any state `(U, W, k) in X_K1` and site `r in Z/5`, define the additive
transverse metric perturbation on `R^4` around `eta = diag(-1, 1, 1, 1)`:

```text
g_r(U, k) = eta + diag(0, h_k(r), -h_k(r), 0) = diag(-1, 1 + h_k(r), 1 - h_k(r), 1),
where h_k(r) = U_r / (2 * 324^k).
```

On every reachable K1 state `x_k^(w)` (`w in W, k >= 1`), `1 + h_k(r) > 41/100`,
`1 - h_k(r) > 1/100`, and `det g_r(U, k) = -(1 - h_k(r)^2) < -199/10000 < 0`.

#### E. Coupled 7-Phase, 40-Integer Source-Holonomy-K1 Apparatus

Let `O = Z[j]` (`1 + j + j^2 + j^3 + j^4 = 0`), `phi = -j^2 - j^3`, `J = 1 + j^2`,
`A = diag(J, phi)`, `B(q) = [[1, q], [0, 1]]`, and let `H_2(O)` be the rank-8
Hermitian `Z`-lattice with positive-definite quadratic norm:

```text
N(H) = Tr_(Q(j)/Q)(tr(H^2))
     = 4 a0^2 + 4 a0 a1 + 6 a1^2 + 4 d0^2 + 4 d0 d1 + 6 d1^2
       + 10 (c0^2 + c1^2 + c2^2 + c3^2) - 2 (c0 + c1 + c2 + c3)^2.
```

Define the coupled 40-integer funded carrier:

```text
X_bridge = { (s, q, H, R, Z, U, W, k, p, b, epsilon) :
             s, q in Z, H, R, Z in H_2(O), (U, W, k) in X_K1,
             p in Z/7, b in Z_(>=0), epsilon in {-1, +1} }
```

(`2 + 8 + 8 + 8 + 5 + 5 + 1 + 1 + 1 + 1 = 40` integers), with total core cost:

```text
E_bridge(s, q, H, R, Z, U, W, k) =
    1 + s^2 - s q + q^2 + N(H) + N(R) + N(Z) + k + sum_(r=0)^4 U_r^2 + sum_(r=0)^4 W_r^2.
```

The bare 7-phase forward step `T_bridge^(+1)` executes:
- Phases `p = 0, 1, 2, 3, 4, 5`: the exact 6-phase source-holonomy steps of
  `#1633` on `(s, q, H, R, Z)` while retaining `(U, W, k)` and advancing
  `p -> p + 1 (mod 7)`:
  - `p = 0`: `(s, q) -> (s - q, s)`
  - `p = 1`: `H -> B(-q) H B(-q)^dagger`
  - `p = 2`: `H -> A^-1 H (A^-1)^dagger`
  - `p = 3`: `H -> B(q) H B(q)^dagger`
  - `p = 4`: `H -> A H A^dagger`
  - `p = 5`: `Z -> Z + (H - R)`
- Phase `p = 6`: retains `(s, q, H, R, Z)` and advances `(U, W, k) -> T_K1^(+1)(U, W, k)`,
  `p : 6 -> 0`.

The bare backward step `T_bridge^(-1)` from phase `p` is defined whenever
`p != 0` or `(p == 0 and (U, W, k) in D_-)`, applying the exact inverse of
phase `(p - 1) mod 7`. Under the Domain-and-Bank Reflection rule `F_bridge` and
direction flip `R_bridge`, `F_bridge` is a total bijection on `X_bridge` with
exact inverse `F_bridge^-1 = R_bridge o F_bridge o R_bridge`.

### 2.2 Code

- Primary verifier: `probes/P-INTEGER-K1-SCALED-BRIDGE-3/verify.py`
  (uses 4-coefficient polynomial representation `Z[j]` mod `1 + j + j^2 + j^3 + j^4`,
  explicit `2 x 2` matrix conjugation, and `fractions.Fraction` rational K1
  cross-checks, then invokes `breaker.py` in a clean subprocess and compares all
  core certificate lines byte for byte).
- Independent breaker: `probes/P-INTEGER-K1-SCALED-BRIDGE-3/breaker.py`
  (uses 5-coefficient cyclic representation `Z[j^0..j^4]` modulo `(1,1,1,1,1)`,
  direct diagonal/triangular Hermitian transport formulas, and pure integer
  scaled K1 recurrences without `fractions.Fraction`).
- Frozen hash manifest: `probes/P-INTEGER-K1-SCALED-BRIDGE-3/FROZEN.sha256`
  binding `PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`, and `breaker.py`
  prior to any execution of `verify.py` or `breaker.py`.

### 2.3 Carrier / Data

Purely mathematical and finite-exhaust audit on exact integer tuples:
1. **K1 reflection bijection finite test box (`2,184` states):**
   - `1,512` states `(U, W, k, b, epsilon)` with
     `U, W in {(-1,0,0,0,0), (0,0,0,0,0), (1,0,0,0,0), (1,-1,0,0,0), (0,1,1,0,0), (324,324,0,0,0)}`,
     `k in {1, 2, 3}`, `b in {0, 1, 2, 10, 100, 209954, 209955}`,
     `epsilon in {-1, +1}`;
   - `432` states with `U_0, U_1, W_0 in {-1, 0, 1}` (other entries `0`),
     `k in {1, 2}`, `b in {0, 1, 2, 5}`, `epsilon in {-1, +1}`;
   - `240` reachable K1 word-trajectory states `(x_n^(w), b, epsilon)` for all
     10 words `w in W`, `n in {1, 2, 3, 4}`, `b in {0, 1, B_sharp^(0010)(2)}`,
     `epsilon in {-1, +1}`.
2. **Exact scaled K1 trajectories across all 10 words and `1 <= n <= 24` (`240`
   state steps, `250` slices including `n = 0`):** verifying `R_K1(x_n^(w)) == h_n^(w)`,
   `T_K1^(-1)(x_(n+1)^(w)) == x_n^(w)`, `v_3(d_n) == 4(n - 1)`,
   `v_3(gcd(U_n^(w), 2 * 324^n)) == 0`, the quadratic precision bound
   `5 * (sum_r P_n(r)^2 + D_n^2) >= 6 * d_n^2 >= 6 * 3^(8(n-1))`, and the
   transverse metric Lorentzian bounds at all 5 sites (`1,250` site-step checks).
3. **Lossless periodic bounce cycles (`60` full cycles):** for all 10 words
   `w in W` and horizons `N in {2, 3, 4}`, verifying exact period `2N` at the
   sharp bank `B_sharp^(w)(N)` and exact period `2(N - 1)` at the underfunded
   bank `B_sharp^(w)(N) - 1`.
4. **Coupled 7-phase, 40-integer bridge test box (`4,032` states) and 8 full
   forward/reverse source-holonomy-K1 trajectories** starting from
   `s in {-1, +1}`, `q = 0`, `H = R = diag(0, 1)`, `Z = Z_0 = [[1, j], [bar(j), 1]]`,
   `(U, W, k) = x_1^(0010)` across banks `772`, `36214831147` (sharp for `s = -1`),
   `36214831203` (sharp for `s = +1`), and `sharp - 1` (`36214831146` and
   `36214831202`).

### 2.4 Systematics and Scope Boundaries

1. **Chosen `L1` coupling and cost functional:** Both `E_K1` and `E_bridge` are
   declared positive integer accounting functionals on `L1`, and the 7-phase
   schedule couples the Hermitian source-holonomy loop and the scaled K1 step
   through the shared bank `b`. Neither is claimed to be a canonically forced
   uniqueness theorem of `DEF-EVOLUTION` or a derived physical stress-energy
   backreaction law.
2. **Horizon growth with bank:** Because K1 precision grows as `3^(4(n-1))` and
   `||U_n^(w)||_2^2 >= (4/5) * 324^(2n)`, any finite bank `B` reaches a finite
   maximum horizon `N(B)` and then reflects reversibly back to `k = 1` in a
   closed cycle of length `2 N(B)`. Unbounded forward K1 evolution requires an
   unbounded initial bank or an external precision reservoir.
3. **Additive transverse metric vs frame pullback:** Representing `g_r(U, k)`
   as an additive perturbation of `eta = diag(-1, 1, 1, 1)` resolves the `L1`
   readout question without contradicting `#1633`'s `Claim I7`, which specifically
   forbids single-form `GL_4(Q(sqrt(5)))` frame congruence.

### 2.5 Failure Threshold (Falsifiers)

The probe fails (`RESULT=FAIL` or nonzero exit) if any of the following occurs:

- **F1 (Pre-pin integrity):** Any hash in `FROZEN.sha256` fails to match
  `PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`, or `breaker.py`.
- **F2 (K1 reflection bijection or energy conservation):** Any of the `2,184`
  tested K1 states fails `(R_K1 o F_K1 o R_K1)(F_K1(S)) == S`,
  `F_K1((R_K1 o F_K1 o R_K1)(S)) == S`, or `E_K1 + b` conservation.
- **F3 (Scaled K1 exactness or quadratic precision bound):** For any word
  `w in W` and step `1 <= n <= 24`, `R_K1(x_n^(w)) != h_n^(w)`,
  `T_K1^(-1)(x_(n+1)^(w)) != x_n^(w)`, `v_3(d_n) != 4(n - 1)`, or
  `5 * (sum_r P_n(r)^2 + D_n^2) < 6 * d_n^2`.
- **F4 (Sharp bounce cycle failure):** For any `w in W` and `N in {2, 3, 4}`,
  the orbit from `(x_1^(w), B_sharp^(w)(N), +1)` fails to reach `k = N` with
  bank `0` at step `N - 1`, fails to reflect at `k = N` on step `N`, fails to
  return to `(x_1^(w), B_sharp^(w)(N), +1)` with exact minimal period `2N`, or
  the underfunded bank `B_sharp^(w)(N) - 1` fails to reflect at `k = N - 1`
  with exact minimal period `2(N - 1)`.
- **F5 (Transverse metric Lorentzian signature):** Any reachable K1 site/step
  for `w in W`, `0 <= n <= 24`, `r in Z/5` fails `1 + h_n(r) > 1/100`,
  `1 - h_n(r) > 1/100`, or `det g_r(U_n, n) < -199/10000`.
- **F6 (Coupled 7-phase bridge bijection or sharp bank mismatch):** Any of the
  `4,032` coupled bridge states fails bijectivity or `E_bridge + b` conservation,
  or the trajectories for `s in {-1, +1}` at `x_1^(0010)` fail to match the
  predicted prefix energies
  `E_bridge(-1) = (209981, 209981, 209993, 210013, 210097, 210327, 210697, 36215041128)`
  (sharp bank `36214831147`) and
  `E_bridge(+1) = (209981, 209981, 209993, 210013, 210097, 210327, 210753, 36215041184)`
  (sharp bank `36214831203`), or fail exact occupied-detector readout and
  step-by-step inverse reconstruction.
- **F7 (Independent breaker disagreement):** `breaker.py` fails to produce the
  exact core certificate lines emitted by `verify.py`.

### 2.6 Action Layer

`L1 -> L1` only. All claims (`B1` through `B5` in `PROOF.md`) are `NON-CANONICAL`
at `L1`. No `L1 -> L2` manifold/Einstein lift (`GATE-L1-L2-MANIFOLD`,
`O-G-EINSTEIN-SOURCE-LAW-1`) is claimed.
