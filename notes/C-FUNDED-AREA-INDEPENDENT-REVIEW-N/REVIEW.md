# Independent Review R2 of PR #1585 (`P-FUNDED-AREA-PHASE-RECORD-1`)

**Status:** PUBLIC / NON-CANONICAL / L1
**Review candidate:** `C-FUNDED-AREA-INDEPENDENT-REVIEW-N`
**Assignment:** [#1588](https://github.com/mathorn1973/twist-j/issues/1588) (parent [#1586](https://github.com/mathorn1973/twist-j/issues/1586))
**Target:** [PR #1585](https://github.com/mathorn1973/twist-j/pull/1585) (`probe/P-FUNDED-AREA-PHASE-RECORD-1`, result head `bb04eb3c582e2ec06f90b1a5768ecdfb1ac2044e`, formal source pin `a4ec92176c9f8ace9f884254e05d57a5466b84e0`), reservation [#1584](https://github.com/mathorn1973/twist-j/issues/1584) (`ChatGPT-funded-area-record-20261017`).
**Reviewer session:** `Antigravity-R2-20261017-8f0b47e9`
**Author:** A. M. Thorn `<thorn@twistj.com>`
**SPDX-License-Identifier:** Apache-2.0
**Overall Verdict:** **`CONFIRMED_IN_SCOPE`** (conditional L1 candidate-T / candidate-C within declared primitives and scope boundaries; `0` scientific counterexamples).

---

## 1. Executive Summary and Exposure Discipline

1. **Method-blind execution protocol:**
   Prior to committing, pushing, publicly reading back (`PINNED_R2`, commit `b7792774aa0a3f093d621220a1f7072115cc7e50`), and executing `notes/C-FUNDED-AREA-INDEPENDENT-REVIEW-N/break.py` (`2026-10-17T22:06:47Z`), this session read only Public Canon v103 normative files, the #1588 assignment, the #1584 reservation body, the one-line summary in #1602, and the pinned `probes/P-FUNDED-AREA-PHASE-RECORD-1/PREREG.md` (`a4ec92176c9f8ace9f884254e05d57a5466b84e0`, SHA-256 `a311e0ae92e61c16ca578d2c18d183f0f3e49720da9f918ae35e599ee6df4213`). The author's `PROOF.md`, `verify.py`, `EXPECTED.txt`, `RUN.md`, and `RESULT.md` were opened **only after** our first frozen run of `break.py` completed with exit code `0` and `0` counterexamples. All six pre-execution files in `notes/C-FUNDED-AREA-INDEPENDENT-REVIEW-N/` remain byte-for-byte unchanged from `b7792774aa0a3f093d621220a1f7072115cc7e50`.
2. **Independence level:**
   Because the preregistration and dispatch surfaces expose the target equations, finite inventory counts, and witness parameters, this review is **method-blind** (both proof-method-blind and implementation-blind prior to the first run), **never result-blind**.
3. **Target source and CI custody verification:**
   At the formal source pin `a4ec92176c9f8ace9f884254e05d57a5466b84e0` and the result head `bb04eb3c582e2ec06f90b1a5768ecdfb1ac2044e`, all five pre-execution target files are byte-for-byte identical:
   - `PREREG.md`: `11149` B, blob `5b8c29bc0c0612ce3f6b78910debf53c04be7f1b`, SHA-256 `a311e0ae92e61c16ca578d2c18d183f0f3e49720da9f918ae35e599ee6df4213`
   - `PROOF.md`: `13609` B, blob `486b502442e2695615755e04a88b1a5b98bc12ad`, SHA-256 `c9e55f49b3a82cb51c8dbc5b88cd27cdeae0957fbc8cd56fc9d7d076b90c7318`
   - `verify.py`: `10639` B, blob `e51e92caa67c8c23ae32dd039b544a9ae5ae4593`, SHA-256 `83524f15518ef30a2f69939cb56e0f2bc43d403ca915d5c2047260ed8a444d5f`
   - `SOURCES.tsv`: `1746` B, blob `2cc7debfd51fc8ee9a414694324f8581f8424fe0`, SHA-256 `5ad369d2cd0b84ec044c0928090debc096789558f20fb4dd6548d1e769a1f307`
   - `README.md`: `1610` B, blob `751b8bcb74388e262425d0f762e3314631386651`, SHA-256 `15e5c0a9deb6fd42839a7b33507e815b49f517d01c2b2928e385935e7f6a7586`

   The result commit `bb04eb3c582e2ec06f90b1a5768ecdfb1ac2044e` adds `EXPECTED.txt` (`1207` B, SHA-256 `e745a01d2f38b303737fe896242dd77217e15c820f11cd8a10d798a88b91133b`), `RUN.md` (`2477` B), and `RESULT.md` (`7560` B), recorded on `aarch64` (`Debian GNU/Linux 12 (bookworm)`, Python `3.11.2`). On GitHub PR #1585 (`bb04eb3c582e2ec06f90b1a5768ecdfb1ac2044e`), because the diff changes `probes/P-FUNDED-AREA-PHASE-RECORD-1/`, `check_verifier.py` replayed `verify.py` on both `architecture-x86_64` and `architecture-aarch64` with `conclusion: success` and aggregate `check: success`.

---

## 2. Attack-by-Attack Comparison and Audit Findings

### Attack 1: Full-Carrier Inverse (`CONFIRMED_IN_SCOPE`)

- **Independent proof and breaker result:**
  In `PROOF.md` §1 (`Lemma 1.1`, `Theorem 1.2`, `Corollary 1.3`), we proved that for every $s = (q, p, u, v, b, \sigma, \eta, c) \in \mathcal{S}$, $F_{\mathrm{axis}, -\epsilon}$ is the two-sided inverse of $F_{\mathrm{axis}, \epsilon}$ on both the accepted branch ($b_1 = b - \Delta \ge 0 \implies b_1 - (-\Delta) = b \ge 0$, so the reverse lattice shear is always affordable) and the rejected branch (where $h_1 = (-\epsilon)(-\sigma) = \epsilon \sigma = h$ tests the identical unaffordable candidate from the unchanged integer tuple $(q,p,u,v)$ and bank $b$, rejecting again and restoring $\sigma$). Both $E(s) = H + b$ and $u - v$ are preserved across the entire carrier.
- **Comparison with author's `PROOF.md` §1–2 and `verify.py`:**
  The author's proof in `PROOF.md` §1–2 gives the same two-branch case analysis and also notes the connection to `INTEGER-ENERGY-FUNDED-INVOLUTION [T]` by viewing $(z, \sigma) \mapsto (T_a^\sigma z, -\sigma)$ as the underlying involution composed with a direction flip.
- **Extended adversarial verification in `break.py`:**
  Beyond confirming all `57680` raw states on $E \le 12$, `break.py` explicitly verified that each of the 4 elementary gates and $U_*$ has image cardinality `57680` on $\mathcal{S}_{\le 12}$ (zero state collisions) and verified all two-sided inverses on the $E \in \{13, 14, 15\}$ shells (`51120` additional states, `204480` additional gate checks, `69568` additional rejections) with `0` counterexamples.

### Attack 2: Two Independent Transition Formulas and $E \le 12$ Inventory Justification (`CONFIRMED_IN_SCOPE`)

- **Independent proof and breaker result:**
  `PROOF.md` §2.1 derives $\Delta_Q(q, h) = 2 h q + 1$ and $\Delta_P(q, p, u, v, h) = 2 h p + 1 + 2 h q(u+v) + 2 q^2$ from $h^2 = 1$. In `PROOF.md` §2.2 (`Theorem 2.2`), we independently justified the $[-3, 3]^4$ coordinate bound ($\lfloor\sqrt{12}\rfloor = 3$) and derived the exact count of `57680` raw states analytically from the truncated generating polynomial $f(t) = 1 + 2t + 2t^4 + 2t^9$, whose fourth power modulo $t^{13}$ has coefficients
  $$(r_4(0), \dots, r_4(12)) = (1, 8, 24, 32, 24, 48, 96, 64, 24, 104, 144, 96, 96),$$
  giving $\sum_{H=0}^{12} r_4(H)(13 - H) = 3605$ integer-and-bank tuples and $3605 \times 16 = 57680$ raw states (`230720` gate evaluations, of which `141568` are accepted and `89152` are rejected).
- **Comparison with author's `PROOF.md` and `verify.py`:**
  The author's `verify.py` (`gate` vs. `alternate_gate`) matches our direct and expanded transition formulas and produces identical counts (`states=57680 gate_checks=230720 rejected=89152`). The author's `PROOF.md` did not include the explicit generating-function table for `3605 * 16 = 57680`, so our `Theorem 2.2` supplies the independent analytical justification of the inventory size requested by #1588.
- **Pre-pin Errata Disclosure (No Retroactive Edit):**
  In the summary `Total` line of the table in our pre-pinned `PROOF.md` §2.2, the unweighted sum $\sum_{H=0}^{12} r_4(H)$ was written as `781` instead of `761` (an arithmetic slip in summing the column by hand), while every individual $r_4(H)$ row, the weighted sum `3605`, the total `57680`, and `break.py`'s computed `r4_sum=761 xb_tuples=3605 raw_states=57680` are exact. In accordance with #1588's no-retroactive-changes rule, `PROOF.md` is left untouched at its pre-run pin hash.

### Attack 3: Area / Record Equation and Unprepared / Zero Reference Failures (`CONFIRMED_IN_SCOPE`)

- **Independent proof and breaker result:**
  `PROOF.md` §3 (`Theorem 3.1` and `Corollary 3.2`) proves that along every actual trajectory (including rejected steps where $\Delta q_i = \Delta p_i = 0$), $u_N = u_0 + A_{\mathrm{path}}$, $v_N = v_0 + A_{\mathrm{path}}$, $2 A_{\mathrm{path}} = A_2 + (q_N p_N - q_0 p_0)$, and
  $$\frac{u_N^2 - v_N^2}{4} = \frac{u_0^2 - v_0^2}{4} + \frac{u_0 - v_0}{2} A_{\mathrm{path}}.$$
  This proves that the uncalibrated quadratic difference reader $A_{\mathrm{read}} = (u_N^2 - v_N^2)/4$ equals $A_{\mathrm{path}}$ for all $A_{\mathrm{path}} \in \mathbb{Z}$ **if and only if** $(u_0, v_0) = (1, -1)$, and classifies all three failure modes outside $(1, -1)$:
  1. $u_0 = v_0$ (including $(0,0)$): $u_N^2 - v_N^2 = 0$ identically (orientation sign lost);
  2. $u_0 \ne v_0$ with $u_0 + v_0 \ne 0$: nonzero additive offset $(u_0^2 - v_0^2)/4 \ne 0$;
  3. $u_0 = -v_0 = d \notin \{0, 1\}$: multiplicative scaling $d A_{\mathrm{path}} \ne A_{\mathrm{path}}$.
- **Comparison with author's `PROOF.md` §3 and `verify.py`:**
  The author's `PROOF.md` §3 derives the same identity $D_{\mathrm{final}} - D_{\mathrm{initial}} = 2(u_{\mathrm{initial}} - v_{\mathrm{initial}})A$ and `word_audit()` checks all `87381` prefixes and `5341` closed words of length $\le 8$ at $B = 8320$. Our `break.py` independently confirmed all `87381` prefixes and `5341` closed words (`min_bank=7776`, `max_abs_A=16`) and additionally tested `28672` length-6 paths across 7 tight-budget and unprepared/occupied initial states (`11521` rejected steps, `15631` explicit unprepared-reader mismatches), confirming that general path reversibility and linear reference shifting hold while uncalibrated $(u^2-v^2)/4$ fails outside $(1, -1)$ exactly as classified.

### Attack 4: Weyl Word and Open-Path vs. Closed-Path Conventions (`CONFIRMED_IN_SCOPE`)

- **Independent proof and breaker result:**
  In `PROOF.md` §4 (`Theorem 4.1`) and `break.py` (`apply_step_weyl` and `expected_weyl`), we rebuilt the 5-state monomial transformations directly from $X|k\rangle = |k + 1 \bmod 5\rangle$, $Z|k\rangle = j^k |k\rangle$, and $I$ on rejected moves, proving by induction that for any trajectory starting at $(q_0, p_0)$ with total displacement $(\Delta q_{\mathrm{tot}}, \Delta p_{\mathrm{tot}}) = (q_N - q_0, p_N - p_0)$:
  $$W_N |k\rangle = j^{k \Delta p_{\mathrm{tot}} + A_{\mathrm{path}} - q_0 \Delta p_{\mathrm{tot}}} |k + \Delta q_{\mathrm{tot}} \bmod 5\rangle.$$
  When $q_0 = p_0 = 0$, $W_N |k\rangle = j^{k p_N + A_{\mathrm{path}}} |k + q_N \bmod 5\rangle$, and when the base path is integer-closed ($q_N = q_0, p_N = p_0$), $\Delta q_{\mathrm{tot}} = \Delta p_{\mathrm{tot}} = 0$ so $W_N = j^{A_{\mathrm{path}}} I$ independent of $(q_0, p_0)$ and basis index $k$.
- **Comparison with author's `PROOF.md` §4 and `verify.py`:**
  Our `Theorem 4.1` and `expected_weyl` agree completely with the author's `PROOF.md` §4 (`W_path |k> = j^(kP + A - q0 P) |k+Q>`) and `mono_next` in `verify.py`. Both confirm that open-path phase depends on convention ($k$-dependent phase when $\Delta p_{\mathrm{tot}} \not\equiv 0 \pmod 5$, noncommutativity $Z X = j X Z$, and basepoint translation $-q_0 \Delta p_{\mathrm{tot}}$), and that modulo-5 closure without integer closure ($\Delta p_{\mathrm{tot}}$ or $\Delta q_{\mathrm{tot}}$ a nonzero multiple of 5) does not reset the integer coordinates.
- **Pre-pin Errata Disclosure (No Retroactive Edit):**
  In `PREREG.md` line 63 (narrative summary of Attack 4), the basepoint translation term was typed as `- p_0(q_N - q_0)`, whereas in both our pre-pinned `PROOF.md` (`Theorem 4.1`) and our pre-pinned `break.py` (`expected_weyl`, line 104: `k * dp_tot + a_path - q0 * dp_tot`), the exact term `- q_0(p_N - p_0)` was derived, implemented, and verified across all `4096` non-origin paths from $(q_0, p_0) = (1, -1)$.

### Attack 5: Observational Obstruction and Reader-Exposure Downgrade (`CONFIRMED_IN_SCOPE`)

- **Independent proof and breaker result:**
  `PROOF.md` §5 (`Proposition 5.1`) and `break.py` (`audit_attack_5`) confirm that starting from $s_{4, \eta} = (0, 0, 1, -1, 4, +1, \eta, 0)$ for $\eta \in \{+1, -1\}$, both four-step trajectories have identical coarse histories $H = (2, 3, 6, 5, 4)$, $b = (4, 3, 0, 1, 2)$, $q^2+p^2 = (0, 1, 2, 1, 0)$, $u^2+v^2 = (2, 2, 4, 4, 4)$, $\sigma = (+1, +1, +1, +1, +1)$, and $c = (0, 1, 2, 3, 0)$, while the ordered endpoint reference costs $(E_+, E_-) = (u_4^2, v_4^2)$ are $(4, 0)$ vs. $(0, 4)$, giving $A_{\mathrm{read}} = \eta$ and $W_{\mathrm{path}} = j^\eta I$.
- **Comparison and Scope Guard:**
  Both our `PROOF.md` §5 and the author's `PROOF.md` §5 / `RESULT.md` §3 explicitly limit this negative statement to coarse observers that receive only $(q^2+p^2, u^2+v^2, H, b, \sigma, c)$. As verified in `break.py`, if a reader is given access to the program bit $\eta$, the intermediate signed coordinate $p_2 = \eta$, or the ordered reference pair $(u^2, v^2)$, the two trajectories are immediately distinguishable.

### Attack 6: Resource Threshold, Five-Lap Witness, Controls, Recurrence, and Hidden-Resource Audit (`CONFIRMED_IN_SCOPE`)

- **Independent proof and breaker result:**
  1. **Funding threshold $B_{\min}(K) = 2 K^2 + 2$:** Proved in `PROOF.md` §6.1 (`Theorem 6.1`) from the peak state cost $\max_{1 \le t \le 4K} H_t = H_{4K-2} = 2 K^2 + 4$ and total energy $E = B + 2$, and verified in `break.py` across all `972` budget cases ($\eta \in \{\pm 1\}, B \in 0..80, K \in 1..6$: `584` fully accepted, `388` with rejections) plus boundary checks for $K = 7..10$.
  2. **Five-lap $K=5, B=52, \eta=+1$ witness:** Verified at step $20$: state `(0, 0, 6, 4, 2, 1, 1, 0)`, ordered costs `(36, 16)`, $A_{\mathrm{read}} = 5$, paid reference work `50`, and $W_{\mathrm{path}} = j^5 I = I$ (fivefold phase closure does not reset the integer record or refund the spent bank).
  3. **Controls ($B=3$ and zero-reference):** At $B=3$, step 0 is accepted to $q=1$ and steps 1, 2, 3 all reject (step 2 attempts $Q_{+1}$ to $q=2$ because step 1 flipped $\sigma = -1$), ending at `(1, 0, 1, -1, 2, -1, eta, 0)` with $A_{\mathrm{path}} = 0$ and $W_{\mathrm{path}} = X^1 \ne j^\eta I$. At $u_0 = v_0 = 0, B=4$, both $\eta = \pm 1$ finish with identical squared reference costs `(1, 1)`.
  4. **Period `124` and complete $E = 6$ cycle spectrum:** Both `verify.py` and `break.py` confirm that $s_{4, +1}$ and $s_{4, -1}$ return to their initial state after `124` steps of $U_*$. In addition, `break.py` decomposed all `3728` states of the $E = 6$ shell into disjoint $U_*$ cycles, establishing the exact cycle-length spectrum on $E = 6$:
     - `16` cycles of length `20` (`320` states),
     - `32` cycles of length `52` (`1664` states),
     - `8` cycles of length `124` (`992` states, including $s_{4, \pm 1}$),
     - `4` cycles of length `188` (`752` states).
     This provides an explicit finite-shell counterexample against any overbroad claim that `124` is the period of the $E = 6$ shell itself.
  5. **Record-capacity bound and hidden-resource audit:** On the invariant slice $u - v = 2$ at $E = B + 2$, $2 + 2 A_{\mathrm{read}}^2 = u^2 + v^2 \le B + 2 \implies |A_{\mathrm{read}}| \le \lfloor\sqrt{B/2}\rfloor$ (checked across all `882` states with $u - v = 2$ and $E \le 15$). The zero-cost control tuple $(\sigma, \eta, c) \in \{+1, -1\}^2 \times C_4$ is a finite 16-state (4-bit) control resource required for autonomous reversibility; because its cardinality is fixed at $16$, it cannot act as an unbounded hidden memory archive.

---

## 3. Summary Disposition Table

| Attack / Criterion | Target Claim in PR #1585 | Independent Review Disposition | Scope / Boundary Condition |
|---|---|---|---|
| **1. Full-carrier inverse** | $F_{\mathrm{axis}, -\epsilon} = F_{\mathrm{axis}, \epsilon}^{-1}$ and $U_*^{-1}$ on $\mathcal{S}$ | **`CONFIRMED_IN_SCOPE`** | Holds on all of $\mathbb{Z}^4 \times \mathbb{N}_0 \times \{\pm 1\}^2 \times C_4$, including occupied $(u,v)$ and rejected moves. |
| **2. Two transition formulas & $E \le 12$ inventory** | $\Delta_Q, \Delta_P$ polynomials; `57680` states, `230720` gates, `89152` rejects | **`CONFIRMED_IN_SCOPE`** | Exact generating-function proof ($3605 \times 16 = 57680$) and exhaustive $E \le 15$ check pass. |
| **3. Area / record equation & unprepared failures** | $u = u_0 + A_{\mathrm{path}}$, $v = v_0 + A_{\mathrm{path}}$, $A_{\mathrm{read}} = A_{\mathrm{path}}$ on $(1,-1)$ | **`CONFIRMED_IN_SCOPE`** | Uncalibrated $(u^2-v^2)/4 = A_{\mathrm{path}}$ holds iff $(u_0, v_0) = (1, -1)$; fails on equal, non-antipodal, or $d \ne 1$ references. |
| **4. Chronological Weyl word** | $W_{\mathrm{path}}|k\rangle = j^{k \Delta p + A_{\mathrm{path}} - q_0 \Delta p}|k + \Delta q\rangle$; $W_{\mathrm{path}} = j^{A_{\mathrm{read}}}I$ on closed base paths | **`CONFIRMED_IN_SCOPE`** | External algebraic character of actual displacements (with $I$ on rejections); open-path phase is convention- and basis-dependent. |
| **5. Observational obstruction ($B=4$)** | Identical coarse $(q^2+p^2, u^2+v^2, H, b, \sigma, c)$ histories for $\eta = \pm 1$; opposite $(E_+, E_-)$ and $j^\eta$ | **`CONFIRMED_IN_SCOPE`** | Strictly restricted to the coarse scalar kernel; exposing $\eta$, $p_2$, or ordered $(u^2, v^2)$ distinguishes $\eta = \pm 1$. |
| **6. Resource bound, $B=52$, controls, recurrence** | $B_{\min}(K) = 2K^2 + 2$; $K=5, B=52$ nonreset; $B=3$ rejection; $|A_{\mathrm{read}}| \le \lfloor\sqrt{B/2}\rfloor$; $s_{4,\pm 1}$ period `124` | **`CONFIRMED_IN_SCOPE`** | Period `124` is specific to the $s_{4,\pm 1}$ orbit class ($E=6$ has cycle lengths `20, 52, 124, 188`); $(\sigma,\eta,c)$ is a 4-bit zero-cost control resource. |
| **Physical / canonical status guard** | Conditional L1 comparison automaton; no $\hbar$, no SI bridge, no native $U$ compilation | **`CONFIRMED_IN_SCOPE`** | Does not close `METRO-EDGE-SCALE`, `QDD-INSTRUMENT-APPARATUS`, or native contact admission. |
