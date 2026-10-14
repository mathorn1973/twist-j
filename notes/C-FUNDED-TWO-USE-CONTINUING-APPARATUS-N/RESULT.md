# Result: `C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N`

**NON-CANONICAL / L1 analytical result summary / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1504](https://github.com/mathorn1973/twist-j/issues/1504), following [#1497#issuecomment-6179898943](https://github.com/mathorn1973/twist-j/issues/1497#issuecomment-6179898943).

```text
candidate_id:               C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N
branch:                     incubation/C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N
base_commit:                8b91a935c426036e00ecb300019fd94734addeec
preregistration_commit:     d4b67e44d14a2f224a0ed77eb8dd08b217711cfb
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

## 1. Proved statements (`PROOF.md` Sections 1–4)

1. **Global bijectivity and involutivity (`Theorem 1` & `Theorem 2`):**
   - On the full composite carrier $\mathcal{Z}_B = \mathbb{N}_0 \times \mathbb{F}_5^6 \times \mathbb{F}_5^6 \times \mathcal{X} \times \mathbb{Q} \times ([0,B]\cap\mathbb{Q}) \times \{\pm 1\}^2 \times \mathbb{F}_5^2 \times (\mathbb{Z}/8\mathbb{Z})$ and the static-source apparatus subcarrier $\mathcal{A}_B$, the delayed-label buffer capture $L_{\mathrm{buf}}(x_B, d) = (x_B, (d + \operatorname{rec}(x_B))\bmod 5)$, the two-tape wave update $F$, and the two bounded-store contact maps $H_{B,A}, H_{B,B}$ (with two-sided guards $0 \le b - \Delta_A \le B$ and $0 \le b - \Delta_B \le B$) are global bijections.
   - Both $H_{B,A}^2 = \mathrm{id}$ and $H_{B,B}^2 = \mathrm{id}$ hold globally across all accepted, refused, and occupied wave states $(u, v) \in \mathbb{Q}^D \times \mathbb{Q}^D$, and $G_B(a, c) = (T_c(a), (c+1)\bmod 8)$ is a two-sided permutation on $\mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z})$.
2. **Closed-form occupied-wave energy increment $\Delta_B(z_A, z_B)$ and exact 25-pair census (`Theorem 3`):**
   - On any common-ready state in $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ where Contact A ($c=1$) is accepted ($\alpha_A = 1$), the wave arriving at Contact B ($c=4$) is $(w_1, w_2) = (T f, (T^2 - J_0)f)$ ($f = S z_A$), which is strictly independent of the old archive $(c_0, c_1)$.
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
4. **Four-cut record retention, archive-independent decoding, and exact native left inverse (`Theorem 5`):**
   - At $c = 7, n = 5$, all four chronological cuts $(b_0, b_1, b_2, b_3)$ are simultaneously retained in $(A_0, A_1, B_1, B_0) = (b_0, b_1, b_2, b_3)$ and satisfy
     $$
     b_0 = \alpha_A R_0 z_A, \quad b_1 = \alpha_A R_1 z_A, \quad b_2 = \alpha_A D_2(z_A) + \alpha_B R_0 z_B, \quad b_3 = \alpha_A D_3(z_A) + \alpha_B R_1 z_B - \frac{1}{2}J_p c_1.
     $$
   - On `(ACC, ACC)` ($\alpha_A = \alpha_B = 1$, certified by $(\sigma_A, \sigma_B)_{\mathrm{final}} = (-1, -1)$), both sources are uniquely decoded from $(b_0, b_2)$ independently of $(c_0, c_1)$ via $z_A = R_0^{-1}b_0 = -4 M^{-1}b_0$ and $z_B = R_0^{-1}(b_2 - D_2(z_A))$.
   - The inverse native evolution $V^{-5}(5, x_A(5), x_B(5))$ provides an exact left inverse on $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ across all $625^2 = 390{,}625$ native input pairs $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$ in all four acceptance/refusal regimes.
5. **Joint energy conservation, conditioned two-use prediction, and comparator boundary (`Theorem 6`, `Theorem 7`, `Theorem 8`):**
   - With stored tape energy counted once in $E_{\mathrm{full}}(X)$, every phase of $\mathcal{G}_B$ conserves $E_{\mathrm{full}}(X) - W$, $E_{\mathrm{full}}(X) + b$, and $W + b$.
   - Conditioned on $\mathcal{A}_{\mathrm{lin}}^{(2)}$, the $39$-dimensional restriction $\theta|_{\Pi_2}$ is uniquely calibrated from $7$ runs in $Z_5 \times Z_5$ (or $5$ runs in the $37$-dimensional rank-one fifth-site subclass) and predicts $(b_0, b_1, b_2, b_3, E_A, \Delta_B, W_{\mathrm{final}}, b_{\mathrm{final}})$ with zero error on all remaining $18$ (or $20$) out-of-sample source pairs in $Z_5 \times Z_5$ ($281{,}250$ out-of-sample native input pairs).
   - $\mathcal{G}_B^8$ is byte-for-byte indistinguishable from the full matched classical comparator $\mathcal{M}_{\mathrm{matched}}^{(2)}$ across all $390{,}625$ input pairs, and is separated by explicit rational witnesses from all five restricted comparator classes ($\mathcal{M}_{\mathrm{single}}$, $\mathcal{M}_{\mathrm{cold}}$, $\mathcal{M}_{2\text{-slot}}$, $\mathcal{M}_{1\sigma}$, $\mathcal{M}_{\text{no-}\sigma}$).

---

## 2. Conditional statements

1. **Conditional L1 primitives ($L_{\mathrm{buf}}, H_{B,A}, H_{B,B}$):** The delayed-label capture $L_{\mathrm{buf}}$ and the two bounded-store contact involutions $H_{B,A}, H_{B,B}$ are admitted as explicit conditional L1 mathematical primitives on $\mathcal{Z}_B$ and $\mathcal{A}_B$; they are not derived from native $U$ or $J$ and are not claimed minimal.
2. **Model-conditioned two-use prediction (`Theorem 7`):** Zero-error out-of-sample prediction on the $18$ uncalibrated pairs of $Z_5 \times Z_5$ holds conditionally within $\mathcal{A}_{\mathrm{lin}}^{(2)}$ (and within $\mathcal{A}_{\mathrm{aff}}^{(2)}$ after adding $(z^{(0)}, z^{(0)})$) restricted to the excited plane $\Pi_2 \times \Pi_2$.

---

## 3. Excluded statements (with explicit witnesses)

1. **Single shared contact direction bit $\sigma \in \{\pm 1\}$ without reset:** Excluded by `Theorem 2` Part 3 on $(p_A, p_B) = ((0,0,0,0), (1,0,0,0))$ at $b_{\mathrm{init}} = B = \frac{4}{5}$, where Contact A flips $\sigma: +1 \mapsto -1$ with $\Delta_A = 0$ and Contact B injects $-S z^{(1)}$ instead of $+S z^{(1)}$, giving $b_2 = -R_0 z^{(1)} \ne +R_0 z^{(1)}$.
2. **Cold-energy second-contact rule $\Delta_B^{\mathrm{cold}} = E_0(z_B)$ on the continuing apparatus:** Excluded by `Theorem 3` & `Theorem 8` on all $16$ pairs with $h_A, h_B \in \{1,2,3,4\}$, and sharply witnessed at $b_{\mathrm{init}} = B = B_* = \frac{8224427}{10497600}$ on $(h_A, h_B) = (4, 4)$, where the true occupied-wave increment $\Delta_B = \frac{4025387}{10497600}$ is **accepted** ($b_{\mathrm{final}} = 0$) whereas the cold increment $E_0(z^{(4)}) = \frac{2}{5} = \frac{4199040}{10497600}$ is **refused**.
3. **Universal two-use funding at single-use capacity $b_{\mathrm{init}} = B = \frac{2}{5}$:** Excluded by `Theorem 4` Part 3 on $12$ of the $25$ pairs in $Z_5 \times Z_5$ ($187{,}500$ native input pairs), including $(h_A, h_B) = (3, 3)$ where $b_1 - \Delta_B = -\frac{1711367}{4665600} < 0$.
4. **Omission of retained direction bits $(\sigma_A, \sigma_B)_{\mathrm{final}}$:** Excluded by `Theorem 5` Part 4 on $\mathcal{R}_{(c_0, 0, \frac{1}{5}, \frac{1}{5})}$ at $(h_A, h_B) \in \{(0,0), (0,3), (3,0), (3,3)\}$, which all yield $(b_0, b_1, b_2, b_3) = (0,0,0,0)$ and $(W_{\mathrm{final}}, b_{\mathrm{final}}) = (0, \frac{1}{5})$ while taking four distinct values of $(\sigma_A, \sigma_B)_{\mathrm{final}}$.
5. **Unconditioned or full-$\mathbb{Q}^4$ two-use parameter identifiability from $Z_5 \times Z_5$:** Excluded by `Theorem 7` Part 2 via the $51$-dimensional out-of-plane kernel $\mathcal{K}_\perp^{(2)}$ on $\Pi_\perp = \mathbb{Q}e_2 \oplus \mathbb{Q}e_3$ and the cubic separator $q_3(z_0, z_1) = z_0 z_1(2z_0 - 1)$, which vanishes on $\{z^{(0)}, z^{(1)}, z^{(2)}, z^{(4)}\}$ and equals $\frac{1}{2}$ on $z^{(3)}$.
6. **Separation from the full matched classical comparator $\mathcal{M}_{\mathrm{matched}}^{(2)}$:** Excluded by `Theorem 8` Part 1 (exact byte-for-byte agreement across all $390{,}625$ native input pairs).

---

## 4. Still-missing items (`UNSUPPLIED`)

1. **Native compilation (`UNSUPPLIED`):** Compilation of $L_{\mathrm{buf}}, H_{B,A}, H_{B,B}$ (and $F$) from native $U$ or a global $\Gamma^+$ circuit.
2. **Multi-period continuing cycles (`UNSUPPLIED`):** Funding and wave-clearing rules for third and later contacts ($c \ge 8$) once $(c_0, c_1)$ and $(b_0, b_1, b_2, b_3)$ have entered the wave.
3. **Full four-port span (`UNSUPPLIED`):** Native receiver lift exciting $\Pi_\perp = \mathbb{Q}e_2 \oplus \mathbb{Q}e_3$ to eliminate the $51$-dimensional out-of-plane kernel $\mathcal{K}_\perp^{(2)}$.
4. **Physical apparatus realization (`NOT_READY`):** Layer L2–L4 instrument design for `QUADRATIC-MEMORY-NATIVE-CONTACT` `[O]` and `QDD-INSTRUMENT-APPARATUS` `[O]`.

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
5. `admitted_conditional_primitives`: $L_{\mathrm{buf}}$, $H_{B,A}$, $H_{B,B}$ (with two-sided store guards $0 \le b - \Delta_i \le B$ and global involutivity $H_{B,A}^2 = H_{B,B}^2 = \mathrm{id}$)
6. `eight_phase_schedule`: $\mathcal{G}_B$ on $\mathcal{Z}_B$ and two-sided permutation $G_B$ on $\mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z})$
7. `common_ready_family`: $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ ($390{,}625$ native input pairs $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$, $25$ ordered source fibres $\mathcal{F}_{h_A} \times \mathcal{F}_{h_B}$ of size $15{,}625$) and Blank-Ready subfamily $\mathcal{R}_{\mathrm{blank}}(b_{\mathrm{init}}, B)$ ($c_0 = c_1 = 0$)
8. `occupied_wave_second_contact_work`: $\Delta_B(z_A, z_B) = E_0(z_B) - \frac{s_B(\mu^T z_A)}{10497600}$ with $\mu = (145483, 173653, 173653, 142153)^T$ and $s_B = \mathbf{1}^T z_B$
9. `input_independent_two_use_store_bounds`: sharp threshold $B_* = \frac{8224427}{10497600} \le b_{\mathrm{init}} \le B$ and canonical cold two-use store $b_{\mathrm{init}} = B = \frac{4}{5}$ (minimum reserve $\frac{173653}{10497600}$), plus exact branch partitions at $B = \frac{2}{5}$ ($13/12/0/0$) and $B = \frac{1}{5}$ ($6/9/6/4$)
10. `unified_four_cut_equations_and_source_decoder`: $b_0 = \alpha_A R_0 z_A$, $b_1 = \alpha_A R_1 z_A$, $b_2 = \alpha_A D_2(z_A) + \alpha_B R_0 z_B$, $b_3 = \alpha_A D_3(z_A) + \alpha_B R_1 z_B - \frac{1}{2}J_p c_1$, with $z_A = -4 M^{-1}b_0$ and $z_B = -4 M^{-1}(b_2 - D_2(z_A))$ on `(ACC, ACC)`
11. `native_prepared_image_left_inverse`: $\mathcal{D}(Z_{\mathrm{final}})$ via $V^{-5}(5, x_A(5), x_B(5))$ and 6-part image recognizer $\mathcal{I}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ across all $390{,}625$ pairs
12. `joint_energy_work_store_invariants`: $E_{\mathrm{full}}(X) - W = 2(\|c_0\|^2 + \|c_1\|^2)$, $E_{\mathrm{full}}(X) + b = 2(\|c_0\|^2 + \|c_1\|^2) + b_{\mathrm{init}}$, $W + b = b_{\mathrm{init}}$ (stored tape energy counted once)
13. `conditioned_two_use_calibration_to_prediction`: $39$-dimensional restricted parameter $\theta|_{\Pi_2}$ in $\mathcal{A}_{\mathrm{lin}}^{(2)}$ calibrated from $7$ runs (or $5$ runs in the $37$-dimensional rank-one $\Omega$ subclass) with zero-error prediction on the remaining $18$ (or $20$) source pairs in $Z_5 \times Z_5$, alongside the $51$-dimensional out-of-plane kernel $\mathcal{K}_\perp^{(2)}$ and cubic separator $q_3(z_0, z_1) = z_0 z_1(2z_0 - 1)$
14. `comparator_boundary_and_separation_witnesses`: byte-for-byte agreement with $\mathcal{M}_{\mathrm{matched}}^{(2)}$ on all $390{,}625$ pairs and five explicit rational separation witnesses against $\mathcal{M}_{\mathrm{single}}$, $\mathcal{M}_{\mathrm{cold}}$, $\mathcal{M}_{2\text{-slot}}$, $\mathcal{M}_{1\sigma}$, and $\mathcal{M}_{\text{no-}\sigma}$
