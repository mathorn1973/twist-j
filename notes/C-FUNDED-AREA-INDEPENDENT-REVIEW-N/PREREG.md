# Six-Field Independent Review Preregistration (`C-FUNDED-AREA-INDEPENDENT-REVIEW-N`)

**Status:** PUBLIC / NON-CANONICAL / L1
**Review task:** Independent review R2 ([#1588](https://github.com/mathorn1973/twist-j/issues/1588), parent [#1586](https://github.com/mathorn1973/twist-j/issues/1586))
**Target:** [PR #1585](https://github.com/mathorn1973/twist-j/pull/1585) (`probe/P-FUNDED-AREA-PHASE-RECORD-1`, head `bb04eb3c582e2ec06f90b1a5768ecdfb1ac2044e`, formal source pin `a4ec92176c9f8ace9f884254e05d57a5466b84e0`), reservation [#1584](https://github.com/mathorn1973/twist-j/issues/1584).
**Reviewer session:** `Antigravity-R2-20261017-8f0b47e9`
**Author:** A. M. Thorn `<thorn@twistj.com>`
**SPDX-License-Identifier:** Apache-2.0
**Normative basis:** Public Canon v103 ACTIVE (`dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`, content `01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`, `canon/CANON.md` `1052518` bytes, SHA-256 `d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b`).

This preregistration freezes the independent mathematical target equations, the standalone adversarial breaker (`break.py`), the complete finite audit and counterexample-search domains, systematics, falsifier thresholds, and L1 scope boundary **before** the first execution of `break.py` and **before** opening the author's `PROOF.md`, `verify.py`, `EXPECTED.txt`, `RUN.md`, or `RESULT.md`.

---

## 1. Equations and Target Claims Under Adversarial Audit

Let the complete state carrier be
$$\mathcal{S} = \mathbb{Z}^4 \times \mathbb{N}_0 \times \{+1, -1\}^2 \times C_4, \qquad s = (q, p, u, v, b, \sigma, \eta, c),$$
where $(q, p, u, v) \in \mathbb{Z}^4$, $b \in \mathbb{N}_0$, $\sigma \in \{+1, -1\}$, $\eta \in \{+1, -1\}$, and $c \in C_4 = \{0, 1, 2, 3\}$.
The chosen quadratic state cost and total energy are
$$H(q, p, u, v) = q^2 + p^2 + u^2 + v^2 \in \mathbb{N}_0, \qquad E(s) = H(q, p, u, v) + b \in \mathbb{N}_0.$$

For $h \in \{+1, -1\}$, the unfunded integer shears on $\mathbb{Z}^4$ are
$$Q_h(q, p, u, v) = (q + h, p, u, v), \qquad P_h(q, p, u, v) = (q, p + h, u + h q, v + h q).$$
For a requested gate $(\mathrm{axis}, \epsilon)$ with $\mathrm{axis} \in \{Q, P\}$ and $\epsilon \in \{+1, -1\}$, let $h = \epsilon \sigma \in \{+1, -1\}$, let $x = (q, p, u, v)$, and let $x' = T_h(x)$ where $T_h = Q_h$ for $\mathrm{axis}=Q$ and $T_h = P_h$ for $\mathrm{axis}=P$. Let $\Delta = H(x') - H(x)$.
The funded elementary gate $F_{\mathrm{axis}, \epsilon} : \mathcal{S} \to \mathcal{S}$ is defined by:
$$F_{\mathrm{axis}, \epsilon}(q, p, u, v, b, \sigma, \eta, c) = \begin{cases} (q', p', u', v', b - \Delta, \sigma, \eta, c) & \text{if } b \ge \Delta \text{ (accepted)}, \\ (q, p, u, v, b, -\sigma, \eta, c) & \text{if } b < \Delta \text{ (rejected)}. \end{cases}$$

The autonomous 4-phase controller selects the letter $L(c, \eta)$ according to
$$L(0, \eta) = (Q, +1), \quad L(1, \eta) = (P, \eta), \quad L(2, \eta) = (Q, -1), \quad L(3, \eta) = (P, -\eta).$$
The autonomous one-step map $U_* : \mathcal{S} \to \mathcal{S}$ applies $F_{L(c, \eta)}$ and advances $c \mapsto (c + 1) \bmod 4$.
Its explicit candidate inverse $U_*^{-1} : \mathcal{S} \to \mathcal{S}$ first decrements $c \mapsto c_{\mathrm{prev}} = (c - 1) \bmod 4$ and then applies $F_{\mathrm{axis}(L(c_{\mathrm{prev}}, \eta)), -\epsilon(L(c_{\mathrm{prev}}, \eta))}$.

The six mandatory attack targets from [#1588](https://github.com/mathorn1973/twist-j/issues/1588) are:

1. **Attack 1 (Full-carrier inverse):**
   For every $s \in \mathcal{S}$, every $\mathrm{axis} \in \{Q, P\}$, and every $\epsilon \in \{+1, -1\}$, test whether
   $$F_{\mathrm{axis}, -\epsilon}(F_{\mathrm{axis}, \epsilon}(s)) = s, \qquad F_{\mathrm{axis}, \epsilon}(F_{\mathrm{axis}, -\epsilon}(s)) = s,$$
   and whether $U_*^{-1}(U_*(s)) = s$ and $U_*(U_*^{-1}(s)) = s$, preserving $E(s) = H + b$, $u - v$, and $\eta$ on both accepted and rejected branches without merging distinct states.
2. **Attack 2 (Two independent transition formulas and $E \le 12$ inventory justification):**
   Independently derive the algebraic cost increments
   $$\Delta_Q(q, h) = 2 h q + 1, \qquad \Delta_P(q, p, u, v, h) = 2 h p + 1 + 2 h q (u + v) + 2 q^2,$$
   compare transitions computed via $(\Delta_Q, \Delta_P)$ against direct candidate-state $H(x') - H(x)$ evaluation across the complete $E \le 12$ raw state space, and independently justify from first principles the inventory bound $[-3, 3]^4$ and the exact counts (`57680` raw states, `230720` gate requests, `89152` rejected requests) via a generating-function decomposition of sums of four squares.
3. **Attack 3 (Area/record equation and unprepared/zero reference failure classification):**
   On any actual trajectory $s_0, s_1, \dots, s_N$ (including reflected rejections where $\Delta q_i = \Delta p_i = 0$), let
   $$A_{\mathrm{path}} = \sum_{i=0}^{N-1} q_i (p_{i+1} - p_i), \qquad A_2 = \sum_{i=0}^{N-1} (q_i p_{i+1} - p_i q_{i+1}).$$
   Test the general reference evolution $u_N = u_0 + A_{\mathrm{path}}$, $v_N = v_0 + A_{\mathrm{path}}$, the endpoint identity $2 A_{\mathrm{path}} = A_2 + (q_N p_N - q_0 p_0)$, and on the once-prepared family $(q_0, p_0, u_0, v_0) = (0, 0, 1, -1)$ test
   $$A_{\mathrm{read}} := \frac{u_N^2 - v_N^2}{4} = A_{\mathrm{path}}, \qquad u_N^2 + v_N^2 = 2 + 2 A_{\mathrm{path}}^2.$$
   Explicitly construct and verify counterexamples demonstrating what fails when $(u_0, v_0) \ne (1, -1)$ (equal references $u_0 = v_0$, including $(0,0)$, where $u_N^2 - v_N^2 = 0$; non-antipodal $u_0 + v_0 \ne 0$ where an initial offset $u_0^2 - v_0^2 \ne 0$ biases $u_N^2 - v_N^2$; and antipodal $u_0 = -v_0 = d \notin \{0, 1\}$ where $(u_N^2 - v_N^2)/4 = d A_{\mathrm{path}}$).
4. **Attack 4 (Weyl word and open-path vs. closed-path conventions):**
   On the five basis states $|k\rangle$ ($k \in \mathbb{Z}_5$), define monomial operators $X^a |k\rangle = |k + a \bmod 5\rangle$ and $Z^b |k\rangle = j^{b k} |k\rangle$ ($j^5 = 1$ primitive). For each actual step $i$ with $\Delta q_i = q_{i+1} - q_i$ and $\Delta p_i = p_{i+1} - p_i$, apply $X^{\Delta q_i}$ on an accepted $Q$ step, $Z^{\Delta p_i}$ on an accepted $P$ step, and $I$ on a rejected step in strict chronological order ($W_{i+1} = U_{\mathrm{step}\,i} W_i$, $W_0 = I$) without substituting $j^A$.
   Test the general open-path action from $(q_0, p_0)$:
   $$W_{\mathrm{path}} |k\rangle = j^{k(p_N - p_0) + A_{\mathrm{path}} - p_0(q_N - q_0)} |k + (q_N - q_0) \bmod 5\rangle,$$
   which for $q_0 = p_0 = 0$ simplifies to $W_{\mathrm{path}} |k\rangle = j^{k p_N + A_{\mathrm{path}}} |k + q_N \bmod 5\rangle$ and on integer-closed base paths ($q_N = p_N = 0$) reduces to $W_{\mathrm{path}} = j^{A_{\mathrm{path}}} I = j^{A_{\mathrm{read}}} I$. Identify why open-path phase depends on convention ($k$-dependent phase when $p_N \not\equiv p_0 \pmod 5$, noncommutativity $Z X = j X Z$, and basepoint translation).
5. **Attack 5 (Observational obstruction and reader-exposure downgrade):**
   Execute the two four-step histories from $s_{4, \eta} = (0, 0, 1, -1, 4, +1, \eta, 0)$ for $\eta \in \{+1, -1\}$. Verify that the coarse scalar histories of $(q^2 + p^2, u^2 + v^2, H, b, \sigma, c)$ are identical at every step $t \in \{0, 1, 2, 3, 4\}$, while the ordered endpoint reference costs $(u^2, v^2)$ are $(4, 0)$ vs. $(0, 4)$, $A_{\mathrm{read}} = \eta$, and $W_{\mathrm{path}} = j^\eta I$. Simultaneously verify that exposing $\eta$, the ordered pair $(u^2, v^2)$, or the intermediate signed coordinate $p_t$ ($t \in \{2, 3\}$) immediately distinguishes the two trajectories.
6. **Attack 6 (Resource threshold, $B=52$ witness, controls, periodicity, capacity bound, and hidden-resource audit):**
   - Test $B_{\min}(K) = 2 K^2 + 2$ across all $K \in \{1, \dots, 6\}$, $B \in \{0, \dots, 80\}$, and $\eta \in \{+1, -1\}$ (`972` cases), plus extended checks up to $K=10$.
   - Verify the five-lap $K=5, B=52, \eta=+1$ witness ($W_{\mathrm{path}} = I$, $(u, v) = (6, 4)$, $(u^2, v^2) = (36, 16)$, $b = 2$, paid reference work $50$).
   - Verify the nominal $B=3$ rejection control (where step 1, 2, and 3 all reject, leaving $(q_4, p_4) = (1, 0)$, $A_{\mathrm{path}} = 0$, $W_{\mathrm{path}} = X^1 \ne j^\eta I$) and both zero-reference controls $(0, 0, 0, 0, 4, +1, \pm 1, 0)$ (where $(u_4^2, v_4^2) = (1, 1)$ for both signs).
   - Trace the full autonomous $U_*$ orbits of $s_{4, +1}$ and $s_{4, -1}$ on the $E=6$ shell, verifying that both return to their initial state with exact period `124`, AND decompose the entire $E=6$ shell into disjoint $U_*$ cycles to exhibit explicit states on the $E=6$ shell whose periods differ from `124` (proving period `124` is orbit-specific, not a shell invariant).
   - Verify the record-capacity bound $|A_{\mathrm{read}}| \le \lfloor \sqrt{B/2} \rfloor$ on the entire $u - v = 2$ slice of $E \le 12$, and audit the zero-cost control tuple $(\sigma, \eta, c) \in \{+1, -1\}^2 \times C_4$ as a finite 16-state (4-bit) control resource that cannot store an unbounded record at fixed energy.

---

## 2. Code (`break.py`)

The sole executable is `notes/C-FUNDED-AREA-INDEPENDENT-REVIEW-N/break.py`, written in Python 3 using only the standard library (`hashlib`, `sys`) and exact integers.
- No floats, random numbers, external packages, file I/O, or network calls are used.
- All transition maps, monomial Weyl operators, shoelace accumulators, and cycle decompositions are implemented from scratch from Section 1 above prior to opening the target `verify.py`.
- Before the first execution, `break.py` undergoes only `python -m py_compile` syntax verification and `python tools/check_policy.py` policy verification; no dry run is permitted before `PINNED_R2`.

---

## 3. Complete Finite Audit and Adversarial Search Domains

1. **Exhaustive $E \le 12$ full-carrier shell (`[-3, 3]^4` box, $b \in [0, 12-H]$, $(\sigma, \eta, c) \in \{\pm 1\}^2 \times C_4$):**
   - Independently compute the 1D and 4D sum-of-squares generating coefficients $r_4(H)$ for $0 \le H \le 12$ and verify $\sum_{H=0}^{12} r_4(H)(13 - H) \times 16 = 57680$ raw states.
   - Enumerate all `57680` raw states and all `230720` elementary gate evaluations, checking direct vs. algebraic $\Delta$, two-sided gate inverses $F_{\mathrm{axis}, -\epsilon} \circ F_{\mathrm{axis}, \epsilon} = \mathrm{id}$ and $F_{\mathrm{axis}, \epsilon} \circ F_{\mathrm{axis}, -\epsilon} = \mathrm{id}$, two-sided autonomous inverses $U_*^{-1} \circ U_* = \mathrm{id}$ and $U_* \circ U_*^{-1} = \mathrm{id}$, injectivity on the shell, and exact invariance of $E$, $u - v$, and $\eta$.
   - Extended adversarial raw-state sweep outside prepared loops: test all raw states on the $E = 13, 14, 15$ shells as well to ensure no inverse or algebraic-increment counterexample hides just above $E = 12$.
2. **Exhaustive four-letter word tree of lengths $0 \le n \le 8$ (`87381` prefixes, `5341` closed base words):**
   - From common ready $s_{8320, +1} = (0, 0, 1, -1, 8320, +1, +1, 0)$, traverse all $\sum_{n=0}^8 4^n = 87381$ words over $(Q_+, P_+, Q_-, P_-)$ in fixed lexicographical depth-first order.
   - Verify affordability ($b \ge 0$), $u = 1 + A_{\mathrm{path}}$, $v = -1 + A_{\mathrm{path}}$, $A_{\mathrm{read}} = A_{\mathrm{path}}$, $u^2 + v^2 = 2 + 2 A_{\mathrm{path}}^2$, $2 A_{\mathrm{path}} = A_2 + q p$, and literal 5-state monomial action $W_{\mathrm{path}}|k\rangle = j^{k p + A_{\mathrm{path}}}|k + q \bmod 5\rangle$ at every prefix, plus $W_{\mathrm{path}} = j^{A_{\mathrm{read}}} I$ at all $\sum_{m=0}^4 \binom{2m}{m}^2 = 5341$ integer-closed words.
3. **Adversarial rejected-word and unprepared-reference suite:**
   - Test all $4^6 = 4096$ words of length $6$ starting from tight budgets $B \in \{0, 1, 2, 3, 4, 5\}$ (where rejections occur frequently and flip $\sigma$) and from unprepared/occupied initial states $(q_0, p_0, u_0, v_0) \in \{(0,0,0,0), (0,0,2,2), (0,0,2,0), (0,0,2,-2), (1,-1,3,0)\}$, verifying that the general open-path identity, path-reversibility by reversed opposite-sign words, and chronological Weyl operator law hold across rejected moves while the uncalibrated $(u^2-v^2)/4$ reader fails outside $u_0 = 1, v_0 = -1$ in the exact predicted manner.
4. **Autonomous budget grid, witness trajectories, and complete $E = 6$ cycle decomposition:**
   - Execute the $B=4, \eta=\pm 1$ four-step histories, the $972$-case budget grid ($\eta \in \{\pm 1\}$, $B \in \{0, \dots, 80\}$, $K \in \{1, \dots, 6\}$), the $K=5, B=52$ five-lap witness, the $B=3$ rejected square, and the $(u_0, v_0) = (0, 0)$ controls.
   - Decompose the entire $E = 6$ shell (`3728` states across both $\eta \in \{\pm 1\}$, `1864` per $\eta$) into disjoint autonomous $U_*$ cycles; verify the exact period `124` of $s_{4, +1}$ and $s_{4, -1}$ and report the complete cycle-length spectrum on $E = 6$.

---

## 4. Systematics and Scope Boundaries

- The carrier $\mathbb{Z}^4 \times \mathbb{N}_0 \times \{+1, -1\}^2 \times C_4$, quadratic cost $H = q^2 + p^2 + u^2 + v^2$, shifts $Q_h$, shears $P_h$, once-only preparation $(u_0, v_0) = (1, -1)$, ordered cost access $(u^2, v^2)$, 4-phase clock $c$, and fifth-root monomial Weyl operators $(X, Z)$ are **chosen model definitions**, not derivations from $J = 1 + \zeta_5^2$ or from the native update $U$ on $\mathbb{N}_0 \times \mathbb{F}_5^6$.
- The Weyl operator $W_{\mathrm{path}}$ is an externally evaluated algebraic character of actual $(q, p)$ displacements; it is not an autonomous physical phase observable or a global group homomorphism of the state-dependent funded maps $F_{\mathrm{axis}, \epsilon}$ (since rejected gates act as $I$ on the Weyl space while flipping $\sigma$ in $\mathcal{S}$).
- The control tuple $(\sigma, \eta, c)$ carries 4 bits of zero-cost state required for autonomous reversibility; this is an explicit model choice and does not create an unbounded zero-cost memory.

---

## 5. Falsifier Thresholds and Classification Protocol

- Zero numerical tolerance: every test uses exact Python integers.
- Any counterexample to a claimed identity at its stated scope in `PREREG.md` (G1–G6) triggers `FALSIFIER_FIRED` and classifies the target item as `COUNTEREXAMPLE`.
- Any unstated assumption or overbroad scope claim is classified as `STOP_INCOMPLETE` or a scope boundary requirement.
- If all G1–G6 identities hold on their stated domains and all scope boundaries are properly delimited, the item is classified as `CONFIRMED_IN_SCOPE`.
- Run command from repository root after public pin readback:
  ```text
  python3 notes/C-FUNDED-AREA-INDEPENDENT-REVIEW-N/break.py
  ```
  with `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.

---

## 6. Action Layer and Ownership Guard

- **Layer:** L1 only (exact discrete automaton and finite monomial algebra).
- **No promotion or physical lift:** This review claims no physical phase, no $\hbar$, no SI action unit, no closure of `METRO-EDGE-SCALE` or `QDD-INSTRUMENT-APPARATUS`, and no modification of `probes/P-FUNDED-AREA-PHASE-RECORD-1/`, `canon/`, or repository workflows.
