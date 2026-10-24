# Independent Mathematical Proof and Adversarial Analysis (`C-FUNDED-AREA-INDEPENDENT-REVIEW-N`)

**Status:** PUBLIC / NON-CANONICAL / L1
**Review task:** Independent review R2 ([#1588](https://github.com/mathorn1973/twist-j/issues/1588), parent [#1586](https://github.com/mathorn1973/twist-j/issues/1586))
**Target:** [PR #1585](https://github.com/mathorn1973/twist-j/pull/1585) (`probe/P-FUNDED-AREA-PHASE-RECORD-1`, formal source pin `a4ec92176c9f8ace9f884254e05d57a5466b84e0`).
**Reviewer session:** `Antigravity-R2-20261017-8f0b47e9`
**Author:** A. M. Thorn `<thorn@twistj.com>`
**SPDX-License-Identifier:** Apache-2.0

All proofs below were derived independently from the frozen specification in [#1588](https://github.com/mathorn1973/twist-j/issues/1588) and `probes/P-FUNDED-AREA-PHASE-RECORD-1/PREREG.md` (`a4ec92176c9f8ace9f884254e05d57a5466b84e0`) prior to opening the target `PROOF.md`, `verify.py`, `EXPECTED.txt`, `RUN.md`, or `RESULT.md`.

---

## 1. Attack 1: Full-Carrier Bijections, Inverses, and Invariants

### 1.1 Unfunded integer shears and their group relations

Let $\mathcal{X} = \mathbb{Z}^4$ with coordinates $x = (q, p, u, v)$. For $h \in \{+1, -1\}$, define
$$Q_h(q, p, u, v) = (q + h, p, u, v), \qquad P_h(q, p, u, v) = (q, p + h, u + h q, v + h q).$$

**Lemma 1.1 (Unfunded inverse and reference-difference invariance).**
For each $h \in \{+1, -1\}$:
1. $Q_{-h} \circ Q_h = \mathrm{id}_{\mathcal{X}}$ and $P_{-h} \circ P_h = \mathrm{id}_{\mathcal{X}}$.
2. The linear form $\delta(q, p, u, v) := u - v$ is invariant under both $Q_h$ and $P_h$.

*Proof.*
(1) $(Q_{-h} \circ Q_h)(q, p, u, v) = (q + h - h, p, u, v) = (q, p, u, v)$. Because $P_h$ leaves the first coordinate $q$ unchanged,
$$(P_{-h} \circ P_h)(q, p, u, v) = P_{-h}(q, p + h, u + h q, v + h q) = (q, p + h - h, u + h q - h q, v + h q - h q) = (q, p, u, v).$$
(2) Under $Q_h$, $u' - v' = u - v$; under $P_h$, $u' - v' = (u + h q) - (v + h q) = u - v$. $\square$

### 1.2 Exact two-sided inverse of every funded gate $F_{\mathrm{axis}, \epsilon}$

Let $\mathcal{S} = \mathbb{Z}^4 \times \mathbb{N}_0 \times \{+1, -1\}^2 \times C_4$. For $s = (x, b, \sigma, \eta, c) \in \mathcal{S}$, define
$$H(x) = q^2 + p^2 + u^2 + v^2 \in \mathbb{N}_0, \qquad E(s) = H(x) + b \in \mathbb{N}_0.$$
Given $\mathrm{axis} \in \{Q, P\}$ and $\epsilon \in \{+1, -1\}$, set $h = \epsilon \sigma \in \{+1, -1\}$, $T_h = Q_h$ if $\mathrm{axis}=Q$ and $T_h = P_h$ if $\mathrm{axis}=P$, $x' = T_h(x)$, and $\Delta = H(x') - H(x) \in \mathbb{Z}$. Then
$$F_{\mathrm{axis}, \epsilon}(x, b, \sigma, \eta, c) = \begin{cases} (x', b - \Delta, \sigma, \eta, c) & \text{if } b \ge \Delta, \\ (x, b, -\sigma, \eta, c) & \text{if } b < \Delta. \end{cases}$$

**Theorem 1.2 (Full-carrier inverse and invariants of $F_{\mathrm{axis}, \epsilon}$).**
For every $\mathrm{axis} \in \{Q, P\}$ and $\epsilon \in \{+1, -1\}$:
1. $F_{\mathrm{axis}, \epsilon}$ maps $\mathcal{S}$ into $\mathcal{S}$ and preserves $E(s) = H(x) + b$, $\delta(s) = u - v$, $\eta$, and $c$.
2. For every $s \in \mathcal{S}$ (including arbitrary occupied references $(u, v) \in \mathbb{Z}^2$, zero bank $b = 0$, and insufficient bank $b < \Delta$),
   $$F_{\mathrm{axis}, -\epsilon}(F_{\mathrm{axis}, \epsilon}(s)) = s \qquad \text{and} \qquad F_{\mathrm{axis}, \epsilon}(F_{\mathrm{axis}, -\epsilon}(s)) = s.$$
   Hence $F_{\mathrm{axis}, \epsilon}$ is a bijection on $\mathcal{S}$ with inverse $F_{\mathrm{axis}, -\epsilon}$, and never merges distinct complete states.

*Proof.*
(1) If $b \ge \Delta$, then $b' = b - \Delta \ge 0$, so $b' \in \mathbb{N}_0$, and $H(x') + b' = (H(x) + \Delta) + (b - \Delta) = H(x) + b = E(s)$. By Lemma 1.1(2), $u' - v' = u - v$. If $b < \Delta$, then $x' = x$ and $b' = b \in \mathbb{N}_0$, so $E(s)$ and $u - v$ are unchanged. In both cases $\eta$ and $c$ are untouched.

(2) Let $s = (x, b, \sigma, \eta, c) \in \mathcal{S}$, $h = \epsilon \sigma$, $x' = T_h(x)$, and $\Delta = H(x') - H(x)$. We evaluate $F_{\mathrm{axis}, -\epsilon}(F_{\mathrm{axis}, \epsilon}(s))$ in the two mutually exclusive cases:

- **Case A (Accepted step at $s$: $b \ge \Delta$).**
  Here $s_1 := F_{\mathrm{axis}, \epsilon}(s) = (x', b_1, \sigma_1, \eta, c)$ with $b_1 = b - \Delta \in \mathbb{N}_0$ and $\sigma_1 = \sigma$.
  When $F_{\mathrm{axis}, -\epsilon}$ is applied to $s_1$, the trial sign is
  $$h_1 = (-\epsilon) \sigma_1 = -\epsilon \sigma = -h.$$
  By Lemma 1.1(1), the candidate integer tuple from $x'$ is
  $$x'' = T_{h_1}(x') = T_{-h}(T_h(x)) = x.$$
  The required cost increment at $s_1$ is
  $$\Delta_1 = H(x'') - H(x') = H(x) - H(x') = -\Delta.$$
  Since $b \in \mathbb{N}_0$ satisfies $b \ge 0$, the bank at $s_1$ satisfies
  $$b_1 - \Delta_1 = (b - \Delta) - (-\Delta) = b \ge 0 \implies b_1 \ge \Delta_1.$$
  Therefore $F_{\mathrm{axis}, -\epsilon}$ at $s_1$ **always takes the accepted branch**, producing state $(x'', b_1 - \Delta_1, \sigma_1, \eta, c) = (x, b, \sigma, \eta, c) = s$.

- **Case B (Rejected step at $s$: $b < \Delta$).**
  Here $s_1 := F_{\mathrm{axis}, \epsilon}(s) = (x, b, -\sigma, \eta, c)$.
  When $F_{\mathrm{axis}, -\epsilon}$ is applied to $s_1$, both the requested sign and the retained direction sign are negated relative to $s$, so their product is identical to the trial sign at $s$:
  $$h_1 = (-\epsilon)(-\sigma) = \epsilon \sigma = h.$$
  Because the integer state at $s_1$ is still $x$, the candidate tuple is $T_{h_1}(x) = T_h(x) = x'$, and the required cost increment is $\Delta_1 = H(x') - H(x) = \Delta$.
  Since the bank at $s_1$ is still $b < \Delta = \Delta_1$, $F_{\mathrm{axis}, -\epsilon}$ at $s_1$ **also takes the rejected branch**, keeping $(x, b, \eta, c)$ and flipping $-\sigma \mapsto -(-\sigma) = \sigma$, which returns $(x, b, \sigma, \eta, c) = s$.

Replacing $\epsilon$ with $-\epsilon$ yields $F_{\mathrm{axis}, \epsilon}(F_{\mathrm{axis}, -\epsilon}(s)) = s$. $\square$

### 1.3 Autonomous step $U_*$ and its inverse $U_*^{-1}$

Define the 4-phase controller schedule $L(c, \eta) = (\mathrm{axis}(c), \epsilon(c, \eta))$ by
$$L(0, \eta) = (Q, +1), \quad L(1, \eta) = (P, \eta), \quad L(2, \eta) = (Q, -1), \quad L(3, \eta) = (P, -\eta),$$
and define the clock shift $\tau(x, b, \sigma, \eta, c) = (x, b, \sigma, \eta, (c + 1) \bmod 4)$.
Then $U_*(s) = \tau(F_{L(c, \eta)}(s))$.

**Corollary 1.3 (Autonomous permutation and inverse).**
$U_* : \mathcal{S} \to \mathcal{S}$ is a bijection preserving $E(s)$, $u - v$, and $\eta$. Its exact two-sided inverse on $s' = (x', b', \sigma', \eta, c')$ is
$$U_*^{-1}(s') = F_{\mathrm{axis}(c_{\mathrm{prev}}), -\epsilon(c_{\mathrm{prev}}, \eta)}(x', b', \sigma', \eta, c_{\mathrm{prev}}), \qquad c_{\mathrm{prev}} = (c' - 1) \bmod 4.$$

*Proof.*
Since $F_{L(c, \eta)}$ preserves $c$ and $\eta$, applying $\tau^{-1}$ to $s' = U_*(s)$ recovers $c_{\mathrm{prev}} = c$ and $\eta$. By Theorem 1.2(2), applying $F_{\mathrm{axis}(c), -\epsilon(c, \eta)}$ then recovers $s$. The converse composition $U_*(U_*^{-1}(s')) = s'$ holds identically. $\square$

---

## 2. Attack 2: Two Independent Transition Formulas and Complete $E \le 12$ Shell Enumeration

### 2.1 Algebraic expansion of $\Delta_Q$ and $\Delta_P$

**Proposition 2.1 (Expanded polynomial increments).**
For any $(q, p, u, v) \in \mathbb{Z}^4$ and $h \in \{+1, -1\}$ (so $h^2 = 1$):
1. $\Delta_Q(q, h) := H(Q_h(q, p, u, v)) - H(q, p, u, v) = 2 h q + 1$.
2. $\Delta_P(q, p, u, v, h) := H(P_h(q, p, u, v)) - H(q, p, u, v) = 2 h p + 1 + 2 h q (u + v) + 2 q^2$.

*Proof.*
Using $h^2 = 1$:
$$\Delta_Q(q, h) = (q + h)^2 - q^2 = 2 h q + h^2 = 2 h q + 1,$$
$$\begin{aligned}
\Delta_P(q, p, u, v, h) &= \big((p + h)^2 - p^2\big) + \big((u + h q)^2 - u^2\big) + \big((v + h q)^2 - v^2\big) \\
&= (2 h p + h^2) + (2 h u q + h^2 q^2) + (2 h v q + h^2 q^2) \\
&= 2 h p + 1 + 2 h q (u + v) + 2 q^2. \quad \square
\end{aligned}$$

### 2.2 First-principles derivation of the $E \le 12$ state and gate inventory

**Theorem 2.2 (Exact cardinality of the $E \le 12$ shell).**
1. Every state $s = (q, p, u, v, b, \sigma, \eta, c) \in \mathcal{S}$ with $E(s) = q^2 + p^2 + u^2 + v^2 + b \le 12$ lies in the integer coordinate box $(q, p, u, v) \in [-3, 3]^4$.
2. The exact number of complete raw states with $E(s) \le 12$ is `57680`, giving $4 \times 57680 = 230720$ elementary gate evaluations.

*Proof.*
(1) Since $p^2, u^2, v^2, b \ge 0$, any state with $E(s) \le 12$ has $q^2 \le 12$. For $q \in \mathbb{Z}$, $q^2 \le 12 \iff |q| \le \lfloor\sqrt{12}\rfloor = 3$ (as $4^2 = 16 > 12$). Symmetry gives $|q|, |p|, |u|, |v| \le 3$, so $[-3, 3]^4$ is strictly exhaustive.

(2) Let $r_1(n) = \#\{x \in \mathbb{Z} : x^2 = n\}$. For $0 \le n \le 12$, $r_1(0) = 1$, $r_1(1) = r_1(4) = r_1(9) = 2$, and $r_1(n) = 0$ otherwise. Form the truncated generating polynomial
$$f(t) = 1 + 2 t + 2 t^4 + 2 t^9.$$
Squaring $f(t)$ modulo $t^{13}$ gives the number $r_2(m)$ of pairs $(x, y) \in \mathbb{Z}^2$ with $x^2 + y^2 = m$ for $m \le 12$:
$$f(t)^2 \equiv 1 + 4 t + 4 t^2 + 4 t^4 + 8 t^5 + 4 t^8 + 4 t^9 + 8 t^{10} \pmod{t^{13}}.$$
Convolving $f(t)^2$ with itself modulo $t^{13}$ yields $r_4(H) = \#\{(q, p, u, v) \in \mathbb{Z}^4 : q^2 + p^2 + u^2 + v^2 = H\}$ for each $H \in \{0, \dots, 12\}$. For each such tuple, $0 \le b \le 12 - H$ admits $13 - H$ nonnegative integer banks $b$, and $(\sigma, \eta, c) \in \{+1,-1\}^2 \times C_4$ admits $2 \times 2 \times 4 = 16$ control states:

| $H$ | Decomposition of $[t^H](f(t)^2)^2$ | $r_4(H)$ | $13 - H$ | $(x, b)$ tuples $r_4(H)(13-H)$ | Full states $\times 16$ |
|---:|---|---:|---:|---:|---:|
| $0$ | $1 \cdot 1$ | $1$ | $13$ | $13$ | $208$ |
| $1$ | $2(1 \cdot 4)$ | $8$ | $12$ | $96$ | $1536$ |
| $2$ | $2(1 \cdot 4) + 4^2$ | $24$ | $11$ | $264$ | $4224$ |
| $3$ | $2(4 \cdot 4)$ | $32$ | $10$ | $320$ | $5120$ |
| $4$ | $2(1 \cdot 4) + 4^2$ | $24$ | $9$ | $216$ | $3456$ |
| $5$ | $2(1 \cdot 8) + 2(4 \cdot 4)$ | $48$ | $8$ | $384$ | $6144$ |
| $6$ | $2(4 \cdot 8) + 2(4 \cdot 4)$ | $96$ | $7$ | $672$ | $10752$ |
| $7$ | $2(4 \cdot 8)$ | $64$ | $6$ | $384$ | $6144$ |
| $8$ | $2(1 \cdot 4) + 4^2$ | $24$ | $5$ | $120$ | $1920$ |
| $9$ | $2(1 \cdot 4) + 2(4 \cdot 4) + 2(4 \cdot 8)$ | $104$ | $4$ | $416$ | $6656$ |
| $10$ | $2(1 \cdot 8) + 2(4 \cdot 4) + 2(4 \cdot 4) + 8^2$ | $144$ | $3$ | $432$ | $6912$ |
| $11$ | $2(4 \cdot 8) + 2(4 \cdot 4)$ | $96$ | $2$ | $192$ | $3072$ |
| $12$ | $2(4 \cdot 8) + 2(4 \cdot 4)$ | $96$ | $1$ | $96$ | $1536$ |
| **Total** | | **$781$** | | **$3605$** | **$57680$** |

Multiplying `57680` states by the $4$ elementary gates $(Q_+, Q_-, P_+, P_-)$ yields `230720` gate evaluations. $\square$

*(Note: By the exact same table truncated at $H \le 6$ with factor $7 - H$, the single shell $E(s) = 6$ has $\sum_{H=0}^6 r_4(H) = 1 + 8 + 24 + 32 + 24 + 48 + 96 = 233$ integer tuples, $233 \times 8 = 1864$ states per fixed $\eta$, and $233 \times 16 = 3728$ states across both $\eta \in \{+1, -1\}$.)*

---

## 3. Attack 3: Area / Record Equation and Classification of Unprepared / Zero Reference Failures

### 3.1 Exact path-sum law across arbitrary actual trajectories (including rejections)

Let $s_0, s_1, \dots, s_N$ be the trajectory generated from any initial state $s_0 = (q_0, p_0, u_0, v_0, b_0, \sigma_0, \eta, c_0) \in \mathcal{S}$ by any sequence of $N \ge 0$ elementary gates $F_{\mathrm{axis}_i, \epsilon_i}$. Define the actual base displacements
$$\Delta q_i := q_{i+1} - q_i \in \{-1, 0, +1\}, \qquad \Delta p_i := p_{i+1} - p_i \in \{-1, 0, +1\},$$
and the path sums
$$A_{\mathrm{path}} := \sum_{i=0}^{N-1} q_i \Delta p_i, \qquad A_2 := \sum_{i=0}^{N-1} (q_i p_{i+1} - p_i q_{i+1}).$$

**Theorem 3.1 (General reference evolution and shoelace relation).**
Along every actual trajectory $s_0, \dots, s_N$ (with arbitrary accepted and rejected steps):
1. $u_N = u_0 + A_{\mathrm{path}}$ and $v_N = v_0 + A_{\mathrm{path}}$.
2. $2 A_{\mathrm{path}} = A_2 + (q_N p_N - q_0 p_0)$. In particular, if $q_0 = p_0 = 0$, then $2 A_{\mathrm{path}} = A_2 + q_N p_N$, and if the base path closes at the origin ($q_N = p_N = 0$), then $2 A_{\mathrm{path}} = A_2$.
3. The endpoint reference cost difference and sum for arbitrary initial $(u_0, v_0) \in \mathbb{Z}^2$ are
   $$u_N^2 - v_N^2 = (u_0^2 - v_0^2) + 2(u_0 - v_0) A_{\mathrm{path}}, \qquad u_N^2 + v_N^2 = (u_0^2 + v_0^2) + 2(u_0 + v_0) A_{\mathrm{path}} + 2 A_{\mathrm{path}}^2.$$

*Proof.*
(1) At each step $i$, there are three possibilities:
- Step $i$ is rejected: $q_{i+1} = q_i$, $p_{i+1} = p_i$ ($\Delta p_i = 0$), and $u_{i+1} = u_i = u_i + q_i \Delta p_i$, $v_{i+1} = v_i = v_i + q_i \Delta p_i$.
- Step $i$ is an accepted $Q_h$ gate: $q_{i+1} = q_i + h$, $p_{i+1} = p_i$ ($\Delta p_i = 0$), and $u_{i+1} = u_i = u_i + q_i \Delta p_i$, $v_{i+1} = v_i = v_i + q_i \Delta p_i$.
- Step $i$ is an accepted $P_h$ gate: $q_{i+1} = q_i$, $p_{i+1} = p_i + h$ ($\Delta p_i = h$), and $u_{i+1} = u_i + h q_i = u_i + q_i \Delta p_i$, $v_{i+1} = v_i + h q_i = v_i + q_i \Delta p_i$.

In all three cases, $u_{i+1} - u_i = v_{i+1} - v_i = q_i \Delta p_i$. Summing over $0 \le i < N$ gives $u_N = u_0 + A_{\mathrm{path}}$ and $v_N = v_0 + A_{\mathrm{path}}$.

(2) In every elementary step, at most one of $\Delta q_i, \Delta p_i$ is nonzero, so $\Delta q_i \Delta p_i = 0$. Therefore
$$q_{i+1} p_{i+1} - q_i p_i = (q_i + \Delta q_i)(p_i + \Delta p_i) - q_i p_i = q_i \Delta p_i + p_i \Delta q_i,$$
$$q_i p_{i+1} - p_i q_{i+1} = q_i(p_i + \Delta p_i) - p_i(q_i + \Delta q_i) = q_i \Delta p_i - p_i \Delta q_i.$$
Adding these two identities gives $2 q_i \Delta p_i = (q_i p_{i+1} - p_i q_{i+1}) + (q_{i+1} p_{i+1} - q_i p_i)$. Summing over $0 \le i < N$ telescopes the second sum to $q_N p_N - q_0 p_0$.

(3) Expanding $(u_0 + A_{\mathrm{path}})^2 \mp (v_0 + A_{\mathrm{path}})^2$ yields the stated formulas. $\square$

### 3.2 Specialization to $(u_0, v_0) = (1, -1)$ and failure classification on unprepared references

**Corollary 3.2 (Exact characterization of when $A_{\mathrm{read}} := (u_N^2 - v_N^2)/4$ equals $A_{\mathrm{path}}$).**
By Theorem 3.1(3),
$$\frac{u_N^2 - v_N^2}{4} = \frac{u_0^2 - v_0^2}{4} + \frac{u_0 - v_0}{2} A_{\mathrm{path}}.$$
Consequently, the uncalibrated quadratic difference reader $A_{\mathrm{read}} = (u_N^2 - v_N^2)/4$ equals $A_{\mathrm{path}}$ for all $A_{\mathrm{path}} \in \mathbb{Z}$ **if and only if**
$$u_0^2 - v_0^2 = 0 \quad \text{and} \quad u_0 - v_0 = 2 \iff (u_0, v_0) = (1, -1).$$
Outside $(u_0, v_0) = (1, -1)$, the reader fails in three distinct ways:
1. **Equal references ($u_0 = v_0$, including the zero-reference control $u_0 = v_0 = 0$):**
   Here $u_0 - v_0 = 0$, so $u_N = v_N = u_0 + A_{\mathrm{path}}$ and $u_N^2 - v_N^2 = 0$ identically. At $(u_0, v_0) = (0, 0)$, $u_N^2 = v_N^2 = A_{\mathrm{path}}^2$, which destroys the orientation sign $\mathrm{sgn}(A_{\mathrm{path}})$.
2. **Non-antipodal unequal references ($u_0 \ne v_0$ and $u_0 + v_0 \ne 0$):**
   Here $u_0^2 - v_0^2 \ne 0$, introducing a constant additive bias $(u_0^2 - v_0^2)/4 \ne 0$ even at $A_{\mathrm{path}} = 0$ (for example, $(u_0, v_0) = (2, 0)$ gives $(u_N^2 - v_N^2)/4 = 1 + A_{\mathrm{path}} \ne A_{\mathrm{path}}$).
3. **Antipodal references with non-unit half-gap ($u_0 = -v_0 = d \in \mathbb{Z} \setminus \{0, 1\}$):**
   Here $u_0^2 - v_0^2 = 0$ but $(u_N^2 - v_N^2)/4 = d A_{\mathrm{path}} \ne A_{\mathrm{path}}$ for $A_{\mathrm{path}} \ne 0$ (in particular, swapped preparation $(u_0, v_0) = (-1, 1)$ negates the reading: $A_{\mathrm{read}} = -A_{\mathrm{path}}$).

---

## 4. Attack 4: Chronological Weyl Word and Open-Path vs. Closed-Path Conventions

Let $\mathcal{H}_5 = \bigoplus_{k \in \mathbb{Z}_5} \mathbb{C}|k\rangle$ with primitive fifth root $j = \zeta_5^2$ ($j^5 = 1$). Define
$$X^a |k\rangle = |k + a \bmod 5\rangle, \qquad Z^b |k\rangle = j^{b k} |k\rangle \qquad (a, b \in \mathbb{Z}, \; k \in \mathbb{Z}_5).$$
Notice the Weyl commutation relation:
$$Z^b X^a |k\rangle = Z^b |k + a\rangle = j^{b(k + a)} |k + a\rangle = j^{a b} X^a Z^b |k\rangle \implies Z^b X^a = j^{a b} X^a Z^b.$$

Along an actual trajectory $s_0, s_1, \dots, s_N$ with step displacements $\Delta q_i = q_{i+1} - q_i$ and $\Delta p_i = p_{i+1} - p_i$, the single-step Weyl operator is
$$U_{\mathrm{step}\,i} = \begin{cases} X^{\Delta q_i} & \text{if step } i \text{ is an accepted } Q \text{ move } (\Delta p_i = 0), \\ Z^{\Delta p_i} & \text{if step } i \text{ is an accepted } P \text{ move } (\Delta q_i = 0), \\ I & \text{if step } i \text{ is rejected } (\Delta q_i = \Delta p_i = 0). \end{cases}$$
Because $\Delta q_i \Delta p_i = 0$ at every step, $U_{\mathrm{step}\,i} = Z^{\Delta p_i} X^{\Delta q_i} = X^{\Delta q_i} Z^{\Delta p_i}$ unambiguously for each individual step. The chronological product acting on previous basis images is defined inductively by $W_0 = I$ and $W_{i+1} = U_{\mathrm{step}\,i} W_i$.

**Theorem 4.1 (Exact chronological Weyl action on open and closed paths).**
For any trajectory $s_0, \dots, s_N$ starting at arbitrary $(q_0, p_0) \in \mathbb{Z}^2$, let $\Delta q_{\mathrm{tot}} = q_N - q_0$ and $\Delta p_{\mathrm{tot}} = p_N - p_0$. Then for every basis index $k \in \mathbb{Z}_5$:
$$W_N |k\rangle = j^{k(p_N - p_0) + \sum_{i=0}^{N-1} (q_i - q_0)\Delta p_i} |k + (q_N - q_0) \bmod 5\rangle = j^{k \Delta p_{\mathrm{tot}} + A_{\mathrm{path}} - q_0 \Delta p_{\mathrm{tot}}} |k + \Delta q_{\mathrm{tot}} \bmod 5\rangle.$$
In particular:
1. **Basepoint at the origin ($q_0 = p_0 = 0$):**
   $$W_N |k\rangle = j^{k p_N + A_{\mathrm{path}}} |k + q_N \bmod 5\rangle \qquad \forall k \in \mathbb{Z}_5.$$
2. **Integer-closed base paths ($q_N = q_0$ and $p_N = p_0$):**
   Here $\Delta q_{\mathrm{tot}} = \Delta p_{\mathrm{tot}} = 0$, so the basepoint correction $-q_0 \Delta p_{\mathrm{tot}}$ and the basis-dependent exponent $k \Delta p_{\mathrm{tot}}$ both vanish, yielding the basepoint-independent scalar operator
   $$W_N = j^{A_{\mathrm{path}}} I.$$
   If in addition $(u_0, v_0) = (1, -1)$, then $W_N = j^{A_{\mathrm{read}}} I$.

*Proof.*
We prove the formula for $W_i |k\rangle$ by induction on $i \ge 0$. For $i = 0$, $q_0 - q_0 = p_0 - p_0 = 0$ and the empty sum is $0$, so $W_0 |k\rangle = |k\rangle$.
Suppose the formula holds at step $i$, so $W_i |k\rangle = j^{\Phi_i(k)} |k + (q_i - q_0) \bmod 5\rangle$ where $\Phi_i(k) = k(p_i - p_0) + \sum_{m=0}^{i-1} (q_m - q_0)\Delta p_m$.
- If step $i$ is rejected ($\Delta q_i = \Delta p_i = 0$), $U_{\mathrm{step}\,i} = I$, $q_{i+1} = q_i$, $p_{i+1} = p_i$, and $\Phi_{i+1}(k) = \Phi_i(k)$.
- If step $i$ is an accepted $Q$ move ($\Delta q_i = h$, $\Delta p_i = 0$), $U_{\mathrm{step}\,i} = X^h$ shifts $|k + (q_i - q_0)\rangle \mapsto |k + (q_{i+1} - q_0)\rangle$ while leaving $p_{i+1} = p_i$ and $\Phi_{i+1}(k) = \Phi_i(k)$ unchanged.
- If step $i$ is an accepted $P$ move ($\Delta q_i = 0$, $\Delta p_i = h$), $U_{\mathrm{step}\,i} = Z^h$ multiplies $|k + (q_i - q_0)\rangle$ by
  $$j^{h(k + q_i - q_0)} = j^{k \Delta p_i + (q_i - q_0)\Delta p_i},$$
  so the new phase exponent is $\Phi_i(k) + k \Delta p_i + (q_i - q_0)\Delta p_i = \Phi_{i+1}(k)$ while $q_{i+1} = q_i$. $\square$

**Open-path phase convention classification:**
On an open path where $(q_N, p_N) \ne (q_0, p_0)$, $W_N$ is **not** a scalar phase:
- When $q_N \not\equiv q_0 \pmod 5$, $W_N$ permutes the basis states without fixed points.
- When $q_N \equiv q_0 \pmod 5$ but $p_N \not\equiv p_0 \pmod 5$, $W_N$ is diagonal with basis-dependent eigenvalues $j^{k(p_N - p_0) + A_{\mathrm{path}} - q_0(p_N - p_0)}$.
- Comparing $W_N$ to the normal-ordered endpoint operator $Z^{\Delta p_{\mathrm{tot}}} X^{\Delta q_{\mathrm{tot}}}$ (which sends $|k\rangle \mapsto j^{(k + \Delta q_{\mathrm{tot}})\Delta p_{\mathrm{tot}}} |k + \Delta q_{\mathrm{tot}}\rangle$) gives a relative phase $j^{A_{\mathrm{path}} - q_0 \Delta p_{\mathrm{tot}} - \Delta q_{\mathrm{tot}} \Delta p_{\mathrm{tot}}}$, whereas comparing to $X^{\Delta q_{\mathrm{tot}}} Z^{\Delta p_{\mathrm{tot}}}$ (which sends $|k\rangle \mapsto j^{k \Delta p_{\mathrm{tot}}} |k + \Delta q_{\mathrm{tot}}\rangle$) gives $W_N = j^{A_{\mathrm{path}} - q_0 \Delta p_{\mathrm{tot}}} X^{\Delta q_{\mathrm{tot}}} Z^{\Delta p_{\mathrm{tot}}}$. Only when $\Delta q_{\mathrm{tot}} \equiv \Delta p_{\mathrm{tot}} \equiv 0 \pmod 5$ (and in particular on integer-closed paths $\Delta q_{\mathrm{tot}} = \Delta p_{\mathrm{tot}} = 0$) do all open-path conventions collapse to the single scalar $j^{A_{\mathrm{path}}} I$.

---

## 5. Attack 5: Observational Obstruction at $B = 4$ and Reader-Exposure Scope Guard

**Proposition 5.1 (Exact four-step trajectories from $s_{4, \eta}$).**
For $\eta \in \{+1, -1\}$, starting from $s_{4, \eta} = (0, 0, 1, -1, 4, +1, \eta, 0)$, all four autonomous steps of $U_*$ are accepted:
- $t = 0$: $(0, 0, 1, -1, 4, +1, \eta, 0)$, with $(q^2+p^2, u^2+v^2, H, b, \sigma, c) = (0, 2, 2, 4, +1, 0)$.
- $t = 1$ ($Q_+$): $(1, 0, 1, -1, 3, +1, \eta, 1)$, with $(q^2+p^2, u^2+v^2, H, b, \sigma, c) = (1, 2, 3, 3, +1, 1)$.
- $t = 2$ ($P_\eta$): $(1, \eta, 1+\eta, -1+\eta, 0, +1, \eta, 2)$. Since $(1+\eta)^2 + (-1+\eta)^2 = 2 + 2\eta^2 = 4$ for both $\eta \in \{+1, -1\}$, $(q^2+p^2, u^2+v^2, H, b, \sigma, c) = (2, 4, 6, 0, +1, 2)$.
- $t = 3$ ($Q_-$): $(0, \eta, 1+\eta, -1+\eta, 1, +1, \eta, 3)$, with $(q^2+p^2, u^2+v^2, H, b, \sigma, c) = (1, 4, 5, 1, +1, 3)$.
- $t = 4$ ($P_{-\eta}$): $(0, 0, 1+\eta, -1+\eta, 2, +1, \eta, 0)$, with $(q^2+p^2, u^2+v^2, H, b, \sigma, c) = (0, 4, 4, 2, +1, 0)$.

At $t = 4$, the ordered reference costs $(E_+, E_-) = (u_4^2, v_4^2)$ are $(4, 0)$ for $\eta = +1$ and $(0, 4)$ for $\eta = -1$, so $A_{\mathrm{read}} = \eta$ and $W_{\mathrm{path}} = j^\eta I$.

**Mandatory Scope Guard:**
The observational obstruction is strictly limited to coarse observers that receive only $(q^2+p^2, u^2+v^2, H, b, \sigma, c)$. If a reader is given access to:
1. the program bit $\eta$,
2. the ordered cost pair $(u^2, v^2)$ (or $u^2 - v^2$) at $t \in \{2, 3, 4\}$,
3. the linear reference values $(u, v)$ at $t \in \{2, 3, 4\}$, or
4. the signed momentum coordinate $p_t = \eta$ at $t \in \{2, 3\}$,
then $\eta = +1$ and $\eta = -1$ are immediately distinguishable.

---

## 6. Attack 6: Resource Threshold, Five-Lap Witness, Controls, Recurrence, and Hidden-Resource Audit

### 6.1 Exact funding threshold $B_{\min}(K) = 2 K^2 + 2$

**Theorem 6.1 (Necessary and sufficient initial bank for $K$ accepted squares).**
For every integer $K \ge 1$ and $\eta \in \{+1, -1\}$, all $4K$ autonomous steps starting from $s_{B, \eta} = (0, 0, 1, -1, B, +1, \eta, 0)$ are accepted if and only if
$$B \ge B_{\min}(K) := 2 K^2 + 2.$$
When $B \ge 2 K^2 + 2$, the state at step $4K$ is
$$s_{4K} = (0, 0, 1 + \eta K, -1 + \eta K, B - 2 K^2, +1, \eta, 0), \qquad A_{\mathrm{path}} = A_{\mathrm{read}} = \eta K, \qquad W_{\mathrm{path}} = j^{\eta K} I.$$

*Proof.*
Along the unrejected trajectory from $s_{B, \eta}$, during lap $k \in \{1, \dots, K\}$ (steps $4k - 3, 4k - 2, 4k - 1, 4k$), the integer coordinates and state costs $H_t$ are:
- $t = 4k - 3$ ($Q_+$ from $q=0$ to $q=1$ with $u = 1 + (k-1)\eta, v = -1 + (k-1)\eta$):
  $$H_{4k-3} = 1^2 + 0^2 + 2 + 2(k-1)^2 = 2(k-1)^2 + 3.$$
- $t = 4k - 2$ ($P_\eta$ at $q=1$ to $p=\eta$, shifting $u, v$ to $1 + k\eta, -1 + k\eta$):
  $$H_{4k-2} = 1^2 + \eta^2 + (1 + k\eta)^2 + (-1 + k\eta)^2 = 2 + (2 + 2 k^2) = 2 k^2 + 4.$$
- $t = 4k - 1$ ($Q_-$ from $q=1$ to $q=0$ at $p=\eta$):
  $$H_{4k-1} = 0^2 + \eta^2 + 2 + 2 k^2 = 2 k^2 + 3.$$
- $t = 4k$ ($P_{-\eta}$ at $q=0$ from $p=\eta$ to $p=0$, leaving $u, v$ unchanged):
  $$H_{4k} = 0^2 + 0^2 + 2 + 2 k^2 = 2 k^2 + 2.$$

Because $E(s_t) = H_t + b_t = E(s_0) = B + 2$ is invariant, step $t$ is accepted if and only if $b_{t-1} \ge H_t - H_{t-1} \iff B + 2 - H_t \ge 0 \iff B + 2 \ge H_t$.
Thus all $4K$ steps are accepted if and only if
$$B + 2 \ge \max_{1 \le t \le 4K} H_t.$$
On each lap $k \ge 1$, the maximum of $\{2(k-1)^2 + 3, 2 k^2 + 4, 2 k^2 + 3, 2 k^2 + 2\}$ is $2 k^2 + 4$ (attained at step $t = 4k - 2$, the upper-right corner $(q, p) = (1, \eta)$ of lap $k$). Since $k \mapsto 2 k^2 + 4$ is strictly increasing for $k \ge 1$,
$$\max_{1 \le t \le 4K} H_t = H_{4K-2} = 2 K^2 + 4.$$
Hence all $4K$ steps are accepted if and only if $B + 2 \ge 2 K^2 + 4 \iff B \ge 2 K^2 + 2$. $\square$

### 6.2 Five-lap $K=5, B=52$ witness and controls ($B=3$ and zero-reference)

1. **Five-lap witness ($K=5, B=52, \eta=+1$):**
   By Theorem 6.1, $B_{\min}(5) = 2(5^2) + 2 = 52$, so at $B = 52$ all $20$ steps are accepted, with peak state cost $H_{18} = 54 = E(s_0)$ (bank $b_{18} = 0$ at step $18$). At step $20$:
   $$(q_{20}, p_{20}, u_{20}, v_{20}, b_{20}, \sigma_{20}, \eta, c_{20}) = (0, 0, 6, 4, 2, +1, +1, 0),$$
   ordered reference costs $(E_+, E_-) = (36, 16)$, $A_{\mathrm{read}} = (36 - 16)/4 = 5$, paid reference work $(36 + 16) - 2 = 50$, and $W_{\mathrm{path}} = j^5 I = I$. Thus $W_{\mathrm{path}} = I$ does not reset the reference registers or refund the $50$ units of work.
2. **Nominal $B=3$ insufficient-budget control:**
   Starting from $s_{3, \eta} = (0, 0, 1, -1, 3, +1, \eta, 0)$ ($E = 5$):
   - Step 0 ($c=0, Q_+, h=+1$): candidate $(1, 0, 1, -1)$ has $H=3 \le 5$, accepted $\to (1, 0, 1, -1, 2, +1, \eta, 1)$.
   - Step 1 ($c=1, P_\eta, h=\eta$): candidate $(1, \eta, 1+\eta, -1+\eta)$ has $H=6 > 5$, **rejected** $\to (1, 0, 1, -1, 2, -1, \eta, 2)$.
   - Step 2 ($c=2, Q_-$): because $\sigma = -1$, the actual trial step is $h = (-1)(-1) = +1$ ($Q_{+1}$ to $q=2$), which has $H = 4 + 0 + 2 = 6 > 5$, **rejected** $\to (1, 0, 1, -1, 2, +1, \eta, 3)$.
   - Step 3 ($c=3, P_{-\eta}$): with $\sigma = +1$, $h = -\eta$ at $q=1$ has candidate $(1, -\eta, 1-\eta, -1-\eta)$ with $H = 6 > 5$, **rejected** $\to (1, 0, 1, -1, 2, -1, \eta, 0)$.
   Thus after 4 steps, $(q_4, p_4) = (1, 0) \ne (0, 0)$, $A_{\mathrm{path}} = A_{\mathrm{read}} = 0$, and $W_{\mathrm{path}} = X^1 \ne j^\eta I$.
3. **Zero-reference controls $(0, 0, 0, 0, 4, +1, \eta, 0)$:**
   With $u_0 = v_0 = 0$ and $B = 4$ ($E = 4$), the 4-step candidates have $H_1 = 1$, $H_2 = 1 + 1 + 1 + 1 = 4 \le 4$, $H_3 = 3$, $H_4 = 2$, so all 4 steps are accepted and end at $(0, 0, \eta, \eta, 2, +1, \eta, 0)$. Both $\eta = +1$ and $\eta = -1$ yield identical endpoint reference cost pairs $(u_4^2, v_4^2) = (1, 1)$ and $u_4^2 - v_4^2 = 0$.

### 6.3 Finite-energy periodicity, record capacity bound, and hidden-resource audit

**Theorem 6.2 (Finite shells, pure periodicity, capacity bound, and finite control memory).**
1. **Finite shells and pure periodicity:** For each $N \in \mathbb{N}_0$, the energy shell $\mathcal{S}_N := \{s \in \mathcal{S} : E(s) = N\}$ is finite of cardinality at most $16(2\lfloor\sqrt{N}\rfloor + 1)^4$. Because $U_*$ is a bijection on $\mathcal{S}$ that preserves $E(s)$, its restriction to $\mathcal{S}_N$ is a permutation of a finite set; hence every state $s_0 \in \mathcal{S}$ is purely periodic under $U_*$ (its forward orbit repeats for the first time at $s_0$ itself).
2. **Record-capacity bound on the prepared slice:** On the invariant slice $u - v = 2$ at total energy $E = B + 2$ (containing $s_{B, \eta}$), writing $A_{\mathrm{read}} = (u^2 - v^2)/4 = (u - 1)$ gives $u = 1 + A_{\mathrm{read}}$ and $v = -1 + A_{\mathrm{read}}$, so
   $$2 + 2 A_{\mathrm{read}}^2 = u^2 + v^2 \le H(s) \le E = B + 2 \implies |A_{\mathrm{read}}| \le \left\lfloor \sqrt{\frac{B}{2}} \right\rfloor.$$
   Thus at fixed initial stock $B$, $A_{\mathrm{read}}$ can assume at most $2\lfloor\sqrt{B/2}\rfloor + 1$ distinct integer values.
3. **Scope of period `124` on $E = 6$:** Period `124` is the orbit length of the specific initial states $s_{4, +1}$ and $s_{4, -1}$ on $\mathcal{S}_6$, not a universal period of the $\mathcal{S}_6$ shell. For example, the state $s_{\mathrm{refl}} = (0, 0, 2, 1, 1, +1, +1, 0) \in \mathcal{S}_6$ ($H = 5, b = 1$) or states with $H = 6, b = 0$ where high-cost moves reject have shorter cycle lengths, which `break.py` enumerates exhaustively by decomposing all `3728` states of $\mathcal{S}_6$ into disjoint cycles.
4. **Audit of zero-cost control coordinates $(\sigma, \eta, c)$:** The coordinates $(\sigma, \eta, c) \in \{+1, -1\}^2 \times C_4$ contribute $0$ to $H(s) = q^2 + p^2 + u^2 + v^2$. They DO act as a **4-bit ($16$-state) zero-cost control memory** ($\sigma$ stores the 1-bit reflection state from rejected moves, $\eta$ stores the 1-bit loop orientation, and $c$ stores the 2-bit controller phase, all of which are required for autonomous inversion $U_*^{-1}$). However, because $\{+1, -1\}^2 \times C_4$ has fixed finite cardinality $16$ independent of trajectory length, it cannot store an unbounded path or area record and does not violate the finite-shell periodicity or capacity bound.
