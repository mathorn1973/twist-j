# Preregistration: P-INTEGER-RETAINED-PAIR-SOURCE-1

```text
probe_id:           P-INTEGER-RETAINED-PAIR-SOURCE-1
status:             NON-CANONICAL
claim_level:        L1
action_layer:       L1 -> L1 (exact cyclotomic trace-form and index-3/41 seam
                    bridge from (J, M) to (S, G, ell), universal division-free
                    integer pair involution on Z^81 x Z_{>0}, and 2-phase
                    positive-definite funded integer pair-source automaton;
                    no global decoder-uniqueness claim, no L1 -> L2 manifold
                    lift, no L1 -> L6 empirical/hardware lift, and no Public
                    Canon promotion)
canonical_effect:   NONE (does not edit canon/* and promotes no claim to T or C)
public_lock_issue:  https://github.com/mathorn1973/twist-j/issues/1698
predecessor_note:   C-JM-RETAINED-PAIR-SOURCE-N (PR #1681, head
                    08836040d7117c9315c0b24be33eb8829f068898, pin
                    760157f57495fb87059b3a8a8e7943be7d0793c1, issue #1680)
related_chain:      C-JM-RESULTANT-SEAM-41-N (merged PR #1671),
                    C-JM-PREPARATION-MEMORY-N (PR #1679, issue #1677),
                    C-JM-DECODER-CHAIN-PUBLICATION-N (PR #1697, issue #1696)
author:             A. M. Thorn <thorn@twistj.com>
```

## 1. Purpose and Scope

`C-JM-RETAINED-PAIR-SOURCE-N` (`PR #1681`, `issue #1680`) established in `notes/`
an `L1` rational Householder reflection `U_z = I_81 - (v_z r_z^T)/d_z` on
`Q^81 = Q^9 tensor Q^9` that prepares two identical anchored outputs
`(y_z tensor y_z)/A_z` with product density `rho_z tensor rho_z` from a
program-independent ready pair `e = e_0 tensor e_0`, swaps the prepared pair
into an occupied output port `P` while preserving the old port state and
correlations inside stock cell `B_n`, and generates the held-label block law
`Gamma_{2K} = sum_z pi_z rho_z^{tensor 2K}` over `K` rounds.

As recorded in `notes/C-JM-RETAINED-PAIR-SOURCE-N/RUN.md` and `PROOF.md`
Sections 1, 4, and 8 (and in our independent review at
`https://github.com/mathorn1973/twist-j/issues/1680#issuecomment-6302142233`):
1. `PR #1681` was executed on a single `aarch64` lane inside `notes/`, where
   ordinary repository CI does not run `verify.py` and no independent
   `breaker.py` implementation was included;
2. the coordinate carrier `S = {z in Z^8 : b_1 - b_2 - b_3 = 0 mod 3}`, trace
   metric `G = diag(5I_4 - 1_4 1_4^T, 4I_4)`, and resultant-41 seam form
   `ell = (1, 10, 18, 16, -1, -27, -32, -3)` were stated as supplied coordinate
   inputs; and
3. the gate `U_z = N_z / d_z` acted on fractional amplitude vectors in `Q^81`
   preserving only the flat probability norm `x^T L x = 1` (`e^T L e = t_z^T L t_z = 1`),
   with an unbounded counter `n` and without a universal program-independent
   integer state carrier or positive-definite integer energy/bank account `E + b`.

In full compliance with `POLICY.md` and the scope clarification in
`notes/C-JM-DECODER-CHAIN-PUBLICATION-N/SCOPE.md` (`#1696` / `#1697`) — namely,
that the JM reading and source chain is a declared `L1` existence and
consistency construction with explicit premises and neither requires nor claims
global decoder uniqueness or native-`U` laboratory hardware — this formal
two-architecture probe (`P-INTEGER-RETAINED-PAIR-SOURCE-1`) proves and audits
three closed `L1` results:

1. **Theorem 1 (Cyclotomic Trace-Form and Index-3/41 Seam Coordinate Bridge):**
   Starting from `J = 1 + j^2 in O_5 = Z[j]` (`Phi_5(j) = 0`, minimal polynomial
   `f(x) = x^4 - 3x^3 + 4x^2 - 2x + 1`) and `M = 1 + m + m^2 in Z[M] subset O_8 = Z[m]`
   (`Phi_8(m) = m^4 + 1 = 0`, minimal polynomial `g(x) = x^4 - 4x^3 + 8x^2 - 4x + 1`),
   the canonical field-trace pairing
   `b((a, beta), (a', beta')) = Tr_{K_5/Q}(a bar(a')) + Tr_{K_8/Q}(beta bar(beta'))`
   on `O_5 (+) O_8` in the basis `(1, j, j^2, j^3; 1, m, m^2, m^3)` has the exact
   Gram matrix `G = diag(5I_4 - 1_4 1_4^T, 4I_4)` (`det G = 125 * 256 = 32000`).
   The transition matrix `T_M` from `(1, M, M^2, M^3)` to `(1, m, m^2, m^3)` has
   `det T_M = -3` and image `T_M(Z^4) = Lambda_3 = {b in Z^4 : b_1 - b_2 - b_3 = 0 mod 3}`,
   giving `det G_S = 9 det G = 288000` and `det G_R = 41^2 det G_S = 484128000`.
   The unique roots `j = 10 mod 41` of `(Phi_5(x) = 0, 1 + x^2 = 19)` and
   `m = 27 mod 41` of `(x^4 + 1 = 0, 1 + x + x^2 = 19)` map the resultant-41
   homomorphism `u(a) - v(b) mod 41` to `ell . z = 0 mod 41` with
   `ell = (1, 10, 18, 16, -1, -27, -32, -3)`.

2. **Theorem 2 (Universal Division-Free Integer Pair Involution on `C = Z^81 x Z_{>0}`):**
   Every pair cell is represented by an 82-integer tuple `(X, D) in C = Z^81 x Z_{>0}`
   encoding the rational vector `X / D in Q^81` together with the positive integer
   scale content `m(X, D) = gcd(X_0, ..., X_80, D) in Z_{>0}`. For any program
   `z in Z^8` and bound `Q >= 8`, the integer map
   `U_hat_z(X, D) = (m(X, D) * (N_z X / g), m(X, D) * (d_z D / g))`
   with `g = gcd(N_z X, d_z D)` (and identity when `z notin B_Q`) is an exact
   involution (`U_hat_z(U_hat_z(X, D)) = (X, D)`) on the entire universal carrier
   `C`, preserves `(X^T L X) / D^2` and `m(X, D)`, and maps `(e, 1) <-> (w_z, A_z)`
   where `w_z = y_z tensor y_z` and `A_z = 1 + q(z)`.

3. **Theorem 3 (Positive-Definite Integer Energy & Bank Account `E + b` and Port-Independent Sharp Bank):**
   Equipping each cell with `E_cell(X, D) = X^T L X + D^2 in Z_{>0}` and the
   2-phase apparatus state `S = (z, z_arch, P, (B_0, ..., B_{K-1}), n, p, b, eps)`
   (`p in {0, 1}`, `b in Z_{>=0}`, `eps in {-1, +1}`) with
   `E(S) = 1 + q(z) + q(z_arch) + E_cell(P) + sum_{j=0}^{K-1} E_cell(B_j) + n^2 + p^2`,
   every constant-budget level set `{E(S) + b = C}` is finite, the funded step `F`
   is an exact bijection satisfying `F^{-1} = J_dir o F o J_dir` and conserving
   `E(S) + b`, and the sharp initial bank required to complete `K` pair rounds
   (`2K` outputs) from ready stock `B_0 = ... = B_{K-1} = (e, 1)` is
   `b_sharp(z, K) = 2K(A_z^2 - 1) + K^2 = 2K q(z)(q(z) + 2) + K^2`,
   strictly independent of the initial occupied output-port state `P_0 = (X_{P_0}, D_{P_0})`.

## 2. Six Frozen Preregistration Fields

1. **Question:**
   Can the coordinate carrier `(S, G, ell)` of `C-JM-RETAINED-PAIR-SOURCE-N` be
   derived by an explicit integral basis bridge from `(J, M)`, and can the
   retained-program pair source be realized on a universal program-independent
   integer carrier `C = Z^81 x Z_{>0}` as a 2-phase funded reversible automaton
   with positive-definite integer energy `E`, conserved total budget `E + b`,
   and port-independent sharp bank threshold `b_sharp(z, K) = 2K(A_z^2 - 1) + K^2`?

2. **Fixed Inputs and Domains:**
   - Cyclotomic polynomials `Phi_5(j) = 1 + j + j^2 + j^3 + j^4 = 0`,
     `Phi_8(m) = m^4 + 1 = 0`, elements `J = 1 + j^2`, `M = 1 + m + m^2`,
     minimal polynomials `f(x) = x^4 - 3x^3 + 4x^2 - 2x + 1` and
     `g(x) = x^4 - 4x^3 + 8x^2 - 4x + 1`.
   - Coordinate lattice `S = {z = (a_0..a_3, b_0..b_3) in Z^8 : b_1 - b_2 - b_3 = 0 mod 3}`,
     Gram matrix `G = diag(5I_4 - 1_4 1_4^T, 4I_4)`, quadratic form `q(z) = z^T G z`,
     bounded source family `B_Q = {z in S : 0 < q(z) <= Q}`, seam vector
     `ell = (1, 10, 18, 16, -1, -27, -32, -3)`.
   - Single-output metric `G_0 = diag(1, G)` on `Z^9`, pair metric `L = G_0 tensor G_0`
     on `Z^81`, reference vector `e_0 = (1, 0, ..., 0) in Z^9`, ready pair
     `e = e_0 tensor e_0 = (1, 0, ..., 0) in Z^81`.
   - Benchmark programs:
     - `e_1 = (1, 0, 0, 0, 0, 0, 0, 0)` (`q = 4, A = 5, d = 20`),
     - `v = (1, 0, 0, 0, -1, 0, 0, 0)` (`q = 8, A = 9, d = 72`),
     - `-v = (-1, 0, 0, 0, 1, 0, 0, 0)` (`q = 8, A = 9, d = 72`),
     - `z_dense = (1, -1, 1, -1, 1, 1, 1, 0)` (`q = 32, A = 33, d = 1056`),
     - `40v, 41v, 42v` (`q in {12800, 13448, 14112}`, `A in {12801, 13449, 14113}`).

3. **Exact Construction and Map Definitions:**
   - Transition matrices:
     ```text
     T_J = [[1, 1,  0, -2],
            [0, 0, -1, -2],
            [0, 1,  1,  0],
            [0, 0, -1, -3]],   det(T_J) = -1,

     T_M = [[1, 1, 0, -5],
            [0, 1, 2,  0],
            [0, 1, 3,  5],
            [0, 0, 2,  7]],    det(T_M) = -3.
     ```
   - Universal cell involution `U_hat_z` on `C = Z^81 x Z_{>0}`:
     For `z in B_Q`, `A_z = 1 + q(z)`, `d_z = A_z(A_z - 1)`, `w_z = y_z tensor y_z`,
     `v_z = A_z e - w_z`, `r_z = L v_z`, `N_z = d_z I_81 - v_z r_z^T`:
     `Y = N_z X`, `M = d_z D`, `g = gcd(Y_0, ..., Y_80, M)`,
     `m = gcd(X_0, ..., X_80, D)`, and `U_hat_z(X, D) = (m * (Y // g), m * (M // g))`.
     For `z notin B_Q`, `U_hat_z(X, D) = (X, D)`.
   - Core 2-phase transition `T_eps` on `u = (z, z_arch, P, B, n, p)`:
     - Forward (`eps = +1`):
       - `p = 0`: if `z in B_Q` and `0 <= n < K`, replace `B_n` by `U_hat_z(B_n)`;
         set `(n', p') = (n, 1)`.
       - `p = 1`: if `z in B_Q` and `0 <= n < K`, swap `(P, B_n) -> (B_n, P)`;
         set `(n', p') = (n + 1, 0)`.
     - Backward (`eps = -1`):
       - `p = 1`: if `z in B_Q` and `0 <= n < K`, replace `B_n` by `U_hat_z(B_n)`;
         set `(n', p') = (n, 0)`.
       - `p = 0`: if `z in B_Q` and `0 <= n - 1 < K`, swap `(P, B_{n-1}) -> (B_{n-1}, P)`;
         set `(n', p') = (n - 1, 1)`.
   - Funded step `F(u, b, eps)`:
     Let `u' = T_eps(u)` and `b' = b + E(u) - E(u')`. If `b' >= 0`, return
     `(u', b', eps)`; if `b' < 0`, return `(u, b, -eps)`.

4. **Analytical Predictions and Exact Certificate Values:**
   - `det(G_5) = 125`, `det(G_8) = 256`, `det(G) = 32000`, `det(G_S) = 288000`,
     `det(G_R) = 484128000`, `Res(f, g) = 41`, unique mod-41 root lift `(j, m) = (10, 27)`.
   - Ternary vectors in `S`: `2187` of `6561`; admitted ternary programs in `B_32`: `2162`.
   - Cell energy of ready pair: `E_cell(e, 1) = 2`; cell energy of prepared pair:
     `E_cell(w_z, A_z) = 2 * A_z^2`; preparation jump: `Delta E_prep(z) = 2 * (A_z^2 - 1)`.
   - 7-point energy difference prefixes `E_t - E_0` (`t = 0..6`) for `K = 3`:
     - `z = e_1` (`A = 5`): `0, 49, 49, 98, 100, 149, 153` (`b_sharp = 153`),
     - `z = v` (`A = 9`): `0, 161, 161, 322, 324, 485, 489` (`b_sharp = 489`),
     - `z = z_dense` (`A = 33`): `0, 2177, 2177, 4354, 4356, 6533, 6537` (`b_sharp = 6537`).
   - Underfunded `K = 3` bank `b_0 = b_sharp(z, 3) - 1`: advances `5` steps to
     `(n = 2, p = 1)` with remaining bank `3`, reflects on step `6` (`Delta E = 4 > 3`),
     and unwinds in `5` steps back to the exact initial state with bank `b_0`.
   - Dirty-stock energy release for `B_0 = (w_v, 9)`: `Delta E_{0,0}^{dirty}(v) = -159`
     (bank increases by `159` and `B_0` returns to `(e, 1)`).
   - Opposite-seam collision (`t in {40, 41, 42}`) reference-pair probability gap:
     `15936/1210262180216419`, with 1-round sharp banks
     `327731201, 361751201, 398353537` and 91-round (`182`-output) sharp banks
     `29823547481, 32919367481, 36250180057`.

5. **Falsifiers:**
   - `FALSIFIER=CYCLOTOMIC_BRIDGE`: any mismatch in `f(J) = 0`, `g(M) = 0`,
     `Res(f, g) = 41`, `G = diag(5I_4 - 1_4 1_4^T, 4I_4)`, `det(G) = 32000`,
     `det(G_S) = 288000`, `det(G_R) = 484128000`, `T_M(Z^4) = Lambda_3`, or
     `u(a) - v(b) = ell . z mod 41` across all `2187` ternary vectors in `S`.
   - `FALSIFIER=PAIR_INVOLUTION`: any violation of `U_hat_z(U_hat_z(X, D)) = (X, D)`,
     `m(U_hat_z(X, D)) = m(X, D)`, `((X')^T L X') / (D')^2 = (X^T L X) / D^2`,
     `U_hat_z(e, 1) = (w_z, A_z)`, `N_z^2 = d_z^2 I_81`, `N_z^T L N_z = d_z^2 L`,
     or product-density factorization `(w_z w_z^T L)/A_z^2 = rho_z tensor rho_z`.
   - `FALSIFIER=FUNDED_AUTOMATON`: any violation of `F^{-1} = J_dir o F o J_dir`,
     `E(F(S)) + b(F(S)) = E(S) + b(S)`, port-independence of `b_sharp(z, K) = 2K(A_z^2 - 1) + K^2`
     across all `81` basis ports and scaled/correlated ports, exact `K = 3` sharp
     and underfunded bounce trajectories, dirty-stock release, or program-capture
     cost `Delta E_cap(x; z, 0) = q(x)`.
   - `FALSIFIER=BREAKER_MISMATCH`: any difference between the output of `verify.py`
     and the independent implementation `breaker.py`.

6. **Verification Protocol:**
   - Freeze `PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`, `breaker.py`, and
     `FROZEN.sha256` on `probe/P-INTEGER-RETAINED-PAIR-SOURCE-1`, push to `origin`,
     and record the public pre-execution readback receipt on issue `#1698` before
     any execution of `verify.py` or `breaker.py`.
   - Execute `python3 -I probes/P-INTEGER-RETAINED-PAIR-SOURCE-1/verify.py` locally,
     capture exact stdout as `EXPECTED.txt`, record neutral execution metadata in
     `RUN.md` and `RESULT.md`, and verify two-architecture (`x86_64` and `aarch64`)
     replay in GitHub Actions.
