# Result: Independent Review R2 of `P-FUNDED-AREA-PHASE-RECORD-1` (`C-FUNDED-AREA-INDEPENDENT-REVIEW-N`)

**Status:** `CONFIRMED_IN_SCOPE` (PUBLIC / NON-CANONICAL / L1)
**Review task:** Independent review R2 ([#1588](https://github.com/mathorn1973/twist-j/issues/1588), parent [#1586](https://github.com/mathorn1973/twist-j/issues/1586))
**Target:** [PR #1585](https://github.com/mathorn1973/twist-j/pull/1585) (`probe/P-FUNDED-AREA-PHASE-RECORD-1`, head `bb04eb3c582e2ec06f90b1a5768ecdfb1ac2044e`, formal source pin `a4ec92176c9f8ace9f884254e05d57a5466b84e0`), reservation [#1584](https://github.com/mathorn1973/twist-j/issues/1584).
**Reviewer session:** `Antigravity-R2-20261017-8f0b47e9`
**Independent pre-execution pin:** `b7792774aa0a3f093d621220a1f7072115cc7e50` ([`PINNED_R2`](https://github.com/mathorn1973/twist-j/issues/1588#issuecomment-6241937368))
**Author:** A. M. Thorn `<thorn@twistj.com>`
**SPDX-License-Identifier:** Apache-2.0

---

## 1. Final Review Verdict

- **Scientific classification:** **`CONFIRMED_IN_SCOPE`** at L1 (conditional theorem-grade proof `T` and exact two-architecture computational verification `C` within the explicitly declared integer comparison automaton and chosen five-state monomial Weyl representation).
- **Fired falsifiers / counterexamples to target claims:** `0`.
- **Independence and exposure:** Method-blind (both proof-method-blind and implementation-blind before `PINNED_R2` and first execution of `break.py`), not result-blind.

---

## 2. Key Independent Findings

1. **Full-carrier bijectivity and exact inversion (Attack 1):**
   Every elementary funded gate $F_{\mathrm{axis}, \epsilon}$ on $\mathcal{S} = \mathbb{Z}^4 \times \mathbb{N}_0 \times \{+1, -1\}^2 \times C_4$ has exact two-sided inverse $F_{\mathrm{axis}, -\epsilon}$ across all occupied reference values $(u, v) \in \mathbb{Z}^2$, zero bank $b = 0$, and rejected attempts ($b < \Delta$), and $U_*$ has exact autonomous inverse $U_*^{-1}$, preserving $E(s) = H + b$, $u - v$, and $\eta$. Verified analytically (`PROOF.md` §1) and computationally across all `57680` raw states on $E \le 12$ plus `51120` raw states on $E \in \{13, 14, 15\}$.
2. **Independent transition derivation and $E \le 12$ inventory proof (Attack 2):**
   The expanded increments $\Delta_Q = 2 h q + 1$ and $\Delta_P = 2 h p + 1 + 2 h q(u+v) + 2 q^2$ agree identically with direct candidate-state cost differences across all `230720` gate evaluations on $E \le 12$ (`141568` accepted, `89152` rejected). The exact inventory size $3605 \times 16 = 57680$ is proved analytically via the fourth power of $f(t) = 1 + 2t + 2t^4 + 2t^9 \bmod t^{13}$ (`PROOF.md` §2.2).
3. **Actual-path area record and necessary preparation $(u_0, v_0) = (1, -1)$ (Attack 3):**
   Along any actual trajectory (including rejected steps), $u_N = u_0 + A_{\mathrm{path}}$, $v_N = v_0 + A_{\mathrm{path}}$, and $2 A_{\mathrm{path}} = A_2 + (q_N p_N - q_0 p_0)$. The uncalibrated quadratic difference reader $A_{\mathrm{read}} = (u_N^2 - v_N^2)/4$ equals $A_{\mathrm{path}}$ for all $A_{\mathrm{path}} \in \mathbb{Z}$ **if and only if** $(u_0, v_0) = (1, -1)$; outside $(1, -1)$ it fails by orientation loss ($u_0 = v_0$), additive offset ($u_0^2 \ne v_0^2$), or scaling ($u_0 = -v_0 = d \notin \{0, 1\}$), verified across `87381` prepared prefixes (`5341` closed words) and `28672` adversarial paths (`15631` unprepared-reader failures).
4. **Chronological Weyl word on actual displacements (Attack 4):**
   Direct 5-state monomial composition ($X^{\Delta q_i}$ on accepted $Q$, $Z^{\Delta p_i}$ on accepted $P$, $I$ on rejected moves) obeys $W_N |k\rangle = j^{k(p_N - p_0) + A_{\mathrm{path}} - q_0(p_N - p_0)} |k + (q_N - q_0) \bmod 5\rangle$, which reduces to the convention-independent scalar $W_N = j^{A_{\mathrm{path}}} I = j^{A_{\mathrm{read}}} I$ on integer-closed base paths ($q_N = q_0, p_N = p_0$).
5. **Scoped observational obstruction at $B = 4$ (Attack 5):**
   From $s_{4, \eta}$, opposite orientations $\eta = \pm 1$ yield identical coarse histories of $(q^2+p^2, u^2+v^2, H, b, \sigma, c)$ over four steps while producing opposite ordered reference costs $(4, 0)$ vs. $(0, 4)$, $A_{\mathrm{read}} = \eta$, and $W_{\mathrm{path}} = j^\eta I$. This obstruction applies strictly to coarse scalar observers; exposing $\eta$, $p_2$, or the ordered reference pair $(u^2, v^2)$ immediately separates the two trajectories.
6. **Sharp funding threshold, nonreset witness, cycle spectrum, and finite control memory (Attack 6):**
   - All $4K$ steps from $s_{B, \eta}$ succeed if and only if $B \ge B_{\min}(K) = 2 K^2 + 2$ (proved in `PROOF.md` §6.1 and checked on all `972` grid cases plus $K = 7..10$).
   - At $K = 5, B = 52, \eta = +1$, $W_{\mathrm{path}} = I$ while $(u, v) = (6, 4)$, $(E_+, E_-) = (36, 16)$, $b = 2$, and paid reference work is `50` (phase return is not state reset).
   - At $B = 3$, steps 1, 2, 3 reject and the actual path ends at $(1, 0, 1, -1, 2, -1, \eta, 0)$ with $W_{\mathrm{path}} = X^1 \ne j^\eta I$.
   - The complete $E = 6$ shell (`3728` states) decomposes into `16` cycles of length `20`, `32` of length `52`, `8` of length `124` (containing $s_{4, \pm 1}$), and `4` of length `188`, proving that period `124` is orbit-specific rather than a shell-wide period.
   - On the $u - v = 2$ slice, $|A_{\mathrm{read}}| \le \lfloor\sqrt{B/2}\rfloor$, and $(\sigma, \eta, c) \in \{\pm 1\}^2 \times C_4$ is a finite 16-state (4-bit) zero-cost control resource that cannot store an unbounded record at fixed energy.

---

## 3. Explicit Physical and Canonical Boundary

This review confirms a conditional L1 mathematical construction only. It establishes no physical action scale, no $\hbar$, no SI unit bridge, no native $U$ or $J$ compilation of the shears or quadratic cost, no physical phase detector, and no closure of `METRO-EDGE-SCALE`, `QDD-INSTRUMENT-APPARATUS`, or native contact admission. PR #1585, R1 (#1587), N (#1589/#1596), and all normative Canon and Registry files remain untouched.
