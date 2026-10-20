# Result: P-INTEGER-RETAINED-PAIR-SOURCE-1

Status: NON-CANONICAL (`L1`, `RESULT=PASS`)

Public lock: `#1698`.
Predecessor note: `C-JM-RETAINED-PAIR-SOURCE-N` (`PR #1681`, head `08836040d7117c9315c0b24be33eb8829f068898`, pin `760157f57495fb87059b3a8a8e7943be7d0793c1`, issue `#1680`).

Immutable pin commit: `32bd52e9d76bbd7b9bfe7588af78e69cb7bbf331`.
Verifier SHA-256: `83ef6f0489ef0d67e2b8c16c796a59d52d18583ad854171749c20b3a1896ad98`.
Breaker SHA-256: `7c6a901b629704a7c766e899a7760f83a680fcc7cc6b55fafd99bfe05db59db6`.
Frozen manifest SHA-256: `529b278c5c355f57758dbcaaee0b9cc96a49f1a74cc60f65b2b356b7ec8abe9f`.
Expected stdout SHA-256: `196e18b6f89b3aaa36d119bed8b1b5c80e97ec89ffa51f25d845f4102e7fcd8d` (`1562` bytes, `24` lines).

## 1. Fired Falsifiers

`NONE` (`CYCLOTOMIC_BRIDGE`, `PAIR_INVOLUTION`, `FUNDED_AUTOMATON`, and `BREAKER_MISMATCH` all passed).

## 2. Summary of Earned `L1` Results

1. **Cyclotomic Trace-Form and Index-3/41 Seam Coordinate Bridge (`Theorem 1`):**
   Starting from `J = 1 + j^2 in O_5 = Z[j]` (`f(J) = 0`) and `M = 1 + m + m^2 in Z[M] subset O_8 = Z[m]` (`g(M) = 0`), the canonical field-trace form on `O_5 (+) O_8` has Gram matrix `G = diag(5I_4 - 1_4 1_4^T, 4I_4)` with `det(G_5) = 125`, `det(G_8) = 256`, and `det(G) = 32000`. The power-basis transition matrices `T_J` (`det(T_J) = -1`) and `T_M` (`det(T_M) = -3`) map `A x B = Z[J] x Z[M]` onto `S_cyc = Z^4 x Lambda_3` (`Lambda_3 = {b in Z^4 : b_1 - b_2 - b_3 = 0 mod 3}`), with `det(G_S) = 288000` and `det(G_R) = 41^2 det(G_S) = 484128000`. Under the unique mod-41 root lifts `j = 10 mod 41` and `m = 27 mod 41` of `J = 19, M = 19 mod 41`, the resultant-41 evaluation difference `u(a) - v(b) mod 41` equals `ell . z mod 41` (`ell = (1, 10, 18, 16, -1, -27, -32, -3)`), verified across all `2,187` ternary vectors in `S_cyc` (`2,162` admitted in `B_32`).

2. **Universal Division-Free Integer Pair Involution on `C = Z^81 x Z_{>0}` (`Theorem 2`):**
   On the universal integer cell space `C = Z^81 x Z_{>0}` with scale content `m(X, D) = gcd(X_0, ..., X_80, D) in Z_{>0}`, the integer pair map `U_hat_z(X, D)` is an exact involution (`U_hat_z(U_hat_z(X, D)) = (X, D)`) for every program `z in Z^8`, preserves `m(X, D)` and the rational invariant `(X^T L X) / D^2`, and maps the ready pair `(e, 1) <-> (w_z, A_z)` with `E_cell(e, 1) = 2` and `E_cell(w_z, A_z) = 2 A_z^2`. Audited across all `2,162` admitted ternary programs, `7` full `81 x 81` integer certificate matrices (`q in {4, 8, 8, 32, 12800, 13448, 14112}`), and `600` cell-program pairs (`pair_involution_sha256 = 56b243ff02cb8326189fd9ed462053141114b035dbcdb4e04884e7055f636b2d`).

3. **2-Phase Funded Integer Automaton and Port-Independent Sharp Bank (`Theorem 3`):**
   Equipping the retained-pair source with the positive-definite integer energy functional `E(S) = 1 + q(z) + q(z_arch) + E_cell(P) + sum_{j=0}^{K-1} E_cell(B_j) + n^2 + p^2` and bank `b in Z_{>=0}` yields finite constant-budget level sets, exact bijectivity `F^{-1} = J_dir o F o J_dir`, and strict conservation of `E + b` (audited across `2,592` states: `1,977` accepted steps and `615` bank reflections). Because `SWAP_{P, B_r}` preserves `E_cell(P) + E_cell(B_r)` identically for every occupied port state `P_0`, the sharp initial bank required to complete `K` pair rounds (`2K` fresh outputs) is:
   ```text
   b_sharp(z, K) = 2K * (A_z^2 - 1) + K^2 = 2K * q(z) * (q(z) + 2) + K^2,
   ```
   strictly independent of `P_0` and `z_arch`:
   - Verified across all `81` basis ports and `9` scaled ports at `z = v, K = 1` (`b_sharp(v, 1) = 161`).
   - For `K = 3` (`6` outputs), the 7-point energy difference prefixes `E_t - E_0` are `(0, 49, 49, 98, 100, 149, 153)` for `e_1`, `(0, 161, 161, 322, 324, 485, 489)` for `v`, and `(0, 2177, 2177, 4354, 4356, 6533, 6537)` for `z_dense`. At `b_0 = b_sharp(z, 3) - 1`, all three advance `5` steps to `(n = 2, p = 1)` with remaining bank `3`, reflect on step `6` (`Delta E = 4 > 3`), and unwind in `5` steps to `(u_0, b_0, -1)`.
   - Dirty-stock control (`B_0 = (w_v, 9)`) releases `159` energy units into the bank (`Delta E = -159`) and returns `(e, 1)` to the output port.
   - Clean-archive program capture (`z_arch = 0`) has exact cost `Delta E_cap(x; z, 0) = q(x)` independent of `z`.
   - For the opposite-seam collision (`t in {40, 41, 42}` at `Q = 14112`), the 1-pair reference gap is `15936/1210262180216419`, with 1-round sharp banks `(327731201, 361751201, 398353537)` and 91-round (`182`-output) sharp banks `(29823547481, 32919367481, 36250180057)`.

## 3. Scope Boundaries

This result is `NON-CANONICAL` at `L1`. In accordance with `POLICY.md` and `notes/C-JM-DECODER-CHAIN-PUBLICATION-N/SCOPE.md` (`#1696` / `#1697`), it establishes the existence and consistency of the declared cyclotomic coordinate bridge, universal integer pair involution, and positive-definite integer energy/bank account. It does not claim global decoder uniqueness, Born rule derivation, or an `L1 -> L6` laboratory hardware realization.
