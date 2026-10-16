# Preregistration: `C-FUNDED-TWO-USE-EXECUTABLE-2-N`

**NON-CANONICAL / L1 executable incubation preregistration on reconciled 705-site domain / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1515](https://github.com/mathorn1973/twist-j/issues/1515), under parent program [#1506](https://github.com/mathorn1973/twist-j/issues/1506), predecessor [#1507](https://github.com/mathorn1973/twist-j/issues/1507) / [#1512](https://github.com/mathorn1973/twist-j/pull/1512), and G1 geometry reconciliation [#1513](https://github.com/mathorn1973/twist-j/issues/1513) / [#1514](https://github.com/mathorn1973/twist-j/pull/1514).

```text
candidate_id:               C-FUNDED-TWO-USE-EXECUTABLE-2-N
branch:                     incubation/C-FUNDED-TWO-USE-EXECUTABLE-2-N
allowed_path:               notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/
authority_base:             8b91a935c426036e00ecb300019fd94734addeec
canon_tag:                  canon-v101
content_commit:             421a4ec1daf07c04d19022c1ee219607e83c09a8
canon_sha256:               b83a99feccac173bd3c9c5851c5874ca27cbd135f71d136d793b45f86c8a87f7
canon_bytes:                992352
g1_reconciliation_pin:      a96646c22267d59179a5a96a161c5f6f95ba6255
g1_reconciliation_result:   82ad219401d87c3900011d1e8801ffef4221e05b
predecessor_pin:            81a70caa8dbcc61b64276e7d3df5ba84e860d4f1
predecessor_result:         d6c48e463e1c7d78e8da828711cdda726f57e00b
action_layer:               L1 (exact standard-library Python over F_5 and Q)
scientific_code_at_pin:     DOMAIN.tsv, apparatus.py, verify.py (frozen before first run)
```

---

## 1. Six frozen preregistration fields (`POLICY.md` Section 3 / `#1515` pin contract)

1. **Equation:**
   - Primary embedded $D_3$ stencil $B_{\mathrm{st}}$ ($60$ offsets, shell weights $(6,1,15,1,1)/324$, diagonal $\frac{8}{9}$, $|B_{\mathrm{zero}}| = 61$), marked sites $Y = (y_0,y_1,y_2,y_3,y_4)$ ($|Y| = 5$), ordered ports $R = (y_0,y_1,y_2,y_3)$, intermediate Minkowski sums $|Y + B_{\mathrm{zero}}| = 142$ and $|B_{\mathrm{zero}} + B_{\mathrm{zero}}| = 489$, reconciled finite causal domain $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$ ($|D| = 705$, wave+tape basis dimension $2|D| + 16 = 1426$), Dirichlet operator $L_D$, wave operator $H = 2I - L_D$, coupler $K = I - \frac{1}{2}PP^T$, projection $J_0 = I - PP^T$, $T = KH$, five-site zero-mean source $S$, and balanced lift $\eta(q, r_2) = (\frac{\ell(q)}{2}, \frac{\ell(r_2)+1}{2}, 0, 0)^T$.
   - Shared-counter two-head native tick $V(n, x_A, x_B) = (n+1, g_{j(n,x_A)}(x_A), g_{j(n,x_B)}(x_B))$ with $j(n, x) = (\sum_{m=0}^5 x_m + 2\theta_n)\bmod 5$ and $\theta_n = \operatorname{popcount}(n)\bmod 2$.
   - Reversible classical wave/tape step $F((u,v),(A_0,A_1),(B_0,B_1),k) = ((v,w_{\mathrm{next}}),(A_1,B_1),(b_{\mathrm{out}},B_0),(k+1)\bmod 2)$ with $w_{\mathrm{next}} = K(H v - J_0 u + 4 P A_0), b_{\mathrm{out}} = A_0 - \frac{1}{2}P^T(w_{\mathrm{next}} - u)$, and exact two-sided inverse $F^{-1}$ with $u = K(H v - J_0 w_{\mathrm{next}} + 4 P b_{\mathrm{out}}), A_0 = b_{\mathrm{out}} + \frac{1}{2}P^T(w_{\mathrm{next}} - u)$.
   - Conditional L1 primitives $L_{\mathrm{buf}}(x_B, d) = (x_B, (d + \operatorname{rec}(x_B))\bmod 5)$, $H_{B,A}$ (reading $\operatorname{rec}(x_A)$ and $\sigma_A$ with guard $0 \le b - \Delta_A \le B$), and $H_{B,B}$ (reading retained $d$ and $\sigma_B$ with guard $0 \le b - \Delta_B \le B$).
   - Eight-phase autonomous schedule $\mathcal{G}_B$ on $\mathcal{Z}_B$ (7 updates $\mathcal{G}_B^7$ from $c=0, n=0$ to completion boundary $c=7, n=5$; 8th update $\mathcal{G}_B^8$ holds data and rolls $c: 7 \mapsto 0$), explicitly distinguishing the two-sided invertible supplied-label apparatus substate transitions $T_{c,B}^{(r_A, r_B)}$ and $S_B^{(r_A, r_B)}$ on $\mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z})$ from the non-invertible full coupled evolution $\mathcal{G}_B$ on $\mathcal{Z}_B$ (which has only the prepared-image left inverse $D(Z(7)) = (p_A, p_B)$).
   - Exact occupied-state second-contact work $\Delta_B(z_A, z_B) = E_0(z_B) + g^T(w_2 - \frac{1}{2}H w_1) = E_0(z_B) - \frac{s_B(\mu^T z_A)}{10497600}$ with $\mu = (145483, 173653, 173653, 142153)^T$, order witness $W(1,4) - W(4,1) = \frac{313}{233280}$ at $B = b_{\mathrm{init}} = \frac{4}{5}$, four-cut equations $b_0 = \alpha_A R_0 z_A$, $b_1 = \alpha_A R_1 z_A$, $b_2 = \alpha_A D_2(z_A) + \alpha_B R_0 z_B$, $b_3 = \alpha_A D_3(z_A) + \alpha_B R_1 z_B - \frac{1}{2}J_p c_1$, archive-independent source decoder $z_A = R_0^{-1} b_0, z_B = R_0^{-1}(b_2 - D_2(z_A))$ on `(ACC, ACC)` with $R_0^{-1} = -\frac{216}{59}(I_4 + \frac{v\mathbf{1}^T}{365})$, and single-counted full energy invariants $E_{\mathrm{full}}(X) - W = 2(\|c_0\|^2 + \|c_1\|^2)$, $E_{\mathrm{full}}(X) + b = 2(\|c_0\|^2 + \|c_1\|^2) + b_{\mathrm{init}}$, $W + b = b_{\mathrm{init}}$.

2. **Code:**
   - `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/DOMAIN.tsv`: frozen 705-site domain list (`5029` bytes, SHA-256 `2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0`).
   - `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/apparatus.py`: self-contained exact standard-library Python machine on the validated 705-site domain.
   - `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py`: complete executable audit and CLI runner (default scientific audit mode, `--compare` mode for `TWOUSE-COMPARE-v2`, and `--witnesses` mode).
   - All files are frozen in the preregistration pin commit and verified by public readback before the first scientific execution. Only static AST inspection (`ast.parse`) is performed before the pin.

3. **Carrier or data:**
   - Native carrier $\mathbb{N}_0 \times \mathbb{F}_5^6 \times \mathbb{F}_5^6$, with $625$ individual preparations $p \in \mathbb{F}_5^4$ ($x_0 = (p, 0, 1)$) per head and $625^2 = 390{,}625$ paired preparations $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$ factoring into $25$ ordered source-sum fibres $\mathcal{F}_{h_A} \times \mathcal{F}_{h_B}$ of cardinality $125^2 = 15{,}625$.
   - Discrete delayed-label buffer $d \in \mathbb{F}_5^2$ ($25$ states), direction bits $(\sigma_A, \sigma_B) \in \{\pm 1\}^2$, tape pointer $k \in \{0, 1\}$, and phase clock $c \in \{0,\dots,7\}$.
   - Exact rational wave/tape carrier $\mathcal{X} = (\mathbb{Q}^D \times \mathbb{Q}^D) \times (\mathbb{Q}^4)^2 \times (\mathbb{Q}^4)^2 \times (\mathbb{Z}/2\mathbb{Z})$ ($|D| = 705$, basis dimension $1426$), signed work $W \in \mathbb{Q}$, and bounded store $b \in [0, B] \cap \mathbb{Q}$ evaluated across capacities $B \in \{0, \frac{1}{10}, \frac{1}{5}, \frac{2}{5}, \frac{8224427}{10497600}, \frac{4}{5}\}$.

4. **Systematics:**
   - Zero-tolerance exact arithmetic (`fractions.Fraction` and `int`) everywhere; `bool` and `float` inputs are rejected by type guards with explicit `expected`/`actual` error messages.
   - Source residue sums $h_A, h_B$ are produced by the native trajectory at $n = 1$, never preloaded into the apparatus.
   - `direct_source_reader` accepts only $(b_0, b_2)$ and declared acceptance/context information (`sigma_A, sigma_B` or `d`) and raises `TypeError` on composite states or native heads; full native input recovery (`recover_prepared_inputs`, `recognize_ready_image`) is a separate endpoint interface.
   - Both `#1506` clarifications are enforced: (i) $q_3(z^{(3)}) = \frac{1}{2}$ so $q_3(z_A) u$ shifts $b_2$ at $h_A = 3$ by $\frac{1}{2}u$, and (ii) on $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$, second acceptance $\alpha_B$ is readable from $(d, b_0, b_2)$ without $\sigma_B$, whereas $\sigma_A$ is required on $(d, b_0, b_2)$ at $b_0 = 0$ and $\sigma_B$ is required for the reversible involution $H_{B,B}^2 = \mathrm{id}$ and for readout on $\Pi_{\mathrm{class}} = (X, W, b)$.
   - Universal rational-carrier claims are certified by exact operator/polynomial coefficient-complete checks in `verify.py` (including all $1426 \times 1426 = 2{,}033{,}476$ polarized bilinear energy entries) and analytical proofs in `PROOF.md`, not inferred from finite wave sampling.
   - The `TWOUSE-COMPARE-v2` comparison mode is separate from ordinary scientific stdout and its digest is withheld from Lane V2 (`#1516`) until both I2 and V2 code pins and first-run records are public.

5. **Failure threshold:**
   - **Zero tolerance (`0`)** on every algebraic, matrix, rational, native-table, inverse, recognizer, energy, and witness assertion.
   - Any mismatch on any frozen test case (`T01`–`T18` or `X01`–`X10`) or regression target records a scoped failure and `STOP` for that claim without altering test cases, costs, source laws, or thresholds.

6. **Action layer:**
   - **Layer L1 (mathematical/symbolic structure and executable conditional apparatus).**
   - Physical status remains `NOT_READY`; native compilation of $L_{\mathrm{buf}}, H_{B,A}, H_{B,B}$ remains `UNSUPPLIED`; Public Canon v101 and open frontier rows remain unchanged.

---

## 2. Frozen test and audit inventory (`verify.py`)

### 2.1 Positive audit and universal certificate suite (`T01`–`T18`)

- `T01_geometry_stencil_and_operators`: Independently construct $B_{\mathrm{st}}$ ($60$ offsets, diagonal $\frac{8}{9}$), $B_{\mathrm{zero}}$ ($61$ sites), $Y + B_{\mathrm{zero}}$ ($142$ sites), $B_{\mathrm{zero}} + B_{\mathrm{zero}}$ ($489$ sites), and $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$ ($705$ lexicographically ordered sites, wave+tape basis dimension $1426$), verify exact byte length (`5029`), SHA-256 (`2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0`), and ordered point equality against `DOMAIN.tsv`, and verify $P^T P = I_4$, $K(I + PP^T) = I_D$, $K J_0 = J_0$, $P^T J_0 = 0$, $P^T S = G_{\mathrm{source}}$, $J_p = P^T H P = \frac{1}{54}(59 I_4 + \mathbf{1}\mathbf{1}^T)$, and $M = P^T H S = \frac{1}{1620}(1770 I_4 - v\mathbf{1}^T)$.
- `T02_generators_and_V_non_invertibility`: Audit all $5$ generators $g_0, \dots, g_4$ across all $5^6 = 15{,}625$ checkpoints $x \in \mathbb{F}_5^6$ (involution $g_k^2(x) = x$ and sum action $(z, -z, 2-z, 2-z, 3-z)\bmod 5$), and verify the $n=0$ collision $g_1(0,0,0,0,0,1) = g_4(2,1,3,4,2,2) = (0,0,0,0,0,4)$ and non-surjectivity onto $n=0$.
- `T03_single_head_625_census_and_recovery`: Audit all $625$ single-head preparations $p \in \mathbb{F}_5^4$ ($125$ per residue sum $h \in \{0..4\}$) through $5$ native ticks $n = 0 \to 5$, verifying $(j_0(h), j_1(h), j_2(h), 1, 1)$, $C_1(h), C_2(h), C_3(h)$, $\operatorname{sum}(x_3) \equiv 1 \pmod 5$, $x_4 = g_1 x_3$, $x_5 = x_3$, and exact recovery $\hat{x}_0 = g_{j_0(h)} g_{j_1(h)} g_{j_2(h)} x_5 = (p, 0, 1)$.
- `T04_paired_factorization_390625`: Verify paired native independence under $V$, apparatus factorization through $(C_1(h(p_A)), C_1(h(p_B)))$, and exhaustive $625 \times 625 = 390{,}625$ paired native-head recovery and selector consistency across all $25$ source-sum fibres.
- `T05_certificate_F_bijectivity_and_energy`: Coefficient-complete universal operator certificate across all $2|D| + 16 = 1426$ basis vectors of $\mathbb{Q}^D \oplus \mathbb{Q}^D \oplus (\mathbb{Q}^4)^4$ verifying that every matrix entry of $F \circ F^{-1} - I$, $F^{-1} \circ F - I$, and the $1426 \times 1426 = 2{,}033{,}476$ polarized symmetric bilinear energy form $\mathcal{B}_Q(X_1, X_2)$ of $E_{\mathrm{full}}(F(X)) - E_{\mathrm{full}}(X)$ is identically zero via the exact sparse column identities $\mathrm{col}_u(E_m) = 0, \mathrm{col}_v(E_m) = 0, \mathrm{col}_a(E_m) = 0$, plus occupied rational state round-trips (including $u = v = 0, A_0 = e_0$).
- `T06_certificate_HB_involutions_and_Lbuf`: Coefficient-complete polynomial identity certificate across all $25$ labels $r \in \mathbb{F}_5^2$ and both $\sigma \in \{-1, +1\}$ verifying $\Delta(u, v + \sigma a(r), -\sigma) + \Delta(u, v, \sigma) \equiv 0$, $H_{B,A}^2 = \mathrm{id}$, $H_{B,B}^2 = \mathrm{id}$, $L_{\mathrm{buf}} \circ L_{\mathrm{buf}}^{-1} = \mathrm{id}$, and two-sided invertibility of the supplied-label apparatus substate transitions $T_{c,B}^{(r_A, r_B)}$ and $S_B^{(r_A, r_B)}$ across all 8 phases and occupied states (explicitly distinguished from the non-invertible full coupled evolution $\mathcal{G}_B$ on $\mathcal{Z}_B$).
- `T07_certificate_bilinear_work_and_mu`: Coefficient-complete extraction of the $4 \times 4$ bilinear work matrix $S^T(T^2 - J_0 - \frac{1}{2}H T)S$ from basis wave evolutions and from $\delta_{y_4}^T(\frac{1}{2}H K H S - S)$ on the 705-site domain $D$, verifying exact equality with $-\frac{1}{10497600}\mathbf{1}\mu^T$ ($\mu = (145483, 173653, 173653, 142153)^T$) and zero dependence on $(c_0, c_1)$.
- `T08_25_pair_work_table_and_capacities`: Execute all $25$ source pairs across capacities $B = b_{\mathrm{init}} \in \{0, \frac{1}{10}, \frac{1}{5}, \frac{2}{5}, \frac{8224427}{10497600}, \frac{4}{5}\}$, verifying the complete 25-row rational table of $(E_A, E_0(z_B), g^T(w_2 - \frac{1}{2}H w_1), \Delta_B, W_{\mathrm{final}})$, sharp maximum $B_* = \frac{8224427}{10497600}$ at $(4,4)$, reserve $\frac{173653}{10497600}$ at $B = \frac{4}{5}$, and exact four-branch counts (`25/0/0/0` at $\frac{4}{5}$ and $B_*$, `13/12/0/0` at $\frac{2}{5}$, `6/9/6/4` at $\frac{1}{5}$, `3/7/6/9` at $\frac{1}{10}$, `1/4/4/16` at $0$).
- `T09_order_witness_14_vs_41`: Direct 7-step wave/tape evolution for $(h_A, h_B) = (1, 4)$ and $(4, 1)$ at blank readiness $B = b_{\mathrm{init}} = \frac{4}{5}$, verifying all initial/intermediate/final boundary states and $W(1,4) - W(4,1) = \frac{10352117}{20995200} - \frac{10323947}{20995200} = \frac{313}{233280}$.
- `T10_certificate_four_cut_operators_and_archives`: Coefficient-complete basis extraction of the linear maps $(z_A, z_B, c_0, c_1) \mapsto (b_0, b_1, b_2, b_3)$ on all 4 acceptance/refusal branches $(\alpha_A, \alpha_B) \in \{0,1\}^2$, verifying $b_0 = \alpha_A R_0 z_A$, $b_1 = \alpha_A R_1 z_A$, $b_2 = \alpha_A D_2 z_A + \alpha_B R_0 z_B$, $b_3 = \alpha_A D_3 z_A + \alpha_B R_1 z_B - \frac{1}{2}J_p c_1$, the 5-row tables of $12960 R_0 z^{(h)}$ and $1399680 R_1 z^{(h)}$, and the `WARM` old-archive trajectories at $c_1 = e_0$ for $(0,0)$ and $(0,1)$.
- `T11_direct_chronological_and_source_readers`: Verify `direct_chronological_cut_reader` at boundaries $c = 0..7$ (`UNWRITTEN` vs `PRESENT(use, cut, vector)` and continued readability of $(b_0, b_1)$ at $c = 4, 5, 6, 7$), verify `direct_source_reader` across all $25$ pairs and multiple non-zero old archives $(c_0, c_1)$, and test its API access restrictions (`inspect.signature` and runtime `TypeError` on `CompositeState`, `ApparatusSubstate`, `WaveTapeState`, and native heads).
- `T12_store_bounds_refusal_and_negative_work`: Verify ready-family lower-bound refusals ($(3,3)$ at $B = \frac{2}{5}$ and $(0,3),(3,0),(3,3)$ at $B = \frac{1}{5}$), occupied-tape warm lower-bound refusal ($A_{\mathrm{init}} = (0, e_0), (h_A, h_B) = (0, 1), B = b_{\mathrm{init}} = \frac{4}{5} \implies \Delta_B^{\mathrm{warm}} = \frac{9}{10}, b - \Delta_B^{\mathrm{warm}} = -\frac{1}{10} < 0$), occupied-tape warm upper-bound refusal with negative work ($A_{\mathrm{init}} = (0, -e_0), (h_A, h_B) = (0, 1), B = b_{\mathrm{init}} = \frac{4}{5} \implies \Delta_B^{\mathrm{warm}} = -\frac{7}{10} < 0, b - \Delta_B^{\mathrm{warm}} = \frac{3}{2} > \frac{4}{5}$), and accepted negative work ($b_{\mathrm{init}} = 0, B = \frac{4}{5} \implies b - \Delta_B^{\mathrm{warm}} = +\frac{7}{10} \in [0, \frac{4}{5}]$).
- `T13_accepted_zero_and_clarification_ii`: At $B = b_{\mathrm{init}} = \frac{1}{5}$ on $\{(0,0), (0,3), (3,0), (3,3)\}$, verify collisions on $\Pi_{\mathrm{class}} = (X, W, b)$ and $\Pi_{\mathrm{class}+d} = (X, W, b, d)$, separation via $(\sigma_A, \sigma_B)_{\mathrm{final}}$, and `Clarification (ii)`: across all ready-family capacities and all $25$ pairs, second acceptance $\alpha_B$ is uniquely readable from $(d, b_0, b_2)$ without $\sigma_B$, whereas $\alpha_A$ is not readable from $(d, b_0, b_2)$ at $b_0 = 0$ and $\sigma_B$ is required for $H_{B,B}^2 = \mathrm{id}$ and to prevent the single-shared-$\sigma$ sign flip on $(0, 1)$.
- `T14_seven_eight_boundary_and_energy_invariants`: Verify across all capacities and old archives that $\mathcal{G}_B^7$ reaches $c = 7, n = 5$, $\mathcal{G}_B^8$ applies $T_7 = \mathrm{id}$ and rotates $c: 7 \mapsto 0$, and $E_{\mathrm{full}}(X) - W = 2(\|c_0\|^2 + \|c_1\|^2)$, $E_{\mathrm{full}}(X) + b = 2(\|c_0\|^2 + \|c_1\|^2) + b_{\mathrm{init}}$, $W + b = b_{\mathrm{init}}$ hold at every step $c = 0..8$ with tape energy counted once.
- `T15_ready_image_left_inverse_all_branches`: Verify `recognize_ready_image` and `recover_prepared_inputs` across all $25$ source fibres in all $4$ acceptance/refusal regimes (at $B = \frac{4}{5}, \frac{2}{5}, \frac{1}{5}, 0$ and with non-zero $(c_0, c_1)$).
- `T16_calibration_prediction_and_clarification_i`: Calibrate the $39$-dimensional parameter $\theta|_{\Pi_2}$ from the $7$ runs in $Z_5 \times Z_5$ (and the $37$-dimensional rank-one subclass from $5$ runs), verify zero-error prediction on all remaining $18$ (or $20$) out-of-sample pairs, and verify `Clarification (i)`: $q_3(z^{(3)}) = \frac{1}{2}$ so $b_2 + q_3(z_A) u$ changes $b_2$ at $h_A = 3$ by $\frac{1}{2}u$ (not $u$).
- `T17_comparator_indistinguishability_and_separations`: Verify exact agreement between $\mathcal{G}_B^7$ and the matched classical comparator $\mathcal{M}_{\mathrm{matched}}^{(2)}$ across all $25$ fibres and $390{,}625$ input pairs, and verify the five explicit separation witnesses against $\mathcal{M}_{\mathrm{single}}, \mathcal{M}_{\mathrm{cold}}, \mathcal{M}_{2\text{-slot}}, \mathcal{M}_{1\sigma}$, and $\mathcal{M}_{\text{no-}\sigma}^{\mathrm{class}} / \mathcal{M}_{\text{no-}\sigma}^{\mathrm{class}+d}$.
- `T18_invalid_endpoint_and_type_rejection_suite`: Execute all $10$ adversarial endpoint and malformed-carrier tests (`X01`–`X10`).

### 2.2 Adversarial invalid-endpoint and malformed-carrier suite (`X01`–`X10`)

- `X01_selector_piston_sum_mismatch`: Fabricated endpoint at $n=5, c=7$ with $x_{5,A} = g_3(1,0,0,0,0,1)$ so $\operatorname{rec}(x_{5,A}) = (1,0) = C_3(0)$ and inverse word $g_1 g_1 g_3 x_{5,A} = (1,0,0,0,0,1)$ has receiver $(0,1)$, but piston sum is $1 \ne 0 = h_A$; must be rejected by `recognize_ready_image` and `recover_prepared_inputs`.
- `X02_invalid_C3_receiver_at_n5`: Endpoint with $\operatorname{rec}(x_{5,A}) \notin \{C_3(0), \dots, C_3(4)\}$ or reconstructed $\operatorname{rec}(\hat{x}_{0,A}) \ne (0,1)$; must be rejected.
- `X03_invalid_clock_n_c_or_k`: Valid $Z(7)$ endpoint perturbed to $n=4, c=7$, or $n=5, c=0$ ($Z(8)$ rollover), or $k=1$; must be rejected.
- `X04_invalid_delayed_label_d`: Valid $Z(7)$ endpoint with $d \ne C_1(h_B)$; must be rejected.
- `X05_invalid_direction_signs_sigma`: Valid $Z(7)$ endpoint with $\sigma_A$ or $\sigma_B$ flipped so reversed initial signs $\ne (+1, +1)$ or reversed guard is inconsistent; must be rejected.
- `X06_invalid_store_b`: Valid $Z(7)$ endpoint with $b$ perturbed inside $[0, B]$ so reversed initial store $b_0 \ne b_{\mathrm{init}}$; must be rejected.
- `X07_invalid_work_W`: Valid $Z(7)$ endpoint with $W$ perturbed so reversed initial work $W_0 \ne 0$; must be rejected.
- `X08_invalid_tapes_A_or_B`: Valid $Z(7)$ endpoint with tape slot $A_0, A_1, B_0$, or $B_1$ perturbed so reversed initial state violates $A_{\mathrm{init}} = (0,0)$, $B_{\mathrm{out,init}} = (c_0, c_1)$, or $(u_0, v_0) = (0,0)$; must be rejected.
- `X09_invalid_wave_u_or_v`: Valid $Z(7)$ endpoint with interior wave coordinate perturbed so reversed $(u_0, v_0) \ne (0,0)$; must be rejected.
- `X10_malformed_input_types_and_carriers`: Passing `bool`, `float`, `str`, wrong tuple lengths (including legacy `869`-entry wave vectors rejected with `expected=705, actual=869`), residues $\notin \{0..4\}$, signs $\notin \{-1, +1\}$, $k \notin \{0, 1\}$, $c \notin \{0..7\}$, $n < 0$, $B < 0$, or $b \notin [0, B]$ to state constructors or transitions, or passing `CompositeState`/native heads to `direct_source_reader`, must raise `TypeError` or `ValueError` with explicit `expected`/`actual` values.

---

## 3. Two-commit pin immutability rule

The nine files `DOMAIN.tsv`, `README.md`, `CONTRACT.md`, `PREREG.md`, `SOURCES.json`, `PROOF.md`, `MIGRATION.md`, `apparatus.py`, and `verify.py` in `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/` are frozen in the preregistration pin commit and must remain byte-for-byte unchanged (`0` diff lines) in the subsequent execution-result commit adding `EXPECTED.txt`, `RUN.md`, `RESULT.md`, `INTERFACE.json`, and `PROMO-C-FUNDED-TWO-USE-EXECUTABLE-2-N.md`.
