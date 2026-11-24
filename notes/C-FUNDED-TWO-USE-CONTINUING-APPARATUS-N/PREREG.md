# Preregistration: `C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N`

**NON-CANONICAL / L1 analytical preregistration / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1504](https://github.com/mathorn1973/twist-j/issues/1504), following [#1497#issuecomment-6179898943](https://github.com/mathorn1973/twist-j/issues/1497#issuecomment-6179898943).

```text
candidate_id:               C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N
branch:                     incubation/C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N
allowed_path:               notes/C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N/
authority_base:             8b91a935c426036e00ecb300019fd94734addeec
canon_tag:                  canon-v101
content_commit:             421a4ec1daf07c04d19022c1ee219607e83c09a8
canon_sha256:               b83a99feccac173bd3c9c5851c5874ca27cbd135f71d136d793b45f86c8a87f7
canon_bytes:                992352
action_layer:               L1 (symbolic mathematical proof over F_5 and Q; no scientific code execution)
```

---

## 1. Six frozen preregistration fields (`POLICY.md` Section 3 / L1 notes scope)

1. **Equation:**
   - Complete 8-phase coupled transition law $\mathcal{G}_B$ on $\mathcal{Z}_B = \mathbb{N}_0 \times \mathbb{F}_5^6 \times \mathbb{F}_5^6 \times \mathcal{X} \times \mathbb{Q} \times ([0,B]\cap\mathbb{Q}) \times \{\pm 1\}^2 \times \mathbb{F}_5^2 \times (\mathbb{Z}/8\mathbb{Z})$ defined in `CONTRACT.md` Section 2.
   - Exact global involutions $H_{B,A}^2 = \mathrm{id}$ and $H_{B,B}^2 = \mathrm{id}$ with two-sided store guards $0 \le b - \Delta_A \le B$ and $0 \le b - \Delta_B \le B$, and reversible delayed-label capture $L_{\mathrm{buf}}(x_B, d) = (x_B, (d + \operatorname{rec}(x_B)) \bmod 5)$.
   - Exact occupied-state second-contact energy increment on the positive ready trajectory:
     $$
     \Delta_B(z_A, z_B) = E_D(w_1, w_2 + g) - E_D(w_1, w_2) = E_0(z_B) + g^T\left(w_2 - \frac{1}{2}H w_1\right) = E_0(z_B) - \frac{s_B (\mu^T z_A)}{10497600},
     $$
     where $\mu = (145483, 173653, 173653, 142153)^T$ and $s_B = \mathbf{1}^T z_B$.
   - Unified four-cut branch output equations across all acceptance/refusal indicators $\alpha_i = \frac{1 - \sigma_{i,\mathrm{final}}}{2} \in \{0, 1\}$:
     $$
     b_0 = \alpha_A R_0 z_A, \quad b_1 = \alpha_A R_1 z_A, \quad b_2 = \alpha_A D_2(z_A) + \alpha_B R_0 z_B, \quad b_3 = \alpha_A D_3(z_A) + \alpha_B R_1 z_B - \frac{1}{2}J_p c_1.
     $$
   - Joint boundary invariants $E_{\mathrm{full}}(X) - W = \mathrm{const}$, $E_{\mathrm{full}}(X) + b = \mathrm{const}$, and $W + b = \mathrm{const}$, with stored tape energy counted once inside $E_{\mathrm{full}}(X)$.

2. **Code:**
   - **NONE (`NOT_RUN`).** This is a purely analytical L1 proof round. No scientific `verify.py`, numerical solver, or finite-census enumeration script is committed or executed. All rational identities are derived by hand from the frozen `#1485`, `#1489`, `#1492`, `#1496`, A1 (`7b4d55502be44b2f2aed4005c909d7dcb50dbc55`), A2 (`c34baa826cb846260b96373ae6d8f10c3a189a5a`), and A3 (`f341b04f737827d9033e60f452fab77231f7b04a`) definitions pinned in `SOURCES.json`.

3. **Carrier or data:**
   - Discrete native carrier $\mathbb{N}_0 \times \mathbb{F}_5^6 \times \mathbb{F}_5^6$ ($625^2 = 390{,}625$ prepared input pairs $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$, partitioned into $25$ ordered residue-sum fibres $\mathcal{F}_{h_A} \times \mathcal{F}_{h_B}$ of cardinality $125^2 = 15{,}625$ each) and delayed receiver buffer $d \in \mathbb{F}_5^2$ ($25$ states).
   - Rational classical wave/tape carrier $\mathcal{X} = (\mathbb{Q}^D \times \mathbb{Q}^D) \times (\mathbb{Q}^4)^2 \times (\mathbb{Q}^4)^2 \times (\mathbb{Z}/2\mathbb{Z})$ with $|D| = 869$, signed work ledger $W \in \mathbb{Q}$, bounded store $b \in [0, B] \cap \mathbb{Q}$, two-bit direction register $(\sigma_A, \sigma_B) \in \{\pm 1\}^2$, and 8-phase clock $c \in \mathbb{Z}/8\mathbb{Z}$.
   - Two-use model parameter carrier $\mathcal{A}_{\mathrm{lin}}^{(2)} = (\mathbb{Q}^{4 \times 4})^4 \times \mathbb{Q}^{4 \times 4}_{\mathrm{sym}} \times \mathbb{Q}^{4 \times 4}$ ($\dim_{\mathbb{Q}} = 64 + 10 + 16 = 90$) and its $\Pi_2 \times \Pi_2$ restriction $\mathcal{I}_{\mathrm{lin}}^{(2)}(\Pi_2) = (\mathbb{Q}^{4 \times 2})^4 \times \mathbb{Q}^{2 \times 2}_{\mathrm{sym}} \times \mathbb{Q}^{2 \times 2}$ ($\dim_{\mathbb{Q}} = 32 + 3 + 4 = 39$, or $37$ under the rank-one fifth-site factorization).

4. **Systematics:**
   - Literal coordinate equality without sign quotient, normalization, or projectivization.
   - Strict separation between the discrete $\mathbb{F}_5^2$ delayed label $d$ and any rational ancillary registers.
   - Explicit admission of $L_{\mathrm{buf}}, H_{B,A}, H_{B,B}$ as conditional L1 primitives (no false claim of native compilation from $U$ or global $\Gamma^+$ compilation).
   - Use of the true occupied-wave energy increment $\Delta_B(z_A, z_B) = E_0(z_B) + g^T(w_2 - \frac{1}{2}H w_1)$ rather than cold source energy $E_0(z_B)$ at Contact B.
   - Single counting of retained tape energy $2(\|A_0\|^2 + \|A_1\|^2 + \|B_0\|^2 + \|B_1\|^2)$ inside $E_{\mathrm{full}}(X)$.
   - Preservation of the four frozen pin files (`README.md`, `CONTRACT.md`, `PREREG.md`, `SOURCES.json`) byte-for-byte in the subsequent result commit.

5. **Failure threshold:**
   - **Zero tolerance (`0`)** on all algebraic, matrix, and rational arithmetic identities.
   - Any violation of global invertibility of $L_{\mathrm{buf}}, H_{B,A}, H_{B,B}, F$, any failure of $0 \le b_{\mathrm{init}} - E_A \le B$ or $0 \le b_{\mathrm{init}} - E_A - \Delta_B \le B$ on $Z_5 \times Z_5$ at the declared input-independent capacity $b_{\mathrm{init}} = B = \frac{4}{5}$ (or $B_* = \frac{8224427}{10497600}$), any failure of four-cut retention or accepted-zero vs. refusal discrimination, or any violation of $E_{\mathrm{full}}(X) - W = \mathrm{const}$ refutes the corresponding positive claim at its exact scope.

6. **Action layer:**
   - **Layer L1 (mathematical/symbolic structure and prospective protocol design).**
   - Physical status remains `NOT_READY`. Native compilation of $L_{\mathrm{buf}}, H_{B,A}, H_{B,B}$ remains `UNSUPPLIED`. Public frontier owners `QUADRATIC-MEMORY-NATIVE-CONTACT` `[O]` and `QDD-INSTRUMENT-APPARATUS` `[O]` remain untouched.

---

## 2. Two-commit immutability rule

The four files `README.md`, `CONTRACT.md`, `PREREG.md`, and `SOURCES.json` in `notes/C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N/` constitute the frozen preregistration pin and must remain byte-for-byte unchanged in the subsequent analytical result commit adding `PROOF.md`, `RESULT.md`, `INTERFACE.json`, and `PROMO-C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N.md`.
