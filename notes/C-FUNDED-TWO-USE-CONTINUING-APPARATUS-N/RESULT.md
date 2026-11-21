# Result: `C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N`

**NON-CANONICAL / L1 analytical result summary / 2026-10-15 (R1 revision).**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1504](https://github.com/mathorn1973/twist-j/issues/1504), following [#1497#issuecomment-6179898943](https://github.com/mathorn1973/twist-j/issues/1497#issuecomment-6179898943).

```text
candidate_id:               C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N
branch:                     incubation/C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N
base_commit:                8b91a935c426036e00ecb300019fd94734addeec
preregistration_commit:     d4b67e44d14a2f224a0ed77eb8dd08b217711cfb
initial_result_commit:      a1517dd03fd8330a2e46a712b5e813d27bdb04df
canon_tag:                  canon-v101
content_commit:             421a4ec1daf07c04d19022c1ee219607e83c09a8
canon_sha256:               b83a99feccac173bd3c9c5851c5874ca27cbd135f71d136d793b45f86c8a87f7
canon_bytes:                992352
action_layer:               L1 (symbolic mathematical proof over F_5 and Q)
scientific_code_status:     NONE / NOT_RUN
physical_status:            NOT_READY
promotion_recommendation:   DO NOT PROMOTE (keep under notes/C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N/)
```

---

## R1 scientific erratum (descendant correction of `a1517dd03fd8330a2e46a712b5e813d27bdb04df`)

This descendant R1 revision corrects the five analytical defects found in the review of the initial deliverable commit `a1517dd03fd8330a2e46a712b5e813d27bdb04df` on Draft PR [#1505](https://github.com/mathorn1973/twist-j/pull/1505). The four frozen preregistration files (`README.md`, `CONTRACT.md`, `PREREG.md`, `SOURCES.json` from `d4b67e44d14a2f224a0ed77eb8dd08b217711cfb`) remain byte-for-byte unchanged (`0` diff lines).

- **`R1-A` (Exact inverse of $F$):** The misstated formula $u = H v - w_{\mathrm{next}} + 2 P b_{\mathrm{out}}$ in `a1517dd03fd8330a2e46a712b5e813d27bdb04df` (which returns $-2 P e_0 \ne 0$ on the image of $u = v = 0, A_0 = e_0$) is withdrawn and replaced in `PROOF.md` Section 1 (`Theorem 1` Part 2) by the exact inherited inverse from A2 (`c34baa826cb846260b96373ae6d8f10c3a189a5a:notes/C-TWO-USE-CONTROL-ARCHIVE-N/PROOF.md` Section 2, eqs. (2)–(3)):
  $$
  u = K\bigl(H v - J_0 w_{\mathrm{next}} + 4 P b_{\mathrm{out}}\bigr), \qquad A_0 = b_{\mathrm{out}} + \frac{1}{2}P^T(w_{\mathrm{next}} - u).
  $$
- **`R1-B` (Withdrawal of false global bijectivity of $V$; restoration of A2's prepared-image recovery):** The false claims in `a1517dd03fd8330a2e46a712b5e813d27bdb04df` that $g_0, \dots, g_4$ preserve $\operatorname{sum}(x) \bmod 5$ and that $V$ is globally invertible are withdrawn. The generator sum actions are $(z, -z, 2-z, 2-z, 3-z) \pmod 5$, and at $n=0$ ($\theta_0 = 0$) the inputs $x = (0,0,0,0,0,1)$ and $\widetilde{x} = (2,1,3,4,2,2)$ collide at $g_1(x) = g_4(\widetilde{x}) = (0,0,0,0,0,4)$ (`Theorem 2` Part 2). `Theorem 5` Part 5 restores A2's exact prepared-image recovery (`PROOF.md` Sections 3 & 7): on any prepared head $x_0 = (p, 0, 1)$, ticks 4 and 5 apply $g_1$ twice so $x_5 = g_1 g_1 x_3 = x_3$; the five pairwise distinct $C_3(h)$ receivers at $n=5$ decode $h_A, h_B \in \{0,1,2,3,4\}$ directly from $(x_{5,A}, x_{5,B})$; the inverse words $\hat{x}_{0,i} = g_{j_0(h_i)} g_{j_1(h_i)} g_{j_2(h_i)} x_{5,i}$ reconstruct the full inputs; and the ready-image recognizer enforces both $\operatorname{rec}(\hat{x}_{0,i}) = (0,1)$ and the piston-sum selector-consistency check $\sum_{m=0}^3 \hat{x}_{0,i,m} \bmod 5 = h_i$.
- **`R1-C` (Restoration of inherited matrices $J_p, D_3$ and the $R_1 z^{(h)}$ table):** The altered formula $J_p = P^T T P - I_4$, the missing term $\frac{1}{2}P^T T J_0 T S z_A$ in $D_3(z_A)$, and the miscomputed $R_1 z^{(h)}$ table in `a1517dd03fd8330a2e46a712b5e813d27bdb04df` are withdrawn. `Theorem 5` Part 2 restores A2's exact recurrence and matrices (`PROOF.md` Section 5, eqs. (7)–(10)) and `#1489`/`#1492`'s exact $1399680 \, R_1 z^{(h)}$ table:
  $$
  J_p = P^T H P = \frac{1}{54}\bigl(59 I_4 + \mathbf{1}\mathbf{1}^T\bigr), \qquad
  D_3(z_A) = \frac{1}{2}P^T(w_2 - a_4) = \frac{1}{2}P^T\bigl(T^2 - T^4 + T^2 J_0 + T J_0 T\bigr)S z_A,
  $$
  matching $b_3 = -\frac{1}{2}J_p e_0 = (-\frac{5}{9}, -\frac{1}{108}, -\frac{1}{108}, -\frac{1}{108})^T$ at $z_A = z_B = 0, c_0 = 0, c_1 = e_0$.
- **`R1-D` (Restoration of exact source-decoder inverse $R_0^{-1}$):** The erroneous expression $-\frac{36}{59}(5 I_4 + \frac{1}{699}v\mathbf{1}^T)$ (which gives $\frac{5}{6}t \ne t$ on $t = e_0 - e_1$) is withdrawn and replaced in `Theorem 5` Part 3 by the exact inherited formula from A2 (`PROOF.md` Section 5):
  $$
  R_0^{-1} = -4 M^{-1} = -\frac{216}{59}\left(I_4 + \frac{v\mathbf{1}^T}{365}\right), \qquad v = (349, 354, 354, 348)^T.
  $$
- **`R1-E` (Unification of the 7-step completion boundary $c = 7, n = 5$ and exact scope of direction-bit / comparator statements):** From $c = 0, n = 0$, **seven** updates $\mathcal{G}_B^7(Z(0))$ reach the completion boundary $c = 7, n = 5$ (whereas the 8th update $\mathcal{G}_B^8(Z(0))$ executes row $c = 7$ and rotates $c: 7 \mapsto 0$ with $T_7 = \mathrm{id}$). All completion definitions, boundary tables, and the ready-image recognizer now uniformly use $Z(7) = \mathcal{G}_B^7(Z(0))$ at $c = 7, n = 5$. The single-$\sigma$ witness is scoped strictly to direct un-reset substitution of one shared bit $\sigma$ into the two $H_B$ calls (not a general minimality theorem over arbitrary controllers), and the zero-cut comparison at $b_{\mathrm{init}} = B = \frac{1}{5}$ explicitly distinguishes the classical readout $\Pi_{\mathrm{class}} = (X, W, b)$ (where all four pairs $(0,0), (0,3), (3,0), (3,3)$ collide) from $\Pi_{\mathrm{class}+d} = (X, W, b, d)$ (where $d = C_1(h_B)$ separates $h_B = 0$ from $h_B = 3$, while $(0,0)$ collides with $(3,0)$ and $(0,3)$ collides with $(3,3)$ without $(\sigma_A, \sigma_B)_{\mathrm{final}}$).

---

## 1. Proved statements (`PROOF.md` Sections 1–4)

1. **Global bijectivity of apparatus primitives and involutivity of $H_{B,A}, H_{B,B}$ (`Theorem 1` & `Theorem 2`):**
   - On the full composite carrier $\mathcal{Z}_B = \mathbb{N}_0 \times \mathbb{F}_5^6 \times \mathbb{F}_5^6 \times \mathcal{X} \times \mathbb{Q} \times ([0,B]\cap\mathbb{Q}) \times \{\pm 1\}^2 \times \mathbb{F}_5^2 \times (\mathbb{Z}/8\mathbb{Z})$ and the static-source apparatus subcarrier $\mathcal{A}_B$, the delayed-label buffer capture $L_{\mathrm{buf}}(x_B, d) = (x_B, (d + \operatorname{rec}(x_B))\bmod 5)$, the two-tape wave update $F$ (with inverse $u = K(H v - J_0 w_{\mathrm{next}} + 4 P b_{\mathrm{out}}), A_0 = b_{\mathrm{out}} + \frac{1}{2}P^T(w_{\mathrm{next}} - u)$), and the two bounded-store contact maps $H_{B,A}, H_{B,B}$ (with two-sided guards $0 \le b - \Delta_A \le B$ and $0 \le b - \Delta_B \le B$) are global bijections.
   - Both $H_{B,A}^2 = \mathrm{id}$ and $H_{B,B}^2 = \mathrm{id}$ hold globally across all accepted, refused, and occupied wave states $(u, v) \in \mathbb{Q}^D \times \mathbb{Q}^D$, and $G_B(a, c) = (T_c(a), (c+1)\bmod 8)$ is a two-sided permutation on $\mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z})$ (while the selector-defined native tick $V$ is neither surjective nor globally injective on $\mathbb{N}_0 \times \mathbb{F}_5^6 \times \mathbb{F}_5^6$).
2. **Closed-form occupied-wave energy increment $\Delta_B(z_A, z_B)$ and exact 25-pair census (`Theorem 3`):**
   - On any common-ready state in $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ where Contact A (row $c=1$) is accepted ($\alpha_A = 1$), the wave arriving at Contact B (row $c=4$) is $(w_1, w_2) = (T f, (T^2 - J_0)f)$ ($f = S z_A$), which is strictly independent of the old archive $(c_0, c_1)$.
   - Because $w_2 - \frac{1}{2}H w_1 = J_0(\frac{1}{2}H K H f - f)$ and $J_0 g = -\frac{s_B}{5}\delta_{y_4}$ ($g = S z_B$, $s_B = \mathbf{1}^T z_B$), the second-contact wave energy increment factors exactly through the fifth source site $y_4 = (2,0,0)$:
     $$
     \Delta_B(z_A, z_B) = E_0(z_B) + g^T\left(w_2 - \frac{1}{2}H w_1\right) = E_0(z_B) - \frac{s_B (\mu^T z_A)}{10497600}, \qquad \mu = (145483,\, 173653,\, 173653,\, 142153)^T.
     $$
   - Across all $25$ ordered source pairs $(z_A, z_B) \in Z_5 \times Z_5$, $0 \le E_A(z_A) \le \frac{2}{5}$, $-\frac{464619}{13996800} \le g^T(w_2 - \frac{1}{2}H w_1) \le 0$, $0 \le \Delta_B(z_A, z_B) \le \frac{2}{5}$ ($\Delta_B = 0 \iff h_B = 0$), and
     $$
     0 \le W_{\mathrm{final}}(z_A, z_B) = E_A(z_A) + \Delta_B(z_A, z_B) \le W_{\mathrm{final}}(z^{(4)}, z^{(4)}) = \frac{8224427}{10497600} < \frac{4}{5}.
     $$
3. **Input-independent two-use funding condition and four-branch classification (`Theorem 4`):**
   - An input-independent store initialization $(b_{\mathrm{init}}, B)$ accepts both Contact A and Contact B (`(ACC, ACC)`) across all $25$ source pairs in $Z_5 \times Z_5$ and all $625^2 = 390{,}625$ native input pairs $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$ on $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ if and only if
     $$
     B_* := \frac{8224427}{10497600} \le b_{\mathrm{init}} \le B.
     $$
   - In particular, the canonical cold two-use capacity $b_{\mathrm{init}} = B = \frac{4}{5}$ accepts all $25$ source pairs with minimum remaining reserve $b_{\mathrm{final}}(z^{(4)}, z^{(4)}) = \frac{173653}{10497600} > 0$, while $b_{\mathrm{init}} = B = \frac{2}{5}$ partitions $Z_5 \times Z_5$ into $13$ `(ACC, ACC)` and $12$ `(ACC, REF)` pairs, and $b_{\mathrm{init}} = B = \frac{1}{5}$ simultaneously inhabits all four branches: $6$ `(ACC, ACC)`, $9$ `(ACC, REF)`, $6$ `(REF, ACC)`, and $4$ `(REF, REF)`.
4. **Four-cut record retention, archive-independent decoding, and exact prepared-image left inverse (`Theorem 5`):**
   - After 7 updates $\mathcal{G}_B^7(Z(0))$ at the completion boundary $c = 7, n = 5$, all four chronological cuts $(b_0, b_1, b_2, b_3)$ are simultaneously retained in $(A_0, A_1, B_1, B_0) = (b_0, b_1, b_2, b_3)$ and satisfy
     $$
     b_0 = \alpha_A R_0 z_A, \quad b_1 = \alpha_A R_1 z_A, \quad b_2 = \alpha_A D_2(z_A) + \alpha_B R_0 z_B, \quad b_3 = \alpha_A D_3(z_A) + \alpha_B R_1 z_B - \frac{1}{2}J_p c_1,
     $$
     with $J_p = P^T H P = \frac{1}{54}(59 I_4 + \mathbf{1}\mathbf{1}^T)$, $D_2(z_A) = \frac{1}{2}P^T(w_1 - a_3) = \frac{1}{2}P^T(T - T^3 + T J_0)S z_A$, and $D_3(z_A) = \frac{1}{2}P^T(w_2 - a_4) = \frac{1}{2}P^T(T^2 - T^4 + T^2 J_0 + T J_0 T)S z_A$.
   - On `(ACC, ACC)` ($\alpha_A = \alpha_B = 1$, certified by $(\sigma_A, \sigma_B)_{\mathrm{final}} = (-1, -1)$), both sources are uniquely decoded from $(b_0, b_2)$ independently of $(c_0, c_1)$ via
     $$
     z_A = R_0^{-1}b_0 = -\frac{216}{59}\left(I_4 + \frac{v\mathbf{1}^T}{365}\right)b_0, \qquad z_B = R_0^{-1}\bigl(b_2 - D_2(z_A)\bigr).
     $$
   - On the common-ready family $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$, decoding $h_A, h_B$ from the five distinct $C_3(h)$ receivers at $n = 5, c = 7$ ($x_{5,i} = g_1 g_1 x_{3,i} = x_{3,i}$) and applying the inverse words $\hat{x}_{0,i} = g_{j_0(h_i)} g_{j_1(h_i)} g_{j_2(h_i)} x_{5,i}$ with the $(0,1)$ receiver and piston-sum selector-consistency checks provides an exact left inverse and ready-image recognizer across all $625^2 = 390{,}625$ native input pairs $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$ in all four acceptance/refusal regimes.
5. **Joint energy conservation, conditioned two-use prediction, and comparator boundary (`Theorem 6`, `Theorem 7`, `Theorem 8`):**
   - With stored tape energy counted once in $E_{\mathrm{full}}(X)$, every phase of $\mathcal{G}_B$ conserves $E_{\mathrm{full}}(X) - W$, $E_{\mathrm{full}}(X) + b$, and $W + b$.
   - Conditioned on $\mathcal{A}_{\mathrm{lin}}^{(2)}$, the $39$-dimensional restriction $\theta|_{\Pi_2}$ is uniquely calibrated from $7$ runs in $Z_5 \times Z_5$ (or $5$ runs in the $37$-dimensional rank-one fifth-site subclass) and predicts $(b_0, b_1, b_2, b_3, E_A, \Delta_B, W_{\mathrm{final}}, b_{\mathrm{final}})$ with zero error on all remaining $18$ (or $20$) out-of-sample source pairs in $Z_5 \times Z_5$ ($281{,}250$ out-of-sample native input pairs).
   - $\mathcal{G}_B^7$ at $c = 7, n = 5$ is byte-for-byte indistinguishable from the full matched classical comparator $\mathcal{M}_{\mathrm{matched}}^{(2)}$ across all $390{,}625$ input pairs, and is separated by explicit rational witnesses from the five restricted comparator classes ($\mathcal{M}_{\mathrm{single}}$, $\mathcal{M}_{\mathrm{cold}}$, $\mathcal{M}_{2\text{-slot}}$, $\mathcal{M}_{1\sigma}$, $\mathcal{M}_{\text{no-}\sigma}^{\mathrm{class}} / \mathcal{M}_{\text{no-}\sigma}^{\mathrm{class}+d}$).

---

## 2. Conditional statements

1. **Conditional L1 primitives ($L_{\mathrm{buf}}, H_{B,A}, H_{B,B}$):** The delayed-label capture $L_{\mathrm{buf}}$ and the two bounded-store contact involutions $H_{B,A}, H_{B,B}$ are admitted as explicit conditional L1 mathematical primitives on $\mathcal{Z}_B$ and $\mathcal{A}_B$; they are not derived from native $U$ or $J$ and are not claimed minimal.
2. **Model-conditioned two-use prediction (`Theorem 7`):** Zero-error out-of-sample prediction on the $18$ uncalibrated pairs of $Z_5 \times Z_5$ holds conditionally within $\mathcal{A}_{\mathrm{lin}}^{(2)}$ (and within $\mathcal{A}_{\mathrm{aff}}^{(2)}$ after adding $(z^{(0)}, z^{(0)})$) restricted to the excited plane $\Pi_2 \times \Pi_2$.

---

## 3. Excluded statements (with explicit witnesses)

1. **Global invertibility of the selector-defined native tick $V$:** Excluded by `Theorem 2` Part 2 at $n = 0$ ($\theta_0 = 0$) via the collision $g_1(0,0,0,0,0,1) = g_4(2,1,3,4,2,2) = (0,0,0,0,0,4)$ and non-surjectivity onto $n = 0$.
2. **Direct un-reset substitution of a single shared direction bit $\sigma \in \{\pm 1\}$ into the two $H_B$ calls:** Excluded by `Theorem 2` Part 3 on $(p_A, p_B) = ((0,0,0,0), (1,0,0,0))$ at $b_{\mathrm{init}} = B \ge \frac{1}{10}$, where Contact A flips $\sigma: +1 \mapsto -1$ with $\Delta_A = 0$ and Contact B injects $-S z^{(1)}$ instead of $+S z^{(1)}$, giving $b_2 = -R_0 z^{(1)} \ne +R_0 z^{(1)}$.
3. **Cold-energy second-contact rule $\Delta_B^{\mathrm{cold}} = E_0(z_B)$ on the continuing apparatus:** Excluded by `Theorem 3` & `Theorem 8` on all $16$ pairs with $h_A, h_B \in \{1,2,3,4\}$, and sharply witnessed at $b_{\mathrm{init}} = B = B_* = \frac{8224427}{10497600}$ on $(h_A, h_B) = (4, 4)$, where the true occupied-wave increment $\Delta_B = \frac{4025387}{10497600}$ is **accepted** ($b_{\mathrm{final}} = 0$) whereas the cold increment $E_0(z^{(4)}) = \frac{2}{5} = \frac{4199040}{10497600}$ is **refused**.
4. **Universal two-use funding at single-use capacity $b_{\mathrm{init}} = B = \frac{2}{5}$:** Excluded by `Theorem 4` Part 3 on $12$ of the $25$ pairs in $Z_5 \times Z_5$ ($187{,}500$ native input pairs), including $(h_A, h_B) = (3, 3)$ where $b - \Delta_B = -\frac{1711367}{4665600} < 0$.
5. **Omission of retained direction bits $(\sigma_A, \sigma_B)_{\mathrm{final}}$ on $\Pi_{\mathrm{class}}$ or $\Pi_{\mathrm{class}+d}$:** Excluded by `Theorem 5` Part 4 on $\mathcal{R}_{(c_0, 0, \frac{1}{5}, \frac{1}{5})}$ at $(h_A, h_B) \in \{(0,0), (0,3), (3,0), (3,3)\}$, where $\Pi_{\mathrm{class}} = (X, W, b)$ collapses all four pairs onto $((0,2P c_0),(0,0),(0,0),0,0,\frac{1}{5})$ and $\Pi_{\mathrm{class}+d} = (X, W, b, d)$ still collapses $(0,0)$ with $(3,0)$ ($d=(0,4)$) and $(0,3)$ with $(3,3)$ ($d=(2,0)$).
6. **Unconditioned or full-$\mathbb{Q}^4$ two-use parameter identifiability from $Z_5 \times Z_5$:** Excluded by `Theorem 7` Part 2 via the $51$-dimensional out-of-plane kernel $\mathcal{K}_\perp^{(2)}$ on $\Pi_\perp = \mathbb{Q}e_2 \oplus \mathbb{Q}e_3$ and the cubic separator $q_3(z_0, z_1) = z_0 z_1(2z_0 - 1)$, which vanishes on $\{z^{(0)}, z^{(1)}, z^{(2)}, z^{(4)}\}$ and equals $\frac{1}{2}$ on $z^{(3)}$.
7. **Separation from the full matched classical comparator $\mathcal{M}_{\mathrm{matched}}^{(2)}$:** Excluded by `Theorem 8` Part 1 (exact byte-for-byte agreement across all $390{,}625$ native input pairs).

---

## 4. Still-missing items (`UNSUPPLIED`)

1. **Independent computational verifier (`UNSUPPLIED` in this analytical note):** As noted in the R1 review, this package is purely analytical (`scientific_code_status: NONE / NOT_RUN`); an independent exact computational verifier of the composed two-use funded apparatus is a separate downstream task.
2. **Native compilation (`UNSUPPLIED`):** Compilation of $L_{\mathrm{buf}}, H_{B,A}, H_{B,B}$ (and $F$) from native $U$ or a global $\Gamma^+$ circuit.
3. **Multi-period continuing cycles (`UNSUPPLIED`):** Funding and wave-clearing rules for third and later contacts ($c \ge 8$) once $(c_0, c_1)$ and $(b_0, b_1, b_2, b_3)$ have entered the wave.
4. **Full four-port span (`UNSUPPLIED`):** Native receiver lift exciting $\Pi_\perp = \mathbb{Q}e_2 \oplus \mathbb{Q}e_3$ to eliminate the $51$-dimensional out-of-plane kernel $\mathcal{K}_\perp^{(2)}$.
5. **Physical apparatus realization (`NOT_READY`):** Layer L2–L4 instrument design for `QUADRATIC-MEMORY-NATIVE-CONTACT` `[O]` and `QDD-INSTRUMENT-APPARATUS` `[O]`.

---

## 5. Administrative and policy checks executed

```text
python3 tools/check_policy.py
python3 tools/check_canon.py
python3 tools/check_ledger.py
python3 tools/check_gate_contract.py
python3 tools/check_verifier.py --base 8b91a935c426036e00ecb300019fd94734addeec
python3 tools/check_reproduce.py --base 8b91a935c426036e00ecb300019fd94734addeec
git diff d4b67e44d14a2f224a0ed77eb8dd08b217711cfb -- notes/C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N/{README.md,CONTRACT.md,PREREG.md,SOURCES.json}
git diff --check
```

---

## 6. Complete 14-item exported interface (`INTERFACE.json`)

1. `candidate_id`: `C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N`
2. `action_layer`: `L1` (`NON-CANONICAL`, `scientific_code_status: NONE / NOT_RUN`, `physical_status: NOT_READY`)
3. `composite_carrier`: $\mathcal{Z}_B = \mathbb{N}_0 \times \mathbb{F}_5^6 \times \mathbb{F}_5^6 \times \mathcal{X} \times \mathbb{Q} \times ([0,B]\cap\mathbb{Q}) \times \{\pm 1\}^2 \times \mathbb{F}_5^2 \times (\mathbb{Z}/8\mathbb{Z})$
4. `apparatus_subcarrier`: $\mathcal{A}_B = \mathcal{X} \times \mathbb{Q} \times ([0,B]\cap\mathbb{Q}) \times \{\pm 1\}^2 \times \mathbb{F}_5^2$
5. `admitted_conditional_primitives`: $L_{\mathrm{buf}}$, $F$ (with $u = K(H v - J_0 w_{\mathrm{next}} + 4 P b_{\mathrm{out}}), A_0 = b_{\mathrm{out}} + \frac{1}{2}P^T(w_{\mathrm{next}} - u)$), $H_{B,A}$, $H_{B,B}$ (with two-sided store guards $0 \le b - \Delta_i \le B$ and global involutivity $H_{B,A}^2 = H_{B,B}^2 = \mathrm{id}$)
6. `eight_phase_schedule`: $\mathcal{G}_B$ on $\mathcal{Z}_B$ (7 updates $\mathcal{G}_B^7$ from $c=0, n=0$ to completion boundary $c=7, n=5$; 8th update rotates $c: 7 \mapsto 0$ with $T_7 = \mathrm{id}$) and two-sided permutation $G_B$ on $\mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z})$
7. `common_ready_family`: $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ ($390{,}625$ native input pairs $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$, $25$ ordered source fibres $\mathcal{F}_{h_A} \times \mathcal{F}_{h_B}$ of size $15{,}625$) and Blank-Ready subfamily $\mathcal{R}_{\mathrm{blank}}(b_{\mathrm{init}}, B)$ ($c_0 = c_1 = 0$)
8. `occupied_wave_second_contact_work`: $\Delta_B(z_A, z_B) = E_0(z_B) - \frac{s_B(\mu^T z_A)}{10497600}$ with $\mu = (145483, 173653, 173653, 142153)^T$ and $s_B = \mathbf{1}^T z_B$
9. `input_independent_two_use_store_bounds`: sharp threshold $B_* = \frac{8224427}{10497600} \le b_{\mathrm{init}} \le B$ and canonical cold two-use store $b_{\mathrm{init}} = B = \frac{4}{5}$ (minimum reserve $\frac{173653}{10497600}$), plus exact branch partitions at $B = \frac{2}{5}$ ($13/12/0/0$) and $B = \frac{1}{5}$ ($6/9/6/4$)
10. `unified_four_cut_equations_and_source_decoder`: $b_0 = \alpha_A R_0 z_A$, $b_1 = \alpha_A R_1 z_A$, $b_2 = \alpha_A D_2(z_A) + \alpha_B R_0 z_B$, $b_3 = \alpha_A D_3(z_A) + \alpha_B R_1 z_B - \frac{1}{2}J_p c_1$ with $J_p = P^T H P = \frac{1}{54}(59 I_4 + \mathbf{1}\mathbf{1}^T)$, $D_2(z_A) = \frac{1}{2}P^T(T - T^3 + T J_0)S z_A$, $D_3(z_A) = \frac{1}{2}P^T(T^2 - T^4 + T^2 J_0 + T J_0 T)S z_A$, and $R_0^{-1} = -\frac{216}{59}(I_4 + \frac{v\mathbf{1}^T}{365})$ decoding $z_A = R_0^{-1}b_0$ and $z_B = R_0^{-1}(b_2 - D_2(z_A))$ on `(ACC, ACC)`
11. `native_prepared_image_left_inverse`: $\mathcal{D}(Z(7))$ decoding $h_i$ from $\operatorname{rec}(x_{5,i}) = C_3(h_i)$ ($x_{5,i} = x_{3,i}$) and reconstructing $\hat{x}_{0,i} = g_{j_0(h_i)} g_{j_1(h_i)} g_{j_2(h_i)} x_{5,i}$, with 4-part ready-image recognizer enforcing $\operatorname{rec}(\hat{x}_{0,i}) = (0,1)$, piston-sum selector consistency $\sum_{m=0}^3 \hat{x}_{0,i,m} \bmod 5 = h_i$, $d = \operatorname{rec}(\hat{x}_{1,B})$, and $(M_{7,B}^{(r_A, r_B)})^{-1}$ recovery across all $390{,}625$ pairs
12. `joint_energy_work_store_invariants`: $E_{\mathrm{full}}(X) - W = 2(\|c_0\|^2 + \|c_1\|^2)$, $E_{\mathrm{full}}(X) + b = 2(\|c_0\|^2 + \|c_1\|^2) + b_{\mathrm{init}}$, $W + b = b_{\mathrm{init}}$ (stored tape energy counted once)
13. `conditioned_two_use_calibration_to_prediction`: $39$-dimensional restricted parameter $\theta|_{\Pi_2}$ in $\mathcal{A}_{\mathrm{lin}}^{(2)}$ calibrated from $7$ runs (or $5$ runs in the $37$-dimensional rank-one $\Omega$ subclass) with zero-error prediction on the remaining $18$ (or $20$) source pairs in $Z_5 \times Z_5$, alongside the $51$-dimensional out-of-plane kernel $\mathcal{K}_\perp^{(2)}$ and cubic separator $q_3(z_0, z_1) = z_0 z_1(2z_0 - 1)$
14. `comparator_boundary_and_separation_witnesses`: byte-for-byte agreement with $\mathcal{M}_{\mathrm{matched}}^{(2)}$ on all $390{,}625$ pairs and five explicit rational separation witnesses against $\mathcal{M}_{\mathrm{single}}$, $\mathcal{M}_{\mathrm{cold}}$, $\mathcal{M}_{2\text{-slot}}$, $\mathcal{M}_{1\sigma}$, and $\mathcal{M}_{\text{no-}\sigma}^{\mathrm{class}} / \mathcal{M}_{\text{no-}\sigma}^{\mathrm{class}+d}$
